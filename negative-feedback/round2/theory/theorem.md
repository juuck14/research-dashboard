# General-policy full-spectrum theorem and negative-count stabilization

Status: complete analytic derivations and executed numerical checks. All results below concern the finite-state normalized lookup model specified here. The mathematics is derived in this work; **publication novelty relative to all earlier literature is not asserted by this file**. Generic distribution-response Jacobian terms are not claimed as new.

## 1. Model and definitions

Let `X=(a,b)` be uniform on `{-1,+1}²`. Each of the four observations has an independently trainable unit embedding `f_i ∈ S^(d−1)`, `d≥3`. Thus there is enough dimension for an injective simplex representation. Positives are identity positives and temperature is one. For K independent negative draws, the loss is

`ell_i=log(1+sum_{r=1}^K exp(f_i·f_{Y_r}−1))`.

Let `omega:[−1,1]→(0,infinity)` be C² and `0<epsilon<1`. The sampling policy is

`q_F(j|i)=epsilon/4+(1−epsilon) omega(f_i·f_j)/sum_l omega(f_i·f_l)`.

The sampler is detached in each learning update. Consequently the population vector field is `G(F)=E_{i,Y~q_F^K}[grad_F ell_i]`, followed by sphere tangent projection. The actual flow is `dot F=−G(F)`. It is generally not the gradient of the composed expected loss through q.

Consider the square `f_i*=(a_i,b_i,0,...)/sqrt(2)`. Define

```
A = exp(−1), B=exp(−2)=A²,
Z = omega(1)+2 omega(0)+omega(−1), c=1−epsilon,
t0=omega(1)/Z, t1=omega(0)/Z, t2=omega(−1)/Z,
u=epsilon/4+c*t0, v=epsilon/4+c*t1, w=epsilon/4+c*t2,
g=c*omega'(0)/Z, eta=−g/v.
```

Here u is the self-category probability, v each adjacent-category probability, and w the opposite-category probability. All are strictly positive. The weights `(t0,2t1,t2)` sum to one, as do `(u,2v,w)`. The matched-frozen comparison keeps `q*=q(F*)` fixed for every subsequent representation F. This frozen objective is exactly the same for any policies with identical omega values at scores `{-1,0,1}`.

Square is a stationary point of both fields by the four-state symmetries. Let `(U,N,W)~Multinomial(K;u,2v,w)` denote self, aggregate-adjacent, and opposite counts. Define

```
D=1+U+A*N+B*W,
M=E[N/D], R=E[N/D²]/M, C=E[W/D],
S=U*t0/u+N*t1/v+W*t2/w.
```

M is positive for every finite K. The denominator D is the InfoNCE denominator after aggregating the two equally likely adjacent categories.

## 2. Theorem 1: exact full tangent spectrum for every K

The Jacobian of the projected loss-gradient field G at the square has the following eigenvalues. The actual flow Jacobian has their negatives. The multiplicity statements exhaust `4(d−1)` tangent degrees of freedom.

| Mode | Frozen q* | Adaptive q |
|---|---|---|
| In-plane factor-balance, one mode | `lambda_b=A*M−A²*E[N/D²]` | `lambda_b + (A*g/v)*M` |
| In-plane remaining characters, two modes | `lambda_p=A*M/2−(A²/4)*E[(N²+N)/D²]+B*C` | `lambda_p + A*g*(E[(N²+N)/D]/(4v)−E[N*S/D]/2)` |
| Normal constant character, each extra dimension | `lambda_+=A*M/2+B*C` | same |
| Normal product character, each extra dimension | `lambda_−=−A*M/2+B*C` | same |
| Rotations, `2d−3` modes | 0 | 0 |

For d≥3 there are d−2 copies of each normal mode. In particular **the arbitrary-K calculation is not limited to one tied angle coordinate**.

### Proof

At the square every anchor sees scores `(1,0,0,−1)`. Work with great-circle perturbations, whose derivatives lie in the product-sphere tangent space. Symmetries of the square make the binary characters `{1,a,b,ab}` simultaneous invariant modes in the in-plane and each normal coordinate. Interchanging a and b gives the two-fold in-plane degeneracy. Reflection in the square plane makes the normal and in-plane blocks independent. Thus it is sufficient to calculate each character's directional derivative. Each chosen direction has squared parameter norm four; directional curvatures must therefore be divided by four to obtain the displayed Jacobian eigenvalues.

