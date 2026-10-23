"""Independent check distinguishing detached feedback from composed-risk curvature."""
from pathlib import Path
from itertools import product
import json
import numpy as np

ROOT=Path(__file__).resolve().parent
C=4;eps=.05;t=.7
G=(C*np.eye(C)-np.ones((C,C)))/(C-1)
H=np.zeros((C,C))
for i,j,v in [(0,1,1),(2,3,1),(0,2,-1),(1,3,-1)]:
    H[i,j]=H[j,i]=v
assert np.max(abs(H.sum(axis=1)))==0

def policy(S):
    mask=1-np.eye(C)
    w=np.exp(-t*S)*mask
    return eps*mask/(C-1)+(1-eps)*w/w.sum(axis=1,keepdims=True)

def direct(delta,K,mode):
    S=G+delta*H
    q=policy(G if mode=='frozen' else S)
    value=0.
    for i in range(C):
        tuples=np.array(list(product([j for j in range(C) if j!=i],repeat=K)),int)
        mass=np.prod(q[i,tuples],axis=1)
        w=np.exp(S[i,tuples]-1)
        D=1+w.sum(axis=1)
        if mode=='detached':
            value+=mass@((w*H[i,tuples]).sum(axis=1)/D)/C
        else:
            value+=mass@np.log(D)/C
    return float(value)

rows=[]
for K in [1,2,3]:
    a=np.exp(-C/(C-1));D=1+K*a;B=K*a/D;T=1-a/D;eta=t*(1-eps)
    pref=B*np.sum(H*H)/(C*(C-1))
    theory={'frozen':pref*T,'detached':pref*(T-eta),'composed':pref*(T-2*eta)}
    for h in [1e-4,3e-5]:
        for mode in ['frozen','detached','composed']:
            if mode=='detached':
                fd=(direct(h,K,mode)-direct(-h,K,mode))/(2*h)
            else:
                fd=(direct(h,K,mode)-2*direct(0,K,mode)+direct(-h,K,mode))/h**2
            rows.append({'K':K,'step':h,'mode':mode,'eta':eta,'T':T,
                         'expected':theory[mode],'direct_fd':fd,'absolute_error':abs(fd-theory[mode])})
assert max(r['absolute_error'] for r in rows)<1e-6
assert all(r['expected']>0 for r in rows if r['mode']!='composed')
assert all(r['expected']<0 for r in rows if r['mode']=='composed')
summary={'C':C,'epsilon':eps,'t':t,'eta':t*(1-eps),'checks':len(rows),
         'maximum_error':max(r['absolute_error'] for r in rows),
         'scope':'ETF feasible Gram shape; composed risk versus detached field, not a practical optimizer comparison',
         'rows':rows}
(ROOT/'composed_risk_check.json').write_text(json.dumps(summary,indent=2)+'\n')
print(json.dumps({k:v for k,v in summary.items() if k!='rows'},indent=2))
