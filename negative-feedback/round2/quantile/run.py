"""Exact population rank filtering; all comparisons use the same initial law."""
from pathlib import Path
from itertools import product
import json,csv
import numpy as np
from scipy.linalg import null_space
from scipy.special import expit

ROOT=Path(__file__).resolve().parent; OUT=ROOT/'results';OUT.mkdir(exist_ok=True)
BITS=np.array(list(product([-1.,1.],repeat=2)))
BASE=np.pad(BITS/np.sqrt(2),((0,0),(0,2)))
EPS=.1; RETAIN=.5; TIE=1e-12
def normalize(z):return z/np.linalg.norm(z,axis=1,keepdims=True)
def sampler(z):
    scores=z@z.T;n=len(z);q=np.zeros((n,n))
    for i in range(n):
        order=sorted([j for j in range(n) if j!=i],key=lambda j:scores[i,j])
        remaining=RETAIN;at=0
        while at<len(order) and remaining>1e-15:
            end=at+1
            while end<len(order) and abs(scores[i,order[end]]-scores[i,order[at]])<=TIE:end+=1
            group=order[at:end];mass=len(group)/(n-1)
            accepted=min(remaining,mass)
            for j in group:q[i,j]=accepted/len(group)/RETAIN
            remaining-=accepted;at=end
        q[i]=(1-EPS)*q[i]+EPS*(1-np.eye(n)[i])/(n-1)
    return q
Q0=sampler(BASE)
def field(z,q):
    z=normalize(z)
    c=q*expit(z@z.T-1)/len(z)
    g=(c+c.T)@z
    return -g+(g*z).sum(axis=1,keepdims=True)*z
def tied(theta):return np.pad(np.stack([np.cos(theta)*BITS[:,0],np.sin(theta)*BITS[:,1]],axis=1),((0,0),(0,2)))
def tied_velocity(theta,policy):
    z=tied(theta); tangent=np.pad(np.stack([-np.sin(theta)*BITS[:,0],np.cos(theta)*BITS[:,1]],axis=1),((0,0),(0,2)))
    return float(np.sum(field(z,Q0 if policy=='frozen' else sampler(z))*tangent)/4)
direction=[]
for sign in [-1,1]:
    for delta in [1e-2,1e-4,1e-6]:
        for p in ['frozen','adaptive']:
            direction.append({'sign':sign,'delta':delta,'policy':p,'velocity':tied_velocity(np.pi/4+sign*delta,p),
                              'one_sided_prediction':sign*(1-EPS)*expit(-1)/6 if p=='adaptive' else 0})
with (OUT/'one_sided.csv').open('w') as f:
    w=csv.DictWriter(f,fieldnames=direction[0]);w.writeheader();w.writerows(direction)
basis=[null_space(z[None,:]) for z in BASE];jac=np.zeros((12,12));h=1e-5
for col in range(12):
    i,j=divmod(col,3);v=np.zeros_like(BASE);v[i]=basis[i][:,j]
    diff=(field(normalize(BASE+h*v),Q0)-field(normalize(BASE-h*v),Q0))/(2*h)
    jac[:,col]=np.concatenate([basis[k].T@diff[k] for k in range(4)])
eig=np.linalg.eigvals(jac);nonzero=eig.real[np.abs(eig.real)>1e-7]
def dist(z):
    u,_,vt=np.linalg.svd(BASE.T@z)
    return float(np.linalg.norm(BASE@(u@vt)-z))
flows=[]
for seed in [7101,7102,7103,7301,7302,7303]:
    rng=np.random.default_rng(seed)
    init=normalize(BASE+1e-4*rng.normal(size=BASE.shape))
    for policy in ['frozen','adaptive']:
        z=init.copy();d0=dist(z)
        for step in range(2000):
            z=normalize(z+.1*field(z,Q0 if policy=='frozen' else sampler(z)))
            if step in [0,9,99,999,1999]:
                gram=z@z.T
                flows.append({'seed':seed,'split':'primary' if seed<7200 else 'confirmation','policy':policy,'step':step+1,
                              'initial_distance':d0,'square_distance':dist(z),'min_candidate_probability':float(sampler(z)[~np.eye(4,dtype=bool)].min()),
                              'gram_eigen_min':float(np.linalg.eigvalsh(gram).min())})
with (OUT/'flows.csv').open('w') as f:
    w=csv.DictWriter(f,fieldnames=flows[0]);w.writeheader();w.writerows(flows)
last=[r for r in flows if r['step']==2000]
summary={'q_square':Q0.tolist(),'frozen_largest_nonrotation':float(nonzero.max()),'frozen_zeros':int(np.sum(np.abs(eig.real)<=1e-7)),
         'stationary_residual':float(np.max(np.abs(field(BASE,Q0)))),'one_sided_limit':float((1-EPS)*expit(-1)/6),
         'one_sided_max_error_at_1e6':max(abs(r['velocity']-r['one_sided_prediction']) for r in direction if r['policy']=='adaptive' and r['delta']==1e-6),
         'frozen_contract':sum(r['square_distance']<r['initial_distance'] for r in last if r['policy']=='frozen'),
         'adaptive_expand':sum(r['square_distance']>10*r['initial_distance'] for r in last if r['policy']=='adaptive'),
         'trajectories_per_policy':6,'tie_tolerance':TIE,'minimum_nonself_support':float(Q0[~np.eye(4,dtype=bool)].min())}
(OUT/'summary.json').write_text(json.dumps(summary,indent=2)+'\n')
print(json.dumps(summary,indent=2))
