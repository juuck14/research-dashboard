from pathlib import Path
from itertools import product
import csv,json
import numpy as np

ROOT=Path(__file__).resolve().parent
EDGES=[(0,1),(0,2),(1,2)]
POINTS=[(.1,-.25,.35),(-.4,.2,.1),(.3,.4,-.2)]

def gram(x):
    S=np.eye(3)
    for v,(i,j) in zip(x,EDGES):S[i,j]=S[j,i]=v
    return S

def coefficients(x,t,eps,K):
    S=gram(x);z=np.exp(-t*S)
    q=eps/3+(1-eps)*z/z.sum(axis=1,keepdims=True)
    if K=='infinity':
        a=q*np.exp(S);a/=a.sum(axis=1,keepdims=True)
    else:
        ix=np.array(list(product(range(3),repeat=K)),int)
        counts=np.eye(3)[ix].sum(axis=1)
        a=np.zeros((3,3))
        for anchor in range(3):
            probability=np.prod(q[anchor,ix],axis=1)
            w=np.exp(S[anchor]-1)
            D=1+counts@w
            a[anchor]=np.sum(probability[:,None]*counts*w/D[:,None],axis=0)
    return np.array([(a[i,j]+a[j,i])/3 for i,j in EDGES])

def diagnostic(x,t,eps,K,h):
    x=np.array(x,float);J=np.zeros((3,3))
    for j in range(3):
        v=np.zeros(3);v[j]=h
        J[:,j]=(coefficients(x+v,t,eps,K)-coefficients(x-v,t,eps,K))/(2*h)
    curl=np.array([J[2,1]-J[1,2],J[0,2]-J[2,0],J[1,0]-J[0,1]])
    C=coefficients(x,t,eps,K)
    return float(C@curl),float(np.linalg.norm(curl)),C

rows=[]
for point,t,eps,K in product(range(3),[np.log(4.),3.],[0.,.3],[1,2,4,8,'infinity']):
    x=POINTS[point];eig=np.linalg.eigvalsh(gram(x))
    assert eig.min()>.1
    first,curl,_=diagnostic(x,t,eps,K,1e-4)
    second,curl2,C=diagnostic(x,t,eps,K,1e-5)
    rows.append({'point':point,'t':t,'epsilon':eps,'K':K,'min_gram_eigenvalue':float(eig.min()),
                 'frobenius_h1e4':first,'frobenius_h1e5':second,'curl_norm':curl2,
                 'step_discrepancy':abs(first-second),'stable_nonzero':abs(second)>1e-8 and abs(first-second)<1e-8+1e-3*abs(second)})
baseline=[r for r in rows if r['epsilon']==0 and r['K']=='infinity']
assert max(r['curl_norm'] for r in baseline)<1e-8
with (ROOT/'potential_checks.csv').open('w') as f:
    w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
summary={'settings':len(rows),'baseline_effective_energy_max_curl':max(r['curl_norm'] for r in baseline),
         'stable_nonzero_obstructions':sum(r['stable_nonzero'] for r in rows),
         'obstruction_cases':[r for r in rows if r['stable_nonzero']],
         'scope':'non-integrability on a realizable open Gram domain; not a limit cycle, harm theorem, or importance proof'}
(ROOT/'potential_summary.json').write_text(json.dumps(summary,indent=2)+'\n')
print(json.dumps({k:v for k,v in summary.items() if k!='obstruction_cases'},indent=2))
