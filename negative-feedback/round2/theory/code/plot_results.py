"""Scientific figure built from executed exact finite-sum CSVs only."""
from pathlib import Path
import csv
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
ROOT=Path(__file__).resolve().parents[1];OUT=ROOT/'results'
def read(name):
    with (OUT/name).open() as f:return list(csv.DictReader(f))
ctrl=read('denominator_controls.csv');sp=read('policy_spectrum.csv')
plt.rcParams.update({'font.size':10,'axes.spines.top':False,'axes.spines.right':False,'svg.fonttype':'none'})
fig,axs=plt.subplots(1,3,figsize=(13.2,3.7),layout='constrained')
ax=axs[0]
for pos,label,color in [(1,'InfoNCE','#1768AC'),(0,'Decoupled','#D47818')]:
    rows=[r for r in ctrl if r['kind']=='natural' and int(r['positive'])==pos and int(r['K'])<=32]
    k=np.array([int(r['K']) for r in rows]);T=np.array([float(r['threshold']) for r in rows])
    ax.plot(k,T,label=label,color=color,lw=2)
ax.axhline(float(rows[0]['eta']),color='#333',ls='--',label=r'$\eta$ (natural filter)')
ax.set(xlabel='Negative count K',ylabel='Stability threshold',title='A  Natural exponential filter',ylim=(0,1.02))
ax.legend(frameon=False,fontsize=9)
ax=axs[1]
for pos,label,color in [(1,'InfoNCE','#1768AC'),(0,'Decoupled','#D47818')]:
    rows=[r for r in ctrl if r['kind']=='natural' and int(r['positive'])==pos and int(r['K'])<=16]
    k=np.array([int(r['K']) for r in rows]);val=np.array([float(r['adaptive_balance']) for r in rows])
    ax.plot(k,val,'o-',ms=3,label=label,color=color)
ax.axhline(0,color='#666',lw=.8)
ax.set(xlabel='Negative count K',ylabel='Balance eigenvalue of G',title='B  Full-space sign transition')
ax.text(.04,.96,'Positive: locally restoring\nNegative: unstable',transform=ax.transAxes,va='top',fontsize=9)
ax=axs[2]
alpha=[-1.5,-.9,0.];rows=[next(r for r in sp if float(r['alpha'])==a and int(r['K'])==1) for a in alpha]
x=np.arange(len(rows));ax.bar(x-.16,[float(r['frozen_balance']) for r in rows],width=.3,color='#A6ADB4',label='Matched frozen q')
ax.bar(x+.16,[float(r['adaptive_balance']) for r in rows],width=.3,color=['#2A8C68','#D47818','#B13242'],label='Adaptive q')
ax.axhline(0,color='#666',lw=.8);ax.set_xticks(x,[str(a) for a in alpha])
ax.set(xlabel=r'Filter-shape parameter $\alpha$',ylabel='Balance eigenvalue of G',title='C  Same q, different feedback')
ax.legend(frameon=False,fontsize=9)
for fmt in ['svg','png','pdf']:fig.savefig(OUT/f'count_stability.{fmt}',dpi=180)
