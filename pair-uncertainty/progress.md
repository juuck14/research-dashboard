# 진행 기록

## 00 — 원문과 가정

저장소 지침, 보고서, Kirchhof2023 §4/AppendixA를 직접 읽었다. Categorical counterexample로 vMF theorem을 반박할 수 없다. Unknown kernel의 family를 먼저 정해야 질문이 성립한다.

## 01 — 실행 전 정식화

Protocol에 circle vMF H1/H2, symmetric categorical branch, exact/finite-sample/optimization 구분, seed·grid·판정조건을 먼저 기록했다.

## 02 — 직접 증명·첫 실행

Positive finite circle concentrations의 full Fourier sequence가(a,b)를 정함을 직접 증명. Bessel expansion에서 multiset{x,x,y}의 cubic을 복구했고 independent reviewer가 검산했다. 이번에 추가한 강한 탐색 H1을 이 subclass에서 반박했다. 원래 존재적 가설의 반박은 아니다(아래 범위 정정 기록).

Categorical404population,60finite datasets,180predictions, circle300primary+400confirmation inverse fits 실행. 식 검산5.55e−16이내. Near-equal concentrations에서 작은 residual에도 parametererror가 남았고 exact counterexample로 부르지 않았다.

## 03 — 측정 오류 정정

Perfect-observation predictor의 exact log regret∞를 numerical floor로 유한값 표시한 문제 발견. 초기CSV/summary를 results/initial-run에 보존하고 Amendment1 뒤 동일 설정 재실행. 최신 결과는 clipped diagnostic/exact-infinite flag를 구별한다. Brier결과·가설기준 불변.

## 04 — acquisition의 정보와 개수

추가 실행 전 Amendment2 기록. Genuine-repeat와 동일3n acquisition budget의 more-positivepairs를60dataset에서 비교. Repeat추정은 truth로 수렴하고 positive-only identified width≈.6은 남았다. 이 제한family에서는 joint triple보다 새 repeat pair law만으로 충분하다. Copy를 independent로 취급하면 a=1의 잘못된 결론.

## 05 — 선행연구가 설명하는 부분 제거

Anandkumar2014/Allman2009 원문: pair/triple principle은 고전. Zhang–Chen2026 v2(Oct14) §3/AppA: aleatoric/expert/stochastic분해는 이미 명시하되 structural separability가 핵심. Root/reviewer는 Rotnitzky2000 singular likelihood 및 replicate-deconvolution 대조.

현재 분석·실험·독립 검토 완료. 새 Bessel계산·sharp interval은 유용하나 실제 nonlinear/heteroscedastic SSL의 핵심 확장은 미해결이다. 기존 원리를 제거하고 남은 새 기여가 부족하다는 판정으로 정리한다. 넓은 uncertainty연구 전체의 불가능성은 아니다.

## 06 — 재현성 감사

내부 문서 링크 누락0개,180predictive rows/60acquisition rows 확인. 정확한 log regret∞인60rows가 별도 flag에 기록됨을 확인했다. 그림의1e−16 machine-roundoff를 눈에 띄는 효과처럼 보이지 않도록 y범위를±1e−12로 표시하고 roundoff라고 명시했다(원자료 불변). 버전 고정 및 n조건간 seed 재사용의 의존성 범위를 추가했다.

## 07 — 원가설 범위 해석 정정

Root가 원자료 tex307/309/687을 다시 대조하여 범위 오류를 지적했다. Owner의 초기 verdict는 “원가설이 family 없이 너무 넓었다”, “원래의 broad impossibility 서사는 유지할 수 없다”라고 썼고, 최초 완료 메시지에도 “원가설 반박”이라고 표현했다. **이는 잘못된 귀속이다.** 원자료는 “예측이 달라질 수 있다”는 존재적 가설이며 보편 불가능성을 명시적으로 배제했다.

원자료를 직접 재확인한 뒤 README/theory/verdict/results와 이 기록을 정정했다. Circle은 이번에 새로 세운 강한 탐색 H1의 반례일 뿐, 원래 가설의 반박이 아니다. Categorical 사례는 원래 가설을 지지하지만 기존 원리의 특수 계산을 넘어서는 기여는 확보하지 못했다. 따라서 판정은 유지하되 기각 근거를 **현재 구체화의 신규성·기여 부족**으로 한정한다. 실행·수치·seed·사전 판정조건은 변경하지 않았다. 더 강한 다른 질문의 성공으로 원래 질문을 대신 해결한 것으로 보고하지 않는다.
