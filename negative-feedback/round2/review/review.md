# Independent mathematical audit: verified, with explicit scope limits

Date: 2026-10-22. Role: independent critic of `../theory/theorem.md`; no author code was imported for the ordered-tuple checks. This report evaluates the mathematics and implementation. It does **not** certify publication novelty; a separate source audit is required.

## Verdict

The arbitrary-K smooth-policy threshold, complete tangent spectrum, monotonicity proof, and sufficient conditions for full-sphere stability withstand this audit. The natural exponential example and the decoupled-denominator control also withstand independent numerical and interval checks. No mathematical counterexample or implementation mismatch was found in the stated model.

The rank-filter counterexample has correct one-sided algebra for an **exact-equality tie rule**. A positive tie tolerance changes infinitesimal stability and must be discussed as a different algorithm. This distinction is consequential, not a floating-point footnote.

## 1. Independently reconstructed expected gradient

`audit.py` enumerates ordered tuples `(Y1,...,YK)` with their direct iid product probabilities. The author's implementation instead enumerates multinomial counts. The audit shares the mathematical model but no aggregation code. It includes gradients through both anchor and sampled-negative embeddings, normalizes each row, and projects the resulting field onto the product-sphere tangent space.

The tangent basis is constructed explicitly from each square vector's in-plane perpendicular plus two normal vectors. This also differs from the author's null-space basis. A separate orthogonal rotation uses seed271828.

Executed:

```bash
python negative-feedback/round2/review/audit.py
```

There were 62 complete twelve-dimensional spectrum comparisons: K1–5, alpha−1.5/−.9/0, two difference steps, frozen/adaptive, and an additional rotated K3 check. Maximum eigenvalue discrepancy was **4.67e−11**; maximum stationary-field residual was **4.17e−17**. The negligible imaginary eigenvalue parts were below1.59e−12. Thus neither a tied-coordinate-only calculation nor omission of sampled-negative gradients explains the reported effect. These are numerical consistency checks; the analytic proof supplies the all-K statement.

## 2. Independently checked proofs

### Factor-mode formula and normalization

For the tied angle, adjacent score derivatives are −2,+2. If `Delta=N2−N1`, then conditional on the aggregated adjacent count N, `E[Delta²|N]=N`. At the square the sampling normalizer has zero derivative in this direction, giving the tuple probability response `2g*Delta/v`. Therefore the derivative of the detached expected angle gradient is exactly

`H_K=4A*E[N/D]*(1−A*R_K+g/v)`.

The squared product-sphere angle tangent norm is four, so the full-field factor eigenvalue is H_K/4. This factor is easy to miss; both the author's formula and independent FD comparison use it correctly. This derivative responds to changes in q between updates; it does not differentiate q inside one update.

### Palm indexing and monotonicity

Conditioning one selected draw to be adjacent gives

`E[N/D^p]=2Kv E[(beta+A+sum_(K−1) Z)^−p]`.

The remaining sum has **K−1** terms, not K. Let `m_j(z)=E[(Y+z)^−j]`. Then the inverse-moment ratio derivative is

`(m2/m1)'=(-2m3*m1+m2²)/m1²<0`,

because Cauchy–Schwarz gives `m3*m1≥m2²`. Adding an independent positive random shift is a positive-weighted average of these strictly smaller deterministic-shift ratios. That establishes strict decrease of R and strict increase of T. Independence and fixed square sampling probabilities as K changes are required. The bound `Z≥A²>0` supplies convergence to one without an unproved exchange of limits.

### Full-space sufficiency

I independently expanded the proposed coefficient of g for the two other in-plane characters. Writing `F_z=E[1/(beta+A+z+S_(K−2))]`, it is

`C_p/A=M*(1−t1)/(2v)+K(K−1)v*[t0(F_A−F_1)+t2(F_A−F_B)]`.

All coefficients, including the N²+N factor, agree. When `t2/t0≥1/A`, the bracket is nonpositive pointwise, so `C_p<C_b/2`. For g≤0 this has the correct reversed inequality after multiplication. The remaining frozen difference

`lambda_pF−lambda_bF/2=A² E[W/D]−(A²/4)E[N(N−1)/D²]`

is strictly positive under the stated normal-mode condition `A²*w>A*v`. The normal-mode Palm comparison is valid because its opposite-category denominator is smaller than its adjacent-category denominator. Thus positive factor curvature indeed suffices for positive curvature in **every nonrotation direction**, for these value conditions. No K≤128 extrapolation is needed.

