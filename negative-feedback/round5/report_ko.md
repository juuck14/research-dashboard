# 최종 연구 판정과 복구 검증

2026-10-25. 원래 연구의 마지막 대용량 업로드가 완료되지 않았고, 중단 중 workspace 정리로 미푸시 파일이 사라졌다. 중간 커밋은 안전하다. 아래 핵심 증명은 대화에 남은 실제 유도에서 복원해 독립 재검토했으며, 대표 실험·독립 검산은 **새로 실행**했다. 사라진 원시 로그를 복구했다고 표시하지 않는다. [정확한 보존·손실 범위](recovery/STATUS.md).

## 1. 최종 판정

**검증된 수정 방향으로 진행. 새 전역 안정 평형 회복 정리를 중심으로 논문의 핵심 기여가 확보됐다.** 사전의 JMLR 구조적 이론 기준에서 핵심50% 단계에 해당한다고 판단한다. 이는 게재 보장이나 객관적으로 측정된 완성도가 아니다. 기존 국소 안정성만의 성공 판정을 복원하는 것이 아니라, 그때 없던 전역 정리와 의미 있는 표현 보장을 근거로 한다.

이전 square 안정 구간이 좋은 표현을 뜻한다는 해석은 기각을 유지한다. 정보 소실이 없는 작은 재조정, task/readout에 따른 평가 반전은 [기존 실패 기록](learning_value/README.md)에 보존되어 있다. 국소 simplex 분석만으로도 부족하다는 추가 비판을 실제 반례로 확인한 뒤, 그 공백을 새 전역 분석으로 해결했다.

## 2. 현재 중심 주장

어떤 평형점 근처에서 돌아오는지를 넘어, **negative 수를 늘렸을 때 모든 안정 정지점에서 클래스 구별이 회복되는 조건**을 제시한다.

클래스마다 단위 feature가 있고 차원은 충분하며, 모든 negative가 올바른 다른 클래스라고 하자. Positive smooth score weight의 전체 점수 범위 easy-slope budget을

