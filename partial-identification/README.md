# 근사 가정 아래의 부분 식별

상태: 기각 — 현재 좁힌 독립 주제의 신규성 근거 부족. 기준일 2026-10-22.

질문: 소스의 조건부 독립이 허용오차만큼 틀리고 환경 변화가 약할 때, 동일한 관측분포를 만드는 잠재 분해들의 집합은 얼마나 큰가?

## 현재 확인된 내용

- 기준환경의 **소스 covariance가 정확히 I**라는 추가 제약을 둔 선형 Gaussian family에서 회전 대안의 정확한 식별집합을 직접 증명했다. 관측 whitening만으로 이 제약을 정당화할 수 없다. 일반 GL(d)/비선형 family에는 feasible subset와 ambiguity lower bound로만 적용한다.
- 41개 population grid 조건과 360개 표본 반복을 실제 실행했다. 수식–covariance 계산 최대 오차 2.5e-16, 관측 covariance 재구성 오차 8.9e-16.
- 이 설정은 이분산 식별, joint diagonalization 및 perturbation 이론과 매우 가깝다. 단순 gap 대비 회복오차를 독립 기여로 주장하지 않는다.
- 구조 오차를 conditional Gaussian total correlation으로 정의해, 좌표별 가역 재매개화에 대한 의존성 척도 문제를 피한다. mixing은 선형·기준환경 소스 공분산을 정확히 신뢰하는 orthogonal family에 한정한다.

## 문서

- [사전 실험 계획](protocol.md)
- [이론 분석](theory.md)
- [문헌 대조](literature.md)
- [진행 기록](progress.md)
- [최종 판정](verdict.md)

완료: exact 2D ambiguity 증명·계산, 3D pairwise 대안, 360개 표본 반복, 독립 critic 반론 반영, 직접 선행 식 대조. 일반 비선형 질문은 미해결이며 기각 범위에 포함하지 않는다.

## 핵심 결론

- Gaussian 평균 total correlation과 그 local sensitivity는 고전 Pham joint diagonalization contrast 및 Hessian과 직접 같다.
- δ>0에서는 별도 exact structural restriction 없이 정확한 component/group 보장이 없다. 방향별 approximate ambiguity만 남는다.
- [직접 실행 결과](results.md), [증명과 범위](theory.md), [최종 판정과 재개 조건](verdict.md)를 함께 읽어야 한다.

재현: `OPENBLAS_NUM_THREADS=1 python code/run_study.py`. 환경과 seed는 protocol.md 및 results/environment.json.
