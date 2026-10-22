# 원문 대조와 신규성 감사

## 검증된 원문

| 문헌 | 실제 확인한 범위 | 본 연구와의 관계 |
|---|---|---|
| Khemakhem, Kingma, Monti, Hyvarinen. Variational Autoencoders and Nonlinear ICA A Unifying Framework. AISTATS 2020. https://proceedings.mlr.press/v108/khemakhem20a/khemakhem20a.pdf | 원문 §3.1 conditional factorial exponential-family prior, §4.1 Definition1–2와 Theorem1의 variability/equivalence; pp2–5 | 참 소스가 조건부 독립인 충분조건. 본 계산의 approximate source independence budget은 이 theorem의 직접 가정이 아니지만 linear Gaussian 전용 분석이 더 오래된 eigenvector 문제로 환원됨. |
| Lyu and Fu. On Finite-Sample Identifiability of Contrastive Learning-Based Nonlinear Independent Component Analysis. ICML 2022. https://proceedings.mlr.press/v162/lyu22a/lyu22a.pdf | 원문 도입, conditional independence와 componentwise invertible equivalence, finite sample/approximation 목표 확인 | 표본 한계 분석은 이미 존재. 본 결과는 n→∞에서도 같은 law인 모형집합이므로 표본오차와 구별되지만 그것만으로 새로움은 아님. |
| Buchholz and Schölkopf. Robustness of Nonlinear Representation Learning. ICML 2024. https://proceedings.mlr.press/v235/buchholz24a.html ; full https://arxiv.org/pdf/2503.15355 | full §2 Assumption2.2, §3 pp2–3의 scope, §4–5의 almost-isometry/perturbed-linear ICA 구조 및 AppendixB.1/B.2 확인. §3는 independence misspecification 및 finite sample은 다루지 않는다고 명시. | 이전 보고서의 구별은 실제 존재. 그러나 '그 논문이 독립성 위반을 안 다룬다'가 논문 공백의 증명은 아니다. 특히 이번 Gaussian exact set은 eigenvalue 계산으로 해결된다. |
| Kleinsteuber and Shen. Uniqueness Analysis of Non-Unitary Matrix Joint Diagonalization. IEEE TSP 2013 (preprint 2011). https://arxiv.org/pdf/1111.7088 | full 도입 및 §2–3 uniqueness/essential uniqueness와 collinearity 조건 확인 | 환경별 covariance의 공통 diagonalizer가 distinct signatures에서 유일한 것은 선행. weak-signature separation의 conditioning narrative를 새롭게 주장 불가. |
| Lütkepohl, Shang, Uzeda, Woźniak. Partial Identification of Structural Vector Autoregressions with Non-Centred Stochastic Volatility. arXiv2404.11057 v2 2025-10-02. https://arxiv.org/pdf/2404.11057 | full §1, AppendixA TheoremA.1 pp37–38. distinct variance sequences인 개별 row의 sign 제외 uniqueness 확인 | **기존 보고서가 누락한 가까운 선행.** 기존 보고서 제목은 v1 제목인 Partial Identification of Heteroskedastic Structural VARs Theory and Bayesian Inference였고 최신 v2 제목은 변경됨. 부분 구조와 conditional heteroskedasticity 자체는 ML 밖에 성숙한 문헌이 있음. |
| Cardoso. Joint Diagonalization (저자 페이지). https://www2.iap.fr/users/cardoso/jointdiag.html | 저자 원문 링크와 1994 Perturbation of Joint Diagonalizers technical report 실재 확인; report 본문은 아직 미확인 | 기존 perturbation 계열을 찾은 primary index. 본문 미확인인 결과를 theorem으로 인용하지 않음. |

## 최근 가까운 논문의 접근 한계

Yuke Li, Yujia Zheng, Ziyi Chen, Kun Zhang, Heng Huang. Towards Identifiable Representations under Misspecified Structure. arXiv2609.33273, 2026-09-27. https://arxiv.org/abs/2609.33273 . 제목·저자·초록 실재 확인. 이번 세션 PDF/HTML 요청은 DisabledError로 차단되어 **원문 정리를 재검증하지 못했다.** 이전 보고서는 observation conditional factorization perturbation이라고 썼지만 이번 문헌 감사에서는 그 상세 정리를 신규성 판정의 확정 근거로 쓰지 않는다. 이 차단은 본 주제의 elementary-Gaussian 결과가 이미 covariance sensitivity라는 판정을 바꾸지 않는다.

Cai and Li. Perturbation Analysis for Matrix Joint Block Diagonalization. arXiv1703.00591. https://arxiv.org/abs/1703.00591 . 검색과 초록·색인에서 실재 및 scope 확인, PDF fetch 실패. 기존에 block error bounds/condition numbers가 있음을 존재 확인하되 정확한 theorem domination을 주장하지 않는다.

## 정식화의 변경

기존 출발: 약한 환경 변화와 소스 의존성 아래 'factor/group/subspace 중 어디까지 식별되는가'.

이번 변경: linear-Gaussian family에서 invariant TC budget을 고정하고, 동일 law의 회전 모형집합을 exact 계산. δ>0에서는 exact block이 자동 유지되지 않으므로 방향별 **approximate identified set**를 목표로 한다.

새 결론: latent ambiguity가 학습 seed 분산보다 클 수 있다는 말은 맞지만 elementary observational equivalence의 결과다. 독립 논문의 핵심 주장을 위해서는 기존 covariance perturbation이 설명하지 않는 비선형/비Gaussian phenomenon 또는 sharp inference가 더 필요하다.

## 교차 검토 후 결정적인 직접 선행

Ablin, Cardoso, Gramfort. Beyond Pham's algorithm for joint diagonalization. arXiv1811.11433v1, 2018. https://arxiv.org/pdf/1811.11433v1 . **원문 직접 확인**: §1 Eq(1)은 Gaussian covariance의 평균 TC와 정확히 같은 cost, §2 Eq(3)는 relative Hessian 및 row-scale invariance, §3.1 Eq(4)–(5)는 exact diagonal point의 sparse Hessian이다. critic이 찾은 source를 담당자도 원문 재확인했다.

대응: 본 평균 TC sublevel set는 이 고전 cost의 sublevel이다. max_e TC<=delta는 각 cost sublevel들의 교집합이라 평균 objective와 동일한 보장이라고 쓸 수는 없다. 그러나 local sensitivity와 scale-equivalence를 '새 원리'로 내세울 근거는 없다. 현재 독립 주제 기각의 핵심 문헌 근거다.
