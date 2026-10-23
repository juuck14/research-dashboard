# A true class-merging attractor with no false negatives

2026-10-23. Direct derivation in this round. The general graph diagonalization and normally attracting-manifold argument are standard. This file supplies the bad-attractor half of the parent's proposed separation between task-optimal fixed-law geometry and closed-loop contrastive learning. It does not claim that every initialization collapses or that arbitrary negative samplers fail.

## 1. Clean model

There are C=2m equiprobable classes, m>=2. First take one prototype per class with freely trainable unit embeddings f_i in dimension d>=C−1, identity positives, temperature1 and K iid negatives with replacement. Candidate j=i is excluded, so **every sampled negative is from a different class**. The detached policy is

\[
q_F(j\mid i)=\frac{\epsilon}{C-1}
 +(1-\epsilon)\frac{e^{-t f_i^Tf_j}}{\sum_{\ell\ne i}e^{-t f_i^Tf_\ell}},
\quad j\ne i,\qquad q_F(i\mid i)=0.
\]

Every admissible negative has probability at least epsilon/(C−1)>0. Both encoder occurrences receive gradients of the joint InfoNCE loss. At a reference containing m copies of u and m copies of−u, let p be the total opposite-group negative probability:

\[
p=\epsilon\frac m{2m-1}
 +(1-\epsilon)\frac{mR}{m-1+mR},\qquad R=e^{2t}.
\]

No input information or output capacity has been removed: an injective simplex is available in the same dimension. The antipodal representation instead identifies m distinct classes with each other.

## 2. Entire tangent spectrum

Put B=e^-2 and W~Binomial(K,p), U=K−W, D=1+U+BW. Define As=E[U/D] and Ao=B E[W/D]. The full projected gradient-field spectrum is

| Mode | Restoring eigenvalue | Multiplicity |
|---|---|---|
| Common rotations |0|d−1|
| Constant normal |2Ao/m|d−1|
| Within-group zero mean |[Ao−m As/(m−1)]/m|(C−2)(d−1)|

These exhaust C(d−1) tangent coordinates. Updating and its **coarse-point matched** frozen policy have the same spectrum there.

**Proof.** Every tangent lies perpendicular to u. All pair-score first derivatives are zero, so the sampler-response derivative vanishes. The expected coefficient from one anchor to an individual same-group candidate is As/(m−1), while an opposite-group candidate gets Ao/m. There is no diagonal same-candidate term. Symmetrizing both encoder appearances gives the off-diagonal tangent operator. Sphere projection adds the radial term2(Ao−As)/C. On a within-group zero-sum vector, the same-group off-diagonal block acts as minus As/(m−1), while the opposite block vanishes; together the eigenvalue is2[Ao−m As/(m−1)]/C. The constant and sign vectors yield2Ao/m and0. QED.

The exclusion correction m/(m−1) matters. Importing the old self-included coarse formula would give the wrong threshold.

## 3. Exact all-count stability condition

Tagged conditioning yields

\[
Ao-k As=Kf_{K-1}(2)\{Bp R_K-k(1-p)\},\qquad k=\frac m{m-1},
\]

where

\[
R_K=\frac{f_{K-1}(1+B)}{f_{K-1}(2)},\qquad
f_n(x)=E[(x+S_n)^{-1}],
\]

and S_n sums n iid weights in {1,B}, with probabilities 1−p and p. The ratio R_K is strictly greater than1 for every finite K and strictly decreases to1. A self-contained proof is as follows. Let a=1+B<b=2 and phi(z)=E[exp(−zV)] for V in {1,B}. The Laplace identity gives

\[
R_{n+1}=\frac{\int_0^\infty e^{-az}\phi(z)^n\,dz}
 {\int_0^\infty e^{-bz}\phi(z)^n\,dz}
=E_{\nu_n}[e^{(b-a)z}],
\qquad d\nu_n(z)\propto e^{-bz}\phi(z)^n\,dz.
\]

Incrementing n tilts nu_n by strictly decreasing phi, while exp((b−a)z) is strictly increasing. Their covariance is strictly negative, so the ratio decreases. It is greater than1 pointwise. Since S_n>=nB, the reciprocal-ratio representation also bounds it above by (b+nB)/(a+nB), which tends to1. Consequently

\[
\boxed{\text{coarse attraction for every finite K}
\quad\Longleftrightarrow\quad Bp\ge k(1-p).}
\]

At equality the finite-count curvature is still positive; the limiting curvature is0. Below this condition it is eventually negative, so it cannot be attractive at every finite count.

Equivalently p>=m/[m+(m−1)B]. For t>1 this becomes

\[
\epsilon\le\epsilon_{coarse}(m,t)
=\frac{(R-e^2)(1+k)}{(R-1)(1+ke^2)}.
\]

The right side increases with m, because k decreases and (1+k)/(1+ke²) decreases with k. Thus the dimension/class-count independent sufficient interval is

\[
0<\epsilon\le\epsilon_*(t)
=\frac{3(R-e^2)}{(R-1)(1+2e^2)}.
\]

For t=log4, epsilon_*=.10915049649902414. The fixed choice epsilon.05 satisfies the condition for **every even C>=4 and every finite K**. This is not an extrapolation of a K sweep.

