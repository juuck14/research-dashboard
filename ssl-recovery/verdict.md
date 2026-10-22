# 판정 — 현재 구체화 기각

**현재 확보한 내용으로 독립 논문 연구에 착수하도록 권하지 않는다.** 초기 보고서의 후보 1 우선 추천은 이 구체화에 대해 철회한다. 일반적인 nonlinear SSL의 회복 문제 전체를 기각한 것은 아니다.

## 결정적 근거

1. 실제 회복 지연은 재현했다. Raw marginal, 모형, LR, exact population exposure를 유지하고 cross-view factor 3의 correlation만 바꿨다. 8개 초기값에서 3000 clean update 후 접근성이 낮았다. BN와 유한 표본 부족은 설계상 없다.
2. 그러나 agreement objective는 missing factor를 복구할 의무가 없었다. Bias-free odd unit map의 정확한 Fourier 계산으로 rank 1·2·3이 모두 같은 전역 하한을 달성함을 증명했다. 이보다 강한 목적함수 대안을 제거하지 않은 채 state reset 결과를 새로운 memory lock으로 부를 수 없다.
3. 같은 법칙의 InfoNCE 대조에는 full-factor allocation의 엄격한 선호가 있고, 실제 nonlinear 8개 seed가 50–250 step에 기준 수준으로 회복했다. Teacher·head·목적함수가 함께 달라지는 비교이므로 teacher만의 효과를 주장하지 않는다.
4. 3000 step의 실패는 장기 불가능성이 아니었다. 원래 설정을 15000 step까지 같은 조건으로 확장하자 4/8 seed가 R²>.9로 회복했다. 나머지 seed의 점근 실패도 증명하지 않았다.
5. Reset의 부분 효과는 있지만 고유 원인과 예측 법칙이 없다. Predictor와 head+teacher 개입은 seed 101에서 .72–.74로 부분 회복한 반면, predictor 자체의 Adam moments까지 reset하면 .049였다. 이러한 상호작용은 일관된 단일 상태 원인을 지지하지 않는다.
6. 가까운 문헌은 CP 현상·fixed LR 통제, full-matrix linear EMA, nonlinear head의 weak-feature 가속, anisotropic weak subspace의 느린 학습, gradient 기반 trainability 진단까지 이미 포함한다. 현재 계산은 elementary spectral/perturbation 분석이며 이를 넘는 기여를 확보하지 못했다.

## 수정 시도와 진행하지 않는 이유

- **Teacher·optimizer·head의 상태 분리:** 여러 개입과 norm matching을 실제 실행했다. 일부 부분 회복과 상호작용을 발견했지만 상태량을 이용한 사전 예측은 없다. Reset 표를 논문 기여로 바꾸지 않는다.
- **Weak-factor recovery boundary:** 제한된 diagonal coefficient 모형의 EMA/head 경계를 직접 증명하고 독립 검산했다. 그러나 nonlinear neural seed 101은 약한 correlation에서도 회복해 그 경계의 일반화는 반박됐다. 작은 모형 자체는 표준 Taylor/spectral 계산이다.
- **Contrastive와 noncontrastive의 차이:** 실제 회복 곡선과 정확한 allocation 최적해 차이를 확인했다. 학습 loss의 기본 선택압 차이여서 새로운 critical-period 메커니즘의 증거로 대신할 수 없다.

## 확보한 결과와 증거 강도

- [직접 증명 A–C](theory.md): 제한 모형 안에서는 완전한 증명. 학술적 신규성 주장은 없다.
- [실제 실행](results.md): 4개 pilot와 4개 confirmation 초기값, 상태 복제 정책, 다른 correlation, 장기 continuation, 목적함수 대조. 자연 자료의 증거는 없다.
- [독립 교차 검토](../prevalidation-20261022/reviews/recovery/review.md): 별도 loss/gradient·flat family·Jacobian 검산. Owner와 reviewer는 현재 구체화의 기각에 동의한다. 개별 neural trajectory의 완전한 정량 설명은 아직 없다.

## 남은 위험과 재개 조건

표현의 의미와 view geometry가 더 복잡한 실제 SSL에서도 같은 flat optimum이 원인인지는 확인하지 않았다. 이번 finite-state 모형의 기각으로 그 질문을 대신하지 않는다. 새로 착수하려면 우선 **clean objective가 목표 factor를 엄격히 선호한다는 증거**를 확보해야 한다. 이후 random initial retention, 작은 mode amplitude, 알려진 head·EMA·optimizer conditioning을 맞추었는데도 다르게 회복하는 최소 사례가 필요하다. 그 차이를 예측하는 새로운 상태량을 별도 조건에서 검증해야 한다. 현재 그 핵심 검증이 없으므로 긍정적인 논문 초안을 작성하지 않는다.

더 많은 reset, backbone, 벤치마크 추가를 다음 작업으로 권하지 않는다. 첫 작업은 이번 [이론](theory.md)과 [독립 검토](../prevalidation-20261022/reviews/recovery/theory.md)를 재현하고, 엄격한 복구 선호 아래 새로운 현상이 실제로 있는지 하나의 사례로 확인하는 것이다.
