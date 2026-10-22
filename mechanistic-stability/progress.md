# 진행 및 수정 이력

## 01 문헌·정식화

MI v2 exact TypeS가 integer ℓ0 gap라는 점과 TypeM의 support-union 조건을 원문에서 확인했다. 기존 Gaussian/AJD 계산은 이번 경로의 새 결과로 사용하지 않았다. 초기 관심은 weak C1 leakage를 견디는 모든 동치 decoder의 구조 의미다.

## 02 weak-anchor counterexample

실행 전 protocol을 썼고 genericθ confirmation family-membership 오류를 계산 전에 수정했다(Amendment1). 6×2 constant Jacobian과 cubic sensor control에서 gap1·conditioning 고정이어도 uniform recovery modulus가 없는 family를 증명·실행했다. 이 결과는 fixed true g0 stability를 반박하지 않으며 continuous margin 가설의 필요조건일 뿐이라고 판단을 좁혔다.

## 03 목적함수 연결

MI가 실제 사용하는 Ccomp를 정확 대입했다. 제한 rotation family의 wrong local minimum·κ² preference gap를 증명·실행했으나 원문에도 bad local minima가 있으므로 그 서사 자체는 신규성 부족이라고 기록했다.

## 04 positive theorem 시도

원래 continuous κ 질문을 반례 하나로 기각하지 않기 위해 explicit amplitude/diversity 조건으로 강화했다. p>q, 모든 row norm floor, learned ℓ0 budget, C1 nearness, ||Dh|| bound 아래 모든 nonlinear transition의 normalized off-block bound·global permutation·rectangle C0 approximation을 직접 증명했다. 별도 nonlinear same-law10조건으로 검산했다. reviewer가 초기 inverse-bound 반론을 철회하고 gauge 설명 오류를 지적하여 수정했다. off-block bound에서 C1 global closeness로 자동 승격하지 않았다.

## 05 fixed-base 반례로 가정의 필요성 확인

positive theorem의 all-row floor를 점검하다 constant observation coordinates에 후보의 weak support를 추가할 수 있음을 발견했다. 고정된 true A와 same-law45° candidate, ε-near exactTypeS references를 구성했다. 실행 전에 Amendment5를 남겼으며27조건과 reviewer 별도10조건이 일치했다. 원래 가설에 candidate-side complexity/margin이 필요하다는 근거가 강화되었다.

## 06 강한 경쟁 설명: high overlap·약한 margin

weak anchors 없이도 row weights로 Ccomp가 wrong chart를 선호할 수 있음을 직접 증명하고12조건에서 계산했다. reviewer의 high-overlap 반론에 따라 p3,q2,overlap40%,strong row floor에서 true4/wrong3인 사례를 실행 전 Amendment7에 적고9조건을 확인했다. 실제 surrogate가 positive theorem의 sparsity budget를 보장하지 않는다는 공백이 핵심으로 남았다.

## 07 최신 misspecified 원문 확인과 잠정 판단

Li etal2609.33273의 web fetch는 실패했으나 HTML 원문을 curl로 확보했다. operator-spectral approximate whole-subspace와 exact component-wise의 다른 가정을 읽었다. 이 논문이 우리 질문 전체를 이미 풀었다는 주장은 하지 않는다. Garfinkle–Hillar2019 full PDF를 읽고 all-alternative dictionary stability 및 quantitative diversity가 오래된 원리임을 확인했다. 직접 positive theorem의 정확한 기존 따름정리 환원은 아직 확인하지 못했다.

현재: **판정 보류**. narrow unqualified near-TypeS class는 반례로 배제, strengthened class에서는 실질 positive proof 확보. 그러나 일반 TypeS의 비자명한 margin·실제 objective/finite data에서의 admissible class·독립 논문 신규성이 해결되지 않았다. 추가 대규모 학습으로 이 수학적/개념적 불확실성을 해결할 수 없으므로 임의 benchmark sweep는 하지 않는다. [판정과 재개 기준](verdict.md).
