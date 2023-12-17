# Random Forest를 활용한 과일 부패 단계 분류

이 프로젝트는 가스 값 4개를 사용하여 과일의 부패 단계를 분류하고, 이 정보를 기반으로 알림을 보내는 기능을 제공합니다.

## 프로젝트 목표

- 과일의 부패 정도를 예측하고 이를 모니터링하기 위한 솔루션을 제공합니다.
- 실험을 통해 수집된 데이터를 가공하여 모델 학습에 적합하게 전처리합니다.
- 가스 값 데이터를 수집하고 부패 단계를 분류하기 위한 머신 러닝 모델을 훈련시킵니다.
- 모델을 활용하여 과일 이름과 가스 값을 입력하면, 과일의 부패 정보를 어플리케이션에 알림으로 보냅니다.

## 주요 기능

1. **데이터 수집 및 가공**:
   -데이터 예쁘게 자르기.py, 데이터 모으기.py, level 추가.py 수집된 가스 값 데이터 CSV 파일을 모으고, 부패 단계 정보를 추가합니다.

2. **머신 러닝 모델 훈련**:
   - random_roest.py 전처리된 데이터를 사용하여 Random Forest 모델을 학습시킵니다.
   - for max_Depth.py random forest 모델에서 최적의 깊이를 알아냅니다.
 
3. **알림 기능**:
   - rf2s.py 과일 이름과 가스 값 4개를 입력하면, 해당 정보를 애플리케이션을 통해 사용자에게 알림으로 전달합니다.
   - random_forest_input.py 사용자가 과일 이름과 가스 값 4개를 입력하면, 해당 정보를 표준 출력합니다.

## 


