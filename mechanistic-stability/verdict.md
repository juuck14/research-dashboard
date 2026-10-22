# 최종 판정: 판정 보류

**원래 후보2에 수개월 연구를 바로 투입하라는 추천은 보류한다.** 질문이 중요하지 않거나 전부 해결되었다는 판정은 아니다. 실제 반례와 제한적 positive theorem를 확보했으나, 일반 Type S에서 필요한 비자명한 quantitative margin과 실제 학습 목적함수를 연결하는 핵심이 아직 남았다. 계산·권한 문제가 아니라 미해결인 수학과 신규성 판단이 병목이다. 증거가 없는 부분을 자연 이미지 학습으로 대신하지 않았다.

## 확정할 수 있는 내용

1. **기각된 좁은 주장:** exact integer ℓ0 gap와 inverse conditioning만으로 approximate mechanistic factor recovery가 uniform하게 안정적이라는 주장. 정확45° same-law 반례가 있다.
2. **더 강한 기각:** 후보가 어떤 exact-TypeS reference에든 가깝기만 하면 충분하고 candidate-side complexity/margin은 통제하지 않아도 된다는 주장. 고정된 true generator와 nonzero witness strength에서도 작은 새 observation support를 만드는 반례가 있다. zero observation rows·larger candidate budget를 허용한 범위다.
3. **직접 positive 결과:** p>q anchor diversity, 모든 row amplitude floor a, learned exact ℓ0 budget, C¹ leakage·chart conditioning 아래 모든 nonlinear 관측 동치 decoder의 normalized off-block derivative와 global permutation, rectangle C⁰ block approximation을 증명했다. [완전 증명](positive_bound.md).
4. **학습으로 이어지는 간극:** MI compositional contrast는 strong margin·overlap40%·perfect reconstruction·동일 Jacobian Gram에서도 wrong axes를 더 선호할 수 있다. 그러므로 위 sparsity budget를 작은 surrogate value로 대체할 수 없다. 이는 general surrogate guarantee가 없는 원문을 반박한다는 뜻은 아니다.

직접 proof와 independent implementation은 이 주장들의 정확성을 상당히 지지한다. numerical conditions의 반복 수는 현실 문제에서의 중요성이나 신규성의 증거가 아니다.

## 무엇을 아직 해결하지 못했는가

- 모든 Type S 모형의 block 의미를 안정적으로 제어하는 continuous gap를 정의하고 sharp bound 또는 불가능 경계를 얻지 못했다. 단순히 recovery modulus를 κ라고 정의하는 tautology는 허용하지 않는다.
- positive theorem의 p>q/all-row floor/learned sparsity budget가 약한 support-overlap 상황에 필요한 최소조건인지 모른다. multidimensional block과 integrability의 새로운 어려움을 해결하지 못했다.
- 실제 reconstruction loss·Ccomp near-optimality·finite samples가 위 C¹-near sparse candidate class를 어떻게 정당화하는지 결과가 없다. small MSE는 derivative 보증이 아니다.
- 본 theorem가 Garfinkle–Hillar 같은 sparse dictionary stability의 문자 그대로 따름정리라는 환원은 확인하지 못했다. 다만 proof의 counting·chain rule·continuity·integration은 elementary하여, 이 작은 결과만으로 독립 논문의 학술적 폭과 신규성을 보장할 수 없다.
- 후보2에 합쳐졌던 rare support/noise 경로를 이번 결과로 해결하거나 기각하지 않았다.

## 살려본 수정과 왜 아직 진행 권고하지 않는가

수정1: oracle Jacobian clustering 대신 모든 관측 동치 transition의 안정성을 목표로 삼았다. 실제 positive theorem가 이 부분을 진전시켰다. 그러나 그 전제는 학습자료만으로 확인하기 어렵고 기존 robustness 원리와의 차이가 작을 수 있다.

수정2: naive near-TypeS prior의 실패를 연구 중심으로 바꾸었다. fixed-base support-creation은 명확한 주장이지만 zero coordinates와 complexity mismatch라는 해석이 강하며, known ℓ0 instability의 representation 예시로 끝날 위험이 있다.

수정3: loss가 구조 의미를 잘못 선호하는 현상을 중심으로 바꾸었다. strong/low-overlap 반례가 있지만 weighted smooth relaxation과 cardinality 구조의 차이는 알려진 문제다. 바로 새로운 penalty를 제안하면 원래 피하려던 사후 방법 정당화로 돌아간다.

## 재개를 가르는 가장 정보량 높은 작업

1. [positive theorem](positive_bound.md)을 robust sparse coding/analysis-operator theorem의 가정·상수·target에 문자 그대로 대입해 보라. 정확히 환원되면 이 부분을 독립 기여로 세지 않는다.
2. zero/weak observation rows를 제외하되 support pattern을 미리 알려주지 않는 compact nonlinear Type S family에서 **candidate-side complexity를 통제한** 실제 반례 또는 비자명한 positive bound를 얻어라. 이것이 original stability 질문을 가장 직접적으로 판정한다.
3. 학습을 하려면 먼저 surrogate near-optimality가 해당 admissible set를 보장할 수 있는 조건을 고정하라. 원문의 overlap sweep 재현이나 한 regularizer 추가의 성능 향상은 진행 기준이 아니다.

진행으로 바꿀 조건은 위2 또는3의 핵심 명제와 비자명한 proof/반례가 나오고, 그 결론이 기존 dictionary conditioning으로 끝나지 않는다는 원문 대조가 되는 것이다. 현재 좁은 결과만을 논문 완성의 뼈대라고 과장하지 않고, 연결된 증명·계산·실행·한계를 연구 노트로 보존한다.

## 검토자와의 합의·이견

독립 검토자는 반례·positive theorem·surrogate counterexample의 수학적 범위를 확인했고 새로운 연구로서의 novelty가 약할 수 있다는 데 동의했다. 초기 inverse-bound 공격은 실제 chain-rule 방향을 읽은 뒤 철회되었고, gauge와 fixed-base vs family-uniform 범위 지적은 반영했다. 일반 Type S 전체가 실패한다는 결론에는 동의하지 않으며 우리도 주장하지 않는다. [독립 기록](../prevalidation-20261022/reviews/mechanism/review.md).
