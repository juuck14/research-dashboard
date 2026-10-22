# 실행 전 계획 2026-10-22

이 파일은 수치 실험을 실행하기 전에 작성했다. 모든 결과는 좁은 모형에 한정하며 실제 DINO/JEPA를 대표한다고 주장하지 않는다.

## 관측·모형

1. 두 독립 binary factor의 유한 상태 X=(X1,X2)∈{-1,+1}². Y는 각 bit를 독립 flip하여 E[Yj|X]=rho_j Xj. stationary distribution uniform. rho_j>0이면 입력, 초기 identity teacher 및 frozen conditional-expectation target 모두 각 요인을 구분한다. encoder output dimension 2로 충분하다.
2. Population squared prediction: exact Bayes predictor f_t(X)=E[g_t(Y)|X]. Teacher update g_{t+1}=(1-beta)g_t+beta f_t. Full-rank initial teacher diag(a1,a2), a_j>0. Frozen teacher 대조, total-norm normalization, per-coordinate variance whitening을 비교한다.
3. Linear predictor + student + EMA teacher의 population gradient flow. diagonal modes (w,p,a); cross-view correlation rho>0; dot w=p(rho*a-p*w)-eta*w; dot p=w(rho*a-p*w)-eta*p; dot a=beta(w-a). frozen teacher에서는 dot a=0. 원래 scalar 관측정보는 동일하다.

## 사전 분석 가설·판정

- Exact operator는 Markov smoothing이며 positive nonconstant eigenmodes를 수축시킬 것. normalization은 power iteration, whitening은 scaling 소실을 없앨 가능성. 이것은 기존 원리 확인이며 새로운 발견으로 세지 않는다.
- Trainable-predictor flow의 balanced nonzero fixed points는 p±=(rho±sqrt(rho²-4eta))/2에 해당할 것. 이는 Tian2021 식의 rescaling 후보이며 직접 환원되면 독립 신규성 주장을 기각한다.
- EMA speed 효과가 고정점 위치를 바꾸는지와 수렴속도만 바꾸는지 분리한다. plateau를 안정점으로 단정하지 않는다.

## 실행·확인

- deterministic exact spectrum: rho=(0.9,0.5), beta=(0.1,0.5,1), a0=(1,0.1), horizon 0..200. float arithmetic와 analytic formula 비교.
- primary ODE grid: rho∈{0.5,0.8}, eta∈{0,0.02,0.06}, beta∈{0.1,1,10}, balanced w0=p0=a0∈{0.01,0.1,0.4,0.8}; scipy solve_ivp T=500 및 필요시 horizon extension. 검증은 training 아닌 population oracle.
- 확인 조건: primary grid 밖 rho∈{0.35,0.65,0.95}, beta∈{0.03,0.3,3}, eta∈{0.005,0.025}; 초기 조건 jitter seeds 20261022, 20261023, 20261024. analytic fixed-point/Jacobian 판정과 수치 결과 일치 여부 기록.
- fixed readout additive noise sigma∈{0,0.01}에서 factor R²=a_j²/(a_j²+sigma²). 무잡음에서 비영 scaling은 정보 손실이 아님을 명시한다.
- neural embedding/large image experiment는 핵심 원리가 선행이론으로 환원되지 않을 때만 고려. 무의미한 계산 확장은 하지 않는다.

## 기록

코드·환경·명령·CSV·그림을 저장. 수치 확인과 증명을 구분. 가설/모형 변경은 progress.md에 이유 기록 후 실행. 모든 초기 w,p,a>0 및 rho>0 확인. tiny positive mode의 초기 소실 여부와 solver tolerance를 점검한다.

## P2 후 추가 검증 계획

기존 실행 완료 후, target의 full-rank linear 변형을 error라고 부르는 대안 해석을 검증한다. `context_basis_control.py`에서 위 4-state exact conditional expectation과 임의의 invertible 2×2 B 20개(seeds20261025,20261026), singular values(1,.001~.5)를 사용. `K(Y B^T)B^{-T}=KY`의 최대오차를 측정하고 새 정보 생성으로 표현하지 않는다. 추가 실행 전에 이 계획을 기록했다.
