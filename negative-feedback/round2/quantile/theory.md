# Bottom-half rank filtering의 정확한 반례

다음은 직접 증명한 제한 모형의 명제다. Hard rank filtering의 불연속성을 smooth Jacobian으로 숨기지 않는다. 이 명제가 GloFND 등의 전체 알고리즘과 같다는 주장도 하지 않는다.

## 명제

네 상태의 충분 차원 normalized lookup sphere와 identity positives, one-negative InfoNCE를 둔다. Self negative를 제외한 균등 세 후보에서 score가 가장 낮은 원 확률질량의 절반을 유지하고, quantile 경계 동점은 균등 분할한다. 재정규화한 sampler에 epsilon uniform-over3 floor를 섞는다. epsilon=.1일 때 balanced square는 matched-frozen 정책에서 회전 제외 strict local stable이지만, adaptive rank 정책에서는 factor-balance 방향으로 Lyapunov unstable이다.

## 증명

Square에서 opposite score=-1, 두 adjacent score=0이다. 낮은 score부터 절반 질량을 유지하면 opposite의 원 질량1/3을 모두 취하고 남은1/6을 두 adjacent에 균등 분배한다. 선택 분포는 opposite2/3, adjacent각1/6이며 floor 후 w=(1-epsilon)2/3+epsilon/3, v=(1-epsilon)/6+epsilon/3이다. 기존 full sphere frozen spectrum을 쓰면 strict stability 조건은 w sigmoid(-2)>v sigmoid(-1)이다. epsilon=.1에서 성립한다.

Tied perturbation f_theta=(cos(theta)*a,sin(theta)*b,0,0)을 보자. theta>pi/4이면 두 adjacent score ±cos(2theta)의 순서가 갈린다. 낮은 adjacent만 남은 원 질량1/6을 채우므로 floor 후 q_low=(1-epsilon)/3+epsilon/3=1/3, q_high=epsilon/3, q_opp=w다. theta→pi/4+에서 loss의 tied derivative는 2 sigmoid(-1)(q_high-q_low)=−2(1-epsilon)sigmoid(-1)/3이다. 네 lookup vectors의 tied tangent metric은4이므로 theta의 projected flow는 +(1-epsilon)sigmoid(-1)/6으로 접근한다. 반대쪽에서는 부호가 반대다.

이 양의 one-sided limit 때문에 충분히 작은 perturbation은 균형점 쪽으로 복귀하지 않고 양의 속도로 벗어난다. Tied 평면은 이 대칭 sampling 아래 불변이며 이 한 admissible 방향의 탈출만으로 전체 평형의 불안정성이 따른다. 정확히 동점인 square에서는 uniform tie rule 덕분에 vector field가0이다. 그러므로 discontinuous equilibrium이며, linear Jacobian 판정으로 대체할 수 없다. QED.

**정리와 수치 구현의 중요한 차이:** 위 Lyapunov 불안정성은 정확한 동점일 때에만 tie split을 적용하는 수학적 정책에 대한 명제다. `run.py`는 floating point score의 오차를 처리하기 위해 TIE=1e-12를 둔다. 그러면 score 차이가 이 tolerance 이내인 유한한 작은 띠에서는 frozen과 같은 tie split이 유지되므로, 이 구현 자체가 infinitesimal Lyapunov unstable이라고 말할 수 없다. Tied angle에서 띠의 폭은 대략 TIE/4이다. 실행한 perturbation1e-4와 one-sided delta1e-6은 이 띠보다 훨씬 크며, 수치 결과는 그 규모에서의 탈출을 검증한다. `tie_tolerance_control.csv`에 exact rank branch와 tolerance branch를 따로 비교한다. 이 구분은 독립 검토에서 지적되어 추가했다.

Small nonzero feature amplitude는 noiseless 정보 소실을 뜻하지 않는다. Smooth filter의 모든-K 정리와 이 불연속 quantile 명제는 별도 결과다.
