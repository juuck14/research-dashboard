# Non-oracle free-embedding accessibility check

2026-10-23. Recorded before scientific outcomes. This is an incremental scope check, not a replacement for earlier ordinary-MLP failures and not an academic-importance test.

## Question and alternatives

A: the local square/view mechanism can influence a representation reached without semantic oracle initialization. B: ordinary trajectories do not approach the stationary geometry to which the exact theorem applies. Neither a finite failure nor a finite success proves generic global behavior.

## Fixed setting

- Four equally weighted classes, four observations per class, N16; free unit embeddings in d16, enough dimension for an injective simplex. Positive correspondence only enters learning; semantic bit labels enter evaluation only.
- Positive matrix `.95I + .05 U_class`. Natural detached q has epsilon.3,tlog4. Actual joint-K population InfoNCE; both encoder appearances differentiated.
- No uniform-policy warmup. Initial rows are normalized iid Gaussian, constructed without labels.
- Same initial rows and q0 for frozen and adaptive comparisons. Frozen keeps q0 from the random point, not from the square. Thus it is a trajectory-level matched-initial-policy control, not the square's matched-q* stability theorem.
- Primary seeds6101/6102/6103; confirmation6201/6202/6203. K4/8/16, frozen/adaptive,36runs.
- Fixed projected Euler update with row normalization, dt2,8000steps (modeltime16000). Uniform early stopping only if full projected-field Frobenius norm<1e-7; inspect every20steps after100steps. No result-based retuning.
- Laplace quadrature64 throughout; final gradient/value checked at96. Absolute field discrepancy must be<1e-6. A numerically inadequate oracle invalidates interpretation rather than counting as a scientific failure.
- Seed6201, all six K/policy conditions: halve step to1 at same total modeltime16000. Compare geometric metrics and terminal fields. If ordering changes materially, the observed finite-time effect is optimizer-sensitive and cannot establish the mechanism.

## Measurements and criteria

Evaluate class-mean Gram distance to the best of the3square matchings (no preference for the original two semantic coordinates), within-class view variance, full projected field norm, class-mean eigenvalues, minimum observation pair distance, and least-squares access to the two fixed factor labels with explicitly recorded readout norm/numerical rank. Finite injectivity, linear access and invariance are different measurements.

An endpoint is theorem-applicable only if best-square relative Gram error<.001, within-view variance<.001 and full field norm<1e-6. A numerical geometry resemblance without stationarity is not a theorem replication. For a non-square endpoint the exact K5..11 prediction is not asserted.

The primary comparison is whether any uninformed initialization reaches a theorem-applicable geometry under these fixed conditions. If none do, report a scope failure within this finite modeltime; do not conclude the phenomenon cannot occur. If K8 approaches while K4/16 do not, this is finite-model evidence of accessibility, not a universal count rule or downstream harm. A scalar factor readout at these finite points does not establish information erasure.

## Timing check

A200oracle-evaluation smoke test, independent of scientific endpoint metrics, determines runtime feasibility. If the projected total exceeds180CPU seconds, the same cap of8000steps is retained but only one primary and one confirmation seed are run; remaining runs are explicitly unexecuted, not silently omitted. A separate timing diagnostic is saved. No geometry is used for this budget decision.

## Post-execution diagnostic amendment

After the base runs, seed6101 and6201 selected different square matchings. The ensuing symmetry check is an algebraic diagnostic prompted by those results, not a prespecified new confirmation experiment. It constructs the three exact square matchings for evaluation, verifies S4-equivariance numerically, and distinguishes factor linear separation from information retention. The run's least-squares readout accuracy is a particular truncated numerical readout, not optimal linear-classifier accuracy or mutual information. No new training seed is selected to favor the diagnostic.

### Reporting clarification at final source review

An initial configuration message to the parent proposed an LP-based linear-separability margin. The executable protocol above and the actual code instead use a truncated pseudoinverse diagnostic. **The LP margin was not implemented or run**, and no margin or optimal-linear-access result is available. The raw columns `factor_a_linear_accuracy` and `factor_b_linear_accuracy` are sign accuracies of the specific zero-intercept least-squares readout `pinv(F, rcond=1e-12) @ bits`; `factor_readout_norm` is its coefficient norm. They are neither an optimized classifier comparison nor an information-retention test. This clarification does not change the raw outputs or any acceptance criterion.

Frozen q0 is taken at the random initial representation. It is not the final square's matched frozen policy. Endpoint differences combine the cumulative changes in the negative sampling law and population update along a trajectory; they do not isolate a local response Jacobian or prove a pure feedback cause. No additional experiment was executed for this reporting clarification.
