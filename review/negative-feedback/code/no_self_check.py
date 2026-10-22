from pathlib import Path
import itertools,json
import numpy as np
from scipy.special import softmax,expit
from scipy.linalg import null_space
OUT=Path(__file__).resolve().parents[1]/'results'
X=np.array(list(itertools.product([-1.,1.],repeat=2)))
F0=np.column_stack([X/np.sqrt(2),np.zeros((4,2))]);basis=np.stack([null_space(f[None,:]) for f in F0])
MASK=1-np.eye(4);k=-2.;eps=.1
def qfun(F):
    logits=k*(F@F.T);np.fill_diagonal(logits,-np.inf)
    return eps*MASK/3+(1-eps)*softmax(logits,axis=1)
q0=qfun(F0)
def retract(y):
    F=F0+np.einsum('idk,ik->id',basis,np.asarray(y).reshape(4,3))
    return F/np.linalg.norm(F,axis=1)[:,None]
def vec(y,mode):
    F=retract(y);q=q0 if mode=='frozen' else qfun(F)
    W=q*expit(F@F.T-1)/4;G=(W+W.T)@F
    V=-(G-np.sum(G*F,axis=1)[:,None]*F)
    return np.einsum('idk,id->ik',basis,V).ravel()
rows=[];maxerr=0.
for mode in ['frozen','adaptive']:
    def jac(h):return np.column_stack([(vec(h*np.eye(12)[j],mode)-vec(-h*np.eye(12)[j],mode))/(2*h) for j in range(12)])
    J=jac(1e-5);JJ=jac(3e-6);maxerr=max(maxerr,float(np.max(abs(J-JJ))))
    eig=np.linalg.eigvalsh((J+J.T)/2);nz=eig[abs(eig)>1e-7]
    if mode=='frozen':assert nz.max()<0,eig
    else:assert nz.max()>0,eig
    rows.append({'policy':mode,'max_nonrotation_eigenvalue':float(nz.max()),'positive_modes':int(np.sum(eig>1e-7)),
                 'zero_rotation_modes':int(np.sum(abs(eig)<=1e-7)),'eigenvalues':eig.tolist()})
summary={'dimension':4,'negative_candidates':3,'min_nonself_q':float(q0[MASK.astype(bool)].min()),
         'q_diagonal':np.diag(q0).tolist(),'jacobian_stepsize_error':maxerr,'conditions':rows,
         'interpretation':'Same instability persists without identical-state negatives.'}
(OUT/'no_self_summary.json').write_text(json.dumps(summary,indent=2)+'\n')
print(json.dumps(summary,indent=2))
