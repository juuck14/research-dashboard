# 독립 재심: 참인 구조 정리와 최상위 학술지 기여를 구분한 판정

2026-10-22. 개선 담당과 분리한 검토다. [사전 질문](protocol.md), [고정 JMLR 기준](../journal/fixed_rubric.md)을 변경하지 않았다. 이 판정은 최초 round2의 추천을 재확인하는 절차가 아니다. 완성된 통합 원고의 주장 범위를 추가 대조했다. 검토자 간 동의는 아래 증거를 대체하지 않는다.

## 1. 현재 판정

**통합 원고 재심 후: 목표 도달 — 수정된 국소 population 이론 논문의 핵심50%에 한정.**

반면 “네 상태에서 알려진 원리를 계산한 것뿐”이라는 최초의 가장 강한 공격은 개선 후 결과 전체에는 맞지 않는다. 일반 점수 법칙, 연속 모집단의 실현 가능한 모형, 일반 class geometry의 view-normal 조건, 실제 joint-K shared-encoder 예측이 추가되었다. 실제 독립적인 연구 결과가 남았다. 따라서 원래 방향 전체를 중단할 근거도 충분하지 않다.

두 판정을 혼동하지 않는다. 제한된 국소 이론의 중심 결과와, 그 분류가 독립적인 구조적 기여를 이룬다는 근거는 확보됐다. 원래의 “의미 정보가 소실되는 경계”는 새 결과가 뒷받침하는 중심 주장이 아니다. 그 원래 논문의50%가 확보됐다는 판정은 하지 않는다. 현 판정은 게재 예측이나 채택 보장이 아니며, 아래 조건과 범위를 따른 이론 논문에 관한 것이다.

이 문서의 원고 전 초안은 중요성·범위를 부분 충족으로 두었다. [원래 판정과 요구를 수정하지 않고 보존](pre_manuscript_verdict.md)했다. 통합 원고를 직접 읽은 뒤 현재 판정을 수정했다. 바뀐 근거와 초안의 과도한 기준 적용은 마지막 절에 명시했다. 다른 검토자의 동의나 추가 검산 횟수로 변경한 판정이 아니다.

## 2. 실제 확보된 새 지식과 검산

**외부 문헌:** 기존 negative-sampling/shortcut 연구는 feature 선택과 suppression을, 고정 분포의 최적해 이론은 negative count와 population minimizer를, graph 이론은 positive 관계와 alignment를 이미 다룬다. MLR 아래 single crossing 보존도 Athey의 기존 원리다. [직접 읽은 원문과 차이](source_audit.md)에 본문 확인 범위와 접근 한계를 남겼다.

**직접 도출한 결과:**

1. Bounded exchange-balanced affine score direction에서 iid negative 수에 따른 안정→불안정 재진입이 불가능하다. 정확한 sampling-floor 식은 단순 K무한대 계산을 넘어, 그 floor 이하에서는 **어떤 유한 K도 해당 mode를 구원하지 못한다**는 필요충분 분류를 준다. [증명 독립 전개](multilevel_proof_audit.md).
2. 연속 product-of-spheres 모형에서도 그 법칙이 성립한다. 독립 후보들의 점수가 거의 확실히 다르더라도 조건부 derivative 분산은 양수다. 따라서 이 현상은 유한 원자의 exact score ties에만 의존하지 않는다. 다만 factor exchange symmetry와 affine score path는 여전히 핵심 가정이다.
3. Score-regular **stationary** class geometry의 zero-class-mean normal-view mode에서는 요구되는 positive graph gap이 K와 함께 엄격히 증가한다. Adaptive balance의 lower-K 조건과 이 upper-K 조건은 서로 다른 mode와 원인을 갖는다. Square에서는 모든 mode를 포함한 안정 K구간을 정확히 분류한다. [증명 검토](window_proof_audit.md).
4. Natural policy, floor.3, graph gap.05에서는 full local attraction이 정확히 K5–11이다. 프로젝트 구현을 import하지 않는 별도 [exact-rational interval 코드](window_certificate_check.py)를 작성·실행하여 K4/5 balance와 K11/12 gap의 네 부호를 재인증했다. [실행 출력](window_certificate_check.json). All-K 구간 판정에는 두 단조성 증명이 함께 필요하다.
5. 같은 q의 one/two-position joint law, source 수, unique-state-set 분포를 맞춰도 higher-order negative 관계로 attraction 부호를 바꿀 수 있다. 별도 ordered-tuple/직접 angular field로 [독립 확인](correlation_check.py)했다. 이는 정확한 불충분성 예제지만, “nonlinear expectation은 higher moments에 의존한다”는 일반 사실과 별도로 중요성을 평가해야 한다.

**직접 실행·재현한 결과:**

