# 독립 검산 실행 전 규약

2026-10-22. Owner의 unconstrained binary-factor exact enumeration을 읽은 뒤 독립 계산을 시작한다.

1. 네 상태 전체를 unit circle 위의 네 독립 각도로 매개화한다. identity positive, one-negative InfoNCE, q=epsilon/4+(1-epsilon)softmax(kappa*cosine). encoder dimension 2는 두 binary factors를 함께 구분할 수 있다.
2. 요인 하나만 남은 antipodal 상태의 **전체 네 tangent 방향** Jacobian을 구한다. diagonal factor path만으로 local minimum을 주장하지 않는다. 모든 실험은 CPU NumPy/SciPy, 정확한 population 열거다.
3. kappa={-8,-2,0,2,8}, epsilon={.01,.1,1}에서 frozen boundary q와 adaptive stop-gradient q의 Hessian/Jacobian을 비교한다. 수치 미분 h=1e-5, 별도 검산 h=3e-6. 차이 허용 1e-7. 전체 sampler를 미분하는 알고리즘은 별도 coefficient로 비교한다.
4. 수식 D=-q_same+2*q_opp*sigmoid(-2)의 곡률 부호와 전체 tangent eigenvalues를 검산한다. kappa<0의 stable state가 있더라도 frozen q에서 동일하면 feedback 자체의 발견으로 세지 않는다.
5. exploration seeds 31,47, confirmation seeds 103,227, 초기 perturbation 규모 1e-4에서 gradient flow를 time=40까지 실행한다. stable setting과 uniform control을 같은 초기 각도에 적용한다. 시간 연장은 하지 않는다.
6. 별도로 owner의 unnormalized missing-mode Jacobian을 독립 차분 계산하여 양의 floor lower bound와 대조한다. finite-time amplitude decay를 information erasure라고 부르지 않는다.

결과가 기존 정리의 직접 corollary인지와 단순 weighted geometry로 설명되는지는 원문 범위를 대조한다. 실험 후 이 규약은 변경하지 않고 추가 분석은 별도 이력으로 남긴다.
