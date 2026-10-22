# 직접 도출한 반례·계산과 증명의 범위

상태: 아래 명제1–4는 완전 증명. 수치는 별도 results.md에 있다. 새 문헌 결과라는 뜻은 아니다. 명제5는 [별도 positive proof](positive_bound.md)에 있다.

## 정식화

observation coordinates와 그 Euclidean metric을 고정한다. 잠재 두 scalar의 순열·각 좌표별 가역 함수는 같은 의미로 취급하고 일반 회전은 다른 의미로 취급한다. 선형 embedding에서 target은 observation tangent plane 안의 unordered factor line pair다. 이 target은 scalar reparameterization와 부호에 불변이다.

Type S는 Dg의 ℓ0를 최소화하는 basis가 true scalar axes에 정렬된 basis에 한정된다는 exact 조건이다. 두 scalar에서는 각 Jacobian row의 projective direction과 그 multiplicity로 전역 최소를 정확히 계산할 수 있다. C¹ norm은 unit disk에서 `max(sup||f||2,sup||Df||op)`로 둔다.

approximate class Mδ는 각각 어떤 exact-TypeS reference g0의 C¹δ 근방에 있는 actual generator g로 이루어진다. reference의 image가 actual image와 같다는 가정은 하지 않는다. 이것은 일반적인 `g=g0+δr` leakage class다. 밀도는 알려지지 않고 dependent해도 되며 actual candidate는 latent 밀도를 pushforward하여 같은 observation law를 만들어야 한다. learned reference의 support/cardinality를 제한하지 않은 class와, 아래 positive theorem의 제한 class를 구별한다.

## 명제1 — 정수 sparsity gap는 uniform stability modulus를 주지 않는다

`Aκ=[e1;e2;(e1+e2)/√2;(e1−e2)/√2;κe1;κe2]`, `R=Rπ/4`, `Bκ=[A0R;κI]`라 하자. 여기서 A0는 Aκ의 앞 네 row다. 모든 κ>0에서 Aκ와 Bκ 모두 true scalar basis에 대한 Type S를 만족하고,

`ρ+=8`, `ρ−=9`, `AκᵀAκ=BκᵀBκ=(2+κ²)I`.

**증명.** Aκ의 row projective directions는 e1,e2가 multiplicity2, 대각 두 방향이 multiplicity1이다. 임의 nonzero basis column은 한 projective direction의 row들만 annihilate할 수 있다. invertible basis의 두 column은 서로 다른 row directions를 annihilate한다. 두 multiplicity의 최대 합은4이며 e1,e2에서만 달성한다. 따라서12개 entries 중 최소 nonzeros8은 generalized permutation basis에서만 나오고, 비정렬 최소는2+1개의 zero를 이용한9다. Bκ에서도45° 회전이 앞 네 directions를 순열하므로 동일하다. Gram identity는 직접 곱하면 얻는다. ∎

actual generator `gκ(s)=Aκs`와 candidate `ĝκ(z)=AκRz`는 `z=Rᵀs`로 정확히 같은 observations와 법칙을 만든다. 그러나 candidate는 다른 exact reference `gbarκ(z)=Bκz`의 근방이며

`||ĝκ−gbarκ||C1 = κ||R−I||op = κ√(2−√2) →0`.

factor line pairs는45° 떨어져 있다. κ→0에서 inverse conditioning, 모든 C² bounds, integer sparsity gap는 균일하지만 구조 의미는 uniform하게 안정적이지 않다. **fixed κ>0의 한 g0 주위 pointwise stability를 이 명제만으로 반박하지 않는다.**

이는 원보고서의 새로운 continuous margin κ가 존재한다는 가설을 반박한 것도 아니다. 오히려 그 margin이 integer ℓ0 gap와 singular-value conditioning 이외의 witness amplitude/diversity를 포함해야 한다는 필요조건이다.

## 명제2 — smooth nonlinear observation map에서도 반례가 유지된다

