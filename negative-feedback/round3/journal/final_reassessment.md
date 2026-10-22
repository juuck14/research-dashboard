# 고정 JMLR 기준에 따른 개선 후 최종 재심

2026-10-22. 심사 대상은 현재 확보된 정리와 저장된 결과다. [사전 target](protocol.md), [고정 gate](fixed_rubric.md), [게재 원문 비교](source_audit.md)를 바꾸지 않았다. 이 심사는 다른 담당자의 동의 여부를 근거로 삼지 않는다. 정리 파일·증명·코드·원시 출력과 직접 읽은 원문을 근거로 한다.

## 1. 판정

**검증된 수정 방향의 이론 논문에는 핵심50% 도달로 판정한다.** 주 target은 여전히 JMLR다. 이는 채택 보장이나 완성 원고의 외부 심사를 대신하는 판정이 아니다. 최초의 semantic-information-erasure 논문이나 일반적인 실제 SSL cutoff 논문에 대한 통과도 아니다.

판정이 바뀐 이유는 seed·문서·계산 개수의 증가가 아니다. Round2에는 square의 국소 부호와 별개의 one-negative neural compression이 있었지만, 지금은 다음 세 결과가 연결돼 있다.

1. Bounded finite/continuous exchange-balanced population에서, **모든 finite K 중 어느 하나라도 scalar mode를 안정화할 수 있는지**를 판정하는 필요충분조건과 한번만 가능한 부호 전환을 증명했다.
2. 임의의 stationary score-regular class geometry에서, normal view mode가 요구하는 positive-graph gap이 K에 따라 엄격히 증가함을 증명했다.
3. 전체 square/view 모델의 모든 접공간 mode를 합쳐, 서로 반대인 두 count 조건의 교집합이 정확한 full local-stability interval임을 증명했다. 실제 joint-K shared-parameter flow가 같은 종류의 예측을 검사한다.

이제 남는 중심 지식은 계산하기 편한 square에서 특정 숫자를 얻었다는 것이 아니라, **negative 수 증가가 한 mode의 회복을 가능하게 하는 조건과 다른 mode의 유지를 어렵게 하는 조건을 구분하고, 회복 가능성과 불가능성을 판정하는 구조**다. 이 수정은 원래의 중요한 질문인 representation-dependent sampling과 학습 안정성의 관계를 유지한다. 정보 소실을 증명하지 못했다는 사실을 다른 이름으로 숨기는 수정이 아니다.

## 2. 직접 확인한 근거와 실제 범위

다음 파일을 직접 읽었다.

- `../foundations/multilevel_theorem.md`: tagged curvature, score single crossing, count에 따른 tagged-weight ordering, no-reentry, Q criterion, hypercube realization.
- `../foundations/continuous_population.md`: non-atomic extension의 적분·미분 교환, product-of-spheres realization과 analytic floor.
- `../foundations/general_normal_graph.md`: stationarity와 score regularity를 분리한 normal block 및 count ordering.
- `../neural/view_theorem.md`: 전체 class/view mode 분해, 두 조건의 필요충분 결합, upper threshold monotonicity.
- `../neural/window_parameter.py`, `results/window_parameter_summary.json`, `results/mixing_interval_certificate.json`, `results/graph_summary.json`: 실제 field 계산, integration 방식, 해당 예측과 원시 출력의 연결.
- `../foundations/results/continuous_summary.json`: continuous density/moment/quadrature 및 독립 tuple 계산의 저장된 수치 확인.
- `../review/window_proof_audit.md`: 독립 rational certification과 standard ODE 재실행의 구체적인 대상·방법·출력. 그 담당자의 최종 평가는 이 심사의 증거가 아니다.

**증명에 대한 직접 판단.** Conditional exchange balance는 각 score에 조건부인 h의 cross terms를 제거한다. Affine score path에서 남는 tagged integrand의 두 변화, 즉 local margin의 개선과 score weight의 MLR tilt가 결합돼 sign no-reentry를 준다. Bounded continuous law에서는 denominator weight의 양의 하한과 bounded derivative가 각 고정 K에서의 dominated differentiation을 정당화한다. 따라서 finite exact ties에만 의존한다는 이전 반론은 연속 product realization으로 해결됐다. Exchange symmetry와 affine path라는 substantive 조건은 유지된다.

