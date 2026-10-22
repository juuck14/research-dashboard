# 직접 도출한 분석

분류: 아래 Proposition 1–3은 이 연구에서 직접 쓴 완전한 증명이다. 선행연구 전체에서 새로운 정리라는 주장은 하지 않는다. 단순 모형의 반증/기준선 역할이다.

## 정의
x=(a,b) in {-1,+1}^2, p(x)=1/4, f_w(x)=(w1 a,w2 b). Positive x+=x. s_w(x,y)=f_w(x)^T f_w(y). One-negative InfoNCE ell_w(x,y)=log(1+exp[s_w(x,y)-s_w(x,x)]).

sampler q_w(y|x)>=epsilon/4, epsilon>0. q_w는 smooth해도 되고 time-dependent여도 된다. 실제 update vector field는 G(w)=E_x E_{y~q_w} [∇_w ell_w(x,y)]이며 q_w는 stop-gradient. 이것은 일반적으로 ∇_w E_{q_w}ell_w와 다르다. gradient flow dw/dt=-G(w).

## Proposition 1. identity positive 아래 factor omission은 attracting하지 않는다
w2=0에서 G2=0. 그러나 q_w가 연속이고 smooth인 경우 이 불변 manifold의 transverse linear growth는

lambda2(w1)=4 E_x sum_{y:b_y=-b_x} q_(w1,0)(y|x) sigmoid[w1²(a_x a_y-1)] >= epsilon/2 >0.

따라서 w2=0은 local attracting factor-omission boundary가 아니며, 어떤 finite w1에서도 아주 작은 비영 w2 perturbation은 증가한다.

### 증명
Delta=w1²(a_x a_y-1)+w2²(b_x b_y-1). ∂ell/∂w2=2w2 sigma(Delta)(b_x b_y-1). b_x b_y-1는 0 또는 -2이므로 -G2=4w2 E_x sum_{b_y=-b_x}q_w sigma(Delta). w2=0에서 q의 derivative는 w2 앞의 계수에만 들어가므로 선형화에 기여하지 않는다. 각 x에서 y=(a_x,-b_x)는 q>=epsilon/4이며 Delta=0이므로 lambda>=4*(epsilon/4)*(1/2)=epsilon/2. QED.

이 증명은 q의 hard/easy 선호, factor dependence를 제한하지 않는다. 필요한 것은 positive-invariant factor, 추가 factor coordinate, unconstrained dot product, stop-grad update와 floor이다. q가 실제로 encoder를 사용하지 않는 고정 정책도 같은 결과다.

## Proposition 2. 국소적 탈출에 대한 유한 시간 상계
0<w2(t)<=delta이면 (어떤 w1(t)에서도)

d log(w2)/dt >= epsilon * sigmoid(-2delta²).

따라서 initial eta in (0,delta), hitting time T_delta <= log(delta/eta)/[epsilon sigmoid(-2delta²)].

### 증명
Proposition 1의 special negative y=(a_x,-b_x)에 대해 모든 w2에서 Delta=-2w2². 그 항만 남기고 q>=epsilon/4를 적용하면 dw2/dt>=epsilon w2 sigma(-2w2²)>=epsilon w2 sigma(-2delta²). 적분하면 결과. QED.

이 bound는 local linearization만을 이용하지 않으며 epsilon이 time-independent lower floor인 동안의 actual escape를 보장한다. 초기값이 정확히0이면 multiplicative parameterization 때문에0에 남는다. 이는 measure-zero invariant manifold이며 안정점 증거가 아니다.

## Proposition 3. 추가 unused coordinate를 이용한 일반 방향
입력 x의 binary feature b(x)가 positive pair에서 항상 동일하고, 임의의 기존 representation h가 그 feature를 누락한다고 하자. 새 coordinate를 붙인 f_t(x)=(h(x),t b(x))를 허용한다. K개의 negatives에 대한 finite InfoNCE에서 q를 stop-grad로 취급하면 dL/d(t²)<=0. positive-probability negative 중 b가 다른 것이 있으면 유한 scores에서 strict inequality.

### 증명
D_i=h(x)^T h(y_i)-h(x)^T h(x+). 각 negative logit contrast는 D_i+t²[b(x)b(y_i)-1]. ell=log[1+sum_i exp(contrast_i)]. t² derivative는 negative softmax weight의 양의 조합에 계수0 또는-2를 곱한 값. factor-mismatched negative가 있으면 한 항이 strict negative. QED.

