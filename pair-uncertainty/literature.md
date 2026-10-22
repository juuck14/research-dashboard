# 원문 대조와 신규성 감사

기준일2026-10-22. 초록, 직접 읽은 본문, 우리 계산을 구별했다. 외부 원문은 scratch에만 두고 저장소에는 올리지 않는다.

## 1. 가장 가까운 positive result: Kirchhof–Kasneci–Oh2023

**Probabilistic Contrastive Learning Recovers the Correct Aleatoric Uncertainty of Ambiguous Inputs**, ICML2023, PMLR202,17085–17104. [공식 서지](https://proceedings.mlr.press/v202/kirchhof23a.html), [원문](https://proceedings.mlr.press/v202/kirchhof23a/kirchhof23a.pdf).

직접 읽음: §4.1–4.2, 식2–4, Prop4.1–4.3/Thm4.4, Appendix A.1–A.4, §5/AppendixB의 통제 실험과 misspecification. PDF SHA256: 2005dfcd0adc9a32c90aa86a04db47bb0d0aa15ae408e3367a3f7818668c4978.

Uniform latent/aggregate posterior, 알려진 고정 positive concentration, true와 learned posterior의 vMF family, population infinite-negative objective 아래 posterior를 orthogonal transform까지 회복한다. Prop4.1은 expected positivity 일치와 loss optimum을 연결한다. AppendixA.3은 동일 observation을 양쪽 argument에 대입하여 concentration을 먼저 고정하고 cosine geometry를 복구한다.

우리와의 차이: unknown kernel이면 전제가 바뀌지만 그 사실만으로 비식별이 따라오지는 않는다. 직접 명제1은 circle/homoscedastic/known mean geometry subclass에서 unknown scalar positive concentration도 식별됨을 보인다. 임의 unknown nonlinear mean map에 대한 결과가 아니다. Arbitrary categorical 반례는 원문 정리의 반례가 아니며, 분포 encoder·MCInfoNCE·known-kernel uncertainty recovery 자체는 새 기여가 아니다. 원문의 empirical non-vMF robustness도 arbitrary family의 exact recovery theorem은 아니다.

## 2. pair/triple 차이는 고전 latent-variable identification

**Anandkumar, Ge, Hsu, Kakade, Telgarsky2014**, *Tensor Decompositions for Learning Latent Variable Models*, JMLR15(80),2773–2832. [원문](https://jmlr.org/papers/volume15/anandkumar14b/anandkumar14b.pdf).

직접 읽음: §3.1 Thm3.1, §3.3 Prop3.1/Thm3.6, §4의 whitening/tensor decomposition. Second-order moment는 rank-one matrix들의 합이고 third-order는 rank-one tensor들의 합이다. 각 view의 component mean matrix가 full column rank이면 asymmetric moments도 symmetrize하여 tensor recovery로 연결한다. 원자료 Q/R는 finite categorical conditional-iid model의 Gram ambiguity다. 세 independent view recovery는 이 틀 안에 있다. 같은 original의 crop 세 개가 conditional independence를 만족한다는 결론은 나오지 않는다.

**Allman, Matias, Rhodes2009**, *Identifiability of parameters in latent structure models with many observed variables*, Annals of Statistics. [저자 원문](https://jarhodesuaf.github.io/papers/Latent.pdf), [DOI](https://doi.org/10.1214/09-AOS689).

직접 읽음 및 독립 검토: 서론의 law identification/label-permutation 구분, Kruskal Thm1/Cor2 조건. r=3과 full-rank3인 세 emission matrix는 ranks 합9≥2r+2=8로 up-to-permutation 식별된다. “pair가 불충분하고 세 independent view면 회복”은 새 원리가 아니다. Our symmetric sharp interval과 똑같은 closed form을 이 논문들이 썼다고 확인한 것은 아니지만 표준 factorization·interval decision의 직접 계산이다.

## 3. replicate와 measurement error

**Delaigle, Hall, Meister2008**, *On deconvolution with repeated measurements*. [저자 원문](https://researchers.ms.unimelb.edu.au/~aurored/dhm9.pdf).

독립 reviewer가 원문을 읽어 replicate-difference characteristic function과 unknown-error 추정을 대조했다. Categorical r=a², circular E cos(X−X')=A1(a)²는 이 Fourier/independence 원리의 특수 경우다. [별도 분석](../prevalidation-20261022/operational-uncertainty/analysis.md)에 대조가 있다. 단순히 independent repeat가 모호성을 줄인다는 것을 새 acquisition 원리로 주장하지 않는다.

**Jeon2025**, *Deconvolution density estimation on Lie groups without auxiliary data*. [출판사](https://www.sciencedirect.com/science/article/pii/S0047259X25000594).

확인 제한: 출판사/소속기관 서지·초록만 확인. Unknown parametric measurement-error를 auxiliary 없이 다룬다. Full theorem을 확보하지 못했으므로 circle A_n(a)²A_n(b) 정리를 이미 해결했다고 주장하지 않고 기각의 단독 근거로도 쓰지 않는다.

## 4. exact-identifiable인데 Fisher singular인 경우도 고전 이론

**Rotnitzky, Cox, Bottai, Robins2000**, *Likelihood-based inference with singular information matrix*, Bernoulli6(2),243–284. [원문](https://projecteuclid.org/journals/bernoulli/volume-6/issue-2/Likelihood-based-inference-with-singular-information-matrix/bj/1081788028.pdf).

Reviewer가 §2, §4.3 Thm4를 직접 읽었다. Higher-order likelihood와 magnitude/sign의 다른 convergence scales를 다룬다. Root의 t⁴/t⁶ KL은 구체 모형의 명제이고 차수 구분 자체의 새 일반 원리가 아니다. Nuisance/estimator 전체의 sharp rate는 별도로 확인해야 하며 two-point KL을 일반 MLE minimax theorem으로 확대하지 않는다.

## 5. 최신2026 직접 충돌

**Zhang–Chen2026**, *Uncertainty-Aware Probabilistic Constrained Clustering from Entangled Pairwise Supervision*, arXiv2608.12027, v2(2026-10-14). [고정 version 원문](https://arxiv.org/pdf/2608.12027v2).

실제 PDF를 확보하여 §3.1–3.2, AppendixA.1–A.5를 읽었다. SHA256 f234e38e118841fc5300eda5bd55cc481db320d69211b2a013e9a251ea915c99. Web parser 실패와 별개로 curl다운로드/PDF text추출에 성공했다. 본문의 NeurIPS2026 표기는 독립 venue확인 없이 공개 preprint로 취급한다.

Canonical aleatoric relation, expert distortion, stochastic corruption을 분리한다. Thm3.5는 logistic-normal+uniform contamination, centering, **Ass3.4 structural separability** 아래 conditional law identification이다. AppendixA.4는 두 함수족이 겹치면 zero-mean shift를 옮길 수 있음을 명시한다. Unknown positive convolution/PCL posterior를 해결한 것은 아니지만 “pair uncertainty의 서로 다른 원인”이라는 넓은 문제 제기의 신규성을 낮춘다.

**Peng et al.2026**, *Does a Shared Temperature Imply a Shared Angular Scale in Probabilistic Contrastive Learning?*, arXiv2609.38784v1(2026-09-30). [원문](https://arxiv.org/html/2609.38784v1).

§2의 ProCo score와 §3–4의 범위 확인. 고차원 vMF class-distribution concentration이 angular gain에 미치는 효과다. Observation aleatoric posterior/unknown acquisition kernel과 같지 않으며 shared-temperature라는 이름만으로 중복 처리하지 않는다.

## 감사 결론

원형 repeated-vMF convolution unknown(a,b) 식별과 완전히 같은 정리를 이미 출판한 논문을 발견했다고 주장하지 않는다. 그러나 현재 내용은 제한 모형의 Bessel급수, 표준 channel factorization의 closed form, singular inference/replicate 원리의 구체화다. 임의 nonlinear/heteroscedastic encoder 및 실제 SSL objective의 중요한 공백은 아직 해결하지 못했다. Toy개수나 seed수로 그 간극을 대신할 수 없다.
