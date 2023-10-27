from transformers import BertModel, BertTokenizer
import torch

#bertModel 다운로드
model = BertModel.from_pretrained('bert-base-uncased') #입력 단어를 소문자로 만들어준다. 어떠한 accent Mark들도 삭제해서 보여준다

#위 모델을 사전학습시키는데 사용된 토크나이저를 다운로드
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')

#입력전처리
sentence = 'i love paris'

#토큰화
token=tokenizer.tokenize(sentence)
print(token)

#토큰추가
token=['[CLS]'] + token + ['[SEP]']
print(token)

#만약 토큰길이를 7로 설정하였다면

token = token + ['[PAD]'] + ['[PAD]']
print(token)

#토큰이 생성되었으니 Attention Mask() 로 실제 문자값과 패딩값을 구분하게 만들기

attention_mask = [1 if i!='[PAD]' else 0 for i in token]
print(attention_mask)

#각각의 모든 토큰들을 토큰ID로 변환한다/토큰ID를 토큰으로 변환할수도있다.

token_ids = tokenizer.convert_tokens_to_ids(token)
print(token_ids)

#임베딩 추출에 사용될 token_id 와 Attention_Mask를 텐서로 변환(레이어에 집어넣어야 하므로)
token_ids = torch.tensor(token_ids).unsqueeze(0)
attention_mask = torch.tensor(attention_mask).unsqueeze(0)

#위 요소들을 모델에 입력하고 임베딩을 얻는다(문맥화된 단어 임베딩)
model_input=tokenizer(sentence+'[PAD]'+ '[PAD]', return_tensors="pt")
outputs= model(**model_input)
#print(model)

#모델이 출력한 값들
print(outputs.keys())

#12계층중 마지막 layer의 차원값
print(outputs.last_hidden_state.shape)
print(outputs.last_hidden_state) # 최종 임베딩값?
