"""Independent full lookup-sphere Jacobian at the balanced factor representation.
OPENBLAS_NUM_THREADS=1 python review/negative-feedback/code/full_sphere_center.py
"""
from pathlib import Path
import itertools,json,csv
import numpy as np
from scipy.special import softmax,expit
from scipy.linalg import null_space
from scipy.integrate import solve_ivp

OUT=Path(__file__).resolve().parents[1]/'results'
X=np.array(list(itertools.product([-1.,1.],repeat=2)));A,B=X.T
K=-2.;EPS=.1

def qfun(F):
    return EPS/4+(1-EPS)*softmax(K*(F@F.T),axis=1)

def riemannian_flow(F,q):
    S=F@F.T
    C=q*expit(S-1)/4
    G=(C+C.T)@F
    return -(G-np.sum(G*F,axis=1)[:,None]*F)

def objective(F,q):
    return float(np.sum(q*np.logaddexp(0,F@F.T-1))/4)

def align_distance(F,F0):
    U,_,Vt=np.linalg.svd(F.T@F0)
    return float(np.linalg.norm(F@(U@Vt)-F0))

checks=[];runs=[];max_fd=0.;max_jacerr=0.
for d in [2,3,4]:
    F0=np.zeros((4,d));F0[:,:2]=X/np.sqrt(2)
    q0=qfun(F0)
    bases=np.stack([null_space(f[None,:]) for f in F0])
    n=4*(d-1)
    def retract(y):
        F=F0+np.einsum('idk,ik->id',bases,np.asarray(y).reshape(4,d-1))
        return F/np.linalg.norm(F,axis=1)[:,None]
    def local_flow(y,mode):
        F=retract(y)
        q=q0 if mode=='frozen' else qfun(F)
        return np.einsum('idk,id->ik',bases,riemannian_flow(F,q)).ravel()
    def jac(mode,h):
        return np.column_stack([(local_flow(h*np.eye(n)[j],mode)-local_flow(-h*np.eye(n)[j],mode))/(2*h) for j in range(n)])
    for mode in ['frozen','adaptive']:
        J=jac(mode,1e-5);Jcheck=jac(mode,3e-6)
        max_jacerr=max(max_jacerr,float(np.max(abs(J-Jcheck))))
        eig=np.linalg.eigvalsh((J+J.T)/2)
        nonzero=eig[abs(eig)>1e-7]
        if mode=='frozen': assert nonzero.max()<0,(d,eig)
        else: assert nonzero.max()>0,(d,eig)
        checks.append(dict(dimension=d,policy=mode,min_q=float(q0.min()),n_tangent=n,
                           n_rotation_zero=int(np.sum(abs(eig)<=1e-7)),positive_eigenvalues=int(np.sum(eig>1e-7)),
                           negative_eigenvalues=int(np.sum(eig<-1e-7)),eigenvalues=json.dumps(eig.tolist())))
    # Check gradient of the frozen objective at an off-center point independently.
    rng=np.random.default_rng(72+d);y=rng.normal(size=n)*.003
    F=retract(y);v=rng.normal(size=(4,d));v-=np.sum(v*F,axis=1)[:,None]*F
    step=1e-6
    def rt(t):
        R=F+t*v
        return R/np.linalg.norm(R,axis=1)[:,None]
    fd=(objective(rt(step),q0)-objective(rt(-step),q0))/(2*step)
    analytic=-float(np.sum(riemannian_flow(F,q0)*v))
    max_fd=max(max_fd,abs(fd-analytic))
    if d>=3:
      for seed,amp in itertools.product([109,239],[1e-4,1e-6]):
        rng=np.random.default_rng(seed)
        y=rng.normal(size=n)*amp
        Fstart=retract(y);dist0=align_distance(Fstart,F0)
        for mode in ['frozen','adaptive']:
          def rhs(t,z):
            R=z.reshape(4,d);R=R/np.linalg.norm(R,axis=1)[:,None]
            q=q0 if mode=='frozen' else qfun(R)
            return riemannian_flow(R,q).ravel()
          sol=solve_ivp(rhs,[0,100],Fstart.ravel(),rtol=1e-10,atol=1e-12)
          end=sol.y[:,-1].reshape(4,d)
          drift=float(np.max(abs(np.linalg.norm(end,axis=1)-1)))
          end=end/np.linalg.norm(end,axis=1)[:,None]
          dist=align_distance(end,F0)
          runs.append(dict(dimension=d,seed=seed,initial_noise=amp,policy=mode,initial_square_distance=dist0,
                           final_square_distance=dist,distance_amplification=dist/dist0,norm_drift=drift))

assert max_fd<1e-7,max_fd
assert max_jacerr<1e-7,max_jacerr
assert all(r['distance_amplification']<1 if r['policy']=='frozen' else r['distance_amplification']>1 for r in runs)
for name,data in [('square_full_tangent.csv',checks),('square_full_flow.csv',runs)]:
    with (OUT/name).open('w') as f:
        w=csv.DictWriter(f,fieldnames=list(data[0]));w.writeheader();w.writerows(data)
summary={'gradient_directional_error':max_fd,'jacobian_stepsize_error':max_jacerr,
         'dimensions':[2,3,4],'epsilon':EPS,'kappa':K,'conditions':checks,'runs':len(runs),
         'all_frozen_shrink_and_adaptive_grow':True,'max_norm_drift':max(r['norm_drift'] for r in runs)}
(OUT/'square_summary.json').write_text(json.dumps(summary,indent=2)+'\n')
print(json.dumps(summary,indent=2))
