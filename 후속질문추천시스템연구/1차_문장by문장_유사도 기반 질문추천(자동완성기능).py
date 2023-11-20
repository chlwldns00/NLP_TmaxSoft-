import konlpy
from konlpy.tag import Okt
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
import scipy as sp
import numpy as np
from scipy.sparse import csr_matrix
from scipy.spatial.distance import cosine
##### 벡터화 하는 방법 == tf-idf 방법 // 유사도 score 유클리디언 거리 &  ######v


#### 형태소 분석기
t=Okt()

#### data slicing(한글질문 위주, 100개만 잘라서 테스트)
df=pd.read_csv("후속질문추천시스템연구/JEUS_application-client_final_DB(문단)_0705_new_eng.csv",encoding='utf-8',header=None)
df=df[2]
df=df[:680]  
contents=df.values.tolist()
#print(len(contents))
#print(df.head(3))
target_q_input=input("타겟질문입력: ")
contents.append(target_q_input)


#### 형태소 단위로 tokenize
contents_tokens=[t.morphs(row) for row in contents]
print('토큰나이징\n', contents_tokens[-1])



#### 형태소로 나눈 토큰을 띄어쓰기로 구분후 한문장으로 붙이기
def token_to_fullsent(contents_tokens):
    ttok_sentence_forVectorize=[]

    for content in contents_tokens:
        sentence=''
        for word in content:
            sentence=sentence+' '+word
        

        ttok_sentence_forVectorize.append(sentence)
    return ttok_sentence_forVectorize


tok_sentence_forVectorize=token_to_fullsent(contents_tokens)
print(tok_sentence_forVectorize[-1])
#### 타겟 문장 설정하고, 현재 질문 DB에 동일한 질문이 있을시 질문DB에서 해당 질문을 삭제한다.
#target_q=tok_sentence_forVectorize[8]


# target_q=t.morphs(target_q_input)   
# for content in target_q:
#         sentence=''
#         for word in content:
#             sentence=sentence+' '+word
        
# print(sentence)
# tok_sentence_forVectorize.append(sentence)  
#           ### 벡터화가 안되는 이슈가 있으므로, 원래 벡터화 할 list에 새로추가된 타겟 질문 토크나이징+문장을 추가해준다.
# print("타겟 문장:\n", target_q)
# print("\n\n------------------")
# #print('원래문장\n',df[0:1],'\n형태소토큰단위로 쪼개진 문장\n', tok_sentence_forVectorize[0])


#### tf-idf vectorize
vectorizer = TfidfVectorizer(min_df=1, decode_error='ignore')
vec=vectorizer.fit_transform(tok_sentence_forVectorize)
num_samples, num_features =vec.shape
print(num_samples, num_features)





#### 타겟질문 임베딩 ###
target_q=[tok_sentence_forVectorize[-1]] #임베딩하기위해 리스트 변환(임의 DB에서 가져오는 코드)

target_q_vec =vectorizer.transform(target_q)

#테스트 케이스
print("타겟 질문의 임베딩 결과: \n", target_q_vec)
print(type(target_q_vec))
print('\n\n\n\n---------------------------------------')




####  단순 벡터 내적 거리계산 함수 정의(유클리디언 거리)
def dist_raw_eculidian(v1,v2):
    delta = v1 - v2
    return sp.linalg.norm(delta.toarray())




#### 코사인 유사도로 score계산하는 경우
def dist_cosine_similarity(v1, v2):
    # Ensure that both input matrices are in Compressed Sparse Row (CSR) format
    if not isinstance(v1, csr_matrix) or not isinstance(v2, csr_matrix):
        raise ValueError("Input matrices must be in CSR format")
    
    dense_matrix1 = v1.toarray().ravel() if hasattr(v1, 'toarray') else v1
    dense_matrix2 = v2.toarray().ravel() if hasattr(v2, 'toarray') else v2

    # Convert the sparse matrices to dense arrays
    dense_matrix1 = dense_matrix1.toarray().ravel() if hasattr(dense_matrix1, 'toarray') else dense_matrix1
    dense_matrix2 = dense_matrix2.toarray().ravel() if hasattr(dense_matrix2, 'toarray') else dense_matrix2

    # Compute the cosine similarity between the dense arrays
    similarity = abs(cosine(dense_matrix1, dense_matrix2))

    return similarity


#### 최적의 유사도를 가진 질문을 찾아보자[일단 best score1개만] (한글형태소 기반 토크나이징, tf-idf 벡터화(임베딩), norm메소드를 이용한 벡터거리 계산 이용)
best_q=None
best_dist=65535
best_i=[]
dis_list=[]

for i in range(0,num_samples):
    if i != num_samples-1: #제거한 문장 제외
        post_vec=vec.getrow(i)
        #print(type(post_vec))

        dis=dist_raw_eculidian(post_vec, target_q_vec)
        print("==Post %i with dist=%.3f : %s" % (i,dis,contents[i]))

        if dis < best_dist:
            best_dist=dis
            best_i.append(i)


print('\n\n\n\n----------------------------------------------------------')
print('타겟질문:',tok_sentence_forVectorize[-1])
print("Best recommendation question is %i -> %s, dist = %.3f" % (best_i[-1],contents[best_i[-1]],best_dist))
print("Best recommendation question is %i -> %s, dist = %.3f" % (best_i[-2],contents[best_i[-2]],best_dist))
print("Best recommendation question is %i -> %s, dist = %.3f" % (best_i[-3],contents[best_i[-3]],best_dist))
#best_i 리스트에서 최상위 n개의 score를 가진 관련질문을 뽑을 수 있다.




####### 2.코사인 유사도로 구하기 ######

