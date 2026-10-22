# 직접 분석: 회복을 요구하는 목적함수인가?

아래 명제는 **직접 증명**이다. 표준 Fourier/spectral 최적화 계산이며 학술적 신규성은 주장하지 않는다. 전체 nonlinear neural trajectory의 정리가 아니다.

## 1. 정의

X는 uniform {-1,+1}³, Y는 독립 bit channel `P(Y|X)=prod_j(1+rho_j X_jY_j)/2`. `K h(x)=E[h(Y)|X=x]`이다. Walsh basis `chi_S(x)=prod_(j∈S)x_j`는 `K chi_S=(prod_(j∈S)rho_j)chi_S`를 만족한다. 이는 조건부 독립성과 E[Yj|X]=rho_j Xj를 곱하면 바로 얻는다.

cosine self-distillation의 정규화된 online prediction q와 teacher f에 `L=2−2 E[q(X)·f(Y)]`를 둔다. 이번 bias-free tanh encoder와 linear predictor는 odd하며 normalization 후에도 odd다. q,f는 row unit norm, 따라서 평균0이다. 원래 BYOL의 모든 architecture를 가정한 정리가 아니다.

## 2. 명제 A — 복구 없이도 clean agreement의 전역 최적값을 달성한다

세 rho_j=rho∈(0,1)이고 q,f가 odd unit maps일 때 `L≥2−2rho`다. 임의 `v∈R³,||v||=1`에서 `f_v(x)=diag(v)x`, `q=f_v`는 그 하한을 달성하며 online encoder와 predictor의 모든 gradient가0이다. v의 일부 성분은0이어도 된다. 그러므로 rank1,rank2,rank3가 모두 같은 clean agreement 최적값을 달성한다.

**증명.** Walsh 전개와 oddness로 nonzero 계수는 singleton 또는 triple에만 있다. 해당 K 고유값은 rho 또는 rho³≤rho다. Parseval·Cauchy–Schwarz로

`E q(X)·f(Y) = sum_S lambda_S <qhat_S,fhat_S> ≤rho (sum||qhat||²)^(1/2)(sum||fhat||²)^(1/2)=rho`.

f_v는 row norm1이고 singleton만 있으므로 Kf_v=rho f_v, equality다. teacher=f_v, predictorI에서 anchor별 output gradient는 `−2 (I−ffᵀ)Kf/8=0`다. q의 gradient 자체가0이므로 predictor gradient도0이고, 연쇄법칙상 어떤 encoder parameterization에서도0이다. □

**실현 가능성.** hidden12 tanh encoder 안에 각 bit의 독립 neuron을 두면 tanh(k*x_j)=tanh(k)*x_j이므로 f_v를 정확히 나타낼 수 있다. capacity 부족으로 rank2만 가능한 것이 아니다. 실제 실험의 작은 epsilon-normalization은 gradient에 O(1e−12) 차이를 만든다.

**해석.** Deficit가 c를 억제한 뒤 clean으로 돌아와도, 목적함수가 c를 복구하도록 요구한다는 전제가 없다. 따라서 BN/LR/optimizer/EMA reset 후에도 c가 돌아오지 않았다는 사실만으로 별도 memory lock을 입증할 수 없다. 이 증명은 실제 네트워크의 모든 trajectory가 해당 manifold에 수렴한다는 정리가 아니며, 관측된 시간곡선을 완전히 정량적으로 설명하지도 않는다.

## 3. 명제 B — 제한 모형의 회복 경계는 spectral gap과 dormant head gain이다

다음은 parameter-EMA MLP가 아니라 **출력 coefficient를 EMA하는 제한된 diagonal family**다. active factors rho1=rho2=r, missing factor rho3=s. `f_a(x)=(sqrt((1−a²)/2)x1,sqrt((1−a²)/2)x2,a*x3)` 및 teacher f_b, predictorI에서

`L(a;b)=2−2[r sqrt(1−a²)sqrt(1−b²)+s ab]`.

student는 b를 고정하고 `dot a=−∂a L`, teacher는 `dot b=beta(a−b)`로 갱신한다. (a,b)=(0,0)의 Jacobian은

