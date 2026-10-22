# 재현 안내

저장소 root에서 Python3.12와 requirements.txt의 NumPy/SciPy/Matplotlib/Pandas를 사용했다. 계산은 CPU에서 실행했다. `OPENBLAS_NUM_THREADS=1`은 작은 행렬 계산의 불필요한 thread overhead를 줄인다. 각 스크립트는 자기 파일 위치로 결과 경로를 정하므로 별도 데이터 다운로드가 필요 없다. 재실행은 해당 results/를 갱신하므로 원 커밋을 보존하고 별도 checkout에서 실행하는 편이 좋다.

## 주제별 실행

```bash
python -m pip install -r requirements.txt
OPENBLAS_NUM_THREADS=1 python partial-identification/code/run_study.py
OPENBLAS_NUM_THREADS=1 python negative-feedback/code/exact_population.py
OPENBLAS_NUM_THREADS=1 python negative-feedback/code/normalized_feedback.py
OPENBLAS_NUM_THREADS=1 python negative-feedback/code/multiple_negatives.py
OPENBLAS_NUM_THREADS=1 python negative-feedback/code/importance_control.py
OPENBLAS_NUM_THREADS=1 python target-correction/code/run_study.py
OPENBLAS_NUM_THREADS=1 python target-correction/code/context_basis_control.py
OPENBLAS_NUM_THREADS=1 python target-correction/code/frozen_exact_check.py
```

## 독립 검토 및 확장

```bash
OPENBLAS_NUM_THREADS=1 python review/partial-identification/code/audit.py
OPENBLAS_NUM_THREADS=1 python review/target-correction/code/independent_checks.py
OPENBLAS_NUM_THREADS=1 python review/negative-feedback/code/stress_check.py
OPENBLAS_NUM_THREADS=1 python review/negative-feedback/code/full_sphere_center.py
OPENBLAS_NUM_THREADS=1 python review/negative-feedback/code/multinegative_check.py
OPENBLAS_NUM_THREADS=1 python review/negative-feedback/code/no_self_check.py
OPENBLAS_NUM_THREADS=1 python review/negative-novelty/check_curvature.py
OPENBLAS_NUM_THREADS=1 python review/three-factor-extension/audit.py
OPENBLAS_NUM_THREADS=1 python review/robustness-extension/run_checks.py
OPENBLAS_NUM_THREADS=1 python review/robustness-extension/plot_results.py
OPENBLAS_NUM_THREADS=1 python review/robustness-extension/independent_check.py
```

사전 설계와 후속 변경은 각 protocol.md/progress.md에 있다. 정확한 seed와 그리드는 코드·CSV에도 포함된다. Root SGD는 primary1001–1006 및 confirmation3001–3004를 사용하고, 평가 feature noise=.05, 평가 seed90210을 고정했다. 최종 embedding은 review/robustness-extension/results/final_embeddings.json에 저장하여 기존 모델을 재학습하지 않고 readout을 재계산할 수 있다.

결과의 해석은 coordination/final_report.md와 각 verdict.md가 기준이다. Solver의 작은 수치 오차나 seed 반복은 완전 증명을 대체하지 않는다. Finite-support noiseless 정보와 고정 noise 아래 접근성의 차이를 유지해야 한다.
