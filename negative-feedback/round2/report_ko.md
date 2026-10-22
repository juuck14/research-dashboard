# Negative 관계와 피드백 — 실제 핵심 결과를 확보한 후속 연구

기준일: 2026-10-22. 최종 판정: **검증된 수정 방향으로 진행**.

이번에 진행을 권하는 것은 **negative 개수와 sampling 정책의 국소 반응이 표현의 안정성을 함께 결정하는 정확한 법칙**을 중심으로 한 제한된 이론 논문이다. 이 법칙에 대해 증명, 전체 표현 공간 분석, 자연 정책에서 성립하는 열린 매개변수 영역, 독립 구현과 경계 인증, 예측한 dynamics의 실제 실행을 확보했다. 핵심 가설을 앞으로 검증해야 하는 제안서 단계는 벗어났다.

반면 ‘adaptive negative가 의미 정보를 지워버린다’는 넓은 주장은 뒷받침하지 못했다. 일반적인 pretrained encoder에서 요인이 영구적으로 삭제되거나, 실제 false-negative filtering 알고리즘이 실패한다고 주장하는 논문은 현재 근거로 성립하지 않는다. 그 주장까지 완성했다고 쓰지 않는다.

## 1. 무엇을 새롭게 밝혔는가

두 가지 의미 요인 a, b가 있다고 하자. 물체의 모양과 색깔처럼 서로 독립적인 두 속성을 생각하면 된다. 현재 표현은 두 속성을 모두 균형 있게 구분하고 있다. 이때 현재 표현에서 비슷해 보이는 예를 negative로 덜 선택하면 어떤 일이 생기는가.

한 요인이 조금 약해지면, 그 요인만 다른 두 예는 더 비슷해 보인다. 필터가 그 두 예를 더욱 덜 선택하면, 약한 요인을 다시 구분하게 만드는 힘도 달라진다. 중요한 질문은 이런 순환이 있을 수 있느냐가 아니다. 일반적인 피드백 자체는 기존 performative learning과 robust weighting으로 설명된다. 이번에 답한 질문은 **그 순환이 언제 균형을 복구하고 언제 불균형을 키우며, negative를 K개 쓰는 것이 그 경계를 정확히 어떻게 바꾸는가**다.

분석한 모형에서는 복구력의 부호가 다음 하나의 비교로 결정된다.

\[
\lambda_{\rm balance}=C_K(T_K-\eta),\qquad C_K>0.
\]

여기서 eta는 현재 score가 조금 바뀔 때 negative 확률이 얼마나 민감하게 반응하는지를 나타낸다. 정확히는 균형을 깨는 경로에서의 국소 반응이며, 임의의 score 하나에 대한 partial derivative와는 구분해야 한다. T_K는 contrastive loss에서 유한한 negative 개수를 사용하는 분모가 만드는 복구 임계값이다. Lambda가 양수이면 negative gradient flow가 균형을 복구하고, 음수이면 불균형이 자란다.

**직접 증명한 결과:** InfoNCE에서 T_K는 K가 커질수록 엄격히 증가한다. K=1일 때의 .7310586에서 출발해 1로 접근한다. 따라서 eta가 그 사이에 있는 정책은 적은 negative에서 불안정하다가, 충분히 많은 negative에서 안정해질 수 있다. 이는 stochastic gradient의 분산을 줄여서 생긴 현상이 아니다. 잡음이 전혀 없는 정확한 기대 업데이트에서도 부호가 바뀐다. K가 달라지면 loss의 모집단 vector field 자체가 달라진다는 점을 명시한다.

이 식을 요인 두 개의 좌표에만 제한해서 얻었다면, 다른 방향의 불안정성을 놓쳤을 수 있다. 그래서 네 개의 embedding을 충분한 차원 d≥3에서 각각 자유롭게 움직이게 두고 **전체 구면 접공간**을 계산했다. 확인 가능한 특정 정책 값 조건 아래에서는 위 식이 회전을 제외한 모든 방향의 안정성을 결정한다. 다른 방향을 무시한 계산이 아니다.

## 2. 구체적으로 증명하고 실행한 결과

### 2.1 전체 공간과 모든 K에 대한 정리

관측은 두 독립 부호 a, b의 네 조합이다. 각 관측의 embedding은 unit vector이며, d≥3이면 네 상태를 tetrahedron으로 구분할 수 있다. Positive는 동일한 관측이다. Negative는 현재 표현의 score에 따라 정해지는 양의 선택확률로, 독립적으로 K번 복원추출한다. Sampler는 한 번의 update 안에서는 detach되며, anchor와 negative의 encoder 양쪽에 gradient가 흐른다.

