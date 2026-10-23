# Does the stability window identify valuable few-label representations?

2026-10-23. This branch executes a task-based attempt to repair the importance gap. It does not change the frozen JMLR bar. The original window-as-quality framing fails this test as a universal preference; a different optimum-destabilization framing must be judged separately.

## 1. A task family that does not privilege the square

Four equally weighted positive classes admit three distinct balanced binary partitions, written a,b,ab. Use all three with equal weight. They are permuted by class relabeling, so this objective does not select the originally named two factors after seeing results. Labels remain constant on positive classes. Train on one or two views per class and evaluate only the held-out views, enumerating all256/1296 support sets.

The primary readout is affine ridge with fixed lambda.01. Lambda0 and.1 are sensitivity controls, not selected by test performance. This target is a declared linear-transfer goal, not a universal representation quality measure. The population positive graph is shared by every representation, including the simple graph-component baseline.

## 2. Actual finite-label results

For one support view per class and primary lambda.01:

| Representation | Seed6101 mean task MSE | Seed6201 mean task MSE | Important qualification |
|---|---:|---:|---|
| K4 adaptive | .33359457 | .33359399 | Injective rectangular class geometry |
| K8 adaptive | .33358965 | .33358965 | Numerically near the stable square |
| K16 adaptive | .54126541 | .53626801 | Nonstationary cap endpoints from the saved runs |
| K4 frozen | .80483131 | .78826209 | Frozen initial random policy, not matched final q* |
| K8 frozen | .83370879 | .82124833 | Same caveat |
| K16 frozen | .85094014 | .84106612 | Same caveat |
| Exact square | .33358965 | same | One balanced task has risk1 |
| Positive-graph components → simplex | .00084834 | same | No additional downstream labels in representation construction |

The K4-vs-K8 difference is only4.3–4.9e-6. Thus the lower stability boundary does not mark an appreciable learning-quality transition for this fixed task family. The upper K16 penalty is real under this readout, but it does not establish a universal harm or a distinct feedback mechanism.

The component baseline computes connected components of the **same population positive matrix** and assigns centered normalized one-hot codes. It is a population-information baseline, not a finite-positive-sampling guarantee. The exact population oracle used for learning also has access to this matrix. This elementary baseline exposes that the square is not the best use of the supplied information for class-permutation-invariant linear transfer.

Class-mean ablations clarify the familiar tradeoff. Replacing frozen embeddings by their class means and renormalizing gives MSE about.00087/.00093 across counts; removing spread reveals nearly simplex semantic geometry. Adaptive mean-only embeddings remain around1/3 because their class means have a practically missing balanced-task direction. These are diagnostics, not a proposed supervised postprocessing method. Class means use the known evaluation grouping, while the component baseline itself gets grouping from P.

## 3. Failures and contrary readout conditions are preserved

Minimum-norm lambda0 does not preserve the favorable K8 ordering. Seed6101's near-square K8 finite embedding has mean MSE1.13746 with one support view/class and2.56394 with two, versus exact-square1/3. Very small residual coordinates and an unregularized interpolating readout produce a rank-sensitive limit. Fixed positive regularization controls that effect. We do not choose the favorable regularizer after seeing data: the primary and two controls were all fixed first.

Likewise classification accuracy near the square's missing task can depend on tiny prediction signs. The explicit1e-10 tie band is retained rather than changed to clean up the table. Continuous squared prediction risk is primary. None of these diagnostics measures information-theoretic erasure.

## 4. A competing ordinary classification task

After observing the ridge results, we introduced a documented counterhypothesis test: four-way original class-ID nearest-centroid classification, using the identical support sets. This was a post-result scope attack, not independent confirmation of the primary transfer task.

Every adaptive K4, K8 and K16 representation has accuracy1.0 on **every** enumerated support set at both budgets. Frozen one-shot class accuracy ranges from.51to.63. Thus the upper instability and binary-transfer penalty do not imply a failure of ordinary class-ID few-shot classification in this finite model. Choosing one target as the final universal quality verdict would repeat the original mistake.

