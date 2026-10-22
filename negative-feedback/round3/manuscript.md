# When Can More Negatives Repair a Contrastive Update?

## Local rescue laws and their conflict with augmentation alignment

Research manuscript, 22 October 2026. All principal results below have proofs or executed computations. This is a local population theory with controlled learning checks, not a claim about natural-image accuracy or generic semantic information erasure. The fixed publication comparator is JMLR; a separate review evaluates whether the contribution meets that bar. Earlier four-state results are retained as prerequisites, not presented as new in this round.

## Abstract

Increasing the number of negatives changes more than the precision of a contrastive gradient estimate: it changes the population update, and with a representation-dependent sampler it changes the response to representation perturbations. We ask a sharper question: when can increasing the negative count ever repair an unstable representation direction? For an exchange-balanced affine score direction and a uniform/exponential mixture policy, we prove an exact necessary and sufficient condition for finite-count rescue. Below a mode-dependent critical uniform floor, every finite count is unstable, including the critical boundary; above it, the direction has at most one unstable-to-stable transition. The result permits multiple score levels and continuous populations, with realizations on products of spheres. A different result applies to stationary score-regular class geometries: the positive-graph gap required to maintain within-class normal alignment strictly increases with the iid negative count. The two conditions can oppose each other. For four semantic states with multiple observations, we derive the entire added view spectrum and certify a full local-stability window of exactly 5 through 11 negatives under a natural monotone sampler. A shared multilayer encoder obeys the same joint-denominator predictions at a controlled reference. Ordinary warmup fails the prespecified reference-applicability check; no typical-training claim follows. Matched correlated-sampling constructions show why pairwise sampling summaries cannot extend the iid law. Finally, endpoint analysis rejects the stronger interpretation of the original four-state threshold as an information-loss boundary.

## 1. Question and contribution

There are three logically different explanations for an unstable contrastive representation. A fixed objective may prefer a different geometry; a sampler that responds to the current representation may introduce a destabilizing derivative; or the representation may not receive enough sampled negatives to realize a favorable limiting update. These explanations imply different responses. Increasing the count is justified by the third explanation, may fail under the second, and can conflict with positive-pair alignment under the first.

This paper does not introduce a sampler or an auxiliary loss. Its proposed contribution is a conditional classification of those explanations:

1. A mode-specific rescue criterion determines whether **any finite iid count** can stabilize an exchange-balanced energy direction. The limiting curvature alone is not the result: the finite-count necessity, exact zero-boundary conclusion, and prohibition of stable-to-unstable re-entry require additional arguments.
2. A separate count-ordering theorem identifies an increasingly stringent positive-graph requirement in normal view directions, beyond a four-class example. This mechanism also exists for a frozen sampler.
3. A full spectrum in a realizable multiview model combines these effects into a certified bounded stability window. The two boundaries concern different directions; this is not a failure of the first theorem.

The reader should learn when “use more negatives” can and cannot repair a specified local geometry, and why connected positives alone do not establish local stability. We do not refute downstream bounds that explicitly assume aligned positives, and we do not equate local imbalance with information erasure.

## 2. Related work and exact exclusions from novelty

Perdomo et al., *Performative Prediction* (ICML 2020), established the importance of distinguishing optimization on a fixed distribution from feedback through a model-dependent distribution. Differentiating an expected detached update into a frozen part and a response part is an application of that principle, not our contribution. Hard-negative and shortcut analyses already show that changing negative relations changes which features are favored. Robinson et al., *Can contrastive learning avoid shortcut solutions?* (NeurIPS 2021), defines feature suppression distributionally and establishes that contrasting on shared features can alter suppression at global optima. Our local, count-indexed spectrum does not newly establish that negatives matter for features.

Awasthi, Dikkala and Kamath, *Do More Negative Samples Necessarily Hurt in Contrastive Learning?* (ICML 2022), analyze population optima and generalization under their distributional assumptions. Their optimal-geometry conclusions are not a statement about the Jacobian of a detached representation-dependent policy at an arbitrary equilibrium. Conversely our local instability results do not contradict their global-optimum claims. Tschannen et al., *On Mutual Information Maximization for Representation Learning* (ICLR 2020), already demonstrate important consequences of non-iid negatives. We claim neither that negative dependence was previously ignored nor that our correlated construction establishes a new general dependence principle.

