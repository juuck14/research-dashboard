**조사 기준: 2026년 10월 21일.** 현재 진행 중인 multimodal interaction 연구와 독립적인 주제를 전제로 했다. 이 문서는 연구 착수 여부를 판단하기 위한 사전 조사이며 새 방법의 성능이나 신규성을 입증한 제안서는 아니다.

**조사 방식과 신뢰 범위.** 대조학습 목적함수, 표현 구조, 비지도 잠재구조, 학습 이론, 분야 밖 탐색의 다섯 독립 연구자가 문헌과 후보를 따로 조사했다. 이후 서로의 최상위 후보를 교차 검토했다. 공식 학회·저널 원문과 저자 원문을 우선 확인했다. 2026년 9~10월 논문은 특히 발표 상태와 범위를 구분했다. 아래의 **[확인]**은 인용 논문의 주장과 조건을 원문에서 확인한 사실, **[해석]**은 여러 결과를 연결한 판단, **[가설]**은 아직 입증하지 않은 연구 명제다. 문헌 검색으로 선행연구의 *부재*를 증명할 수 없으므로 신규성 판정은 잠정적이다. 주석 [R번호]는 Part VI의 원문 링크다.

# Part I. 연구 지형 분석

**목적함수의 성공과 의미 있는 정보의 보존은 다르다.** [확인] Contrastive, redundancy-reduction, prediction, reconstruction은 여러 데이터 영역에서 쓸 만한 표현을 만든다. 그러나 positive view의 공통성만으로 모든 잠재 요인과 가능한 downstream task를 보존한다는 결론은 나오지 않는다. 2026년 *Which Tasks Survive Self-Supervised Learning?*은 특정 이중 view 목적함수의 모집단 최적 부분공간과 task posterior의 중첩으로 회복 가능성을 설명한다 [R1]. *The Loss Is Not Enough*는 sampling 조건과 inductive bias를 구별하고, support를 조정해도 실제 학습 해의 선택까지 자동 해결되는 것은 아님을 보여준다 [R2]. 이 둘을 무시하고 “어떤 정보가 살아남는가”를 처음 묻는 것은 이미 늦다. [해석] 열린 부분은 **약한 신호·유한 표본·유한 학습 시간·다른 의미적 구분이 충돌하는 경우**에 어떤 정보가 *실제로 접근 가능한가*다.

**식별가능성은 가정이 맞을 때의 유일성에서, 가정이 근사적으로 맞을 때의 정직한 주장으로 옮겨간다.** [확인] 추가 구조 없는 disentanglement에는 근본적인 비식별성이 있고 [R3], 보조 환경과 소스 가정을 주면 식별 정리가 가능하다 [R4]. 유한 표본 비선형 ICA 분석 [R5], 근사적 모델의 강건성 [R6], 2026년의 근접 식별성 [R7]도 존재한다. 같은 해의 misspecified-structure 논문은 관측 잡음이 만드는 observation 쪽 조건부 독립 위반을 직접 다룬다 [R8]. [해석] “식별 정리의 조건을 조금 완화”하는 일반론은 이미 혼잡하다. 한 가지 견고한 방향은 **소스 독립성 자체가 약하게 틀리고 환경 변화가 약할 때, 데이터가 지지하는 *부분 구조의 집합*을 정하는 것**이다.



**비지도 학습에는 결과뿐 아니라 주장 가능한 불확실성이 필요하다.** [확인] 2026년 conformal clustering은 알려진 고정 군집 수에서 label confidence를 다루며, 군집 수 선택 후 추론은 별도 문제로 남긴다 [R9]. 하지만 “K를 선택한 뒤 conformal을 적용한다”는 것만으로는 저자들이 명시한 후속 과제의 단순 확장이다. 생성모델의 denoising geometry, 시간적 예측, 재귀적 predictive sufficiency에서도 어떤 구조가 데이터와 측정 기준에 의존하는지 문제가 남는다 [R10–R12].

**계산량을 늘려 해결할 문제와 학습 원리가 틀린 문제를 구분해야 한다.** [확인] streaming SSL에서는 시간적으로 겹치는 minibatch가 목적함수에 따라 다르게 해를 끼친다. 최근 연속 영상 연구는 intra-batch 근접 중복의 역할을 이미 밝힌다 [R13]. 계층 잠재 예측의 표본 복잡도를 다룬 2026년 분석도 있다 [R14]. [해석] 여기서 남는 성과는 또 하나의 모듈보다, 같은 정보·같은 학습량에서 **데이터의 제시 순서나 교사 표현의 오류가 언제 실패를 만드는지 예측하는 작은 법칙**이다.

**교차 검토에서 제외한 인기 있는 간결한 아이디어.** 여러 view의 선형 PSD 목적함수에 대한 rank-d Pareto trade-off는 multi-criteria PCA에 환원된다 [R15]. 독립 instance 수와 반복 view 수를 분리하는 표본 할당은 Wang의 다중 뷰 학습 이론에서 이미 분석됐다 [R16]. PCFG가 단계적으로 학습된다는 관찰과 전부 병렬로 학습된다는 관찰을 ‘모순’이라고 놓는 것도 부정확하다. 두 논문의 sample-size와 학습 시간, final-token과 all-token target, subgrammar loss 정의가 다르며 [R17–R19], 2026년 잠재 예측 이론 자체도 단계적 학습과 teacher 갱신을 논한다 [R14]. 단순 비교 실험을 독립 핵심 후보로 세지 않았다.

# Part II. 후보 연구 방향 11개

**분류.** `심층`은 Part III에서 집중 검토, `조건부`는 먼저 신규성 검증, `탐색`은 흥미롭지만 선행·정의의 위험이 큼을 뜻한다. 질문은 모두 연구 문제이며 방법을 확정한 문장이 아니다.

