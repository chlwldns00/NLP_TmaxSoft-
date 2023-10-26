
import pandas as pd
from gensim.models.word2vec import Word2Vec
from gensim.models import word2vec
import nltk
import gensim
import gensim.models as g
from konlpy.tag import Okt








t=Okt()

tokenized=[]
def tokenize(df):
    for sentences in df:  #### 전처리및 토크나이징
        
        sentences=sentences.replace('\n','')
        sentences=sentences.replace(',','')
        sentences=sentences.replace('"','')
        sentences=sentences.replace("'",'')
        sentences=sentences.replace('-','')
        sentences=sentences.replace('(','')
        sentences=sentences.replace(')','')

        #print(sentences)
        contents_tokens=t.morphs(sentences)
        tokenized.append(contents_tokens)
    
    return tokenized

df=pd.read_csv("JEUS_application-client_final_DB(문단)_0705_new_eng.csv",encoding='utf-8',header=None)
df_q=df[2]
df_q=df_q[:1000]
df_a=df[3] #답변데이터 추출
df_a=df_a[:1000]  
df_q=df.values.tolist() #리스트로 시작(매개변수)
df_a=df.values.tolist()
df_a=tokenize(df_a)
df_q=tokenize(df_q)
tokens=df_a+df_q
model=word2vec.Word2Vec(tokens,min_count=1)
print(model.wv.similarity('애플리케이션','JEUS'))

