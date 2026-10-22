# 원문 검토 기록

## 확인 완료 또는 진행 중인 핵심 문헌

1. Tian, Yuandong; Chen, Xinlei; Ganguli, Surya. Understanding Self-Supervised Learning Dynamics without Contrastive Pairs. ICML 2021. https://proceedings.mlr.press/v139/tian21a/tian21a.pdf . **원문 §2 Lemma1, §3.1–3.2, Eq2–4/11–16 및 Fig3–4 읽음.** Linear online/predictor/EMA의 정확한 population flow와 proportional EMA·isotropic augmentation 아래 mode/basin 분석. 본 연구의 scalar predictor 안정성 분석에 가장 직접적인 선행. 단순 full-rank init 뒤 collapse는 이미 포함.
2. Richemond et al. The Edge of Orthogonality: A Simple View of What Makes BYOL Tick. ICML 2023. https://proceedings.mlr.press/v202/richemond23a/richemond23a.pdf . **원문 §3–5 및 Proposition4/7, Appendix noise decomposition 읽음.** rank-conditioned optimal predictor의 PCA 해석과 orthonormalization. normalization으로 본질적 문제가 해결되는 경우를 신규성으로 부르지 않기 위한 기준.
3. Korchinski, Favero, Wyart. Learn from your own latents and not from tokens: A sample-complexity theory. 2026 preprint. https://arxiv.org/html/2605.27734v1 . **§3 Theorem1, §5 A1/A2, Appendix C.2–C.3, D 원문 확인 완료.** Theorem1의 rigorous recovery는 balanced/separated RHM 및 stable clustering 아래 ILC에 해당. data2vec 설명은 teacher를 phase마다 refresh하며, A1의 learned latent nonzero linear projection과 A2의 detectable correlation을 GD가 추출한다는 가정에 의존한다. B_a nonzero를 full-rank target 보장이라고 확대하면 안 된다. C.3 layerwise dynamics와 D의 teacher trace probe도 이미 제시. 본 audit의 arbitrary scalar target-error correction을 해결한 일반 정리는 아니나 단순 phase/teacher 업데이트 설명은 이미 존재한다.
4. Grill et al. Bootstrap Your Own Latent: A New Approach to Self-Supervised Learning. NeurIPS2020. https://proceedings.neurips.cc/paper/2020/hash/f3ada80d5c4ee70142b17b8192b2958e-Abstract.html . 공식 서지·초록 확인. online/target EMA 원형. abstract-only로 상세 정리 근거를 만들지 않는다.

5. Li et al. Rethinking JEPA: Compute-Efficient Video SSL with Frozen Teachers. 2025 preprint. https://arxiv.org/pdf/2509.24317 . **원문 §1–2.2와 §3의 matched setup 확인.** SALT는 reconstruction teacher를 학습한 뒤 고정하고 masked-latent student를 학습한다. frozen teacher가 충분할 수 있다는 실험 선행이지, 동일 정보·동일 target의 일반 자기교정 정리는 아님. 'EMA와 frozen 비교 자체가 새롭다'는 framing을 배제.

6. Guo et al. When Should the Teacher Move? Temporal Coupling and Stability in Self On-Policy Distillation. arXiv2606.03532, v2 2026-10-09. https://arxiv.org/pdf/2606.03532 . **원문 §2–3 및 Eq1–3 확인.** LLM rollout과 feedback-conditioned teacher의 JSD objective에서 freeze/EMA/hard-refresh를 비교. temporal coupling 문제 자체의 최신 인접 선행. 외부 feedback·policy 분포가 변하는 문제라 현재 fixed pair SSL의 직접 theorem으로 사용하지 않음. 해당 논문의 실험 결론을 모든 representation SSL에 전이하지 않음.

7. Caron et al. Emerging Properties in Self-Supervised Vision Transformers. ICCV2021. https://openaccess.thecvf.com/content/ICCV2021/papers/Caron_Emerging_Properties_in_Self-Supervised_Vision_Transformers_ICCV_2021_paper.pdf . DINO 원문 PDF는 CVF403, arXiv PDF는 retrieval size limit로 본 실행에서 읽지 못했다. 해당 논문의 상세 안정성 주장을 기각 근거로 사용하지 않았다. 중복 판정의 직접 근거는 접근해 읽은 Tian2021의 정확한 방정식이다.

원문 결과/직접 도출/수치 확인은 theory.md·results에서 구분했다. 신규성 부재를 검색만으로 증명하지 않으며, 현재 기각의 결정적 근거는 Tian2021 Lemma1에 대한 **식의 직접 대입**이다. 문헌 검색에서 관련 최신 결과가 많다는 인상으로 기각하지 않았다.
