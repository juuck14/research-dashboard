# Full Support Does Not Guarantee Factor Retention Under Adaptive Negative Filtering

상태: 직접 증명과 실행 결과를 담은 연구 노트 초안. 독립 논문으로서의 신규성은 아직 최종 확정하지 않았다. 기존 feature-suppression의 재현이나 generic performative instability를 새 원리로 주장하지 않는다.

## 1. 연구 질문

현재 표현을 기준으로 유사한 negative를 덜 선택하는 규칙은, 표현에 이미 존재하는 요인의 구분을 스스로 약하게 만들 수 있는가? 모든 negative에 양의 확률이 남아 있고 표현 차원이 충분해도 그런 현상이 생기는가?

이 질문에서 구별할 것은 세 가지다. 첫째는 고정된 negative 분포가 선호하는 목적함수의 해다. 둘째는 현재 표현이 negative 분포를 계속 바꾸는 갱신의 효과다. 셋째는 동일한 원래 목적함수를 다른 sampling으로 추정할 때 생기는 최적화 오차다. 본 연구의 주된 결과는 둘째에 관한 것이며, 셋째라는 주장은 importance-correction 통제로 배제한다.

## 2. 선행연구와 정확한 차이

Robinson et al.(ICLR 2021)은 표현에 의존하는 exponential hard-negative sampling과 false-negative correction을 이미 제안했다. Xue et al.(ICML 2023)은 simplicity bias와 augmentation 아래 feature suppression을 분석했고, Zhang et al.(ECCV 2024)의 MCL은 학습한 특징을 공유하는 negative를 이용해 덜 배운 특징을 학습한다. GloFND(ICML 2025)는 anchor별 similarity threshold로 negative를 제거하며, FALCON(CVPR 2026)은 hardness 선택을 학습한다. 따라서 task-relative false negative, 학습 특징에 따른 sampling, 또는 hard/FN 균형 자체는 새 문제로 주장할 수 없다.

기존 보고서에서 빠졌던 Jiang et al.(TMLR 2025)은 hard-negative sampling, normalization과 dimensional collapse를 직접 다룬다. 그 이론은 nondecreasing hardening과 latent-label 구조에서 global optimal geometry를 분석하고, 실험은 초기화 및 normalization의 영향을 비교한다. 본 노트는 easy-filtering과 full-support floor가 있는 finite-state sphere에서, 동일한 stationary representation에 맞춘 frozen sampler의 안정성과 adaptive sampler의 안정성을 정확히 비교한다. 이 차이 때문에 구체적인 local spectrum과 factor-selective 불안정 영역이 필요하다. 다만 전반적인 geometry–dynamics 차이를 처음 구별한 연구라는 주장은 하지 않는다.

또한 Perdomo et al.(ICML 2020)의 performative prediction은 모델이 학습 분포를 바꾸는 문제와 frozen-risk 최적성 및 갱신 안정성을 이미 구별한다. `DG = frozen curvature + distribution response`라는 일반 분해는 새 기여가 아니다. 독립 기여가 될 수 있는 부분은 contrastive sphere에서의 명시적인 factor-retention 경계다. 이 분석이 기존 틀의 작은 예제 이상으로 충분히 중요한지는 남은 문헌 및 확장 검증 대상이다. 원문별 확인 범위는 [literature.md](literature.md)에 있다.

## 3. 문제 설정

관측 상태는 독립적인 두 binary factor `x=(a,b)`이며 각 조합의 확률은 1/4다. Positive는 같은 상태의 다른 instance로 두어 두 factor 모두 정확히 보존된다. 사람의 의미 label은 학습에 사용하지 않는다.

먼저 무제약 표현 `f_w(x)=(w1*a,w2*b)`를 분석한다. 이후 더 넓은 normalized lookup class `f_i ∈ S^(d−1), d≥3`를 다룬다. 후자는 네 상태를 모두 구별하는 tetrahedral representation까지 표현할 수 있어 단순한 차원 부족으로 설명되지 않는다.

One-negative InfoNCE는 `ell=log[1+exp(f(x)^T f(y)−1)]`이다(normalized 경우). Negative 분포는

`q_F(y|x)=epsilon/4+(1−epsilon) softmax_y[kappa f(x)^T f(y)]`.

`kappa<0`는 높은 similarity의 negative를 덜 고르는 soft filtering이다. `epsilon>0`이므로 모든 상태가 항상 선택 가능하다. Sampler는 stop-gradient로 취급하고 sphere projected gradient flow로 표현을 갱신한다. 비교군은 uniform q, 초기 표현으로 만든 frozen q, 분석할 stationary point에 맞춘 frozen q*, adaptive q다. q(F)까지 미분한 전체 risk gradient는 별도의 알고리즘이다.

