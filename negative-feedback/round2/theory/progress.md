# Progress

2026-10-22: reread previous theory and K-negative enumeration. Derived conditional-count simplification, inverse-moment ratio monotonicity argument, and candidate arbitrary-K full tangent spectrum. Protocol stored before new numerical checks. No new execution results yet.

## Completed general theory and original numerical run

- **Executed/derived:** theorem.md Sections2–5 give the complete d≥3 tangent spectrum for arbitrary K and positive C² weight, exact monotone threshold, all-K sufficient conditions making it the full-sphere criterion, and a same-values/different-slope family.
- **Actual evidence:** code/verify_general.py evaluated K1–128, four fixed alpha policies, 32 complete d4 tangent finite differences and independent count aggregation. Maximum adaptive eigenvalue discrepancy 8.86e−11. The alpha−.9 policy crosses from unstable K8 to stable K9, and the proof makes stability universal for K≥9. JSON serialization failed after numerical assertions on the first run; builtin-bool conversion fixed output only, followed by a complete rerun.
- **Cross-review:** the independent theory critic rederived the C_p Palm coefficients and residual bound, confirmed the sufficient-condition proof, and reported a separate ordered-tuple finite-difference audit with maximum discrepancy 4.67e−11. Its own files are in round2/review/.
- **Judgment change:** the arbitrary-K full spectrum is stronger than the initial one-mode/count hypothesis. It is no longer only a K≤128 observation. Publication novelty remains under separate primary-source scrutiny.

## Follow-up: natural policy, DCL, and effective-temperature objection

- **Reason for follow-up:** an engineered matched-value family could make count rescue look artificial. Removing the positive denominator term is a strong competing explanation based on known positive-negative coupling. Neither question is deferred to future work.
- **Derived before run:** theorem.md Sections8–9 prove the general offset threshold, T_DCL<T_InfoNCE, DCL count rescue, and a nonempty open natural-exponential parameter regime. For every t>1, rho can be chosen strictly between max{(e−1)/(exp(t)−1),T1/t} and 1/t; all-K full stability follows from the prior theorem.
- **Executed:** analytically selected omega=4^(−s), epsilon=.3 gives exact q=(.103,.187,.523), eta=.8302939489. Finite sums bracket the InfoNCE cutoff at K4/5 and the DCL cutoff at K7/8. Matched alpha−.9 DCL cutoff is K13/14, versus InfoNCE8/9. 512 control settings and 20 new d4 full-field checks, maximum adaptive error9.04e−11. Full commands, CSVs and JSON preserved. No exploratory numerical policy sweep was used to select the natural example.
- **Current interpretation:** positive-negative coupling shifts the boundary but is not the sole source of count dependence. Natural exponential policies support an open finite-count rescue regime when the uniform probability floor is nonzero. At zero floor and infinite K, natural exponential reweighting admits the elementary effective-temperature reduction; this is acknowledged and not counted as a contribution.
- **Largest remaining objections:** whether these exact results are sufficiently novel relative to adaptive sampling/performative and contrastive analyses; whether the unit-sphere lookup mechanism survives a shared neural encoder. Those are handled by separate literature and encoder agents. The K4 natural instability is weak and requires time-scale-aware dynamics checks.
- **Scope:** exact local population results; no global basin theorem, no claim of complete nonlinear factor erasure, no practical benchmark win. Resource shortage is not used as a rejection reason.
- **Status:** theory/results complete for the specified model; promising mathematical core pending synthesis with novelty and learned-encoder evidence.

## Final independent control audit

- The critic independently passed theorem.md Sections8–9, including the general-offset degeneracy exception, the natural-policy open regime, and epsilon inverse. Its separate ordered-tuple control finite differences had maximum discrepancy5.73e−11.
- It certified the natural InfoNCE4/5, natural DCL7/8, and matched DCL13/14 cutoffs with 70-digit outward intervals. Certificates and source are in round2/review/. The original matched InfoNCE8/9 boundary was independently certified there too. This improves explicit integer-cutoff evidence from floating-point illustration to computer-assisted strict brackets.
- Root executed full d4 near-equilibrium flow integrations with four independent arbitrary perturbation seeds for natural K4/K5, both frozen and adaptive (16runs). Its communicated balance ratios match exp(+3) and exp(−3) respectively, resolving the weak-K4-time-scale concern. Those independent runs remain in the root dynamics directory and are not counted as executions of this theory subtask.
