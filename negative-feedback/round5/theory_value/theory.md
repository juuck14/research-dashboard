# An independently justified target and the simplex-response calculation

2026-10-23. These results separate a standard task-geometry target from the proposed sampling-dynamics contribution. The linear-estimation and simplex optimality arguments are not claimed as new principles. The shape-response calculation is a direct derivation for this update and needs a separate novelty/importance assessment.

## 1. A task family that does not privilege the original binary factors

Let C be even and let the positive components be equally likely. A class-constant unit representation is a matrix F with rows f_i. Select y uniformly from all balanced vectors in{−1,+1}^C. This family and prior are invariant under every class permutation. Observe X=f_I+sigma Z, I uniform and Z standard isotropic Gaussian, independently of y. For each selected task allow the best population affine squared-error readout; downstream optimization and finite labels are not bottlenecks in this calculation.

Let J=I−11^T/C, G=JFF^TJ, and lambda_j>0 its nonzero eigenvalues. Then

\[
\boxed{\mathbb E_y\min_{w,b}\mathbb E[(y_I-w^TX-b)^2]
=1-\frac1{C-1}\sum_j\frac{\lambda_j}{\lambda_j+C\sigma^2}.}
\]

At sigma0 interpret the expression as1−rank(G)/(C−1). It is a population optimal affine regression result, not a claim about optimal nonlinear or zero-one classification performance.

**Proof.** Balanced symmetry gives E_y yy^T=CJ/(C−1). Center X by its mean. Its covariance is F^TJF/C+sigma²I and its cross-covariance with a fixed task is F^Ty/C. The optimal affine risk is1−Cov(y,X)Cov(X)^dagger Cov(X,y). Average this quadratic expression over y, use the covariance identity, and diagonalize JF with its singular values. The trace expression yields the displayed formula. At sigma0 the covariance inverse is the pseudoinverse on its exact range. QED.

For sigma>0, every unit F satisfies trG=C−C||mean(F)||²≤C, with at most C−1 nonzero eigenvalues. The function x/(x+C sigma²) is strictly increasing and strictly concave. Jensen's inequality therefore gives

\[
\boxed{R(F)\ge \frac{(C-1)\sigma^2}{1+(C-1)\sigma^2}.}
\]

When d≥C−1, equality holds exactly for the regular-simplex Gram G=CJ/(C−1). Equality requires centered rows, C−1 identical positive eigenvalues, hence that unique Gram. The same spectral expression applies to any task prior with covariance CJ/(C−1), so no binary-factor naming is involved. For odd C one can instead use an isotropic continuous prior on centered unit-variance tasks; the algebra is unchanged.

This is a standard LMMSE/isotropic-design calculation. It justifies the simplex as a natural full-class-spectrum target, not the originally selected rank-two square. The square's centered spectrum is(2,2,0), so its noise-free average risk is1/3, while the simplex's is0. At sigma.2 these risks are .3827160494 and .1071428571. The K4 rectangle also has rank2 and therefore noise-free average risk1/3. Thus stabilizing the original square is not itself a universal linear-utility recovery.

## 2. Matched frozen risk has a unique global simplex optimum

Now let C≥4, d≥C−1 and identity positives. At a regular simplex V, all self scores are1 and off scores r=−1/(C−1). Freeze any full-support permutation-symmetric row law q*: self probability u and equal off probability v, u+(C−1)v1. Use the joint-K denominator log(1+sum exp(s_ij−1)). The population risk as a function of a feasible Gram is permutation invariant, coordinatewise increasing in the off-diagonal entries, and strictly convex in all off-diagonal entries. Strict convexity follows already from the positive-probability tuple events where all K negatives equal a given j≠i: log(1+K exp(g_ij−1)) is strictly convex in g_ij. Other events are convex.

