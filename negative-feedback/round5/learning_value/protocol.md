# Finite-label learning value: fixed task family and support protocol

2026-10-23. Written before evaluating the saved embeddings. This is an attempted rescue of the learning-importance gap, not additional gradient verification.

## Required claim and disconfirmation

The candidate claim is that the previously studied stable count window identifies a representation that is distinctly valuable for learning label-preserving tasks from few labels, rather than merely preferring one designated semantic factor. To remove that preference, use **all three** balanced binary partitions of four uniform classes with equal weight. Average and worst-task squared prediction risk are primary; do not select a task after inspecting results.

There are four views per class. Draw one or two labeled views per class, uniformly without replacement, and test only the remaining views. Enumerate all256 or1296 support sets exactly. All task labels are constant inside the supplied positive classes. The population evaluation needs no hidden-task oracle in pretraining; labels enter only downstream training/evaluation.

Use affine ridge with centered inputs, unpenalized intercept, and objective mean squared error + lambda||w||². Freeze lambda=.01 as primary, with0and.1 as sensitivity cases. Lambda0 uses the minimum-norm pseudoinverse at cutoff1e-12 and is explicitly a different readout. Do not choose lambda on test data. Report classification accuracy with a declared absolute prediction tie band1e-10 only as a diagnostic; continuous prediction risk avoids interpreting infinitesimal coordinates as robust access.

## Representations and controls

- Every saved base run from round4: two seeds × K4/8/16 × initial-policy-frozen/adaptive. No new embedding selected from outcome.
- Exact square and regular-simplex class collapse, each repeated across views.
- A primitive baseline using connected components of the **same population positive graph**, with regular-simplex component codes. This uses no extra downstream labels. It is a population-information baseline, not a claim about finite positive-pair sample complexity.
- A canonical regular-simplex semantic code plus zero-mean within-class simplex nuisance. Fixed nuisance energy nu={0,.05,.1,.3,.6,.9}. This isolates the familiar effect of within-class spread under the same support rule and supplies an exact ridge prediction formula.

Compute all metrics from Gram matrices and verify selected dual predictions against an independent primal solve. This is inherited kernel/linear regression algebra, not a new theorem. If empirical learning differences are explained by ordinary task rank, within-class spread and regularization, do not attribute a new downstream mechanism to count feedback. Conversely, a beneficial finite-label result is genuine evidence of utility within this model, even if it fails the independent novelty/importance test.

## Decision criteria

1. A stable square that loses a full balanced task or is dominated by the same-information component baseline does not establish universally desirable balanced geometry.
2. A K8 advantage over frozen weak-positive runs can be reported, but it does not isolate local feedback because the endpoint negative laws differ.
3. A finite-label harm explained by standard within/between geometry cannot itself carry a new top-journal contribution. A further new count/dynamics prediction would be needed; absence of that contribution is recorded as a failed rescue route, not shifted to optional work.
4. Preserve every saved base representation and every fixed lambda, including reversals. No favorable task or support set is retained alone.

## Post-result counterhypothesis amendment

The primary ridge analysis found a square-vs-simplex transfer-task gap and a K16 penalty. To attack the interpretation that this establishes a general few-label harm, also evaluate the ordinary four-way class-ID nearest-centroid task under exactly the same support sets. This target and readout are introduced **after** the ridge outcomes, as a competing explanation/scope test, not held-out confirmation. Report every representation and both support budgets. If K16 remains perfect on class-ID recovery while binary transfer risk worsens, distinguish those goals rather than selecting one as universally definitive.
