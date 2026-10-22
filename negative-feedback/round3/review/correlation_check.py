from pathlib import Path
from itertools import product
import json
import numpy as np
P=Path(__file__).resolve().parent
raw=json.loads((P.parent/'correlation'/'results'/'summary.json').read_text())['moment_matched']
K=12;EPS=.3;T=np.log(4.);tuples=np.array(list(product(range(4),repeat=4)),dtype=int)

def angular_field(theta,part,alpha):
    s=np.array([1.,np.cos(2*theta),-np.cos(2*theta),-1.])
    ds=np.array([0.,-2*np.sin(2*theta),2*np.sin(2*theta),0.])
    z=np.exp(-T*s+alpha*s*(s*s-1))
    q=EPS/4+(1-EPS)*z/z.sum()
    prob=np.prod(q[tuples],axis=1)
    w=np.exp(s[tuples]-1)*np.array(part)[None,:]
    deriv=(w*ds[tuples]).sum(axis=1)/(1+w.sum(axis=1))
    # Return the projected loss-gradient field, not the negative flow.
    return float(prob@deriv/4)

checks=[]
for r in raw:
    part=r['partition'];alpha=r['alpha'];h=1e-5
    fd=(angular_field(np.pi/4+h,part,alpha)-angular_field(np.pi/4-h,part,alpha))/(2*h)
    a=-T+alpha*np.array([-1.,2.])
    checks.append({'partition':part,'balance_fd':fd,'expected_balance':r['balance_analytic'],
                   'difference':abs(fd-r['balance_analytic']),
                   'same_source_pair':sum(x*(x-1) for x in part)/(K*(K-1)),
                   'max_logweight_derivative_exact':float(a.max())})
assert max(r['difference'] for r in checks)<1e-8
assert checks[0]['balance_fd']*checks[1]['balance_fd']<0
assert checks[0]['same_source_pair']==checks[1]['same_source_pair']
out={'checks':checks,'source_draws':4,'K':K,
     'interpretation':'Scalar signs independently verified; significance is assessed separately from this numerical agreement.'}
(P/'correlation_check.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