General normal-view block은 모든 class-center span에 수직이므로 first-score derivative가0이다. 따라서 sampler-response가 없는 frozen curvature와 같다. Zero class-view mean은 negative cross terms를 제거하고, positive graph는 Dirichlet form을 준다. 이 계산으로 얻는 gap 요구량 `xi_K=R_K/B_K`의 증가가 한 square를 벗어나는 결론이다. Stationarity를 transitivity나 동일 score histogram에서 자동 도출하지 않는 latitude 반례도 중요하다.

**실행 결과에 대한 판단.** Continuous `m=2,r=3`에서 epsilon.25는 K64까지 unstable이지만 analytic floor상 결국 stable이다. 이는 finite horizon 부재를 no-rescue 증명으로 오인하지 않은 좋은 통제다. Epsilon.25의 `m>=3` no-rescue는 이 관찰이 아니라 analytic floor 판정에서 나온다. Full square window의 K5..11은 grid가 아니라 K4/5·K11/12 certified signs와 두 monotonicity 증명으로 나온다.

Shared MLP의 K4/8/16 결과는 updating policy의 growth/contraction/growth와 frozen의 low-K contraction/high-K growth를 구분한다. 이는 old one-negative/joint-K mismatch를 실제로 해결한다. 그러나 constructed reference, surjective tangent Jacobian, eigenmode perturbation을 사용하므로 일반 training의 대표성에 관한 독립 증거로 세지 않는다. 원래 코드는 linearly implicit integration을 사용한다. Step refinement 및 별도의 unpreconditioned ODE 확인이 있는 범위에서 flow 검산이라고 부를 수 있으며, 이를 그대로 ordinary SGD 실험이라고 쓰면 안 된다. Ordinary warmup의 applicability 실패3/3은 그대로 남긴다.

## 3. 기존 수학·선행연구를 제외하고 남는 신규 지식

### 표준 수학은 기여에서 제외한다

