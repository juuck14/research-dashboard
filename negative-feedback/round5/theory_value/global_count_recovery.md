# Global negative-count recovery of every stable equilibrium

Original derivation: 2026-10-23. Reconstructed from the preserved conversation and independently re-audited on 2026-10-25 after interruption removed unpublished workspace files. This is a restored mathematical proof, not a claim that missing original raw experiment files were recovered. Newly rerun computations have separate provenance.

## 1. Population, update, and scope

There are C≥4 equiprobable distinguishable classes, with one unit feature f_i per class. Write F∈R^{C×d}, d≥C−1, and s_ij=f_i^T f_j. For each anchor i draw K≥1 negative indices iid, with replacement, from j≠i. Every candidate is a genuinely different class.

For a temperature τ>0, a mixing floor 0<ε<1, and a positive C² function ω on the score interval [−1,1], let

\[
q_F(j\mid i)=\frac{\epsilon}{C-1}
 +(1-\epsilon)\frac{\omega(s_{ij})}{\sum_{\ell\ne i}\omega(s_{i\ell})},
\qquad q_F(i\mid i)=0.
\]

The identity-positive tuple loss is

\[
\ell_i(F;Y_1,\ldots,Y_K)=
\log\left(1+\sum_{k=1}^K e^{(s_{iY_k}-1)/\tau}\right).
\]

Both embedding appearances receive loss gradients. The sampling distribution is detached per update. Let G(F) be the expected product-sphere gradient and let the population flow be \(\dot F=-G(F)\).

Here a linearly stable stationary point has G(F)=0 and no eigenvalue of DG(F), restricted to the product-sphere tangent, with negative real part. This necessary spectral condition is enough for the theorem; it is not asserted sufficient for nonlinear attraction. Positive restoring eigenvalues mean attraction for the negative flow.

The result is about every stable stationary geometry, not arbitrary-trajectory convergence, absence of cycles, practical stochastic convergence, neural parameter dynamics, or general multiview recovery. Current geometry need not be symmetric or close to a simplex. Balanced classes, iid negatives, sufficient dimension, row normalization, and the scalar score policy remain assumptions.

## 2. The quantitative theorem

Let r=−1/(C−1), and define

