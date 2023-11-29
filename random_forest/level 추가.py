import pandas as pd

# CSV 파일 경로
csv_file_path = r"C:\Users\nahcooy\PycharmProjects\pythonProject\random_forest\mandarin\mandarin_1129-1.csv"

# CSV 파일 읽기
df = pd.read_csv(csv_file_path)

# "corruption_level" 열 추가하고 값 설정
corruption_level_value = 3  # 원하는 레벨 값을 설정하세요
df['corruption_level'] = corruption_level_value

# 결과를 다시 CSV 파일로 저장
df.to_csv(csv_file_path, index=False)