| 번호·상태 | 핵심 질문과 중요성 | 가장 가까운 선행과 남은 공백 | 가능한 첫 접근·위험·성격 |
|---|---|---|---|
| **1 심층: 근사 가정 아래의 부분 식별** | 환경 변화가 약하고 *소스*의 조건부 독립이 조금 틀릴 때, 어떤 latent factor/group 주장만 데이터가 지지하는가? 과학적 해석의 정직성을 좌우한다. | iVAE·finite-sample ICA·강건성 [R4–R8]. 특히 [R8]은 **관측** 쪽 의존성 위반이라 정확히 같은 질문은 아니지만 매우 가깝다. 유일한 해 대신 허용 해 집합과 방향별 부분 주장에 공백이 있다. | 2~4차원 조건부 생성모형에서 동일 관측 적합도의 대안 latent를 구성. 간단한 perturbation bound 재발견 위험. **이론·통계적 발견**. |
| **2 심층·조건부: 정성적 회복과 실제 회복의 경계** | 동일한 모집단 목표를 갖는 positive mechanism에서도 약한 방향의 유한 자료 및 SGD 회복 경계가 달라지는가? identifiability가 실제 학습 성공을 뜻하는지 시험한다. | finite-sample nICA, AnInfoNCE, spectral SSL, augmentation graph consistency [R2,R5,R20–R22]가 크고 직접적인 선행. **기존 eigengap 설명을 넘는** 통계–최적화 분해가 필요하다. | 고정 eigenfunction의 full-support kernel, 모집단/경험적 oracle/신경망 세 층 비교. 알려진 condition-number 결과에 흡수될 위험. **이론·기전 실험**. |
| **3 심층·고위험: 의미 요인별로 달라지는 false-negative 관계** | 한 요인의 동일함은 다른 요인의 동일함이 아닐 때, negative 규칙은 어떤 요인의 *표현 가능성*을 희생시키는가? | suppression, MCL, GloFND, FALCON [R23–R26]이 이미 negative 조정·거짓 음성을 다룬다. 단순 mining 방법은 신규성이 없다. 요인별 관계의 양립성과 **metric 충돌 vs 정보 소실**을 구분해야 한다. | 2~3 독립 요인의 합성 자료, 정책별 선형·비선형 probe와 oracle factor. retrieval 차이를 정보 소실로 과장할 위험. **목적함수 원리·실험적 발견**. |
| **4 심층: 상관된 스트림의 배치 통계와 학습 기억** | 같은 고유 이미지와 업데이트 횟수라도 제시 순서·배치 구성·teacher 시간척도가 붕괴 경계를 바꾸는가? iid 가정의 실제 내용을 묻는다. | 연속 영상 [R13], streaming orthogonal gradients [R27], replay [R28]. intra-batch 중복과 EMA sweep 자체는 이미 연구됐다. 손실별 **사전 예측 가능한 조건**이 공백이다. | 작은 고정 데이터셋의 permutation만 조작. batch rank나 기존 결과 재현으로 끝날 위험. **학습동역학·실험적 발견**. |
| **5 심층·고위험: 불완전한 자기 생성 target의 교정 가능성** | 하위 표현이 중요한 두 상태를 합쳐 버린 경우, raw context와 teacher의 갱신이 상위 구분을 되살릴 수 있는가? 추상화의 자기 수정 한계를 묻는다. | latent prediction sample complexity와 data2vec 계층·teacher 분석 [R14], 자기증류 이론 [R29]. 단순 frozen target merge의 실패는 자명하다. **teacher 오차가 내생적일 때의 회복 경계**가 필요하다. | 작은 PCFG/Markov 구조, frozen vs evolving teacher와 raw evidence 통제. 기계적 data-processing 재증명 위험. **이론·학습동역학**. |
| **6 조건부: task-free 모델 선택에 필요한 최소 task prior** | label 없는 scalar 품질 지표로 선택이 불가능할 때 어떤 소량의 선호 정보가 두 표현의 순위를 정하는가? | RankMe·LiDAR·GULP·2026 task recoverability [R1,R30–R32]. “모든 과제에 최고”는 불가능하거나 공허하다. task family를 지정한 query complexity가 남을 수 있다. | 두 상반된 합성 task, 허용 feedback 한 비트. no-free-lunch 재진술 위험. **결정이론·평가 원리**. |
| **7 고위험: 예측 가능한 nuisance의 비식별성 경계** | 신호와 방해 요소가 모두 시간적으로 예측 가능하면 task-free predictor는 어느 것을 버려야 하는가? | RP-GSSM과 2026 predictive SSL 이론 [R33,R11]. nuisance도 예측 가능하다는 관찰 자체는 새롭지 않다. swap 대칭을 깨는 최소 관측/개입 조건이 핵심. | 두 독립 Markov 과정의 역할 교환과 한 종류의 side information. 이미 알려진 temporal ICA 조건으로 끝날 위험. **식별 이론**. |
| **8 조건부: 군집 수 선택 후의 진술 해상도** | K를 고른 뒤 ‘두 점은 같은 군집’이라고 정직하게 말할 수 있는 조건은? | fixed-K conformal clustering [R9], cluster-tree inference [R35]. 선택 후 추론은 이미 지목된 확장이다. component 병합 경계에서 coverage–abstention 한계가 필요하다. | 2D 혼합분포에서 pairwise 3값 진술. 단순 data split이면 기여 부족. **통계적 추론**. |
| **9 탐색: 생성 정보와 작은 readout의 접근성** | diffusion의 요인별 정보량이 많아도 제한된 label·probe로 못 읽는 영역을 예측할 수 있는가? | low-dimensional diffusion 분석·invariant contamination·2026-10 feature MI [R36–R38]. 중간 timestep의 semantic peak는 선점됐다. | oracle denoiser와 고정 probe의 표본위험. invertible feature·whitening으로 차이가 없어질 위험. **표현 통계·고위험**. |
| **10 탐색: 유한 predictive tests의 보장 범위** | 반복 압축에서 몇 개의 예측 테스트가 보지 못한 긴 미래의 정보를 보증하는가? | predictive-state representation [R39], 2026 local predictive sufficiency [R12]. finite-test residual 자체도 논의됐다. 한정된 finite-rank 계에서 sharp 경계가 필요하다. | 작은 HMM의 동일 test score·다른 먼 미래 쌍. 기존 spectral PSR 재발견 위험. **이론**. |
| **11 탐색: diffusion 기하의 좌표·noise kernel 의존성** | 같은 분포를 단위 변환했을 때 ‘내재적’ denoising geometry는 어느 부분까지 유지되는가? | geometric phases, spacetime/Fisher geometry [R40,R10]. 새로운 metric 하나를 붙이는 것은 중복. 관측 변환과 noise kernel의 동시 변환 규칙이 문제다. | oracle 2D mixture, affine 및 비선형 좌표 변환. covariance normalization만으로 설명될 위험. **기하·원리 분석**. |

