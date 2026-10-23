# 조건부 균형 가정의 실제 강도: 증명과 실행

2026-10-23. **상태: 범위 분석 완료.** 기존 정리의 오류를 발견한 것이 아니라, 왜 그것을 일반적인 비대칭 학습 표현의 법칙으로 사용할 수 없는지 정확히 분석했다. 아래 결과를 최상위 수준의 새로운 기여나 원래 중요성 문제의 해결로 세지 않는다.

[완전 유도와 증명](general_derivative.md) · [실행 전 protocol](protocol.md) · [실행 코드](check_assumptions.py) · [원시 요약](results/summary.json)

## 직접 확보한 내용

1. **일반 update의 미분:** `E[h|s]=0`을 사용하지 않고 exponential policy의 normalizer derivative까지 유지한 G와 G'를 도출했다. 비대칭일 때 추가되는 항은 기존 단일 tagged 항으로 환원되지 않는다.
2. **정확한 분해:** h를 점수로 예측되는 부분 m(s)와 잔차 xi=h−m(s)로 나누면, G[h]=G[m], H[h]=H[xi]+H[m]이다. 기존 정리는 조건부 중심화 잔차의 slope에 해당한다.
3. **작은 위반의 효과:** balanced h0에 tau*a(s)를 더하면, 같은 reference에서 drift는 정확히 tau*G[a], slope는 H[h0]+tau²H[a]다. 작은 비대칭을 주어도 slope가 거의 유지되는 것과, 그 점이 여전히 equilibrium인 것은 다르다.
4. **공통 stationarity의 특성화:** 같은 reference와 같은 q0,beta에서 모든 K의 drift가0인 것과 조건부 균형은 동치다. Finite L score levels에서는 첫 L개 count의 stationarity만으로도 groupwise conditional balance가 필요하다. 증명은 기존 moment uniqueness와 strict total positivity 도구의 직접 적용이다.

이 분석은 가정을 조금만 깨면 현상이 즉시 사라진다는 주장도 지지하지 않는다. Hyperbolic equilibrium의 작은 perturbation에 대한 보존은 표준 안정성 이론이다. 깨진 대칭에서는 K마다 **이동한 평형점**을 비교해야 한다는 뜻이다.

## 실행한 검사

| 검사 | 관측 | 의미 |
|---|---|---|
| 고정35개 law/count/mean-amplitude 조합 | drift 선형 항등오차≤2.09e-17, slope 이차 항등오차≤7.57e-17 | 일반식을 독립 전개와 대조 |
| Six-candidate ordered tuples의 직접 G 차분 | 최대 slope 오차1.30e-11 | Normalizer를 포함한 식의 검산 |
| 점수 동률을 깨는 고정 jitter9조건 | 모두 사전 bracket에서 root를 찾았으며 위치가 K마다 다름 | 고정 reference와 count별 equilibrium을 구분 |
| L=6 first-L count matrix | 수치 condition number≈2.04e10 | Exact stationarity 동치를 approximate stationarity 보장으로 확대할 수 없음 |

예를 들어 jitter .001에서 scalar root는 K1에서 .0001601024, K4에서 .0002690737, K8에서 .0018963175로 이동했다. 이 세 root는 모두 기존 repelling branch의 continuation이며 **새로운 instability counterexample이 아니다.** 원래 점의 비영 drift를 무시한 채 slope만 평가하면 이 차이를 놓친다. Score law 분석이지 generic Gram embedding의 실현 가능성을 증명한 연구도 아니다.

## 현재 연구에 주는 판단

연속 모집단 확장은 유한 score tie artifact를 제거하지만, 공통 count-reference의 구조적 조건까지 제거하지 않는다. 작은 비대칭에서는 slope 검산이 통과하더라도 equilibrium 위치가 먼저 바뀔 수 있다. 따라서 현재 exact count law를 generic training에 연결하려면 moving equilibrium 또는 실제로 방문하는 표현의 분석이 필요하다. 이 파일의 새로운 계산을 추가했다고 그 핵심 연결이 확보된 것은 아니다.

## 재현

Repository root에서 실행한다.

```bash
OPENBLAS_NUM_THREADS=1 python negative-feedback/round4/assumptions/check_assumptions.py
```

Python3.12.14, NumPy2.3.5, SciPy1.17.0에서 CPU 환경에서 약0.62초(관측 wall time)에 실제 실행했다. 전부 exact population finite sums이며 Monte Carlo seed는 없다. CSV3개와 summary.json을 results에 쓴다. Mean-violation/jitter 실험의 root bracket[-.1,.1]과 score/weight/tau/jitter 설정은 protocol에서 먼저 고정했다. Kernel conditioning은 분석적 finite-L 증명에서 파생된 진단이며, 새로운 확인 실험으로 세지 않는다. Finite-kernel conditioning은 분석적 invertibility 증명의 수치 진단이며, determinant 부호의 부동소수점 관찰을 증명으로 쓰지 않았다.
