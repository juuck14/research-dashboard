# Independent check of the positive-graph stability window

2026-10-22. Read `../neural/view_theorem.md`, the actual `mixing.py`, `view_spectrum.py`, and saved window parameter results. This review checks mechanism and scope; repeating every finite difference would not add to its importance.

## V1: extra view directions

At a collapsed class, all positive first score derivatives vanish. For a unit-normalized normal perturbation `v_i`, every negative first score derivative also vanishes. Therefore adaptive sampling contributes no response term in those normal directions. The field derivative there agrees with the matched-frozen derivative. A claim that both ends of the proposed window are caused by sampler feedback would be false.

The expected reference Euclidean gradient is radial. Differentiating its sphere projection yields `lambda_plus/m` on a within-class tangent direction. The positive score coefficient is `-Btot*P/(4m)` before the two encoder branches are combined; the symmetric stochastic positive channel therefore contributes `-Btot*mu/(2m)` in its nonconstant eigenvector. This verifies the normal eigenvalue `[lambda_plus-Btot*mu/2]/m`.

In-plane view perturbations additionally change adjacent negative scores. Conditional zero mean of the view eigenvector removes cross-view products. The affected anchor class and its two adjacent classes together give `lambda_b/2` in the unnormalized quadratic form; dividing by its squared direction norm m yields the additional `lambda_b/(2m)`. This is consistent with the normal formula, reduces to the uniform-view result at mu0, and gives the identity-positive limit at mu1. No missing first-order positive response or policy normalization term was identified.

Class means see exactly the old four-state categories, with each view receiving1/m of the old gradient. Symmetry and uniform stationary view measure eliminate class/view cross terms. Thus the decomposition exhausts the full tangent dimensions. The symmetric-channel assumption matters; a general directed positive graph is not covered merely because it is connected.

## V2: why the upper count boundary is ordered

The tagged masses of score values z in `{B,A,1}` are proportional to `p(z)*z*f_(K-1)(1+z)`. Their normalized signed mean, with score values assigned signs−1,0,+1, equals xi_K. Adding an independent negative multiplies those masses by the increasing ratio `f_K(1+z)/f_(K-1)(1+z)`, because the Stieltjes expectation is strictly log-convex. Its covariance with the sign function is strictly positive. This verifies strict increase for positive u,v,w and hence an upper-count constraint from the positive graph gap.

The balance threshold supplies a lower-count constraint, while the view threshold supplies an upper one. Under the existing sufficient policy conditions, their intersection is exactly an integer interval of full local attraction, possibly empty or unbounded. This is not a re-entrant sign for a single mode. The old scalar mode theorem is not refuted by full stability disappearing again at large K.

The finite-sum interval certificate for K11/12 was inspected as an artifact, but this reviewer did not independently reimplement its arbitrary-precision arithmetic. The root owns that certificate audit. The algebraic monotonicity proof, rather than the K1–128 grid, supports the all-K interval statement.

## What the shared encoder test actually resolves

The saved three-seed parameter results have the predicted adaptive growth/contraction/growth at K4/8/16, while frozen K4 contracts and frozen K16 shares the view instability. The half-step check gives approximately.15% amplitude variation. These runs use the joint denominator, recompute the nonlinear gradient, permit every layer and view direction to move, and separate output rank from inertia. They address the old mismatch between a joint-K theorem and averaged one-negative MLP experiments.

The reference is deliberately constructed with semantic geometry, and its tangent Jacobian is surjective. The pullback/inertia relation is standard. This experiment therefore checks that no lookup-only or missing-view-mode artifact explains the local law; it does not establish that ordinary unlabeled training chooses this geometry. The ordinary warmup arm fails its applicability gate in all three fixed seeds and must remain visible.

## Contribution check kept separate

The graph spectral decomposition is established background. JMLR2025's augmentation-overlap theorem also uses connectivity and spectral quantities, while assuming epsilon-alignment of the encoder. The new candidate result concerns the local dynamical feasibility of a desired collapsed representation as count changes. It is neither a direct corollary nor a refutation of that conditional theorem.

The genuine candidate addition is the exact coupling of two count requirements with opposite monotonic directions, not the generic statement that positives attract and negatives repel. The full interval theorem still assumes four class centers arranged as a square. None of these results establish terminal semantic erasure or a downstream performance optimum.

## Wider normal-block theorem, read after the square proof

The subsequently available `../foundations/general_normal_graph.md` was read directly. For C score-regular class centers and m views, stationarity and symmetry of the negative score coefficients are explicit assumptions. A zero-class-mean perturbation normal to their entire span has zero first score derivatives. Its negative cross products cancel on averaging views, leaving radial contribution `-2*R_K/(Cm)`. The positive quadratic form is `2*B_K/(Cm)*(I-P)`. Their sum gives exactly `2/(Cm)*[B_K*(1-mu)-R_K]` and no sampler-response term. The same tagged-weight tilt proves strict increase of `R_K/B_K` for any fixed row score policy with at least two distinct scores. I found no algebraic defect in this generalization.

This theorem removes the square restriction for the normal block, but does not supply the other blocks or a full-stability window for an arbitrary geometry. Its explicit latitude example correctly prevents transitivity/identical score rows from being mistaken for a stationary representation: the remaining force need not be radial. Ambient dimension must also exceed the center span for this normal block to exist. The theorem's restrictions are therefore substantive and correctly preserved.
