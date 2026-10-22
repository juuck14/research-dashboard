# 독립 검토 실행 이력

- 지침 및 주담당 protocol을 읽고 별도 protocol 작성. 고전 moment/label-noise/replicate/singular likelihood 원문 대조.
- `independent_check.py` 실행 성공: 1201개 categorical orbit, 42개 Bessel 점근 계산. 증명과 수치 확인을 분리했다.
- `owner_audit.py` 최초 실행은 enumeration을 통과한 뒤 CSV 경로 root가 한 단계 높아 FileNotFoundError로 종료. `HERE.parents[3]`를 `[2]`로 정정했다. 모형·수식·seed·기준 변경 없음. 재실행 결과는 results/owner_audit.json에 기록한다.
