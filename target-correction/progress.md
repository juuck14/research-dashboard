# 진행 기록

## 2026-10-22 P0 시작·실행 전 설계

- 실행: 기존 보고서 해당 방향 읽기, Tian2021·Richemond2023 원문 핵심 절 및 Korchinski2026 §5/C.3 확인 착수.
- 새 사실: collapse basin과 약한 initialization의 실패는 Tian2021이 이미 명시적으로 다룸. 기존 보고서보다 신규성 전망을 낮춤.
- 계획: finite-state Bayes operator와 linear predictor population flow를 분리 도출하고 실행. protocol.md를 실행 전에 저장.
- 반론: exact Bayes teacher update는 알려진 Markov smoothing/power iteration이고 predictor boundary는 Tian2021 재표기일 가능성이 높음.
- 상태: 분석 중. 수치 실험 아직 미실행.

## P1 정확한 식 도출·실행 전 설계 보완

- 직접 도출: theory.md 명제1–4. 유한상태 Bayes teacher update의 q_j^t 수축은 유한시간 정보 보존과 양립. trainable predictor에서 정확 EMA 고정점 및 Jacobian을 계산했다.
- 선행 관계: Tian2021 일반 Lemma1/Eq2–4의 특수화이며 §3.2 basin 결과와 같은 메커니즘. 독립 신규성에 대한 반론 강화.
- 설계 보완(실행 전): frozen-vs-EMA를 가장 명료하게 구분하는 analytic interval eta/rho<s0<s−의 midpoint 한 개를 지정해 추가한다. 결과를 보고 고른 조건이 아니라 방정식에서 미리 정한 비교다.
- 판정 변경: 원래 넓은 'full-rank target도 고착될 수 있다' 주장은 기존 dynamics로 재현될 가능성이 매우 높다. 결과 확인 후 기각 범위를 좁혀 기록한다.

## P2 Population 계산 완료

- 실행: `OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python target-correction/code/run_study.py`.
- 결과: exact 4-state recurrence error 8.88e−16. Primary72개 equilibrium max error 5.18e−9; 별도 rho/beta/3 seeds의108개 확인 max error8.64e−10. Jacobian36개 max error3.11e−15. Fixed predictor54개 stability criterion 전부 일치.
- frozen 대비 EMA 차이: 사전 지정 rho=.5,eta=.02,s0=.04192236에서 frozen equilibrium .03100290, EMA→0. 이는 명제3의 기존 weight-decay basin 설명과 일치.
- 대안 설명: eta=0에서 initial .001/.003/.01는 각각 t1257.82/421.67/126.90에 amplitude .2에 도달. rho*initial*time≈1로 느린 회복을 확인. finite-time plateau를 안정적 고착으로 해석할 수 없음.
- 판정: 현재 모형에서 독립 연구 신규성 기각. generic nonlinear impossibility는 주장하지 않음.
- 추가 반론 검사 계획: arbitrary full-rank target reparameterization B는 exact predictor에서 B E[Y|S]에 불과하다는 항등식을 도출. 원 문맥이 target의 약한 amplitude를 교정한다는 설명이 단순 조건부기대와 basis-change를 새 현상으로 부르는지 확인할 별도 exact 계산을 다음 실행에 추가한다. 기존 실험결과를 보고 성능을 높이는 수정은 아님.

## P3 Readout/시간축 대안 설명 및 교차 검토 대응

- 실행: context_basis_control.py 20개 exact nonorthogonal B 검증. 최대 inversion error4.71e−14. teacher full-rank scaling 자체는 population predictive-state 정보 교정이 아님.
- 그림 QA에서 발견: frozen 대조는 t1500에서 .0314034로 asymptotic .0310029에 아직 완전히 도달하지 않았음. 이는 작은 positive k의 logistic relaxation. finite-time 값을 equilibrium 관측으로 쓰지 않는다. 원래 결과·설정을 보존한다.
- 추가 확인 계획: 기존 frozen trajectory를 exact finite-time logistic 식과 비교한다. 새로운 simulation을 늘리지 않고 이미 저장한 CSV와 이론식을 검산할 것.
- 독립 reviewer가 Tian2021의 직접 동등성, Jacobian 및 finite-state rank!=MI 반례를 재확인. 우리는 diagonal finite-time invertibility만 주장하며 일반 rank 저하를 정보 소실이라고 부르지 않는다.
