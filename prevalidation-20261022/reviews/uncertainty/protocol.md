# 후보 3 독립 검토 — 실행 전 설계

담당: uncertainty_review. 2026-10-22. 문헌 조사는 실행과 구분한다. 주담당 파일은 수정하지 않는다.

## 먼저 확인한 문헌 충돌

- Allman–Matias–Rhodes2009의 Corollary 2: 3-view latent class Kruskal rank 조건. uniform3 full-rank emission toy에 즉시 적용한다.
- Anandkumar et al.2014의 Theorem3.1, Condition4.1, Theorem4.3: conditional independent categorical observations의 2/3차 moment 및 whitening/tensor recovery.
- Liu–Cheng–Zhang2023 Theorem4.2와 부록: noisy-label transition 식별에 관한 2-view 반례·3-view 보장. 조건을 제거한 일반 주장으로 확장하지 않는다.

위 내용은 원문 확인이며 이번 실행 결과가 아니다. 구체적 충돌과 읽은 범위는 review.md에 남긴다.

## 독립 확인 A — 3-state toy와 sharp interval

uniform latent3, 동일 column-stochastic emission E, uniform observation을 고정한다. 기준 E=J/3+a(I−J/3), a=.4. 고정 pair Gram을 만족하는 **doubly-stochastic 3×3** 모형만 대상으로 O(2) orbit을 분석한다. 범위를 임의 prior·rectangular emission으로 확대하지 않는다.

사전 수식: Eθ=J/3+aOθ(I−J/3), Oθ1=1. a≤.5이면 모든 θ에서 nonnegative. T111=(1+6a²+2a³cos(3θ))/27이 예상된다(회전 방향에 따른 부호·phase는 코드에서 직접 대조). conditional endpoints는 numerator의 ±값을 3(1+2a²)로 나눈 값. 생성모형을 직접 열거하여 Gram, triple law, 조건부 값을 계산한다. primary θ 고정 1001 grid, confirmation seed7319의 random angles 200개. 수식 오차1e−12 이하를 판정 기준으로 둔다. 숫자가 맞아도 신규성은 별도 심사한다.

## 독립 확인 B — circle-vMF unknown-kernel 반박

주담당의 반박 가설: emission concentration a>0와 positive kernel concentration b>0를 모두 몰라도 모든 Fourier coefficients Bn=[In(a)/I0(a)]²[In(b)/I0(b)]가 정확히 알려지면 (a,b)는 joint identifiable. a=0 또는 b=0 퇴화는 별도로 취급한다.

독립 증명: fixed-concentration large-order Bessel series의 항별 전개를 직접 확인한다. x=a²/4,y=b²/4로 두고 logBn의 n,상수,n−1,n−3 항이 정하는 x²y, 2x+y, 2x²+y²에서 중복root x와 singleton y를 복원하는 논리가 타당한지 검사한다. 이를 수치적 fitting으로 증명했다고 하지 않는다.

직접 실행: concentration (a,b)=(.5,.5),(1,2),(2,1),(2,2),(4,8),(8,4). n=5,10,20,40의 log expansion residual을 측정하고 n=1..4 harmonic map의 log-parameter Jacobian singular values를 계산한다. 큰 n의 underflow를 피하려 In factorial-normalized series를 사용한다. a=b에서 finite-order Jacobian columns가 정확히 2:1이면 rank loss로 보고한다. exact global injection과 local regularity/finite sample conditioning을 구별한다.

실행 후 조건 변경은 아래에 추가한다. 실패·반례도 보존하며 숫자에 맞춰 기준을 바꾸지 않는다.

### 실행 전 역할 조정

Root가 circle-vMF diagonal의 density KL·LRT·singular Jacobian을 별도 구현하기로 했다. 중복 실행을 피하려 여기서는 exact-injection 증명과 Bessel expansion, 3-state independent enumeration에 집중한다. Bessel n grid는 큰 고정 concentration에서 점근 영역을 확인하기 위해 **실행 전에** 80,160,320을 추가한다. 다른 결론·판정 기준은 바꾸지 않는다.

## C — 주담당 결과에 대한 후속 독립 감사(실행 전)

주담당의 코드·population/finite CSV를 읽었다. 이제 주담당의 matrix einsum을 import하지 않고 latent Z,Z+ 및 세 관측을 중첩 열거해 positive-transition family를 재계산한다. c=.02,.16,.5,.9 각각 11개 a와 seed9319의 100 random (a,b)를 확인한다. pair formula·repeat conditional formula·normalization·전체 risk를 계산하고 최대오차1e−12를 요구한다. finite CSV의 같은 dataset별 세 policy가 실제로 같은 c_hat를 쓰는지, unknown-b 두 대안의 pair risk가 동일한지 확인한다. 이는 owner 결과를 본 후의 **감사**이며 독립 사전 discovery로 세지 않는다.
