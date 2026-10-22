# 독립 공격·재심과 재현

상태:2026-10-22 최종 원고 재심 완료. **수정된 국소 population 이론 논문의 핵심50% 확보**로 판정했다. 원래 의미 정보 소실이나 일반 학습 cutoff 논문에 대한 판정은 아니다. [최종6-gate 심사](final_review.md)는 최초 반대와 판정 변경 이유, 성공·실패·남은 제한을 분리한다. [원고 전의 중요성/범위 부분 충족 판정](pre_manuscript_verdict.md)은 수정하지 않고 별도로 보존했다.

## 직접 확인한 근거

- [사전 kill questions와 실행 기준](protocol.md), [round2 최초 공격](initial_critique.md).
- [직접 읽은 원문과 새 지식의 경계](source_audit.md). Title/abstract만 확인한 원문, 구버전만 읽은 경우, final PDF 접근 실패도 구분했다.
- [다중·연속 점수 법칙의 독립 증명 전개](multilevel_proof_audit.md).
- [View window와 일반 normal block 증명·코드 검토](window_proof_audit.md).
- [Coarse endpoint 및 open local basin 검토](coarse_endpoint_audit.md).
- [Nonlinear endpoint ordered-tuple 검산](endpoint_check.json), [pair-matched negative law 검산](correlation_check.json).
- [별도 exact-rational interval 인증](window_certificate_check.json), [zero-self-positive cycle 인증](cycle20_certificate_check.json).
- [Standard ODE 실제 재실행](standard_ode_recheck.json). 저자 gradient source를 재실행한 것이며 독립 gradient 구현으로 포장하지 않는다.
- [실패한 heterogeneous-anchor 반례 검색](anchor_mixture_check.json). 반례를 찾지 못한 것이 가정 확장 증명은 아니다.

## 실행

Repository root에서 Python3, NumPy와 SciPy로 실행한다. Exact-rational certificate 두 개는 표준 라이브러리만 사용하며, cycle 파일은 이 디렉터리의 독립 Bound 클래스만 import한다.

```bash
python negative-feedback/round3/review/endpoint_check.py
python negative-feedback/round3/review/correlation_check.py
python negative-feedback/round3/review/window_certificate_check.py
python negative-feedback/round3/review/cycle20_certificate_check.py
python negative-feedback/round3/review/anchor_mixture_check.py
python negative-feedback/round3/review/standard_ode_recheck.py
```

Endpoint/correlation 검산은 담당자가 고정한 root/partition 값을 입력으로 읽지만, 그 담당자의 field/count 코드를 import하지 않고 ordered tuple field를 직접 구성한다. Exact-rational code는 프로젝트의 과학 코드나 기존 interval arithmetic을 import하지 않는다. 정리 검산, 코드 재실행, 독창성 판단, 중요성 판단은 서로 다른 증거다.

이 담당자는 원고를 직접 수정하거나 Git/API로 게시하지 않았다. 통합·외부 저장은 root 담당이다.
