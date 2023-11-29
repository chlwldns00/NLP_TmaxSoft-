from textrank import KeysentenceSummarizer
import pandas as pd
from konlpy.tag import Okt
import os 
import openai
import csv
openai.api_key = "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"

t=Okt()
df=pd.read_csv("후속질문추천시스템연구/JEUS_application-client_final_DB(문단)_0705_new_eng.csv",encoding='utf-8',header=None)
df=df[3]  ##답변데이터들
df_list=df.values.tolist()
tokenized=[]

def pre_processing(df):
    for sentences in df:  #### 전처리및 토크나이징
        
        sentences=str(sentences)
        sentences=sentences.replace('\n','')
        sentences=sentences.replace(',','')
        sentences=sentences.replace('"','')
        sentences=sentences.replace("'",'')
        sentences=sentences.replace('-','')
        sentences=sentences.replace('(','')
        sentences=sentences.replace(')','')
        #sentences=sentences.replace('.','')
        sentences=sentences.replace('{','')
        sentences=sentences.replace('}','')
        sentences=sentences.replace('`','')
        sentences=sentences.replace('<','')
        sentences=sentences.replace(':','')
        sentences=sentences.replace('>','')
        #print(sentences)
        tokenized.append(sentences)
    
    return tokenized

# def token_to_fullsent(contents_tokens):
#     ttok_sentence_forVectorize=[]

#     for content in contents_tokens:
#         sentence=''
#         for word in content:
#             sentence=sentence+' '+word
        

#         ttok_sentence_forVectorize.append(sentence)
#     return ttok_sentence_forVectorize

t=pre_processing(df)



def okt_tokenizer(sents):

    #### 형태소 단위로 tokenize
    contents_tokens=[t.morphs(sent) for sent in sents]
    return contents_tokens #->list



# a=okt_tokenizer(sent)
# print(a)
# textrank사용해서 키워드 추출 ##

##### 여기서 부터 작업1128

summarizer = KeysentenceSummarizer(
    tokenize = okt_tokenizer,
    min_sim = 0.3,
    verbose = False
)

answerKeyword_list=[]
## 반복문으로 전구간 순회 

    
sent=t[0]
sent=sent.split('.')
print(sent)

keysents = summarizer.summarize(sent, topk=3) 
print(type(keysents))
print(keysents)
for j in range(0,3):
    s=keysents[j][2]+'\n'
answerKeyword_list.append(s)
s=''

# answerKeyword_list.insert('답변핵심문장모음문단',0)
# ## s를 csv에 추가/합침

# csv_filename = "답변핵심문장모음문단.csv"

# with open(csv_filename, mode="w", newline="", encoding="utf-8") as file:
#     writer = csv.writer(file)
    
#     # 리스트 데이터를 CSV 파일에 쓰기
#     writer.writerows(answerKeyword_list)

# ### keysents 를 합치는 작업(하나의 문단으로 만듬)



