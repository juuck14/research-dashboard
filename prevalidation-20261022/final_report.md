# 후보 1·2·3 실제 사전 검증: 최종 착수 판단

기준일 2026-10-22. **후보1은 현재 구체화 기각, 후보2는 판정 보류, 후보3은 현재 구체화 기각이다. 이번 검증에서 바로 수개월 연구를 권하는 후보는 없다.** 세 분야 전체가 해결됐거나 불가능하다는 판단은 아니다. 이전 보고서의 추천보다 이번 직접 증거를 우선한다.

## 비교 판단

| 대상 | 최종 판정 | 확보한 가장 강한 증거 | 아직 남은 위험 | 직접 착수한다면 첫 작업 |
|---|---|---|---|---|
| 1 SSL 특징 회복 지연 | **현재 구체화 기각** | nonlinear exact-population 학습·상태 개입·장기 continuation; rank 결손 agreement optimum 증명; 독립 gradient 감사 | 넓은 nonlinear 회복의 원인은 미해결. 이번 지연이 새 상태 원리를 요구한다는 증거가 없음 | clean objective가 목표 factor를 엄격히 선호하면서 기존 conditioning 설명이 같은데 회복이 다른 최소 사례부터 확보 |
| 2 근사 메커니즘 식별 안정성 | **판정 보류** | same-law 45° 반례, fixed-base support-creation 반례, all-candidate 제한 안정성의 완전 증명, 실제 surrogate의 잘못된 선호 반례 | 일반 Type S의 quantitative margin과 학습된 해의 admissibility, 독립 논문 신규성이 미확보 | 제한 정리의 기존 sparse-basis 결과 환원 여부를 확인하고 candidate complexity를 통제한 비선형 경계를 증명 |
| 3 확률적 SSL의 식별 가능한 예측 | **현재 구체화 기각** | categorical sharp set·실제 표본·예산 대조, circle joint identification 증명, KL t⁴/t⁶와 독립 FFT 감사 | 지금 결과는 고전 factorization·singular inference·replicate 원리와 가까움. 실제 heteroscedastic SSL 목적함수의 공백은 미해결 | PCL과 고전 직접 선행을 대조한 뒤, 실제 near-optimal objective가 허용하는 새로운 observable prediction law가 있을 때만 재개 |

판정의 강도도 구분한다. 제한 모형의 수학·수치 결과는 서로 다른 코드와 증명 검토를 거쳐 신뢰가 높다. 그 결과가 **독립 논문의 새 기여가 되는지**는 별도 문제다. 같은 정리를 이미 출판한 논문을 못 찾았다는 사실을 신규성의 증거로 쓰지 않았다.

## 대상·작업 범위

입력은 `research_directions_20261022.pdf`의 번호1·2·3이다. 저장소 기존 `partial-identification`, `negative-feedback`, `target-correction`의 세 주제와 다르다. 기존 README·coordination 지침을 읽고 이번 기록을 별도 디렉터리에 추가했다. 기존 Gaussian/AJD와 선형 EMA 결과는 실제 파일을 읽어 경쟁 설명으로 활용했으며 새 기여로 재계산하지 않았다.

세 독립 담당과 세 별도 비판 검토자가 실제로 작업했다. Root는 원자료와의 범위 대조, circle pair-law의 별도 증명·계산·표본 검정, 종합판정과 출판을 맡았다. 각 protocol은 해당 실행 전에 썼으며, 가설 변경·추가 실험·해석 정정은 amendment/progress로 남겼다. [역할 및 증거 목록](evidence.md), [재현 안내](reproduction.md), [진행 이력](progress.md).

이번 검증에는 소규모 nonlinear neural 학습, 정확한 모집단 계산, 이론 증명과 수치 검산이 포함된다. 자연 이미지 실험이나 neural MCInfoNCE calibration을 수행했다고 주장하지 않는다. 비용 때문에 좋은 주제를 배제한 것이 아니라, 현재 판정을 바꾸지 못할 benchmark 확장을 하지 않았다.

## 1. 회복 지연: 현상은 있었지만 새 원인은 확보하지 못했다

### 질문과 설계

관측 X는 uniform 3 bits, 두 view의 각 bit correlation은 rho_j다. Raw marginal과 모델 용량을 유지하고 cross-view relation만 deficit→clean으로 바꿨다. Bias-free tanh encoder 3→12→3, normalized cosine self-distillation, linear predictor, EMA teacher, Adam을 사용했다. BN·LR schedule·유한 training sample은 설계상 제거했다. 평가 factor label은 loss에 사용하지 않았다.

