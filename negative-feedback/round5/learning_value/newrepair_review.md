# Independent review of the revised simplex-optimum / class-merging center

2026-10-23. This review follows a separate parent task after the old square-quality route was rejected. The old analysis and rejection are preserved. I inspected the actual new theorem files, source and saved data, then independently recomputed the metric below. This is not a vote based on the author's preference.

## 1. What I actually checked

- `../theory_value/theory.md`: the task-symmetric affine risk, the frozen-risk simplex optimum argument, filtered shape calculation and coarse Bayes consequence.
- `../theory_value/filtered_full_spectrum.md`: the complete simplex tangent decomposition for arbitrary local positive omega and temperature, including the fixed-law comparator and sufficient count threshold.
- `../global_mechanism/collapse_protocol.md`, `check_collapse.py`, saved adaptive and uniform embeddings/summaries: true-negative-only model, nonzero floor, identical starts, stopping rules and finite-time qualification.
- `../global_mechanism/check_nonidentity.py` and the two nonidentity summaries: positive pairs are different views and every negative excludes the full anchor class. The nonidentity full coarse spectrum is independently checked elsewhere by the critic; I inspected the source and actual endpoints rather than reinterpreting prototype-only evidence as a multiview proof.
- My own `check_newrepair.py` recomputes interclass distances directly from the arrays, without importing the parent's radius implementation.

## 2. The old task-meaning objection is genuinely repaired

For class-indexed prototype sets F_c, define the supremal common feature-perturbation radius for which **some decoder can classify every class correctly**. It is

\[
r_*(F)=\tfrac12\min_{c\ne d}\|F_c-F_d\|.
\]

Any radius strictly below this value is attained by nearest-prototype classification. Above it, the two closest classes have intersecting perturbation balls, so no decoder can be correct for every permitted perturbed observation. This includes nonlinear decoders. Boundary inclusion depends on whether balls are open or closed; the supremum is unchanged.

For multiple observations per class, take the minimum over interclass pairs and ignore within-class pairs. Nearest-prototype with class labels still attains every smaller radius. The proof does not require the representation to be one point per class, and two positive views collapsing together is not an error.

For C unit prototypes,

\[
r_*^2\le\tfrac14\operatorname{Avg}_{c<d}\|f_c-f_d\|^2
\le \frac C{2(C-1)}.
\]

The first inequality is min≤average; the second follows from the nonnegativity of the squared centroid norm. Equality requires all pair distances equal and the centroid zero, so the regular-simplex Gram uniquely attains the bound when the ambient dimension permits it. This is the standard simplex/Rankin coding argument, not a new research contribution.

Unlike the old balanced square, this target does not privilege named binary coordinates. No Gaussian noise scale, class-task weights, regularizer or linear-probe limitation must be selected. Its desired distinctions are already present in the learning information: the filtered sampler regards every other class as a correct negative. A representation merging different such classes demonstrably fails to preserve an observed distinction. This is a much stronger justification than naming one factor “semantic” and another “nuisance.”

Therefore the revised class-ID question resolves the previous core objection **why this geometry is worth maintaining**. It does not prove that worst-case feature robustness is the only useful task or that natural-image generalization follows. It supplies an independently meaningful, permutation-invariant objective whose degradation is not an artifact of the old probe/task choice.

## 3. Actual metric audit

I evaluated all12paired prototype endpoints and all4paired nonidentity-positive endpoints supplied by the completed, fixed configurations. The largest adaptive robust radius was5.70e-8. Every uniform control achieved at least.999999875 of the relevant unit-norm simplex bound. The arrays, not rounded rank labels, supplied these values. See `results/newrepair_radii.csv` and `results/newrepair_summary.json`.

