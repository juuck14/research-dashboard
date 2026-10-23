# Primary-source audit and exclusions from novelty

2026-10-23. This audit covers this branch's claims. Parent round5 also has a broader novelty/importance review. A setting difference is not treated as sufficient novelty.

## Awasthi, Dikkala and Kamath, ICML2022

**Do More Negative Samples Necessarily Hurt In Contrastive Learning?** [Official paper](https://proceedings.mlr.press/v162/awasthi22b/awasthi22b.pdf). Directly inspected §§2–3, Theorem3.8 and Claim3.9 in the16-page primary PDF.

Their data distribution is fixed: positives share a latent class, negatives come from the marginal. Under nonoverlapping equiprobable classes, the population NCE optimizer has simplex geometry independently of K. The proof uses class collapse, Gram averaging and convexity. Thus neither simplex optimality nor “increasing K need not degrade the optimizer” is this branch's new contribution. Our representation-dependent detached sampler is outside that fixed objective. The strongest candidate addition is a finite-count dynamic separation at the *same current uniform law*, together with fully supported, false-negative-free class-merging attractors. This does not contradict their theorem. Merely producing a poorer solution under a different fixed law would add insufficient knowledge.

## Jiang, Nguyen, Aeron and Ishwar, TMLR2025

**Hard-Negative Sampling for Contrastive Learning: Optimal Representation Geometry and Neural- vs Dimensional-Collapse.** [Publication PDF](https://openreview.net/pdf?id=3cnpZ5SIjU), [author HTML inspected](https://arxiv.org/html/2311.05139v2). Publication metadata/search-indexed primary PDF identifies April2025. Direct access to the final OpenReview PDF encountered a verification wall; the inspected complete author HTML has the v2 URL, and byte identity with the final journal version is **not asserted**.

Inspected §3.2 Definition2, §4 Theorem2/Corollary2 and §5. Their hardening function is nonnegative and argument-wise nondecreasing; the exponential example uses positive hardness. They establish optimal simplex geometry for supervised/hard-supervised objectives and analyze dimensional collapse empirically, including normalization and optimization effects. Our decreasing exp(−t s) policy is outside this hypothesis. Their paper already prevents a novelty claim based solely on “negative selection affects rank” or “simplex optimum can differ from learned geometry.” The candidate difference must remain the exact finite-K feedback/common-law separation and a proven attracting class-merging mechanism under nonzero support and correct negatives. Whether that difference is important requires the parent's substantive review, not a claim that their equation omits ours.

## Results deliberately not presented as independent novelty

1. Simplex packing maximizes the worst-case class radius. The elementary sum-of-distances identity is included to justify the metric, not claim a new packing result.
2. The zero-floor infinite-K field has an effective fixed exponential energy. Its balanced-antipodal global minimum follows from an endpoint chord and Jensen. This is an inherited reduction plus standard inequalities.
3. Graph/block diagonalization, reciprocal-moment monotonicity and normal-attraction theory are standard tools. Their specialization is useful for the all-K attractor statement, not automatically top-journal novelty.
4. A feedback field need not be conservative. The exact Gram counterexample excludes a proposed universal fixed-energy explanation; nonzero curl itself establishes neither harm nor scholarly importance.
5. Rank deficiency, feature selection tradeoffs, temperature effects and false-negative damage are known broad phenomena. The no-self/correct-negative model specifically removes the last explanation; it does not make the remaining statement unprecedented by assertion.

## Precise applicability limits

The proof uses an even number of equally weighted finite classes, unit-dot-product scores at loss temperature1, iid negative draws with replacement, an exponential easy-negative mixture, a fully expressive representation space, and a class-consistent symmetric positive channel. The exclusion mask is supplied by the finite problem's positive components. There is no theorem here about arbitrary adaptive or hard-negative policies, general neural optimization, unknown class masks, natural images, finite stochastic-gradient trajectories, or all random initializations. None of those results has been inferred from the numerical checks.
