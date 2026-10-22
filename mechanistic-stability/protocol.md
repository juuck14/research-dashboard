# 실행 전 설계와 판정 기준

작성: 2026-10-22 UTC. 현재는 문헌·기호 분석을 했으며 아래 수치 계산은 아직 실행하지 않았다.

## 원래 질문과 이번 검증의 범위

원래 질문은 exact mechanistic factorization의 작은 C¹ 오지정 아래 모든 관측 동치 decoder의 factor 의미가 안정적인가이다. 후보2의 여러 하위 경로를 동시에 해결하지 않는다. 이번에는 MI Type S의 sparsity gap가 robustness에 충분한지, 추가 정량 margin이 무엇을 측정해야 하는지 검증한다. Gaussian independence/AJD 예제는 이미 다른 회차에서 기각되었으므로 새 결과로 재사용하지 않는다.

## 관측·숨은 대상·동치류

- 관측: 고정된 여섯 observation coordinates의 두 차원 immersed manifold와 그 위 분포. 모집단에서는 선형 embedding A의 column space 및 분포를 완전히 알 수 있다고 허용한다.
- 숨은 대상: 두 scalar latent axes. 잠재 밀도는 알려지지 않고 dependent해도 된다. 관측적으로 동치인 generator A와 AR는 latent density를 pushforward하여 정확히 같은 law를 만든다.
- 같은 해: 축 순열과 좌표별 가역 재매개화. 비교는 정규화된 선형 부분족에서 signed permutation quotient angle로 한다. 일반 GL와 nonlinear 대안은 더 넓으므로 이 부분족의 반례는 lower bound로 유효하다. 이것을 전체 exact identified set로 부르지 않는다.
- 허용 reference generator: Type S exact sparsity 최소화가 true basis에서만 성립하는 full-column-rank 6×2 constant Jacobian. 양의 weak-anchor amplitude κ를 사용한다.
- 오지정: compact latent unit disk에서 generator와 first derivative의 uniform norm. 기준 생성기·candidate 모두 observation 좌표는 동일하다. latent/observation rescaling으로 δ를 작게 만드는 가짜 반례를 배제하기 위해 두 큰 singular values를 명시한다.

## 가설과 가장 강한 반박

H0: integer ℓ0 gap와 inverse conditioning만 고정하면 δ→0일 때 factor-axis ambiguity가 0으로 간다.

H1: 정확 Type S gap는 weak nonzero coefficient의 크기를 제어하지 않는다. uniformly conditioned family에서 weak anchors를 0으로 보내면 finite angle ambiguity가 O(κ) C¹ 오지정에 이미 허용된다. H0를 직접 반박한다.

H2(추가): 명시된 normalized orthogonal candidate family에서 strong anchors와 leakage budget의 비가 각도 해상도를 정한다. 이는 sparse dictionary/subspace robustness의 표준 따름정리일 수 있으며, 선행연구를 넘지 못하면 독립 연구로 권하지 않는다.

## 수치 실행 A: exact algebra audit

Aκ의 앞 네 row는 e1,e2,(e1+e2)/√2,(e1−e2)/√2, 뒤 두 row는 κe1,κe2다. κ grid=[1,.3,.1,.03,.01,.003,.001], rotation θ=π/4. 별도 확인에서는 RNG seed 20261023로 κ log-uniform 및 θ∈[.15,π/4] 40개를 쓴다.

계산: singular values, exact/thresholded ℓ0 count across candidate row-annihilator basis(2D global optimum를 완전 열거), reconstruct observation law equality, alternative decoder의 exact-TypeS reference와 C¹ distance, signed-permutation quotient transition angle. 행렬 identity 잔차 목표 ≤1e−12.

순위가 다른 모형이나 데이터량 비교를 하지 않는다. 이 단계는 최적화·유한 표본 문제가 아닌 모집단 observational equivalence 계산이다.

## 수치 실행 B: nonlinear/measurement controls

단순 선형 표준 결과에만 머물지 않는지 확인하기 위해 좌표별 bounded smooth nonlinear reparameterization를 양쪽 exact reference에 동일하게 적용할 수 있는지 이론적으로 먼저 점검한다. C⁰ 재구성 오차가 Jacobian 오차를 통제하지 않는 표준 high-frequency 예제를 별도로 계산한다. 이 예제를 새 기여로 세지 않는다.

## 결정 기준

