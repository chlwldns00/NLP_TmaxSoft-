# NLP를 활용한 QA챗봇 연구 목표
## - NLP 공부/embedding공부   
## - 다양한 언어모델들의 임베딩/fine-tunning 과정공부
## - 학습된 DB를 참조하지 않고, 허구 세계에서의 지식을 가져오는 hallucination 을 최소화하는 연구  
----------  
# 챗봇AI알고리즘학습에 데이터로 넣을 데이터 전처리    
## - 자사 시스템관련 질문 답변 DB를 csv파일로 변환 및 전처리    
## - 한글 질문/답변 들은 영어로, 영어 질문들은 한글로 변환    
## - 임베딩하기 쉽게 질문/답변 데이터 전처리(띄어쓰기 구분, 특수문자 제거등)    
## - 자사 개발 인코더로 질문/답변 데이터들을 임베딩 한뒤, 한개의 데이터셋(csv)로 합치고, 학습용 셋과 테스트 용 셋으로 split   
------------------  
# 후속질문 추천 알고리즘 프로젝트 연구
## - 자체 제작 알고리즘 구상
## - 자연어 질문 임베딩후 유사도 측정 및 추천 필터링  
## - textRank 알고리즘 이용한 문서/문장에서 키워드 summarize  
## - word2vec모델을 학습시킨후 단어:단어 유사도 비교해서 핵심키워드 추출 
## - 질문이 잘못된 형식으로 input 되었을때, 질답DB에 있는 질문 형식의 새로운 질문 추천하는 알고리즘 추가 제작 
## - 자세한 설명 -- 학사논문 - 연구내용2 참조
-----------------  
## 사용해본 pre-trained 모델
1. [bert-base-uncased](https://huggingface.co/bert-base-uncased), kobert
2. [vicuna](https://huggingface.co/lmsys/vicuna-13b-v1.5-16k), [Korani](https://huggingface.co/KRAFTON/KORani-v3-13B)
3. Use(Universal Sentence Encoder)[https://huggingface.co/vprelovac/universal-sentence-encoder-4]  
-------------------
# 학사논문 작성 
## - 연구내용 1 - hallucination 방지 
## - 연구내용 2 - 사용자 지식수준을 고려한 후속질문 추천시스템
