# 자기 target 갱신의 정확한 작은 모형 분석

상태: 아래 명제 1–4는 이 문서에 증명을 제공한 **직접 도출**이다. 새로운 학술적 결과라는 뜻이 아니다. 명제 1–2는 Markov smoothing/power iteration의 직접 계산이고, 3–4는 Tian–Chen–Ganguli (2021) Lemma1/Eq2–4의 대각 특수화다. 논문 신규성 근거로 사용하지 않는다.

## 1. 관측과 비교 조건

독립 latent bits Z1,Z2는 균형 분포다. 조건부 독립 views X,Y는 각 latent bit를 독립 flip하여 E[Xj|Z]=E[Yj|Z]=sqrt(rho_j)Zj, 0<rho_j<1. 따라서 E[Xj Yk]=rho_j 1(j=k), Cov(X)=I이고 E[Yj|X]=rho_j Xj. 각 관측은 latent factor에 대해 양의 정보를 갖는다. teacher g0(Y)=diag(a01,a02)Y, a0j>0은 full rank이므로 관측 Y의 정보를 전부 보존한다. positive law·관측 정보는 frozen/EMA 비교에서 고정한다.

### 명제 1. 무제약 최적 예측+teacher 평균 갱신은 정확한 수축이다

조건부기대 연산자 K h(x)=E[h(Y)|X=x], Bayes squared-loss predictor f_t=K g_t, teacher refresh g_{t+1}=(1-beta)g_t+beta f_t, 0<beta≤1로 둔다. 초기 teacher가 g0(x)=(a01 x1,a02 x2)이면

`g_t(x)=(a01 q1^t x1, a02 q2^t x2), qj=1-beta+beta*rho_j∈(0,1)`.

증명. 조건부 독립 bit-flip law를 합산하면 K xj=rho_j xj. 갱신의 선형성으로 각 성분이 qj 배가 되며 induction하면 식을 얻는다. qj>0이므로 모든 유한 t에서 diag(a0j qj^t)는 invertible이다. t→∞에서 0으로 수렴한다. frozen teacher는 f(x)=(a01 rho1 x1,a02 rho2 x2)를 유지한다. □

**해석 한계:** frozen 대비 EMA의 amplitude 감소는 신뢰 가능한 정보 소실 증거가 아니다. 유한 t의 representation은 X의 일대일 변환이다. MI(Zj;g_t(X))=MI(Zj;X)이며 latent bit의 Bayes 분류율 `(1+sqrt(rho_j))/2`도 일정하다. 수치 underflow·제한된 readout·고정 noise를 도입하면 결과가 달라진다.

### 명제 2. 보이는 rank/접근성 저하는 normalization 가정에 의존한다

rho1>rho2이면 global output norm으로 매 step 재정규화한 teacher도 성분비 `(a02/a01)(q2/q1)^t`를 갖는다. 각 좌표 variance를 따로 1로 whitening하면 두 선형 factor는 모든 step 유지된다. 고정된 independent additive readout noise epsilon_j, Var(epsilon_j)=sigma²를 더하면 관측 factor Xj를 회귀하는 최적 linear R²는 `a_j(t)²/(a_j(t)²+sigma²)`이고 latent Zj에 대해서는 `rho_j*a_j(t)²/(a_j(t)²+sigma²)`이다.

증명. global normalization은 공통 scalar만 곱하므로 성분비가 바뀌지 않는다. coordinate whitening은 positive coefficient를 1로 나누어 없앤다. R²식은 Cov(Xj,aXj+epsilon)=a, Var(aXj+epsilon)=a²+sigma², Cov(Zj,Xj)=sqrt(rho_j)를 대입한 단순 회귀 공식이다. □

**결론:** '초기 full rank인데 target refresh로 요인 정보가 지워졌다'는 주장에는 finite/asymptotic, noise/precision/readout class를 명시해야 한다. 이것을 생략한 원래 가설은 검증 가능한 단일 주장이 아니다.

## 2. Predictor를 학습하는 정확한 EMA population flow

한 mode의 student w, predictor p, teacher a를 두고 L=(1/2)E[(pwX-aY)²], teacher 쪽 stop-gradient, student/predictor 각각 weight decay eta, teacher EMA speed beta>0를 사용한다. predictor/student learning-rate ratio는 1로 고정한다. 정확한 gradient flow는

`dot w=p(rho*a-p*w)-eta*w`

`dot p=w(rho*a-p*w)-eta*p`

`dot a=beta*(w-a)`.

Tian2021 Lemma1에서 X_paper=rho, (X+X0)_paper=1, alpha_p=1로 둔 식과 동일하다. rho는 observable pair law의 cross-correlation이며 추가 supervision은 없다.

### 명제 3. Balanced positive initialization의 회복/소실 경계

초기 w0=p0=a0=s0>0일 때 w(t)=p(t)=s(t)>0이고

`dot s=s*(rho*a-s²-eta), dot a=beta*(s-a)`.

(i) eta=0이면 모든 s0>0에서 (s,a)→(rho,rho).

(ii) 0<eta<rho²/4이면 `s±=(rho±sqrt(rho²-4eta))/2`가 존재한다. 0<s0<s−에서는 (s,a)→(0,0), s0=s−는 saddle에 머무르고, s0>s−에서는 (s,a)→(s+,s+).

