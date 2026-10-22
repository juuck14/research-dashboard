# 세 연구 방향의 착수 판단을 위한 실제 사전 연구

기준일 2026-10-22. 기존 보고서의 추천을 그대로 유지하지 않는다. **부분 식별과 자기 target 교정은 현재 구체화한 독립 주제로서 기각한다. Negative 선택은 원래 설명을 반박한 뒤, 정규화된 표현에서 적응 sampling이 요인 균형을 불안정하게 만드는 문제로 수정해 진행할 가치가 있다.** 투고할 논문의 독창성과 실제 자료에서의 중요성까지 확정한 것은 아니다.

## 최종 비교

| 주제 | 최종 판정 | 가장 강한 증거 | 아직 주장할 수 없는 것 | 직접 착수한다면 첫 작업 |
|---|---|---|---|---|
| 근사 가정 아래의 부분 식별 | **기각: 현재 Gaussian 중심 구체화** | 동일 관측법칙 대안·정확한 제한 모형 식별집합·표본 무관 하한을 증명했으나 기존 AJD contrast와 정확히 환원 | 일반 비선형 부분 식별이 불가능하다거나, 이번 회전 집합이 모든 모형의 exact set라는 주장 | 새 비선형 현상 또는 정직한 confidence target이 없으면 착수하지 않음 |
| Negative 관계와 피드백 | **수정 후 진행** | 무제약 원가설 반증; 정규화된 충분 차원에서 matched-frozen 안정/adaptive 불안정의 전체 국소 spectrum 증명; 다중 negative·3요인·positive 변형·SGD 확인 | 모든 SSL의 정보 소실, 실제 filtering 알고리즘의 실패, 자연 이미지 성과, 완성된 신규성 검증 | 현재 증명·코드 재현 후 실제 filtering 규칙과 일반 K의 mode 조건을 연결 |
| 불완전한 자기 target 교정 | **기각: 현재 선형 자기증류 구체화** | 도출한 ODE가 Tian–Chen–Ganguli2021 Lemma1의 정확한 특수 경우; 고정점·회복/고착·EMA 통제 실행 | 모든 비선형·계층적 자기교정의 불가능성 | 기존 conditional expectation·spectral/Tian 설명이 같은데 교정 여부가 다른 최소 사례가 먼저 필요 |

## 조사와 검증의 구성

세 독립 담당이 원문·정식화·증명·실험을 수행하고, 다른 세 담당이 각 주제의 논리와 코드를 공격했다. 별도로 negative 신규성 검토자는 performative prediction·self-paced learning의 경쟁 설명을 조사했다. Root는 세 요인 확장, 비동일 positive 채널, 실제 minibatch SGD를 사전 조건을 적은 뒤 실행했다. 기록의 `직접 증명`, `수치 확인`, `외부 문헌`, `추측`은 구별했다.

원래 저장소에는 README만 있었다. 그 지침에 따라 주제별 디렉터리와 최신 README를 만들었다. 기존 Pages 보고서의 snapshot, 실행 전 protocol, 수정 이유, 코드, 작은 원자료, 그림, 독립 반론을 보존했다. GPU나 대형 데이터가 필요한 주제를 원칙적으로 배제한 것은 아니다. 이번 판단에는 정확한 경쟁 설명을 분리할 수 있는 작은 모형이 더 정보량이 높았다.

## 1 부분 식별에서 실제로 얻은 것

관측 환경 두 개를 `X|e=0 ~ N(0,I)`, `X|e=1 ~ N(0,diag(1+gamma,1−gamma))`로 고정했다. 기준환경에서 **소스 covariance까지 정확히 I라고 신뢰하는 제한 모형**에서는 모든 orthogonal 회전이 동일 관측법칙의 대안 생성모형이 된다. 좌표의 순서·부호 차이는 같은 해로 인정하지만 두 소스를 섞는 일반 회전은 다른 해석으로 본다.