- K2/3/4 nonlinear rectangle roots를 별도 ordered-tuple field로 확인했다. K4 endpoint는 weak factor energy.46914를 갖는 injective geometry다. sigma.2 Gaussian Bayes accuracy는.999692로 balanced.999797과 차이가 작다. 따라서 K4/K5를 실질적인 의미 정보 소실 경계로 해석하는 주장은 반박된다. [코드](endpoint_check.py), [결과](endpoint_check.json).
- 새 oracle와 parameter-flow 코드를 직접 읽었다. 저장된 K4/8/16 shared-encoder 실험은 이제 joint-K denominator를 사용하며, low-K adaptive imbalance와 high-K frozen/adaptive view instability를 구분한다. 과거 one-negative MLP bridge의 불일치는 이 국소 명제에 한해 해결됐다.
- Preconditioner artifact 반론을 위해 standard DOP853 source를 출력 경로만 바꿔 실제 재실행했다. K16의 frozen/adaptive growth가 exp3와 각각 약7.0e-7/7.8e-7의 상대 차이로 일치한다. [재실행 출력](standard_ode_recheck.json). 이는 별도 gradient 구현이 아니라 독립 실행이며, oracle 정확성은 별도 multinomial/증명 근거에 의존한다.
- 이질 anchor law 혼합이 sign 재진입을 만들지 공격한 고정512개 모집단/K1–24 검색은 반례를 찾지 못했다. [실패 기록](anchor_mixture_check.json)과 [재생성 코드](anchor_mixture_check.py)를 보존했다. 이를 확장 정리의 증거로 사용하지 않는다.
- Positive의95%가 identity인 설정만 현상을 만들었다는 반론도 검토했다. Self-positive가 전혀 없는20-cycle의 정확한 gap `1-sqrt(10+2sqrt5)/4`를 독립 rational square-root enclosure로 계산하고 xi11/xi12와 비교했다. [코드](cycle20_certificate_check.py)와 [결과](cycle20_certificate_check.json)는 같은 K5–11 구간을 인증한다. 전체 theorem이 이미 임의 symmetric P를 포함하므로 새 정리가 아니라 중요한 가정 공격에 대한 구체적 corollary다.
- 요청했던 weak-positive ordinary arm의18개 출력도 읽었다. 같은 세 seed 모두 applicability gate를 다시 통과하지 못했다. K8→16의 view variance 증가는 탐색적 연관이며 exact-window replication으로 인정하지 않는다. 이 실패를 현 통과 판정에서 성공 증거로 사용하지 않았다.

## 3. 여섯 gate: 평균하지 않는 재심

| 기준 | 판정 | 구체적 근거와 가장 강한 남은 반론 |
|---|---|---|
| 신규성 | **통과 — 명시한 국소 분류에 한함** | 기존 fixed-risk 최적해, graph alignment bound, generic performative-response bound 또는 Athey의 aggregation 원리를 그대로 대입하면 새 all-K 조건이 나오지 않는다. Tagged finite-negative weights와 exponential-policy margin의 조건 검증이 필요하고, 그 결과 exact no-rescue/order 분류가 남는다. 반대로 MLR 자체, graph diagonalization, 네트워크 pullback 또는 sampling이 feature를 바꾼다는 큰 주장은 신규 기여에서 제외해야 한다. 문헌 검색 부재를 근거로 통과시킨 것은 아니다. |
| 중요성 | **통과 — 구조적 국소 이론으로 평가** | 대표 결과는 단순 square 상수가 아니다. 어떤 count가 충분히 크면 되는 경우와 어떤 유한 count도 구원하지 못하는 경우를 bounded finite/continuous score law에서 정확히 분리한다. 또한 일반 stationary class geometry에서 count를 늘릴수록 필요한 augmentation gap은 반대로 엄격히 증가한다. 따라서 한 mode의 count rescue를 전체 geometry rescue로 사용할 수 없고, count를 계속 늘리는 처방과 sampling floor/positive 관계를 바꾸는 처방을 구별하는 구조적 지식이 생긴다. 이것은 고정 JMLR 기준이 허용한 일반 분류 경로이며, 자연 이미지 성능이나 ordinary initialization 방문이 필수인 방법론 주장은 아니다. Balanced square 자체가 정보 보존의 필요충분조건이라는 주장은 여전히 불가하다. |
| 중심 결과 | **통과 — 수정된 국소 이론에 한함** | No-reentry, 모든 유한 K의 no-rescue floor, 연속 실현 모형, 일반 normal-block 단조 조건과 square의 exact full window가 증명·계산 결과로 존재한다. 핵심 식이 “앞으로 맞으면” 성립하는 상태는 아니다. 원래 semantic-erasure 명제에 대해서는 통과가 아니다. |
| 설득력 | **통과 — 이론과 실제 측정이 일치하는 범위** | Frozen/current sampler, joint-K/one-negative, class-mean/view modes, 수용량/parameter metric, preconditioned/standard ODE를 분리했다. 독립 exact certificate와 endpoint check도 일치한다. 이 통과는 reference를 일반 훈련이 방문한다는 뜻이 아니다. Ordinary warmup은 사전 applicability gate를3개 seed 모두 통과하지 못했다. |
| 범위 | **통과 — 일반 분류와 완결된 예제의 범위를 분리** | Semantic-mode 법칙은 finite/continuous exchange-balanced affine directions, view-mode 법칙은 row-regular stationary geometry의 normal block을 다룬다. 이 일반 법칙들이 충분히 넓은 구조적 기여를 주고, square는 그 제약들의 동시 작용을 모든 mode에서 완결하는 실현이다. 전체 안정 window를 arbitrary geometry로 확장하지 않는다. Correlated sampling, nonstationary transitivity, finite distinct-score 문제와 continuous exchangeable 실현으로 주요 가정의 작동 위치도 확인했다. Generic asymmetry·전체 nonlinear basin은 여전히 미해결이지만 현재 정리의 몰래 남긴 전제는 아니다. |
| 연결성 | **통과 — 수정 중심 주장에 한함** | Negative count를 통한 local rescue의 가능/불가능과 positive graph의 추가 제약이라는 한 질문으로 증명·계산·joint-K 실험을 연결할 수 있다. Endpoint/correlation 예제는 그 주장의 한계를 규정하는 보조 결과다. 이를 모두 “정보 소실을 교정하는 학습 원리”라는 더 큰 결론에 묶으면 이 gate도 미충족으로 돌아간다. |