위 표의 9–11은 의도적으로 위험한 후보를 남긴 것이다. 현 단계에서 수개월의 주제로 추천한다는 뜻은 아니다. 1과 2는 같은 ‘약한 신호’ 어휘를 쓰지만, **1은 잘못 지정된 모형에서 무한 자료에도 남는 모호성**, **2는 올바른 목표가 정해진 뒤 유한 자료·학습의 회복 실패**를 묻는다. 3은 objective의 negative 관계, 4는 stream 순서, 5는 잘못된 자기 생성 target이라는 서로 다른 원인을 검토한다.

# Part III. 유망한 다섯 방향 심층 분석

## 1. 데이터가 실제로 지지하는 잠재 구조: 부분 식별

**문제와 중요성.** 해석 가능한 representation이라고 주장할 때 seed별 MCC가 높거나 한 학습기가 늘 같은 요인을 출력하는 것으로는 부족하다. 같은 관측분포를 거의 똑같이 설명하는 다른 잠재 분해가 있으면 데이터는 그 좌표를 선택하지 못한다. 여기서는 소스가 환경에 조건화했을 때 완전히 독립이라는 가정의 작은 위반과, 환경 변화가 일부 방향에서 약한 상황을 결합한다. 무한 자료에서도 어떤 factor, factor group, 또는 subspace만 공통으로 남는가가 목표다.

**선행의 발전과 차이.** Locatello의 무가정 불가능성 [R3] 이후 iVAE [R4]는 보조변수와 충분한 variability로 식별을 확보했다. Lyu–Fu [R5]는 유한 표본 오차를 이미 다뤘고, Buchholz–Schölkopf [R6]는 misspecification 강건성과 불연속적 실패를 연구했다. Nelson 등 [R7]의 near-identifiability 및 2026년 Li 등의 perturbed factor analysis [R8] 때문에 “조금 틀린 모형도 괜찮다”는 표어는 새롭지 않다. [R8]의 오류는 *observation* 조건부 독립 쪽이며, 여기의 초점은 **latent source의 약한 조건부 의존성과 환경의 약한 식별력 아래 관측자료가 허용하는 모든 구조**다. 이 구별만으로 신규성이 보장되지는 않는다.

**[가설]** 같은 총 의존성 편차라도 약한 환경 방향에 정렬된 편차는 큰 모호성을 만들고, 강한 방향의 편차는 공통 부분구조를 유지할 수 있다. 편차의 수치는 좌표·latent 재매개화에 따라 달라지므로 허용 변환군과 divergence 측도를 먼저 고정해야 한다. 단순 `오차/최소 특이값` 상계 이상의 주장은 **동일한 허용 관측분포를 내는 대안 생성모형과, 방향별로 유지되는 식별 집합**으로 제시해야 한다.

**가능한 접근.** (a) 2~4개의 조건부 Gaussian/exponential-family 소스와 invertible mixing에서 두 대안 모형을 직접 구성하여 identified set의 지름과 부분구조를 상·하한으로 묶는다. (b) near-optimal 관측 likelihood와 구조 위반 tolerance를 만족하면서 latent disagreement를 크게 하는 adversarial alternative-fit를 찾는다. (b)의 탐색 실패를 유일성 증명으로 해석하지 않고 (a)의 정확한 사례와 연결한다. 독립 학습 seed 간 일치도는 보조 진단에 그친다.

**최소 검증.** 3 latent, 환경 6~12개, mixing 고정. 환경 변화의 작은 singular value와 latent 조건부 의존도를 각각 두세 단계로 변화시킨다. 동일 holdout density-fit를 갖는 해 중에서 factor/group 판정이 달라지는 사례를 찾고, 이 차이가 표본을 늘려도 남는지 본다. 참 latent는 합성 실험의 oracle 평가에만 쓰며 실제 데이터에 적용 가능한 인증이라고 과장하지 않는다.

**중단 조건과 기여.** 고전 joint diagonalization perturbation으로 정확히 예측되거나 [R8]의 재매개화로 동일 정리에 환원되면 독립 주제를 접는다. 원리상 다른 분해의 존재를 보여도 유용한 *부분 주장*이 전혀 남지 않으면 실용적 의미가 약하다. 성공 시 기여는 새로운 encoder보다 **모형 오류 아래 latent 해석의 식별 경계와 정직한 보고 단위**다. 수학 위험 높음, 계산·엔지니어링 부담 낮음.

## 2. 정성적 식별과 유한 학습의 간극

**문제와 중요성.** “모든 요인이 양의 확률로 변한다”는 조건은 요인이 *언제* 보이게 되는지 말하지 않는다. 그러나 finite-sample ICA [R5], anisotropic InfoNCE [R20], spectral contrastive loss [R21], augmentation graph consistency [R22]가 있으므로 약한 singular value가 힘들다는 것만으로 독창적 연구가 아니다. [R2]의 교훈도 크다. support가 같아도 목표 표현이 같다는 보장은 없다. 먼저 모든 실험 조건에서 **동일한 population target function space**를 갖는 가족을 증명해야 한다.

