# Relabeling symmetry does not identify preferred semantic factors

2026-10-23. Direct derivation prompted by two non-oracle trajectories selecting different square matchings. This is a standard symmetry/identifiability argument, not a new learning theorem. Its role is to prevent geometric accessibility from being mistaken for semantic-factor recovery.

## Setting and equivariance

There are four equally weighted classes, each with the same number of views. The positive channel is `.95I+.05U_class`. The candidate base measure is uniform, and the current negative policy depends only on pair scores with the same weight function at every anchor. Let S be a permutation of the four class blocks that leaves the view index within each block unchanged. Then `S P S^T=P`. Pair scores transform as `Gram(SF)=S Gram(F) S^T`, and the negative policy obeys the same identity. The summed joint-K population loss is therefore unchanged by replacing F with SF.

The detached projected update obeys `G(SF)=S G(F)` because both score appearances are differentiated and the sphere projection is rowwise. For a frozen sampler the corresponding identity holds when its matrix is also conjugated by S. Projected Euler with row normalization commutes with S. An iid Gaussian initial representation has a law invariant under every such S.

No original binary label a or b enters this argument or the representation gradient. Those labels are assigned to the four classes only for evaluation.

## Three indistinguishable square matchings

For four class vertices there are three ways to choose the two pairs of opposite square corners. Class relabelings act transitively on these three possibilities. Each has the same spectrum, same objective value and same local stability result under the declared symmetric learning problem.

There are three nontrivial balanced binary class partitions: a, b, and their product ab. At any exact square, two of them are affine-linearly separable; the remaining one is XOR (equal labels on opposite corners). Both label convex hulls then contain the square center, so no affine hyperplane separates it. A classifier can isolate one corner and make exactly one of four errors, giving optimal affine-classifier accuracy3/4 on the four uniform class vertices. This is not the same as a least-squares readout's accuracy, which may be1/2 when its projected target is0.

Every square has four distinct class vertices. A nonlinear decoder can recover the entire class, and consequently each balanced bit has exactly one bit of noiseless information. The linear/nonlinear distinction is therefore real while information erasure is absent.

Only one of the three square matchings makes both originally designated a and b linearly separable. The other two prefer one original bit and the product bit. The symmetric training information supplies no preference among those choices.

## Conditional probability, not convergence claim

If an equivariant deterministic learning algorithm with this iid class-symmetric initialization **converges exactly to one of the three square classes**, each matching has conditional probability1/3 given that event, by transitivity and symmetry of the event. This does not prove convergence, the event's probability, or a factor-erasure rate. It also does not assign these exact limiting linear-separability statements to a finite, almost-square cloud: arbitrarily small extra coordinates can preserve perfect linear separation with extremely large readout norm.

## Executed algebraic diagnostic

`symmetry_check.py` directly evaluates all24class permutations at three K values and two policy modes. Max field-equivariance discrepancy4.16e-17; value discrepancy2.66e-15. It separately constructs all three exact squares and checks the two-exact-affine/one-XOR residual pattern. These are algebraic sanity checks, not144independent training experiments. The construction is explicitly post-execution and is not presented as held-out statistical confirmation.

## Consequence for the research's importance claim

The non-oracle result can close the narrow objection that the square can only be installed by a latent-factor oracle. It does not establish that the balanced square is the uniquely desirable semantic representation. A factor-specific quality claim requires a task/readout or extra structural information that distinguishes the original a,b partitions from ab. The current positive correspondence and uniform candidate law do not do that on their own.
