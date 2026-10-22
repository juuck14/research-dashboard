# 독립 교차검토: 근사 독립성과 약한 환경에서의 부분 식별

검토일 2026-10-22. 검토자는 주제 제안/실행 담당과 별개다. 검토 범위는 owner의 `protocol.md` 및 선형 Gaussian 회전 분석이다. 독립 코드와 별도 seed로 정확식을 재계산했다.

## 판정

**현재의 작은 Gaussian identified-set 프로그램은 독립 논문 주제로 기각하는 것이 타당하다.** 정확한 계산과 반례는 유용하지만, 핵심 dependence contrast가 기존 approximate joint diagonalization(AJD) 목적함수와 동일하고, 신호 차이 대비 민감도는 기존 covariance/eigenspace 식별 문제의 중심이다. 아래 exact tolerance set가 기존 논문에 동일한 문장으로 이미 있다는 부재/존재까지 증명한 것은 아니다. 작은 닫힌식 하나가 기존 분야의 문제를 넘어서는 중요한 새 결론을 제공하지 않는다는 판단이다.

**더 넓은 비선형 source-misspecification 질문 전체를 불가능하다고 판정하지 않는다.** 현재 결과로 진행 권고할 근거가 부족하다. 특히 어떤 task나 functional이 여전히 공통으로 유지되는지, 데이터에서 유용한 신뢰 진술을 만들 수 있는지는 미해결이다.

## 1. 확인한 수식과 완전 증명

소스가 환경 e에서 `s|e ~ N(0,D_e)`이고, D_e는 양의 대각행렬이며 환경 수는 유한하다고 하자. 관측은 x=A s. 좌표 i,j에만 작용하는 회전 R(theta)를 적용해 u=R s, A_new=A R^T로 두면 `A_new u=x`가 경로별로 성립한다. 따라서 모든 환경의 전체 관측법칙은 정확히 같다.

Gaussian total correlation은

`TC(C)=.5[sum_i log C_ii − log det C]`

이다. i,j의 분산을 a,b라 쓰면 회전 후 두 대각 원소의 곱은

`ab + ((a-b)^2/4) sin^2(2 theta)`

이고 determinant는 ab로 같다. 나머지 좌표는 상쇄되므로

`TC_e(theta)=.5 log[1 + k_e sin^2(2 theta)]`, `k_e=(a_e-b_e)^2/(4 a_e b_e)`.

이는 owner의 대칭분산 `a=1+gamma,b=1-gamma` 식과 일치한다. 이 도출은 완전 증명이며 아래 수치실험은 코드의 구현을 별도로 점검한다.

### 유한 환경과 양의 tolerance 아래 exact block은 유지되지 않는다

모든 환경에서 TC<=delta, delta>0를 허용하면 모든 유한 k_e에 대해 0이 아닌 충분히 작은 theta가 feasible하다. e=0의 D0=I를 추가로 신뢰해도 이 환경의 k0=0이므로 결론은 같다. 임의의 proper coordinate block S에 대해 i in S와 j outside S를 골라 작은 회전을 적용하면 그 block의 span이 변한다. 이 회전은 sign/permutation 또는 componentwise invertible reparameterization으로 환원되지 않는다. Gaussian support가 전체 공간인 경우 회전 좌표의 Jacobian에 다른 소스 좌표에 대한 0이 아닌 편미분이 있기 때문이다. 따라서 **이 모형과 tolerance만으로 개별 축뿐 아니라 임의의 proper coordinate block의 exact uniqueness도 일반적으로 보장할 수 없다.**

이 결론은 작은 theta를 허용하는 연속성의 직접 귀결이다. approximate cone/기능의 안정성은 다른 연구 대상이며 이 명제가 그것들을 배제하지 않는다.

## 2. 중요한 모델 범위 교정: whitening이 O(d)를 정당화하지 않는다

