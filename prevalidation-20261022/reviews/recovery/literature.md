# 후보1 독립 원문 대조

확인일 2026-10-22. 제목·초록만으로 세부 정리를 추정하지 않았다.

| 직접 선행 | 읽은 범위 | 원문이 해결한 것과 이번 검증에 미치는 영향 |
|---|---|---|
| Tian, Chen, Ganguli, **Understanding Self-Supervised Learning Dynamics without Contrastive Pairs**, ICML2021. [원문](https://proceedings.mlr.press/v139/tian21a/tian21a.pdf) | §2 Lemma1 Eq2–4, Theorem1 Eq5, §3 scalar modes와 basin | encoder/predictor/EMA/weight decay의 full-matrix population flow가 직접 주어진다. 단순 scalar recovery·EMA 고정점·weight-decay collapse basin은 이 식의 특수화다. 새로운 nonlinear checkpoint 메커니즘까지 자동 해결한 것은 아니다. |
| Saxe, McClelland, Ganguli, **Exact solutions to the nonlinear dynamics of learning in deep linear neural networks**, ICLR2014. [저자 원문](https://www.saxelab.org/assets/papers/Saxe2014.pdf) | §1 Eq8–12와 Fig3 설명 | 깊이가 input-output 함수족을 바꾸지 않아도 학습 동역학·plateau·mode timescale을 바꾼다. 작은 초기신호와 약한 상관에 의한 delay 자체는 오래된 현상이다. squared-loss supervised linear model이므로 cosine nonlinear SSL 결과의 완전 설명으로 사용하지 않는다. |
| Lee, Dias, Chiang, Lunga, **Understanding the Learning Phases in Self-Supervised Learning via Critical Periods**, ICLR2026. [원문](https://proceedings.iclr.cc/paper_files/paper/2026/file/86ddf3543ad437d71c37e510f41b1a53-Paper-Conference.pdf) | §3.2 deficit, §3.3 FI, Appendix F Fig15 | noise deficit 후 clean continuation의 이력 의존성과 fixed-vs-cosine LR 통제가 이미 있다. 새로 constant LR로 deficit를 보이는 것만으로 신규성은 없다. 원문은 raw views를 noise로 바꿔 marginal까지 달라지므로 이번 pair-correlation-only 조작과 다르다. 그 차이가 새 원인 분리를 주는지 증거가 필요하다. FI는 empirical-gradient proxy와 true Fisher의 차이를 원문도 인정한다. |
| Ponce, Terver, Hebert, Arbel, **Dual Perspectives on Non-Contrastive Self-Supervised Learning**, arxiv2507.01028v3, 2026-02-05. [원문](https://arxiv.org/html/2507.01028v3) | §3 Prop3.1–3.2, §4 Prop4.5/4.10, Appendix proof Eq44–49 | SG/EMA를 일반 scalar loss minimization과 동일시하면 안 된다는 관점을 준다. 다만 개별 equilibrium의 generic asymptotic stability라는 Prop4.10 문구는 orthogonal output gauge를 quotient하지 않은 채 사용하지 않는다. 독립 직접 반론·계산은 theory.md에 있다. 이 문제는 새 SSL 회복 논문의 기여가 아니라 인용 신뢰성 검산이다. |
| Farias, Jozefiak, **Self-Normalized Resets for Plasticity in Continual Learning**, arxiv2410.20098v3. [metadata](https://arxiv.org/abs/2410.20098), [원문 HTML](https://arxiv.org/html/2410.20098v3) | §3.1.3 Theorem3.2/§3.1.4 reset oracle, §4 optimizer 비교 | single-ReLU adversarial target에서 기존 초기화의 trap과 reset의 remedy를 분석한다. reset efficacy 자체를 새 원리로 쓰지 못하게 하는 직접 선행이다. 현재 tanh/bias-free/exact-population SSL과 동일 정리는 아니다. metadata의 v3 날짜는 2025-09-28인데 HTML 내부에는 2026-08-24가 표시되어 버전 날짜 불일치를 기록한다. 이를 새 2026 정리라고 세지 않는다. |

Nature2024 **Loss of plasticity in deep continual learning**의 존재와 서지는 공식 페이지 검색으로 확인했으나 Nature 원문은 인증 redirect, PMC는 CAPTCHA로 막혔다. 이 실행에서 본문을 읽은 것처럼 상세 원인·정리·실험 범위를 인용하지 않는다. 직접 기각 근거는 읽은 Tian 및 Saxe와 직접 계산이다.

현재 가장 강한 경쟁 설명은 (1) clean objective의 mode allocation indifference, (2) unused predictor scale의 국소 안정성, (3) 작은 신호와 optimizer conditioning에 의한 유한 회복시간이다. 선행의 존재만으로 nonlinear 문제를 기각하지 않는다. 이번 실제 결과가 이 설명들을 넘어서는 예측을 주어야 독립 연구 가치가 생긴다.