균형 표현은 네 상태를 square로 배치한다. 좌표 회전은 같은 해로 취급한다. 이 표현은 두 요인을 모두 보존하지만, global optimum이라고 가정하지는 않는다. 충분한 차원은 표현 용량의 엄격한 제한을 제거하기 위한 통제다. 그렇다고 unit normalization이 만드는 실제 에너지 제약까지 없어지는 것은 아니다.

`theory/theorem.md`의 여섯 정리에서 확보한 내용은 다음과 같다.

| 직접 도출한 결과 | 확보한 수준 | 의미 |
|---|---|---|
| 일반적인 smooth positive score 정책의 전체 tangent spectrum | 완전 증명 | balance 방향뿐 아니라 normal mode까지 포함한다. |
| T_K의 정확식과 K에 대한 엄격한 단조성 | 완전 증명 | negative 개수에 따른 전이의 방향과 유일성을 모든 K에서 예측한다. |
| 하나의 scalar 경계가 전체 안정성을 결정하는 충분조건 | 완전 증명 | angle 하나의 안정성을 전체 안정성으로 과장하지 않는다. |
| InfoNCE와 DCL을 연결하는 분모 offset 분석 | 완전 증명 | positive term은 경계를 바꾸지만, 현상을 전부 설명하지는 않는다. |
| 자연 exponential 정책에서 negative 개수 증가가 안정화를 만드는 열린 영역 | 완전 증명 | 특수하게 조각한 필터 하나에만 의존하지 않는다. |
| Square에서 같은 negative 법칙을 갖는 정책, frozen 목적, 국소 반응이 다른 정책의 비교 | 정확 구성 | 현재 q 값만으로는 동역학을 알 수 없음을 확인하는 통제다. |

단조성 증명은 ‘negative가 더 많으면 좋을 것’이라고 가정하지 않는다. Adjacent negative 하나를 조건으로 고정하면, 임계값이 양의 iid 합에 대한 inverse-moment ratio로 바뀐다. 양의 항을 더할 때 그 비율이 엄격히 감소한다는 사실을 Cauchy–Schwarz와 독립적인 random shift로 증명했다. 전체 공간에 대한 충분조건도 별도 모드의 부호를 실제로 비교해 도출했다.

### 2.2 단순한 자연 정책의 정확한 정수 경계

Score가 클수록 덜 뽑는 omega(s)=4^(-s)에 uniform 확률 30%를 섞는다. Square에서 negative 확률은 self .103, 두 adjacent 각각 .187, opposite .523이며, eta=.830293948906이다. 모든 후보에는 양의 확률이 있다.

| 동일한 정책 | 불안정 구간 | 모든 방향이 안정인 구간 |
|---|---|---|
| InfoNCE | K≤4 | 모든 K≥5 |
| Positive denominator를 제거한 DCL | K≤7 | 모든 K≥8 |

이는 K=128까지 계산한 뒤 ‘그 뒤에도 그럴 것’이라고 추정한 결과가 아니다. 모든 K에 대한 정리와 충분조건에, 독립적인 70자리 outward interval 계산으로 인증한 인접 정수 경계를 결합했다. 자연 정책은 열린 매개변수 영역의 간단한 예다. 이 값은 증명 이후 해석적으로 선정한 예이며, 독립 holdout 설정에서 발견했다고 주장하지 않는다.

K=4에서의 불안정성은 매우 느리다. E-fold 시간은 약 10,930 flow 단위다. 짧게 실행하면 거의 변하지 않는 모습을 안정성으로 잘못 읽을 수 있다. 이 때문에 실행 전에 이론적 시간척도에 맞춘 protocol을 작성하고, 실제로 적분했다.

4개 seed에서 각 K에 대해 frozen과 adaptive를 비교한 16개 적분은 모두 사전에 정한 기준을 충족했다. 일반적인 d=4 perturbation을 넣어, 움직임을 tied 평면에만 가두지 않았다.

- Adaptive, K=4: 요인 에너지 불균형이 20.08518–20.08533배가 되었다. 국소 예측은 exp(3)≈20.08554다.
- Adaptive, K=5: 요인 에너지 불균형이 .049787075–.049787081배가 되었다. 국소 예측은 exp(-3)≈.049787068이다.
- Frozen: 두 K 모두 균형으로 복귀했다. 최종 극소값은 numerical floor에 도달하므로 정확한 수렴률로 해석하지 않는다.

