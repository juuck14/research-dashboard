# Composed objective preference and detached feedback are different questions

Direct independent derivation and ordered-tuple verification, 2026-10-23. This check was added in response to the strong alternative explanation that adaptive sampling merely changes the optimized objective. It is not a new method and does not rescind the observed preference reversal of the composed risk.

Let the notation be that of the verified general-omega simplex theorem. There are three relevant objects:

1. The risk with the target's uniform-off law frozen.
2. The detached field G(F)=E_{Q(F)}[grad ell(F,Y)].
3. The full derivative of the composed scalar risk R(F)=E_{Q(F)}[ell(F,Y)].

The policy's value at the simplex is the same uniform law in all three objects. Their derivatives differ. In particular, G is generally not grad R.

At the simplex every ordered negative tuple has the same loss ell_0=log(1+Ka). For a normalized embedding curve through it,

R''=sum_Y Q ell''+2 sum_Y Q' ell'+sum_Y Q'' ell_0.

The last term is zero because sum_Y Q(F,Y)=1 along the entire curve. The first is the frozen Hessian including the sphere geometry. The middle is twice the policy-response term of the detached Jacobian. Thus the composed-risk quadratic form is exactly the general-omega form with eta replaced by 2eta; no approximation or count limit is used.

For C≥4 the full strict local criteria modulo rotations are consequently

| Object | Criterion |
|---|---|
| Frozen uniform-off risk | Always strictly positive for every finite K |
| Detached closed-loop field | eta<T_K |
| Full composed adaptive risk | 2eta<T_K |

Equality in the last two rows is neutral in the shape block. For T_K/2<eta<T_K, the task-optimal simplex is locally attractive under the detached field despite being a shape saddle of the composed risk. Conversely, in the strong-easy regime eta>T_K, both become unstable. Therefore the strong-easy failure does not establish that detachment is uniquely responsible for harm. But it is also invalid to substitute composed-risk geometry for detached stability.

## A fixed, non-tuned witness and executed check

Set C4, epsilon=.05, omega(s)=exp(−.7s), tau1. Then eta=.665. At K1, T_1=1/(1+exp(−4/3))≈.791391. T_K increases towards1, so eta<T_K and 2eta>1>T_K for **every** finite K. This gives an all-count sign separation between detached stability and composed-risk instability for the same policy.

`composed_risk_check.py` independently enumerates all ordered true-negative tuples for K1/2/3 and computes a feasible row-centered Gram shape. Frozen-risk second differences, detached-field first differences and composed-risk second differences agree with their three predicted coefficients at two steps, for 18 checks. The maximum error is2.08e−7; the larger error is the expected loss-of-significance effect of a scalar second difference, not a direct field Jacobian error. Full raw values and signs are in `composed_risk_check.json`.

## Interpretation and limitation

The old claim that adaptive training failed to optimize an unchanged uniform objective is not supported and must not appear. The strong-easy policy can give a lower composed risk at class collapse than at the simplex. The actual result concerns the closed-loop field's exact response threshold and its semantic consequences, while explicitly separating it from both the frozen objective and full composed-risk optimization. This is a sharper mechanism statement than attributing every preference change to one of these objects.