HaoChen et al., *Provable Guarantees for Self-Supervised Deep Learning with Spectral Contrastive Loss* (NeurIPS 2021), and Tan et al., *Contrastive Learning Is Spectral Clustering on Similarity Graph* (ICLR 2024), make spectral and attraction/repulsion structure central. Graph diagonalization in Section 5 uses established tools. The additional claim is the exact monotone dependence of a required local graph gap on the iid count, followed by its intersection with the opposite count condition in a different block.

Zhang, Wang and Wang, *An Augmentation Overlap Theory of Contrastive Learning* (JMLR 2025), derives downstream guarantees under augmentation overlap and an explicit alignment condition. Li and Neuman, *Consistency of Augmentation Graph and Network Approximability in Contrastive Learning* (JMLR 2026), analyzes graph approximation and network realizability. Our analysis asks whether a declared aligned equilibrium is locally dynamically maintainable; it does not invalidate their conditional guarantees. Additional recent geometric and statistical comparisons, and the exact original versions inspected, are in [the source audit](journal/source_audit.md) and [graph audit](journal/graph_extension_audit.md).

The mathematical aggregation principle used below is also established. Athey, *Characterizing Properties of Stochastic Objective Functions*, §3.3.1, Corollary 5.3, gives preservation of single-crossing under monotone likelihood-ratio changes. Our application-specific work verifies the score crossing and inverse-denominator ordering for the contrastive field. Neither MLR aggregation nor the ordinary graph Laplacian is claimed as new mathematics.

## 3. Model, observations and interpretation

Let candidates have base law p. A scalar representation path has candidate scores s_delta=s+delta h and positive score one. Scores and h are bounded, E_p[h|s]=0, and E_p h²>0. The affine path and conditional balance are active assumptions, not generic properties of learned representations. The policy is

\[
q_\delta(dy)=\left[\epsilon+(1-\epsilon)e^{-t s_\delta(y)}/Z_\delta\right]p(dy),\qquad
Z_\delta=\mathbb E_p e^{-t s_\delta},\quad 0<\epsilon<1,\ t>1.
\]

It is an **easy-negative exponential policy** mixed with a uniform/base floor. Conclusions are not automatically claims about hard-negative mining, arbitrary policies, or a differentiated-through sampler. Given K conditionally iid negatives, set

\[
\ell_{K,\beta}=\log\left(\beta+\sum_{r=1}^K e^{s_\delta(Y_r)-1}\right),\qquad \beta\ge0.
\]

Beta=1 is the identity-positive joint InfoNCE denominator and beta=0 its decoupled version. The scalar update is G_K(delta)=E_(q_delta^K)[partial_delta ell], holding the policy fixed inside that partial derivative. Its restoring derivative is H_K=G'_K(0): positive means attraction for dot-delta=−G_K. A frozen policy uses q_0 at every perturbed delta; the adaptive policy recomputes q_delta. All support probabilities remain positive.

A scalar curvature is not automatically an eigenvalue of a full representation dynamics. When a geometric realization is stationary and its energy-transfer subspace is invariant, its sign is a genuine local restoring sign; a coordinate/metric factor may change the rate. Theorems below label directional and full-spectrum conclusions separately. Population results are not finite-sample convergence guarantees.

## 4. Which energy directions can any iid count rescue?

Define W=e^(s−1), S_n=sum_(r=1)^n W_r for iid reference-policy W_r, and

\[
f_n(x)=\mathbb E(x+S_n)^{-1},\quad
R_n(x)=\mathbb E(x+S_n)^{-2}/f_n(x),\quad
\rho(W)=\frac{(1-\epsilon)e^{-ts}/Z}{\epsilon+(1-\epsilon)e^{-ts}/Z}.
\]

**Proposition 1 (exact curvature).**

\[
\frac{H_K}{K}=\mathbb E_q\!\left[h^2W f_{K-1}(\beta+W)
\{1-t\rho(W)-W R_{K-1}(\beta+W)\}\right].
\]

**Proof.** With D=beta+sum W_r and A=sum W_r h_r, the differentiated loss gives sum W_r h_r²/D−A²/D². The tuple-policy derivative contributes (A/D)(−t sum rho(W_r)h_r), since conditional balance gives Z'_0=0. Conditional on all scores, independent draws have zero conditional mean h, so every cross-draw product vanishes. Selecting one tagged draw yields the formula. This argument remains valid when sampled candidates happen to be equal: the original draws are independent. Boundedness justifies differentiating the finite tuple integral. QED.

Write a_n(W)=1−t rho(W)−W R_n(beta+W).

