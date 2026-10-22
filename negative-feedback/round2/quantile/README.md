# Rank filtering: 별도의 불연속 경계 결과

상태: 증명·실행·독립 검토 완료. [정의와 증명](theory.md), [규약](protocol.md), [실행 코드](run.py), [결과](results/summary.json), [독립 검토](../review/review.md).

Self를 제외한 세 후보에서 낮은 score의 원 확률질량 절반을 유지한다. 정확한 동점만 균등 분할하는 이상적 정책은 square에서 frozen stable/adaptive Lyapunov unstable이다. epsilon=.1에서 frozen의 가장 느린 비회전 flow eigenvalue는 -.0261893이며, adaptive factor-angle 속도의 일방향 극한은 ±.0403412이다. 일반 d4 perturbation6개에서 frozen 수축/adaptive 확장을 실제 관측했다.

중요한 수정: TIE=1e-12를 쓰는 수치 정책에는 아주 작은 안정 띠가 존재한다. 따라서 이 구현에 이상적 정책의 infinitesimal 불안정성 정리를 그대로 적용하지 않는다. [직접 비교 CSV](results/tie_tolerance_control.csv)에서 delta1e-13이면 exact branch 속도+.0403412지만 tolerance branch는 -7.20e-15다. 본 수치 궤적은 이 띠보다 큰 유한 perturbation에서의 탈출이다.

GloFND 전체 알고리즘에 대한 반례가 아니다. Learned quantile/EMA 상태, 보통의 제거 비율, loss 및 positive 설정이 다르다. 이 결과는 smooth theorem의 주기여와 구분하는 보조 결과다.

재현: `OPENBLAS_NUM_THREADS=1 python negative-feedback/round2/quantile/run.py`.
