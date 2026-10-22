# 증거와 역할 목록

| 역할 | 실제 작업 | 기록 |
|---|---|---|
| recovery_study | nonlinear SSL, checkpoint 개입, spectral/contrastive/장기 대조, 직접 증명 | [후보1](../ssl-recovery/README.md) |
| mechanism_study | TypeS 정식화, same-law/fixed-base/positive theorem/surrogate 직접 분석·실행 | [후보2](../mechanistic-stability/README.md) |
| uncertainty_study | PCL 대조, vMF identification, categorical sharp set·표본·acquisition 실행 | [후보3](../pair-uncertainty/README.md) |
| recovery_review | 원문 collision, 별도 gradients·stationarity·Jacobian·metric 비판 | [검토1](reviews/recovery/review.md) |
| mechanism_review | GL basis·all-support audit·가정 삭제·weighted surrogate, 증명 비판 | [검토2](reviews/mechanism/review.md) |
| uncertainty_review | 고전 latent/singular/replicate 대조, 별도 Fourier·FFT·acquisition 감사 | [검토3](reviews/uncertainty/review.md) |
| Root | 원자료·기존 repo 범위 확인, singular KL 증명·표본 실행, 교차 범위 감사, 종합·출판 | [별도 계산](operational-uncertainty/analysis.md), [종합](final_report.md) |

## 네 종류의 증거

- **외부 문헌 확인:** 각 literature/review에 실제 읽은 절·정리·식과 링크를 기록했다. 원문 미확보인 Jeon2025·접근 차단된 일부 world-model 항목은 결정적 근거로 쓰지 않았다.
- **직접 도출:** 제한 모형의 명제는 theory/positive_bound/exact_identification/analysis에 완전 증명 또는 명시적 증명 범위를 남겼다. 기존 원리의 구체 계산을 신규 일반 정리로 주장하지 않는다.
- **직접 실행:** 코드·protocol·설정·seed·원자료 CSV/JSON·그림·환경을 연결했다. 실패한 해·예외·초기 clipping 정정·생략한 LRT도 보존했다.
- **미검증 가설:** general nonlinear recovery state, general TypeS stability와 learned-candidate bridge, learned-mean/heteroscedastic SSL query는 verdict에서 미해결로 표시한다.

## 문헌 범위와 서지 감사

각 주제의 결정적 직접 선행은 [1](../ssl-recovery/literature.md), [2](../mechanistic-stability/literature.md), [3](../pair-uncertainty/literature.md)과 독립 review에 있다. 2026-10-22까지 공개된 가까운 원문을 우선했다. 출판본·version이 고정된 preprint·초록만 확보한 항목을 구분했다.

Root가 추가로 기존 보고서의 Xue et al.2023 공식 PDF §5 Theorem5.1/5.4와 LeJEPA2026 §5.3/AppendixC를 다시 확인했다. 전자는 feature suppression이 embedding dimension뿐 아니라 augmentation 조건에도 의존함을 다루고, 후자는 Gaussian/OU·whitening 아래 orthogonal target의 근사 식별이다. 어느 것도 이번 일반 mechanistic theorem이나 neural trajectory 전체를 이미 해결했다는 근거로 쓰지 않았다.

기존 보고서의 Explicit Concentration2024 및 Variational Contrastive Learning2025는 arXiv 서지·초록을 Root가 재확인했지만 이번 검증에서는 본문을 다시 읽지 않았다. 현재 결과의 신규성 기각을 이 두 논문에 의존하지 않는다. 후보2에서 이번에 선택하지 않은 rare-support/noise 하위 경로 및 다른5개 연구 후보의 모든 인용을 새로 전수 감사한 것은 아니다. 이를 세 주제 전체의 선행이 완전히 소진됐다는 주장으로 확대하지 않는다.

날짜 정정: Robustness of Nonlinear Representation Learning은 ICML2024이며 arXiv2025와 다르다. Self-Normalized Resets는 최초2024·v3수정2025를 확인했고 HTML 내부 표기만으로2026신규 출판이라 하지 않았다. UPCC2026는 공개 preprint로 다뤘으며 본문의 venue 표기만으로 학회 채택을 확인했다고 쓰지 않았다.
