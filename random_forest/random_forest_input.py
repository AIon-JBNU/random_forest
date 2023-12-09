import joblib
import pandas as pd

print("random forest 바탕 귤 부패 분류")
model_filename = 'random_forest_model.joblib'
loaded_model = joblib.load(model_filename)

print("MQ-2, MQ-3, MQ-136, MQ-137 순서로 입력해주세요")

value1, value2, value3, value4 = map(float, input().split())
# 새로운 데이터에 모델을 적용 예측
new_data = pd.DataFrame({'MQ-2': [value1], 'MQ-3': [value2], 'MQ-136': [value3], 'MQ-137': [value4]})
prediction = loaded_model.predict(new_data)

print('예측 결과:', prediction)

if prediction == 1:
    print("부패하지 않음")
elif prediction == 2:
    print("부패 예정")
else:
    print("부패 함")
