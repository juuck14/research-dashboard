# 중요성 판정 정정과 실제 추가 검증

2026-10-23. **최종 판정: 추가 핵심 연구 필요. 최상위 학술지 논문의 핵심50% 확보 판정은 철회하며, 이번 결과로 복구하지 않는다.** [정정문](../ASSESSMENT_CORRECTION.md).

## 1. 이전 판단에서 잘못된 부분

기존의 국소 정리·계산·인증과 그 적용 범위는 유지한다. 잘못된 것은 이 결과들의 존재에서 JMLR 수준의 중요성 충족으로 넘어간 판단이다.

심사 이력을 다시 읽으면 [원고 전 반대판정](../round3/review/pre_manuscript_verdict.md)도 이미 일반·연속 all-K 분류, 일반 normal-gap ordering, full-window 실현을 인정했다. 그런데 [최종 재심](../round3/review/final_review.md)은 상당 부분 같은 결과를 다시 열거하고, ordinary 학습 방문을 필수로 요구하는 것은 pure theory에 과도하다고 판단했다.

‘자연 이미지 성능이나 ordinary 학습 방문이 모든 순수 이론에 필수는 아니다’는 맞는 문장이다. 그러나 그것은 특정 현재 이론의 중요성이 충족됐다는 증거가 아니다. 필수적이지 않은 요구를 제거한 것과, 독립적인 중요성의 근거를 확보한 것을 혼동했다. 이 판단 오류는 책임을 내부 심사자에게 넘기지 않고 최종 보고를 한 root의 오류로 정정한다.

이번에는 기존 결과를 다시 설명하는 데 그치지 않고 가정, 비 oracle 접근성, task 의미를 실제로 분석·실행했다. 그 결과 긍정적 근거도 추가됐지만 중요성 공백은 남았다.

## 2. 가정의 강도를 더 정확하게 밝혀낸 결과

조건부 균형을 제거하면 `G'_K(0)`에는 sampler normalizer와 조건부 평균에서 오는 항들이 남는다. 특히 기존 정리가 허용하는 성분은 다음과 같이 구분된다.

\[
h=m(s)+\xi,\quad m(s)=E[h\mid s],\qquad
G[h]=G[m],\quad H[h]=H[\xi]+H[m],\quad H=G'.
\]

기존 정리는 중심화된 성분 xi를 다룬다. 균형 방향에 작은 `eta*a(s)`를 더하면 **drift는 1차, slope 변화는 2차**다. 따라서 수치미분값이 거의 바뀌지 않았어도 기존 위치가 equilibrium이라는 사실은 먼저 깨질 수 있다. 미분 검산의 통과를 적용 범위의 강건성으로 해석하면 안 된다.

또한 같은 score law·offset 아래에서 다음을 직접 증명했다.

\[
G_K(0)=0\text{ for every }K\ge1
\quad\Longleftrightarrow\quad E[h\mid s]=0.
\]

유한 L개 score level에서는 첫 L개 count의 stationarity만으로도 충분하다. 따라서 균형은 단순한 증명 편의가 아니라 **모든 count에서 같은 reference를 비교할 수 있는 조건**에 해당한다. 일반 비대칭 계에서는 보통 K에 따라 이동하는 equilibrium을 비교해야 한다. 이 결과는 기존 moment uniqueness와 total positivity의 직접 적용이며 새 학술적 기여로 승격하지 않는다.

35개 고정 조건에서 분해식과 독립 tuple 차분을 검사했다. 작은 score jitter에서는 count별 stationary 위치가 달라졌다. 기존 정리가 틀렸거나 작은 비대칭이 반드시 불안정성을 만든다는 결론은 아니다. [증명·전체 미분식](assumptions/general_derivative.md), [실행 근거](assumptions/README.md).

## 3. 온도와 sampler 특수성

정책을 raw cosine score에서 `exp(−t*s)`로 고정하고 loss 온도 tau를 바꾸면, 기존 증명이 요구하는 무차원 반응 강도는

\[
\theta=t\tau>1
\]

이다. Loss 온도만 바꾸는 것과 sampler도 s/tau에 적용하는 것은 다른 정책족이다. 고정된 K5..11 숫자를 일반적 안정 구간처럼 읽을 수 없다. theta≤1은 기존 no-rescue 증명 밖이며 그 자체가 실패나 불안정성의 증거는 아니다.

