# 후속 단계 중간 기록

## 체크포인트 1 — 2026-10-22

상태: 분석·실험 중. 아직 최종 판정 아님.

### 실행하여 확보한 것

- `theory/results/`: 일반 smooth score filter에서 factor-balance curvature를 finite-K multinomial expectation으로 계산했다. full tangent spectrum과 finite difference를 비교했다. 엄밀 증명과 독립 검토가 진행 중이며, 수치 sweep을 모든 K의 증명으로 취급하지 않는다.
- `quantile/theory.md`: no-self bottom-half negative retention에서 square의 frozen 안정성과 adaptive의 일방향 불안정성을 별도 도출했다. smooth Jacobian을 rank rule에 적용하지 않았다.
- `quantile/results/summary.json`: fixed policy의 가장 느린 비회전 flow eigenvalue -0.0261893, adaptive의 일방향 angular speed 0.0403412. 일반 d4 perturbation 6개에서 frozen 수축, adaptive 확장을 관측했다. 관측한 궤적은 정보 소실의 증거가 아니다.
- `encoder/`: 사전 규약과 수동 NumPy MLP gradient check를 남긴 뒤 실제 shared nonlinear encoder 학습을 실행 중이다. 완료된 개별 seed 결과는 임시 파일이며 전체 확인 집합과 평가가 끝나기 전 일반 성공으로 요약하지 않는다.

### 이전 판단에서 달라진 점

같은 순간의 q 값과 다른 local q sensitivity를 구분하는 것 자체는 robust/self-paced curvature의 일반 원리다. 이를 독립적 신규성으로 주장하지 않는다. 핵심 후보는 finite negative 수에 따른 정확한 안정성 경계와 그 경계가 만드는 검증 가능한 예측이다. negative 수를 늘리는 실험은 population field 자체를 바꾸므로 optimizer noise 효과로 설명하지 않는다.

### 가장 강한 반론

1. 네 상태 square의 대칭성이 결론을 만드는가.
2. 자연 exponential filter에서는 normal mode가 불안정할 수 있으므로 factor-angle 안정성만으로 전체 안정성을 말할 수 없다.
3. finite-K correction은 알려진 InfoNCE denominator bias/NPC의 직접 재현인가.
4. 비선형 warmup이 tetrahedral geometry를 만들면 mechanism의 실용적 범위는 제한될 수 있다.

### 다음 검증

독립 담당이 proof와 count oracle를 공격한다. 문헌 담당은 DCL에서 positive denominator를 제거한 exact control을 실행한다. encoder 담당은 고정된 primary/confirmation seed를 끝까지 실행한다. 이 세 작업이 각각 증명의 오류, 기존 설명에 의한 환원, 표현 학습으로의 적용 범위를 결정한다.

## 체크포인트 2 — 실제 핵심 결과 확보

상태: 검증된 수정 방향으로 진행. 이 기록은 최종 실행과 교차 검토 이후 작성했다.

- 일반 smooth policy의 full spectrum,엄격한 K 단조성,full-space 충분조건을 완전 도출했다. 독립 reviewer가 count-Palm 전개와 proof를 다시 계산했다.
- DCL/general offset 분석에서 count 전이가 남는 것을 증명·실행했다. NPC의 영향은 존재하지만 sole explanation은 아니다.
- 최초 자연 exp κ=-1,epsilon.1은 normal mode에서 실패했다. 이를 보존한 뒤 root가 value/slope 부등식으로 log4,epsilon.3을 선정했고, 열린 natural-policy 영역의 증명으로 일반화했다. Numeric policy sweep로 성공 예를 고른 것은 아니다. 예 선택과 열린 영역 증명의 정확한 선후를 과장하지 않도록 원고를 교정했다.
- 독립 directed interval로 InfoNCE naturalK5,DCLK8,matchedInfoK9,DCLK14 경계를 인증했다. 초기 Decimal unaryminus rounding 오류는 reviewer가 발견·수정하고 다시 실행했다.
- Root가 protocol을 먼저 저장한 뒤 naturalK4/5의 full d4 population flow16건을 적분했다. 모든 기준 통과. Adaptive 불균형 비율은 K4 약20.0852,K5 약.0497871이었다.
- SharedMLP36fork의 원래 clean/noisy gate는 실패했다. Energy compression과 noisy fragility는 관측했지만 strongcollapse 주장은 살리지 않았다. OLS는 관측후 선언한 고정 diagnostic이고 PCA의 잔여 clean정보를 보여줬다.
- Critic은 별도 seed150좌표 gradient와36모델 OLS를 독립 재계산했다. Energy ratio를 coefficient norm ratio라고 쓴 문장을 수정했다.
- Quantile의 positive tie tolerance가 작은 stable band를 만든다는 반론을 실제 비교하고 ideal policy theorem과 finite-tolerance experiment를 구분했다.
- 독립 원고 심사에서 toy Z support,K1 curvature 비례상수,Palm sum기호,InfoNCE-only 안정성 범위,검산 집계 단위를 교정했다. 새로운 증명 결함이나 현재 좁은 claim의 미실행 핵심 검증은 발견되지 않았다.

최종 문서: `report_ko.md`,`manuscript.md`,`decisive_questions.md`,`reproduction.md`. 남은 작업의 실패가 무엇을 무너뜨리는지는 불확실성 표에 명시했다. 넓은 neural semantic-erasure 논문은 성립했다고 말하지 않는다.
