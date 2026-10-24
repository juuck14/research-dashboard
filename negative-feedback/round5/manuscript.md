# Negative-count recovery of stable representations under adaptive contrastive sampling

Recovered and independently rechecked manuscript, 2026-10-25. The completed global proof was recorded in the interrupted research session; this document restores its argument. Raw files after the earlier GitHub checkpoint were removed during workspace maintenance. The linked recovery experiments are explicitly **new executions**, not purported byte-identical recoveries of those lost outputs.

## Abstract

Adaptive negative sampling can change which class distinctions contrastive learning retains. We prove a quantitative recovery theorem for every linearly stable equilibrium in a balanced finite-class population with unit-normalized, sufficiently expressive features and iid true negatives. A global bound on the easy-negative log-slope gives an explicit O(1/K) mean squared Gram error from the regular simplex. A computable finite count therefore excludes all class-merging stable equilibria and bounds decoder-independent robust class separation. The permitted policy family includes genuinely decreasing and nonmonotone score weights. Conversely, a stronger exponential easy policy with a fixed positive probability floor admits class-merging attractors at every finite count. Exact local stability does not replace the global premise: a smooth policy identical to uniform on an open neighborhood of the optimum still has bad attractors elsewhere. The proof uses a closed-loop stress certificate, exact finite-count tagging and quantitative effective hardening. The guarantee concerns equilibrium geometry, not convergence of arbitrary trajectories, cycles, or general neural-training prevalence.

## 1. Question and prior knowledge

Fixed-distribution contrastive theory identifies class-separated simplex optima in balanced populations. Pair-weight optimization, generic distribution response, easy-negative fixation and fixed-weight low-rank solutions are established knowledge. Our question is more specific: under what global policy condition does increasing negative count force **every stable stationary representation** to retain the correct negative distinctions, and when can a bad endpoint survive every count?

The original square-window quality interpretation failed task/readout checks. A subsequent local-simplex classification also did not answer this global question. An independent reviewer proposed a policy whose local dynamics look safe while another basin merges classes. We constructed that counterexample and continued the research; the global theorem is the additional result that resolves the identified gap. Its importance does not rest on numerical precision or reviewer agreement.

Awasthi et al. (ICML2022) supply fixed-law simplex/count geometry; Jiang et al. (TMLR2025) supply nondecreasing-hardening guarantees. Tian (NeurIPS2022) supplies detached pair-weight structure and a different fixed-weight linear rank-one analysis. Behnia and Thrampoulidis (ISIT2024) and Burer–Monteiro landscape theory supply convex-Gram stress arguments. These tools are inherited. Their fixed-objective or nondecreasing-policy conclusions do not directly constrain every equilibrium of the mildly decreasing adaptive field considered here. [Primary comparison](critic/primary_comparison.md).

## 2. Population, policy and independently justified target

There are C≥4 equiprobable classes with unit-row features F in dimension d≥C−1. Identity positives have score1. Each anchor independently draws K≥1 negatives with replacement from every j≠i; every negative is from a different class and has positive probability. Correct candidate support is a favorable theoretical information condition, not a new unsupervised filtering algorithm.

For τ>0, positive C² weight ω and 0<ε<1,

\[
q_F(j|i)=\epsilon/(C-1)+(1-\epsilon)\omega(f_i^Tf_j)/\sum_{l\ne i}\omega(f_i^Tf_l),
\]

and the joint-K loss is log[1+Σ_k exp((f_i·f_Yk−1)/τ)]. Both embedding occurrences receive gradients; the sampler is detached. Let G be the expected product-sphere gradient and train by −G. A linearly stable stationary point has G=0 and no negative-real-part eigenvalue of DG.

