import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split, KFold
import numpy as np

# 데이터셋 불러오기 (예: dataset.csv)
data = pd.read_csv('random_forest_data.csv')

# 입력 특성과 타겟 변수 분리
X = data[['MQ-2', 'MQ-3', 'MQ-136', 'MQ-137']]  # 입력 특성 선택
y = data['corruption_level']  # 타겟 변수 선택

# 데이터 분할
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 다양한 max_depth 값을 시도하고 교차 검증을 통해 성능 측정
max_depths = range(1, 21)  # 원하는 범위로 수정 가능
cv = KFold(n_splits=5)  # 5-폴드 교차 검증 사용

# 각 max_depth 값에 대한 교차 검증 결과 저장
mean_test_scores = []

for max_depth in max_depths:
    test_scores = []
    rand_clf = RandomForestClassifier(n_estimators=100, criterion='gini', max_depth=max_depth, bootstrap=True,
                                      random_state=42)

    for train_fold, valid_fold in cv.split(X_train):
        X_train_fold, X_valid_fold = X_train.iloc[train_fold], X_train.iloc[valid_fold]
        y_train_fold, y_valid_fold = y_train.iloc[train_fold], y_train.iloc[valid_fold]

        rand_clf.fit(X_train_fold, y_train_fold)
        test_score = rand_clf.score(X_valid_fold, y_valid_fold)
        test_scores.append(test_score)

    mean_test_score = np.mean(test_scores)
    mean_test_scores.append(mean_test_score)

# 결과 출력
best_max_depth = max_depths[np.argmax(mean_test_scores)]
print(f'최적의 max_depth: {best_max_depth}')
print("\n".join([f"{i}: {score:.4f}" for i, score in zip(max_depths, mean_test_scores)]))

# 시각화
plt.figure(figsize=(10, 6))
plt.plot(max_depths, mean_test_scores, marker='o')
plt.title('Random Forest - Cross Validation Scores')
plt.xlabel('max_depth')
plt.ylabel('Mean Test Score')
plt.grid(True)
plt.show()
