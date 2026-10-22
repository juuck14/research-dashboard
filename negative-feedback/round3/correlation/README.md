# Why iid count laws cannot be extended from pairwise sampling summaries

Status: explicit counterexample and exact balance-sign certificate, with independent field verification. This is an assumption-boundary result, not the paper's main novelty. [Protocol](protocol.md), [construction and execution](run.py), [exact certificate](certify.py).

Draw four independent candidate sources from the current policy. Repeat them with block sizes r=(5,3,2,2), or r=(4,4,3,1), and uniformly shuffle the12positions. Both schemes have four sources, count12, and sum r²42. The one-position laws match and any pair has same-source probability30/132. Hence the complete two-position law matches at **every** representation. The set of distinct sampled observations is exactly the set of the four sources, so its whole distribution matches too.

The count-vector laws do not match. For a square reference let A=e^-1, independent source categories have exact probabilities(103,374,523)/1000 and weights(1,A,A²). Write

\[
D=1+\sum_l r_l W_l,\quad
V_1=\sum_l r_l 1_{adjacent,l},\quad V_2=\sum_l r_l^2 1_{adjacent,l}.
\]

The balance restoring coefficient is

\[
\lambda=A\mathbb E[V_1/D]\left[1-A\frac{\mathbb E[V_2/D^2]}{\mathbb E[V_1/D]}-\eta\right].
\]

The bracket thresholds are.71572461274677 and.70977108505890. Choose eta to be their **exact midpoint**. A smooth positive monotone weight

`omega(s)=exp(−log(4)s+alpha*s*(s²−1))`

keeps the square policy values and sets the required slope with alpha=eta*.187/.112−log4≈−.19626. Its log derivative is −log4+alpha(3s²−1). Since alpha<0 its maximum is at s0 and is about−1.19003<0; monotonicity is analytic, not just grid-checked. Thus the construction satisfies a natural monotone easy-negative preference while giving opposite balance signs.

The [exact rational certificate](results/rational_certificate.json) proves a positive threshold gap greater than.005953527687868222030768 using outward bounds for e and monotonicity of the inverse-denominator moments. It certifies the balance signs; full-space eigenvalues are separately finite-difference verified in [summary](results/summary.json). Independent ordered-source gradients agree to1.12e-11 in [review](../review/correlation_check.json).

Uniform repetition of M sources r times is a simpler control, but its identity `loss=log(r)+loss_(M,beta/r)` is a direct old-offset corollary. Neither that identity nor the general fact that nonlinear expectations depend on higher-order laws carries a novelty claim. The matched construction precisely records what an iid count theorem cannot infer from ESS, pairwise marginals or unique-set diversity.
