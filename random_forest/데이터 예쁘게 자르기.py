import os
import csv

# 입력 TXT 파일들이 있는 디렉토리 경로
input_directory = r"C:\Users\nahcooy\PycharmProjects\pythonProject\random_forest\banana"

# 입력 디렉토리 내의 모든 TXT 파일을 순회
for filename in os.listdir(input_directory):
    if filename.endswith('.txt'):
        # 입력 파일 경로
        input_file_path = os.path.join(input_directory, filename)

        # 출력 파일 경로 (확장자를 .csv로 변경)
        output_file_path = os.path.join(input_directory, filename.replace('.txt', '.csv'))

        # CSV 파일로 저장할 열 번호 (0부터 시작)
        columns_to_extract = [1, 2, 3, 4]

        # 텍스트 파일 읽기
        with open(input_file_path, 'r') as txt_file:
            lines = txt_file.readlines()

        # 숫자 데이터 추출
        data = []
        for line in lines:
            try:
                # 쉼표로 데이터 분리
                parts = line.strip().split(',')
                # 필요한 열만 선택하여 실수로 변환
                selected_data = [float(parts[i]) for i in columns_to_extract]
                data.append(selected_data)
            except:
                print(f"잘못된 데이터 라인: {line}")

        # CSV 파일로 저장
        with open(output_file_path, 'w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            # 열 이름 추가
            csv_writer.writerow(['MQ-2', 'MQ-3', 'MQ-136', 'MQ-137'])
            # 데이터 쓰기
            csv_writer.writerows(data)

        print(f"데이터가 {output_file_path}로 저장되었습니다.")
