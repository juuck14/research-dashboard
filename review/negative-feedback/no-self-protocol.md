# Self negative 제거 확인

2026-10-22. full-support K1/K2/K4 결과 뒤 root가 동일 latent state를 negative로 뽑는 설정의 대안 설명을 지적했다. 이번 확인은 anchor 자신과 동일한 네 상태의 index를 negative 후보에서 제외한다. 나머지 세 후보 위 q>=eps/3, eps=.1,kappa=-2를 유지한다. d4 square lookup의 전체 tangent frozen/adaptive Jacobian을 h1e-5/3e-6으로 비교한다. 이 추가 실험은 원래 네 후보 실험을 대체하지 않는다.