Strict transverse eigenvalues and orthogonal equivariance give a normally attracting rotation manifold. Its local attracting neighborhood contains injective embeddings arbitrarily close to the collapsed manifold. This uses standard stability theory. The result proves an open local basin for each fixed finite K, not its measure under random initialization, a K-uniform basin size, or a uniform-in-K convergence rate. The equality boundary is especially not a claim of a nonvanishing limiting stability margin.

## 4. Class identification and a task-neutral robustness consequence

At the exact limiting two-point representation and uniform class prior, any downstream classifier, including nonlinear ones, has class-ID accuracy at most2/C. Information about the class is only1bit, rather than log2(C). This does not require selecting one binary factor or a preferred square matching.

For finite prototypes a separate robust discrimination metric is

\[
r(F)=\frac12\min_{i\ne j}\|f_i-f_j\|.
\]

Nearest-prototype classification is correct under all feature perturbations of norm strictly below r(F). If a radius exceeds r(F), two differently labeled balls overlap, so no classifier can be correct for every such perturbation. The extremal bound

\[
\sum_{i<j}\|f_i-f_j\|^2=C^2-\|\sum_i f_i\|^2\le C^2
\]

gives r(F)<=sqrt(C/[2(C−1)]), with equality precisely at the regular-simplex Gram matrix. The collapsed limit has radius0. This is standard simplex-packing reasoning, not new mathematics, but it supplies a quality criterion independent of chosen noise magnitude or factor weighting.

Actual finite arrays retain tiny within-cluster differences, so we do **not** call their noiseless mutual information exactly1bit. The exact information statement concerns the proved limiting attractor; their numerically measured robust radius is reported separately.

## 5. Nonidentity positive extension

Give each class v observations, and let P be any symmetric stochastic positive channel acting only within that class. Exclude the anchor's entire class from negative candidates. At the same class-coarse reference the class-mean eigenvalues are the prototype spectrum divided by v. A within-class zero-mean positive mode with eigenvalue mu has

\[
\lambda_{view}=\frac{Ao-As+(As+Ao)(1-\mu)}{mv}.
\]

Indeed class-constant negative coefficient blocks annihilate a zero-class-mean view vector, leaving the radial2(Ao−As)/(Cv) term. Positive curvature supplies2(As+Ao)(I−P)/(Cv). The first score derivatives still vanish, so response does not enter. Since mu<=1, this value exceeds the smallest class-shape eigenvalue whenever the latter is positive. Thus the same all-K sufficient floor condition establishes full attraction for class-consistent positive channels as well.

For v2 and Pswap the self-positive probability is0 and mu=−1. Full56-dimensional finite differences at C4,d8 confirm all modes for K1/8/32 to maximum error3.83e-11. No same-class negative is present. The candidate filter is part of the declared finite data model, not a proposed label-free filtering algorithm for arbitrary data.

## 6. Executed trajectories and paired fixed-law controls

From normalized iid Gaussian initial embeddings, all12prespecified prototype adaptive runs (C4/8,K1/8/32,primary7301/confirmation7401) reached the balanced antipodal neighborhood at the fixed field tolerance. Maximum final antipodal RMS was1.86e-7; halving the step in the declared confirmation arm retained the result. These are finite-model observations, not generic convergence theorems.

The exact uniform-off-diagonal **fixed** policy from the same Gaussian starts reached the regular simplex in all12paired runs. Maximum ETF Gram relative error was3.75e-7. The fixed law equals the adaptive policy at the ETF, rather than the adaptive policy at the random starting point. Observed robust radii were about.81649658 for C4 and.7559289 for C8, versus at most5.70e-8 in their paired adaptive runs.

Four additional nonidentity-positive adaptive runs (C4,v2,Pswap,K8/32,two fixed seeds) approached the class-coarse geometry, with within-class view variance0 and antipodal RMS at most4.73e-8. Their four uniform-other-class paired controls reached class-simplex geometry with Gram error at most1.90e-14 and between-class robust radius about.81649658. This control removes the identity-positive explanation as well as false negatives.

The maximum final quadrature discrepancy in these arms is1.12e-16. Every setting, seed and cap was fixed in the protocol before its respective arm; the paired-control and robust-radius additions are explicitly post-collapse diagnostics. Raw files and scripts are linked in README. These numbers support reachability and implementation; they are not the proof of all-K attraction or evidence of importance by their count.

## 7. Relation to the parent separation theorem

At the coarse point its own matched frozen policy is also stable, because the first-order policy response is zero. This fact must remain explicit. The proposed feedback separation instead compares the ETF's common uniform policy: the parent's fixed-law theorem makes it task-optimal, while the updating sampler's response destabilizes it and admits the class-merging basins proved here. Freezing at a different coarse-policy law is a different objective and cannot refute or establish that separation by itself.

The old square's K4/5 instability remained mild and injective. This is a changed, explicitly justified regime (positive floor.05 and no false negatives) with a different task-optimal reference and a genuine class-merging limiting attractor. It must not be retroactively reported as vindicating the rejected old semantic-erasure interpretation.