이는 충분한 자유 coordinate가 있는 population model에서 positive-invariant binary factor omission을 local minimum이라 부를 수 없다는 기준선이다. normalized sphere, fixed total norm, projection bottleneck, augmentation이 feature를 변경하는 경우, weight decay, encoder가 새 coordinate에 접근할 수 없는 경우에는 이 방향이 허용되지 않아 적용되지 않는다. 데이터의 모든 의미 요인이 positive-invariant라고 가정하는 것도 타당하지 않다.

## 정보 보존과 접근성
이 exact finite-state family에서는 w2가 아무리 작아도 nonzero이면 z2=w2*b에서 b=sign(z2)로 정확 복원되어 H(b|f)=0이다. 작지만 nonzero인 amplitude를 정보 손실로 부를 수 없다. finite precision, noise, regularized finite-label probe에서는 접근성 저하가 생길 수 있으나 별도 모형이다. w2=0이면 b가 독립이고 representation은 a만의 함수이므로 H(b|f)=log2이며 b의 최적 정확도는1/2이다. 수치 probe 실패로 이 conditional entropy 결론을 대신하지 않았다.

## 무엇을 반박하고 무엇을 반박하지 않는가
원래 '현재 유사도 기반 soft filtering만으로 두 번째 요인이 영구적으로 배제되는 attracting state'라는 가설은 이 family에서 반박된다. 전체 (w1,0)은 w1 방향 drift가 있어 stationary saddle라고 부르지 않는다. 정확히는 invariant boundary의 transverse repulsion이다. 시간 지연은 가능하지만 floor에 따른 finite bound가 있다. 일반 nonlinear SSL에서 feature suppression이 없다는 결론은 아니다. 특히 augmentation이 두 factor를 다르게 바꾸거나 norm·regularizer의 competition이 있으면 다른 objective와 feasible directions를 분석해야 한다.

## Proposition 4. importance correction은 uniform population update를 정확히 복구한다
고정 marginal p(y)=1/4와 full support q_w에 대해 negatives iidK개이면, sampler와 importance weight를 모두 detached로 두고

E_(y1:K~q_w^K) [(product_j p(yj)/q_w(yj|x)) ∇ell_w(x,y1:K)] = E_(y1:K~p^K) ∇ell_w(x,y1:K).

증명: 각 tuple의 q product와 denominator가 취소되어 p product만 남는다. QED. 따라서 아래 normalized 현상은 동일 uniform population objective의 sampling-only optimizer failure가 아니다. q로 실제 reweighting한 decoupled field의 현상이다. p/q 미분까지 포함하면 다른 알고리즘이다. code/importance_control.py는90 설정을 exact enumeration하여 최대오차1.39e-15를 얻었다.

## Proposition 5. normalized square의 matched-frozen 안정성과 adaptive 불안정성

이 명제는 critic /root/negative_feedback_critic의 독립 유도·검산과 일치한다. 4-state lookup representation F=(f_i)에서 f_i in S^(d-1), d>=3를 허용한다. 이는 additive2차원 제한보다 넓고, 네 state를 모두구별하는 simplex도 표현가능하다. Positive는 identity. K1 InfoNCE, q_ij=epsilon/4+c softmax_j(kappa f_i^T f_j), c=1-epsilon. 점 f_i*=(a_i,b_i,0,...)/sqrt2(square)를 고려한다. q*를 고정한 update와 매step q(F)를 갱신한 detached update를 비교한다. Sphere projected gradient flow 사용.

기호: Z=2+2cosh(kappa), alpha=1/Z, v=epsilon/4+c alpha(adjacent q), w=epsilon/4+c exp(-kappa)/Z(opposite q), r=sigmoid(-1), r'=r(1-r), s=sigmoid(-2).

Square는 두 vector field의 stationary point이다. 다음은 loss/gradient-field linearization DG의 eigenvalues이며 실제 flow Jacobian은 부호를 뒤집는다. Rotation zero modes를 제외한다.

| tangent mode | frozen q* DG | adaptive DG |
|---|---|---|
| in-plane ab (factor balance), multiplicity1 | 2v r' | 2[v r'+c kappa alpha r] |
| in-plane a,b, multiplicity2 | v r'+w s | v r'+w s+c kappa alpha r(1-alpha) |
| normal 1, 각 extra ambient coordinate | v r+w s | 같음 |
| normal ab, 각 extra ambient coordinate | w s-v r | 같음 |
| global rotations | 0 | 0 |

