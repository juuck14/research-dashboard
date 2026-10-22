# 실행 전 설계 — 후보 1

작성 2026-10-22. 아래 설정은 결과를 보기 전에 고정했다. Pilot와 confirmation을 구분하며 변경은 하단에 추가한다.

## 질문과 판정

초기에 한 factor의 cross-view 관계만 없앤 뒤 관계를 회복시킬 때, BN·LR schedule·표본 노출과 무관한 회복 지연이 생기는가? 생긴다면 EMA lag, predictor, optimizer state 중 어느 개입이 차이를 설명하는가? 이는 현재 특정 작은 모형의 질문이며 SSL 전체에 대한 불가능성 주장이 아니다.

진행에 필요한 것은 (a) deficit 이후 clean-from-scratch보다 늦은 학습, (b) 독립 seed와 설정에서 같은 원인의 재현, (c) 기존 Tian2021 mode/basin 또는 표준 optimizer conditioning을 넘는 정량 예측이다. (a)만 관측하거나 reset 표만 남으면 독립 주제 진행을 권하지 않는다. (a)가 없으면 이 구체화는 반증이다. (c)가 미검증이면 진행 권고로 올리지 않는다.

## 관측·숨은 대상·범위

- X,Y는 {-1,+1}^3. P(X)=P(Y)=uniform, P(Y|X)=prod_j(1+rho_j X_jY_j)/2. 학습기는 pair law만 사용한다. factor label은 평가·진단에만 사용한다.
- Deficit rho=(.9,.9,0), 이후 clean=(.9,.9,.9). 각 raw view에 세 bit는 항상 존재한다. 변화하는 것은 pair 관계다. finite 8x8 law를 정확히 합산하므로 finite-sample 부족·augmentation sampling 잡음은 없다.
- Encoder f(x)=tanh(x W1) W2, W1 3x12, W2 12x3, bias 없음. Predictor P 3x3. 출력과 예측을 row unit normalize해 BYOL류 cosine regression을 수행한다. teacher는 encoder parameter EMA. BN 없음, weight decay 없음, 일정 LR .003. 표준 BYOL 전체를 대표하지 않는다. bias 제거로 상수 output collapse 경로를 제한하며 그 제한을 결과에 명시한다.
- 같은 해는 output의 공통 orthogonal 변환으로 보며, 평가 값은 이에 불변이다. 작은 nonzero signal을 noiseless 정보 소실로 부르지 않는다.
- 직접 추적하는 것: normalized encoder 및 teacher의 factor Walsh sensitivity, fixed additive readout noise sigma=.1 아래 population 최적 linear R², loss, gradient norm, 각 parameter block의 실제 update norm, teacher-student 출력 거리.
- R²는 제한된 noisy linear 접근성이다. exact mutual information이나 모든 decoder의 정보 부재가 아니다.

## 비교·초기 설정

Pilot seeds 0,1,2,3; confirmation seeds 101,102,103,104는 별도. W1~N(0,1/sqrt(3)), W2~N(0,1/sqrt(12)), P=I+.05N. encoder/predictor를 같은 초기값으로 복제한다. deficit 1500 steps, clean continuation 3000; scratch는 같은 초기값에서 clean 3000; clean-from-start는 4500. Adam beta=(.9,.999), eps=1e-8.

동일 deficit checkpoint에서 continue, optimizer-only reset, teacher=current student, predictor=초기값, predictor+teacher, encoder+predictor+optimizer+teacher 전체 scratch를 비교한다. predictor reset은 encoder feature를 즉시 바꾸지 않는다. optimizer reset에는 추가로 매 block update norm을 reference continue의 같은 step 값에 맞춘 control을 둔다. 일정 LR이므로 LR restart와 continue는 동일하다. 모든 continuation은 같은 informative pair law·update 수를 쓴다.

Recovery time은 factor3의 noisy linear R²가 scratch clean 3000step 값의 90%에 도달하고 다음 두 평가시점에도 유지되는 첫 step이다. 80%와95%도 보고하고 censoring을 무한 회복불능으로 해석하지 않는다. 평가 매50step, raw curve 보존. clean-from-start는 전체 학습시간 통제이며 scratch는 informative exposure 통제다.

## 검산·경쟁 설명

실행 전 analytic backprop를 중앙차분(고정 teacher)으로 점검한다. 모든 pair law marginal·correlation을 직접 검산한다. BN와 finite-sample 부족은 설계상 없다. Adam reset의 효과가 norm-matched에서 사라지면 scalar step size가 우선 설명이다. teacher sync 효과가 EMA 반감기 수준에서만 지속되면 lag 설명이다. 어떤 개입도 고유한 memory location을 증명하지 않으며 충분한 조작이라는 의미만 갖는다.

## 변경 기록

