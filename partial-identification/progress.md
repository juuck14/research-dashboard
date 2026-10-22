# 진행 기록

## 2026-10-22 단계 0

실행: 기존 보고서의 주제 1을 재정의하고 관련 원문 검색. iVAE 2020, Lyu–Fu 2022, Buchholz–Schölkopf 2024 원문 확인. 기존 보고서가 빠뜨린 이분산 SVAR 부분 식별 및 joint diagonalization perturbation을 발견.

직접 도출: 2D Gaussian의 exact observational equivalence와 total-correlation tolerance 식별집합의 닫힌식.

아직 미실행: numerical oracle 및 finite-sample illustration.

판단 변화: 기존 보고서의 '강한 방향은 그룹까지 식별'은 tolerance>0에서 정확/근사 구분이 부족했다. 정확한 부분공간보다 방향별 ambiguity cone을 목표로 좁힌다. 이 수정은 신규성 위험을 낮추지 않으며 고전 perturbation과 더 직접 겹친다.

가장 큰 반론: exact 식별집합의 2D 공식도 Gaussian mutual-information 식과 eigenvector gap의 재표현일 수 있다.
