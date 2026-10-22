# Reproduction

Run from the repository root. No GPU, torch, external data, model downloads or checkpoints are required. Keep the prior `negative-feedback/round2/theory/code/` and `round2/review/certify_cutoff.py`: they supply the old class-mean formula and reviewed interval arithmetic. All new scientific changes stay in this directory.

Observed environment: Python3.12.14,NumPy2.3.5,SciPy1.17.0,Matplotlib3.10.8. See [environment.json](results/environment.json). Requirements versions describe the executed environment, not proof that other versions fail.

```bash
python -m venv /tmp/negative-window-env
source /tmp/negative-window-env/bin/activate
python -m pip install -r negative-feedback/round3/neural/requirements.txt
export OPENBLAS_NUM_THREADS=1
python negative-feedback/round3/neural/validate_oracle.py
python negative-feedback/round3/neural/check_parameter_gradient.py
python negative-feedback/round3/neural/view_spectrum.py
python negative-feedback/round3/neural/shared_parameter.py
python negative-feedback/round3/neural/ordinary_warmup.py
python negative-feedback/round3/neural/ordinary_weak_positive.py
python negative-feedback/round3/neural/mixing.py
python negative-feedback/round3/neural/certify_mixing.py
python negative-feedback/round3/neural/graph_check.py
python negative-feedback/round3/neural/cycle_no_self.py
python negative-feedback/round3/neural/window_parameter.py
python negative-feedback/round3/neural/standard_ode_check.py
python negative-feedback/round3/neural/plot_results.py
```

Scripts write their declared files under `results/` and `figures/`; reruns replace those files, so preserve a checkout or copy before independent auditing. Embedded seed/configuration lists are fixed and also described in [protocol.md](protocol.md). No favorable subset selection or external randomness is needed. Dependency installation requires available package network access or preinstalled wheels; the current run used already installed libraries.

## Outputs and pass conditions

| Script | Main raw outputs | Executed check |
|---|---|---|
|validate_oracle.py|oracle_validation.json|quadrature/enumeration/finite-difference errors below1e-7|
|check_parameter_gradient.py|parameter_gradient_check.json|20scalar-loss parameter differences, abs<1e-6 and rel<1e-5 for nontrivial derivatives|
|view_spectrum.py|view_spectrum.csv/json|full class/view decomposition, all added directions|
|shared_parameter.py|parameter_spectrum/trajectories.csv,parameter_summary.json|full output rank, direct pullback agreement, K4/5actual dynamics|
|ordinary_warmup.py|ordinary_runs/traces.csv,ordinary_summary.json,ordinary_final_embeddings.json|scope test;0/3applicable is retained, not an execution failure|
|ordinary_weak_positive.py|weak_ordinary_runs/traces.csv,weak_ordinary_summary.json,weak_ordinary_final_embeddings.json|reviewer-triggered weak-positive scope test;0/3applicable retained;endpoint ordering exploratory|
|mixing.py|mixing_curve/fd.csv,mixing_summary.json|fixed rho grid/full spectra agreement<1e-7|
|certify_mixing.py|mixing_interval_certificate.json|70-digit outward xi11<.05<xi12|
|graph_check.py|graph_fd.csv,graph_summary.json|cycle/path full spectra agreement<1e-7|
|cycle_no_self.py|cycle_no_self.json|N80 zero-self-loop cycle,4normal-direction FD checks;full 560D spectrum analytic only|
|window_parameter.py|window_parameter_spectrum/trajectories.csv,window_parameter_summary.json|K4adaptive/K16both expand>10,K4frozen/K8both contract<.15;halfstep discrepancy<1%|
|standard_ode_check.py|standard_ode_check.json|unpreconditionedDOP853 final exp3 discrepancy<1%|
|plot_results.py|figures/threePNG+PDFpairs|renders actual preserved data, no new experiments|

Observed single-thread executions: ordinary uniform-positive scope test8.85s,weak-positive scope test8.70s, first shared-parameter arm about16s, new window arm26.55s, unpreconditioned DOP8531.3s total for its two integrations. These are measured current-machine times, not GPU estimates. Population quadrature and full Jacobian checks have their own additional CPU costs. Rerun runtime depends on BLAS/threading/hardware. Outputs are small; no checkpoints or datasets are written.

## Independent audit order

1. Check `oracle.py` against independent `direct4` enumeration before interpreting spectra.
2. Reconstruct `view_theorem.md` without relying on numeric agreement; check sampler detachment versus vector-field response.
3. Independently check the monotone tagged-weight proof and exact K11/12 interval signs; a numeric K128 sweep is not an all-K proof.
4. Inspect full tangent rank, stationary residuals and directional finite differences before interpreting parameter modes.
5. Read all ordinary failures and the post-result solver diagnostic, not only successful constructed-reference figures.
6. Compare the exact classification with closest positive-graph and finite-negative originals; this is essential to publication-level judgment, not an implementation test.