For the factor-balance character, the two adjacent scores have derivatives `−2,+2`, while self and opposite scores have derivative zero; all second derivatives vanish. Let their individual counts be N1,N2 and `Delta=N2−N1`. Conditional on U,N,W, the two adjacent categories are equally likely, so

`E[Delta²|U,N,W]=N`.

The loss first derivative is `2A*Delta/D`; its frozen second derivative is `4A*N/D−4A²*Delta²/D²`. The score-policy normalizer has derivative zero in this direction, so the tuple log-probability derivative is `2g*Delta/v`. The detached-field derivative is the frozen second derivative plus the first loss derivative times this log-probability derivative. Conditional averaging and division by four yield

`lambda_b^adaptive=A*M−A²*E[N/D²]+A*g*M/v`.

For an in-plane a or b character, one adjacent score has derivative ±2, the other zero, and the opposite score has second derivative four. The relevant adjacent count, say N2, satisfies

`E[N2|U,N,W]=N/2`, `E[N2²|U,N,W]=(N²+N)/4`.

The frozen directional second derivative is

`4A*N2/D−4A²*N2²/D²+4B*W/D`.

Along the representative with negative adjacent score derivative, the loss first derivative is `−2A*N2/D`. The derivative of the tuple log-probability is

`g*(−2N2/v+2S)`.

Here S includes the row-normalizer derivative and the epsilon mixture; omitting this term gives an incorrect answer. Multiplication, conditional averaging, and division by four give the displayed lambda_p and its response term. All anchors have the same expected directional curvature by symmetry.

For a normal character chi, write `f_i(t)=cos(t)f_i*+sin(t)chi_i e_normal`. Every pair score has first derivative zero, so the sampler response contributes nothing. The score second derivative is `2(chi_i chi_j−s_ij)`. Constant chi gives aggregate second derivative `2A*N/D+4B*W/D`, whereas chi=ab gives `−2A*N/D+4B*W/D`. Divide by four to obtain lambda_+ and lambda_−. Normal characters a,b correspond to global rotations and give zero. The in-plane constant character is also a rotation. The resulting zero-mode count is `1+2(d−2)=2d−3`.

These modes exhaust the tangent space: three nonrotation in-plane modes, `2(d−2)` nonrotation normal modes, and `2d−3` rotations sum to `4(d−1)`. This completes the spectrum. QED.

## 3. Theorem 2: exact factor-balance threshold and its monotonicity in K

Let

`T_K=1−A*R_K`, where `R_K=E[N/D²]/E[N/D]`.

Then

`lambda_b^adaptive = A*E[N/D]*(T_K−eta)`.

The threshold sequence is strictly increasing, with

```
T_1 = 1/(1+A) = 0.7310585786...,
T_K < 1 for every finite K,
lim_K T_K = 1.
```

Thus eta<T_K gives positive factor-balance curvature and eta>T_K gives an unstable factor-balance mode. Equality is a nonhyperbolic boundary; this theorem does not determine nonlinear stability there.

### Proof of the curvature identity

It is direct factorization of Theorem 1 and the definition eta=−g/v. The frozen factor-balance eigenvalue is positive because

`A*R_K ≤ A/(1+A) < 1`.

The bound follows since N≥1 whenever its size-bias weight is nonzero, hence D≥1+A.

### Proof of strict monotonicity

By exchangeability of the K negative draws, select one adjacent draw and condition on it. If `Z_l` are iid with values `{1,A,B}` and probabilities `{u,2v,w}`, then

```
E[N/D^p]=2K*v*E[Y_K^(−p)],
Y_K=1+A+sum_{l=1}^{K−1} Z_l,
R_K=E[Y_K^(−2)]/E[Y_K^(−1)].
```

For any positive bounded random variable Y, let

`r_Y(z)=E[(Y+z)^−2]/E[(Y+z)^−1]`, z≥0.

Put m_j(z)=E[(Y+z)^−j]. Differentiation yields

`r_Y'(z)=(-2m3*m1+m2²)/m1² < 0`.

Cauchy–Schwarz gives `m3*m1≥m2²`, so the numerator is at most `−m2²<0`. Now add an independent strictly positive random Z. Its ratio is a weighted average of the deterministic-shift ratios:

