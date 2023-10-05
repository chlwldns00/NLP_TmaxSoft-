import konlpy
from konlpy.tag import Okt
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
import csv

#벡터 방법 tf-idf
vectorizer = TfidfVectorizer(min_df=1, decode_error='ignore')
t=Okt() #형태소 분석기

#data slicing
df=pd.read_csv("kor_pair_train.csv",encoding='utf-8')
df=df['question1']
df=df[:100]
contents=df.values.tolist()
print(len(contents))


#tokenize
contents_tokens=[t.morphs(row) for row in contents]
print(contents_tokens[1])

#