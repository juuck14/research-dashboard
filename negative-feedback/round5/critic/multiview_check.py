"""Independent full-tangent check: two positive-linked views per class.

No scientific imports from the author implementations. Enumerates ordered negative
tuples, includes gradients through both query and key embeddings, and differentiates
the complete sphere-projected population gradient. Positives always use the other
view of the same class. Every sampled negative belongs to another true class.
"""
from pathlib import Path
from itertools import product
from math import comb
import json
import numpy as np

ROOT = Path(__file__).resolve().parent

def policy(F, classes, t, eps):
    N = len(F)
    S = F @ F.T
    mask = classes[:, None] != classes[None, :]
    w = np.exp(-t*S)*mask
    return eps*mask/(N-2)+(1-eps)*w/w.sum(axis=1, keepdims=True)

def gradient(F, classes, positive, K, t, eps, frozen_q=None):
    N = len(F)
    S = F @ F.T
    Q = policy(F, classes, t, eps) if frozen_q is None else frozen_q
    A = np.zeros((N,N))
    for i in range(N):
        candidates = np.flatnonzero(classes != classes[i])
        tuples = np.asarray(list(product(candidates, repeat=K)), dtype=int)
        mass = np.prod(Q[i,tuples], axis=1)
        en = np.exp(S[i,tuples])
        ep = np.exp(S[i,positive[i]])
        D = ep + en.sum(axis=1)
        A[i,positive[i]] -= np.dot(mass, en.sum(axis=1)/D)/N
        terms = mass[:,None]*en/D[:,None]/N
        np.add.at(A[i], tuples.ravel(), terms.ravel())
    euclidean = (A+A.T) @ F
    return euclidean - (euclidean*F).sum(axis=1, keepdims=True)*F

def expected(C, r, K, t, eps):
    m=C//2
    R=np.exp(2*t)
    p=eps*m/(2*m-1)+(1-eps)*m*R/((m-1)+m*R)
    B=np.exp(-2.)
    As=Ao=0.
    for O in range(K+1):
        S=K-O
        prob=comb(K,O)*p**O*(1-p)**S
        D=1+S+B*O
        As+=prob*S/D
        Ao+=prob*B*O/D
    # One spatial tangent coordinate: C*r dimensions in total.
    # r=2: positive transition has the unique within-class eigenvalue mu=-1.
    eigenvalues=[0., 2*Ao/(m*r)]
    eigenvalues += [(Ao-m/(m-1)*As)/(m*r)]*(C-2)
    eigenvalues += [2*(As+3*Ao)/(C*r)]*C
    return np.sort(eigenvalues), {'p':p, 'As':As, 'Ao':Ao,
                                  'class_margin':Ao-m/(m-1)*As}

rows=[]
C=4;r=2;N=C*r;d=3
classes=np.repeat(np.arange(C),r)
positive=np.arange(N)^1
F=np.zeros((N,d));F[:,0]=np.repeat([1,1,-1,-1],r)
t=np.log(4.);eps=.05
for K in [1,2,3]:
    expected_one, info=expected(C,r,K,t,eps)
    predicted=np.sort(np.repeat(expected_one,d-1))
    for mode in ['frozen','adaptive']:
        frozen=policy(F,classes,t,eps) if mode=='frozen' else None
        for step in [1e-5,3e-6]:
            jac=np.empty((N*(d-1),N*(d-1)))
            for col in range(N*(d-1)):
                i,k=divmod(col,d-1)
                tangent=np.zeros_like(F);tangent[i,k+1]=1.
                plus=F+step*tangent;plus/=np.linalg.norm(plus,axis=1,keepdims=True)
                minus=F-step*tangent;minus/=np.linalg.norm(minus,axis=1,keepdims=True)
                gp=gradient(plus,classes,positive,K,t,eps,frozen)
                gm=gradient(minus,classes,positive,K,t,eps,frozen)
                jac[:,col]=((gp-gm)/(2*step))[:,1:].ravel()
            actual=np.linalg.eigvalsh((jac+jac.T)/2)
            rows.append({'K':K,'policy':mode,'step':step,**info,
                         'maximum_spectrum_error':float(np.max(abs(actual-predicted))),
                         'jacobian_asymmetry':float(np.max(abs(jac-jac.T))),
                         'drift':float(np.max(abs(gradient(F,classes,positive,K,t,eps,frozen)))),
                         'predicted_spectrum':predicted.tolist(),'fd_spectrum':actual.tolist()})
assert max(x['maximum_spectrum_error'] for x in rows)<1e-7
assert max(x['drift'] for x in rows)<1e-12
assert min(x['class_margin'] for x in rows)>0
summary={'checks':len(rows),'maximum_error':max(x['maximum_spectrum_error'] for x in rows),
         'scope':'C=4, two swap-linked views per class; full sphere tangent; no same-class negatives; local calculation only',
         'rows':rows}
(ROOT/'multiview_check.json').write_text(json.dumps(summary,indent=2)+'\n')
print(json.dumps({k:v for k,v in summary.items() if k!='rows'},indent=2))
