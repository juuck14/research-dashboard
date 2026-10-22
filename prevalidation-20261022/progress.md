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

## 02 — 직접 검증과 최종 판정

- 후보1의 원 설정 장기 continuation·InfoNCE 대조·독립 gradient와 metric 감사를 완료했다. 낮은 접근성만으로 영구 고착을 주장할 수 없고, flat agreement optimum이라는 강한 대안 설명이 있다. 현재 구체화 기각.
- 후보2는 제한 positive theorem의 완전 증명·800 B의 all-support 독립 감사, fixed-base 새 support 반례, strong/low-overlap surrogate의 잘못된 global preference 예를 추가했다. 단순 integer-gap 안정성은 반박되지만 일반 quantitative margin과 실제 학습으로의 연결은 미해결. 담당·검토자 모두 판정 보류로 갱신.
- 후보3는 pair sharp set·표본·3n acquisition 예산 대조와 별도12dataset 확인, Root KL의 독립 FFT 검산을 완료했다. 원래 존재적 가설을 강화된 보편 가설로 잘못 부른 부분을 원자료와 대조해 정정했다. 원 가설은 지지되지만 현재 결과의 독립 기여 폭이 부족해 현재 구체화 기각.
- 독립 검토에서 지적된 scalar/sphere metric 혼용, log regret∞ clipping, chain-rule 방향, 원가설의 범위 오류를 수정하고 이전 해석·실행 파일을 보존했다.
- 실험·중간 검토의 첫 묶음109files를 `6dc82e042d4d3bd6d6cfe7330074e56846455e73`으로 main에 반영하고 ref를 다시 읽어 성공 확인했다. 다른 연구의 동시 commit을 parent/base로 보존했다.
- 최종 종합보고·재현·증거 목록·후보2 연구 노트를 작성했다. 코드 구문·Markdown 내부 링크·PNG checksum와 주요 그림의 시각 확인을 수행했다. 최종 출판은 별도 commit과 remote ref 검증으로 마무리한다.
- 계속 실행 중인 연구 process는 없다. 다음 실행의 출발점은 final_report와 각 verdict이며, 미완료 핵심을 완료했다고 표시하지 않았다.
