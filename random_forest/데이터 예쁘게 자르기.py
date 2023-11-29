import csv

# 텍스트 파일 경로

input_file = r"C:\Users\nahcooy\PycharmProjects\pythonProject\data\11.21 2차 측정\11.21 귤 2차측정수정.txt"
# CSV 파일 경로
output_file = "mandarin/mandarin_1121-2.csv"

# CSV 파일로 저장할 열 번호 (0부터 시작)
columns_to_extract = [1, 2, 3, 4]

# 텍스트 파일 읽기
with open(input_file, 'r') as txt_file:
    lines = txt_file.readlines()

# 숫자 데이터 추출
data = []
for line in lines:
    try:
        # 쉼표로 데이터 분리
        parts = line.strip().split(',')
        # 필요한 열만 선택
        selected_data = [float(parts[i]) for i in columns_to_extract]
        data.append(selected_data)
    except:
        print(line)

# CSV 파일로 저장
with open(output_file, 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    # 열 이름 추가
    csv_writer.writerow(['MQ-2', 'MQ-3', 'MQ-136', 'MQ-137'])
    # 데이터 쓰기
    csv_writer.writerows(data)

print(f"데이터가 {output_file}로 저장되었습니다.")
