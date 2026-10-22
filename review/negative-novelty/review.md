# Negative feedback의 추가 발견에 대한 독립 신규성 검토

2026-10-22. 검토 대상은 normalized square에서 동일 equilibrium sampler q를 고정하면 양의 곡률인데, 현재 표현에 맞춰 q를 갱신하면 음의 field derivative가 생기는 현상이다. 본 담당은 전체 구면 tangent 안정성 검사와 분리하여 기존 이론·목적함수 해석을 공격했다.

## 결론

수치 부호 반전은 독립 계산과 일치한다. 그러나 **frozen objective의 local minimum이 adaptive dynamics에서 불안정할 수 있다는 일반 명제**, 혹은 sampler derivative가 추가 Jacobian 항을 만든다는 분해는 새로운 원리가 아니다. Decision-dependent distribution의 performative learning과 self-paced reweighting의 이미 알려진 구도를 직접 적용한 것이다. 그렇다고 기존 문헌이 이 정확한 contrastive sphere의 모든 factor-selective 경계를 해결했다고 확인한 것은 아니다. 이 특수 반례가 존재한다는 것만으로 진행 권고를 내리기에는 부족하다.

## 1 가장 가까운 일반 이론의 원문 확인

- Perdomo, Zrnic, Mendler-Dünner, Hardt. [Performative Prediction, ICML 2020](https://proceedings.mlr.press/v119/perdomo20a/perdomo20a.pdf). §2의 induced distribution과 stable model, §3.3 Definition3.7의 repeated gradient descent, Theorem3.8의 sensitivity-versus-curvature 조건을 직접 확인했다. Distribution derivative를 무시한 risk gradient로 매번 업데이트하는 식이 detached q update의 일반형이다. Proposition3.6의 비수렴 예는 frozen risk의 convexity만으로 feedback 수렴을 보장할 수 없음을 보여준다. 구면의 비볼록 대비에 이 강한 볼록 정리를 그대로 적용할 수는 없으나, 그 일반적 문제를 처음 발견했다는 주장은 성립하지 않는다.
- Fan, He, Liang, Hu. [Self-Paced Learning: an Implicit Regularization Perspective, 2016 preprint/AAAI 2017](https://arxiv.org/pdf/1606.00128). Definition1, Proposition1, §3.2와 Appendix6.1을 읽었다. Loss에 따라 감소하는 sample weight는 latent robust objective와 연결된다. 따라서 쉬운 예만 강화할 때 바뀌는 곡률을 feedback이라는 이름만으로 새 현상으로 볼 수 없다. 단 anchor별 softmax normalization 및 epsilon-mixture가 있는 본 sampler가 그 SPL objective와 **전역적으로 정확히 같다**고 주장하지 않는다.
- Robinson et al. [Contrastive Learning with Hard Negative Samples, ICLR2021](https://arxiv.org/pdf/2010.04592), §3.1 Eq.2–4를 확인했다. Normalized representation에 의존하는 exponential tilting과 hardness-dependent objective는 이미 직접 연구됐다. 이 논문은 양의 hardness와 latent-class correction을 다루므로 easy kappa<0의 본 local instability를 직접 증명한 것은 아니다.
- Zhang and Stratos. [Understanding Hard Negatives in Noise Contrastive Estimation, NAACL2021](https://aclanthology.org/2021.naacl-main.86.pdf), §3.1 Theorem3.1–3.2 및 §3.2를 확인했다. Conditional negative law에 따른 gradient bias와 adversarial 해석이 이미 있다. 해당 결과는 supervised candidate softmax의 기준 gradient에 대한 것이며 본 네 상태 구면 모형의 exact theorem으로 인용하면 안 된다.
- Jiang et al. [Hard-Negative Sampling for Contrastive Learning: Optimal Representation Geometry and Neural- vs Dimensional-Collapse](https://arxiv.org/html/2311.05139v3), §1.1, §4, §5.3–5.7을 확인했다. Norm-bounded representations와 nonnegative nondecreasing hardening 아래 global geometry와 collapse/initialization/normalization의 관계를 다룬다. 본 easy filtering과 detached local reaction의 exact statement는 확인하지 못했다. 설정이 다르다는 사실은 새 기여를 보장하지 않는다.

## 2 일반 Jacobian 항의 의미

Finite-state detached field를 G(theta)=sum_z q_theta(z) grad_theta ell(theta,z)로 쓰면, equilibrium theta*에서

```
DG(theta*) = H_frozen + B_reaction
H_frozen = sum_z q_theta*(z) Hessian_theta ell(theta*,z)
B_reaction = sum_z grad_theta ell(theta*,z) grad_theta q_theta*(z)^T
```

이는 곱의 미분이다. H_frozen이 양의 정부호여도 reaction 항 때문에 DG에 음의 실수부 고유값이 생길 수 있다. Dynamics는 theta_dot=−G이므로 이 경우 equilibrium이 불안정하다. 이 식 자체가 핵심 논문 명제라면 기여가 부족하다. 특히 performatively stable model이라는 이름과 dynamically attracting equilibrium이라는 뜻을 혼동하지 않아야 한다.

## 3 normalized square의 exact 부호 반전 재계산

두 bit (a,b)에 f_theta=(cos(theta)*a,sin(theta)*b)를 둔다. theta*=pi/4에서 점들이 square가 된다. c=cos(2theta)이면 한 anchor에 대한 negative scores는 {1,c,−c,−1}. One-negative InfoNCE는 ell(s)=log(1+exp(s−1)).

q=(1−epsilon)softmax(kappa*s)+epsilon/4, Z=exp(kappa)+exp(−kappa)+2, q0=(1−epsilon)/Z+epsilon/4로 둔다. theta*에서 c′=−2, c″=0이고 Z′=0이다. 따라서 직접 미분하면

```
frozen angle curvature = 8*q0*ell″(0)
adaptive field derivative = 8*[q0*ell″(0)+(1−epsilon)*kappa*ell′(0)/Z].
```

이는 분포의 반응이 없는 경우와 있는 경우를 정확히 나눈다. epsilon=.1, kappa=−2에서 값은 각각 +.1879519276와 −.2186626593이다. `check_curvature.py`가 analytic formula와 1e−5 finite difference를 비교했으며 kappa={−10,−2,−1,0,1}의 최대 오차는1.38e−10이다.

또한 kappa=−10이면 adaptive derivative는 +.0385076147로 다시 양수가 된다. 극단적인 쉬운 sampling에서는 epsilon floor의 uniform 성분이 상대적으로 지배적이므로, “easy 정도가 강할수록 무조건 불안정하다”는 단조 일반화는 거짓이다. 이 비단조성도 위 한 줄 식으로 설명되며 그 자체로 큰 기여가 확보된 것은 아니다.

## 4 implicit objective 설명이 어디까지 적용되는가

가중치 r(s)에 대해 sample gradient r(s)*ell′(s)는 primitive H′(s)=r(s)*ell′(s)를 갖는다. 대칭점에서 나타난 추가 곡률 r′ell′는 감소하는 reweighting의 latent robust loss 곡률에 대응한다. 따라서 위 부호 반전은 기존 self-paced 설명과 경쟁해야 한다.

하지만 전역 scalar potential을 함부로 선언해서도 안 된다. 독립 score coordinates s_i를 쓰고 pure-softmax q를 두면, G_i=q_i*ell′(s_i)의 cross derivatives는 일반적으로 서로 다르다:

```
partial_j G_i = −kappa*q_i*q_j*ell′(s_i), i!=j.
```

ell′(s_i)!=ell′(s_j)일 때 curl이0이 아니므로 G 자체는 일반적으로 gradient field가 아니다. Pure-softmax에서는 Z*G가 additive primitive의 gradient가 되는 integrating factor를 갖지만, epsilon uniform mixture에는 그 환원이 자동 적용되지 않는다. 본 1D angle family에서는 항상 primitive를 만들 수 있으므로 그것만으로 고차원 동역학의 새 기제를 입증했다고 볼 수 없다.

## 5 같은 objective의 optimizer failure라는 해석은 제외

q_theta(z)>0이므로 기준 고정 law p(z)에 대한 exact importance weight p(z)/q_theta(z)를 detached로 곱하면

```
E_{z~q_theta}[(p(z)/q_theta(z))*grad ell(theta,z)]
  = E_{z~p}[grad ell(theta,z)].
```

Population field에서 sampling dependence는 정확히 사라진다. 따라서 현재 관측된 차이는 동일한 uniform objective를 푸는 방법끼리의 순수한 optimizer failure가 아니다. 의도적으로 기울기를 재가중하는 학습 규칙 또는 decision-dependent objective다. Finite-sample importance variance는 다른 질문이므로 지금 결과와 섞지 않는다.

## 6 착수 판정에 필요한 추가 증거

전체 sphere에서도 frozen/adaptive 부호 차이가 살아남는다면 restricted-angle artifact라는 반론은 줄어든다. 그래도 다음 중 하나가 추가로 필요하다.

1. 기존 performative sensitivity bound나 robust reweighting 원리만으로 예측되지 않는, SSL의 positive geometry·factor structure에 특유한 정량 조건.
2. 배치수/negative수·augmentation noise·더 많은 factor에서도 사전에 정한 criterion으로 검증되는 경계. 단순 새로운 sweep는 부족하다.
3. 실제 filtering 규칙의 detached update를 정확히 도출했을 때도 같은 현상이 나타나고, 기존 static reweighting 설명이 놓치는 concrete prediction.

현재로서는 원래 unconstrained 영구배제 가설의 반증은 강하고, normalized exact counterexample는 실질적인 계산 결과지만 독립 신규성의 근거는 약하다. 최종 논문의 핵심이 단지 frozen과 adaptive의 Hessian 부호가 다르다는 것이라면 **현재 상태에서 진행 권고는 하지 않는다**. 이 계산을 원리 검증 사례로 보존하고, 위 추가 증거가 없으면 broad 질문을 해결했다고 주장하지 않은 채 기각 또는 판정 보류로 정리하는 편이 타당하다.