**Lemma 1 (three orderings).** For positive bounded W: (i) a_(n+1)(W)>a_n(W); (ii) a_n(W) has at most one score sign crossing, from negative to positive, except that a_0<0 everywhere when beta=0; (iii) f_(n+1)(x)/f_n(x) is strictly increasing in x.

**Proof.** Let m_j(x)=E(x+S_n)^−j. Then (m_2/m_1)'=(−2m_3m_1+m_2²)/m_1²<0 by Cauchy–Schwarz. Adding an independent positive shift gives (i). For (ii), put T=1−W R_n. Differentiating and applying the same moment inequality gives W(WR_n)'≤T(1−T). At a zero, T=t rho, and W a'_n≥t²rho(1−rho)−T(1−T)=(t−1)T>0. All zeros are strict upward crossings; the small- and large-W limits establish the sign pattern. For (iii), (log f_n)''=(2m_3m_1−m_2²)/m_1²>0. Thus f_n(x+z)/f_n(x) increases in x for every z>0. Averaging over the added W gives (iii). Full exceptional-case and endpoint details are in [the complete proof](foundations/multilevel_theorem.md). QED.

**Theorem 1 (no re-entry and exact rescue floor).** If H_K≥0, then H_(K+1)>0. Furthermore, define

\[
Q=\epsilon\mathbb E_p[h^2e^s]
 -(t-1)\frac{1-\epsilon}{Z}\mathbb E_p[h^2e^{(1-t)s}].
\]

There exists a finite count with positive curvature **if and only if Q>0**. If Q≤0, H_K<0 for every finite K, including the critical case Q=0. Thus a stable-to-unstable transition is impossible in this direction, and no finite count can repair a subcritical mode.

**Proof.** Use the positive measure dnu(y)=h(y)²W(y)q_0(dy). Moving from n to n+1 tilts dnu f_n(beta+W) toward larger W by Lemma 1(iii). Because a_n has a single upward sign crossing, this tilt preserves a nonnegative integral: pointwise (r(W)−r(c))a_n(W)≥0 at its crossing c. Then the strict pointwise improvement in (i) makes the next integral positive. This is an application of existing MLR/single-crossing comparative statics.

For the rescue criterion, bounded positive W gives K f_(K−1)(beta+W)→1/E_q W, so H_K→e^−1 Q/E_q W. Q>0 therefore suffices. For necessity, a_infinity=1−t rho is increasing with a single sign crossing, while f_n(beta+W) is decreasing. If the unweighted dnu integral of a_infinity is nonpositive, its decreasing tilt is nonpositive as well. The finite margin is strictly smaller by W R_n>0 wherever h²>0, so H_K<0. This also settles Q=0 without extrapolating a numerical limit. QED.

Equivalently the critical floor is

\[
\epsilon_c=\frac{(t-1)\mathbb E_p[h^2e^{(1-t)s}]}
{(t-1)\mathbb E_p[h^2e^{(1-t)s}]+Z\mathbb E_p[h^2e^s]}.
\]

This depends on the derivative of the **particular mode**, not just the score histogram. Beta changes onset counts but not the floor. The infinite-K weighted-curvature computation alone is straightforward; the all-finite-K exclusion and no-re-entry statements are what complete the classification.

### 4.1 Realizations without a capacity or discrete-tie explanation

For m independent Rademacher factors, use unit embeddings with energies 1/m+delta, 1/m−delta, and 1/m in the remaining factors. Then s=m^−1 sum z_j and h=z_1−z_2. Factor exchange proves conditional balance. Hamming and permutation symmetry gives a stationary projected field. Ambient dimension can exceed the number of observations; an inadequate output dimension is unnecessary. Direct product moments give

\[
Z=\cosh(t/m)^m,\qquad \mathbb E[h^2e^{cs}]=2\cosh(c/m)^{m-2}.
\]

To remove the repeated-score-atom explanation, let each factor be uniform on S^(r−1), r≥2, and weight its coordinate group in the same way. Relative dots z_j are iid continuous variables; exchange still preserves s and reverses h. For r=3, M(a)=sinh(a)/a and

