# string_A = "클라이언트 컨테이너"
# string_B = "클라이언트"

# if string_B.lower() in string_A.lower():
#     print("string_B는 string_A에 포함됩니다.")
# else:
#     print("string_B는 string_A에 포함되지 않습니다.")
from gensim.models.word2vec import Word2Vec
from gensim.models import word2vec
def define_recomm_keyword(key_ans,key_qes,model):
    
    key_ans_list=[]
    final=[]
    
    for i in range(len(key_qes)):
        for j in range(len(key_ans)-1,-1,-1):
            if key_qes[i][0] in key_ans[j][0]:
                del key_ans[j] # **error index out of range에러 =>> 해결
    
    #2차 겹치는거 제거후 질문과 가장 유사도가 작은 키워드 추출 하위 3개(word2vec활용해서)10/27 10/30~
    
    for i in range(len(key_qes)):
        for j in range(len(key_ans)):
            key_ans_list.append(model.wv.similarity(key_qes[i][0],key_ans[j][0]))#여기서 판별함수를 어떤걸 사용할지
    # **
    indexed_list = list(enumerate(key_ans_list))
    sorted_list = sorted(indexed_list, key=lambda x: x[1], reverse=True)
    sorted_list = sorted_list[-3:]
    finall = [item[0]%(len(key_ans)) for item in sorted_list]
    final=[key_ans[i][0] for i in finall]
        

    return final

model=word2vec.Word2Vec.load("reccmodel")
vocab = model.wv.vocab
sorted(vocab, key=vocab.get, reverse=True)[:30]
dict1={
   "애플리케이션 클라이언트": "JEUS 서버와 별도의 JVM에서 수행되는 standalone 클라이언트",
   "JEUS": "클라이언트 컨테이너를 사용하여 Jakarta EE 환경에서 애플리케이션 호출 및 서비스 제공",
   "클라이언트 컨테이너": "Naming Service, Scheduler, Security 등의 JEUS 서비스 사용",
   "JEUS 클라이언트 라이브러리": "JNDI, Security 등의 서비스 사용 가능하지만 Dependency Injection, JEUS Scheduler 등의 서비스는 사용 불가",
   "Jakarta EE 스펙": "더 자세한 내용 확인 가능",
   "JEUS XML 스키마": "jeusclientdd.xml로 참고 가능"
}
dict2={ 
    "JEUS": None,
    "클라이언트 라이브러리": None,
    "서비스": None,
    "이용": None
}
dict1=list(dict1.items())
dict2=list(dict2.items())
# a=len(dict1)
# for i in range(len(dict2)):
#     for j in range(len(dict1)-1,-1,-1):
#         if dict2[i][0] in dict1[j][0]:
#             print('delete1')
#             print(j)
#             del dict1[j] # **error
#             print(dict1)
#print(define_recomm_keyword(dict1,dict2,model))

# l=[1,2,3,4,5,6,7,8,9]
# b=l[-3:]
# print(b)