반대로 같은 exponential-mixture 족에서 t≤0이면 harder-negative 선호 또는 uniform이 된다. Beta>0인 기존 **exchange-balanced affine 방향**에서는 모든 유한 K에 대한 curvature가 양수임이 기존 식에서 바로 나온다. 다른 방향이나 일반 hard-negative 학습까지 안정하다는 정리가 아니다. 이는 현재 메커니즘의 정책 특수성을 더 명확히 하는 따름정리다.

96개 고정 tuple 조건과 별도 finite difference를 실행했다. 결과는 위 직접 유도와 일치한다. 이것 역시 새 top-journal 중요성의 증거로 세지 않는다. [정확한 rescaling과 범위](temperature_scope.md).

## 4. 비 oracle 접근성: 실제로 나아진 근거

기존 MLP 실험과 별도로, 충분한 차원 d16에서 N16개 unit embedding을 Gaussian random으로 초기화했다. 잠재 요인을 이용한 square 초기화나 고유방향 perturbation, warmup을 사용하지 않았다. 같은 joint-K population 목적과 positive channel `.95I+.05U_class`를 사용했다. Primary6101, 별도 confirmation6201을 실행했다.

| Adaptive 조건 | 실제 관측 | 해석 |
|---|---|---|
| K4 | Injective rank2 rectangle, best-square 오차 약.076–.081 | 이론의 특정 square와 다른 geometry로 이동 |
| K8 | 두 seed 모두 best-square 오차 약3.3e-10, view variance 약3.4e-10, field norm<1e-7 | 이 작은 free-embedding 모형에서 square 근방에 실제 접근 |
| K16 | View variance 약.054, field norm 약1.6–2.1e-5, 시간 상한에서 종료 | 퍼짐 관측. 미수렴이며 endpoint 정리의 직접 확인으로 세지 않음 |

12개 base run과6개 half-step 비교를 실제 실행했다. 시간 제한을 scientific outcome 전에 적용해 나머지 네 seed는 실행하지 않았다고 명시했다. 새 두 seed의 결과는 보편적인 도달 확률이나 shared-network 일반성이 아니다.

이 양성 결과로 ‘오직 oracle 초기화에서만 보이는 현상’이라는 강한 반론은 **이 finite lookup 모형 안에서는** 약해졌다. 기존 MLP0/3 실패를 삭제하거나 성공으로 바꾼 것은 아니다. K4/8/16만 검사했으므로 random-start 실험으로 정확한5..11 경계 전체를 확인했다고 쓰지 않는다.

Frozen 비교는 초기 random q0를 고정한다. 나중의 adaptive 정책과 분포·모집단 목적도 달라지므로 endpoint 차이는 pure local sampler-response 항만의 인과 증거가 아니다. Pseudoinverse readout 수치는 특정 rcond 아래의 측정이며 최적 선형 성능·margin·정보량이 아니다. LP margin은 계획에 언급됐지만 미실행이라고 기록했다. [코드·사전 기준·모든 결과](nonoracle/README.md).

## 5. 안정성이 곧 품질은 아니라는 실제 반례

기존 upper-K 경계에 해당하는 normal-view 방향을 그대로 검사했다. 실제로 K8에서는 restoring, K16에서는 repelling이었다. 그러나 그 방향의 표현

\[
f_\alpha(a,b,v)=
\bigl(\sqrt{(1-\alpha^2)/2}\,a,
\sqrt{(1-\alpha^2)/2}\,b,\alpha v\bigr)
\]

는 0<alpha<1에서 두 semantic bit를 선형으로 완벽히 보존하고, view bit를 추가한다. 불안정한 방향이라는 사실만으로 정보가 나빠졌다고 할 수 없다. 이 식은 nonlinear flow의 endpoint를 증명한 것이 아니라, 부호에서 곧바로 해로움을 추론할 수 없다는 반례다.

View task는 positive-invariant가 아니라는 한계도 분리했다. 그래서 기존 K4 rectangle에서 **둘 다 positive-consistent인 a,b task**만으로도 비교했다. 선언한 Gaussian noise sigma.5 아래 balanced accuracy는 두 task 각각.9213504이고, rectangle에서는 a=.9274697, b=.9146373이다.

