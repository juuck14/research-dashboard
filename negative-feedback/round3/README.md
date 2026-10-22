# 최상위 학술지 기준의 비판적 재검증

시작:2026-10-22(KST). 상태: 조사·분석·실험 중. 이전 round2의 ‘진행’ 판정과 ‘핵심 결과 확보’는 최상위 학술지급 기여의50%를 입증한 판정으로 받아들이지 않는다. 수학적으로 참인 제한 모형의 결과와 중요한 논문 기여를 별도로 심사한다.

## 작업 전에 고정한 목표

Primary target은 JMLR의 일반 머신러닝·학습 이론 독자다. TPAMI는 실제 visual representation/SSL로의 연결이 확보되는 경우에만 secondary 후보이며, 결과가 약하다고 TMLR나 학회 논문으로 준거를 낮추지 않는다. Journal 담당이 최근 실제 게재 원문4편의 기여 크기와 증거를 비교하고 고정 rubric을 보완한다. 그 과정은 현재 개선 결과를 보기 전에 수행한다.

핵심 문턱은 다음이다. 신규성과 중요성은 정확성이나 검산 횟수로 상쇄하지 않는다.

1. 기존 PP/robust weighting/finite-negative curvature를 아는 독자가 독립적이고 비자명한 구조를 새로 배운다.
2. 그 구조가 어떤 연구 판단을 바꾸는지 명시한다. 네 상태의 새 식이 존재한다는 것만으로 통과하지 않는다.
3. 실제 중심 명제가 증명 또는 실험으로 존재하고, 이론과 실험이 같은 정량적 질문을 검사한다.
4. 식별한 치명적 반론과 가정 의존성을 이번에 직접 검사한다.
5. 적용 범위를 좁힌 뒤에도 JMLR급 독자에게 중요한 기여가 남는다.
6. 남은 일에 중심 가설의 미검증이 숨어 있지 않다.

## 분리된 연구와 심사

- `journal/`: 실제 최상위 게재 논문·고정 기준·기여 크기 비교.
- `foundations/`: square 밖 일반화, 알려진 이론으로의 환원, 반례와 새 구조 분석.
- `neural/`: joint-K 목적에서 shared encoder가 이론과 같은 예측을 따르는지 실제 실행.
- `endpoints/`: root의 nonlinear stationary branch·endpoint·task consequence 분석.
- `review/`: 별도 검토자가 중요성·신규성·연결성을 공격하고 개선 후6항목을 재심.

처음부터 검증할 치명적 질문은 balanced square 불안정성이 실제로 해로운가, 다른 injective geometry로 이동할 뿐인가, joint-K neural 실험은 같은 중심 예측을 지지하는가, exact symmetry/identity positives/four states가 결과를 만드는가다. 반박된 가설과 실패한 기준은 보존한다. 최종 판정은 목표 도달/추가 핵심 연구 필요/중단 권고 중 하나다.
