# 후보 3 — pairwise SSL의 식별 가능한 불확실성

상태: **기각 — 현재 confounding 및 간결한 수정안의 독립 연구 기여 부족**. 2026-10-22 실제 분석·실험·독립 검토 완료. 넓은 nonlinear uncertainty 문제 전체의 불가능성을 주장하지 않는다.

원래 가설은 unknown correspondence를 허용하면 pair-fit이 같은 해들 사이에서 관측 예측이 달라질 **수 있다**는 존재적 명제다. Symmetric categorical family의 c=a²b exact ridge와 repeat-prediction sharp interval은 이 가설을 지지한다. Positive finite circle-vMF의 unknown 두 concentration 공동 식별은 이번에 추가한 더 강한 탐색 H1만 반박하며 원가설의 반박이 아니다. 실제 표본·예산 통제도 실행했지만 고전 latent-class/replicate/singular-inference를 제거한 뒤 남는 독립 기여는 충분하지 않았다. 기각 이유는 원가설이 거짓이어서가 아니라 현재 구체화의 신규성·기여 부족이다.

- [최종 판정·수정 시도·재개 조건](verdict.md)
- [관측·가정·실행 전 설계와 변경 이력](protocol.md)
- [직접 증명과 범위](theory.md)
- [원문 대조와 신규성 감사](literature.md)
- [직접 실행 결과·재현 명령](results.md)
- [독립 비판](../prevalidation-20261022/reviews/uncertainty/review.md)
- [Root의 operational KL 분석·실제 실행](../prevalidation-20261022/operational-uncertainty/analysis.md)
- [진행 기록](progress.md)

직접 실행은404population조건,60pair datasets(180predictive-policy평가),700oracle inverse fits,60acquisition datasets다. 여러 policy나 start를 독립 dataset수로 세지 않는다. Neural MCInfoNCE 또는 자연 이미지 calibration은 실행하지 않았다. 첫 log-score clipping을 exact log risk와 혼동할 수 있던 문제는 초기결과를 보존하고 수정했다.

이번 회차는 [검증 규칙](../prevalidation-20261022/README.md)을 따른다. Git commit/push는 Root가 직렬화한다.
