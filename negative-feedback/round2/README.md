# Negative feedback — 논문의 핵심 결과를 확보한 후속 단계

2026-10-22. **최종 판정: 검증된 수정 방향으로 진행.** 현재 표현에 의존하는 negative 정책의 일반적인 정보 삭제 논문이 아니라, negative 수와 sampling 반응이 만드는 정확한 국소 안정성 법칙을 중심으로 한 이론 논문이다.

## 읽는 순서

1. [쉽게 풀어 쓴 한국어 최종보고](report_ko.md)
2. [실제 증명·분석·실험을 연결한 논문 원고](manuscript.md)
3. [논문을 무너뜨릴 질문과 실제 판정](decisive_questions.md)
4. [코드·환경·명령·seed·결과 재현 안내](reproduction.md)

## 확보한 중심 결과

일반적인 smooth positive score sampler의 전체 product-sphere tangent spectrum을 모든 negative 수 K에서 도출했다. Balance mode는 `lambda=C_K*(T_K-eta)`,C_K>0이며 T_K가 K에 따라 엄격히 증가함을 증명했다. 추가적인 정책 값 조건 아래 이 부호가 모든 비회전 방향의 안정성을 결정한다.

자연적인 exponential 정책 omega(s)=4^(-s),uniform floor epsilon=.3에서는 다음 경계를 증명하고 독립 interval 계산으로 인증했다.

| 동일 정책의 loss | 불안정 | 전체 공간에서 안정,회전 제외 |
|---|---|---|
| InfoNCE | K≤4 | 모든 K≥5 |
| DCL | K≤7 | 모든 K≥8 |

이 전이가 가능한 열린 매개변수 영역도 증명했다. Exact population dynamics16건에서 예측한 불균형 성장/수축을 실제 확인했다. Generic feedback product rule,same-q/다른 slope 구성,K∞의 effective-temperature 환원은 신규 기여로 주장하지 않는다.

## 반박 검토와 실패 결과

- 독립 ordered-tuple 구현78개 full spectrum 검산 최대오차5.73e-11. 70자리 outward interval로 네 정수 cutoff 인증.
- Shared nonlinear MLP36fork 학습은 약한 요인 energy를 크게 압축하고 지정한 feature noise 아래 접근성을 낮췄다. 그러나 원래 큰 clean/noisy loss 기준은 primary1/3,confirmation3/3으로 실패했다. 이를 성공으로 바꾸지 않았다.
- OLS가 PCA 초기화의 clean factor access를 상당히 회복하므로 완전 정보 소실을 주장하지 않는다.
- 다른 natural 정책에서는 balance가 안정해도 normal mode가 불안정했다. 충분조건 없는 전체 안정성 주장은 배제했다.
- Exact rank tie 정책과 finite-tolerance 구현은 infinitesimal 안정성이 다르다. 이 반론을 실제 계산하고 문서를 수정했다.

## 산출물

| 디렉터리 | 담당과 근거 |
|---|---|
| [theory](theory/README.md) | 여섯 정리·증명,1,024개 count/policy/loss 설정,52 paired tangent 검산 |
| [review](review/README.md) | 독립 증명 재도출·tuple oracle·interval·150-coordinate encoder 감사 |
| [prior-art](prior-art/README.md) | 가장 가까운 원문 정리 대조,기존 설명의 직접 환원·반례 |
| [dynamics](dynamics/README.md) | Natural K4/5의 사전 규약·실제 population 적분16건 |
| [encoder](encoder/README.md) | Continuous nuisance+shared MLP36run,실패 gate,readout/OLS/energy 자료 |
| [quantile](quantile/README.md) | 별도 one-sided rank 증명과 tolerance 반례 |

[진행 및 변경 이력](progress.md),[환경 의존성](requirements.txt),[산출물 검사](check_artifacts.py)를 함께 제공한다. 이전 단계 결과와 실패 가설은 원래 디렉터리에 보존했다. 현재 핵심 주장을 판단하기 위해 기다리는 필수 외부 GPU 실행은 없다. 자연 이미지나 일반 pretrained encoder에 대한 주장으로 넓힐 때는 별도의 핵심 검증이 필요하다.
