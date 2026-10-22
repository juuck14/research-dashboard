# 논문 성립을 좌우하는 질문과 실제 판정

2026-10-22. 이 문서는 각 하위 protocol과 중간 기록을 모아 최종적으로 대조한 결과다. 표 전체를 최초 실행 전에 등록했다고 주장하지 않는다. 최초 질문은 round2/README에 보존된 checkpoint와 각 protocol에서 확인할 수 있다. 결과를 관측한 뒤 추가한 DCL, natural policy, OLS, tolerance 검증의 시점은 해당 progress에 따로 기록했다.

| 핵심 주장 | 시작 당시 근거 | 가장 강한 반론 | 결정적 검증과 기록된 기준 | 실제 판정 |
|---|---|---|---|---|
| 고정된 sampler에 대한 설명을 넘어, 독립적인 새 결론이 있다. | 기존 K=1의 전체 구면 공간 예제. | Generic PP나 robust weighting의 자명한 사례일 수 있다. | 원문 정리를 대조하고 비SSL counterexample을 구성했다. 일반적인 설명만 남으면 독립 기여를 기각하기로 했다. | Generic DG 및 ‘같은 q에서 안정성이 다르다’는 일반 주장은 기각했다. 정확한 finite-K 법칙은 기존 결과에서 직접 제공되지 않는다. |
| Negative 개수는 feedback instability의 정량적 경계를 바꾼다. | 이전 단계의 K≤16 수치 curvature. | Finite-batch bias나 NPC를 재현한 것이거나, scalar 모형에서만 생긴 인공적인 현상일 수 있다. | 모든 K에 대한 정확한 spectrum, inverse-moment proof, negative-only control을 확보했다. | Threshold의 엄격한 단조성을 증명했고, DCL에서도 전이가 유지되었다. 분산만의 효과라는 해석과, 동일한 uniform objective라는 주장은 제거했다. |
| Balance 경계가 전체 공간의 안정성을 결정하는 조건이 있다. | Square에서 K=1에 대해 구한 closed form. | Tied angle만 보아서 normal mode의 불안정성을 놓쳤을 수 있다. | 전체 접공간의 모드를 계산했다. 충분조건 없이는 전체 안정성을 주장하지 않는다. | 자연 정책 κ=-1, eps .1에서는 전체 안정성이 성립하지 않았다. 별도 조건 아래 모든 모드에 대한 정리와 자연 정책의 열린 성립 영역을 확보했다. |
| 특수하게 조각한 shaped filter에서만 생기는 효과가 아니다. | 같은 q를 갖는 α family. | 원하는 sampler derivative를 인위적으로 만든 구성일 수 있다. | 자연 exp 정책의 값과 기울기 조건을 분석하고, 열린 영역을 증명했다. | 모든 t>1에서 비어 있지 않은 rho 영역이 있다. log4, eps .3에서 정확한 InfoNCE 경계는 K=5, DCL 경계는 K=8이다. |
| K 경계가 실제 flow를 예측한다. | DG eigenvalue와 독립적인 FD. | 미분식, metric, branch gradient의 오류이거나 아주 느린 drift를 잘못 해석했을 수 있다. | Ordered-tuple FD, interval certificate, 일반적인 d=4 ODE로 검증했다. 미리 정한 비율로 성장하거나 수축하는지를 확인했다. | 독립적으로 계산한 78개 spectrum의 최대 오차는 5.73e-11이었다. ODE 16개가 모두 기준을 통과했다. K=4에서 약 20.085배, K=5에서 약 .049787배가 되었다. |
| Lookup 밖에서도 강한 factor loss가 관측된다. | 이전 lookup SGD 30회. | Shared MLP가 tetrahedron을 학습하거나, probe가 측정상의 착시를 만들 수 있다. | 실행 전에 36개 run의 규약을 정했다. Primary와 confirmation 각각에서 2/3 이상이 clean/noisy gate를 통과해야 하며, readout을 비교하기로 했다. | 원래 gate는 실패했다. Primary 통과는 1/3이었다. 강한 collapse로의 확장은 기각했다. Secondary 결과인 energy 압축과 noisy fragility는 실제로 관측했다. |
| 낮은 readout 점수는 정보 삭제를 뜻한다. | 작은 factor amplitude와 noisy accuracy. | 잔여 정보가 있거나, ridge가 작은 방향을 축소했을 수 있다. | 저장된 36개 모델 모두에 고정된 OLS audit을 적용하고, 독립적인 pinv로 검산했다. | PCA에서 clean OLS가 .950으로 회복되었다. 정확한 정보 삭제는 주장할 수 없다. |
| Rank filter도 같은 smooth 법칙을 따른다. | 실용적인 quantile filtering에 대한 동기. | Rank는 구간별로 일정하고, tie에서 불연속일 수 있다. | 별도의 one-sided proof와 numerical tolerance 비교를 수행했다. | Smooth 법칙의 직접 적용은 기각했다. Exact rank의 불안정성과, tolerance가 만드는 작은 안정 띠를 구분했다. |

