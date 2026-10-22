# 직접 분석: 무엇이 모형 가정이고 무엇이 관측 정보인가

증거 상태: 아래 명제 1–4는 제한된 모형에서 **직접 증명**이다. 원형 명제 1은 별도 검토자가 Bessel 급수와 대수 복구를 독립 검산했다. 수치 탐색은 이 증명의 대체물이 아니다. 신규성은 [문헌 대조](literature.md) 및 [판정](verdict.md)에서 별도로 평가한다.

## 0. 원래 질문과 추가 탐색 가설의 분리

원래 보고서의 가설은 observation ambiguity와 unknown correspondence law를 함께 허용하면 pairwise objective가 거의 같은 해들 사이에서 관측 예측이 달라질 **수 있다**는 존재적 명제다(source tex307). 모든 unknown kernel에서 실패한다는 주장이 아니며, 보고서는 그 보편 명제를 명시적으로 배제했다(tex309,687). 아래 categorical 결과는 원래 가설의 한 사례를 지지한다. 그 사례가 학술적으로 새로운지는 별도 질문이다.

Protocol의 H1인 **unknown scalar positive concentration 자체가 비식별을 뜻하는가**는 이번 검증에서 추가로 세운 더 강한 탐색 가설이다. 원래 가설의 바꿔 쓴 표현이 아니다. Circle 결과는 이 강한 H1을 반박하지만 원래의 존재적 명제를 반박하지 않는다. Kernel family를 고정하면 어떤 경우 비식별이고 어떤 경우 식별되는지 경계를 정리한 결과로 해석한다. Arbitrary categorical 반례가 Kirchhof et al.2023의 vMF 정리를 반박한다는 주장도 하지 않는다.

## 1. 원형 vMF 모형과 전체 pair law

원형 각도 \(Z\)는 Haar-uniform이다. \(h_k(u)=\exp(k\cos u)/(2\pi I_0(k))\), \(k>0\)라 두고

\[
X\mid Z\sim h_a(X-Z),\quad
Z^+\mid Z\sim h_b(Z^+-Z),\quad
X^+\mid Z^+\sim h_a(X^+-Z^+).
\]

세 noise는 조건부 독립이다. \(X\) 역시 uniform이고 posterior \(Z\mid X\sim h_a(Z-X)\)이므로 원문 PCL의 uniform aggregate/vMF posterior를 만족하는 genuine subclass다. 단 homoscedastic circular geometry와 mean-map identity로 제한한다. 임의 unknown nonlinear encoder에 대한 결과가 아니다. 잠재 회전/반사는 같은 해이며, 임의 diffeomorphism을 동치로 허용하지 않는다.

관측 pair 차이 \(\Delta=X^+-X\)의 Fourier coefficient는

\[
B_n(a,b)=A_n(a)^2A_n(b),\qquad A_n(k)=I_n(k)/I_0(k),\quad n=1,2,\ldots.
\]

이는 \(h_a*h_b*h_a\)의 Fourier 곱에서 직접 따른다. 따라서 pair law를 정확히 아는 것과 모든 \(B_n\)을 아는 것은 같다.

### 명제 1 — unknown positive concentration도 이 subclass에서는 공동 식별된다

양의 유한한 \(a,b\)에 대해 전체 수열 \(\{B_n(a,b)\}_{n\ge1}\)는 ordered pair \((a,b)\)를 유일하게 정한다.

**증명.** \(x=a^2/4,\ y=b^2/4\)라 두자. Bessel의 양의 급수 정의에서

\[
I_n(a)=\frac{(a/2)^n}{n!}S_n(x),\quad
S_n(x)=\sum_{j=0}^{\infty}\frac{x^j}{j!(n+1)\cdots(n+j)}.
\]

\(j=0\)의 분모는1이다. 고정된 \(x\)에서 \(j\ge4\)의 합은
\(\sum_{j\ge4}(x/n)^j/j!=O(n^{-4})\)로 상계된다. \(j=1,2,3\) 항을 전개하여

\[
S_n(x)=1+\frac{x}{n}
+\frac{-x+x^2/2}{n^2}
+\frac{x-3x^2/2+x^3/6}{n^3}+O(n^{-4}).
\]

그러므로

\[
\log S_n(x)=\frac{x}{n}-\frac{x}{n^2}
+\frac{x-x^2/2}{n^3}+O(n^{-4}).
\]

\(H=x\sqrt y=a^2b/8,\ C=2\log I_0(a)+\log I_0(b)\),
\(S=2x+y,\ R=2x^2+y^2\)로 쓰면

\[
\log B_n=n\log H-3\log n!-C
+\frac S n-\frac S{n^2}+\frac{S-R/2}{n^3}+O(n^{-4}).
\tag{1}
\]

