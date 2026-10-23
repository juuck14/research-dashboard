# Assumption audit protocol

2026-10-23. Owner: independent assumption analyst. No Git or external publication changes are made by this task. This is a scope audit of the existing theorem, not a claim of a new publishable learning principle.

## Fixed questions before numerical execution

1. Derive the detached scalar field derivative for arbitrary conditional mean h|s, retaining the derivative of the exponential-policy normalizer.
2. Distinguish a nonzero field at the reference from instability at an equilibrium. No slope at a drifting point will be labeled a stability eigenvalue.
3. Test the exact algebraic prediction that adding a small deterministic score-dependent mean to an exchange-balanced h produces first-order drift but only second-order slope changes at the same reference scores.
4. Perturb repeated reference scores into distinct scores, and solve for each count's nearby scalar stationary point. Determine whether stationary points differ by count instead of claiming that the old fixed reference remains an equilibrium.

## Fixed law and controls

Base score law: scores[-.6,0,.6], probabilities[.2,.6,.2]. Each score has two equally likely derivative signs with amplitudes[.4,1,.7]. Policy epsilon=.3,t=log4,beta=1. For conditional-mean violation use h_tau=h_zero+tau*a(s),a(s)=s+.5, tau in[0,.001,.01,.05,.1], counts[1,2,4,8,16,32,64]. Enumerate category counts exactly; no Monte Carlo seeds are involved.

Record exact population G,H and the algebraic residuals G_tau−tau G_a and H_tau−H_zero−tau²H_a. Independently differentiate the ordered six-candidate tuple field at K1/2/3, tau0/.01/.1, steps1e-5 and1e-6. Acceptance: maximum absolute slope discrepancy<1e-7. A failed check triggers a correction, not a changed hypothesis.

Distinct-score perturbation: six fixed score offsets[.03,−.2,.4,.07,−.13,.25], jitter amplitudes[1e-4,1e-3,.01], original h_zero, counts1/4/8. Locate a scalar root inside[-.1,.1] when the endpoints bracket it, and record G(0),H(0),root,G(root),H(root). Root existence or attraction will not be inferred from the slope at0. No root outside the declared bracket will be pursued in this task.

## Analytical status

Complete proofs will be separated from executed checks. The candidate characterization 'common reference stationary at every K iff E[h|s]=0' will be proved using tagged Laplace integrals and moment uniqueness. A finite-support strengthening for the first L counts will be attempted only if its invertibility proof can be completed; the use of standard total positivity/moment uniqueness will be acknowledged rather than claimed as a novel learning contribution.
