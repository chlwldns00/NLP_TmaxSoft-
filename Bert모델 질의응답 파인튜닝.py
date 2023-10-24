import torch
from transformers import BertForQuestionAnswering, BertTokenizer
#bert모델 학습에 쓰이는 데이터셋 -> squad
model = BertForQuestionAnswering.from_pretrained('bert-large-uncased-whole-word-masking-finetuned-squad')
tokenizer = BertTokenizer.from_pretrained('bert-large-uncased-whole-word-masking-finetuned-squad')

#Bert의 입력정의
question = "What is the immune system?"
paragraph = "The immune system is a system of many biological structures and processes within an organism that protects against disease. To function properly, an immune system must detect a wide variety of agents, known as pathogens, from viruses to parasitic worms, and distinguish them from the organism's own healthy tissue."

#토큰설정
question = '[CLS] ' + question + '[SEP]'
paragraph = paragraph + '[SEP]'

#토큰으로 나누기
question_tokens = tokenizer.tokenize(question)
paragraph_tokens = tokenizer.tokenize(paragraph)

#질문과 단락의 토큰을 일단 합친뒤, 모델에 입력하기 위해 인코딩
tokens = question_tokens + paragraph_tokens 
input_ids = tokenizer.convert_tokens_to_ids(tokens)

#질문과 단락을 구분하는 세그먼트 id값 추가 0:질문 , 1s:단락
segment_ids = [0] * len(question_tokens)
segment_ids += [1] * len(paragraph_tokens)


#인코딩 값과 세그먼트 id값을 텐서로 변환
input_ids = torch.tensor([input_ids])
segment_ids = torch.tensor([segment_ids])

#인코딩된값의 토큰 하나하나를 돌면서 이 토큰이 답변의 시작지점일 확률, 끝지점일 확률을 각각 계산하여 확률값의 텐서를 반환한다.
scores = model(input_ids, token_type_ids = segment_ids)
print(scores)

#argmax함수로 시작지점의 확률중 가장 큰값, 끝지점의 확률중 가장 큰값의 인덱스를 반환해온다.
start_index = torch.argmax(scores.start_logits)
end_index = torch.argmax(scores.end_logits)

#슬라이싱 값을 하나의 문자열로 join
print(' '.join(tokens[start_index:end_index+1]))
