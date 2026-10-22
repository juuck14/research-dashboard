# 후보 1 — SSL 특징 회복 지연

상태: **기각 — 현재 구체화는 새로운 회복 원리의 근거 부족**. 기준일 2026-10-22. 초기 보고서의 우선 추천은 현재 구체화에 대해 철회한다. 넓은 nonlinear SSL 회복 질문 전체의 불가능성을 주장하지 않는다.

4개 pilot와 4개 확인 초기값에서 비선형 8-state 학습 및 checkpoint 상태별 개입을 실제 수행했다. 3000 clean step의 낮은 factor 접근성은 재현했지만, 정확한 분석에서 clean agreement가 rank 1·2·3을 모두 최적해로 인정함을 확인했다. 같은 관측 법칙의 contrastive 대조는 50–250 step에 회복했고, 원래 agreement도 15000 step까지 연장하면 4/8 seed가 R²>.9로 회복했다. 독립 검토자는 gradient·최적해·mode Jacobian을 별도로 검산했으며 현재 구체화의 기각에 동의했다.

- [실행 전 설계와 변경 이유](protocol.md)
- [원문과 신규성 재검증](literature.md)
- [직접 증명 A–C](theory.md)
- [실제 결과·예외·그림](results.md)
- [기각 근거·수정 시도·재개 조건](verdict.md)
- [재현 명령·환경·원자료](reproduction.md)
- [독립 교차 검토](../prevalidation-20261022/reviews/recovery/review.md)
- [진행 및 정정 이력](progress.md)

결과는 고정 readout noise 아래 population 최적 linear R²이며 noiseless 정보 소실이 아니다. Reset의 부분 효과, seed 예외, 다른 factor의 손실을 보존했다. 작은 모형의 표준 spectral 설명을 새로운 memory lock으로 부르지 않았다.
