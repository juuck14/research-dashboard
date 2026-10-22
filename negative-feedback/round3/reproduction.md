# Reproducing the round3 results

Run from the repository root in a separate checkout: scripts overwrite their declared output files. No external dataset, GPU or private page is required. The saved results were executed with Python3.12.14; dependencies are pinned in requirements.txt. Tiny last-digit BLAS/solver differences are expected. Signs with directed certificates and analytic theorems do not depend on those last digits.

```bash
python -m venv .venv
. .venv/bin/activate
python -m pip install -r negative-feedback/round3/requirements.txt
export OPENBLAS_NUM_THREADS=1
export OMP_NUM_THREADS=1
```

## Minimal scientific audit

```bash
python negative-feedback/round3/foundations/verify_multilevel.py
python negative-feedback/round3/foundations/hypercube_prediction.py
python negative-feedback/round3/foundations/continuous_check.py
python negative-feedback/round3/neural/validate_oracle.py
python negative-feedback/round3/neural/certify_mixing.py
python negative-feedback/round3/review/window_certificate_check.py
python negative-feedback/round3/correlation/certify.py
python negative-feedback/round3/journal/zero_self_cycle_certificate.py
```

These CPU scripts check the formulas, continuous realization and certified signs. They cannot substitute for reading the proofs: a grid with no violation is not an all-K proof. The independent window certificate uses exact Fraction arithmetic and its own e/log4 series without importing the author's interval arithmetic.

## Actual dynamics, alternative explanations and failure arms

```bash
python negative-feedback/round3/endpoints/run.py
python negative-feedback/round3/endpoints/flow.py
python negative-feedback/round3/review/endpoint_check.py
python negative-feedback/round3/correlation/run.py
python negative-feedback/round3/review/correlation_check.py
python negative-feedback/round3/neural/check_parameter_gradient.py
python negative-feedback/round3/neural/view_spectrum.py
python negative-feedback/round3/neural/graph_check.py
python negative-feedback/round3/neural/mixing.py
python negative-feedback/round3/neural/shared_parameter.py
python negative-feedback/round3/neural/window_parameter.py
python negative-feedback/round3/neural/standard_ode_check.py
python negative-feedback/round3/neural/ordinary_warmup.py
python negative-feedback/round3/neural/ordinary_weak_positive.py
python negative-feedback/round3/neural/cycle_no_self.py
python negative-feedback/round3/review/cycle20_certificate_check.py
python negative-feedback/round3/review/standard_ode_recheck.py
python negative-feedback/round3/neural/plot_results.py
```

The [neural reproduction guide](neural/reproduction.md) gives output-level acceptance checks and measured timings. The joint-K MLP window arm took26.55s and the last weak-positive ordinary arm8.70s on the recorded machine; these are observations, not portable runtime guarantees. The full endpoint solves take additional CPU time. There is no unexecuted essential GPU arm.

`endpoints/flow.py` preserves primary seeds9301–9303 and confirmation9501–9503. Its reported `time` is **ODE model time**, not wall-clock runtime. The square-neighborhood test is not a random-global-initialization study. Neural oracle-reference seeds4101/4102/4301 and ordinary seeds3801/3802/3901 are separate. The second weak-positive scope arm reuses ordinary seeds after the reviewer request and is explicitly not a new held-out confirmation.

## Data-to-claim map

| Claim | Proof | Main executed evidence |
|---|---|---|
| Finite-count rescue iff Q>0; no re-entry | foundations/multilevel_theorem.md | foundations/results/summary.json, ordered_tuple_checks.csv |
| No atomic-score-tie requirement | foundations/continuous_population.md | continuous_summary.json, continuous_joint_tuple_checks.csv |
| Required normal positive gap strictly increases | foundations/general_normal_graph.md | neural graph_fd.csv and general proof |
| Full square/view window5..11 | neural/view_theorem.md plus round2/theory/theorem.md | mixing_interval_certificate.json, review/window_certificate_check.json |
| Same joint-K shared-parameter local predictions | neural/view_theorem.md plus declared pullback assumptions | window_parameter_summary.json, standard_ode_check.json |
| Ordinary reference applicability fails | No global claim | ordinary_summary.json, weak_ordinary_summary.json, all runs/traces |
| OldK4 boundary does not establish information erasure | endpoints/coarse_cluster_lemma.md and interior-injectivity argument | branches.csv, flow_summary.json, review/endpoint_check.json |
| Pairwise law and unique-set law insufficient outside iid | correlation/README.md | rational_certificate.json, review/correlation_check.json |

## Provenance and dependencies

Round3 is incremental research. Its scripts intentionally import the saved round2 exact population moment, tangent and interval utilities by relative paths. Clone the **whole repository**, not just this directory. Those prerequisites are unchanged; see [the earlier reproduction file](../round2/reproduction.md). A clean environment requires the pinned NumPy/SciPy/Matplotlib versions or compatible equivalents; the code does not require PyTorch.

The final manifest records byte-level SHA256 and Git blob IDs. CSV line endings are preserved. Rerunning a script may change wall-clock fields or platform metadata, so raw bytes need not be identical after rerunning; formula values and declared tolerances are the scientific checks. The manifest is for the delivered snapshot, not a promise of bitwise cross-machine training identity.

## Delivered snapshot re-execution

```bash
python negative-feedback/round3/audit_snapshot.py
```

This executed audit copies the topic and its round2 dependencies to a temporary directory and reruns14decisive scripts without changing the delivered raw data. All14exit codes were0 and five saved numerical/certificate bundles matched. See [audit_snapshot.json](audit_snapshot.json). This is reproducibility QA, not another scientific contribution.
