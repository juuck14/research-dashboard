# 재현 안내와 완료 범위

저장소 root를 기준으로 한다. CPU Python3.12.14, NumPy2.3.5, SciPy1.17.0, Matplotlib3.10.8. 각 주제 requirements와 environment가 실제 실행환경을 기록한다. Torch·GPU·외부 dataset이 필요한 실행은 없다. [공통 환경](environment.json).

실험 설계와 seed는 각 protocol에 있으며 추가 실행은 amendment에 기록했다. 이미 통과한 실험을 benchmark 규모로 확대하지 않았다. 아래는 실제 사용한 실행 명령이며 전체 재실행은 결과 파일을 재생성한다. Elapsed time·OS 문자열·부동소수점 끝자리는 달라질 수 있다.

## 후보1

[상세 명령](../ssl-recovery/reproduction.md). `run_population.py --phase pilot`, `--phase confirmation`, `run_spectral_control.py`, `run_contrastive_control.py`, `run_long_equal.py`, `summarize.py`를 실행했다. 정확한 population expectation을 사용하고 seed는 network 초기값이다. Full trace는 `SSL_RECOVERY_RAW_DIR`에 쓰며 repo에는 전체 run의 summary·고정간격 curve와 SHA manifest를 보존한다. 대형 checkpoint는 없다.

## 후보2

[상세 명령·결과](../mechanistic-stability/results.md). 해당 디렉터리에서 `code/run_study.py`, `surrogate_check.py`, `positive_check.py`, `fixed_base_check.py`, `surrogate_preference.py`, `low_overlap_surrogate.py`를 각각 실행했다. 이들은 exact construction과 수치 감사이며 neural autoencoder training이 아니다.

## 후보3

```bash
OPENBLAS_NUM_THREADS=1 python3 pair-uncertainty/code/run_study.py
OPENBLAS_NUM_THREADS=1 python3 pair-uncertainty/code/acquisition_check.py
OPENBLAS_NUM_THREADS=1 python3 prevalidation-20261022/operational-uncertainty/run.py
```

Root의 figure만 재생성하려면 `operational-uncertainty/plot.py`를 실행한다. Root run은 사전2M pair cap을 지켰으며 생략한 LRT 조건은 summary에 명시한다. Exact log regret∞와 clipped diagnostic을 구분한 수정 전 파일도 보존했다.

## 독립 검토

- [후보1 protocol·명령](reviews/recovery/protocol.md): 원 loss를 별도로 미분해 gradient와 flat optima·Jacobian을 검사했다.
- [후보2 protocol·명령](reviews/mechanism/protocol.md): 별도 row-direction·nonlinear lift, 모든 C support에 대한 finite-threshold 계산, 가정 삭제 반례, weighted surrogate를 검사했다.
- [후보3 protocol·명령](reviews/uncertainty/protocol.md): 별도 emission enumeration·Gram orbit·Bessel series, FFT convolution, acquisition simulator로 검사했다.

같은 코드에서 seed만 바꾼 것을 독립 구현으로 세지 않았다. LRT 행수 감사는 그 표본을 별도로 재생성한 실험과 구별한다.

## 최종 확인

코드 구문 검사, Markdown 내부 링크 검사, 모든 PNG의 checksum 검사와 주요 그림의 시각 확인을 수행했다. [QA 기록](qa.json)에 결과를 남겼다. 이 확인은 새로운 과학적 반복실험의 수가 아니다.

이번 연구의 지속 실행 process는 없다. 다음 세션은 [최종보고](final_report.md), 각 verdict, protocol과 원자료에서 이어갈 수 있다. 현재 남은 것은 권한·package 설치가 아니라 연구 문제다.
