# Reproduction and provenance

Run from repository root with Python3.12 and the existing NumPy/SciPy environment. The scripts depend on the preserved round3 population oracle; copy the whole repository, not only round4. No GPU or external dataset is required.

```bash
export OPENBLAS_NUM_THREADS=1
export OMP_NUM_THREADS=1
python negative-feedback/round4/assumptions/check_assumptions.py
python negative-feedback/round4/value_audit/task_meaning_check.py
python negative-feedback/round4/temperature_check.py
python negative-feedback/round4/nonoracle/run.py
python negative-feedback/round4/nonoracle/symmetry_check.py
```

These commands overwrite the specified results. Preserve a copy before reproducing. The nonoracle script reads the saved prescientific timing_smoke.json to apply the recorded budget rule; it does not select seeds based on outcome. It ran primary6101 and confirmation6201,12base runs plus6half-step comparisons,29.1seconds on the recorded machine. The remaining four planned seeds were not executed. Runtime is machine-dependent. It does not require or create model checkpoints.

```bash
python negative-feedback/round4/recheck.py
```

The recheck copies the topic to a temporary directory, reruns four scope/symmetry scripts and replays seed6201's three adaptive count conditions. It leaves delivered raw outputs unchanged. This is a same-source reproducibility check, not an independent gradient implementation, a new confirmation seed or importance evidence.

Protocols precede the scientific runs. The post-result source-review amendments explicitly record the unexecuted LP metric and the limits of the frozen endpoint comparison. `factor_*_linear_accuracy` means the zero-intercept pseudoinverse classifier at the stated numerical cutoff, not optimal linear separability or mutual information. Exact claims about square/XOR readout are separately proved and checked, not inferred from this classifier.

The prior assessment and new scope results are distinguished in report_ko.md. The manifest records the delivered bytes; elapsed-time fields need not reproduce bit-for-bit on a new machine. No publication-level conclusion is inferred from the number of scripts or checks.
