# 판정

**기각 — 현재 구체화한 간결한 독립 연구 주제로서는 신규 기여의 근거가 부족하다.**

이 판정은 '근사 가정 아래 잠재 구조를 연구하는 것은 불가능하거나 중요하지 않다'는 뜻이 아니다. 이번 작업에서 확보한 좁은 모형의 핵심 결과가 독립적인 새 논문의 중심이 되기 어렵다는 판정이다. 일반 nonlinear/source-dependence 질문은 미해결이며 긍정 결과를 얻지 못했다.

## 실제 확보한 증거

1. **완전 증명:** 기준환경 source covariance를 정확히 I로 고정한 선형 Gaussian family의 same-law rotation alternatives 및 exact quotient angle set. arbitrary GL/nonlinear에는 feasible subset/lower bound로만 적용.
2. **완전 증명:** 모든 표본 크기에서 유지되는 observational-equivalence two-point angle risk 하한.
3. **완전 증명:** 유한 환경과 δ>0에서 모든 pair의 충분히 작은 회전이 허용되므로 별도 exact block 제약 없이 정확한 nontrivial source group 보장은 나오지 않는다는 반례.
4. **실행:** 41개 oracle 조건, 9개 3D examples, 360개 표본 반복 및 별도 확인 seed. theory/implementation 일치.
5. **선행 중복:** Gaussian average TC는 Ablin–Cardoso–Gramfort2018 Eq(1)의 Pham joint-diagonalization contrast와 정확히 동일. Hessian·scale symmetry도 이미 분석됨. heteroskedastic source의 component/block identification은 ML 밖의 독립·경제계량 문헌에 존재.

## 결정적인 기각 이유

- '약한 방향은 먼저 불확실해진다'는 현상은 기존 diagonalizer conditioning을 벗어나지 않는다.
- exact identified-set 공식과 표본 무관 하한은 유용한 진단이지만 Gaussian entropy+same-law two-point argument의 초등 결과다.
- 3D 방향별 radius는 기존 eigen-gap 설명과 일치하고, 새로운 nonlinear 원리를 보이지 않았다.
- source-independent reference environment를 신뢰한 제한 모형이므로 실제 approximate independence 전체에 실용 인증을 제공하지 않는다.

## 살려보려 한 수정안

A. scalar robustness error 대신 direction별 identified set → 정확 계산 가능하나 고전 TC cost sublevel와 겹침.

B. 개별 component가 안 되면 group/subspace만 보존 → δ>0에서는 exact group도 작은 cross-block rotation에 바뀜. approximate group notion은 가능하나 이것만으로 신규성 부족.

C. seed stability와 data-supported uniqueness 비교 → same-law 대안으로 차이는 증명되지만 알려진 비식별성의 직접 결과. neural diagnostic를 붙여도 새 검증 원리가 없으면 engineering 추가일 뿐.

## 재개하려면 필요한 결과

- Gaussian covariance/joint-diagonalization만으로 설명되지 않는 비선형 혹은 비Gaussian 관측 동치 집합의 sharp characterization.
- arbitrary componentwise reparameterization에 불변인 구조 tolerance와 실질적인 부분 구조의 target.
- 구조 오차 예산을 관측자료로 정당화하거나, 정직한 finite-sample confidence set와 비자명한 해상도–coverage 경계.
- 최신 misspecified-structure 원문의 정리를 다시 확보하여 직접 비교. 이번 세션 retrieval 차단 범위는 literature.md에 기록.

이 중 핵심 결과는 현재 없다. 따라서 제목·목차만 갖춘 긍정적 논문 초안은 만들지 않고, `theory.md`와 `results.md`를 완결된 기각 근거로 보존한다. 실험을 무작정 키워 해결할 문제가 아니다.
