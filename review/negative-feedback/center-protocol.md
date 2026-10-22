# 추가 분석 규약: 충분 요인 표현의 피드백 불안정성

2026-10-22. 최초 15조건 corner 검산 완료 뒤 owner가 balanced square에서 frozen-q와 adaptive-q의 곡률 부호가 다르다는 공식을 전달했다. 처음의 '누락 요인 상태의 local Hessian'과 다른 질문이므로 추가 분석을 별도 기록한다.

- F0(a,b)=(a,b,0,...)/sqrt2를 S^(d-1) 위 **네 개의 독립 lookup vectors**로 다룬다. additive 두 parameter에 제한하지 않는다.
- d={2,3,4}, eps=.1, kappa=-2. d>=3는 four-state simplex를 표현할 수 있는 차원이다. q0=q(F0)를 고정한 것과 q(F)를 매번 갱신하는 것을 같은 basepoint에서 비교한다. sampler는 stop-gradient.
- 전체 4(d-1) tangent Jacobian eigenvalues를 계산한다. 전역 회전에 해당하는 zero modes를 제외한다. finite difference h=1e-5, 확인 h=3e-6, discrepancy<1e-7.
- frozen vector field 모든 nonrotation eigenvalue<0, adaptive 적어도 하나>0이면 이 basepoint의 policy responsiveness에 의한 local instability를 인정한다. 조건을 보고 바꾸지 않는다.
- d={3,4}, seeds={109,239}, initial tangent noise={1e-4,1e-6}, horizon100. 같은 초기 F를 frozen/adaptive에 주고 Procrustes 정렬 뒤 square 거리 변화를 기록한다. 이 실험은 global convergence나 정보 소실을 증명하지 않는다.
- 각 조건의 analytic tangent directional derivative와 independent scalar finite-difference loss gradient를 대조한다. minimum q, sphere norm drift, source/code versions를 기록한다.
