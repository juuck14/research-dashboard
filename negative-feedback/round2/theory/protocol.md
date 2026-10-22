# General score-policy and arbitrary-negative-count theory verification

Recorded before the numerical work in this directory, 2026-10-22. Symbolic derivations motivated the following fixed checks. This is a follow-up to the earlier square discovery, not a pre-registration before the whole research program.

## Questions and refutations

1. Does the exact factor-balance stability threshold depend only on an effective local score slope and a K-dependent inverse-denominator moment?
2. Does that threshold strictly increase with negative count K? A single mathematical counterexample or numerical failure outside numerical tolerance refutes the stated universal result.
3. Can two positive smooth nonincreasing score policies agree at every square score {-1,0,1}, hence have identical frozen distributions/objectives for every K, yet have opposite adaptive stability?
4. Can increasing K stabilize a borderline policy rather than always worsen suppression? Test the full tangent space, not just the tied factor coordinate.

## Fixed model and checks

Uniform two bits, normalized independent lookup vectors in dimension4, identity positives, temperature1, detached sampler q=epsilon/4+(1-epsilon)w(s)/sum(w). Family w_alpha(s)=exp(-2s+alpha*s*(s²-1)), alpha∈[-2,1], which is positive and nonincreasing on [-1,1].

Primary eps=.1. Fixed alpha levels {-1.5,-.9,0,.5}; all have identical policy values at {-1,0,1}. Fixed K=1,...,128 for exact moment enumeration; full tangent finite-difference checks for K∈{1,2,4,8,16} and alpha∈{-1.5,-.9,0}. Moment enumeration aggregates the two symmetric adjacent categories into a three-category multinomial; compare independent four-category enumeration for K1–8 and actual vector-field differences for K1–16. Fixed steps1e-5 and3e-6. No seed is needed for exact expectation. A separate random orthogonal orientation(seed70313) will test coordinate dependence where needed.

Expected support: all candidate probabilities remain ≥eps/4. Frozen full-sphere positive curvature plus adaptive factor-balance sign reversal demonstrates response-specific instability. Count stabilization is accepted only if all nonrotation adaptive flow eigenvalues are negative at the claimed larger K; otherwise state only scalar-mode stabilization. Same-value policy matching requires max q difference<1e-13. Analytic eigenvalue versus finite-difference tolerance2e-7 and exact probabilities within1e-11.

Threshold formula and monotonicity will be distinguished as complete analytic proofs. Numerical checks do not prove them. Policy-form construction and frozen/adaptive distinction alone are not claimed as publication novelty. Root performs literature and contribution review separately.

## Follow-up analytic controls (fixed before execution)

The general proof suggested two controls after the original run. These were selected analytically, not by testing multiple numerical settings. The original protocol/results stay unchanged.

1. **Natural exponential policy:** omega(s)=4^(−s), epsilon=.3, giving exact square probabilities (u,v,w)=(.103,.187,.523), eta=(112/187)log(4). The full-stability sufficient conditions can be checked before running code. Evaluate K=1,...,128 and establish the first stable count using exact finite sums. This tests whether count rescue needs the matched-value polynomial family; it does not test global dynamics or learned encoders.
2. **Positive-denominator removal (DCL control):** replace loss log(1+sum exp(s−1)) by log(sum exp(s−1)), keeping the same sampler, positive, and feasible representation space. Evaluate both the natural policy and the originally fixed alpha=−.9 policy for K=1,...,128. Derive the threshold and compare to InfoNCE before interpreting numbers. Anticipated falsifier of a broad claim: if rescue disappears after removing the positive term, do not call it a generic multiple-negative sampling effect.
3. Full-field tangent finite-difference checks: K=1,2,4,8,16, two losses, both policies, step 1e−5. Same formula and 2e−7 eigenvalue error tolerance as the first run. The sampler is detached; the field is recomputed on perturbation. No Monte Carlo sampling and no optimizer are used.
4. Numerical thresholds are illustrations of already proved inequalities, not a novelty certification. Decoupling is an explicit strongest competing explanation and must be included in the manuscript.

Derivations before numerical execution: DCL has Palm denominator Y_K=A+sum_(K−1) Z instead of 1+A+sum_(K−1)Z. The same monotonic-ratio proof gives T_1^DCL=0, strict increase to one, and T_K^DCL<T_K^InfoNCE for every K. This predicts a later cutoff but not disappearance of count rescue for every eta in (0,1). K=1 frozen balance curvature is zero under DCL and cannot be called a stable matched-frozen contrast.
