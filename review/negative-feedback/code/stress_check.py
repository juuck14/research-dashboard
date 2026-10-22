"""Independent full tangent-space check; no owner code imports.
OPENBLAS_NUM_THREADS=1 python review/negative-feedback/code/stress_check.py
"""
from pathlib import Path
import json,csv,itertools
import numpy as np
from scipy.special import softmax,expit
from scipy.integrate import solve_ivp

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'results';OUT.mkdir(exist_ok=True)
X=np.array(list(itertools.product([-1.,1.],repeat=2)))
A,B=X.T
PHI=np.where(A>0,0.,np.pi)

def policy(phi,k,e):
    s=np.cos(phi[:,None]-phi[None,:])
    sm=softmax(k*s,axis=1)
    return e/4+(1-e)*sm,sm

def loss(phi,q):
    s=np.cos(phi[:,None]-phi[None,:])
    return np.sum(q*np.logaddexp(0,s-1))/4

def grad(phi,k,e,mode='adaptive',q0=None):
    d=phi[:,None]-phi[None,:]
    s=np.cos(d)
    q,sm=policy(phi,k,e)
    if mode=='frozen': q=q0
    elif mode=='uniform': q=np.ones((4,4))/4
    weight=q*expit(s-1)/4
    if mode=='full':
        ell=np.logaddexp(0,s-1)
        weight+=(1-e)*k*sm*(ell-np.sum(sm*ell,axis=1)[:,None])/4
    return -np.sum((weight+weight.T)*np.sin(d),axis=1)

def jac(fun,x,h):
    return np.column_stack([(fun(x+h*np.eye(len(x))[j])-fun(x-h*np.eye(len(x))[j]))/(2*h) for j in range(len(x))])

rows=[];max_fd=0.;max_jacdiff=0.
for k,e in itertools.product([-8,-2,0,2,8],[.01,.1,1.]):
    q0,_=policy(PHI,k,e)
    H=jac(lambda z:grad(z,k,e,'frozen',q0),PHI,1e-5)
    HA=jac(lambda z:grad(z,k,e,'adaptive'),PHI,1e-5)
    HC=jac(lambda z:grad(z,k,e,'adaptive'),PHI,3e-6)
    max_jacdiff=max(max_jacdiff,float(np.max(abs(H-HA))),float(np.max(abs(HC-HA))))
    eig=np.linalg.eigvalsh((H+H.T)/2)
    # f_t=(a,t*b)/sqrt(1+t²) has angle tangent a*b.
    v=A*B
    D=-q0[0,1]+2*q0[0,2]*expit(-2)
    predicted_curvature=2*D
    measured=float(v@H@v)
    assert abs(predicted_curvature-measured)<1e-7,(k,e,predicted_curvature,measured)
    nonrot=eig[np.argsort(abs(eig))[1:]]
    rows.append(dict(kappa=k,epsilon=e,q_floor=float(q0.min()),D=D,mode_curvature=measured,
                     eigenvalues=json.dumps(eig.tolist()),strict_min_mod_rotation=bool(nonrot.min()>1e-8),
                     adaptive_frozen_max_error=float(np.max(abs(H-HA)))))
    z=PHI+np.array([.021,-.013,.017,-.019])
    g=grad(z,k,e,'frozen',q0)
    fd=np.array([(loss(z+np.eye(4)[j]*1e-6,q0)-loss(z-np.eye(4)[j]*1e-6,q0))/(2e-6) for j in range(4)])
    max_fd=max(max_fd,float(np.max(abs(g-fd))))
assert max_fd<1e-7,max_fd
assert max_jacdiff<1e-7,max_jacdiff

runs=[]
for seed in [31,47,103,227]:
    rng=np.random.default_rng(seed)
    perturb=rng.normal(size=4)*1e-4
    perturb-=perturb.mean()
    for k,e in [(-2,.1),(0,.1)]:
      q0,_=policy(PHI,k,e)
      for mode in ['frozen','adaptive','uniform']:
        sol=solve_ivp(lambda t,z:-grad(z,k,e,mode,q0),[0,40],PHI+perturb,rtol=1e-10,atol=1e-12)
        end=sol.y[:,-1]-PHI;end-=end.mean()
        runs.append(dict(seed=seed,split='confirm' if seed>100 else 'explore',kappa=k,epsilon=e,policy=mode,
                         initial_perturb_norm=float(np.linalg.norm(perturb)),final_perturb_norm=float(np.linalg.norm(end)),
                         amplification=float(np.linalg.norm(end)/np.linalg.norm(perturb))))

uncon=[]
for k,e in itertools.product([-8,-2,0,2,8],[.01,.1,1.]):
    def flow(t):
        F=np.column_stack([2*A,t*B]);S=F@F.T
        q=e/4+(1-e)*softmax(k*S,axis=1)
        gap=S-np.diag(S)[:,None]
        dg=2*t*(B[:,None]*B[None,:]-1)
        return -np.sum(q*expit(gap)*dg)/4
    growth=(flow(1e-6)-flow(-1e-6))/(2e-6)
    assert growth>=e/2-1e-9,(k,e,growth)
    uncon.append(dict(kappa=k,epsilon=e,growth=growth,lower_bound=e/2))

for name,data in [('normalized_full_tangent.csv',rows),('normalized_runs.csv',runs),('unnormalized_jacobian.csv',uncon)]:
    with (OUT/name).open('w') as f:
        writer=csv.DictWriter(f,fieldnames=list(data[0]));writer.writeheader();writer.writerows(data)
summary={'gradient_fd_max_error':max_fd,'adaptive_frozen_jacobian_max_error':max_jacdiff,
         'normalized_strict_minima_mod_rotation':sum(x['strict_min_mod_rotation'] for x in rows),
         'normalized_conditions':len(rows),'flow_runs':len(runs),
         'confirmation_runs':sum(x['split']=='confirm' for x in runs),
         'all_unnormalized_directions_unstable':True,
         'interpretation':'Normalization allows full-support omission, but local adaptive Jacobian equals frozen-q Jacobian; no feedback-specific trap shown.'}
(OUT/'summary.json').write_text(json.dumps(summary,indent=2)+'\n')
print(json.dumps(summary,indent=2))
