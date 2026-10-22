# 불완전한 자기 target의 교정 가능성

상태: **기각 — 현재 추천의 간결한 정식화는 기존 이론에 직접 환원**. 담당: target_correction_study. 기준일: 2026-10-22.

입력과 초기 teacher target 모두 구분 정보를 가진 조건에서 frozen teacher와 갱신 teacher를 비교한다. 단순 소실 target의 복구 실패는 연구 결과로 세지 않는다. 기존 보고서의 신규성 평가는 미확정으로 되돌렸다.

Tian, Chen, Ganguli (ICML2021) Lemma1/Eq2–4에 대한 직접 대입으로 이번 student–predictor–EMA 모형이 동일함을 확인했다. 직접 도출한 고정점·안정성과 72 primary+108 조건외 ODE 확인은 기존 basin 설명과 일치한다. full-rank target의 finite-time amplitude 감소를 정보 소실로 해석하는 것도 정정했다. **현재 내용으로 독립 논문 착수는 권하지 않는다.** 넓은 nonlinear hierarchy 문제의 불가능성을 주장하는 판정은 아니다.

- 실행 전 설계: [protocol.md](protocol.md)
- 원문 검토: [literature.md](literature.md)
- 증명과 환원: [theory.md](theory.md)
- 실행 결과와 그림: [results/RESULTS.md](results/RESULTS.md)
- 최종 판정과 재개 조건: [verdict.md](verdict.md)
- 독립 교차검토: [../review/target-correction/review.md](../review/target-correction/review.md)
- 변경 이력: [progress.md](progress.md)

재현 명령과 환경은 results/RESULTS.md에 있다. 미해결 핵심은 기존 conditional-expectation/spectral/dynamical theory로 구분되지 않는 비선형 교정 사례의 존재다. 이것이 확보되기 전 teacher sweep나 대규모 학습으로 확장하지 않는다.