\[
\gamma=\max\left\{0,\sup_{s\in[-1,1]}
[-\tau(\log\omega)'(s)]\right\}<1,
\quad b=e^{-2/\tau},
\quad \alpha=\frac{1-\gamma}{\tau},
\quad c_\alpha=\frac{1-e^{-2\alpha}}2>0.
\]

Thus genuinely decreasing or nonmonotone weights are permitted. Define the mean squared off-diagonal Gram error

\[
\mathcal E(F)=\frac1{C(C-1)}
 \sum_{i\ne j}(s_{ij}-r)^2,
\qquad M=\frac{(1+r)(2-b)}{b c_\alpha}.
\]

**Theorem.** Every linearly stable stationary point satisfies

\[
\boxed{\mathcal E(F)\le \frac M K.} \tag{1}
\]

Let

\[
E_K=\sqrt{\frac{C(C-1)M}{2K}}.
\]

Its decoder-independent robust class radius obeys

\[
\boxed{
r_*(F):=\frac12\min_{i\ne j}\|f_i-f_j\|
\ge \sqrt{\frac{\max\{0,1-r-E_K\}}2}.
} \tag{2}
\]

In particular, no two classes coincide at any such stationary point whenever

\[
\boxed{K>\frac{M(C-1)^3}{2C}.} \tag{3}
\]

The constants are explicit sufficient bounds, not estimates of the smallest safe count. They become conservative at low temperature or near γ=1. The proof is uniform over the declared geometry and policy family; it does not infer (1) from a finite sweep over equilibria.

## 3. Stable stationary points have a PSD stress certificate

Freeze Q=q_F at the stationary representation under consideration. Its loss R_Q(X), as a function of a symmetric Gram matrix X with unit diagonal, is convex: it is an expectation of log-sum-exp functions of off-diagonal Gram entries. Put X=FF^T, let A be the symmetric Gram derivative, and set A_ii=0. Explicitly, the coefficient definition in Section 4 gives

\[
A_{ij}=\frac{\beta_{ij}+\beta_{ji}}{2C\tau}>0
\quad (i\ne j).
\]

Set

\[
\lambda_i=f_i^T(AF)_i,\qquad
H=A-\operatorname{diag}(\lambda).
\]

The expected detached sphere field at this representation is exactly 2HF, so HF=0 at stationarity. All off-diagonal H_ij are strictly positive.

### Rank-deficient embeddings

If rank F<d, choose a unit u∈R^d with Fu=0. For any x∈R^C, Z=xu^T is a feasible rowwise tangent. Its first Gram derivative is

\[
FZ^T+ZF^T=(Fu)x^T+x(Fu)^T=0.
\]

Hence the sampler derivative is zero, and so is the first derivative of A. At a stationary point the first derivative of each λ_i is also zero. The closed-loop Jacobian on the invariant normal subspace is therefore

\[
DG(F)[xu^T]=2Hxu^T. \tag{4}
\]

A negative eigenvalue of the symmetric H gives an actual negative restoring eigenvalue of DG. Linear stability consequently forces H⪰0. This step does not assume that the entire closed-loop field is conservative.

### The boundary dimension d=C−1

If rank F=d=C−1, then HF=0 implies rank H≤1. H is not zero because its off-diagonal entries are positive. A negative rank-one symmetric H would have the form −vv^T times a positive constant. Positivity of every off-diagonal entry would require v_i v_j<0 for every pair i≠j. This is impossible for any triple of nonzero entries. Thus H must be PSD.

If d≥C and F had full row rank C, HF=0 would force H=0, again impossible. All cases with d≥C−1 have now been covered, and H⪰0 holds at every linearly stable stationary point.

### Testing against the simplex

Let X_* be the regular-simplex Gram, diagonal one and off-diagonal r. It is PSD and attainable in d≥C−1. Since HFF^T=0 and X_* and FF^T have the same diagonal,

\[
\operatorname{tr}[A(X_*-FF^T)]
=\operatorname{tr}(H X_*)\ge0. \tag{5}
\]

Equivalently,

\[
\mathbb E_i\sum_{j\ne i}\beta_{ij}(s_{ij}-r)\le0. \tag{6}
\]

The stress/KKT and unused-normal mechanism is inherited from convex-Gram and Burer–Monteiro landscape arguments. The closed-loop verification (4) is essential; one cannot replace the adaptive field by a frozen objective without it. Positivity of off-diagonal stress is also essential for the d=C−1 completion. General positive-channel multiview systems do not automatically satisfy this prototype proof.

## 4. Exact finite-count tagging and the one-sided bound

Fix one anchor. Write

\[
z_j=e^{(s_j-1)/\tau}\in[b,1],
\quad q_j=q_F(j\mid i),
\quad \mu=\sum_j q_j z_j\in[b,1].
\]

Let S_{K−1} sum K−1 iid negative weights with this row law. Tagging one position of the ordered negative tuple gives the exact detached score coefficient, with the common 1/τ omitted,

\[
\beta_j=
Kq_j z_j\,\mathbb E\left[\frac1{1+z_j+S_{K-1}}\right].
\tag{7}
\]

Define \(\pi_j=q_jz_j/\mu\). These π values sum to one; no count-limit approximation is used in their definition.

By reciprocal Jensen,

\[
\frac{\beta_j}{\pi_j}
=K\mu\,\mathbb E\frac1{1+z_j+S_{K-1}}
\ge
\frac{K\mu}{1+z_j+(K-1)\mu}
\ge
\rho_K:=\frac{Kb}{2+(K-1)b}. \tag{8}
\]

For the last step first use z_j≤1 and then the fact that
\(K\mu/[2+(K-1)\mu]\) increases with μ≥b.

Moreover,

\[
\sum_j\beta_j
=\mathbb E\frac{S_K}{1+S_K}<1.
\]

Thus δ_j=β_j−ρ_Kπ_j is nonnegative, and its mass is at most 1−ρ_K. Since every candidate score satisfies s_j−r≥−(1+r),

\[
\sum_j\beta_j(s_j-r)
\ge
\rho_K\sum_j\pi_j(s_j-r)
-(1-\rho_K)(1+r). \tag{9}
\]

Combine (9), averaged over anchors, with the stable-point certificate (6). It follows that

\[
\mathbb E_i\sum_{j\ne i}\pi_{ij}(s_{ij}-r)
\le
\frac{1-\rho_K}{\rho_K}(1+r)
=
\frac{(1+r)(2-b)}{Kb}. \tag{10}
\]

This is a finite-K uniform inequality. It requires neither an exchange of limits nor an unquantified approximation of the expected denominator.

## 5. Global easy-slope control produces quantitative effective hardening

For a fixed row normalizer \(Z_i=\sum_{\ell\ne i}\omega(s_{i\ell})\), define the auxiliary positive weight

\[
v_i(s)=e^{(s-1)/\tau}
\left[\frac{\epsilon}{C-1}
+\frac{(1-\epsilon)\omega(s)}{Z_i}\right].
\]

Its normalized values at the actual candidate scores are π. This definition holds Z_i fixed only to compare candidate weights within that row; it does not incorrectly differentiate the actual policy normalizer as a constant in the closed-loop field.

The global slope condition gives

\[
(\log v_i)'(s)
=\frac1\tau+\chi_i(s)(\log\omega)'(s)
\ge\frac{1-\gamma}{\tau}=\alpha,
\]

where 0≤χ_i(s)≤1 is the weight-dependent component's share. Therefore \(v_i(s)e^{-\alpha s}\) is nondecreasing.

Let m_i and V_i be the uniform candidate mean and variance of the scores. Monotone likelihood-ratio ordering, or the nonnegative covariance between score and a nondecreasing weight, implies that the π-weighted mean is at least the mean under the exponential tilt of the uniform row by e^{αs}.

For completeness, under a tilt e^{ts}, t≥0, each tilted probability is at least e^{−2t} times its uniform probability, because s∈[−1,1]. The variational characterization of variance gives

\[
\operatorname{Var}_t(s)
=\min_a\mathbb E_t(s-a)^2
\ge e^{-2t}\min_a\mathbb E_0(s-a)^2
=e^{-2t}V_i.
\]

The derivative of the tilted mean is its variance. Integrating from zero to α yields

\[
\sum_j\pi_{ij}s_{ij}
\ge m_i+\int_0^\alpha e^{-2t}V_i\,dt
=m_i+c_\alpha V_i. \tag{11}
\]

This is the step that needs a global score-range condition. A derivative at the simplex, all derivatives at that point, or even a uniform local field on an open neighborhood cannot imply it for arbitrary current geometry.

## 6. From row moments to the entire Gram

Put S=Σ_i f_i and define

\[
A_0=\mathbb E_i(m_i-r)
=\frac{\|S\|^2}{C(C-1)}\ge0,
\qquad V=\mathbb E_i V_i.
\]

Equations (10) and (11) imply

\[
A_0+c_\alpha V
\le \frac{(1+r)(2-b)}{Kb}. \tag{12}
\]

The exact row-mean identity is

\[
m_i-r=\frac{f_i^TS}{C-1}.
\]

Hence

\[
\mathbb E_i(m_i-r)^2
\le\frac{\|S\|^2}{(C-1)^2}
=\frac C{C-1}A_0.
\]

Using c_α≤1/2≤(C−1)/C,

\[
\begin{aligned}
\mathcal E(F)
&=V+\mathbb E_i(m_i-r)^2\\
&\le V+\frac C{C-1}A_0
\le\frac{A_0+c_\alpha V}{c_\alpha}
\le\frac{(1+r)(2-b)}{Kb c_\alpha}.
\end{aligned}
\]

This proves (1).

Each off-diagonal score appears twice in the symmetric Gram sum, so

\[
\max_{i<j}|s_{ij}-r|
\le\sqrt{\frac{C(C-1)}2\mathcal E(F)}
\le E_K.
\]

Since \(r_*^2=(1-\max_{i<j}s_{ij})/2\), (2) follows. A collision has s_ij=1 and contributes at least

\[
\frac{2(1-r)^2}{C(C-1)}
=\frac{2C}{(C-1)^3}
\]

to \(\mathcal E\); (3) follows. QED.

## 7. Positive-floor extension

Drop the restriction γ<1 while retaining its definition as the nonnegative supremal easy slope. Since ω is positive and continuous on a compact interval,

\[
R_\omega=\frac{\max\omega}{\min\omega}<\infty.
\]

The weight-dependent share satisfies, for every row and score,

\[
\chi_i(s)\le
\rho_{\max}:=
\frac{(1-\epsilon)R_\omega}
{\epsilon+(1-\epsilon)R_\omega}<1.
\]

Consequently the proof applies with

\[
\gamma_{\mathrm{eff}}=\gamma\rho_{\max},
\qquad
\alpha_{\mathrm{eff}}=(1-\gamma_{\mathrm{eff}})/\tau,
\]

whenever γ_eff<1. A raw γ=1 with a positive floor is therefore eventually recoverable under this sufficient bound; its count constant can be large. Some raw γ>1 policies are included too. The theorem does not establish a necessary-and-sufficient global budget threshold for every individual policy.

## 8. Interpretation, contrasts, and inherited ingredients

Theorem (1) concerns every stable stationary geometry and therefore differs from a local simplex criterion. It also differs from a fixed-objective nondecreasing-hardening theorem: ω here may favor easy negatives, and small-count stable mergers can actually exist under the same allowed global budget. The finite-count tagging and quantitative effective-tilt certificate yield the recovery statement.

The existing all-count class-merging construction in [global_collapse.md](../global_mechanism/global_collapse.md) supplies a contrasting stronger-response regime with positive floor and enough dimension. That construction does not imply that every policy above the sufficient budget fails. Local plateau/bistability constructions, when separately documented with available evidence, show why a local field criterion cannot replace the premise used here.

The arbitrary-decoder robust radius and simplex packing bound are standard geometry, not new theorems claimed by this work. The stress/unused-normal mechanism is likewise inherited. Relevant precedents include [Behnia and Thrampoulidis, 2024, Section III-C](https://arxiv.org/html/2402.18884v1) for a fixed supervised-contrastive Gram landscape, and [Boumal, Voroninski and Bandeira, 2016, rank-deficient argument](https://proceedings.neurips.cc/paper/6517-the-non-convex-burer-monteiro-approach-works-on-smooth-semidefinite-programs.pdf). Their fixed-objective conclusions are not being claimed as new here.

The result does not automatically extend to imbalanced classes, without-replacement sampling, arbitrary feature-dependent policies, a shared neural parameterization, or full multiview systems. Failure of such an extension would not refute the stated prototype equilibrium theorem. Conversely, any claim of typical practical training success would require additional evidence beyond this proof.

