# Why this target and this failure matter

2026-10-23. The following geometric/statistical facts are standard tools, fully proved here to define the learning target. They are **not** claimed as new simplex-packing or information-theoretic results. The new candidate concerns whether an adaptive contrastive update can maintain this independently justified target and what its attractors retain.

## 1. Decoder-independent robust class distinction

Let C distinct classes have unit feature prototypes f_i. The largest feature-perturbation radius for which some decoder can classify **every** class correctly is, as a supremum,

\[
r(F)=\tfrac12\min_{i\ne j}\|f_i-f_j\|.
\]

If two different-class closed balls intersect, a single decoder cannot give both labels at the intersecting feature. This proves the upper bound. For every smaller radius nearest-prototype decoding is correct, which proves achievability below the supremum. The statement allows arbitrary nonlinear decoders; no particular linear probe or ridge parameter defines the target.

Writing mean f as barf, the average squared pair distance is

\[
\frac1{C(C-1)}\sum_{i\ne j}\|f_i-f_j\|^2
=\frac{2C}{C-1}(1-\|\bar f\|^2)
\le\frac{2C}{C-1}.
\]

The minimum is at most this average, so r(F)≤sqrt(C/[2(C−1)]). Equality requires mean zero and every pair distance equal, hence the regular-simplex Gram. It is attainable in d≥C−1. Thus class permutation, original factor coordinates, task weights and noise hyperparameters do not select the target: it is the standard optimum for distinguishing all correctly distinct classes robustly under the unit-norm constraint already used by the loss.

Multiple observations of a class do not avoid this bound: pick any one observation per class. Class-collapsed simplex features attain it for every observation. The positive/negative information in the proposed construction explicitly distinguishes these classes. Identifying them as one class is not merely keeping extra nuisance information.

## 2. Exact coarse limit

At a balanced two-valued representation with C/2classes per value, H(Y)=log2(C) while I(Y;F)=1bit. Even an unrestricted decoder has optimal class-ID accuracy2/C. This concerns the **exact limiting representation**, not finite floating-point arrays with tiny residual distinctions. For finite distinct arrays noiseless Bayes accuracy may remain1.

The robust radius is continuous and tends to0 along trajectories approaching the class-merging limit. This finite-time consequence does not require declaring tiny coordinates absent or choosing a numerical rank cutoff.

## 3. A fixed-noise finite-time bound

Suppose f_i is within RMS distance delta of a two-valued reference a_i u, with both groups nonempty. For feature observation f_Y+sigma Z, Z standard isotropic Gaussian, compare the joint law with the reference a_Y u+sigma Z. The average conditional Gaussian KL divergence is delta²/(2sigma²); Pinsker gives joint total variation≤delta/(2sigma). Dropping any view index from the joint law cannot increase this bound.

The optimal classification success probability changes by at most total variation. Since the ideal two-valued reference has Bayes accuracy≤2/C even after noise,

\[
A^*_{\sigma}(F)\le 2/C+\delta/(2\sigma).
\]

The bound is capped at1. Conversely, for any feature set with radius r, each nearest-prototype error against a particular wrong class has Gaussian probability at most Phi(−r/sigma). A union bound gives

\[
A^*_{\sigma}(F)\ge A^{NN}_{\sigma}(F)
\ge 1-(C-1)\Phi(-r/\sigma),
\]

clipped at0. These bounds use the same class-ID objective and noise for both policies; they do not optimize a favorable downstream readout after seeing the outcome. The geometric radius is the primary criterion and does not require any chosen sigma. The inequalities quantify the consequences for every fixed sigma>0 as the limit is approached.

## 4. What the bridge establishes

The original square-window paper could not infer usefulness from balanced energy or view alignment. In the new proposed separation, the fixed-law optimum maximizes a class-distinction criterion, while an adaptive attractor merges classes that are supplied as correct negatives. This is a genuine failure of an independently meaningful property. Proving it does not itself guarantee novelty: biased sampling, dimensional collapse, simplex geometry and generic feedback are old knowledge. The full local policy-response classification and the all-count, full-support, true-negative-only class-merging construction must add the independent result. The primary-source review assesses that separately.
