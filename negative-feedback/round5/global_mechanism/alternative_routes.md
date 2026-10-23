# Attempted alternative explanations and what survived

2026-10-23. These routes were actually analyzed or executed. They are not a list of future experiments.

## Route A: global large-count energy and true collapse

At epsilon0,K→infinity, let a=t−1>0. The detached negative-score coefficients become proportional to exp(−a s). Hence the representation field is exactly the gradient of

\[
E_\infty(F)=-\frac1{aC}\sum_i\log\left[\frac1{C-1}\sum_{j\ne i}e^{-a f_i^Tf_j}\right]
\]

for identity positives (whose contribution is constant). It is not the derivative of the composed expected original loss through q. This effective-energy equivalence was known in the earlier work and is excluded from novelty.

**Global minimizer result.** For even C, E_infinity is minimized exactly by a balanced antipodal representation, with value

\[
-\frac1a\log\{\cosh a+\sinh a/(C-1)\}.
\]

Proof: the convex exponential lies below its endpoint chord on[-1,1], so exp(−a s)<=cosh(a)−s sinh(a). Write mean vector mu=C^−1 sum_i f_i. The row mean of off-diagonal scores is (C f_i·mu−1)/(C−1). Applying the chord bound and Jensen to the average log gives at most log[cosh(a)+sinh(a)/(C−1)−C||mu||²sinh(a)/(C−1)], itself at most the stated constant. Equality requires mu0 and every off-diagonal score in{−1,+1}. Since all vectors are unit, this forces a common antipodal axis and balanced counts. Conversely that geometry attains the bound. QED.

For an arbitrary unit-embedding population with unrestricted independent candidates, the same argument gives bound−log(cosh a)/a and equality exactly at the balanced two-point law. These are elementary chord/Jensen consequences after the energy reduction. **They do not carry the finite-count feedback contribution.** They establish an exact limiting explanation, and motivated the positive-floor finite-K extension in global_collapse.md.

## Route B: is the finite-count field just another fixed energy?

Three unit vectors in d3 have an open realizable Gram domain with independent coordinates x=s12,y=s13,z=s23. The expected detached update defines a one-form omega=Cx dx+Cy dy+Cz dz. A fixed scalar energy, even after a positive scalar time reparameterization, would require omega wedge d(omega)=0, equivalently C dot curl(C)=0. This is a necessary local integrating-factor condition.

Exact tuple expectations at three fixed positive-definite Gram triples were differentiated at two steps. With self candidates included,54of60settings had a stable nonzero obstruction; the zero-floor infinite-count baseline was gradient to numerical tolerance. With the clean off-diagonal candidate law, all48finite-count settings had stable nonzero obstructions. The twelve tested infinite-count settings were integrable in this three-observation special case; two-candidate rows have a one-dimensional score-difference structure, so this is not evidence of generic positive-floor integrability.

An exact **constructed** K1 counterexample replaces the exploratory score values with x=log(6/5),y=log(4/5),z=log(7/5),t3,epsilon1/20. Let r=(6/5,4/5,7/5), f_i=r_i/(e+r_i),

q(r_i,r_j)=epsilon/2+(1−epsilon)/(1+(r_i/r_j)^3),

k(r_i,r_j)=3(1−epsilon)(r_i/r_j)^3/[1+(r_i/r_j)^3]^2.

Then C_i=(f_i/3)sum_(j≠i)q(r_i,r_j). Differentiating the two candidate rows gives

\[
C\cdot\operatorname{curl}C=\frac{eS}{9\prod_i(e+r_i)},
\quad
S=-\frac{112610544188193}{1132297363071875}\ne0.
\]

All Gram off-diagonals have absolute values below.4 and each row's absolute off-diagonal sum is below.65, establishing strict positive definiteness and realizability. The exact rational sign is certified in certify_nonpotential.py/json. Therefore no smooth positive integrating factor makes this field the differential of a fixed potential locally. This is stronger than merely observing a different expected loss value.

**Outcome:** the broad explanation “the finite-count field is always ordinary optimization of a transformed fixed energy” is false. But generic nonconservativeness is familiar from performative/model-dependent distributions. Non-integrability alone does not show cycles, harmful learning, important novelty, or top-journal value. It is an auxiliary exclusion, not a replacement main contribution.

## The candidate that remains

The substantive finite-count route is the joint separation: an independently task-optimal, fixed-law simplex can have the same current negative law as the adaptive sampler, yet the response destabilizes it for every K, and the same full-support/no-false-negative regime admits open class-merging basins. The parent's reference instability and this branch's all-K coarse theorem must be evaluated together against the closest prior work. This route now has an actual learning consequence; it is not another defense of a preferred balanced square. Whether it meets the fixed novelty/importance standard remains a substantive review question, not a conclusion from these auxiliary checks.
