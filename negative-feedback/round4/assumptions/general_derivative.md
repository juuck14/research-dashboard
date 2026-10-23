# What conditional balance removes, exactly

2026-10-23. Direct analysis of the existing scalar score model. These are scope clarifications and standard moment/total-positivity arguments, not evidence of top-journal importance or a new general learning theory.

## 1. General affine scalar field

Let p be fixed, s_delta=s+delta h, W=exp(s−1), beta≥0, and

\[
r_\delta(dy)=e^{-t s_\delta(y)}p(dy)/Z_\delta,
\quad q_\delta=\epsilon p+(1-\epsilon)r_\delta,
\quad \rho(y)=(1-\epsilon)\frac{dr_0}{dq_0}(y).
\]

Set b=E_(r0)h. There is **no** conditional-balance assumption here. The derivative of the normalizer is Z'_0/Z_0=−t b, so

\[
\frac{q'_0(y)}{q_0(y)}=-t\rho(y)\{h(y)-b\}.
\]

For K iid q0 draws, put D=beta+sum W_i, A=sum W_i h_i. The detached field and its derivative at0 are exactly

\[
\boxed{G_K(0)=\mathbb E\frac A D,}
\]

\[
\boxed{G'_K(0)=\mathbb E\left[
\frac{\sum_i W_i h_i^2}{D}
-\frac{A^2}{D^2}
-t\frac A D\sum_i\rho_i(h_i-b)
\right].}
\]

Proof: differentiate the loss for a fixed tuple, then differentiate its probability. The last term is the tuple score of q_delta, including its normalizer. Finite sums or bounded positive score weights justify differentiation. This is a direct product-rule calculation, not new mathematics.

**Crucial interpretation:** G'_K(0) is a derivative at a potentially drifting point. It is a restoring/stability derivative of an equilibrium only if G_K(0)=0. If a perturbation destroys stationarity, a retained positive slope is not a proof that the old point is still stable, and a negative slope is not itself a new instability counterexample.

## 2. Exact conditional-mean decomposition

Write m(W)=E[h|W], v(W)=Var(h|W). Conditioning on tuple scores gives M=sum W_i m_i and T=sum rho_i(m_i−b), where b=E_r m. Then

\[
G_K(0)=\mathbb E[M/D],
\]

\[
G'_K(0)=\mathbb E\left[
\frac{\sum W_i(v_i+m_i^2)}D
-\frac{M^2+\sum W_i^2v_i}{D^2}
-t\frac{MT+\sum W_i\rho_i v_i}{D}
\right].
\]

The existing tagged formula is precisely the m=0 part. For any h, let xi=h−m(W). At fixed reference score law, G is linear in h and H=G' is quadratic in h. Conditional centering makes all bilinear terms between xi and any deterministic score function vanish. Therefore

\[
\boxed{G[h]=G[m],\qquad H[h]=H[\xi]+H[m].}
\]

Here H[xi] obeys the old balance-law hypotheses, while H[m] does not. Thus the existing theorem governs the **conditionally centered component** of a score perturbation. In a finite generic list with all different scores, xi=0, so it does not cover a nontrivial direction of that list.

For a balanced h0 and a deterministic score function a(W), set h_tau=h0+tau a(W). The decomposition yields the exact identities

\[
\boxed{G[h_\tau]=\tau G[a],\qquad
H[h_\tau]=H[h_0]+\tau^2 H[a].}
\]

Small conditional-mean violations can therefore produce **first-order drift and only second-order slope changes**. A numerical derivative may appear robust even while the point being differentiated is no longer stationary. If |a|≤L, then |G[h_tau]|≤|tau|L and the elementary fixed-K bound |H[h_tau]−H[h0]|≤tau²(1+2|t|K)L² follows from the displayed tuple formula. This is a loose finite-K bound, not a uniform all-count robustness theorem.

## 3. Common stationarity across counts is equivalent to conditional balance

Assume W lies in a compact subset of(0,infinity), h is bounded, beta is fixed, and the same q0 is used at the reference for every K. The policy need not be exponential for this proposition. For the detached affine loss,

\[
G_K(0)=0\text{ for every integer }K\ge1
\quad\Longleftrightarrow\quad E_{q_0}[h|W]=0.
\]

If dq0/dp is a positive function of s, as in the existing policy, the right side is equivalent to E_p[h|s]=0.

