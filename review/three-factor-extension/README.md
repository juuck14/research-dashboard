# Three-factor independent extension

상태: 실행 완료. 2026-10-22. Root가 two-factor 발견 뒤 추가 범위를 별도 사전 기록하고 실행했다.

Exact population, identity positives, full normalized lookup의 complete tangent Jacobian을 계산했다. m=3,d=8,epsilon=.1,kappa=-2에서 matched frozen 최대 비회전 고유값은 -0.01238159, adaptive는 +0.02590878(양의 방향 5개)였다. 따라서 four-state 또는 additive encoder만의 현상은 아니다.

전체 54조건 중 three-factor 후보18개를 두 추가 finite-difference step과 별도 직교 회전 좌표(seed20261022)에서 확인한54계산이 모두 기준을 유지했다. Equilibrium residual 최대1.39e-17. 이것은 3-factor 일반 정리나 실제 데이터 성공률이 아니라 exact expectation의 수치 Jacobian 근거다. 수치 안정성은 전체 basin이나 semantic information loss를 보장하지 않는다.

명령: `OPENBLAS_NUM_THREADS=1 python review/three-factor-extension/audit.py` (저장소 root에서). 설계 protocol.md, 원자료 results/grid.csv와 confirmation.csv, 집계 results/summary.json.