**[가설]** 같은 최적 부분공간과 같은 independent samples에서도 희소한 방향의 neural 회복 실패에는 경험적 추정 오차만으로 설명되지 않는 학습 시간/매개화의 성분이 있고, 그 크기는 단순 objective value보다 factor별 gradient 신호나 Hessian 조건수로 예측된다. 이것이 전부 기존 고유값 간격과 optimizer 조정으로 설명된다면 가설은 실패다.

**가능한 접근.** 균형 잡힌 유한 상태 공간의 고정된 정규직교 함수 ψ_j와 양의 λ_j를 두고 `K_λ(x,x′)=M⁻¹[1+Σ_j λ_j ψ_j(x)ψ_j(x′)]` 같은 양의 전이 kernel을 *분석용 통제*로 삼는다. 적절한 λ의 범위에서는 full support와 top-d 함수공간을 유지하면서 한 방향의 강도만 낮출 수 있다. 이 모형 자체는 새 방법이나 기여가 아니다. 다른 목적함수의 optimum이 정말 같은지는 별도로 증명한다. (i) 모집단 oracle, (ii) 동일 자료의 경험적 spectral/global solution, (iii) 작은 neural encoder의 결과를 나란히 두고 통계 gap과 추가 neural gap을 구분한다. 반복 view 수는 [R16]과의 중복을 피하기 위해 하위 대조만 둔다.

**최소 검증.** 요인 3개, 약한 λ 4수준, 독립 instance 3수준, optimizer budget 3수준. factor별 held-out recovery, 최적 목적함수와의 gap, 선형·비선형 readout을 함께 본다. positive pair 개수를 독립 관측 개수로 잘못 계산하지 않는다. 1주차에 full-support target의 불변성을 보이고, 한 고정 데이터의 empirical oracle와 neural curve를 그리는 것으로 충분하다.

**중단 조건과 기여.** population target이 변하면 이 비교를 중단한다. neural gap이 learning-rate/normalization 변경이나 알려진 eigengap·matrix concentration으로 전부 설명되면 새 원리의 자리가 없다. 여러 작은 생성모형에서 예측력 있는 neural-specific 경계가 남으면 “식별가능한 목표가 학습 가능한 목표가 되는 조건”에 기여할 수 있다. **신규성 위험이 매우 높으며**, 상위 추천이라기보다 빨리 죽일 수 있는 조건부 실험이다.

## 3. 여러 의미적 동치관계와 negative의 역할

**문제와 중요성.** 같은 shape의 다른 color 물체는 shape에 대해서 positive처럼 보이지만 color에 대해서는 다른 예다. ‘false negative’는 task 또는 잠재 요인이 정해져야 의미가 있다. [R23]은 feature suppression, [R24]는 learned feature를 고려한 negative mining, [R25]는 전역 거짓 음성 탐지, [R26]은 hard/false-negative 균형을 이미 다룬다. 그래서 유사한 점을 제거하는 스케줄러나 새 weight를 만들자는 제안은 이 조사에서 제외한다.

**남은 문제.** 요인별 다른 동치관계와 batch sampling policy가 학습한 표현의 **요인별 정보 보존**, 또는 표현에는 있으나 작은 readout으로 못 읽는 **접근성**, 단일 cosine metric의 실패 중 어디에 영향을 주는가? 이는 task posterior와 SSL 부분공간을 연결한 [R1]도 기준선으로 삼아야 한다. 충분한 표현 차원과 모든 negative에 양의 선택확률이 있어도 **현 표현에 의존하는 mining 피드백이 특정 요인을 배우지 않는 안정점을 만드는가**가 가장 날카로운 미검증 질문이다. downstream retrieval 하나에서 나쁜 결과를 보고 정보가 지워졌다고 결론내릴 수 없다.

**[가설]** negative policy가 현재 가장 잘 학습된 요인에 의존하면, 다른 요인의 학습 신호가 커질 수도 있고 반대로 밀려날 수도 있다. 방향은 요인의 prevalence, 표현 용량, policy feedback에 의해 달라질 것이다. 따라서 보편적으로 “false negative를 제거해야 한다”는 주장보다 **어떤 조건에서 어느 요인의 접근성이 바뀌는지**가 연구 결과다.

**가능한 접근.** 2~3개 독립 요인을 갖는 합성 이미지/이산 code. positive law는 고정하고 negative policy만 독립 sampling, 현재 embedding hard mining, 요인 oracle matching, 고정 혼합 비율로 바꾼다. hard deletion 대신 모든 negative에 작은 확률 하한을 두는 soft policy도 포함한다. 같은 encoder 용량과 updates에서 요인별 Bayes/선형/작은 MLP probe, mutual-information oracle 또는 exact posterior, retrieval을 분리 기록한다. factor labels는 학습하지 않고 진단에만 쓴다. 간단한 density-ratio optimum을 먼저 구해 policy로 인한 모집단 목표 변화와 최적화 변화를 나눈다.

**중단 조건과 기여.** cosine retrieval만 달라지고 충분한 readout의 요인 정보는 같다면 ‘정보 소실’ 논지를 접고 metric-alignment 질문으로 격하한다. 결과가 FALCON/MCL의 알려진 hard–FN trade-off에 그대로 들어가면 독립 주제로 접는다. 성공 시 하나의 부호(negative)가 특정 task에 대한 부호를 정하지 못한다는 **목적함수의 다중 관계 경계**가 기여다. 계산은 작고 해석 난도·선행 밀도는 높다.

## 4. 상관된 스트림에서 무엇이 학습 실패를 만드는가

**문제와 선행.** streaming 영상은 동일 분포의 무작위 minibatch를 전제하기 어렵다. orthogonal gradients [R27], replay [R28], 2026년 *I Have a Stream* [R13]이 이미 관련 방법과 실패 현상을 보고했다. 특히 [R13]은 intra-batch 중복을 주요 요인으로 찾고 여러 loss와 완화책을 비교한다. 따라서 ‘순서가 중요하다’, ‘EMA를 바꾸면 낫다’, ‘버퍼로 해결한다’는 것은 새 기여가 아니다.

