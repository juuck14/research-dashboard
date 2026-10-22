# An exchange-balanced, multilevel negative-count law

Status2026-10-22: direct derivation and hostile numerical checks completed; independent review found no mathematical defect in the stated scope. This is not a publication-quality verdict. The Stieltjes/log-convexity lemmas are elementary existing mathematical tools, not contributions in themselves. Bounded continuous populations and a realizable product-of-spheres extension are proved separately in `continuous_population.md`.

## 1. Model and what is being generalized

Let a finite candidate population have fixed base probabilities p_j>0,sum p_j=1. A scalar representation direction changes candidate scores affinely near zero:

\[
s_j(\delta)=s_j+\delta h_j,\qquad s_j\in[-1,1].
\]

Identity-positive score is1. Assume exchange balance

\[
\mathbb E_p[h\mid s]=0,\qquad \mathbb E_p[h^2]>0.
\]

Conditional balance is substantive: it removes cross-negative first-derivative products and makes delta0 stationary for every K. It follows from an involutive semantic-factor exchange that preserves the reference score and reverses h. The candidate model is not an arbitrary unbalanced equilibrium. Multiple anchors may be averaged if their conditional score/derivative law is identical; averaging unrelated anchor laws is not covered.

The current-policy negatives have probabilities

\[
q_\delta(j)=\epsilon p_j+(1-\epsilon)
\frac{p_j e^{-t s_j(\delta)}}{Z_\delta},\qquad
Z_\delta=\sum_jp_j e^{-t s_j(\delta)},
\]

where0<epsilon<1,t>1. Negatives are iid with replacement from q_delta. For beta≥0, use

\[
\ell_{K,\beta}(\delta;Y)=\log\left(\beta+\sum_{r=1}^K e^{s_{Y_r}(\delta)-1}\right).
\]

The detached scalar field is G_K(delta)=E_{Y~q_delta^K}[partial_delta ell(delta;Y)], where q is held fixed inside that partial derivative. Its restoring curvature is H_K=G_K'(0). H_K>0 is scalar negative-flow attraction; H_K<0 is repulsion. No full-space stability, information erasure, or shared-encoder metric statement is made.

The previous square theorem had h≠0 at only one score level. Here any finite number of score levels may carry nonzero conditional variance. The hypercube construction in Section6 makes this a realizable normalized representation direction rather than an arbitrary score perturbation.

## 2. Exact curvature with arbitrary score levels

Put W_j=exp(s_j-1)>0,Z=E_p exp(-t s),and

\[
\rho(W_j)=\frac{(1-\epsilon)e^{-t s_j}/Z}
{\epsilon+(1-\epsilon)e^{-t s_j}/Z}.
\]

The function rho extends to all W>0 as gamma W^(-t)/(epsilon+gamma W^(-t)),gamma=(1-epsilon)e^(-t)/Z. Conditional balance gives Z'_0=0, and therefore q'_0(j)/q_0(j)=−t rho(W_j) h_j.

Let W_1,... be iid according to q_0 and S_n=sum_(l=1)^n W_l. For x>0 define

\[
f_n(x)=\mathbb E[(x+S_n)^{-1}],\quad
R_n(x)=\frac{\mathbb E[(x+S_n)^{-2}]}{f_n(x)}.
\]

Selecting one exchangeable tagged negative gives the exact identity

\[
\boxed{\frac{H_K}{K}=\sum_j q_j h_j^2 W_j
f_{K-1}(\beta+W_j)\,a_{K-1}(W_j),}
\]

where

\[
a_n(W)=1-t\rho(W)-W R_n(\beta+W).
\]

**Proof.** For a tuple, write D=beta+sum W_r. The loss first derivative is A/D with A=sum W_r h_r. Its second derivative is sum W_r h_r²/D−A²/D². The derivative of the tuple log probability is−t sum rho(W_r)h_r. Conditional on all tuple scores, different h_r are independent with conditional means zero, even if candidate values repeat, because the draws themselves are independent. Hence cross terms in A² and A times the log-probability derivative vanish in conditional expectation. The remaining terms are sum W_r h_r²[(1−t rho(W_r))/D−W_r/D²]. Exchangeability yields the displayed tagged-draw form. QED.

