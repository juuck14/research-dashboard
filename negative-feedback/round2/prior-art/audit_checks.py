"""Independent exact checks of simple explanations; no training or imported project code."""
from pathlib import Path
import csv
import json
import math
import numpy as np
from scipy.special import gammaln

OUT=Path(__file__).resolve().parent/'results'
OUT.mkdir(exist_ok=True)

def tangent(field,f):
    return field-np.sum(field*f,axis=1,keepdims=True)*f

def softmax(s):
    s=s-s.max(axis=1,keepdims=True)
    z=np.exp(s)
    return z/z.sum(axis=1,keepdims=True)

def infinite_field(f,kappa,eps):
    n=len(f)
    s=f@f.T
    q=eps/n+(1-eps)*softmax(kappa*s)
    c=q*np.exp(s)
    c=c/c.sum(axis=1,keepdims=True)/n
    return tangent((c+c.T)@f,f)

def effective_temperature_gradient(f,kappa):
    # Gradient of sum_i log sum_j exp((1+kappa)*s_ij)/(n*(1+kappa)).
    # At kappa=-1, use sum_ij s_ij/n^2, the finite limiting gradient.
    n=len(f)
    s=f@f.T
    c=softmax((1+kappa)*s)/n
    return tangent((c+c.T)@f,f)

def exact_counts(K,q):
    counts=np.array([(i,j,K-i-j) for i in range(K+1) for j in range(K-i+1)],dtype=float)
    probs=np.exp(gammaln(K+1)-gammaln(counts+1).sum(axis=1)+counts@np.log(q))
    return counts,probs

def mode_moments(K,eps,kappa,alpha=None,positive=True):
    # alpha=None means natural exp(kappa*s); otherwise cubic policy with base -2.
    if alpha is None:
        ws=np.exp(kappa*np.array([1.,0.,-1.]))
        derivative=kappa
    else:
        ws=np.exp(-2*np.array([1.,0.,-1.]))
        derivative=-2-alpha
    Z=ws[0]+2*ws[1]+ws[2]
    u=eps/4+(1-eps)*ws[0]/Z
    v=eps/4+(1-eps)*ws[1]/Z
    w=eps/4+(1-eps)*ws[2]/Z
    g=(1-eps)*ws[1]/Z*derivative
    ct,pr=exact_counts(K,np.array([u,2*v,w]))
    n0,N,no=ct.T
    a=math.exp(-1)
    D=float(positive)+n0+a*N+a*a*no
    A=pr@(N/D)
    B=pr@(N/(D*D))
    C=pr@(no/D)
    threshold=1-a*B/A
    # Independent calculations, same sign convention as positive gradient Jacobian.
    return dict(K=K,positive_term=int(positive),threshold=float(threshold),eta=float(-g/v),
                balance=float(a*A-a*a*B+a*g/v*A),
                frozen_balance=float(a*A-a*a*B),
                normal_ab=float(-a*A/2+a*a*C),
                probability_sum=float(pr.sum()),u=u,v=v,w=w)

def save_csv(path,rows):
    with path.open('w') as f:
        writer=csv.DictWriter(f,fieldnames=list(rows[0]))
        writer.writeheader();writer.writerows(rows)

def main():
    checks=[]
    for seed in range(901,911):
        rng=np.random.default_rng(seed)
        f=rng.normal(size=(6,4));f/=np.linalg.norm(f,axis=1,keepdims=True)
        for kappa in [-2.,-1.,-.5,0.,1.,2.]:
            expected=effective_temperature_gradient(f,kappa)
            for eps in [0.,.1]:
                error=np.abs(infinite_field(f,kappa,eps)-expected).max()
                checks.append(dict(seed=seed,kappa=kappa,epsilon=eps,max_error=float(error)))
    pure_error=max(x['max_error'] for x in checks if x['epsilon']==0)
    assert pure_error<1e-12
    natural=[mode_moments(K,.1,-1.) for K in [1,2,4,8,9,16,32,64,128]]
    dcl=[mode_moments(K,.1,-2.,alpha=-.9,positive=False) for K in [1,2,4,8,9,16,32,64,128]]
    infonce=[mode_moments(K,.1,-2.,alpha=-.9,positive=True) for K in [1,2,4,8,9,16,32,64,128]]
    assert abs(dcl[0]['threshold'])<1e-12
    assert all(b['threshold']>a['threshold'] for a,b in zip(dcl[:-1],dcl[1:]))
    summary=dict(pure_temperature_identity_max_error=pure_error,
                 mixture_vs_pure_identity_max_error=max(x['max_error'] for x in checks if x['epsilon']==.1),
                 natural_exponential=natural,
                 shaped_infonce=infonce,shaped_dcl=dcl,
                 generic_performative_witness=[dict(m=m,frozen_curvature=1.,adaptive_curvature=1-m,
                                                    frozen_positive_probability=.5) for m in [.5,2.]])
    save_csv(OUT/'natural_exponential.csv',natural)
    save_csv(OUT/'dcl_scalar_control.csv',dcl)
    save_csv(OUT/'temperature_identity.csv',checks)
    (OUT/'audit_checks.json').write_text(json.dumps(summary,indent=2)+'\n')
    print(json.dumps(summary,indent=2))

if __name__=='__main__':main()
