"""Deterministic publication tables and one compact scientific figure."""
import csv,json,pathlib,platform
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from run_population import ROOT
R=ROOT/'results'
base=[]
for phase in ['pilot','confirmation']:base+=json.loads((R/f'{phase}_summary.json').read_text())['summary']
spectral=json.loads((R/'spectral_summary.json').read_text())['summary'];contrastive=json.loads((R/'contrastive_summary.json').read_text())['summary'];long=json.loads((R/'long_equal_summary.json').read_text())['summary']
policies=['scratch','clean_long','continue','optimizer_reset','optimizer_normmatch','teacher_sync','predictor_reset','head_teacher']
lines=['# 실제 실행 결과 — 후보 1','', '주지표는 normalized representation에 고정 noise sigma=.1를 더했을 때의 population 최적 **linear R²**다. noiseless 정보량, 모든 decoder의 성능, 자연 이미지 결과가 아니다. 4개 pilot + 4개 별도 확인 seed를 사용했으며 동일 DGP·구현을 공유하는 초기값 반복이다.','', '## 원래 equal-spectrum 설정, clean 3000 step','', '| 정책 | 최종 R² 최솟값 | 중앙값 | 최댓값 | 사전 90% 기준 도달 |','|---|---:|---:|---:|---:|']
for p in policies:
 rows=[r for r in base if r['policy']==p];a=[r['final_r2'] for r in rows];n=sum(r['recovery']['0.9'] is not None for r in rows)
 lines.append(f'| {p} | {min(a):.6g} | {np.median(a):.6g} | {max(a):.6g} | {n}/8 |')
lines +=['','Scratch의 초기 factor 3 R² 자체가 높다. 특히 일부 seed는0step부터 threshold를 충족하므로 위 scratch값은 새 factor 획득만이 아니라 random initialization의 정보 보존을 포함한다. 그 값을 새 학습 성공으로 읽지 않는다.','', 'Predictor reset과 head+teacher는 seed 101에서 각각 .7221/.7447의 상당한 **부분 회복**을 보였다. 모든 reset이 무효라는 결론은 틀리다. 다만 사전 90% 기준까지 도달한 reset은 없었다. Predictor parameter와 해당 Adam moments를 함께 reset한 추가 control에서 seed 101은 .0490으로 달라졌다. Head개입의 결과를 head에만 저장된 기억의 증거로 해석하지 않는다.','', '## 장기 continuation 및 상대 pair correlation 변경','', '| seed | 원래 rho3=.9:3000 | 원래 rho3=.9:15000 | rho3=.8:15000 | rho3=1:15000 |','|---|---:|---:|---:|---:|']
for r in long:
 seed=r['seed'];vals=[next(x for x in spectral if x['seed']==seed and x['rho3']==rho)['r2_15000'] for rho in [.8,1.]]
 lines.append(f"| {seed} | {r['r2_3000']:.6g} | {r['r2_15000']:.6g} | {vals[0]:.6g} | {vals[1]:.6g} |")
lines +=['','원래 setting에서도15000 step까지8개 seed 중 4개가 .9이상으로 회복했다. 3000 step 실패를 영구 고착으로 읽을 수 없다. rho3=1은8개 모두 .972–.985로 회복했으나 다른factor 손실이 동반될 수 있다(예:seed3의factor 2 R²≈4.87e−6). rho3=.8의seed 101도 .9559로 회복했다. 따라서 작은 fixed-head spectral sign은 실제 MLP의 필요충분조건이 아니다.','', '## 목적함수 대조: population InfoNCE, temperature1','', '| seed | deficit후 R² | clean90%도달 step | clean3000 R² | clean15000 R² |','|---|---:|---:|---:|---:|']
for r in contrastive:lines.append(f"| {r['seed']} | {r['switch_r2']:.3g} | {r['t90']} | {r['r2_3000']:.8f} | {r['r2_15000']:.8f} |")
lines +=['','같은 raw marginal·pair복구·encoder·Adam/LR 아래 contrastive 대조에서는 50–250 step에90%기준에 도달했다. Agreement와 이 비교에서 teacher/head/목적함수가 함께 달라지므로 **teacher만의 인과효과**가 아니다. [직접 증명C](theory.md)는 제한 diagonal family에서 agreement의 flat optimum과 contrastive의 strict full-factor optimum을 구분한다.','', '## 검산과 증거 강도','', '- Owner cosine gradient 중앙차분 최대8.89e−11, InfoNCE4.04e−11. Pair marginal/correlation 최대3.34e−16.','- 독립 reviewer는 새 구현으로 cosine5.28e−10, contrastive4.81e−11, flat family 및 dormant-mode Jacobian을 검산했다. [독립 기록](../prevalidation-20261022/reviews/recovery/review.md).','- [이론A–C](theory.md)는 직접 증명, neural표는 직접 실행이다. 전자의 제한 모형이 후자의 모든 경로를 정량 설명했다는 주장은 없다.','- EMA teacher sync는 초기lag만 없앤다. Adam normmatch는 block scalar norm만 맞춘다. 어느개입도 고유한 기억위치나 SSL특유원인을 증명하지 않는다.','- Figure의 각 선은 정해진 모든seed를 포함한다. 원자료의 고정간격CSV, 모든 run summary, full trace SHA/재생성경로를 보존했다.','', '![All-seed recovery controls](results/recovery_controls.png)','', '## 저장·재현','', 'Fulltrace는 outcome별 선택 없이500 step간격+final로 CSV를 줄였다. 모든 run의최종값과 50 step threshold는summary에 남아 있다. Full raw JSON경로·행수·바이트수·SHA256은 각 `*_trace_manifest.json`에 있다. Scratch raw는 재현 가능한 임시자료이며 저장소의코드+seed가 보존 근거다. 이 실행의full trace 디렉터리는 `/workspace/scratch/7655b5d2f6fb/research/ssl-recovery-raw`다.','', '실행명령은 [reproduction.md](reproduction.md). 큰 dataset/checkpoint/원문PDF는 저장소에 넣지 않았다.']
(ROOT/'results.md').write_text('\n'.join(lines)+'\n')

