# 연구 노트: approximate mechanism class, candidate complexity, surrogate preference

상태: **판정 보류인 후보2의 실제 결과를 연결한 수학 노트**. 투고 가능한 신규 논문이라는 판정이나 아직 없는 일반 Type S theorem을 포함하지 않는다.

## 문제

Exact support 구조로 정의한 factor를 C¹ 오지정 아래 해석하려면, 같은 관측법칙을 설명하는 모든 decoder의 factor 관계가 얼마나 달라질 수 있는지 알아야 한다. 관측 좌표·source chart metric을 고정하고 dependent latent를 허용한다. Factor별 재매개화·순서는 동치이고 dense rotation은 다른 해다.

가까운 MI2026 Type S theorem는 exact integer sparsity와 irreducibility를 쓴다. Robust nonlinear representation/dictionary 선행은 conditioning·모형 제한의 중요성을 이미 보여 준다. 따라서 단순히 gap 분모를 넣는 것이 연구 기여가 될 수는 없다. [원문 대조](literature.md).

## 실제 주장과 근거

**명제1.** Exact Type S와 균일 conditioning만으로 approximate class의 uniform factor stability는 나오지 않는다. 6×2 weak-anchor family의 gap1을 유지하면서 C¹ budget→0, axis distance45°인 same-law 대안을 구성했다. 완전한 [구성·증명](theory.md), 47조건 [직접 계산](results.md), 별도 구현의 검토를 연결했다.

**명제2.** True generator를 고정해도 각 candidate가 *어떤* exact TypeS reference에 가깝다는 조건만으로는 충분하지 않다. 네 constant observation coordinates에 candidate reference의 작은 새 support를 넣는 fixed-base 예가 있다. Candidate complexity를 통제하지 않는 범위이며, common known base에 대한 실패로 확대하지 않는다.

**명제3.** Pure anchor의 수 p가 overlap row 수 q보다 많고, 모든 row의 진폭 floor a, learned reference의 ℓ0 budget, chart regularity를 가정하면 모든 관측 동치 nonlinear candidate의 normalized off-block derivative를 제어할 수 있다. η=δ(1+L)<a/√2에서 off-block≤Lη/a. Connectedness로 하나의 global permutation을 얻고 rectangle 적분으로 C⁰ block approximation을 얻는다. [완전 증명](positive_bound.md). Global C¹ approximation은 별도 미해결이며 명제를 과장하지 않는다.

**명제4.** 위 구조 조건을 실제 compositional surrogate가 보장하지는 않는다. p3,q2,w2의 strong-witness 예에서 완전 재구성·Gram7I를 맞춰도 true contrast4보다 wrong45° contrast3이 작다. 이는 optimizer나 finite sample 문제가 아니다. 원 MI 논문이 일반 surrogate guarantee를 주장한 것은 아니므로 그 theorem의 반박도 아니다.

## 검증과 남은 핵심

Direct construction·nonlinear lift·surrogate grid·all-support 독립 audit가 [결과](results.md)에 연결된다. 조건 수를 새 원리의 증거로 세지 않는다. 독립 검토는 제한 정리의 chain-rule 방향, zero row 배제, 두 축 assignment, 전역 연결성과 가정 삭제 반례를 확인했다. [독립 기록](../prevalidation-20261022/reviews/mechanism/review.md).

이 네 명제는 중요한 구분을 명확히 하지만 아직 독립 논문의 기여 폭을 확보하지 못했다. 일반 Type S의 비자명한 quantitative margin, 후보 complexity의 적정 정의, 실제 loss에서 이 admissible class로 가는 연결이 남았다. 제한 정리가 기존 sparse-basis theorem의 문자 그대로 따름정리라는 환원도 확인되지 않았다. 새 loss나 benchmark를 빈칸에 넣지 않았다. [최종 판정·재개 기준](verdict.md).
