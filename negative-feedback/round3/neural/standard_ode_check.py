from pathlib import Path
import json,time,numpy as np
from scipy.integrate import solve_ivp
from model import *
from oracle import policy
from view_spectrum import positive,reference,jacobian
ROOT=Path(__file__).resolve().parent;OUT=ROOT/'results'
seed,K=4101,16;x,bits,render=dataset();P=.95*np.eye(16)+.05*positive(4);f0=reference(4);v=construct(seed)
J=output_jacobian(v,x);u,s,vh=np.linalg.svd(J,full_matrices=False);Q=vh[s>1e-9].T
H,T=jacobian(f0,P,K);JQ=T.T@J@Q;B=JQ.T@((H+H.T)/2)@JQ
vals,vec=np.linalg.eigh(B);idx=int(np.argmin(vals));target=Q@vec[:,idx];rate=abs(vals[idx])
rng=np.random.default_rng(seed+K);init=v+1e-5*target+1e-7*rng.normal(size=len(v));a0=float(target@(init-v))
rows=[]
for pol in ['frozen','adaptive']:
    count=[0];qf=policy(f0) if pol=='frozen' else None;started=time.time()
    def rhs(t,w):
        count[0]+=1
        if count[0]>200000:raise RuntimeError('declared RHS budget reached')
        return -value_gradient(w,x,P,K,qf)[1]
    try:
        sol=solve_ivp(rhs,[0,3/rate],init,method='DOP853',t_eval=[0,3/rate],rtol=1e-9,atol=1e-12)
        assert sol.success,sol.message
        ratio=abs(float(target@(sol.y[:,-1]-v))/a0)
        rows.append({'policy':pol,'success':True,'rhs_calls':count[0],'final_ratio':ratio,
                     'continuous_linear_prediction':float(np.exp(3)),
                     'relative_error_to_linear':abs(ratio/np.exp(3)-1),'elapsed_seconds':time.time()-started})
    except RuntimeError as e:
        rows.append({'policy':pol,'success':False,'rhs_calls':count[0],'block':str(e),'elapsed_seconds':time.time()-started})
summary={'seed':seed,'K':K,'rho':.05,'method':'standard unpreconditioned DOP853','runs':rows}
(OUT/'standard_ode_check.json').write_text(json.dumps(summary,indent=2)+'\n');print(json.dumps(summary,indent=2))
assert all(r['success'] and r['relative_error_to_linear']<.01 for r in rows)
