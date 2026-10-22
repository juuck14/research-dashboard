# Natural exponential cutoff: population dynamics check

Recorded 2026-10-22 before this dynamical execution, after the exact theorem identified the cutoff. This is a prediction check, not a blind discovery of the parameter values. The policy omega(s)=4^(-s),epsilon=.3 was selected by the analytic value/slope inequalities, not by searching successful trajectories. Previous shaped-family and natural kappa=-1 failures remain in the record.

## Fixed model and controls

Four equiprobable two-bit observations, independently trainable d4 unit embeddings, identity positives, iid negatives with replacement. Exact multinomial enumeration of the finite-K population field; no Monte Carlo noise. Compare K4 and K5, each frozen-square q versus adaptive q, identical initial embeddings. Both embedding branches receive gradients. Use the existing field implementation only after it passed independent ordered-tuple/finite-difference checks; this experiment is a dynamics check, not an independent reimplementation of the field.

## Initial conditions and measures

Seeds8101,8102 primary and8301,8302 confirmation. Initialize with a factor-balance angle delta=1e-5 plus arbitrary ambient d4 perturbation with standard deviation1e-6, then row normalize. Thus the initialization is not constrained to the tied-angle subspace. Measure B(F)=||E[a f]||²-||E[b f]||², a rotation-invariant factor energy imbalance. Near the square its leading mode is the balance mode. This is a geometry measure, not MI or readout accuracy.

For each K integrate to3/abs(lambda_balance_adaptive) with Radau,rtol1e-8,atol1e-12. This long horizon is specified from the predicted slow eigenvalue before running: K4 is just below the threshold and can otherwise look stable for a finite observation window. Save t×abs(lambda)∈{0,.5,1,2,3}. Check norm error. At fixed endpoints, frozen B should shrink below.1 of its initial magnitude for both K; adaptive K4 should grow above10 and adaptive K5 shrink below.1. Expected local ratios are exp(+3) and exp(-3), respectively. If these criteria fail, inspect solver accuracy and nonlinearity without changing the initial magnitude/parameters to produce a desired result. No claim of global convergence or semantic erasure follows.
