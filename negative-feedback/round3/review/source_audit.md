# Additional primary-source comparison from the independent critic

Date: 2026-10-22. This file addresses the knowledge increment, not a search-count argument. Search results without inspected bodies are not used to assert absence of overlap.

## Robinson et al.: Can contrastive learning avoid shortcut solutions?

Joshua Robinson, Li Sun, Ke Yu, Kayhan Batmanghelich, Stefanie Jegelka, Suvrit Sra. NeurIPS2021,34:4974–4986. The PMC author manuscript is available since May2022; it is **not a Nature journal paper** merely because a biomedical archive hosts it. [Primary author text](https://pmc.ncbi.nlm.nih.gov/articles/PMC9089441/).

Read: Section2.1 Definition1 and the latent-product setup; Section2.2 Proposition1; Section2.3 Proposition2 and the hardness experiments; Section3's intervention motivation. Their model has independently sampled latent factors and an injective observation renderer. Suppression is equality of conditional representation distributions, while distinguishing requires disjoint supports. This is stronger than small factor-mean energy or a failed regularized probe.

Proposition1 constructs suppressing and distinguishing encoders that both attain the limiting InfoNCE optimum. Proposition2 conditions positives and negatives to share a factor subset and establishes suppression of that subset at the limiting optimum. The hardness study observes feature tradeoffs, motivating an intervention that seeks other discriminative features.

**What is already known for our reader:** sampling relations and instance difficulty change which factors are learned; objective optimality does not ensure every feature is retained; lower contrastive loss can harm a downstream factor. A general claim that negative relationships control semantic learning is therefore insufficiently new. The current exact finite-K closed-loop curvature is not their theorem, but needs an independently important implication beyond reproducing these broad conclusions in a four-state model.

**Material difference:** our current result is local stability of a parameter-dependent negative law, not limiting global minimizer structure under prescribed feature-conditioned sampling. We must not claim it is a direct corollary of Proposition2; nor should we treat the different setup itself as novelty. The unresolved question is whether an exact local threshold yields a new usable understanding when these established results are already known.

## Inspected versus screened endpoints

Ash et al., AISTATS2022, *Investigating the Role of Negatives in Contrastive Representation Learning*, official landing page and abstract were initially retrieved. The proceedings PDF endpoint was rejected by the browsing tool for a39.9MB content length. Later the [primary arXiv HTML, version1](https://arxiv.org/html/2106.09943) was accessible and inspected: setup and Definition1, Theorem1 and its collision/coverage discussion, and AppendixC's two-representation calculation. This is the2021 preprint body, not a verified line-by-line match to the final AISTATS2022 PDF. Its fixed negative distribution and loss-to-downstream transfer concern neither a changing sampler nor an adaptive-field Jacobian. Its finite-K preference reversal example is not a classification of the trained optimum. Those scope limits are material; we must not attribute all later interpretations of the paper to its theorem. [Final official record](https://proceedings.mlr.press/v151/ash22a.html).

Searches for correlated/duplicated negatives found negative-count, conditional-sampling, correction and diversity papers, but no exact matching local closed-loop formula was established from those searches. This is **not evidence of novelty**. The obvious algebraic reduction of equal block duplication to the existing denominator-offset theorem is recorded below regardless of search results.

## A control that changes the interpretation without automatically adding novelty

If one negative is repeated K times, its loss is log(beta+K exp(s−1)). At the square its balanced-mode scalar curvature is governed by beta/(beta+K exp(−1)), which decreases with K. The iid-negative threshold instead increases with K. Thus 'count' must specify the negative joint law, not merely the number of denominator terms.

Equal groups of r copies of M iid draws are algebraically log r plus the existing M-negative loss with offset beta/r. Their threshold is exactly T_(M,beta/r). This is a direct corollary of round2's offset result and should not be advertised as a separate fundamental theorem. It is a decisive control against an explanation based only on larger denominators. More general correlation statements, or useful predictions beyond an effective-count heuristic, would need independent evidence and originality assessment.

## Tschannen et al.: On Mutual Information Maximization for Representation Learning

ICLR2020. [Inspected primary PDF](https://arxiv.org/pdf/1907.13625). Read Section4's negative-sampling discussion and AppendixD's non-iid argument. They show that dependent negative batches can invalidate the usual InfoNCE mutual-information bound even when the individual distributions remain unchanged. Their example shares a Gaussian latent variable across a batch. They also distinguish true information from representation geometry and readout quality.

Therefore 'the negative joint law matters, not only marginals/count' is established knowledge. A new same-pairwise/opposite-attraction construction could make a stronger quantity-specific insufficiency statement, but cannot claim to discover that dependence matters. Their MI-bound analysis does not itself classify the local response Jacobian, so a direct-corollary allegation is also unjustified.

## Ochieng: Diversity Is All You Need for Contrastive Learning

NeurIPS2025. [Official proceedings record](https://papers.nips.cc/paper_files/paper/2025/hash/f8792f6177801b9df2a10478682e9017-Abstract-Conference.html), [inspected arXiv full text](https://arxiv.org/html/2510.05767v1). Inspected Section1.2, Section2.3's independence caveat, and AppendixA. The analyzed object is a gradient-norm band involving alignment, count and batch second moments, with empirical dependence qualifications. This is not an exact adaptive-Jacobian-sign classification. The current pair-matched construction does not refute such a norm bound: both fields can be stationary while their derivatives have opposite signs. We do not infer a theorem's validity merely from publication, and do not need to adjudicate all of this paper's bounds to make that object distinction.

## Round3's pair-matched correlation construction

Root supplied multiplicities(5,3,2,2) and(4,4,3,1),K12,source count4,sum of squares42. With a final uniform shuffle they have the same one-position and two-position law for every q_F: the same-source probability is30/132. Their sampled-state-set distribution is also identical because each is generated by four iid source states. Their higher-order weighted counts differ.

The root's exact finite-sum thresholds differ, and a response slope selected between them produces opposite scalar stability signs. `correlation_check.py` independently evaluates the ordered four-state source tuples and the direct angular derivative. It agrees with the positive and negative analytic curvatures within1.12e-11. It also verifies monotone score weights by the exact endpoints of the quadratic log-derivative, not only a grid.

This is a stronger and correct insufficiency construction than the duplicated-negative control. It still faces a substantive novelty/importance question: a nonlinear log-sum can depend on higher-order joint law even when lower-order summaries match. One must explain which scientifically used inference the exact local counterexample changes, or supply a broader structural characterization and decisive learning evidence. The verified signs alone do not answer that question or establish semantic harm.

## Awasthi, Dikkala and Kamath: Do More Negative Samples Necessarily Hurt In Contrastive Learning?

ICML2022, PMLR162:1101–1116. [Inspected final proceedings PDF](https://proceedings.mlr.press/v162/awasthi22b/awasthi22b.pdf). Read setup, Theorems3.5/3.8, Claim3.9 and its Jensen argument, Section3.3, and the AppendixA proof route. Negatives use a fixed marginal; positive pairs share a latent class. Under disjoint uniform classes, every logistic population minimizer is a class-collapsed simplex ETF, independent of negative count. The paper distinguishes an actual optimizer statement from an all-representation error bound or two-function preference reversal. No parameter-dependent sampling law or local adaptive Jacobian is analyzed.

This is an especially important competing reader account for round3: nondegradation with more negatives is already known in one global-optimum framework. A bare statement that more iid negatives cannot hurt is not a new contribution. The new multilevel result instead concerns a local mode of a detached adaptive update, permits no rescue at any finite count, and proves an exact floor criterion. These are not direct consequences of the fixed-distribution optimizer theorem. Conversely, local directional attraction does not inherit that paper's downstream or global-optimum consequences. Its proof uses convexity/Gram structure, whereas the new sign-order proof uses tagged inverse moments and a likelihood-ratio tilt. Different proof tools alone do not establish importance; the finite-count rescue classification is the knowledge increment to assess.

## Zhang, Wang and Wang: An Augmentation Overlap Theory of Contrastive Learning

JMLR26(228),2025. [Inspected author arXiv full text](https://arxiv.org/html/2511.03114v1). Read setup, Theorem10, Corollaries11/12, and the proof route using graph paths and alignment. The class-graph theorem assumes an already epsilon-aligned encoder, connectivity and label consistency; it then controls downstream risk using graph radius or spectral quantities and a finite-negative term. Its main denominator excludes positives, so its objective must not be silently equated with beta1 InfoNCE here.

The proposed round3 positive-graph window analyzes whether an exactly class-collapsed equilibrium is locally attracting as negative count changes. This is neither a direct corollary nor a counterexample to that JMLR theorem. In particular, connectedness alone not ensuring attraction does not refute a theorem that explicitly assumes alignment. The possible knowledge increment is a dynamical feasibility boundary for that desired geometry, coupled to a distinct adaptive balance mode. The upper boundary also occurs for the matched-frozen sampler and must not be attributed solely to feedback. Standard graph-Laplacian spectral decomposition itself is established background.

## Additional modern and landscape checks

Luthra, Yang and Galanti, *Self-Supervised Contrastive Learning is Approximately Supervised Contrastive Learning*, NeurIPS2025. [Inspected primary version2](https://arxiv.org/html/2506.04411v2): setup, Theorems1/2, AppendixB's partition bound and AppendixD's unconstrained-feature proof formulation. Their result compares fixed DCL and a label-aware negatives-only supervised loss; its global minimizer is class-collapsed simplex ETF. It does not classify finite-K detached adaptive equilibria or graph-dependent local stability. Global class collapse is already established geometry, not our contribution.

Ziyin et al., *What Shapes the Loss Landscape of Self-Supervised Learning?*, ICLR2023. The final OpenReview PDF was blocked by a challenge. The [inspected original arXiv version1](https://arxiv.org/pdf/2210.00638v1) contains the linear/quartic expansion, stationary-point Theorem1 and its rank discussion in Sections3.1–3.2. Feature/augmentation competition and curvature-based collapse criteria already exist. This version uses a linear small-norm expansion and a normalization surrogate, not the exact normalized finite-K current-sampler field. We do not treat that version as a verified copy of the final paper. The new work needs more than another threshold showing generic attraction/repulsion competition.

## Athey: the sign-preservation principle is established mathematics

Susan Athey, *Characterizing Properties of Stochastic Objective Functions*, August1999 working-paper revision. [Inspected primary author PDF](https://web.mit.edu/athey/www/CPSO99.pdf), Section3.3.1, Corollary5.3 and its proof, printed pages26–27. It characterizes preservation of single crossing under integration by a likelihood-ratio condition, and discusses the monotone-likelihood-ratio/log-supermodularity specialization.

Thus round3's signed aggregation under an increasing density ratio is an application of established comparative-statics machinery, not a new general mathematical principle. The CL-specific content to assess is the derivation of the tagged finite-negative Stieltjes weights, proof that those weights and the exponential-policy margin satisfy the required properties, the all-count no-rescue classification, and their opposing view-mode consequence. Merely applying the old principle to a convenient example would be insufficient; the general score law and realizable families are what can supply additional subject-matter knowledge. This primary check supports attributing the proof tool correctly and does not by itself settle the contribution's importance.