Checkpoint를 복제해 encoder/head/teacher/optimizer state의 개입을 비교하고, 일부 개입에는 block별 실제 update norm을 맞춘 대조를 넣었다. 4개 pilot+4개 confirmation 초기값을 사용했다. 여기서 seed는 dataset 반복이 아니라 initialization이다. 고정 readout noise 아래 population 최적 linear R²를 측정했으며, 작은 값은 noiseless 정보 부재를 의미하지 않는다.

### 직접 결과와 반론

3000 clean update 뒤 suppressed factor의 R²는 8개 초기값 모두 낮았고 최대 .00424였다. 하지만 같은 원 설정을 15000 update까지 연장하면 **4/8이 R²>.9로 회복**했다. 이는 긴 지연의 증거이며 영구 불가능성의 증거가 아니다. 원 보고서가 처음부터 영구 고착을 확정했던 것도 아니다.

더 결정적인 문제는 clean objective의 선택압이었다. Equal rho에서 Walsh conditional-expectation operator의 singleton eigenvalue는 모두 rho다. Odd unit map q,f에 대해

$$L=2-2E[q(X)^Tf(Y)]\ge 2-2\rho.$$

임의 unit v의 `f_v(x)=diag(v)x`, q=f_v가 하한을 달성한다. v의 일부 성분이0이어도 성립하므로 **rank1·2·3 표현이 같은 전역 최적값**을 갖는다. 복구를 요구하지 않는 objective 아래 reset 실패를 별도의 memory lock으로 해석할 근거가 부족하다. 이 증명은 실제 MLP의 모든 trajectory를 완전히 설명하는 정리가 아니다.

같은 관측법칙의 제한 diagonal contrastive family에는

$$L_{NCE}(w)=-\sum_j\rho_jw_j/\tau+\sum_j\log\cosh(w_j/\tau),\quad w_j\ge0,\ \sum_jw_j=1$$

라는 엄격 볼록 목적함수가 있다. Equal rho의 유일 allocation은 w_j=1/3이다. 실제 nonlinear InfoNCE 대조도 8개 초기값 모두 50–250 clean update에 회복했다. **Teacher·head·loss가 함께 달라지는 대조이므로 teacher 하나의 인과 효과라고 주장하지 않는다.**

Reset의 부분 효과도 보존했다. 한 초기값에서 predictor/head 개입이 .72–.74까지 회복시켰지만 predictor의 Adam moments까지 reset하면 .049였다. 다른 correlation에서는 제한 tangent 모형의 예측을 벗어나는 neural recovery와 다른 factor의 손실도 나왔다. 일관된 새 상태량이나 조건 외 회복시간 예측을 확보하지 못했다.

### 신규성·판정

CP2026는 이미 deficit 후 continuation과 fixed-vs-cosine LR를 조사했다. Tian2021은 full-matrix linear encoder/predictor/EMA를, Wen–Li2022는 nonlinear prediction head의 weak-feature 학습을 다룬다. 최근 plasticity 연구도 norm·optimizer 상태와 별개인 weak subspace/gradient 조건을 분석한다. 이들이 이번 tanh/Adam 전체를 정확히 해결한다는 주장은 하지 않는다. 다만 현재 직접 계산은 기본 spectral 선택과 작은 mode의 시간척도를 넘지 못한다.

**현재 구체화는 기각한다.** 더 많은 reset·backbone을 다음 단계로 권하지 않는다. 엄격한 factor 복구 선호, random initial retention 및 기존 conditioning을 맞춘 상태에서 새로운 회복 예측이 가능한 최소 사례가 재개 조건이다. [증명](../ssl-recovery/theory.md), [전체 결과](../ssl-recovery/results.md), [판정](../ssl-recovery/verdict.md), [독립 검토](reviews/recovery/review.md).

## 2. 식별 안정성: 명확한 경계와 제한 정리는 얻었지만 핵심 연결은 남았다

### 무엇을 식별하는가

Fixed observation coordinates에서 dependent latent도 허용하고, factor별 일변수 재매개화·순서는 같은 해로 본다. 일반 rotation으로 두 factor를 섞는 것은 다른 해다. True Jacobian graph를 알고 clustering하는 문제로 바꾸지 않고 **같은 관측을 설명하는 모든 허용 decoder**의 transition h를 대상으로 삼았다. 관측 geometry와 chart 단위를 고정했다.