Average any Gram over class permutations. The resulting Gram has a common off score m. Jensen gives no larger risk after averaging. Positive semidefiniteness implies m≥−1/(C−1), since ||sum f_i||²≥0. Coordinate monotonicity then gives no smaller risk than at the regular simplex. Strict convexity and monotonicity imply equality only at the simplex Gram.

The permutation average need not obey the original rank bound; this is harmless because the argument is a lower bound on the larger PSD relaxation, and the simplex attaining it is feasible for d≥C−1. Thus the frozen objective has a **unique global optimum in Gram space**, not merely a locally attractive square reference. The same proof works for the uniform-off law with self probability0, because every off tuple event still has positive probability.

This argument is a direct convexity/symmetrization application related to existing ETF optimality theorems. It is included to ensure that the target and matched frozen comparison are independently meaningful.

## 3. Exact adaptive simplex shape eigenvalue

Let V be a regular simplex, embedded in any d≥C−1. A shape perturbation Z is tangent rowwise and preserves the class centroid: sum z_i0. Remove global rotations. Its first Gram derivative H=VZ^T+ZV^T is symmetric, has zero diagonal and zero row sums. Conversely, every such H has the rotation-orthogonal representative

\[
Z=\frac{C-1}{2C}HV,\qquad
\|H\|_F^2=\frac{4C}{C-1}\|Z\|_F^2.
\]

This space has dimension C(C−3)/2, so C≥4 is essential. At C3 there is no such shape direction.

For the easy exponential/base mixture with self candidates, put

\[
a=e^{-C/(C-1)},\quad
b=\frac1{C-1+e^{-tC/(C-1)}},\quad
v=\epsilon/C+(1-\epsilon)b,\quad
\rho=\frac{(1-\epsilon)b}{v},\quad\eta=t\rho.
\]

Let L~Binomial(K,(C−1)v), D=1+K−L+aL, M_K=E[L/D], and T_K=1−a E[L/D²]/M_K. The restoring eigenvalue on every shape direction is

\[
\boxed{\lambda_{shape}(K)=\frac{4aM_K}{(C-1)^2}(T_K-\eta).}
\]

**Proof.** Each row's off-score derivatives sum to0. Conditional on L, independent off candidates are uniform, so the squared sum of their score derivatives has expectation L sum_j H_ij²/(C−1). The ordinary log-sum curvature gives a M_K T_K/(C−1) times that row sum; the sampler normalizer derivative vanishes by row centering, and its response contributes −a M_K eta/(C−1). Average over C anchors.

The geometric second-score term along a normalized embedding path sums to(2b_off/C)||sum z_i||². It is zero on this shape subspace; it was not silently omitted. Finally use the displayed norm identity to divide directional curvature by ||Z||². Every shape has the same scalar coefficient, proving the eigenvalue and multiplicity. QED.

T_K<1 for every finite K. Therefore eta≥1 makes the independently optimal simplex **repelling in these directions at every finite count**, even though its matched frozen risk has the unique global simplex optimum. For t>1, this is equivalent to

\[
\epsilon\le\epsilon_{ETF}(C,t)
=\frac{C(t-1)}{C-1+e^{-tC/(C-1)}+C(t-1)}.
\]

At the exact boundary eta1, the finite-count eigenvalue is still strictly negative. For the natural tlog4 policy the floors at C4 and C8 are .3285746695 and .3001673819; epsilon.3 lies below them. The floor tends to1−1/t as C grows. These formulas do not prove global failure of every initialization or information erasure at the later endpoint.

## 4. Excluding the anchor class from every negative draw

If the base law is uniform on j≠i and the exponential reweighting uses that same off set, all negative weights at the simplex equal a. At the reference q* is uniform-off for every t and epsilon. The normalizer derivative still vanishes on the shape space. Now L=K deterministically and rho=1−epsilon. Therefore

\[
\boxed{\lambda_{shape}(K)=
\frac{4aK}{(C-1)^2(1+Ka)}
\left[1-\frac{a}{1+Ka}-t(1-\epsilon)\right].}
\]

