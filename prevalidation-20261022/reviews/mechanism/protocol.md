# 후보 2 독립 검토: 실행 전 기준

검토자: mechanism_review. 작성 2026-10-22 UTC, 아래 수치 실행 전.

## 검토 대상

담당자의 6×2 weak-anchor 반례를 별도 코드로 확인한다. 정렬된 모든 가역 basis를 고려하는 정확한 ℓ0 최소화는 유한 row-direction 열거와 일반 위치 방향 열거로 검산한다. 전역 증명은 row multiplicity 논증으로 별도 제공한다. 수치탐색을 전역 증명의 대체로 쓰지 않는다.

`Aκ=[e1;e2;(e1+e2)/sqrt(2);(e1−e2)/sqrt(2);κe1;κe2]`, `R=Rπ/4`, `Cκ=AκR`, `Bκ=[A0R;κI]`다. C와 A는 latent rotation으로 정확한 같은 관측을 생성한다. B는 C와 가까운 별도 exact sparse model이다. C가 exact TypeS aligned model이라는 주장은 하지 않는다.

## 사전 판정 기준

1. A 및 B의 최소 ℓ0 score=8이고, 허용 scaling/permutation 밖 모든 GL(2) basis score≥9임을 검증. 하나라도 반례면 owner 명제를 반박한다.
2. `σmin(A)=σmax(A)=sqrt(2+κ²)`, `||C−B||op=κ sqrt(2−sqrt(2))`, `A s=C Rᵀs`를 검증한다. κ grid=`10^-1,...,10^-8`. 부호/순서 quotient에서 rotation45°가 작아지지 않아야 한다.
3. 독립 confirmation은 seed 813, 997; 각 seed 20개 κ 로그무작위 및 nonzero strong-row weight [0.7,1.4]. weights 변경은 supports 보존과 uniform inverse condition 확인만 위한 것으로 새로운 현상 발견으로 세지 않는다.
4. 원리의 선형성 한계를 보기 위한 사전 nonlinear lift: 각 관측 좌표 `φi(t)=t+βi tanh(t)`, βi in [.1,.4]. 이는 row support 보존하는 알려진 가역 sensor map이다. random unit disk 점 1000에서 same-law identity 및 C1 차이가 O(κ)인지 계산한다. 전역 C1 주장은 bounded φ′,φ″ mean-value 부등식으로만 정당화한다. 진정한 새로운 nonlinear identification 정리라고 부르지 않는다.

## 경쟁 설명과 평가

이것은 작은 표본·학습·optimizer의 실패가 아니라 admissible model class 안 exact observational equivalence다. ℓ0 gap은 정수 support count라 amplitude margin을 담지 못한다. 반례만으로 fixed well-separated g0의 pointwise stability를 반증하지 않는다. 또한 sharp all-model identified set를 주지 않는다.

신규성: support instability 및 sparsest-basis perturbation의 초등적 사례일 수 있다. 논문을 진행하려면 기존 sparse dictionary/metric regularity를 넘는 정량적인 연속 mechanism margin 또는 원래 질문과 연결된 새로운 식별 목표가 필요하다. ‘최신 exact theorem의 빈틈을 보였다’는 것만으로 논문 가치 판정하지 않는다.

## Amendment 1 — surrogate 산출물 검토 후 추가 실행 전

담당자가 compositional-contrast rotation formula를 추가했다. 해당 구현을 읽은 뒤 독립 검산한다. κ=10^-1..10^-8, θ는 [0,π] 고정10001점에서 직접 row products와 `(1+κ²)|sin2θ|+|cos2θ|`를 비교한다. 이는 전역 GL 최적화 검증이 아니라 명시된 rotation 부분족 공식 확인이다. 선행 Example2/§5의 이미 알려진 local-minimum 한계를 새로운 현상으로 포장하지 않는다.

## Amendment 2 — positive anchor 명제 추가 뒤 독립 실행 전

담당자의 positive_bound.md를 읽었다. 실제 chain-rule residual은 `A−CB`, B=Dh이다. 검토자 초기 메시지는 반대 `AB−C` 방향을 가정하여 σmin(B)가 필요하다고 공격했으나, 실제 방향에는 그 반론이 적용되지 않는다. 이 정정 이력을 보존한다.