def curves(name):
 with (R/f'{name}_curves.csv').open() as f:return list(csv.DictReader(f))
fig,ax=plt.subplots(2,2,figsize=(11,7.2),layout='constrained')
rows=curves('pilot')+curves('confirmation')
for p,c in [('scratch','#377eb8'),('continue','#e41a1c'),('predictor_reset','#4daf4a')]:
 steps=sorted(set(int(r['step']) for r in rows if r['policy']==p));a=np.array([[float(next(r for r in rows if r['policy']==p and int(r['seed'])==seed and int(r['step'])==t)['f_r2_3']) for t in steps] for seed in [0,1,2,3,101,102,103,104]])
 ax[0,0].plot(steps,np.median(a,axis=0),label=p,color=c);ax[0,0].fill_between(steps,a.min(0),a.max(0),color=c,alpha=.13)
ax[0,0].set(title='Equal spectrum: median and full seed range',xlabel='Clean updates',ylabel='Factor 3 noisy linear R²');ax[0,0].legend(fontsize=8)
rows=curves('long_equal')
for seed in [0,1,2,3,101,102,103,104]:
 q=[r for r in rows if int(r['seed'])==seed];ax[0,1].plot([int(r['step']) for r in q],[float(r['f_r2_3']) for r in q],lw=1,label=str(seed))
ax[0,1].set(title='Original setting: long continuation, all seeds',xlabel='Clean updates',ylabel='Factor 3 noisy linear R²');ax[0,1].legend(fontsize=7,ncol=4)
rows=curves('contrastive')
for seed in [0,1,2,3,101,102,103,104]:
 q=[r for r in rows if int(r['seed'])==seed and r['policy']=='continue' and int(r['step'])<=3000];ax[1,0].plot([int(r['step']) for r in q],[float(r['f_r2_3']) for r in q],lw=1)
ax[1,0].set(title='InfoNCE control: all seeds (500-step plot grid)',xlabel='Clean updates',ylabel='Factor 3 noisy linear R²')
for seed in [0,1,2,3,101,102,103,104]:
 vals=[next(r for r in spectral if r['seed']==seed and r['rho3']==rho)['r2_15000'] for rho in [.8,1.]];equal=next(r for r in long if r['seed']==seed)['r2_15000'];ax[1,1].plot([.8,.9,1.],[vals[0],equal,vals[1]],'o-',lw=.8,ms=3)
ax[1,1].set(title='Correlation change: final at 15000, all seeds',xlabel='Restored factor correlation',ylabel='Factor 3 noisy linear R²');ax[1,1].set_xticks([.8,.9,1.])
for a in ax.flat:a.set_ylim(-.03,1.03);a.grid(alpha=.2)
fig.savefig(R/'recovery_controls.png',dpi=150);plt.close(fig)
env=dict(python=platform.python_version(),numpy=np.__version__,matplotlib=matplotlib.__version__,platform=platform.platform(),threads='OPENBLAS_NUM_THREADS=1',seed_kind='initialization only; exact finite-state expectation, no sampled training data')
(R/'environment.json').write_text(json.dumps(env,indent=2))
