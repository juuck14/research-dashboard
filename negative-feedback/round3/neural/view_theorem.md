# Joint negative count and augmentation spectrum: exact local result

2026-10-22. Direct derivation in this research, independently reconstructed algebraically by the foundations agent. Numeric spectrum checks and neural tests are separate evidence. This result does not by itself certify journal-level originality or importance. In particular positive-graph spectral analysis and neural pullback inertia are established tools.

## 1. Model

There are four equiprobable semantic states c=(a,b)∈{−1,+1}² and m≥2 equiprobable views r per state. Every one of the N=4m observations has its own freely trainable unit embedding f_(c,r)∈S^(d−1),d≥3. A positive is a view of the same state, drawn from a symmetric row-stochastic m×m matrix P_c. Its row sum is one and its symmetry makes the uniform view measure stationary. The channel may differ across states. The learner receives the positive correspondence; latent factor labels are not used in a representation gradient.

The negative policy is the previous detached positive score policy with epsilon/N uniform floor over all N observations. K negatives are conditionally independent draws with replacement. Both appearances of the representation receive gradients. Use the joint-denominator InfoNCE loss, not a weighted average of one-negative losses.

At the reference, all views of state c collapse to f_c*=(a,b,0,...)/sqrt2. Thus positives have score one and every negative draw has semantic score categories1,0,−1 with probabilities u,2v,w from the old four-state model. Conditional views inside a category are uniform. Let

```
A=exp(−1),B=A²,
(U,N,W)~Multinomial(K;u,2v,w),D=1+U+A*N+B*W,
b0=E[U/D],b1=A*E[N/D]/2,b2=B*E[W/D],
Btot=b0+2*b1+b2=E[(D−1)/D],lambda_plus=b1+b2.
```

Let lambda_b be the old four-state factor-balance gradient-field eigenvalue, either frozen or adaptive according to the current policy. Lambda_plus is the old normal-constant eigenvalue. Let μ_(c,j),j=1,...,m−1, denote the nonconstant eigenvalues of P_c. Define

`gamma=1−max_(c,j) μ_(c,j)`.

This is the algebraic Dirichlet spectral gap, not an absolute-value mixing coefficient. Symmetric stochastic channels can have negative eigenvalues, and no claim about aperiodic total-variation mixing is needed.

## 2. Theorem V1: the entire added view spectrum

The class-mean tangent subspace is invariant and its spectrum is exactly the old four-state spectrum divided by m. For each nonconstant eigenvector of each P_c, the added within-class modes have eigenvalues

```
lambda_view_normal(μ) = [lambda_plus−Btot*μ/2]/m,
lambda_view_plane(μ)  = [lambda_plus−Btot*μ/2+lambda_b/2]/m.
```

There is one in-plane mode and d−2 normal modes per (c,j). The class-mean modes have dimension4(d−1), and the view modes have dimension4(m−1)(d−1), exhausting the full tangent dimension4m(d−1). Class/view cross terms vanish. Normal refers to the complement of the square's two-dimensional span, not a restriction to one chosen extra output coordinate.

### Proof: class means and geometric terms

When all views of a class are perturbed equally, positive scores stay one, negative probabilities aggregate to the old four-state law, and each of its m embeddings receives1/m of the old gradient. In an orthonormal class-mean tangent basis the Jacobian is therefore the old one divided by m.

For a view mode supported on state c, choose an eigenvector ψ of P_c with sum_r ψ_r=0 and sum_r ψ_r²=m. At the reference, the expected negative loss-score coefficient matrix is constant on each class-pair block. Hence it annihilates every zero-class-mean perturbation. The positive coefficient matrix is −Btot P/(4m); symmetrization over its two encoder branches contributes −Btot μ/(2m) to the geometric tangent Hessian.

The expected Euclidean reference gradient is radial. At every node its coefficient is

`2/(4m)*[b0−b2−Btot] = −(b1+b2)/m = −lambda_plus/m`.

Differentiating the sphere projection consequently adds +lambda_plus/m to each tangent mode. These two contributions give the displayed normal eigenvalue. Every first score derivative is zero in a normal direction, so the log-sum curvature and sampler response add nothing there.

### Proof: extra in-plane score-response term

For an in-plane view perturbation, positive first-score derivatives are still zero, independent of the positive eigenvalue. The second-score geometric terms were already counted above. The additional log-sum curvature and policy response arise only from adjacent negative states.

For an anchor in c, the two adjacent score derivatives are ±ψ_r. Conditional adjacent-count symmetry gives E[(N2−N1)²|N]=N. The corresponding frozen-plus-response directional derivative is ψ_r² lambda_b. Averaging its anchor class contributes lambda_b/4 to the total quadratic form.

For an anchor in either adjacent state, only sampled views of c have nonzero first score derivative, equal to ±ψ of that sampled view. Its conditional sum has zero mean and variance equal to its count. That category has mean N/2 conditional on aggregate adjacent count. Thus each such anchor class contributes lambda_b/8. The two adjacent classes together contribute lambda_b/4. Opposite anchors have no first score derivative. The total additional quadratic form is lambda_b/2.

Divide by the direction's squared norm m to obtain lambda_b/(2m). This calculation uses the same conditional moments for frozen and adaptive lambda_b, and does not differentiate the sampler inside a learning update. Positive symmetry, independent zero view means, and the class-pair-constant negative kernel eliminate mixed class/view terms. Diagonalizing P_c exhausts its zero-mean subspace, completing the spectrum. QED.