\[
\mathbb E[h^2e^{cs}]=2\{M''(c/m)M(c/m)-M'(c/m)^2\}M(c/m)^{m-2}.
\]

The law is non-atomic, yet Theorem 1 applies. For fixed r the critical floor tends to 1−1/t as m grows. This is not a claim that arbitrary asymmetry preserves the theorem. Conditional exchange balance remains necessary for the proof, and the interior energy paths remain injective.

At t=log4, epsilon=.25, the cube with m8 first becomes restoring at numerical count349, while m16 lies analytically below its critical floor and is unstable for **all finite counts**. The distinction demonstrates why a finite search that finds no recovery cannot establish impossibility. In the continuous three-factor S2 product, epsilon=.25 is already below the exact critical floor .2524716321. See [analytic moments and executed checks](foundations/README.md). These rounded onsets are numerical evaluations of a proved ordered law, not interval-certified integer thresholds unless explicitly labeled.

## 5. A count condition in the opposite direction

There are C unit class vectors v_c and m equally weighted views per class. At the reference all views in class c equal v_c. Assume separately: (a) the projected population update is stationary; (b) every anchor has the same score histogram and score-policy row law; (c) expected score coefficients b_cd=b_dc. A transitive geometry alone need not imply (a): three equally spaced vectors on a non-equatorial latitude have equal score rows but a nonradial force. The explicit counterexample is retained in [the general proof](foundations/general_normal_graph.md).

Positives within each class use a symmetric stochastic view matrix P. Negatives are iid with replacement, and b_cd=E[N_d exp(s_cd−1)/(beta+sum N_j exp(s_cj−1))]. Put B_K=sum_d b_cd and R_K=sum_d b_cd s_cd. Let z have zero mean across each class's views and be normal to the span of every v_c. For a view eigenmode Pz=mu z:

**Theorem 2 (normal-view gap and count ordering).**

\[
\lambda_{K,\mu}=\frac{2}{Cm}\{B_K(1-\mu)-R_K\}.
\]

The restoring sign is the same for frozen and updating samplers at the reference. With at least two scores of positive probability, xi_K=R_K/B_K strictly increases with K. The view mode is attractive exactly when its positive-graph gap 1−mu exceeds xi_K.

**Proof.** Every first score derivative is zero in a normal direction, so there is no linear policy response. The negative cross-view quadratic terms average to zero by the classwise zero means. The remaining sphere/radial term is −2R_K/(Cm) times the norm. The positive contribution is 2B_K/(Cm) z^T(I−P)z, yielding the eigenvalue. For count ordering, the tagged identity is b_cd=K q_cd W_cd f_(K−1)(beta+W_cd). Lemma 1(iii) gives an MLR tilt toward larger W, hence toward larger scores, so their normalized mean xi_K strictly increases. QED.

Graph Laplacian decomposition is standard. The additional conclusion is the exact count ordering of the required alignment gap. This theorem concerns an invariant normal block, not all tangent directions at arbitrary geometries. It does not assert that a positive graph has no useful downstream guarantee; it asks whether its aligned reference is locally maintained by this update.

### 5.1 Full spectrum and a bounded window

For four semantic classes c=(a,b) and collapsed reference v_c=(a,b)/sqrt2, write A=e^−1 and B=A². The category counts (U,N,W) have probabilities (u,2v,w), denominator D=1+U+AN+BW, and

\[
b_0=E[U/D],\quad b_1=A E[N/D]/2,\quad b_2=B E[W/D],
\quad B_K=b_0+2b_1+b_2,\quad \lambda_+=b_1+b_2.
\]

Let lambda_b be the factor-balance eigenvalue from the earlier four-state full-spectrum theorem, evaluated for the frozen or adaptive policy as appropriate. Class-mean eigenvalues are precisely the old full spectrum divided by m. For each nonconstant eigenvalue mu of a class's positive matrix, the added modes are

\[
\lambda_{view,normal}=(\lambda_+-B_K\mu/2)/m,
\qquad
\lambda_{view,plane}=(\lambda_+-B_K\mu/2+\lambda_b/2)/m.
\]

There is one in-plane and d−2 normal modes for each class/view eigenvector; dimensions exhaust the complete tangent space. Positive graph terms and sphere projection yield the normal formula; the in-plane first-score curvature and policy response add lambda_b/(2m). The complete derivation, including anchor and candidate contributions, is in [Theorem V1](neural/view_theorem.md). It is also checked against the full independently differentiated field.

For clarity, the sufficient policy conditions used to control every class-mean mode are g≤0, t2/t0≥e, and B w>A v, where Z_omega=omega(1)+2omega(0)+omega(−1), t0=omega(1)/Z_omega, t2=omega(−1)/Z_omega, and g=(1−epsilon)omega'(0)/Z_omega. With eta=−g/v and T_K=1−A E[N/D²]/E[N/D], the balance eigenvalue is lambda_b=A M (T_K−eta), where M=E[N/D]. The [earlier complete class-mean theorem](../round2/theory/theorem.md) proves that these policy conditions make all other nonrotation class modes strictly attractive. Therefore full adaptive attraction modulo rotations is equivalent to **both** eta<T_K and gamma>xi_K, where gamma is the smallest nonconstant algebraic positive-graph gap. The first condition improves with count; the second worsens. Thus the admissible integer counts form one interval, possibly empty, bounded, or unbounded.

For omega(s)=4^−s, epsilon=.3, and P=.95I+.05 Uniform, the lower class-mean threshold is K5. Independent outward interval calculations give

| Quantity | Certified enclosing value / sign |
|---|---|
| xi_11 | .04853516089345359… < .05 |
| xi_12 | .05201103415789361… > .05 |
| limit xi_K | .10347795217711012… |
| full attraction | **exactly K=5,6,…,11** |

This window is not an identity-positive artifact. Use20views per class and the simple cycle channel P(i,i±1)=1/2, P(i,i)=0. Every positive is a distinct observation. Its algebraic gap is 1−sqrt(10+2sqrt5)/4≈.0489434837048464, strictly between the certified xi_11 and xi_12. The same full theorem therefore gives exactly K5..11. A [rational radical certificate](journal/zero_self_cycle_certificate.json) verifies the inequalities, and a separately executed80-observation normal-mode gradient check agrees at K11/12 for both policies (maximum vector residual8.40e−12). The560-dimensional inertia is calculated from the proved spectrum; a full560-dimensional numerical Jacobian was not evaluated.

The upper failure is present for frozen policies too; attributing it to sampler feedback would be incorrect. The lower boundary is a semantic balance direction and the upper a within-class view direction. The example does not violate Theorem 1's no-re-entry result for one fixed mode.

## 6. Executed validation and falsification

All protocols precede their corresponding execution or explicitly record an exploratory construction. Seeds, raw arrays, environments and commands are linked in [reproduction](reproduction.md). Counts of checks are audit coverage, not evidence of importance.

### 6.1 Checks of the population formulas

Multilevel laws were checked on 18432 settings and separate ordered-tuple finite differences; no forbidden sign transition was found. This does not prove an unsearched generalization. The continuous S2 product was checked by its exact conditional density and separate two-dimensional tuple calculations; refinement changes curvature by at most 1.07e−15 and tuple finite differences differ by at most 5.89e−12. Full view spectra with uniform, cycle and path positive matrices match differentiated population fields at errors below 2.3e−10. A second reviewer implemented exact rational interval arithmetic without importing the author's certificate and independently enclosed all four K4/5 and K11/12 boundary signs.

### 6.2 Same-objective shared encoder test

A 16→64 tanh→8 normalized encoder has all layers trainable and full output-tangent rank at the controlled reference. It uses the **joint K-negative InfoNCE** expectation and nonidentity positive views. This replaces the earlier one-negative neural comparison, which could not test the count theorem. The initialization is an oracle realization of the reference; it is a mechanism control, not an unsupervised discovery procedure.

At positive mixing .05, held-out confirmation seeds reproduce the predicted local behavior:

| K | Updating policy | Matched frozen policy | Tested interpretation |
|---|---|---|---|
| 4 | balance-mode perturbation grows | same mode contracts | policy-response lower boundary |
| 8 | tested slow modes contract | tested slow modes contract | interior of stable interval |
| 16 | normal view perturbation grows | same mode grows | positive-graph upper boundary |

Twenty-one parameter-flow runs, including step-refinement checks, meet their recorded criteria. An ordinary, unpreconditioned nonlinear DOP853 parameter-gradient solve at K16 gives mode amplification 20.08552181/20.08555197 (frozen/adaptive), compared with exp(3)=20.08553692; the relative error is below 7.6e−7. This removes the alternative that the displayed effect is created by the discretized integration method. A reviewer separately reruns it with comparable error. It remains a **local** test near the constructed reference.

The ordinary-warmup arm is a negative result. All three prespecified initializations fail the square applicability gate, including the independent confirmation seed. Their later outcomes therefore cannot be presented as a verification of the square K5 threshold. This limits claims about commonly visited representations; changing warmup until the gate passes would invalidate that arm.

A reviewer-triggered second ordinary arm used the same seeds, step sizes and warmup length with the new weak positive channel P=.95I+.05U. All three initializations again fail applicability. The18outcomes show an exploratory increase in adaptive view variance from K8 (.0346–.0441) to K16 (.0633–.0708) on all three reused seeds, but the final Gram errors remain .0434–.0564 and .0745–.0830 respectively. Without a stationary applicable reference or an independently predicted local field at those endpoints, this ordering is **not** an exact-window replication. It is preserved as a scope result, not promoted to confirmation.

### 6.3 Endpoint analysis rejects the original harm interpretation

The four-state nonlinear rectangular family is v_ab(theta)=(a cos theta,b sin theta), with balanced theta=pi/4. At K4, the attracting branch has theta=.7545192717973 and weak energy .46914073346, close to .5. At every interior angle the representation remains injective and each factor is exactly recoverable without noise. Under a declared isotropic Gaussian readout-noise model, optimal weak-factor accuracy at sigma .2 is .99969225 versus .99979652 at balance. Six separately seeded nearby flows at each of K1,4,5,8 verify their endpoint predictions; these are not global random-start basin estimates.

K1 has a genuine coarse local attractor. Its full tangent spectrum and an open attracting neighborhood modulo rotations can be proved. However, its first-score sampler derivative is zero, so it also exists for the matched frozen policy. Neither observation supports calling the K4/5 boundary a generic feedback-induced information-erasure transition. We explicitly withdraw that interpretation rather than using a noisier metric to manufacture it.

### 6.4 An iid assumption boundary

Consider four independent source draws, replicated with block sizes (5,3,2,2) or (4,4,3,1), then uniformly shuffled into K12 positions. For every representation the one-position and two-position laws match: both have total squared block size42. Their unique-state-set distributions match too, since both depend only on the same four iid source draws. Yet the joint weighted denominator laws differ.

At the square, an explicit smooth monotone policy can match reference values while placing its slope between the two resulting balance thresholds. Exact rational enclosures certify a threshold separation greater than .005953527687868222030768; the two restoring signs are opposite. Full-field finite differences and an independent reviewer confirm the signs. The slope is **constructed using the thresholds**, not selected by an undisclosed search or independently confirmed by random seeds. This counterexample shows that neither count, pairwise ESS nor even the unique-set distribution is sufficient to extend Theorem 1 to dependent tuples. The general fact that nonlinear denominators can depend on higher joint laws is already known; this is an explicit limitation of our count law.

## 7. Scope, failure conditions and present contribution

Theorems 1–2 classify local restoring behavior in declared families. The first requires affine scores, conditional exchange balance, a uniform/easy-exponential mixture, bounded scores, and iid negatives; it does not cover arbitrary heterogeneous anchor laws or nonlinear score paths without extra terms. The second requires a stationary score-regular geometry, symmetric coefficients and positive channel, and an ambient normal direction. The full bounded window is proved for the four-class multiview realization, not for arbitrary regular geometries.

The new knowledge, if judged important enough, is that a single “negative sample budget” explanation is incomplete even locally. The exact rescue floor separates insufficient count from an unrepairable policy/mode interaction; the independent view condition shows why restoring one part of the spectrum need not stabilize the representation. A connected graph with too small a gap can fail the latter condition. These claims are grounded in completed proofs and same-objective tests, and require no information-erasure claim to be true.

Two limitations affect the contribution's importance rather than the validity of the proofs. First, ordinary training has not been shown to approach these symmetric equilibria. Second, within-scope imbalance often leaves an injective representation and need not hurt a downstream task. A purely theoretical paper may still be justified by the general classification, but that must be defended on its structural explanatory value; natural-image relevance and top-journal suitability do not follow from the number of computed examples. The independent final review records that distinction.

## Evidence index

- Complete scalar proofs and continuous realizations: [foundations](foundations/README.md).
- General normal block: [proof and stationarity counterexample](foundations/general_normal_graph.md).
- Full multiview proof and actual encoder results: [neural](neural/README.md).
- Endpoint raw results: [branches](endpoints/results/branches.csv), [flows](endpoints/results/endpoint_flows.csv), [coarse lemma](endpoints/coarse_cluster_lemma.md).
- Correlation construction: [protocol](correlation/protocol.md), [rational certificate](correlation/results/rational_certificate.json).
- Independent audits: [multilevel](review/multilevel_proof_audit.md), [window](review/window_proof_audit.md), final six-gate review linked by the round README.
- Primary source and fixed-journal comparisons: [journal](journal/README.md); [verified bibliography](references.md).

This manuscript contains no unexecuted natural-image result, missing theorem filled by expectation, or claim of typical-training success. The final verdict and remaining work are separate from this statement of proved results.