![예측한 경계의 실제 dynamics](dynamics/results/cutoff_flow.png)

좌우 그림의 시간은 각각 eigenvalue로 정규화했다. 같은 가로축 값이 같은 실제 시간이나 계산량을 뜻하지 않는다. 그래프는 국소 불균형의 성장과 회복을 보여준다. 마지막에 한 bit가 완전히 사라졌다는 결과는 아니다.

### 2.3 학습된 비선형 encoder에서는 무엇이 남았는가

Lookup vector를 자유롭게 조정하는 설정이 너무 인위적일 수 있다. 이를 확인하기 위해 관측을 16차원 비선형 renderer로 만들고, 14차원의 연속 nuisance를 추가했다. Positive는 의미 요인을 공유하지만 nuisance는 독립이다. Encoder는 16→32 tanh→8 shared MLP이며, 요인 label을 보지 않고 학습한다. Uniform SSL warmup 후 동일한 초기 encoder를 uniform, frozen-snapshot, adaptive 정책으로 나누고, 같은 batch stream으로 학습했다. 실행 전에 별도로 선언한 unlabeled PCA 초기화 통제도 두었다.

6개 seed×2개 초기화×3개 정책, 총 36개 fork 학습을 실제로 실행했다. Batch 64, SGD learning rate .05, warmup 1,000 step, fork 3,000 step을 고정했고, 결과를 보고 시간을 늘리거나 설정을 바꾸지 않았다. 이 배치 실험은 q로 가중한 **one-negative pair loss**를 사용한다. Negative 63개를 하나의 log 안에 넣는 InfoNCE가 아니다. 따라서 위의 K=5 경계를 neural encoder에서 재현한 실험이라고 부르지 않는다.

관측 결과는 선명하지만, 더 강한 주장에는 실패했다.

| Warmup arm의 worst-factor 지표 | Uniform/Frozen | Adaptive: 6개 seed의 평균 [최소, 최대] |
|---|---:|---:|
| Clean ridge accuracy | 1.000 | .762 [.667,.926] |
| Clean RBF accuracy | 1.000 | .780 [.684,.920] |
| Clean OLS audit accuracy | 1.000 | .785 [.689,.938] |
| Feature noise σ=.05에서의 OLS accuracy | 1.000 | .597 [.545,.667] |

약한 요인의 class-mean **energy, 즉 coefficient의 squared norm**은 frozen 대비 882–7,260배 작아졌다. Norm 자체의 비율은 약 29.7–85.2배다. 이 큰 수치를 정보량의 비율로 바꾸어 말하지 않는다. 대괄호는 confidence interval이 아니라, 6개 seed에서 관측한 최소값과 최대값이다.

실행 전에 정한 더 강한 endpoint는 clean linear accuracy의 감소폭≥.15와 noisy accuracy의 감소폭≥.20이 primary와 confirmation 각각에서 2/3 이상 성립할 것을 요구했다. Warmup은 primary 1/3, confirmation 3/3이므로 **원래 endpoint는 실패했다**. PCA도 각각 0/3과 2/3으로 실패했다. Confirmation 결과만 보고 성공으로 바꾸지 않았다.

작아진 신호를 ridge regularization이 무시했을 가능성을 검증하기 위해, 결과 관측 후 고정된 OLS 진단을 선언하고 저장된 모든 모델에 동일하게 적용했다. PCA에서는 clean OLS 평균이 .950으로 회복되어, 정보에 접근할 수 있음을 보여주었다. 그러나 noisy OLS는 .511이었다. 따라서 **잔여 정보가 있어도 geometry가 압축되어, 지정한 noise 아래 매우 취약해졌다**는 해석이 맞다. 표현이 정보를 완전히 잃었다고 해석하지 않는다. OLS는 primary endpoint를 대체하지 않는다.

독립 검토자는 새로운 seed에서 150개 좌표의 gradient를 검산했고, 최대 절대오차는 1.02e-10이었다. 저장된 36개 모델의 OLS를 별도의 pinv로 재계산했을 때도 accuracy가 일치했다. Fork 시점에서 adaptive와 frozen의 loss와 gradient도 정확히 같았다. 구현 오류, 초기 정보 부족, ridge만의 측정 효과로 결과를 설명하기는 어렵다. 다만 단일 renderer, 네 가지 의미 조합, 유한한 학습 시간이라는 제한은 남는다.

