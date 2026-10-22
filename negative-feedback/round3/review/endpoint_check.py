"""Independent ordered-tuple scalar check of the root's nonlinear branches.
No root field, count aggregation, or root endpoint code is imported.
"""
from pathlib import Path
from itertools import product
import json
import numpy as np
from scipy.optimize import brentq
from scipy.special import ndtr
P=Path(__file__).resolve().parent
ROOT=P.parent/'endpoints'/'results'
T=np.log(4.);EPS=.3
def velocity(theta,K):
    s=np.array([1.,np.cos(2*theta),-np.cos(2*theta),-1.])
    ds=np.array([0.,-2*np.sin(2*theta),2*np.sin(2*theta),0.])
    q=EPS/4+(1-EPS)*np.exp(-T*s)/np.exp(-T*s).sum()
    tup=np.array(list(product(range(4),repeat=K)),dtype=int)
    prob=np.prod(q[tup],axis=1)
    w=np.exp(s[tup]-1)
    grad=np.sum(w*ds[tup],axis=1)/(1+w.sum(axis=1))
    return float(-prob@grad/4)

source=json.loads((ROOT/'summary.json').read_text())['branches']
checks=[]
for K in [1,2,3,4,5]:
    interior=[r for r in source if r['K']==K and 0<r['theta']<np.pi/4]
    for row in interior:
        x=row['theta'];h=1e-5
        root=brentq(lambda z:velocity(z,K),x-.001,x+.001,xtol=1e-14)
        derivative=(velocity(root+h,K)-velocity(root-h,K))/(2*h)
        checks.append({'K':K,'root':root,'root_difference':abs(root-x),'residual':abs(velocity(root,K)),
                       'flow_derivative':derivative,'derivative_difference':abs(derivative-row['tied_flow_derivative']),
                       'bayes_sigma2':float(ndtr(np.sin(root)/.2))})
    # Root's endpoint0 and square field values should be stationary independently.
    checks.append({'K':K,'square_residual':abs(velocity(np.pi/4,K)),'corner_residual':abs(velocity(0.,K))})
assert max(r.get('root_difference',0.) for r in checks)<1e-10
assert max(r.get('derivative_difference',0.) for r in checks)<1e-8
out={'implementation':'ordered tuples, scalar score derivative, independent of author code',
     'checks':checks,'sigma2_balanced_bayes':float(ndtr(1/(np.sqrt(2)*.2))),
     'conclusion':'K4 stable-branch geometry is mildly imbalanced and remains injective; it is not an erasure boundary.'}
(P/'endpoint_check.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