(iii) eta>rho²/4이면 모든 positive balanced initialization에서 (s,a)→(0,0).

증명. d(w²-p²)/dt=−2eta(w²-p²)이므로 초기 차이 0은 유지된다. 평형은 a=s이고 s[s(rho−s)−eta]=0을 만족하여 0,s−,s+뿐이다. reduced flow는 positive quadrant에서 cooperative: ∂dot s/∂a=rho*s>0, ∂dot a/∂s=beta>0. s0∈(0,s−)이면 사각형 [0,s0]²는 forward invariant이고 처음 dot s<0, dot a=0이다. order-preserving semigroup으로 s,a가 단조 감소하며 극한은 그 사각형 안의 유일한 평형 0이다. s0∈(s−,s+)이면 [s0,s+]²가 forward invariant이고 단조 증가하여 s+로 수렴한다. s0>s+는 [s+,s0]²에서 같은 논리로 단조 감소한다. eta=0은 positive lower barrier s0<rho 또는 rho< s0에 같은 논리를 적용. eta>rho²/4는 rho*s−s²−eta<0이므로 positive 평형이 없고 upper-bound 사각형에서 0으로 수렴한다. □

eta=rho²/4의 nonhyperbolic 경계는 별도이며 위 iii에 포함하지 않았다. 수치 primary grid도 이 정확한 경계를 피한다.

### 명제 4. EMA speed는 이 모형에서 고정점·balanced basin 경계를 바꾸지 않는다

eta>0에서 nonzero equilibrium w=p=a=s*의 full 3D Jacobian 고유값은 `−2eta`와 다음 2×2 matrix의 고유값이다:

`B=[[-2s*², rho*s*],[beta,-beta]]`.

trace(B)<0이고 det(B)=beta*s*(2s*−rho). 따라서 s+는 locally asymptotically stable, s−는 saddle이다. origin의 선형 고유값은 −eta,−eta,−beta로 eta>0이면 안정하다. eta=0에서는 origin이 nonhyperbolic이며 명제3의 nonlinear flow가 positive initialization을 회복시킨다.

증명. full Jacobian의 w−p 방향은 −2eta의 고유값을 갖고 w=p의 tangent subspace에서는 B가 된다. trace/determinant criterion을 적용하면 끝난다. □

**선행 관계:** Tian2021 §3.2 Eq16/ Fig3–4는 weight decay가 안정적 collapse basin을 만들고 predictor 초기값에 따라 회복이 갈리는 현상을 이미 명시한다. 위의 정확한 scalar EMA와 anisotropic correlation 표기는 일반 Lemma1의 직접 적용이다. proportional-EMA 근사와 다른 표기라는 사실만으로 신규성은 생기지 않는다.

## 3. 비자명해 보이는 frozen-vs-updated 비교도 기존 방정식으로 설명된다

frozen a=a0=s0에서 balanced learner는 `dot s=s*(rho*s0−eta−s²)`다. rho*s0>eta이면 positive fixed point sqrt(rho*s0−eta), 그렇지 않으면 0으로 수렴한다. k=rho*s0−eta>0일 때 정확한 finite-time solution은 `s(t)²=k/[1+(k/s0²−1)exp(−2kt)]`이다(미분해 직접 확인). 따라서 eta/rho<s0<s−인 초기값은 frozen teacher에서는 positive mode를 유지하지만 EMA에서는 0으로 수렴한다. 이 구간은 eta>0일 때 비어 있지 않다.

이것은 입력과 initial target 모두 full rank인 상태에서도 teacher feedback이 차이를 만들 수 있다는 *정확한 예시*다. 그러나 결정 원인은 이미 알려진 weight-decay/predictor basin이며 새 자기교정 원리의 증거가 아니다. eta=0 대조에서는 모든 positive mode가 장기 회복된다.

## 4. 아직 도출하지 않은 것

비선형 계층, 원 문맥의 새로운 요인 발굴, normalization이 결합된 full-matrix neural dynamics의 일반 경계는 증명하지 않았다. 작은 모형의 기각을 이 더 넓은 문제 전체의 불가능성으로 확대하지 않는다. 이 문서의 exact controls가 기존 연구의 직접 결과이므로, 이를 독립 논문으로 진행하라는 권고는 할 수 없다.

## 5. Raw context와 invertible target 오차의 구분

### 명제 5. Full-rank linear target 변형은 무제약 population predictor의 정보 내용을 바꾸지 않는다

관측 context S, target vector Y, 고정 invertible B에 대해 squared loss를 최소화하는 모든 measurable predictor의 Bayes solution은 f_B(S)=E[BY|S]=B E[Y|S]다. 그러므로 f_B와 f_I는 invertible한 선형 변환 관계다.

증명. squared-loss conditional expectation의 유일성(거의 확실히)과 조건부기대의 선형성을 적용한다. B가 고정 invertible이므로 두 예측값은 서로 복원된다. □

이때 작은 target singular value는 finite-sample/regularized readout의 conditioning을 악화할 수 있으나, population nonlinear predictive state에 없는 정보를 teacher refresh가 새로 창조했다는 증거는 아니다. 문맥 S가 처음부터 더 많은 정보를 제공하거나 predictor class가 제한되면 그 조건을 별도 명시해야 한다. 본 명제는 conditional expectation의 기본 성질이며 신규성은 없다.