\[
\gamma=\max(0,\sup_s[-\tau(\log\omega)'(s)])<1
\]

로 제한하면, adaptive detached update의 모든 선형 안정 정지점에서 simplex Gram오차가 \(M/K\) 이하임을 증명했다. \(M\)은 명시적 상수다. 따라서 충분히 큰 **유한 K** 이후에는 어떤 안정 평형도 두 클래스를 같은 feature로 병합할 수 없다. 이 결과는 current geometry가 이미 simplex 근처라는 가정이나 임의 방향의 conditional balance를 요구하지 않는다.

표현의 의미는 선택한 factor나 probe가 아니라, 임의 decoder가 모든 클래스를 구별할 수 있는 최대 feature 교란 반경 \(\min_{i\ne j}\|f_i-f_j\|/2\)으로 정했다. 새 정리가 그 반경의 하한을 준다. 더 강한 exponential easy 정책에서는 양의 floor·올바른 negatives·충분 차원 아래 **모든 유한 K**의 병합 attractor가 존재한다. Negative coverage만으로 회복 여부를 결정할 수 없다는 대비다.

## 3. 실제 확보한 근거

**완전 증명:** [global_count_recovery.md](theory_value/global_count_recovery.md). 안정 정지점의 PSD stress certificate, 정확한 tagged finite-count 하한, 전역 effective hardening, centroid/variance에서 Gram 및 decoder-radius로의 변환을 연결한다. 표준 convex-Gram·Jensen·MLR 원리는 계승한 도구로 명시했다. [새 독립 증명 감사](recovery/proof_review.md)는 차원 경계 d=C−1까지 다시 계산했다.

**복구 후 새로 실행한 대표 실험:** omega=exp(−.9s),floor.01,온도1,C4/6,K1/4096,두 seed·Gaussian/작은 injective coarse 초기화의16회다. 조건과 budget은 실행 전에 고정했다.

| 클래스 수 | K1 결과 | K4096 결과 | K4096의 정리 보장 |
|---|---|---|---|
|4|4회 모두 병합 근방|4회 simplex 근방, radius≈.81650|MSE≤.02474255,radius≥.68848907|
|6|4회 모두 병합 근방|4회 simplex 근방, radius≈.77460|MSE≤.02969105,radius≥.51606330|

모든 실행이 정한 field tolerance를 충족했다. 큰K의 최대 관측 Gram MSE는3.30e−14,64/96-node 차이는1.96e−14였다. 사전 선택한 두 전체 Jacobian은 tolerance1e−6에서 음의 모드를 분해하지 못했고, 회전 zero-mode 수는 coarse5/simplex15였다. 나머지 endpoint를 spectrum 인증한 것으로 쓰지 않는다. [모든 원시 배열·수치](recovery/population_rerun.json).

**새 독립 구현:** 작성자 oracle을 쓰지 않고 nonlinear 정책216조건의 direct tuple·tagging·전역 부등식을 계산했다. 계수 최대 오차1.39e−16, normal-block 검산 최대 오차2.96e−13이다. 작은K의 실제 coarse 안정점과 큰K의 불안정점을 구별했다. 무작위 geometry 검사로 모든 평형을 탐색했다고 주장하지 않는다. [코드](recovery/independent_check.py), [전체 raw](recovery/independent_check.json), [해석](recovery/independent_results.md).

## 4. 가장 가까운 선행연구와 차이

Awasthi 등의 fixed-law simplex, Jiang 등의 nondecreasing hardening, Tian의 detached pair-weight 및 fixed-weight low-rank 분석은 기존 지식이다. Behnia–Thrampoulidis와 Burer–Monteiro의 stress/unused-normal 원리도 계승했다. [원문 비교](critic/primary_comparison.md), [새 증명 감사의 primary 비교](recovery/proof_review.md).

새 결론은 **genuinely decreasing·nonmonotone 정책도 허용하면서 모든 안정 평형의 finite-count Gram recovery를 정량화**한다는 것이다. 작은K에서 실제 병합 attractor가 있으므로 기존 nondecreasing hardening 보장의 단순 대입이 아니다. 정확한 한 점의 부호 계산이나 'easy negative가 해로울 수 있다'는 직관을 대표 기여로 삼지 않는다.

## 5. 강한 반론과 처리

- **국소 안전성이 전역 안전성을 뜻하는가?** 아니다. Uniform과 열린 simplex 근방의 전체 field가 같아도 모든K의 bad basin이 존재하는 smooth plateau를 구성했다. 새 정리는 국소 derivative 대신 전체 score range 조건으로 이 문제를 처리한다.
- **Coarse는 그 frozen objective의 최적 표현 아닌가?** 맞다. 그것을 optimizer 실패나 feedback만의 현상으로 포장하지 않는다. 핵심은 global response 조건과 count가 모든 안정 평형의 class retention을 어떻게 바꾸는지다.
- **부정확한 probe·작은 좌표의 반올림이 만든 정보 소실인가?** 유한 feature의 injectivity를 인정한다. 증명된 극한의 병합과 연속적인 robust radius를 분리한다.
- **모든 학습 경로가 성공한다는가?** 아니다. 정리의 정량자는 모든 선형 안정 정지점이다. Cycles·global convergence·일반 neural parameter flow·현실 발생 빈도는 주장하지 않는다.
- **Nonidentity 실패 검증이 회복 정리의 확장인가?** 아니다. 기존 nonidentity 증명은 bad-attractor 쪽이며, 전역 recovery는 balanced prototype·iid 모형에 한정한다.

## 6. 고정한 목표 수준과 핵심50% 판단

신규성·중요성·중심 결과·설득력·범위·연결성을 따로 평가한다. 중요한 추가 지식은 전역 response budget 아래 **모든 안정 표현**의 회복/실패 대비이며, 그 대표 정리·유한 무병합 count·decoder-level 의미가 이미 존재한다. 대규모 benchmark의 향후 성공이 있어야 기여가 생기는 상태는 아니다. 독립 검토나 검산 개수는 이 판단의 대체 근거가 아니다.

[기존 JMLR 기준](../round3/journal/fixed_rubric.md)은 바꾸지 않았다. 현재 결과의 한계는 실제로 남지만, 선언한 전역 평형 보장을 한 점의 국소 분석으로 되돌리지는 않는다. 이것이 기존에 철회한 local-only 판정과 다른 이유다.

## 7. 남은 작업과 보존 상태

원고·증명 편집, 참고문헌 통일, 보수적 count 상한 개선은 남는다. Unequal priors·without-replacement·full multiview recovery·일반 neural training은 별도 확장이다. 그 확장이 실패해도 현재 정리와 반례는 유지된다. Global convergence를 새 중심 주장으로 바꾼다면 새로운 핵심 연구가 필요하며 현재 확보했다고 쓰지 않는다.

[원고](manuscript.md), [재현 명령](reproduction.md), [정확한 recovery provenance](recovery/STATUS.md)를 함께 제공한다. 사라진 보조 로그와 원래 재심 파일은 복원되었다고 주장하지 않으며, 현재 근거는 안전한 중간 커밋·복원 후 재검토한 증명·새로 저장한 실행 결과다.