고정된 coordinate-wise map `F(x)_j=x_j+.1x_j³`를 gκ,ĝκ,gbarκ에 적용한다. F의 Jacobian은 양의 대각행렬이라 row support와 ℓ0 basis optimum가 변하지 않는다. C1 distance는 κ≤1,||z||≤1에서

`||F∘ĝκ−F∘gbarκ||C1 ≤ κ(1+.9κ²)||R−I||op`.

**증명.** 차이는 마지막 두 coordinates에만 있으며 `F(κRz)−F(κz)`다. cubic의 derivative Lipschitz bound와 |z_i|≤1를 사용하면 C0는 κ(1+.3κ²)||R−I||, derivative는 κ(1+.9κ²)||R−I|| 이하이다. F'≥1이라 min singular bound는 악화되지 않으며 F'≤1.3이라 max singular도 균일하게 bounded다. ∎

이 확장은 constant Jacobian만의 artifact가 아님을 보이지만, observation-wise reparameterization로 얻은 구조 보존 확장이다. genuinely nonlinear latent transition의 새로운 식별성 정리라는 기여로 세지 않는다.

## 명제3 — 같은 reconstruction에서 surrogate preference와 구조 의미는 다른 문제다

정규화된 orthogonal candidate family `gθ(z)=AκRθz`에서 MI compositional contrast를 계산하면

`Ccomp(θ)=(1+κ²)|sin2θ|+|cos2θ|`.

θ=0과θ=π/4는 이 rotation family 안에서 모두 strict local minimum이며 loss gap는κ², θ=0에서 출발한 barrier는 `√((1+κ²)²+1)−1`이다. κ→0에서 gap는0으로 가지만 barrier는√2−1로 간다.

**증명.** 첫 두 row의 absolute column product 합은 |sin2θ|, 대각 두 row의 합은 |cos2θ|, 뒤 두 weak row의 합은κ²|sin2θ|다. [0,π/4] 내부에서 Ccomp=(1+κ²)sin2θ+cos2θ이며 endpoint one-sided slope와 최대값을 계산하면 된다. ∎

이것은 population objective의 선택과 local optimization barrier를 분리한 정확한 계산이다. `Ccomp−min≤ε`인 **이 제한 family**는 ε≥κ²일 때45° 대안을 포함한다. full GL이나 nonlinear decoder class의 global near-optimum 정리가 아니다. MI 논문 자체가 bad local minima를 보고하므로 현상 서사 자체는 새 기여가 아니다.

### 명제3b — strong margin과 낮은 overlap도 surrogate 일관성을 보장하지 않는다

더 나아가 A의 observation rows를 e1 p개, e2 p개, `w(e1+e2)/√2`, `w(e1−e2)/√2`로 둔다(p≥3). 이 때

`ρ+=2p+4`, `ρ−=3p+3`, `AᵀA=(p+w²)I`,
`Ccomp(θ)=p|sin2θ|+w²|cos2θ|`.

row-direction multiplicity와 앞의 absolute product 합산이 완전 증명이다. p=3,w=2이면 모든 row norm≥1, TypeS gap2, support overlap40%이고 condition number1이다. 그런데 true axis의 contrast4보다45°의 contrast3이 엄격히 작다. wrong candidate의 ℓ0=14는 true sparsity budget10을 넘는다.

따라서 `low overlap + strong true witness + small Ccomp`만으로 positive theorem의 learned ℓ0 budget를 보장할 수 없다. 두 chart의 reconstruction과 Jacobian Gram7I는 같으므로 norm·capacity·data 차이 때문이 아니다. 같은 Gram을 고정한 **aligned** component-wise chart는 scalar derivative의 절댓값이1이어야 하므로 같은 contrast4를 가진다. 허용 full class에 wrong chart가 들어 있으면 aligned chart가 그 class의 global optimum가 될 수 없다는 candidate comparison이기도 하다. 모든 nonlinear optimizer의 attractor나 오류확률을 구한 결과는 아니다.

