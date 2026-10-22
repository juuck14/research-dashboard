# 원문 재검증과 신규성 경계

기준일2026-10-22. 아래는 실제 원문에서 확인한 범위다. 검색/초록만으로 정리의 범위를 확대하지 않는다. 신규성 없음은 검색에서 안 보였다는 이유로 증명되지 않는다.

| 문헌 | 원문 확인 범위 | 이번 질문을 대체하는 부분·남는 부분 |
|---|---|---|
| Lee, Dias, Chiang, Lunga. **Understanding the Learning Phases in Self-Supervised Learning via Critical Periods**, ICLR2026. [공식 PDF](https://proceedings.iclr.cc/paper_files/paper/2026/file/86ddf3543ad437d71c37e510f41b1a53-Paper-Conference.pdf) | §3.1–3.3, §3.2 deficit definition, Appendix Fig15 | noise입력 deficit 후 clean continuation·시점별 영향과 fixed-vs-cosine LR 대조가 이미 있다. BN/head/optimizer별 causal localization을 다 해결했다는 근거는 없다. 단순 CP 재현과 LR통제만은 신규 기여가 아니다. |
| Tian, Chen, Ganguli. **Understanding Self-Supervised Learning Dynamics without Contrastive Pairs**, ICML2021. [원문](https://proceedings.mlr.press/v139/tian21a/tian21a.pdf) | §2 Lemma1 Eq2–4, Theorem1, §3.1–3.2 | full matrix encoder/predictor/EMA dynamics가 직접 선행이다. scalar 회복/weightdecay basin은 정확한 특수 경우라 제외했다. 이번 cosine+MLP+Adam을 이 선형 squared-loss 정리가 그대로 해결한다고 말하지 않는다. |
| Ponce, Terver, Hebert, Arbel. **Dual Perspectives on Non-Contrastive Self-Supervised Learning**, ICLR2026. [v3 원문](https://arxiv.org/html/2507.01028v3), [공식 PDF](https://proceedings.iclr.cc/paper_files/paper/2026/file/349a45f211fb1b3850da1ccd829e869e-Paper-Conference.pdf) | §3.2, §4 Eq4–7, Prop4.5/4.10/4.11, proof부분 | SG/EMA가 일반 smooth objective gradient가 아니며 linear equilibrium algebra를 다룬다. 그러나 Prop4.10의 개별점 asymptotic stability 문구를 이번 연구의 확정 사실로 채택하지 않는다: rotation gauge의 연속 equilibrium orbit와 충돌할 수 있다는 독립 검토가 있다. quotient·normal attraction 해석이 필요하며 [reviewer 기록](../prevalidation-20261022/reviews/recovery/)을 따른다. |
| Wen, Li. **The Mechanism of Prediction Head in Non-contrastive Self-supervised Learning**, NeurIPS2022. [공식 PDF](https://papers.nips.cc/paper_files/paper/2022/file/9d276b0a087efdd2404f3295b26c24c1-Paper-Conference.pdf) | §1.1, §2–3 설정, Theorem4.1/4.3, Lemma5.3, Proposition5.4 | nonlinear network·output normalization·predictor가 weak feature 학습을 가속하는 기작까지 직접 다룬다. 초기 head 경로와 최종 head가 다를 수 있음을 명시한다. 이번 finite-bit/tanh/Adam 정리를 그대로 포함하지는 않지만 'head가 weak feature recovery를 바꾼다' 자체는 신규성이 없다. |
| Farias, Jozefiak. **Self-Normalized Resets for Plasticity in Continual Learning**. [v3 원문](https://arxiv.org/html/2410.20098v3), [버전 metadata](https://arxiv.org/abs/2410.20098) | §2, §3.1.1–3.1.4, Theorem3.2/3.3 | task이력에 따른 bad initialization·single ReLU failure·reset oracle를 분석한다. 이번 tanh에는 dead ReLU 경로가 없지만 reset아이디어 자체는 새롭지 않다. metadata는 최초2024·v3수정2025-09-28, HTML 내부2026표시는 불일치하므로2026신규논문으로 인용하지 않는다. |
| Kastner, De La Vega, Farahmand. **SingularClip: Preventing Spectral Collapse to Maintain Plasticity in Continual and Reinforcement Learning**, arXiv2608.18319v1, 2026-08-18. [원문](https://arxiv.org/html/2608.18319) | §2–4, Theorem4.2, §5.1 | dormant units·stale optimizer·norm에 따른 effectiveLR와 별도로, 약한 singular subspace의 느린 적응을 분석한다. 두층linear·projected flow에서 taskcompletion time의 logarithmic lowerbound다. 이번cosine MLP를 직접 해결하는 정리가 아니지만 'norm통제뒤 느린복구'만으로 새원리를 주장하기 어렵게 한다. |
| Wang, Srinivasa, Chen, Liu, Payani, Zhang. **Predicting Plasticity in Deep Continual Learning: A Theoretical Perspective**, arXiv2605.09044v1, 2026-05-09. [PDF](https://arxiv.org/pdf/2605.09044) | §2–4, Lemma3.1, Theorem4.6, AppendixB.6 | 입력·구조rank만으로 trainability를 보장못함을 반례로 보이고, task-dependent gradientstrength/reliability와 unbiased β-smooth SGD의 one-step gain하한을 준다. SG/EMA가 smooth scalar objective gradient가 아닌 이번jointdynamics에 그정리를 자동전이하지 않는다. gradient/state진단 자체가 새로운 문제라는 framing은 배제한다. |

## 이번 계산의 정확한 신규성 판정

이번에 직접 얻은 flat optima와 spectral-gap 계산은 finite Walsh basis의 elementary Rayleigh/Cauchy–Schwarz 및 missing-mode Taylor 분석이다. 특정 표기가 기존 논문과 같지 않다는 사실만으로 새 원리가 되지 않는다. 반면 CP2026가 실제 이미지에서 관측한 모든 시점효과를 이 계산 하나로 반박한 것은 아니다. 이번 모델의 실패원인을 분리했을 뿐이다.

원래 추천을 유지하려면, clean objective가 목표factor를 엄격히 선호하는 설정에서도 알려진 geometry/optimizer/EMA/head 설명을 넘는 상태량이 복구를 예측해야 한다. 현재 그 핵심 주장은 입증되지 않았다.

추가 최신검색에서 OpenReview `t6sUZeEbkt`의 **When Prediction Chooses the Representation: Learning Dynamics and Planning in World Models**가 나왔으나 원문은 challenge page로 막혔다. 초록/검색문구로 정리범위나 중복판정을 만들지 않았다. 후속문헌심사가 필요한 항목으로만 남긴다.