- 진행 권고: 같은 질문의 중요한 새 정량 명제와 기존 sparse coding robustness로 환원되지 않는 새 결론을 확보하고 독립 검토를 통과할 때.
- 수정 후 진행: 원가설은 반박되었으나 비선형·관측 가능한 quantitative margin의 새 결과가 실질적으로 지지될 때.
- 기각: 확보한 주요 증거가 integer gap의 불연속성, 표준 dictionary perturbation, 또는 C⁰/C¹ 차이라는 알려진 원리의 작은 예제에 그치면 현재 구체화를 독립 주제로 권하지 않는다.
- 보류: 원래 비선형 all-candidate 안정성 질문의 핵심 정리/반례를 결정하지 못하고 실행 환경상 해결 불가인 경우, 넓은 질문은 미해결로 남긴다. 작은 하위문제의 기각을 전체 질문 기각으로 확대하지 않는다.

새 실험이나 설계 변경은 이 문서에 amendment로 먼저 추가한다. 원하는 결과에 맞춘 grid 이동은 하지 않는다.

## Amendment 1 — 실행 전 수학적 가정 점검

아직 계산을 실행하지 않았다. generic θ에서는 회전된 앞 네 row 방향이 e1/e2와 일치하지 않아 Bκ의 true basis가 unique sparsity minimizer라는 보장이 사라진다. 따라서 confirmation은 θ=π/4를 고정하고 κ와 강한 row들의 비영 크기만 독립 변화한다. θ를 넓히는 별도 이론 확장은 2m개 등간격 projective directions와 θ=π/(2m)를 쓰는 유한 대칭으로만 허용한다. 이는 불리한 결과를 제외한 것이 아니라 실행 전 family-membership 오류를 제거한 것이다. 원래 generic θ 설계는 위에 보존한다.

## Amendment 2 — 실행 전 nonlinear control 구체화

F(x)_j=x_j+.1x_j³를 같은 observation coordinates에서 적용한다. 양의 대각 Jacobian은 row support를 보존하므로 F(Aκs)와 F(Bκz)는 여전히 exact TypeS reference다. 관측 동치 후보 F(AκRz)와 F(Bκz)의 C¹ 거리는 unit disk에서 κ(1+.9κ²)||R−I|| 이하라는 직접 bound를 검산한다. 이는 새로운 nonlinear ICA theorem이라는 주장이 아니며 constant-Jacobian만의 artifact인지 구분하기 위한 조건외 확인이다. 재구성 동치 sample은 dependent, nonGaussian latent s=(tanh(U),tanh(.6U+.8V))/√2로 생성하여 ICA independence를 가정하지 않는다. primary seed20261022, confirmation seed20261023를 고정한다.

## Amendment 3 — 앞의 반례 이후 실제 surrogate와 연결

실행 A/B에서 반례를 확인했다. 더 많은 회복 실험 대신 MI §5의 실제 compositional contrast를 같은 관측 동치·동일 norm인 AκRθ family에 대입한다. 실행 전 분석은 Fκ(θ)=(1+κ²)|sin2θ|+|cos2θ|를 예측한다. 따라서 θ=0과45° 모두 이 제한족에서 strict local minimum이고 gap=κ², barrier=maxθFκ(θ)−1=√((1+κ²)²+1)−1이다. κ grid는 동일하다. θ∈[0,π/4] 10001-point grid와 행렬 직접 계산을 비교하고, reflection/signed permutation quotient 처리한다. 이 결과는 full GL/nonlinear optimizer의 stationary point 정리가 아니며 실제 SGD를 실행했다는 주장도 아니다. 원문이 bad local minima를 이미 보고한 점을 최종 신규성 판단에 반영한다.

## Amendment 4 — 반례가 막지 않는 명시적 positive bound

반례가 integer gap만으로 충분하지 않다는 것을 보였지만 원보고서의 continuous margin κ 가설을 반박하지는 않았다. 따라서 강화한 부분족을 별도로 검증한다. m=2p+q rows, p>q; 각 scalar true axis에 p개 pure rows가 있고 amplitude≥a, q개 mixed rows도 row norm≥a. learned exact reference의 total ℓ0≤m+q를 요구한다. 두 actual decoder가 각각 자기 exact reference의 C¹δ 근방이고 h=ĝ⁻¹g의 Jacobian norm≤L이다. η=δ(1+L)<a/√2이면 모든 admissible h는 전역 동일 permutation에서 off-block derivative≤Lη/a를 만족할 것이라는 직접 증명을 시도한다. 이는 원가정의 단순 재표현이 아니라 quantitative anchor·row-norm·overlap·learned sparsity·chart conditioning의 **추가 가정**이다.

