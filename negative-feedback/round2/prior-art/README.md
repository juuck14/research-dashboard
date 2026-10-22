# Round 2: 독립 신규성 심사와 대안 설명의 직접 검증

2026-10-22. 상태: **범위를 제한한 수정 방향의 진행 근거 있음**. 이것은 논문 채택 가능성이나 문헌의 전수조사 완료를 뜻하지 않는다.

## 판정

중심 기여 후보는 **유한 K의 InfoNCE에서 detached score policy의 local response slope와 loss curvature가 경쟁하는 정확한 mode law, 그리고 K에 따른 임계값의 엄밀한 단조성**이다. 확인한 가장 가까운 원문 정리들에서 이 결과가 직접 따라오지는 않는다. ‘feedback이 frozen minimum을 불안정하게 만들 수 있다’, `DG=H+B`, ‘같은 equilibrium weights인데 안정성이 다르다’는 일반적인 주장은 독립 기여에서 제외한다. 아래 환원으로 기존 이론만으로도 그 현상을 만들 수 있음을 직접 보였다.

기존 negative-number 연구와의 차이는 ‘K도 중요하다’가 아니다. 정해진 정책의 **전체 기대 vector field**에서 정확한 안정/불안정 조건과 부호가 바뀌는 K를 계산한다는 점이다. 유한 K가 infinite-negative objective와 다르다는 사실 자체는 이미 알려져 있다. 이를 같은 목적의 SGD 분산 감소 효과로 해석해서도 안 된다.

이전보다 더 강한 제한도 확보했다. 자연적인 exponential easy policy에서는 factor-balance mode가 큰 K에 안정화되어도 다른 구면 mode가 불안정해질 수 있다. 그러나 이것은 natural family에서 full rescue가 불가능하다는 뜻은 아니다. 첫 실패를 본 뒤 root가 분석적으로 선택한 epsilon=.3,kappa=-log4의 follow-up은 우리 독립 계산에서 K5부터 balance가 안정하며 normal_ab도 K1-128에서 양수였다. 이후 theory 담당은 **열린 natural exponential parameter 영역에 대한 full-sphere theorem**과 이 예의 InfoNCE K≥5/DCL K≥8 cutoffs를 증명하고 별도 finite-difference로 검산했다. 본 담당은 theorem.md §9의 열린 영역 증명과 §8의 DCL 확장을 읽어 대조했다. shaped policy는 static weights와 response slope를 분리하는 통제이지, natural exponential에서 현상이 없음을 전제로 만든 장치가 아니다.

## 실제 확보한 결과

| 공격/검증 | 결과 | 해석 |
|---|---|---|
| A의 일반적 신규성 | strongly convex squared loss와 full-support two-point induced distribution으로 동일 frozen law/반대 adaptive stability를 정확히 구성 | A의 일반 원리는 performative prediction의 사례다 |
| K1의 robust-loss 설명 | balance curvature가 `q(0) ell''(0)+q'(0) ell'(0)`로 환원 | self-paced reweighting 원리만으로 K1 부호 반전을 설명할 수 있다 |
| exponential K-infinite field | epsilon=0에서 effective inverse temperature `1+kappa`의 potential gradient와 정확히 일치; 60 random representation/parameter checks 최대 오차 `1.11e-16` | infinite-K 임계값1 자체를 새 원리로 내세우면 안 된다 |
| natural exponential, kappa=-1, epsilon=.1 | K8: balance `+.0043669`, normal_ab `-.0014561`; K128: `+.0542300`과 `-.0172401` | scalar rescue를 full stability라고 부르는 해석을 반박 |
| exploratory natural exponential follow-up, kappa=-log4, epsilon=.3 | 독립 moments: K5부터 balance양수, normal_ab 최소 `+.00753310`; theory: full InfoNCE K≥5, DCL K≥8 | natural family 전체가 실패한다는 추론도 반박. 일반 열린 영역의 theorem이 사후 단일 사례 의존을 제거 |
| DCL의 negative-only denominator | shaped alpha=-.9에서 K1 balance `-.2078873`, K16 `+.00958794`; threshold0→1 | negative-positive coupling을 제거해도 count-dependent slope effect는 남는다. 기존 NPC 설명만으로 충분하지 않다 |

이는 학습된 이미지 모델의 결과가 아니라 **직접 도출한 항등식/반례와 exact finite-state 계산**이다. DCL 계산은 scalar balance control이며 DCL 전체 tangent 안정성 증명이 아니다.

## 산출물

- [문헌 원문 대조와 신규성 범위](literature_audit.md)
- [직접 수행한 환원·증명·계산의 해석](reductions.md)
- [실행 전 검사 기준 및 문헌을 읽고 추가한 control](protocol.md)
- [독립 실행 코드](audit_checks.py)
- [결과 JSON](results/audit_checks.json), [natural exponential CSV](results/natural_exponential.csv), [분석 후 선택한 natural follow-up](results/natural_exponential_followup.csv), [DCL scalar control CSV](results/dcl_scalar_control.csv)
- [변경 이력과 남은 반론](progress.md)

재현: 저장소의 기존 Python 환경에서 `python negative-feedback/round2/prior-art/audit_checks.py`. NumPy와 SciPy만 사용한다. 다른 연구 코드를 import하지 않는다. seed901-910은 algebraic identity의 좌표 불변 검산용이며 확률적 학습의 반복 실험을 대신하지 않는다.

## 논문 원고에서 허용할 중심 문장

“A finite-negative denominator changes the exact response-slope threshold at which balanced factor geometry loses local stability. In a normalized finite-state model the threshold strictly increases with negative count, so additional negatives can stabilize a borderline response policy. Matching its equilibrium sampling weights does not recover this threshold. The effect survives a negative-only denominator, but balance-mode stabilization need not imply stability in other representation directions.”

이 문장은 제한 모형의 분석 결과다. 최종 theorem과 full-sphere 증명은 [theory 담당 결과](../theory/)를 함께 확인해야 한다. 본 독립 심사는 정확한 phase law가 이미 출판되었다는 근거를 찾지 못했지만, 새 설정이라는 이유만으로 신규성을 인정한 것은 아니다. 경쟁 이론의 실제 정리에서 무엇이 도출되는지와 무엇이 도출되지 않는지를 따로 검토했다.

## 최종 독립 판정

**범위를 제한한 이론 논문으로 진행을 권고한다.** 이제 중심 가설 자체를 미래 검증에 맡긴 상태는 아니다. Exact full-spectrum law, K와 positive-denominator offset에 대한 엄밀한 threshold monotonicity, natural monotone exponential 정책의 열린 full-rescue 영역이 연결되어 있다. 기존 generic feedback 설명과 NPC 설명으로 줄여본 뒤에도 유한-K 정량 예측이 남는다. 이것은 증명 없는 흥미로운 가설이나 첫 반례의 설정 변경만으로 만든 새로움과는 구별된다.

진행 권고의 범위는 finite-state representation geometry다. 학습 정보의 영구 소실, 일반 neural encoder의 global convergence, 실제 false-negative 탐지 알고리즘의 실패까지 입증한 것은 아니다. 논문 완성 단계에서 필요한 일은 이 확보된 결과의 중요성을 전달하고 경계 조건을 보강하는 것이다. 확보하지 않은 광범위한 경험 법칙을 중심 주장으로 바꾸면 이 권고는 적용되지 않는다.
