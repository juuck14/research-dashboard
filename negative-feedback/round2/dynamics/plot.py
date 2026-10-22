from pathlib import Path
import csv
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
P=Path(__file__).resolve().parent
with (P/'results'/'trajectories.csv').open() as f:rows=list(csv.DictReader(f))
fig,axes=plt.subplots(1,2,figsize=(10,3.8),sharey=True)
for ax,K in zip(axes,[4,5]):
    for policy,color in [('frozen','#7c8793'),('adaptive','#b74436')]:
        for seed in [8101,8102,8301,8302]:
            a=[r for r in rows if int(r['K'])==K and r['policy']==policy and int(r['seed'])==seed]
            x=np.array([float(r['scaled_time']) for r in a]);y=np.array([float(r['ratio']) for r in a])
            ax.plot(x,np.maximum(y,1e-12),'-o',color=color,alpha=.6,label=policy if seed==8101 else None,ms=4)
    x=np.linspace(0,3,100);ax.plot(x,np.exp(x if K==4 else -x),'--',c='black',label='local prediction',lw=1.2)
    ax.set(yscale='log',xlabel=r'Scaled time $t|\lambda_b|$',title=f'K = {K}: '+('unstable' if K==4 else 'stable'),ylim=(1e-12,40))
    ax.grid(alpha=.15)
axes[0].set_ylabel('Absolute factor imbalance / initial value')
axes[1].legend(frameon=False)
fig.suptitle('Natural exponential filter: full d4 population flow, four matched initializations',fontsize=11)
fig.tight_layout()
for suffix in ['png','svg']:fig.savefig(P/'results'/f'cutoff_flow.{suffix}',dpi=180)
