"""Exact arbitrary-K spectrum, independent full-field FD, and fixed-policy comparisons."""
from pathlib import Path
from functools import lru_cache
from itertools import product
import json,csv
import numpy as np
from scipy.linalg import null_space
from scipy.special import gammaln

ROOT=Path(__file__).resolve().parents[1];OUT=ROOT/'results';OUT.mkdir(exist_ok=True)
A=np.exp(-1.);B=np.exp(-2.)
BITS=np.array(list(product([-1.,1.],repeat=2)))
F0=np.pad(BITS/np.sqrt(2),((0,0),(0,2)))
def weight(s,alpha):return np.exp(-2*s+alpha*s*(s*s-1))
def policy(f,alpha,eps=.1):
    s=f@f.T;z=weight(s,alpha)
    return eps/4+(1-eps)*z/z.sum(axis=1,keepdims=True)

@lru_cache(None)
def counts3(K):
    c=np.array([(u,K-u-w,w) for u in range(K+1) for w in range(K-u+1)],float)
    coef=gammaln(K+1)-gammaln(c+1).sum(axis=1)
    return c,coef
@lru_cache(None)
def counts4(K):
    c=np.array([(u,v,w,K-u-v-w) for u in range(K+1) for v in range(K-u+1) for w in range(K-u-v+1)],float)
    coef=gammaln(K+1)-gammaln(c+1).sum(axis=1)
    return c,coef
def moments(K,eps=.1):
    c=1-eps;Z=np.exp(-2)+2+np.exp(2)
    soft=np.array([np.exp(-2),1,np.exp(2)])/Z
    q=np.array([eps/4+c*soft[0],2*(eps/4+c*soft[1]),eps/4+c*soft[2]])
    u,v,w=q[0],q[1]/2,q[2]
    ct,coef=counts3(K);prob=np.exp(coef+ct@np.log(q))
    n0,N,nopp=ct.T;D=1+n0+A*N+B*nopp
    E=lambda z:float(prob@z)
    mom={
      'A':E(N/D),'B':E(N/D**2),'C':E(nopp/D),
      'N2D2':E((N*N+N)/D**2),'N2D':E((N*N+N)/D),
      'NSD':E(N*(n0*soft[0]/u+N*soft[1]/v+nopp*soft[2]/w)/D),
      'prob_sum':float(prob.sum()),'u':u,'v':v,'w':w,'soft_adj':soft[1]
    }
    mom['R']=mom['B']/mom['A'];mom['threshold']=1-A*mom['R']
    return mom
def spectrum(mom,alpha,eps=.1):
    v=mom['v'];g=(1-eps)*mom['soft_adj']*(-2-alpha)
    hf=A*mom['A']-A*A*mom['B']
    ha=hf+A*g/v*mom['A']
    frozen_ab=A/2*mom['A']-A*A/4*mom['N2D2']+B*mom['C']
    adaptive_ab=frozen_ab+A*g*(mom['N2D']/(4*v)-mom['NSD']/2)
    normal_one=A/2*mom['A']+B*mom['C'];normal_ab=-A/2*mom['A']+B*mom['C']
    return {'eta':-g/v,'g':g,'frozen_balance':hf,'adaptive_balance':ha,
            'frozen_ab':frozen_ab,'adaptive_ab':adaptive_ab,
            'normal_one':normal_one,'normal_ab':normal_ab}
def fullfield(f,K,alpha,qfixed=None,eps=.1):
    f=f/np.linalg.norm(f,axis=1,keepdims=True)
    q=policy(f,alpha,eps) if qfixed is None else qfixed
    s=f@f.T;cts,coef=counts4(K);co=np.zeros((4,4))
    for i in range(4):
        prob=np.exp(coef+cts@np.log(q[i]))
        logits=np.exp(s[i]-1)
        denom=1+cts@logits
        co[i]=(prob[:,None]*cts*logits[None,:]/denom[:,None]).sum(axis=0)/4
    grad=(co+co.T)@f
    return grad-(grad*f).sum(axis=1,keepdims=True)*f
