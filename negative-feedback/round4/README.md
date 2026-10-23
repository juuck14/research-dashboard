# 중요성 공백과 가정 강도의 재검증

2026-10-23. **상태: 이번 분석·실험 완료. 현재 판정은 ‘추가 핵심 연구 필요’이며 이전 최상위 핵심50% 판정은 철회했다.** [정정 이유](../ASSESSMENT_CORRECTION.md).

[최종보고](report_ko.md) · [재현](reproduction.md) · [실행 기록](progress.md) · [별도 복사본 재실행](recheck.json)

이번 회차는 또 하나의 예제나 정확한 식을 확보해 중요성이 해결됐다고 선언하는 작업이 아니다. 수학적으로 신뢰할 만한 제한적 이론과, 중요한 학습 현상에 대한 설명 사이의 간격을 직접 검사한다.

## 분리된 작업

- `value_audit/`: 이전 중요성 논증의 논리적 간격과, normal-view 불안정성이 곧 품질 저하가 아닌 실제 반례.
- `assumptions/`: 조건부 균형이 깨진 일반 affine direction의 정확한 field, stationarity와 curvature의 구분, count 공통 reference가 요구하는 조건.
- `nonoracle/`: 잠재 요인으로 평형점을 구성하지 않고 충분 차원의 random embedding에서 학습. 같은 목적·정보를 유지하고 어떤 geometry에 접근하는지 검사.

각 담당은 protocol을 결과 전에 기록하고, root가 해석과 최종 판정을 통합한다. 중요한 결과가 나오더라도 top-journal 중요성 충족은 별도로 판단한다. 최초 user 비판의8항목은 최종 응답에서 삭제하지 않고 대응한다.

## 판정 원칙

1. 주정리의 정확성은 유지/오류 발견 여부로 따로 평가한다.
2. 일반 score law라고 부르는 것이 generic representation direction을 뜻하지 않는다.
3. Frozen과 adaptive, 국소 안정성과 finite-time 접근성, noiseless 접근성과 noise-dependent 성능을 구분한다.
4. Non-oracle 실험에서 예측과 연관된 현상이 나와도 finite-state population 실험의 범위를 넘기지 않는다.
5. 기존 국소 geometry를 특정 task에서 선호하도록 새 평가를 설계했다는 사실만으로 중요성이나 해로움을 입증하지 않는다.


## 이번에 실제로 확보한 것

- [가정 분석](assumptions/README.md): 모든K에서 같은 reference가 stationary인 조건과 conditional balance의 동치, 일반 미분식과 작은 비대칭의 drift/slope 차이.
- [온도·정책 범위](temperature_scope.md): loss와 raw-score sampler의 무차원 반응 강도 t*tau, 반대 exponential 선호의 제한적 직접 따름정리.
- [비 oracle 접근성](nonoracle/README.md): d16의 무작위 free embeddings에서 실행한 두seed 모두K8 square근방에 도달. K16은 미수렴이며 범용 수렴·shared-network 결과가 아니다.
- [품질 반례와 가치 감사](value_audit/README.md): 불안정 방향에서도 의미 선형 접근성 보존/정보 추가, positive-consistent task의 비중에 따른 utility 역전. 이 반례들 역시 새 top-journal 기여가 아니다.

**최종 해석:** Oracle-only 반론은 작은 모형에서 일부 해소됐지만 중요한 학습목표와 연결되는 공백은 미해결이다. 신규성 후보와 기술적 신뢰도를 중요성의 대체물로 사용하지 않는다. 이전 top50 판정은 복구하지 않았다.
