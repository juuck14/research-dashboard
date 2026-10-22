# 연구 진행

## 2026-10-22 시작
- 계획: exact population factor model로 feedback-induced stable omission을 먼저 반증한다.
- 실행: primary PDF 7개 retrieval; hard-negative geometry 2311.05139 PDF는 retrieval 실패여서 대체 원문 찾는 중.
- 분석: 동일-instance positives에서 누락 factor의 2차 방향 gradient는 모든 full-support q에서 escape 방향이라는 짧은 증명을 발견. protocol 작성 후 수치 검증 예정.
- 가장 큰 반론: 너무 단순한 additive separated encoder 및 identity positives가 현상을 없앤 것일 수 있음. 모형 밖 일반 불가능성을 주장하지 않는다.

## 2026-10-22 base 실행 완료
- 직접 관측: exact population1080 설정/초기값 반복, 확인 seed540, 모든 run이 derived deadline 내탈출. sample-based probability evidence가 아님.
- gradient checker max absolute error3.92e-11. finite solver settings 코드/summary 보존.
- 같은 setting eps.01,w1약2,w2약1e-6: uniform hitting23.037, easy κ-8 adaptive2285.163/frozen2285.179, hard κ8 adaptive11.623/frozen11.581.
- 판단 변경: 초기 permanent exclusion 기제는 unconstrained model에서 반박. finite horizon 실패는 대부분 q exposure timescale.
- reviewer 반론: normalized setting은 append direction을 허용하지 않는다. 두 factor 충분차원과 무제약 norm은 다르다.
- 후속 계획: N1 amendment 작성 후 normalized symmetric point의 frozen-vs-adaptive curvature 계산 및 trajectory 실행. 별도 모형이며 base 결과 보존.

## 2026-10-22 N1 및 N2 완료
- N1 direct analytic Jacobian vs finite-difference error1.12e-10,672 exact-flow 설정. eps.1,kappa-2에서 frozen curvature+.18795/adaptive-.21866. frozen-at-initial도 양요인 유지, adaptive는한요인 amplitude가약3e-10으로감소(t200). finite-time 정보소실이라고주장하지않음.
- 독립critic: d3/d4 full sphere tangent에서 matched-frozen stable modulo rotations, adaptive1unstable 확인. closed-form spectrum도독립유도하여 theory Prop5로정리.
- reviewer 반론 해결: one-negative artifact? N2 K1,2,4,8,16 exact multinomial105조건, 핵심signflip전부유지. probabilitysumerror3.55e-15. criticK2/4 fullsphere검산도성공.
- 대안설명 통제: importance correction90설정으로 uniform field복구오차1.39e-15. 따라서same-uniform-objective optimization failure로쓰지않음.
- 신규성반론: PerformativePrediction의generic chainrule 현상. 다만 full-sphere SSL-specific exact phase boundary는 별도결과. 독립논문으로충분한학술적차이는아직정밀대조가필요.

## 2026-10-22 독립 검토 반영과 판정
- critic은 fullsphere K2/K4 및 no-selfnegative에서도 차이를 확인. root는 별도 사전protocol로3factor수치확인. owner 결과에 합쳐 단일 성공률처럼 세지 않음.
- 최신SnaPhArd ICLR2026 원문대조: fixed-key query collapse와 factor collapse의 의미차이를 기록.
- 담당판정: 수정후진행. 다만 generic performative instability 이상의 학술적새로움은 남은위험이며, 이견은 root종합판정에보존한다.
- 저장: paper_draft.md는 실제결과만포함. verdict.md와 results/experiment_report.md 연결.
