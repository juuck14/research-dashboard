# 후보 2 독립 검토

검토자: mechanism_review. 기준일: 2026-10-22. 담당자 코드를 가져오지 않고 별도 구현을 실행했다. 실험 전 [protocol](protocol.md), [코드](independent_check.py), [48조건 원자료](results/checks.csv), [실행 요약](results/summary.json).

## 최신 판정 — 추가 positive bound와 fixed-base 반례 이후

**판정 보류: 제한된 안정성 정리와 강한 반례는 검증했으나, 원래의 넓은 논문급 정량 안정성 질문은 해결하지 못했다.** 아래 초기 판정 후 두 결과가 추가되어 평가를 갱신했다. §6–8에 증거·가정·남은 쟁점을 분리했다. 기존 ℓ0/conditioning만으로 주는 무조건 안정성은 기각되지만, 아직 정의되지 않은 모든 연속 margin 기반 안정성까지 반박한 것은 아니다.

## 초기 판정 — 추가 분석 이전 기록

**정수 ℓ0 gap와 inverse conditioning만으로 주어지는 균일 robustness 가설은 반박된다.** 담당자 반례는 성립한다. 그러나 이 반례만으로 수개월의 독립 논문 착수는 권하지 않는다. 지금 확보한 것은 support count가 amplitude margin을 담지 않는다는 명확한 예이며, 원래의 연속 정량 mechanism margin을 어떻게 정의하고 증명할지는 여전히 핵심 미해결 문제다.

현재 좁힌 구체화를 기각하거나, 새 정량 명제를 얻기 전 장기 착수를 보류하는 것이 타당하다. ‘모든 approximate mechanistic identification이 불가능하다’는 판정에는 동의하지 않는다.

## 1. 직접 원문 대조

### Matthes–Han–Shen, ICLR 2026

