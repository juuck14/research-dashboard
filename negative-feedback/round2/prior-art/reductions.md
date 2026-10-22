# 기존 설명을 실제로 적용해 본 결과

2026-10-22. 아래는 외부 논문의 정리를 그대로 옮긴 것이 아니라, 본 감사에서 직접 수행한 환원과 계산이다. 목적은 얻은 결과를 최대한 기존의 단순한 설명으로 설명해 보고도 남는 기여가 무엇인지 정하는 것이다.

## 1. Equal frozen weights/opposite adaptive stability는 SSL 없이 가능하다

실수 theta와 두 점 Z∈{-1,1}에서

\[
\ell(\theta,Z)=\tfrac12\theta^2-Z\theta,
\qquad P_m(Z=1\mid\theta)=\tfrac12[1+\tanh(m\theta)].
\]

유한 theta에서 모든 점의 확률은 양수다. theta=0에서 m과 관계없이 induced distribution은 균등하며, 그 frozen risk는 theta²/2로 strictly convex하다. Detached/repeated-gradient field는

\[
G_m(\theta)=\mathbb E_{Z\sim P_m(\cdot\mid\theta)}\partial_\theta\ell(\theta,Z)
=\theta-\tanh(m\theta),\qquad G_m'(0)=1-m.
\]

