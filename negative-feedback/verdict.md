# 판정

## 담당자 판단: 수정 후 진행

원래의 task-relative false-negative 일반론이나 새로운 mining 방법은 독립 주제로 추천하지 않는다. 또한 무제약 dot-product 모형에서 soft filtering이 positive-invariant factor를 영구적으로 배제한다는 최초 기제는 직접 반박됐다.

다만 normalized full-capacity sphere에서 **matched frozen sampler의 안정점을 adaptive sampler의 반응이 factor-selective하게 불안정하게 만드는 조건**은 exact proposition과 독립 수치 검산으로 확보했다. 이를 수정된 핵심 질문으로 삼아 연구를 더 진행할 실질적 근거가 있다. 이 판정은 generic performative sign flip 자체의 신규성을 인정한다는 뜻이 아니다.

## 확보한 증거
- 직접 완전 증명: 무제약 available-coordinate 모형의 transverse escape와 finite-time bound.
- 직접 완전 유도 및 critic 검산: K1 full-sphere square의 전체 tangent spectrum, frozen-stable/adaptive-unstable parameter 영역.
- 직접 실행: base 1,080 설정, normalized 672 설정, K<=16 exact expectation105 설정, importance control90 설정. 확률적 성공률이 아니라 정확한 모집단 계산의 설정 반복이다.
- 독립 critic: d3/d4 full sphere flow 및 Jacobian, K2/K4 exact full tangent 검산.

## 가장 큰 위험
Perdomo2020의 decision-dependent learning 및 Jiang2025의 hard-negative/collapse 분석을 접목한 작은 예제로 끝날 수 있다. 원래 보고서의 '이유가 다르니 새롭다'는 평가는 유지하지 않는다. 독립 논문의 공백은 SSL-specific sharp spectrum과 그 외삽 예측력에서 확보해야 한다.

## 착수 후 첫 작업
1. K-general full-sphere spectrum을 count moments로 정리하여 K1 특수성을 제거한다.
2. 후속 검증에서 비퇴화 positive 채널과 toy SGD는 확인됐으므로, 이제 실제 filtering 한 규칙과 비대칭 요인에서 stationary point와 spectrum이 어떻게 바뀌는지 먼저 예측한다. 결과가 계속 좋은 설정만 고르는 방식은 사용하지 않는다.
3. 그 경계가 기존 performative/generalized self-paced objective 결과의 즉각적인 corollary인지 원문 정리별로 대조한다. 즉각적 적용이거나 augmentation에서 특별한 가정 없이는 설명력이 없어지면 수개월의 독립 주제로는 기각한다.

paper_draft.md는 이미 있는 증명과 계산에만 의존한 연구 노트 뼈대다. 자연 이미지 성능, 일반 회복 정리, finite-time 정보 소실 등의 없는 결과는 넣지 않았다.

## Root 후속 확인

세 요인·d8 full-capacity, bit-flip positive channel, 실제 minibatch lookup SGD를 별도 사전 규약으로 추가 실행했고 독립 감사를 통과했다. [종합보고](../coordination/final_report.md)와 [후속 원자료](../review/robustness-extension/README.md) 참조. 이 추가 근거는 identity-positive·pure population·제한 차원이라는 반론을 줄인다. 실제 이미지 encoder나 일반 filtering의 신규 기여까지 확정한 것은 아니다.
