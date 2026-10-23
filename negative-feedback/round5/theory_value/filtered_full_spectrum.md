# Entire regular-simplex spectrum with correct negatives

2026-10-23. Direct derivation and independently enumerated full-Jacobian checks. This is an exact theorem for the declared finite class-constant population, not a statement about generic encoders or all adaptive policies.

## Model

C≥4 equally probable observations have unit vectors f_i in dimension d≥C−1. Identity-positive score is1. Every negative is drawn independently from j≠i, so there are no same-class/false negatives. The detached policy is

\[
q_F(j\mid i)=\frac{\epsilon}{C-1}
+(1-\epsilon)\frac{\omega(f_i^Tf_j)}{\sum_{l\ne i}\omega(f_i^Tf_l)},\quad j\ne i;
\qquad q_F(i\mid i)=0.
\]

Require omega to be positive and twice continuously differentiable near the reference scores. At temperature one the loss is
\[
\ell_i(F;Y_1,\ldots,Y_K)=\log\left(1+\sum_{r=1}^K\exp(f_i^Tf_{Y_r}-1)\right).
\]
Both encoder occurrences receive gradients, followed by product-sphere projection. The vector field is the expected detached **gradient**, so positive eigenvalues mean attraction for its negative flow.

At a regular simplex V, off score r=−1/(C−1) and q* is uniform over all other observations, independent of the entire omega function and epsilon. Thus all these policies have the **same actual sampling law and same frozen objective at the target**. Write

\[
a=e^{-C/(C-1)},\quad D=1+Ka,\quad B=Ka/D,
\quad T=1-a/D,\quad\eta=-(1-\epsilon)(\log\omega)'(r),\quad b_1=B/(C-1).
\]

The matched frozen comparator holds this uniform-off q* fixed at every representation.

## Theorem: full tangent spectrum

| Mode | Restoring eigenvalue | Multiplicity |
|---|---|---|
| Centroid-preserving shape | `4B/(C−1)^2 * (T−eta)` | `C(C−3)/2` |
| In-span centroid change | `B*[2(C−2)/(C−1)^2 + C²/(C−1)^4*(T−eta) + C(C−2)/(C−1)^4/D]` | `C−1` |
| Common normal displacement | `2B/(C−1)` | `d−C+1` |
| Global rotations | `0` | `(C−1)d−C(C−1)/2` |

For the matched frozen policy replace eta with0. Multiplicities sum to C(d−1). In particular, no untested normal direction is hidden by restricting to one energy coordinate.

For C≥4, **strict linear attraction modulo rotations holds iff eta<T**. If eta>T, the shape block is repelling. Equality has neutral shape directions and is not declared strictly attractive.

If eta≥1, no finite count is attractive. If eta<1, strict attraction is equivalent to

\[
\boxed{K>\frac1{1-\eta}-\frac1a.}
\]

This is a complete count classification for this full reference geometry, not only one selected mode. A locally nondecreasing log weight has eta≤0 and is attractive for every finite count; that local fact does not exclude other failures elsewhere. The exponential omega(s)=exp(−ts) specializes to eta=t(1−epsilon).

## Proof of the quadratic form

Take any rowwise tangent Z and its first Gram derivative h_ij=v_i^Tz_j+z_i^Tv_j, i≠j. For each anchor let barh_i and Var_i(h) be mean and variance over the C−1 correct negatives. Because all negative exponential weights equal a at the reference,

\[
Q_{score}(Z)=\frac{Ka}{D}\frac1C\sum_i
\left[(T-\eta)\operatorname{Var}_i(h)+\frac1D\bar h_i^2\right].
\]

Indeed a tuple's score sum has second moment K Var(h)+K²barh². The ordinary log-sum derivative supplies B[T Var(h)+barh²/D]. The row-normalized policy derivative is (1−epsilon)(log omega)'(r)(h−barh), whose contribution is −B eta Var(h). This explicitly includes the sampler normalizer.

The second Gram derivatives induced by normalized vectors contribute

\[
Q_{geom}(Z)=\frac{2b_1}{C}\left\|\sum_i z_i\right\|^2.
\]

This follows by summing2 z_i dot z_j−r(||z_i||²+||z_j||²) over i≠j and using r=−1/(C−1). Positive first-score and sampler derivatives were not confused with this geometry term.