각 gate를 별도로 통과시킨 것이다. 정확성·실행량으로 중요성을 상쇄하지 않았고, 중요성은 sharp all-count classification과 서로 반대되는 일반 spectral 조건이라는 독립적인 근거로 판단했다.

## 4. 강한 반론의 처리 결과

| 반론 | 처리 결과 |
|---|---|
| 원래 결과는 한 square의 curvature 상수 계산뿐이다. | **상당 부분 해결.** 일반 finite/continuous score 법칙과 다른 geometry의 normal-block ordering이 실제로 증명됐다. |
| Finite scores가 모두 다르면 조건부 균형이 h0을 강제한다. | **구조화된 연속 모형에서는 해결.** Product sphere의 연속 conditional h 분산은 양수다. Generic asymmetric finite cloud로 확대되지는 않는다. |
| Single-crossing aggregation은 새 수학인가? | **새로움 주장 철회가 정답.** Athey1999 Cor5.3의 기존 원리로 귀속하고, CL-specific 조건과 결론을 기여로 남긴다. |
| Upper-K 실패도 feedback 때문인가? | **그 해석은 반박됨.** Normal score derivatives가0이라 response가 없고 frozen도 같은 upper boundary를 갖는다. 두 원인 결합으로 기술해야 한다. |
| Balanced square 불안정은 정보 소실인가? | **그 강한 해석은 반박됨.** K4는 mild injective reshaping이다. Coarse K1의 asymptotic merging은 별개의 경계다. |
| Shared MLP는 실제 K를 바꾸는 실험이 아니었다. | **해결.** 새 oracle·parameter flow는 joint-K 조건과 같은 정량적 mode 질문을 직접 검사한다. |
| 특수 초기점의 이론을 network로 재표현했을 뿐 아닌가? | **국소 검증에는 타당하지만 적용성 반론은 남음.** Full-rank pullback은 기존 원리이고 constructed reference는 학습에서 선택된 geometry가 아니다. |
| Positive가 대부분 identity라서 만든 인공 현상인가? | **그 한정 반론은 해결.** Diagonal0인 cycle channel의 exact radical gap과 별도 derivative check에서도 동일 full window가 성립한다. 이것은 generic real augmentation 효과의 검증은 아니다. |
| 비선형 flow에서 다른 geometry로 갈 뿐이다. | **의미 해석을 수정함.** K4에서는 실제 그렇게 된다. Coarse point의 strict transverse gap은 standard attracting-manifold 이론으로 injective 이웃을 포함한 open local basin을 주지만, random initialization 확률이나 전체 basin은 알려주지 않는다. [검토](coarse_endpoint_audit.md). |

## 5. 남은 작업과 실패 시 영향

현재 수정 원고의 정리들이 성립하기 위해 아직 성공해야 할 핵심 실험은 없다. 다음 항목은 주장 확장 경로이며, 실패하면 그 확장 주장을 포기해야 한다. 현 국소 분류의 증거로 미리 계산하지 않는다.

