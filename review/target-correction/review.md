# 자기 target 교정 방향 독립 교차검토

판정 의견: **현재의 선형 고정점·EMA basin 기여는 기각**. 더 넓은 계층적 target 교정 질문 전체의 불가능성은 증명하지 않았다. 본 검토는 제안자 파일을 읽은 뒤 별도 증명과 코드로 검산했다.

## 1 선행연구와의 정확한 동등성

[Tian, Chen, Ganguli, ICML 2021 원문](https://proceedings.mlr.press/v139/tian21a/tian21a.pdf) Lemma 1 Eq.2–4를 직접 읽었다. 해당 논문의 online W, predictor Wp, target Wa에 각각 w,p,a를 대응하고 X=rho, X′=1−rho, alpha_p=1을 대입하면 owner의 다음 식과 정확히 같다.

```
w′ = p(rho*a−p*w)−eta*w
p′ = w(rho*a−p*w)−eta*p
a′ = beta(w−a)
```

여기서 X+X′는 view variance 1, X는 cross-view covariance rho다. 따라서 whitening 뒤 scalar correlation을 바꾸는 것도 그 Lemma의 다른 covariance를 고른 경우다. 같은 논문 §3.2 Eq.14–16 및 Fig.4는 balancing, collapsed/noncollapsed fixed points, 초기값에 따른 두 basin을 이미 다룬다. 현재 결과를 새로운 오류 교정 원리라고 부를 수 없다. 다만 임의의 비선형 teacher correction 이론 전체가 이 논문으로 해결됐다고 주장해서도 안 된다.

[Richemond et al., ICML 2023](https://proceedings.mlr.press/v202/richemond23a/richemond23a.pdf) §3–5는 predictor와 orthonormalization의 연결을 직접 분석한다. 단순 whitening 후 amplitude를 살리는 대조 역시 새 해결책으로 제시하기 어렵다.

[Korchinski et al., 2026 preprint](https://arxiv.org/html/2605.27734v1) §5 A1은 학습한 latent의 nonzero linear projection이 target에 남는다는 가정이고 A2는 detectable correlation의 학습 가정이다. Appendix C.3은 층별 clustering과 prediction loss의 진행을 보고한다. 이는 임의의 target 오류를 교정한다는 일반 정리가 아니므로 그 부분에는 논리적 공백이 있을 수 있다. 그러나 위의 scalar flow만으로 이 공백을 메웠다고 주장할 수 없다.

## 2 직접 도출한 고정점과 안정성 검산

rho,eta,beta>0이고 양의 초기값에 한정한다. 세 축의 경계에서 바깥으로 나가는 미분이 음수가 아니므로 양의 orthant는 불변이다.

직접 계산하면 `(w²−p²)′=−2*eta*(w²−p²)`다. 비영 평형에서는 w=p=s, a=s이고 s²−rho*s+eta=0이다. rho²>4eta일 때 s±=(rho±sqrt(rho²−4eta))/2가 있다.

원점의 Jacobian 고유값은 −eta,−eta,−beta이므로 국소 안정이다. 비영점의 transverse 고유값은 −2eta이고, balanced 부분의 Jacobian은 다음과 같다.

```
[ −2s²   rho*s ]
[  beta   −beta ]
```

trace<0, determinant=beta*s*(2s−rho)이므로 s+는 국소 안정, s−는 saddle이다. beta는 이 평형의 존재와 local stability 부호를 바꾸지 않고, 과도경로와 basin 도달 여부를 바꿀 수 있다. rho²=4eta의 경계는 비쌍곡점이므로 위의 strict stability 판단에서 제외한다. 이 직접 계산은 선행의 동역학을 검산한 것이며 독립 신규 정리가 아니다.

별도 `code/independent_checks.py`는 54개 평형에서 finite-difference Jacobian과 analytic spectrum을 비교했다. `results/summary.json`: 최대 Jacobian 오차 2.876e−10, spectrum 오차 8.882e−15, fixed-point residual 9.888e−17이다. 수치 검산이 위 증명을 대신하지는 않는다.

## 3 실제 frozen/EMA stress test

사전 protocol대로 rho=.8, eta=.02, w0=p0=.01, a0=.1에서 scipy solve_ivp를 T=5000까지 실행했다. 학습 predictor+EMA의 beta=.001에서는 (w,p,a)=(.72308,.72308,.67860)으로 성장했으나 아직 평형에 도달하지 않았다. beta=.1과 10에서는 w가 각각 약 3.02e−45,6.25e−46로 줄었다. 후자의 a가 수치적으로 −3e−13 근처를 보인 것은 solver absolute tolerance 수준의 오류이며 실제 음수 target이나 정확한 finite-time collapse로 해석하지 않는다. 이 수치 차이는 이미 알려진 teacher lag와 basin 효과의 재현이다.

predictor가 없는 경우에는 `w′=rho*a−(1+eta)*w`, `a′=beta*(w−a)`다. trace<0이고 determinant=beta*(1+eta−rho)>0이므로 rho<1+eta에서 원점으로 수렴한다. frozen teacher에서는 w*=rho*a0/(1+eta)다. 이 대조에서 feedback 자체의 차이는 존재하지만 선형 smoothing의 결과로 충분히 설명된다.

## 4 정보 소실 해석에 대한 결정적 반론 두 개

### 유한시간 amplitude decay는 noiseless 정보 소실이 아니다

owner의 bit-flip Markov/Bayes smoothing에서 nonconstant factor의 multiplier는 lambda_j=1−beta+beta*rho_j다. 현재 rho_j,beta 범위에서 0<lambda_j<=1이므로 a_j(t)=a_j(0)*lambda_j^t>0는 모든 유한 t에 성립한다. 따라서 두 bit를 `(a1(t)*x1,a2(t)*x2)`로 출력하면 noiseless exact decoder는 두 bit를 모두 읽는다.

별도 enumeration은 t=0,10,100,200 모두 4상태를 구분하고 joint MI=2bits임을 확인했다. 고정 sigma=.01 관측 잡음을 도입하면 bit accuracy는 Phi(a_j/sigma)로 감소하지만, 이는 잡음 아래 접근성의 결과다. `lim I(X;g_t(X))`와 `I(X;lim g_t(X))`를 바꿔 쓸 수 없다. 실제 구현의 underflow나 정규화 때문에 0이 됐다면 그 수치 조건을 별도로 정의해야 한다.

### finite support에서는 rank 저하도 정보 소실을 보장하지 않는다

독립 uniform bits (x1,x2)를 rank1 선형 표현 `r=x1+c*x2`로 보낸다. c=.001 또는 .5면 네 상태의 r 값이 모두 달라 정확히 2bits를 보존한다. c=0이면 1bit, c=1이면 1.5bits다. `results/rank_one_counterexample.json`에 exact enumeration을 저장했다. 선형 probe가 factor를 읽기 어렵거나 행렬 rank가 1이라는 것만으로 nonlinear 정보가 없다고 결론내릴 수 없다. 연속 Gaussian source의 rank 주장과 유한 binary source의 injectivity 주장을 섞으면 안 된다.

## 5 연구 판정에 미치는 영향과 남은 범위

현재 모형의 결과가 뒷받침하는 것은 다음까지다.

- full-positive 초기 teacher라도 known linear SSL flow에서 asymptotic collapse basin에 들어갈 수 있다.
- EMA의 lag는 동일 시작점의 경로를 바꿀 수 있지만 이 기제는 이미 선행의 직접 대상이다.
- Markov smoothing의 amplitude 감소를 정보 소실로 읽으면 과장이고, noiseless finite-time 또는 finite-support nonlinear decoding은 별도로 봐야 한다.

원래 질문 중 다층 문맥에서 새 latent 구분이 생기고 teacher 갱신이 그 구분을 구조적으로 교정하는가라는 부분은 이 모형이 다루지 않는다. 해당 부분을 살리려면 단순 diagonal shrinkage·correlation threshold와 다른 현상을 먼저 확보해야 한다. 예컨대 같은 frozen-target Bayes 성능을 가진 오류 구조끼리 갱신 후 결과가 다르고, 차이를 분석으로 설명해야 한다. 그러한 결과가 아직 없으므로 현재의 실질적 선형 결과를 근거로 '수정 후 진행'을 권하지 않는다. **현재 정식화의 기여는 기각, 더 넓은 질문은 미해결**이라는 구분이 타당하다.

## 재현

실행: `OPENBLAS_NUM_THREADS=1 python review/target-correction/code/independent_checks.py` (저장소 root 기준). 독립 protocol, CSV/JSON, 전체 스크립트가 같은 디렉터리에 있다. deterministic population 계산이며 대규모 신경망 학습이나 empirical dataset의 결론이 아니다.
