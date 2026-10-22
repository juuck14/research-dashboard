# 직접 수행한 이론 분석

증거 구분: 아래 정리 1–4는 본 연구에서 직접 쓴 완전 증명이다. 알려진 Gaussian mutual-information 공식과 행렬 회전에 대한 초등 계산을 사용한다. 새 정리라는 문헌상 신규성 주장은 하지 않는다. 마지막 고차원 식은 Taylor 전개이며 별도의 일반 정리로 주장하지 않는다.

## 1 문제 정의와 equivalence

관측 환경 E in {0,1}, P(X|0)=N(0,I_2), P(X|1)=N(0,D_gamma), D_gamma=diag(1+gamma,1-gamma), 0<gamma<1. 관측분포는 모집단 수준에서 정확히 알려져 있다고 가정한다. 선형 invertible x=A s, 기준환경 source covariance가 정확히 I라는 추가적인 신뢰 가정을 둔다. Gaussian이므로 기준환경에서는 정확한 소스 독립성까지 요구하는 셈이다. 이것은 관측 X의 whitening만으로 얻어지는 정규화가 아니다. 이 추가 가정 아래 A A^T=I, 즉 A는 orthogonal이다. 따라서 아래 exact set는 이 제한된 family 안에서 exact하며, 일반 approximate-independent GL(d)/비선형 family에는 feasible subset 및 ambiguity lower bound로만 적용된다.

각 대안 Q in O(2)는 sources y=Q^T x와 decoder x=Q y를 갖는다. 모든 Q는 두 관측분포를 **정확히 동일하게** 생성한다. 허용 structural misspecification은 max_e TC(P(y|e))<=delta, TC(P)=KL(P || product_i P_i). delta는 관측에서 검증 가능한 '참 오차'가 아니라 사용자가 허용하는 소스 가정의 민감도 예산이다.

동일해 equivalence는 source coordinate의 순서·부호(orthogonal normalization 후 남는 scale 대칭)다. 일반 nonlinear ICA의 componentwise invertible transforms도 표현 의미상 같은 해로 인정해야 하지만 이번 Gaussian linear family의 내부 변환은 아니다. TC는 개별 좌표에 대한 가역 변환에 불변이다: 분자·분모 밀도의 Jacobian이 상쇄되어 KL 적분이 같다. 따라서 arbitrary units/scaling으로 dependence budget을 줄이는 속임수는 없다. 두 source를 섞는 비trivial rotation은 componentwise 재매개화가 아니므로 실질적 대안이다.

O(2)를 source signed permutations로 quotient하면 rotation의 각도는 pi/2를 주기로 본다. theta in [-pi/4,pi/4]를 취할 수 있고 true basis로부터의 **거리**는 |theta|다. 양·음 각도는 일반적으로 서로 다른 해이며 아래 수식은 대칭이므로 양의 반쪽에서 radius를 계산한다.

## 정리 1 Exact two-dimensional identified set

R_theta의 열을 (cos theta,sin theta),(-sin theta,cos theta)로 둔다. D_theta=R_theta^T D_gamma R_theta이면

TC(theta) = 1/2 log(1 + gamma^2 sin^2(2theta)/(1-gamma^2)).

따라서 quotient 위 허용각 집합은 |theta|<=theta_max이며 (경계의 주기 동일시 포함)

theta_max = 1/2 asin(min{1, sqrt[(exp(2delta)-1)(1-gamma^2)/gamma^2]}).

전체 quotient가 허용되는 문턱은 delta_crit=-1/2 log(1-gamma^2).

### 증명

회전된 covariance의 두 diagonal은 1+gamma cos 2theta 및 1-gamma cos 2theta, offdiagonal은 부호를 제외하면 gamma sin 2theta다. determinant는 rotation invariance로 1-gamma^2. 2D Gaussian의 differential entropy h(N(0,C))=log(2pi e)+1/2 log det C와 marginal entropy 합을 빼면 TC=1/2 log(C11 C22/det C). 대입하면 식이 나온다. theta in [0,pi/4]에서 sin 2theta가 단조 증가하므로 TC<=delta를 풀면 exact interval. theta=pi/4 대입으로 문턱. 모든 R_theta가 동일 observed covariance를 재구성하므로, 이 양·음 대칭 arc는 제한된 O(2) family에서 upper bound만이 아니라 정확한 허용 모델의 집합이다. QED.

### 해석과 초등 점근식

작은 delta에서 theta_max ≈ sqrt[delta(1-gamma^2)/(2 gamma^2)]. 즉 dependence tolerance가 KL 단위이면 ambiguity는 sqrt(delta)/gamma로 커진다. '오차/최소 특이값'이라는 막연한 말은 오차 측도에 따라 지수가 달라진다. 그러나 이 scaling은 Gaussian MI+eigen-gap 계산의 즉각적인 결과이며 독립 신규성은 약하다.