수열은 다음 순서의 극한으로 \(H,C,S,R\)을 정한다.

\[
H=\lim_{n\to\infty}(n+1)^3\frac{B_{n+1}}{B_n},\qquad
-C=\lim_{n\to\infty}\{\log B_n-n\log H+3\log n!\}.
\]

두 번째 중괄호를 \(D_n\)이라 하면 \(S=\lim n(D_n+C)\),
\(S-R/2=\lim n^3(D_n+C-S/n+S/n^2)\)다. 이제

\[
e_1=S,\quad e_2=(S^2-R)/2,\quad e_3=H^2
\]

는 multiset \(\{x,x,y\}\)의 elementary symmetric polynomials다. 따라서

\[
u^3-e_1u^2+e_2u-e_3=(u-x)^2(u-y).
\]

이 monic cubic은 \(\{x,x,y\}\)를 유일하게 정한다. \(x\ne y\)이면 double root가 observation parameter \(x\), singleton이 positive parameter \(y\)다. \(x=y\)도 두 값이 같다고 유일하게 정한다. 양의 square root로 \(a,b\)를 복구한다. \(\square\)

**범위.** \(a=0\) 또는 \(b=0\)이면 모든 \(B_n=0\)여서 이 주장은 거짓이다. 양의 finite parameter 조건은 필요하다. 이 증명은 population sequence의 주입성이지 유한 harmonic 또는 유한 표본의 안정성을 보장하지 않는다. 특히 무한대차 극한을 실용 추정법으로 제안하는 것이 아니다.

### 명제 2 — 정확한 식별성과 1차 정보의 특이성은 양립한다

\(f_n(k)=\log A_n(k)\)이면 \(\log B_n=2f_n(a)+f_n(b)\)이다. \(a=b=k\)에서

\[
\partial_a B_n=2\partial_b B_n\quad\text{for every }n.
\]

모든 pair-density derivative 역시 이 비례를 만족한다. 따라서 tangent \((1,-2)\)에서 pair law의 1차 변화는0이다. 어떤 harmonic을 더 보아도 이 점의1차 Jacobian rank는1을 넘지 않는다. 이는 명제1의 global injection과 모순이 아니다.

단순히 rank가 작다고 parameter 비식별을 결론내릴 수 없다. Root의 [운영적 안정성 분석](../prevalidation-20261022/README.md)은 이 점의 고차 local law와 알려진 singular-likelihood 이론을 별도로 검토한다. 본 파일은 아직 없는 sharp rate나 neural loss 명제를 주장하지 않는다.

## 2. categorical unknown-channel 모형의 sharp 집합

이제 다른, 유한한 모형을 쓴다. 이는 vMF 정리의 반례가 아니다. \(J\)는3×3 all-ones matrix,
\(Q_a=aI+(1-a)J/3,\ K_b=bI+(1-b)J/3\), \(0\le a,b\le1\).

\(Z\) uniform, \(X_1\mid Z\sim Q_a\), \(Z^+\mid Z\sim K_b\),
\(X_2\mid Z^+\sim Q_a\). 잠재 permutation만 동치다. 원형 모형과 달리 이 family는 negative eigenvalue를 허용하지 않는다.

### 명제 3 — pair law는 \(c=a^2b\)만 정한다

\[
P_{12}=\frac13Q_aK_bQ_a^\top=\frac13Q_c,
\quad c=a^2b.
\]

따라서 \(0<c<1\)에서 같은 pair law의 **모든** parameter는
\[
\mathcal I(c)=\{(a,b):\sqrt c\le a\le1,\ b=c/a^2\}.
\tag{2}
\]

**증명.** \(P=J/3\)는 projection이고 \(Q_a=P+a(I-P)\)이므로 matrix 곱은 \(P+a^2b(I-P)\)다. Diagonal 또는 off-diagonal entry가 \(c\)를 정한다. \(b\le1\)과 \(a\le1\)은 \(a\in[\sqrt c,1]\)와 동치이며, 구간의 모든 점이 stochastic channel을 만든다. \(\square\)

이는 oracle population의 ambiguity다. 같은 law에서 finite sample이나 seed를 늘려도 (2)는 줄지 않는다. 원문 PCL은 \(b\)를 known으로 고정하고 더 엄격한 geometry를 가정하므로 이 결과와 충돌하지 않는다.

### 명제 4 — 관측 가능한 independent-repeat 예측의 sharp interval

\(R\mid Z\sim Q_a\)를 독립으로 새로 측정한다. 이는 same bytes의 복사나 같은 noisy original의 세 번째 crop이 아니다. \(X_1,X_2,R\)의 법칙은

\[
P(i,j,k)=\frac13\sum_z Q_a(i,z)Q_{ab}(j,z)Q_a(k,z).
\]

사건 \(X_1=X_2=i\)에서

