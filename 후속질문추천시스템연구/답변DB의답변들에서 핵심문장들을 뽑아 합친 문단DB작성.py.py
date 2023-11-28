from textrank import KeysentenceSummarizer
import pandas as pd
from konlpy.tag import Okt
import os 
import openai
openai.api_key = "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"

t=Okt()
df=pd.read_csv("후속질문추천시스템연구/JEUS_application-client_final_DB(문단)_0705_new_eng.csv",encoding='utf-8',header=None)
df=df[3]
df_list=df.values.tolist()
tokenized=[]

def tokenize(df):
    for sentences in df:  #### 전처리및 토크나이징
        
        sentences=str(sentences)
        sentences=sentences.replace('\n','')
        sentences=sentences.replace(',','')
        sentences=sentences.replace('"','')
        sentences=sentences.replace("'",'')
        sentences=sentences.replace('-','')
        sentences=sentences.replace('(','')
        sentences=sentences.replace(')','')
        sentences=sentences.replace('.','')
        #print(sentences)
        contents_tokens=t.morphs(sentences)
        tokenized.append(contents_tokens)
    
    return tokenized



def keyword_extractor_Qanswer(tokenizinedList):
    idx=0 #### gpt로 키워드 뽑는 부분

    answer=str(tokenizinedList[idx]) #토큰화된것중에 타겟질문에 대한 해답을 index로 반환해주는 idx
    context='' #gpt 시스템에서는 context가 존재하지않는거 같다. 혹은 context로 어떤것을 넣어줘야할지는 미정.
    prompt=context+answer+' 다음 문장의 핵심 키워드들을 문맥을 참고하여 중요한 순서대로 dict자료형으로 뽑아줘'
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


def okt_tokenizer(sents):

    #### 형태소 단위로 tokenize
    contents_tokens=t.morphs(sents)
    return contents_tokens #->list



# a=okt_tokenizer(sent)
# print(a)
# textrank사용해서 키워드 추출 ##

##### 여기서 부터 작업1128

summarizer = KeysentenceSummarizer(
    tokenize = tokenize,
    min_sim = 0.3,
    verbose = False
)
## 반복문으로 전구간 순회 
keysents = summarizer.summarize(sent, topk=3)
print(type(keysents))
print(keysents)

### keysents 를 합치는 작업(하나의 문단으로 만듬)



