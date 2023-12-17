import requests
import json
import joblib
import pandas as pd

f_list = ['바나나', '귤', '감', '사과']

def post(f_name, prediction):

    if prediction == 1:
        message = "1단계, 부패하지 않음"
    elif prediction == 2:
        message = "2단계, 부패 진행 중"
    else:
        message = "3단계, 부패 진행 완료"
    # POST (JSON)
    headers = {'Content-Type': 'application/json; chearset=utf-8'}
    data = {'title': f'{f_name}', 'body': message, 'targetToken': 'fftX9XPPRtCqsP150KOvMF:APA91bF99JLuNP0-zPK0Ae7HdEASnaVJw-BNdzuL1KiMUtz2wNbB-pLGYvhm9c2h3GxChyOcKMC494D64G6_lVdBJzIRK8Gq_urtbFD2R0tanspMvbjzDcUr-vlHQ0ojE3s6G2QxIxuV'}
    res = requests.post('http://34.64.58.152:8080/api/notification', data=json.dumps(data), headers=headers)
    print(str(res.status_code) + " | " + res.text)

def main():
    while(1):
        print("과일의 이름과 센서값을 MQ-2, MQ-3, MQ-136, MQ-137 순서로 입력해주세요")
        fruit_name, mq_2, mq_3, mq_136, mq_137 = map(str, input().split())

        if fruit_name not in f_list:
            print("올바르지 않은 과일 이름입니다. 다시 입력해주세요.")
            continue

        if fruit_name == '바나나': # 바나나
            model_filename = 'random_forest_model_banana.joblib'
            loaded_model = joblib.load(model_filename)
            new_data = pd.DataFrame({'MQ-2': [mq_2], 'MQ-3': [mq_3], 'MQ-136': [mq_136], 'MQ-137': [mq_137]})
            prediction = loaded_model.predict(new_data)
        elif fruit_name == '귤': # 귤
            model_filename = 'random_forest_model_mandarin.joblib'
            loaded_model = joblib.load(model_filename)
            new_data = pd.DataFrame({'MQ-2': [mq_2], 'MQ-3': [mq_3], 'MQ-136': [mq_136], 'MQ-137': [mq_137]})
            prediction = loaded_model.predict(new_data)

        elif fruit_name == '감': # 감
            model_filename = 'random_forest_model_gam.joblib'
            loaded_model = joblib.load(model_filename)
            new_data = pd.DataFrame({'MQ-2': [mq_2], 'MQ-3': [mq_3], 'MQ-136': [mq_136], 'MQ-137': [mq_137]})
            prediction = loaded_model.predict(new_data)
        else: # 사과
            model_filename = 'random_forest_model_apple.joblib'
            loaded_model = joblib.load(model_filename)
            new_data = pd.DataFrame({'MQ-2': [mq_2], 'MQ-3': [mq_3], 'MQ-136': [mq_136], 'MQ-137': [mq_137]})
            prediction = loaded_model.predict(new_data)
        post(fruit_name, prediction)




if __name__ == "__main__":
    main()