## 3. 방향을 무너뜨릴 반론들을 어떻게 처리했는가

| 반론 | 실제 검증 | 결론 |
|---|---|---|
| Generic feedback을 재발명한 것인가? | Performative PP와 robust loss로 직접 환원하고, 비SSL toy를 구성했다. | 이 일반적인 주장은 기여에서 제외했다. |
| K∞ 효과는 temperature 변화만으로 설명되는가? | Zero-floor exponential field의 effective-temperature 항등식을 도출하고, 60개 좌표와 매개변수를 검산했다. | 그렇다. 이 limit만을 신규 기여로 삼지 않는다. |
| Negative 수의 효과는 알려진 finite-batch bias에 불과한가? | 원문을 비교하고, 정확한 finite-K field를 분석했다. | Finite-K에서 mean이 바뀐다는 사실은 기존 결과다. 새 기여는 정확한 stability boundary와 모든 K에 대한 법칙이다. |
| NPC 때문에 gradient가 작아진 것뿐인가? | Positive denominator를 제거한 DCL을 증명하고 실행했으며, 독립적인 interval 인증도 수행했다. | 경계는 바뀌지만 전이는 남는다. |
| Angle 하나만 보았기 때문에 생긴 결과인가? | 전체 sphere spectrum을 도출하고, 별도의 ordered-tuple oracle과 대조했다. | 제한된 모형 안에서는 이 반론을 해소했다. |
| 어떤 parameter에서는 balance만 좋아지고 다른 방향은 불안정한가? | omega=exp(-s), epsilon .1에서 normal mode 반례를 실행했다. | 실제로 가능하다. 충분조건이 없는 일반 주장은 기각했다. |
| Shaped filter에서만 가능한가? | 자연 exp 정책에서 성립하는 열린 영역을 증명했다. | 이 반론을 해소했다. 다만 floor는 수학적으로 중요하다. |
| Lookup에서만 생기는 인공적인 현상인가? | Continuous nuisance를 포함한 shared MLP에서 36개 run을 실행했다. | Compression은 관측했다. 일반 신경망이나 K cutoff까지 확장해 증명한 것은 아니다. |
| 요인을 잊었다는 측정 자체가 틀렸는가? | Ridge, RBF, OLS, noise, energy, raw oracle을 구분해 검토했다. | 완전한 정보 소실 주장은 제거하고, robust geometry에 대한 주장으로 제한했다. |
| Rank filter에도 smooth 정리를 억지로 적용했는가? | 별도의 one-sided proof와 tolerance control을 수행했다. | Exact tie와 finite tolerance가 서로 다르다는 점을 명시했다. |

Rank 보조 결과에서는 독립 검토가 중요한 오류 가능성을 발견했다. 수학적인 exact tie 규칙은 무한소 수준에서 불안정하지만, 구현에서 TIE=1e-12를 두면 아주 작은 복귀 띠가 생긴다. Delta=1e-13에서 exact branch의 속도는 +.0403412, tolerance branch의 속도는 약 -7.2e-15임을 실제로 계산했다. 이 차이를 정리와 수치실험 모두에 반영했다. 이 보조 결과를 GloFND 전체 알고리즘의 반례로 포장하지 않는다.

## 4. 가장 가까운 선행연구와 정확히 다른 점

문헌 조사는 자기 결과를 살리려는 담당과 분리했다. 별도 검토자가 원문의 정리와 가정을 확인하고, 이번 결과가 기존 결과로 직접 환원되는지 검토했다. 최신성 검토의 기준일은 2026-10-22다. 제목과 초록만 본 논문을 근거로 ‘이 정리는 기존에 없다’고 판단하지 않았다.

가장 가까운 연구와의 관계는 다음과 같다.