위 첫 여섯 행의 검토를 거쳐 최종적으로 살아남은 주장은 **finite-state 모형에서의 국소적인 negative 개수 법칙**이다. Neural과 rank 결과는 적용 범위와 실패 조건을 정하는 근거다. Clean endpoint의 실패를 통과로 바꾸거나, 실제 정보 삭제를 핵심 주장에 남겨두지 않는다.

## 아직 남은 작업이 실패하면 무엇이 달라지는가

| 남은 작업 | 실패 시 의미 | 현재 논문에 미치는 영향 |
|---|---|---|
| 비대칭 population에서도 현상이 유지되는 정량적 범위를 구한다. | 정확한 대칭을 벗어나면 근사적인 예측력이 작을 수 있다. | 증명한 대칭 모형의 법칙은 유효하다. 다만 적용 범위와 중요성에 대한 평가는 약해진다. 이미 비대칭까지 일반화한 논문으로 제시하지 않는다. |
| Shared encoder에서 joint-K phase 실험을 수행한다. | Parameter metric이나 nuisance가 lookup의 K cutoff를 바꿀 수 있다. | 현재의 정확한 모형에 대한 정리가 무효화되지는 않는다. 다만 일반 신경망의 K 법칙이라는 별도 주장은 성립하지 않는다. |
| 더 많은 semantic state로 확장한다. | K boundary가 각 mode와 geometry마다 다를 수 있다. | 네 상태의 정리는 유효하다. 보편적인 K threshold라는 주장은 처음부터 하지 않았다. |
| Natural image로 확장한다. | 실제 알고리즘이나 학습된 geometry에서는 현상이 중요하지 않을 수 있다. | 실용 알고리즘의 실패를 주장하는 논문은 성립하지 않는다. 현재의 제한된 이론 논문은 그 주장을 하지 않으며, 모형에서 확보한 정량적 결과 자체를 근거로 진행을 권고한다. |
| 외부 전문가가 신규성을 무너뜨리는 선행연구를 제시한다. | 아직 확인하지 못한 가장 가까운 원문에 정확히 같은 법칙이 있다면 새로움이 무너진다. | 모든 연구에 남는 실질적인 위험이다. 현재 읽은 primary 문헌과 최신 2026년 결과에서는 직접적인 중복을 확인하지 않았다. 정확한 중복의 새 증거가 나오면 기여를 재평가하거나 기각한다. |

현재 판정은 넓은 neural 논문에 필요한 핵심 검증을 실행하지 않은 채 향후 과제로 넘긴 것이 아니다. 실제로 입증한 수학적 대상을 논문의 주기여로 선택한 것이다. 넓은 practical claim은 기각한다. 제한된 주장은 모든 K에 대한 정확한 분류와 자연 정책의 열린 성립 영역이라는 독립적인 결과를 근거로 유지한다.
