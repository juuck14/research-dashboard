# 원고 전 재심 초안의 판정 기록 — 변경하지 않고 보존

2026-10-22. 이 문서는 통합 `manuscript.md`를 읽기 전에 root에 전달한 독립 판정의 원문 핵심을 보존한다. 현재 판정은 [최종 재심](final_review.md)에 있으며, 아래를 현재 결론으로 읽으면 안 된다. 결과나 사전 기준이 바뀐 것처럼 소급해 쓰지 않기 위한 기록이다. 근거의 원문·증명·실행 검토는 당시에도 이미 별도 audit 파일에 있었다.

## 초안의 최종 판정 원문

**추가 핵심 연구 필요. 최상위 학술지급 논문의 핵심50% 도달은 아직 인정하지 않는다.**

반면 “네 상태에서 알려진 원리를 계산한 것뿐”이라는 최초의 가장 강한 공격은 개선 후 결과 전체에는 맞지 않는다. 일반 점수 법칙, 연속 모집단의 실현 가능한 모형, 일반 class geometry의 view-normal 조건, 실제 joint-K shared-encoder 예측이 추가되었다. 실제 독립적인 연구 결과가 남았다. 따라서 원래 방향 전체를 중단할 근거도 충분하지 않다.

두 판정을 혼동하지 않는다. 제한된 국소 이론의 중심 결과는 확보됐다. 그러나 그 분류가 JMLR 독자의 중요한 학습 판단을 바꿀 만큼 강한 기여라는 증거는 아직 부분적이다. 원래의 “의미 정보가 소실되는 경계”는 새 결과가 뒷받침하는 중심 주장이 아니다. 이는 표제만 바꾸면 해결되는 문제도 아니다.

## 초안의 여섯 gate 원문

| 기준 | 판정 | 구체적 근거와 가장 강한 남은 반론 |
|---|---|---|
| 신규성 | **통과 — 명시한 국소 분류에 한함** | 기존 fixed-risk 최적해, graph alignment bound, generic performative-response bound 또는 Athey의 aggregation 원리를 그대로 대입하면 새 all-K 조건이 나오지 않는다. Tagged finite-negative weights와 exponential-policy margin의 조건 검증이 필요하고, 그 결과 exact no-rescue/order 분류가 남는다. 반대로 MLR 자체, graph diagonalization, 네트워크 pullback 또는 sampling이 feature를 바꾼다는 큰 주장은 신규 기여에서 제외해야 한다. 문헌 검색 부재를 근거로 통과시킨 것은 아니다. |
| 중요성 | **부분 충족** | “더 많은 negatives가 factor mode를 안정화한다”와 “전체 표현을 안정화한다”를 분리하고, count 증가로 해결할 수 없는 floor를 준다는 연구적 이해는 있다. 그러나 현재 가장 강한 결과의 대상은 특정 균형 기하의 국소 feasibility다. Balanced square는 정보 보존의 필요조건도 충분조건도 아니며, 기존 graph 논문도 alignment를 별도로 가정한다. 일반 학습이나 더 넓은 기하에서 이 분류가 어떤 잘못된 선택을 고치는지에 대한 증거는 아직 약하다. 이는 계산량을 늘리면 해결되는 문제가 아니다. |
| 중심 결과 | **통과 — 수정된 국소 이론에 한함** | No-reentry, 모든 유한 K의 no-rescue floor, 연속 실현 모형, 일반 normal-block 단조 조건과 square의 exact full window가 증명·계산 결과로 존재한다. 핵심 식이 “앞으로 맞으면” 성립하는 상태는 아니다. 원래 semantic-erasure 명제에 대해서는 통과가 아니다. |
| 설득력 | **통과 — 이론과 실제 측정이 일치하는 범위** | Frozen/current sampler, joint-K/one-negative, class-mean/view modes, 수용량/parameter metric, preconditioned/standard ODE를 분리했다. 독립 exact certificate와 endpoint check도 일치한다. 이 통과는 reference를 일반 훈련이 방문한다는 뜻이 아니다. Ordinary warmup은 사전 applicability gate를3개 seed 모두 통과하지 못했다. |
| 범위 | **부분 충족** | 원자 ties와 four-state-only라는 공격은 상당히 해결됐다. 하지만 semantic-mode 법칙은 exact exchange-balanced affine directions, view-mode 법칙은 row regularity·stationarity·normal complement에 의존한다. 전체 안정 window는 아직 square에서만 완결됐다. 이러한 범위가 정직하게 명시됐다는 사실과, 그 범위만으로 최상위 수준의 기여가 충분하다는 판단은 다르다. |
| 연결성 | **통과 — 수정 중심 주장에 한함** | Negative count를 통한 local rescue의 가능/불가능과 positive graph의 추가 제약이라는 한 질문으로 증명·계산·joint-K 실험을 연결할 수 있다. Endpoint/correlation 예제는 그 주장의 한계를 규정하는 보조 결과다. 이를 모두 “정보 소실을 교정하는 학습 원리”라는 더 큰 결론에 묶으면 이 gate도 미충족으로 돌아간다. |

신규성·중심 결과·구현 검증의 통과로 중요성의 부분 충족을 상쇄하지 않는다. 따라서 현재 판정은 목표 도달이 아니다.

## 초안에서 요구했던 핵심 성과 원문

아래는 모두 해야 한다는 목록이 아니다. 적어도 하나가 현재 중요성의 공백을 직접 메워야 한다. 단순한 논문 표현 보강이나 추가 seed는 그 역할을 하지 못한다.

1. **더 넓은 학습 구조에 대한 완결된 분류.** General energy-transfer/normal-block 법칙을 병치하는 수준을 넘어, 독립적으로 자연스러운 geometry family에서 어떤 목표 구조가 실제로 가능하고 어떤 정책/count 선택으로 불가능한지를 대표 정리로 완결한다. 지금처럼 한 mode의 부호를 전체 learning rescue로 확대하지 않아야 한다.
2. **비 oracle 학습에서 실제 달라지는 판정.** 사전에 고정한 관측/positive-channel 환경에서 학습이 도달하거나 방문하는 geometry에 대해, 기존 fixed-risk/attraction-repulsion 설명만으로 내릴 판단과 새로운 count/response 판정을 구별한다. 실제 joint-K, 동일 정보, 비교 가능한 최적화, 별도 seed와 phase 조건이 필요하다. 자연 이미지나 GPU가 반드시 필요한 것은 아니다. Constructed equilibrium에서 exp3를 다시 재현하는 것은 이 검증의 대체물이 아니다.

이 중 어느 쪽도 확보하지 못하면, 현재 결과는 재사용 가능한 정리·기술 원고로 보존하되 최상위 학술지 목표의 장기 투자는 재검토해야 한다. 이는 계산 자원이 없어서 기각한다는 판단이 아니다.

## 이후 변경의 기록

위 문장을 삭제하거나 고쳐 현재 판정인 것처럼 바꾸지 않는다. 통합 원고 재심에서 해당 요구가 pure-theory 분류에 과도하게 적용됐다고 판단한 이유, 그리고 현재 수정 기여 자체를 통과시킨 근거는 `final_review.md` 마지막 절에 별도로 있다. Ordinary warmup 실패와 원래 정보 소실 해석의 반박은 두 판정에서 모두 유지된다.
