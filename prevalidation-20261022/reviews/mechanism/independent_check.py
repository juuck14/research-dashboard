"""Independent row-direction audit; see protocol.md written before execution."""
import csv, itertools, json, platform
from pathlib import Path
import numpy as np

OUT=Path(__file__).parent/'results'
OUT.mkdir(exist_ok=True)
c=2**-.5
R=np.array([[c,-c],[c,c]])
A0=np.array([[1.,0],[0,1],[c,c],[c,-c]])

def count(mat, tol=1e-11):
    # Per-row relative tolerance avoids silently deleting weak anchors.
    norms=np.linalg.norm(mat,axis=1)
    return int(np.sum(np.abs(mat)>tol*norms[:,None]))

def audit_basis(mat):
    dirs=[np.array([-row[1],row[0]])/np.linalg.norm(row) for row in mat]
    dirs += [np.array([np.cos(t),np.sin(t)]) for t in np.linspace(.021,3.12,137)]
    minimum=100; best=[]; nonaligned=100
    for u,v in itertools.combinations(dirs,2):
        U=np.column_stack([u,v])
        if abs(np.linalg.det(U))<1e-8: continue
        score=count(mat@U)
        aligned=all(min(abs(x[0]),abs(x[1]))<1e-9 for x in (u,v))
        minimum=min(minimum,score)
        if not aligned: nonaligned=min(nonaligned,score)
        if score<=8: best.append(bool(aligned))
    return minimum,nonaligned,all(best)

def one(kappa,weights,beta,rng,phase,seed):
    a=np.vstack([weights[:,None]*A0,kappa*np.eye(2)])
    C=a@R
    B=np.vstack([weights[:,None]*A0@R,kappa*np.eye(2)])
    am,an,aa=audit_basis(a); bm,bn,ba=audit_basis(B)
    u=rng.normal(size=(1000,2)); u/=np.linalg.norm(u,axis=1,keepdims=True)
    s=u*np.sqrt(rng.uniform(size=(1000,1)))
    z=s@R
    x=s@a.T; xc=z@C.T; xb=z@B.T
    phi=lambda t:t+beta*np.tanh(t)
    der=lambda t:1+beta/np.cosh(t)**2
    jacC=der(xc)[:,:,None]*C
    jacB=der(xb)[:,:,None]*B
    return dict(phase=phase,seed=seed,kappa=kappa,min_l0_A=am,next_l0_A=an,
                minimizers_aligned_A=aa,min_l0_B=bm,next_l0_B=bn,minimizers_aligned_B=ba,
                sigma_min=float(np.linalg.svd(a,compute_uv=False)[-1]),
                sigma_max=float(np.linalg.svd(a,compute_uv=False)[0]),
                op_distance=float(np.linalg.norm(C-B,2)),
                op_distance_ratio=float(np.linalg.norm(C-B,2)/kappa),
                exact_identity_error=float(np.max(np.abs(x-xc))),
                nonlinear_identity_error=float(np.max(np.abs(phi(x)-phi(xc)))),
                nonlinear_C0_over_kappa=float(np.max(np.linalg.norm(phi(xc)-phi(xb),axis=1))/kappa),
                nonlinear_C1_over_kappa=float(np.max(np.linalg.norm(jacC-jacB,ord=2,axis=(1,2)))/kappa),
                quotient_rotation_degrees=45.)

rows=[]
for i,k in enumerate(10.**-np.arange(1,9)):
    rows.append(one(float(k),np.ones(4),np.full(6,.2),np.random.default_rng(100+i),'grid',100+i))
for seed in (813,997):
    rng=np.random.default_rng(seed)
    for j in range(20):
        k=10**rng.uniform(-8,-1)
        rows.append(one(float(k),rng.uniform(.7,1.4,4),rng.uniform(.1,.4,6),rng,'confirmation',seed))

with (OUT/'checks.csv').open('w') as f:
    w=csv.DictWriter(f,fieldnames=rows[0].keys()); w.writeheader(); w.writerows(rows)
summary=dict(n=len(rows),all_l0_exact=all(r['min_l0_A']==r['min_l0_B']==8 and r['next_l0_A']==r['next_l0_B']==9 and r['minimizers_aligned_A'] and r['minimizers_aligned_B'] for r in rows),
             max_identity_error=max(r['exact_identity_error'] for r in rows),
             max_nonlinear_identity_error=max(r['nonlinear_identity_error'] for r in rows),
             max_ratio_formula_error=max(abs(r['op_distance_ratio']-np.sqrt(2-np.sqrt(2))) for r in rows),
             min_sigma_min=min(r['sigma_min'] for r in rows),
             max_condition=max(r['sigma_max']/r['sigma_min'] for r in rows),
             max_nonlinear_C0_over_kappa=max(r['nonlinear_C0_over_kappa'] for r in rows),
             max_nonlinear_C1_over_kappa=max(r['nonlinear_C1_over_kappa'] for r in rows),
             python=platform.python_version(),numpy=np.__version__)
(OUT/'summary.json').write_text(json.dumps(summary,indent=2)+'\n')
print(json.dumps(summary,indent=2))
