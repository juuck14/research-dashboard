# 원문 대조와 신규성 경계

검증일 2026-10-22. 외부 논문 결과와 직접 도출 결과를 구분한다. 아래 요약은 제목·초록만으로 추정하지 않고 명시한 본문 범위를 확인한 기록이다. 논문 부재는 증명하지 못했다.

| 원문 | 실제 확인한 설정·결과 | 이번 질문과의 관계 |
|---|---|---|
| Robinson, Chuang, Sra, Jegelka. **Contrastive Learning with Hard Negative Samples**, ICLR2021. https://arxiv.org/pdf/2010.04592 | §2–3.1, Eq1 및 hard sampling q_beta∝p exp(beta fᵀf), β>=0와 latent same-class correction; normalized sphere. Appendix global optimum characterization. | encoder-dependent q는 이미 고전. hard/FN tradeoff도 새 아님. 우리의 easy κ<0, floor 및 frozen-vs-adaptive local Jacobian은 논문 주정리의 직접 진술은 아님. 단 sampler 재가중치를 일반화한 것만으로 기여 주장 불가. |
| Chuang et al. **Debiased Contrastive Learning**, NeurIPS2020. https://arxiv.org/pdf/2007.00224 | §1–2 Eq1, same-latent-label negatives의 mixture contamination과 corrected objective, downstream bound. | false-negative가 왜 문제냐는 일반 질문 선점. 다중 independent factors의 task relation은 이것의 단순 변형이 될 수 있다. |
| Xue et al. **Which Features are Learnt by Contrastive Learning? On the Role of Simplicity Bias in Class Collapse and Feature Suppression**, ICML2023. https://proceedings.mlr.press/v202/xue23d/xue23d.pdf | §5.1 Theorem5.1(minimum-norm minimizer와 embedding dimensionality), §5.2 Definition5.3/imperfect augmentation 및 Theorem5.4(embedding arbitrarily large여도 suppression). | '충분한 차원이면 suppression 없다'는 일반 주장은 틀림. 직접 Prop1은 positive-invariant feature와 unconstrained available coordinate만의 결과. minimum-norm/augmentation mechanism으로 알려진 현상을 새 feedback으로 포장하지 않는다. |
| Zhang et al. **Learning the Unlearned: Mitigating Feature Suppression in Contrastive Learning**, ECCV2024. https://arxiv.org/pdf/2402.11816 | §3 feature-aware negative sampling, 이전 단계 cluster 내부 negative, 단계 표현 통합; Fig1 및 관련 실험. | 학습한 factor가 같은 negatives로 덜 배운 factor를 배우자는 방법은 이미 있음. 새 mining algorithm 제안은 제외. |
| Balmaseda et al. **Discovering Global False Negatives On the Fly for Self-supervised Contrastive Learning**, ICML2025. https://arxiv.org/pdf/2502.20612 | §3.2.2 Eq5/Algorithm1: anchor별 quantile threshold로 유사 negative 제거, moving average objective 추정. §5 conclusion. | easy filtering의 직접 현실적 동기. 원문 hard threshold는 본 연구 q floor와 같지 않다. 본 toy의 κ<0 soft law가 GloFND 전체 algorithm을 이론 설명한다고 주장하지 않는다. |
| Kim, Shim, Lee. **FALCON: False-Negative Aware Learning of Contrastive Negatives in Vision-Language Alignment**, CVPR2026(v5). https://arxiv.org/pdf/2505.11192 | §3 anchor별 hardness quantile scheduler, similarity distribution 입력, epoch-wise embedding cache 갱신, policy improvement proxy. | adaptive hard/FN 균형은 선점. full-support sphere stability의 analytic boundary와 동일 정리를 확인한 것은 아니나 실용적 방법 경쟁으로 들어가면 구별 어려움. |
| Jiang, Nguyen, Aeron, Ishwar. **Hard-Negative Sampling for Contrastive Learning: Optimal Representation Geometry and Neural- vs Dimensional-Collapse**, TMLR2025, https://arxiv.org/html/2311.05139v3 | §3 model, §4 Theorem1–3, §5.3–5.5 dimensional collapse/initialization/normalization. Norm-bounded d>=C-1, hardening nonnegative nondecreasing. UCL positive conditional independence 등 조건 명시. | 기존 보고서에서 빠진 강한 경쟁 선행. hard sampling과 normalization이 geometry/DC에 미치는 영향은 이미 직접 연구됨. κ<0 easy filtering 및 matched-frozen stable point가 adaptive unstable로 바뀌는 specific counterexample는 확인한 theorem statement에는 없음. 하지만 global optimum과 dynamics를 처음 구분했다는 주장은 불가. |
| Perdomo, Zrnic, Mendler-Dünner, Hardt. **Performative Prediction**, ICML2020. https://proceedings.mlr.press/v119/perdomo20a/perdomo20a.pdf | §2–3 decoupled risk와 induced distribution, performative optimum/stability 및 repeated risk minimization의 stability 조건. | encoder가 q를 바꾼 뒤 detached-gradient update하는 구조는 decision-dependent distribution의 특수 경우. generic sampler-Jacobian decomposition 자체는 기존 performative framework의 재서술. Contrastive sphere에서의 exact factor-selective boundary 이상의 결과가 필요. |

