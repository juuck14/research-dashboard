# 실행 이력

- 2026-10-22: protocol 작성 후 최초 실행. Bessel derivative의 scalar/vector broadcasting 오류로 결과 계산 전 종료(`(3,64)`와 `(3,)`). `[:,None]`으로 shape를 명시해 수정했다. 가설·조건·판정 기준 변경은 없다.
- 수정 후 완료: 15 population 조건, 6 integration convergence 조건, discrete-convolution/Taylor 검산, primary/confirmation oracle LRT 24행(총48 datasets, 1,571,928 pair). 사전 cap을 넘긴 4조건은 이유를 남기고 생략. 명제와 수치 일치, generic singular-likelihood 이론의 강한 신규성 반론을 확인했다.
- 최종 시각 QA에서 PNG의 마지막 checksum이 불완전함을 확인했다. 저장된 population CSV만 읽는 plot.py로 그림을 다시 만들고 atomic rename을 사용하도록 저장을 수정했다. 수치 결과·가설·조건은 바뀌지 않았다.
