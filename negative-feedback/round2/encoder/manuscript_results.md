# Shared nonlinear encoder: results and limits

## Result, and the failed stronger endpoint

We tested the square-geometry sampling mechanism with a shared trainable nonlinear encoder, stochastic finite minibatches, independent continuous nuisance in positive views, and eight normalized output coordinates. Adaptive easy-negative sampling compressed one factor's class-mean coefficient energy (squared norm) by 882–7,260 times relative to the matched frozen sampler after uniform SSL warmup. The corresponding coefficient-norm reduction was approximately29.7–85.2 times. Both initially available factors remained robustly accessible under uniform and frozen sampling. Under adaptive sampling, mean worst-factor accuracy after a fixed isotropic feature-noise channel fell from 1.000 to 0.599 with ridge readout and 0.597 with ordinary least squares (OLS). These are directly executed results, not predictions of the lookup theorem.

The stronger predeclared replication endpoint **failed**. It required a clean linear accuracy loss of at least .15 together with a noisy linear loss of at least .20 in at least two of three primary seeds and two of three independent confirmation seeds. Warmup passed one of three primary and three of three confirmation seeds; the PCA control passed zero of three primary and two of three confirmation seeds. Confirmation success does not override primary failure. Consequently we do not claim that the prespecified magnitude of clean-factor loss reliably replicated.

The defensible interpretation is compression of a factor's geometry and loss of robustness under the specified channel. The results do not establish exact information erasure, a stable globally attracting blind representation, or a universal failure of pretrained encoders.

## Data, learner information, and matched comparison

Let a,b be independent uniform signs. Each observation is generated from s=(a,b,n) with n distributed as N(0,.25² I₁₄), a fixed orthogonal matrix Q drawn once with seed 916, and the invertible pointwise map g(u)=u+.1 tanh³(u): x=g(Qs). Positive views have the same a,b and independent n. The encoder receives x, positive correspondence, and sampled candidate batches. It never receives a,b or the rendering inverse during representation training. Factor labels enter diagnostic probes only.

The encoder is a shared 16→32 tanh→8 network with both biases trained, followed by exact unit normalization. SGD uses batch size 64 and learning rate .05, without momentum or weight decay. The primary initialization is 1,000 uniform-sampling SSL updates of a randomly initialized encoder. This is followed by three forks, each trained for exactly 3,000 steps. One fixed PCA-based near-linear initialization without warmup was declared as a mechanistic control before executing training. No initialization, duration, or learning-rate search was performed.

For view embeddings fᵢ and fⱼ⁺, let Sᵢⱼ=〈fᵢ,fⱼ⁺〉. The loss is the weighted finite-batch average of the **one-negative** pair loss softplus(Sᵢⱼ−Sᵢᵢ). It is not the standard loss with 63 negatives jointly inside a logarithm. For each anchor, negatives exclude its own positive index; other examples sharing its latent state are allowed. The policy is

qᵢⱼ = .1/(B−1) + .9 softmaxⱼ(−2 Sᵢⱼ), j≠i.

The weights q are detached for differentiation. Both appearances of the shared encoder receive gradients. We average exactly over the finite candidate batch law rather than drawing one negative index. Thus minibatch composition and views are stochastic, while additional sampling-index noise is removed. Every candidate has probability at least .1/63≈.001587. Uniform q is the first control. The second uses q recomputed on each new batch with an immutable snapshot of the fork encoder. Frozen and adaptive policies therefore have identical loss and parameter gradient at the fork, not merely similar initial quality. Training streams are shared across policies within a seed.

The experiment contains six fixed seeds, split before execution into primary 1101–1103 and confirmation 2201–2203. It comprises 36 fork runs and six warmups, about 114,000 SGD updates, and took 290 seconds with single-threaded BLAS in the recorded environment. The raw-source oracle, obtained by inverting g and Q, recovers both signs with accuracy 1.000. This establishes data availability and is not a baseline given to the learner.

## Checks that preceded or audited interpretation