`E[(Y+Z)^−2]/E[(Y+Z)^−1] = E_Z[m1(Z)*r_Y(Z)]/E_Z[m1(Z)]`.

Every r_Y(Z) is strictly less than r_Y(0), so the weighted average is too. Apply this with `Y=Y_K`, `Z=Z_K`. Therefore R_{K+1}<R_K and T_{K+1}>T_K.

At K=1, Y1=1+A is constant, giving T1=1−A/(1+A)=1/(1+A). Since Z≥B>0, `R_K≤1/[1+A+(K−1)B]→0`, hence T_K→1. QED.

### Corollaries

- If eta<T1, the balance mode is stable for all K.
- If eta≥1, it is unstable for every finite K.
- If T1<eta<1 and eta is not exactly a threshold, there is a finite cutoff after which the mode is stable; increasing K crosses at most once from unstable to stable.
- With `mu=u+2v*A+w*B`, bounded convergence gives `K*R_K→1/mu`, hence `T_K=1−A/(K*mu)+o(1/K)`.

These statements concern the sign of a particular local mode, not an assertion that more negatives universally improve optimization or downstream tasks.

## 4. Theorem 3: sufficient conditions making the threshold a full-sphere criterion

Suppose the policy values and slope obey

```
g≤0,
t2/t0≥1/A (=e),
B*w>A*v.
```

Then for every K≥1 the matched-frozen square is strictly linearly attracting modulo global rotations. The adaptive square is strictly linearly attracting modulo rotations **if and only if** eta<T_K. If eta>T_K it is unstable. No conclusion is asserted at equality.

### Proof

The frozen lambda_b is always positive by Theorem 2. Its lambda_p is also positive: `A*N2/D−A²*N2²/D²` is nonnegative and strictly positive with nonzero probability, and the opposite term is nonnegative. Lambda_+ is positive.

For lambda_−, Palm conditioning gives

```
C=K*w*E[1/(1+B+S_{K−1})],
M=2K*v*E[1/(1+A+S_{K−1})],
```

where `S_{K−1}=sum Z_l`. Since B<A, the first inverse expectation exceeds the second. Consequently `B*w>A*v` implies `lambda_−=B*C−A*M/2>0` for all K. Frozen square therefore has positive curvature in every nonrotation direction.

Let the adaptive response coefficients be `C_b=A*M/v` and

`C_p=A*(E[(N²+N)/D]/(4v)−E[N*S/D]/2)`.

We first prove C_p<C_b/2. For K≥2, another Palm expansion gives

```
C_p/A = M*(1−t1)/(2v)
       +K(K−1)v * [ t0*(F_A−F_1)+t2*(F_A−F_B) ],
F_z=E[1/(1+A+z+S_{K−2})].
```

For each value y=1+A+S_{K−2},

```
F_A−F_1 integrand = (1−A)/[(y+A)(y+1)],
F_B−F_A integrand = (A−B)/[(y+A)(y+B)].
```

Because B=A², the condition t2/t0≥1/A implies

`t0*(F_A−F_1) ≤ t2*(F_B−F_A)`.

Indeed the required pointwise ratio is `(1/A)*(y+B)/(y+1)<1/A`. Thus the bracket is nonpositive and

`C_p ≤ A*M*(1−t1)/(2v) < A*M/(2v)=C_b/2`.

For K=1 the K(K−1) term is absent, so the same inequality holds directly.

Since g≤0, multiplying the inequality reverses its direction. Consequently

`lambda_p^adaptive ≥ (lambda_b^adaptive)/2 + (lambda_p^frozen−lambda_b^frozen/2)`.

The residual is

`lambda_p^frozen−lambda_b^frozen/2 = B*C−(A²/4)E[N(N−1)/D²]`.

Since `A(N−1)<D`, it exceeds `B*C−A*M/4`. The already proved normal stability gives `B*C>A*M/2`; hence this residual is strictly positive. Therefore balance stability implies positivity of the remaining in-plane eigenvalues. Normal eigenvalues have no sampler-response term, and rotations remain neutral. All modes are stable when eta<T_K; when eta>T_K the balance mode itself is unstable. QED.

The assumptions are sufficient and checkable; no claim of necessity for general policy values is made. They hold for the matched-policy examples below.