[공식](https://proceedings.iclr.cc/paper_files/paper/2026/hash/b287c2f8630583f5fac5dcf4f544c7c9-Abstract-Conference.html), [읽은 v2 원문](https://arxiv.org/html/2509.22196v2). §3.2–3.4, Thm3–5와 Appendix A.5를 확인했다. Type M에는 Eq6의 support-union/no-cancellation 조건이 따로 필요하다. Type S의 Eq7은 모든 비정렬 tangent basis에 대한 엄격한 ℓ0 gap이며, Thm4의 양쪽 decoder는 exact Type S여야 한다. 따라서 이번 approximate candidate가 exact theorem과 충돌한다는 해석은 잘못이다. 해당 원문은 Jacobian sparsest-basis 관점을 이미 명시한다. 이번 반례는 그 관점의 연속 robustness에 관한 제한을 보여줄 뿐이다.

추가로 Appendix B Example2의 5×2 linear generator에 대한 generalized-permutation 전역 surrogate minimizer 증명과, §5/AppD의 overlap 증가 시 bad-local-minimum 현상을 읽었다. 그러므로 linear surrogate의 비정렬 local minimum 자체를 새로운 일반 현상으로 주장할 수 없다.

### Buchholz–Schölkopf, ICML 2024

[공식](https://proceedings.mlr.press/v235/buchholz24a.html), [읽은 원문](https://arxiv.org/html/2503.15355v1). §2–4, 특히 §3의 brittle exact-identifiability 예와 Eq2를 확인했다. 본문은 exact 식별성이 오지정에 안정적이지 않을 수 있음을 이미 지적하며, mixing과 inverse의 derivative geometry를 통제한다. 복원 보장의 ICA 부분은 독립 비Gaussian latent를 가정한다. 이번 dependent-latent Type S 반례를 이 논문의 직접 따름정리로 만들지는 못했다. 다만 ‘exact가 곧 robust를 뜻하지 않는다’ 자체를 새 원리로 주장하는 것은 이 선행과 중복이다.

### Garfinkle–Hillar, IEEE TSP 2019

[저자 원문](https://redwood.berkeley.edu/wp-content/uploads/2019/12/garfinkle2019uniqueness.pdf), DOI 10.1109/TSP.2019.2935914. pp5885–5887의 Definition1, Theorem1–3 및 Eq5–8을 읽었다. 이 연구는 sparse dictionary의 모든 충분히 잘 맞는 대안을 상대하며, support diversity와 정량 conditioning에 의존하는 안정성을 준다. 이번 6×2 예를 그 정리에 직접 대입했다고 주장하지 않는다. dense diagonal rows를 codes로 보면 k=m인 행이 있어 해당 k<m 가정이 맞지 않는다. 그럼에도 새 positive theorem은 이 고전적인 all-candidate sparse robustness보다 무엇을 더 말하는지 밝혀야 한다.

## 2. 완전 증명으로 확인한 내용

단위 row 방향을 `e1,e2,d+,d−`로 쓰고 `d±=(1,±1)/sqrt(2)`라 하자. `Aκ`의 rows는 `e1,e2,d+,d−,κe1,κe2`다. κ>0이며 singular values는 모두 `sqrt(2+κ²)`이다. 따라서 true generator의 inverse가 불안정해지는 예가 아니다.

임의의 `U∈GL(2)`의 각 column은 하나의 비영 latent 방향이다. 그 column이 Aκ의 row를 0으로 만드는 것은 그 row와 직교할 때뿐이다. distinct projective row 방향의 multiplicities는 `2,2,1,1`이다. 서로 독립인 두 column이 만들 수 있는 zero 수는 최대4이며, 최대4는 e1/e2 축을 scaling/permutation한 basis에서만 된다. 그러므로

`min_U ||Aκ U||0 = 12−4 = 8`이고, 모든 비정렬 basis의 score는 적어도9다. 각 scalar factor는 irreducible이다. 이 증명은 회전만 훑는 수치실험보다 강한 GL(2) 전체 결과다.

`R=Rπ/4`, `Cκ=AκR`, `Bκ=[A0R;κI]`로 둔다. A0는 앞4rows다. R에 의해 앞4개의 projective row 방향 집합이 순열되므로 Bκ에도 같은 multiplicity 증명이 성립한다. 따라서 Bκ는 z축에 exact Type S이며, Cκ는 그 근방에 있다:

`||Cκ−Bκ||op = κ||R−I||op = κ sqrt(2−sqrt(2))`.

latent unit disk에서는 이 값이 `max(sup function norm,sup Jacobian op norm)`으로 정의한 C¹ 차이와 같다. 동시에 `Aκs=Cκ(Rᵀs)`가 모든 s에서 정확히 성립한다. 임의 latent law를 회전해 pushforward하면 관측법칙도 정확히 같다. 허용 동치를 scalar 재매개화/순열로 둘 때 45° 회전은 다른 해다. κ→0에서 오지정 거리는0으로 가지만 factor angle은45°로 남는다. 정수 gap은1 이상, inverse condition은1로 고정된다.

중요한 해석: **true Aκ와 candidate Cκ가 모두 exact Type S aligned라고 주장하지 않는다.** Cκ는 exact Bκ에 가까운 approximate model이다. 또한 가변 family κ→0를 사용하므로, 이미 고정한 well-separated g0 한 개의 pointwise stability를 반증한 것이 아니다. 새로운 연속 mechanism margin을 허용하면 이 반례가 그 margin을0으로 보낼 가능성이 높다.

## 3. 직접 실행 결과와 비선형 대조

실행 명령:

```bash
OPENBLAS_NUM_THREADS=1 python3 prevalidation-20261022/reviews/mechanism/independent_check.py
```

Python3.12.14, NumPy2.3.5. κ grid8개와 독립 seed813/997의40개 조건을 실행했다. confirmation은 strong row의 비영 크기와 κ를 바꾸며 support 구조는 고정한다. 별도의 무관한 데이터48개라는 뜻이 아니다.

| 확인 | 관측 |
|---|---:|
| A와 B의 최소ℓ0 / 비정렬 최소 | 모든48조건에서8 / 9 |
| ℓ0=8인 basis가 정렬된 경우뿐인지 | 모든 조건 일치 |
| δ/κ exact formula 최대오차 | 2.22e−16 |
| 관측 same-law pointwise identity 최대오차 | 4.44e−16 |
| confirmation 최소 singular value | 1.03479 |
| confirmation 최대 condition number | 1.44708 |

독립 nonlinear control은 담당자의 cubic map과 다른 `φi(t)=t+βi tanh(t)`, `βi∈[.1,.4]`를 사용했다. φ′는 [1,1.4] 안에 있으므로 Jacobian의 row support를 보존한다. φ″의 uniform bound와 mean value 정리로 compact unit disk에서 `||φ(Cκ·)−φ(Bκ·)||C1=O(κ)`이다. 단순한 ‘계산에서 작게 나왔다’를 전역 증명으로 삼지 않는다. 1000점씩 확인한 sampled C0/κ 최대1.05935, sampled Jacobian-op 차이/κ 최대1.07084, nonlinear identity 최대오차6.66e−16이었다. 이는 known rowwise sensor diffeomorphism로 lift한 것으로 새로운 nonlinear identification 이론이 아니다.

### 추가 surrogate 독립 검산

담당자의 rotation-family 계산을 읽은 뒤 protocol amendment1을 먼저 기록하고 [별도 코드](surrogate_audit.py)를 실행했다. 각 row의 두 derivative 절댓값 곱을 합하면 정확히

`Ccomp(AκRθ)=(1+κ²)|sin2θ|+|cos2θ|`

가 된다. e1/e2 rows와 weak anchors가 첫 항을, 두 diagonal rows가 둘째 항을 준다. θ=0과π/4의 값 차이는κ²지만 중간 barrier는 `sqrt((1+κ²)²+1)−1`로 남는다. 이는 objective의 약한 선호와 최적화 장벽을 분리하는 유용한 정확 계산이다. [8개 κ×10001각 검산](results/surrogate_audit.json)에서 직접 row 계산과 공식 차이는8.89e−16 이하였다. κ=10^-8에서는 부동소수점 `(1+κ²)−1`이0으로 반올림됐다. 그 관측을 exact gap0이라고 해석하지 않는다.

이 부분은 rotation 부분족의 정확 공식이며 GL(2) 전체 surrogate landscape나 실제 autoencoder 학습을 검증하지 않는다. 전역 GL TypeS ℓ0 증명과 혼합해서 읽으면 안 된다.

## 4. 여전히 강한 반론

1. **중요성:** 최근 exact 조건이 작은 dense leakage를 허용할 때 무엇을 보장하는지는 의미 있다. 하지만 weak nonzero가 사라지는 support instability의 예만으로 충분한 새 지식인지는 별개다.
2. **신규성:** 현재 반례의 핵심은 저차원 matrix sparsification이다. nonlinear lift는 지식의 폭을 크게 넓히지 않는다. 위 sparse dictionary 원문과 정확히 같은 정리는 못 찾았으나, 검색에서 못 찾은 것이 신규성 증거는 아니다.
3. **긍정적 정량 명제 부재:** 데이터에서 정당화할 수 있는 연속 margin, 그 margin이 유지되는 함수족, near-equivalent 모든 decoder의 회복오차 상계는 아직 없다. 이 항목을 남겨둔 채 ‘수정 후 진행’의 완성된 핵심 주장으로 세면 안 된다.
4. **범위:** 관측 단위와 latent gauge를 고정했다. arbitrary observation row normalization을 허용하면 weak anchors가 O(1)이 되어 이 perturbation metric 자체가 바뀐다. 실제 센서 단위를 어떻게 정할지는 후속 과제다.
5. **표본과 목적함수:** 이번 증거는 population admissibility다. 실제 SSL loss의 near-optimal set를 모두 특성화하지 않았다. exact law matching 대안이 있다는 점은 강하지만, 특정 학습법이 그 대안을 선택한다는 주장은 하지 않는다.

## 5. 재개 조건

새로운 연속 mechanism margin을 단순한 ‘허용 모든 나쁜 해까지 거리’라는 tautology로 정의하지 않고, generator의 미분/관측 설계에서 구체적으로 계산해야 한다. 그 margin이 주는 상계와 불가능성 하계를 맞추거나, classical sparsest-basis perturbation과 다른 비선형 현상을 확보해야 한다. 이 결과가 없으면 대규모 학습 실험을 추가하는 것으로 현재의 신규성 약점을 해결하기 어렵다.

## 6. 추가된 positive anchor 정리의 독립 검토

담당자의 [positive_bound.md](../../../mechanistic-stability/positive_bound.md)를 읽고 검토했다. 실제 관계는 `A−CB`, `B=Dh`다. 초기 메모에서 검토자는 반대 `AB−C` 방향을 가정하여 lower singular bound가 필요하다고 공격했다. 실제 관계에서는 그 반론이 적용되지 않음을 확인하고 담당자·root에 정정했다.

가정은 m=2p+q,p>q, 두 true axis마다 p개 pure rows, **모든** true reference row의 norm≥a, learned reference C의 전체ℓ0≤m+q, row residual norm≤η, B invertible 및 ||B||op≤L이다. η<a/√2면 다음 논증은 성립한다.

1. Czero row라면 CB도0이므로 Arow norm≤η<a가 되어 모순이다.
2. m개 nonzero rows에 budget m+q이므로 dense row는 최대q개다. p>q인 각 anchor group에는 적어도 하나 singleton Crow가 있다.
3. true row `αe_i`가 Csingleton row `c e_j`와 대응하면 `dist(αe_i,span B_j)≤η`다. 따라서 normalized B_j의 off-axis 성분≤η/a다.
4. 같은 B_j가 두 true axes와 모두 대응하면 두 성분이 모두η/a보다 작아 unit norm과 모순이다. 두 row는 서로 다른 axes에 대응한다. η/a<1/√2와 continuous invertible B 때문에 연결된 domain에서 대응 순열은 일정하다.
5. ||B||≤L로 off-block derivative≤Lη/a이며 rectangle에서 적분하면 block function까지 C0 distance를 제어한다. 각 diagonal derivative는0이 아니므로 component function는 단조다.

이는 all-candidate 명제다. Csupport를 true support와 같다고 가정하지 않는다. 반면 강한 pure-anchor·mixed-row amplitude·sparsity budget을 추가한 결과이며, 일반 TypeS의 자동 귀결은 아니다. C1-near decoder와 작은 reconstruction MSE의 간극도 메우지 않았다.

### 별도 all-support 계산

[protocol amendment2](protocol.md)에 먼저 기록하고 [positive_audit.py](positive_audit.py)를 실행했다. 각 sampled B에서 C의 각 row는 zero/singleton1/singleton2/dense 중 하나다. singleton 최소오차는 B row가 생성하는 line까지 거리, dense는0이다. 이 네 종류와 support 비용을 finite residual thresholds로 완전 열거하여 **고정 B에 대한 모든 C의 minimax row residual**을 계산했다. B연속공간 전체를 수치로 검증했다는 뜻은 아니다.

독립 seed20261025/20261026 총800개 B 중 η<a/√2인473개에서 위 normalized 및 absolute bound 위반은0이었다. normalized observed/bound 최대.99647, absolute 최대.99450이었다. admissible B의 condition number가6697.65인 경우에도 성립했다. 이는 lower singular bound가 필요 없다는 실제 관계의 검산이기도 하다. [원자료](results/positive_all_support.csv), [요약](results/positive_audit.json).

### mixed-row lower bound를 없애면 실제 실패

`A=[e1;1.2e1;e2;1.1e2;ε(e1+e2)]`, `B=[[1,ε],[1,−ε]]`로 두자. C는 앞2row를 singleton으로, 다음2row를 dense coefficient로 e2에 정확히 맞추고 마지막row를0으로 둔다. totalℓ0(C)=6=m+q이고 ||B||=√2다. row residual은√2ε→0이지만 두 normalized B rows가 모두 e1으로 간다. 어떤 순열도 axis recovery를 보장하지 못한다. 코드에서 ε=.1..10^-6의6조건으로 확인했다. 이 예는 원정리의 반례가 아니라 그 **전 rownorm≥a 가정이 핵심**이라는 독립 증거다.

이 positive 정리는 유용한 실질 분석이다. 다만 핵심은 sparse support counting과 line-distance perturbation, connectedness, 적분이다. 현재 어떤 기존 정리와 문구까지 동일하다고 단정하지 않지만, 새 학습 원리 또는 충분한 논문 기여라는 판정도 아직 정당화되지 않는다.

## 7. true generator까지 고정한 더 강한 부정 결과

기존 §2 반례는 trueκ→0 family였다. 담당자가 그 한계를 해결할 구성을 제시했고, [amendment3](protocol.md) 작성 후 [별도 코드](fixed_base_audit.py)로 검증했다.

관측차원10을 처음부터 고정하고 `A=[A1;0_(4×2)]`, `C=AR45`를 모두 고정한다. A1은 §2의 κ=1 six-row matrix다. true exactTypeS minℓ0는8, nonaligned 최소9, singular values는√3으로 고정이다. C는45° transition의 정확한 관측 동치 actual decoder다.

candidate exact reference를 `Bε=[A1R45;εI;εI]`로 둔다. 그 projective row-direction multiplicities는 candidate축에서3,3,diagonal축에서2,2다. 따라서 같은 전역 GL row-count 논증으로 exactTypeS minℓ0는20−6=14이고 비정렬 최소15다. 한편

`||C−Bε||C1 = ||C−Bε||op = sqrt(2) ε → 0`

가 latent unit disk에서 성립한다. Bε의 singular values는√(3+2ε²)여서 inverse conditioning도 유지된다. ε=.1..10^-10의10조건에서 모든 수식·sparsity count를 확인했고 observation covariance identity 오차는7.20e−16 이하였다. [원자료](results/fixed_base_audit.json). same-law는 covariance만이 아니라 `As=C Rᵀs`라는 pointwise identity에서 정당화한다.

이것은 **true와 candidate가 각각 어떤 exactTypeS reference의 작은 C1근방에 있으면 모든 관측 동치 표현이 true축에 가까워진다**는 무조건 주장을, true base까지 고정하여 반박한다. true에 네 constant observation coordinates가 있고 candidate reference가 그 자리에 약한 새 anchors를 만드는 것이 핵심이다. 차원을 실행 중 늘린 반례는 아니다.

공통된 알려진 reference 하나 주변의 안정성, 또는 모든 candidate reference에 uniform amplitude margin·sparsity budget을 부여한 모형에는 적용되지 않는다. 아직 정의되지 않은 κ가 이러한 class-boundary 거리를 측정하여 이 true A에서0이 되는 경우까지 배제한 결과도 아니다. 따라서 ‘어떤 κ기반 안정성 정리도 불가능하다’는 주장은 하지 않는다.

## 8. 최종 갱신 판단과 재개 조건

초기에는 integer gap 실패 예에 불과해 현재 구체화 기각을 권했다. 이후 fixed true-base 부정 결과와 explicit anchor positive bound를 모두 독립 검증했으므로 **판정 보류**로 갱신한다. 이 둘은 어떤 구조 가정을 강화해야 하는지 실제로 보여주는 분석이다. 그러나 장기 착수를 권하려면 다음 핵심이 남았다.

- 연속 mechanism margin을 true·learned 양쪽 모형 class에 대해 명확히 정의하고, 왜 현실적 혹은 관측적으로 정당화 가능한지 설명할 것.
- pure anchors와 모든 row amplitude floor를 벗어나는 비선형 조건에서 상·하계 또는 새로운 현상을 확보할 것.
- sparse-basis/dictionary robustness의 표준 perturbation과 비교하여 새로운 결론이 무엇인지 확정할 것.
- 실제 학습 목적함수 또는 데이터 오차가 필요한 decoder C1 및 learned sparsity 가정을 보장하는지 연결할 것.

현재 positive lemma 자체의 신뢰는 높지만 그것이 원래 broad hypothesis를 해결한다는 주장은 반대한다. 단순 benchmark나 큰 neural 실험을 먼저 늘릴 단계도 아니다. 위 이론적 연결이 후속 연구의 가장 정보량 높은 첫 작업이다.

## 9. 추가로 확인한 surrogate의 population 선호 실패

담당자는 diagonal mixed rows의 크기를 w배 하는 수정안을 제시했다. 검토자는 이를 pure anchors 각축 p개와 `w*d±` mixed rows2개로 일반화하고, [amendment4](protocol.md)를 먼저 기록한 뒤 [별도 코드](weighted_surrogate_audit.py)로 실행했다. row directions의 multiplicity는 p,p,1,1이므로 p>1에서 true basis가 전역 GL sparsest basis다. 정확한 ℓ0 최소는2p+4, 비정렬 최소는3p+3이다.

그런데 compositional contrast는 같은 reconstruction과 같은 전체 Jacobian metric를 가진 rotation족에서

`Ccomp(A Rθ)=p|sin2θ|+w²|cos2θ|`

다. 따라서 `w²>p`이면 trueθ0의 값w²보다45°의 값p가 낮다. [p2/3/5×w1/2/3 총9조건](results/weighted_surrogate_audit.json)을 실행했고 직접 row product와 공식 최대차이는8.89e−15 이하였다. formula는 θ∈[0,π/4]에서 concave인 양의 sine/cosine 합이므로 최소는 endpoint 둘 중 하나다. 이 논증으로 명시된 rotation족의 global comparison이 된다.

특히 **p3,q2,w2**에서는 pure anchors가 mixed rows보다 많고 모든 row norm≥1이며 support overlap은2/(3+2)=40%다. true exactTypeS ℓ0 최소10, 비정렬 최소12이고 `AᵀA=7I`다. 그럼에도 true Ccomp4,45° Ccomp3이다. 공통 metric로 normalize해도4/7 대3/7로 순서가 유지된다. 앞 positive lemma와 모순되는 것이 아니다. 잘못 정렬된 candidate의 ℓ0는14여서 learned budget10을 만족하지 않는다. **실제 surrogate가 그 budget을 보장하지 않는다는 간극**을 드러내는 결과다.

이는 finite sample이나 최적화가 아니라 population objective의 선호 비교다. 회전은 가역이므로 정보 소실이나 모든 downstream task의 악화를 주장하지 않는다. 무엇이 ‘wrong’인지는 scalar block equivalence라는 목표에 한정한다. 전체 gauge를 풀어 arbitrary block scaling까지 허용하면 objective가 퇴화할 수 있으므로, 고정된 전체 metric의 비교라는 조건도 필요하다.

단순한 high-overlap local-minimum 재현보다 강하지만, 이 증거 하나로 새 독립 논문을 권할지는 여전히 신중하다. 원문이 일반적인 Ccomp consistency를 약속한 것은 아니고, TypeS는 nonzero row scaling에 불변인 반면 magnitude-weighted surrogate는 그렇지 않다는 점 자체는 자연스러운 경쟁 설명이다. 실질적 후속 기여를 만들려면 이 불일치를 일반적인 정량 원리와 타당한 surrogate 조건으로 발전시키고 직접 선행과 비교해야 한다. 현재 판정 보류를 유지한다.