## 확정된 차이와 미확정 신규성
- 직접 도출: unconstrained positive-preserved factor의 strict transverse growth 및 epsilon-floor escape bound.
- 직접 도출/실행: normalized additive family에서 frozen-at-current q의 양의 curvature가 adaptive sampler reaction으로 음수가 되는 exact point.
- 미확정: 이 특수경계가 위 geometry/dimensional-collapse 및 performative literature의 단순 application을 넘어 독립 논문 기여인지. 현재는 '설정이 다르다'는 이유로 신규성이 있다고 판정하지 않는다.
- 남은 가장 강력한 반론: norm budget+distribution-dependent loss가 만드는 잘 알려진 symmetry breaking의 작은 예제일 뿐이며 새로운 학습원리가 아닐 수 있음.

## 원문 검증 범위의 한계
GLOFND/FALCON은 실제 finite-batch algorithm과 auxiliary state를 갖는다. 본 연구는 그 코드 재현이 아니라 exact finite-state counterexample를 연구했다. empirical performance 개선을 주장하지 않는다. Jiang HTML header의 날짜가 arXiv metadata와 다르게 표시되어, 서지는 arXivv3 및 TMLR2025 metadata를 우선하고 header 날짜로 새 version을 추정하지 않았다.

## 추가 확인한 최신 경쟁 선행

Meng, Yang, Li, Guo. **SnaPhArd Contrast Learning**, ICLR2026. [공식 PDF](https://proceedings.iclr.cc/paper_files/paper/2026/file/42a24a7a3e7cf7dd127a76daf487cffd-Paper-Conference.pdf). §2.2와 Theorem2.1을 확인했다. Fixed key vectors와 positive vectors를 두고 단일 query의 sphere optimum 및 positive와 일치하는 해를 논한다. 여기서 말하는 collapse와 본 노트의 factor/dimensional collapse는 같지 않다. easy-negative fixation이라는 동기는 가깝지만 sampler-response Jacobian 또는 모든 representation을 함께 움직이는 matched-frozen 비교는 해당 정리의 진술이 아니다. 이 사실은 신규성 증명이 아니라 직접 비교의 출발점이다.

Farina and Perdomo. **The Stability of Online Algorithms in Performative Prediction**, 2026 preprint. [원문](https://arxiv.org/html/2602.24207v1). §1–3은 mixed performative stability와 online learning의 관계를 다룬다. 본 노트의 pointwise local instability를 반박하거나 그대로 증명하는 결과라고 해석하지 않았다. '분포가 바뀌면 학습 안정성이 바뀐다'는 일반 설명 자체는 이 넓은 분야에서 신규하지 않다.
