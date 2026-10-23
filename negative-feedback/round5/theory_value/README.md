# Theory route: justified target, failed square repair, simplex response

2026-10-23. The original square-as-universal-target repair fails under a natural class-permutation-invariant task family. The resulting derivation identifies a meaningful regular-simplex target and an exact adaptive instability law, now for arbitrary positive C² score weights and any positive loss temperature. Publication-level novelty is not decided by this branch alone.

- [Protocol and pivot record](protocol.md).
- [Task risk, global frozen optimum, shape derivation, coarse Bayes risk](theory.md).
- [Complete filtered-simplex tangent spectrum and proof](filtered_full_spectrum.md).
- [Closest original papers and inherited arguments](source_audit.md).
- [Code](check_theory.py), [summary](results/summary.json), [all risk comparisons](results/population_risk.csv), [complete spectrum checks](results/filtered_full_spectra.csv), [general policy/temperature checks](results/general_omega_tau_spectra.csv), [coarse Bayes costs](results/coarse_bayes.csv).

## Exact results

1. For uniform balanced class tasks and isotropic noisy observation, average optimal affine MSE is an exact function of the full centered class Gram spectrum. A regular simplex is uniquely optimal for every positive noise level in sufficient dimension. This is standard linear-estimation/spectral reasoning, used to justify the target rather than claimed as new theory.
2. The same frozen correct-negative policy has a unique global simplex Gram optimum. This is a direct convexity/symmetrization application of known ETF geometry.
3. With no same-class negatives, every score sampler has the same uniform-off law at the simplex. Its update response depends on eta=−tau(1−epsilon)(log omega)'(−1/(C−1)). Entire-product-sphere strict attraction holds exactly when eta<1−a/(1+Ka), a=exp(−C/((C−1)tau)). All finite counts fail when eta≥1. The proof includes every tangent mode and all rotation/null directions, for C≥4,d≥C−1.
4. If a two-group coarse attractor is established by another branch, average **unrestricted nonlinear** noiseless Bayes MSE on the same tasks is(C−2)/(C−1), versus0at an injective simplex. This is a real distinction cost, not just a named-factor or restricted-probe artifact. Exact information loss concerns the limiting representation; finite-time near-collapse can stay injective.

## Executed checks

Exact per-task regressions match the spectral identity to3.89e-16. Independent ordered-tuple field derivatives match the shape law to4.06e-11. The full filtered spectrum matches every numerical tangent eigenvalue in36cases to3.84e-11; another24nonlinear-policy/temperature cases match to1.77e-11. Coarse-task enumeration matches the unrestricted Bayes formula exactly. These numbers verify implementation, not importance.

Run from repository root:

```bash
OPENBLAS_NUM_THREADS=1 python negative-feedback/round5/theory_value/check_theory.py
```

Python3.12, NumPy2.3.5, SciPy1.17.0. No datasets, GPU, model training or external run required. The script writes only this branch's result CSV/JSON files. The first implementation's collapsed-feature centering residue was corrected and recorded in theory.md; no scientific setting was retuned.

## Current branch decision

Do not defend the old square as task-universally desirable: that route is contradicted by the completed risk optimization. The simplex-response route is a substantive candidate repair because its target is independently justified and its filtered policy law is identical at that target for all samplers. It is still not enough to call a top-journal paper successful from a local coefficient: the parent's all-count bad-attractor, actual learning and independent prior-art attack must determine whether a complete, important new separation survives. This branch provides completed mathematical parts, not an unexecuted research plan.
