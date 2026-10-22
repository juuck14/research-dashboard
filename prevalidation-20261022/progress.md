# 진행 기록

## 00 — 원자료 및 기존 기록 확인

- 실행: 현재 보고서 파일 읽기, GitHub README·전체 트리 확인, 로컬 clone 및 기준 commit 확인.
- 관측: 기존 저장소는 다른 세 후보의 연구를 이미 포함한다. 이번 번호와 대상이 달라 별도 디렉터리를 사용한다. 기존 Gaussian 부분 식별과 선형 EMA 분석은 가까운 경쟁 설명이므로 재검증 대상이다.
- 현재 판단: 세 후보 모두 미판정. 이전 추천은 증거로 세지 않는다.
- 다음: 독립 담당의 원문 재검증·정식화·실행 전 설계, 직접 계산 및 실험.

## 01 — 독립 분석·실행 및 첫 반론

- 3개 독립 주제 담당과 3개 별도 비판 검토자가 실제로 작업했다. Root가 추가로 circle pair-law의 local KL 분석을 수행했다. 역할은 각 코드·review 기록에서 확인할 수 있다.
- 후보1: exact finite-state nonlinear 학습을 실행했다. 초기 회복 실패를 새 고착으로 해석하기 전에, equal cross-view spectrum에서 모든 factor allocation이 같은 agreement optimum이라는 대안 설명을 발견했다. spectral contrast와 contrastive control로 후속 검증 중이다. 선형 EMA의 기존 Tian2021 환원을 재기여로 세지 않는다.
- 후보2: well-conditioned TypeS reference의 weak-anchor가 작아질 때 같은 관측법칙의 45° 다른 설명이 허용되는 직접 반례와 독립 계산을 확보했다. 고정 g0의 pointwise continuity를 반박한 것은 아니다. continuous anchor margin을 넣은 제한 family의 positive bound를 추가 분석 중이다.
- 후보3: unknown scalar vMF transition은 전체 Fourier 법칙에서 joint identifiable한 제한 모형을 직접 증명했다. categorical confounding은 별도 family에서 정확하지만 고전 결과와 가깝다. Root는 equal-channel 지점의 KL t⁴/t⁶ 및 15 population 조건과 1.57M pair oracle 검정을 실행했다. 이 rate 구분도 고전 singular likelihood 이론과 직접 대조했다.
- 출판: 초기 지침·대상 mapping을 commit `aa676e87d142eec69a5ce49d5a197a504f40d766`으로 main에 반영·성공 확인했다. 첫 시도 중 다른 연구의 동시 commit을 감지해 그 commit을 parent/base로 다시 만들었다. 기존 negative-feedback round2 기록을 보존했으며 force push는 하지 않았다.
- 현재 판단: 전부 최종 미판정. 결과 자체와 독립 연구의 신규성은 구별한다. 다음 작업은 강화된 정리의 타당성, 실험 대안 설명, 직접 선행과의 중복을 가른다.
