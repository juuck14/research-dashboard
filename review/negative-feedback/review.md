# Negative 피드백 독립 검토

검토일 2026-10-22. 검토자는 주제 제안 담당과 독립적으로 식·전체 tangent 공간·코드를 확인했다. owner 디렉터리를 수정하지 않았고 이 디렉터리의 코드는 owner 코드를 import하지 않는다.

## 판정

**원래의 가장 단순한 기제는 기각하지만, 수정된 질문은 실질적 결과를 확보했다.** Unnormalized identity-positive 모형에서는 full support가 있으면 누락 요인은 transverse repelling이다. Normalized 모형에서 누락 요인 상태의 local 안정성만 관측해도 피드백의 고유 효과라고 할 수 없다. 그러나 **두 요인을 모두 보존한 square 표현의 local 안정성이, 같은 basepoint의 negative 분포를 고정했을 때와 갱신했을 때 반대**가 되는 결과는 독립 검산을 통과했다. d=3/4 전체 lookup sphere에서도 성립하며 K2/K4와 동일상태 negative 제거에도 유지됐다.

최종 논문 기여의 신규성은 이 exact 결과만으로 확정되지 않는다. Performative prediction의 일반적 불안정성을 contrastive loss에 대입한 예 이상으로, 실제 sampler 및 stochastic encoder 학습에 적용되는 예측 법칙인지가 남아 있다. 다만 이번 결과는 '수정 후 진행'을 논의할 실질적 근거이며, 최초 주제의 말뿐인 가능성 평가보다 강하다.

## 1 Unnormalized 결과의 검토와 용어 수정

X=(a,b), 독립 균등 binary factors, f=(u a,t b), positive=X, one-negative loss ell=log(1+exp(s_neg-s_pos)). t=0에서 negative q를 고정하면

`d ell / d(t²) = sigmoid(u²(aa'-1)) (bb'-1) <= 0`.

b'=-b인 negative의 확률이 양수면 평균값은 엄격히 음수다. q가 현재 score의 smooth function이어도 score는 t의 짝함수이므로 q(t)-q(0)=O(t²), transverse vector field의 1차계수는 q(0)을 고정한 것과 같다. epsilon/4 floor를 두면 owner의 missing-mode growth lower bound epsilon/2와 독립 계산이 일치했다.

**중요한 수정:** (u,0)은 u 방향 gradient가 일반적으로 0이 아니므로 유한 stationary saddle point라고 부르면 부정확하다. 정확히는 t=0이 invariant boundary이고 그에 수직인 작은 nonzero t가 자라나는 **transverse repelling**이다. 이 반증은 이 모형의 영구 실명 기제를 부정하며 모든 adaptive sampling을 부정하지 않는다.

재현: `code/stress_check.py`, `results/unnormalized_jacobian.csv`. 15조건에서 epsilon/2 하한 확인.

## 2 Normalized 누락 상태: full support만으로 회복을 보장하지 않음

f_t(a,b)=(a,t b)/sqrt(1+t²)에서는 positive score=1이고, score의 t² 계수는 bb'-aa'다. q_same은 같은 a·반대 b인 negative 하나의 확률, q_opp는 반대 a·같은 b의 확률이라 두면

`L(t;q0)=L(0;q0)+D t²+O(t⁴)`,

`D=-q_same+2 q_opp sigmoid(-2)`.

easy filtering이 충분히 강하면 D>0이라 누락 상태가 안정하다. 이 현상은 d=2가 두 요인을 표현할 수 있어도 unit-norm budget에서 static weighted objective가 한 구분을 더 선호할 수 있음을 뜻한다.

그러나 이 상태에서는 모든 score의 tangent 1차 변화가 0이므로 adaptive q의 local Jacobian은 frozen q0와 같다. 전 범위 tangent eigenvalue를 계산하지 않고 diagonal t 한 방향만으로 local minimum을 주장하지 않았다. 4-state S1 전체 tangent에서 15조건 중 4조건이 회전 제외 strict minimum이고, adaptive/frozen Jacobian 최대차는 2.73e-11이다. 확인 seed를 포함한 24회 flow도 이 일치를 확인했다.

**해석:** full support+표현 차원 충분이라는 두 조건만으로 모든 요인 회복이 보장되지는 않지만, 이 terminal omission의 존재 자체는 피드백 고유 발견이 아니다.

## 3 새 결과의 전체 tangent 분석

기준점 F0(a,b)=(a,b,0,...)/sqrt2를 네 개의 독립 unit vectors로 둔다. additive 두 parameter에 제한하지 않는다. 각 negative는

`q_F(j|i)=epsilon/4+(1-epsilon) exp(kappa s_ij)/sum_l exp(kappa s_il)`.

