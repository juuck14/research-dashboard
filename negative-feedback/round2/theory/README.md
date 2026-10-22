# Arbitrary-count policy feedback: completed theory and checks

**Current status: derived and independently numerically verified.** Publication novelty/significance is assessed at the round2 synthesis level; no generic distribution-response chain rule is claimed as new here.

## Main result

A finite four-state, two-bit representation model admits an exact **full product-sphere tangent spectrum for every negative count K**, not only a tied angle. For smooth positive detached score-based samplers, factor balance is controlled by an effective local sampling slope eta and an exact threshold T_K. This threshold strictly increases with K to one. Explicit sufficient conditions make its sign the complete transverse stability criterion.

A natural filter `omega(s)=4^(−s)` with probability floor epsilon=.3 has the same policy at every count, yet its square is unstable for K≤4 and stable modulo rotations for every K≥5. Under a decoupled denominator the cutoff is K=8. A separate family of smooth monotone filters induces **exactly the same square q and exactly the same matched-frozen objective** but has opposite adaptive stability, isolating policy response from frozen objective geometry.

These are local lookup-model results. They neither show nonlinear information erasure nor establish practical learned-encoder generality. The natural example's K4 instability is weak and can require long trajectory times to observe. The probability floor and unit-norm geometry are mathematically active conditions.

## Artifacts

- [theorem.md](theorem.md): full spectrum; monotone-ratio proof; all-K full-sphere stability criterion; matched-value construction; DCL/general-offset extension; open natural-exponential regime; exact contribution boundary.
- [protocol.md](protocol.md): fixed original numerical design, and separately recorded analytic follow-up controls before execution.
- [progress.md](progress.md): work/result/criticism record.
- [results/summary.json](results/summary.json): 512 matched-policy settings, full-field finite-difference checks, and count-aggregation checks.
- [results/denominator_summary.json](results/denominator_summary.json): 512 natural/matched and InfoNCE/DCL control settings.
- [results/count_stability.pdf](results/count_stability.pdf): scientific figure from executed CSVs. SVG and PNG also available.
- Full CSV outputs are in results/. Independent ordered-tuple and interval audits are maintained by the cross-review agent in round2/review/.

## Reproduce

From the research-dashboard repository root, with Python, NumPy, SciPy and Matplotlib:

```bash
OPENBLAS_NUM_THREADS=1 python negative-feedback/round2/theory/code/verify_general.py
OPENBLAS_NUM_THREADS=1 python negative-feedback/round2/theory/code/verify_controls.py
python negative-feedback/round2/theory/code/plot_results.py
```

No GPU, data downloads, checkpoints, optimizer, or Monte Carlo samples are used. Count moments require only O(K²) finite multinomial states; full-field finite differences independently use four-category count distributions. Finite-difference errors below 1e−10 support the algebra, while all-K conclusions follow from proofs rather than extrapolation from K≤128. The second script imports count enumeration utilities from the first.

## Claims to retain and reject

Retain: same frozen law does not determine adaptive restoring behavior; there is an exact count-dependent slope boundary; natural exponential filters with a probability floor have an open count-rescue regime; decoupling changes but does not remove the transition.

Reject as overclaims: this is a new generic Jacobian principle; every hard/easy negative rule has this behavior; increasing K always improves information retention; observed convergence proves statistical identifiability; arbitrary learned neural encoders inherit the complete lookup spectrum; local instability alone proves loss of a bit.
