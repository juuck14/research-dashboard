# 불완전한 자기 target의 교정 가능성

상태: **분석 중**. 담당: target_correction_study. 기준일: 2026-10-22.

입력과 초기 teacher target 모두 구분 정보를 가진 조건에서 frozen teacher와 갱신 teacher를 비교한다. 단순 소실 target의 복구 실패는 연구 결과로 세지 않는다. 기존 보고서의 신규성 평가는 미확정으로 되돌렸다.

현재 확인: Tian, Chen, Ganguli (ICML 2021) Lemma 1 및 §3.2가 이미 predictor/EMA/weight decay가 만드는 collapse·회복 고정점과 basin을 분석한다. Korchinski et al. (2026) §5 A1/A2와 Appendix C.3도 검토 중이다. 기존 이론에 환원되는 현상을 새 결과로 제시하지 않는다.

- 실행 전 설계: [protocol.md](protocol.md)
- 원문 검토: [literature.md](literature.md)
- 변경 이력: [progress.md](progress.md)

다음: 정확한 population self-prediction operator 및 trainable linear predictor ODE를 도출하고 deterministic 계산/별도 seed 검증을 실행. 본 README는 결과 확보 후 갱신한다.
