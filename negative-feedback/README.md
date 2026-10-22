# Negative 관계와 학습 피드백

**최신 상태(2026-10-22): 수정된 국소 population 이론으로 진행 — 핵심50% 확보 판정.** [round3 최종보고](round3/report_ko.md), [새 원고](round3/manuscript.md), [독립 재심](round3/review/final_review.md), [재현](round3/reproduction.md). 일반·연속 분포의 all-count rescue 법칙과 positive-gap 상충 조건을 증명했다. 원래 정보 소실 해석은 기각, 일반 학습 applicability 실패는 보존했다. 실전 성능·일반 cutoff를 확보했다는 뜻은 아니다.

## 이전 round2와 첫 단계의 보존 기록

상태: **검증된 수정 방향으로 진행 — 후속 핵심 결과 확보.** 기준일 2026-10-22.

**최신 결과:** [round2/README.md](round2/README.md),[한국어 최종보고](round2/report_ko.md),[논문 원고](round2/manuscript.md). 후속 단계에서 arbitrary-K 전체 spectrum·단조 임계값·자연 exponential 정책의 열린 영역을 증명하고 독립 검산했다. 일반 정보 삭제 주장은 배제했다. 아래는 첫 단계의 보존된 결과이며 최신 판정과 구분한다.

## 현재 결론
1. **직접 증명:** positive-invariant binary factor, unconstrained dot-product encoder의 추가 coordinate, stop-gradient sampler와 q>=epsilon/4 아래 누락 factor boundary는 transverse repelling이다. 작은 비영 perturbation의 탈출 시간 상계도 도출했다. 전체 stationary saddle와 혼동하지 않는다.
2. **직접 실행:** exact population gradient-flow 1,080 설정/초기값 반복 중 1,080개가 이론적 deadline 안에서 amplitude0.1까지 탈출. seed101·211의 확인 설정540개 포함. 독립 dataset1,080개나 성공확률의 통계추정이 아니다.
3. **대안 설명:** soft easy-negative 선택은 동일 초기조건에서 탈출을 약99배 늦췄으나 frozen q도 거의 같은 지연이다. time100 관측만으로 영구 실명이라고 결론낼 수 없다.
4. **수정된 핵심 결과:** normalized full-capacity d3/d4 sphere의 square는 matched frozen q 아래 stable인데 adaptive q에서는 factor-balance mode가 unstable인 열린 조건을 도출했다. K1 전체 tangent spectrum 증명, K<=16 exact curvature와 독립 critic의 K2/K4 full tangent 검산이 있다.
5. **목적함수 통제:** importance correction은 uniform field를 정확 복구(max error1.39e-15). 같은 uniform objective의 최적화 실패라고 주장하지 않는다.

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
Python3.12.14, NumPy2.3.5, SciPy1.17.0, Matplotlib; solver rtol1e-8,atol1e-11(base). 위 base 결과는 population 계산이다. 후속 actual minibatch lookup 결과는 아래 별도 기록을 참조한다. Neural image learning 결과는 없다.

## 현재 가장 큰 반론
충분한 차원만으로 normalization의 에너지 제약이 제거되지 않는다. normalized corner에서의 stable omission이 frozen q에서도 유지되면 피드백 고유성의 증거가 아니다. full d3/d4 sphere tangent와 K2/K4 검산은 critic이 완료했다. Generic performative Jacobian 이상의 독립적 학술성과 실제 filtering 정책에서의 예측력은 남은 문턱이다.

## 독립 후속 실행

[세 요인·충분 차원 검증](../review/three-factor-extension/README.md), [비동일 positive 및 실제 minibatch30회](../review/robustness-extension/README.md), [후속 코드 독립 감사](../review/robustness-extension/independent-review.md)를 추가했다. Nonidentity positive는 population 검산이고 SGD는 identity positives다. SGD의 worst-factor noisy Bayes accuracy는 uniform/frozen 관측1.000,adaptive.4934–.4984였다. Noiseless 정보 소실을 주장하지 않는다. [최종 종합판정](../coordination/final_report.md).

## 기록
`literature.md`, `progress.md`, `verdict.md`와 모든 코드·결과를 연결한다. 실패한 base 가설은 N1 성공으로 덮어쓰지 않는다.

## 최종 문서
- [verdict.md](verdict.md): 수정 후 진행 판정 및 남은 문턱
- [paper_draft.md](paper_draft.md): 실제 결과를 중심으로 한 논문 뼈대
- [results/multi_negative_summary.json](results/multi_negative_summary.json): K1–16 exact control
- [results/importance_control.json](results/importance_control.json): 동일 목적함수 보정 통제
