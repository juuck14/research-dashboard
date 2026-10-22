# Bounded continuous populations and a realizable product of spheres

Status 2026-10-22: proved extension of the multilevel law. Finite generic lists and continuous populations are different: if every finite score is unique, E[h|s]=0 forces h0. A continuous sum of exchangeable factors can have a nondegenerate conditional derivative law even though independent candidates almost surely have different exact scores. This removes the discrete-tie limitation, but not the exchange-symmetry assumption.

## Theorem extension

Replace the finite candidate list in `multilevel_theorem.md` with a probability law p on a standard Borel space, bounded measurable scores s and derivatives h, E_p[h|s]=0 almost surely, and E_p h²>0. Require the scalar path s_delta=s+delta h, fixed positive score1, and the same mixture/exponential policy with0<epsilon<1,t>1. Negative draws remain iid. Scores need only have compact support; cosine scores are a special case.

Every conclusion of Sections2–5 continues to hold, with sums replaced by integrals: the exact tagged-draw curvature, no stable-to-unstable transition as K increases, and eventual positive curvature iff Q>0. In particular Q≤0 implies strict negative curvature at every finite K, including Q0.

**Proof.** On a fixed small interval around delta0, s_delta and h are uniformly bounded, policy probabilities relative to p and their first derivatives are bounded, and all denominator weights are bounded above and away from zero. Differentiation under each fixed finite-tuple integral is justified by dominated convergence. Conditional on the tuple scores, the iid conditional h variables still have mean zero. This proves the same tagged-draw formula with the positive finite measure dnu=q h²W dp. All three inverse-moment lemmas concern bounded positive random W and do not require atoms. The score-crossing comparison is a pointwise inequality integrated against dnu, so it also applies to non-atomic populations. The K limit follows from bounded positive W and the law of large numbers with uniform inverse-denominator domination. The Q≤0 argument remains strict because dnu is nonzero and W R_n is positive on its support. QED.

This theorem allows continuous conditional variation h|s. It does not allow arbitrary perturbations violating exchange balance or nonlinear score paths without the extra second-derivative terms.

## Product-of-spheres representation

For m≥2 and r≥2, let x=(u_1,...,u_m), where factors are independent uniform points on the unit sphere S^(r−1). Define

\[
F_\delta(x)=\left(\sqrt{1/m+\delta}\,u_1,
\sqrt{1/m-\delta}\,u_2,u_3/\sqrt m,\ldots,u_m/\sqrt m\right).
\]

Every embedding has norm1 for |delta|<1/m. For a fixed anchor, relative factor dots z_k=u_k dot v_k are iid continuous variables on[-1,1]. Candidate scores and derivatives are

\[
s=m^{-1}\sum_k z_k,\qquad h=z_1-z_2,\qquad s''=0.
\]

Exchanging the first two z values preserves s and reverses h, giving E[h|s]=0, while E h²=2/r>0. Reference score rows have the same law at every anchor. The product of orthogonal-factor symmetries and factor permutations makes the expected base force radial at each anchor, so delta0 is a projected equilibrium of the free-function field. The scalar result therefore describes a genuine local factor-energy direction.

The function-space model permits all measurable unit embeddings, so the result does not depend on imposing an insufficient finite output capacity. It remains a local energy-direction result: it does not prove global information loss, a global attractor, or parameter-space convergence.

Let M_r(a)=E exp(a z) for one relative factor. Symmetry makes M_r even. Write

\[
L_{m,r}(c)=2\left[M_r''(c/m)M_r(c/m)-M_r'(c/m)^2\right]
M_r(c/m)^{m-2}.
\]

Independence gives Z=M_r(t/m)^m and E[h² exp(c s)]=L_(m,r)(c). Hence the exact critical uniform floor is

\[
\epsilon_c(m,r,t)=
\frac{(t-1)L_{m,r}(1-t)}
{(t-1)L_{m,r}(1-t)+M_r(t/m)^m L_{m,r}(1)}.
\]

For r3, z is uniform on[-1,1] and M_3(a)=sinh(a)/a, with the continuous value1 at0. For r2, M_2(a)=I_0(a), the modified Bessel function. These are analytic moment formulas, not Monte Carlo estimates.

For any fixed r, M_r(0)=1, M_r'(0)=0, M_r''(0)=1/r. Consequently L_(m,r)(c) tends to2/r and Z tends to1 as m grows, yielding the same limiting critical floor1−1/t as the discrete cube. The fixed-K curvature limit is

\[
\lim_{m\to\infty}H_K(m,r)=\frac{(2/r)KA}{\beta+KA}
\left[1-t(1-\epsilon)-\frac{A}{\beta+KA}\right],\quad A=e^{-1}.
\]

Thus discreteness is unnecessary for the no-rescue floor and count-ordering phenomenon. The common exchange structure is necessary for this proof; this is not evidence that arbitrary asymmetry leaves the law unchanged.

## Two-factor continuous law for independent numerical checking

For r3,m2, the score density is p_s(s)=1−|s| on[-1,1], while

\[
\mathbb E[h^2\mid s]=\frac43(1-|s|)^2.
\]

Indeed at fixed z1+z2=2s, h=z1−z2 is uniform on the interval with endpoints plus/minus2(1−|s|). This conditional variance remains positive on the whole open score interval, despite the absence of discrete score ties. The accompanying script integrates this exact density separately on either side of0 and compares two quadrature resolutions. It is deterministic numerical validation of the derived law, not a proof by discretization.
