# Independent novelty audit and competing-explanation checks

2026-10-22. This record is written after source exploration and analytic reduction, but before executing the new audit script below. It is not a retrospective preregistration of the whole research program.

## Claims under attack

- A: policies with equal values at all square scores but different local slopes can have opposite closed-loop stability despite an identical frozen objective.
- B: the exact K-negative balance-mode threshold increases strictly with K and can produce stabilization.

The original prior-art review already covered performative prediction, self-paced implicit losses, hard-negative tilting and feature suppression. This round must not present their renewed reading as newly discovered literature.

## Strong null explanations

1. A is an ordinary repeated-gradient/robust-reweighting curvature effect, requiring no contrastive structure.
2. The K-infinite exponential-policy limit is merely a change of effective softmax temperature. Finite-K changes should be described relative to that elementary limit.
3. Balance-mode stabilization does not imply stability on the full representation sphere. In particular, a natural exponential policy can lose a normal mode as K grows.
4. Finite-K expectation differs from the infinite-negative population objective. This is already understood as nondecomposability/gradient bias; a new finite-K law must predict more than the existence of that difference.

## Fixed numerical checks

All are exact finite-state expectations or algebraic identities, not trained-network evidence.

- Check the K-infinite effective-temperature gradient identity at 10 independent random normalized 6x4 representations, seeds 901-910, kappa in {-2,-1,-.5,0,1,2}. For epsilon=0 accept equality only if max absolute coordinate error <1e-12. Include kappa=-1 via the mean-score limiting expression. Epsilon=.1 is a scope control, not a theorem of impossibility of any potential.
- For the natural exponential policy, epsilon=.1 and kappa=-1, enumerate K in {1,2,4,8,9,16,32,64,128}. Record the balance eigenvalue and the normal ab eigenvalue separately. Positive values are gradient-field Jacobian values, hence attracting for negative gradient flow. The prediction is that positive balance curvature at large K does not rescue full square stability because the normal mode is negative.
- Algebraic witness: squared loss with Z in {-1,1}, mean tanh(m theta), m in {.5,2}, has identical full-support frozen distribution at theta=0 but flow derivative -(1-m). This makes the broad content of A a generic performative example, independent of SSL. No numerical simulation is needed to prove it.

No policy parameters will be adjusted to obtain a favorable audit result. Outputs go to results/audit_checks.json and results/natural_exponential.csv.

## Addendum before execution

After reading Yeh et al., ECCV 2022, Proposition1-2, add a stronger control: remove the positive term from the loss denominator, as in DCL. Recompute the same exact balance-mode moments with D_minus=n_self+exp(-1)*N+exp(-2)*n_opp, using the identical preselected shaped policy alpha=-.9 and epsilon=.1. Test K in {1,2,4,8,9,16,32,64,128}. The prediction is threshold0 at K1 and an increasing threshold toward1, so eliminating negative-positive coupling alone does not eliminate the response-slope count effect. This was motivated by a newly read competing explanation, not by results from the audit script. It is a scalar-mode control; it will not by itself establish all-mode DCL stability.

## Analytic follow-up selected after the first audit results

The root analyst constructed a natural exponential example analytically after seeing the epsilon=.1,kappa=-1 normal-mode failure: epsilon=.3,kappa=-log(4), yielding u=.103,v=.187,w=.523, w/v>e and eta between .731 and1. This is an explicitly exploratory analytic construction, not an independent preregistered replication. Enumerate K1-128 with the unchanged moment code and preserve it as natural_exponential_followup.csv. The original failure example remains; it rules out a universal inference from balance stabilization to full stability, not the existence of natural exponential full-stability rescue. Full tangent verification belongs to the theory owner's checks.