## 5. Exact geometry calculation

For an arbitrary representation matrix F, affine ridge predictions are determined by its Gram matrix and the labeled support. Center the training inputs and labels. With n labeled rows, centered train Gram Kc and train/test cross Gram Ktc,

\[
\widehat Y_T=\overline Y_S+
K_{tc}(K_c+n\lambda I)^{\dagger}(Y_S-\overline Y_S).
\]

This is elementary linear regression/kernel algebra. It is not a new theorem. Same-Gram representations have the same predictions for the fixed support protocol. That does **not** make all learning-dynamics theory unimportant: a new dynamic theory can matter by predicting which Gram geometry is reached. It only prevents attributing a new downstream mechanism to the observed risk formula itself.

An exactly calculable control isolates nuisance acquisition. Let v_c be regular-simplex class vectors and u_(c,r) be independent orthogonal class blocks, each containing a four-vertex zero-mean unit simplex. Define

\[
F_{c,r}=\sqrt{1-\nu}\,v_c\oplus\sqrt\nu\,u_{c,r}.
\]

One support per class yields centered support Gram eigenvalue(4−nu)/3 on every balanced target. A held-out view's target-direction cross Gram coefficient is(4−5nu)/3. Therefore every balanced task receives the exact prediction

\[
\widehat y=\kappa y,\qquad
\kappa=\frac{4-5\nu}{4-\nu+12\lambda},\qquad
R=(1-\kappa)^2.
\]

The general support ridge calculation agrees with this formula to5.6e-16. Selected independent primal solves agree with dual predictions to2.94e-14. These computations show how an ordinary geometric/sample effect can explain few-label errors; they do not automatically supply the missing count-feedback contribution.

## 6. Closest existing perspective and what is not claimed

I inspected Luthra, Yang and Galanti, *Self-Supervised Contrastive Learning is Approximately Supervised Contrastive Learning*, primary v2,2025, [original](https://arxiv.org/html/2506.04411v2), §3.2 and Proposition1, plus the setup/expansion in AppendixC. The paper explicitly relates few-shot prediction to class-distance-normalized and directional dispersion. Its proposition uses a different nearest-centroid/classification setting with a sample-size condition; our one/two-support binary ridge formulas are **not literal corollaries** of that bound. The overlap is the already established conceptual explanation that within/between geometry governs few-shot adaptation. The exact ridge formulas above use standard linear algebra instead.

Hence “nuisance spread hurts few-label learning” is not a sufficient novelty claim. A new count/feedback theory would need to predict a nontrivial failure of an independently valuable geometry, distinguish it from static repulsion, and explain a regime that existing fixed-objective optima do not decide. This branch provides a fixed task-based test for such a result but does not assert that the old square window meets that requirement.

## 7. Verdict for the attempted rescue

**Reject the route that treats the old stable square window as intrinsically desirable task-universal geometry.** It fails against a symmetric task family and a same-information positive-graph baseline; the lower boundary has negligible effect here, while a different reasonable classification goal is perfect even above the upper boundary. The finite-label effect that remains is compatible with standard task rank/dispersion/regularization explanations.

This is not a rejection of every possible revised question in the parent research. In particular, a proved result that a task-universal simplex optimum becomes dynamically inaccessible under adaptive policy response would be a different and more consequential question. The current branch's measurements furnish a non-handpicked utility distinction between that optimum and the rank-two endpoints, but they do not establish the new dynamic theorem or its novelty.

## Provenance

`evaluate.py` uses all12saved base representations, canonical geometries and prespecified mean-only controls, producing264risk rows from44representations. No new pretraining is claimed. `ncc_check.py` is explicitly post-result. Files under results contain every fixed regularizer/support budget and contrary outcome. Total primary enumeration took about4seconds in the recorded environment. A separate clean rerun is possible without external data or GPUs.
