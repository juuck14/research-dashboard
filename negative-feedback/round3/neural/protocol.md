# Joint-negative prediction bridge: fixed protocol

2026-10-22, recorded before the new computations. The previous shared MLP used averaged one-negative pair losses and did not test the finite-K joint-denominator law. This task directly tests that gap. A positive result is a mechanism/scope result, not evidence of universal information erasure or a top-journal contribution by itself.

## Stage A: population oracle and extra view directions

Each of four binary semantic states has m=4 fixed nuisance views (N=16); a separate m=2 condition checks view-count dependence. Inputs contain the two signs plus14 Gaussian nuisance coordinates (sd.25), followed by a fixed orthogonal16D renderer (seed3401). A positive is an independently selected uniform view of the same semantic state, including itself. The learner receives only observations and positive correspondence. Negatives are iid with replacement from the adaptive score distribution over all N views. Policy omega(s)=4^(-s),epsilon=.3 is inherited from the prior analytic prediction and will not be tuned.

The reference geometry collapses each state's views onto the balanced square. It is an oracle geometry control, not a claim that unlabeled training reaches it. All individual view embeddings may move. This adds within-class nuisance tangent modes absent in the earlier four-observation theorem.

For arbitrary finite populations and positive channels, the exact expected joint-K gradient will be evaluated by a one-dimensional Laplace integral and Gauss-Laguerre quadrature. Before using this oracle, compare its value/gradient with direct multinomial enumeration on N=4 at K1,2,4,5,8,16 and with numerical derivative at fixed q. Compare96/128 quadrature nodes on N16 random embeddings. Absolute discrepancies above1e-7 block subsequent claims; algorithm fixes must be recorded.

At K1,2,4,5,8,16 and m2/4, compute the complete free-embedding tangent Jacobian. Independently project into class-mean and zero-class-mean view subspaces. Primary prediction: class-mean eigenvalues equal the prior four-state spectrum divided by m; within-view modes must be reported, and any negative one refutes full-stability transfer. No inference of information loss follows from leaving the square.

## Stage B: actual shared nonlinear parameterization

Use a16→64 tanh→8 network with output normalization. Construct the square reference using two population principal directions of the renderer (known in this mechanism control). Remaining hidden units depend on nuisance and have zero output weights initially, so they do not alter the reference but permit additional view-dependent tangent directions. Parameters of every layer are trainable. This is a constructed reference, not random warmup or a semantically blind initialization.

Compute the output Jacobian and its tangent rank. The comparison to free embeddings is conditional on surjectivity; an insufficient-rank encoder is a separate capacity/tangent restriction. The pullback relation itself is standard, not a new theorem. At K4/K5 compare the actual parameter-gradient Jacobian in the active parameter subspace against J^T H J. Require relative matrix error<1e-5 and report inertia. Report the stationary residual before interpreting eigenvalues. Three fixed hidden-feature seeds3501,3502 primary and3701 confirmation. No seed replacement.

Integrate the actual parameter-gradient flow from an initial square angle imbalance1e-5 plus a generic parameter perturbation of size1e-7. Compare fixed square-q and adaptive policies for K4/K5. Integration horizon is3 divided by the magnitude of the slow nonrotation parameter eigenvalue predicted before integration. Because parameter metric can mix modes, compare the measured unstable/stable eigenmode amplitude rather than assuming the old lookup rate. A measured sign opposite to the full parameter prediction is failure; changing learning rate or increasing horizon after seeing results is not authorized.

## Stage C: ordinary SSL warmup, separate scope test

Three fixed random-initialization seeds3801,3802 primary and3901 confirmation. Same architecture/data. Uniform joint-K4 warmup1000 gradient steps, lr.05. At the fork record complete geometry, residual, and K2/4/5/8 instantaneous vector fields. Do not change warmup to force a square. Proceed with frozen/adaptive joint-K forks for1000 steps at each K, same initialization and exact population updates, and record factor energies and within-class variation. These finite-time runs are not a direct threshold validation unless the stationary square conditions are met. Failure to visit the geometry is a scope limitation rather than a theorem counterexample. No natural-image or permanent-erasure claim is permitted.

All scientific files remain in this directory. Root owns repository publication and final journal-level judgment.

## Numerical choices before parameter-flow execution