소스 독립성의 허용 편차를 환경별 최대 total correlation `max_e KL(P(S|e) || product_i P(S_i|e)) ≤ delta`로 정의했다. 이 척도는 각 소스 좌표의 가역 재매개화에 불변이다. 회전각 theta에 대한 직접 완전 증명은 다음 식을 준다.

`TC(theta) = 0.5 log[1 + gamma² sin²(2theta)/(1−gamma²)]`.

이에 따라 true axis에서 허용되는 반지름은 `theta_max = 0.5 asin(min(1,sqrt(expm1(2delta)(1−gamma²)/gamma²)))`다. 부호와 순서를 quotient해도 +theta와 −theta는 일반적으로 다른 해여서 signed arc를 고려해야 한다. 표본을 아무리 늘려도 동일 law의 두 대안을 구별할 수 없고, 임의 estimator의 두 대안 중 큰 angle risk는 적어도 theta_max/2다. 유한 개 환경과 양의 delta에서는 임의의 두 축을 조금 섞는 회전이 허용되므로 별도 exact block 제약 없이 정확한 proper group을 보존한다는 주장도 성립하지 않는다.

직접 실행: 41개 population oracle 조건, 9개 3D 예시, 360개 표본 반복. 식과 covariance 계산의 최대 차이는 2.50e−16이었다. 독립 검토는 다른 seed의 400조건에서 3.11e−15 이내로 일치했다. 예를 들어 delta=.001에서 gamma=.03이면 허용 반지름이 45°이지만 gamma=.3에서는 약4.09°다. 이는 구조 오차와 표본오차를 분리하는 실제 예시다.