관측 x의 기준환경 covariance를 I로 whitening했다는 것과, 허용하는 모든 source 모형의 기준환경 covariance가 I라는 것은 다르다. 정확한 소스 독립성을 가정하면 diagonal scaling으로 C_s0=I를 맞출 수 있지만, source dependence를 허용하면 covariance whitening은 요인들을 섞는 추가 변환이다. 이것은 componentwise equivalence가 아니다.

독립 반례를 직접 구성했다. 관측 covariance가 D0=I, D1=diag(1.3,.7)일 때

`u=T x`, `T=[[1,epsilon],[0,1]]`, `x=T^-1 u`

로 둔다. epsilon=.03579498364, delta=.001을 쓰면 source TC는 환경별 .00064023036/.00034484129로 두 tolerance를 모두 만족한다. 관측 covariance 복원오차는 1.2e-16 미만이다. source의 각 좌표 분산을 1로 정규화해도 source correlation=.03577207이 남고, mixing의 orthogonality residual은 .05068657이다.

따라서 O(d)로 구한 집합은 **기준환경의 소스 covariance=I를 추가로 가정한 restricted family의 exact set**다. broader approximate-independence 선형 모형에서는 feasible subset이며 ambiguity에 대한 하한만 제공한다. owner에게 전달했고 이 제한을 받아들여 문서를 교정하기로 했다.

## 3. dependence budget도 결과의 일부다

`max_e TC_e<=delta`와 `sum_e pi_e TC_e<=delta`는 서로 다른 조건이다. 후자만이 통상 확률가중 conditional TC와 직접 일치한다. owner는 전자를 명시했으므로 수식 자체는 맞지만 명칭을 생략하면 오해가 생긴다.

독립 수치 대조에서 gamma=.6, delta=.01, informative environment 확률 pi=.01이면:

- 모든 환경에 각각 delta를 요구: quotient angle 최대 5.46205도.
- 확률가중 평균 TC에 delta를 요구: 전체 quotient 45도까지 허용.

이는 새 현상으로 제시할 결과가 아니라 가정 선택의 실질적 차이다. 드문 환경을 추가했다는 사실만으로 구조 ambiguity가 줄었다고 결론내릴 수 없다.

## 4. 원문으로 확인한 가장 강한 경쟁 설명

### AJD와의 정확한 목적함수 동등성

Ablin, Cardoso, Gramfort, **Beyond Pham’s algorithm for joint diagonalization**, 2018 preprint, <https://arxiv.org/html/1811.11433v1>. 직접 읽은 범위: §1 Eq(1), §2 Eq(2)-(3), §3.1 Eq(4).

Eq(1)은 평균 `TC(B C_e B^T)`와 정확히 같은 log-det diagonality cost다. 따라서 평균-budget identified set는 이미 사용되는 이 contrast의 sublevel set다. max-budget는 개별 cost sublevel의 교집합이므로 해당 논문의 최적화 정리가 그대로 모든 결과를 증명한다고 말할 수는 없다. 하지만 TC contrast 자체와 그 국소 curvature를 새 원리로 주장할 수는 없다.

Afsari, **Sensitivity Analysis for the Problem of Matrix Joint Diagonalization**, 2007 author manuscript / SIMAX 2008, <https://isr.umd.edu/Labs/ISL/ICA2006/SensitivityJD4.pdf>. 직접 읽은 범위: §1의 orthogonal versus nonorthogonal 구분, uniqueness/conditioning scope. 이분산 환경 정보의 유사성과 demixing 조건수가 noise sensitivity를 좌우한다는 문제는 오래된 분석 대상이다. 최종 출판본의 theorem numbering과 완전히 동일하다고 가정하지 않았다.

### 이미 존재하는 partial identification의 목표

