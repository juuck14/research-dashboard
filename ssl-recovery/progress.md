# 진행 기록

## 0. 원문과 초기 정식화

저장소 지침과 기존 target-correction의 기각 이유를 읽었다. Tian 2021의 선형 predictor/EMA basin을 반복하는 것은 신규성 근거에서 제외했다. CP 2026 원문 §3과 Appendix Fig15에서 fixed LR 대조가 이미 있음을 재확인했다. Dual Perspectives 2026 §4의 실제 방정식과 평형 범위를 확인했다. BN-free nonlinear finite-state 학습에서 cross-view 관계 변화만을 조작하는 실행 전 protocol을 작성했다.

## 1. Pilot 실행 및 강한 대안 설명

- 실행: protocol대로 4개 seed와 8개 정책의 exact population neural 학습. Analytic gradient 중앙차분 최대 차이는 8.89e−11, marginal 오차는 2.78e−17.
- 관측: continue의 최종 factor 3 noisy linear R²는 2.73e−7–.00216, scratch는 .929–.989. 상태 reset으로 원래 기준까지 회복한 경우는 없었다.
- 변경: 이를 memory lock의 지지로 해석하기 전에 equal primitive spectrum이 rank별 allocation을 선호하지 않는다는 대안을 도출했다. Amendment 1에 flat optimum의 직접 증명, spectral gap 대조, 원래 confirmation, predictor moment control을 결과 전에 기록했다.
- 반론: predictor reset은 predictor moments를 유지해 stale-moment mismatch까지 포함한다는 독립 검토자의 지적을 받았다. 별도 control을 추가하고 기존 실패를 보존했다.
- 당시 상태: 분석·실험 중. 신규 기여나 진행 권고를 내리지 않았다.

## 2. 독립 확인·목적함수 대조·장기 실행

- 실행: 원래 설정의 확인 seed 101–104, 모든 8개 seed의 rho3=.8/1 대조 15000 step, predictor 자체 moments reset, InfoNCE temperature 1 대조, 원래 equal rho의 15000 step 연장.
- 관측: 원래 3000 step continue의 최대 R²는 .00424였다. 그러나 15000 step에서는 4/8 seed가 >.9로 회복했다. Predictor와 head reset은 seed 101에서 .72–.74의 부분 회복이 있었고, 자체 moments까지 reset하면 .049였다. 어느 reset도 효과 없다는 주장을 하지 않는다.
- 관측: InfoNCE는 8개 seed 모두 50–250 step에 90% 기준에 도달했다. Rho3=1 대조도 장기에 모두 회복했지만 다른 factor 손실이 있었다. Rho3=.8의 seed 101 예외는 작은 fixed-head 경계를 neural 회복의 필요충분조건으로 쓸 수 없음을 보여 준다.
- 분석: odd map의 Fourier 상한, rank별 flat 최적해, 제한된 EMA/head mode의 안정성, contrastive allocation의 strict convexity를 직접 증명했다. 표준 spectral 계산으로 새로운 원리의 신규성을 주장하지 않는다.

## 3. 독립 검토에 따른 정정과 최종 보존

- Scalar Euclidean flow와 sphere Riemannian flow의 global time 식을 혼용한 부분을 분리했다. 독립 검토자가 정정 완료를 확인했다.
- SNR의 metadata상 2025년 v3와 HTML 내부 2026년 날짜의 불일치를 명시했다. Dual Perspectives의 개별 equilibrium 안정성은 rotation gauge 문제를 무시해 인용하지 않는다.
- Full trace는 scratch 외부로 이동하고 SHA·바이트 수·행수와 재생성 명령을 남겼다. 저장소에는 모든 run의 summary와 고정 간격 곡선 및 그림을 보존했다. 수치 결과에 따른 seed 선별은 없다.
- 원래 3000 step 값과 긴 실행의 3000 step 값은 모든 seed에서 정확히 일치했다. Norm-matched 개입의 평균 update norm 차이는 최대 2.72e−20이었다.
- 최종 상태: **기각 — 현재 구체화**. 원래 넓은 질문은 미해결이다. 새로운 가설의 핵심 검증이 없는 긍정 논문 초안을 작성하지 않았다. Owner와 독립 검토자의 판정은 일치한다.
