# Negative 관계와 학습 피드백

상태: 분석 중. 기준일 2026-10-22.

## 질문
표현이 충분하고 모든 negative에 양의 확률이 있어도 현재 표현에 의존한 negative 선택이 요인 부재의 안정점을 만드는가? sampler에 의한 population objective 변화와 stop-gradient 갱신 피드백을 구분한다.

## 현재 확보한 근거
아직 실행 전. 두 독립 binary factor와 동일-instance positive의 exact population InfoNCE를 첫 반증 모형으로 정했다. 빠진 요인 방향의 local Jacobian을 직접 도출한다.

## 기록
- protocol.md: 실행 전 설계 및 반증 기준
- theory.md: 도출한 명제와 증명
- literature.md: 원문 검증
- progress.md: 변경 이력
- code/ 및 results/: 실행 명령과 결과

## 다음 작업
exact enumeration gradient 검증, uniform/frozen/adaptive sampling의 요인 회복 속도와 작은 perturbation 안정성 확인.
