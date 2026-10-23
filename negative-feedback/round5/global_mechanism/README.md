# Global mechanism branch — actual class-merging attractors

2026-10-23. This branch replaces the rejected interpretation of the old square instability with a different, explicitly declared model and an actual classification consequence. It supplies the **bad-attractor half** of round5's fixed-law/simplex versus adaptive-law separation. It does not independently certify JMLR importance or “50% complete.”

## What was established

- **Direct proof:** For every even class count C>=4 and every finite negative count K, an easy exponential sampler with t=log4 and epsilon.05 admits an open basin of balanced antipodal class-merging representations. All negative candidates are different classes and have positive sampling probability. There is enough representation dimension for an injective simplex.
- **Exact scope:** The proof gives a local basin for each finite K, not global convergence, basin probability, K-uniform basin size, or a K-uniform rate. Its coarse-point matched frozen law is also stable. Feedback specificity instead comes from the parent's common-law comparison at the task-optimal simplex.
- **Learning meaning:** The limiting attractor identifies C classes with two points, so even nonlinear class identification is bounded by2/C. The limiting worst-case prototype robustness radius is0. Finite tiny differences are not called exact information loss.
- **Actual trajectories:** Twelve prespecified Gaussian-start adaptive runs reached balanced antipodal neighborhoods; the same twelve starts with the exact simplex-matched fixed uniform law reached simplexes. Four swap-positive adaptive runs and their four fixed-law controls retained this difference with no self positives or same-class negatives.
- **Independent adversarial check:** The independent critic rederived the full prototype/view spectra and all-K floor algebra. See [its multiview audit](../critic/multiview_proof.md). This checks correctness, not scholarly importance by agreement.

The self-contained derivation, assumptions and scope are in [global_collapse.md](global_collapse.md). [alternative_routes.md](alternative_routes.md) preserves the failed standalone novelty routes: effective-temperature global collapse is elementary after the energy reduction; nonintegrability alone supplies no important learning conclusion. [source_audit.md](source_audit.md) identifies what the closest sources already establish and what was actually read.

## Numerical results

| Arm | Actual configurations | Result | Raw evidence |
|---|---|---|---|
| Prototype adaptive | C4/8 × K1/8/32 × seeds7301/7401 |12/12 balanced antipodal; maximum RMS1.852e-7|[CSV](collapse_runs.csv), [summary](collapse_summary.json), [embeddings](collapse_embeddings.json), [trace](collapse_traces.json)|
| Prototype uniform fixed | Same twelve starts and caps |12/12 ETF; maximum Gram relative error3.745e-7|[CSV](uniform_control.csv), [summary](uniform_summary.json), [embeddings](uniform_embeddings.json)|
| Step control | C8,K32,seed7401,step1 instead of2 |Same attractor, RMS2.945e-8|[adaptive summary](collapse_summary.json), arm halfstep|
| Prototype full tangent Jacobian |C4,d4,K1/8/32,frozen/adaptive|max eigenvalue error4.30e-11|[coarse_fd.json](coarse_fd.json)|
| Swap-positive adaptive |C4,2views,d8,K8/32,seeds7301/7401|4/4 class-merging; max RMS4.721e-8|[summary and embeddings](nonidentity_summary.json)|
| Swap-positive uniform fixed |Same four starts and caps|4/4 class ETF; max Gram error1.891e-14|[summary and embeddings](nonidentity_uniform_summary.json)|
| Swap-positive full tangent Jacobian |56 tangent directions,K1/8/32,frozen/adaptive|max eigenvalue error3.83e-11|[full-spectrum checks](nonidentity_summary.json)|

Prototype robust radius under fixed law is about.81649658(C4) or.7559289(C8), versus at most5.698e-8 under paired adaptive updates. This radius was added as a **post-collapse diagnostic**, not a preregistered discovered metric. The original success criterion and every amendment are preserved in [collapse_protocol.md](collapse_protocol.md). Final64-versus96-node Laplace differences were at most1.12e-16 in these arms; this is a numerical consistency check, not a proof of quadrature accuracy globally.

## Reproduction

Recorded runtime: Python3.12.14, NumPy2.3.5, SciPy1.17.0. The scripts are CPU-only. From the repository root:

```bash
python -m pip install numpy==2.3.5 scipy==1.17.0
python negative-feedback/round5/global_mechanism/check_collapse.py
python negative-feedback/round5/global_mechanism/check_uniform_control.py
python negative-feedback/round5/global_mechanism/check_nonidentity.py
python negative-feedback/round5/global_mechanism/check_nonidentity_uniform.py
```

The fixed-policy scripts depend on the preceding adaptive output for paired diagnostics. Both prototype and multiview scripts reuse the preserved [Laplace expectation oracle](../../round3/neural/oracle.py); this dependency is explicit. The independent critic uses an ordered-tuple implementation. Scripts overwrite only this branch's generated result files. Seeds7301(primary) and7401(confirmation), the stopping rule, step and cap are in code and protocol. Runtime fields can change on reproduction; scientific values should agree within the stated tolerances.

Auxiliary route reproduction:

```bash
python negative-feedback/round5/global_mechanism/check_potential.py
python negative-feedback/round5/global_mechanism/check_potential_off.py
python negative-feedback/round5/global_mechanism/certify_nonpotential.py
```

The [integrability protocol](protocol.md), [self-included raw CSV](potential_checks.csv), [no-self raw CSV](potential_off_checks.csv), [exact rational certificate](nonpotential_certificate.json) and [alternative analysis](alternative_routes.md) retain all diagnostic cases, including zero obstructions. These diagnostics are exclusions, not evidence of important harm on their own.
