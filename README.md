이 레포지토리는 여러 연구 주제들을 병렬적으로 연구하고 그 현황을 보고하는 곳이다.

각 연구주제별로 디렉토리를 만들고 안에 README.md파일 만들어서 거기에 현황을 보고하라.

## 새 검증 회차: 보고서 후보 1·2·3

2026-10-22 시작. **SSL 회복 지연 / 근사 메커니즘 식별 안정성 / pairwise 확률적 SSL의 불확실성**을 실제 사전 검증한다. [대상·규칙·진행 기록](prevalidation-20261022/README.md). 기존 연구 결과는 별도 회차로 보존한다.

## 이번 사전 연구

후속 심화 단계(2026-10-22): [negative feedback의 핵심 기여 검증](negative-feedback/round2/README.md)을 실제로 진행 중이다. 아래 표와 첫 단계 최종보고는 이전 단계의 판정이며, 후속 단계에서 일반 필터·모든 negative 수에 대한 증명, 비선형 encoder 실험, 독립 반박 검토로 재검증한다.

2026-10-22 실제 분석·실험·독립 검토를 마쳤다. [최종 종합보고](coordination/final_report.md), [재현 안내](coordination/reproduction.md), [진행 이력](coordination/progress.md).

| 주제 | 현재 판정 | 결정적 근거 |
|---|---|---|
| 부분 식별 | 현재 구체화 기각 | 정확한 Gaussian ambiguity를 도출했으나 기존 AJD contrast로 환원 |
| Negative 피드백 | 수정 후 진행 | normalized full-capacity에서 matched frozen 안정/adaptive 불안정의 명제와 독립 실행 확보 |
| 자기 target 교정 | 현재 구체화 기각 | 회복·고착 ODE가 Tian2021의 정확한 특수 경우 |

Negative의 [실제 결과 기반 논문 초안](negative-feedback/paper_draft.md)에는 없는 증명·자연 이미지 결과를 넣지 않았다. 일반 비선형 부분 식별·teacher 교정 전체의 불가능성을 주장하지 않는다.

- [전체 진행 및 증거 규칙](coordination/README.md)
- [근사 가정 아래의 부분 식별](partial-identification/README.md)
- [의미 요인별 negative 관계와 피드백](negative-feedback/README.md)
- [불완전한 자기 생성 target의 교정](target-correction/README.md)
