# Coarse clustering and square balance have different boundaries

This auxiliary direct derivation tests the semantic interpretation of square instability. Weighted-graph diagonalization and coarse clustering are not claimed as new general principles.

## Full local spectrum for arbitrarily many states

Let N=2m uniform observations,m≥2,be partitioned into two equal groups a_i=±1. Put f_i=a_i e1. Choose d≥N−1 if nominal representation capacity is a concern,so a simplex encoding every observation is available. Positives are identity observations and K negatives are iid. At the antipodal coarse point,let total opposite-group sampling probability be p,same-group probability1−p. Individual probabilities are p/m,(1−p)/m.

Write B=exp(−2),W~Binomial(K,p),U=K−W,D=beta+U+BW. The complete product-sphere gradient Jacobian has:

| Mode | Eigenvalue | Multiplicity |
|---|---|---|
| Rotations | 0 | d−1 |
| Constant normal | (2/m) B E[W/D] | d−1 |
| Within-group zero-mean | (1/m)(B E[W/D]−E[U/D]) | (2m−2)(d−1) |

All tangent dimensions are covered. Adaptive and matched-frozen Jacobians coincide **at this coarse point**: every tangent pair-score first derivative vanishes,so sampler response has no first-order effect. This is different from square balance instability.

**Proof.** Tangents v_i are normal to e1. Their first score derivatives vanish. Same/opposite per-state expected score-gradient coefficients are

`c_s=(K/m)(1−p) E[1/(beta+1+S_(K−1))]`,
`c_o=(K/m)p B E[1/(beta+B+S_(K−1))]`,

where S sums iid1/B variables. The symmetric gradient prefactor is2/N=1/m. Its row radial coefficient is c_s−c_o. Decompose every normal coordinate into group sign a,constant1,and vectors with zero sum in each group. The corresponding eigenvalues are0,2c_o,c_o−c_s. Palm count identities yield the table. QED.

## A different all-K transition

Define `R_K=E[1/(beta+B+S_(K−1))]/E[1/(beta+1+S_(K−1))]`. Coarse attraction is equivalent to `B p R_K>1−p`. R_K strictly decreases with K,from `(beta+1)/(beta+B)` to1.

For proof,fix low<high and consider r(z)=E[1/(low+S+z)]/E[1/(high+S+z)]. Its logarithmic derivative is negative because the inverse-moment ratio decreases with its argument. Adding an independent positive increment gives a positive denominator-weighted average of strictly smaller r(z). This proves decrease; bounded positive summands give the limit.

Therefore a coarse attractor can disappear at most once as K grows. If p≥1/(1+B),it is stable at every finite K(the limiting margin is zero at equality). If p<1/(1+B),it is eventually unstable. For beta1,K1 stability requires p>(1+B)/(1+3B).

For omega=4^(−s),epsilon=.3,p=.3/2+.7(16/17)=.808823529411...,the coarse point is stable at K1 and unstable at K2. At N4,d4,the computed smallest nonrotation gradient eigenvalues are+.0004129464 and−.0051202013. The general result applies to every even N,with magnitudes scaled by1/m.

Strictly positive transverse eigenvalues establish a local attracting neighborhood modulo rotations. It contains injective representations with arbitrarily small within-group differences. Those differences disappear in the limiting coarse representation,not necessarily at any finite time. For binary-factor observations,a partition by one bit loses all other bits at that limit. Balanced partitions number binomial(N,N/2)/2 up to group exchange; symmetry gives corresponding attractors. This is a standard combinatorial consequence,not a basin-volume or typical-initialization theorem.

The numerical K2–4 rectangle attractors remain injective. K4 has weak-factor energy.46914 rather than.5,so the exact square instability is not a substantial information-retention boundary in the inspected noise channels. Root finding is not a proof that no other attractors exist.
