"""Independent tagged-draw quadrature and direct tuple checks of a new multilevel law."""
from pathlib import Path
from itertools import product
import csv,json,time
import numpy as np
from scipy.integrate import quad_vec
from scipy.special import gammaln

ROOT=Path(__file__).resolve().parent;OUT=ROOT/'results'

def policy(scores,p,t,eps):
    w=np.exp(-t*scores);Z=p@w
    q=eps*p+(1-eps)*p*w/Z
    rho=(1-eps)*w/Z/(eps+(1-eps)*w/Z)
    return q,rho

def critical(scores,h2,p,t):
    Z=p@np.exp(-t*scores)
    a=(t-1)*(p@(h2*np.exp((1-t)*scores)))
    b=Z*(p@(h2*np.exp(scores)))
    return a/(a+b)

def curvature(scores,h2,p,t,eps,beta,Ks):
    Ks=np.asarray(Ks,float)
    q,rho=policy(scores,p,t,eps);W=np.exp(scores-1)
    nu=q*h2*W
    def integrand(u):
        r=u/Ks
        e=np.exp(-r[:,None]*W[None,:])
        phi=e@q
        with np.errstate(divide='ignore'):
            pre=np.exp(-beta*r+(Ks-1)*np.log(np.maximum(phi,1e-300)))
        inner=np.sum(e*nu[None,:]*((1-t*rho)[None,:]-r[:,None]*W[None,:]),axis=1)
        return pre*inner
    value,error=quad_vec(integrand,0,np.inf,epsabs=2e-12,epsrel=2e-11)
    mu=q@W
    Q=np.sum(q*h2*W*(1-t*rho))
    return value,{'quad_error':float(error),'limit':float(Q/mu),'critical_floor':float(critical(scores,h2,p,t))}

def tuple_field(delta,scores,h,p,t,eps,beta,K,frozen=False):
    ix=np.array(list(product(range(len(scores)),repeat=K)),int)
    sd=scores+delta*h
    q,_=policy(scores if frozen else sd,p,t,eps)
    probs=np.prod(q[ix],axis=1)
    Ws=np.exp(sd[ix]-1);D=beta+Ws.sum(axis=1)
    return float(probs@((Ws*h[ix]).sum(axis=1)/D))

def write(name,rows):
    with (OUT/name).open('w') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)

