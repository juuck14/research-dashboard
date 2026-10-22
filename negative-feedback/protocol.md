# 실행 전 연구 규약

작성: 2026-10-22. 이 파일을 만든 시점에는 아래 실험을 실행하지 않았다.

## H1
현재 similarity에 의존한 soft negative filtering이 충분한 encoder 차원 및 q>=epsilon/M 아래 누락된 factor를 local asymptotically stable하게 만들 수 있다.

## 첫 모형
X=(a,b), a,b 독립 균등 {-1,+1}. f_w=(w1*a,w2*b), d=2이며 두 요인을 모두 표현 가능. Positive는 먼저 X+=X로 고정. one-negative InfoNCE를 모든 상태에서 정확히 평균: ell=log(1+exp(s(x,x-)-s(x,x+))). s=f(x)^T f(y), temperature=1. negative marginal은 anchor 상태도 포함(같은 state의 다른 instance 허용). q=(1-epsilon)softmax(kappa*s)+epsilon/4. kappa<0는 유사 negative를 약하게 뽑는 filtering, kappa>0는 hard mining. 업데이트는 q stop-gradient. differentiate-through q는 별도 통제이며 동일 알고리즘으로 혼동하지 않는다.

## 대조
1. 독립 uniform q.
2. 같은 초기 encoder로 만든 q를 고정.
3. 매 step encoder로 갱신 q.
4. 전체 L(w,q(w))를 미분한 update(별도 알고리즘).

## 정확 계산
analytic stop-grad gradient와 frozen-q finite differences를 비교(오차<1e-6). 누락 w2=0의 Jacobian eigenvalue를 양/음으로 판정. 작은 초기값은 1e-2,1e-4,1e-6 및 확인 1e-5. identity positives에서 안정점이 없다면 H1의 이 모형 구현은 기각. 몇 번의 큰 초기값 run에서 못 배우는 것은 안정점 증거로 세지 않는다.

## 실험
kappa {-8,-2,0,2,8}, floor epsilon {0.01,0.1,1}, w1 initial {0.5,2}, missing w2를 작은 양수로 seed에 따라 교란. exploration seed {11,17}, confirmation {101,211}. exact gradient flow solve_ivp (rtol1e-8,atol1e-11), endpoint time100. epsilon=0.01의 느린 복원은 이론적 탈출 시간 bound와 비교하고 필요하면 그 bound에 따라 time 연장(결과를 보고 임의 연장하지 않음). w2 threshold0.1의 hitting time, floor lower bound, factor별 representation amplitude, exact sign-probe accuracy를 저장. float arithmetic 정보손실은 정보이론 소실과 다르다.

## 사전 판정
positive-invariant factor의 부재가 full-support 아래 saddle이면 단순 '유사 negative 제거가 영구적 실명'이라는 최초 기제를 기각한다. 추가 정규화나 augmentation/regularization을 넣을 경우 새로운 설정으로 기록하고 원래 반증을 덮어쓰지 않는다. 논문으로 진행하려면 알려진 feature suppression/geometry 결과와 다른 경계가 필요하다.

## 분석 후 추가한 별도 실험 N1 (base 결과를 변경하지 않음)
Base 1,080 exact-flow runs 모두 finite-time escape(confirmation540), 따라서 unconstrained trap 가설은 반박됐다. normalization이 Proposition3의 feasible append 방향을 제거한다는 reviewer 반론에 따라 별도 family를 추가한다.

N1: f_theta=(cos(theta)a,sin(theta)b), theta in[0,pi/2]. d2는 두 binary factors 표현에 충분하나 unit-norm budget 존재. q 정의와 identity positive는 동일. symmetric theta*=pi/4에서 G'=H_frozen+sampling-feedback-term을 직접 계산했다. 실행 전 예측: floor.1,kappa-2이면 frozen q(theta*)의 curvature>0인데 adaptive의 curvature<0. epsilon{.01,.1,.5}, kappa{-8,-4,-2,-1,-.5,0,2}, 초기 offset ±{1e-3,1e-5}, 확인 seed{101,211}의 perturbation으로 검증. finite-difference Jacobian error<1e-6. full-support q 유지. adaptive/frozen-at-initial/frozen-at-center/uniform 비교, horizon200 사전 고정. time 연장으로 성공사례 탐색하지 않음.

판정: 이 구별이 맞으면 normalized additive family 내 feedback-specific instability를 입증할 수 있으나 full representation class나 일반 SSL 결과로 확대하지 않는다. finite positive amplitude를 정보 부재라고 부르지 않으며 theta->0 극한의 factor loss와 finite noisy-readout accessibility를 구분한다. normalized geometry와 sampler-dependent objective 선행과 비교하여 신규성 없으면 독립 연구 추천은 하지 않는다.

## 후속 분석 N2 실행 전 기록
Reviewer가 one-negative artifact를 공격. K in{1,2,4,8,16} iid negatives의 multinomial category counts를 exact enumerate하여 symmetric square의 frozen/adaptive curvature를 계산한다. ε in{.01,.1,.5}, κ in{-8,-4,-2,-1,-.5,0,2}. 검증 기준은 K>1에서도 matched frozen H>0 및 adaptive H<0가 존재하는지. KL/MC 추정 불사용, multinomial probabilities 합1 및 analytic-vs-finite-difference 오차<1e-5 확인. N2는 scalar additive mode이며 full-sphere K>1의 모든 tangent eigenvalue를 증명하지 않는다. K1 full-sphere 검산과 구별한다.
