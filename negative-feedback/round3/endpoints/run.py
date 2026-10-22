"""Nonlinear endpoints of the previously proved square instability."""
from pathlib import Path
import sys,json,csv
import numpy as np
from scipy.optimize import brentq
from scipy.linalg import null_space
from scipy.special import ndtr
ROOT=Path(__file__).resolve().parent;OUT=ROOT/'results';OUT.mkdir(exist_ok=True)
sys.path.insert(0,str(ROOT.parents[1]/'round2'/'theory'/'code'))
from verify_controls import field,policy,moments
from verify_general import BITS
def embedding(theta):return np.pad(np.stack([np.cos(theta)*BITS[:,0],np.sin(theta)*BITS[:,1]],axis=1),((0,0),(0,2)))
def tangent(theta):return np.pad(np.stack([-np.sin(theta)*BITS[:,0],np.cos(theta)*BITS[:,1]],axis=1),((0,0),(0,2)))
def velocity(theta,K):
    return float(-np.sum(field(embedding(theta),K,'natural',1)*tangent(theta))/4)
def spectrum(theta,K):
    f=embedding(theta);basis=[null_space(z[None,:]) for z in f];h=3e-6;J=np.zeros((12,12))
    for col in range(12):
        i,j=divmod(col,3);v=np.zeros_like(f);v[i]=basis[i][:,j]
        d=(field(f+h*v,K,'natural',1)-field(f-h*v,K,'natural',1))/(2*h)
        J[:,col]=np.concatenate([basis[k].T@d[k] for k in range(4)])
    eig=np.linalg.eigvals(J);nz=eig.real[np.abs(eig)>1e-7]
    return {'min_gradient_real':float(nz.min()),'max_gradient_real':float(nz.max()),
            'max_imag':float(np.abs(eig.imag).max()),'zero_modes':int(np.sum(np.abs(eig)<=1e-7)),
            'stationary_residual':float(np.abs(field(f,K,'natural',1)).max()),'full_stable':bool(nz.min()>0)}
branches=[];curves=[]
for K in range(1,9):
    grid=np.linspace(1e-6,np.pi/4-1e-6,401);vel=np.array([velocity(x,K) for x in grid])
    for x,v in zip(grid,vel):curves.append({'K':K,'theta':float(x),'velocity':float(v)})
    roots=[0.,np.pi/4]
    for lo,hi,vl,vh in zip(grid[:-1],grid[1:],vel[:-1],vel[1:]):
        if vl*vh<0:roots.append(brentq(lambda x:velocity(x,K),lo,hi,xtol=1e-13))
    for theta in sorted(roots):
        h=1e-5;dv=(velocity(theta+h,K)-velocity(theta-h,K))/(2*h)
        minimum=float(min(abs(np.sin(theta)),abs(np.cos(theta))))
        r={'K':K,'theta':theta,'delta_from_square':float(np.pi/4-theta),'weak_energy':minimum**2,
           'tied_flow_derivative':dv,'noiseless_factor_information_bits':0 if theta==0 else 1,
           'worst_factor_bayes_sigma05':float(ndtr(minimum/.05)),
           'worst_factor_bayes_sigma2':float(ndtr(minimum/.2)),**spectrum(theta,K)}
        branches.append(r)
def save(name,rows):
    with (OUT/name).open('w') as f:
        writer=csv.DictWriter(f,fieldnames=list(rows[0]));writer.writeheader();writer.writerows(rows)
save('branches.csv',branches);save('angular_fields.csv',curves)
summary={'branches':branches,'criterion':'Interior root finding is a finite grid numerical search, not a uniqueness proof.',
         'mild_branch_hypothesis':'If K4 endpoint remains near square, local instability is not major semantic degradation.'}
(OUT/'summary.json').write_text(json.dumps(summary,indent=2)+'\n');print(json.dumps(summary,indent=2))