- a의 평가 비중이.9면 utility는.9261864로 상승한다.
- a의 평가 비중이.1이면.9159206으로 하락한다.
- 무잡음 선형 접근성은 둘 다 완벽하다.

같은 불안정성·같은 endpoint를 좋다고 할지 나쁘다고 할지는 task, noise, worst-case 기준 등에 의존한다. 이 익숙한 원리를 새 논문 기여로 주장하지 않는다. 현재 선택한 균형을 중요한 목표라고 보려면 독립적인 정당화가 필요하다는 뜻이다. [직접 실행과 원문 대조](value_audit/analysis.md).

추가로, 이 positive graph와 score-only sampler는 모든 class permutation에 대해 equivariant하다. 세 가지 square opposite-matching이 목적함수상 동등하다. 각 square는 a,b,ab 중 두 partition을 선형 분리하고 하나를 XOR로 남기지만 모두 무잡음 정보는 보존한다. 따라서 원래 이진 요인 a,b를 특별히 원하는 것까지 이 학습 정보만으로 정할 수 없다. [대칭성 증명](nonoracle/symmetry_lemma.md).

## 6. 사용자 비판8항목에 대한 현재 답

| 비판 | 현재 처리와 남은 공백 |
|---|---|
| 1. 정확성과 중요성의 혼동 | 인정하고 top50 판정 철회. 새 일반정리가 있다는 사실만으로 중요성 통과 처리하지 않음 |
| 2. 일반성 과장 | 공통 reference stationarity와 balance의 동치를 증명해 범위를 명확히 함. Generic 비대칭 학습의 count-dependent equilibrium은 여전히 미해결 |
| 3. 정책·온도 특수성 | theta=t*tau와 반대 sampler 방향의 직접 따름정리 확인. 현재 법칙은 일반 adaptive/hard-negative 이론이 아님 |
| 4. Oracle MLP의 한계 | 실제 nonoracle random free embeddings에서 좁은 양성 근거 추가. Shared network와 일반 데이터의 설명력은 여전히 미확보 |
| 5. 불안정성의 학습 의미 | 정보 추가·접근성 유지와 task 비중에 따른 품질 역전 반례. 현재 중요성 공백의 핵심 |
| 6. 구별됨과 중요한 신규성의 차이 | Conditional novelty 후보는 유지하되 top-level 기여 판정은 보류 |
| 7. 두 불안정성 교집합의 의미 | 정확한 조합은 유지. 동시 유지 목표가 독립적으로 중요한 이유는 아직 입증되지 않음 |
| 8. 검증량·내부심사 과대해석 | 계산·재실행은 기술 신뢰도로만 기록. 내부 찬성이나 새 실행 수로 중요성을 보상하지 않음 |

## 7. 투자 판단

현재 결과 전체를 기각할 근거는 없다. 이번 nonoracle 접근성은 실제 진전이며, 가정의 특성화도 이후 분석을 정확하게 만든다. 그러나 **현재 framing으로 최상위 논문 완성을 밀어붙이는 장기 투자는 권고를 보류한다.** 더 많은 curvature 검산이나 같은 안정 구간 재현으로 핵심 공백을 메울 수 없다.

추가 투자를 정당화할 핵심 결과는, 학습상 독립적으로 중요한 목표를 먼저 고정한 뒤 기존 정적 repulsion/graph 설명으로는 얻을 수 없던 판정을 현재 count/response 법칙이 제공한다는 연결이다. 예를 들어 robustness나 finite-label 접근 비용을 택한다면 그것이 단지 특정 geometry를 선호하도록 임의로 고른 평가가 아닌지도 검증해야 한다. 이 연결은 **미완의 핵심 연구**다. 현재 원고를 완성하는 선택적 후처리라고 부르지 않는다.

그 연결이 성립하지 않으면 현재 정리와 코드를 기술 결과로 보존하고 이 framing의 논문화를 중단하는 것이 타당하다. 사용자가 요청한 ‘정확한 정리와 중요한 문제 사이의 거리’를 새 문서 분량으로 덮지 않는다.

## 재현

[실행 안내](reproduction.md), [가정 분석](assumptions/README.md), [학습 접근성](nonoracle/README.md), [중요성 감사](value_audit/README.md). 이전 round3 원고·심사·manifest는 과거 snapshot으로 보존했고 현재 README에 판정 철회를 표시했다.
