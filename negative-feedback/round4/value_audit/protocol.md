# Task-meaning audit before computation

2026-10-23. Purpose: test whether an actually unstable direction of the existing model can be equated with poorer representation quality. This is an adversarial scope check, not a proposed publication contribution.

## Fixed setting

- Observation X=(a,b,v), three independent uniform signs.
- Four semantic classes c=(a,b), two observed views v per class.
- Positive channel P=.95I+.05U_class, natural policy epsilon=.3,t=log4.
- Joint negative count K8 and16; both updating and reference-frozen policy.
- Reference f0=(a,b,0)/sqrt2. Normal view direction z=(0,0,v) has zero classwise mean.
- Perturbation f_alpha=(sqrt((1-alpha²)/2)a,sqrt((1-alpha²)/2)b,alpha*v), all unit norm.

No random search is used. Counts, amplitudes[0,.001,.01,.1,.3,.6], Gaussian noise sigma[.2,.5], and task weights[0,.1,.5,1] are fixed before execution. First independently check that this normal direction contracts atK8 and expands atK16 by differentiating the actual population field with step1e-5 and1e-4; report both samplers. This oracle is inherited code, so call it a new scope calculation, not an independent gradient implementation.

## Exact mathematical checks

For every0<alpha<1, signs of the three coordinates recover a,b,v linearly. Thus each factor has noiseless mutual information1bit and X has3bits; atalpha0, v has0bits and X has2bits. The semantic coordinates remain perfect. With additive isotropic Gaussian observation noise sigma, exact Bayes accuracies are Phi(sqrt((1-alpha²)/2)/sigma) for a,b and Phi(alpha/sigma) forv. Nuisance coding may therefore improve one task while worsening another; no task-independent quality ordering follows from local instability.

Because v need not be invariant under the positive channel, separately evaluate the old K4 rectangular endpoint at theta=.7545192717973 versuspi/4 for tasks a andb, both of which ARE positive-consistent. Their exact noisy accuracies are Phi(cos(theta)/sigma),Phi(sin(theta)/sigma). Weighted task utilities with prior weights.1/.5/.9 are fixed; opposite task preferences should permit opposite quality ordering for the same endpoint.

## Decision criteria

- If the normal direction is not unstable atK16, do not use it as a counterexample to the interpretation of that boundary.
- If information preservation or Bayes formulas fail, retract that claim rather than changing the noise condition.
- If task orderings disagree, conclude that the stability theorem alone does not identify downstream harm. Do NOT conclude the theorem false, arbitrary learning safe, or this familiar task-dependence principle newly discovered.
- This cannot establish what endpoints generic learning reaches. It supplies the exact missing distinction a global or learning-relevance claim must resolve.
