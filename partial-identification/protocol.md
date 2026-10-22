# 사전 기록 2026-10-22

이 문서는 첫 수치 실행 전에 작성했다.

## 모형과 정보

관측은 환경 label e와 x. 원 잠재 s와 mixing A는 합성 검증자만 안다. e=0에서 covariance I, e=1에서 D_gamma=diag(1+gamma,1-gamma). x=A s, 관측 whitening에 더해 기준환경 소스 covariance가 정확히 I라는 추가 신뢰 가정을 둔 제한된 family에서 A는 orthogonal. broader GL(d) family에서는 본 결과를 feasible subset/lower bound로만 해석한다. 허용 모델은 동일 두 Gaussian 관측분포를 정확히 만들고 각 환경의 source Gaussian total correlation이 delta 이하인 모든 회전이다. sign/permutation은 같은 해. componentwise 가역 비선형 변환도 일반 개념상 같지만 수치모형의 선형 family 밖이므로 선형회전과 혼동하지 않는다.

## 사전 명제

1. theta in [0,pi/4]에서 TC(theta)=.5 log(1+gamma^2 sin^2(2theta)/(1-gamma^2)).
2. theta_max=.5 asin(min(1,sqrt(expm1(2delta)*(1-gamma^2)/gamma^2))).
3. delta>=-.5 log(1-gamma^2)면 전체 회전 quotient 허용. n 증가로 이 ambiguity를 없앨 수 없다.
4. delta>0이면 true independent point 주변의 비자명한 작은 회전이 항상 허용된다. 따라서 정확한 axis와 approximate cone은 구분해야 한다.

## 실험 A 정확 계산

- gamma=[.01,.03,.1,.3,.6], delta=[1e-6,1e-4,1e-3,.01,.05]. theta 100001-point grid.
- covariance의 TC를 직접 계산해 닫힌식과 비교. grid endpoint 오차 <=2 grid steps. 관측 covariance 재구성 오차 <=1e-12.
- 별도 확인 gamma=[.017,.071,.23,.49], delta=[2e-5,7e-4,.007,.03].
- 실패 시 수식/코드 오류를 기록하고 수정한다. 수치값은 증명으로 세지 않는다.

## 실험 B 3D 구조 해상도

- D=diag(1.02,.98,1.8), D0=I. 1-2 weak pair와 1-3 strong pair를 각각 회전.
- delta=1e-4,1e-3,.01에서 최대 각도를 exact TC로 계산. 모든 비자명한 회전은 정확한 mixing interpretation을 바꾸지만 동일 x law.
- 비교는 기존 eigengap에 따른 효과인지 평가. 강한 subspace의 정확한 식별이라고 과장하지 않는다.

## 실험 C 표본과 구조 ambiguity의 분리

- theta 별 population identified set를 정답으로 두고 covariance 표본오차만 반복 측정.
- gamma=.03,.3, n=[100,1000,10000], exploration seed=100..119, confirmation=1000..1039.
- joint covariance diagonalization의 최소점이 표본 증가로 정확해져도 delta>.0 identified set가 남음을 설명용으로 확인.
- 새 통계적 보장으로 주장하지 않는다. raw seed별 값과 aggregate를 보존한다.

## 판정 문턱

현재 모형의 결과가 covariance perturbation과 이분산 식별의 즉각적 귀결이면 원 주제를 독립 연구로는 기각/보류한다. exact identified-set formulation이 문헌상 새롭다는 증거 없이 논문 권고하지 않는다. 비선형/비Gaussian 확장에 핵심 검증이 남으면 '진행 권고'로 쓰지 않는다.

## 실행 전 scope 정정

독립 critic의 지적으로 기준환경 소스 covariance I를 단순 normalization이라고 부른 것을 정정했다. 이는 실제 추가 모델 제약이다. 사전 수치 grid/판정 기준은 그대로이며, broader family에 대한 exact-set 주장은 하지 않는다.
