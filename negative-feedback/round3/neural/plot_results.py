"""Figures from preserved CSV/JSON outputs; no experiment or fitted parameter selection."""
from pathlib import Path
import csv, json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
ROOT = Path(__file__).resolve().parent
OUT = ROOT / 'results'
FIG = ROOT / 'figures'
FIG.mkdir(exist_ok=True)

def rows(name):
    with (OUT / name).open() as handle:
        return list(csv.DictReader(handle))

plt.rcParams.update({'font.family':'DejaVu Sans','font.size':10,'axes.spines.top':False,'axes.spines.right':False,'savefig.bbox':'tight'})
# All data choices are fixed in protocol.md. The shading is from the proved integer interval.
r = [x for x in rows('mixing_curve.csv') if float(x['rho']) == .05 and int(x['K']) <= 32]
k = np.array([int(x['K']) for x in r])
fig, ax = plt.subplots(1, 2, figsize=(10, 3.35))
for a in ax:
    a.axvspan(4.5,11.5,color='#d5eadb',zorder=0,label='Full stable window: K = 5–11')
    a.set_xlabel('Number of negatives K')
    a.set_xticks([1,4,8,12,16,24,32])
ax[0].plot(k,[float(x['mean_balance']) for x in r],color='#1c5c91',marker='.',label='Class-mean balance eigenvalue')
ax[0].plot(k,[float(x['within_normal']) for x in r],color='#b24425',marker='.',label='Within-class normal eigenvalue')
ax[0].axhline(0,color='black',lw=.8)
ax[0].set_ylabel('Gradient-field eigenvalue')
ax[0].set_title('Different modes impose opposite K constraints')
ax[0].legend(fontsize=8,loc='lower right')
ax[1].plot(k,[float(x['critical_rho']) for x in r],color='#b24425',label=r'Exact critical gap $\xi_K$')
ax[1].axhline(.05,color='#34674a',ls='--',label=r'Positive graph gap $\gamma=0.05$')
ax[1].axhline(.1034779521771101,color='gray',ls=':',label=r'$\xi_\infty=0.10348$')
ax[1].set_ylabel('Algebraic positive graph gap')
ax[1].set_title('Upper constraint is also present for frozen q')
ax[1].legend(fontsize=8,loc='lower right')
fig.tight_layout(); fig.savefig(FIG/'count_graph_window.png',dpi=180); fig.savefig(FIG/'count_graph_window.pdf');plt.close(fig)

tr=rows('window_parameter_trajectories.csv')
fig,ax=plt.subplots(1,3,figsize=(10,3.2),sharey=True)
for a,K in zip(ax,[4,8,16]):
    for pol,color in [('frozen','#236192'),('adaptive','#b24425')]:
        for seed in [4101,4102,4301]:
            rr=[r for r in tr if int(r['seed'])==seed and int(r['K'])==K and r['policy']==pol]
            a.plot([0]+[float(x['scaled_time']) for x in rr],[1]+[float(x['amplitude_ratio']) for x in rr],color=color,alpha=.8,lw=1.4,label=pol if seed==4101 else None)
    ts=np.linspace(0,3,100)
    a.plot(ts,np.exp((-1 if K==8 else 1)*ts),'k:',lw=1,label=r'$e^{\pm t|\lambda|}$')
    a.set_yscale('log');a.set_ylim(1e-10,40);a.set_xlabel(r'Scaled time $t|\lambda|$');a.set_title(f'K = {K}')
    a.grid(axis='y',alpha=.15)
ax[0].set_ylabel('Parameter-mode amplitude / initial')
ax[1].legend(fontsize=8,loc='lower left')
fig.suptitle('Actual shared MLP nonlinear gradient flows at a constructed reference',fontsize=11)
fig.tight_layout();fig.savefig(FIG/'neural_window_modes.png',dpi=180);fig.savefig(FIG/'neural_window_modes.pdf');plt.close(fig)

rr=rows('ordinary_runs.csv')
summ=json.loads((OUT/'ordinary_summary.json').read_text())
fig,ax=plt.subplots(1,2,figsize=(9.5,3.4))
seeds=[3801,3802,3901]
colors=['#236192','#648e37','#994062']
for seed,color in zip(seeds,colors):
    for pol,style in [('frozen','--'),('adaptive','-')]:
        r=[x for x in rr if int(x['seed'])==seed and x['policy']==pol]
        ax[0].plot([int(x['K']) for x in r],[float(x['weaker_energy']) for x in r],style,marker='o',color=color,label=f'{seed}, {pol}')
ax[0].axhline(.5,color='gray',lw=.8,ls=':');ax[0].set_xticks([2,4,5,8]);ax[0].set_ylim(0,.52)
ax[0].set_xlabel('Number of negatives K');ax[0].set_ylabel('Weaker semantic factor energy')
ax[0].set_title('Finite-time forks retain seed dependence',fontsize=10)
ax[0].legend(fontsize=7,ncol=2)
vals=[d['geometry']['square_gram_relative_error'] for d in summ['initials']]
ax[1].bar([str(s) for s in seeds],vals,color=colors)
ax[1].axhline(.001,color='black',ls='--',label='Prespecified applicability gate = 0.001')
ax[1].set_yscale('log');ax[1].set_ylabel('Warmup Gram relative error')
ax[1].set_xlabel('Seed');ax[1].set_title('0/3 warmups meet the square gate',fontsize=10)
ax[1].legend(fontsize=8)
fig.tight_layout();fig.savefig(FIG/'ordinary_scope_limit.png',dpi=180);fig.savefig(FIG/'ordinary_scope_limit.pdf');plt.close(fig)
print('Saved three PNG/PDF figure pairs from raw outputs.')
