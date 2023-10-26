import os 
import openai
from konlpy.tag import Okt
import re
import pandas as pd
openai.api_key = "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"



df=pd.read_csv("JEUS_application-client_final_DB(문단)_0705_new_eng.csv",encoding='utf-8',header=None)
df=df[3] #답변데이터 추출
df=df[:10]  
df=df.values.tolist()
tokenized=[]
t = Okt()

#print(df[0])
for sentences in df:  #전처리및 토크나이징
    #sentences = sentences.replace(". ",".")
    #sentences = re.sub(r'([^\n\s\.\?!]+[^\n\.\?!]*[\.\?!])', r'\1\n', sentences)
    sentences=sentences.replace('\n','')
    #txt=txt.replace('.','')
    sentences=sentences.replace(',','')
    sentences=sentences.replace('"','')
    sentences=sentences.replace("'",'')
    sentences=sentences.replace('-','')
    sentences=sentences.replace('(','')
    sentences=sentences.replace(')','')

    #print(sentences)
    contents_tokens=t.morphs(sentences)
    tokenized.append(contents_tokens)

tok_sentence_forVectorize=[]

for content in tokenized:
    sentence=''
    for word in content:
        sentence=sentence+' '+word
    

    tok_sentence_forVectorize.append(sentence)
print(tok_sentence_forVectorize[0])