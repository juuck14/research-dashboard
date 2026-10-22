# 근사 가정 아래의 부분 식별

상태: 분석 중. 기준일 2026-10-22.

질문: 소스의 조건부 독립이 허용오차만큼 틀리고 환경 변화가 약할 때, 동일한 관측분포를 만드는 잠재 분해들의 집합은 얼마나 큰가?

## 현재 확인된 내용

- 선형 Gaussian 통제모형에서 동일 관측분포를 만드는 회전 대안의 정확한 식별집합을 직접 도출했다. 아직 코드를 실행하지 않았다.
- 이 설정은 이분산 식별, joint diagonalization 및 perturbation 이론과 매우 가깝다. 단순 gap 대비 회복오차를 독립 기여로 주장하지 않는다.
- 구조 오차를 conditional Gaussian total correlation으로 정의해, 좌표별 가역 재매개화에 대한 의존성 척도 문제를 피한다. mixing은 선형·기준환경 공분산 정규화로 orthogonal family에 한정한다.

## 문서

- [사전 실험 계획](protocol.md)
- [이론 분석](theory.md)
- [문헌 대조](literature.md)
- [진행 기록](progress.md)
- [최종 판정](verdict.md)

계획: exact 2D ambiguity를 계산으로 검증하고, 3D에서 약한 pair와 강한 axis의 차이를 확인한다. 미실행 계획과 직접 관측 결과를 분리한다.
