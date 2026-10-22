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
