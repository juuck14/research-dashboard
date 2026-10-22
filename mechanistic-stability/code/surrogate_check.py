#!/usr/bin/env python3
"""Exact MI compositional contrast on a normalized rotation subfamily."""
from pathlib import Path
import csv,json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from run_study import matrices,ROOT

theta=np.linspace(0,np.pi/4,10001)
rows=[]
fig,ax=plt.subplots(figsize=(6,3.5),constrained_layout=True)
for k in [1.,.3,.1,.03,.01,.003,.001]:
    A,_=matrices(k)
    exact=(1+k*k)*np.abs(np.sin(2*theta))+np.abs(np.cos(2*theta))
    calc=[]
    for t in theta:
        R=np.array([[np.cos(t),-np.sin(t)],[np.sin(t),np.cos(t)]])
        C=A@R
        calc.append(np.sum(np.abs(C[:,0]*C[:,1])))
    calc=np.array(calc)
    rows.append(dict(kappa=k,formula_max_error=float(np.max(np.abs(calc-exact))),
        true_axis_loss=float(calc[0]),rotated_axis_loss=float(calc[-1]),
        gap=float(calc[-1]-calc[0]),predicted_gap=k*k,
        barrier_sample=float(calc.max()-calc[0]),
        barrier_exact=float(np.sqrt((1+k*k)**2+1)-1)))
    if k in [1.,.1,.001]:ax.plot(theta*180/np.pi,calc,label=f'kappa={k}')
with (ROOT/'results/surrogate.csv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
ax.set(xlabel='rotation (degrees)',ylabel='compositional contrast')
ax.legend();fig.savefig(ROOT/'figures/surrogate_landscape.png',dpi=180)
print(json.dumps({'max_formula_error':max(x['formula_max_error'] for x in rows),'rows':rows},indent=2))