### Open natural-policy regime

For the natural policy, `rho=(c/Z)/v`, `eta=t*rho`, and `w/v=1+rho*(exp(t)−1)`. Consequently the normal-mode condition is exactly `rho>(e−1)/(exp(t)−1)`. For t>1 the latter lower bound is strictly below1/t. The open interval in Theorem6 is therefore nonempty; the count-rescue effect does not require the shaped matched-value policy. The inverse epsilon formula in that proof also checks out.

## 3. Integer cutoffs certified beyond floating-point agreement

`certify_cutoff.py` encloses e using 51 exact factorial-series terms and a rigorous tail bound. Every subsequent operation is enclosed using 70-digit directed Decimal rounding. `certify_controls.py` additionally encloses `log(4)=4*sum_(k≥0) (1/3)^(2k+1)/(2k+1)` using90 terms and a positive geometric tail bound. The JSON outputs preserve lower and upper bounds, rather than printing a rounded point estimate.

| Policy and denominator | Last unstable K | Certified T_K−eta, approximately | First stable K | Certified T_K−eta, approximately |
|---|---:|---:|---:|---:|
| Matched alpha−.9, InfoNCE | 8 | −.001174412758358 | 9 | +.008109957749173 |
| Natural `4^(−s)`, epsilon.3, InfoNCE | 4 | −.000370208139525 | 5 | +.019175621957906 |
| Natural `4^(−s)`, epsilon.3, DCL | 7 | −.021143046685147 | 8 | +.004224315183842 |
| Matched alpha−.9, DCL | 13 | −.000082918712460 | 14 | +.009277846257819 |

For the natural example, q is exactly `(103,187,187,523)/1000` in self/adjacent/adjacent/opposite order and `eta=(112/187)log4`. Its normal-mode sufficient-condition margin `A²*w−A*v` is enclosed above **.0019868976336887**, strictly positive. For the matched example that margin exceeds **.0539181395424398**. Combining these certified finite brackets with the analytic monotonicity and full-spectrum theorem establishes the quoted all-K cutoffs.

The interval script initially used Decimal unary minus, which silently rounded in the default28-digit context and invalidated enclosure rigor for subtractions. This was detected from unexpectedly zero-width intervals, corrected to exact `copy_negate()`, and the scripts were rerun with nonzero-width enclosure assertions. No result from that first failed certificate is used. The FD model checks were unaffected.

## 4. Independent natural/DCL implementation control

The audit was extended after the root requested natural and DCL checks; this is a recorded scope extension, not a prospectively selected original audit condition. The ordered-tuple field is unchanged except for policy slope/epsilon and denominator offset. `control_audit.py` executed16 additional complete tangent comparisons at K1,2,4,5, both denominator offsets and both frozen/adaptive fields. Maximum discrepancy was **5.73e−11** and maximum stationary residual **2.78e−17**.

The offset extension is algebraically valid. DCL removes the identity-positive1 but retains multiple-negative log-sum curvature. Its threshold starts at zero and rises to one, so count rescue surviving DCL rules out the claim that the positive-negative coupling factor is the sole explanation. It does not rule out generic finite-negative softmax-curvature explanations, which are part of the mechanism.

**DCL K1 caveat:** its frozen factor mode has zero curvature. It is not a strictly stable-frozen/unstable-adaptive comparison. The author's updated theorem explicitly records this exception.

## 5. Quantile rule: valid ideal theorem, different finite-tolerance algorithm

The independent scalar calculation in `quantile_audit.py` verifies the no-self bottom-half rule. At the square, each adjacent probability is `(1+epsilon)/6` and the opposite probability is `(2−epsilon)/3`. At epsilon.1 its matched-frozen normal-product curvature is **+.02618925669617534**. It is strictly positive throughout `0≤epsilon<.4097198918550527...`, so this comparison is not a single epsilon coincidence.

An arbitrarily small nonzero factor imbalance breaks the adjacent tie under the exact rule. Their probabilities jump to1/3 and epsilon/3. The tied projected flow tends to **±.040341213205499264**, directed away from balance. The tied subspace is invariant; this proves Lyapunov instability of the ideal discontinuous equilibrium, without invoking a nonexistent smooth Jacobian.

