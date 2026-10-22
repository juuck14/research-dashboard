# 진행 기록

## 2026-10-22 단계 0

실행: 기존 보고서의 주제 1을 재정의하고 관련 원문 검색. iVAE 2020, Lyu–Fu 2022, Buchholz–Schölkopf 2024 원문 확인. 기존 보고서가 빠뜨린 이분산 SVAR 부분 식별 및 joint diagonalization perturbation을 발견.

직접 도출: 2D Gaussian의 exact observational equivalence와 total-correlation tolerance 식별집합의 닫힌식.

아직 미실행: numerical oracle 및 finite-sample illustration.

판단 변화: 기존 보고서의 '강한 방향은 그룹까지 식별'은 tolerance>0에서 정확/근사 구분이 부족했다. 정확한 부분공간보다 방향별 ambiguity cone을 목표로 좁힌다. 이 수정은 신규성 위험을 낮추지 않으며 고전 perturbation과 더 직접 겹친다.

가장 큰 반론: exact 식별집합의 2D 공식도 Gaussian mutual-information 식과 eigenvector gap의 재표현일 수 있다.

## 2026-10-22 단계 1 실행 완료

실행: 사전 계획한 population 41개 조건, 3D pair rotation 9개, sample covariance 360 반복. checks.json의 assertion 전부 통과. 직접 계산 TC와 공식 오차 최대2.5e-16, covariance 동치 오차8.9e-16.

판단 변화: δ>0이면 exact component/group가 보존된다는 모호한 기대는 continuity 반례로 기각. strong direction은 작은 ambiguity cone으로만 말할 수 있다. 이는 가설의 긍정 실험이 아닌 원 주장 범위 수정이다.

교차 검토: baseline whitening을 source covariance I의 정규화 근거처럼 쓴 표현이 오류라는 critic을 수용. 원 관측 whitening+정확한 reference-source covariance라는 별개 제약을 명시. 제한 family의 exact set와 broader family의 feasible lower subset를 구분했다. 또한 max-environment 예산과 average conditional TC 예산을 다르게 적었다.

문헌 변화: critic이 찾은 Ablin–Cardoso–Gramfort2018 원문 Eq(1),(3),(4)를 직접 읽었다. Gaussian TC cost 및 Hessian은 고전 approximate joint diagonalization과 직접 동일. local sensitivity를 새 학습 원리로 제안할 근거가 없다.

현재 가장 큰 반론: 새로 얻은 식은 기존 Gaussian entropy와 matrix diagonalization을 낮은 차원에서 다시 쓴 것이다. 이를 넘어서는 nonlinear positive result가 없다.

다음: 현재 좁힌 독립 주제를 기각하는 판정과, 어떤 추가 결과가 있어야 재개할지 문서화. 코드와 결과를 최종 검토자에게 전달.
