# 독립 실행 결과

환경 Python3.12.14, NumPy2.3.5, SciPy1.17.0. 실행:

```bash
OPENBLAS_NUM_THREADS=1 python3 prevalidation-20261022/reviews/recovery/code/independent_checks.py
OPENBLAS_NUM_THREADS=1 python3 prevalidation-20261022/reviews/recovery/code/spectral_audit.py
OPENBLAS_NUM_THREADS=1 python3 prevalidation-20261022/reviews/recovery/code/contrastive_audit.py
```

실행 전 기준은 [protocol](../protocol.md)에 있다.

- **직접 실행 / 해석식 검산:** output3/input2 equilibrium의 vector-field residual1.43e−16, 회전한 별도 equilibrium1.32e−16. 두 점의 거리는.010475다. rotation equivariance residual3.87e−15. finite-difference h=1e−4,1e−5,1e−6 모두 rotational zero modes3개를 보였다. 원자료 [independent_checks.json](independent_checks.json).
- **직접 실행 / 기존 작은 모형:** rho=.8, threshold=.4에 초기신호 .001/.003/.01/.03/.1의 정확한 회복시간은1257.32/422.26/128.70/43.61/12.42였다. 독립 ODE event와 최대 상대오차7.26e−11. [delay_control.csv](delay_control.csv).
- **직접 실행 / 대체 설명:** equal rho=.9에서5개 allocation의 loss가 모두.2, lookup·predictor 중앙차분 gradient 최대9.99e−11. rank2와 fullrank 모두 stationary임을 확인했다. 이것은 신경망의 모든 attractor에 대한 증명이 아니다.
- **직접 실행 / teacher·head tangent:** rho3=.8/.9/1, unused predictor scale=.8/1/1.2, finite-difference h 세 개의27조건에서 분석한 Jacobian 최대오차1.20e−6. 부호 경계rho3=rho0*p가 확인됐다.
- **직접 실행 / 주담당 backprop의 독립 검산:** 담당자의 check()를 호출하지 않고 독립 loss·law를 작성했다. 별도 seed901/902/903와3개 pair law, 모든 parameter에서 중앙차분 최대오차5.28e−10. raw marginal/cross moment도 맞았다. [spectral_audit.json](spectral_audit.json).
- **직접 실행 / contrastive 경쟁 설명:** log-cosh closed-form8조건을 직접 negative expectation과 비교해 최대오차3.89e−16. 별도 seed1901/1902의 clean/deficit gradient 검산 최대오차4.81e−11. [contrastive_audit.json](contrastive_audit.json).

위 계산은 실제 실행이다. 표준 대칭·spectral 설명을 새 학술적 기여로 세지 않는다. 반복된 seed는 같은 구현의 오류를 배제하지 못하므로 주담당 gradient와 독립 계산을 구분했다.
