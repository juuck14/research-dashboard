"""Independent exact-population full-tangent check for multiple binary factors."""
from pathlib import Path
from itertools import product
import json,csv
import numpy as np
from scipy.linalg import null_space
from scipy.special import expit,softmax

OUT=Path(__file__).resolve().parent/'results'
OUT.mkdir(exist_ok=True)

def sampler(z,eps,kappa):
    return (1-eps)*softmax(kappa*(z@z.T),axis=1)+eps/len(z)

def field(z,q):
    z=z/np.linalg.norm(z,axis=1,keepdims=True)
    c=q*expit(z@z.T-1)/len(z)
    g=(c+c.T)@z
    return -g+(g*z).sum(axis=1,keepdims=True)*z

def evaluate(m,d,eps,kappa,h=1e-5,rotate=False):
    bits=np.array(list(product([-1.,1.],repeat=m)))
    z=np.pad(bits/np.sqrt(m),((0,0),(0,d-m)))
    if rotate:
        rng=np.random.default_rng(20261022)
        u=np.linalg.qr(rng.normal(size=(d,d)))[0]
        z=z@u
    q0=sampler(z,eps,kappa)
    basis=[null_space(zi[None,:]) for zi in z]
    n=len(z); dim=n*(d-1)
    all_eigs={}; maxres=0
    for policy in ['frozen','adaptive']:
        def flow(y):
            y=y/np.linalg.norm(y,axis=1,keepdims=True)
            q=q0 if policy=='frozen' else sampler(y,eps,kappa)
            return field(y,q)
        maxres=max(maxres,float(np.max(np.abs(flow(z)))))
        jac=np.zeros((dim,dim))
        for col in range(dim):
            i,j=divmod(col,d-1)
            perturb=np.zeros_like(z);perturb[i]=basis[i][:,j]
            diff=(flow(z+h*perturb)-flow(z-h*perturb))/(2*h)
            jac[:,col]=np.concatenate([basis[k].T@diff[k] for k in range(n)])
        eig=np.linalg.eigvals(jac)
        all_eigs[policy]=eig.real
        if np.max(np.abs(eig.imag))>1e-6: raise AssertionError('unexpected complex spectrum')
    row={'m':m,'d':d,'epsilon':eps,'kappa':kappa,'h':h,'rotated':rotate,'residual':maxres,
         'minq':float(q0.min())}
    rank=m; expected_rot=rank*(2*d-rank-1)//2
    row['expected_rotation_zeros']=expected_rot
    for policy,eig in all_eigs.items():
        nz=eig[np.abs(eig)>1e-7]
        row[policy+'_zeros']=int(np.sum(np.abs(eig)<=1e-7))
        row[policy+'_positive']=int(np.sum(eig>1e-7))
        row[policy+'_max_nonzero']=float(nz.max()) if len(nz) else 0.
        row[policy+'_min_nonzero']=float(nz.min()) if len(nz) else 0.
    row['candidate']=row['frozen_positive']==0 and row['frozen_zeros']==expected_rot and row['adaptive_positive']>0
    return row

rows=[]
for m,d in [(2,4),(3,4),(3,8)]:
    for eps in [.01,.1,.5]:
        for kappa in [-10.,-6.,-4.,-2.,-1.,0.]:
            rows.append(evaluate(m,d,eps,kappa))
with (OUT/'grid.csv').open('w') as f:
    w=csv.DictWriter(f,fieldnames=rows[0].keys());w.writeheader();w.writerows(rows)
candidates=[r for r in rows if r['candidate'] and r['m']==3]
confirmation=[]
for r in candidates:
    for h,rotate in [(3e-6,False),(3e-5,False),(1e-5,True)]:
        confirmation.append(evaluate(r['m'],r['d'],r['epsilon'],r['kappa'],h,rotate))
if confirmation:
    with (OUT/'confirmation.csv').open('w') as f:
        w=csv.DictWriter(f,fieldnames=confirmation[0].keys());w.writeheader();w.writerows(confirmation)
summary={'grid_conditions':len(rows),'three_factor_candidates':len(candidates),'confirmations':len(confirmation),
         'confirmation_pass':all(r['candidate'] for r in confirmation),
         'max_equilibrium_residual':max(r['residual'] for r in rows+confirmation),
         'candidates':[{k:r[k] for k in ['m','d','epsilon','kappa','frozen_max_nonzero','adaptive_max_nonzero','adaptive_positive']} for r in candidates]}
(OUT/'summary.json').write_text(json.dumps(summary,indent=2)+'\n')
print(json.dumps(summary,indent=2))
