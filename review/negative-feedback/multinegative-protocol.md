# K>1 정확 기대 검산 규약

2026-10-22. K1 full-tangent square instability 확인 후 root가 one-negative 특수성 검사를 요청했다. Owner는 일반 K 법칙/trajectory를 수행하고 본 검산자는 K2/K4의 d4 full lookup tangent spectrum을 독립 계산한다.

동일 eps=.1, kappa=-2, square, detached q, q*=q(square) frozen 대조를 유지한다. K negatives는 조건부 iid q이며 각 네 상태의 count vector를 multinomial로 정확 열거한다. K2/K4에서는 모든 ordered negative sequences도 독립 열거하여 기대 loss/score gradient를 1e-12 안에서 비교한다. 전체12 tangent Jacobian을 h1e-5와3e-6 두 값으로 검산하고 frozen stable/adaptive unstable 부호가 유지되는지 기록한다. 실패해도 K/κ를 튜닝해 덮지 않는다. K1을 구현 sanity check로 추가한다.
