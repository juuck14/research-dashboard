"""All-support minimax C audit for fixed B; protocol amendment 2."""
import csv,json
from pathlib import Path
import numpy as np
OUT=Path(__file__).parent/'results'

def global_C_error(A,B,budget=6):
    u=B/np.linalg.norm(B,axis=1,keepdims=True)
    norms=np.linalg.norm(A,axis=1)
    d=np.sqrt(np.maximum(0,norms[:,None]**2-(A@u.T)**2))
    single=d.min(axis=1)
    for eta in sorted(set([0.]+list(norms)+list(single))):
        cost=np.where(norms<=eta+1e-12,0,np.where(single<=eta+1e-12,1,2))
        if cost.sum()<=budget:return float(eta)
    raise AssertionError('no feasible support')

def rotation(t):return np.array([[np.cos(t),-np.sin(t)],[np.sin(t),np.cos(t)]])

rows=[]
for seed in (20261025,20261026):
    rng=np.random.default_rng(seed)
    for i in range(400):
        aa=rng.uniform(.9,1.4,4)
        mixed=rng.uniform(.9,1.4,2)*rng.choice([-1,1],2)
        A=np.vstack([np.diag(aa[:2])[0],np.array([aa[1],0]),np.array([0,aa[2]]),np.array([0,aa[3]]),mixed])
        # First row above equals [aa0,0]; all four true anchor rows fixed.
        if i<200:B=rng.normal(size=(2,2))
        else:
            t=rng.uniform(-.65,.65)
            B=rotation(t)
            if rng.integers(2):B=B[::-1]
        B=np.diag(10**rng.uniform(-3,1,2))@B
        B*=1.5/np.linalg.norm(B,2)
        if abs(np.linalg.det(B))<1e-14:continue
        eta=global_C_error(A,B)
        u=B/np.linalg.norm(B,axis=1,keepdims=True)
        normoffs=[max(abs(u[0,1]),abs(u[1,0])),max(abs(u[0,0]),abs(u[1,1]))]
        p=int(np.argmin(normoffs))
        off=max(abs(B[0,1]),abs(B[1,0])) if p==0 else max(abs(B[0,0]),abs(B[1,1]))
        admiss=eta<.9/np.sqrt(2)
        rows.append(dict(seed=seed,index=i,eta=eta,a=.9,L=1.5,condition=float(np.linalg.cond(B)),
                         sufficient_condition=bool(admiss),normalized_off=normoffs[p],normalized_bound=eta/.9,
                         off=off,absolute_bound=1.5*eta/.9,
                         normalized_fraction=normoffs[p]/(eta/.9) if eta else 0,
                         absolute_fraction=off/(1.5*eta/.9) if eta else 0))

with (OUT/'positive_all_support.csv').open('w') as f:
    w=csv.DictWriter(f,fieldnames=rows[0]);w.writeheader();w.writerows(rows)
valid=[r for r in rows if r['sufficient_condition']]
violations=[r for r in valid if r['normalized_fraction']>1+1e-8 or r['absolute_fraction']>1+1e-8]
outside=[]
for e in 10.**-np.arange(1,7):
    A=np.array([[1.,0],[1.2,0],[0,1],[0,1.1],[e,e]])
    B=np.array([[1.,e],[1.,-e]])
    C=np.array([[1.,0],[1.2,0],[1/(2*e),-1/(2*e)],[1.1/(2*e),-1.1/(2*e)],[0,0]])
    eta=float(np.max(np.linalg.norm(A-C@B,axis=1)))
    u=B/np.linalg.norm(B,axis=1,keepdims=True)
    best_norm=min(max(abs(u[0,1]),abs(u[1,0])),max(abs(u[0,0]),abs(u[1,1])))
    outside.append(dict(epsilon=float(e),residual=eta,C_nonzero=int(np.count_nonzero(C)),
                        op_B=float(np.linalg.norm(B,2)),smallest_A_row=float(np.min(np.linalg.norm(A,axis=1))),
                        best_normalized_off=best_norm,naive_bound=eta))
summary=dict(cases=len(rows),admissible_cases=len(valid),violations=len(violations),
             max_normalized_fraction=max(r['normalized_fraction'] for r in valid),
             max_absolute_fraction=max(r['absolute_fraction'] for r in valid),
             max_condition_among_admissible=max(r['condition'] for r in valid),
             necessity_without_mixed_row_lower=outside,
             evidence='Global C support minimization for sampled B, not global B search or proof')
(OUT/'positive_audit.json').write_text(json.dumps(summary,indent=2)+'\n')
print(json.dumps(summary,indent=2))