Athey의 *Characterizing Properties of Stochastic Objective Functions*, revised1999 [primary PDF](https://web.mit.edu/athey/www/CPSO99.pdf), §3.3.1 Corollary5.3과 증명(pp26–27)을 직접 확인했다. Single-crossing integrand의 부호가 likelihood-ratio 조건 아래 보존된다는 aggregation 원리는 기존 결과다. Laplacian diagonalization, bounded convergence, ordinary neural pullback/inertia도 새로운 수학으로 세지 않는다.

현재 no-reentry는 그 aggregation 원리를 적용하는 결과다. 다만 적용 조건이 학습장에 대해 성립한다는 사실을 가정하지 않고 도출한다. Contrastive-specific tagged field에서 `a_K`의 score crossing과 Stieltjes weight의 count ordering을 함께 증명하고, 이를 Q criterion에 연결한 부분이 추가된 지식이다. 이 차이는 ‘기존 논문에 현재 식이 없다’는 이유와 다르다. 기존 원리를 아는 독자도 현재 field가 그 조건을 만족하는지와 그 결과 어떤 finite K가 가능한지는 별도로 알아야 한다.

### 가장 가까운 ML 원문과의 차이

자세한 원문 위치는 [graph audit](graph_extension_audit.md)에 있다.

- **HaoChen et al2021:** Augmentation graph와 spectral-loss optimum의 linear-probe 보장. 현재의 local detached adaptive InfoNCE count classification과 다르다.
- **Tan et al2024:** Fixed positive graph의 Laplacian attraction과 all-object InfoNCE regularizer 분해. Positive spectrum을 사용하는 것 자체는 이 연구의 신규 지식이 아니다. Finite iid count에 따른 두 반대 임계조건은 그 정리의 결론이 아니다.
- **Zhang/Wang/Wang JMLR2025:** Graph radius/spectrum으로 intraclass variance를 제어하지만 encoder의 alignment를 별도로 가정한다. 현재는 그 collapsed geometry가 local dynamics에서 가능한 count 범위를 묻는다. 그 논문을 반박한 결과는 아니다.
- **Li/Neuman JMLR2026:** Graph consistency와 neural approximability가 공백이다. 현재는 count와 local dynamics가 공백이다. Network로 표현 가능하다는 것과 학습에서 안정하다는 것을 혼동하지 않는다.
- **Awasthi et al2022:** Fixed marginal/conditional-independent class setting의 global NCE optima. 현재 local result는 이 positive global theorem의 반례가 아니다.

### 추가로 확인한2026 문헌

**Cai, Zhang, Liu, Shi, ICML2026**, *The Geometric Mechanics of Contrastive Representation Learning*. [공식 기록](https://proceedings.mlr.press/v306/cai26o.html), [실제로 읽은 게재 PDF](https://raw.githubusercontent.com/mlresearch/v306/main/assets/cai26o/cai26o.pdf). PDF를 직접 받아 §2–3, Theorem3.1, 그 proof의 relevant part, AppendixF.1을 확인했다. Marginal data-law sampling 아래 large-batch value/gradient consistency와 low-temperature variational geometry를 다룬다. Finite-K detached-policy feedback이나 현재 count window는 도출하지 않는다.

**Li, Wei, Yang, Ying, ICML2026**, *Statistical Consistency and Generalization of Contrastive Representation Learning*. [읽은 primary PDF](https://arxiv.org/pdf/2605.02116), §2의 정의·Remarks2.1–2.2 및 §4의 error decomposition을 확인했다. Fixed data laws의 population objective와 finite-negative approximation/generalization이 대상이다. 현재의 closed-loop local law와 동일하지 않다.

이 두 편은 새로 찾은 관련 연구이며, 처음 고정한 journal benchmark를 더 쉬운 conference benchmark로 바꾸는 데 사용하지 않았다. 원문 접근 실패나 검색 결과 없음은 신규성의 근거로 쓰지 않았다.

## 4. 중요성 판정이 달라진 구체적인 이유

‘더 많은 negatives가 항상 좋지는 않다’는 일반론은 이미 알려졌다. ‘Weak positive graph는 좋지 않다’도 알려졌다. 이것만 남았다면 여전히 미도달이다.

이번에 새롭게 가능한 판정은 다음과 같다.

1. **Large-K limit만으로 finite budget 전체의 불가능성을 판정할 수 있는 조건을 안다.** 일반적으로 limiting curvature가 negative라고 해서 중간 K의 안정 구간이 없다는 결론은 나오지 않는다. 현재 exchange-balanced theorem은 정확한 count ordering을 증명해 이 추론을 가능하게 한다. Q=0에서도 모든 finite K가 strictly negative라는 경계까지 확보한다.
2. **한 mode에서 더 많은 negatives가 도움이 되는 이유와 full geometry를 안정화하는 조건을 분리한다.** Scalar mode의 no-reentry와 full local stability의 유한 interval이 함께 참일 수 있다. 이는 서로 모순되는 empirical count effects를 같은 메커니즘으로 뭉뚱그리는 설명을 막는다.
3. **Augmentation strength를 고정한 채 count를 늘리는 선택이 어떤 다른 제약을 강화하는지 안다.** General stationary geometry의 normal block에서 필요한 gap이 증가한다는 결과는 square의 계수 하나 이상이다. Full square example은 그 상충이 실제로 양립 가능한 count를 제한한다는 완성된 witness다.

따라서 현재 기여는 성능을 조금 높이는 법이나 실전 hyperparameter rule이 아니라, conditional graph theory·large-K limit·local learning dynamics 사이의 서로 다른 질문을 구분하고 count-rescue 가능성을 분류하는 이론이다. 이는 사전 기준에서 허용한 **구조적 이론 경로**다. Ordinary warmup이 square를 방문하지 못했다는 이유만으로 이 경로를 다시 막는다면, 처음부터 허용했던 pure theory 경로에 사후적인 실전 벤치마크 조건을 추가하는 셈이다.

동시에 이 결과가 arbitrary policies나 arbitrary learned geometry를 설명한다고 하면 이 중요성 논증은 성립하지 않는다. 핵심 가정이 적용되는 명확한 class를 연구하는 이론 논문으로 정직하게 제시해야 한다.

## 5. 비보상형6-gate 재심

| 항목 | 수정된 이론 논문 판정 | 근거 | 가장 강한 남은 반론과 적용 한계 |
|---|---|---|---|
| 신규성 | **통과** | 기존 MLR/Laplacian 원리를 제외하고도, contrastive-specific finite-count ordering·sharp rescue criterion·상충하는 count constraints의 exact conjunction이 남는다. 확인한 가장 가까운 primary theorem의 직접 결론이 아니다. | 모든 출판물을 빠짐없이 검색했다는 증명은 불가능하다. ‘새 수학 원리’나 graph theory 최초라는 과장은 금지한다. |
| 중요성 | **통과 — 구조적 이론으로** | 위 세 판단이 limit만 보거나 한 mode만 보는 분석으로는 얻어지지 않는다. Broad bounded exchange-balanced laws와 여러 regular equilibrium geometry에서 count의 역할을 구분한다. | 실전 성능·정보소실을 보여주는 결과는 아니다. 그 응용 claim을 대표 기여로 다시 넣으면 이 통과를 사용할 수 없다. |
| 중심 결과 | **통과** | No-reentry와 Q necessity/sufficiency, continuous realization, normal-gap ordering, entire-square spectrum와 certified finite interval이 현재 결과 형태로 존재한다. | Full stability outside square는 미완료다. 현재 대표 기여에 그것이 필요한 것처럼 원고를 쓰면 통과가 무효다. |
| 설득력 | **통과 — 명시 범위 안에서** | Population theorem·gradient oracle·전체 mode·fixed-vs-updating control·actual joint-K parameter-flow가 같은 결론을 검사한다. Static upper boundary와 feedback lower boundary를 분리한다. | Constructed reference의 수치 검증은 ordinary learning의 representative evidence가 아니다. 원래 warmup 실패와 mild injective endpoint를 지우면 안 된다. |
| 범위 | **통과 — 조건을 유지하면** | Finite ties만의 결과에서 bounded non-atomic exchangeable realization으로 확장했고, upper block은 square 밖이다. 실패 조건과 inactive cases를 정확히 명시한다. | Exchange balance, affine score path, iid sampling, exponential-mixture policy, regular stationary reference가 substantive다. Generic asymmetry/heterogeneous anchors/global attractor는 보강으로 자동 획득되지 않는다. |
| 연결성 | **통과** | 대표 질문은 count에 따른 local feasibility이고, 세 중심 정리와 controlled neural check가 그 질문을 구성한다. 원래 정보소실 claim의 부정적 결과도 논문 경계를 정한다. | Independent findings를 다 붙인 현상 모음으로 쓰지 말고, shared tagged-denominator count ordering과 서로 다른 mode의 competition을 중심으로 원고를 구성해야 한다. |

평균 점수를 만들지 않았다. 중요성 통과는 수치 정확성이나 seed 수로 보상한 결과가 아니다. **참인 제한 명제의 성립**과 **현재 수정 기여가 JMLR 독자에게 충분한 구조적 지식을 제공하는지**를 별도로 검토한 뒤 둘 다 충족한다고 판단했다.

## 6. 원래 claim과 수정 claim은 별도로 판정한다

| Claim | 판정 |
|---|---|
| Finite-K adaptive stability가 semantic factor의 정보 소실 경계다. | **기각.** 현재 endpoint는 mild injective compression이며 정보 소실과 다르다. |
| 현재 cutoff가 ordinary pretrained SSL에서 바로 쓸 수 있는 rule이다. | **미확보.** Warmup 적용 gate 실패, 일반 learned visitation 증거 없음. |
| Exact count-rescue/no-rescue와 positive-view constraint의 local feasibility 분류가 독립적인 이론 기여다. | **진행 권고·핵심50% 도달.** 결과가 존재하고 핵심 novelty/importance 논증이 현재 범위에서도 성립한다. |
| TPAMI용 visual SSL contribution도 이미 확보했다. | **미도달.** TPAMI를 낮은 대체 target으로 쓰지 않는다. |

## 7. 남은 작업: 핵심 미해결과 보강을 구분

**현재 수정 논문 성립을 위해 새 실험 성공을 기다릴 필요는 없다.** 남은 직접 작업은 정리·가정·증명의 단위를 통합하고, 원고에서 inherited tools와 추가된 학습 지식을 정확히 표시하며, raw artifacts와 claim을 연결하는 일이다. 정리의 독립적인 추가 검산과 presentation을 위한 theorem dependency 정리는 좋은 보강이지만, 독립 검토자의 승인 자체를 증거로 사용하지 않는다.

다음은 가치 있는 **새 핵심 연구**이지 현재 결과를 문장으로 확장하는 후처리가 아니다: generic asymmetric geometry의 full spectrum, heterogeneous anchor laws, arbitrary nonlinear score directions, 실제 training의 방문·basin·global endpoint. 이들이 실패해도 위에 명시한 이론은 남는다. 반대로 이들을 지금 대표 claim에 포함한다면 각각이 논문 성립을 좌우하는 미해결 과제가 된다.

선택적 보강으로는 continuous analytic example의 읽기 쉬운 그림, count/floor/gap의 다른 구체값, ordinary learning에서 다른 equilibrium을 보이는 반례 등이 있다. 이 결과가 없어도 대표 지식은 이미 존재한다. 반복 seed나 benchmark 수를 늘려 현재 중요성의 근거를 대신할 필요는 없다.
