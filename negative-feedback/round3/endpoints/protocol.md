# 국소 불안정성 이후 무엇이 되는가

2026-10-22. 실행 전에 기록했다. 이전 round2는 infinitesimal imbalance의 부호를 확인했지만, 그 결과가 의미 있는 factor degradation을 만드는지 확인하지 못했다. 이번 계산은 이론의 미분식을 다시 확인하는 검산이 아니라 nonlinear endpoint와 task consequence라는 강한 반론을 검사한다.

## 고정한 질문과 모형

기존 네 상태 square,unit-sphere d4,identity positives,iid negatives,detached natural policy omega=4^(-s),epsilon=.3,InfoNCE를 유지한다. K1–8을 검사한다. 이 값은 이전 자연 정책 예를 유지한 것이며 유리한 parameter를 찾는 sweep이 아니다.

1. Tied rectangle 경로 f(a,b)=(cos(theta)a,sin(theta)b,0,0)에서 정확한 population angular field를 계산한다. 내부 stationary root를 모든 theta∈(0,pi/4]에서 탐색한다. Grid root 탐색은 analytic uniqueness proof가 아니다.
2. Square 아래 K의 instability가 theta≈0인 omitted-factor representation으로 가는가,유한theta의injective rectangle로 가는가,두형태가 공존하는가를 구분한다.
3. 각 stationary candidate에서 full d4 tangent Jacobian을 finite difference로 계산해 tied 안정과 full 안정이 다른지 검사한다. Generic ambient perturbation의 실제 flow로 대표후보를 확인한다.
4. theta의endpoint면 네 Gaussian mixture centers를 이용해 지정한 feature noise에서 Bayes-optimal factor accuracy를 계산한다. 사전에 σ∈{.05,.2}로 고정한다. 작은 noise를 고른 뒤만성공을주장하지않는다. 네 centers가 서로다르면 noiseless정보2bits라는exactfact와분리한다.

## 반증과 판정

- K4의 square instability가 안정한 mildimbalance로 끝나고 두factorBayesaccuracy가거의같다면, K4/K5 localphase를중대한semanticretention경계로해석할수없다.
- Root가 tied 평면에서만 stable이고 fullspace에서unstable이면 endpoint에대한전역/실질적해석을보류하고genericflow검증을추가한다.
- collapse endpoint가있어도본실험이 globalbasin을증명하지않는다. 네상태외일반정보삭제주장은금지한다.
- 임계근처 root 크기/normal form을 직접분석해local pitchfork인지확인한다. 관측한 branch로부터분기유형을추측하면수치추정이라고명시하고,가능한부분은증명한다.

Exact K count enumeration을우선사용하고,도출식과fullfield의독립적인수치미분으로오류를검사한다. 판정은결과를본뒤noise나K를변경하여성공하게만들지않는다.

## Root 이후 별도 flow 확인 규약

내부 root를 계산한 후,실제 attraction을 확인할 기준을 적분 전에 추가한다. K1,4,5,8 각각 primary9301–9303,confirmation9501–9503. 시작은 square의 angle imbalance.01+generic ambient noise.001이다. 각 K의 stable candidate에서 가장 느린 비회전 고유값을 사용해 horizon=20/lambda_min을 정한다. Candidate와의 rotation-invariant 거리<1e-5를 확인 기준으로 둔다. 실패하면 시간을 늘려 성공시키지 않는다. 이는 숫자로 찾은 도달점의 후속 검증이고,global basin/uniqueness의 증명이 아니다.
