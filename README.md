이 레포지토리는 여러 연구 주제들을 병렬적으로 연구하고 그 현황을 보고하는 곳이다.

각 연구주제별로 디렉토리를 만들고 안에 README.md파일 만들어서 거기에 현황을 보고하라.

## 최신: negative feedback의 최상위 기준 재검증

2026-10-22 [round3 최종보고](negative-feedback/round3/report_ko.md) · [논문 원고](negative-feedback/round3/manuscript.md) · [재현](negative-feedback/round3/reproduction.md) · [독립 재심](negative-feedback/round3/review/final_review.md). **수정된 국소 이론 논문의 핵심50% 확보로 판정.** 일반·연속 score law의 all-finite-count rescue 조건, 반대 방향의 positive-gap 조건, exact full-stability window를 증명했다. 원래 정보 소실 해석은 기각하고 ordinary applicability 실패를 보존했다. 실전 SSL 성능이나 cutoff 확보 판정이 아니다. 아래 다른 회차 기록은 그대로 보존한다.

## 이번 사전 연구

후속 심화 단계(2026-10-22): [negative feedback의 핵심 결과 확보](negative-feedback/round2/README.md)를 마쳤다. [한국어 최종보고](negative-feedback/round2/report_ko.md),[논문 원고](negative-feedback/round2/manuscript.md),[핵심 반론 대조표](negative-feedback/round2/decisive_questions.md),[재현 안내](negative-feedback/round2/reproduction.md). 판정은 **검증된 수정 방향으로 진행**이며, 모든 negative 수의 정확한 국소 안정성 법칙과 자연 정책의 열린 성립 영역을 증명·독립 검산했다. 강한 neural clean-loss endpoint 실패와 정보 소실 비주장도 기록했다.

### 보존된 1차 사전 연구

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


## 새 검증 회차: 보고서 후보 1·2·3

2026-10-22 실제 분석·실험·독립 교차 검토를 완료했다. **후보1 현재 구체화 기각 / 후보2 판정 보류 / 후보3 현재 구체화 기각.** 이번 결과로 즉시 수개월 연구를 권하는 후보는 없다.

| 후보 | 실제 확보한 것 | 남은 핵심 |
|---|---|---|
| SSL 회복 지연 | nonlinear 학습·상태 개입·장기 및 contrastive 대조, flat optimum 증명 | 기존 설명을 넘는 새 회복 예측 미확보 |
| 근사 메커니즘 식별 안정성 | same-law 반례·all-candidate 제한 정리·surrogate preference 반례 | 일반 quantitative margin·learned candidate 연결·신규성 미해결 |
| pairwise 확률적 SSL의 불확실성 | sharp prediction set·표본/예산 실험·vMF 식별·singular KL | 고전 원리를 넘는 실제 SSL 기여 미확보 |

[최종 종합보고](prevalidation-20261022/final_report.md) · [증거·역할](prevalidation-20261022/evidence.md) · [재현 안내](prevalidation-20261022/reproduction.md) · [진행 이력](prevalidation-20261022/progress.md). 아래 기존 연구 결과는 별도 회차로 보존한다.
