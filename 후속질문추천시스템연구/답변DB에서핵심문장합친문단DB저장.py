from textrank import KeysentenceSummarizer
from konlpy.tag import Okt
import pandas as pd
import csv



## answer 전처리(데이터셋읽어오기) ##
df=pd.read_csv("후속질문추천시스템연구/JEUS_application-client_final_DB(문단)_0705_new_eng copy.csv",encoding='utf-8',header=None)
df=df[3]
df_list=df.values.tolist()
df_answer_list=[]
for txt in df_list:
    txt=txt.replace('\n','')
    txt=txt.replace(',','')
    txt=txt.replace('"','')
    txt=txt.replace("'",'')
    txt=txt.replace('-','')
    txt=txt.replace('(','')
    txt=txt.replace(')','')
    txt=txt.replace('{','')
    txt=txt.replace('}','')
    txt=txt.replace('`','')
    txt=txt.replace('<','')
    txt=txt.replace(':','')
    txt=txt.replace('>','')
                    
    df_answer_list.append(txt)

print('전처리 완료 \n------------------------------------------')

#### 형태소 분석기 함수화 ####
t=Okt()


def okt_tokenizer(sents):

    contents_tokens=t.morphs(sents)
    return contents_tokens #->list


# textrank사용해서 키워드 추출 ##


summarizer = KeysentenceSummarizer(
    tokenize = okt_tokenizer,
    min_sim = 0.3,
    verbose = False
)


## 반복문으로 전구간 순회하여 답변DB의 핵심문장모음문단 만들기(keyword뽑기용)
answerKeyword_list=[]
s=''
for i in range(len(df_answer_list)):

    sent=df_answer_list[i]
    sent=sent.split('.')
    #print(sent)
    if len(sent)<=4:                 #error수정사항#  
                                    #에러내용=>summarizer함수에서 리스트내 문장중 topk만큼의 핵심문장을 비교 / 선택 하는데 답변이 3문장이 안되는 답변리스트 요소가 exception코드에 걸린거같다.
        for k in range(len(sent)): #답변이 너무짧아 핵심문장을 못뽑는경우는 그냥 전부를 문장단위로 자른뒤 토크나이징및 전처리만 함
            s=sent[k]+'\n'
        print(i,'*')
        answerKeyword_list.append(s)
        s=''
    
    else:
        keysents = summarizer.summarize(sent, topk=3)   
        # print(type(keysents))
        # print(keysents)
        print(i)
        for j in range(len(keysents)):
            s=s+keysents[j][2]+'\n'

        answerKeyword_list.append(s)
        s=''

print(answerKeyword_list[0])

## 기존 [메뉴얼,질문,답변] DB에 답변의 핵심문장문단 추가 코드 ##

# 기존 CSV 파일 경로
csv_filename = "후속질문추천시스템연구/JEUS_application-client_final_DB(문단)_0705_new_eng copy.csv"

# CSV 파일 열기 (기존 데이터를 읽어오기 위해)
with open(csv_filename, mode="r", newline="", encoding="utf-8") as file:
    reader = csv.reader(file)
    
    # 기존 데이터 읽어오기
    existing_data = list(reader)

# 새로운 데이터를 열로 추가
for i, item in enumerate(answerKeyword_list):
    # 각 행에 해당 열의 데이터 추가
    existing_data[i].append(item)

# CSV 파일 열기 (추가된 데이터를 쓰기 위해)
with open(csv_filename, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    
    # 추가된 데이터를 CSV 파일에 쓰기
    writer.writerows(existing_data)

print(f"{csv_filename} 파일에 새로운 행이 추가되었습니다.")

