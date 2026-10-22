# Independent audit of the multilevel sign theorem

2026-10-22. Reviewed `../foundations/multilevel_theorem.md` directly. This audit derives the coefficients and checks the proof logic; it does not treat the author's numerical sweep as a proof, and does not equate a correct theorem with a JMLR-level contribution.

## Assumptions actually needed

The candidate population is finite, has fixed positive base probabilities, and the scalar path has exactly affine scores `s_j(delta)=s_j+delta*h_j`. The conditional balance `E_p[h|s]=0` holds at every active score. Negatives are independent with replacement from the current score policy. The exponential policy is decreasing with exponent `t>1`, has a nonzero uniform/base floor strictly below one, and is detached inside each gradient update. Positive score is constant one. These assumptions imply stationarity of the scalar field at zero; they do not establish stationarity of an arbitrary full representation.

## Coefficient check

At zero, conditional balance also holds under `q`, because `q/p` depends only on score. It gives `Z'=0` and `q'_j/q_j=-t*rho_j*h_j`. For a tuple, let `D=beta+sum W_r`, `A=sum W_r*h_r`, with `W_r=exp(s_r-1)`. Differentiating the detached expected field gives

`E[sum W_r*h_r^2/D - A^2/D^2 - t*A*sum rho_r*h_r/D]`.

Conditional on the tuple's scores, the sampled candidate identities remain independent, each with zero conditional mean derivative. This remains true with replacement: two draws may coincide, but coincidence was not conditioned upon. Cross-draw terms therefore vanish. The remaining tagged term is exactly

`H_K/K = sum_j q_j*h_j^2*W_j*f_(K-1)(beta+W_j) * [1-t*rho_j-W_j*R_(K-1)(beta+W_j)]`.

No missing factor of K, policy normalizer, or log-probability derivative was found.

## Sign-order proof check

For a positive random variable Y, the ratio `E(Y+z)^-2/E(Y+z)^-1` decreases strictly in z. Its derivative numerator is `-2*m3*m1+m2^2<0`. Adding one independent positive negative is a weighted average of smaller deterministic-shift ratios. This verifies the pointwise increase of each score-local margin in count. That fact alone would not prove the theorem because its tagged weights also change.

The extra likelihood-ratio argument is valid. `f_n(x)=E(x+S_n)^-1` is strictly log-convex; hence `f_n(x+z)/f_n(x)` increases in x for each z>0. Averaging over the new independent draw gives increasing `f_(n+1)/f_n`. This is the necessary control on the changing weights.

For `r=W*m2/m1` and `T=1-r`, Cauchy–Schwarz gives `W*r'<=r-r^2=T*(1-T)`. At a zero of `a=T-t*rho`,

`W*a' >= t^2*rho*(1-rho)-T*(1-T) = (t-1)*T >0`.

Except at beta=n=0, small W gives negative a and large W gives positive a. Thus a has just one upward sign crossing. Multiplying its negative and positive portions by an increasing ratio cannot turn a nonnegative weighted mean negative. Strict pointwise margin improvement then proves `H_K>=0 => H_(K+1)>0`. The exceptional beta=n=0 margin is strictly negative, so it does not invalidate the implication. The claim concerns sign ordering, not monotonicity of numerical curvature magnitude.

## Critical-floor check

Finite positive support gives a uniform law-of-large-numbers limit for the tagged inverse moments. The limiting curvature is `e^-1*Q/E_q W`. A positive Q guarantees eventual positive curvature. For nonpositive Q, the limiting margin `1-t*rho(W)` is increasing, while the finite-count factor `f_n(beta+W)` decreases in W. That tilt cannot make a nonpositive signed mean positive; the additional strictly negative `-W*R_n` term makes every finite curvature negative, including Q=0. This is stronger than merely evaluating the infinite-count field. The necessity at every finite K is the part not supplied by the standard effective-temperature limit.

The hypercube product moments also agree independently: when `h=z1-z2`, only opposite first-two signs contribute, yielding `E[h^2*exp(c*s)]=2*cosh(c/m)^(m-2)`. Therefore the displayed critical-floor formula and limit `1-1/t` follow. The path has affine pairwise scores and unit norms, so this is a realizable directional curvature, not an arbitrary score table.

## What remains outside this verification

The full representation may have other unstable modes. Unrelated anchor score laws cannot simply be averaged under this theorem without another proof. Non-affine paths introduce an extra score-second-derivative term. A generic learned representation need not satisfy the required symmetry, conditional balance or stationarity. Correlated negatives violate the iid denominator argument. No theorem here establishes terminal factor removal, a Bayes error increase, or a learned network's tendency to visit the analyzed geometry.

**Mathematical verdict:** no proof defect identified in the stated restricted theorem. This is a substantive structural extension beyond the old one-score-level square formula. **Contribution verdict:** separate; the old infinite-count curvature account explains Q's formula, whereas the no-re-entrant finite-count sign law and exact no-rescue criterion are the candidate independent knowledge. Their importance must be judged at the fixed journal bar rather than inferred from this proof audit.
