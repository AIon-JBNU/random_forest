import joblib
import pandas as pd

model_filename = 'random_forest_model.joblib'
loaded_model = joblib.load(model_filename)

value1, value2, value3, value4 = map(float, input().split())
# 새로운 데이터에 모델을 적용 예측
new_data = pd.DataFrame({'MQ-2': [value1], 'MQ-3': [value2], 'MQ-136': [value3], 'MQ-137': [value4]})
prediction = loaded_model.predict(new_data)

print('예측 결과:', prediction)