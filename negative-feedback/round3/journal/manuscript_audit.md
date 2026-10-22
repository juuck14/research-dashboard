# 통합 원고의 claim-to-evidence 재심

2026-10-22. 직접 읽은 파일: `../manuscript.md`. 이 검토는 [최종 질적 재심](final_reassessment.md)의 독립 판정을 유지하면서, 원고가 그 판정 범위를 넘어서는지 확인한다. 다른 검토자의 중요성 ‘부분 충족’ 이견은 별도로 보존해야 한다. 동의자 수가 판정 근거가 아니다.

## 핵심 판단

원고는 현재 확보된 수정 기여와 대체로 정확히 일치한다. 중요한 철회와 경계가 본문 안에 남아 있다: semantic erasure 철회, ordinary applicability 실패, upper boundary의 frozen 기전, constructed encoder의 oracle reference, standard MLR/Laplacian 도구의 기여 제외. 원래 one-negative neural 결과를 joint-K 검증으로 재사용하지도 않는다.

대표 지식은 다음 순서로 연결된다: finite-count feasibility의 필요충분조건 → 같은 count가 다른 normal-view mode에 부과하는 반대 제약 → 두 조건의 full-spectrum 교집합. 이 구조가 일반적인 ‘more negatives may hurt’와 구별되는 이유다. Natural-image 결과나 일반적인 learned visitation이 없다는 사실을 감춘 문장은 확인하지 못했다.

## 수정이 필요한 구체적인 두 지점

1. Theorem1 proof의 `dnu=q h²W dp`는 §3에서 q가 measure인 정의와 충돌한다. `dν(y)=h(y)²W(y)q₀(dy)`로 쓰면 된다. 정리의 증명이나 결론이 바뀌는 문제는 아니다.
2. §5.1의 full-attraction equivalence는 ‘earlier square class-mean stability conditions’만으로 호출한다. 해당 충분 조건 `g≤0`, `t2/t0≥e`, `Bw>Av` 및 사용한 `lambda_b`/`T_K` 정의의 명시나 정확한 원증명 링크가 필요하다. 이 조건 없이는 독자가 현재 manuscript만으로 full stability iff를 검증하기 어렵다. 새 핵심 실험을 요구하는 것이 아니라 대표 정리의 가정과 dependency를 완성하는 작업이다.

추가로 Related Work가 ‘additional recent comparisons’를 `source_audit.md`와 `graph_extension_audit.md`에만 연결하면, 실제로 나중에 읽은 Cai2026와 Li/Wei/Yang/Ying2026 비교는 찾을 수 없다. 그 내용을 추가하거나 `final_reassessment.md`의 source-comparison 구간을 함께 연결해야 한다. Athey는 revised1999 working paper임을 참고문헌에 명시하면 정확하다.

## 검토 중 발견해 직접 해결한 더 강한 positive control

회의적인 독자는 유한 window witness의 `P=.95I+.05Uniform`가95% identity positive를 포함한다는 점을 지적할 수 있다. 이 반론은 새 large experiment를 기다리지 않고 이미 완성된 TheoremV1의 corollary로 해결된다.

각 class에20개 views를 놓고, positive channel을 self-loop 없는 undirected cycle의 random walk로 정한다:

\[
P_{i,i+1}=P_{i,i-1}=\tfrac12,\qquad P_{ii}=0.
\]

모든 positive는 다른 observation이다. 이 행렬은 symmetric stochastic이고, nonconstant 최대 eigenvalue는 `cos(π/10)`이다. Algebraic gap은

\[
\gamma=1-\cos(\pi/10)=1-\frac{\sqrt{10+2\sqrt5}}4.
\]

[실행한 rational certificate](zero_self_cycle_certificate.py)는 `489/10000 < gamma < 49/1000`을 증명한다. [저장 결과](zero_self_cycle_certificate.json)는 별도 xi certificate와 결합되는 범위를 명시한다. 이미 인증한 `xi11<.0486`와 `xi12>.0520` 사이에 있으므로, 같은 class-mean lower boundary와 결합해 이 **zero-self-positive** 모델도 exact full window가 K5..11이다.

Cycle의 periodicity는 문제가 아니다. 현재 theorem은 absolute-value mixing coefficient가 아니라 algebraic Dirichlet gap을 쓰며, eigenvalue−1은 attraction을 더 강하게 할 뿐이다. 이 witness는 C4,m20의80 observations에 관한 직접 도출된 corollary다.80-node neural experiment를 실행한 것은 아니며, 새로운 독립 contribution으로 세지 않는다. 그러나 ‘identity positives를 제거하면 window가 사라진다’는 대안 설명에는 결정적 반례다.

## 최종 원고 판정의 범위

위 표기·dependency 수정을 반영하면 현재 원고의 대표 claim은 [최종 재심](final_reassessment.md)에서 통과시킨 구조적 이론 기여와 일치한다. Importance에 관한 다른 독립 검토자의 이견은 없애지 말아야 한다. 저널 적합성 판단이 논쟁적이라는 사실과 증명·계산이 이미 존재한다는 사실은 함께 보고할 수 있다.

앞으로 ordinary training이 더 자주 square를 방문한다는 결과가 나오면 application scope를 별도로 평가할 수 있다. 나오지 않아도 현재 pure theory 정리가 사라지지는 않는다. 반대로 이를 자연스러운 실전 cutoff 또는 semantic-erasure theorem으로 다시 서술하면 현재의 novelty/importance 통과 판정은 적용할 수 없다.