1. **Perdomo2020 / SPRINT2026:** 현재 parameter가 만드는 분포에서 detached gradient를 사용하는 틀과 nonconvex stationarity 결과가 이미 있다. 이번 모형에서는 stable square와 unstable square가 모두 G=0을 만족한다. 따라서 gradient norm에 근거한 stationarity만으로는 두 상태가 주변 표현을 끌어당기는 성질, 즉 attraction의 차이를 알 수 없다. 이번에 추가한 결과는 CL에서 K별로 정확하게 구한 spectrum과 boundary다.
2. **Fan2016/2017:** K=1에서 나타나는 q'ell' 곡률은 self-paced learning과 robust weighting으로 설명된다. 따라서 새 학습 원리를 발명했다는 주장은 빼고, 유한한 negative tuple에 대한 정확한 개수 법칙을 중심에 두었다.
3. **Chen2022 / Wu2022 / Yeh2022:** Finite-batch bias, negative 개수의 효용, NPC는 이미 핵심적으로 연구된 문제다. 이번 결과는 단순히 ‘K가 중요하다’는 발견이 아니다. Sampler가 바뀌는 기대 field에서 정확한 불안정·안정 경계와 엄격한 단조성을 추가했다. DCL control은 가장 가까운 대안 설명을 실제로 적용해 본 검증이다.
4. **Jiang2025 / Awasthi2022 / Parulekar2023:** Global representation geometry와 cluster-preserving optimality는 이번에 다룬 local closed-loop stability와 분석 대상이 다르다. 설정이 다르다는 사실 자체를 새로움의 근거로 삼지는 않았다. 기존 정리로는 예측할 수 없는 negative 개수와 slope에 따른 부호를 직접 구했다.
5. **Xue2023 / GloFND2025 / SnaPhArd2026:** Feature suppression, score filtering, optimality에 관한 연구가 이미 있다. 이번 연구는 suppression 자체를 발견했다고 하지 않으며, 실제 GloFND의 실패도 주장하지 않는다. 최근 SnaPhArd에서 다룬 fixed-key query collapse는 요인 정보 삭제와 개념부터 다르다.

