# 후보 3 — 독립 비판 검토

담당 uncertainty_review. 2026-10-22. **현재 구체화의 독립 연구 착수에는 기각 의견**이다. 이는 uncertainty/unknown-correspondence 문제 전체가 해결됐다는 결론이 아니다. 원가설은 명시한 vMF subclass에서 반박되었고, 실행으로 살아남은 categorical·singular 사례는 고전 결과의 구체 대입이라는 반론을 아직 넘지 못했다.

## 무엇을 직접 확인했는가

| 증거 종류 | 확인 내용 | 범위 |
|---|---|---|
| 문헌 원문 | PCL2023 Theorem4.4의 known positive concentration; Allman2009 Cor2; Anandkumar2014 Thm3.1/4.3; Liu2023 Thm4.2; Rotnitzky2000 §2/Thm4; Delaigle2008 Eq2.1–2.3 | 아래 읽은 범위 명시 |
| 직접 증명 | circle-vMF의 양의 두 concentration은 전체 pair Fourier sequence로 joint identifiable | known mean map, homoscedastic circle family |
| 직접 증명 검토 | diagonal null-path의 KL 차수 t⁴/t⁶와 양의 leading constants | 특정 simple vs simple 판별; 일반 minimax theorem 아님 |
| 독립 실행 | 1001 primary+200 random categorical Gram orbit 계산; 42 Bessel expansion 계산 | script가 owner code를 import하지 않음 |
| owner 감사 | 144개 explicit latent enumeration; 60 pair datasets/180 prediction CSV 검사 | posterior/held-out repeat 위험은 population law로 평가 |

재현 명령은 `OPENBLAS_NUM_THREADS=1 python prevalidation-20261022/reviews/uncertainty/independent_check.py`, `OPENBLAS_NUM_THREADS=1 python prevalidation-20261022/reviews/uncertainty/owner_audit.py`. 실행 전 [protocol](protocol.md), [실패·변경 이력](progress.md), [summary](results/summary.json), [owner audit](results/owner_audit.json), [독립 증명](exact_identification.md)을 함께 보라.

## 결정적인 문헌 충돌