Mechanistic Independence의 Type S는 exact sparsity gap로 factor를 식별하지만 gap은 정수이고 작은 nonzero의 진폭을 통제하지 않는다. 이번에는 이 조건을 C¹ leakage로 완화할 때 무엇이 필요한지 분석했다. 원 보고서의 rare-support/noise 경로까지 해결한 것은 아니다.

### 반례: 참인 exact theorem이 안정성 theorem을 자동 주지 않는다

첫 구성은 잘 조건화된 6×2 Jacobian에 강한 축·대각 방향과 κ 크기의 weak anchor를 둔다. κ>0마다 exact Type S gap1을 유지하지만, 45° 회전된 같은-law decoder가 다른 exact-TypeS reference의 `κ√(2−√2)` 근방에 있다. κ→0에도 factor 의미의 차이는45°다. Primary7+confirmation40조건과 독립 구현에서 재구성 residual 최대4.44e−16을 확인했다. 이는 **family-uniform 안정성 실패**이며 고정 g0 하나의 pointwise 안정성을 이 예만으로 반박하지 않았다.

이후 true generator를 고정한 더 강한 예를 만들었다. True generator에4개 constant observation coordinates를 두고, 회전된 actual decoder 자체도 고정했다. Candidate reference에 ε 크기의 새 support를 넣으면 exact TypeS를 만들 수 있고 거리는√2ε→0이다. True witness 강도와 conditioning은 고정인데도 다른 factor 설명이 남는다. **Constant coordinates와 candidate-side support/complexity 증가를 허용한 범위**다. Common known reference에 모든 decoder를 제한한 문제의 반례는 아니다.

### 긍정 결과: 모든 동치 nonlinear decoder를 통제하는 제한 정리

두 scalar factor, m=2p+q rows, 각 축에 p개 pure anchors, q개 overlap rows, p>q를 둔다. 모든 true reference row norm≥a, learned reference sparsity≤m+q, true/learned C¹ leakage≤δ, `||Dh||≤L`을 가정한다. η=δ(1+L)<a/√2이면 하나의 global permutation에서

$$\|Dh_{off}\|_{max}\le L\eta/a.$$

Rectangle에서는 선분 적분으로 좌표별 C⁰ block approximation≤rLη/a를 얻는다. 이는 임의의 허용 candidate에 대한 직접 증명이다. Chain rule `A−CB`의 row residual≤η, support counting, 두 축에 동시에 가까울 수 없는 normalized row, connectedness를 순서대로 사용했다. **Global C¹ block approximation까지 증명한 것은 아니다.**

독립 검토자는 800개의 B에 대해 각 B의 모든 C support를 계산했고 전제를 만족한473조건에서 위반을 발견하지 않았다. 증명의 근거는 유한 탐색이 아니라 위 논증이다. Mixed-row amplitude floor를 삭제하면 실패하는 별도 반례도 찾았다. 이 강한 가정들은 원래 일반 Type S에 자동으로 주어지지 않는다.

### 실제 surrogate와의 간극

강한 anchor가 있고 overlap도40%인 8×2 예에서 true Jacobian Gram과 회전된 Gram은 모두7I다. 완전 재구성·차원·norm을 맞추어도 compositional contrast는 true axes의4보다45° 회전의3을 선호한다. True ℓ0=10, 비정렬 최소12이며 그45° 후보는ℓ0=14다. 그러므로 **낮은 surrogate loss가 위 정리의 learned sparsity budget를 보장한다는 연결은 거짓**이다. Optimizer failure가 아니라 objective preference다.

MI 원문이 이런 일반 surrogate 보장을 주장한 것은 아니므로 원 논문 정리의 반증이라고 쓰지 않는다. Weighted smooth relaxation과 cardinality 기준이 다를 수 있다는 현상도 그 자체로 새 일반 원리는 아니다.

### 신규성·판정

새 제한 정리를 기존 Garfinkle–Hillar dictionary theorem에 문자 그대로 대입해 얻었다는 환원은 확인하지 못했다. 반대로 counting·chain rule·연속성·적분의 결합만으로 독립 논문 신규성이 확보됐다고도 판단하지 않는다. Buchholz–Schölkopf2024, Nelson2026, Li2026의 robustness 결과는 다른 모형·목표·가정을 갖는다. 차이가 있다는 사실만으로 공백을 해결한 것은 아니다.

