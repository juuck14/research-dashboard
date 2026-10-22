"""Independent 8-state cosine and finite-difference audit (no owner check() calls)."""
from pathlib import Path
import importlib.util
import itertools
import json
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
REPO = ROOT.parents[2]
OUT = ROOT/'results'; OUT.mkdir(exist_ok=True)
xs = np.array(list(itertools.product([-1.,1.],repeat=3)))


def pairs(rhos):
    table = np.zeros((8,8))
    for i,x in enumerate(xs):
        for j,y in enumerate(xs):
            probability = 1/8
            for k in range(3):
                probability *= (1+rhos[k]*x[k]*y[k])/2
            table[i,j] = probability
    return table


def unit(x):
    return x/np.linalg.norm(x,axis=1,keepdims=True)


def lookup_loss(f,t,pred,p):
    return 2-2*np.einsum('ij,ik,jk->',p,unit(f@pred),unit(t))


flat=[]
for a in [0.,.001,.1,.5,.9]:
    v=np.array([np.sqrt((1-a*a)/2),np.sqrt((1-a*a)/2),a])
    f=xs*v;p=pairs([.9,.9,.9]); t=f.copy();pred=np.eye(3)
    derivatives=[];h=1e-5
    for arr in [f,pred]:
        for ind in np.ndindex(arr.shape):
            old=arr[ind];arr[ind]=old+h;lp=lookup_loss(f,t,pred,p)
            arr[ind]=old-h;lm=lookup_loss(f,t,pred,p);arr[ind]=old
            derivatives.append((lp-lm)/(2*h))
    flat.append({'a':a,'loss':float(lookup_loss(f,t,pred,p)),
                 'max_finite_gradient':float(np.max(np.abs(derivatives)))})


def parameter_flow(z,rho3,predscale,beta=.01):
    a,b=z
    first=np.sqrt((1-a*a)/2)
    tf=np.sqrt((1-b*b)/2)
    f=xs*np.array([first,first,a])
    teacher=xs*np.array([tf,tf,b])
    df=xs*np.array([-a/(2*first),-a/(2*first),1.])
    pred=np.diag([1.,1.,predscale]);q=f@pred;dq=df@pred
    qnorm=np.linalg.norm(q,axis=1,keepdims=True)
    du=dq/qnorm-q*np.sum(q*dq,axis=1,keepdims=True)/qnorm**3
    da=2*np.einsum('ij,ik,jk->',pairs([.9,.9,rho3]),du,teacher)
    return np.array([da,beta*(a-b)])


tangent=[]
for rho3 in [.8,.9,1.]:
    for predscale in [.8,1.,1.2]:
        expected=np.array([[-1.8*predscale**2,2*rho3*predscale],[.01,-.01]])
        for h in [1e-3,1e-4,1e-5]:
            j=np.column_stack([(parameter_flow(h*np.eye(2)[k],rho3,predscale)-
                                parameter_flow(-h*np.eye(2)[k],rho3,predscale))/(2*h)
                               for k in range(2)])
            tangent.append({'rho3':rho3,'predictor_unused_scale':predscale,'h':h,
                            'max_jacobian_error':float(np.max(np.abs(j-expected))),
                            'lambda_max':float(np.max(np.linalg.eigvals(j).real))})

module_path=REPO/'ssl-recovery/code/run_population.py'
spec=importlib.util.spec_from_file_location('candidate_recovery',module_path)
owner=importlib.util.module_from_spec(spec);spec.loader.exec_module(owner)


def independent_loss(theta,teacher,p):
    f=np.tanh(xs@theta['w1'])@theta['w2']
    target=np.tanh(xs@teacher['w1'])@teacher['w2']
    # Match the specified epsilon, independently of owner's norm/loss functions.
    q=f@theta['pred'];q=q/np.sqrt(np.sum(q*q,axis=1,keepdims=True)+1e-12)
    t=target/np.sqrt(np.sum(target*target,axis=1,keepdims=True)+1e-12)
    return 2-2*np.sum((q@t.T)*p)


gradient=[]
for seed in [901,902,903]:
    rng=np.random.default_rng(seed)
    theta={'w1':rng.normal(size=(3,12))*.5,'w2':rng.normal(size=(12,3))*.3,
           'pred':np.eye(3)+rng.normal(size=(3,3))*.1}
    teacher={'w1':rng.normal(size=(3,12))*.5,'w2':rng.normal(size=(12,3))*.3}
    for rho in [[.9,.9,0],[.9,.9,.9],[.8,.9,1.]]:
        p=pairs(rho);loss,g=owner.loss_grad(theta,teacher,p);err=[]
        for k,arr in theta.items():
            for ind in np.ndindex(arr.shape):
                old=arr[ind];h=1e-5
                arr[ind]=old+h;lp=independent_loss(theta,teacher,p)
                arr[ind]=old-h;lm=independent_loss(theta,teacher,p);arr[ind]=old
                err.append(abs((lp-lm)/(2*h)-g[k][ind]))
        gradient.append({'seed':seed,'rho':rho,'loss_difference':abs(loss-independent_loss(theta,teacher,p)),
                         'max_absolute_gradient_error':float(max(err)),
                         'marginal_max_error':float(np.max(np.abs(p.sum(0)-1/8))),
                         'cross_moment_max_error':float(np.max(np.abs(xs.T@p@xs-np.diag(rho))))})

out={'flat_family':flat,'tangent_checks':tangent,'independent_backprop_checks':gradient,
     'scope':'Exact finite-state objective and isolated teacher/predictor tangent only; not full checkpoint dynamics.'}
(OUT/'spectral_audit.json').write_text(json.dumps(out,indent=2)+'\n')
assert max(r['max_finite_gradient'] for r in flat)<1e-8
assert max(abs(r['loss']-.2) for r in flat)<1e-12
assert max(r['max_jacobian_error'] for r in tangent)<3e-6
assert max(r['max_absolute_gradient_error'] for r in gradient)<1e-6
print(json.dumps({'flat_gradient_max':max(r['max_finite_gradient'] for r in flat),
                  'tangent_error_max':max(r['max_jacobian_error'] for r in tangent),
                  'backprop_error_max':max(r['max_absolute_gradient_error'] for r in gradient)},indent=2))
