# Normal view modes for regular class geometries

Status 2026-10-22: directly derived general normal-block theorem. This is a local spectral result. The elementary positive-graph quadratic form is inherited graph-Laplacian geometry; the count ordering below is the additional conclusion. It does not establish stability in the other representation directions.

## Assumptions

There are C unit class vectors v_c and m equally likely view nodes per class. At the reference every view of class c is v_c. Their Gram scores are s_cd. The reference is an **equilibrium of the projected expected update**. This stationarity assumption is separate from score regularity.

Each anchor class has the same score histogram and the same score-based negative policy. The policy gives class probabilities q_cd, split uniformly across the m candidate views. Negatives are independent with replacement. Positive sampling within a class uses a symmetric stochastic matrix P; its stationary distribution is uniform. The loss has denominator beta exp(s_pos)+sum exp(s_neg), with its positive score subtracted, so the negative score derivatives sum to B_K and the positive score derivative is minus B_K. This includes beta1 InfoNCE and beta0 DCL. In the following, scores in the negative denominator are shifted by the reference positive score1.

Put W_cd=exp(s_cd-1). With N_d the number of negative draws from class d, define the detached expected score coefficient

\[
b_{cd}=\mathbb E\frac{N_dW_{cd}}{\beta+\sum_jN_jW_{cj}}.
\]

Assume b_cd=b_dc, and set

\[
B_K=\sum_db_{cd},\qquad R_K=\sum_db_{cd}s_{cd}.
\]

Both quantities are independent of c under the row-law assumption. Let the ambient dimension exceed the span of the class vectors, so a nonzero normal direction exists.

## Proposition: exact normal-view eigenvalue

Let z_ci be perpendicular to every class vector, have zero average over the views of each class, and be an eigenmode of P with eigenvalue mu. In this invariant normal block, the restoring eigenvalue of the population detached update is

\[
\boxed{\lambda_{K,\mu}=\frac{2}{Cm}\left[B_K(1-\mu)-R_K\right].}
\]

It is the same for frozen and updating samplers evaluated at the same reference policy.

**Proof.** Consider normalized view perturbations

\[
f_{ci}(a)=v_c+a z_{ci}-\tfrac12a^2\|z_{ci}\|^2v_c+O(a^3).
\]

Every first derivative of a positive or negative score is zero, because z is normal to the class span. Consequently the first derivative of the score-dependent sampler is also zero. The sampler-response part of the linearization vanishes; only the ordinary frozen-policy score curvature remains.

The negative score second derivative between nodes ci,dj is

\[
2z_{ci}\!\cdot z_{dj}-s_{cd}(\|z_{ci}\|^2+\|z_{dj}\|^2).
\]

The cross product averages to zero, since each class has zero mean view perturbation. Summing the anchor and candidate radial terms using symmetry of b gives minus 2R_K times the squared perturbation norm, divided by Cm.

Positive pairs have score second derivative 2z_ci dot z_cj-minus their two squared norms. Its coefficient is minus B_K. Symmetric stochastic P therefore contributes

\[
\frac{2B_K}{Cm}\sum_c z_c^T(I-P)z_c.
\]

For Pz=mu z the Rayleigh quotient is the stated eigenvalue. The normal-view subspace is invariant: all negative cross-view linear terms depend only on the zero class means, and the remaining operators are the radial identity and P. QED.

## Count ordering, beyond a four-class square

At a fixed reference score policy q, the tagged-draw identity gives

\[
b_{cd}=Kq_{cd}W_{cd} f_{K-1}(\beta+W_{cd}),\qquad
f_n(x)=\mathbb E(x+S_n)^{-1},
\]

where S_n sums n independent positive score weights from the reference row law. By the strict log convexity argument in Lemma3 of `multilevel_theorem.md`, f_(n+1)(x)/f_n(x) increases strictly in x. Therefore the normalized tagged score weights shift to larger scores in monotone likelihood ratio order as K increases. In particular

\[
\xi_K:=R_K/B_K
\]

strictly increases with K whenever at least two different scores have positive probability. The view-normal mode is attractive precisely when the positive-graph gap 1-mu exceeds xi_K. Thus adding iid negatives makes this normal-view condition progressively harder, even though adding negatives can stabilize a semantic energy-transfer mode.

For finite score support, or a bounded continuous score law,

\[
\xi_K\longrightarrow
\frac{\mathbb E_q[Ws]}{\mathbb E_qW}
=\frac{\mathbb E_q[e^s s]}{\mathbb E_qe^s}.
\]

The limit follows by bounded convergence applied to Kf_(K-1).

For the square, C4, R_K=b_0-b_2 and B_K=b_0+2b_1+b_2, recovering the independent view-spectrum calculation. The within-plane and class-mean modes require the separate square theorem. Only their conjunction gives a full local-stability interval; this proposition alone supplies an upper count condition for one block.

## Why equilibrium is not implied by transitivity

Take three class vectors on a non-equatorial latitude,

\[
v_c=(a\cos(2\pi c/3),a\sin(2\pi c/3),b),\quad a^2+b^2=1,\ ab\ne0.
\]

Their score rows are identical and the geometry is transitive under rotations about the third axis. But if b_off is a positive off-diagonal coefficient, its weighted vector force contains

\[
(b_{self}-b_{off})v_c+3bb_{off}e_3,
\]

which is not parallel to v_c. The projected field is not stationary. Calling the displayed curvature a stability eigenvalue at this geometry would be wrong. An orthogonal symmetry group whose stabilizer fixes only span(v_c), or an independently verified projected equilibrium, suffices to close this gap. Regular simplex, orthoplex, square, and balanced hypercube references meet the radial-force condition.

## Scope and remaining prior-art challenge

The Laplacian spectral decomposition, radial sphere correction, and MLR sign-ordering principles are standard tools. The potential research knowledge is the exact negative-count dependence of the required augmentation gap across score-regular equilibria, and its competition with the different semantic-mode lower threshold. This upper-bound mechanism is present for frozen samplers too, so it must not be attributed to policy feedback. Its importance and novelty must be assessed together with the full square window and the source audit, not from this formula alone.
