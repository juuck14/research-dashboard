# 주제5 독립 교차검토 사전 계획

2026-10-22. owner의 실행 전 protocol과 literature를 읽고 다음 독립 검산을 먼저 고정했다.

1. rho>0, eta>0, beta>0의 scalar flow에 대해 직접 Jacobian finite difference와 비영 고정점의 analytic spectrum을 비교한다. rho={0.35,0.8,0.95}, eta={0.005,0.02}, beta={0.001,0.1,10}. eta>rho²/4이면 비영점 부재를 확인한다.
2. frozen/EMA 및 predictor 없음/학습됨의 대조를 같은 rho=.8, eta=.02, 초기 w=p=.01, a=.1에서 실행한다. EMA beta={.001,.1,10}; solve_ivp T=5000, rtol=1e-10 atol=1e-12. 긴 시간 tiny amplitudes의 solver 음수/0는 의미 있는 정보 소실 증거로 쓰지 않는다.
3. 두 binary factor의 exact positive coefficient smoothing: (rho1,rho2)=(.9,.5), a0=(1,.1), beta=.5, t={0,10,100,200}. 유한시간 계수 양수의 정확식과 무잡음 state distinguishability를 기록한다. sigma=.01 고정 측정 잡음에서 Bayes bit accuracy Phi(a/sigma)를 보조 기록한다. 이는 무잡음 MI와 다른 측정 목표다.
4. finite-support rank counterexample: 네 binary states를 rank1 projection (1,c)로 보낸다. c={0,.001,.5,1}; distinct output 개수와 정보량을 정확 enumeration한다. rank1 자체가 semantic MI loss를 뜻하는지 반증한다.
5. analytic predictions 또는 source-equivalence가 틀리면 review에 수정한다. 새로운 양의 현상을 찾으려 설정을 무제한 변경하지 않는다.
