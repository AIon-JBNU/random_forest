import pandas as pd
import matplotlib.pyplot as plt

# 실제 CSV 파일 경로와 이름으로 수정
csv_file_path = r"C:\Users\nahcooy\PycharmProjects\pythonProject\random_forest\random_forest_data.csv"

# CSV 파일 읽기
df = pd.read_csv(csv_file_path)

# "corruption_level" 열의 값을 스케일링 (예: 0-10 범위로 조정)
min_value = df['corruption_level'].min()
max_value = df['corruption_level'].max()
df['corruption_level'] = ((df['corruption_level'] - min_value) / (max_value - min_value)) * 10

# 모든 데이터를 하나의 선 그래프로 시각화
plt.plot(df.index, df['MQ-2'], label='MQ-2')
plt.plot(df.index, df['MQ-3'], label='MQ-3')
plt.plot(df.index, df['MQ-136'], label='MQ-136')
plt.plot(df.index, df['MQ-137'], label='MQ-137')
plt.plot(df.index, df['corruption_level'], label='corruption_level')

# 특정 간격(180번째 샘플)마다 빨간색 수직선 추가
for x in range(179, len(df), 180):
    plt.axvline(x, color='red', linestyle='--')

# 그래프 스타일과 레이블 설정
plt.xlabel('180*n')
plt.ylabel('value')
plt.title('total data for random forest')

# 두 번째 y 축 추가
plt.twinx()

# "corruption_level" 그래프 설정
plt.plot(df.index, df['corruption_level'], label='corruption_level', color='purple', linestyle='--')
plt.ylabel('corruption_level')

# 범례 표시
lines, labels = plt.gca().get_legend_handles_labels()
plt.legend(lines, labels)

# 그래프 출력
plt.show()
