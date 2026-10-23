# Independent audit of the general policy and temperature theorem

2026-10-23. Reviewed `theory_value/filtered_full_spectrum.md` directly; rederived the quantities below rather than treating the author's numerical checks as proof. No defect was found in the stated theorem. This audit establishes mathematical support within its assumptions, not academic importance by itself.

At the class simplex, every negative cosine equals r=−1/(C−1). Write a=exp((r−1)/tau), D=1+Ka, B=Ka/D, T=1−a/D and eta=−tau(1−epsilon)(log omega)'(r). For any sphere tangent Z, let h_ij be the first Gram derivative and let bar h_i and V_i be its row mean and variance on j≠i.

## Checks that could have broken the result

1. **The tuple mean term.** With K independent uniform off-class candidates,
   E(sum h)^2=K V_i+K² bar h_i². Substituting into the ordinary log-sum Hessian gives B[T V_i+bar h_i²/D]/tau². Using K E h² instead would incorrectly remove the mean correction.
2. **The sampler normalizer.** Its score derivative is (1−epsilon)(log omega)'(r)(h_ij−bar h_i). Pairing the score gradient with the derivative of the tuple law gives −B eta V_i/tau². The response therefore acts on variance, not on the row mean. The row normalization is essential.
3. **Sphere curvature.** For a normalized curve, s''_ij=2 z_i·z_j−r(||z_i||²+||z_j||²). Summing over i≠j cancels all individual norms because r(C−1)=−1, leaving 2||sum z_i||². This gives 2B||sum z_i||²/[C(C−1)tau]. The different temperature power from score curvature is retained.
4. **Possible non-self-adjoint part.** At the simplex, the score-response operator is the bilinear row covariance; it is symmetric. Combining it with the ordinary Hessian and sphere term gives the entire linearization, rather than only its symmetric part. This uses the common off score and independent uniform candidate law at the reference.

Thus the exact directional form is

Q=B/tau² E_i[(T−eta)V_i+bar h_i²/D]+2B||sum z_i||²/[C(C−1)tau].

## Independent coefficient derivations

For the centroid-changing mode z_i=u−(v_i·u)v_i with u in the simplex span, direct summation gives

- ||Z||²=C(C−2)||u||²/(C−1).
- E_i V_i / ||Z||²=C²/(C−1)^4.
- E_i bar h_i² / ||Z||²=C(C−2)/(C−1)^4.
- ||sum z_i||²/||Z||²=C(C−2)/(C−1).

These reproduce the stated barycentric rate. Shape directions have zero row means and centroid; ||h||²/||Z||²=4C/(C−1), reproducing 4B(T−eta)/[(C−1)² tau²]. Common ambient-normal motion has h=0 and centroid-norm ratio C, hence rate 2B/[(C−1)tau]. The remaining ambient-normal zero-sum directions and in-span skew motions are rotations. Their dimensions sum with the shape and barycentric blocks to C(d−1); no tangent subspace is omitted.

For eta<T, the quadratic form is nonnegative and its only null directions are rotations. For eta>T, the nonempty C(C−3)/2 shape block is negative. C≥4 is indispensable; the claimed necessity is not justified from an empty shape space at C3. Equality eta=T gives a zero shape block and is correctly excluded from strict linear attraction.

Algebraically eta<1−a/(1+Ka) is equivalent, when eta<1, to K>1/(1−eta)−1/a. At eta≥1 no finite K meets it. For fixed finite K every sufficiently hard/nondecreasing local log weight has eta≤0 and is strictly attractive at this target. This is a local criterion, not a theorem that all hard samplers work globally.

## Scope preserved by this audit

The result is exact for full-capacity, row-normalized finite class prototypes with independent true negatives and detached gradient flow. Its extension from exponential to general positive smooth score weights is legitimate, since only their first log derivative is present in the reference linearization. It does not remove the regular-simplex exchange symmetry. It also does not establish behavior of a general neural parameterization or a global convergence probability. The independent multiview calculation in `multiview_proof.md` addresses a different issue—whether the bad attractor relies on identity positives—not this theorem's generalization to arbitrary geometry.
