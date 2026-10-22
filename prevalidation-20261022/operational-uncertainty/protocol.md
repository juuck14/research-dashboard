# Circle vMF pair-law의 국소 구분 가능성 — 실행 전 설계

작성: 2026-10-22 UTC. 담당 Root. 후보3 담당의 exact-identifiability 분석과 독립 계산이다. 결과를 보기 전에 기록한다.

## 문제와 허용 정보

원 위 균일 latent, 두 관측의 동일 vMF posterior concentration a>0, latent positive-transition concentration b>0를 고정한 homoscedastic family다. pair-angle density의 Fourier 계수는 c_m(a,b)=[I_m(a)/I_0(a)]²[I_m(b)/I_0(b)]다. 관측은 독립 pair들, 단 각 pair 안 두 관측은 종속된다. 동일 원본의 augmentation을 독립 acquisition으로 취급하지 않는다. a,b를 모두 미지로 둔다.

관측 가능한 목표는 pair 법칙이며 a는 이 제한 family의 posterior concentration이다. 일반 categorical/PCL 전체에 확대하지 않는다. 평균방향 전역 회전은 같은 해이며 a와 b의 교환은 같은 해가 아니다(관측 channel은 두 번, transition은 한 번 등장).

## 사전 가설

H1: exact pair-law가 a,b를 식별하더라도 a=b=c>0에서는 pair-law Jacobian의 두 열이 2:1이므로 Fisher information은 특이하다. path a=c+t,b=c−2t는 모든 harmonics의 1차 변화를 상쇄한다.

H2: p_t=p_0+t²A+t³B+O(t⁴)이고 A,B가 0이 아니라면 KL(p_t||p_0)~C4 t⁴, KL(p_t||p_{−t})~C6 t⁶. 이는 null direction의 서로 다른 두 판별문제다. 단순 vs 단순 검정의 표본 비용이며 일반 estimator minimax rate나 새로운 일반 이론으로 주장하지 않는다.

가장 강한 경쟁 설명은 알려진 singular inverse/mixture/blind-deconvolution의 국소 비정규성이다. 본 계산이 그 현상의 특수 경우라면 신규 결과로 권하지 않는다. 정확한 식별성은 별도 담당/검토자의 증명이 필요하며 이 실험 자체는 증명하지 않는다.

## 실행 조건과 판정

- population density: Fourier 64 modes, 8192-point periodic trapezoidal integration. c=1,2,4; |t|=.02,.04,.08,.12,.16 (양의 parameter 유지).
- 독립 해석 검산: Bessel derivative와 Taylor coefficient로 C4=.5∫A²/p0, C6=2∫B²/p0 계산; mode32/grid4096 및 mode96/grid16384로 적분 수렴 확인.
- 직접 numerical criterion: 작은 t에서 KL/t^k가 이론 상수에 접근하는지, log-log slope가 해당 차수를 지지하는지 보고. roundoff가 지배하는 수치는 제외 기준을 명시한다(KL≤1e−13).
- finite-sample 확인은 c=2, t=.08,.12,.16, n≈1/KL를 사용한 oracle likelihood-ratio test. primary seeds 3401–3406, confirmation 9401–9406. 양 모형에 동일 n; true parameters를 아는 oracle 판별이므로 학습기 성능으로 해석하지 않는다. 총 생성 관측을 2백만 pair 이내로 제한하며 큰 n이면 KL/Hellinger 계산으로 대체하고 대체 이유 기록.
- 반박 조건: 1차 sensitivity가 0이 아니거나, A/B가 0이거나, 적분 오차를 줄여도 예측 차수/상수가 성립하지 않으면 가설 수정. 가설을 바꾼 후 같은 데이터로 확인했다고 보고하지 않는다.

정확한 법칙, finite-sample 판별, parameter-estimation 최적화는 다른 증거다. 원자료·명령·환경·실패/변경 이력을 함께 보존한다.
