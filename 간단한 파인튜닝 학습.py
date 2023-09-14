import torch
from transformers import BertTokenizer, BertForSequenceClassification, AdamW
from torch.utils.data import DataLoader, TensorDataset

# 미리 학습된 BERT 모델 및 토크나이저 로드
model_name = "bert-base-uncased"
tokenizer = BertTokenizer.from_pretrained(model_name)
model = BertForSequenceClassification.from_pretrained(model_name, num_labels=2)  # 이 예시에서는 이진 분류

# 파인튜닝을 위한 데이터 로드 및 전처리
# 예시 데이터: 간단한 이진 분류 작업을 위한 데이터
texts = ["I love this product.", "This product is terrible."]
labels = [1, 0]  # 긍정(1) 또는 부정(0) 클래스

# 토큰화 및 패딩
input_ids = []
attention_masks = []
for text in texts:
    encoded_dict = tokenizer.encode_plus(
        text,
        add_special_tokens=True,
        max_length=64,
        padding="max_length",
        return_attention_mask=True,
        return_tensors="pt"
    )
    input_ids.append(encoded_dict["input_ids"])
    attention_masks.append(encoded_dict["attention_mask"])

input_ids = torch.cat(input_ids, dim=0)
attention_masks = torch.cat(attention_masks, dim=0)
labels = torch.tensor(labels)

# 데이터 로더 생성
batch_size = 2
dataset = TensorDataset(input_ids, attention_masks, labels)
dataloader = DataLoader(dataset, batch_size=batch_size, shuffle=True)

# Optimizer 및 학습 설정
optimizer = AdamW(model.parameters(), lr=1e-5)

# 파인튜닝 학습
num_epochs = 3
for epoch in range(num_epochs):
    model.train()
    total_loss = 0.0
    for batch in dataloader:
        input_ids, attention_mask, labels = batch
        optimizer.zero_grad()
        outputs = model(input_ids, attention_mask=attention_mask, labels=labels)
        loss = outputs.loss
        loss.backward()
        optimizer.step()
        total_loss += loss.item()
    average_loss = total_loss / len(dataloader)
    print(f"Epoch {epoch+1} - Average Loss: {average_loss:.4f}")

# 파인튜닝된 모델을 저장하거나 추론에 사용할 수 있습니다.
# 예시에서는 학습만 수행한 예시입니다.
