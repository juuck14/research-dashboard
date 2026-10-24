# Independent recovery execution

2026-10-25. These are **new executed outputs**, replacing lost unpublished raw checks. They are not the original October23 file bytes. The protocol was written before this execution, all cases/tolerances were fixed, and no scientific author implementation was imported.

`OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python negative-feedback/round5/recovery/independent_check.py` completed successfully with Python3.12.14, NumPy2.3.5 and SciPy1.17.0. The complete new raw values are in [independent_check.json](independent_check.json) and [independent_cases.csv](independent_cases.csv).

| Independent comparison | Observed maximum error or minimum slack |
|---|---:|
| Direct ordered-tuple beta versus tagged beta | max1.39e−16 |
| Pointwise beta−rho*pi | min.0142893 |
| Quantitative tilted-score inequality | min.000287598 |
| Centroid/Gram identities | max1.11e−16 |
| Stress trace identities | max2.22e−16 |
| Exact coarse graph spectrum versus assembled stress | max1.67e−16 |
| Closed-loop unused-normal derivative versus2H | max2.96e−13 |

The216 general geometries use two nonlinear weight families with analytic global easy budgets .85/.9. All prescribed finite-count, residual-mass, tilt and geometry tests passed the fixed tolerances. These random geometries are not assumed stationary, and no final stable-equilibrium bound is applied merely because a random point was generated.

## Stationary coarse controls

With omega=exp(−.9s), floor.01 and temperature1:

| C | K | Coarse stress PSD? | Off-Gram MSE | M/K bound | Interpretation |
|---|---:|---|---:|---:|---|
|4|1|yes|.888889|101.3455|Bad stable point allowed; bound vacuous |
|4|8|yes|.888889|12.6682|Coarse and simplex both locally stable |
|4|16|no|.888889|6.3341|Unstable merger; stable-point premise fails |
|4|4096|no|.888889|.024743|Unstable merger, so theorem does not assert this Gram satisfies the stable-point bound |
|6|1|yes|.960000|121.6146|Bad stable point allowed; bound vacuous |
|6|8|yes|.960000|15.2018|Coarse and simplex both locally stable |
|6|16|no|.960000|7.6009|Unstable merger |
|6|4096|no|.960000|.029691|Unstable merger |

K2 controls are also preserved in the raw output. Rotation zeros produce tiny signed floating-point values and are interpreted at tolerance. The separate twelve normal-direction differences recompute the sampler after perturbation; their agreement with2H independently checks the closed-loop response argument rather than freezing it by implementation.

These tests support the correctness of the separately proved global coefficient/certificate calculation. They do not enumerate every equilibrium, prove the all-C/all-K theorem numerically, establish global trajectory convergence, or make a journal-importance judgment by their count.