def main():
    started=time.time();rng=np.random.default_rng(33017);populations=[]
    for i in range(16):
        levels=np.sort(rng.uniform(-.9,.9,3));mass=rng.dirichlet(np.ones(3));amp=rng.uniform(.2,1.4,3)
        s=np.repeat(levels,2);h=np.repeat(amp,2)*np.tile([-1.,1.],3);p=np.repeat(mass/2,2)
        populations.append((s,h,p))
    rows=[];checkrows=[];violations=[];maxerr=0;boundary=0
    for i,(s,h,p) in enumerate(populations):
        for t in [1.2,1.8,3.0]:
            ec=critical(s,h*h,p,t)
            for scale in [.8,1.,1.2]:
                eps=float(np.clip(ec*scale,1e-5,1-1e-5))
                for beta in [0,1]:
                    val,diag=curvature(s,h*h,p,t,eps,beta,np.arange(1,65))
                    pos=val>1e-9;neg=val< -1e-9
                    if np.any(pos):
                        first=int(np.flatnonzero(pos)[0]);bad=np.flatnonzero(neg[first:])+first
                        if len(bad):violations.append({'population':i,'t':t,'eps':eps,'beta':beta,'type':'stable_to_unstable','Ks':(bad+1).tolist()})
                    if scale<=1 and np.max(val)>1e-9:
                        violations.append({'population':i,'t':t,'eps':eps,'beta':beta,'type':'subcritical_positive'})
                    for K,v in enumerate(val,1):rows.append({'population':i,'t':t,'eps':eps,'critical_scale':scale,'beta':beta,'K':K,'curvature':float(v),**diag})
                    maxerr=max(maxerr,diag['quad_error'])
                    if scale==1:boundary=max(boundary,float(np.max(val)))
        if i<4:
            t=1.8;eps=.3
            for beta in [0,1]:
                val,_=curvature(s,h*h,p,t,eps,beta,[1,2,3,4])
                for K in [1,2,3,4]:
                    for step in [1e-5,3e-6]:
                        fd=(tuple_field(step,s,h,p,t,eps,beta,K)-tuple_field(-step,s,h,p,t,eps,beta,K))/(2*step)
                        err=abs(fd-val[K-1]);checkrows.append({'population':i,'beta':beta,'K':K,'step':step,'quadrature':float(val[K-1]),'direct_tuple_fd':fd,'abs_error':float(err)})
    cube=[];cubechecks=[]
    for m in [2,3,4,8,16,32,128]:
        for t in [1.2,np.log(4),2.,3.]:
            z=np.arange(m+1);s=(m-2*z)/m
            p=np.exp(gammaln(m+1)-gammaln(z+1)-gammaln(m-z+1)-m*np.log(2))
            h2=8*z*(m-z)/(m*(m-1)) # h=z1-z2, with conditional P(h!=0)=2r(m-r)/(m(m-1))
            a=(t-1)*np.cosh((t-1)/m)**(m-2)
            b=np.cosh(t/m)**m*np.cosh(1/m)**(m-2)
            ec=a/(a+b);ec_direct=critical(s,h2,p,t)
            assert abs(ec-ec_direct)<2e-13
            for scale in [.8,1.2]:
                eps=float(np.clip(ec*scale,1e-5,1-1e-5))
                val,diag=curvature(s,h2,p,t,eps,1,np.arange(1,65))
                positive=np.flatnonzero(val>1e-9)
                cube.append({'m':m,'t':float(t),'critical_floor':float(ec),'eps':eps,'scale':scale,'limit_floor':float(1-1/t),
                             'H1':float(val[0]),'H64':float(val[-1]),'Hinf':diag['limit'],'first_positive_through64':int(positive[0]+1) if len(positive) else None})
    for m in [2,3,4,8]:
        bits=np.array(list(product([-1.,1.],repeat=m)));s=bits.mean(axis=1);h=bits[:,0]-bits[:,1];p=np.full(len(bits),1/len(bits));t=np.log(4)
        Z=p@np.exp(-t*s);ec=critical(s,h*h,p,t)
        for c in [-2.,-1.,0.,1.,2.]:
            actual=p@(h*h*np.exp(c*s));pred=2*np.cosh(c/m)**(m-2)
            cubechecks.append({'m':m,'check':'moment','parameter':c,'actual':float(actual),'predicted':float(pred),'abs_error':float(abs(actual-pred))})
        if m in [2,3]:
            val,_=curvature(s,h*h,p,t,.3,1,[1,2,3])
            for K in [1,2,3]:
                fd=(tuple_field(1e-5,s,h,p,t,.3,1,K)-tuple_field(-1e-5,s,h,p,t,.3,1,K))/(2e-5)
                cubechecks.append({'m':m,'check':'tuple_fd','parameter':K,'actual':float(fd),'predicted':float(val[K-1]),'abs_error':float(abs(fd-val[K-1]))})
    assert not violations,violations
    assert max(x['abs_error'] for x in checkrows)<2e-6
    assert max(x['abs_error'] for x in cubechecks)<2e-6
    write('random_curvatures.csv',rows);write('ordered_tuple_checks.csv',checkrows);write('hypercube_floors.csv',cube);write('hypercube_checks.csv',cubechecks)
    summary={'population_count':len(populations),'random_settings':len(rows),'tuple_checks':len(checkrows),'hypercube_checks':len(cubechecks),
             'max_direct_tuple_error':max(x['abs_error'] for x in checkrows),'max_cube_error':max(x['abs_error'] for x in cubechecks),
             'max_reported_quadrature_error':maxerr,'stable_to_unstable_or_subcritical_violations':violations,
             'critical_boundary_max_positive':boundary,'elapsed_seconds':time.time()-started}
    (OUT/'summary.json').write_text(json.dumps(summary,indent=2)+'\n');print(json.dumps(summary,indent=2))
if __name__=='__main__':main()