따라서 m=.5는 attracting, m=2는 repelling이다. 같은 frozen distribution과 같은 frozen objective의 curvature1을 갖고도 동역학은 반대다. 이것은 [Perdomo et al., Definition3.7](https://proceedings.mlr.press/v119/perdomo20a/perdomo20a.pdf)의 반복 gradient 틀에 정확히 들어가는 elementary witness다. 원 논문의 global strong-convexity convergence theorem을 구면에 억지 적용할 필요조차 없다. **같은 weights/다른 response라는 일반 명제는 독립 신규성 근거가 아니다.**

## 2. K1 balanced mode는 self-paced 곡률로 환원된다

Square의 adjacent scores를 t와 −t로 쓰고 `ell(s)=log(1+exp(s−1))`라 두자. Policy

\[
q_j(t)=\epsilon/4+(1-\epsilon)w(s_j(t))/Z(t)
\]

에서 self/opposite scores는1,−1로 일정하며 `Z(t)=w(1)+w(−1)+w(t)+w(−t)`이므로 Z'(0)=0이다. Adjacent 확률과 도함수를 v=q_adj(0), g=q'_adj(0)라고 쓰면, balance 방향 field derivative는 양의 metric 상수를 제외하고

\[
v\ell''(0)+g\ell'(0).
\]

Frozen policy에는 첫 항만 남는다. Primitive `rho'(s)=q_local(s)ell'(s)`를 두면 이는 정확히 `rho''(0)`이다. 감소하는 weight가 loss curvature를 뒤집을 수 있는 것은 [Fan et al.의 implicit robust loss](https://arxiv.org/pdf/1606.00128)와 같은 원리다. 이 local 환원을 full epsilon-mixture field의 전역 potential 등식으로 확대하지 않는다.

K1에서 `ell'(0)=sigma(−1)`, `ell''(0)/ell'(0)=sigma(1)`이므로 stability threshold는

\[
\eta=-g/v<\sigma(1)=0.7310585786.
\]

K1 수치만으로 기존 robust-weighting 이론이 놓친 새로운 기제라고 주장할 수 없다.

## 3. Pure exponential 정책의 infinite-K limit은 effective temperature다

Identity positives와 normalized representations에서 positive score는1이다. Negative 후보 j의 score를 s_ij, policy를

\[
q_{ij}(F)=\frac{\exp(\kappa s_{ij})}{\sum_l\exp(\kappa s_{il})}
\]

로 두자. 유한 후보와 양의 support이므로 K→∞에서 law of large numbers로 negative tuple에 대한 detached mean gradient가

\[
G_\infty(F)=\frac1n\sum_i\sum_j
\frac{q_{ij}e^{s_{ij}}}{\sum_lq_{il}e^{s_{il}}}\nabla_Fs_{ij}
=\frac1n\sum_i\sum_j\operatorname{softmax}_j((1+\kappa)s_i)\nabla_Fs_{ij}
\]

가 된다. 이는 kappa≠−1에서

\[
\Phi_\kappa(F)=\frac1{n(1+\kappa)}\sum_i\log\sum_j\exp((1+\kappa)s_{ij})
\]

의 gradient와 정확히 같다. 구면에서는 양쪽에 같은 tangent projection을 하면 등식이 유지된다. kappa=−1에서는 divergent constant를 제외한 limit이 `n^{-2} sum_ij s_ij`이다. 따라서 infinite-K에서 critical slope1은 temperature inversion이라는 단순한 설명을 갖는다. 이 limit만으로는 유한 K 임계곡선이 나오지 않는다.

`audit_checks.py`는 seed901-910의 임의 normalized6x4 lookup과 kappa∈{-2,-1,-.5,0,1,2}에서 이를 독립 계산했다. 최대 coordinate error1.11e−16. Epsilon=.1 mixture는 같은 pure-temperature 식과 최대.0256571 차이가 났다. 이는 특정 pure-temperature 환원이 mixture에 그대로 성립하지 않는다는 검사이며, mixture에 어떤 integrating factor도 존재하지 않는다는 증명은 아니다.

## 4. Natural exponential에서는 mode stabilization이 전체 안정성을 보장하지 않는다

기존 shaped policy는 static square weights를 base kappa=−2로 고정하고 slope만 바꾼다. 이 설계의 필요성을 확인하려고 natural `w(s)=exp(−s)`, epsilon=.1을 사전 고정해 계산했다. Square에서

\[
u=.09009654,\quad v=.20195074,\quad w=.50600198,
\quad\eta=.87620744.
\]

`u`는 self, `v`는 adjacent 하나, `w`는 opposite의 확률이다. `a=exp(−1)`, N은 adjacent 개수, O는 opposite 개수, D는 InfoNCE denominator라 두면 normal ab mode의 gradient curvature는

\[
\lambda_\perp=-\frac a2\mathbb E[N/D]+a^2\mathbb E[O/D].
\]

| K | balance curvature | normal ab curvature |
|---:|---:|---:|
| 1 | −.01576692 | +.00600400 |
| 4 | −.01237810 | +.00442992 |
| 8 | +.00436686 | −.00145613 |
| 16 | +.02411616 | −.00793832 |
| 128 | +.05423005 | −.01724015 |

Curvature 양수는 negative gradient flow에서 attracting이다. Factor mode가 돌아오는 동안 normal mode가 무너진다. Infinite-K에서는

\[
\lambda_\perp\to\frac{-av+a^2w}{u+2av+a^2w}<0
\]

이며 w/v≈2.506<exp(1)이므로 부호가 엄밀히 음수다. 이 한 설정에서의 balance rescue를 exponential policy 일반에 대한 full rescue로 바꾸어 말하면 틀린다. 반대로 exponential family 전체에서 rescue가 불가능하다고 해석해도 틀린다. 이 변화는 더 많은 negative가 정보 보존을 해친다는 결론도 아니다. Square를 떠난 다른 high-rank geometry는 두 bit를 보존할 수 있다.

### 분석 후 선택한 follow-up: natural family도 가능하다

위 실패를 본 뒤 root가 epsilon=.3,kappa=−log4를 분석적으로 구성했다. 이는 독립된 사전 고정 replication이 아니다. 이때 u=.103,v=.187,w=.523이며 w/v≈2.79679>e, eta≈.83029395다. 변경하지 않은 enumeration 코드로 K1-128을 계산했을 때 첫 balance-stable K는5, normal_ab의 최솟값은+.00753310이었다. `natural_exponential_followup.csv`에 전부 보존했다. Full tangent의 남은 mode를 검사하는 것은 theory 담당의 별도 작업이다. 이 수정은 결과를 살리려고 원래 실패를 삭제하는 것이 아니라, 실패의 논리적 범위를 명확히 한 것이다: **balance 안정화는 충분조건이 아니지만, natural exponential에서도 적절한 floor와 slope가 다른 mode를 함께 안정화할 수 있다.**

## 5. DCL control: negative-positive coupling만으로는 충분하지 않다

[Yeh et al., ECCV2022, Proposition1-2](https://www.ecva.net/papers/eccv_2022/papers_ECCV/papers/136860653.pdf)는 positive score를 denominator에서 제거하여 negative-positive coupling(NPC) multiplier를 제거한다. 이 설명이 유한-K phase의 전부인지 직접 확인했다.

동일 detached policy와 finite tuple를 유지하고 loss denominator만

\[
D_-=n_{self}+aN+a^2O
\]

로 바꾼다. Balanced point에서 adjacent 두 방향을 조건부 균등분할하면, conditional square count difference의 분산이 N이므로 balance-mode의 angle field derivative는

\[
H_K^-=4a\,\mathbb E[N/D_-]
\left(1+g/v-aR_K^-\right),
\qquad R_K^-=\frac{\mathbb E[N/D_-^2]}{\mathbb E[N/D_-]}.
\]

K1에는 adjacent가 뽑힌 경우 D_-=a이므로 `R_1^-=1/a`, threshold0이다. Size-bias identity로 `R_K^-`는 `T=a+sum_{r=1}^{K-1}Z_r`, Z_r∈{1,a,a²}에 대한 `E[T^{-2}]/E[T^{-1}]`이다. 독립 양의 항을 추가할수록 이 비율은 엄밀히 감소한다. 실제로 deterministic shift c에 대한 도함수는

\[
\frac{-2\mathbb E[(T+c)^{-3}]\mathbb E[(T+c)^{-1}]
+\mathbb E[(T+c)^{-2}]^2}{\mathbb E[(T+c)^{-1}]^2}<0
\]

이며 Cauchy-Schwarz가 부호를 준다. Random positive shift는 각 shifted ratio의 양의 weighted average이므로 역시 원 비율보다 작다. T는 최소 `a+(K−1)a²`이므로 ratio→0, threshold→1이다. 이것은 직접 증명한 scalar-mode extension이며 theory 담당의 independent verification 대상이다.

동일 shaped policy alpha=−.9, epsilon=.1에서 exact count enumeration 결과:

| K | InfoNCE threshold | DCL threshold | DCL balance curvature |
|---:|---:|---:|---:|
| 1 | .73105858 | 0 | −.20788730 |
| 4 | .81283012 | .59944381 | −.09819630 |
| 8 | .86868895 | .78915305 | −.03101624 |
| 16 | .91881352 | .89438118 | +.00958794 |
| 128 | .98752186 | .98707931 | +.04609512 |

Negative-positive coupling을 없애도 sampler response와 finite-negative softmax curvature의 경쟁은 남는다. 그러므로 “이번 결과는 NPC multiplier가 작아서 학습이 느린 현상일 뿐”이라는 강한 null은 이 제한 모형에서 반박된다. 반면 이것은 DCL이 실전에서 나쁘다는 주장도, DCL 전체 tangent가 안정해졌다는 주장도 아니다. K1 DCL frozen balance curvature는0이므로 그 점의 strict-frozen-minimum 반전 예로 쓸 수도 없다.
