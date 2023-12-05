import csv

# 저장할 딕셔너리 데이터
keywords = {
    "JEUS": None,
    "클라이언트 컨테이너": None,
    "Jakarta EE 환경": None,
    "standalone 클라이언트": None,
    "Jakarta EE 스펙": None,
    "애플리케이션 클라이언트 컨테이너": None,
    "Naming Service": None,
    "Scheduler": None,
    "Security": None,
    "JEUS 서비스": None,
    "JEUS 클라이언트 라이브러리": None,
    "JNDI": None,
    "Dependency Injection": None,
    "JEUS Scheduler": None
}

csv_filename = "user_data_dict.csv"

# CSV 파일 열기 (기존 데이터를 읽어오기 위해)
with open(csv_filename, mode="r", newline="", encoding="utf-8") as file:
    reader = csv.reader(file)
    
    # 기존 데이터 읽어오기
    existing_data = list(reader)

# 새로운 데이터를 열로 추가
for i, item in enumerate(keywords):
    # 각 행에 해당 열의 데이터 추가
    existing_data[i].append(item)

# CSV 파일 열기 (추가된 데이터를 쓰기 위해)
with open(csv_filename, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    
    # 추가된 데이터를 CSV 파일에 쓰기
    writer.writerows(existing_data)

print(f"{csv_filename} 파일에 새로운 행이 추가되었습니다.")

