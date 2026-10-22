from pathlib import Path
import csv
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
ROOT=Path(__file__).resolve().parent
with (ROOT/'results/positive_channel.csv').open() as f: positive=list(csv.DictReader(f))
with (ROOT/'results/sgd.csv').open() as f: sgd=list(csv.DictReader(f))
fig,ax=plt.subplots(1,2,figsize=(10,3.8),layout='constrained')
for policy,color in [('frozen','#2271B3'),('adaptive','#C44E52')]:
    rows=[r for r in positive if r['policy']==policy and float(r['h'])==1e-5]
    ax[0].plot([float(r['eta']) for r in rows],[float(r['max_nonzero']) for r in rows],'-o',color=color,label=policy)
ax[0].axhline(0,color='.5',lw=1);ax[0].set(xlabel='Positive bit-flip probability',ylabel='Largest nonrotation flow eigenvalue',title='Exact population stability')
ax[0].legend(frameon=False)
for i,policy in enumerate(['uniform','frozen','adaptive']):
    rows=[r for r in sgd if r['policy']==policy]
    vals=[float(r['worst_accuracy']) for r in rows]
    ax[1].scatter(i+np.linspace(-.08,.08,len(vals)),vals,s=35,color=['#888888','#2271B3','#C44E52'][i],alpha=.8)
ax[1].axhline(.5,color='.5',lw=1,ls='--');ax[1].set(xticks=[0,1,2],xticklabels=['uniform','frozen','adaptive'],ylim=(.45,1.04),ylabel='Worst-factor Bayes accuracy',title='Minibatch SGD, fixed feature noise 0.05')
fig.savefig(ROOT/'results/robustness.svg');fig.savefig(ROOT/'results/robustness.png',dpi=170)
