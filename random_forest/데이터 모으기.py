import os
import pandas as pd

# 입력 CSV 파일들이 있는 디렉토리 경로
input_directory = r"C:\Users\nahcooy\PycharmProjects\pythonProject\random_forest\mandarin"

# 결과 CSV 파일 경로
output_file = ('random_forest_data.csv')

# CSV 파일 목록을 저장할 리스트 생성
csv_files = []

# 입력 디렉토리 내의 모든 CSV 파일을 순회
for filename in os.listdir(input_directory):
    if filename.endswith('.csv'):
        file_path = os.path.join(input_directory, filename)
        csv_files.append(file_path)

# 파일명을 가지고 정렬
csv_files.sort()

# 결과를 저장할 빈 DataFrame 생성
result_df = pd.DataFrame()

# 정렬된 CSV 파일들을 읽어서 데이터 합치기
for file_path in csv_files:
    print(file_path)
    df = pd.read_csv(file_path, skiprows=[1])  # 첫 번째 행을 건너뜁니다.
    result_df = pd.concat([result_df, df])

# 결과를 하나의 CSV 파일로 저장
result_df.to_csv(output_file, index=False)
