# 실행 전 프로토콜 — 후보 3

작성: 2026-10-22 UTC. 아래 수치 실험은 작성 뒤 실행한다. 이 문서는 이전 보고서의 toy 산술 외 새 실행 결과를 보지 않은 상태의 계획이다.

## 질문과 두 경쟁 설명

원래 질문은 probabilistic pairwise SSL이 observation uncertainty와 unknown positive-correspondence noise를 구분하는가이다. 먼저 **모형족의 명시가 없으면 질문 자체가 결정되지 않는다**는 대안 설명을 검증한다.

- H1: unknown positive parameter만으로도 uncertainty는 본질적으로 식별 불가능하다.
- H2: 고정된 parametric kernel family에서는 전체 pair law의 고차 구조가 두 원인을 구분한다. 비식별은 unrestricted factorization 또는 측정/유한표본 한계에서 온다.

H1을 가장 직접 반박하는 결과는 원문 PCL의 한 genuine subclass에서 unknown observation concentration과 unknown positive concentration이 pair law로 모두 식별됨을 증명하는 것이다. arbitrary categorical 반례로 PCL 정리를 반박하지 않는다.

## A: 원형 vMF subclass

Z와 X는 S1(각도 mod2π), Z uniform. observation channel h_a(x−z)=exp(a cos(x−z))/(2π I0(a)), a>0. Positive latent Z+|Z는 같은 family h_b(z+−z), b>0. X+|Z+는 h_a이며 두 observation noise는 조건부 독립이다. 동일 b를 알고 있다고 가정하지 않는다. 잠재 회전/반사는 같은 설명으로 인정한다. 불확실성의 표적은 명시된 posterior h_a이며 a 또는 관측 가능한 independent-repeat Fourier moment A1(a)^2다.

관측은 population pair law 또는 iid pair sample뿐이다. 이 법칙의 n차 Fourier coefficient는 Bn=A_n(a)^2 A_n(b), A_n(k)=I_n(k)/I0(k). n=1만 쓰면 두 parameter의 곡선이 남지만 모든 n을 쓰면 joint identification이 가능한지 직접 증명한다. 저차 moment fit과 full-law fit을 혼동하지 않는다.

계산: exploration (a,b)=(2,5),(5,2),(1,1),(0.5,8),(8,0.5). concentration 범위 [0.1,12]. deterministic grid와 bounded multi-start least squares로 B1-only, B1..2, B1..8 inverse를 비교한다. optimizer success는 uniqueness 증명이 아니다. exact analytic argument와 독립 reviewer가 필요하다. confirmation parameters는 seed20261023로 loguniform[0.3,10]의 20개 쌍. 필요하면 finite difference Hessian condition을 보고하되 통계 표본복구 정리로 부르지 않는다.

판정: 전체 sequence의 주입성을 직접 보이면 H1 보편 주장은 기각한다. 이를 넘어 실제 near-optimal probabilistic SSL의 비자명한 안정성/추가측정 원리가 남지 않으면 현재 독립 연구 후보를 기각한다. inverse가 나쁜 저차 harmonic에서만 모호하면 이를 이론적 비식별로 쓰지 않는다.

## B: sharp categorical confounding (제한 모형)

m=3, Z uniform, Q_a=a I+(1−a)J/3, K_b=b I+(1−b)J/3, 0≤a,b≤1. observation X|Z~Q_a, latent positive Z+|Z~K_b, X+|Z+~Q_a. 관측 pair는 c=a²b만 정한다. 잠재 permutation을 quotient한다. arbitrary categorical latent-class 모형 전체가 아니라 이 symmetric channel family에서만 exact set를 말한다.

목표는 posterior uncertainty뿐 아니라 **기존 pair와 독립적으로 같은 Z에서 얻은 X_repeat**의 실제 예측이다. c 고정 시 a∈[sqrt(c),1], b=c/a²라는 sharp set 및 proper score의 irreducible predictive regret를 직접 계산한다. 원자료 Q/R 반례도 분수 산술로 다시 확인한다. 이 결과는 표준 channel factorization이면 신규 기여로 세지 않는다.

oracle grid c=.02,.16,.5,.9, 101개 a. primary finite sample: truth a=.8,b=.25(c=.16), n=1e3,1e4,1e5 pairs, seeds0..9. 같은 표본의 pair-MLE c_hat를 사용하고 알려진 b 또는 unknown b를 비교한다. 모든 경쟁 모델에 같은 pair sample을 준다. additional true repeat는 추가 acquisition 비용이 있음을 표시하며 pair-only와 data-budget-equal 우월성으로 주장하지 않는다.

별도 confirmation seeds101..110. entropy gauge 문제는 finite categorical 고정 측도와 permutation으로 제한하고, 핵심 판정은 observable repeat prediction의 Brier/log score로 둔다.

## 문헌과 중단 조건

Kirchhof et al2023 Thm4.4 및 Appendix A, Anandkumar2014 multi-view moments, Allman–Matias–Rhodes2009 latent class identification을 직접 대조한다. 2026-10-22 최신 direct collision을 추가 탐색한다. 세 번째 acquisition이 고전 tensor 결과의 특수 경우이면 별도 기여로 주장하지 않는다. generic unknown measurement error의 예제 및 old pair/triple distinction만 남으면 현재 구체화 기각이 합리적이다.

## 증거 분리

증명(가정과 전 단계), 수치 확인, 실제 finite-sample 실행, 외부 문헌, 미검증 추측을 구별한다. exact population toy에서 neural MCInfoNCE 학습이나 natural-image uncertainty로 확장하지 않는다. 아직 없는 neural 결과로 paper draft를 쓰지 않는다.

## Amendment 1 — log-score 정정 (첫 실행 뒤, 재실행 전)

첫 실행의 log 계산은 모든 예측을1e−15로 floor했다. a=1 대안은 repeat를 결정론적으로 예측하므로 true conditional에 양의 질량이 있는 다른 값에0을 부여한다. 따라서 **정확한 log regret는 무한대**이고, 숫자7.577은 clipped diagnostic이다. 초기 CSV/summary를 results/initial-run에 보존했다. 새 실행은 동일 seed·설계·모형을 유지하고 해당 열을 repeat_clipped_log_regret로 명확히 이름붙이며 exact_log_regret_is_infinite를 별도 기록한다. Brier와 pair-law 결과 및 판정 기준은 바꾸지 않는다.

## Amendment 2 — acquisition lineage와 정보예산 검증 (추가 실행 전)

이 수정은 초기에 계획한 additional true repeat의 구체적 비교를 확정한다. 모형 B에서 independent repeat pair의 correlation r=a²이므로 c=a²b와 함께 두 parameter를 정한다. 반면 X1의 bytes 복제는 r=1을 주며 이 공식을 적용할 근거가 없다. 일반 full-rank categorical emission의 third-order tensor 복구와는 다른 제한 모형이다.

truth a=.8,b=.25. n=1000/10000/100000. primary seeds20..29, confirmation201..210. 원래 n positive pair(2n acquisition)에 anchor-state independent repeat n개를 더해 총3n acquisition. 같은 3n acquisition budget에서1.5n positive pair만 수집한 조건도 실행한다. Pair-only에서 a가 비식별이므로 arbitrary point estimate를 비교해 이긴다고 주장하지 않고 c 추정과 sharp interval만 보고한다. 같은 bytes 복제는 추가 acquisition 비용0인 별도 invalid-lineage 진단이며 공정한 성능 경쟁으로 세지 않는다. 판정은 independent repeat의 추정 a가 .8로 수렴하는지와, budget-matched positive pair의 구조구간이 사라지지 않는지다.