**정확한 공백과 [가설].** 같은 고유 이미지, marginal, updates라도 (i) minibatch의 occupancy/covariance, (ii) 순서에 따른 gradient noise, (iii) teacher·centering의 상태가 다른 효과를 낼 수 있다. [R13]의 부록은 slow/fast teacher, prototype 속도, temporal positives 등의 조작까지 이미 시험했다. [가설] 한 개의 유효 표본 수나 batch rank보다 **같은 minibatch 집합의 순서와 학습 상태의 기억 길이**가 특정 objective의 collapse boundary를 예측한다. 이 결론을 모든 SSL에 일반화해서는 안 된다. 처음부터 Markov/mixture stream에서 예측할 수 있는 부호나 임계 조건을 적어야 사후 설명을 피한다.

**가능한 접근.** 선형 encoder의 teacher-based SSL과 per-sample reconstruction을 통제 모형으로 비교하고, 이어 작은 MLP/CNN에서 재현한다. 하나의 고정된 데이터셋을 무작위 순서와 긴 burst 순서로 제시한다. 각 이미지의 노출 횟수, augmentation 횟수, update 수를 같게 한다. 더 강한 대조에서는 **미리 만든 동일한 minibatch들의 순서만 바꿔** 내부 통계를 정확히 일치시키고 optimizer state의 효과를 따로 통제한다. minibatch 다양성을 직접 회복하는 intervention과 teacher 기억 길이만 바꾸는 intervention을 따로 시행한다. 데이터가 달라져 생기는 ‘정보 부족’을 순서 효과와 섞지 않는다.

**최소 검증·중단 조건.** 첫 주에는 두 순서, 두 손실, 두 burst 길이로 effective rank와 factor별 probe를 측정하고, second week에 모형에서 정한 한 예측을 검증한다. 배치 다양성 회복만으로 모든 차이가 사라지고 [R13]의 결론을 반복한다면 이 주제는 끝낸다. 반대로 **동일한 배치 occupancy에서도 상태 기억의 효과가 분리되고 사전 모형이 예측**하면 원리적 기여 가능성이 있다. 엔지니어링 낮음~중간, 현실성 높음, 신규성 위험 중상.

## 5. 잘못된 자기 생성 target을 상위 학습이 고칠 수 있는가

**문제와 선행.** 계층 잠재 예측의 잠재 상태를 이미 완벽히 알고 주는 이론은 강력하지만 [R14], 실제 self-distillation의 teacher는 스스로 오류를 만든다. [R14]는 data2vec의 계층적 학습과 teacher update도 연구했으므로 “teacher가 차례대로 배운다”는 관찰은 새롭지 않다. 정지한 하위 표현이 A와 B를 같게 mapping하면 그 값만 받는 다음 단계가 구분을 복구할 수 없다는 것은 정보처리 부등식의 평범한 결과다.

**남은 문제와 [가설].** 상위 predictor가 *원 관측의 추가 문맥*을 계속 보고, teacher가 학생이나 더 긴 문맥에서 갱신되는 경우에는 하위 오분류가 잠깐 존재해도 회복 경로가 남는다. 정보가 완전히 소실된 merge는 trivial하다. **raw context와 초기 teacher target 양쪽 모두 해당 구분을 약하게 보존하는 full-rank 영역에서도** 갱신 피드백이 오류를 고착시키는 안정점이 있는지가 새로운 질문이다. 하위 표현의 평균 정확도보다 conditional prediction operator의 conditioning과 teacher refresh 규칙이 회복 시간을 예측할 수 있다는 것은 미검증 가설이다.

**접근과 작은 실험.** 깊이 2~3 PCFG 또는 작은 Markov 생성기에서 대조 상태 한 쌍을 초기에 teacher가 *약하게* 구별하도록 한다. target confusion matrix의 rank와 singular value, frozen teacher의 Bayes-optimal predictor를 먼저 계산한다. raw token/context를 어느 경로에 남기는지 조작하고 frozen·EMA/evolving teacher를 비교한다. 모두 같은 관측·예산·model capacity를 써야 한다. 초기 오차만 다른 두 teacher가 결국 같은 해로 수렴하는지, 혹은 안정적 편향에 갇히는지 시간축으로 기록한다. 먼저 toy population update의 고정점/안정성을 분석하고 그다음 작은 신경망으로 확장한다.

**중단 조건과 기여.** frozen target 실패는 결과로 세지 않는다. 이론이 [R14]의 teacher dynamics나 고전 자기훈련 분석을 변수만 바꿔 재현하면 접는다. end-to-end 갱신에서도 raw context 추가와 self-correction이 분리되지 않으면 설명력이 없다. 살아남는다면 계층적 SSL에서 **불완전한 target의 가역적·비가역적 오류 경계**가 성과다. 위험 높고 사용자 선호의 간결성은 초기 toy model까지만 보장된다.

# Part IV. 비교 평가

평가의 뜻: `높`은 높은 중요성/기여/적합성/실현성/확장성, `낮`은 낮은 엔지니어링 부담/실패 위험을 뜻한다. 수치 점수의 평균은 만들지 않았다. 기여와 실패 위험의 평가는 **문헌 조사에 근거한 판단**이지 채택 가능성의 확률이 아니다.

