"""Independent ordered-tuple check of the meaningful-target ETF repair."""
from pathlib import Path
from itertools import product
from math import comb
import json
import numpy as np

ROOT=Path(__file__).resolve().parent

def setup(C):
    G=(C*np.eye(C)-np.ones((C,C)))/(C-1)
    H=np.zeros((C,C))
    for i,j,v in [(0,1,1),(2,3,1),(0,2,-1),(1,3,-1)]:
        H[i,j]=H[j,i]=v
    assert np.max(abs(H.sum(axis=1)))==0
    assert np.min(np.linalg.eigvalsh(G+1e-4*H))>-1e-12
    return G,H

def policy(S,t,epsilon):
    z=np.exp(-t*S)
    return epsilon/S.shape[0]+(1-epsilon)*z/z.sum(axis=1,keepdims=True)

def scalar(delta,G,H,t,epsilon,K,frozen):
    C=len(G);S=G+delta*H
    q=policy(G if frozen else S,t,epsilon)
    tuples=np.array(list(product(range(C),repeat=K)),int)
    value=0.
    for i in range(C):
        w=np.exp(S[i,tuples]-1)
        probs=np.prod(q[i,tuples],axis=1)
        value+=float(probs@((w*H[i,tuples]).sum(axis=1)/(1+w.sum(axis=1))))/C
    return value

def tagged(G,H,t,epsilon,K):
    C=len(G);q=policy(G,t,epsilon);u=q[0,0];v=q[0,1]
    w=np.exp(-C/(C-1));rho=(v-epsilon/C)/v;eta=t*rho
    m1=m2=0.
    for nself in range(K):
        probability=comb(K-1,nself)*u**nself*(1-u)**(K-1-nself)
        D=1+w+nself+(K-1-nself)*w
        m1+=probability/D;m2+=probability/D**2
    pref=K*v*w*np.sum(H*H)/C
    return pref*(m1-w*m2),pref*((1-eta)*m1-w*m2),eta

rows=[]
for C,epsilon in [(4,.25),(6,.25),(12,.25),(4,.3)]:
    G,H=setup(C);t=np.log(4.)
    for K in [1,2,3]:
        exact_f,exact_a,eta=tagged(G,H,t,epsilon,K)
        for frozen,expected in [(True,exact_f),(False,exact_a)]:
            for step in [1e-5,3e-6]:
                fd=(scalar(step,G,H,t,epsilon,K,frozen)-scalar(-step,G,H,t,epsilon,K,frozen))/(2*step)
                row={'C':C,'epsilon':epsilon,'K':K,'policy':'frozen' if frozen else 'adaptive',
                     'eta':eta,'step':step,'tagged':expected,'direct_fd':fd,
                     'absolute_error':abs(expected-fd),'drift':scalar(0,G,H,t,epsilon,K,frozen)}
                rows.append(row)
assert max(r['absolute_error'] for r in rows)<1e-7
assert max(abs(r['drift']) for r in rows)<1e-12
assert all(r['tagged']>0 if r['policy']=='frozen' else r['tagged']<0 for r in rows)
summary={'checks':len(rows),'maximum_error':max(r['absolute_error'] for r in rows),
         'rows':rows,'scope':'independent tuple and feasible-Gram directional check; no all-mode or novelty conclusion'}
(ROOT/'etf_check.json').write_text(json.dumps(summary,indent=2)+'\n')
print(json.dumps({k:v for k,v in summary.items() if k!='rows'},indent=2))