The analytical backpropagation was checked at 50 random parameter coordinates against central finite differences while holding the sampler weights fixed, as required by the actual detached update. The executable absolute-error gate ran before training and passed at 6.00×10⁻¹¹. The later audit also verified the protocol's relative-error criterion across non-tiny derivatives: maximum discrepancy 4.03×10⁻⁸. No correction of the training implementation was required.

A separate deterministic audit reconstructed all twelve initial snapshots. Frozen and adaptive losses and all gradient coordinates agreed exactly at the fork. Final unit-norm errors were at most 3.33×10⁻¹⁶. All twelve initial snapshots achieved 1.000 with clean and noisy ridge and RBF readouts. Both factors were available before adaptive feedback began. Initial probes were reconstructed after training from the same declared seeds because the main training script originally saved only initial linear probes and geometry; this fills the initial heavy-probe measurement omitted by that script and does not change training.

## Geometry actually visited by the MLP

For the four heldout class means µ(a,b), write

µ(a,b)=c₀+a cₐ+b c_b+ab cₐ_b.

The Walsh energies are squared Euclidean norms of these coefficients. We save the entire class-mean Gram matrix and its eigenspectrum, in addition to energies, to distinguish a nearly square arrangement from a tetrahedron. A tetrahedron could encode the interaction ab and invalidate an extrapolation from square-only theory.

All six uniform-warmup snapshots had interaction fraction ‖cₐ_b‖²/(‖cₐ‖²+‖c_b‖²+‖cₐ_b‖²) between 3.04×10⁻⁵ and 3.09×10⁻⁴. Their geometry was therefore nearly square in this fixed training window, rather than tetrahedral. This is an observed property of this learner and task, not a general theorem about SSL geometry. The PCA snapshots had an even smaller fraction, between 2.55×10⁻⁸ and 1.14×10⁻⁷.

After the 3,000-step fork, the smaller factor-mean energy was .495–.498 under the frozen sampler, compared with 6.84×10⁻⁵–5.65×10⁻⁴ under adaptive sampling in the warmup arm. Paired frozen/adaptive ratios were 882–7,260. The stronger factor retained energy close to .998. With the declared PCA initialization, the weaker energy was 2.83×10⁻⁸–5.74×10⁻⁸ under adaptive sampling, versus .495–.499 under frozen sampling: ratios of 8.65×10⁶–1.76×10⁷. The factor selected as weaker varied by seed.

These are mean-geometry statistics. Small mean separation alone does not prove statistical independence of a factor and the full representation. Energy curves continue decreasing over the observed window; these finite-time curves do not establish an attracting fixed point.

## Readouts and the readout-regularization objection

The probe training set has 512 independently rendered observations and the test set 2,048. Initial and final geometry use the same 2,048 heldout observations; intermediate traces use a separate fixed 256-observation heldout set, so trace endpoints and final geometry estimates need not be numerically identical. Ridge regularization is .001 per sample. RBF-kernel ridge uses the unlabeled median squared training distance as bandwidth and the same regularization; neither bandwidth nor regularization was label-selected. The noisy channel adds independent N(0,.05² I₈) to train and test features without renormalization. This measures robustness under a specific feature channel, not robustness to every input perturbation.

After observing small factor energies, we recorded a fixed post hoc audit: centered OLS with `lstsq(rcond=1e-10)` on the same observations, without searching settings. It tests whether ridge regularization itself hides a weak available direction. The audit was not substituted into the preregistered endpoint.

All uniform and frozen runs attained 1.000 with every readout, clean and noisy. The table reports adaptive results, mean [minimum, maximum] over six seeds. The three primary and three confirmation results remain individually available in `results/runs.csv`, and split aggregates are in `results/aggregate.md`.