## 5. Theorem 4: identical frozen objectives, opposite adaptive stability

Consider the smooth positive policy family

`omega_alpha(s)=exp[−2s+alpha*s*(s²−1)]`, `alpha∈[−2,1]`.

Its logarithmic derivative is `−2+alpha*(3s²−1)`, which is nonpositive for every s∈[−1,1] in this alpha interval. It is strictly decreasing for interior alpha. All members agree exactly at s=−1,0,1, so they induce the same square q*, the same frozen objective everywhere in embedding space, and the same frozen full spectrum for every K. Their central derivative is instead `omega_alpha'(0)=−2−alpha`.

With epsilon=.1, all satisfy the value conditions in Theorem 3 and have eta proportional to `2+alpha`. In particular:

| alpha | eta | Full adaptive square stability |
|---:|---:|---|
| −1.5 | .39539244 | Stable for every K≥1 |
| −.9 | .86986336 | Unstable through K=8; stable from K=9 onward |
| 0 | 1.58156974 | Unstable for every finite K |

Thus identical instantaneous negative laws and frozen-risk geometry do not determine adaptive retention stability. More negatives can stabilize a borderline filtering rule without changing the policy's square distribution at all.

The universal statements follow from Theorems 2–3. The explicit integer cutoff for alpha=−.9 uses the finite moment values `T8=.86868894615...`, `T9=.87797331666...`, bracketing eta=.86986335891... and monotonicity. These decimals were first evaluated by finite sums and finite-difference checks. A subsequent independent directed-interval audit certified the signs of T8−eta and T9−eta; its code and certificate are in `../review/` and `../review/results/cutoff_interval_certificate.json`. One can also avoid the explicit numerical instance and state the exact result for any eta strictly between exact T8 and T9.

## 6. Executed checks and their scope

Command from repository root:

`OPENBLAS_NUM_THREADS=1 python negative-feedback/round2/theory/code/verify_general.py`

The fixed protocol evaluated K1–128, four alpha policies (512 policy settings), and 32 independent full-field tangent checks at K1,2,4,8,16 with two finite-difference steps and separate orthogonal orientation checks. Results:

- Maximum full frozen eigenvalue discrepancy: 5.85e−11.
- Maximum full adaptive eigenvalue discrepancy: 8.85e−11.
- Maximum stationary residual: 1.81e−16.
- Same-policy q* discrepancy: 1.11e−16.
- Three-category moments versus separate four-category enumeration: 9.99e−16.
- Maximum probability-sum error across K1–128: 9.65e−14.
- Threshold increased at every K, from .73105858 to .98752186.

The code first completed its numerical assertions but failed to serialize a NumPy boolean into JSON. That output-only issue was fixed by conversion to builtin bool and the run was repeated; neither design nor numeric criteria changed. CSVs from the final completed execution are in results/.

These checks validate formulas; the analytic arguments establish the universal statements. No neural-image result, nonlinear information-erasure theorem, or global basin characterization is implied. Full support and dimension sufficiency do not remove the unit-norm geometric constraint.

## 7. Contribution boundary

The additional Jacobian term from a changing sampler is the familiar product rule and belongs to existing performative learning/reweighting theory. This file contributes a candidate sharper object: a closed full-sphere arbitrary-K spectrum, an exact monotone K-dependent feedback-elasticity threshold, and a matched-value policy construction separating static sampling geometry from adaptive stability. Whether these specific results are sufficiently original and important for a paper must be assessed against source literature and learned-encoder tests; this file does not replace that assessment.

## 8. Extension: general denominator offset and the DCL control

### Theorem 5 (offset, count, and positive-negative coupling)

Replace the loss by

`ell_i^(beta)=log(beta+sum_(r=1)^K exp(f_i·f_(Y_r)−1))`, beta≥0.

Beta=1 is the previous InfoNCE loss; beta=0 is the decoupled loss obtained by deleting the identity-positive term from its denominator, while retaining the same negative policy. The negative tuple can include any of the four states, including the anchor state; this convention stays fixed in both controls.

All spectrum formulas of Theorem 1 remain valid with

`D_beta=beta+U+A*N+B*W`.

The balance threshold becomes