## 4. 첫 가설의 반증: full support와 자유 coordinate가 주는 복원

**명제 1.** 무제약 dot-product 표현과 identity positive에서 `w2=0` boundary는 attracting하지 않는다. `q≥epsilon/4`이면 작은 비영 w2의 성장률은 boundary에서 적어도 `epsilon/2`다. `0<w2≤delta`인 동안

`d log(w2)/dt ≥ epsilon sigmoid(−2delta²)`.

따라서 `eta>0`에서 delta까지의 탈출 시간은

`T≤log(delta/eta)/[epsilon sigmoid(−2delta²)]`.

**증명의 핵심.** Anchor와 첫 factor가 같고 둘째 factor만 반대인 negative는 항상 확률 epsilon/4 이상으로 존재한다. 이 비교는 첫 factor를 키워도 해결되지 않는다. 누락 factor를 추가하는 방향은 positive score를 높이고 그 negative score를 낮추므로 반드시 descent 방향이다. 전체 `(w1,0)`은 w1 방향으로 drift할 수 있어 stationary saddle라고 부르지 않는다. 정확한 결론은 invariant boundary의 transverse repulsion이다. 완전 증명 및 K-negative append 방향은 [theory.md](theory.md)의 명제 1–3에 있다.

**실행 결과.** Exact expectation을 이용한 1,080개 설정/초기값 반복 모두 이론적으로 정한 deadline 안에 `w2=0.1`에 도달했다. 그중 독립 확인 seed 설정은 540개다. 이 수치는 독립 dataset 성공률의 통계 추정이 아니다. Gradient checker 오차는 최대 `3.92e−11`이다. 한 설정에서는 filtering이 uniform 대비 탈출을 약 99배 늦췄지만, frozen q도 거의 같은 지연을 만들었다. 유한 horizon의 저성능만으로 영구 배제 또는 피드백 고유 효과라고 해석할 수 없었다.

| epsilon=.01, w1≈2, w2≈1e−6 | uniform | frozen | adaptive |
|---|---:|---:|---:|
| easy filtering kappa=−8: hitting time | 23.037 | 2285.179 | 2285.163 |
| hard mining kappa=8: hitting time | 23.037 | 11.581 | 11.623 |

이 반증은 normalization이 없는 available-coordinate 모형의 결과다. 일반적인 feature suppression이 불가능하다는 주장은 아니다.

## 5. 수정된 핵심 명제: normalized full-capacity 표현의 피드백 불안정

네 상태를 square `f_i*=(a_i,b_i,0,…)/sqrt(2)`로 표현하자. 두 factor는 모두 쉽게 선형 복원된다. Square는 frozen q*와 adaptive q의 stationary point다.

다음 기호를 사용한다.

- `c=1−epsilon`, `Z=2+2cosh(kappa)`, `alpha=1/Z`.
- `v=epsilon/4+c*alpha`: adjacent 상태를 고르는 확률.
- `w=epsilon/4+c*exp(−kappa)/Z`: opposite 상태를 고르는 확률.
- `r=sigmoid(−1)`, `r'=r(1−r)`, `s=sigmoid(−2)`.

**명제 2.** 모든 d≥3에 대해 frozen q*의 square는 global rotations를 제외하고 local stable일 필요충분조건이 `w*s>v*r`이다. 동시에

`v*r'+c*kappa*alpha*r<0`

이면 adaptive update는 factor-balance 방향에서 unstable이다. 다른 tangent mode의 부호도 닫힌 형태로 계산된다.

| DG mode (flow Jacobian은 음수) | frozen q* | adaptive q |
|---|---|---|
| factor-balance, 1개 | `2*v*r'` | `2*(v*r'+c*kappa*alpha*r)` |
| in-plane 다른 mode, 2개 | `v*r'+w*s` | `v*r'+w*s+c*kappa*alpha*r*(1−alpha)` |
| 각 normal coordinate의 첫 mode | `v*r+w*s` | 같음 |
| 각 normal coordinate의 ab mode | `w*s−v*r` | 같음 |
| rotations | 0 | 0 |

**증명의 핵심.** 네 상태의 tangent perturbation을 binary group의 Fourier basis `1,a,b,ab`로 분해한다. Frozen field의 in-plane curvature는 neighbor/opposite weighted graph Laplacian이 된다. Adaptive field에는 softmax normalizer까지 미분한 sampler-response 항이 더해진다. Normal 방향은 score의 1차 변화가 없어 이 response 항이 0이다. 이를 모든 mode에 적용하면 표를 얻는다. 전체 유도는 theory.md의 명제 5에 있다. 이 closed-form spectrum은 독립 critic의 별도 코드와도 일치했다.