| 방향 | 중요성 | 신규 기여 여지 | 간결성·관심 적합성 | 엔지니어링·실현성 | 위험·확장성 | 판단을 가르는 이유 |
|---|---|---|---|---|---|---|
| 1 부분 식별 | 높 | 중상 | 높·높 | 낮·중 | 높·높 | 해석 주장 자체를 바꿀 수 있으나 [R6–R8]과의 차이가 수학적으로 정확해야 한다. |
| 2 유한 회복 경계 | 높 | 중 | 높·매우 높 | 낮·높 | 매우 높·높 | 빠르게 반증 가능하나 기존 eigengap/finite-sample 이론과 중복하기 쉽다. |
| 3 의미별 negatives | 높 | 중 | 중상·매우 높 | 낮·높 | 높·높 | 질문은 직관적이나 mining 선행이 풍부하고 metric과 정보 혼동이 쉽다. |
| 4 streaming 원인 경계 | 높 | 중상 | 중상·높 | 낮~중·높 | 중상·높 | 동일 데이터의 순서만 바꿀 수 있어 좋은 통제; [R13]을 넘어선 예측이 관건. |
| 5 target 자기 교정 | 높 | 중 | 중·높 | 중·중 | 높·높 | 계층 학습의 핵심이나 [R14]와 겹치고 teacher 설계로 복잡해질 수 있다. |
| 6 최소 task prior | 중상 | 중 | 높·높 | 낮·높 | 높·중상 | 평가 문제에 실용성은 있으나 no-free-lunch의 재서술 위험. |
| 7 예측 nuisance | 높 | 중 | 높·중상 | 낮·중 | 매우 높·높 | 불가능성은 쉽고 유의미한 positive boundary가 어렵다. |
| 8 K 선택 후 군집 진술 | 중상 | 낮~중 | 높·중 | 낮·높 | 중상·중 | 가까운 논문이 후속 과제로 이미 명시했으며 단순 split으로 끝날 수 있다. |
| 9 diffusion 정보/읽기 | 중상 | 낮~중 | 중·중 | 낮~중·중 | 매우 높·중상 | 2026년 직접 선행과 경쟁하며 단순 probe 결과는 약하다. |
| 10 finite predictive tests | 중상 | 중 | 중상·중상 | 낮·중 | 높·높 | 이론적으로 깊지만 PSR 선행을 소화해야 한다. |
| 11 diffusion 좌표 기하 | 중 | 낮~중 | 중상·중 | 낮·중 | 높·중 | 변환군의 정의가 명확해도 normalization으로 해소될 수 있다. |

**주요 trade-off.** 1은 계산보다 수학적 정의가 어렵고 무한표본에서 무엇을 말할 수 있는지를 다룬다. 2는 가장 짧은 실험으로 탈락 여부를 알 수 있지만, 논문 기여의 문턱이 예상보다 높다. 3은 선호 분야의 중심에 있지만 negative-policy 분야가 혼잡하다. 4는 엔지니어링 없는 학습 원리 발견의 기회가 크되 2026년 직접 선행의 실험을 벗어나야 한다. 5는 지적 매력이 가장 큰 축 중 하나이나 연구 중간에 여러 학습 모듈의 조합으로 변질되지 않도록 통제할 필요가 있다. **추천 순위는 성공을 보장하는 점수가 아니라 지금 조사에서 가장 정보량 높은 다음 판정 순서**다.

# Part V. 최종 추천과 첫 1–2주

**1순위 — 부분 식별(후보 1).** interaction 연구와 완전히 독립적으로 진행할 수 있으며 “데이터로 무엇을 안다고 말할 수 있는가”라는 근본 질문이 명확하다. 이론·작은 생성모형으로 시작할 수 있다. 먼저 [R4–R8]에서 어느 독립성(소스/관측), 어느 위반(모형/표본), 어느 equivalence class를 다루는지 한 장 표로 대조한다. 3일 안에 동일한 관측 law를 만드는 두 latent 모형의 반례를 찾아보고, 1주차에는 환경 신호 강도×의존성 편차의 2D 격자에서 부분적으로 공통인 구조가 있는지 분석한다. 2주차에는 seed agreement와 alternative-fit ambiguity를 비교한다. **판정:** [R8] 또는 고전 perturbation의 즉각적인 corollary면 접는다; 무한표본에서도 남는 비자명한 부분 진술과 대안 DGP가 함께 나오면 계속한다.

**2순위 — 의미별 negative 관계(후보 3).** contrastive learning의 근본 목적함수를 직접 건드리면서 빠른 작은 실험이 가능하다. 다만 ‘새 negative mining 기법’으로 시작하지 않는다. 첫 3일은 [R23–R26]과 [R1]의 목표·정의·측정값을 맞추고, 두 요인의 정확한 positive/negative 관계표를 만든다. 1주차에는 positive 법을 고정한 2-factor synthetic에서 독립·hard·oracle policy의 모집단 score를 계산한다. 2주차에는 충분한 표현 차원과 negative 확률 하한을 유지한 채, endogenous mining feedback에 따른 factor 회복, retrieval, linear/MLP probes를 나란히 측정한다. **판정:** metric만 달라지거나 기존 FN 균형으로 설명되면 접는다; soft policy에서도 요인 접근성을 가로막는 안정점과 예측 가능한 경계가 있으면 계속한다.

**3순위 — 불완전한 자기 target의 교정(후보 5, 야심 찬 선택).** [R14]의 A1/A2 가정과 teacher 갱신 결과를 먼저 정리한다. 1주차에는 raw context와 teacher target이 **둘 다 약하지만 양의 구별 정보를 담는 full-rank** toy PCFG에서 frozen teacher의 Bayes 예측 한계와 학습 동역학을 분리한다. 2주차에는 동일한 초기 오류에서 teacher를 한 번만 갱신하는 조건과 지속 갱신하는 조건의 안정점·교정 시간을 예측한다. **판정:** target의 rank나 frozen noisy-label 난도로 모든 차이가 설명되면 접는다. 정보가 남아 있는데도 teacher feedback만으로 교정/고착이 갈리는 경계가 나오면 계속한다. 큰 data2vec 실험의 재현을 착수 요건으로 삼지 않는다.

후보 4(streaming)는 실제로 작업하기 쉬운 **대체 3순위**이지만, [R13] 부록이 이미 teacher·prototype 속도와 temporal positives 등 여러 조작을 시험했다. 동일한 minibatch 집합을 **순서만 바꾸고** optimizer state와 batch occupancy를 통제한 뒤, 손실별 안정성을 사전에 예측할 수 있을 때 추천 순위에 올린다. 후보 2는 한 주의 **병렬적인 신규성 반증용 소실험**으로 가치가 있다. 고정 target을 증명하고 경험적 oracle와 neural learner의 gap이 기존 이론 이상의 예측인지 확인한 뒤에만 주력과 바꾼다.

