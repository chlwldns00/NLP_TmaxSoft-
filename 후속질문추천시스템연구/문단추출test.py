from textrank import KeywordSummarizer
import konlpy
from konlpy.tag import Okt
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
import scipy as sp

import pandas as pd


## answer 전처리 ##
df=pd.read_csv("후속질문추천시스템연구/JEUS_application-client_final_DB(문단)_0705_new_eng.csv",encoding='utf-8',header=None)
df=df[3]
#df=df[:10]  
df_list=df.values.tolist()
f=[]
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
                    
    f.append(txt)
#f='\n'.join(f)
# sent=f[0]
# #print(sent)
# sent=sent.split('.')
# print(sent)
# print(type(sent))
print('\n------------------------------------------')
#### 형태소 분석기 함수화 ####
t=Okt()


def okt_tokenizer(sents):

    #### 형태소 단위로 tokenize
    contents_tokens=t.morphs(sents)
    return contents_tokens #->list



# a=okt_tokenizer(sent)
# print(a)
# textrank사용해서 키워드 추출 ##
from textrank import KeysentenceSummarizer

summarizer = KeysentenceSummarizer(
    tokenize = okt_tokenizer,
    min_sim = 0.3,
    verbose = False
)
#print(sent)
answerKeyword_list=[]

sent=f[404]
sent=sent.split('.')
keysents = summarizer.summarize(sent, topk=3)   
        # print(type(keysents))
        # print(keysents)

for j in range(len(keysents)):
    s=keysents[j][2]+'\n'
    print(s)
answerKeyword_list.append(s)
s=''
print(answerKeyword_list[0])