`epsilon=.1,kappa=−2`에서 두 조건은 동시에 성립한다. d3 square는 frozen update 아래 rotation 3개를 제외한 5방향 모두 stable인데, adaptive update에서는 factor-balance 한 방향이 unstable이 된다. d4에서도 같은 결론이 유지된다. 별도 critic의 full-sphere Jacobian 오차는 약 `5.6e−12`다.

이는 frozen q에서의 normalized corner suppression과 다르다. Corner는 matched frozen q에서도 stable일 수 있으므로 그것만으로 피드백 고유성은 입증되지 않는다. Square에서는 **동일한 representation과 동일한 현재 q**에서 출발해 q를 갱신하는 반응이 local stability의 부호를 바꾼다.

## 6. 직접 실행한 확인

정규화된 tied-coordinate trajectory의 672개 사전 기록된 설정에서 analytic curvature와 finite difference를 대조했고 최대 오차는 `1.12e−10`이었다. 핵심 설정의 같은 초기 표현에서 adaptive만 한 factor 방향으로 이동했고, frozen-at-initial, frozen-at-square, uniform은 양 factor를 유지했다.

| epsilon=.1,kappa=−2, 초기 theta=.7864159 | t=200에서 theta | 작은 factor amplitude |
|---|---:|---:|
| adaptive | 1.5707963265 | 3.00e−10 |
| frozen at initial | .7875999464 | .70555 |
| frozen at square | .7853981642 | .70711 |
| uniform | .7853981637 | .70711 |

이 finite-time amplitude는 수학적으로 0이 아니다. Exact real arithmetic에서는 nonzero factor를 읽을 수 있다. 고정 readout noise를 추가한 접근성과 attracting boundary에서의 극한 정보 손실을 구분한다.

독립 critic은 d3/d4 full lookup에서 두 확인 seed, perturbation `1e−4/1e−6`, frozen/adaptive의 16개 flow를 별도로 실행해 frozen contraction과 adaptive expansion을 확인했다. 이는 tied additive parameterization만의 방향 artifact가 아니라는 근거다.

## 7. K>1 및 동일 목적함수 통제

K개의 iid negatives에 대해 네 category의 multinomial counts를 모두 열거했다. K=1,2,4,8,16, epsilon 3수준, kappa 7수준의 105조건에서 확률합 오차는 `3.55e−15`, analytic curvature와 finite difference의 최대 차이는 `4.53e−10`이었다.

| K, epsilon=.1,kappa=−2 | frozen curvature | adaptive curvature |
|---:|---:|---:|
| 1 | .18795 | −.21866 |
| 2 | .34138 | −.36473 |
| 4 | .57217 | −.54113 |
| 8 | .85368 | −.70057 |
| 16 | 1.11836 | −.80669 |

위 표는 factor-balance scalar mode이며, full-sphere K2/K4 안정성은 critic이 별도 exact count enumeration으로 확인했다. 모든 K의 full-spectrum theorem은 아직 쓰지 않았다.

Importance weight `product_j p(yj)/q_F(yj|x)`를 detached로 적용하면 exact population update는 uniform negative update와 동일하다. 90조건의 열거 검산 최대 차이는 `1.39e−15`였다. 따라서 현재 현상은 same-uniform-objective의 optimizer가 잘못 수렴한다는 사례가 아니다. 갱신되는 negative 분포가 실제 update field를 재가중하는 현상이다. Full derivative of composed risk와도 다르다.

## 8. 한계와 다음 논문 단계

증명된 것은 finite-state identity-positive 모형의 local stability다. Population 분석이므로 데이터 부족, finite minibatch noise, generalization을 입증하지 않는다. 장기 trajectory의 모든 basin과 모든 K의 full stability는 아직 분석하지 않았다. Soft filtering이 실제 GloFND/FALCON의 전체 동역학을 대표한다는 주장도 없다.

남은 핵심 질문은 두 가지다. 첫째, 위 spectrum이 performative prediction과 기존 collapse 이론의 사소한 적용을 넘어 새로운 factor-retention 원리를 제공하는가. 둘째, 실제 filtering 규칙과 비대칭 factor distribution에서도 임계식의 예측력이 유지되는가. 아래 후속 검증은 비퇴화 positive와 toy SGD 반론을 일부 해결하지만, 자연 이미지의 정책·encoder 일반화는 다루지 않는다.

