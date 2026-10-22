# 후보1 독립 교차검토 — 현재 구체화 기각

검토자 recovery_review, 2026-10-22. 주담당과 별도 문헌 대조·수학 도출·실행 코드를 작성했다. 주담당 파일을 수정하거나 주담당 코드의 check()를 독립 검증으로 재명명하지 않았다.

## 판정

**이번 구체화로 독립 논문 착수는 권하지 않는다.** 회복 지연 현상은 실제이며 raw marginal·BN·LR schedule·유한표본의 일부 대안은 통제됐다. 그러나 무엇이 새로운 원리인지, 어느 상태량이 회복을 정량적으로 예측하는지는 확보되지 않았다. 현재 가장 강한 결과는 새로운 memory lock이 아니라 **복구를 요구하지 않는 objective와 긴 transient를 잘못 해석하면 안 된다는 반증**이다. 이 판정은 nonlinear SSL의 모든 이력 의존성·회복 문제를 기각하는 것이 아니다.

## 1. 직접 확인한 신뢰 가능한 증거

주담당의 8state law는 X,Y marginal을 uniform으로 유지하고 pair factor3 correlation만0→.9로 바꾼다. raw view에 factor3가 항상 있어 정보 자체의 부재와 training signal의 부재를 구별한다. exact population 합산이므로 표본 변동을 제거한다. tanh·bias-free·BN-free·weight-decay0·constantLR 범위는 제한적이지만 명확하다.

별도 law와 loss를 구현한 뒤 seed901/902/903와3개 pair law의 전 parameter 중앙차분으로 주담당 backprop를 검산했다. 최대 절대오차5.28e−10이었다. InfoNCE 코드도 별도 loss·seed1901/1902에서4.81e−11로 검산했다. 공통 코드의 반복 실행만으로 옳다고 판단하지 않았다. [실행 전 설계](protocol.md), [실행 결과](results/README.md), [원자료](results/spectral_audit.json), [contrastive 검산](results/contrastive_audit.json).

## 2. 결정적 대안 설명

equal clean rho에서는 normalized agreement가 모든 primitive mode allocation을 구별하지 못한다. rank1/rank2/fullrank f_v=diag(v)x가 모두 loss2−2rho의 전역 하한을 달성하고 exact stationary다. 독립 증명과5개 allocation의 수치 gradient 검산이 있다. 따라서 deficit 후 factor3가 돌아오지 않는다는 것만으로 별도 causal lock을 지지하지 못한다. [직접 증명](theory.md).

같은 diagonal family에서 population InfoNCE는 strictly convex log-cosh term으로 full allocation을 선호한다. 주담당의 실제 nonlinear8seed는50–250step 내90% threshold에 도달했고3000step factor3 R²는 모두약.970874였다. 이것은 목적함수의 복구 선택압이라는 경쟁 설명과 부합한다. 목적함수·teacher·head가 동시에 달라지는 비교이므로 teacher만의 인과 효과로 해석하지 않는다.

제한된 scalar teacher/head tangent의 안정성은 spectral gap과 dormant predictor gain으로 달라진다. 독립27조건 Jacobian 검산 최대오차1.20e−6. 그러나 rho3=.8의 neural seed101이15000step 뒤R²=.955865로 회복하므로 이 작은 모형을 실제 nonlinear 전 과정의 완전한 회복 법칙으로 올릴 수 없다.

## 3. 시간 범위와 예외를 숨기면 결론이 바뀐다

원래 equalrho continuation8seed의3000step final factor3 R² 범위는2.44e−8–.004242, 중앙값2.18e−6이다. 그러나 동일 설정을15000step까지 늘리면 seed0/1/101/104는.96575/.93843/.97603/.92312로 회복한다. 나머지4seed는4.19e−5이하다. **초기 관측을 영구 고착·정보 소실로 부르는 설명은 직접 반박됐다.** 낮게 남은 seed가 영원히 회복하지 못한다는 증거도 아니다.

reset도 '효과없음'으로 묶으면 안 된다. predictor reset과 head+teacher reset은 각각 최고.72207/.74470까지 부분 회복한 seed가 있다. 반면 predictor와 그 자체 Adam moments를 함께 초기화한 seed101은.04899였다. stale optimizer/head interaction이라는 대안과 큰 seed 의존성을 보존해야 한다. 충분한 개입과 고유한 memory location은 다르다.

scratch 초기부터 factor3 noisy linear R²가.377–.988로 높고, 일부 seed는 step0에서 recovery threshold를 넘는다. scratch final도 seed103에서는.30795에 그쳤다. 따라서 scratch 결과를 순수한 새 factor의 active acquisition이라고 해석할 수 없다. random feature의 정보 보존도 포함한다.

## 4. 문헌과 증명의 범위

CP2026는 noise deficit/clean continuation 및 fixed-vs-cosine LR를 이미 다룬다. Tian2021은 full matrix linear encoder/predictor/EMA flow를 제시한다. Saxe2014는 작은 신호와 mode strength가 학습 시간척도를 바꾸는 직접 선행이다. 단순 delay·reset 표는 이들을 넘어서는 기여가 아니다. 한편 이들이 현재 nonlinear cosine MLP+Adam을 그대로 해결했다고 주장하지도 않는다. 원문·읽은 범위·접근 실패는 [문헌 검토](literature.md)에 구분했다.

독립 도출한 scalar dot s=s²(rho−s)의 회복시간은 O(1/s0)이며 ODE와7.26e−11 상대오차로 일치한다. 이것도 Tian flow의 직접 적분이라 새 결과로 세지 않는다.

Ponce et al.의 Prop4.10 개별점 점근안정 문구는 output rotation gauge를 무시하면 성립할 수 없음을 직접 증명·계산했다. nonzero equilibrium 근처에 별도 equilibrium과 rotational zero modes가 강제된다. 이 검산은 부정확한 인용을 피하기 위한 것으로, 이번 회복 주제의 새 기여로 대체하지 않는다.

## 5. 검토 중 정정 요청과 해소 상태

- Predictor-only reset의 stale moments를 지적했고, 주담당이 predictor-specific moment reset control을 추가했다.
- scalar Euclidean coordinate flow와 sphere Riemannian flow의 global logistic식을 혼용한 부분을 지적했다. 주담당 최종 theory에서 두 dynamics와 metric을 명시적으로 분리했음을 확인했다. local Jacobian이 같다는 사실만으로 global time law를 바꿔 쓸 수 없다.
- SNR arxiv metadata의 v3 날짜2025-09-28와 HTML 내부2026-08-24가 다르다. 주담당 최종 literature에서 metadata 날짜를 채택하고 불일치를 기록했음을 확인했다.
- 3000step censoring을 long-time failure로 읽는 것을 지적했고, 주담당이 원 equalrho8seed를15000step까지 일괄 연장했다. 실제 회복4seed를 확인했다.

## 6. 재개할 조건

clean objective가 평가할 factor를 엄격히 선호하고, random initial retention·작은 mode amplitude·known head/EMA/optimizer conditioning을 통제한 뒤에도 알려진 설명이 구별하지 못하는 회복 차이가 있어야 한다. 그 차이를 실행 전 상태량으로 예측하고 별도 조건에서 맞혀야 한다. 지금 확보한 계산과 실험은 그 핵심 요건을 충족하지 못한다. 더 많은 reset·backbone·벤치마크를 덧붙이는 것은 현재의 신규성 문제를 해결하지 않는다.
