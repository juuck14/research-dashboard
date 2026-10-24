# Independent recovery check: protocol before execution

2026-10-25. The unpublished original raw files were removed by workspace maintenance after the final upload stalled. This is a **new independently implemented recovery run**, not a byte recovery of the original outputs. No author population oracle or scientific implementation is imported. The proof being tested was already derived in the earlier conversation; numerical tests are not a substitute for its quantified proof.

## Fixed cases and criteria

- General geometries: C4/5/6, dimension C−1, normalized iid Gaussian feature rows from new seeds8851/8852; temperatures .7/1/1.4; uniform floors .01/.13; iid negative counts K1/2/3.
- Two nonlinear log weights are fixed: `[-g*s+a*sin(pi*s)/pi]/tau`, with `(g,a)=(.6,.25)` and `(.85,.05)`. Their exact global easy-slope budgets are g+a=.85/.9, not estimates from a score grid.
- For every candidate row, compute beta in two independent finite sums: full ordered K-tuples, and a tagged position with K−1 other tuples. Require maximum difference below1e−11.
- Check coordinatewise `beta >= rho*pi`, where `rho=K*b/[2+(K−1)*b]`, and verify the residual beta−rho*pi is nonnegative and has mass at most1−rho. Verify sum beta<1.
- Check the quantitative tilted-mean inequality, centroid and full Gram identities, the exact stress trace identity, and the final Gram conversion inequality. Numerical tolerance1e−11 is fixed before execution. These random geometries are not assumed stationary or stable, and the final stable-equilibrium conclusion is not applied to them.
- Stationary controls: balanced coarse representations at C4/6, temperature1, floor.01, exponential omega=exp(−.9s), K1/2/8/16/4096. Compute coefficients by exact binomial expectation, stationarity, stress eigenvalues, and the M/K bound **only where the stress is PSD**. Compare the independently assembled stress spectrum with the analytic graph spectrum. A PSD stress at this collinear point is the relevant full normal-space stability criterion; random-state PSD values are not used to infer stationarity.
- Separate finite differences: C4/6, K1/2/3 at the same coarse reference. Use a negative-stress eigenvector and a fixed deterministic class-vector direction in an unused ambient feature coordinate. Recompute the sampler after each normalized perturbation; compare the closed-loop derivative to2H. Require max error below1e−8 at step3e−6.

## Outputs and failures

Write `independent_check.json` with every case's parameters and metrics, `independent_cases.csv`, and `independent_results.md` with a concise interpretation. Preserve failures rather than changing seeds or tolerances. The summary identifies this execution as2026-10-25 and records versions/runtime. No Git mutation is performed by this check.
