# Positive-graph extension: 가까운 원문과 기여의 경계

2026-10-22. 상태: 개선 중간 단계의 독립 문헌 검증. 이 문서는 최종6-gate 재심 판정이 아니다. [고정 기준](fixed_rubric.md)은 유지한다. 아래에서 **문헌 사실**, **현재 결과의 보고**, **검토자의 판단**을 분리한다.

## 실제로 읽은 가장 가까운 원문

### HaoChen, Wei, Gaidon, Ma (NeurIPS2021)

*Provable Guarantees for Self-Supervised Deep Learning with Spectral Contrastive Loss*. [공식 원문](https://proceedings.neurips.cc/paper/2021/file/27debb435021eb68b3965290b5e24c49-Paper.pdf).

**문헌 사실:** §3.1–3.3는 augmentation graph의 normalized adjacency spectral decomposition과 quadratic contrastive objective를 연결한다. Theorem3.7은 realizability, label recoverability, graph conductance 아래 population optimum의 linear-probe error를 제어한다. Theorem4.2는 excess loss와 eigengap을 통해 유한 표본에 연결한다. 확인한 회의 원문은12쪽이며, 별도 긴 supplement의 모든 증명을 읽었다고 주장하지 않는다.

**대조 판단:** 현재 detached adaptive InfoNCE Jacobian의 finite-K 임계값은 이 정리에 직접 대입해 얻는 결과가 아니다. 반대로 graph connectivity/spectrum이 표현의 class 구조를 제어한다는 큰 해석을 이번에 처음 발견했다고 주장할 수 없다.

### Tan, Zhang, Yang, Yuan (ICLR2024)

*Contrastive Learning is Spectral Clustering on Similarity Graph*. [공식 게재 원문](https://proceedings.iclr.cc/paper_files/paper/2024/file/52eb24c316c78cc144dfa54f1f4bb4ec-Paper-Conference.pdf).

**문헌 사실:** Theorem3.1과 AppendixA는 symmetric fixed positive graph와 all-object denominator를 사용하는 InfoNCE를 graph-Laplacian attraction과 representation regularizer로 분해한다. 실제 미니배치와 all-object 가정의 차이는 본문이 명시한다. Theorem4.2는 관련 pair-graph 구성을 CLIP으로 확장한다. 본문§3과 AppendixA의 해당 증명을 읽었다.

**대조 판단:** 일반 symmetric positive matrix를 diagonalize해 각 mode의 alignment 비용을 얻는 것은 새로운 spectral 원리가 아니다. 이 분해는 finite i.i.d. negative count와 representation-dependent detached sampler의 반응을 포함하지 않으므로, 현재 all-K 결과를 그대로 함의하지도 않는다.

### Zhang, Wang, Wang (JMLR2025)

*An Augmentation Overlap Theory of Contrastive Learning*. [공식 기록](https://jmlr.org/papers/v26/22-1009.html), [실제로 읽은 저자 본문](https://arxiv.org/html/2511.03114v1). 전체 원문 확인 범위와 journal PDF 접근 한계는 [source audit](source_audit.md)에 기록했다.

**추가 확인한 문헌 사실:** §5.2 Theorem10은 connected graph와 ε-alignment를 가정해 graph radius로 intraclass variance를 제어한다. §5.3 Corollary12는 인접행렬 eigenvalue ratio로 표현한다. §4의 negative count 항은 Monte Carlo approximation gap이다.

**대조 판단:** 그 정리는 alignment를 가정한다. 따라서 어떤 finite-K dynamics가 alignment를 유지하거나 깨뜨리는지를 자동으로 설명하지 않는다. 현재 window가 참이어도 이 bound를 반박하는 것은 아니다. Negative count가 증가하면 모든 학습 성질이 단조롭게 좋아진다는 정리로 오독한 뒤 이를 깨는 식으로 중요성을 부풀려서는 안 된다.

### Li, Neuman (JMLR2026)

*Consistency of Augmentation Graph and Network Approximability in Contrastive Learning*. [공식 게재 원문](https://jmlr.org/papers/volume27/25-1466/25-1466.pdf). 확인한 가정·Theorems11–13·증명 범위는 [source audit](source_audit.md)5번에 있다.

**대조 판단:** Graph 자체의 statistical/continuum consistency와 optimum의 neural approximability는 현재 학습 dynamics와 다르다. 이 논문이 존재한다는 이유만으로 current theorem을 기각할 수 없다. 그러나 graph spectrum의 학습 연결을 주장하려면 최적해의 존재, parameterization, dynamics 사이의 어느 공백을 해결했는지 정확히 말해야 한다.

## 보고된 새 결과가 실제로 추가하는 것

다음은 담당자의 중간 보고이며 최종 theorem·증명의 독립 심사는 아직 진행 중이다. Full positive graph의 class-mean mode에는 기존 finite-K threshold가 남고, within-class view modes에는 positive graph spectrum이 들어간다. Graph gap 조건과 class-mean feedback 조건이 반대 방향의 K 제약을 주어, 특정 natural policy에서는 모든 비회전 mode가 안정인 K가 정확히 유한 구간이 될 수 있다는 주장이다. 이 결과는 K1–128 grid를 관찰한 주장보다 강하다. 실제 all-K 증명과 모든 mode의 충분·필요 조건이 완료됐는지는 별도 확인해야 한다.

**남을 수 있는 독립적 지식:** 단순히 ‘많은 negative가 나쁠 수 있다’가 아니라, negative count가 같은 system의 두 서로 다른 mode를 반대로 움직이며, 그 사이에서만 local stability가 가능하다는 mechanism-separated classification이다. 특히 한 경계만 보면 영구적 rescue로 오판하는 상황을 구체적으로 구별한다. 일반 finite-score class의 no-reentry 법칙까지 연결된다면, 한 square 예제의 숫자보다 더 넓은 구조가 남는다.

**기존 지식으로 남겨야 하는 부분:** Positive attraction과 negative repulsion의 경쟁, weak connectivity의 한계, positive graph eigenmode의 diagonalization, false negatives가 nuisance invariance에 불리할 수 있다는 직관 자체다. 현재 확인한 원문에 같은 식이 없다는 것은 독립 기여의 충분조건이 아니다.

## 가장 강한 현재 반론과 통과해야 할 검증

| 반론 | 현재 구분 | 중요성에 미치는 영향 |
|---|---|---|
| Upper-K boundary는 adaptive feedback의 결과가 아니라 frozen objective의 취향이다. | 담당자도 frozen에서 나타나는 boundary라고 보고했다. 두 메커니즘을 분리하면 반론을 숨긴 것은 아니지만, upper boundary를 feedback-induced semantic failure라고 부르면 틀리다. | Combined window의 새 해석은 남을 수 있으나 새 feedback 원리의 수는 늘지 않는다. |
| 이미 알려진 graph attraction/repulsion tradeoff에 finite-K 계수를 대입했을 뿐이다. | 그 가능성을 배제하려면 계수 계산 이상인 monotonicity/no-reentry/필요충분 분류의 핵심 비자명성을 증명하고, 기존 theorem으로 얻을 수 없는 판정을 명시해야 한다. | 정확하지만 지역적인 phase diagram이 top journal의 중요한 지식인지 판단하는 핵심이다. |
| Stable square가 왜 바람직한지 불명확하다. | Balance, view collapse, class separability는 서로 다른 성질이다. Square attraction은 factor 정보 보존의 필요조건도 충분조건도 아니다. | 원래 semantic factor boundary 동기를 직접 지지하지 못하면 local stability 논문으로 중요성을 다시 평가해야 한다. |
| Shared MLP 검산은 특수 equilibrium을 network로 다시 표현한 것뿐이다. | Constructed initialization/full-rank tangent 확인은 구현·용량 대안을 제거하지만, 그 equilibrium이 일반 학습에서 선택되거나 방문된다는 증거는 아니다. | 자연 이미지가 반드시 필요한 것은 아니다. 다만 실제 learning claim을 하려면 같은K 예측의 독립적 parameterized 검증이 필요하다. |
| 새 graph condition이 all-K 결과라 해도 restricted model의 내부 분류다. | 참일 수 있다. 그런 제한 자체를 감점하지는 않는다. | 그 분류가 기존 intuition을 어떤 상황에서 틀린 판정으로 이끄는지, 새 design/understanding을 얼마나 바꾸는지 별도로 확보해야 한다. |

### General finite-score 결과의 구체적인 범위 반론

이는 문헌 인용이 아니라 가정으로부터 직접 확인되는 사실이다. Finite support에서 모든 score가 서로 다르면 조건 `E[h|s]=0`은 각 support point에서 `h=0`을 강제한다. 따라서 이 조건 아래의 nonzero perturbation은 반복 score가 있는 구조를 필요로 한다. 여러 score level, 많은 상태, hypercube 요인으로의 확장은 실제 구조적 진전이지만, generic geometry의 열린 집합을 덮는 결과와 동일하지 않다. Exact ties가 자연스러운 semantic symmetry인 경우는 있을 수 있다. 그 경우 그 symmetry class의 연구적 중요성을 설명해야 하며, 단순히 상태 수가 커졌다는 이유로 symmetry 의존이 사라졌다고 하면 안 된다. 작은 perturbation에서 고정된 finite K의 부호가 continuity로 유지된다는 사실도 모든 K에 대한 exact no-reentry의 일반적 유지와 구분한다.

## Interim 결론

확인한 primary sources는 새 exact finite-K window의 직접적인 따름정리를 제공하지 않는다. 동시에 ‘graph gap이 중요하다’와 ‘negative 수 증가가 항상 유리하지 않다’는 일반 설명은 신규 기여로 사용할 수 없다. All-K 두 경계의 구조와 실제로 바뀌는 판정이 핵심이다. 현재 문헌 조사는 literal duplication 반론을 좁혔으며, 중요성·대표 결과의 완결성·실제 학습 연결을 통과시켰다는 뜻은 아니다. 최종 판정은 완성된 정리, 원시 결과, 독립 재심을 같은6개 gate에 적용해 기록한다.
