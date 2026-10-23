# Primary-source checks for the actual round5 repair

2026-10-23. These checks distinguish known principles from the new candidate, rather than treating any different setting as novelty. The original top50 assessment remains withdrawn while the new claim is tested.

## Luthra, Yang and Galanti, NeurIPS2025

*Self-Supervised Contrastive Learning is Approximately Supervised Contrastive Learning*. [Read primaryv2](https://arxiv.org/html/2506.04411v2). Inspected §3.2 Proposition1, §3.3 Theorem2, AppendixC proof and AppendixD's characterization.

The few-shot NCC/linear-probe bound already uses directional class-normalized variance and label-count-scaled full variance. Its optimum theorem gives augmentation/class collapse and simplex geometry for its supervised negatives-only objective. Thus nuisance acquisition causing finite-label costs is a known explanatory route, not a new contribution merely because a new sampler produces the nuisance. However its fixed objective/global optimizer analysis does not state the detached adaptive finite-K Jacobian or classify harmful attractors of the new field. A task-utility experiment must add a distinct learning conclusion, not call this theorem a failure.

## Awasthi, Dikkala and Kamath, ICML2022

*Do More Negative Samples Necessarily Hurt In Contrastive Learning?* [Read published PDF](https://proceedings.mlr.press/v162/awasthi22b/awasthi22b.pdf). Inspected Assumptions3.1/3.6, Theorem3.5, Theorem3.8, Claim3.9 with the Jensen proof, §3.3, and AppendixA.2.

Their fixed marginal sampling and class-conditional-positive setting has class-collapsed simplex optima independently of K. Claim3.9 symmetrizes Gram scores and then uses their attainable average bound. Reproving simplex optimality for a symmetric frozen conditional sampler is a nearby extension of that existing argument. It is a baseline, not an independent discovery. A detached adaptive policy that repels this same meaningful target is a different question; neither the fixed-objective global theorem nor an upper-bound preference reversal implies its answer.

## Jiang et al., TMLR2025

*Hard-Negative Sampling for Contrastive Learning: Optimal Representation Geometry and Neural- vs Dimensional-Collapse*. [Read primaryv3](https://arxiv.org/html/2311.05139v3). Inspected §3, §4 Theorems1–3 and proof route, §5.3–5.6. ThearXivmetadata and rendered body dates differ, as already recorded in round2; no new publication revision is inferred from that mismatch.

Nondecreasing hardening functions give global loss/geometry guarantees; the experiments already connect hardness, normalization, dimensional collapse and initialization. The candidate cannot claim discovery that sampling and optimization affect rank. The proposed easy-negative policy has the opposite monotonicity, and detached joint-K local attraction is not the analyzed global objective. Existing results therefore supply competing knowledge and an important sign restriction, not the claimed all-K failure theorem.

## Robinson et al., ICLR2021

*Contrastive Learning with Hard Negative Samples*. [Read primary published-version PDF](https://arxiv.org/pdf/2010.04592). Inspected §3 equations2–5, §4 Theorem4, AppendixA.1–A.2 and implementation discussion in AppendixD.

The paper explicitly conditions on true-negative support and uses exponential hardness with nonnegative hardness; its large-hardness minimax optimum separates classes. The practical objective is importance-reweighted and must not be silently equated with a detached discrete sampling update. True-negative conditioning and exponential reweighting are established ingredients. What requires fresh verification here is the combination of a semantically safe support, fixed positive floor, every finite count, unstable task-optimal geometry and stable class-merging attractor. That combination is not a direct conclusion of the inspected theorem.

## Meng et al., ICLR2026

*SnaPhArd Contrast Learning*. [Read published PDF](https://proceedings.iclr.cc/paper_files/paper/2026/file/42a24a7a3e7cf7dd127a76daf487cffd-Paper-Conference.pdf). Inspected §2.2.1 Theorem2.1, Remark2.3, Lemma2.4 and AppendixA.1.1.

Its symmetry condition concerns a single variable query with fixed positive/negative keys, and “collapse” there is query equals its sole positive. The remarks already describe easy negatives as fixation forces. Neither this observation nor its negative-count gradient-norm bound establishes all-encoder semantic class merging or the detached response at a simplex. Therefore “easy negatives can collapse” is old intuition and insufficient as a title-level novelty claim; the meaningful all-K obstruction must be stated and supported more precisely.

## Tian et al., NeurIPS2020

*What Makes for Good Views for Contrastive Learning?* [Read primaryv3](https://arxiv.org/pdf/2005.10243). Inspected §3.1–3.3 Definition3/Proposition3.1 and AppendixA.2. Task-dependent sufficiency and preserving relevant information while removing nuisance are already explicit. The new candidate needs a declared task-neutral utility or direct class-identity information loss; it cannot derive importance from an arbitrary preference for the original two factor coordinates.

## Immediate consequences for review

The former square-window paper does not acquire importance by adding a finite-label curve. The regular-simplex repair is stronger because its goal has a task-neutral justification and a fixed-risk global-optimum baseline. It still needs the actual adaptive result, and a class-merging/no-rescue extension would materially strengthen it. If both are valid, the review must reassess the resulting **domain-specific limitation theorem**, rather than dismiss it because its proof uses known mathematics. Conversely, none of the above sources prove the absence of some closer paper elsewhere; source coverage is not exhaustive.

## Two additional possible reductions, checked after the class-merging repair

### Tian, NeurIPS2022

*Understanding Deep Contrastive Learning via Coordinate-wise Optimization*. [Published PDF](https://papers.nips.cc/paper_files/paper/2022/file/7b5c9cc08960df40615c1d858961eb8b-Paper-Conference.pdf). Inspected §3 Theorems1–2, the stop-gradient and hard-negative discussion after equation7, and §4.2–4.3 Theorem3 with its distinct-top-eigenvalue caveat.

This is a particularly strong competing explanation: contrastive updates already admit detached, representation-dependent pair weights; holding those weights fixed can yield rank-one optima in normalized deep linear networks. Therefore neither a detached weight response nor a rank-one endpoint is new by itself. Its rank-one theorem concerns global layer/Frobenius norm constraints and a fixed contrastive covariance, rather than unrestricted row-normalized class embeddings. It does not supply the new candidate's sharp finite-K simplex response, or an all-K class-merging attractor despite true-negative support and full class capacity. Those are the additional conclusions that must survive; merely renaming its fixed-weight PCA collapse would fail the novelty gate.

### Lee, Chang and Sohn, AISTATS2024

*Analysis of Using Sigmoid Loss for Contrastive Learning*. [Primary PDF](https://arxiv.org/pdf/2402.12613). Inspected §3.1 equation2, Definitions1–2, §4's CCEM formulation and §5's temperature-dependent optimum result. In their Definition2, antipodal means every first-view embedding equals the negative of every second-view embedding: positive pairs point oppositely, with each modality individually collapsed. This is a fixed sigmoid-loss optimum under two separately variable embedding sets. It is a real precedent for meaningful degenerate contrastive geometry; “first contrastive antipodal collapse” would be false. It does not establish a balanced two-group partition of semantic classes in a shared encoder under detached adaptive InfoNCE, nor its all-K attraction and same-law optimum instability. The semantic content of “antipodal” must not be confused across these settings.