Bacchiocchi, Bastianin, Kitagawa, Mirto, **Partially identified heteroskedastic SVARs**, <https://arxiv.org/pdf/2403.06879>, v3 2026-03-09. 직접 읽은 범위: §II.2, §III.2 Theorem1/Examples1-2, §III.3. 서로 같은 variance shifts는 고유공간 내 회전 ambiguity를 남기며, 다른 고유값의 방향과 반복 고유값의 부분공간을 구별한다. 이 논문은 정확한 orthogonal shocks와 추가 zero/sign restrictions를 다루므로 delta-TC misspecification 모델과 동일하지 않다. 그러나 '한 요인은 식별하고 다른 요인은 묶음만 식별한다'는 연구 목표 자체를 새 것으로 볼 수 없다.

Lütkepohl et al., <https://arxiv.org/pdf/2404.11057>, 현재 v2 제목은 **Partial Identification of Structural Vector Autoregressions with Non-Centred Stochastic Volatility** (2025-10-02)로 초기 preprint/검색 제목과 다르다. 본문 §1 및 appendix의 covariance-volatility uniqueness 조건을 확인했다. 논문의 버전·제목과 정확히 무엇을 partial identification이라 부르는지 구분해야 한다.

Cardoso, **Dependence, Correlation and Gaussianity in Independent Component Analysis**, JMLR2003, <https://www.jmlr.org/papers/v4/cardoso03a.html>. mutual-information contrast와 Gaussian correlation의 관계를 이해하기 위한 고전이며 원문 abstract와 linked PDF 진입을 확인했다. 위 determinant 식은 이 검토에서 직접 증명했으며 이 abstract만으로 특정 theorem을 재구성하지 않았다.

## 5. 직접 실행 증거와 재현 명령

사전 조건은 [protocol.md](protocol.md), 독립 구현은 [code/audit.py](code/audit.py). 실행 명령:

`OPENBLAS_NUM_THREADS=1 python review/partial-identification/code/audit.py`

환경은 coordination/environment.json을 따른다. owner 구현은 import하지 않았다. seed20261022와 별도 seed8675309에서 각 200개 무작위 variance/angle 사례를 계산했다.

- 총 400사례 TC 닫힌식 최대 절대오차: 3.11e-15.
- 관측 covariance 복원 최대 Frobenius 오차: 7.17e-15.
- 성분별 scaling 이후 TC 변화 최대: 5.55e-15.
- 결과: [audit_summary.json](results/audit_summary.json), 원시 값 [random_checks.csv](results/random_checks.csv).

이것은 모집단 Gaussian algebra의 구현 검증이다. finite-sample coverage, 비Gaussian 정보량, 신경망 최적화 성능을 검증하지 않았다.

## 6. 남은 반론과 회생 조건

- δ는 실제 source dependence의 알려진 robustness budget이다. 같은 관측법칙이 독립 또는 약하게 의존하는 생성설명을 동시에 허용하므로 관측자료만으로 true source δ를 학습했다는 주장은 성립하지 않는다. 단, 어떤 관측법칙이 restricted exact-ICA class와 호환되는지 테스트하는 문제 전체가 불가능하다는 뜻은 아니다.
- 작은 모형이 허용한 approximate cones가 학술적으로 중요한 task/functional 보장으로 이어지는지는 아직 증거가 없다.
- 대안 모형을 찾지 못한 것은 모형 부재의 증명이 아니며, optimization-selected minimizer와 data-supported identified set를 구별해야 한다.
- 회생에는 단순 수식 확장보다 **기존 AJD/SVAR가 다루지 않는 실질적인 결론**이 필요하다. 예컨대 명시된 비선형 함수군과 dependence budget에서 동일 관측법칙의 sharp ambiguity 하한과 동시에 nontrivial functional의 uniform 안정성을 입증하거나, 추가 정보 한 종류가 그 모호성을 얼마나 줄이는지 새로운 최적 경계를 제시해야 한다. 현재 그런 결과는 없다.

주제1의 첫 순위를 유지할 근거는 이번 검토에서 확보되지 않았다. Gaussian audit는 연구를 시작할 범위를 명확히 한 음성 결과로 보존하고, 이 결과만으로 수개월 연구에 착수하는 것은 권하지 않는다.