\[
p(a,c):=P(R=i\mid X_1=X_2=i)
=\frac{1+2a^2+4c+2ac}{3(1+2c)}.
\tag{3}
\]

따라서 sharp identified interval은

\[
\boxed{\quad
\frac{1+6c+2c^{3/2}}{3(1+2c)}
\le p\le1.\quad}
\tag{4}
\]

**증명.** \(Q_a\)의 같은 행에서 diagonal \(u=(1+2a)/3\), off-diagonal \(v=(1-a)/3\)이다. \(Q_{ab}\)의 corresponding entries를 \(r=(1+2ab)/3,\ s=(1-ab)/3\)라 하면 triple numerator는 \((u^2r+2v^2s)/3\). Pair denominator는 \((1+2c)/9\). 전개하면 (3)이다. \(\partial_a p=(4a+2c)/(3(1+2c))>0\)이며 (2)의 양 끝이 모두 feasible하다. \(\square\)

\(c=.16\)이면 (4)는 \([29/55,1]\approx[.52727,1]\)이다. 예측할 관측이 존재하고 proper score로 검증할 수 있다는 점에서 posterior entropy 비교보다 명확한 표적이다. 다만 이 식을 얻는 데 새로운 학습 원리가 필요한 것은 아니다.

**제한 모형의 minimax regret.** 같은 context에서 나머지 두 repeat category의 확률은 \((1-p)/2\)다. Vector Brier score의 excess risk는 \((3/2)(\hat p-p)^2\)이므로 구간 width \(\Delta\)에 대한 minimax value는 \(3\Delta^2/8\), midpoint에서 달성된다. 이는 전체 모형·context의 minimax theorem이 아니라 이 명시된 context와 symmetric predictive family의 정확한 값이다. 표준 interval decision의 직접 귀결이며 신규 일반 원리로 세지 않는다.

## 3. 목적함수와의 연결

위 categorical pair model의 density-ratio score는
\[
s_c(i,j)=\log\{3Q_c(j,i)\}
=\begin{cases}\log(1+2c)&i=j\\\log(1-c)&i\ne j.\end{cases}
\]

Uniform negatives에 대해 population infinite-negative contrastive conditional log-loss는 상수까지
\(-\sum_{ij}P_{c_*}(i,j)\log P_c(i,j)\)다. Excess는 \(KL(P_{c_*}\|P_c)\)이며 (2)의 모든 parameter가 동일 optimum이다. 따라서 이 예제의 ambiguity는 optimizer failure가 아니라 objective의 observational equivalence다.

이것은 **정확한 pair-score analogue**이고 original neural MCInfoNCE 구현의 finite-M/finite-K 동역학을 실행했다는 뜻이 아니다. Softmax score의 density-ratio property 및 partial-identification의 표준 귀결을 독창적 loss 이론으로 주장하지 않는다. Near-optimal loss 집합도 scalar \(c\)의 KL sublevel과 각 \(c\)의 ridge의 합집합으로 계산될 뿐이다.

## 4. 추가 acquisition은 무엇을 바꾸는가

모형 B에서 genuine repeat pair \((X_1,R)\)는 correlation \(r=a^2\)를 준다. 따라서 \(a=\sqrt r,\ b=c/r\)로 population point-identification된다. **이 제한 family에서는 joint triple tensor가 필요하지 않다.** 새 repeat pair law로 충분하다.

반대로 original report의 Q/R example은 이미 같은 latent의 conditionally-iid pair(\(K=I\))인데도 emission matrix 자체의 Gram ambiguity가 있다. 세 view의 tensor 식별이 필요한 이유가 다르다. 일반 emission model에 모형 B의 two-moment 결론을 확대하지 않는다.

복제 \(R=X_1\)는 언제나 empirical agreement1을 주지만 conditional independence를 만족하지 않는다. 이를 repeat라고 잘못 취급하면 \(a=1\)을 결론낸다. 이것은 더 많은 tensor entries의 문제가 아니라 acquisition provenance와 가정의 문제다. Bayesian coherence만으로는 이 provenance를 복구하지 못한다.

## 5. 남는 공백

직접 증명한 내용은 새로 추가한 강한 탐색 H1을 좁은 모형에서 반박하고, 다른 family에서 원래 존재적 가설을 지지하는 exact predictive interval을 계산한 것이다. 원래 질문을 circle의 식별 성공으로 대신 해결했다고 주장하지 않는다. 아직 임의 heteroscedastic probabilistic encoder의 near-optimal set, 불완전한 acquisition 조건, 자연 이미지의 calibrated uncertainty를 해결하지 않았다. 이 남은 질문 자체가 다음 논문 기여라는 근거도 아직 없다. 선행 singular inference와 blind deconvolution을 제거하고 남는 새 명제가 필요한 상태다.
