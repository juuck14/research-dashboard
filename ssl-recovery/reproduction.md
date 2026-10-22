# 재현 안내

저장소 root에서 실행한다. CPU, NumPy 2.3.5, Matplotlib 3.10.8, Python 3.12.14를 사용했다. 학습에 Torch·autograd·GPU는 필요 없다. 정확한 8-state expectation이므로 training data 다운로드는 없다. 아래 seed는 초기값 seed이며 dataset 반복이 아니다.

```bash
python3 -m pip install -r ssl-recovery/requirements.txt
export OPENBLAS_NUM_THREADS=1
export SSL_RECOVERY_RAW_DIR=/tmp/ssl-recovery-raw
python3 ssl-recovery/code/run_population.py --phase pilot
python3 ssl-recovery/code/run_population.py --phase confirmation
python3 ssl-recovery/code/run_spectral_control.py
python3 ssl-recovery/code/run_contrastive_control.py
python3 ssl-recovery/code/run_long_equal.py
python3 ssl-recovery/code/summarize.py
```

원 실행은 stdout를 `results/*_stdout.log`로 redirect했다. Elapsed seconds와 platform 문자열은 환경에 따라 달라진다. Full trace는 `SSL_RECOVERY_RAW_DIR`에 생성하고 SHA·크기·행수와 compact CSV를 저장소 results에 쓴다. Compact는 모든 run에서 500 step 간격과 final을 보존한다. 50 step 간격으로 측정한 threshold와 모든 run의 final metric은 summary JSON에 별도로 보존한다. Full raw가 없어도 명령으로 재생성할 수 있다.

`run_population.py`는 법칙의 marginal/correlation과 analytic gradient의 중앙차분을 검산한다. `run_contrastive_control.py`는 별도 gradient 검산을 한다. 독립 검토의 명령과 코드는 [review 폴더](../prevalidation-20261022/reviews/recovery/protocol.md)에 있다. 이 명령은 문헌의 전체 실험을 재현하는 것이 아니라 이번 작은 모형의 직접 검증이다.

명령별 실제 elapsed time은 pilot 약 45초, confirmation 55초, spectral 68초, contrastive 50초, long-equal 65초였다. 동시 실행과 환경에 따라 변하며 GPU 비용은 없다.

## 파일 역할

- `protocol.md`: 실행 전 가설·모형·판정 기준과 후속 amendment.
- `theory.md`: 직접 증명과 범위, scalar/sphere metric 구분.
- `literature.md`: 실제 확인한 원문·정리·한계.
- `results/*_summary.json`: 모든 run의 최종값·회복 threshold·실행 검산.
- `results/*_curves.csv`: 모든 run의 고정 간격 곡선.
- `results/*_trace_manifest.json`: full raw의 SHA256·바이트 수·행수·경로.
- `results/environment.json`: 실행 환경.
- `code/`: 실제 사용한 학습·개입·요약 코드.
- `verdict.md`: 현재 구체화의 기각 근거와 재개 조건.

원문 PDF, 대형 데이터, model checkpoint는 저장하지 않았다. 실험의 주장은 noisy linear accessibility에 한정한다. Threshold 미도달을 정보 소실이나 영구 학습 불가능으로 읽지 않는다.
