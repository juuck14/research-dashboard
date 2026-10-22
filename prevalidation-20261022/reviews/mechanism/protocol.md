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
