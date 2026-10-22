# 판정 기각

**판정 대상:** 기존 보고서가 후보5에서 제안한, 초기 full-rank target의 약한 구분이 teacher feedback으로 교정/고착되는 경계를 작은 prediction/EMA 모형에서 발견하여 독립 연구로 삼는 계획. **이 형태로 연구 착수를 권하지 않는다.** 불완전한 teacher를 이용한 모든 비선형·계층 학습이 불가능하다는 판정이 아니다.

## 결정적인 근거

1. **직접 선행과 정확히 같은 방정식.** Tian, Chen, Ganguli (ICML2021) Lemma1 Eq2–4에 X=rho, X+X0=1, alpha_p=1을 대입하면 이번 student–predictor–teacher population flow와 동일하다. 따라서 weak positive init→collapse/recovery 및 EMA·weight decay의 역할은 용어만 바꾼 새 원리가 아니다.
2. **직접 증명과 실행이 기존 설명을 지지.** theory.md 명제3–4의 roots s± 및 Jacobian을 도출했고 72 primary+108 조건외 확인에서 max equilibrium error5.18e−9/8.64e−10이었다. eta>0의 고착과 eta=0의 느린 회복을 구별했다. numerical evidence는 exact statement의 검산이지 theorem 증명 대체가 아니다.
3. **교정이라는 말의 정보적 모호성.** teacher amplitude가 작거나 rank condition이 나빠지는 것만으로 finite-time 정보가 사라지지 않는다. exact Bayes refresh·20개 full-rank basis controls가 보여주는 차이는 conditioning/readout·asymptotic limit이다. target scaling을 오류라고 부르려면 probe/noise/precision/task 기준이 추가로 필요하다.

## 살려보려 한 수정과 결과

| 수정 | 실제 분석·실행 | 그래도 진행하지 않는 이유 |
|---|---|---|
| frozen 대비 EMA만의 차이를 찾음 | 동일 full-rank init에서 frozen positive vs EMA→0, exact interval eta/rho<s0<s− | 알려진 weight-decay/predictor basin으로 완전히 설명 |
| weight decay 제거 | 모든 balanced positive init의 회복 증명, tiny init escape time 계산 | 안정적 고착 대신 알려진 느린 초기 학습 |
| EMA 시간척도로 경계 이동 | Jacobian36개, beta의 고정점 안정성 부호 독립 증명 | 이 모형에서는 시간만 바뀜; 새로운 boundary 아님 |
| raw context에서 정보 복구 | E[BY|S]=B E[Y|S], nonorthogonal B20개 검산 | invertible target 변형이면 population 정보 동치, 단순 regression 성질 |
| normalization으로 mode 보존 | global norm은 power iteration, coordinate whitening은 두 mode 보존 | PCA/whitening과 기존 selfdistillation 해석에 가까움 |
| hierarchical target로 확장 | Korchinski2026 §5 A1/A2/C.3/D 원문 비교 | 기존 phase/latent trace를 넘는 새 명제는 아직 없음; core hypothesis 자체 미검증 |

## 독립 검토 대응

review/target-correction/review.md의 reviewer가 선행 동등성과 3D Jacobian을 별도 계산으로 확인했다. finite-state generic rank1 projection도 여러 상태에 injective할 수 있다는 반론을 수용한다. 본 결과는 coordinate-wise zero limit와 finite-time invertibility만 주장하며 일반적인 'rank 감소=정보 소실'을 주장하지 않는다. 아주 느린 teacher가 finite horizon에 평형에 도달하지 않을 수 있음을 RESULTS.md에 반영했다.

## 남은 문제와 재개 조건

Nonlinear hierarchical prediction에서 관측정보를 동일하게 맞추고도 생기는 teacher-specific 오류 안정성은 여전히 별도 문제다. 하지만 이것이 실질적인 새 문제라는 직접 근거를 확보하지 못했다. 현재 확보한 결과로 '수정 후 진행'이나 논문 초안을 만들면 핵심 검증을 빈칸으로 둔 셈이다.

재개하려면 적어도 다음이 먼저 필요하다: (a) full-rank amplitude/basis를 넘어선 의미 있는 target 오류 정의, (b) 기존 conditional-expectation/spectral/Tian dynamics가 같은 예측을 주는데 실제로 교정 여부는 다른 최소 사례, (c) task signal·view information·capacity·normalization·optimizer에 의한 대안 설명을 배제한 명제. 이 결과가 없으면 큰 모델이나 teacher rule sweep를 먼저 시작할 이유가 없다.

## 신뢰 범위

기각의 신뢰도는 **현재 간결한 정식화의 중복에 대해서 높음**. 전체 비선형·계층 연구 가능성은 **미판정**. 수치 확인은 합성 population dynamics에 한정하고 실제 DINO/JEPA의 학습 결과로 확대하지 않는다. 본 저장소의 증명·코드·결과는 사용자가 같은 중복과 측정 함정을 다시 밟지 않도록 하는 완성된 사전연구 결과다.
