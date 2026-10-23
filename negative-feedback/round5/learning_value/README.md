# Finite-label value test: old window route rejected

**Status: actual task-based rescue attempt completed; the old stable-square-as-desirable framing fails.** This does not adjudicate the parent's distinct simplex-optimum/feedback hypothesis.

[Protocol and post-result amendment](protocol.md) · [Analysis and exact formulas](analysis.md) · [All risks](results/all_risks.csv) · [Summary](results/summary.json) · [Class-ID counterhypothesis](results/ncc_summary.json)

We evaluated all three balanced class partitions equally, with one or two labeled views per class and exact256/1296support enumeration. The primary affine-ridge regularizer.01 and controls0/.1 were fixed before outcomes. The old K4/K8 adaptive risks are essentially identical(~1/3); K16 increases this transfer risk(~.54), but all adaptive counts remain perfect at ordinary four-way class-ID nearest-centroid classification. A same-positive-information component/simplex baseline has primary transfer risk.000848 rather than square.333590.

This resolves the proposed finite-label meaning rather than leaving it as future work: there is a meaningful task-based contrast, but it does not make the square window universally desirable or by itself yield a new downstream mechanism. Standard class geometry and readout regularization explain the evaluated effects. The meaningful optimum for this symmetric linear-transfer goal is simplex-like, motivating a separately testable revised question rather than re-labeling the old result as success.

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python negative-feedback/round5/learning_value/evaluate.py
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python negative-feedback/round5/learning_value/ncc_check.py
```

Run from repository root with NumPy/SciPy. Both commands overwrite their own results. Source data are preserved round4embeddings; no training checkpoint, GPU or external dataset is used. The second command is a documented post-result competing-goal test. Minimum-norm readout reversals and the fixed classification tie band are retained. Code writes only this owned directory and does not modify earlier results.
