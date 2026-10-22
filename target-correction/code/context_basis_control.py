#!/usr/bin/env python3
"""Exact check of theory Proposition 5; plan added before this script ran."""
from pathlib import Path
import csv,json
import numpy as np

out=Path(__file__).resolve().parents[1]/'results'
states=np.array([[-1,-1],[-1,1],[1,-1],[1,1]],float)
rho=np.array([.9,.5]);K=np.ones((4,4))
for j in range(2): K*=(1+rho[j]*states[:,j,None]*states[None,:,j])/2
rows=[]
for seed in [20261025,20261026]:
 rng=np.random.default_rng(seed)
 for k in range(10):
  u=np.linalg.qr(rng.normal(size=(2,2)))[0]
  v=np.linalg.qr(rng.normal(size=(2,2)))[0]
  eps=float(np.geomspace(.001,.5,10)[k]); B=u@np.diag([1.,eps])@v.T
  target=states@B.T; pred=K@target
  recovered=np.linalg.solve(B,pred.T).T
  rows.append({'seed':seed,'small_target_singular_value':eps,
      'target_rank':int(np.linalg.matrix_rank(B)),
      'max_recovery_error':float(np.max(np.abs(recovered-K@states)))})
with (out/'context_basis_control.csv').open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=rows[0]);w.writeheader();w.writerows(rows)
s={'runs':len(rows),'max_error':max(r['max_recovery_error'] for r in rows)}
(out/'context_basis_summary.json').write_text(json.dumps(s,indent=2));print(json.dumps(s,indent=2))
