# 직접 실행 결과

실행: `OPENBLAS_NUM_THREADS=1 python code/run_study.py`. 실행 전 protocol.md 저장. 이후 수정은 표기 범위 정정과 SVG 추가이며 수치 조건·판정 문턱은 바꾸지 않았다.

## 1 정확한 관측 동치와 식별각

41개 (gamma,delta) 조건, gamma당 100001각의 grid로 닫힌식과 covariance 계산을 대조했다. 탐색 25개, 확인 16개의 조건은 사전 분리했다.

- TC 공식 최대 오차: 2.50e-16.
- 동일 관측 covariance 재구성 최대 오차: 8.88e-16.
- endpoint grid 오차 최대 7.83e-6 rad (<한 grid step 수준).

이는 theory.md 증명의 계산 검증이며 수치 결과가 증명을 대신하지 않는다.

## 2 무한 표본에도 남는 구조 모호성

δ=.001 nat일 때 gamma=.03의 quotient radius는 45°(전체 signed-permutation quotient), gamma=.3의 radius는 4.0898°. 이 radius는 restricted O(2) family의 exact 값이고 broader GL family에는 lower feasible radius다.

이 예에서 truth는 정확히 독립인 모델을 골랐지만, 허용 가정의 집합에는 dependent alternative sources가 들어 있다. 알고리즘은 정확 독립을 추가 선호해 한 해를 고를 수 있으나, 가정 tolerance만으로 다른 허용 DGP를 배제할 수는 없다.

## 3 방향별 해상도는 exact group 보장이 아니다

D=diag(1.02,.98,1.8), δ=.0001에서 pairwise feasible rotation radius:

| 회전 pair | 허용각 |
|---|---:|
| 1–2 weak pair | 22.4957° |
| 1–3 strong pair | 1.4082° |
| 2–3 strong pair | 1.3129° |

이것은 pairwise feasible examples이며 고차원 전체 집합의 projection upper bound가 아니다. 작은 positive tolerance에서는 strong axis도 작은 회전을 허용해 **정확히** 고정되지 않는다. 기존 추천의 표현을 이 점에서 정정한다.

## 4 표본오차와 구조 모호성은 다른 양이다

독립 확인 seed 1000–1039, 조건당 40회. 각 n은 환경1의 sample 수이며 baseline whitening covariance는 oracle I로 고정했다.

| gamma | n | 관측 covariance eigenaxis 오차 중앙값 | 구조적 radius δ=.001 |
|---|---:|---:|---:|
| .03 | 100 | 24.874° | 45° |
| .03 | 1,000 | 20.618° | 45° |
| .03 | 10,000 | 7.513° | 45° |
| .3 | 100 | 8.251° | 4.090° |
| .3 | 1,000 | 1.994° | 4.090° |
| .3 | 10,000 | .797° | 4.090° |

샘플이 늘면 특정 exact-independence estimator의 오차는 감소한다. 이는 구조 identified set가 줄었다는 뜻이 아니다. 이 표는 원리를 보여주는 확인 실험이며 새 finite-sample bound 또는 estimator 제안이 아니다.

## 5 독립 critic 반론과 수정

critic은 approximate source independence의 일반 GL family에서는 source covariance I를 WLOG라 할 수 없다는 점을 지적했다. 담당자가 수용하여 theory/README/protocol에서 추가 exact reference-environment assumption을 전면 명시했다. GL shear 반례와 max-vs-average budget 반례는 `../review/partial-identification/`에 독립 보존된다. O(2) 결과를 broader family의 exact set로 주장하지 않는다.

그림: [population_radius.svg](figures/population_radius.svg), [sample_vs_structure.svg](figures/sample_vs_structure.svg). 원자료: `results/*.csv`, 수치 검증 `results/checks.json`, 환경 `results/environment.json`.
