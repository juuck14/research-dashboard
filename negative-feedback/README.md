# Negative 관계와 학습 피드백

상태: 분석 중 → 원래 가설 수정 필요. 기준일 2026-10-22.

## 현재 결론
1. **직접 증명:** positive-invariant binary factor, unconstrained dot-product encoder의 추가 coordinate, stop-gradient sampler와 q>=epsilon/4 아래 누락 factor boundary는 transverse repelling이다. 작은 비영 perturbation의 탈출 시간 상계도 도출했다. 전체 stationary saddle와 혼동하지 않는다.
2. **직접 실행:** exact population gradient-flow 1,080 설정/초기값 반복 중 1,080개가 이론적 deadline 안에서 amplitude0.1까지 탈출. seed101·211의 확인 설정540개 포함. 독립 dataset1,080개나 성공확률의 통계추정이 아니다.
3. **대안 설명:** soft easy-negative 선택은 동일 초기조건에서 탈출을 약99배 늦췄으나 frozen q도 거의 같은 지연이다. time100 관측만으로 영구 실명이라고 결론낼 수 없다.
4. **설정 수정 후 확인 중:** normalized encoder에서는 누락 factor가 안정할 수 있다. 단 norm budget과 static q의 목적변화를 먼저 분리해야 한다. symmetric all-factor point의 adaptive vs matched frozen-q Jacobian 차이를 추가 분석한다.

## 실행 근거
- `theory.md`: Proposition1–3과 완전 증명, 적용 범위
- `protocol.md`: base 실행 전 설계 및 결과 후 별도 N1 amendment
- `results/summary.json`: gradient-check 최대오차3.92e-11, 확인 개수/수치환경
- `results/population_runs.csv`: 각 설정/seed/hitting time/정당화된 deadline
- `results/local_stability.csv`: transverse eigenvalues
- `results/escape.svg`: frozen/adaptive 비교
- `code/exact_population.py`: 실행 코드

```bash
OPENBLAS_NUM_THREADS=1 python code/exact_population.py
OPENBLAS_NUM_THREADS=1 python code/normalized_feedback.py
```
Python3.12.14, NumPy2.3.5, SciPy1.17.0, Matplotlib; solver rtol1e-8,atol1e-11(base). finite-difference checker 포함. sampled minibatch나 neural image learning 결과가 아니다.

## 현재 가장 큰 반론
충분한 차원만으로 normalization의 에너지 제약이 제거되지 않는다. normalized corner에서의 stable omission이 frozen q에서도 유지되면 피드백 고유성의 증거가 아니다. full d3 sphere tangent 및 가장 가까운 geometry 선행을 critic이 독립 검토 중이다.

## 기록
`literature.md`, `progress.md`, `verdict.md`와 모든 코드·결과를 연결한다. 실패한 base 가설은 N1 성공으로 덮어쓰지 않는다.