def fd_spectrum(K,alpha,h,rotate=False):
    f=F0.copy()
    if rotate:
        rng=np.random.default_rng(70313)
        f=f@np.linalg.qr(rng.normal(size=(4,4)))[0]
    basis=[null_space(z[None,:]) for z in f]
    q0=policy(f,alpha)
    result={};residual=0.
    for name in ['frozen','adaptive']:
        def func(y):return fullfield(y,K,alpha,q0 if name=='frozen' else None)
        J=np.zeros((12,12));residual=max(residual,float(np.abs(func(f)).max()))
        for col in range(12):
            i,j=divmod(col,3);v=np.zeros_like(f);v[i]=basis[i][:,j]
            diff=(func(f+h*v)-func(f-h*v))/(2*h)
            J[:,col]=np.concatenate([basis[i].T@diff[i] for i in range(4)])
        eig=np.linalg.eigvals(J)
        if np.abs(eig.imag).max()>1e-7:raise AssertionError('complex eigenvalues')
        result[name]=np.sort(eig.real)
    sp=spectrum(moments(K),alpha)
    predicted={}
    for name in ['frozen','adaptive']:
        predicted[name]=np.sort([sp[name+'_balance']]+[sp[name+'_ab']]*2+[sp['normal_one']]*2+[sp['normal_ab']]*2+[0]*5)
    return {'K':K,'alpha':alpha,'h':h,'rotate':rotate,'residual':residual,
      'frozen_max_error':float(np.abs(result['frozen']-predicted['frozen']).max()),
      'adaptive_max_error':float(np.abs(result['adaptive']-predicted['adaptive']).max()),
      'min_candidate_q':float(q0.min())}
def write_csv(name,rows):
    with (OUT/name).open('w') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
def main():
    rows=[];momentrows=[]
    for K in range(1,129):
        m=moments(K);momentrows.append({'K':K,**m})
        for alpha in [-1.5,-.9,0.,.5]:
            s=spectrum(m,alpha)
            rows.append({'K':K,'alpha':alpha,'threshold':m['threshold'],**s,
                         'full_frozen_stable':bool(min(s['frozen_balance'],s['frozen_ab'],s['normal_one'],s['normal_ab'])>1e-10),
                         'full_adaptive_stable':bool(min(s['adaptive_balance'],s['adaptive_ab'],s['normal_one'],s['normal_ab'])>1e-10)})
    checks=[]
    for K in [1,2,4,8,16]:
        for alpha in [-1.5,-.9,0.]:
            for h in [1e-5,3e-6]:checks.append(fd_spectrum(K,alpha,h))
    for K,alpha in [(1,-.9),(16,-.9)]:checks.append(fd_spectrum(K,alpha,1e-5,True))
    assert max(c['frozen_max_error'] for c in checks)<2e-7
    assert max(c['adaptive_max_error'] for c in checks)<2e-7
    # Independent four-category count moment check (not the fullfield FD itself).
    count_checks=[]
    q=policy(F0,0.)[0]
    for K in range(1,9):
        ct,coef=counts4(K);prob=np.exp(coef+ct@np.log(q))
        D=1+ct@np.exp((F0@F0.T)[0]-1)
        N=ct[:,1]+ct[:,2];d=ct[:,2]-ct[:,1]
        H=float(prob@(4*A*N/D-4*A*A*d*d/D**2))
        count_checks.append({'K':K,'full_count_H':H,'aggregated_H':4*spectrum(moments(K),0.)['frozen_balance'],'error':abs(H-4*spectrum(moments(K),0.)['frozen_balance'])})
    thresholds=np.array([r['threshold'] for r in momentrows])
    assert np.all(np.diff(thresholds)>0)
    assert max(abs(r['prob_sum']-1) for r in momentrows)<1e-11
    sameq=max(float(np.max(np.abs(policy(F0,alpha)-policy(F0,0.)))) for alpha in [-1.5,-.9,0.,.5])
    transition={}
    for alpha in [-1.5,-.9,0.,.5]:
        selected=[r for r in rows if r['alpha']==alpha]
        stable=[r['K'] for r in selected if r['full_adaptive_stable']]
        transition[str(alpha)]={'effective_eta':selected[0]['eta'],'first_full_stable_K':min(stable) if stable else None,
                               'K1':selected[0],'K128':selected[-1]}
    summary={'moment_settings':128,'policy_settings':len(rows),'full_tangent_checks':len(checks),
      'max_full_frozen_error':max(c['frozen_max_error'] for c in checks),
      'max_full_adaptive_error':max(c['adaptive_max_error'] for c in checks),
      'max_stationary_residual':max(c['residual'] for c in checks),
      'max_probability_sum_error':max(abs(r['prob_sum']-1) for r in momentrows),
      'same_q_error':sameq,'threshold_K1':thresholds[0],'threshold_K128':thresholds[-1],
      'threshold_strictly_increasing':bool(np.all(np.diff(thresholds)>0)),
      'four_category_check_error':max(r['error'] for r in count_checks),'policies':transition}
    write_csv('moments.csv',momentrows);write_csv('policy_spectrum.csv',rows);write_csv('fd_checks.csv',checks);write_csv('count_checks.csv',count_checks)
    (OUT/'summary.json').write_text(json.dumps(summary,indent=2)+'\n')
    print(json.dumps(summary,indent=2))
if __name__=='__main__':main()
