# 実行 기록 / research progress

2026-10-22. 모든 단계의 구분은 외부 원문 / 직접 증명 / 직접 실행 / 미검증 해석이다. 최상위 기여의 판정은 정리의 정확성과 별도다.

## R3-1 — 기준 고정과 원래 중요성 주장 반박

**계획:** JMLR를 primary target으로 고정하고 실제 게재 원문과 비교한다. 가장 먼저 square 불안정성이 의미 정보 소실인지 검사한다.

**실행:** `journal/`의 고정 rubric과 원문 대조, `endpoints/run.py`, 별도 seed의 `endpoints/flow.py`, 독립 `review/endpoint_check.py`.

**관측:** K4의 실제 안정 branch는 약한 요인 에너지 .46914를 보존한다(균형값 .5). 무잡음 representation은 injective다. K1에는 비식별 coarse attractor가 있지만 K4/5 경계를 일반적인 정보 소실 경계로 해석할 수 없다. 24개 흐름이 endpoint 예측을 확인했으며, 이것은 전역 basin 확률의 증명이 아니다.

**판단 변화:** round2의 제한 정리는 유지하지만 그것만으로 중요한 semantic-loss 설명을 확보했다는 해석은 기각. 상태: 수정 필요.

## R3-2 — square 밖의 증명과 동일 목적의 학습 검증

**실행:** `foundations/multilevel_theorem.md`에서 exchange-balanced score 방향의 all-K no-reentry와 필요충분 rescue-floor를 증명. `continuous_population.md`는 원자적 score tie 없이 연속 product-of-spheres에 실현한다. `general_normal_graph.md`는 stationary score-regular geometry에서 augmentation gap의 요구량이 K와 함께 엄격증가함을 증명한다. 기존 MLR 비교정태와 graph Laplacian 도구는 신규성에서 제외한다.

**실행:** `neural/view_theorem.md`의 full view spectrum과 `neural/results/mixing_interval_certificate.json`의 유향 반올림 계산. 동일 joint-K 목적, nonidentity positives, 모든 층을 학습하는 MLP에서 두 경계 모드를 검사한다.

**관측:** 자연 정책의 weak-positive-mixing .05 모형에서 full local stability는 정확히 K5..11. K16의 upper-bound 불안정은 frozen과 adaptive에 공통이며 feedback 효과로 부르지 않는다. 직접 비선형 parameter-gradient ODE가 선형 예측 exp(3)을 상대오차 7.6e-7 이내로 확인했다.

**실패 보존:** ordinary warmup 세 조건은 모두 사전에 정한 square applicability gate를 실패했다. oracle reference에서의 MLP 검증이 ordinary training에서 그 geometry에 도달한다는 증거는 아니다.

**현재 반론:** 일반 정리가 허용하는 symmetry 범위에서 새 지식이 JMLR 독자에게 충분히 중요한가. 독립 재심 전이므로 상태: 분석·재심 중.

## R3-3 — iid 범위의 결정적 반례

**실행:** `correlation/run.py`와 독립 `review/correlation_check.py`는 K12, source 수4, pair law와 unique-state-set 분포가 같은 두 block sampler의 반대 balance 부호를 확인했다. `correlation/certify.py`는 threshold 차이 >.005953527687868222030768을 정확한 유리수 구간으로 인증했다.

**해석:** pairwise ESS나 unique-set 분포만으로 iid count law를 확장할 수 없다. slope는 두 threshold 사이에 놓도록 구성한 반례이며, 별도 무작위 확인 결과라고 표현하지 않는다. nonlinear denominator에서 higher-order dependence가 중요할 수 있다는 일반 원리는 기존 지식이므로 보조 결과로 둔다.

**다음 판단:** 통합 원고에 중심 결과와 실패 범위를 연결하고, 작성 담당과 분리된 두 검토가 고정 6gate를 재적용한다. 핵심 gate가 미충족이면 50% 도달을 선언하지 않는다.