### Amendment 1 — Pilot 후, 추가 결과 전

Pilot4seed에서 deficit 후 factor3 접근성이 작고 reset도 회복하지 않았다. 그러나 이것이 학습 상태의 새로운 고착이라는 설명보다 강한 경쟁 설명이 있다: clean의 세 primitive eigenvalue가 같아 cosine agreement가 rank별 allocation을 선호하지 않을 수 있다. 이를 직접 검증한다.

1. 원래 confirmation seeds101–104는 설정을 바꾸지 않고 실행한다.
2. 정확한 lookup f_v(x)=diag(v)x/||v||, teacher=f_v, predictor=I에서 v3=0부터 fullrank까지 stationary인지 직접 미분·계산한다. 이론상 equal rho=.9에서는 모두 stationary일 것으로 예상한다. 이 계산을 새로운 결과로 포장하지 않고 spectral indifference 대안설명의 통제로 쓴다.
3. clean rho3=.8/.9/1.0, 다른rho=.9를 고정해 신호의 상대 고유값만 바꾼다. fixed predictor I·tied teacher에서는 normalized diagonal flow의 v3²가 logistic law du/dt=4(rho3−.9)u(1−u)를 따를 것으로 예상한다. EMA의 missing-mode 선형화는 [[−2r,2s],[beta,−beta]]가 될 것으로 예상하며 수치 Jacobian으로 검산한다. 이 제한 모형의 결과를 nonlinear network 전체 정리로 전이하지 않는다.
4. Neural 추가 control은 같은 checkpoint에서 rho3=.8/1.0을 informative3000steps와 확장15000steps로 비교한다. Primary seed0–3, 확인101–104. 긴학습을 해도 censoring은 불가능성으로 해석하지 않는다.
5. Reviewer 지적에 따라 predictor parameter reset과 함께 predictor-specific Adam m/v도 reset한 control을 추가한다。다른 parameter optimizer는 유지한다. 원래 reset은 stale-moment mismatch를 포함하는 개입임을 명시한다. 전체 Adam t를0으로 바꾸면 encoder biascorrection도 바뀌므로 해당 control에서는 perparameter Adam t를 별도로 관리한다.

판정 기준은 유지한다. 원래 뚜렷한 deficit가 objective의 flat optimum·표준 spectral selection으로 설명되면 새로운 causal lock 기여로 인정하지 않는다. 더 유리한 rho3에서만 회복해도 원설정의 성공으로 바꾸어 세지 않는다.

### Amendment 2 — 대조 학습기의 복구 구동력 검증, 실행 전

Flat agreement만으로 원래 넓은 회복 질문을 기각할 수 없다. 같은 nonlinear encoder·같은 exact law·동일 Adam/LR/exposure에서 population infinite-negative InfoNCE(temperature1)를 별도 비교한다. teacher/predictor는 없다. 이는 단일 state의 인과 효과가 아니라 목적함수의 선택압 유무를 검증하는 비교다. 8seed 모두 deficit1500 및 clean continuation3000을 실행하고, 15000까지 같은 설정으로 연장한다. 처음부터 clean3000 baseline도 둔다.

전제 분석: f_v(x)=diag(v)x, w_j=v_j², sum w=1에서는 L=−sum rho_j w_j/tau + sum log cosh(w_j/tau). equal clean rho와 tau1에서는 strictlyconvex uniformity가 유일한 w=(1/3,1/3,1/3)을 선호한다. deficit rho3=0에서는 w=(1/2,1/2,0)이 최적이다. 따라서 같은 generator에서도 contrastive objective에는 factor3 재획득 구동력이 있고 agreement에는 없다. 이 계산과 neural 결과가 부합해도 새로운 원리가 아니라 원래 해석에 대한 경쟁 설명이다. code gradient는 중앙차분으로 별도 확인한다.

### Amendment 3 — 원래 equal-spectrum의 유한시간 범위, 실행 전

3000step 원래 setting의 낮은 결과를 장기 불가능성으로 읽지 않도록, 모든8seed의 원래 equal-clean continue를15000step까지 일괄 확장한다. 동일 checkpoint·동일 optimizer·EMA·LR을 유지한다. rho3=.8 neural대조의 seed101에서 회복이 관측되어 작은 fixed-head linearization의 부호가 전체 MLP 회복의 필요충분조건이 아님도 이미 확인했다. 이 예외와 확장결과 모두 보존한다.

저장 방식 변경(수치결과 불변): full trace는 scratch 외부 경로와 SHA256으로 기록하고 실행코드가 재생성한다. 저장소에는 모든run의 고정500step간격+마지막값 CSV 및 모든run의summary/threshold를 남긴다. outcome에 따른 대표seed선택은 하지 않는다. 50step 회복시간의 원자료는 fulltrace에 있다.
