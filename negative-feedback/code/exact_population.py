"""Exact four-state InfoNCE; sampler gradients are explicitly separated.
Run: OPENBLAS_NUM_THREADS=1 python code/exact_population.py
"""
import json,csv,itertools,time,platform
from pathlib import Path
import numpy as np
from scipy.special import expit,softmax
from scipy.integrate import solve_ivp
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
ROOT=Path(__file__).resolve().parents[1]
X=np.array(list(itertools.product([-1.,1.],repeat=2)))
C=X[:,None,:]*X[None,:,:]

def qfun(w,kappa,eps):
    sm=softmax(kappa*np.einsum('ijk,k->ij',C,w*w),axis=1)
    return eps/4+(1-eps)*sm,sm

def objective(w,q,rho=(1.,1.)):
    pp=np.prod((1+C*np.array(rho))/2,axis=-1)
    ds=C[:,None,:,:]-C[:,:,None,:] # anchor,positive,negative,factor
    delta=np.einsum('ipnk,k->ipn',ds,w*w)
    prob=pp[:,:,None]*q[:,None,:]/4
    val=np.sum(prob*np.logaddexp(0,delta))
    grad=2*w*np.einsum('ipn,ipnk->k',prob*expit(delta),ds)
    return val,grad

def update_grad(w,kappa,eps,policy,q0=None,full=False,rho=(1.,1.)):
    q,sm=qfun(w,kappa,eps)
    if policy=='uniform': q=np.full((4,4),.25)
    elif policy=='frozen': q=q0
    val,g=objective(w,q,rho)
    if full:
        pp=np.prod((1+C*np.array(rho))/2,axis=-1)
        ds=C[:,None,:,:]-C[:,:,None,:]
        delta=np.einsum('ipnk,k->ipn',ds,w*w)
        losses=np.sum(pp[:,:,None]*np.logaddexp(0,delta),axis=1)
        centered=C-np.einsum('ij,ijk->ik',sm,C)[:,None,:]
        dq=(1-eps)*kappa*sm[:,:,None]*centered*(2*w)
        g+=np.einsum('ij,ijk->k',losses,dq)/4
    return val,g

def run():
    dest=ROOT/'results';dest.mkdir(exist_ok=True)
    rng=np.random.default_rng(29)
    maxerr=0
    checks=[]
    for kappa in [-8,-2,0,2,8]:
      for eps in [.01,.1,1]:
       w=rng.uniform(.1,2,size=2);q,_=qfun(w,kappa,eps)
       _,g=objective(w,q)
       fd=np.array([(objective(w+np.eye(2)[j]*1e-6,q)[0]-objective(w-np.eye(2)[j]*1e-6,q)[0])/2e-6 for j in range(2)])
       maxerr=max(maxerr,float(np.max(abs(g-fd))))
       wb=np.array([2.,0.]);h=1e-6
       # Jacobian of -gradient, not Hessian of composed L(q(w)).
       lam=-(update_grad(wb+np.array([0,h]),kappa,eps,'adaptive')[1][1]-update_grad(wb-np.array([0,h]),kappa,eps,'adaptive')[1][1])/(2*h)
       qboundary,_=qfun(wb,kappa,eps)
       exact=4*np.mean(qboundary[np.arange(4),[1,0,3,2]]*.5+qboundary[np.arange(4),[3,2,1,0]]*expit(-8))
       checks.append(dict(kappa=kappa,eps=eps,missing_factor_growth=lam,formula=exact,lower_bound=eps/2))
    assert maxerr<1e-6,maxerr
    assert all(r['missing_factor_growth']>=r['lower_bound']-1e-9 for r in checks)
    rows=[];traces={};start=time.time()
    # Both exploration and independent confirmation seeds, deterministic population data.
    settings=list(itertools.product([-8,-2,0,2,8],[.01,.1,1],[.5,2],[1e-2,1e-4,1e-6],[11,17,101,211]))
    for kappa,eps,w1,w2,seed in settings:
      gen=np.random.default_rng(seed);w0=np.array([w1,w2])*(1+gen.uniform(-.02,.02,2));q0,_=qfun(w0,kappa,eps)
      # until w2=.1, identity positive gives rate>=eps*sigmoid(-.02),
      # so this is a pre-derived finite deadline, not performance-based extension.
      deadline=max(100.,1.02*np.log(.1/w0[1])/(eps*expit(-.02)))
      for policy in ['uniform','frozen','adaptive']:
       def rhs(t,w):return -update_grad(w,kappa,eps,policy,q0)[1]
       def event(t,w):return w[1]-.1
       event.terminal=True;event.direction=1
       sol=solve_ivp(rhs,[0,deadline],w0,rtol=1e-8,atol=1e-11,events=event)
       hit=float(sol.t_events[0][0]) if len(sol.t_events[0]) else None
       rows.append(dict(kappa=kappa,eps=eps,w1_initial=w0[0],w2_initial=w0[1],seed=seed,split='explore' if seed<100 else 'confirm',policy=policy,hit_time=hit,deadline=deadline,final_w2=sol.y[1,-1],nfev=sol.nfev))
       if seed==101 and w1==2 and w2==1e-6 and kappa in [-8,0,8] and eps==.01:traces[(kappa,policy)]=(sol.t.tolist(),sol.y[1].tolist())
    # Full sampler differentiation check; this is intentionally a different vector field.
    full=[]
    for k in [-8,-2,0,2,8]:
      w=np.array([1.2,.2]);_,g=update_grad(w,k,.1,'adaptive',full=True)
      fd=[]
      for j in range(2):
       e=np.eye(2)[j]*1e-6
       def l(z):q,_=qfun(z,k,.1);return objective(z,q)[0]
       fd.append((l(w+e)-l(w-e))/2e-6)
      full.append(dict(kappa=k,max_gradient_error=float(np.max(abs(g-fd))),stopgrad=update_grad(w,k,.1,'adaptive')[1].tolist(),differentiate_sampler=g.tolist()))
    for fname,data in [('local_stability.csv',checks),('population_runs.csv',rows)]:
      with (dest/fname).open('w') as f:
       wr=csv.DictWriter(f,fieldnames=list(data[0]));wr.writeheader();wr.writerows(data)
    summary=dict(gradient_max_abs_error=maxerr,n_runs=len(rows),n_failed_escape=sum(r['hit_time'] is None for r in rows),confirmation_runs=sum(r['split']=='confirm' for r in rows),min_escape_jacobian=min(r['missing_factor_growth'] for r in checks),max_escape_jacobian=max(r['missing_factor_growth'] for r in checks),wall_seconds=time.time()-start,full_sampler_checks=full,python=platform.python_version(),numpy=np.__version__)
    (dest/'summary.json').write_text(json.dumps(summary,indent=2))
    (dest/'traces.json').write_text(json.dumps({str(k):v for k,v in traces.items()}))
    fig,ax=plt.subplots(figsize=(7,4))
    for (k,p),(t,w) in traces.items():
      if p=='adaptive' or (k==0 and p=='uniform'):ax.semilogy(t,w,label=f'{p}, kappa={k}')
    ax.axhline(.1,color='black',ls=':',label='escape threshold');ax.set(xlabel='gradient-flow time',ylabel='omitted factor amplitude',title='All full-support policies escape; timescales differ');ax.legend();fig.tight_layout();fig.savefig(dest/'escape.png',dpi=160);fig.savefig(dest/'escape.svg');plt.close(fig)
    print(json.dumps(summary,indent=2))
if __name__=='__main__':run()