1. **Allman, Matias, Rhodes (2009), _Identifiability of parameters in latent structure models with many observed variables_.** [저자 원문](https://jarhodesuaf.github.io/papers/Latent.pdf), pp16–17 Theorem1/Corollary2와 pp30–31 증명 확인. 세 conditional-independent observation의 Kruskal rank 합이 `2r+2` 이상이면 mixture parameters가 label permutation까지 식별된다. r=3, rank3 emission toy는 `9≥8`로 직접 적용된다. 따라서 pair 모호성과 informative third view의 식별은 새 발견이 아니다. 모든 세-view가 자동 식별된다는 일반 명제도 아니다.

2. **Anandkumar et al. (2014), _Tensor Decompositions for Learning Latent Variable Models_.** [JMLR 원문](https://jmlr.org/papers/volume15/anandkumar14b/anandkumar14b.pdf), §3.1 Theorem3.1, §3.3, §4.3 Condition4.1/Theorem4.3 확인. conditional independent categorical data의 pair/triple moments가 emission의 rank-one sums가 되고, positive mixture weight와 independent emission columns에서 whitening된 third-order tensor가 원래 parameters를 복원한다. 이번 3-state toy의 tensor recovery는 이 계산에 포함된다.

3. **Liu, Cheng, Zhang (2023), _Identifiability of Label Noise Transition Matrix_.** [ICML 원문](https://proceedings.mlr.press/v202/liu23g/liu23g.pdf), Theorem4.2 및 부록 pp15–16의 sufficiency/2-label construction 확인. conditional iid informative noisy labels라는 조건에서 세 noisy labels의 필요·충분을 다룬다. label noise는 observation 의미가 다르지만 같은 latent-mixture inverse problem이므로 ‘관측 ambiguity와 noise를 여러 view로 분리’라는 일반 주장의 신규성을 차단한다. arbitrary correspondence kernel 전체를 다룬 논문이라고 해석하지 않는다.

4. **Rotnitzky, Cox, Bottai, Robins (2000), _Likelihood-based inference with singular information matrix_.** [출판사 링크](https://projecteuclid.org/journals/bernoulli/volume-6/issue-2/Likelihood-based-inference-with-singular-information-matrix/bj/1081788028.pdf)는 접근 challenge가 있어 [저자 업로드 원문](https://www.researchgate.net/profile/Andrea-Rotnitzky/publication/38322350_Likelihood-Based_Inference_with_Singular_Information_Matrix/links/55840d1e08ae89172b885135/Likelihood-Based-Inference-with-Singular-Information-Matrix.pdf)을 읽었다. §2(pp246–247), §4.2 B1–B3, §4.3 Theorem4와 pp262–263 확인. s=2의 magnitude `n^-1/4`와 sign `n^-1/6` 구분 자체가 이미 명시되어 있다. 우리 t⁴/t⁶는 유용한 모델별 계산이지만 새 일반률이 아니다. nuisance score에 대한 고차 derivative residual 조건을 확인하지 않고 그 논문의 estimator 정리를 그대로 적용할 수도 없다.

5. **Delaigle, Hall, Meister (2008), _On deconvolution with repeated measurements_.** [저자 공개 원문](https://arxiv.org/pdf/0804.0713), §2.1 Eq(2.1)–(2.3)와 §3 정리의 가정 확인. 같은 latent의 independent symmetric measurement repeats에서 difference의 Fourier coefficient로 error Fourier transform의 제곱근을 추정한다. 우리 `E cos(X−X_repeat)=r1(a)^2`는 정확히 같은 cancellation을 circle의 integer harmonic에 적용한 것이다. repetition의 유용성만으로 새로운 관측설계 원리를 확보했다고 볼 수 없다.

6. **Jeon (2025), _Deconvolution density estimation on Lie groups without auxiliary data_.** [출판사](https://www.sciencedirect.com/science/article/pii/S0047259X25000594), DOI10.1016/j.jmva.2025.105464와 저자 publication 목록은 확인했다. 검색으로 접근 가능한 초록·서론·section preview에는 unknown parametric noise의 identification과 parametric MLE, circle의 wrapped Gaussian/Laplace/Cauchy simulation이 보인다. **Proposition1의 정확한 가정·증명 및 본문 전체는 확보하지 못했다.** 따라서 이 논문이 우리 exact-vMF 정리를 이미 포함한다고 단정하지 않으며, 최종 기각의 결정 근거로 쓰지 않는다. 본격 확장 시 반드시 확보할 직접 인접 문헌이다.

7. PCL2023의 local copy 본문 Theorem4.4와 §4.1/AppendixA를 대조했다. known `κ_pos`, uniform spherical latent, vMF true/learned posteriors, population limit의 보장이다. 임의 categorical 반례는 이 theorem 반박이 아니다. Owner의 circle example은 genuine generative subclass이지만 **mean map까지 고정**하므로 unknown-kernel neural encoder 전체를 식별한 결과도 아니다.

## 독립 계산 결과와 해석

이전 Q/R example의 pair law는 같고 triple 예측은 다르다. 그러나 uniform3·doubly-stochastic square emissions·고정 Gram이라는 제한 family에서는 전체 대안이 `Eθ=J/3+aOθ(I−J/3)`인 orthogonal orbit이다. `a=.4≤.5`여서 모든 angle이 feasible하다. determinant −1 부분도 column permutation 뒤 같은 angle family로 환원되므로 범위가 더 넓어지지 않는다. 직접 cubic moment 대입은

`P(X3=1 | X1=X2=1)=(1+6a²+2a³cos3θ)/(3(1+2a²))`

를 준다. sharp interval은 `[.4626262626,.5272727273]`다. 1201개 enumeration에서 formula 최대오차 `3.33e−16`, pair law 최대오차 `8.33e−17`였다. 이는 정확하지만 **표준 Gram factorization을 cubic target으로 밀어낸 결과**라는 반론을 넘지 못한다. 임의 prior·rectangular emission을 허용한 sharp set가 아니다.

Owner의 unknown-kernel symmetric channel branch도 별도 double-latent enumeration으로 확인했다. 144조건에서 pair formula 오차≤`1.67e−16`, repeat conditional formula 오차≤`3.33e−16`, mass 오차≤`4.44e−16`. 같은 finite-pair sample의 세 policy는 실제로 같은 c_hat를 쓰며 unknown-b 두 policy의 expected pair risk 차이는≤`3.43e−16`다. finite60 data sets/180 predictions가 180개 독립 증거라는 뜻은 아니다. known-b 비교는 추가 oracle 정보를 가지므로 공정한 pair-only estimator 우월성 비교가 아니다. Owner는 이 점을 모델 assumption 비교로 사용한다.

Finite-sample script가 실제로 생성한 것은 pair samples이며 repeat 위험은 true population conditional에 대한 정확한 기대값이다. 별도 held-out third observations를 생성해 calibration을 측정한 실험은 없다. 이 분석에는 population score가 적절하지만, ‘neural SSL calibration 확인’이라고 쓰면 안 된다. a=1 대안의 log risk는 무한대이며 clipped diagnostic을 exact finite log score와 구별한 owner amendment는 타당하다.

## 반박에 대한 결론과 미해결 이견

- ‘kernel 폭을 몰라서 두 uncertainty를 원리상 구분 못한다’는 원가설은 model family를 명시하면 참/거짓이 갈린다. circle-vMF의 양의 scalar case는 직접 반례다.
- 가장 명확한 negative result는 categorical unrestricted factorization이다. 그러나 고전 inverse problem의 특수 경우라 독립 기여의 크기가 작다.
- exact circle identification과 singular sensitivity는 흥미로운 기술 note가 될 수 있다. 다만 singular inference와 independent repeat의 핵심 논리는 기존 원리다. **현재 확보한 자료만으로 수개월 독립 연구를 우선 착수하라는 근거는 부족하다.**
- Root가 보는 운영상 분해 가능성의 중요성은 인정한다. 내가 낮게 평가하는 부분은 결과의 진실성이 아니라 기존 일반론을 제거한 뒤 남는 학술적 폭이다. 새로운 architecture/loss를 추가하는 것으로 이 반론이 해결되지는 않는다.

재개하려면 (i) 실제 probabilistic SSL objective의 near-optimal set에서 representation/observable target의 sharp law를 얻거나, (ii) heteroscedastic/learned mean family에서 정확한 추가 acquisition budget의 하한·상한이 맞거나, (iii) standard singular explanation은 같지만 uncertainty claim의 성패를 구분하는 현상을 확보해야 한다. 핵심 검증이 아직 이 상태라면 ‘수정 후 진행’ 대신 보류 또는 현재 구체화 기각이 정직하다.