Thus t(1−epsilon)≥1 guarantees shape repulsion at every finite count, with **no same-class/false negatives** in this class-constant model. The frozen uniform-off objective still has the unique global simplex optimum by Section2. This removes a specific false-negative explanation; it does not make the entire statement a new phenomenon beyond existing adaptive-negative/performative-prediction knowledge. That is a separate closest-work question.

## 5. Executed checks and what they establish

The script directly solves optimal affine regressions for every balanced task and compares the spectral formula, including C4/6/8, random/noncentered/collapsed/square/rectangle/simplex geometries and five noise levels. It independently enumerates ordered candidate tuples for the adaptive field and differentiates it on the explicit simplex shape direction, without importing the earlier population oracle. The preserved output records maximum risk identity discrepancy3.89e−16 and shape finite-difference vector residual4.06e−11.

The first execution exposed floating-point centering residue at an exactly collapsed geometry when using J@F, which a relative pseudoinverse cutoff treated as a nonzero signal. Centering by F−mean(F) avoids that artifact for the exactly collapsed input; no theorem, task family or pass threshold changed. This implementation failure is not a scientific counterexample.

The target-repair route has two different conclusions. Defending the original square as a task-universal target fails under the declared natural symmetric criterion. Reframing the instability around the globally justified simplex yields a stronger candidate separation that must be combined with actual bad attracting outcomes and the strongest prior work before any paper-level success verdict.

## 6. A coarse attractor has a task-level information cost

This section evaluates a two-group representation if another analysis establishes its attraction. It does not itself prove the dynamics converge there.

Let C=2m distinguishable positive components be merged into two equal groups, represented only by their group sign. For the same uniformly balanced task family, even an unrestricted nonlinear predictor has average noiseless Bayes MSE

\[
\boxed{R_{Bayes}=1-\frac1{C-1}=\frac{C-2}{C-1}.}
\]

**Proof.** Conditional on the group, the Bayes regression prediction is its mean label. Balanced-task symmetry gives E y_i y_j=−1/(C−1) for i≠j, so the expected squared mean of m group labels is[m−m(m−1)/(C−1)]/m²=1/(C−1). The Bayes MSE is1minus this predictable variance. Both groups have the same value. QED.

The average zero-one Bayes error is E[min(N,m−N)]/m, where N is hypergeometric with population C, C/2 positives and sample m. It is1/3 at C4. Direct enumeration in coarse_bayes.csv checks C4/6/8. This is not a failure caused by limiting the readout to a linear probe: the representation has only two values, and all functions of that sign are already affine on its support.

The lower bound survives any additive observation noise at the exact coarse geometry. In general, if pi_i(X) is the posterior probability of the original class given the observation, averaging the Bayes regression risk over balanced tasks gives

\[
R=\frac C{C-1}\left[1-E\sum_i\pi_i(X)^2\right].
\]

At equal two-group collapse, pi_i is the same within each group. Thus sum pi_i²≤1/m=2/C, giving R≥(C−2)/(C−1). At zero noise equality holds. By contrast an injective simplex has zero noiseless Bayes risk on every task. Under a fixed positive Gaussian noise, the Bayes risks vary continuously with the means, so sufficiently small neighborhoods of a bad collapsed limit retain a positive risk gap; this continuity is standard, not a new theorem claimed here.

**Finite-time qualification:** a flow approaching the coarse point may remain injective at every finite time. Its noiseless information need not drop before the limit. The exact lost-information claim refers to the limiting representation; practical finite-time robustness requires a declared nonzero noise/margin or finite-label condition, not rounding tiny coordinates to zero.

The excluded-anchor model also gives a direct observational reason not to merge these groups: every cross-class negative relation is correct and observed. Thus this is not merely a preference for named bits a,b over another equally plausible latent labeling. Whether an all-count bad attractor under that information is genuinely new relative to existing adaptive-negative/performative theories must still be determined independently.
