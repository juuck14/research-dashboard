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
