# Nonidentity positive links do not remove the local class-merging attractor

Independent derivation, 2026-10-23. This is a scope check of the new candidate, not a separate claimed new principle. The numerical script uses no author scientific implementation.

## Setup and a globally meaningful frozen comparison

There are C=2m true classes, each with r equally likely views, N=Cr. Each row f_i has unit norm. Positives stay in their true class and have a symmetric stochastic transition P_c; use r=2 with the swap matrix for the executed check. All negatives are outside the anchor's entire class. The base law is uniform on the N−r allowed views. The adaptive policy is its epsilon mixture with normalized exp(−t s_ij). The gradient is detached through the policy and includes both query and key roles.

Under the **fixed uniform-off-class** law, the global optimum is the class-collapsed regular simplex, for every K≥1 and d≥C−1. This baseline is a standard Jensen consequence, not a new contribution. To see it without assuming class-constant embeddings, let mu_c be the within-class mean. Then

E s_negative = (||sum_c mu_c||²−sum_c||mu_c||²)/(C(C−1)) ≥ −1/(C−1),

while E s_positive≤1. Joint Jensen on log(1+sum_k exp(s_negative,k−s_positive)) gives loss≥log(1+K exp(−C/(C−1))). The class-collapsed simplex attains it. Equality requires every positive edge to have inner product1, so a connected positive graph collapses each class; strict convexity of log-sum-exp with its fixed zero coordinate then requires equal cross-class scores. This establishes the unique optimal Gram. At the simplex the adaptive law equals this exact fixed law, including with swap positives.

## Full added-view modes at a balanced antipodal class merger

Put m classes at +e and the other m at −e, with all r views of a class identical. Let A_s and A_o be the expected total softmax weights of negative candidates in the same and opposite antipodal group, respectively. The denominator is 1+S+exp(−2)O. These are the same binomial moments used in the prototype calculation. Define B=A_s+A_o and R=A_s−A_o.

All score first derivatives vanish at this configuration. In particular, the adaptive policy's first derivative is zero for every sphere tangent direction. Thus its complete linearization equals the field with the **coarse-point** policy frozen; this fact must not be used to attribute coarse-point stability alone to feedback.

The tangent space splits into class-mean directions and within-class mean-zero directions. Class-mean eigenvalues equal the prototype eigenvalues divided by r. For a within-class eigenvector of P_c with eigenvalue mu, the negative quadratic form contributes −R||z||²/N and the positive term contributes B(1−mu)||z||²/N. Therefore the restoring eigenvalue is

lambda_view = 2[B(1−mu)−R]/N = 2[2A_o−B mu]/(Cr).

Since P_c is symmetric stochastic, mu≤1. Consequently lambda_view≥2(A_o−A_s)/(Cr)>0 whenever the stronger class-mean condition A_o>m A_s/(m−1) holds. For r=2 swap positives, mu=−1 and lambda_view=2(A_s+3A_o)/(Cr). The zero modes are exactly rotations of the common antipodal axis. A strict class-mean inequality therefore gives normal attraction in the complete view-level sphere tangent space, not just in a class-constant slice.

## Executed independent check

Run `python negative-feedback/round5/critic/multiview_check.py` from the repository root. The script enumerates all ordered tuples for C4, r2, d3, t=log4, epsilon=.05 and K1/2/3. It uses positive mates rather than identity positives, excludes both views of the anchor class from every negative, and differentiates the entire 16-dimensional projected gradient. Both the adaptive and coarse-point-frozen spectra agree with the above formula at two finite-difference steps. Twelve checks have maximum spectrum discrepancy 9.52e−12 and zero numerical drift. Raw spectra are preserved in `multiview_check.json`.

The computation checks the full local spectrum in this nonidentity example. It does not establish a generic neural-network training frequency or global convergence probability. The all-K sign claim depends on the separate moment inequality proof; checking K1/2/3 is not its proof.