# Part VI. 핵심 참고문헌과 역할

표시 `★`는 추천 세 방향에 특히 가까운 원문, `†`는 2026년 최근 선행으로 신규성 주장에 결정적이다. 출판 연도는 공식 proceedings가 확인된 경우 그것을 썼고, 그 외에는 preprint로 표기했다. 원문에서 직접 다루는 범위를 넘겨 일반 결과로 인용하지 않았다.

| 번호 | 논문·연도·링크 | 조사에서의 의미 |
|---|---|---|
| R1 † | Luthra et al., [Which Tasks Survive Self-Supervised Learning?](https://arxiv.org/abs/2609.38393), 2026-09 preprint | task posterior와 population SSL 부분공간의 관계; 표현 보존 일반론의 가장 가까운 선행. |
| R2 | Zaliaduonis et al., [The Loss Is Not Enough: Sampling Conditions and Inductive Bias in Contrastive Representation Learning](https://proceedings.mlr.press/v306/zaliaduonis26a.html), ICML 2026 | sampling support, 학습 편향, optimum 선택의 구분. |
| R3 | Locatello et al., [Challenging Common Assumptions in the Unsupervised Learning of Disentangled Representations](https://proceedings.mlr.press/v97/locatello19a.html), ICML 2019 | 무가정 disentanglement 불가능성의 기준. |
| R4 ★ | Khemakhem et al., [Variational Autoencoders and Nonlinear ICA: A Unifying Framework](https://proceedings.mlr.press/v108/khemakhem20a.html), AISTATS 2020 | 보조변수·소스 구조 아래 식별의 출발점. |
| R5 ★ | Lyu and Fu, [On Finite-Sample Identifiability of Contrastive Learning-Based Nonlinear Independent Component Analysis](https://proceedings.mlr.press/v162/lyu22a.html), ICML 2022 | finite-sample nICA는 이미 연구됐다는 필수 비교. |
| R6 ★ | Buchholz and Schölkopf, [Robustness of Nonlinear Representation Learning](https://proceedings.mlr.press/v235/buchholz24a.html), ICML 2024 | misspecification의 robust/fragile 식별 직접 선행. |
| R7 | Nelson et al., [Statistical and Structural Identifiability in Representation Learning](https://arxiv.org/abs/2603.11970), ICLR 2026 | near-identifiability의 최신 경계. |
| R8 ★† | Li et al., [Towards Identifiable Representations under Misspecified Structure](https://arxiv.org/abs/2609.33273), 2026-09 preprint | 관측 conditional independence 위반을 다룸; 후보 1과 명시적으로 차별화할 직접 선행. |
| R9 | Hur, Nath and Allen, [Inference for Clustering: Conformal Sets for Cluster Labels](https://arxiv.org/abs/2604.03488), 2026 preprint | fixed K 보장 및 K 선택 후 추론의 근접 문제. |
| R10 | Karczewski et al., [The Spacetime of Diffusion Models: An Information Geometry Perspective](https://proceedings.iclr.cc/paper_files/paper/2026/hash/ad2b3b0963114adddbd2c97d6e74abb9-Abstract-Conference.html), ICLR 2026 | denoising posterior의 기하; 후보 11 신규성 제한. |
| R11 | Mikulasch et al., [Predictive Self-Supervised Learning Provably Identifies Stochastic Signals under Nuisance](https://arxiv.org/abs/2609.37789), 2026 preprint | stochastic dynamics와 observation-private nuisance 선행; formal 범위는 착수 전 재검토. |
| R12 † | Wang et al., [What to Preserve in Recursive Computation: A Local Predictive Sufficiency Principle](https://arxiv.org/abs/2610.04303), 2026-10 preprint | 재귀 예측 충분성 및 finite-test 검토의 직접 선행. |
| R13 ★† | Martinović et al., [I Have a Stream: Making Self-Supervised Learning Work on Continuous Video](https://arxiv.org/abs/2609.40333), 2026-09 preprint | streaming SSL의 intra-batch 중복 및 목적함수 차이, 후보 4의 가장 가까운 실험 선행. |
| R14 † | Korchinski et al., [Learn from your own latents and not from tokens: A sample-complexity theory](https://arxiv.org/abs/2605.27734), 2026 preprint | 계층 latent prediction, data2vec 및 teacher 갱신; 후보 5의 핵심 경쟁 선행. |
| R15 | Tantipongpipat et al., [Multi-Criteria Dimensionality Reduction with Applications to Fairness](https://proceedings.neurips.cc/paper/2019/hash/2201611d7a08ffda97e3e8c6b667a1bc-Abstract.html), NeurIPS 2019 | 초기 ‘여러 view의 PSD Pareto’ 아이디어를 제외한 직접 환원 대상. |
| R16 | Wang, [Self-Supervised Metric Learning in Multi-View Data: A Downstream Task Perspective](https://arxiv.org/abs/2106.07138), JASA 2023 | 독립 instance와 반복 view의 이론적 구별; 초기 후보 제외. |
| R17 | Cagnetta and Wyart, [Towards a theory of how the structure of language is acquired by deep neural networks](https://arxiv.org/abs/2406.00048), NeurIPS 2024 | 문법 계층의 sample-size 단계. |
| R18 | Schulz et al., [Unraveling Syntax: Language Modeling and the Substructure of Grammars](https://arxiv.org/abs/2510.02524), 2025 preprint, 2026 개정 | all-token autoregressive subgrammar 학습 분석; R17과 측정축 다름. |
| R19 | Parley et al., [Deep Networks Learn to Parse Uniform-Depth Context-Free Languages from Local Statistics](https://arxiv.org/abs/2602.06065), ICML 2026 | 문법 학습의 다른 조건·목표; 단순 단계 대 병렬 구도를 경계. |
| R20 | Rusak et al., [InfoNCE Identifying the Gap Between Theory and Practice](https://arxiv.org/abs/2407.00143), AISTATS 2025 | anisotropic 신호 강도 연구; 후보 2에 대한 직접 신규성 제약. |
| R21 | HaoChen et al., [Provable Guarantees for Self-Supervised Deep Learning with Spectral Contrastive Loss](https://papers.nips.cc/paper/2021/hash/27debb435021eb68b3965290b5e24c49-Abstract.html), NeurIPS 2021 | spectral graph의 population/sample 결과. |
| R22 | Li and Neuman, [Consistency of Augmentation Graph and Network Approximability in Contrastive Learning](https://www.jmlr.org/papers/v27/25-1466.html), JMLR 2026 | augmentation graph의 통계·근사 조건; 후보 2의 경쟁 선행. |
| R23 ★ | Xue et al., [Which Features are Learnt by Contrastive Learning? On the Role of Simplicity Bias in Class Collapse and Feature Suppression](https://proceedings.mlr.press/v202/xue23d.html), ICML 2023 | feature suppression의 기전 선행. |
| R24 ★ | Zhang et al., [Learning the Unlearned: Mitigating Feature Suppression in Contrastive Learning](https://arxiv.org/abs/2402.11816), ECCV 2024 | 학습된 요인에 맞춘 negative mining의 직접 선행. |
| R25 ★ | Balmaseda et al., [Discovering Global False Negatives On the Fly for Self-supervised Contrastive Learning](https://proceedings.mlr.press/v267/balmaseda25a.html), ICML 2025 | 거짓 음성 탐지 자체는 새 방법이 아님. |
| R26 ★† | Kim et al., [FALCON: False-Negative Aware Learning of Contrastive Negatives in Vision-Language Alignment](https://arxiv.org/abs/2505.11192), CVPR 2026 | hard/false-negative 적응적 균형; 후보 3의 최신 경쟁 선행. |
| R27 ★ | Han et al., [Learning from Streaming Video with Orthogonal Gradients](https://openaccess.thecvf.com/content/CVPR2025/html/Han_Learning_from_Streaming_Video_with_Orthogonal_Gradients_CVPR_2025_paper.html), CVPR 2025 | stream 학습 기울기와 개선의 선행. |
| R28 ★ | Yang and Ren, [Memory Storyboard: Leveraging Temporal Segmentation for Streaming Self-Supervised Learning from Egocentric Videos](https://proceedings.mlr.press/v330/yang26a.html), PMLR 2026 | temporal segmentation/replay 방법의 비교. |
| R29 | Grill et al., [Bootstrap Your Own Latent: A New Approach to Self-Supervised Learning](https://proceedings.neurips.cc/paper/2020/hash/f3ada80d5c4ee70142b17b8192b2958e-Abstract.html), NeurIPS 2020 | online/target network 자기증류의 고전적 출발점. |
| R30 | Garrido et al., [RankMe: Assessing the Downstream Performance of Pretrained Self-Supervised Representations by Their Rank](https://proceedings.mlr.press/v202/garrido23a.html), ICML 2023 | label-free 품질 지표. |
| R31 | Thilak et al., [LiDAR: Sensing Linear Probing Performance in Joint Embedding SSL Architectures](https://arxiv.org/abs/2312.04000), ICLR 2024 | surrogate task 기반 label-free 평가. |
| R32 | Boix-Adserà et al., [GULP: a prediction-based metric between representations](https://proceedings.neurips.cc/paper_files/paper/2022/hash/2f0435cffef91068ced08d7c7d8e643e-Abstract-Conference.html), NeurIPS 2022 | 제한된 probe family의 표현 비교. |
| R33 | Hromadka et al., [Maximum-Likelihood Learning of Latent Dynamics Without Reconstruction](https://proceedings.mlr.press/v306/hromadka26a.html), ICML 2026 (2025 preprint) | RP-GSSM의 reconstruction-free temporal state 및 배경 nuisance. |
| R35 | Kim et al., [Statistical Inference for Cluster Trees](https://arxiv.org/abs/1605.06416), NeurIPS 2016 | hierarchy confidence를 새 것으로 착각하지 않기 위한 선행. |
| R36 | Li et al., [Understanding Representation Dynamics of Diffusion Models via Low-Dimensional Modeling](https://arxiv.org/abs/2502.05743), 2025 preprint | 중간 노이즈의 표현 peak 분석. |
| R37 | Li et al., [Evaluating the Representation Space of Diffusion Models via Self-Supervised Principles](https://arxiv.org/abs/2606.09718), 2026 preprint | feature invariance/contamination 선행. |
| R38 † | Pan et al., [Feature Information Dynamics in Diffusion](https://arxiv.org/abs/2610.08626), 2026-10 preprint | 요인 MI의 noise-scale 동역학; 후보 9의 직접 신규성 장벽. |
| R39 | Littman et al., [Predictive Representations of State](https://proceedings.neurips.cc/paper/2001/file/1e4d36177d71bbb3558e43af9577d70e-Paper.pdf), NeurIPS 2001 | predictive test representation의 고전적 기원. |
| R40 | Ventura et al., [Manifolds, Random Matrices and Spectral Gaps: The Geometric Phases of Generative Diffusion](https://proceedings.iclr.cc/paper_files/paper/2025/hash/dbdb2729f874e209b56ffecd23aa3b36-Abstract-Conference.html), ICLR 2025 | score·noise의 기하적 phase 선행. |

**사용상 주의.** 주변 후보 7–11의 원문 세부, 특히 R11의 formal assumptions는 추천 세 방향보다 덜 검증됐다. 이를 바탕으로 주제를 확정하기 전 가정과 발표 상태를 재확인해야 한다. 이 보고서의 모든 실험·기여 설명은 사전 연구 판단이며 실제 발견으로 취급해서는 안 된다.