```
T_(K,beta)=1−A*E[N/D_beta²]/E[N/D_beta],
Y_(K,beta)=beta+A+sum_(l=1)^(K−1) Z_l.
```

It satisfies:

1. For each beta≥0, T_(K,beta) strictly increases with K and tends to one.
2. `T_(1,beta)=beta/(beta+A)`; in particular DCL starts at zero rather than .731... .
3. For each K, the threshold strictly increases with beta. Consequently `T_(K,0)<T_(K,1)` at every finite K.
4. For every eta∈(0,1), the DCL balance mode eventually becomes stable as K grows. For sufficiently large K, the same Theorem 3 value conditions turn this into full-sphere stability. Thus count rescue is not removed by eliminating the positive-negative denominator coupling.

Under the same sufficient conditions `g≤0`, `t2/t0≥1/A`, and `B*w>A*v`, the adaptive full-sphere square has strictly positive nonrotation eigenvalues if and only if `eta<T_(K,beta)`. If eta is larger, it is unstable; equality is not classified. The matched-frozen square is strictly stable except at the degenerate case `(K,beta)=(1,0)`, where its balance eigenvalue is zero. This exception must not be presented as a stable-frozen/unstable-adaptive comparison.

### Proof

The first derivatives of the log loss and all great-circle second derivatives used in Theorem 1 are unchanged except for D→D_beta. The same conditional moment identities and permutation symmetries apply. In particular no sampler derivative is inserted into one learning update.

Palm conditioning gives `R_(K,beta)=E[Y_(K,beta)^−2]/E[Y_(K,beta)^−1]`. The strict K monotonicity and limit follow from the positive-random-shift argument of Theorem 2. Increasing beta is instead a deterministic positive shift of Y, for which the same r_Y derivative is strictly negative. At K=1, Y=beta+A is constant. These prove items 1–3; item 4 follows from convergence to one.

The full-sphere proof also carries over: the normal-mode Palm denominators are `beta+B+S` and `beta+A+S`, preserving their ordering. In the C_p coefficient proof, simply replace `y=1+A+S` by `y=beta+A+S`; the pointwise ratio `(1/A)*(y+B)/(y+1)<1/A` remains true for every y>0. The residual bound uses only `A*(N−1)<D_beta`, which still holds. The frozen balance eigenvalue is nonnegative since D_beta≥A when N≥1; equality in its Palm form requires K=1 and beta=0. For K≥2 a further strictly positive Z makes it positive. QED.

### What this rules out, and what it does not

For a fixed tuple, let `D_−=sum exp(s−1)`. The InfoNCE gradient is the DCL gradient times `D_−/(1+D_−)`. This is the familiar positive-negative coupling factor. The strict inequality `T_DCL<T_InfoNCE` shows that this coupling contributes to the exact stability boundary; it cannot be ignored. However the DCL threshold itself increases from zero to one, so the count transition is not solely that factor. Multiple-negative softmax curvature and a current-representation-dependent sampling law remain after decoupling. This is an exact control inside the specified four-state model, not a claim that DCL is inferior on practical benchmarks or that existing DCL theory is unaware of count effects.

## 9. Natural exponential policies have an open count-rescue region

The matched-value family in Section 5 is useful for separating frozen geometry from slope response. It is not necessary for count stabilization.

### Theorem 6 (an open regime, not a single engineered filter)

Let `omega(s)=exp(−t*s)`, t>1, and define

```
Z_t=exp(−t)+2+exp(t),
rho=(1−epsilon)/[epsilon*Z_t/4+1−epsilon],
eta=t*rho,
L(t)=(e−1)/(exp(t)−1).
```

For every t>1 the interval

`max{L(t), T_(1,1)/t} < rho < 1/t`

is nonempty. Every rho in this interval corresponds to a unique epsilon∈(0,1), yields a strictly stable matched-frozen square for every K, and gives an adaptive square which is unstable at K=1 but strictly stable for all sufficiently large K (apart from unclassified equality at a threshold). Consequently a natural monotone exponential family with a uniform probability floor has an **open parameter region** with full-sphere count rescue. Its DCL counterpart also has a finite rescue cutoff and cannot cross earlier than InfoNCE.

### Proof

For the natural policy, `g=−(1−epsilon)*t/Z_t` and `v=epsilon/4+(1−epsilon)/Z_t`, so eta=t*rho. Also

