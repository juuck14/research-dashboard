# 후보 2 — 근사 메커니즘 식별 안정성

상태: **판정 보류**. 실제 반례·제한적 nonlinear positive theorem·정확 surrogate 계산·독립 검토를 마쳤다. 원래의 일반 Type S quantitative stability와 실제 loss에서의 candidate class를 연결하는 핵심은 남았다. [최종 판정](verdict.md).

기존 Gaussian/AJD 부분 식별 계산을 새 결과로 재사용하지 않았다. 이번 회차의 대상은 latent density가 dependent해도 되는 mechanistic sparsity다. [전체 규칙](../prevalidation-20261022/README.md)을 따른다.

## 실제 확보한 결과

- integer sparsity gap·inverse conditioning만으로 uniform 안정성은 없다.6×2 same-law45° 반례, nonlinear sensor control,47조건을 직접 실행했다.
- candidate reference의 sparsity/강도를 통제하지 않으면 fixed true generator에서도 support-creation 반례가 있다.27조건 및 독립10조건에서 확인했다.
- explicit anchor amplitude/diversity·learned sparsity budget·C¹ regularity 아래 **모든 nonlinear 동치 decoder**의 off-block derivative와 global 동일 permutation, rectangle C⁰ block approximation을 직접 증명했다.
- 실제 Ccomp surrogate는 overlap40%·strong row margin·동일 Jacobian metric에서 true4/wrong3을 준다. 따라서 좋은 smooth surrogate value를 정확 sparsity budget로 바꿀 수 없다.

이 결과를 general Type S 해답이나 완성된 신규 논문의 증거로 확대하지 않는다. 반례의 class와 positive theorem의 강화 가정을 분리했다.

## 연결된 기록

- [실행 전 protocol·설계 변경7건](protocol.md)
- [가까운5개 원문과 정확한 공백](literature.md)
- [반례·surrogate 계산·증명](theory.md)
- [nonlinear all-candidate positive theorem와 완전 증명](positive_bound.md)
- [직접 실행 결과·재현 명령·환경](results.md)
- [진행·가설 수정 기록](progress.md)
- [독립 반박·별도 코드 검산](../prevalidation-20261022/reviews/mechanism/review.md)

먼저 할 일은 새로운 benchmark 학습이 아니라, 제한 정리가 기존 sparse dictionary theorem에 정확 환원되는지 확인하고 candidate-side complexity를 고정한 nonlinear 모형에서 남은 stability 명제를 판정하는 것이다.
