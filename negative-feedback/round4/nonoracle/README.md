# Non-oracle accessibility of the local square/view mechanism

**Status: a positive finite-model accessibility result; academic importance and downstream harm remain unestablished.** 2026-10-23. This addresses one specific criticism of the old oracle-initialized MLP study. It does not reverse the old MLP's0/3applicability failures or restore a top-journal50% verdict.

[Pre-execution protocol](protocol.md) · [actual code](run.py) · [raw summary](results/summary.json) · [all rows](results/runs.csv) · [traces](results/traces.csv) · [final embeddings](results/embeddings.json) · [semantic relabeling limitation](symmetry_lemma.md)

## What was actually changed

We used16independently trainable unit embedding rows in16dimensions, initialized as normalized iid Gaussian vectors without latent labels or a prepared equilibrium. There are four classes with four observations each. The learner sees positive correspondence `.95I+.05U_class`; the bit labels are used only in evaluation. This is an overcomplete finite lookup model, not a shared neural encoder and not a novel architecture.

The current negative policy is the old easy-exponential mixture with epsilon.3 and tlog4. K4/8/16 are actual joint-denominator population objectives, evaluated with the previous round's Laplace oracle. Adaptive and frozen runs start from identical embeddings and identical negative policy q0. Frozen then keeps **the random point's q0**, not the square's q*. It is a trajectory-level matched-initial-policy control; its later behavior cannot be read as the old matched-q* local stability theorem. At the endpoints, the two policies generally induce different sampling laws and different population objectives. Their long-trajectory endpoint difference therefore does **not** isolate the local policy-response Jacobian as its sole cause, and is not pure policy-feedback causal evidence.

No warmup, label-based initialization or favorable seed selection was used. Fixed step2 and8000steps give modeltime16000; full projected-field tolerance1e-7 allows uniform early stopping. A prespecified timing-only rule reduced the six planned seeds to one primary6101 and one confirmation6201, with all other four explicitly unexecuted. The timing smoke predicted272s for the full plan, above180s; single-thread full execution ultimately took29.1s for the reduced plan. We did not use that outcome to add favorable seeds afterward.

## Observed endpoints

These are base step2 runs. Square error minimizes over all3opposite-pair matchings; it does not favor the original semantic-bit arrangement. View variance is the mean squared deviation from the within-class mean.

| Seed | K | Policy | Best square error | View variance | Full field norm | Stop |
|---|---:|---|---:|---:|---:|---|
|6101|4|adaptive|.081214|1.44e-31|2.71e-6|cap|
|6201|4|adaptive|.076282|1.50e-31|1.83e-6|cap|
|6101|8|adaptive|3.26e-10|3.25e-10|9.64e-8|tolerance|
|6201|8|adaptive|3.46e-10|3.45e-10|9.94e-8|tolerance|
|6101|16|adaptive|.054452|.054451|2.13e-5|cap|
|6201|16|adaptive|.054186|.054184|1.55e-5|cap|
|6101|4|frozen|.763534|.629668|7.86e-7|cap|
|6201|4|frozen|.745971|.637580|9.98e-8|tolerance|
|6101|8|frozen|.775742|.650556|2.42e-6|cap|
|6201|8|frozen|.759954|.658807|2.55e-6|cap|
|6101|16|frozen|.783783|.664133|9.98e-8|tolerance|
|6201|16|frozen|.768758|.672075|9.79e-8|tolerance|

Both K8 adaptive trajectories meet the prespecified approximate-reference criterion (squareerror<.001, variance<.001,fieldnorm<1e-6). This supplies actual non-oracle access to the reference neighborhood in this finite model, rather than inserting the exact geometry. It is not a proof of a generic basin or convergence probability. No square theorem is applied to the nonstationary K4/K16 cap endpoints.

## Competing numerical explanations

- Seed6201's six conditions were rerun at half-step1 and the same total modeltime. Max square-error change1.33e-5; max view-variance change1.08e-6. The qualitative ordering remains. Full comparisons are in summary.json.
- Final quadrature64→96 gradient discrepancy is at most2.78e-17. Thus the result is not explained by an inaccurate low-resolution population oracle in these outputs.
- Frobenius full-field norms are recorded, rather than loss decrease alone. Several cap endpoints are not certified stationary.
- Output dimension16≥N−1 rules out a shortage of representational dimension for this finite population. It does not remove unit-sphere geometry or prove that a shared encoder has the same accessibility.

## Why this does not establish semantic quality

The two K8 seeds approach different square matchings. Because the positive graph and score policy are equivariant under arbitrary class relabeling, those matchings are indistinguishable to the learner. At every exact square, two of the balanced bits a,b,ab are linearly separable and one is XOR; every bit is nonlinearly and information-theoretically recoverable. See [the exact symmetry argument](symmetry_lemma.md) and [its diagnostic](results/symmetry_check.json).

The CSV's `factor_a_linear_accuracy` and `factor_b_linear_accuracy` mean accuracy of one specific **zero-intercept least-squares pseudoinverse readout**, with coefficients `pinv(F, rcond=1e-12) @ bits`, thresholded at zero. The names do not mean optimal linear-classifier accuracy. `factor_readout_norm` is the coefficient Frobenius norm, not a margin. No LP-based maximum-margin or optimal classification calculation was executed. Near-collapse coordinates can change numerical rank or require enormous coefficients, while the truncation can discard small but informative coordinates. The reported low accuracy for one seed cannot be called factor erasure or a bound on information. Likewise K16 view variance by itself is not a harmful-task result: nuisance retention may be harmless or useful depending on the target.

## Verdict within this test

**Resolved narrowly:** the declared square geometry need not be produced by oracle initialization; two fixed uninformed free-embedding trajectories reach its numerical neighborhood at K8.

**Still unresolved:** shared-network non-oracle visitation, how broad the effect is across policy/temperature/graph conditions, a task-based reason to prefer this geometry, downstream harm, and whether this restricted classification is an important independent journal contribution. This experiment does not justify top50by itself. The original no-information-erasure correction remains necessary.

## Reproduce

From repository root, Python3.12.14 with NumPy2.3.5/SciPy1.17.0:

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python negative-feedback/round4/nonoracle/run.py
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python negative-feedback/round4/nonoracle/symmetry_check.py
```

The script reads the saved timing rule and uses the same fixed seed subset. Runs overwrite this subdirectory's declared result files; preserve the delivered outputs before a rerun. Source imports the unchanged round3 oracle and therefore needs the whole repository. `results/run_log.txt` contains every completed run, while `results/progress_rows.json` was checkpointed after each run. There are no external datasets, model weights, GPU runs or processes left running.
