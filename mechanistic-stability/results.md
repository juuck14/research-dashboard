# 직접 실행 결과

2026-10-22. 모든 결과는 exact population construction의 수치 감사다. neural autoencoder training이나 실제 데이터 실험으로 부르지 않는다. 모집단 정보 한계와 objective preference를 먼저 구분하는 것이 이번 질문에서 더 정보량이 높았다. 데이터·최적화 규모를 늘려 반례의 동일-law ambiguity를 해결할 수 없다.

| 실행 단위 | 실제 조건 수 | 관측 결과 | 의미와 한계 |
|---|---:|---|---|
| weak-anchor same-law 반례 | primary7 + independent-seed40 | integer gap1 유지, distance/κ=√(2−√2), axis45° | family-uniform stability 실패; fixed g0 반증 아님 |
| cubic nonlinear sensor control | 위47조건의4096 points/조건 | measured C1≤analytic upper bound; 최고비율.9999999999 | analytic bound 감사; sampled maximum가 supremum라는 뜻 아님 |
| MI surrogate local landscape | κ7×θ10001 | gapκ², barrier→√2−1, formula error≤8.89e−16 | fixed-Gram rotation family의 실제 objective 계산 |
| fixed-base new-support 반례 | primary7 + confirmation20 | fixed true min8/nonalign9, candidate ref14/15, distance√2ε, axis45° | constant observation coordinates·larger candidate budget 허용 시 true-side margin만으로 불충분 |
| nonlinear positive theorem 확인 | β5×primary/confirmation2 | 같은-law residual≤2.23e−16, 모든 η<a/√2, 모든 bound 만족 | theorem은 별도 proof; grid가 모든 candidate를 열거한 것은 아님 |
| strong-weight surrogate preference | κ3×w4=12 |5조건에서45°의 contrast가 true보다 낮음 | positive true structure와 surrogate preference는 다른 문제 |
| low-overlap reviewer challenge | p3×w3=9 | p3,w2: overlap40%, exact TypeS gap2, true4/wrong3 | 높은 overlap50%만으로는 이 현상을 설명 못 함 |

## 대표 수치

weak-anchor 반례의 최대 same-observation reconstruction residual4.44e−16, 거리 공식 오차1.11e−16. κ=.001에서 candidate-reference distance.0007653669이지만 factor tangent orientation45°다. min singular는√(2+κ²)여서 inverse가 폭발하는 현상이 아니다. 행렬 sparsity의 nonzero amplitude가 약해지는 것이 원인이다.

fixed-base 반례에서는 true A와 actual candidate AR를 전혀 바꾸지 않고 candidate **reference**만 ε로 바꿨다. ε=1e−6에서 distance1.41421356e−6, true singular√3, candidate-reference singular√(3+2e−12)이다. 모든 관측 분포가 같으므로 n의 문제와 분리된다. 이는 learned reference의 complexity를 true와 맞춘 실험이 아니다. 그 차이가 허용된 class를 명시하여 broad stability 주장에 필요한 가정을 찾은 것이다.

positive theorem의 polynomial g0와 hβ에는 nonlinear latent transition이 있다. candidate를 root solver로 역변환한 뒤 source와 맞췄고 최대 inverse error1.11e−16이었다. measured candidate C1/analytic allowance≤.4717, measured off-block/predicted bound≤.1018, C0-to-block/predicted≤.0958. Bound가 느슨하다는 사실도 유지한다. β=.01에서 실제 off-block.01, predicted.10025다. 이 수치는 정리의 sharpness를 지지하지 않는다.

surrogate low-overlap 사례에서는 m8,p3,q2,w2로 고정했다. 모든 row norm≥1, Gram7I, true ℓ0=10, generalized-permutation이 아닌 basis의 ℓ0 최소12다. 그런데 wrong45° representation의 ℓ0는14이고 Ccomp는3으로 true4보다 작다. 따라서 smooth surrogate value만으로 learned ℓ0≤10을 전제할 수 없다. 이 정확한 mismatch는 데이터 노출량·차원·재구성·norm을 모두 같게 유지한다.

## 재현

환경: Python3.12.14, NumPy2.3.5, SciPy1.17.0, Matplotlib3.10.8. [기록](results/environment.json), [requirements](requirements.txt), [코드 SHA256](results/code_sha256.json). 저장소 root에서:

```bash
cd mechanistic-stability
OPENBLAS_NUM_THREADS=1 python3 code/run_study.py
OPENBLAS_NUM_THREADS=1 python3 code/surrogate_check.py
OPENBLAS_NUM_THREADS=1 python3 code/positive_check.py
OPENBLAS_NUM_THREADS=1 python3 code/fixed_base_check.py
OPENBLAS_NUM_THREADS=1 python3 code/surrogate_preference.py
OPENBLAS_NUM_THREADS=1 python3 code/low_overlap_surrogate.py
```

원자료는 results/*.csv 및 summary.json 계열, 그림은 figures/ 아래에 있다. seed20261022는 primary,20261023은 weak-anchor confirmation,20261024는 nonlinear random-point confirmation,20261025는 fixed-base confirmation다. 반복 조건 수를 서로 독립 dataset의 성공 확률처럼 해석하지 않는다. 두 그림은 눈으로 확인했다.

독립 검토자는 별도 코드·seed·tanh sensor, 모든 candidate support 열거 및 fixed-base construction을 확인했다. [독립 검토](../prevalidation-20261022/reviews/mechanism/review.md)의 범위와 새 실행 기록을 함께 읽어야 한다. 제안자의 같은 코드를 seed만 바꾼 결과를 독립 구현이라 부르지 않았다.
