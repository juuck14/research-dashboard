"""Exact iid negative-count expectation and independent ordered-sequence check.
OPENBLAS_NUM_THREADS=1 python review/negative-feedback/code/multinegative_check.py
"""
from pathlib import Path
import itertools,json,csv,math
import numpy as np
from scipy.special import softmax
from scipy.linalg import null_space

OUT=Path(__file__).resolve().parents[1]/'results'
X=np.array(list(itertools.product([-1.,1.],repeat=2)))
F0=np.column_stack([X/np.sqrt(2),np.zeros((4,2))])
BASE=np.stack([null_space(f[None,:]) for f in F0])
EPS=.1;KAPPA=-2.

def counts(K):
    C=np.array([(a,b,c,K-a-b-c) for a in range(K+1) for b in range(K-a+1) for c in range(K-a-b+1)],dtype=float)
    coef=np.array([math.factorial(K)/math.prod(math.factorial(int(v)) for v in row) for row in C])
    return C,coef

def policy(F): return EPS/4+(1-EPS)*softmax(KAPPA*(F@F.T),axis=1)

def loss_and_coeff(F,q,C,m):
    S=F@F.T
    E=np.exp(S-1)
    denom=1+E@C.T
    probs=np.exp(np.log(q)@C.T)*m[None,:]
    assert np.max(abs(probs.sum(axis=1)-1))<1e-12
    coeff=np.einsum('ic,ic,cj,ij->ij',probs,1/denom,C,E)
    loss=float(np.sum(probs*np.log(denom))/4)
    return loss,coeff

def brute(F,q,K):
    S=F@F.T;E=np.exp(S-1)
    co=np.zeros((4,4));loss=0.
    for seq in itertools.product(range(4),repeat=K):
      C=np.bincount(seq,minlength=4)
      p=np.prod(q[:,seq],axis=1)
      d=1+E@C
      loss+=float(np.sum(p*np.log(d))/4)
      co+=p[:,None]*(C[None,:]*E)/d[:,None]
    return loss,co

def flow(F,q,C,m):
    _,co=loss_and_coeff(F,q,C,m)
    G=(co+co.T)@F/4
    return -(G-np.sum(G*F,axis=1)[:,None]*F)

def retract(y):
    F=F0+np.einsum('idk,ik->id',BASE,np.asarray(y).reshape(4,3))
    return F/np.linalg.norm(F,axis=1)[:,None]

rows=[];max_brute=0.;max_step=0.
for K in [1,2,4]:
    C,m=counts(K);q0=policy(F0)
    probe=retract(np.random.default_rng(991+K).normal(size=12)*.01)
    p=policy(probe)
    l,g=loss_and_coeff(probe,p,C,m);lb,gb=brute(probe,p,K)
    max_brute=max(max_brute,abs(l-lb),float(np.max(abs(g-gb))))
    for mode in ['frozen','adaptive']:
      def vec(y):
        F=retract(y);q=q0 if mode=='frozen' else policy(F)
        return np.einsum('idk,id->ik',BASE,flow(F,q,C,m)).ravel()
      def jac(h): return np.column_stack([(vec(h*np.eye(12)[j])-vec(-h*np.eye(12)[j]))/(2*h) for j in range(12)])
      J=jac(1e-5);JJ=jac(3e-6);max_step=max(max_step,float(np.max(abs(J-JJ))))
      eig=np.linalg.eigvalsh((J+J.T)/2)
      nz=eig[abs(eig)>1e-7]
      if mode=='frozen': assert nz.max()<0,(K,mode,eig)
      else: assert nz.max()>0,(K,mode,eig)
      rows.append(dict(K=K,dimension=4,policy=mode,n_compositions=len(C),min_q=float(q0.min()),
                       zero_modes=int(np.sum(abs(eig)<=1e-7)),positive_eigenvalues=int(np.sum(eig>1e-7)),
                       largest_eigenvalue=float(nz.max()),eigenvalues=json.dumps(eig.tolist())))

assert max_brute<1e-12,max_brute
assert max_step<1e-7,max_step
with (OUT/'multinegative_tangent.csv').open('w') as f:
    w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
summary={'ordered_vs_count_max_error':max_brute,'jacobian_stepsize_max_error':max_step,'checks':rows,
         'all_frozen_stable_adaptive_unstable':True}
(OUT/'multinegative_summary.json').write_text(json.dumps(summary,indent=2)+'\n')
print(json.dumps(summary,indent=2))
