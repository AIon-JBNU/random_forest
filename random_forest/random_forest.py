import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib

# 데이터셋 불러오기 (예: dataset.csv)
data = pd.read_csv('random_forest_data.csv')

# 입력 특성과 타겟 변수 분리
X = data[['MQ-2', 'MQ-3', 'MQ-136', 'MQ-137']]  # 입력 특성 선택
y = data['corruption_level']  # 타겟 변수 선택

# 데이터 분할
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Random Forest 모델 학습
rand_clf = RandomForestClassifier(n_estimators=100, criterion='gini', max_depth=5, bootstrap=True, random_state=42)
rand_clf.fit(X_train, y_train)

# 모델 평가
train_accuracy = rand_clf.score(X_train, y_train)
test_accuracy = rand_clf.score(X_test, y_test)

print('훈련세트 정확도: {:.3f}'.format(train_accuracy))
print('테스트세트 정확도: {:.3f}'.format(test_accuracy))

# 특성 중요도 계산
feature_importances = rand_clf.feature_importances_

print(feature_importances)

# 특성 중요도 시각화
plt.figure(figsize=(10, 6))
sns.barplot(x=feature_importances, y=X.columns)
plt.title("Random Forest - Feature Importance")
plt.xlabel("Feature Importance")
plt.ylabel("Features")
plt.xticks(rotation=45)
plt.show()

# 모델을 저장할 파일 경로와 이름 지정
model_filename = 'random_forest_model.joblib'

# 모델을 파일에 저장
joblib.dump(rand_clf, model_filename)