따라서 frozen square는 w s>v r이면 rotation을 제외하고 strict stable이다. 동시에 v r'+c kappa alpha r<0이면 adaptive는 factor-balance 방향 unstable이다. epsilon=.1,kappa=-2에서 두 부등식이 동시에 성립하며 충분 표현 차원에서도 matched-frozen stable point가 adaptive 갱신 때문에 불안정해지는 exact counterexample를 제공한다. 이는 '모든 negative 확률이 양수'만으로 feedback safety를 보장할 수 없다는 수정된 명제다.

### 유도와 증명
1. square에서 scores는 self1, adjacent0, opposite-1, 그리고모든 anchor의 softmax normalizer는 Z로같다. 양옆 vector가대칭이라 sphere-projected frozen/adaptive gradient가0이다.
2. 각 point의 in-plane unit tangent e_i=(-b_i,a_i,0)/sqrt2를 잡고 변위 t_i e_i를 쓴다. 네 scalar t_i는 group Fourier basis1,a,b,ab로분해된다. Neighbor pair score의 1차 변화는 h_ij(t_i-t_j), h_ij=sin(phi_j-phi_i)=±1; opposite pair의1차변화는0,2차는(t_i-t_j)^2/2. Frozen Hessian은 neighbor weight v r'/2, opposite weight w s/2의 graph Laplacian. Fourier characters를 적용하면 ab는2v r', a,b는v r'+w s, 1은rotation0이 된다.
3. Adaptive feedback은 delta q_ij=c kappa softq_ij [delta s_ij-m_i], m_i=sum_j softq_ij delta s_ij. Per-point gradient에 q_ij+q_ji가 들어가므로 추가 linear term은 (c kappa/4)sum_neighbor alpha[2delta s_ij-m_i-m_j]r h_ij. ab mode는 m_i=0여서2c kappa alpha r를 추가. a,b mode는 행 normalizer 변화까지 합쳐c kappa alpha r(1-alpha)를 추가한다. 이것이 목적함수를 고정했을 때의 curvature와 구별되는 sampler response이다.
4. 각 normal coordinate에서 perturbation n_i는 basis1,a,b,ab로분해된다. Score의1차변화가0이라 delta q=0. 2차변화는 n_i n_j-s_ij(n_i²+n_j²)/2이다. 직접합하면 eigenvalues v r+w s,0,0,w s-v r. 중간0 둘은 평면을 회전하는 global rotations이다. d-2개의 normal coordinate마다 반복된다. 전역 in-plane rotation 하나를 더하면총2d-3 rotation modes. 다른 mode는 위표로소진된다.
5. 두 부등식에서 frozen의 nonzero eigenvalues는양수이고 adaptive factor-balance eigenvalue는음수다. flow Jacobian=-DG이므로 stability 진술이따른다. QED.

Scalar tied theta의 f_theta=(cos theta*a,sin theta*b)에서 구한 curvature는 위 eigenvalue의4배다. 네 point를 하나의 theta로 묶었을 때 parameter metric norm²가4이기 때문이며 수치불일치가아니다.

### K>1
네 negative category count n~Multinomial(K;q*)를 exact enumerate한다. theta*=pi/4에서 D=1+n_self+exp(-1)(n_adj1+n_adj2)+exp(-2)n_opp, d=n_adj2-n_adj1라 두면

H_frozen=E[4exp(-1)(n_adj1+n_adj2)/D-4exp(-2)d²/D²],
H_adaptive=H_frozen+4c kappa alpha exp(-1)/v * E[d²/D].

증명은 log denominator를 theta미분한 frozen 항과 multinomial logprob derivative=2c kappa alpha*d/v를 곱한 feedback 항을 더한것이다. code/multiple_negatives.py가 finite enumeration과 별도 FD로확인한다. K1,2,4,8,16에서epsilon.1,kappa-2의 H_adaptive는전부음수이고 frozen전부양수다. K2/4 full sphere의 나머지 tangent 안정성은 critic이 독립수치검산했고, 모든K full-spectrum analytic theorem은아직없다.

## 주장 범위
- full sphere K1의 stationary-point stability와 existence region은직접증명.
- K2/4 full tangent와 K<=16 scalar mode는 exact expectation의 수치확인 및 analytic moment formula로지지.
- finite time에 amplitude가작아졌다고 MI=0은아님. 수치run은 noisy readout 접근성 저하를측정하며 exact factor loss는 attracting boundary의극한에대한말이다.
- generic DG=H_frozen+feedback의분해는 performative prediction chain rule로새롭지않다. 기여후보는 SSL의 full-capacity sphere와 floor 아래 explicit factor-selective spectrum/phase boundary다. 실질적중요성및문헌상의독창성은별도검증대상.