| Initialization | Clean ridge | Clean RBF | Clean OLS audit | Noisy ridge | Noisy RBF | Noisy OLS audit |
|---|---:|---:|---:|---:|---:|---:|
| Uniform SSL warmup | 0.762 [0.667,0.926] | 0.780 [0.684,0.920] | 0.785 [0.689,0.938] | 0.599 [0.551,0.668] | 0.598 [0.542,0.666] | 0.597 [0.545,0.667] |
| Unlabeled PCA control | 0.842 [0.646,0.982] | 0.831 [0.660,0.980] | 0.950 [0.916,0.995] | 0.512 [0.502,0.528] | 0.503 [0.493,0.520] | 0.511 [0.501,0.529] |

OLS recovers substantial clean accuracy in the PCA arm. Thus a low ridge or median-bandwidth RBF score there cannot be treated as missing factor information. In the warmup arm, OLS improves mean clean accuracy by only .022 and does not remove the loss: ordinary nuisance-sensitive readouts also struggle with the compressed direction. Under the stated feature-noise channel, all three readouts agree closely about a large loss. This supports a robustness interpretation and contradicts a claim of demonstrated exact factor erasure. It also shows why reporting only cosine retrieval or one regularized probe would have been misleading.

## What is controlled, and what is still a competing explanation

The comparison excludes insufficient nominal output dimension, lack of initial data information, initially unavailable factors, exclusion of a negative class from the support, a detached-gradient implementation mistake, and a sole reliance on linear regularized readout. It also demonstrates that a free lookup table is not necessary: one ordinary shared MLP with continuous observation nuisance can show the geometric compression.

It does **not** distinguish every effect of a changing sampling objective from every effect of feedback. The frozen and adaptive samplers match at the fork; their conditional sampling laws subsequently diverge. Local field theory, rather than the final metrics alone, is needed to isolate the extra derivative introduced by feedback. Parameter-space tangent geometry, learned nuisance directions, and finite-batch composition can alter free-embedding stability calculations.

The data still have four semantic combinations. Therefore this experiment weakens a lookup-parameterization objection, but does not rule out a four-semantic-state limitation. It has one renderer, one noise scale, one pairwise loss, one negative-policy parameter, and one finite training window. Shared evaluation observations make policy comparisons matched; six seeds represent initialization and training variation rather than six independently sampled applications. No claim about natural images, arbitrary pretrained representations, hard-negative mining in general, or asymptotic stability follows.

## Contribution boundary

These results can serve as a limited empirical bridge accompanying a genuinely new local feedback theorem. They cannot by themselves establish a new general collapse theory or justify a standalone broad empirical claim. The preregistered large clean-loss endpoint failed, and that failure belongs in any paper. The robust compression and continued clean accessibility provide a sharper phenomenon than “the representation forgot a factor”: feedback can make a factor geometrically fragile before, and without proving, exact information loss.

Necessary reinforcement depends on the theorem's final claim. If it is restricted to local normalized geometry and the influence of sampling-policy derivatives, the remaining experiment work is broader task/state and loss validation. If the proposed contribution requires permanent semantic erasure or general pretrained failure, the current evidence does not establish its central hypothesis; that would be a different and currently unsupported research claim.

## Reproducibility map

- `protocol.md`: fixed pre-execution design and original decision endpoint.
- `progress.md`: execution history, failed endpoint, and time of OLS audit declaration.
- `run_encoder.py`, `config.json`: renderer, model, manual gradients, exact finite-batch policy average, training seeds and all endpoints.
- `audit_results.py`: fixed OLS measurement check, reconstruction of initial snapshots, initial sampler match and numerical checks.
- `analyze_results.py`: numeric aggregates and figure creation.
- `results/runs.json`: final metrics, class-mean Gram matrices, eigenspectra, Walsh energies and training curves.
- `results/models.json`, `results/models_initial.json`: all compact parameter arrays; no large checkpoints or data downloads.
- `results/gradient_check.json`, `results/audit_summary.json`: raw numerical verification.
- `figures/readout_audit.{png,svg}`, `figures/factor_energy_dynamics.{png,svg}`: verified scientific figures.

All equations in this file specify the experiment. No unexecuted experiment or unproved generalization is presented as an observed result.
