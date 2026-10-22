# 첫 실행 보존과 측정 정정

원래 `repeat_log_regret`는 예측 probability를1e−15로 floor한 값이었다. 무한대인 정확한 log regret를 유한한 proper-score 결과처럼 읽을 위험이 있어 protocol Amendment1에서 정정했다. 이 디렉터리는 초기 숫자와 열이름을 그대로 보존한다. 최신 결과는 상위 results에 있고 clipping 여부·정확한 무한대 여부를 구별한다. 가설이나 조건을 바꾸어 좋은 결과를 찾은 재실행이 아니다.
