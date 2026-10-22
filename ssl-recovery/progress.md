# 진행 기록

## 0. 원문과 초기 정식화

저장소 지침, 기존 target-correction의 기각 이유를 읽었다. Tian2021의 선형 predictor/EMA basin을 반복하는 것은 신규성 근거에서 제외한다. CP2026 원문 §3과 Appendix Fig15에서 fixed-LR 대조가 이미 있음을 재확인했다. Dual Perspectives2026 §4의 실제 방정식·평형 범위를 확인했다. BN-free nonlinear finite-state 학습에서 cross-view 관계 변화만을 조작하는 사전 protocol을 작성했다.

## 1. Pilot 실제 실행 및 강한 대안 설명

- 실행: protocol대로4seed·8정책의 exact population neural 학습. analytic gradient 중앙차분 최대차8.89e-11, marginal오차2.78e-17.
- 관측: continue의 최종 factor3 noisy linear R²는 2.73e-7–.00216, scratch는 .929–.989. state reset만으로 원래 기준까지 회복한 경우 없음.
- 변경: 이를 memory lock 지지로 해석하기 전에 equal primitive spectrum이 rank별 allocation을 선호하지 않는다는 대안을 도출했다. Amendment1에 flat optimum 직접 증명·spectral gap 대조·원래 confirmation·predictor moment control을 결과 전에 기록했다.
- 반론: predictor reset은 predictor moments를 유지해 stale-moment mismatch까지 포함한다는 reviewer 지적. 별도 control을 추가하되 기존 실패를 지우지 않는다.
- 상태: 분석·실험 중. 아직 신규 기여나 진행 권고 없음.
