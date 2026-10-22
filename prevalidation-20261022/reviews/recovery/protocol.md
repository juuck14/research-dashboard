# 후보1 독립 검토 — 실행 전 설계

작성 2026-10-22 UTC, 담당 recovery_review. 주제 담당자의 코드·결과를 아직 읽기 전에 작성했다. 검토자는 주제 담당 디렉터리를 수정하지 않는다.

## 검토할 주장

1. 회복 지연 또는 checkpoint reset의 성공만으로 SSL 고유의 정보 고착을 입증할 수 있는가?
2. 직접 선행연구의 정리가 실험의 가능한 경쟁 설명을 이미 포함하는가?
3. equilibrium의 안정성 주장이 출력 좌표계의 연속 대칭을 제대로 처리하는가?

## 문헌 확인

원문 우선: Tian–Chen–Ganguli ICML2021 Lemma1/Eq2–4, Saxe et al. ICLR2014 §2 mode flow, Lee et al. ICLR2026 §3.2/AppF Fig15, Ponce et al. arxiv2507.01028v3 §4/Prop4.10. 문헌 주장과 검토자의 수학적 반론을 구분한다.

## 독립 계산 A — 출력 대칭과 안정성

선형 BYOL population flow를 직접 작성한다. X marginal covariance I2, cross-covariance diag(.8,.6), output dimension3, alpha_p=1, weight decay .02, EMA rate .2. 큰 양의 scalar root를 두 factor에 배치한 exact equilibrium을 사용한다. Seed 2718에서 생성한 skew-symmetric matrix의 exponential로 출력 전체를 회전한다. A,C→QA, B→QBQᵀ를 적용한다.

확인: 원래와 회전 equilibrium vector field norm <1e−10; flow equivariance <1e−10; rotational tangent의 Jacobian action norm <1e−7. Finite-difference steps 1e−4,1e−5,1e−6를 모두 쓴다. 이것은 명시적 정리의 논리적 검산이지 데이터 기반 신규 연구결과가 아니다. 표준 gauge symmetry를 새로운 기여로 제안하지 않는다.

## 독립 계산 B — conditioning만으로 생기는 회복 지연

Balanced scalar SG/no-decay BYOL의 정확한 모형 dot s=s²(rho−s), rho=.8. 입력 correlation은 모든 비교에서 동일하다. 초기값 .001,.003,.01,.03,.1에서 threshold s=.4에 도달하는 시간을 SciPy solve_ivp event로 구하고 직접 적분식과 비교한다. 제3자가 확인할 수 있도록 식과 오차를 기록한다. 테스트 범위는 실행 결과에 맞춰 변경하지 않는다.

반증 기준: 해석식–ODE event 상대오차 >1e−5이면 구현 또는 도출 재검토. 정확히 일치하면 '회복 지연=새 SSL 현상'이라는 약한 설명을 기각하는 대조군일 뿐 비선형 전체를 기각하지 않는다. 단일 작은 모형의 회복시간은 실제 모델에 대한 검증된 설명이 아니다.

## 후속 독립 검토

주담당 결과가 생성되면 gradient finite difference, raw marginal invariance, matched informative exposure, encoder/head/EMA/optimizer 개입 정의, holdout seeds, 조건수·fixed-noise readout과 정보 소실의 구별을 확인한다. 실행 전 amendment를 추가하고 별도 코드로 확인한다.

## Amendment 1 — pilot 이후 대안 설명의 직접 검증

주담당 pilot를 읽은 뒤 작성했다. 4seed 모두 deficit 후 낮은 factor3 접근성이 관측됐으나, clean rho 세 개가 같으면 학습 목적이 factor allocation에 무관한 stationary family를 갖는다는 대안이 발견됐다. 이 대안은 원래 protocol의 경쟁 설명을 구체화한다. 새로운 결과를 탐색한 뒤 사전 계획이었다고 주장하지 않는다.

독립적인 8state cosine objective를 작성하고 v=(sqrt((1−a²)/2),sqrt((1−a²)/2),a), a∈{0,.001,.1,.5,.9}를 평가한다. equal rho=.9에서는 loss=.2 및 모든 lookup/predictor gradients=0. rho3∈{.8,.9,1}에서는 a=b=0 stationary의 student/teacher tangent Jacobian [[−2rho0,2rho3],[beta,−beta]]를 중앙차분으로 검산한다. beta=.01, finite difference h∈{1e−3,1e−4,1e−5}. Predictor unused direction p3∈{.8,1,1.2}일 때 첫 행은 [−2rho0 p3²,2rho3 p3]라는 확장도 동일 grid로 확인한다.

주담당 backprop는 seed{901,902,903}, deficit/clean 및 비동일 rho=(.8,.9,1)에서 독립 중앙차분으로 검산한다. 주담당의 check()는 호출하지 않는다. 상대/절대오차 max<1e−6을 요구한다. 결과는 모델 가정 아래 표준 spectral explanation의 타당성만 검증하며 일반 SSL memory의 부재를 주장하지 않는다.

## Amendment 2 — contrastive 경쟁 설명 검산

주담당 InfoNCE 대조 결과가 생성된 뒤 독립 검토를 설계했다. 새 generator나 유리한 training seed를 찾지 않는다. normalized diagonal family의 모집단 loss와 simplex convex 해를 별도로 검산한다. tau1, w=(.5,.5,0), (1/3,1/3,1/3), (.7,.2,.1), (.01,.01,.98), clean(.9,.9,.9)/deficit(.9,.9,0)를 사용한다. 독립 loop law 및 직접 negative expectation과 log-cosh식을 비교한다. 또한 seed1901/1902에서 MLP InfoNCE gradient를 독립 finite-difference loss로 확인한다. 기대 허용오차 loss1e−12, gradient1e−6. 이 대조는 objective 전체가 달라지므로 특정 teacher/optimizer state의 인과 효과로 해석하지 않는다.
