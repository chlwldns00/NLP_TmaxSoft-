import konlpy
from konlpy.tag import Okt
import pandas as pd

df=pd.read_csv("JEUS_application-client_final_DB(문단)_0705_new_eng.csv",encoding='utf-8',header=None)
df=df[3]
df=df[:10]  
df_list=df.values.tolist()
f=[]
for txt in df_list:
    txt=txt.replace('\n','')
    f.append(txt)

#f='\n'.join(f)
print(f[0])


t=Okt()
def okt_tokenizer(sents):
#### data slicing(한글질문 위주, 100개만 잘라서 테스트)
    
    #print(len(contents))
    #print(df.head(3))



    #### 형태소 단위로 tokenize
    contents_tokens=[t.morphs(row) for row in sents]
    return contents_tokens

rst=okt_tokenizer(f)
print(rst)