## 정리 2 모집단 비식별성의 통계적 하한

동일 관측분포 P와 tolerance delta에서 theta0=0 및 theta1=theta_max를 허용하는 두 DGP가 있다. source-axis parameter의 quotient 거리 d에 대해 triangle inequality를 쓰면 임의 estimator T_n(X_1,E_1,...,X_n,E_n)에 대해

max(E_{theta0} d(T_n,theta0), E_{theta1} d(T_n,theta1)) >= theta_max/2.

이는 n과 무관하다.

### 증명

두 DGP의 데이터 법칙이 같으므로 estimator law도 같다. 모든 출력 t에 d(t,theta0)+d(t,theta1)>=d(theta0,theta1)=theta_max. 공통 law에 적분하고 두 risk 중 큰 값이 합의 절반 이상이라는 사실을 적용한다. QED.

이것은 새 정보이론 기법이 아니라 observational equivalence의 표준 two-point argument다. seed stability는 이 하한을 회피할 수 없다. 알고리즘이 항상 theta0를 출력해도 theta1 DGP에서 오류가 남는다.

## 정리 3 양의 tolerance에서 정확한 axis/group의 국소 비식별성

유한 개 환경에서 source covariance D_e가 positive definite이고 diagonal이라고 하자. 임의 delta>0와 임의 pair i!=j에 대해 그 pair를 비trivial하게 섞는 충분히 작은 Givens rotation R가 모든 환경에서 TC(R^T D_e R)<delta를 만족한다.

### 증명

각 e에서 TC(I)=0이고 positive-definite covariance에 대한 TC는 연속이다. 환경 수가 유한하므로 각 환경의 연속성 neighbourhood 교집합에 작은 nonzero Givens rotation이 존재한다. 이 rotation은 i,j axes를 섞고 여전히 동일 x law를 만든다. QED.

어떤 고정된 proper coordinate block을 고르더라도 그 block과 complement의 두 axis를 작은 각도로 섞는 rotation이 허용된다. 따라서 별도 exact sparsity/block restriction 없이, delta>0만으로 **정확한** coordinate axis 또는 nontrivial block subspace가 공통 유지된다는 주장은 성립하지 않는다. approximate cone이나 허용 tolerance 해상도만 말할 수 있다. baseline identity도 모든 rotation에서 독립이므로 이 반례를 막지 않는다.

## 정리 4 pairwise 일반화와 강한 축의 근사 회복

d차원 covariance에서 eigenvalues a,b인 pair만 theta만큼 회전시키면 다른 좌표의 TC 기여는 0이고

TC_pair(theta)=1/2 log(1+[(a-b)^2/(4ab)] sin^2 2theta).

따라서 theta_max=1/2 asin(min{1,sqrt[4ab(exp(2delta)-1)/(a-b)^2]}). a=b이면 모든 theta 허용.

증명: 정리 1의 covariance diagonal product를 일반 a,b로 다시 계산한다. product=ab+(a-b)^2 cos^2 theta sin^2 theta. determinant=ab. QED.

이 식은 weak pair의 ambiguity가 크고 strong-separated pair의 ambiguity가 작음을 보이지만 **strong axis가 정확히 identified라는 뜻은 아니다.** 또한 두 좌표를 각각만 회전해 얻은 radius는 전체 O(d) identified set의 projection에 대한 완전한 upper bound가 아니다. 결과표는 'pairwise feasible lower examples'로 표시한다.

## 여러 환경과 local geometry

평균 예산 sum_e p_e TC_e<=delta를 쓰면 (max-budget과 다른 문제) 작은 skew angles theta_ij에 대해

sum_e p_e TC_e = (1/2) sum_{i<j} [sum_e p_e (d_ei-d_ej)^2/(d_ei d_ej)] theta_ij^2 + O(||theta||^3).

이를 conditional dependence sensitivity ellipsoid로 볼 수 있지만 바로 joint-diagonalizer conditioning이다. 이것을 새로운 SSL 원리라고 부르지 않는다. exact environment signatures가 같은 pair는 zero curvature를 갖고 arbitrary rotation이 가능하다는 고전 joint diagonalization 결과와 연결된다.

## 원래 질문에 대한 범위

확보한 것: 같은 관측분포의 실제 대안, 허용 transform의 구분, exact 2D identified set, 표본 무관 하한, exact block 주장의 반례.

미확보: 일반 nonlinear source-dependence budget의 identified set, 유한 자료의 정직한 confidence set, 신경망 학습 dynamics, 실제 자료에서 delta를 정하는 원리. 이들이 논문 핵심이라면 여전히 핵심 검증이 남았다.
