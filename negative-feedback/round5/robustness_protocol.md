# Decoder-independent class-distinction check

2026-10-23. This bridges the new meaningful-target theorem to the already fixed paired trajectories; it is not a new search for a favorable downstream task.

Primary objective is the largest L2 feature perturbation radius under which **every correctly distinct class** can still be decoded. For unit class prototypes its value is half the minimum interclass distance, over all possible decoders, and the simplex packing bound is uniquely optimal. This criterion uses neither original binary coordinates nor a chosen probe/regularizer.

Before evaluating the stored embeddings, fix Gaussian feature noise sigma in{.05,.1,.25} as an additional illustration. The proof is for every fixed sigma>0. For a representation within RMSdelta of any two-valued class-merging representation, Pinsker's Gaussian shift inequality gives Bayes class-ID accuracy≤2/C+delta/(2sigma), capped at1. A nearest-prototype classifier under Gaussian noise gives accuracy≥1−(C−1)Phi(−r/sigma), clipped at0, for any representation with minimum radius r. These are mathematical bounds, not Monte Carlo estimates or optimal-probe fits.

Use every preserved primary/confirmation C4/8,K1/8/32 adaptive trajectory, its same-initialization uniform-off control, and the saved half-step arm. If prototypes are finite and distinct, do not report exact noiseless information erasure. The theorem concerns an exact limiting attractor; the finite observation is radius shrinkage and a noise-dependent accuracy bound. The root code recomputes radii and the two-valued fit from raw embeddings.