```
t2/t0=exp(2t)>e,
w/v=1+rho*(exp(t)−1).
```

Thus `B*w>A*v` is exactly `rho>L(t)`. The derivative g is negative. The upper bound rho<1/t makes eta<1, while rho>T_(1,1)/t makes eta>T_(1,1). Theorems 2–3 now give a unique finite onset of full stability, modulo possible isolated equality counts.

It remains to show the interval is nonempty. Obviously `T_(1,1)/t<1/t`. For t>1,

`exp(t)−1 > t*(e−1)`.

Both sides are equal at t=1; the derivative of their difference is `exp(t)−(e−1)>0` for t≥1. Therefore L(t)<1/t. Finally rho decreases continuously from one to zero as epsilon increases from zero to one, and

`epsilon = [4*(1/rho−1)/Z_t] / [1+4*(1/rho−1)/Z_t]`.

It realizes every rho in (0,1). All inequalities are strict and continuous, proving the regime is open. The DCL threshold is strictly lower at every finite K but converges to the same one, proving its stated cutoff relation. QED.

### Analytically selected explicit instance, then executed

Take `t=log(4)`, epsilon=.3. Before numerical execution these simple values imply

```
(u,v,w)=(103,187,523)/1000,
eta=(112/187)*log(4)=.830293948906...,
t2/t0=16>e,
w/v=523/187=2.79679...>e.
```

Thus the sufficient conditions are strict. The exact finite-sum evaluations and independent full-field finite-difference checks give:

| Policy | Loss | Last unstable count | Its threshold | First stable count | Its threshold |
|---|---|---:|---:|---:|---:|
| Natural `4^(−s)`, epsilon=.3 | InfoNCE | 4 | .8299237407665 | 5 | .8494695708639 |
| Natural `4^(−s)`, epsilon=.3 | DCL | 7 | .8091509022209 | 8 | .8345182640899 |
| Matched-value alpha=−.9, epsilon=.1 | InfoNCE | 8 | .8686889461511 | 9 | .8779733166586 |
| Matched-value alpha=−.9, epsilon=.1 | DCL | 13 | .8697804401970 | 14 | .8791412051673 |

The monotonicity theorem upgrades the finite brackets to all-K cutoffs; it is not an extrapolation from K≤128. A separate reviewer subsequently certified the natural InfoNCE K4/5, natural DCL K7/8, and matched DCL K13/14 brackets with 70-digit directed intervals and rigorous exponential/logarithm enclosures. The certificate is `../review/results/control_interval_certificate.json`, including a certified positive lower bound for the natural normal-mode condition. Its own implementation and correction history are recorded in `../review/review.md`. The natural instance was selected analytically after the first protocol to demonstrate the proved open regime. It is not an independently held-out effect estimate and was not selected by sweeping many numeric policies. Its K4 InfoNCE instability is weak (`lambda_b=−9.1488991e−5`), which matters for finite-duration trajectory tests.

The post-proof control protocol was recorded before execution in protocol.md. Command:

`OPENBLAS_NUM_THREADS=1 python negative-feedback/round2/theory/code/verify_controls.py`

The run evaluated K1–128 for two policies and two losses (512 settings), plus 20 full-field d=4 tangent checks at K1,2,4,8,16. Maximum eigenvalue discrepancies were 7.06e−11 frozen and 9.04e−11 adaptive. Complete outputs are denominator_controls.csv, denominator_fd.csv, and denominator_summary.json in results/.

### Large-K effective-temperature reduction and scope

For epsilon=0 and the natural exponential policy, the K→infinity tuple-average gradient weights reduce to

`q_F(j|i)*exp(s_ij) / sum_l q_F(l|i)*exp(s_il)
 = exp((1−t)*s_ij)/sum_l exp((1−t)*s_il)`.

For t≠1 this is the gradient of the corresponding row log-partition divided by `(1−t)`; t=1 gives uniform score weights. This elementary reduction should be acknowledged rather than claimed as a discovery. It neither supplies the finite-K threshold nor the nonzero-floor open regime proved above. At epsilon=0, eta=t>1 for t>1, so the balance mode in the natural easy-filter regime is unstable at every finite K. The uniform floor is mathematically active in the count-rescue regime, not just a sampling implementation detail. The complete claims retain this explicit modeling condition.