## 3. Corollary: two stability constraints, not one

Retain the previous sufficient policy conditions g≤0,t2/t0≥e,Bw>Av. Then class means are stable exactly when eta<T_K. When this holds, lambda_b>0, making each view-plane mode larger than its corresponding view-normal mode. Therefore the entire adaptive square is strictly attracting modulo rotations exactly when

`eta<T_K AND gamma>xi_K`,

where

`xi_K=1−2*lambda_plus/Btot=(b0−b2)/Btot`.

Equalities are nonhyperbolic and are not classified. For the matched-frozen policy, class means are always stable under these conditions, and the sole additional condition is gamma>xi_K. Consequently high-K view instability can be shared by frozen and adaptive policies. It must not be attributed solely to closed-loop sampling feedback.

## 4. Theorem V2: the augmentation requirement increases strictly with K

For any strictly positive u,v,w with u+2v+w=1, xi_K strictly increases with K and

`lim_K xi_K=(u−B*w)/(u+2A*v+B*w)`.

### Proof

Let Z have support{1,A,B} with probabilities{u,2v,w}, and let S_n=sum_(r=1)^n Z_r. Put

`f_n(x)=E[(x+S_n)^−1]`.

Size-bias conditioning one tagged negative gives weights

`b0=K*u*f_(K−1)(1+1)`,
`2b1=K*2v*A*f_(K−1)(1+A)`,
`b2=K*w*B*f_(K−1)(1+B)`.

Thus normalized(b0,2b1,b2) is a probability distribution on Z, proportional to p(z)*z*f_(K−1)(1+z). Xi_K is the expectation of the strictly increasing function h(B)=−1,h(A)=0,h(1)=1 under that distribution.

For fixed n, f_n is strictly log-convex: writing inverse moments m_j(x),

`f_n'' f_n−(f_n')²=2*m3*m1−m2²>0`

by Cauchy–Schwarz. Therefore for every a>0, f_n(x+a)/f_n(x) is strictly increasing in x. Independence gives

`f_(n+1)(x)/f_n(x)=E_Z[f_n(x+Z)/f_n(x)]`,

also strictly increasing. Passing from K to K+1 hence tilts the tagged-weight distribution by a strictly increasing function of z. The covariance of this tilt with h(z) is strictly positive because every support value has positive mass. This proves strict increase of xi_K.

Finally Z≥B>0. Bounded inverse-sum convergence yields K*f_(K−1)(1+z)→1/E[Z], uniformly over the finite support. The normalized weights therefore tend to p(z)*z/E[Z]. Taking the expectation of h gives the stated limit. QED.

The same proof was independently reconstructed in the foundations task using ratios of shifted Stieltjes transforms. This is a proof, not extrapolation from the numeric K sweep.

## 5. Exact finite stable window

T_K strictly increases, so eta<T_K imposes a lower-count constraint. Xi_K also strictly increases, so gamma>xi_K imposes an upper-count constraint. Their intersection is an interval of integers, possibly empty, finite, or unbounded. A connected positive channel is not by itself sufficient: its quantitative gap matters.

For omega(s)=4^(−s),epsilon=.3 and P=.95 I+.05 Uniform_class, gamma=.05. The old balance certificate gives instability through K4 and class-mean stability from K5. New outward70-digit finite-sum bounds give

```
xi_11=.04853516089345359... < .05,
xi_12=.05201103415789361... > .05,
xi_infinity=.1034779521771101... .
```

Consequently the full square is stable **exactly for K5,...,11**. K≥12 is unstable in within-class normal directions even though its class-mean factor mode is restoring. The new certificate is `results/mixing_interval_certificate.json`; its interval arithmetic imports the already independently reviewed class from the preceding stage. This certificate has not yet received a separate independent reviewer replication in this round; the root owns that audit.

This window combines two mechanisms: low-K factor imbalance caused by the adaptive response, and high-K failure of view invariance shared by its matched-frozen objective. It is not a claim that one feedback instability changes sign twice. Nor is it a theorem about lost semantic information: an unstable view mode can encode more nuisance information, while a mild factor imbalance can remain fully injective.

## 6. Executed tests and present scope

- Direct multinomial4-state loss/gradient versus Laplace quadrature: value discrepancy≤2.49e-14,gradient≤5.97e-15; fixed-q finite-difference value gradient≤3.01e-10.
- Uniform positive views,m2/4,K1,2,4,5,8,16:24 full tangent settings; class-mean spectrum discrepancy≤3.95e-11 and class/view cross blocks≤1.31e-11.
- Lazy complete mixing,20 additional full tangent settings including weak positive channels: maximum entire-spectrum discrepancy2.24e-10.
- Lazy cycle and reflecting-path channels,12 settings: full spectrum discrepancy3.16e-11 using their actual nonconstant eigenvalues, not a complete-graph approximation.
- Constructed shared MLP full-rank tangent test, actual parameter-flow tests, and ordinary warmup are reported separately. The ordinary warmup did not meet the square applicability criterion in any of three seeds. This limitation is not removed by the exact constructed-reference result.

The theorem extends the number and structure of nuisance views and positive correspondence. It still has four semantic states in a symmetric collapsed square and says nothing general about arbitrary class-center geometries or global attractors. The more general score-regular normal-mode result is developed by the foundations task, not silently assumed here.