Here the affine-score condition is exact. If scores have nonzero second derivatives, the additional E[sum W_r s''_r/D] term must be retained, and the following sign theorem does not automatically hold.

## 3. Three elementary lemmas

### Lemma1: adding an independent negative improves each local margin

For every fixed W>0,n≥0,

\[
R_{n+1}(\beta+W)<R_n(\beta+W),\qquad
a_{n+1}(W)>a_n(W).
\]

For positive Y,write m_l(z)=E(Y+z)^(-l). The derivative of m2/m1 is(-2m3m1+m2²)/m1²<0,by Cauchy–Schwarz. Adding an independent strictly positive W' is a positive-weighted average of the smaller deterministic-shift ratios. This gives the strict inequality. This is the same elementary inverse-moment argument used in the one-level square result, now applied separately at every tagged score.

### Lemma2: the local margin has an upward-only crossing in score

For fixed n,beta, the function a_n(W) has at most one zero on W>0, and it is negative below that zero and positive above it. The exception(beta,n)=(0,0) has a_n(W)=−t rho(W)<0 everywhere.

**Proof.** Set T(W)=1−W R_n(beta+W). Since beta+W+S_n≥W,0≤T<1,with T>0 outside the exception. Differentiate r(W)=W R_n(beta+W). If m_l=E(beta+W+S_n)^(-l),then

\[
Wr'(W)=r+W^2[-2m_3/m_1+(m_2/m_1)^2]
\le r-r^2=T(1-T).
\]

Also W rho'(W)=−t rho(1−rho). At a zero of a_n,T=t rho,so

\[
W a_n'(W)\ge t^2\rho(1-\rho)-T(1-T)
=(t-1)T>0.
\]

Every zero is therefore a strict upward crossing; there cannot be two zeros without an intervening non-upward crossing. As W↓0,the margin tends to1−t<0 (or stays negative in the exceptional case). For large W, T(W)~(beta+E S_n)/W whereas rho(W)=O(W^(-t)); since t>1,the margin eventually becomes positive outside the exception. This proves the sign pattern. QED.

### Lemma3: added negatives tilt tagged weights toward larger scores

The ratio f_(n+1)(x)/f_n(x) is strictly increasing in x>0. Indeed f_n is strictly log-convex:

\[
(\log f_n)''=(2m_3m_1-m_2^2)/m_1^2>0.
\]

