# 부분 식별 독립 교차검토

상태: 검토 완료, 2026-10-22.

판정: 현재 Gaussian standalone 프로그램 기각에 동의. 일반 nonlinear/source-dependence 질문의 불가능성을 주장하지 않는다.

- [검토 보고서 및 완전 증명](review.md)
- [독립 검토 사전 기록](protocol.md)
- [독립 코드](code/audit.py)
- [실행 요약](results/audit_summary.json)
- [별도 seed 포함 원시 수치](results/random_checks.csv)

주요 교정: 기준환경 observation whitening과 exact source covariance=I 가정을 구분해야 한다. owner가 이를 받아들여 theory.md와 verdict.md를 수정했다. max-environment TC와 probability-averaged conditional TC의 budget convention도 구분한다.

독립 재검산 400사례에서 식/구현 오차는 1e-14 미만이었다. 마지막으로 owner theory.md/최종 verdict.md를 재독했고 위 scope 교정과 exact block 반례가 반영됐음을 확인했다.
