# Temperature and sampler specificity

2026-10-23. This is algebra and a direct corollary of the existing field formula, not a new main contribution. [Pre-execution protocol](temperature_protocol.md), [code](temperature_check.py), [actual output](temperature_summary.json).

Let the **raw cosine** score be s_delta=s+delta h, the loss denominator be D=beta+sum exp((s_delta−1)/tau), and the policy keep its raw-score exponential exp(−t*s_delta). Assume E[h|s]=0 and bounded variables. Put a=1/tau and W=exp(a(s−1)). The same tagged computation gives

\[
\frac{G'_K(0)}{K}=a^2\mathbb E_q[h^2Wf_{K-1}(\beta+W)
\{1-\theta\rho-WR_{K-1}(\beta+W)\}],
\qquad\theta=t/a=t\tau.
\]

The old proof's condition is **theta>1**, not merely t>1 in raw cosine units. This follows by writing the shifted rescaled score as S=1+(s−1)/tau and its derivative as h/tau. The rescaled sampler exponent is theta; its irrelevant constant cancels in normalization. The proof allows compact score intervals beyond[-1,1], so boundedness is enough for this rescaling.

For theta>1 the critical floor becomes

\[
\epsilon_c(\tau)=
\frac{(\theta-1)\mathbb E[h^2 e^{(a-t)s}]}
{(\theta-1)\mathbb E[h^2 e^{(a-t)s}]+Z\mathbb E[h^2e^{as}]},
\qquad Z=\mathbb E e^{-ts}.
\]

If the sampler is instead defined on s/tau, changing tau changes a different policy family. The two conventions cannot be silently identified. When theta≤1, the earlier no-reentry/rescue proof does not apply; this is not a counterexample or a declaration of instability.

## Opposite sampler monotonicity

For t≤0 the same mixture favors harder negatives, or is uniform at t0. With beta>0,

\[
W R_{K-1}(\beta+W)<1,
\quad 1-\theta\rho-WR>0.
\]

Hence this **particular exchange-balanced affine mode** has positive curvature at every finite K for t≤0. The central easy-negative feedback instability is absent in this mode under this opposite exponential preference. This does not imply that arbitrary hard-negative training is stable, informative or free of feature tradeoffs. It says the current mechanism is sampler-specific even inside the tractable family.

## Executed check and interpretation

The fixed three-factor tuple calculation evaluated96settings. Drift at the balanced reference was at most2.78e-17, the independent detached-field finite-difference discrepancy at most1.11e-9, and every tested hard/uniform-policy value was positive (minimum.1168349). Only30settings satisfy theta>1, the regime covered by the old no-rescue proof. Finite checks support the derivation and do not turn an out-of-scope condition into an all-K theorem.

The first attempt completed the computations and assertions but failed to serialize one NumPy int64 count. Casting that reporting count to Python int corrected the output; no configuration, pass criterion or scientific formula changed. The successful rerun is the preserved result.

This clarification supports the user's concern about temperature and policy scope. It makes the dimensionless assumption explicit; it does not make the fixedK5..11 window a practical universal rule.