고정 정책은 q*=q(F0), 갱신 정책은 각 step q(F)를 사용하되 sampler 미분은 학습 gradient에서 detach한다. positive는 identity이며 temperature=1이다. 양쪽 vector field는 F0에서 정확히 0이다.

### 정확한 K1 고유값

`c=1-epsilon`, `Z=2+2 cosh(kappa)`, `t=1/Z`,

`v=epsilon/4+c/Z` (square adjacent negative 하나의 확률),

`w=epsilon/4+c exp(-kappa)/Z` (opposite negative 확률),

`r=sigmoid(-1)`, `r'=r(1-r)`, `s=sigmoid(-2)`.

아래는 loss-gradient Jacobian의 고유값이다. Gradient-flow 안정성은 부호를 반대로 읽는다.

| tangent mode | frozen q* | adaptive detached q |
|---|---|---|
| in-plane factor-balance mode ab | 2 v r' | 2[v r'+c kappa t r] |
| in-plane modes a,b | v r'+w s (각 1개) | v r'+w s+c kappa t r(1-t) (각 1개) |
| in-plane global rotation | 0 | 0 |
| 각 out-of-plane coordinate의 constant mode | v r+w s | 동일 |
| 각 out-of-plane coordinate의 ab mode | w s-v r | 동일 |
| 각 out-of-plane coordinate의 a,b modes | 0,0 (전역회전) | 동일 |

이는 4(d-1)개의 모든 tangent 자유도를 소진한다. Square의 회전 orbit 차원은 2d-3이며 나머지 2d-1개 mode의 부호를 모두 통제한다. 따라서 d>=3에서 frozen q*가 회전 제외 strict local minimum일 필요충분조건은 `w s>v r`다. Adaptive factor-balance 불안정성은 `v r'+c kappa t r<0`일 때 생긴다. 이것은 기존의 generic Jacobian 항을 보여주는 것보다 구체적인 이 모형의 phase condition이지만, 별도의 novelty 주장과 구분한다.

### 유도

In-plane 각도 perturbation h_i에 대해 s_ij=cos(phi_i-phi_j)다. 고정 q의 loss Hessian은 adjacent pair의 `v r'` graph Laplacian과 opposite pair의 `w s` matching Laplacian 합으로 분해된다. 네 characters {1,a,b,ab}가 동시에 대각화한다.

Adaptive correction은 `sum_ij (Dq_ij) (D ell_ij)`다. Square에서 adjacent pair만 score의 1차 변화를 갖는다. q의 row normalization 미분까지 포함하면 ab mode에 `2 c kappa t r`, a/b mode에 `c kappa t r(1-t)`가 추가된다. Out-of-plane perturbation은 모든 score의 1차 변화가 0이므로 correction이 없다.

Out-of-plane scalar perturbation h_i는 retraction으로 unit norm을 유지한다. Pair score의 t² 계수는 `h_i h_j - s_ij(h_i²+h_j²)/2`이며 이 quadratic form을 같은 characters로 대각화하면 표의 마지막 세 행을 얻는다. 이로써 additive family 밖의 탈출 방향도 검사한다.

### 독립 수치 검산

epsilon=.1, kappa=-2에서 d2/d3/d4 모두 frozen stable, adaptive 정확히 한 unstable mode다. d4의 growth eigenvalues는 frozen 비회전 최대 -0.04698798, adaptive 최대 +0.05466566이다. q 최소는 .0377884로 양수다. 전체 tangent finite-difference step을 1e-5에서3e-6으로 바꾼 최대 오차는5.60e-12, 독립 loss-gradient directional check 오차는5.84e-12다.

d3/d4, 확인 seed109/239, noise1e-4/1e-6, 같은 초기조건의16회 flow에서 Procrustes 정렬 후 square 거리는 frozen 모두 감소, adaptive 모두 증가했다. Unit-norm drift 최대1.21e-12. 이는 local instability 확인이며 global collapse 도착의 증명이 아니다.

재현: `code/full_sphere_center.py`, `results/square_summary.json`, `results/square_full_flow.csv`.

## 4 One-negative와 동일상태 negative 대안 설명

K iid negatives의 InfoNCE를 네 상태 multinomial counts로 정확 평균했다. K2/K4에서는 ordered sequences도 전부 열거해 loss와 score-gradient 기대값을 독립 대조했으며 최대차4.16e-16이다. d4 전체 tangent에서 frozen stable/adaptive unstable 부호가 K2/K4에도 유지된다. 최대 adaptive growth는 K2 .09118284, K4 .13528304다. `code/multinegative_check.py`와 `results/multinegative_summary.json` 참조.

Anchor와 동일한 상태를 negative 후보에서 아예 제외한 q over3에서도 동일 현상이 유지됐다. d4,K1,eps=.1,kappa=-2에서 frozen 최대 비회전 growth=-.05080044, adaptive +.05231846, min candidate probability=.1291896. 따라서 네 상태 중 같은 latent state의 negative collision만으로 결과를 설명할 수 없다. `code/no_self_check.py`, `results/no_self_summary.json` 참조.