With tolerance1e−12, however, an open interval of sufficiently small score differences remains tied. Inside it the field matches the frozen sampler and points toward balance. Independent output `quantile_tolerance.csv` gives, at delta1e−14, approximately **−7.22e−16** with tolerance versus **+.0403412** for the ideal equality rule. The root was notified and added an explicit tolerance control. Practical finite perturbation escape and exact-rule infinitesimal instability must remain separate claims.

## 6. Boundaries that the paper must retain

- Uniform four-state population, independent trainable unit embeddings, identity positives, temperature one, and iid negative sampling **with replacement** define the theorem. A finite dataset sampler without replacement, learned encoder, changing temperature, or minibatch-shared sampling requires a separate argument.
- The square is a local equilibrium and has rank two. Dimension d≥3 removes a hard rank/capacity obstruction, but unit normalization still creates directional resource competition. The result does not establish a global basin or explain why an arbitrary initialization learns the square rather than a tetrahedron.
- Local factor imbalance is not an information-theoretic erasure result. Any finite nonzero factor amplitude can retain exact noiseless distinguishability; access under a fixed noisy or linear readout is a different observable.
- At equality eta=T_K the linearization is nonhyperbolic; neither the proof nor the numeric certificate classifies nonlinear stability there.
- A detached adaptive field is generally not the gradient of the composed expected risk. The derivative of the sampler between updates is the object studied here; claiming an additional gradient term inside an SGD update would describe a different algorithm.
- The generic distribution-response product rule, finite-K moment algebra, and matched-value-versus-derivative construction do not by themselves establish academic novelty. The defensible mathematical object is the connected complete spectrum, strict monotone threshold, full-space sufficient conditions, open natural-policy regime, and controlled count transition. Closest-literature and learned-encoder evidence decide whether that object merits a paper.

## 7. Additional read-only learned-encoder audit

The root subsequently requested a check of `../encoder/run_encoder.py` and `audit_results.py`. Source inspection confirms that the loss is an exactly batch-averaged **one-negative** logistic risk, not K63 joint InfoNCE. Its manual derivative correctly subtracts each row's summed negative weight on the positive diagonal, backpropagates through both shared-encoder branches, and holds q detached. Both positive views share the two generated bits but have independent nuisance draws. No factor labels enter gradient computation; trace/probe labels affect reporting only.

The frozen snapshot is immutable and evaluated on every new input batch. The three policies receive common random training streams within a seed. The warmup prerequisite and PCA control are declared separately. OLS uses no ridge shrinkage and therefore tests an important competing measurement explanation; it cannot itself certify mutual information or Bayes-optimal access. The original primary clean-loss endpoint failed and is explicitly retained as a failed endpoint in the results manuscript.

`encoder_audit.py` executed an additional150 parameter finite differences at two new seeds for uniform, adaptive, and distinct-snapshot frozen policies,25 coordinates each. Maximum absolute error was **1.03e−10**, maximum relative error for non-tiny derivatives **1.60e−7**. At two new matched forks, loss and every gradient coordinate matched exactly. All36 saved final models were separately passed through a pseudoinverse OLS readout; every accuracy agreed exactly with the author's stored `lstsq` outputs. These checks identify no training or result-linkage bug.

One wording issue was reported: the reported882–7,260 ratios are **squared coefficient energies**, not coefficient norm ratios. The corresponding norm ratios are their square roots, approximately29.7–85.2. The encoder owner was notified to correct the first results sentence.

To respect read-only ownership, the audit removes the source module's one top-level config-write expression from its AST before loading functions; it does not modify that source or encoder artifacts. The config import side effect is a reproducibility convenience issue, not a numerical error in the executed run. Audit outputs are entirely within this review directory.

## Reproduction and files

From the repository root:

```bash
python negative-feedback/round2/review/audit.py
python negative-feedback/round2/review/control_audit.py
python negative-feedback/round2/review/certify_cutoff.py
python negative-feedback/round2/review/certify_controls.py
python negative-feedback/round2/review/quantile_audit.py
OPENBLAS_NUM_THREADS=1 python negative-feedback/round2/review/encoder_audit.py
```

NumPy2.3.5 and Python3.12.14 were used; the interval certificate uses only Python's standard library. CSV/JSON outputs are in this directory's `results/`. This audit did not mutate git or publish externally; the root agent owns repository integration.
