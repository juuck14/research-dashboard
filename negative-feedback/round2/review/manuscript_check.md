# Final read-only manuscript verification

Date: 2026-10-22. Audited `../manuscript.md` after the complete round-two results were assembled. No manuscript edits were made by this critic; the root owns integration.

## Overall assessment

The displayed complete tangent spectrum, inverse-moment threshold proof, full-space sufficient conditions, natural exponential open regime, denominator ordering, four certified integer brackets, and principal numerical results agree with the independently verified analysis. The manuscript explicitly retains the DCL K1 frozen-neutral exception, nonhyperbolic equality boundary, failed encoder primary endpoint, exact-information limit, and quantile tolerance issue. No new experiment is required to resolve an identified mathematical defect.

## Corrections requested from the root

1. **Section2.1 toy performative example:** explicitly state `Z∈{−1,+1}`. With that support, the adaptive field is `theta−tanh(m theta)` and its derivative is1−m. If readers interpret Z as Bernoulli0/1, zero is not an equilibrium and the derivative would be1−m/2. Suggested insertion: “for Z in {−1,+1}, loss theta²/2−Z theta ...”.
2. **Section2.1 K1 scalar-weighting reduction:** replace “reduces locally to” by “is proportional to” before `v ell''(0)+g ell'(0)`. The factor eigenvalue for the one-negative logistic loss is twice that expression; the argument concerns its sign.
3. **Section4.4 Palm sums:** `S_(K−1)` is undefined and collides with the already defined weighted-count S. Define a new name, e.g. `L_m=sum_(l=1)^m Z_l`, and use it in both normal Palm denominators and F_z.
4. **Section6.1 shaped-policy all-K stability:** qualify alpha−1.5's “stable for every K” as **InfoNCE, beta1**. It is false for DCL K1 because eta>0 while T_(1,0)=0. The alpha0 instability claim is valid for both denominators. For the same reason, add “Under InfoNCE” to Section5's summary sentence about the square being frozen-stable for all K before introducing its DCL counterpart.
5. **Section7.1 check-count units:** the author's52 finite-difference settings each check frozen and adaptive spectra, whereas the critic's78 count individual policy spectra. Suggested wording: “52 settings, checking both frozen and adaptive spectra”; retain “78 individual spectrum comparisons” for the critic. This is a reporting-unit clarification, not an invalid numerical result.

These requests were sent to the root by message for direct integration. The count-law theorem itself remains verified.

## Root integration

2026-10-22: All five corrections above were applied to manuscript.md, including the explicit InfoNCE qualifiers and separate Palm sum notation. The natural-example chronology was also aligned with the independent source reviewer: analytic example selection preceded completion of the open-regime proof.
