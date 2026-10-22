# Learned nonlinear encoder experiment

Recorded before training on 2026-10-22. This experiment tests whether the earlier normalized lookup phenomenon survives an ordinary shared nonlinear encoder, and whether learned initial geometry removes it. A failed replication is retained.

## Data and model

Two independent uniform binary factors a,b. Four combinations are sampled iid, with fourteen independent continuous nuisance variables. The sixteen source coordinates are multiplied by one fixed orthogonal matrix (renderer seed 916), then a fixed invertible smooth pointwise warp y+0.1*tanh(y)^3 is applied. Positive views share a,b but have independent nuisance N(0,.25^2). No factor labels are used in encoder training. The raw-source oracle is exactly available by inverting the scalar warp and orthogonal map.

The shared encoder is a trainable 16→32 tanh→8 MLP, including both biases, followed by exact unit normalization. Training uses the same encoder on both views and all off-diagonal within-batch negatives. The one-negative logistic InfoNCE risk is exactly averaged over the finite batch sampling law q. This is a stochastic minibatch estimator of a pair loss, not K=batchsize−1 multi-negative InfoNCE. Sampler probabilities are detached; both anchor and negative representations receive gradients.

## Policies and controls

Uniform q, matched-frozen q from a snapshot encoder, adaptive q from the current encoder. Filtering uses epsilon=.1,kappa=−2: q=epsilon/(B−1)+(1−epsilon)*softmax(kappa*s) over off-diagonal candidates. The frozen encoder is evaluated on each new batch; its parameters never update. All policies start with the same current encoder and use common input/augmentation random streams. Their q values are identical at the fork for frozen vs adaptive.

Primary arm: unsupervised uniform warmup of 1000 steps, followed by 3000 fork steps. Success prerequisite is both clean linear factor probe accuracies ≥.95 at the fork. If this fails for a seed, report a warmup failure and do not tune the encoder to pass.

Mechanistic control: one unlabeled PCA-based near-linear initialization with small trainable residual features, no warmup, then the same 3000 fork steps. This is a separately declared control, not a replacement of the primary arm. It tests dependence on initially factorized geometry. PCA uses no latent labels. No post-result warmup or initialization search.

Both arms: width32,output8,batch64,SGD learning rate .05,no momentum,no weight decay. Primary seeds1101–1103; confirmation2201–2203. Renderer and evaluation draws are shared across settings. Training time is fixed; do not extend a nonreplicating run until it succeeds.

## Checks and measurements

Before training, check 50 randomly chosen parameter gradient coordinates by central finite differences while holding q fixed, including adaptive q computed at the base parameters. Also verify normalization derivatives. Tolerance max absolute error1e−6 and relative error1e−4 for non-tiny derivatives. Failure blocks training until corrected with an explicit code-fix record.

At fork and final: factor-specific clean linear ridge and RBF-kernel ridge probes on heldout nuisance draws; an isotropic feature-noise sigma=.05 test with independently noised probe train/test features; raw-input oracle ceiling. Probe train512/test2048, fixed ridge regularizer .001 per sample; RBF bandwidth is the median unlabeled train distance and is not selected using labels. Report both linear and nonlinear access, not MI.

Geometry: four heldout class means, Gram matrix, eigenvalues, Walsh mean coefficients 1,a,b,ab and interaction energy fraction. Tetrahedral geometry can provide a strong alternative explanation if primary warmup introduces ab structure absent from the square theorem.

Predeclared primary replication criterion: adaptive worst clean linear factor accuracy at least .15 below frozen and adaptive worst noisy accuracy at least .20 below frozen in at least2/3 primary and2/3 confirmation seeds. Also report nonlinear readout: nonlinear recovery above .90 means reduced linear access rather than established broad factor loss. Failure of the criterion is not a proof that adaptive filtering is universally safe.

## Scope

This synthetic nonlinear shared encoder is more general than free lookup vectors but is not a natural-image benchmark. Exact four-state theory does not automatically predict this model because nuisance, minibatch composition and encoder tangent metric differ. We test their consequences instead of calling every low probe score information loss. The warmup arm and PCA control must remain separate in the report.
