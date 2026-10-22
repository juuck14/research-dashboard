"""Produce numeric summaries and scientific figures from the saved encoder runs."""
from pathlib import Path
import csv,json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
ROOT=Path(__file__).resolve().parent;OUT=ROOT/'results';FIG=ROOT/'figures';FIG.mkdir(exist_ok=True)
rows=json.loads((OUT/'runs.json').read_text())
audit={x['name']:x for x in json.loads((OUT/'ols_audit.json').read_text())}
initials=json.loads((OUT/'initial_probe_audit.json').read_text())
for r in rows:r.update(audit[f"{r['seed']}/{r['arm']}/{r['policy']}"])
metrics=['worst_linear','worst_rbf','worst_ols','worst_noise_linear','worst_noise_rbf','worst_noise_ols']
summary=[]
for arm in ['warmup','pca']:
 for policy in ['uniform','frozen','adaptive']:
  for split in ['primary','confirmation','all']:
   sub=[r for r in rows if r['arm']==arm and r['policy']==policy and (split=='all' or r['split']==split)]
   s={'arm':arm,'policy':policy,'split':split,'n':len(sub)}
   for key in metrics:
    a=np.array([r[key] for r in sub]);s[key]={'mean':float(a.mean()),'sd':float(a.std(ddof=1)),'min':float(a.min()),'max':float(a.max())}
   a=np.array([min(r['geometry']['walsh_energy_1_a_b_ab'][1:3]) for r in sub])
   s['minimum_factor_mean_energy']={'mean':float(a.mean()),'min':float(a.min()),'max':float(a.max())}
   summary.append(s)
(OUT/'aggregate.json').write_text(json.dumps(summary,indent=2)+'\n')
lines=['| Arm | Policy | Split | Clean ridge | Clean RBF | Clean OLS audit | Noisy ridge | Noisy RBF | Noisy OLS audit |','|---|---|---|---:|---:|---:|---:|---:|---:|']
for s in summary:
 lines.append('| '+' | '.join([s['arm'],s['policy'],s['split']]+[f"{s[k]['mean']:.4f} [{s[k]['min']:.4f}, {s[k]['max']:.4f}]" for k in metrics])+' |')
(OUT/'aggregate.md').write_text('\n'.join(lines)+'\n')
colors={'uniform':'#2575ad','frozen':'#32834b','adaptive':'#c44236'}
fig,axs=plt.subplots(2,2,figsize=(10.5,7.2),sharey=True)
for row,arm in enumerate(['warmup','pca']):
 for col,noisy in enumerate([False,True]):
  ax=axs[row,col];keys=metrics[3:] if noisy else metrics[:3];x=np.arange(3)
  for j,policy in enumerate(colors):
   sub=[r for r in rows if r['arm']==arm and r['policy']==policy]
   a=np.array([[r[k] for k in keys] for r in sub]);means=a.mean(0);dx=(j-1)*.20
   ax.plot(x+dx,means,'o-',color=colors[policy],label=policy,linewidth=1.5,markersize=5)
   ax.vlines(x+dx,a.min(0),a.max(0),color=colors[policy],lw=1.5)
   for i,rr in enumerate(a):ax.scatter(x+dx+(i-2.5)*.015,rr,color=colors[policy],s=12,alpha=.5)
  ax.axhline(.5,color='.65',ls=':',lw=1);ax.set_xticks(x,['Ridge .001','RBF .001','OLS audit']);ax.set_ylim(.44,1.025);ax.set_yticks([.5,.6,.7,.8,.9,1.0]);ax.grid(axis='y',alpha=.2)
  ax.set_title(f"{'Uniform SSL warmup' if arm=='warmup' else 'Unlabeled PCA control'} / {'feature noise .05' if noisy else 'clean features'}",fontsize=10)
  if col==0:ax.set_ylabel('Worst factor heldout accuracy')
axs[0,0].legend(loc='lower left',fontsize=8)
fig.suptitle('Shared 16–32–8 nonlinear encoder: six fixed seeds\nDots are seeds; lines mark means; vertical intervals are seed ranges',fontsize=12)
fig.tight_layout(rect=[0,0,1,.94]);fig.savefig(FIG/'readout_audit.png',dpi=180);fig.savefig(FIG/'readout_audit.svg');plt.close(fig)
fig,axs=plt.subplots(1,2,figsize=(10,3.6),sharey=True)
for ax,arm in zip(axs,['warmup','pca']):
 for policy in colors:
  sub=[r for r in rows if r['arm']==arm and r['policy']==policy]
  curves=[]
  for r in sub:
   ini=next(v for v in initials if v['arm']==arm and v['seed']==r['seed'])
   curves.append([min(ini['geometry']['walsh_energy_1_a_b_ab'][1:3])]+[min(t['factor_energy_a'],t['factor_energy_b']) for t in r['trace']])
  a=np.array(curves);t=np.array([0]+[v['step'] for v in sub[0]['trace']]);ax.plot(t,np.median(a,axis=0),color=colors[policy],label=policy,lw=2);ax.fill_between(t,a.min(0),a.max(0),color=colors[policy],alpha=.12)
 ax.set_title('Uniform SSL warmup' if arm=='warmup' else 'Unlabeled PCA control');ax.set_xlabel('Fork SGD steps');ax.set_yscale('log');ax.grid(alpha=.2)
axs[0].set_ylabel('Smaller mean factor Walsh energy');axs[0].legend(fontsize=8)
fig.suptitle('Adaptive sampling compresses a factor mean, while a residual signal remains\nMedian and full seed range; theory concerns local geometry, not information erasure',fontsize=10)
fig.tight_layout(rect=[0,0,1,.88]);fig.savefig(FIG/'factor_energy_dynamics.png',dpi=180);fig.savefig(FIG/'factor_energy_dynamics.svg');plt.close(fig)
print(json.dumps({'runs':len(rows),'figures':['readout_audit','factor_energy_dynamics']}))