The stationary parameter Jacobian is low rank. To avoid an extremely long explicit run for the weak K4 instability, integrate the actual recomputed nonlinear gradient with linearly implicit Euler using the fixed reference Jacobian as preconditioner. Each step solves its low-rank linear system exactly; it does not freeze the neural gradient or output kernel. Set scaled step dt*abs(target eigenvalue)=.002 and1500 steps. For seed3501 in both K conditions, also execute3000 steps at half step. The sign criterion is unchanged. Report backward-Euler's known linear prediction separately from continuous exp(±3); require the adaptive final-amplitude ratios to agree within1% under halving. This method choice is recorded before any parameter-flow output.

For ordinary warmup, a direct square-threshold interpretation requires relative class-mean Gram error<.001 and parameter gradient norm<1e-6 at the fork. If either fails, the arm remains an observed scope test and cannot be counted as quantitative cutoff replication.

The first oracle run completed its calculations but failed JSON serialization of a NumPy boolean. Casting to builtin bool fixed only output; the validation was repeated. Positive Laplace terms can underflow to zero at large quadrature nodes; log(0) is represented explicitly as negative infinity so the final exponential term is zero. No physical parameters or acceptance criterion changed.

## Stage A2: augmentation mixing, analytically motivated extension

After StageA's uniform within-class positives yielded positive extra modes, the first-score and radial-gradient decomposition suggested a necessary role for positive mixing. This is a new analytic scope question, not a replacement of the original condition. Before evaluating its numeric curve, record the hypothesis: with P_rho=(1−rho)I+rho Uniform_class, a zero-class-mean normal mode has eigenvalue [lambda_plus−Btot(1−rho)/2]/m; the in-plane version adds lambda_balance/(2m). Here Btot is the total expected negative softmax mass. Predict that class-mean K stabilization need not imply full stability when augmentation mixing is weak.

Fixed curve: K1–128,rho∈{0,.025,.05,.075,.1,.15,.3,1}. Independently evaluate complete tangent finite differences at K{3,5,16,64},rho{0,.05,.1,.2,1},m4. Require spectral formula agreement<1e-7. All rho/K conditions are retained whether or not a bounded stable-count interval appears. If the hypothesis fails, preserve the curve and revise the decomposition rather than choosing successful rho settings.

## Stage A3/B2: post-discovery confirmation of the mixing-window prediction

The A2 fixed grid found an intermediate stable interval for rho=.05 and suggested the exact augmentation-graph eigenvalue formula. This is an analytically interpreted discovery, not a held-out parameter choice. Before new graph/dynamics execution, fix these checks:

- General symmetric positive graph: lazy cycle and reflecting path on4views, each at mixing scales.05 and.2, at K5,8,16. Compare the entire112D tangent spectrum with the predicted eigenvalues using the actual positive-graph eigenvalues. Tolerance1e-7. Complete-graph mixing is not a substitute for these different graphs.
- Directed interval finite sums at K11/12,rho=.05 must certify opposite signs of rho−critical_rho. Together with the newly derived strict critical-rho monotonicity and old lower cutoff, this establishes K5–11 for every count, not a sweep extrapolation.
- Actual shared nonlinear encoder: rho=.05,K4/8/16,three fresh hidden-feature seeds4101,4102 and confirmation4301. Constructed square reference, all layers trainable, no label-gradient training. Target the predicted most unstable mode for K4/16 and slowest nonrotation stable mode at K8; perturb parameters by1e-5 along that mode plus fixed1e-7 generic noise. For each K compare frozen/adaptive samplers, integrate actual recomputed gradients for3 target e-fold times with the earlier fixed-reference linearly implicit method. Frozen K4 and both K8 should contract below.15; adaptive K4 and both K16 should expand above10. Half-step refinement on seed4101 adaptive in all3conditions must agree within1%. Upper-K instability being shared by frozen and adaptive is part of the prediction and prevents a feedback-only interpretation.

No semantic-erasure or real-data-generalization interpretation is authorized. The new predictions concern separation between class-mean balance and within-class augmentation invariance.

## Post-flow numerical-method attack

After the low-rank linearly implicit flows passed, a possible numerical circularity remains: the integrator uses the predicted reference Jacobian to handle stiffness. Although it recomputes the actual nonlinear gradient and step-halving agrees, add one standard DOP853 comparison at seed4101,K16,rho=.05 for frozen and adaptive channels. This uses no reference-Jacobian preconditioner. Reuse the exact declared initial perturbation and horizon; require final modal amplitude within1% of exp(3), and compare with the known first-order implicit discretization bias. This is a post-result method diagnostic, not a new independent primary success or a parameter search. Cap at200,000 RHS calls; if exceeded, record a numerical-resource block rather than scientific failure.
