from pathlib import Path
import sys,json,csv
import numpy as np
from scipy.integrate import solve_ivp
ROOT=Path(__file__).resolve().parent;OUT=ROOT/'results'
sys.path.insert(0,str(ROOT.parent/'theory'/'code'))
from verify_controls import policy,field,moments,F0
from verify_general import BITS

def norm(z):return z/np.linalg.norm(z,axis=1,keepdims=True)
def imbalance(z):
    ma=BITS[:,0]@z/4;mb=BITS[:,1]@z/4
    return float(ma@ma-mb@mb)
rows=[];checks=[]
for K in [4,5]:
    lam=moments(K,'natural',1)['adaptive_balance'];rate=abs(lam);times=np.array([0,.5,1,2,3])/rate
    for seed in [8101,8102,8301,8302]:
        rng=np.random.default_rng(seed);theta=np.pi/4+1e-5
        init=np.pad(np.stack([np.cos(theta)*BITS[:,0],np.sin(theta)*BITS[:,1]],axis=1),((0,0),(0,2)))
        init=norm(init+1e-6*rng.normal(size=init.shape));b0=imbalance(init)
        assert abs(b0)>1e-6
        for pol in ['frozen','adaptive']:
            q0=policy(F0,'natural') if pol=='frozen' else None
            fun=lambda t,z:-field(z.reshape(4,4),K,'natural',1,q0).reshape(-1)
            sol=solve_ivp(fun,[0,times[-1]],init.reshape(-1),method='Radau',t_eval=times,rtol=1e-8,atol=1e-12)
            assert sol.success,sol.message
            err=0
            for t,z in zip(sol.t,sol.y.T):
                z=z.reshape(4,4);err=max(err,float(np.abs(np.linalg.norm(z,axis=1)-1).max()))
                b=imbalance(norm(z))
                rows.append({'K':K,'seed':seed,'split':'primary' if seed<8200 else 'confirmation','policy':pol,'time':t,
                             'scaled_time':t*rate,'imbalance':b,'initial_imbalance':b0,'ratio':abs(b/b0),
                             'linear_adaptive_prediction':float(np.exp(-lam*t)),'adaptive_eigenvalue':lam})
            last=rows[-1];passed=(last['ratio']>10 if pol=='adaptive' and K==4 else last['ratio']<.1)
            checks.append({'K':K,'seed':seed,'policy':pol,'passed':bool(passed),'final_ratio':last['ratio'],
                           'nfev':sol.nfev,'max_norm_error':err})
with (OUT/'trajectories.csv').open('w') as f:
    w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
summary={'runs':len(checks),'passed':sum(x['passed'] for x in checks),'max_norm_error':max(x['max_norm_error'] for x in checks),'checks':checks}
(OUT/'summary.json').write_text(json.dumps(summary,indent=2)+'\n')
print(json.dumps(summary,indent=2))
