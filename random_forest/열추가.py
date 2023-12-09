import os
import csv
import pandas as pd
# 입력 파일 경로
input_file_path = r"C:\Users\nahcooy\PycharmProjects\pythonProject\random_forest\banana\11.29.csv"

# CSV 파일을 데이터프레임으로 읽기
df = pd.read_csv(input_file_path)

# 'corruption_level' 열 추가 및 값 1 할당
df['corruption_level'] = 3

# 수정된 데이터프레임을 새로운 CSV 파일로 저장
output_file_path = input_file_path

df.to_csv(output_file_path, index=False)

print(f"'corruption_level' 열이 {output_file_path}에 추가되었습니다.")