이 예시는 저자들의 exact-TypeS 정리와 모순되지 않는다. wrong actual decoder는 exact-TypeS aligned reference가 아니고 surrogate가 exact sparse constraint를 실현하지 못하기 때문이다. 원문이 일반 surrogate guarantee를 증명했다고 오해하면 안 된다. ℓ0 구조와 weighted smooth relaxation이 다른 선호를 갖는다는 원리 자체는 알려진 것이어서, 이 정확 예시만으로 독립 논문을 권할 신규성은 확인되지 않았다.

## 명제4 — 후보 complexity를 제한하지 않으면 fixed true generator에서도 실패한다

`A=[A1;0_(4×2)]`를 고정한다. A1는 명제1의 κ=1 행렬이다. actual true g(s)=As, candidate ĝ(z)=ARz는 정확히 같은 observation law를 만든다. 다음 candidate reference를 둔다.

`Bε=[A1R;εI;εI]`.

모든 ε>0에서 Bε도 Type S이며

`true ρ+=8,ρ−=9; candidate-reference ρ+=14,ρ−=15`,
`AᵀA=3I`, `BεᵀBε=(3+2ε²)I`, `||AR−Bε||C1=√2ε→0`.

**증명.** A의 zero row는 아무 basis에서도0으로 남으므로 명제1의 true proof가 유지된다. Bε의 top directions e1,e2는 각각 multiplicity1, 대각들은 각각2이고, 마지막 네 row가 e1,e2의 multiplicity를 각2씩 추가한다. 따라서 최대 두 방향의 합6은 e1,e2에서만 나오고 비정렬 최대5다.20개 entries에서 min14/nonaligned15를 얻는다. 나머지 identities는 직접 곱한다. ∎

여기서는 g0 자체와 그 nonzero witness strength가 고정되어 있다. 후보 reference가 원래 constant였던 observation coordinates에 극소 amplitude의 새 support를 추가하여 ℓ0 ranking을 바꾼다. 그러므로 **true-side quantitative margin만 고정한 채 모든 reference support/cardinality를 허용하는 approximate-TypeS class**에서는 pointwise robustness도 없다. generalized permutation quotient의45° ambiguity는 모든 n에서 유지된다. 관측 law가 같은 두 target의 angular risk에 triangle inequality를 쓰면 임의 orientation estimator의 두 world 중 최대 expected error≥22.5°다.

이 명제는 zero observation coordinates와 true보다 큰 candidate-reference sparsity budget을 허용한다. 모든 row가 uniformly active이거나 learned reference의 sparsity budget가 true 이하인 class의 반례가 아니다. positive theorem은 정확히 이런 강화 가정으로 이 현상을 제외한다. 실제 sensor coordinate의 임의 추가가 물리적으로 허용되는지 또한 별도 모델 선택 문제다.

## 명제5 — positive 결과의 범위

[positive_bound.md](positive_bound.md)는 explicit anchor amplitude a, p>q diversity, 모든 row norm≥a, learned ℓ0 budget, C1 reconstruction relation, ||Dh||bound 아래 **모든** 관측 동치 nonlinear decoder에 대한 normalized off-block derivative와 global 동일 permutation, rectangle 위 C0 block approximation을 증명한다. 이는 true oracle Jacobian clustering 실험보다 강하지만, 강한 구조 전제에 의존한다. 일반 Type S 안정성, arbitrary near-optimal loss→C1 nearness, 다차원 block은 미해결이다.

## 검증 수준과 남은 논리

- 명제1/4의 same-law ambiguity는 모집단 정보의 한계다. 더 긴 학습·더 많은 데이터·다른 초기화로 해결되지 않는다.
- 명제3의 near-minimum gap는 지정된 surrogate와 candidate family의 성질이며 통계적 불가능성과 동일하지 않다.
- reconstruction C0는 derivative error를 보장하지 않는다. `sin(ωt)/ω`는 C0→0이나 derivative maximum=1인 표준 예다.
- 새로운 학술 기여 후보가 되려면 일반 Type S의 비자명한 continuous margin 또는 실제 loss/finite-data에서 정당화되는 feasible class가 필요하다. 이번 직접 증명들을 그 결과의 대용품으로 내세우지 않는다.
