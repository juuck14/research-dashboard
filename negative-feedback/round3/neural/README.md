# Joint-K neural bridge and augmentation-graph stability window

2026-10-22. **현재 상태: 직접 증명·계산·CPU 실험 완료. 이 폴더의 결과만으로 최상위 학술지 핵심 50% 확보를 선언하지 않는다.** 실제 joint-K shared-encoder 검증과 새 graph/count 분류는 확보했지만, 구성한 평형의 의미와 보통 학습에서의 적용성을 구분해야 한다. Ordinary warmup은 세 seed 모두 사전 적용성 기준을 통과하지 못했다.

이번 단계는 기존 MLP 실험이 `one-negative loss의 평균`이었다는 불일치를 바로잡았다. 새로운 oracle은 실제로 **K개의 negative가 하나의 분모에 함께 들어가는 InfoNCE**의 모집단 손실과 detached-policy gradient를 계산한다. 표현 차원8, observation16, full shared MLP1608개 parameter 모두 trainable이며 negative 선택확률은 전부 양수다.

## 확보한 결과

1. **직접 도출한 정리:** 같은 semantic state의 view 사이 positive channel이 임의 symmetric stochastic graph P일 때 전체 class/view tangent spectrum을 도출했다. Positive graph의 gap이 작으면 K를 늘려 class-mean balance를 안정시킨 뒤에도 within-class view invariance가 다시 불안정해질 수 있다. 두 반대 제약이 만드는 안정 구간을 모든 정수 K에 대해 분류했다. [정의·증명·적용 범위](view_theorem.md).
2. **정확한 예:** 기존 자연 정책 omega(s)=4^(-s),epsilon=.3, positive graph gap=.05에서는 full square가 **정확히 K5–11에서만 안정**이다. K11/12 경계를 outward interval finite sums로 인증했다. Positive가 항상 다른 view인 simple20-cycle에서도 같은 구간을 exact gap certificate와 N80 oracle 방향검사로 확인했다. K>=12 실패는 **matched-frozen도 공유**하며 feedback만의 실패로 해석하지 않는다.
3. **직접 실행한 검증:** noncomplete cycle/path positive graphs12개 전체 spectrum 오차≤3.16e-11. 새 shared nonlinear encoder3seeds, K4/8/16의21개 실제 parameter-flow 검증이 사전 기준을 만족했다. 표준 unpreconditioned DOP853도 K16의 연속 선형 성장 예측 exp(3)에 상대오차≤7.53e-7로 일치했다.
4. **적용성 실패 보존:** random ordinary warmup3seeds에서 square 적용성 gate를 **0/3** 통과했다. 독립 reviewer 제안으로 새 weak positive P=.05 조건에서도 동일18개 fork를 실행했으며 gate는 다시 **0/3**이다. K8/K16 endpoint tradeoff는 연관된 탐색 관측으로 남겼다. 따라서 이 실험은 K5나 K5–11 경계의 일반 학습 재현이 아니다. 결과를 얻기 위해 warmup이나 seed를 교체하지 않았다.

![Different K constraints](figures/count_graph_window.png)

Low-K는 adaptive factor-balance 불안정, high-K는 weak-positive graph의 view 불안정이다. 이 그림은 작은 score-regular collapsed-square의 **국소 기하** 결과이며 semantic information 소실이나 downstream failure의 경계가 아니다.

## 증거와 재현

- [실행 전 기준·수정 이력](protocol.md)
- [결과, 대안 설명, 한계](results.md)
- [재현 명령](reproduction.md), [고정 환경](requirements.txt), [환경 스냅샷](results/environment.json)
- [실제 도출한 정리](view_theorem.md)
- [일반 class-count normal-mode 확장](../foundations/general_normal_graph.md): 별도 foundations 담당의 결과이며, 여기의 full-square spectrum과 적용 범위를 혼합하지 않는다.
- [원시 결과](results/), [계산된 그림](figures/), [그림 재생성 코드](plot_results.py)
- [의미 있는 작업별 이력](progress.md)

가장 가까운 graph SSL 원문과 top-journal contribution 비교·최종 판정은 [상위 round3 기록](../README.md)의 별도 문헌/독립 재심 결과와 연결한다. Positive graph eigenmode 대각화와 neural pullback inertia 자체를 신규성으로 계산하지 않는다.
