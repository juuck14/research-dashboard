# 최상위 학술지 수준 비교 — 사전 고정 절차

2026-10-22. 이 문서는 round3 개선 결과를 보기 전에 고정했다. 담당자는 round2의 주장을 옹호하는 역할이 아니라, 공개된 게재 논문과 대조하여 연구의 기여 크기를 심사한다.

## Target 고정

- **주 target: Journal of Machine Learning Research (JMLR).** 독자는 일반적인 머신러닝 학습 원리, 표현 학습 및 이론 연구자다. 특정 영상 benchmark 성능보다 중요한 구조적 결과를 중심으로 판단한다.
- **후보: IEEE Transactions on Pattern Analysis and Machine Intelligence (TPAMI).** 실제 visual/SSL 학습 현상과 이론·분석이 연결되는 경우의 비교 대상이다. 현재 toy model에만 증거가 남으면 TPAMI를 더 쉬운 대체 목표로 쓰지 않는다.
- TMLR, workshop, arXiv, ICLR/ICML은 선행연구로 읽을 수 있지만 이번 **최상위 학술지 게재 수준 비교의 대체 기준**으로 바꾸지 않는다. 학회 연구의 질을 낮게 평가하는 뜻이 아니라, 사용자가 명시한 journal 기준을 사후에 바꾸지 않기 위한 규칙이다.

## 먼저 선택한 가까운 게재 논문

원문의 접근 가능성과 contribution 형태를 보고 선택했으며, round3 성공 결과를 보고 고르지 않았다.

1. Zhang, Wang, Wang. *An Augmentation Overlap Theory of Contrastive Learning*. JMLR26(228),2025. 공식 record22-1009.
2. Ji, Deng, Nakada, Zou, Zhang. *The Power of Contrast for Feature Learning: A Theoretical Analysis*. JMLR24(330),2023. 공식 record21-1501.
3. Neumayer, Chizat, Unser. *On the Effect of Initialization: The Scaling Path of 2-Layer Neural Networks*. JMLR25(15),2024. 공식 record23-0549.
4. Huang et al. *Understanding Whitening Loss in Self-Supervised Learning*. TPAMI46(12),2024. DOI10.1109/TPAMI.2024.3417438; author-hosted accepted article PDF.

이 논문들의 분량이나 실험 개수를 최소 기준으로 삼지 않는다. 실제 중심 질문, 알려진 결과와의 차이, 가정이 제한돼도 얻는 일반적 지식, 중심 주장을 검증하는 증거를 원문에서 비교한다.

## 고정한 비보상형 기준

1. **신규성:** 기존 이론을 아는 독자가 새롭게 알게 되는 비자명한 결론이 있어야 한다. 같은 식/설정이 검색되지 않는다는 사실은 통과 근거가 아니다.
2. **중요성:** 그 지식이 연구자의 설명·판단·설계 중 적어도 하나를 바꾸는 이유가 구체적이어야 한다. 계산하기 편한 equilibrium의 분류만 남는다면 중요성을 별도로 입증해야 한다.
3. **중심 결과:** 논문을 대표할 결론이 현재 증명·반례·직접 실험으로 이미 존재해야 한다. 이후 핵심 실험의 성공을 전제로 하지 않는다.
4. **설득력:** 현상을 만든 실제 원인과 주요 대안 설명을 구분하는 증거가 있어야 한다. FD 반복, seed 개수, reviewer 동의는 기여 크기를 대신하지 않는다.
5. **범위:** 작은 모형을 허용하되, 그 범위에서 기존 이해의 어떤 구조를 드러내는지 확인한다. 가정을 완화한 표준 continuity나 Sylvester-inertia 따름정리만으로 JMLR 중요성이 자동 증가하지 않는다.
6. **연결성:** 이론과 실험이 같은 대표 질문을 검증해야 한다. one-negative의 compression과 multi-negative의 local K cutoff가 각각 참이어도 직접적인 bridge 없이 같은 검증이라고 부르지 않는다.

각 항목은 통과/부분 충족/미충족으로 따로 판정한다. 신규성·중요성 미충족을 수학적 정확성이나 실험량으로 보상하지 않는다. ‘제한 명제는 참’과 ‘최상위 수준의 핵심50%’는 별도 판정한다.
