# 독립 이론 검토

아래는 직접 증명이며, 수학적 신규성을 주장하지 않는다. 문헌의 주장을 무비판적으로 재사용하지 않기 위한 검산이다.

## 1. 비영 linear BYOL equilibrium은 출력 gauge를 quotient하지 않으면 개별점 점근안정일 수 없다

encoder A, predictor B, teacher C의 population field를 V라 하자. 모든 출력 orthogonal Q에 대해 T_Q(A,B,C)=(QA,QBQᵀ,QC)로 두면 squared-loss BYOL, Frobenius decay, EMA는 V(T_Q z)=T_Q V(z)를 만족한다. 각 식에 대입하면 확인된다. 따라서 V(z*)=0이면 모든 T_Q z*도 equilibrium이다.

A*≠0이고 출력 차원이 적어도2이면 일반적으로 nontrivial smooth orbit가 존재한다. Q(t)=exp(tΩ), Ω skew-symmetric에서 dT_Qz*/dt|0≠0인 Ω를 고를 수 있다. 같은 orbit의 이웃 equilibrium은 z*로 수렴하지 않으므로 z*는 **개별점으로서** asymptotically stable일 수 없다. 미분하면 DV(z*)·(ΩA*,ΩB*−B*Ω,ΩC*)=0이므로 zero mode도 강제된다. 이것은 데이터가 generic해져도 없어지지 않는 구조적 대칭이다. □

따라서 Ponce et al. arxiv2507.01028v3 Prop4.10의 개별점 안정성 문구는 이 연구의 확정된 외부 근거로 사용하지 않는다. 해당 논문 Eq46–49 proof에서 zero mode를 nongeneric으로 취급하는 단계는 이 대칭을 처리하지 못한다. orbit의 Lyapunov 안정성이나 quotient에서의 normal attraction은 별도 질문이며 위 반론으로 부정되지 않는다. 해당 논문의 다른 정리까지 오류라고 주장하지 않는다.

## 2. 작은 신호만으로 큰 회복시간이 생긴다

Tian2021 linear flow의 no-decay, SG, balanced scalar 특수화는 dot s=s²(rho−s)다. 0<s0<b<rho이면 도달시간은

`T(s0→b)=F(b)−F(s0), F(s)=rho^(−2)log[s/(rho−s)]−1/(rho s)`.

증명: F′(s)=1/[s²(rho−s)]이므로 separation of variables를 적용한다. s0→0에서 T=1/(rho s0)+O(|log s0|)이다. □

이 결과는 이미 기존 flow의 직접 적분이므로 새로운 learning principle이 아니다. 매우 느린 회복, head reset의 효과, 유한시간 threshold 미도달만으로 비가역적 정보 소실이나 새로운 memory lock을 주장할 수 없다는 대조군이다.

## 3. equal-spectrum normalized SSL은 factor allocation을 구별하지 못한다

X는 uniform independent 3bits, Y의 j번째 bit는 E[Yj|X]=rho_j Xj를 만족한다. Walsh basis χ_S(x)=prod_(j∈S)xj에서 conditional-expectation operator K는 Kχ_S=(prod_(j∈S)rho_j)χ_S다. 이는 conditional bit independence로 바로 따른다.

모든 rho_j=rho∈(0,1)이면 odd/zero-mean vector functions에서 ||Kf||_(L2)≤rho||f||_(L2). odd unit representation f와 odd unit predictor output g에 Cauchy–Schwarz를 적용하면 E[g(X)·f(Y)]≤rho. 따라서 cosine regression loss 2−2E[g·f]의 하한은 2−2rho다.

임의 v∈R³, ||v||=1에 f_v(x)=diag(v)x를 두면 모든 row가 unit, Kf_v=rho f_v다. teacher=f_v, predictor=I이면 g=f_v이므로 하한을 달성한다. 또한 anchor별 student gradient는 (I−ffᵀ)Kf=0이고 predictor gradient도0이다. v3=0인 rank2와 v3≠0인 fullrank가 모두 최적·stationary이므로 이 clean objective는 세 factor를 전부 학습해야 할 이유를 주지 않는다. □

이것은 실제 nonlinear encoder의 모든 attractor를 완전히 설명하는 정리가 아니다. 그러나 동등 clean correlation에서 회복이 없다는 실험은 이 spectral degeneracy라는 강한 대체 설명을 배제하지 못한다.

## 4. 약한 mode의 국소 안정성은 teacher 신호와 predictor scale에 좌우된다

f_a=(sqrt((1−a²)/2)x1,sqrt((1−a²)/2)x2,a x3), teacher=f_b를 사용하고 rho1=rho2=rho0라 하자. Predictor=I이면 expected loss는

`L(a,b)=2−2[rho0 sqrt(1−a²)sqrt(1−b²)+rho3 ab]`.

teacher branch를 고정한 student gradient descent와 dot b=beta(a−b)의 a=b=0 선형화는

`J=[[-2rho0,2rho3],[beta,−beta]]`.

trace<0, determinant=2beta(rho0−rho3)이므로 rho3<rho0에서는 수축, rho3=rho0에서는 zero mode, rho3>rho0에서는 불안정 증가가 있다. EMA는 이 모형에서 부호의 경계를 바꾸지 않는다.

unused output predictor scale이 p>0이면 normalized prediction의 norm은 sqrt[1+(p²−1)a²]다. 같은 계산에서

`J_p=[[-2rho0 p²,2rho3 p],[beta,−beta]]`.

따라서 threshold는 rho3>rho0 p다. predictor는 새 factor가 정확히0이면 해당 scale을 학습할 신호를 받지 않는다. Head reset 효과만으로 새로운 메커니즘이라 부를 수 없는 이유다. 이 작은 모형을 주담당의 nonlinear checkpoint 전체에 대한 검증된 설명으로 확장하려면 실제 tangent/gradient가 위 예측과 맞는지 별도 검증해야 한다. □

## 5. InfoNCE 대조에는 factor 재획득의 목적함수 구동력이 있다

f_v(x)=diag(v)x, ||v||=1, w_j=v_j², temperature tau로 두자. Uniform negative X′의 bits가 독립이므로 E_exp=prod_j cosh(w_j/tau)다. 따라서 infinite-negative population objective는

`L(w)=−sum_j rho_j w_j/tau+sum_j log cosh(w_j/tau), w_j≥0, sum_jw_j=1`.

Hessian은 diag(sech²(w_j/tau)/tau²)>0이므로 simplex에서 유일한 최소해를 갖는다. equal rho에서는 permutation symmetry로 w=(1/3,1/3,1/3)이다. rho=(.9,.9,0), tau1에서는 w=(.5,.5,0)의 active gradient=tanh(.5)−.9<0, inactive gradient0이므로 KKT를 만족하고 유일한 최적해다. □

즉 이번 generator에서 deficit 후 clean으로 바꾸면 InfoNCE는 세 번째 factor를 선호하지만 normalized agreement는 allocation에 무관한 optimum family를 갖는다. 학습기 전체를 바꾸는 대조이므로 'teacher 상태만이 원인'을 증명하지 않는다. 선택압의 차이라는 더 단순한 경쟁 설명을 실제로 시험하는 수단이다. 위 식도 표준 independent-negative expectation의 직접 계산이며 새 논문 기여로 세지 않는다.