정확한 제목, 링크, 연도, 읽은 section, 이번 결과와의 차이는 [문헌 대조표](prior-art/literature_audit.md)와 [논문 참고문헌](manuscript.md#references)에 정리했다. Jiang의 HTML 본문 날짜와 arXiv·journal metadata가 일치하지 않는 점도 기록했으며, 공식 TMLR index에서 2025년 5월(May2025)을 확인했다. SPRINT는 2026년 10월(October2026)의 공식 journal record와 primary 본문을 확인했다. 이 검색이 문헌을 빠짐없이 검토했다는 증명은 아니다. 다만 실제로 확인한 가장 가까운 원문의 직접적인 따름정리로 이번 결과가 환원되지는 않았다.

## 5. 논문의 핵심 절반이 있는가

**제한된 이론 논문이라는 기준에서는 있다.** 다음 요소들이 실제 결과를 통해 연결되어 있다.

- **문제:** Sampler가 바뀌는 상황에서 negative 개수가 표현의 attraction을 어떻게 바꾸는가.
- **공백:** 고정된 정책이나 global optimum에 대한 분석, 일반적인 PP bound로는 얻을 수 없는 정확한 국소 K 법칙이 필요하다.
- **중심 명제:** 전체 spectrum, 단조적인 boundary, 모든 모드에 대한 조건, 자연 정책에서 성립하는 열린 영역을 확보했다.
- **근거:** 완전한 증명, 독립적인 tuple 구현, 정수 경계에 대한 interval 인증, 예측한 실제 flow가 있다.
- **범위 확인:** Shared MLP에서의 compression과 더 강한 endpoint의 실패, normal mode 반례, rank tolerance에 따른 차이를 확인했다.
- **원고:** 문제 정의부터 관련 연구, 정리, 증명, 실행, 반례, 한계, 참고문헌까지 작성했다.

이는 학술지나 학회 채택을 보장한다는 뜻이 아니다. 현재 가장 큰 위험은 정리의 참·거짓이 아니라, **네 상태의 대칭 모형에서 얻은 정확한 법칙이 얼마나 넓은 독자의 이해를 바꾸는가**다. 모형이 작다는 이유만으로 결과를 기각하지도 않고, 많은 FD 검산 횟수를 학술적 중요성으로 대신하지도 않는다. 실제 기여는 하나의 정확한 법칙과, 그 법칙이 예측하거나 반박하는 조건이다.

기각한 넓은 주장은 분명하다. ‘Full support이면 절대 suppression이 없다’, ‘adaptive filtering이면 항상 permanent blindness가 생긴다’, ‘balance를 회복하면 전체 표현이 안정하다’, ‘낮은 probe 점수는 정보 삭제를 뜻한다’, ‘같은 q에서 반대 stability가 나오는 것 자체가 새 학습 원리다’는 주장을 현재 원고의 기여로 삼지 않는다.

## 6. 남은 일: 보강과 다른 연구를 구분

[핵심 불확실성 대조표](decisive_questions.md)에 시작 당시의 근거, 반론, 결정적 검증, 판정과 함께 남은 검증이 실패할 경우의 영향을 따로 정리했다. 이 표는 기존 protocol과 기록을 사후에 모은 감사표이며, 표 전체를 사전등록했다고 주장하지 않는다.

### 현재 논문을 보강하는 일

1. **약간 비대칭인 population에서 현상이 유지되는 정량적 범위.** 현재 확보한 엄격한 고유값 margin은 정확히 대칭인 모형에서 국소 결과를 보장한다. 작은 perturbation에 대한 연속성은 표준적인 사실이다. 그러나 어느 정도의 불균형까지 현상이 지속되는지 정량화하면 정리의 설명력이 커진다. 이 범위를 이미 증명한 것처럼 쓰지는 않았다.
2. **Shared encoder에서 finite-K boundary를 별도로 검증하는 실험.** 이번 MLP는 one-negative pair risk를 사용하므로 K=5 boundary를 검증하지 않는다. 현재 수학적 결과의 핵심 검증은 완료했다. 같은 threshold가 parameterized network에서 얼마나 정확하게, 또는 근사적으로 나타나는지 측정하면 경험적 적용 범위를 넓힐 수 있다. 이 실험이 실패하더라도 lookup 정리가 무효화되지는 않으며, 적용 범위를 규정하는 결과가 된다.
3. **더 많은 의미 조합.** 이전 단계에 3-bit 수치 결과가 있지만, 이번 모든 K의 법칙을 그대로 확장한 정리는 아니다. 일반적인 확장을 추측만으로 논문 중심에 넣지 말고, 검증된 경우에 추가해야 한다.
4. **원고 압축과 외부 전문가 검토.** 현재 원고는 검증 과정을 추적할 수 있도록 길게 작성되어 있다. 주기여를 threshold와 열린 성립 영역에 모으고, spectrum의 세부 계산을 appendix로 정리할 수 있다. 실제 외부 연구자에게 보내지는 않았다.

### 현재 완료했다고 말할 수 없는 별도의 중심 가설

일반 pretrained encoder의 영구적인 정보 삭제, 실제 false-negative filter의 실패율, 임의의 augmentation이나 비복원추출 sampler에 대한 동일한 법칙, 전역 basin 이론은 별도의 문제다. 이를 향후 그림 몇 개만 추가하면 완료되는 보강으로 취급해서는 안 된다. 그런 넓은 논문으로 목표를 바꾸면 새로운 중심 증거가 필요하다.

현재 판정의 핵심을 좌우하는 미실행 GPU 실험은 없다. 이번 작업은 CPU에서 필요한 분석, 학습, 반박 검증을 완료했다. 더 넓은 벤치마크에서 성공한 것처럼 쓰지 않았다.

## 7. 산출물과 읽는 순서

1. [논문 원고](manuscript.md): 실제 결과를 연결한 중심 문서다.
2. [여섯 정리의 전체 증명](theory/theorem.md): 모든 가정, 각 모드, DCL 예외, 열린 성립 영역을 확인할 수 있다.
3. [독립 수학·코드 심사](review/review.md): 증명 재도출, 78개 spectrum, interval 인증, encoder의 150개 FD 검산, quantile 반론을 기록했다.
4. [가장 가까운 선행연구 대조](prior-art/literature_audit.md): 실제로 읽은 원문의 범위와, 기존 결과로 직접 환원되는지에 대한 판정을 정리했다.
5. [비선형 encoder 결과](encoder/manuscript_results.md): 원래 gate의 실패, readout별 결과, energy와 noise에 대한 해석을 확인할 수 있다.
6. [재현 안내](reproduction.md): 환경, 명령, seed, 설정, 원자료, 그림의 연결을 제공한다.
7. [연구 변경 이력](progress.md): 계획, 관측, 판정의 변경을 구분해 기록했다.

보고서의 ‘직접 증명’은 이번 작업에서 수학적으로 도출한 결과, ‘직접 실행’은 저장된 코드로 실제 계산하거나 학습한 결과, ‘문헌’은 연결된 원문에서 확인한 내용을 뜻한다. 제한된 모형 밖으로의 확장은 현재 증명과 실행 결과에서 구분했다. 이전 단계의 기록은 덮어쓰지 않았다.
