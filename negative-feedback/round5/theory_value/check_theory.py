"""Exact small-population checks, not a claim of new linear-estimation theory."""
from pathlib import Path
from itertools import product, combinations
import csv,json
import numpy as np
from scipy.special import gammaln
from scipy.linalg import null_space

ROOT=Path(__file__).resolve().parent;OUT=ROOT/'results';OUT.mkdir(exist_ok=True)

def simplex(C):
    return np.sqrt(C/(C-1))*(np.eye(C)-np.ones((C,C))/C)

def tasks(C):
    rows=[]
    for ix in combinations(range(C),C//2):
        y=-np.ones(C);y[list(ix)]=1;rows.append(y)
    return np.array(rows)

def population_risk(F,sigma):
    C,d=F.shape;X=F-F.mean(axis=0,keepdims=True)
    cov=X.T@X/C+sigma*sigma*np.eye(d)
    labels=tasks(C);cross=X.T@labels.T/C
    weights=np.linalg.pinv(cov,rcond=1e-12)@cross
    actual=1-2*np.sum(weights*cross,axis=0)+np.einsum('it,ij,jt->t',weights,cov,weights)
    vals=np.linalg.eigvalsh(X@X.T);vals=vals[vals>1e-10]
    predicted=1-np.sum(vals/(vals+C*sigma*sigma))/(C-1)
    optimum=(C-1)*sigma*sigma/(1+(C-1)*sigma*sigma)
    return float(np.mean(actual)),float(predicted),float(optimum),len(vals)

def coefficients(C,K,t,eps):
    soft=1/(C-1+np.exp(-t*C/(C-1)))
    v=eps/C+(1-eps)*soft;p=(C-1)*v
    ell=np.arange(K+1)
    logprob=gammaln(K+1)-gammaln(ell+1)-gammaln(K-ell+1)+ell*np.log(p)+(K-ell)*np.log1p(-p)
    prob=np.exp(logprob);a=np.exp(-C/(C-1));D=1+K-ell+a*ell
    M=float(prob@(ell/D));R=float(prob@(ell/D**2))/M
    threshold=1-a*R;eta=t*(1-eps)*soft/v
    eigen=4*a*M/(C-1)**2*(threshold-eta)
    floor=C*(t-1)/(C-1+np.exp(-t*C/(C-1))+C*(t-1))
    return eigen,threshold,eta,floor

def policy(F,t,eps,exclude_self=False,kind='linear'):
    score=F@F.T
    if kind=='linear':logw=-t*score
    elif kind=='quadratic':logw=.7*score**2+.2*score
    elif kind=='cubic':logw=-t*score+.4*score**3
    elif kind=='hard':logw=t*score
    else:raise ValueError(kind)
    raw=np.exp(logw)
    if exclude_self:
        np.fill_diagonal(raw,0)
        return eps*(1-np.eye(len(F)))/(len(F)-1)+(1-eps)*raw/raw.sum(axis=1,keepdims=True)
    return eps/len(F)+(1-eps)*raw/raw.sum(axis=1,keepdims=True)

def field(F,K,t,eps,q=None,exclude_self=False,tau=1.,kind='linear'):
    F=F/np.linalg.norm(F,axis=1,keepdims=True);C=len(F)
    if q is None:q=policy(F,t,eps,exclude_self,kind)
    ix=np.array(list(product(range(C),repeat=K)),int)
    counts=np.eye(C)[ix].sum(axis=1);score=F@F.T;b=np.zeros((C,C))
    for i in range(C):
        prob=np.prod(q[i,ix],axis=1);a=np.exp((score[i]-1)/tau)
        b[i]=(prob[:,None]*counts*a[None,:]/(1+counts@a)[:,None]).sum(axis=0)
    G=(b+b.T)@F/(C*tau)
    return G-(G*F).sum(axis=1,keepdims=True)*F

def shape(C):
    V=simplex(C);H=np.zeros((C,C))
    for i,j,s in [(0,1,1),(0,2,-1),(1,3,-1),(2,3,1)]:H[i,j]=H[j,i]=s
    Z=(C-1)/(2*C)*H@V
    assert np.max(np.abs((V*Z).sum(axis=1)))<1e-12
    assert np.max(np.abs(Z.sum(axis=0)))<1e-12
    assert np.max(np.abs(V@Z.T+Z@V.T-H))<1e-12
    return V,Z

def full_filtered_spectrum(C,K,t,eps,frozen,tau=1.,kind='linear'):
    V=simplex(C);d=V.shape[1]
    basis=[null_space(row[None]) for row in V]
    J=np.zeros((C*(d-1),C*(d-1)));step=3e-6
    q=(1-np.eye(C))/(C-1) if frozen else None
    for col in range(len(J)):
        i,j=divmod(col,d-1);Z=np.zeros_like(V);Z[i]=basis[i][:,j]
        diff=(field(V+step*Z,K,t,eps,q=q,exclude_self=True,tau=tau,kind=kind)-field(V-step*Z,K,t,eps,q=q,exclude_self=True,tau=tau,kind=kind))/(2*step)
        J[:,col]=np.concatenate([basis[k].T@diff[k] for k in range(C)])
    r=-1/(C-1)
    gp={'linear':-t,'quadratic':1.4*r+.2,'cubic':-t+1.2*r*r,'hard':t}[kind]
    a=np.exp(-C/((C-1)*tau));D=1+K*a;T=1-a/D;eta=0 if frozen else -tau*gp*(1-eps)
    scale=K*a/D
    shapeval=4*scale/((C-1)**2*tau*tau)*(T-eta)
    bary=scale*(2*(C-2)/((C-1)**2*tau)+C*C/((C-1)**4*tau*tau)*(T-eta)+C*(C-2)/((C-1)**4*tau*tau*D))
    normal=2*scale/((C-1)*tau)
    rotations=(C-1)*d-C*(C-1)//2
    predicted=np.array([0.]*rotations+[shapeval]*(C*(C-3)//2)+[bary]*(C-1)+[normal]*(d-C+1))
    eig=np.linalg.eigvals(J)
    return {'C':C,'d':d,'K':K,'t':t,'eps':eps,'frozen':frozen,'tau':tau,'logweight_kind':kind,'eta':eta,'dimension':len(J),
            'shape_value':shapeval,'shape_multiplicity':C*(C-3)//2,'bary_value':bary,
            'bary_multiplicity':C-1,'normal_value':normal,'normal_multiplicity':d-C+1,
            'rotation_multiplicity':rotations,'maximum_spectrum_error':float(np.max(np.abs(np.sort(eig.real)-np.sort(predicted)))),
            'maximum_imaginary':float(np.max(np.abs(eig.imag))),
            'numeric_symmetry_error':float(np.max(np.abs(J-J.T)))}

def main():
    riskrows=[];maxriskerr=0
    for C in [4,6,8]:
        geom={'simplex':simplex(C),'collapsed':np.tile(np.eye(C)[0],(C,1))}
        if C==4:
            bits=np.array(list(product([-1.,1.],repeat=2)))
            geom['square']=bits/np.sqrt(2)
            theta=.7545192717973
            geom['rectangle']=bits*np.array([np.cos(theta),np.sin(theta)])
        for seed in [7121,7133]:
            rng=np.random.default_rng(seed);F=rng.normal(size=(C,C+2));F/=np.linalg.norm(F,axis=1,keepdims=True)
            geom[f'random{seed}']=F
        for name,F in geom.items():
            for sigma in [0.,.05,.2,.5,1.]:
                actual,pred,opt,rank=population_risk(F,sigma)
                maxriskerr=max(maxriskerr,abs(actual-pred))
                riskrows.append({'C':C,'geometry':name,'sigma':sigma,'mean_optimal_affine_mse':actual,
                                 'spectral_formula':pred,'simplex_optimum':opt,'rank':rank,
                                 'excess_above_simplex':actual-opt,'absolute_error':abs(actual-pred)})
    countrows=[];fdrows=[];maxfd=0
    for C,t,eps in product([4,5,6,8,9,16],[np.log(4),2.],[.25,.3,.5]):
        for K in [1,2,3,4,8,16,32,64,128,256]:
            eigen,T,eta,floor=coefficients(C,K,t,eps)
            countrows.append({'C':C,'K':K,'t':t,'eps':eps,'shape_eigenvalue':eigen,'threshold':T,
                              'eta':eta,'critical_floor':floor,'all_finite_count_repelling':bool(eps<=floor),
                              'shape_multiplicity':C*(C-3)//2})
        if C in [4,5,6,8]:
            V,Z=shape(C);norm=float(np.sum(Z*Z));q=policy(V,t,eps)
            for K in [1,2,3]:
                expected=coefficients(C,K,t,eps)[0]
                for step in [1e-5,3e-6]:
                    diff=(field(V+step*Z,K,t,eps)-field(V-step*Z,K,t,eps))/(2*step)
                    observed=float(np.sum(diff*Z)/norm)
                    residual=float(np.linalg.norm(diff-expected*Z))
                    maxfd=max(maxfd,residual)
                    fdrows.append({'C':C,'K':K,'t':t,'eps':eps,'step':step,'predicted':expected,
                                   'observed_rayleigh':observed,'vector_residual':residual})
    filtered=[]
    for C,eps,K in product([4,6,8],[.05,.25,.5],[1,2,3]):
        t=np.log(4);V,Z=shape(C);norm=float(np.sum(Z*Z));a=np.exp(-C/(C-1))
        expected=4*a*K/((C-1)**2*(1+K*a))*(1-a/(1+K*a)-t*(1-eps))
        for step in [1e-5,3e-6]:
            diff=(field(V+step*Z,K,t,eps,exclude_self=True)-field(V-step*Z,K,t,eps,exclude_self=True))/(2*step)
            residual=float(np.linalg.norm(diff-expected*Z))
            filtered.append({'C':C,'eps':eps,'K':K,'step':step,'expected':expected,
                             'observed':float(np.sum(diff*Z)/norm),'vector_residual':residual})
    coarse=[]
    for C in [4,6,8]:
        labels=tasks(C);m=C//2
        conditional=np.column_stack([labels[:,:m].mean(axis=1),labels[:,m:].mean(axis=1)])
        bayes_mse=float(np.mean(1-np.mean(conditional**2,axis=1)))
        bayes_error=float(np.mean((1-np.abs(conditional))/2))
        expected=(C-2)/(C-1)
        coarse.append({'C':C,'tasks':len(labels),'bayes_mse':bayes_mse,'predicted_mse':expected,
                       'bayes_zero_one_error':bayes_error,'simplex_noiseless_bayes_mse':0.,
                       'absolute_error':abs(bayes_mse-expected)})
    spectra=[full_filtered_spectrum(C,K,np.log(4),eps,frozen) for C,K,eps,frozen in product([4,6,8],[1,3],[.05,.3,.5],[False,True])]
    nonlinear=[full_filtered_spectrum(C,K,np.log(4),.2,False,tau=tau,kind=kind) for C,K,tau,kind in product([4,6],[1,3],[.5,2.],['quadratic','cubic','hard'])]
    summary={'population_risk_rows':len(riskrows),'max_risk_formula_error':maxriskerr,
             'count_rows':len(countrows),'independent_ordered_tuple_shape_fd_rows':len(fdrows),
             'max_shape_fd_vector_residual':maxfd,
             'filtered_shape_fd_rows':len(filtered),'filtered_max_vector_residual':max(r['vector_residual'] for r in filtered),
             'coarse_bayes_formula_error':max(r['absolute_error'] for r in coarse),
             'filtered_full_spectrum_cases':len(spectra),
             'filtered_full_spectrum_error':max(r['maximum_spectrum_error'] for r in spectra),
             'filtered_full_spectrum_max_imaginary':max(r['maximum_imaginary'] for r in spectra),
             'general_omega_tau_spectrum_cases':len(nonlinear),
             'general_omega_tau_spectrum_error':max(r['maximum_spectrum_error'] for r in nonlinear),
             'natural_floor_by_C':{str(C):coefficients(C,1,np.log(4),.3)[3] for C in [4,5,6,7,8,9,16,64]},
             'scope':'direct linear-estimation/ETF application plus analytic simplex response; publication novelty is assessed separately'}
    assert maxriskerr<1e-10
    assert min(r['excess_above_simplex'] for r in riskrows)>-1e-10
    assert maxfd<1e-7
    assert summary['filtered_max_vector_residual']<1e-7
    assert summary['coarse_bayes_formula_error']<1e-12
    assert summary['filtered_full_spectrum_error']<1e-7
    assert summary['filtered_full_spectrum_max_imaginary']<1e-8
    assert summary['general_omega_tau_spectrum_error']<1e-7
    for name,data in [('population_risk.csv',riskrows),('simplex_shape.csv',countrows),('shape_fd.csv',fdrows),('filtered_shape_fd.csv',filtered),('coarse_bayes.csv',coarse),('filtered_full_spectra.csv',spectra),('general_omega_tau_spectra.csv',nonlinear)]:
        with (OUT/name).open('w') as f:
            writer=csv.DictWriter(f,fieldnames=list(data[0]));writer.writeheader();writer.writerows(data)
    (OUT/'summary.json').write_text(json.dumps(summary,indent=2)+'\n')
    print(json.dumps(summary,indent=2))

if __name__=='__main__':main()
