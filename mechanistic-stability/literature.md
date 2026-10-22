# 직접 선행연구 재검증

조사 기준일 2026-10-22. 제목·초록만으로 정리를 추정하지 않았다. 원문은 작업 공간에서 읽었고 저장소에는 복제하지 않는다. 아래의 수학적 비교는 이번 분석이며 외부 논문이 우리 반례를 이미 제시했다는 주장은 아니다.

## 신규성 판단에 결정적인 원문

### 1. Matthes, Han, Shen — Mechanistic Independence: A Principle for Identifiable Disentangled Representations

ICLR 2026. [공식 기록](https://proceedings.iclr.cc/paper_files/paper/2026/hash/b287c2f8630583f5fac5dcf4f544c7c9-Abstract-Conference.html), [직접 읽은 v2 원문](https://arxiv.org/html/2509.22196v2), 2026-05-10.

읽은 범위: §2–5, AppA.4–A.5, AppB Example2, AppD.1. Thm3 Type M에는 mutual non-inclusion뿐 아니라 sparsity inequality와 Eq6의 support-union/no-cancellation 조건이 있다. Thm4 Type S는 integer ℓ0 gap와 irreducibility로 same-manifold decoder의 block equivalence를 보장한다. 작은 dense C¹ 오지정을 다룬 정리는 아니다. §5/AppD.1은 overlap0/5/20/50%, 120 autoencoders의 compositional surrogate와 나쁜 local minima를 이미 조사했다. AppB는 특정 선형 모형의 surrogate 최적해도 분석한다.

남은 공백: 모든 approximate-TypeS candidate의 quantitative stability와 loss-near-optimum이 그 class를 보장하는지. 이번 반례는 exact theorem을 반박하지 않으며, strong row weighting으로 surrogate 순위가 틀리는 정확 예시다. overlap/high-local-minima 서사만으로는 신규성이 없다.

### 2. Buchholz, Schölkopf — Robustness of Nonlinear Representation Learning

ICML **2024**, PMLR235:4785–4821. [공식](https://proceedings.mlr.press/v235/buchholz24a.html), [직접 읽은 저자 HTML](https://arxiv.org/html/2503.15355v1). arXiv 등록2025와 출판연도2024를 구별한다.

읽은 범위: §3–5, Thm4.1, Assumptions5.2–5.4, Thm5.5/5.7/5.11, AppE/F. near-isometric generator를 최대한 isometric한 observationally equivalent choice로 바꾸는 rigidity 및 independent-source ICA의 작은 nonlinear perturbation을 분석한다. ICA contrast의 nonzero curvature 같은 conditioning이 필요하다. 모든 임의 동치 해가 좋은 것이 아니라 지정한 class/선택 규칙의 bound다.

우리 차이: latent density independence를 요구하지 않는 support-based factor target이며 arbitrary full mixing의 오류 bound가 아니다. 일반적인 '오지정/condition number도 중요하다'는 메시지는 이미 이 연구에 있다. 우리의 anchor proof가 이 정리의 문자 그대로 따름정리임은 확인하지 못했다.

### 3. Nelson, Fumero, Karaletsos, Locatello — Statistical and structural identifiability in representation learning

2026, [직접 읽은 v1](https://arxiv.org/html/2603.11970v1), 2026-03-12.

읽은 범위: §3 전체, AppA.3.2/A.3.5/A.3.6. decoder의 local bi-Lipschitz 제약과 rigid near-identifiability, ICA로 남은 선형 ambiguity를 줄이는 단계를 구분한다. structural 결과에는 생성기와 source distribution의 추가 전제가 있다. coordinate-wise factor recovery와 rotation-equivalent statistical stability는 같은 목표가 아니다.

우리 차이: dependent latent 아래 Type S 구조 의미를 목표로 하므로 단순히 위 near-identifiability 정의를 적용한 결과로 해결되지 않는다. 반대로 부드러운 representation robustness를 처음 제시한다는 구호도 불가능하다.

### 4. Garfinkle, Hillar — On the uniqueness and stability of dictionaries for sparse representation of noisy signals

IEEE Transactions on Signal Processing67(23), **2019**; [arXiv v4](https://arxiv.org/abs/1606.06997v4), [PDF](https://arxiv.org/pdf/1606.06997v4), 2019-05-14. 최초 preprint2016.

읽은 범위: §II Thm1/2, §III Eq(19), sparse-support hypergraph·restricted singular-value·subspace-angle constants. bounded noise 아래 sparse representations를 맞추는 대안 dictionary 전체를 다루고, coefficient diversity/strength가 bound의 상수에 들어간다. 따라서 '작은 구조 오차 대비 feature 강도', 'all-alternative stability', '정보량 있는 anchor'라는 일반 원리는 새롭지 않다.

정확한 차이: 이번 Jacobian rows에는 mixed rows가 dense할 수 있고, nonlinear decoder의 pointwise bases가 integrable transition h를 이루어야 한다. 원문 정리를 그대로 대입해 우리 positive bound 전체를 얻는 환원은 확인하지 못했다. 현 proof가 elementary sparse-basis counting·chain rule·connectedness라는 사실과, 문자 그대로 기존 정리의 따름정리라는 주장은 구분한다.

### 5. Li, Zheng, Chen, Zhang, Huang — Towards Identifiable Representations under Misspecified Structure

2026-09-27 preprint, [원문](https://arxiv.org/html/2609.33273v1), [서지](https://arxiv.org/abs/2609.33273).

web fetch는 차단되었으나 curl로933,340-byte HTML 원문을 확보했다. §2–3, AppendixB.3 및 component assumptions를 직접 읽었다. 세 observation blocks의 conditional factorization 오지정을 integral-operator spectral perturbation으로 분석한다. Thm2는 conditional-distribution map Θ의 inverse-Lipschitz 조건으로 latent whole-subspace의 approximate error를 제어한다. Prop2의 exact component recovery는 latent independence·structural sparsity·learned ℓ0 budget을 추가한다. §3.3은 approximate component-wise 확장을 미해결로 남긴다.

따라서 제목만 보고 우리의 dependent-latent deterministic TypeS C¹ 문제를 이미 해결했다고 판단하면 틀리다. 반대로 이 차이만으로 우리의 새로운 기여가 생기는 것도 아니다. 원문의 bounded-below conditional operator, matched spectrum, inverse-Θ assumptions가 없으면 그 bound를 옮길 수 없다.

## 직접 읽은 원문 파일의 감사 정보

HTML/PDF는 임시 작업공간에만 있으며 repository에는 올리지 않았다. SHA256는 확보한 버전을 추적하기 위한 기록이다. HTML의 동적 생성 차이는 생길 수 있다.

| 원문 | SHA256 |
|---|---|
| MI v2 HTML | `8ec9193b3130d012ac37df82a974c8a2c6b565886f98a58fb087663401af0ba0` |
| Buchholz HTML | `148fa84f323bfc5a03470245de1dc79e963518d9851a9343a8e012021bf46b53` |
| Nelson v1 HTML | `0932c25106c91231a771e7d24b3cfa61ee30f647b000dca6c39ffad34900957f` |
| Li v1 HTML | `36372d6081ee6046ca24d8c3daab6f758346cff292ae450ba1df5ac440d748e1` |
| Garfinkle–Hillar v4 PDF | `410bb1f76d6c335dd57a52285ca8de7ca59e33f581f6e31214e6fe9ea1e55d70` |

## 조사 한계와 남긴 불확실성

이번 실제 검증은 후보2의 mechanistic sparsity 경로를 택했다. 원보고서에서 합쳐졌던 rare-support/noise acquisition의 다른 경로를 이 결과로 해결·기각했다고 말하지 않는다. 그 경로의 Functional Orthogonality·finite-sample papers를 이번 결론의 결정적 근거로 인용하지 않았다. 최신 검색은2026-10-22까지의 mechanistic/approximate/structural sparsity 관련 원문을 우선했으며, 모든 분야의 exhaustive absence proof가 아니다. 새로운 anchor theorem과 정확히 동일한 선행 정리를 찾지 못했다는 사실을 신규성의 증명으로 세지 않는다.
