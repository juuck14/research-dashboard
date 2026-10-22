# Round3 foundations: count, response, and geometric scope

**Current status: proved and numerically verified within a structured population model; publication-level importance still requires the fixed independent journal audit.** No GPU or external run is required for the results in this directory.

The four-state result alone was too narrow to establish a broad principle. We derived a score-distribution theorem for exchange-balanced affine directions under a uniform/exponential mixture policy and iid negatives. It proves a single possible count transition and an exact floor below which **no finite negative count** can stabilize that direction. The same proof applies to bounded continuous populations, and product spheres realize it without discrete score ties. A separate general normal-view theorem shows why more negatives can make augmentation mixing requirements harder. These are local directional statements; they do not prove global factor erasure.

## Read first

- [Multilevel law and proofs](multilevel_theorem.md): exact field, score crossing, Stieltjes MLR, all-finite-K rescue criterion, hypercube application.
- [Continuous population proof](continuous_population.md): product-sphere realization, exact moments, continuous two-factor check.
- [Normal-view graph theorem](general_normal_graph.md): general score-regular stationary geometries, opposite K ordering, stationarity counterexample.
- [Source audit](source_audit.md): what is inherited from single-crossing comparative statics, and what remains a contrastive-specific claim.
- [Protocol](protocol.md): comparisons and acceptance criteria recorded before each computation.
- [Progress and revision history](progress.md): what changed and why.

## Executed evidence

| Check | Observed result | Raw output |
| --- | --- | --- |
| Random multilevel laws,18432 settings | No forbidden sign transitions or subcritical positives | `results/random_curvatures.csv`, `summary.json` |
| Independent ordered-tuple gradient finite differences | Maximum absolute discrepancy1.40e-10 | `results/ordered_tuple_checks.csv` |
| Hypercube moment/tuple checks | Maximum discrepancy4.18e-11 | `results/hypercube_checks.csv` |
| Fixed-floor cube prediction | At eps.25 cutoff349 for m8; m16/32/128 analytically unrescuable | `results/fixed_floor_predictions.csv` |
| Continuous product-S2 score integration | Two resolutions differ by1.07e-15 | `results/continuous_curvatures.csv` |
| Independent continuous joint-factor tuple gradient | Maximum discrepancy5.89e-12 | `results/continuous_joint_tuple_checks.csv` |

For continuous product S2, t=log4, the exact floor is .24283216 at two factors and .25247163 at three. Therefore eps.25 is rescuable at m2 but cannot be rescued by **any finite K** at m3. At m2,eps.3, the numerically observed first positive count is11. The eps.25 m2 field remains negative through64 despite the theorem guaranteeing eventual rescue; it is not classified as impossible by the finite sweep.

## Reproduction

From the repository root, using Python3.11+ with NumPy and SciPy:

```bash
python -m pip install -r negative-feedback/round3/foundations/requirements.txt
python negative-feedback/round3/foundations/verify_multilevel.py
python negative-feedback/round3/foundations/hypercube_prediction.py
python negative-feedback/round3/foundations/continuous_check.py
```

Recorded environment: Python3.12.14, NumPy2.3.5, SciPy1.17.0. Runs are deterministic; the random-population generator uses seed33017. `verify_multilevel.py` completed in about5.4 CPU seconds in the current environment; timings are environment-dependent. The continuous checker and fixed-floor prediction are also CPU computations, not trained-model experiments. No checkpoints or external datasets are used.

The proof is exact. Saved decimals use deterministic adaptive Laplace/finite-score quadrature and Gaussian score integration; they are not directed-interval certificates. The counts at which tiny signs change are numerical brackets. Analytical impossibility and all-K ordering do not rely on extrapolating the finite sweep.

## Remaining decisive risks

The generalized law is not a new general MLR theorem. Its high-level proof principle appears in Athey1999, and the K-infinite floor is an effective-temperature curvature calculation. Top-journal value therefore rests on whether the exact finite-count classification, opposing spectral mechanisms, and nontrivial continuous realizations materially change understanding compared with the closest ML work. Full stability outside the square, generic asymmetric geometry, and global semantic harm are not proved here. These cannot be claimed as routine postprocessing of the present scalar result.

## Candidate new knowledge for the fixed journal audience

A reader already familiar with robust weighting, finite-batch gradient bias, and augmentation graphs would learn a conditional decision law rather than another example of biased sampling. For the declared easy-biased score-policy family, the population score/derivative law determines whether **any** finite negative count can stabilize a balanced factor-energy direction; it is not enough that more independent negatives reduce denominator effects. At the same time, a different normal-view block demands **more** positive-graph mixing as the count increases, giving competing lower and upper constraints even at stationary geometries with many score levels. Continuous factor products show that the first constraint is not a discrete-score coincidence. This would change the diagnosis from “the batch is too small” to an explicit distinction between a rescuable direction, an analytically unrescuable direction, and an augmentation-limited count range. Whether that local classification is important enough for JMLR still depends on the closest-work audit and the integrated paper's scope; no generic practical or global semantic conclusion follows from it alone.
