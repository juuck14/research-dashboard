# Negative count와 학습 피드백 — 최상위 기준 재검증

**최종 판정: 목표 도달 — 검증된 수정 방향의 국소 population 이론 논문으로 진행.** 2026-10-22. 이는 JMLR를 비교 대상으로 고정한 핵심 기여 확보 판정이며, 채택 보장·일반 학습 성능·정보 소실 논문에 대한 판정이 아니다.

[한국어 최종보고](report_ko.md) · [실제 결과 기반 논문 원고](manuscript.md) · [재현 안내](reproduction.md) · [연구 기록](progress.md)

## 새로 확보한 중심 기여

1. Bounded finite/continuous exchange-balanced score direction에서, **어떤 유한 negative 수라도 안정화할 수 있는지**의 필요충분조건과 count에 따른 no-reentry를 증명했다.
2. 일반 stationary score-regular geometry의 normal-view 유지에 필요한 positive graph gap은 count와 함께 엄격히 증가함을 증명했다. 이 상한 기전은 frozen에도 존재한다.
3. 전체 square/view spectrum에서 두 조건이 합쳐지는 정확한 안정 구간을 도출·독립 인증했다. 자연 정책의 사례는 **K5..11**이며, 자기 positive가 전혀 없는20-cycle에서도 성립한다.
4. 동일 joint-K shared MLP의 국소 flow를 실제 실행해 같은 모드 예측을 검사했다. 구성된 평형점 검증이며 일반 학습 방문 증거는 아니다.

## 반박된 해석과 보존한 실패

원래 K4/5 경계는 의미 정보 소실 경계가 아니다. K4의 안정 endpoint는 injective하며 약한 요인 에너지는.46914다. 원래 ordinary warmup과 새 weak-positive scope arm은 모두 적용성0/3이었다. 이 실패를 exact-window 확인으로 세지 않는다. Generic geometry/global learning/실전 filtering cutoff는 현재 주장 밖이다.

## 근거를 직접 확인할 경로

| 자료 | 내용 |
|---|---|
| [foundations](foundations/README.md) | 일반·연속 정리, analytic floor, arbitrary stationary geometry normal block |
| [neural](neural/README.md) | 전체 view spectrum, 실제 joint-K MLP, exact certificates, ordinary 실패 |
| [endpoints](endpoints/README.md) | 원래 의미 소실 해석의 반박과 coarse attractor의 별도 국소 결과 |
| [correlation](correlation/README.md) | Pair law/unique-set law만으로 iid law를 확장할 수 없는 반례 |
| [journal](journal/README.md) | 작업 전 고정한 JMLR bar, 실제 게재5편 원문 비교, 최근2026 원문 대조 |
| [review](review/README.md) | 독립 증명·코드·유리수 인증·최종6gate 재심 |

작성 담당과 검토 담당을 분리했다. [최초 비판](review/initial_critique.md), [원고 전 반대판정](review/pre_manuscript_verdict.md), [최종 재심](review/final_review.md)을 모두 보존했다. 판정 변경의 근거는 더 많은 문서/seed나 담당자의 동의가 아니라, 네 상태 계산을 넘어선 sharp all-count 분류와 반대 spectral 제약의 실제 증명이다.

[초기 작업 규약](initial_scope.md)과 [고정 평가 기준](journal/fixed_rubric.md)은 결과에 맞춰 목표를 낮추지 않았는지 확인하는 자료다. 이전 단계 결과는 [round2](../round2/README.md)에 보존한다.
