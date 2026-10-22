#!/usr/bin/env python3
"""Population same-law counterexample; no trained model or sample estimator."""
import csv, json, platform
from pathlib import Path
import numpy as np
import scipy
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
ROOT=Path(__file__).resolve().parents[1]
R=np.array([[1,-1],[1,1]],float)/np.sqrt(2)
A0=np.array([[1,0],[0,1],[1,1],[1,-1]],float)
A0[2:]/=np.sqrt(2)

def matrices(k,scales=None):
    if scales is None: scales=np.ones(4)
    top=scales[:,None]*A0
    return np.vstack([top,k*np.eye(2)]),np.vstack([top@R,k*np.eye(2)])

def sparse_bases(A,tol=1e-10):
    # Any nonzero column has zeros only in one row-direction class in R^2.
    # An optimum may therefore be chosen using two row-annihilators.
    normals=[]
    for row in A:
        if np.linalg.norm(row)<tol: continue
        n=np.array([-row[1],row[0]])/np.linalg.norm(row)
        if not any(abs(np.dot(n,m))>1-tol for m in normals): normals.append(n)
    out=[]
    for i,u in enumerate(normals):
        for v in normals[i+1:]:
            B=np.column_stack([u,v])
            if abs(np.linalg.det(B))<tol: continue
            count=int(np.count_nonzero(np.abs(A@B)>tol))
            aligned=int(np.count_nonzero(np.abs(B)>tol))==2
            out.append((count,aligned))
    return min(x[0] for x in out),min(x[0] for x in out if not x[1]),len(out)

def make_points(seed,n=4096):
    q=np.random.default_rng(seed).normal(size=(n,2))
    return np.column_stack([np.tanh(q[:,0]),np.tanh(.6*q[:,0]+.8*q[:,1])])/np.sqrt(2)

def case(k,seed,scales=None):
    A,B=matrices(k,scales)
    C=A@R
    E=C-B
    d=np.linalg.norm(E,2)
    S=make_points(seed)
    Z=S@R
    same_error=float(np.max(np.abs(S@A.T-Z@C.T)))
    svals=np.linalg.svd(A,compute_uv=False)
    bvals=np.linalg.svd(B,compute_uv=False)
    amin,anon,nb=sparse_bases(A)
    bmin,bnon,nb2=sparse_bases(B)
    X=Z@C.T;Y=Z@B.T
    Fn=lambda x:x+.1*x**3
    nonlinear_c0=float(np.max(np.linalg.norm(Fn(X)-Fn(Y),axis=1)))
    dc=(1+.3*X**2)[:,:,None]*C[None,:,:]
    db=(1+.3*Y**2)[:,:,None]*B[None,:,:]
    nonlinear_c1=float(max(np.linalg.norm(a-b,2) for a,b in zip(dc,db)))
    bound=float(k*(1+.9*k*k)*np.linalg.norm(R-np.eye(2),2))
    return dict(kappa=k,theta_degrees=45.,linear_C1_distance=d,
                predicted_linear_distance=float(k*np.sqrt(2-np.sqrt(2))),
                minimum_singular=float(min(svals.min(),bvals.min())),
                maximum_singular=float(max(svals.max(),bvals.max())),
                condition_A=float(svals.max()/svals.min()),
                sparsity_min_A=amin,sparsity_nonaligned_A=anon,
                sparsity_min_B=bmin,sparsity_nonaligned_B=bnon,
                examined_projective_pairs=nb+nb2,
                same_law_reconstruction_error=same_error,
                nonlinear_sample_C0=nonlinear_c0,nonlinear_sample_C1=nonlinear_c1,
                nonlinear_C1_upper_bound=bound)

def write_csv(path,rows):
    with path.open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)

def main():
    primary=[case(k,20261022) for k in [1.,.3,.1,.03,.01,.003,.001]]
    rng=np.random.default_rng(20261023)
    confirm=[case(float(10**rng.uniform(-5,-.05)),20261023,
                  rng.uniform(.6,1.4,4)) for _ in range(40)]
    write_csv(ROOT/'results/primary.csv',primary)
    write_csv(ROOT/'results/confirmation.csv',confirm)
    t=np.linspace(-1,1,10001)
    highfreq=[]
    for w in [10,30,100,300,1000]:
        highfreq.append(dict(omega=w,C0=float(np.max(np.abs(np.sin(w*t)/w))),
                             derivative_C0=float(np.max(np.abs(np.cos(w*t))))))
    write_csv(ROOT/'results/measurement_control.csv',highfreq)
    summary=dict(primary_cases=len(primary),confirmation_cases=len(confirm),
        max_same_law_error=max(x['same_law_reconstruction_error'] for x in primary+confirm),
        max_distance_formula_error=max(abs(x['linear_C1_distance']-x['predicted_linear_distance']) for x in primary+confirm),
        min_sparsity_gap=min(min(x['sparsity_nonaligned_A']-x['sparsity_min_A'],x['sparsity_nonaligned_B']-x['sparsity_min_B']) for x in primary+confirm),
        max_nonlinear_bound_ratio=max(x['nonlinear_sample_C1']/x['nonlinear_C1_upper_bound'] for x in primary+confirm),
        seeds=[20261022,20261023],
        evidence='Exact population algebra plus numerical audits; no empirical identifiability estimator')
    (ROOT/'results/summary.json').write_text(json.dumps(summary,indent=2)+'\n')
    env=dict(python=platform.python_version(),numpy=np.__version__,scipy=scipy.__version__,matplotlib=matplotlib.__version__)
    (ROOT/'results/environment.json').write_text(json.dumps(env,indent=2)+'\n')
    fig,ax=plt.subplots(1,2,figsize=(9,3.3),constrained_layout=True)
    k=np.array([x['kappa'] for x in primary])
    ax[0].loglog(k,[x['linear_C1_distance'] for x in primary],'o-',label='C1 leakage budget')
    ax[0].loglog(k,k*np.sqrt(2-np.sqrt(2)),'--',label='exact formula')
    ax[0].set(xlabel='weak anchor amplitude kappa',ylabel='generator distance')
    ax[0].legend(fontsize=8)
    ax[1].semilogx(k,[45]*len(k),'o-',label='axis ambiguity')
    ax[1].set(xlabel='weak anchor amplitude kappa',ylabel='quotient angle (degrees)',ylim=(0,50))
    ax[1].legend(fontsize=8)
    fig.savefig(ROOT/'figures/counterexample.png',dpi=180)
    print(json.dumps(summary,indent=2))
if __name__=='__main__':main()