그러나 이 결과만으로 독립 논문을 권하지 않는다. Gaussian 환경평균 TC는 [Ablin–Cardoso–Gramfort2018 Eq(1)](https://arxiv.org/html/1811.11433v1)의 기존 joint-diagonalization contrast와 정확히 같다. 그 논문의 Hessian과 기존 이분산 source/SVAR 식별 이론이 방향별 conditioning을 이미 다룬다. 정확한 2D 식과 two-point 하한은 유용하지만 새로운 학습 원리를 확보한 것은 아니다.

독립 검토에서 두 오류 가능성을 수정했다. 첫째, **관측 whitening만으로 소스 whitening을 정당화할 수 없다.** 일반 GL mixing에는 이번 orthogonal 집합이 exact identified set가 아닌 feasible alternatives와 ambiguity lower bound다. 둘째, 환경별 max 예산과 확률가중 평균 예산은 다른 문제다. rare environment를 두면 같은 수치에서 허용각이 5.462°와45°로 달라졌다. 상세 반례는 [독립 검토](../review/partial-identification/review.md)에 있다.

살려본 수정은 방향별 집합, group 식별, seed stability 진단이었다. 각각 기존 sensitivity, 작은 cross-block rotation, 관측 동치의 직접 결과를 벗어나지 못했다. 일반 비선형 identified set나 정직한 finite-sample inference는 여전히 미해결이지만, 그 핵심 결과가 없는 상태를 긍정적 논문 초안으로 포장하지 않았다. [주제 판정과 재개 조건](../partial-identification/verdict.md).

## 2 Negative 주제의 원가설은 어떻게 바뀌었는가

원래 질문은 현재 유사도로 negative를 덜 고르면서 특정 요인을 영구적으로 못 배우는 안정점이 생기는가였다. 먼저 독립 두 bit `x=(a,b)`와 positive가 같은 요인을 보존하는 무제약 `f=(w1*a,w2*b)`를 분석했다. q에 항상 양의 확률 하한이 있고 sampler를 stop-gradient로 쓰면 누락 요인 방향의 작은 신호는 증가한다.

직접 증명한 국소 성장률 하한은 epsilon/2이고, `0<w2≤d`에서 `d log(w2)/dt ≥ epsilon sigmoid(−2d²)`다. 따라서 양의 작은 초기값에서 정한 크기까지 탈출하는 유한 시간 상계가 있다. 1,080개 exact population 설정/초기값을 계산했고 모두 그 범위에서 탈출했다. 이 숫자는 독립 dataset의 성공 확률이 아니다. 약99배 늦은 회복은 있었지만 frozen 정책도 비슷하게 늦췄다. 학습 지연을 영구적 고착 또는 피드백 고유 효과라고 부를 수 없었다.

### 수정한 연구 질문

**충분한 표현 차원과 full-support sampling이 있어도, unit-norm 표현에서 negative 분포의 적응적 반응이 두 요인을 보존한 평형의 안정성을 바꾸는가?**

원가설을 살리기 위한 임의 튜닝이 아니라, unnormalized 증명의 전제인 자유 norm 증가가 normalized representation에서는 허용되지 않는다는 구체적 이유로 정식화를 바꿨다. 이 변경은 protocol의 후속 amendment에 실행 전에 남겼다.

네 상태 각각에 독립적인 unit vector를 허용하는 full lookup `f_i ∈ S^(d−1), d≥3`를 썼다. 네 상태를 모두 구별하는 tetrahedron도 가능하므로 차원 부족이 아니다. 현재 표현에 따른 sampler는 `q_F(j|i)=epsilon/4+(1−epsilon)softmax_j(kappa f_i·f_j)`이며 kappa<0가 유사한 negative를 덜 고르는 soft filtering이다. Positive law는 정책 비교마다 동일하다. 동일 평형에서 q를 고정한 matched-frozen control과 매 step q를 갱신하는 detached update를 비교했다.

### 핵심 명제와 실제 증거

Square `f_i=(a_i,b_i,0,…)/sqrt(2)`는 두 갱신 모두의 평형이다. 모든 tangent 방향을 binary group Fourier mode로 분해하여 전체 국소 spectrum을 완전 유도했다. 이때 `alpha=1/(2+2cosh(kappa))`, `c=1−epsilon`, `v=epsilon/4+c*alpha`, `w=epsilon/4+c*exp(−kappa)*alpha`, `r=sigmoid(−1)`, `s=sigmoid(−2)`라고 하자.

- Frozen square의 회전 제외 안정성 조건: `w*s > v*r`.
- Adaptive의 요인 균형 방향 불안정 조건: `v*r*(1−r)+c*kappa*alpha*r < 0`.

epsilon=.1,kappa=−2는 두 조건을 만족한다. d=4의 full tangent에서 frozen 최대 비회전 flow 고유값은 −.04698798, adaptive는 +.05466566이다. 음수는 작은 perturbation의 수축, 양수는 증가를 뜻한다. 제안자와 독립 검토자가 서로 다른 코드로 확인했고 나머지 tangent 방향과 전역 회전의 zero modes까지 셌다. 단순 1차원 angle 제한에서만 나타난 현상이 아니다.

| 추가 검증 | 실제 결과 | 근거의 범위 |
|---|---|---|
| Negative 수 K=1,2,4,8,16 | 105개 exact multinomial 조건; 주요 설정에서 frozen 곡률 양수, adaptive 음수 유지 | K≤16 factor-balance mode; K2/K4 full tangent는 독립 확인. 모든 K full spectrum 정리는 없음 |
| Anchor 자신의 상태 제외 | 3개 negative 모두 양의 확률인 d4 모형에서도 부호 전환 | Self-negative 포함의 artifact가 아님 |
| 세 요인·8상태, d=8 | epsilon=.1,kappa=−2에서 frozen −.01238159, adaptive +.02590878 | 사전 grid와 추가 step·좌표회전 검산; 일반 m 정리 아님 |
| 비동일 positive | 각 bit flip eta=.001,.01,.05,.1에서도 frozen 안정/adaptive 불안정. eta=.1에서 −.08697142 vs+.03214919 | Positive channel full-rank; 자연 영상 augmentation을 대표한다고 주장하지 않음 |
| 실제 minibatch SGD | batch64,lr.1,6000steps,primary6+confirmation4 seeds. 세 정책 총30실행 | Toy lookup·identity positives에서의 확률적 학습; 이미지 일반화 아님 |
| 고정 noise 아래 Bayes readout | sigma=.05에서 uniform/frozen의 관측 worst-factor accuracy1.000, adaptive .4934–.4984 | 학습 probe 한계가 아닌 명시된 noisy representation의 접근성. 유한시간 noiseless MI 소실은 아님 |
| Importance correction | 90 exact 조건 최대 차이1.39e−15로 uniform population field 복원 | 동일 원래 목적함수의 순수 optimizer failure라는 해석은 제외 |

Positive-noise Jacobian과 SGD는 별도 실험이다. SGD에서 positive noise까지 동시에 사용한 결과는 없다. 그림과 원자료는 [추가 검증](../review/robustness-extension/README.md)에 연결돼 있다.

### 무엇이 새 기여 후보이고 무엇은 아닌가

`DG = frozen Hessian + sampler response`는 곱의 미분이며 [Perdomo et al.2020](https://proceedings.mlr.press/v119/perdomo20a/perdomo20a.pdf)의 performative prediction 구도와 연결된다. 쉬운 표본의 가중치를 높이며 곡률을 바꾸는 것은 [self-paced implicit regularization](https://arxiv.org/pdf/1606.00128)의 경쟁 설명도 있다. 그러므로 '적응 분포는 고정 분포와 다르다'는 일반론을 새 원리로 주장하지 않는다.

[Robinson2021](https://arxiv.org/pdf/2010.04592), [Jiang et al.의 hard-negative geometry 연구](https://arxiv.org/html/2311.05139v3), [SnaPhArd ICLR2026](https://proceedings.iclr.cc/paper_files/paper/2026/file/42a24a7a3e7cf7dd127a76daf487cffd-Paper-Conference.pdf)도 직접 대조했다. 마지막 논문의 fixed-key anchor alignment를 global factor collapse와 동일시하지 않았다. 현재 기여 후보는 **충분한 차원·양의 sampling floor 아래, contrastive 요인 균형의 정확한 전체 spectrum과 그 예측력**이다. 문헌 차이가 실제로 필요한 새로운 결론을 만들었는지에 대한 최종 학술적 평가는 여전히 위험하다.

특히 kappa=−10에서는 factor-balance mode가 다시 안정해질 수 있다. 'filtering이 강할수록 언제나 나쁘다'는 단조 주장은 반박됐다. 현재 결과는 특정 phase window를 말한다. 또한 작은 비영 amplitude에는 noiseless 정보가 남을 수 있으므로 정보 소실·접근성·metric를 구분했다.

### 검토자 간 이견과 종합 판정

담당자와 full-tangent 검토자는 수정 후 진행 의견이다. 별도 신규성 검토자는 초기 sign flip만으로는 performative/self-paced의 작은 예제일 수 있으므로 진행 권고에 신중했다. Root는 그 반론 이후 세 요인·비동일 positives·실제 SGD를 추가 확인했다. 이 결과는 일부 artifact 반론을 해결하지만 자연 정책에서의 중요성을 증명하지는 않는다.

종합 판정은 **수정 후 진행**이다. 연구 착수 가치의 근거는 이미 존재하는 정확한 명제와 여러 독립 확인이며, 새로운 mining 모듈을 만들어 성능을 올리자는 제안이 아니다. 다만 지금 바로 투고 가능한 독창성을 확정했다는 판정은 내리지 않는다. [실제 결과 기반 논문 초안](../negative-feedback/paper_draft.md), [이론](../negative-feedback/theory.md), [독립 비판](../review/negative-feedback/review.md), [신규성 반론](../review/negative-novelty/review.md)을 함께 읽어야 한다.

## 3 자기 target 교정의 기각 근거

먼저 full-rank target의 conditional-expectation 반복을 계산했다. 양의 informative mode가 유한시간에는 남아 있으면 invertible한 좌표 변형이며, amplitude 감소만으로 noiseless 정보가 소실됐다고 말할 수 없다. 일반 finite-state에서는 rank1 projection도 여러 상태를 모두 구별할 수 있다는 반례도 실행했다.

그다음 student–predictor–EMA teacher의 scalar population ODE를 직접 도출했다. 그러나 [Tian, Chen, Ganguli2021 Lemma1 Eq2–4](https://proceedings.mlr.press/v139/tian21a/tian21a.pdf)에 `X=rho`, `X+X′=1`, `alpha_p=1`을 넣으면 정확히 같은 방정식이다. Weak full-rank initialization에서의 collapse·회복, weight decay와 predictor basin은 이미 선행 범위에 포함된다.

72개 primary 및108개 별도 조건에서 고정점 예측 최대오차는5.18e−9 및8.64e−10이었다. Jacobian36개, fixed predictor54개, full-rank basis20개를 검산했다. Independent reviewer는54 고정점을 별도 코드로 확인했다. 같은 초기값에서 frozen은 유지되고 EMA는 감소하는 실제 예시도 있지만, 이미 알려진 basin으로 정확히 설명된다. Frozen t1500 관측 .0314034와 점근 예측 .0310029를 구별했고 finite-time 정확해 오차1.78e−11을 확인했다.

Weight decay를 없애면 작은 양의 초기값이 영구적으로 갇히는 대신 느리게 회복했다. 초기신호 .001/.003/.01에서 회복시간은 약1257.8/421.7/126.9였다. 이 차이를 새 오류 고착으로 부르지 않았다. 최근 [Korchinski et al.2026](https://arxiv.org/abs/2605.27734)의 phase별 latent target 분석도 대조했으나, 그것을 넘는 비선형 자기교정 명제는 확보하지 못했다.

현재 정식화는 기각한다. 다시 시작하려면 amplitude·basis conditioning을 넘어선 target 오류를 정의하고, 기존 conditional expectation·spectral·Tian dynamics가 같은 예측을 주는데 실제 교정 여부가 다른 최소 비선형 사례가 먼저 필요하다. [판정·수정 시도·재개 조건](../target-correction/verdict.md).

## 다음 착수 순서

1. **Negative 수정 주제만 우선 재현한다.** full-sphere 명제와 matched-frozen control, importance correction부터 읽고 코드 결과를 확인한다. 자연 이미지 성능 개선을 첫 성공 기준으로 잡지 않는다.
2. **일반 K의 전체 mode와 실제 filtering 규칙을 연결한다.** 현재 soft exponential filtering의 명시적 임계식이 실제 threshold/learned filtering에서 어떤 사전 예측을 주는지 한 규칙으로 검증한다. 기존 performative sensitivity bound의 즉각적 적용만으로 끝나면 독립 주제로 접는다.
3. **비대칭 요인과 일반 encoder를 좁게 확인한다.** 현재 대칭 lookup에는 정확해가 있다. 요인 빈도나 positive 채널을 한 축만 바꾸었을 때 평형과 spectrum 이동을 먼저 예측하고 확인한다. 실험 뒤 그럴듯한 설명을 붙이지 않는다.

부분 식별과 teacher 주제는 현재 기각 노트를 남기고 멈추는 것이 낫다. 더 큰 실험이나 복잡한 구현으로 신규성 문제를 해결하려 해서는 안 된다. 이는 원래 넓은 분야 전체의 부정이 아니라, 이번에 검증한 연구 출발점의 판정이다.

## 재현성과 보존

모든 연구 파일은 [research-dashboard](https://github.com/juuck14/research-dashboard)에 있다. 각 주제 README에 최신 상태·protocol·code·results·문헌·판정을 연결했다. [실행 안내](reproduction.md), [환경](environment.json), [변경 이력](progress.md)을 함께 보존한다. 큰 데이터·원문 PDF·모델 checkpoint는 올리지 않았다. 외부 문헌과 직접 결과의 상세 출처·절·검증 범위는 각 literature.md 및 review에 있다.

원래 보고서의 1순위 추천과 teacher 주제의 낙관적 신규성 평가는 철회한다. 이번 연구의 긍정 결과는 좁혀진 negative 피드백 명제이며, 기각 두 건도 직접 증명·계산·선행 대조를 갖춘 완성된 사전 연구 결과다.
