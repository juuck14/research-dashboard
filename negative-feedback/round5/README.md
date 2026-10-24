# 전역 안정 평형 회복 — 현재 결과

2026-10-25. **새 전역 count-recovery 정리를 중심으로 진행.** [최종보고](report_ko.md) · [논문 원고](manuscript.md) · [완전 증명](theory_value/global_count_recovery.md) · [재현](reproduction.md).

전체 score의 easy-response budget 아래 모든 안정 정지점의 simplex Gram오차 M/K와 명시적 유한 무병합 count를 증명했다. 더 강한 response의 all-count 병합 및 국소 field만으로 전역 안전성을 판정할 수 없다는 한계도 구분한다. 전역 궤적 수렴·일반 신경망·현실 빈도는 주장하지 않는다.

**업로드 중단 후 복구:** 중간82파일 커밋은 보존됐다. 미푸시 파일 일부는 workspace 정리로 사라졌다. 핵심 증명은 대화의 유도에서 복원·독립 재검토했고, 대표16실험과216조건 독립 검산은 새로 실행했다. 원래 모든 로그가 byte-identical하게 복원됐다고 말하지 않는다. [상태와 보존 범위](recovery/STATUS.md), [새 proof review](recovery/proof_review.md), [새 raw](recovery/population_rerun.json).

## 보존된 최초 중간보고

# 핵심 공백 해결을 위한 계속 연구

2026-10-23. 상태: 연구 중. Round4의 ‘추가 핵심 연구 필요’를 종료 판정으로 사용하지 않고 다음 분석·실험을 수행한다. 목표 학술지 기준은 [기존 JMLR rubric](../round3/journal/fixed_rubric.md)을 유지한다. 이번 정상 종결은 목표 도달 또는 실제 대안 시도에 근거한 기각이다.

## 시도한 세 경로와 현재 수정

1. `learning_value/`: 원래 square 안정 구간이 task-neutral few-label 성능을 설명하는가. 모든 balanced binary task와 모든 작은 label-support 조합, stronger same-information baseline, 반대 readout을 실제 검사했다. 이 구제 경로는 지지되지 않았다.
2. `theory_value/`: 임의의 두 요인 균형 대신, task들을 대칭적으로 평가했을 때 정당화되는 simplex를 기준으로 한다. 같은 negative law를 고정하면 유일 전역 최적해인데, sampler를 갱신하면 그 표현이 어떤 count에서도 불안정해지는지 직접 유도한다.
3. `global_mechanism/`: 단순한 local 불균형을 넘어 실제 서로 다른 class를 병합하는 attractor가 존재하는지 증명·실행한다. 잘못된 class를 negative로 뽑는 효과를 제거하기 위해 same-class negatives를 완전히 제외한 경우도 분석한다.

`critic/`는 이 세 경로를 원문·독립 계산으로 공격한다. 기존 도구·알려진 geometry 원리를 새 기여로 세지 않으며, 검토자의 동의 자체를 중요성의 증거로 사용하지 않는다.

## 새 후보의 정확한 질문

무작위 task 하나를 사후 선택하지 않는다. Class 구별의 최악 adversarial radius와 모든 balanced task를 대칭적으로 평가한 위험이 기준이다. 이 목적에서 이미 정당화된 ETF/simplex가 sampler response로 유지 불가능해지고, true-negative-only의 full-support sampling에서도 class-merging attractor에 도달할 수 있는가?

기존 square의 안정성이 곧 중요한 품질이라는 주장은 폐기한 채 시작한다. 새로운 중심 질문은 더 강하며, 이전 generic feedback 직관이나 effective-temperature 환원만으로 충분히 설명되는지 별도로 검토한다. 성공을 미리 판정하지 않는다.

