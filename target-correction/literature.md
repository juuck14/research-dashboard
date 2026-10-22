# 원문 검토 기록

## 확인 완료 또는 진행 중인 핵심 문헌

1. Tian, Yuandong; Chen, Xinlei; Ganguli, Surya. Understanding Self-Supervised Learning Dynamics without Contrastive Pairs. ICML 2021. https://proceedings.mlr.press/v139/tian21a/tian21a.pdf . **원문 §2 Lemma1, §3.1–3.2, Eq2–4/11–16 및 Fig3–4 읽음.** Linear online/predictor/EMA의 정확한 population flow와 proportional EMA·isotropic augmentation 아래 mode/basin 분석. 본 연구의 scalar predictor 안정성 분석에 가장 직접적인 선행. 단순 full-rank init 뒤 collapse는 이미 포함.
2. Richemond et al. The Edge of Orthogonality: A Simple View of What Makes BYOL Tick. ICML 2023. https://proceedings.mlr.press/v202/richemond23a/richemond23a.pdf . **원문 §3–5 및 Proposition4/7, Appendix noise decomposition 읽음.** rank-conditioned optimal predictor의 PCA 해석과 orthonormalization. normalization으로 본질적 문제가 해결되는 경우를 신규성으로 부르지 않기 위한 기준.
3. Korchinski, Favero, Wyart. Learn from your own latents and not from tokens: A sample-complexity theory. 2026 preprint. https://arxiv.org/html/2605.27734v1 . **§5 및 C.3 현재 읽는 중.** data2vec teacher refresh의 phase와 A1 target nonzero linear latent trace/A2 correlation learning 가정. 실제 이론 범위를 확인해 미해결을 과장하지 않는다.
4. Grill et al. Bootstrap Your Own Latent: A New Approach to Self-Supervised Learning. NeurIPS2020. https://proceedings.neurips.cc/paper/2020/hash/f3ada80d5c4ee70142b17b8192b2958e-Abstract.html . 공식 서지·초록 확인. online/target EMA 원형. abstract-only로 상세 정리 근거를 만들지 않는다.

원문 결과/직접 도출/수치 확인은 각 theory.md·results에서 구분할 예정. 신규성 부재를 검색만으로 증명하지 않는다.