For each z>0,the ratio f_n(x+z)/f_n(x) is therefore increasing in x. Taking expectation over an independent new W' preserves the inequality because f_(n+1)(x)=E_W'[f_n(x+W')]. Thus the tagged weights q_j h_j²W_j f_n(beta+W_j) undergo a monotone likelihood-ratio tilt toward larger W when n increases. This is a property of positive iid denominator sums, not an assumption about the representation.

## 4. Theorem: a single possible stability transition as K increases

**Prior mathematical principle.** Preservation of a single-crossing sign under a monotone-likelihood-ratio weight change is established comparative statics, not a new theorem here. Athey, *Characterizing Properties of Stochastic Objective Functions* (MIT working paper, revised1999), Section3.3.1, Corollary5.3, [primary PDF](https://web.mit.edu/athey/www/CPSO99.pdf), gives the general aggregation principle. The application-specific work below verifies its score crossing and Stieltjes weight conditions for this contrastive field and combines them with the pointwise strict change in the margin.

If H_K≥0 for some finite K,then H_(K+1)>0. Consequently the curvature can never change from stable to unstable as the number of iid negatives increases. It has at most one transition from negative to positive,possibly with one zero-curvature count at the boundary.

**Proof.** Write nu_j=q_j h_j² W_j and mu_n(j)=nu_j f_n(beta+W_j). By Lemma2,a_n has a single score sign crossing c,if both signs occur. Lemma3 gives an increasing positive ratio r_n(W)=f_(n+1)(beta+W)/f_n(beta+W). Hence pointwise

\[
r_n(W)a_n(W)\ge r_n(c)a_n(W).
\]

For W<c both factors in the comparison reverse sign; for W>c both preserve it. Thus H_K/K=sum mu_n a_n≥0 implies sum mu_(n+1) a_n≥0. Lemma1 strictly increases the margin on every h²-positive support point,giving sum mu_(n+1) a_(n+1)>0. The cases in which a_n has one sign on the actual support are immediate. This proves H_(K+1)>0. QED.

The proof does not assert monotonicity of the numeric magnitude H_K. Its sign is the ordered object. The nonlinear geometry may have other unstable directions.

## 5. Exact criterion for whether more iid negatives can ever stabilize

Let mu=E_q W>0. Define

\[
Q=\epsilon\mathbb E_p[h^2e^s]
-(t-1)\frac{1-\epsilon}{Z}\mathbb E_p[h^2e^{(1-t)s}].
\]

Then

\[
\lim_{K\to\infty}H_K=e^{-1}Q/\mu.
\]

If Q>0,there is a finite K after which H_K>0. If Q≤0,then H_K<0 for **every** finite K. Therefore Q>0 is necessary and sufficient for eventual positive curvature. Increasing the number of iid negatives cannot rescue a mode below this critical floor.

**Proof of the limit.** Finite score support bounds W above and strictly away from zero. Thus K f_(K−1)(beta+W)→1/mu uniformly on the finite tagged support,and K E(beta+W+S_(K−1))^(-2)→0. Substituting the exact curvature identity gives sum_j q_j h_j²W_j(1−t rho_j)/mu=e^(-1)Q/mu.

**Proof for Q≤0,including the zero boundary.** The limiting score margin a_infinity(W)=1−t rho(W) is strictly increasing and single-crossing. The finite margin satisfies a_n(W)=a_infinity(W)−W R_n(beta+W)<a_infinity(W). The factor f_n(beta+W) decreases strictly in W. Thus tilting nu_j by f_n puts relatively more weight below the sign crossing. If sum nu_j a_infinity(W_j)=e^(-1)Q≤0,then sum nu_j f_n a_infinity≤0 by the same crossing comparison with a decreasing ratio. Subtracting the strictly positive R term makes H_K strictly negative. QED.

Equivalently define

\[
\epsilon_c=\frac{(t-1)\mathbb E_p[h^2e^{(1-t)s}]}
{(t-1)\mathbb E_p[h^2e^{(1-t)s}]+Z\mathbb E_p[h^2e^s]}.
\]

Then some sufficiently large finite K has positive curvature iff epsilon>epsilon_c. This criterion depends on the distribution of **both** scores and mode-specific score derivatives,not merely score histogram,negative count,or model output dimension. Beta changes the onset count but not this limiting floor boundary.

## 6. Realizable many-factor unit-sphere application

Let x be uniform on{−1,+1}^m,m≥2,and use

\[
f_\delta(x)=(\sqrt{1/m+\delta}\,x_1,
\sqrt{1/m-\delta}\,x_2,x_3/\sqrt m,\ldots,x_m/\sqrt m,0,\ldots).
\]

For |delta|<1/m every embedding is unit-normalized. At delta0,candidate relative signs z_k=x_k y_k are uniform,and

\[
s=\frac1m\sum_{k=1}^m z_k,\quad h=z_1-z_2,\quad s''=0.
\]

Exchanging z1,z2 fixes s and reverses h,so conditional balance holds at every one of the m+1 score levels. The reference is an equilibrium of the complete free-embedding projected field: Hamming-distance and coordinate-permutation symmetry make the expected unprojected gradient parallel to each reference vector. H_K is therefore its genuine directional restoring curvature,not a nonstationary loss derivative. Sufficient ambient dimension can be chosen as d≥2^m−1 if one wants an unconstrained simplex representation; no insufficient-dimension mechanism is required. The theorem still concerns the energy-transfer mode,not every tangent direction.

By direct product moment calculation,

\[
Z=\cosh(t/m)^m,\qquad
\mathbb E[h^2e^{cs}]=2\cosh(c/m)^{m-2}.
\]

Hence

\[
\epsilon_c(m,t)=
\frac{(t-1)\cosh((t-1)/m)^{m-2}}
{(t-1)\cosh((t-1)/m)^{m-2}
+\cosh(t/m)^m\cosh(1/m)^{m-2}}.
\]

As m→infinity,this converges to1−1/t. Thus a fixed subcritical floor cannot be repaired by arbitrarily many iid negatives in sufficiently many-factor balanced geometry. This is a local geometry statement,not a theorem that a factor is globally or information-theoretically erased. No monotonicity in m is asserted without a separate proof.

For any fixed K,the complete scalar curvature also has the limit

\[
\lim_{m\to\infty}H_K(m)=\frac{2KA}{\beta+KA}
\left[1-t(1-\epsilon)-\frac{A}{\beta+KA}\right],\qquad A=e^{-1}.
\]

Indeed the hypercube score converges to zero in probability,E[h²]=2,and h²≤4. The finite-tuple integrand is a bounded continuous function of the candidate scores on their compact domain,so dominated convergence gives W→A,rho→1−epsilon and the displayed expression. This is a fixed-K limit,not an unproved exchange of the K and m limits. It describes a local energy-transfer curvature; the admissible delta interval shrinks as1/m and no uniform dynamical rate in the free-embedding metric is implied.

For t=log4,epsilon=.3,beta1,the limiting sign is positive precisely when K>1/[1-.7log4]−e,so the first strictly positive integer is32. For epsilon=.25,the large-m limiting floor is below critical and no K can rescue sufficiently large finite-m models. The exact finite-m critical-floor expression,not this limiting heuristic,is used to classify each finite m.

## 7. Why this could matter,and what it does not solve

The additional knowledge is not merely that feedback can defeat static curvature. It gives a distribution/mode-specific necessary and sufficient rescue criterion and an ordered count transition across multiple score levels. It identifies when spending more negative samples can never restore a balanced factor mode,as opposed to merely requiring a larger batch. The hypercube application extends from four states to arbitrarily many independent factors while preserving normalized Gram realizability.

The conditional-balance,affine-score,iid and natural-policy assumptions are active. Arbitrary current-encoder policies,unbalanced/heterogeneous anchor laws,correlated negatives and other representation directions are outside the theorem. The result alone does not demonstrate practical importance or top-journal sufficiency. In particular a mode can become stable while an orthogonal mode remains unstable,as the earlier square counterexample already shows. A source/quality comparison must evaluate whether this structural law and any direct learning predictions meet the fixed journal bar.

The K-infinite floor by itself is an effective-temperature/weighted-curvature calculation and cannot carry the novelty claim. The stronger statement is that the limit determines **whether any finite count can ever rescue the direction**, including the exact critical boundary, and that no stable-to-unstable re-entry occurs under the stated iid model. An independent mathematical review has checked the zero-crossing, MLR, and critical-boundary steps. That review is not evidence that the result is sufficiently important for the fixed journal bar.

## 8. Executed checks and interpretation

The preregistered hostile test evaluated18432 settings across16 random multilevel score/derivative laws. It found no forbidden sign transition and no positive curvature below or at the analytical floor. The independently evaluated ordered-tuple detached-gradient finite differences agree to1.40e-10 absolute error. Explicit hypercube moment/tuple checks agree to4.18e-11. See `results/summary.json`, the raw CSV files, and the fixed commands in README.

At t=log4 and fixed epsilon.25, the cube's first-positive counts are12,19,29,349 for m2,3,4,8. For m16,32,128, epsilon is below the exact critical floor, proving negative curvature at **all** finite K. For epsilon.3 the corresponding onsets are5,7,8,13,18,23,29 for m2,3,4,8,16,32,128. Onset decimals are deterministic numerical quadrature, not interval-certified signs; the all-K ordering and subcritical impossibility are analytical. The m8,epsilon.25 case illustrates why observing no positive curvature through K64 is insufficient to declare impossibility.
