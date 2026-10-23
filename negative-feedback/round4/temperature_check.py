from pathlib import Path
from itertools import product
import csv, json
import numpy as np

ROOT=Path(__file__).resolve().parent
bits=np.array(list(product([-1.,1.],repeat=3)))
s=bits.mean(axis=1);h=bits[:,0]-bits[:,1]

def policy(scores,t,eps):
    w=np.exp(-t*scores);q=eps/8+(1-eps)*w/w.sum()
    rho=((1-eps)*w/w.sum())/q
    return q,rho

def field(delta,tau,t,eps,ix):
    sd=s+delta*h;q,_=policy(sd,t,eps)
    probability=np.prod(q[ix],axis=1)
    w=np.exp((sd[ix]-1)/tau);D=1+w.sum(axis=1)
    return float(probability@((w*h[ix]).sum(axis=1)/(tau*D)))

rows=[];checks=[]
for tau,t,eps,K in product([.25,.5,1.,2.],[-2.,0.,np.log(4.),3.],[.1,.3],[1,2,3]):
    ix=np.array(list(product(range(8),repeat=K)),int)
    q,rho=policy(s,t,eps);probability=np.prod(q[ix],axis=1)
    w=np.exp((s[ix]-1)/tau);D=1+w.sum(axis=1)
    numerator=(w*h[ix]).sum(axis=1)
    second=(w*h[ix]**2).sum(axis=1)/D-numerator**2/D**2
    response=-t*numerator*(rho[ix]*h[ix]).sum(axis=1)/D
    H=float(probability@(second/tau**2+response/tau))
    drift=field(0,tau,t,eps,ix)
    rows.append({'tau':tau,'policy_t':t,'epsilon':eps,'K':K,'theta':t*tau,
                 'existing_no_rescue_theorem_applies':t*tau>1,'curvature':H,'drift':drift})
    if tau in [.5,1.] and t in [-2.,np.log(4.)] and eps==.3:
        for step in [1e-5,3e-6]:
            fd=(field(step,tau,t,eps,ix)-field(-step,tau,t,eps,ix))/(2*step)
            checks.append({'tau':tau,'policy_t':t,'K':K,'step':step,'analytic':H,
                           'detached_field_fd':fd,'absolute_error':abs(H-fd)})
summary={'settings':len(rows),'max_stationary_drift':max(abs(x['drift']) for x in rows),
         'max_fd_error':max(x['absolute_error'] for x in checks),
         'hard_or_uniform_min_curvature':min(x['curvature'] for x in rows if x['policy_t']<=0),
         'theta_gt1_settings':int(sum(x['existing_no_rescue_theorem_applies'] for x in rows)),
         'scope':'temperature rescaling and a direct local corollary; neither new top-journal contribution nor generic hard-negative guarantee'}
assert summary['max_stationary_drift']<1e-12
assert summary['max_fd_error']<1e-6
assert summary['hard_or_uniform_min_curvature']>0
for name,data in [('temperature_rows.csv',rows),('temperature_fd.csv',checks)]:
    with (ROOT/name).open('w') as f:
        writer=csv.DictWriter(f,fieldnames=list(data[0]));writer.writeheader();writer.writerows(data)
(ROOT/'temperature_summary.json').write_text(json.dumps(summary,indent=2)+'\n')
print(json.dumps(summary,indent=2))