작은 nonlinear 계산: p=2,q=1, s,t∈[−.6,.6]. g0=(s+.1s³,1.2s+.05s³,t+.07t³,.9t+.1t³,s+t+.1st). hβ=(s+βsin t,t+βsin s), actual ĝ=g0∘hβ⁻¹, reference ĝ0=g0 on hβ(domain). β=[.001,.003,.01,.03,.05], a=.9,L=1+β. analytic C¹ allowance δ=3β/(1−β)+√2β (g0 norm≤3, derivative Lipschitz≤1 on enlarged domain). 同law reconstruction 및 derivatives를 grid로 확인하고 predicted off-block bound와 C⁰ block approximation을 검산한다. 확인 grid는 primary61×61, confirmation 독립 seed20261024의1024 random points. optimizer/finite-sample 실험으로 부르지 않는다.

별도 norm 점검: off-block derivative가 작다는 사실만으로 global C¹ distance to block function가 같은 선형률로 작아지는지 확인한다. 이것을 원래 decoder-C¹ leakage 주장 전체의 반례로 확대하지 않는다. 실제 theorem이 증명하는 norm을 최종 문서에서 명시한다.

## Amendment 5 — fixed true generator에서 후보 complexity의 필요성

앞 반례는 κ가 줄어드는 family였고 fixed g0의 pointwise stability는 반박하지 않았다. positive proof의 all-row norm 가정을 점검하면서 zero observation rows가 허용될 때 candidate reference가 작은 새 support를 추가하여 sparsity ranking을 바꿀 수 있다는 별도 반례를 발견했다. 실행 전 family를 기록한다: A=[Aκ=1;0_(4×2)] 고정, R=45°, actual C=AR, exact reference Bε=[A1R;εI;εI]. ε=[.1,.03,.01,.003,.001,1e−4,1e−6]. 예측 true minℓ0=8/nonaligned9, Bε min14/nonaligned15, singular values √3와√(3+2ε²), C¹ distance√2ε. 동일한 row-annihilator 전역 열거 및 independent weighted strong-row confirmation20조건(seed20261025)을 시행한다. 이 경우 후보 reference의 전체 sparsity가 true보다 크고 일부 weak witness가 ε로 줄어든다는 점이 핵심이다. 알려진 sparsity budget이나 candidate-side quantitative margin이 고정된 class의 반례로 쓰지 않는다.

## Amendment 6 — weak witnesses 이외의 surrogate preference

명제3은 local-minimum 문제였으므로 objective 자체의 순위와 구별한다. Aκ의 diagonal± 두 row만 w배 scaling하여 강도를 바꾼다. 실행 전 예측은 `Ccomp(θ)=(1+κ²)|sin2θ|+w²|cos2θ|`, `AᵀA=(1+w²+κ²)I`, TypeS min8/nonaligned9다. κ=1,w=2에서는 witness amplitude·condition이 고정되어도 trueaxis4,45°axis2일 것이다. grid κ=[.3,1,2], w=[.5,1,2,3], θ10001points를 계산한다. 같은 observation coordinates와 Jacobian metric을 유지하므로 latent/observation 차원·norm 차이는 원인이 아니다. 단 observation row-weighting이 structural ℓ0와 smooth weighted surrogate를 다르게 변화시키는 것이 원인이다. 이 결과는 저자들이 general Ccomp guarantee를 증명했다는 주장이나 전체 nonlinear 학습 실패 확률로 쓰지 않는다.

## Amendment 7 — 검토자가 제시한 overlap 대안 설명 검증

독립 검토자는 앞6row 예가 support overlap50%라는 반론을 제기하고 p=3 pure rows/axis +2 mixed diagonals,w=2를 제안했다. 실행 전 예측은 TypeS min10/nonalign12, overlap40%, Gram7I, trueCcomp4/wrong45°Ccomp3이다. p=[3,4,6], w=[1,2,3]9조건을 검산한다. p>q2와 모든 row amplitude floor를 갖는 family에서도 smooth surrogate가 learned ℓ0 budget를 보장하지 않는지를 직접 구분한다. 이는 실험 후 유리한 조건만 선별하는 것이 아니라 명시된 대안 설명을 새 사전조건에서 시험하는 추가 검증이다.