**Proof.** Let phi(u)=E_q exp(−uW), psi(u)=E_q[Wh exp(−uW)]. Tagged exchangeability and the Laplace denominator identity give

\[
G_K(0)/K=\int_0^\infty e^{-\beta u}\phi(u)^{K-1}\psi(u)\,du.
\]

Phi is continuous and strictly decreasing from1 to0. The signed measure with density e^(-beta*u)psi(u) is finite because W has a positive lower bound. Push it forward by phi onto[0,1]. If every G_K is zero, every nonnegative-integer moment of this finite signed measure is zero. Polynomial density in C[0,1] implies the signed measure is zero. Since phi is one-to-one, psi=0 almost everywhere, hence everywhere by continuity. Differentiating psi at0, or applying uniqueness of the Laplace transform on compact support, gives E[Wh|W]=0, equivalently E[h|W]=0. Conversely conditional centering immediately gives G_K=0 for every K. QED.

This proposition explains the strength of the hypothesis. Balance is not merely a convenient way to cancel algebra; in this affine scalar family it characterizes a **common reference equilibrium across all negative counts**. It does not imply that an arbitrary trained system lacks equilibria. Rather, generic asymmetric systems must usually be compared at count-dependent equilibria instead of at one universal reference point.

## 4. Finite-support strengthening: the first L counts suffice

Suppose W has exactly L distinct support values0<W1<...<WL with positive masses q_i. Write m_i=E[h|W_i]. Then

\[
G_1(0)=\cdots=G_L(0)=0\quad\Longleftrightarrow\quad m_i=0\text{ for every }i.
\]

**Proof.** Put f_n(x)=E(x+S_n)^(-1). The equations are linear in c_i=q_i W_i m_i, with coefficient matrix F_(i,k)=f_(k−1)(beta+W_i). Its determinant is strictly positive. Indeed f_n(beta+W_i)=integral_0^infinity exp(−W_i*u)phi(u)^n exp(−beta*u)du. Expanding the determinant and symmetrizing the L integration variables gives the Andreief identity

\[
\det F=\frac1{L!}\int_{(0,\infty)^L}
\det[e^{-W_i u_j}]\det[\phi(u_j)^{k-1}]
\prod_j e^{-\beta u_j}du_j.
\]

On0<u1<...<uL both determinants have sign(−1)^(L(L−1)/2), so their product is strictly positive. The second determinant is a Vandermonde determinant in decreasing phi(u_j). For completeness the first determinant is nonzero because a nontrivial linear combination of L exponentials with distinct exponents has at most L−1 real zeros: divide by one exponential and apply Rolle's theorem inductively to its derivative. Its sign follows by coalescing the ordered u values; the Wronskian has sign(−1)^(L(L−1)/2). Continuity preserves that sign throughout the ordered domain. Hence det F>0, c=0, and all m_i=0. The converse is immediate. QED.

The determinant argument is an application of established strict total positivity/sign regularity and the integration identity, not a new mathematical principle. It reinforces the scope point: on L distinct deterministic candidate scores, requiring one nonzero affine direction to be stationary at the first L counts is already impossible. Conversely, being stationary at just one count does **not** imply conditional balance or the all-K sign classification.

## 5. What this does and does not change

The old conditional-balance theorem is not refuted. Its exact classification is valid in the stated common-reference setting. The analysis clarifies that continuity of the population distribution and many score levels do not make that setting generic. Breaking exact symmetry can move the stationary point by first order while barely changing a measured slope; the location and sign must be studied together.

For a general twice differentiable score path with s''_0=kappa, the general formula also acquires the term E[sum W_i*kappa_i/D]. Conditional centering of h does not remove this term. Thus the audit does not remove the existing affine-path restriction either. A Gram-realizable nonlinear embedding perturbation may have such geometric curvature even when its first-order score derivative resembles the affine model.

Smooth perturbation of a hyperbolic equilibrium may preserve a nearby equilibrium with the same local inertia. That is standard implicit-function/stability theory, not a discovery here and not a reason to claim that arbitrarily small asymmetry destroys the mechanism. Near a zero-curvature boundary, location shifts can be amplified, and no generic count law follows from the old proof. The numerical checks in this directory verify the exact decomposition and count-dependent root shifts, without labeling those shifted models a new representation-learning contribution.
