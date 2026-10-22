# 정량 anchor 조건 아래 모든 관측 동치 decoder에 대한 한정된 positive 결과

상태: 직접 증명. 넓은 원래 질문의 해답은 아니다. 원래 MI Type S보다 아래 조건이 훨씬 강하다. 이 결과가 새로운 정리라는 주장은 하지 않는다.

## 가정과 명제

S⊂R²는 connected open domain. g0:S→R^m, ĝ0:Z→R^m는 C¹이고 m=2p+q,p>q. 각 s에서 A=Dg0(s)는 다음을 만족한다.

1. p개의 row는 (a_r,0), 다른 p개는 (0,a_r), |a_r|≥a>0. 각 group의 row index는 고정한다.
2. 남은 q개의 row는 arbitrary이며 Euclidean row norm≥a. 이들은 서로 다른 factor가 동시에 작용하는 행으로 허용한다.
3. learned reference C=Dĝ0(z)는 각 z에서 ||C||0≤m+q. C의 row pattern은 미리 알려 주지 않는다.

g,ĝ는 같은 observation manifold의 C¹ diffeomorphic charts이며 g=ĝ∘h, h:S→Z는 C¹ diffeomorphism이다. ||Dg−Dg0||op≤δ, ||Dĝ−Dĝ0||op≤δ, ||Dh||op≤L를 가정한다. 두 decoder의 singular values를 위아래로 제어하면 마지막 L bound를 유도할 수 있지만 이 노트는 L을 알려진 chart regularity 상수로 둔다. 이는 transition의 무한 확대를 제한하며 h=tI,t→0 같은 축소 gauge까지 금하지는 않는다. 아래 absolute derivative/C⁰ bound는 고정된 chart의 단위에 의존하고, normalized row direction에 대한 angle bound가 좌표별 재매개화에 불변인 핵심이다.

η=δ(1+L)<a/√2라 하자. 그러면 하나의 global permutation π가 존재하여 모든 s에서

각 Dh row를 길이1로 정규화했을 때 off-axis entry≤η/a이며, 따라서

`|∂h_{π(1)}/∂s2| ≤ Lη/a`, `|∂h_{π(2)}/∂s1| ≤ Lη/a`.

이는 true Jacobian의 graph를 알고 군집화하는 알고리즘 명제가 아니다. 위 조건을 만족하면서 **동일 관측을 정확히 설명하는 모든** learned decoder에 대한 transition h의 제한이다. 모집단 명제이고 작은 reconstruction MSE만으로 전제를 확인할 수는 없다.

## 증명

B=Dh(s)라 쓰면 chain rule로 Dg=Dĝ B이고,

`A−CB=(A−Dg)+(Dĝ−C)B`, 따라서 각 row residual의 norm≤η.

A의 모든 row norm≥a>η이므로 C에는 zero row가 없다. m개 row에 각 최소1개의 nonzero가 있고 총 nonzero≤m+q이므로 두 nonzero를 모두 가진 row는 최대 q개다. 따라서 p>q인 각 true anchor group에는 C에서 singleton인 row가 적어도 하나 있다.

true group i에서 그런 row를 택하면 A_r=a_r e_i^T, C_r=c_r e_j^T이고 c_r≠0이다. 따라서 dist(a_r e_i,span(B_j))≤η다. u_j=B_j/||B_j||라 하면 `|u_{j,3−i}|≤η/|a_r|≤η/a`다. 두 true groups가 같은 j를 택하면 ||u_j||²≤2(η/a)²<1이 되어 모순이다. 따라서 두 group은 서로 다른 B의 row를 선택한다. ||B_j||≤L이므로 해당 off-block entry의 절댓값≤Lη/a다.

이 assignment는 점마다 unique하다. η/a<1/√2이면 같은 normalized row가 두 축에 모두 허용되는 일은 없고, B는 invertible하므로 row가0을 지나지도 않는다. 연속인 B와 S의 connectedness로 assignment는 locally constant, 따라서 globally constant다. ∎

## 함수 수준으로 옮길 수 있는 범위

S=(−r,r)²이고 π로 행을 정렬한 뒤 `hbar(s,t)=(h1(s,0),h2(0,t))`라 하자. 위 off-block derivative를 선분 위 적분하면

`||h−hbar||∞ ≤ r Lη/a` (좌표별 maximum norm).

각 hbar_i는 일변수 C¹ 가역 함수다. 실제로 Dh의 row norm가0이 아니고 off-axis normalized entry<1/√2이므로 diagonal entry도0이 아니다. 연속성에 따라 그 부호가 일정하고 단조성을 얻는다.

그러나 이 증명만으로 `||h−hbar||C1=O(η)`를 얻은 것은 아니다. diagonal derivative가 다른 좌표에 따라 달라지는 양을 별도로 제어하지 않았다. `h_e(s,t)=(s+e² sin(s/e)t,t)`는 compact rectangle에서 off-block derivative O(e²), uniform C² bound를 가지지만 diagonal derivative의 t-variation은 O(e)다. 이는 **off-block derivative bound를 global C¹ approximation bound로 자동 승격하는 것**의 반례이며, decoder-C¹ leakage에 대한 원래 δ/κ 가설 전체를 반박하지는 않는다.

## 가정의 의미와 한계

- p>q는 pure anchors가 overlap보다 많다는 combinatorial diversity 조건이다. MI의 overlap<half support 조건과 가깝다.
- a는 row amplitude margin이다. ℓ0 gap를 연속화해 이름 붙인 tautological recovery modulus가 아니다.
- mixed row norm lower bound는 candidate zero row가 sparsity budget을 소모하지 않도록 방지한다. 이를 삭제하면 위 p>q counting은 성립하지 않는다.
- learned sparsity bound는 학습 결과가 자동 만족하는 성질이 아니다. surrogate loss가 작다고 이 ℓ0 또는 C¹-nearness를 보장하지 않는다.
- 전체 Type S, 다차원 block, weak anchor, arbitrary sensor mixing, finite samples, approximate reconstruction에 대한 정리가 아니다.
- 핵심 증명은 robust sparse-basis counting과 chain rule·connectedness·적분이다. 새 비선형 학습 원리보다 표준 perturbation 논리의 구체화에 가깝다. 이 부분만으로 수개월 독립 연구를 권할 근거는 약하다.