**원래 후보2는 판정 보류다.** 계산 자원·권한이 아니라 일반 quantitative margin과 admissible learned class의 연결, 그 학술적 신규성이 병목이다. 이미 얻은 수학 노트는 실질적이지만 핵심 일이 아직 남아 있으므로 “추가 실험만 하면 되는 논문”으로 부르지 않는다. [연결된 연구 노트](../mechanistic-stability/research_note.md), [제한 정리](../mechanistic-stability/positive_bound.md), [반례](../mechanistic-stability/theory.md), [판정](../mechanistic-stability/verdict.md), [독립 검토](reviews/mechanism/review.md).

## 3. 불확실성: 가능성은 확인했지만 현재 확장은 고전 inverse problem과 가깝다

### 원자료의 가설을 바꾸어 반박하지 않았다

원 보고서는 observation ambiguity와 unknown correspondence를 함께 허용하면 **pair fit이 같아도 추가 acquisition의 예측이 달라질 수 있다**는 존재적 가설을 제안했다. 이번 categorical 결과는 이를 지지한다. Circle의 식별 성공은 조사 중 추가한 더 강한 해석, 즉 “unknown scalar positive parameter만으로 반드시 비식별”을 반박한다. 원 가설의 반박으로 잘못 부른 초기 문구를 원자료와 대조해 정정·기록했다.

### 정확한 ambiguity와 예측 범위

Uniform 3-state latent, `Q_a=J/3+a(I−J/3)`, `K_b=J/3+b(I−J/3)`, a,b∈[0,1]이면 pair 법칙은 c=a²b만 정한다. 같은 law의 모든 parameter는 `√c≤a≤1,b=c/a²`다. Anchor latent에서 독립 repeat R을 받을 때 `X1=X2=i` context의 확률은

$$P(R=i\mid X_1=X_2=i)=\frac{1+2a^2+4c+2ac}{3(1+2c)}.$$

따라서 c=.16의 sharp interval은 `[29/55,1]`이다. 구간은 grid 탐색이 아니라 모든 feasible parameter에 대한 증명으로 얻었다. Population infinite-negative pair-score의 optimum도 같은 ridge를 가지므로 이 사례는 optimizer나 encoder capacity 문제가 아니다. Original neural MCInfoNCE와 같은 알고리즘을 실행한 것은 아니다.

404 population 조건, 60 pair datasets·180 predictive evaluations, 700 oracle inverse fits, 60 추가 acquisition datasets를 실행했다. n=100000에서도 pair fit이 같은 잘못된 ridge 선택의 repeat Brier regret는 약.158로 남았다. Privileged known-b oracle와의 차이는 정보 가정 차이이며 동등한 방법 경쟁으로 해석하지 않는다.

총 acquisition 수3n을 맞춘 대조에서 genuine repeat는 a²라는 새 moment를 제공했지만 positive pair 추가는 c 추정만 개선했다. 독립 검토자는 별도 inverse-CDF 구현·새12datasets에서도 이를 확인했다. Copy는 비용0의 가정위반 진단이며 같은 예산의 competing acquisition으로 세지 않았다.

### vMF에서는 정확 식별과 operational instability가 양립한다

Known mean geometry·homoscedastic circle family의 pair Fourier sequence는

$$B_m(a,b)=[I_m(a)/I_0(a)]^2[I_m(b)/I_0(b)]$$

다. 양의 finite a,b에서는 Bessel large-order expansion으로 전체 sequence가 ordered pair(a,b)를 유일하게 정함을 직접 증명했다. 이는 arbitrary learned mean·heteroscedastic encoder의 결과가 아니다. 유한 harmonic에 수치적으로 맞는다는 사실도 full-law 비식별의 반례가 아니다.

그런데 a=b=c에서 모든 score derivative가2:1로 비례한다. `a=c+t,b=c−2t` 경로는1차 변화가 사라지고, 직접 증명으로 모든 c>0에 대해

$$KL(p_t\|p_0)\asymp t^4,\qquad KL(p_t\|p_{-t})\asymp t^6$$

