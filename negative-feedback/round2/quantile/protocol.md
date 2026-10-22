# Rank-filter 확인 규약

2026-10-22 실행 전 기록. 목적은 exponential soft-filter의 미분에서 나온 현상이 score rank로 선택하는 규칙에서도 있는지, 그리고 충분 차원 및 matched frozen 통제에서 유지되는지 확인하는 것이다. 이 규칙이 GloFND 전체 알고리즘과 같다고 주장하지 않는다.

네 상태 full sphere lookup d4, identity positives, one-negative InfoNCE. Anchor 자신을 제외한 세 상태에 균등한 원 후보분포를 둔다. 가장 낮은 score의 후보부터 원 확률질량의 정확히50%를 유지한다. 경계에서 필요한 만큼 fractional acceptance를 하고, 동점에서는 남은 질량을 균등 분배한다. 재정규화 후 epsilon=.1 uniform-over3 floor를 섞는다. 이 규칙은 불연속이며 smooth Jacobian으로 평가하지 않는다.

Square 평형에서 예상 q는 opposite w=2/3*(1-eps)+eps/3, adjacent 각각v=1/6*(1-eps)+eps/3. 같은 q를 고정한 대조와 현재 rank로 갱신하는 정책을 비교한다. theta=pi/4±delta의 tied factor perturbation은delta∈{1e-2,1e-4,1e-6}. 예상 one-sided tied field는 부호에 따라 극한 ±(1-eps)*sigmoid(-1)/6이며, 이 계수는 전체 lookup metric을 반영한다. 계수가 틀리면 코드와 수식을 점검하고 변경 이유를 기록한다.

실행은 frozen 전체 tangent finite difference, discontinuous adaptive의 one-sided vector field, 동일 초기조건 trajectory를 먼저 확인한다. full lookup d4의 arbitrary perturbation primary seeds7101–7103, confirmation7301–7303, positive noise는 이번 실험에서 추가하지 않는다. 결과를 본 뒤 retention ratio를 바꿔 성공 조건을 찾지 않는다. Frozen이 stable하지 않거나 adaptive가 더 이상 성장을 보이지 않으면 rank 규칙으로의 확장은 실패로 기록한다. 유한시간 거리 감소를 noiseless 정보 소실로 해석하지 않는다.
