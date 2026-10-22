# 보고서 후보 1·2·3의 실제 사전 검증

시작·완료: 2026-10-22 UTC. 상태: 실제 분석·실행·독립 검토 및 착수 판단 완료. 이전 저장소 연구와 독립된 검증 회차다.

**판정: 1 현재 구체화 기각 / 2 판정 보류 / 3 현재 구체화 기각.** [최종 종합보고](final_report.md), [증거·역할](evidence.md), [재현 안내](reproduction.md). 즉시 수개월 연구를 권하는 후보는 없다. 후보2는 제한 정리가 있으나 일반 안정성과 실제 loss의 연결·신규성이 핵심 미해결이다.

## 대상과 원자료

입력은 `research_directions_20261022.pdf`(24쪽, 2026-10-22)에서 번호를 붙인 세 후보다. 보고서의 현재 파일을 다시 읽어 대상을 확인했다. 저장소의 기존 세 주제와 번호를 혼동하지 않는다.

| 번호 | 이번 대상 | 기록 |
|---|---|---|
| 1 | SSL 특징 회복 지연의 상태와 원인 | [ssl-recovery](../ssl-recovery/README.md) |
| 2 | 약한 메커니즘 가정 위반 아래 식별 안정성 | [mechanistic-stability](../mechanistic-stability/README.md) |
| 3 | pairwise 확률적 SSL에서 식별 가능한 불확실성 | [pair-uncertainty](../pair-uncertainty/README.md) |

기준 저장소 commit: `ebff86b15237106953487dd9a63f44734e9ef9db`. README와 coordination/README를 읽었다. 저장소 안 AGENTS.md는 없다. 기존 partial-identification 및 target-correction의 기각 결과는 재사용 가능성을 직접 검토하되 이번 질문의 기각 근거로 자동 전용하지 않는다. 기존 파일은 수정하지 않고 최상위 README에 새 회차 링크만 추가한다.

## 실행 규칙

세 담당이 독립적으로 원문·문제 정의·증명·실험을 수행한다. 이후 다른 담당이 별도 검토와 계산을 수행한다. Root만 git commit/push를 직렬화한다. 실험 전 protocol에 가정·경쟁 설명·seed·판정 기준을 남긴다. 변경은 덮어쓰지 않고 amendment로 기록한다.

증거 표시는 **문헌 확인 / 직접 증명 / 직접 실행 / 미검증 가설**로 구분한다. 정확한 식별성, 유한 표본, 학습 목적함수, 최적화, 측정 오류를 구별한다. 신규성 없는 재현을 독립 기여로 세지 않으며, 선형 특수 경우의 실패를 넓은 질문 전체로 확대하지 않는다.

코드·작은 결과·환경·실행 명령·실패와 수정 이력을 보존한다. 외부 논문 원문, 큰 데이터, checkpoint는 저장소에 올리지 않는다. 최종 판정은 진행 권고 / 수정 후 진행 / 기각 / 판정 보류이며 증거 강도와 남은 핵심 검증을 명시한다.

## 현황

- [진행 기록](progress.md)
- 주제별 protocol과 최신 현황은 각 README에 연결했다.
- 진행 권고·수정 후 진행 주제가 없어, 아직 없는 결과를 채운 긍정적 paper draft는 작성하지 않았다. 후보2의 [실제 결과 기반 연구 노트](../mechanistic-stability/research_note.md)는 판정 보류 상태와 미해결 핵심을 명시한다.
