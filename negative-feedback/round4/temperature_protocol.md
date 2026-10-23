# Temperature and policy scope check — before execution

2026-10-23. This is a scope clarification, not a new main contribution. Keep the policy on **raw cosine scores** q_delta∝epsilon*p+(1−epsilon)*p*exp(−t*s_delta)/Z_delta, and vary only the loss temperature tau. The policy exponent need not rescale when tau changes; assuming that it does would be a different experiment.

Use the three-bit balanced product construction, s=mean(z), h=z1−z2, uniform8candidates, beta1, iid negatives, both scalar score occurrences represented by the affine Gram path. Fixed tau={.25,.5,1,2}, t={−2,0,log4,3}, epsilon={.1,.3}, K={1,2,3}. Enumerate ordered tuples exactly; compare a separate detached-field finite difference on the tau.5/1, t−2/log4, epsilon.3 subset.

Record dimensionless response strength theta=t*tau. The existing no-reentry/no-rescue proof uses theta>1 after rescaling. Do not infer failure when theta≤1: that is outside the stated theorem. A direct corollary predicts strictly positive scalar curvature for all finiteK when t≤0 and beta>0. This is a statement about this exchange-balanced affine mode, not all hard-negative training.

Checks before inspection: population drift atdelta0<1e−12; tuple finite-difference error<1e−6; every hard/uniform-policy value>0. The purpose is to expose which parameter is essential and avoid calling the fixedK5..11 number a universal constant. No seed selection or repeated tuning is involved.
