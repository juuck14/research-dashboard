# 독립 검토 실행 이력

- 지침 및 주담당 protocol을 읽고 별도 protocol 작성. 고전 moment/label-noise/replicate/singular likelihood 원문 대조.
- `independent_check.py` 실행 성공: 1201개 categorical orbit, 42개 Bessel 점근 계산. 증명과 수치 확인을 분리했다.
- `owner_audit.py` 최초 실행은 enumeration을 통과한 뒤 CSV 경로 root가 한 단계 높아 FileNotFoundError로 종료. `HERE.parents[3]`를 `[2]`로 정정했다. 모형·수식·seed·기준 변경 없음. 재실행 결과는 results/owner_audit.json에 기록한다.
- `owner_audit.py` 재실행 성공: explicit latent144조건 및 CSV60datasets/180predictions 확인.
- `root_audit.py` 실행 성공: 별도 FFT convolution 18조건으로 KL 검산. 상대오차 t⁴≤1.01e−11, t⁶≤3.36e−10. LRT24행=48truth datasets, pair 합계1,571,928 확인. 새로운 LRT 표본을 생성한 것은 아니다.
- 해석 정정: Root의 원보고서 tex 대조 후 ‘원가설 반박’을 ‘조사 중 강화한 보편 H1 반박’으로 고쳤다. 원보고서의 existential uncertainty ambiguity는 categorical branch로 지지되며 vMF 주입성이 반박하지 않는다. 수치 및 신규성 때문에 기각하는 판단은 바뀌지 않았다.
- `acquisition_audit.py` 실행 성공: owner60행 및 summary 오차0; inverse-CDF mod3 offset 별도구현+새seeds7501–7506으로 n10000/100000 총12datasets 실제 반복. n100000 mean±sampleSD a=.800397±.001768,b=.250148±.003284, positive-only plugin 구조폭=.600144±.001933. 독립 repeat 원리 확인이며 신규성 반론은 남는다.
