"""Exact identity control. The correction changes the algorithm's estimand."""
import json,itertools
from pathlib import Path
import numpy as np
from scipy.special import gammaln
from multiple_negatives import compositions,q_at,calc
ROOT=Path(__file__).resolve().parents[1]
rows=[]
for K,k,e,t in itertools.product([1,2,4,8,16],[-4,-2,2],[.01,.1],[.3,.7854,1.1]):
 s,q=q_at(t,k,e);n=compositions(K);lc=gammaln(K+1)-gammaln(n+1).sum(axis=1)
 logp=lc+(n*np.log(q)).sum(axis=1);logimp=(n*np.log(.25/q)).sum(axis=1)
 weights=np.exp(logp+logimp);exp=np.exp(s-1);den=1+n@exp;ds=np.array([0,-2*np.sin(2*t),2*np.sin(2*t),0]);g=(n@(exp*ds))/den
 corrected=float(weights@g);uniform=calc(t,k,e,K,np.full(4,.25))[0]
 rows.append(dict(K=K,kappa=k,eps=e,theta=t,error=abs(corrected-uniform)))
summary=dict(settings=len(rows),max_abs_error=max(r['error'] for r in rows),identity='E_q^K [(product_j p/q) grad ell] = E_p^K grad ell; q/weights detached')
(ROOT/'results'/'importance_control.json').write_text(json.dumps(summary,indent=2));print(json.dumps(summary,indent=2))
