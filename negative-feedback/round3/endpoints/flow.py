from pathlib import Path
import sys,json,csv
import numpy as np
from scipy.integrate import solve_ivp
ROOT=Path(__file__).resolve().parent;OUT=ROOT/'results'
sys.path.insert(0,str(ROOT.parents[1]/'round2'/'theory'/'code'))
from verify_controls import field
from verify_general import BITS
branches=json.loads((OUT/'summary.json').read_text())['branches']
def make(theta):return np.pad(np.stack([np.cos(theta)*BITS[:,0],np.sin(theta)*BITS[:,1]],axis=1),((0,0),(0,2)))
def norm(z):return z/np.linalg.norm(z,axis=1,keepdims=True)
def energies(f):return np.sum((BITS.T@f/4)**2,axis=1)
def distance(f,target):
    u,_,vt=np.linalg.svd(target.T@f);return float(np.linalg.norm(target@(u@vt)-f))
rows=[];final=[]
for K in [1,4,5,8]:
    endpoint=next(r for r in branches if r['K']==K and r['full_stable']);target=make(endpoint['theta'])
    horizon=20/endpoint['min_gradient_real']
    for seed in [9301,9302,9303,9501,9502,9503]:
        rng=np.random.default_rng(seed);initial=norm(make(np.pi/4-.01)+.001*rng.normal(size=(4,4)))
        sol=solve_ivp(lambda t,z:-field(z.reshape(4,4),K,'natural',1).reshape(-1),[0,horizon],initial.reshape(-1),
            method='Radau',rtol=1e-8,atol=1e-11,t_eval=np.array([0,.01,.1,.5,1])*horizon)
        assert sol.success
        for t,z in zip(sol.t,sol.y.T):
            f=norm(z.reshape(4,4));e=energies(f)
            rows.append({'K':K,'seed':seed,'split':'primary' if seed<9400 else 'confirmation','time':t,
                'weak_factor_energy':float(e.min()),'strong_factor_energy':float(e.max()),'distance_to_candidate':distance(f,target)})
        last=rows[-1];final.append({**last,'criterion_passed':bool(last['distance_to_candidate']<1e-5),'nfev':sol.nfev})
with (OUT/'endpoint_flows.csv').open('w') as f:
    w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
(OUT/'flow_summary.json').write_text(json.dumps({'runs':len(final),'passed':sum(r['criterion_passed'] for r in final),'final':final},indent=2)+'\n')
print(json.dumps({'runs':len(final),'passed':sum(r['criterion_passed'] for r in final),'final':final},indent=2))