독립 계산은 p2,q1,m5 및 totalℓ0(C)≤6에서 모든 C support에 대한 최적 max-row residual을 정확히 계산한다. 고정 B에서 각 row의 C 선택은 zero/singleton1/singleton2/dense 네 종류다. singleton은 해당 B row line에 대한 projection, dense는 정확 복원이다. 가능한 residual threshold의 유한 집합을 열거하여 support 비용≤6인 최소 threshold η를 얻는다. 이는 B를 고정한 모든 C의 전역해이며, B 전체 전역열거는 아니다.

seed20261025의 400개 invertible B를 고정 사전 생성한다. half는 임의 random rows, half는 두 축 또는 순열에 가까운 rows, row norm10^-3..10^1 후 opnorm1.5로 normalize한다. A는 각 축 두 pure rows 및 하나 dense row, 모든 rownorm≥a=.9를 유지한다. η<a/√2인 경우 normalized-row conclusion과 absolute offblock bound를 확인한다. ratio>1+1e−8이면 반례로 보고한다. independent seed20261026의 같은400조건으로 확인한다.

가정 necessity도 확인: A=[e1;1.2e1;e2;1.1e2;ε(e1+e2)], B=[[1,ε],[1,−ε]], C는 앞 두row singleton, 다음 두row dense, 마지막zero. ε=10^-1..10^-6. mixed-row norm lower를 제거하면 residualη→0과 bounded||B||를 유지하면서 normalized rows가 둘다 e1으로 가므로 결론이 실패한다고 예측한다. 이 조건밖 반례를 원래 strengthened theorem의 반박이라고 부르지 않는다.

## Amendment 3 — fixed true-base 반례 독립 실행 전

담당자가 앞 반례의 가변 trueκ 한계를 해결할 새 구성을 제시했다. 관측차원10을 처음부터 고정하고 true A=[Aκ=1;0_(4×2)], C=AR45를 고정한다. candidate exact reference만 Bε=[A1R45;εI;εI]로 바꾼다. ε=10^-1..10^-10. 예측은 A minℓ0=8/nonaligned9, Bε min14/nonaligned15, svA=√3, svB=√(3+2ε²), ||C−Bε||op=√2ε, 45° observationally equivalent transition이다. 검산은 별도 projective direction enumeration 및 Gaussian covariance equality로 한다.

정확한 적용 범위는 true와 candidate가 각각 **자신의 어떤 exact-TypeS reference**에 작은 C¹근방이라는 all-model family다. 공통된 알려진 reference 하나 주변의 안정성은 반박하지 않는다. true에는 네 constant observation coordinates가 있고 candidate reference는 그 자리에 weak anchors를 만드는 것이 핵심이다. all-row amplitude floor·learned sparsity budget을 추가하면 이 예를 배제한다. 따라서 특정 continuous margin을 정의하기도 전에 모든 κ기반 정리를 반박했다고 말하지 않는다.

## Amendment 4 — weighted surrogate preference 독립 실행 전

담당자의 weighted diagonal-row 제안은 exactTypeS와 continuous surrogate의 선호가 다를 수 있다는 별도 문제다. 검토자는 pure anchors를 각축 p개, mixed rows w*d± 두개로 일반화했다. p=3,q=2,w=2이면 overlap2/(p+2)=40%, 모든row norm≥1, trueℓ0min10/nonalign12, Gram7I다. Ccompθ=p|sin2θ|+w²|cos2θ|로 예측되므로 true4보다wrong45°3이 낮다. 이는 동일한 전체Jacobian metric를 가진 rotation족의 global preference 비교이며, arbitrarygauge model전체최적화를 뜻하지 않는다.

실행은 p=[2,3,5], w=[1,2,3], θ∈[0,π/4]10001점의 고정grid. 직접row product와formula, globalendpointminimum, row-count GLmin을검산한다. p3w2 조건은 primary설정, 다른조건은 formula/범위확인이다. 실패/동률조건도모두보존한다.
