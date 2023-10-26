import os 
import openai
from konlpy.tag import Okt
import re
import pandas as pd
openai.api_key = "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"



df=pd.read_csv("JEUS_application-client_final_DB(문단)_0705_new_eng.csv",encoding='utf-8',header=None)
df_q=df[2]
df_q=df_q[:10]
df_a=df[3] #답변데이터 추출
df_a=df_a[:10]  
df_q=df.values.tolist()
df_a=df.values.tolist()

t = Okt()

#print(df[0])
def tokenize(df):
    for sentences in df:  #### 전처리및 토크나이징 후 다시붙이기
        tokenized=[]
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

    tok_sentence_forVectorize=[]

    for content in tokenized:
        sentence=''
        for word in content:
            sentence=sentence+' '+word
        

        tok_sentence_forVectorize.append(sentence)

    return tok_sentence_forVectorize
# print(tok_sentence_forVectorize[0])


########
    
###타겟질문의 상위3개 문맥을 고려한 키워드와, 타겟질문의 답변의 문맥을 고려한 상위 3개 키워드를 비교하여 동일하게 일치되지 않은 키워드를 추천중요 키워드로 선정한다

def keyword_extractor(tokenizinedList):
    idx=0 #### gpt로 키워드 뽑는 부분

    answer=tokenizinedList[idx] #토큰화된것중에 타겟질문에 대한 해답을 index로 반환해주는 idx
    context=str(df[1][idx]) #gpt 시스템에서는 context가 존재하지않는거 같다. 혹은 context로 어떤것을 넣어줘야할지는 미정.
    prompt=context+'\n 위 문맥을 참고해서\n'+answer+' 다음 문장의 핵심 키워드들을 중요한 순서대로 dict자료형으로 뽑아줘'
    completion = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role":"user","content":prompt}
        ]
    )


    keyword_dict=completion.choices[0].message.content
    # print(type(keyword_dict))
    keyword_dict=eval(keyword_dict) #str->dict type difference

    print(completion.choices[0].message.content)
    return keyword_dict

##### first main
df_a=tokenize(df_a)
df_q=tokenize(df_q)
key_ans=keyword_extractor(df_a)
key_qes=keyword_extractor(df_q)


####### 10/26~ 키워드 비교 작업후 추천키워드에 핵심이 될 키워드 선정() ######
def define_recomm_keyword(key_ans,key_qes):
    for 