1. **더 넓은 geometry의 full stability.** Square 밖의 energy-transfer/normal-block 법칙을 모든 나머지 mode와 결합하면 더 강한 이론이 된다. 그 확장에 실패해도 지금 증명한 일반 block별 법칙과 square full window는 남는다. 현재 한 mode의 부호를 전체 learning rescue로 확대하지 않는 것이 필수다.
2. **비 oracle 학습의 예측.** 사전에 고정한 관측/positive-channel 환경에서 일반 학습이 방문하는 geometry까지 예측하려면 별도 증거가 필요하다. 이 부분의 실패는 실용적 설계 지침이나 typical-training 주장을 막지만, 국소 구조 이론을 반박하지 않는다. 자연 이미지나 GPU가 반드시 필요한 것은 아니다. Constructed equilibrium에서 exp3를 다시 재현하는 것은 이 확장 검증의 대체물이 아니다.

논문 완성에는 기여의 범위·반례·전체 증명을 하나의 일관된 서술로 편집하고, 기존 정리와의 비교를 더 정밀하게 제시하며, 현재 원시 결과와 재현 명령을 안정적으로 묶는 일이 남는다. 정확한 추가 선행연구가 대표 분류를 이미 함의한다는 것이 발견되거나 독립 증명 오류가 발견되면 신규성·중심 결과 gate를 다시 열어야 한다. 이는 모든 연구에 남는 검증 위험이지 아직 수행하지 않은 실험을 현재 기여로 계산한 것은 아니다.

## 6. 선택적 보강과 핵심 과제를 구분

현재 증명 아래의 더 촘촘한 K grid, 같은 square의 추가 parameterization, 동일 oracle의 반복 finite differences, 표·그림·서지 형식 정리는 **선택적 보강**이다. 이 결과들이 실패하면 실제 구현 또는 주장 오류를 고쳐야 하지만, 그 양을 늘려 중요성 gate를 통과시킬 수는 없다.

Generic asymmetry에서의 정량 예측이나 비 oracle learning claim은 현재 증명의 단순 보강이 아니다. 그것을 별도 대표 기여로 삼으려면 **그 확장을 위해 필요한 핵심 연구**라고 표시해야 한다. 반대로 지금 증명된 제한적 국소 분류는 그런 후속 실험이 실패해도 사라지지 않는다.

## 7. 통합 원고 재심 기록

이 문서의 최초 버전은 새 결과와 코드·출력을 직접 확인한 뒤, 통합 원고 작성 전에 저장했다. 당시 판정은 중요성·범위 부분 충족이었다. 이후 `../manuscript.md` 전체를 읽고 abstract, 세 대표 기여, 정리·증명, 실제 실험, 한계를 대조했다.

재심에서 확인한 점은 다음과 같다.

- 대표 기여는 “특수 square의 exact coefficient”가 아니라, 무한-count 부호를 **모든 유한 count의 가능/불가능**으로 올리는 sharp 분류다. 임의 bounded continuous score law의 조건을 검증하고 정리하므로 한 예제의 추가 계산이라는 최초 공격으로는 이 결과를 제거할 수 없다.
- 두 번째 법칙은 square 밖 score-regular stationary geometry에서도 성립한다. 첫 번째 법칙의 성공을 전체 rescue로 확장하면 왜 틀리는지, 서로 다른 원인의 count 제약으로 정확히 보여준다. 모든 mode를 완결한 square는 일반 법칙의 대체물이 아니라 그 동시 실현이다.
- 원고는 “아무 모델에서 count를 늘리면 좋아지거나 나빠진다”는 generic 원리, graph connectivity의 최초 발견, feedback-induced global erasure를 주장하지 않는다. Upper boundary가 frozen에도 같다는 사실과 ordinary warmup의 실패도 숨기지 않는다.
- 초안에서 ordinary training이 reference를 방문하는 결과를 사실상 필수처럼 요구한 부분은 pure-theory 경로에 과도한 조건을 붙인 것이었다. 고정 rubric은 **실제로 새로운 일반 분류 또는 실패 원인**이 확보되면 natural-image 성공 없이도 통과할 수 있다고 명시한다. 현재 확보된 sharp 구조 분류를 그 기준으로 평가해 중요성·범위를 통과로 수정했다. 새 seed 수, 문서 분량, 다른 agent의 찬성은 그 이유가 아니다.

따라서 최종 판정은 **수정된 국소 이론 논문의 핵심50% 확보**다. 원래 의미 정보 소실 논문, 실제 필터링 방법의 성능 논문, 일반적 학습 cutoff 예측 논문의50%라는 판정은 하지 않는다. 이 구별은 여전히 핵심적인 제한이다.
