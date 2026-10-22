# Nonidentity positives and actual minibatch training

상태: 실행 완료, 2026-10-22. 설계는 protocol.md에 실행 전 기록했다. 코드 run_checks.py, 원자료 results/positive_channel.csv와 sgd.csv, 집계 results/summary.json.

## 결과

- 각 bit의 positive 변형 확률 eta=.001,.01,.05,.1에서도 full-rank positive channel을 유지한다. 두 numerical step에서 frozen square는 전체 비회전 tangent 안정, adaptive는 한 불안정 방향이다. eta=.1의 최대 비회전 flow eigenvalue: frozen -.08697142, adaptive +.03214919. 대칭점 residual<2.8e-17.
- 실제 normalized lookup SGD 30 runs: 6 primary seeds+4 confirmation seeds, 각각 uniform/frozen/adaptive. batch64, lr.1,6000steps. 독립 평가 feature noise sigma=.05 아래 Bayes-optimal worst-factor accuracy는 uniform/frozen 모두1.0, adaptive .4934–.4984였다.
- 사전 기준은 primary6/6, confirmation4/4에서 충족했다. 같은 초기값과 anchor/uniform 난수 stream을 policy끼리 맞췄다. 이 횟수를 일반화 성공확률이나 이미지 benchmark의 성능으로 해석하지 않는다.
- 유한시간 작은 거리나 작은 amplitude를 noiseless information loss로 부르지 않는다. 보고한 accuracy는 **명시한 noise channel 아래의 접근성**이며 학습된 probe가 실패한 결과가 아니다.

명령(저장소 root): `OPENBLAS_NUM_THREADS=1 python review/robustness-extension/run_checks.py`. Positive-noise Jacobian과 SGD identity-positive는 서로 다른 두 실험이며, stochastic training에서 positive noise까지 함께 사용한 결과는 아니다.
