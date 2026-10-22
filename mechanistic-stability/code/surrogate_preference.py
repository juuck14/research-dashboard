#!/usr/bin/env python3
import csv,json
import numpy as np
from run_study import matrices,sparse_bases,ROOT
theta=np.linspace(0,np.pi/4,10001)
rows=[]
for k in [.3,1.,2.]:
    for w in [.5,1.,2.,3.]:
        A,_=matrices(k,np.array([1,1,w,w]))
        amin,anon,_=sparse_bases(A)
        formula=(1+k*k)*np.abs(np.sin(2*theta))+w*w*np.abs(np.cos(2*theta))
        direct=[]
        for t in theta:
            R=np.array([[np.cos(t),-np.sin(t)],[np.sin(t),np.cos(t)]])
            C=A@R;direct.append(np.abs(C[:,0]*C[:,1]).sum())
        direct=np.array(direct)
        rows.append(dict(kappa=k,diagonal_row_weight=w,sparsity_min=amin,
            nonaligned_sparsity_min=anon,true_axis_contrast=float(direct[0]),
            rotated_axis_contrast=float(direct[-1]),rotation_minimum=float(direct.min()),
            minimum_angle=float(theta[direct.argmin()]*180/np.pi),
            formula_error=float(np.abs(direct-formula).max()),
            gram_error=float(np.abs(A.T@A-(1+w*w+k*k)*np.eye(2)).max())))
with (ROOT/'results/surrogate_preference.csv').open('w',newline='') as f:
    wr=csv.DictWriter(f,fieldnames=list(rows[0]));wr.writeheader();wr.writerows(rows)
summary=dict(cases=len(rows),wrong_rotation_strictly_preferred=sum(r['rotated_axis_contrast']<r['true_axis_contrast']-1e-10 for r in rows),
    max_formula_error=max(r['formula_error'] for r in rows),max_gram_error=max(r['gram_error'] for r in rows),
    decisive_case=[r for r in rows if r['kappa']==1 and r['diagonal_row_weight']==2][0],
    limitation='Exact preference among rotations with fixed Jacobian metric; no arbitrary decoder training')
(ROOT/'results/surrogate_preference_summary.json').write_text(json.dumps(summary,indent=2)+'\n')
print(json.dumps(summary,indent=2))
