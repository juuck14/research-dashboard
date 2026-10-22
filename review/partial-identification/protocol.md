# Independent review protocol

Recorded 2026-10-22 before executing independent audit code. Reviewer owns only review/partial-identification/.

## Claims to test

1. Recompute Gaussian total correlation directly from covariance determinants; verify the Givens-rotation formula across random variance pairs, not only the owner's symmetric D_gamma family.
2. Construct nonorthogonal shear source transforms, preserve each observed covariance exactly by inverse mixing, and show that observation whitening does not imply orthogonal mixing under approximate source independence.
3. Distinguish the max-over-environments dependence budget from the probability-weighted conditional total-correlation budget. One rare informative environment should produce materially different feasible sets.
4. Prove (not infer numerically) that every finite diagonal-Gaussian environment family with positive TC tolerance admits small cross-block Givens rotations. Hence no proper coordinate block is exactly identified from these assumptions alone.

## Execution and criteria

- Exploration seed 20261022, independent confirmation seed 8675309, 200 random variance-pair/angle cases per seed.
- Gaussian TC direct/formula error <=1e-11; observed-covariance reconstruction error <=1e-11.
- Shear epsilon chosen at 0.8 of the exact dependence-budget endpoint for delta=1e-3, source variances e0=(1,1), e1=(1.3,.7). Both TC constraints must pass; normalized source correlations and mixing nonorthogonality must be nonzero.
- Rare environment example gamma=.6, delta=.01, probability=.01. Enumerate 200001 angles in [0,pi/4]. Compare analytic and direct feasible endpoints.
- No claim about a general nonlinear model, finite-sample confidence coverage, or novel theorem follows from these tests. Primary literature comparison is separate.
