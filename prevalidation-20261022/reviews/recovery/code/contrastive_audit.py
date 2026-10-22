"""Independent contrastive loss and gradient checks, after owner results."""
from pathlib import Path
import importlib.util
import itertools
import json
import sys
import numpy as np

ROOT=Path(__file__).resolve().parents[1];REPO=ROOT.parents[2];OUT=ROOT/'results'
X=np.array(list(itertools.product([-1.,1.],repeat=3)))

def law(rho):
    P=np.zeros((8,8))
    for i in range(8):
        for j in range(8):
            P[i,j]=1/8
            for k in range(3):P[i,j]*=(1+rho[k]*X[i,k]*X[j,k])/2
    return P

def objective(F,P):
    Z=F/np.sqrt(np.sum(F*F,axis=1,keepdims=True)+1e-12)
    S=Z@Z.T
    # This grid is bounded, so direct expectation avoids a shared logsumexp implementation.
    return -np.sum(P*S)+np.log(np.mean(np.exp(S),axis=1)).mean()

closed=[]
for rho in [[.9,.9,.9],[.9,.9,0]]:
    for w in [[.5,.5,0],[1/3,1/3,1/3],[.7,.2,.1],[.01,.01,.98]]:
        v=np.sqrt(w);F=X*v
        # Remove epsilon from this exact closed-form comparison.
        S=F@F.T
        empirical=-np.sum(law(rho)*S)+np.log(np.exp(S).mean(1)).mean()
        exact=-np.dot(rho,w)+np.log(np.cosh(w)).sum()
        closed.append({'rho':rho,'w':w,'direct_loss':float(empirical),'closed_loss':float(exact),
                       'error':abs(float(empirical-exact))})

sys.path.insert(0,str(REPO/'ssl-recovery/code'))
spec=importlib.util.spec_from_file_location('owner_contrastive',REPO/'ssl-recovery/code/run_contrastive_control.py')
owner=importlib.util.module_from_spec(spec);spec.loader.exec_module(owner)
gradient=[]
for seed in [1901,1902]:
    rng=np.random.default_rng(seed)
    theta={'w1':rng.normal(size=(3,12))*.5,'w2':rng.normal(size=(12,3))*.3}
    for rho in [[.9,.9,.9],[.9,.9,0]]:
        P=law(rho);_,G=owner.loss_grad(theta,P);errors=[]
        for k,arr in theta.items():
            for ind in np.ndindex(arr.shape):
                old=arr[ind];h=1e-5;arr[ind]=old+h
                lp=objective(np.tanh(X@theta['w1'])@theta['w2'],P)
                arr[ind]=old-h;lm=objective(np.tanh(X@theta['w1'])@theta['w2'],P);arr[ind]=old
                errors.append(abs((lp-lm)/(2*h)-G[k][ind]))
        gradient.append({'seed':seed,'rho':rho,'gradient_max_abs_error':float(max(errors))})
out={'closed_form_checks':closed,'independent_gradient_checks':gradient}
(OUT/'contrastive_audit.json').write_text(json.dumps(out,indent=2)+'\n')
assert max(r['error'] for r in closed)<1e-12
assert max(r['gradient_max_abs_error'] for r in gradient)<1e-6
print(json.dumps({'closed_form_error':max(r['error'] for r in closed),
                  'independent_gradient_error':max(r['gradient_max_abs_error'] for r in gradient)},indent=2))
