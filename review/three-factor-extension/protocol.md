# Three-factor full-capacity extension

Recorded before execution, 2026-10-22. Root independent check following the four-state square discovery.

Question: does matched-frozen stability versus adaptive instability extend beyond two binary factors, or does unrestricted lookup capacity expose another unstable direction?

Model: uniform m independent binary factors, identity positives, all 2^m states, normalized lookup embeddings initialized to the balanced hypercube. One-negative exact InfoNCE. q=(1-epsilon)softmax(kappa*dot)+epsilon/M; stop-gradient sampler. Frozen control holds the exact q at the same equilibrium. Embedding dimension d>=m+1, including d=M sufficient to represent all states without a dimension bottleneck.

Primary settings: m=2,d=4 calibration; m=3,d=4 and d=8; epsilon in {.01,.1,.5}; kappa in {-10,-6,-4,-2,-1,0}. Jacobian uses complete product-sphere tangent basis and central finite differences at h=1e-5. Stability modulo rotation is assessed from all eigenvalues, not one tied factor coordinate. Confirm any candidate with h=3e-6 and h=3e-5 and independent orthogonal orientation seed 20261022. No random dataset or empirical success-probability claim.

Criteria: frozen strict attraction modulo known rotations requires every nonrotation eigenvalue <−1e-7; adaptive instability requires at least one eigenvalue >1e-7. Count zero eigenvalues explicitly and check equilibrium residual. A positive case must survive the step/orientation confirmation. If none exists for m=3, report that limitation rather than expand settings to find a positive result. This is an exploratory extension, not preregistration before the original discovery.
