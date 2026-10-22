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