이 추가 확인들은 사후 발견을 숨기지 않기 위해 각각 center-protocol.md, multinegative-protocol.md, no-self-protocol.md에 실행 전에 따로 기록했다. 최초 corner 규약을 덮지 않았다.

## 5 강한 선행과 실제 차이

**Jiang et al., TMLR2025, Hard-Negative Sampling for Contrastive Learning: Optimal Representation Geometry and Neural- vs Dimensional-Collapse.** 원문 https://arxiv.org/pdf/2311.05139 의 §3.2, Theorem1–3 및 §5를 확인했다. Hardening은 nonnegative, coordinatewise nondecreasing이고 주로 bounded representations의 global geometry와 경험적 최적화를 다룬다. 이번 kappa<0 easy filtering과 detached policy-response local Jacobian은 그 정리의 직접 대상으로 확인되지 않았다. 따라서 '그 논문이 있으니 동일'이라는 기각은 부당하지만 negative sampling과 collapse의 일반적 연결을 처음 주장할 수도 없다.

**Meng et al., ICLR2026, SnaPhArd Contrast Learning.** 공식 원문 https://proceedings.iclr.cc/paper_files/paper/2026/file/42a24a7a3e7cf7dd127a76daf487cffd-Paper-Conference.pdf §2.2와 Theorem2.1을 확인했다. Easy negatives의 fixation이라는 설명이 가깝다. 그러나 이 논문의 해당 'collapse'는 고정 key vectors를 둔 한 anchor x가 positive p와 일치하는 상황이다. 네 표현을 모두 갱신하는 factor-loss나 adaptive sampler Jacobian과 혼동하면 안 된다. 이 논문을 읽지 않고 'easy negatives가 representation을 가둘 수 있다'는 서사를 novelty로 내세우는 것은 피해야 한다.

MCL2024, feature suppression2023, performative prediction2020과의 더 넓은 대조는 owner 및 별도 novelty 감사에서 수행한다. 이 독립 검토는 두 fulltext 결과를 직접 환원 근거로 과장하지 않았다.

## 6 남은 반론과 권고

1. **Generic performative mechanism:** 분포가 parameter에 반응하면 frozen stable/adaptive unstable은 일반적으로 가능하다. 이 generic fact는 새 결과가 아니다. Exact contrastive phase boundary와 실제 sampler에서의 예측이 논문의 중심이어야 한다.
2. **정책 대표성:** exp(kappa cosine), kappa<0는 similarity filtering의 stylized family다. 실제 quantile false-negative detection, hard filtering, annealing과 동일하지 않다. 현실 정책에서 kernel derivative의 같은 부호가 발생하는지 필요하다.
3. **정보 주장:** 유한시간에 네 vectors가 모두 다르면 binary factor 정보는 noiseless oracle decoder로 남을 수 있다. Local anisotropy·readout conditioning·asymptotic rank loss를 구분한다. Finite-time MI=0은 이번 결과가 지지하지 않는다.
4. **확률적 최적화:** Population Riemannian flow는 finite-batch SGD/learned encoder가 아니다. 사전 예측한 instability eigenmode가 작은 stochastic 모델에서 나타나는지 확인해야 한다.
5. **비특이성:** strict eigenvalue margins가 있으므로 finite-support law와 score의 충분히 작은 smooth perturbation에서는 부호가 연속적으로 유지된다. 그러나 이것만으로 noisy natural images의 일반화를 주장할 수 없다.

**독립 권고:** 원래 설명은 수정하되, 'full-support adaptive filtering이 충분한 표현을 불안정하게 만드는 contrastive-specific 경계'로 좁혀 추가 진행할 가치가 있다. 이번 분석은 그 핵심 현상이 실제 존재한다는 근거를 제공한다. 다만 자연스러운 정책/확률적 학습과 기존 performative theory를 넘는 기여가 핵심 남은 과제이므로, 완성 논문의 신규성과 중요성까지 승인한 것은 아니다.

## 후속 확장 감사

Root가 추가 실행한 nonidentity full-rank positive-channel population 검산과30회 finite-minibatch normalized SGD를 별도로 감사했다. [감사 문서](../robustness-extension/independent-review.md), [432개 gradient 검산 결과](../robustness-extension/results/independent_audit.json) 참조. Exactfield와 독립 scalar FD의 최대차1.24e-10, SGD 기대 gradient 차이5.20e-17로 구현상 반론은 발견하지 못했다. Noisy-feature Bayes readout도 정확하다. 이 추가 근거는 pure identity/population/linear-probe 대안 설명을 완화하지만 image-encoder 일반화나 noiseless information loss를 입증하지 않는다.
