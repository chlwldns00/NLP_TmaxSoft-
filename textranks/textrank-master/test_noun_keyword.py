from krwordrank.word import summarize_with_keywords
import konlpy
from konlpy.tag import Okt
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
import scipy as sp
import re
import pandas as pd


## answer 전처리 ##
df=pd.read_csv("JEUS_application-client_final_DB(문단)_0705_new_eng.csv",encoding='utf-8',header=None)
df=df[3]
df=df[:10]  
df=df.values.tolist()
df=df[0]
df=''.join(df)
print(df)
def split_noun_sentences(text):
    okt = Okt()
    sentences = text.replace(". ",".")
    sentences = re.sub(r'([^\n\s\.\?!]+[^\n\.\?!]*[\.\?!])', r'\1\n', sentences).strip().split("\n")
    
    result = []
    for sentence in sentences:
        if len(sentence) == 0:
            continue
        sentence_pos = okt.pos(sentence, stem=True)
        nouns = [word for word, pos in sentence_pos if pos == 'Noun']
        if len(nouns) == 1:
            continue
        result.append(' '.join(nouns) + '.')
        
    return result

sent=split_noun_sentences(df)
print(sent)

from krwordrank.word import KRWordRank

min_count = 1   # 단어의 최소 출현 빈도수 (그래프 생성 시)
max_length = 10 # 단어의 최대 길이
wordrank_extractor = KRWordRank(min_count=min_count, max_length=max_length)
beta = 0.85    # PageRank의 decaying factor beta
max_iter = 20

keywords, rank, graph = wordrank_extractor.extract(sent, beta, max_iter)
for word, r in sorted(keywords.items(), key=lambda x:x[1], reverse=True):
        print('%8s:\t%.4f' % (word, r))