를 얻었다. Root가 15 population 조건, 사전 예산 안의48 truth datasets(1,571,928 pairs)에서 oracle LRT를 실행했다. 독립 FFT 구현의 KL 상대오차는 최대3.36e−10이었다. c=2,t=.08에서는 부호 대조의 pair KL≈1.7147e−8이라 n=10000에서도 equal-prior oracle 오류는 Pinsker로 최소 약.4954다. 이는 두 점 판별문제이지 일반 MLE의 minimax rate를 증명한 것은 아니다.

### 신규성·판정

PCL2023의 known-kernel vMF theorem을 categorical 반례로 반박하지 않았다. Pair/triple moment와 latent-class 식별에는 Allman2009·Anandkumar2014가 직접 선행이다. Independent repeat의 Fourier cancellation은 Delaigle2008과 같고, magnitude/sign의 다른 higher-order scale은 Rotnitzky2000에 이미 있다. 정확히 같은 circle-vMF 정리를 선행에서 발견했다고 단정하지 않지만, 이번 제한 계산만으로 원래 표현 학습 문제의 새 기여를 충분히 확보하지 못했다.

**현재 구체화는 기각한다.** 실제 지정된 SSL objective의 near-optimal set에서 새 observable-prediction 법칙, 또는 learned-mean/heteroscedastic family의 비자명한 acquisition upper/lower bounds가 재개 조건이다. 새 uncertainty head부터 만들 이유는 현재 없다. [직접 증명](../pair-uncertainty/theory.md), [전체 결과](../pair-uncertainty/results.md), [판정](../pair-uncertainty/verdict.md), [Root 분석](operational-uncertainty/analysis.md), [독립 검토](reviews/uncertainty/review.md).

## 교차 검토에서 실제로 달라진 것

| 최초 해석·공격 | 확인 뒤 정정 |
|---|---|
| equal-rho의 회복 실패를 상태 고착 후보로 해석 | flat agreement optimum을 증명; 장기4/8 회복과 objective 선택압을 우선 대안으로 채택 |
| 제한 scalar와 sphere flow에 같은 global 식 사용 | metric이 달라 정의·시간법칙을 분리, 독립 검토자가 정정 확인 |
| scalar positive kernel 미지를 원래의 보편 비식별 주장으로 귀속 | 원 보고서는 존재적 가설임을 확인; 강화한 탐색 가설만 반박된 것으로 정정 |
| perfect-observation 대안의 log regret를 floor로 유한 표시 | exact∞와 clipped diagnostic을 분리; 초기 파일 보존 후 재실행 |
| positive theorem에 inverse lower bound가 꼭 필요하다는 공격 | 실제 chain relation A−CB를 읽은 뒤 철회; all-row floor와 sparsity budget은 핵심 전제로 유지 |
| near-TypeS 실패가 family-uniform에만 해당 | 이후 constant coordinates·candidate support creation을 허용한 fixed-base 반례를 별도로 확보 |

최종 판정에 남은 검토자 간 반대 의견은 없다. 다만 후보2의 제한 정리가 독립 기여가 될지와 세 넓은 연구 질문의 해답은 여전히 미해결이다. 해소되지 않은 연구 문제를 검토자 합의로 해결했다고 부르지 않는다.

## 지금 선택할 다음 행동

수개월 착수라는 기준에서는 **1·3은 현재 구체화를 종료하고, 2만 제한된 이론 확인 대상으로 남기는 것**을 권한다. 후보2도 진행 권고가 아니다. 먼저 새 regularizer를 만들거나 자연 이미지 benchmark를 돌리는 대신 다음을 판별해야 한다.

1. 제한 anchor theorem을 기존 robust sparse-basis/analysis-dictionary 결과의 가정·상수·target에 정확히 대입했을 때 새로 남는 수학이 있는가.
2. Candidate-side complexity를 통제하고 zero/weak witness를 제외한 일반 Type S family에서 여전히 비자명한 ambiguity가 있는가, 아니면 측정 가능한 margin으로 모든 해를 제어할 수 있는가.
3. 선택한 실제 loss의 near-optimality가 그 candidate class를 정당화할 수 있는가. 이번 반례 때문에 compositional contrast만으로는 자동 성립하지 않는다.

위 핵심 명제 없이 더 큰 실험을 쌓는 것은 현재 불확실성을 해결하지 못한다. 이번 작업의 완성물은 긍정적 논문 보장이 아니라, 실행한 증거와 실패·수정·남은 위험이 연결된 착수 판단이다.
