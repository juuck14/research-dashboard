# Independent mathematical and implementation audit

Recorded 2026-10-22 before executing the independent checks here. The proposed formulas and their author's numerical output were read first. This is a verification protocol, not a discovery preregistration.

## Scope and acceptance criteria

1. Rebuild the detached expected gradient using **ordered iid negative tuples**, independently of the author's multinomial aggregation. Test K=1,2,3,4,5; exact expectation, no Monte Carlo.
2. Obtain the complete product-sphere tangent Jacobian by finite differences of that expected gradient. Use d=4, h=1e-5 and 3e-6; alpha=-1.5,-.9,0. Exact field zero requires residual <1e-12. All twelve eigenvalues must match the proposed spectrum within 2e-7.
3. Independently enumerate three-category moments using Python integer multinomial coefficients. Verify factor-mode threshold at K=8,9 and retain numeric sign margins. These finite checks establish no claim for all K without a proof.
4. Prove or refute the inverse-moment ratio monotonicity. Explicitly separate a deterministic shift from an independent random shift; check size-bias indexing K versus K-1.
5. Distinguish factor-mode stability from complete tangent stability. Audit the all-K signs of the remaining modes, or mark that extension unproved.
6. Check the selected w_alpha is positive and nonincreasing on the allowed cosine interval, and that all policies have the same square sampler values. Check the policy derivative rather than differentiating the composed risk (which would be a different algorithm).
7. Optionally audit the hard quantile rule separately. It is discontinuous and cannot inherit the smooth Jacobian proof.

Any mismatch above is reported immediately. Finite-difference and floating-point agreement count as numerical verification; algebraic statements require a proof. All claims remain scoped to uniform four-state lookup embeddings, unit norm, identity positives, temperature one, and iid sampling with replacement. No encoder or real-data generality is inferred here.
