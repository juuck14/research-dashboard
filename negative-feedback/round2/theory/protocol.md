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
