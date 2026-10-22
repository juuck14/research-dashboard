# 게재 논문 원문 대조와 고정한 질적 기준

2026-10-22. Target은 [사전 규약](protocol.md)에 고정했다. JMLR를 주 target으로, TPAMI를 실제 visual/SSL 연결이 있는 경우의 후보로 둔다. 아래 네 편은 분량이나 실험 개수의 모방 대상이 아니라, 가정이 제한되어도 독립적인 지식을 만드는 방식의 비교 대상이다. 논문 게재 사실만으로 그 모든 해석이나 증명이 무조건 옳다고 간주하지 않는다.

## 1. An Augmentation Overlap Theory of Contrastive Learning

Qi Zhang, Yifei Wang, Yisen Wang. JMLR26(228):1–42,2025. [공식 게재 기록](https://jmlr.org/papers/v26/22-1009.html), [게재 PDF](https://jmlr.org/papers/volume26/22-1009/22-1009.pdf), [읽은 저자 원문 HTML](https://arxiv.org/html/2511.03114v1).

**실제로 확인한 원문:** §3 문제 설정, §4 negative의 Monte Carlo 해석, §5 Theorem5/Proposition6와 augmentation graph, §6 graph 연결성과 augmentation 강도, §7 ARC/GARC와 실험, AppendixA의 관련 증명 구간 및 AppendixB 실행 범위. 게재 PDF는10.9MB로 도구 한도에 걸렸으므로 본문 검토는 저자 arXiv판을 사용했다. 모든 줄이 journal PDF와 동일한지 byte 비교한 것은 아니다.

**외부 문헌에서 확인한 사실:** Conditional independence가 positive 학습을 class 중심 정렬로 바꾸는 강한 가정임을 지적한다. Label consistency만 남기면 downstream bound에 제어되지 않는 class 내 variance가 생기며, augmentation graph의 연결성으로 이를 제어한다. §4는 negative들을 Monte Carlo 항으로 다루어 count-dependent error를 분석한다. Synthetic graph 실험과 CIFAR/ImageNet의 augmentation·모델 평가 검증을 연결한다. 다만 classification 범위를 벗어난 임의 semantic factor 복구나 실제 SGD의 global convergence까지 증명하는 논문은 아니다.

**이번 연구에 적용하는 판단:** 이 논문의 기여는 ‘새로운 bound 식’만이 아니다. 기존 설명에서 빼기 어려웠던 가정을 문제의 실제 구조로 치환하고, 왜 instance discrimination이 class-level 구조를 만들 수 있는지 설명한다. Round2의 count law가 이와 경쟁하려면, 정확한 symmetry point의 부호 이상으로 어떤 넓은 추론을 바꾸는지 보여야 한다. General downstream theorem을 꼭 복제할 필요는 없지만, 같은 정도로 명확한 설명상의 변화가 필요하다.

## 2. The Power of Contrast for Feature Learning: A Theoretical Analysis

Wenlong Ji, Zhun Deng, Ryumei Nakada, James Zou, Linjun Zhang. JMLR24(330):1–78,2023. [공식 기록](https://jmlr.org/papers/v24/21-1501.html), [읽은 게재 원문](https://jmlr.org/papers/volume24/21-1501/21-1501.pdf).

**실제로 확인한 원문:** §2–3의 linear loss/augmentation 및 spiked covariance 설정, Assumptions8–10, Theorems13–14/17–18, §4 supervised/transfer 대비, §5 synthetic 검증 및 AppendixB.9의 spectral recovery 증명 연결.78쪽 모든 부등식을 독립 재증명했다는 뜻은 아니다.

**외부 문헌에서 확인한 사실:** Linear representation과 random masking, diagonal noise 및 incoherent signal 가정 아래 feature recovery를 분석한다. Theorem13의 autoencoder 하한과 Theorem14의 contrastive 상한은 같은 regime에서 회복 능력을 구분한다. 이어 downstream classification/regression 위험을 연결하고, label 정보가 in-domain에는 도움이 되지만 제한된 source task의 transfer에는 불리할 수 있는 조건을 분석한다. 실험에서 분석한 데이터 모형과 feature subspace 오류 및 downstream 측정을 직접 비교한다.

**이번 연구에 적용하는 판단:** Restricted linear model이어도 중요한 비교 질문을 해결하고, 경쟁 방법의 실패 하한과 성공 상한을 같은 기준에서 연결하기 때문에 독자가 아는 것이 달라진다. 현재 square equilibrium이 attractive인지 여부는 명확한 수학 질문이지만 그것이 최적표현, 회복 또는 학습에서 중요한 이유는 아직 별도의 주장이다. Round2의 noisy-access 결과를 이론적 K 경계와 동일 검증으로 부르면 안 된다.

## 3. On the Effect of Initialization: The Scaling Path of 2-Layer Neural Networks

Sebastian Neumayer, Lénaïc Chizat, Michael Unser. JMLR25(15):1–24,2024. [공식 기록](https://jmlr.org/papers/v25/23-0549.html), [읽은 게재 원문](https://jmlr.org/papers/volume25/23-0549/23-0549.pdf).

**실제로 확인한 원문:** §1 dynamic/static 경로의 구분, Eq3/5의 초기분포 의존 variational problem, §2–3의 measure/optimal transport reformulation, Lemma8, Propositions11–12, Theorem13과 그 증명, §4의 작은 interpolation 실험.

**외부 문헌에서 확인한 사실:** Infinite-width2-layer homogeneous representation의 scale-dependent 정규화 문제를 convex한 measure 최적화와 연결한다. Optimal solutions의 연속성 및 initialization scale의 극한을 분석해 rich/kernel regimes를 통합한다. 실제 gradient-flow optimization path와 scaling path가 언제나 같다는 정리는 아니다. 그 관계의 실험은10개 점으로 이루어진 작은2D interpolation 문제에서도 수행한다.

**이번 연구에 적용하는 판단:** 이 사례는 natural-image 실험이나 대규모 GPU가 top journal 기여의 필수 조건이 아니라는 반증이다. 작은 실험으로 충분한 이유는 중심 지식이 하나의 낮은 차원 예제의 eigenvalue가 아니라, 여러 알려진 regime을 연결하는 구조와 변분적 정리이기 때문이다. 따라서 round2에 더 많은 toy seeds만 추가하는 것은 이 사례와 같은 기여가 아니다. 단순한 continuity 또는 full-rank Jacobian pullback도 이러한 새로운 구조적 연결을 자동으로 만들어 주지 않는다.

## 4. Understanding Whitening Loss in Self-Supervised Learning

Lei Huang, Yunhao Ni, Xi Weng, Rao Muhammad Anwer, Salman Khan, Ming-Hsuan Yang, Fahad Shahbaz Khan. TPAMI46(12):9479–9492,2024. DOI10.1109/TPAMI.2024.3417438. [읽은 저자-hosted 게재 원문](https://faculty.ucmerced.edu/mhyang/papers/pami2024_whitening.pdf). 원문 첫 페이지의 journal/volume/issue/DOI를 확인했다.

**실제로 확인한 원문:** §IV의 whitening별 관측, §V Proposition1과 Theorems2–4 및 증명, §VI–VII의 SSL 방법 관계 및 group partition, §VIII의 실제 실행 범위.

**외부 문헌에서 확인한 사실:** Embedding이 반드시 whitened돼야 한다는 해석과 full-rank만 필요한 조건을 분리한다. Proposition1은 nonzero singular values가 자유로운 해를 구성하며, Theorems3–4는 embedding gradient의 직교성과 작은 learning rate·bounded derivative 아래의 stable-rank 불변을 분석한다. Network parameter SGD에 대한 무조건적인 불변 정리는 아니다. Channel whitening/random grouping 설계와 CIFAR류, ImageNet, COCO 검증을 통해 분석상의 구분을 방법 선택과 연결한다.

**이번 연구에 적용하는 판단:** 여기서 중요한 것은 ‘singular values에 관한 계산’ 자체가 아니라 기존 동작 설명의 수정과 그 수정이 실제 설계 조건을 바꾼다는 연결이다. 반면 round2의 representation norm 제약, finite-time readout, one-negative와joint-K의 구분은 올바른 범위 설정이지 그 자체로 실용적 기여의 증명은 아니다. 현재 TPAMI 수준으로 확정하려면 같은 핵심 메커니즘을 실제 학습에서 검증하는 연결이 필요하다.

## 5. Consistency of Augmentation Graph and Network Approximability in Contrastive Learning

Chenghui Li, A. Martina Neuman. JMLR27(178):1–68,2026; 게재 원문 첫 페이지는 Published8/26을 명시한다. [공식 기록](https://jmlr.org/papers/v27/25-1466.html), [읽은 게재 원문](https://jmlr.org/papers/volume27/25-1466/25-1466.pdf). 이 다섯 번째 논문은 최초 네 편으로 target과 gate를 고정한 뒤, graph extension의 가까운 원문을 찾는 중 추가했다. 기존 기준을 대체하거나 낮추는 근거가 아니다.

**실제로 확인한 원문:** §1의 realizability 공백, §2의 Gaussian augmentation/graph 구성, §3의 manifold·parameter assumptions와 spectral objective, §4 Theorems11–13, §7.2 spectral consistency 증명 구조. 전체68쪽의 모든 기술 부등식을 독립 검산하지 않았다.

**외부 문헌에서 확인한 사실:** Smooth compact manifold와 augmentation/connectivity scale 조건 아래 augmentation Laplacian의 pointwise·spectral consistency를 증명한다. Theorem12는 eigenvector와 continuum eigenfunction의 근접성을, Theorem13은 spectral optimum을 정해진 복잡도의 ReLU network로 근사할 수 있음을 보인다. 이는 network가 실제 gradient descent로 그 optimum에 도달한다는 정리가 아니다.

**이번 연구에 적용하는 판단:** 알려진 spectral embedding을 다시 쓰는 데 그치지 않고, 기존 보장의 검증되지 않은 realizability 가정을 구체적인 geometry·regularity·network 복잡도로 대체한다. 이번 graph extension도 ‘graph spectrum이 중요하다’라는 기존 지식 이상으로 무엇을 판정 가능하게 했는지를 보여야 한다. 작은 모형을 더 큰 neural network로 parameterize할 수 있다는 사실과, 학습이 그 모형의 대표 예측을 실제로 따른다는 사실은 구분한다.

## 공통 기준 — 결과를 보고 낮추지 않는다

최초 네 편에서 고정했고 다섯 번째에서도 유지하는 공통점은 정리 수나 dataset 수가 아니다. 모두 제한된 가정을 사용하지만, 그 가정 안에서 중요한 설명상의 대비나 통합을 제공한다. 적절한 범위 제한은 진실성을 지키며, 기여의 중요성은 별도로 확보한다.

이번 연구에 요구하는 것은 다음 중 적어도 한 가지 실질적 진전이다.

- **구조적 이론 경로:** finite-negative feedback의 알려진 일반 원리를 넘어, 넓은 데이터/geometry/정책 class에서 새로운 분류·불가능성·비교 결과를 도출한다. 적용범위를 표준 continuity로 조금 넓히는 것만으로는 이 조건을 만족하지 않는다.
- **정량적 학습 설명 경로:** 현재 이론의 대표 예측이 독립적인 실제 parameterized 학습 조건을 예측하고, 강한 대안 설명을 구분하며, 기존 판단을 바꾸는 것을 보인다. 단순히 compression이 다시 관측되는 것으로는 K-law의 설명력을 입증하지 못한다.

두 경로를 모두 요구하지는 않는다. 순수 이론의 가치와 작은 모형을 인정하면서도, 식이 더 길어지고 검산이 늘어난 것을 중요성으로 계산하지 않기 위한 기준이다. 어느 경로에서도 결정적 지식이 확보되지 않으면 최상위 수준의핵심50%를 미도달로 판정한다.
