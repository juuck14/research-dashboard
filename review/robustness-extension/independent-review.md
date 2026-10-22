# Positive-channel 및 SGD 확장 독립 감사

2026-10-22. Root가 이미 실행한 run_checks.py와 protocol/results를 읽고 source를 수정하지 않은 채 독립 검산했다.

## 확인한 결과

- **Gradient:** Root의 exactfield는 anchor/positive/negative 64개 상태 조합을 독립 scalar loss로 평균한 함수의 normalized tangent gradient와 일치한다. eta0/.01/.1, random unit embeddings seed77/2011/4027, 세 frozen q에서 총432 coordinate 중앙차분 최대오차1.24e-10. 현재 q를 detach하여 평가했으며 FD 중 q를 갱신하지 않았다.
- **Positive channel:** 두 독립 bitflip 채널의 고유값은 `1,1-2eta,1-2eta,(1-2eta)^2`이며 구현 오차2.22e-16. eta=.1에서도 invertible이고 확률적 positive에 요인 구분 신호가 남는다.
- **Sampled training:** identity-positive에서 anchor/negative counts의 기대값은 q/4이고, root SGD gradient의 기대값과 exactfield 최대차5.20e-17. 각 step의 shared encoder 양쪽 score 기여, unit-sphere projection, retraction이 일관된다. Full sampler differentiation은 포함하지 않는다.
- **Bayes 측정:** evaluate는 equal-prior four-state isotropic Gaussian-mixture에서 각 bit의 class likelihood들을 logsumexp로 합친 Bayes-optimal classifier다. Feature noise sigma=.05를 명시한 조건에서 정확하다. 독립 sanity 실행의 square accuracy=[1,1], 완전 onefactor representation=[1,.5]다.

## 결과 보고에 필요한 한계

1. Nonidentity-positive 실험은 **population Jacobian** 확인이고,30회 실제 stochastic training은 **identity positives**다. 이 둘을 합쳐 noisy-positive SGD까지 검증했다고 쓰면 안 된다.
2. 사전 protocol의 합격선은 primary5/6 이상, confirmation3/4 이상이다. 실행 관측이6/6 및4/4이므로 '사전 기준6/6+4/4'라고 쓰지 않는다.
3. 평가 noise는 모델 입력이나 augmentation의 noise가 아니라 **학습된 feature에 가한 명시적 관측 채널**이다. noisy Bayes factor accuracy≈.5는 그 채널 아래의 접근성/강건성 저하이며 unnoised MI 소실의 증명이 아니다.
4. Four-state full lookup normalized SGD는 실제 확률적 최적화이지만 학습된 image encoder·실제 이미지·새 input generalization 실험은 아니다. finite lookup에 대한 차원·sampling 반론을 줄인 증거로 해석한다.
5. Same seed/common uniform draws는 policy 사이의 비교를 정당하게 결합한다. 평가용 Gaussian draws도 같은 seed90210을 재사용하므로 서로 다른 training seed 결과의 평가 noise가 독립이라고 주장하지 않는다. Training seeds 자체는 분리되어 있다.
6. Final vectors를 결과파일에 저장하지 않아 이 독립 감사에서 각 SGD run의 Bayes accuracy를 재계산하지는 않았다. 코드와 seed가 보존되어 재실행 가능하고 최종 벡터는 run당16개 실수로 작으므로 후속 분석을 위해 저장할 수 있다. 이번 감사는 정확 gradient와 평가식 및 기록된 결과 해석에 한정한다.

## 실행

`OPENBLAS_NUM_THREADS=1 python review/robustness-extension/independent_check.py`

결과 `results/independent_audit.json`에는 감사 대상 source SHA256과 수치오차를 저장했다. 이 실행은 root의30회 training을 다시 실행하지 않았다.

## 판정에 주는 영향

초기 identity-positive exact-flow 결과에 대해 'positive가 너무 자명하다', 'population ODE만의 현상이다', 'linear probe가 약해서 실패했다'는 세 대안 설명을 각각 완화한다. Full-rank positive channel에서 population sign flip이 유지되고, 작은 stochastic training에서도 명시적 noise 아래의 **Bayes readout** 악화가 재현된다는 점은 수정 주제의 실질적 증거를 강화한다. 자연스러운 실제 sampler와 encoder에서도 같은 phase law가 예측력을 갖는지 및 기존 performative theory를 넘는 학술적 기여는 여전히 핵심 후속 과제다.
