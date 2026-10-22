#!/usr/bin/env python3
import csv,json
import numpy as np
from run_study import sparse_bases,ROOT
theta=np.linspace(0,np.pi/4,10001);rows=[]
for p in [3,4,6]:
    for w in [1.,2.,3.]:
        A=np.vstack([np.tile([1.,0],(p,1)),np.tile([0.,1],(p,1)),w*np.array([[1,1],[1,-1]])/np.sqrt(2)])
        amin,anon,_=sparse_bases(A)
        formula=p*np.abs(np.sin(2*theta))+w*w*np.abs(np.cos(2*theta))
        direct=[]
        for t in theta:
            R=np.array([[np.cos(t),-np.sin(t)],[np.sin(t),np.cos(t)]])
            C=A@R;direct.append(np.abs(C[:,0]*C[:,1]).sum())
        R=np.array([[1,-1],[1,1]])/np.sqrt(2);C=A@R
        rows.append(dict(pure_rows_per_axis=p,mixed_rows=2,diagonal_weight=w,
            support_overlap=2/(p+2),sparsity_min=amin,nonaligned_sparsity_min=anon,
            actual_wrong_sparsity=int(np.count_nonzero(np.abs(C)>1e-10)),
            true_contrast=float(direct[0]),wrong_contrast=float(direct[-1]),
            formula_error=float(np.abs(np.array(direct)-formula).max()),
            gram_error=float(np.abs(A.T@A-(p+w*w)*np.eye(2)).max())))
with (ROOT/'results/low_overlap_surrogate.csv').open('w',newline='') as f:
    wr=csv.DictWriter(f,fieldnames=list(rows[0]));wr.writeheader();wr.writerows(rows)
summary=dict(cases=len(rows),max_formula_error=max(r['formula_error'] for r in rows),
    decisive_case=[r for r in rows if r['pure_rows_per_axis']==3 and r['diagonal_weight']==2][0],
    source='Independent reviewer proposed this family before execution; owner implementation')
(ROOT/'results/low_overlap_summary.json').write_text(json.dumps(summary,indent=2)+'\n')
print(json.dumps(summary,indent=2))
