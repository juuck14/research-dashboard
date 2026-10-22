# Negative feedback second research stage

시작일 2026-10-22. 앞선 수정 후 진행 판정은 독창성과 중요성을 확정한 결과가 아니며, 이번 단계에서 다시 검증한다.

## 결정적인 불확실성

1. 정확한 contrastive spectrum이 기존 performative/self-paced 이론의 작은 예제에 그치는가.
2. Sampler 값과 국소 감도를 구분해 일반 smooth filtering 및 negative 수 K에 대한 새로운 검증 가능한 법칙을 얻을 수 있는가.
3. Square/lookup geometry가 현상을 만드는 것인가. 비선형 encoder나 uniform warmup 이후의 tetrahedral geometry에서는 사라지는가.
4. Rank/quantile filtering 같은 다른 해석 가능한 규칙에도 예측이 적용되는가.

## 작업 분담

- theory/: 일반 score filter, 모든 K의 정확한 임계값과 가능한 전체 tangent spectrum.
- prior-art/: 가장 강한 선행연구와 기존 설명에 의한 반증.
- encoder/: 사전 규약에 따른 nonlinear encoder 학습, warmup geometry 및 readout 비교.
- quantile/: root의 rank-filter 분석과 실행.

Root가 최종 판정과 GitHub commit/push를 담당한다. 미실행 항목을 결과로 쓰지 않는다. 이번 판정은 진행, 검증된 수정 방향으로 진행, 또는 기각이다. 핵심 판단이 남으면 완성을 선언하지 않는다.
