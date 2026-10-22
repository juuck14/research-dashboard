# 재현 안내 — negative feedback 후속 연구

2026-10-22. 모든 아래 핵심 계산과 학습은 실제 실행했다. GPU, 외부 데이터 다운로드, 사전학습 모델이 필요하지 않다. 저장소는 전체 데이터 대신 생성기·seed·작은 모델 배열과 결과표를 보존한다.

## 환경

실행 환경 Python3.12.14,NumPy2.3.5,SciPy1.17.0,Matplotlib3.10.8. 저장소 최상위에서 실행한다. 아래 설치 명령은 재현자를 위한 안내이며, 이번 환경에 새로 설치했다고 주장하지 않는다.

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r negative-feedback/round2/requirements.txt
export OPENBLAS_NUM_THREADS=1
export OMP_NUM_THREADS=1
```

정확한 hardware별 속도는 보장하지 않는다. 원 실행에서 encoder36fork+6warmup은 single-threaded BLAS 약290초였다. 기타 수학/FD/interval 계산은 K128 유한합과 작은 tuple enumeration으로 구성되며 보통 수초~수분 범위다. 재현 환경/선형대수 구현에 따라 시간과 마지막 자릿수는 달라질 수 있다.

## 1. 핵심 정리의 계산 및 그림

```bash
python negative-feedback/round2/theory/code/verify_general.py
python negative-feedback/round2/theory/code/verify_controls.py
python negative-feedback/round2/theory/code/plot_results.py
```

첫 스크립트는 matched-value 정책4개,K1–128,전체 tangent FD32개를 계산한다. 두 번째는 natural/matched ×InfoNCE/DCL ×K1–128과 FD20개다. `theory/results/summary.json`, `denominator_summary.json` 및 CSV가 원자료다. 수식은 `theory/theorem.md`, 실행 전 규약과 변경은 같은 디렉터리의 protocol/progress다. PNG/SVG/PDF 그림은 이 CSV에서 만들어진다.

정상 기준: FD오차<2e-7(관측최대9.04e-11),확률합오차<1e-11,threshold의엄격증가. Natural InfoNCE 첫 stableK5,DCLK8. 이 비교는 double precision이며 다음 독립 interval 인증이 정수 cutoff의 엄밀성을 보강한다.

## 2. 독립 구현·증명 검토·정수 경계 인증

```bash
python negative-feedback/round2/review/audit.py
python negative-feedback/round2/review/control_audit.py
python negative-feedback/round2/review/certify_cutoff.py
python negative-feedback/round2/review/certify_controls.py
python negative-feedback/round2/review/quantile_audit.py
```

Ordered iid tuple 구현은 저자의 count aggregation 코드를 import하지 않는다. 78개 full spectrum 비교의 최대오차5.73e-11이었다. `cutoff_interval_certificate.json`, `control_interval_certificate.json`은70자리 outward Decimal 연산과 명시적 exp/log tail bound로 부호를 인증한다. 정리의 모든K 결론은 interval 한 개가 아니라 인접 K 부호 인증+단조성+full-space 충분조건의 결합이다. Decimal unaryminus 반올림 오류를 발견·수정한 기록은 `review/review.md`에 있다.

## 3. 예측된 population trajectory

```bash
python negative-feedback/round2/dynamics/run.py
python negative-feedback/round2/dynamics/plot.py
```

Primary8101–8102,confirmation8301–8302. K4/5 ×frozen/adaptive ×4초기값=16적분. `dynamics/protocol.md`에서 기준을 실행 전에 정했다. `results/trajectories.csv`에 모든 평가 시점과 실제시간·정규화시간을 저장한다. Expectedadaptivefinalratios exp(3),exp(-3). 관측20.0852와.0497871. Frozen의 극소 수치는 numericalfloor이며 비율 정확도를 과장하지 않는다. `summary.json`의 passed16,runs16,maxnormerror3.75e-13을 확인한다.

## 4. Shared nonlinear encoder

```bash
python negative-feedback/round2/encoder/run_encoder.py
python negative-feedback/round2/encoder/audit_results.py
python negative-feedback/round2/encoder/analyze_results.py
python negative-feedback/round2/review/encoder_audit.py
```

Primary1101–1103,confirmation2201–2203,renderer916. B64,lr.05,warmup1000,fork3000,MLP16→32→8. 두 initialization×3policies×6seeds=36fork. Last세스크립트는 저장 모델을 평가/집계하며 마지막은 독립 pinv OLS와 새 seed150좌표 FD다.

이 학습은 q-weighted **one-negative pair loss**를 배치에서 평균한다. Batch64를 joint63-negative InfoNCE로 해석하면 재현 대상이 달라진다. Frozen snapshot은 매번 같은 새관측배치에 평가되며 가중치는 변하지 않는다. Adaptive와 초기조건·batchstream을 맞춘다.

`encoder/results/models.json`에36최종모델, `models_initial.json`에12초기모델을 저장했다. `runs.json`에는 readout·Gram·Walshenergy·trace,CSV에는평면표, `aggregate.md`에는seed분할집계가 있다. 원 학습 스크립트는 initial heavyprobe와initialmodel을 저장하지 않아 audit에서 동일seed로초기상태를 재구성했다. 원 학습 결과를 바꾸지 않았다.

**의도된 failed endpoint:** warmupprimary1/3,confirmation3/3으로 원래two-of-three각split기준미충족. 이것은 스크립트실패가 아니며, 재현시 성공으로 바꿔야 할 수치가 아니다. OLS는 관측후 고정diagnostic임을progress에 기록했다. Accuracy표의대괄호는6seedmin/max이며confidenceinterval이 아니다.

## 5. Rank rule 및 기존 설명의 직접 통제

```bash
python negative-feedback/round2/quantile/run.py
python negative-feedback/round2/prior-art/audit_checks.py
```

Rank의 exacttie명제와 TIE1e-12수치정책은 다르다. `tie_tolerance_control.csv`에서 delta1e-13의복귀/탈출차이를 확인한다. `prior-art/results`는 K-infinite effective-temperature identity,naturalκ=-1normalmode반례,DCLscalarcontrol,자연log4후속분석을 보존한다. `prior-art/literature_audit.md`는 실제읽은원문섹션과직접환원여부를 명시한다.

## 파일을 읽는 순서

처음에는 [한국어 최종 판정](report_ko.md),[논문 원고](manuscript.md),[정리 전체 증명](theory/theorem.md),[독립 심사](review/review.md),[선행연구 대조](prior-art/literature_audit.md) 순서를 권한다. 원자료·코드·변경 이력은 해당문서의상대링크로 연결된다. 모든 상대 링크를 [기계적 검사](check_artifacts.py)로 확인한다.