The target is not a chosen binary factor or probe. The supremal feature perturbation radius permitting correct decoding of every class is r*(F)=min_{i≠j}||f_i−f_j||/2. Nearest-prototype decoding achieves smaller radii, while overlap of different-class balls proves the upper bound for arbitrary decoders. Standard simplex packing gives the unique optimal Gram with off score r=−1/(C−1), achieving sqrt[C/(2(C−1))]. The frozen uniform-other-class contrastive risk has the same unique Gram optimum, by established strict convexity and permutation symmetrization. These facts justify the target but are not new contributions.

## 3. Global finite-count theorem

Define the global easy-response budget

\[
\gamma=\max(0,\sup_{s\in[-1,1]}[-\tau(\log\omega)'(s)])<1,
\quad b=e^{-2/\tau},\quad
\alpha=(1-\gamma)/\tau,\quad c=(1-e^{-2\alpha})/2,
\quad M=(1+r)(2-b)/(bc).
\]

**Theorem.** Every linearly stable stationary point in dimension d≥C−1 satisfies

\[
\mathcal E(F)=\frac{\sum_{i\ne j}(f_i^Tf_j-r)^2}{C(C-1)}\le M/K.
\]

Consequently, with E_K=sqrt[C(C−1)M/(2K)],

\[
r_*(F)\ge\sqrt{\max(0,1-r-E_K)/2}.
\]

No such equilibrium merges any two classes if K>M(C−1)^3/(2C). The bound is sufficient and conservative; it is not the minimal transition count.

### Complete proof route

Freeze q at a stationary F. Let A be the symmetric derivative of its convex fixed-q Gram risk and H=A−diag(λ), where λ_i=f_i·(AF)_i. The sphere field is2HF, so HF=0; every off-diagonal H entry is positive. If rankF<d, an unused ambient direction makes all first Gram derivatives zero. The sampler response vanishes on this invariant block and DG equals2H, so stability requires HPSD. If rankF=d=C−1, rankH≤1; a negative rank-one matrix cannot have every off-diagonal entry positive for C≥3. A full-row-rank stationary F is impossible. Thus HPSD also in the boundary case. Testing this certificate against the simplex Gram gives a global score-direction inequality.

For one row set z_j=exp[(s_j−1)/τ]∈[b,1], μ=Σq_jz_j,

\[
\beta_j=Kq_jz_j E[1/(1+z_j+S_{K-1})],\qquad \pi_j=q_jz_j/\mu.
\]

Tagging one negative gives this coefficient exactly. Reciprocal Jensen yields the pointwise bound β_j≥ρ_Kπ_j with ρ_K=Kb/[2+(K−1)b]. Also Σβ<1. Hence β−ρ_Kπ is nonnegative with mass≤1−ρ_K. Combining its worst possible score s−r≥−(1+r) with the stress certificate gives

\[
E_i\sum_j\pi_{ij}(s_{ij}-r)\le(1+r)(2-b)/(Kb).
\]

The effective unnormalized weight v_i(s)=exp[(s−1)/τ][ε/(C−1)+(1−ε)ω(s)/Z_i], with fixed row normalizer Z_i, has log derivative≥α. Its weighted score mean therefore exceeds that of a uniform row exponentially tilted by exp(αs). Variance under tilt exp(ts) is at least exp(−2t) times the uniform variance. Integrating the tilted-mean derivative gives mean_π(s)≥m_i+c V_i.

Write S=Σf_i, A0=||S||²/[C(C−1)], V=mean_i V_i. Then A0+cV≤(1+r)(2−b)/(Kb), and m_i−r=f_i·S/(C−1). Thus

\[
\mathcal E=V+E_i(m_i-r)^2\le V+CA0/(C-1)\le(A0+cV)/c\le M/K.
\]

Symmetry makes each off-score error appear twice, giving the radius bound. A collision contributes at least2C/(C−1)^3 to Gram error, proving the finite no-collision count. [Full self-contained proof](theory_value/global_count_recovery.md).

Dropping the raw restriction γ<1, a positive-floor refinement permits γ_eff=γ(1−ε)Rω/[ε+(1−ε)Rω]<1, where Rω=maxω/minω. Raw γ=1 is therefore eventually recoverable with a fixed positive floor and positive smooth weight. This remains sufficient, not a necessary/sufficient condition for each policy.

## 4. Obstruction and why local tests fail

For ω=exp(−ts),τ1,C=2m, let m class features equal u and m equal−u. If p is opposite-group negative probability, b=e^-2, W~Binomial(K,p),U=K−W, define As=E[U/(1+U+bW)] and Ao=bE[W/(1+U+bW)]. The full nonrotation rates are2Ao/m and[Ao−mAs/(m−1)]/m. All finite counts are attracting iff bp≥m(1−p)/(m−1).

For every t>1, the fixed positive-floor interval

\[
0<\epsilon\le3(e^{2t}-e^2)/[(e^{2t}-1)(1+2e^2)]
\]

suffices for every even C≥4. At t=log4 the upper bound is.109150496499; ε.05 lies inside it. The same finite model has enough capacity for simplex, correct negatives and full allowed support. The exact limiting class-ID accuracy is at most2/C and robust radius0. This is also attractive for its own matched frozen bipartite objective: it is not uniquely a detachment failure. [Published complete proof and observations](global_mechanism/global_collapse.md).

Local simplex stability is exactly η<T_K, with η=−τ(1−ε)(logω)'(r), T_K=1−a/(1+Ka),a=exp[−C/((C−1)τ)]. Its full tangent spectrum is [proved here](theory_value/filtered_full_spectrum.md). It does not imply global safety. For example, a positive smooth weight constant on[−.4,.1] can equal exp(±log4) at scores∓1. It has exactly uniform dynamics throughout an open simplex neighborhood for every C≥4, yet the same all-count bad basin above. For an explicit construction, let h(x)=exp(1−1/x) for x>0 and0 otherwise, a=−.4,b0=.1, g(s)=h((s−b0)/(1−b0))−h((a−s)/(a+1)), and omega(s)=exp(−log4 g(s)). This is positive C∞, constant on[a,b0], and has endpoint ratio16. The global slope assumption is therefore essential to our proof, rather than a stronger interpretation of a local criterion.

## 5. Newly rerun evidence and scope

The recovery protocol fixed t.9,ε.01,τ1,C4/6,d=C,K1/4096,seeds7701/7702, Gaussian and small injective coarse starts, step2 and cap20000 before execution. All16 runs converged at the declared field tolerance. K1 endpoints approached balanced mergers; all K4096 endpoints approached simplex, with maximum Gram MSE3.30e−14. The proved K4096 bounds are MSE≤.02474255/radius≥.68848907 forC4 and MSE≤.02969105/radius≥.51606330 forC6. Two prespecified complete endpoint Jacobians had no resolved negative mode at tolerance1e−6; other endpoints remain converged candidates, not spectrum-certified equilibria.

An independent implementation imports no author oracle. It directly enumerates216 nonlinear-policy configurations, checks separate tagging and all proof inequalities, ten exact stationary controls and twelve normal-block differences. Direct/tagged coefficient error is≤1.39e−16 and normal-block error≤2.96e−13. These checks validate code and algebra, not the all-geometry quantifier by enumeration. [Raw data and commands](reproduction.md).

The guarantee concerns balanced prototype populations, row normalization, iid draws and smooth scalar score policies. It does not assume symmetric current geometry or arbitrary-direction conditional balance. It does not prove arbitrary trajectory convergence, exclusion of cycles, full multiview recovery, shared neural-parameter dynamics or natural-data prevalence. Those extensions may fail without invalidating the stated global equilibrium recovery/obstruction. The existing nonidentity extension supports the bad side only. The new global theorem, rather than a future favorable benchmark, supplies the paper's representative core. Remaining work is exposition, ordinary proof review, references and optional sharper constants.