`J=[[-2r,2s],[beta,−beta]]`.

trace는 음수, determinant는 `2beta(r−s)`다. 따라서 s>r면 양의 eigenvalue, s<r면 두 고유값의 실수부 음수, s=r면0과−(2r+beta)다. EMA speed만으로 경계의 부호를 바꾸지 못한다. 이는 zero mode를 asymptotically stable이라고 부르면 안 되는 예시다.

**증명.** 위 explicit L을 미분하고 원점에서 Taylor 전개하면 된다. predictor의 unused dimension gain이 p>0이고 active gain1이면 첫 행은 `[-2r p², 2s p]`로 바뀌며 경계는 s>rp다. p=0은 선형화만으로 판단할 수 없는 별도 경우다. □

**다른 metric의 추가 통제.** 위 scalar Euclidean a의 flow를 그대로 쓰고 teacher를 매 순간 online과 같게 두면 `dot a=2(s−r)a`다. 다음 logistic law는 그와 다른, coefficient vector `v∈S²`의 **sphere Riemannian flow**를 정의했을 때의 식이다. 이 경우 `dot v_j=2v_j(rho_j−sum_k rho_k v_k²)`이고, r1=r2=r, r3=s, u=v3²에 대해 `dot u=4(s−r)u(1−u)`다. 따라서 u0∈(0,1)에 대한 정확한 해는

`u(t)=1/[1+(1/u0−1)exp(−4(s−r)t)]`.

증명은 sphere tangent projector `I−vvᵀ`를 online gradient `2diag(rho)v`에 적용한 뒤 v3²를 미분하면 된다. scalar a의 induced sphere metric은 `1/(1−a²)`이므로 위 Euclidean a dynamics와 global speed가 다른 이유도 설명된다. 원점의 local linearization은 같지만 전역 시간을 혼동하지 않는다. 이 수정은 독립 검토의 지적으로 명시했다.

이는 표준 logistic/spectral selection이다. 매우 작은 u0의 회복시간은 gap의 역수와 log(1/u0)에 의존한다. 작은 positive mode가 유한시간 검출되지 않았다는 사실을 영구 정보 소실로 바꾸지 않는다.

## 4. 명제 C — 같은 관측에서 contrastive objective는 복구 압력을 갖는다

같은 diagonal unit family에서 infinite-negative population InfoNCE temperature tau>0는

`L_NCE(w)=−sum_j rho_j w_j/tau + sum_j log cosh(w_j/tau)`, `w_j=v_j², w_j≥0, sum w=1`.

**증명.** positive alignment는 sum rho_jw_j. marginal negative Y의 bits는 독립이므로 `E_Y exp(f_v(x)·f_v(Y)/tau)=prod_j cosh(w_j/tau)`이며 x와 무관하다. □

각 Hessian diagonal은 sech²(w_j/tau)/tau²>0다. equal clean rho에서는 simplex 유일해가 w=(1/3,1/3,1/3)다. deficit rho=(.9,.9,0),tau1에서는 w=(1/2,1/2,0)가 KKT를 만족한다: active gradient는−.9+tanh(.5)<0이고 inactive gradient는0으로 더 크다. strict convexity로 유일해다.

따라서 agreement와 contrastive 비교는 단순 teacher 유무의 인과 실험이 아니다. 목적함수의 feature allocation 선택압부터 다르다. 이 elementary contrast가 이미 새 lock 가설보다 단순한 설명을 제공한다.

## 5. 근거의 범위

증명 A는 rank결손 agreement optimum의 존재와 최적성을 확정한다. B는 제한된 missing-mode 안정성·시간척도를 확정한다. C는 제한 diagonal contrastive family의 유일한 allocation을 확정한다. 실제 nonlinear MLP의 Adam trajectory는 별도 실행 결과다. B와 neural curve를 적합해 학습 일반법칙을 증명했다고 주장하지 않는다. 본 직접 증명들은 기존 spectral/feature suppression 원리를 계산한 통제이며 독립 논문의 완성된 새 기여가 아니다.