If eta<T, every term is nonnegative, and its null space requires \(h=0\) and \(\sum_i z_i=0\). In coordinates V=[S,0], S^TS=C/(C−1)I, the latter condition writes Z=[SA,SB]. The former forces \(A+A^T=0\); extending [A,B] to an ambient skew-symmetric matrix shows precisely that Z is a global rotation. Hence the quadratic form is strictly positive on nonrotation directions.

For necessity take the nonempty shape subspace described below. Its sign is T−eta, proving the strict-attraction iff criterion.

## Mode rates

For a centroid-preserving shape, h is a symmetric zero-diagonal matrix with zero row sums. Its rotation-orthogonal representative is Z=(C−1)hV/(2C), satisfying ||h||²=4C||Z||²/(C−1). The row means and geometric term vanish, yielding the displayed shape eigenvalue and the dimension C(C−3)/2.

For a centroid-changing in-span mode choose u in span(V), k_i=v_i dot u and z_i=u−k_i v_i. Direct simplex identities give

\[
\|Z\|^2=\frac{C(C-2)}{C-1}\|u\|^2,\quad
\frac{E_i Var_i(h)}{\|Z\|^2}=\frac{C^2}{(C-1)^4},\quad
\frac{E_i\bar h_i^2}{\|Z\|^2}=\frac{C(C-2)}{(C-1)^4},\quad
\frac{\|\sum z_i\|^2}{\|Z\|^2}=\frac{C(C-2)}{C-1}.
\]

Substitution gives the barycentric rate. There are C−1 independent u directions. The permutation-invariant quadratic form makes this subspace invariant; its bilinear terms with zero-row-sum shapes vanish by row summation. It also has no coupling to normal directions.

For z_i equal to a common vector perpendicular to span(V), first Gram derivatives vanish and only the geometric term remains. Its rate is2b1. Normal zero-sum vectors are rotations of the simplex span into unused ambient coordinates. Along with in-span rotations they give the displayed rotation multiplicity. This exhausts the tangent space and proves the spectrum.

## Executed verification

`check_theory.py` constructs the entire product-sphere tangent basis, independently enumerates ordered negative tuples, recomputes or freezes q, and differentiates every vector-field column. Thirty-six cases cover C4/6/8,dC,K1/3,epsilon.05/.3/.5, both policies. Maximum discrepancy across the **whole sorted spectrum** is3.84e-11; maximum imaginary residual5.92e-12. A separate54shape-direction comparison agrees to1.99e-11. These are numerical checks of the proof, not all-K proofs by extrapolation.

The desirable simplex geometry and convex fixed-risk optimum are established separately in theory.md; new knowledge cannot be claimed merely because the displayed coefficient has not appeared in an earlier paper. The complete separation must be assessed together with the bad-attractor and prior-art work.

## General temperature

Keep omega defined on the raw cosine score and use loss exponent(s−1)/tau. Define a=exp(−C/((C−1)tau)), D=1+Ka, B=Ka/D, T=1−a/D and eta=−tau(1−epsilon)(log omega)'(r). The exact quadratic form is

\[
Q(Z)=\frac B{\tau^2}E_i\left[(T-\eta)Var_i(h)+\frac1D\bar h_i^2\right]
+\frac{2b_1}{C\tau}\left\|\sum_i z_i\right\|^2.
\]

The full rates are

- Shape: `4B/[(C−1)^2*tau^2]*(T−eta)`.
- In-span centroid: `B*[2(C−2)/((C−1)^2*tau) + C²/((C−1)^4*tau²)*(T−eta) + C(C−2)/((C−1)^4*tau²*D)]`.
- Common normal: `2B/[(C−1)*tau]`.
- Rotations:0, with the previous multiplicities.

The strict full-attraction criterion remains eta<T. The proof is the same score variance/mean and sphere geometry calculation with their different temperature factors retained. No exponential form or global monotonicity of omega is required for this local result. Two samplers may have identical q* and opposite eta signs because their derivatives differ at the common off score; static target sampling alone cannot determine this stability.

Additional full-Jacobian checks use nonlinear positive weights exp(.7s²+.2s), exp(−log4*s+.4s³), and exp(log4*s), at tau.5/2 and C4/6,K1/3. All24cases match the general spectrum at maximum discrepancy1.77e-11. The formulas were sent to the parent before this implementation; these deterministic checks are not new empirical findings.