현재 성과는 막연한 최초 가설보다 좁지만 강하다. 무제약 경우의 permanent blindness 주장은 반박됐고, normalized full-capacity 경우의 matched-frozen/adaptive stability 차이는 정확한 명제와 실행 결과로 확보했다. 독립 논문으로 채택하기 전에는 위 두 문턱을 넘겨야 한다.

## 9. 독립 후속 실행 결과

Root가 별도 사전 protocol을 작성한 뒤 세 요인·8상태를 d4/d8 전체 sphere tangent에서 확인했다. epsilon=.1,kappa=-2,d8에서 frozen의 최대 비회전 flow eigenvalue는 -.01238159이고 adaptive는 +.02590878이었다. 54조건 grid의18개 three-factor 후보를 추가 step size와 직교 좌표회전으로54회 확인했다. 이 결과는 exact expectation의 수치 Jacobian 검산이며 일반 factor수 정리는 아니다. [기록](../review/three-factor-extension/README.md).

또 다른 사전 규약 아래 positive를 독립 bit flip eta=.001,.01,.05,.1로 바꿨다. 모든 경우 channel full-rank를 유지하며 frozen stable/adaptive unstable이 두 finite-difference step에서 확인됐다. eta=.1의 최대 비회전 flow eigenvalue는 -.08697142 및+.03214919였다. Strict local margins의 작은 변형 강건성과 일치한다. 자연 augmentation을 대표한다는 주장은 하지 않는다.

실제 normalized lookup SGD도 실행했다: identity positives, batch64,lr.1,6000steps,primary1001–1006 및 confirmation3001–3004, 세 정책 총30실행. 같은 초기값과 anchor/uniform 난수 stream을 policy별로 맞췄다. 명시된 isotropic feature noise sigma=.05 아래 정확한 Gaussian-mixture Bayes readout을 적용했을 때 worst-factor 관측 정확도는 uniform/frozen1.000, adaptive.4934–.4984였다. 사전 성공 기준5/6·3/4에 대해 관측6/6·4/4가 충족됐다. 이는 고정 noise 아래 접근성 차이이며 noiseless finite-time MI 소실이 아니다. Positive-noise population 실험과 identity-positive SGD는 별개다.

Independent reviewer는 별도 코드로432개의 coordinate gradient FD(max1.24e-10), expected SGD gradient(max5.20e-17), Bayes 평가 sanity를 확인했다. [실행·규약·원자료](../review/robustness-extension/README.md), [독립 감사](../review/robustness-extension/independent-review.md). 이 결과는 lookup model 밖의 이미지 encoder 성과를 대신하지 않으며, 실제 filtering 규칙과 기존 performative 설명을 넘는 중요성은 여전히 남았다.

## 재현

```bash
OPENBLAS_NUM_THREADS=1 python code/exact_population.py
OPENBLAS_NUM_THREADS=1 python code/normalized_feedback.py
OPENBLAS_NUM_THREADS=1 python code/multiple_negatives.py
OPENBLAS_NUM_THREADS=1 python code/importance_control.py
```

실행 전 설계와 후속 변경 이유는 protocol.md, 원시 결과는 results/*.csv 및 summary JSON, SVG 그림은 results/escape.svg 및 results/normalized_feedback.svg에 있다. 독립 교차 검토 결과는 저장소 review/negative-feedback/를 참조한다.

### 추가 교차 검토와 범위 확인

ICLR2026 **SnaPhArd Contrast Learning**의 §2.2/Theorem2.1도 대조했다. 해당 정리는 key/positive vectors를 고정한 단일 query optimum을 다루며, 그 collapse 정의는 본 노트의 factor collapse와 다르다. easy-negative fixation이라는 일반 동기가 가깝다는 점은 남기되, 동일 정리 또는 신규성의 확증으로 취급하지 않았다.

독립 critic은 자기 상태와 같은 negative category를 제외한 3-candidate sampling에서도 d4 square의 frozen-stable/adaptive-unstable 차이를 확인했다. 따라서 같은-state negatives를 허용한 것만으로 현상을 설명할 수는 없다. 설정과 결과는 [review/negative-feedback](../review/negative-feedback/no-self-protocol.md)에 있다.

Root는 별도의 사전 protocol에 따라 3-factor, 8-state, d4/d8 sphere도 검산했다. epsilon=.1,kappa=−2에서 frozen의 largest nonzero flow eigenvalue는 −.01238159이고 adaptive는 +.02590878이다. 54개의 confirmation 수치 점검이 조건을 통과했으며 stationary residual은 최대 약1.39e−17이었다. 이는 exact expectation의 수치 Jacobian 확장 근거이며, 3-factor theorem이나 실제 dataset 결과가 아니다. [독립 extension 기록](../review/three-factor-extension/protocol.md).
