# Recovery audit of the global count-recovery proof

2026-10-25. This is a new independent mathematical audit during recovery. The unpublished local workspace was removed after an interrupted final upload. The complete theorem was reconstructed from the preserved conversation, not read back from a surviving original proof file. This audit does not recreate missing experiment outputs, original reviewers' files, or a byte-identical historical artifact.

## Disposition

**Mathematical proof: passes the present independent audit.** I found no fatal gap in the restored global all-stable-equilibria bound, its radius consequence, or its positive-floor extension. The required assumptions remain explicit. This verdict is about correctness of the stated theorem, not an acceptance certificate or an independent determination of journal-level importance.

The restored file is [global_count_recovery.md](../theory_value/global_count_recovery.md). It contains the full model, proof, constants, boundary-dimension case and limitations. No numerical experiment is needed to fill a missing algebraic step of that proof. New numerical recovery runs must be labeled as new runs rather than recovered original raw evidence.

## What I rederived independently

### 1. The actual adaptive field has the required normal block

For frozen Q=q_F, the symmetric Gram derivative satisfies

A_ij=(β_ij+β_ji)/(2Cτ)>0 for i≠j.

On the product of spheres the detached field is 2HF, with H=A−diag(λ), λ_i=f_i^T(AF)_i. Identity-positive scores are constant one on this manifold. Their ambient radial derivatives disappear under projection, so using a constant positive score in the lifted Gram expression does not omit a tangent force.

At a stationary point HF=0. If Fu=0, then every normal perturbation Z=xu^T has zero first Gram derivative. Consequently the score-policy derivative, A's derivative and λ's derivative vanish in this direction, and DG[Z]=2HZ. This is an invariant tangent block. A negative eigenvalue of H is therefore a real negative restoring eigenvalue of the closed-loop field, even though its full Jacobian can be nonconservative. Linear stability implies H PSD.

This verifies the needed feedback step rather than assuming that the whole adaptive process minimizes the frozen risk.

### 2. The dimension boundary is covered

At rank F=d=C−1, stationarity implies rank H≤1. Its strictly positive off-diagonal entries rule out a negative rank-one matrix for C≥3: three real nonzero entries cannot have negative pairwise products. A full-row-rank stationary F when d≥C is impossible, because HF=0 would force H=0 contrary to strict off-diagonal positivity.

Thus d≥C−1 is justified; an unproved unused-feature direction was not silently assumed in the full-rank boundary case. Positivity uses the complete other-class candidate set and full-support policy. This argument is not a theorem for an arbitrary sparse candidate graph or general multiview stress.

### 3. The stable-point certificate has the correct sign and normalization

With the simplex Gram X_*, H PSD, HF=0 and equal diagonals give

tr[A(X_*−FF^T)]=tr(HX_*)≥0.

Using the symmetric A definition, this is precisely

mean_i sum_j β_ij(s_ij−r)≤0,

after multiplication by the positive τ. No anchor factor, factor of two, or off-diagonal duplication is missing.

### 4. The finite-count domination is exact

Tagging one of K iid positions gives

β_j=Kq_jz_j E[1/(1+z_j+S_{K−1})].

For π_j=q_jz_j/μ and z_j∈[b,1], reciprocal Jensen yields the pointwise bound

β_j/π_j≥Kμ/[1+z_j+(K−1)μ]≥Kb/[2+(K−1)b]=ρ_K.

The second inequality increases in μ and decreases in z_j. Also sum β<1. Hence β−ρ_Kπ is coordinatewise nonnegative with mass at most1−ρ_K. The score lower bound s−r≥−(1+r), combined with the certificate, yields the claimed finite-K upper bound on the π-weighted score deviation.

This is stronger than merely asserting that β tends to π as K grows. The constant is neither a fitted coefficient nor dependent on an unproved uniform approximation.

### 5. Global effective hardening follows from the actual premise

Because the raw easy-slope budget γ is nonnegative, the uniform mixture can only dilute its negative log derivative. Thus the effective weight v_i has log derivative at least α=(1−γ)/τ. Keeping the realized row normalizer fixed when comparing the auxiliary v_i(s) values is legitimate; it is not a claim that the policy normalizer can be ignored in DG.

The likelihood-ratio ordering follows from v_i(s)e^{−αs} being nondecreasing. The tilted probability of each candidate is at least e^{−2t} times its uniform probability for t≥0. Minimizing squared deviation from a constant therefore bounds tilted variance below by e^{−2t} times uniform variance. Integrating the tilted-mean derivative gives c_α=(1−e^{−2α})/2, as stated.

The entire score range is essential. A local slope at the simplex cannot replace this hypothesis.

### 6. Geometry, robust radius, and the integer count agree

The row identity m_i−r=f_i^TS/(C−1) gives

A_0=||S||²/[C(C−1)],

and mean_i(m_i−r)²≤C A_0/(C−1). Since c_α≤1/2, the bound on A_0+c_αV implies exactly the claimed mean off-Gram MSE M/K.

Each off-diagonal Gram error is counted twice. Therefore the maximum pair error is bounded by sqrt[C(C−1)M/(2K)], not the looser version lacking that factor of two. The robust-radius expression and strict no-collision criterion K>M(C−1)^3/(2C) follow.

I independently recomputed the representative constants with standard-library arithmetic:

| C | τ | γ | M | Strict count threshold | First guaranteed integer K | Radius lower bound at4096 |
|---|---:|---:|---:|---:|---:|---:|
|4|1|.9|101.3454657960717|342.040947061742|343|.688489068408062|
|6|1|.9|121.6145589552860|1266.818322450896|1267|.516063301384519|

These are sufficient bounds and are not claimed to equal the actual transition.

### 7. Positive-floor improvement is valid, with its changed premise explicit

For positive continuous ω, its max/min ratio is finite. The omega component's share is at most

ρ_max=(1−ε)R_ω/[ε+(1−ε)R_ω].

Replacing γ by γ_eff=γρ_max is valid whenever γ_eff<1. The raw γ<1 restriction must first be dropped for this extended statement. Raw γ=1 with positive floor is included, but raw γ>1 does not universally imply failure: this remains a sufficient criterion, not a necessary-and-sufficient global policy classification.

## Inherited tools and what this audit does not establish

I reopened the primary Behnia–Thrampoulidis2024 text, Sections II–III-C, and the Boumal–Voroninski–Bandeira2016 text around its rank-deficient second-order argument. Convex Gram KKT/stress and unused-normal negative curvature are established tools. The adaptive zero-response block check and finite-count recovery chain must not be confused with inventing those tools. These primary reads do not establish exhaustive novelty of the complete result.

The mathematical audit supports a global equilibrium statement outside a merely local reference analysis. It does not prove all trajectories converge, exclude cycles, establish practical safe counts, or verify general shared neural networks. In particular, a small computed field norm only identifies a numerical stationary candidate; it is not automatically a stability certificate. Any recovery report should keep those distinctions.

The previous conversation reports extensive original experiments and independent reviews, but their missing unpublished raw files are not evidence newly recovered by this audit. Preserved published checkpoint results may be used with their existing provenance. New executions and new mathematical reviews need their own dates and output files.

