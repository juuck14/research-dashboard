# 판정: 현재 구체화는 기각

이 판정은 **현재 제안한 confounding/간결한 수정안을 수개월의 독립 연구로 착수하지 않음**을 뜻한다. Probabilistic representation, unknown correspondence, nonlinear uncertainty 전체가 해결됐거나 불가능하다는 결론이 아니다.

## 결정적인 이유

1. **원래의 존재적 가설은 지지되지만 그 사실만으로 신규 기여가 되지 않는다.** 원자료는 unknown correspondence를 허용하면 pair-fit이 같아도 관측 예측이 달라질 수 있다고 했으며, 보편 불가능성을 명시적으로 주장하지 않았다. Categorical 결과는 그 가설을 지지한다. Circle-vMF의 joint identification은 이번에 추가한 더 강한 탐색 H1만 반박한다. 따라서 원가설이 틀렸기 때문에 기각하는 것이 아니라, 이를 지지하는 현재 사례가 고전 원리를 넘어서는지로 판단한다.
2. **명확하게 살아남은 categorical ambiguity는 고전 문제다.** Exact identified ridge c=a²b, observable-repeat sharp interval, proper Brier regret, acquisition-budget 실험까지 수행했다. 하지만 표준 channel factorization/latent-class moments/replicate deconvolution을 구체화한 것이다. 식이 조금 다르다는 이유만으로 새 학습 원리라 할 수 없다.
3. **vMF의 operational instability도 알려진 강력한 설명이 있다.** Exact joint identification과 equal-channel Fisher singularity가 양립함을 확인했다. Root가 직접 계산한 KL t⁴/t⁶와 LRT는 실질적인 결과이나 magnitude/sign의 higher-order 구분은 Rotnitzky2000의 singular-inference 틀 안에 있다. 아직 실제 nonlinear/heteroscedastic SSL objective에서 이 설명을 넘어선 명제가 없다.
4. **남은 핵심 일이 아직 기여 자체다.** 임의 learned mean map, heterogeneous posterior, acquisition lineage가 불완전한 실데이터에서 sharp prediction set를 정하는 문제는 해결하지 못했다. 이것을 “추가 benchmark만 남음”이라고 쓰면 현재 증거를 과장한다.

## 증거 강도와 한계

직접 증명: circle full-sequence injection, exact categorical ridge/conditional sharp interval, 제한 context의 minimax Brier regret. 실제 실행:404population조건,60pair datasets/180predictions,700oracle inverse fits,60acquisition datasets. 별도 reviewer가 emission enumeration·CSV를 감사했고 Root는 Fourier/KL/LRT를 별도 실행했다. 원래 가설의 가능성과 각 제한 명제의 근거는 강하지만 **독립 논문의 신규성과 중요성은 확보하지 못했다.** Circle의 성공으로 원래 부분식별 질문을 대체해 해결했다고 주장하지 않는다.

Counterpoint: circle exact-identification theorem과 구체 constants는 기술 note로 유용할 수 있다. 똑같은 정리를 이미 출판한 문헌을 찾았다고 단정하지 않는다. 그러나 known geometry/homoscedastic subclass의 Bessel 계산만으로 원래 representation-learning 질문의 새 지식을 충분히 제공한다고 판단하기 어렵다. 이 반론 때문에 “흥미로운 새 계산”과 “몇 달 우선 투자할 연구”를 구분한다.

## 살려보려 한 수정안

| 수정안 | 실제로 얻은 것 | 그래도 진행하지 않는 이유 |
|---|---|---|
| Q/R toy를 sharp interval로 확장 | Reviewer가 full Gram orbit의 sharp range 증명·실행 | 표준 matrix factorization의 cubic target 계산 |
| unknown kernel를 symmetric channel로 제한 | c=a²b exact set와 independent-repeat prediction interval | 고전 inverse/measurement-error 구조 |
| 원문에 가까운 unknown scalar vMF | 전체 Fourier sequence의 joint injection 직접 증명 | known mean/homoscedastic circle에 한정, 실제 learned encoder 공백 미해결 |
| exact 식별 대신 operational query | equal-channel singularity, Root KL t⁴/t⁶·oracle tests | known singular-likelihood 원리로 설명, general estimator/SSL law 없음 |
| 추가 acquisition의 가치 | total budget맞춘 repeat vs more-positivepairs 실행 | replicate Fourier 원리의 직접 적용 |

## 재개 조건

지금 직접 착수한다면 먼저 [직접 증명](theory.md), [독립 비판](../prevalidation-20261022/reviews/uncertainty/review.md), PCL AppendixA와 Rotnitzky2000을 대조하는 것이 가장 정보량이 높다. 새 uncertainty head나 loss를 만들 이유는 아직 없다.

다음 중 하나를 먼저 확보하면 재개할 수 있다.

- 실제로 지정한 probabilistic SSL objective의 near-optimal 해 집합에서 observable target의 sharp law를 구하고, 단순 pair-density fitting 이상의 현상을 보인다.
- Heteroscedastic/learned-mean family에서 최소 acquisition budget의 matching upper/lower bounds를 얻는다. Known identity mean map을 제거한 차이가 어떤 새 결론을 요구하는지 분명해야 한다.
- 기존 singular/replicate 이론이 같은 예측을 주는 두 설정에서 uncertainty calibration의 성패를 달리 만드는 검증 가능한 구조를 찾는다.

이는 아직 계획이며 실행 결과가 아니다. 현재 모든 제안을 논문 초안으로 유지하지 않고 기각 기록을 남긴다. 현재 결과로 실증된 범위를 넘어선 paper draft는 작성하지 않는다.
