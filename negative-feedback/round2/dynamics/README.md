# 임계 negative 수의 실제 population dynamics 검증

상태: 완료. [실행 전 규약](protocol.md), [실행 코드](run.py), [원자료](results/trajectories.csv), [요약](results/summary.json).

자연 필터 omega(s)=4^(-s),epsilon=.3의 정확한 경계 K4/K5를 generic d4 perturbation으로 검사했다. 4개 초기조건 ×2개 K ×2개 정책의16개 적분을 실행했으며 사전에 정한 판정16개 모두 충족했다. 이는16개의 독립 데이터셋이 아니라 한 exact population의 초기조건/정책 비교다.

- Adaptive K4: 최종 요인 에너지 불균형 비율20.08518–20.08533. 선형 예측 exp(3)=20.08554에 근접.
- Adaptive K5: .049787075–.049787081. 선형 예측 exp(-3)=.049787068에 근접.
- Frozen: 두 K 모두 최종 비율≤1.39e-11. 이 영역의 아주 작은 수치는 부동소수점 한계이며 정확한 수렴률 추정에 쓰지 않는다.
- Unit norm 최대오차3.75e-13.

K4의 불안정 eigenvalue는 -9.1489e-5로 작다. 적분 시간은 해당 시간척도에 맞춰3/abs(lambda)로 사전 지정했다. 짧은 시간의 무변화를 안정성으로 해석하지 않았다. 초기값은 factor-angle perturbation1e-5에 일반 ambient perturbation1e-6을 더했으므로 tied 평면에만 갇힌 적분이 아니다. 결과는 국소 geometry 회복/증폭이며 정보 소실의 주장이 아니다.

```bash
OPENBLAS_NUM_THREADS=1 python negative-feedback/round2/dynamics/run.py
python negative-feedback/round2/dynamics/plot.py
```

![Population dynamics](results/cutoff_flow.png)