This is a finite robustness contrast. I do **not** call the finite arrays exactly non-injective. A very small coordinate may retain noiseless class information. Exact information loss belongs to the proved limiting class-merging attractor; for C balanced classes its class-ID Bayes accuracy is at most2/C, regardless of decoder. For any fixed positive feature-perturbation radius, a trajectory actually approaching the coarse point eventually loses the uniform robust classification guarantee. No favorable noise magnitude needs to be chosen after viewing the data.

The two-view control specifically addresses the identity-positive objection. It is not a claim of shared-network training or arbitrary augmentations. The prototype frozen-risk global optimum proof and the multiview numerical controls should remain distinct unless the paper separately proves the corresponding multiview global-optimum statement.

## 4. Why the revised contribution differs from the rejected rescue

The old paper asked whether a selected square stays stable, although a different injective geometry could be as good and the square itself omitted one balanced linear task. The new chain is:

1. The simplex is independently optimal for robust class-ID spacing, and is the unique global Gram optimum of the target's matched frozen InfoNCE risk.
2. At that target the adaptive and frozen samplers have **identical actual negative probabilities**, but their response derivatives differ. The new full spectrum determines when the optimum is repelling for every finite count.
3. There is also an analytically attracting class-merging geometry under a positive floor, with correct negatives and sufficient dimension. Its exact limit loses observed class distinctions for every decoder.
4. Fixed random starts in the controlled finite model approach the bad neighborhood under the updating policy and the simplex under the fixed target law. Nonidentity positives are separately controlled.

This explains something that the old window-as-quality argument did not: a static-risk target and its task benefit can be valid, while the associated adaptive sampling process fails to maintain it and can reach a genuinely harmful representation. The harmful geometry is not inferred from a merely negative eigenvalue.

Coarse stability alone is not feedback-specific: its first score derivatives vanish, so its local response term vanishes too. The relevant feedback separation is at the **shared desirable target**, and the trajectory changes in the negative law matter. The parent source correctly distinguishes the target-matched uniform frozen control from freezing the random initial policy.

## 5. Remaining strongest objections and their disposition

| Objection | Review result |
|---|---|
| The target is chosen to make the old square look good. | Resolved: the target is now simplex, and the old square-quality route remains rejected. Class-ID robust coding is independent of its stability. |
| A different readout or task weighting rescues the merged representation. | Resolved for the exact limit and robust class-ID property: no decoder separates coincident classes; no named-bit weighting is used. |
| Tiny finite coordinates were rounded away to claim erasure. | Avoided: finite results are robust-radius contrasts; information claims are limiting ones supported by the attractor theorem. |
| Bad collapse comes from false negatives or identity positives. | Removed in declared controls: filtered candidates are other classes, and the two-view swap-positive case also collapses. |
| More negatives may eventually repair the same target. | The supplied general target theorem treats all finite counts under its declared derivative condition; it is not inferred from K1/8/32 alone. |
| Nonzero sampling support should prevent the failure. | The controlled theorem and actual data show an open positive-floor failure regime under the stated normalized geometry. This is not a claim about all floors or samplers. |
| The result is already known, or the remaining novelty is not JMLR-level. | Not adjudicated by this task-meaning audit. Performative mismatch, weighted repulsion and feature-collapse precedents require the independent primary-source comparison. Correct utility and true harmful attraction cannot substitute for that novelty judgment. |

## 6. Verdict

**The specific importance gap I was assigned—the arbitrary quality interpretation of the old stability point—is repaired by the new center.** It is repaired by a different, independently justified target and an actual destructive attracting outcome, not by weakening the old claim or adding more validation rows.

I would support continuing the revised optimum-destabilization contribution through the fixed final novelty/importance review. I do not automatically certify top-journal core50 from this audit alone: the decisive remaining judgment is whether the proved all-count/full-support/correct-negative separation adds sufficiently nontrivial knowledge beyond the closest adaptive-negative and performative results. If the independent comparison establishes that novelty, the current utility connection does not require an additional favorable downstream benchmark to exist. Natural-data generality would be an additional claim, not silently supplied by these finite models.
