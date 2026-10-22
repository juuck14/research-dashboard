"""Post-result independent audit, does not rerun or mutate root's training.
OPENBLAS_NUM_THREADS=1 python review/robustness-extension/independent_check.py
"""
from pathlib import Path
import ast,hashlib,json,itertools
import numpy as np
from scipy.special import expit,softmax,logsumexp

HERE=Path(__file__).resolve().parent
source=(HERE/'run_checks.py').read_text()
tree=ast.parse(source)
names={'norm','qfun','positive','exactfield','evaluate'}
defs=ast.Module(body=[n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name in names],type_ignores=[])
BITS=np.array(list(itertools.product([-1.,1.],repeat=2)))
BASE=np.pad(BITS/np.sqrt(2),((0,0),(0,2)))
env={'np':np,'EPS':.1,'KAPPA':-2.,'BITS':BITS,'expit':expit,'softmax':softmax,'logsumexp':logsumexp}
exec(compile(ast.fix_missing_locations(defs),'<audited root functions>','exec'),env)
norm=env['norm'];Q0=env['qfun'](BASE)

def scalar_loss(z,q,t):
    z=z/np.linalg.norm(z,axis=1)[:,None]
    value=0.
    for i,p,j in itertools.product(range(4),repeat=3):
        delta=float(z[i]@z[j]-z[i]@z[p])
        value+=t[i,p]*q[i,j]*np.logaddexp(0.,delta)/4
    return float(value)

maxerr=0.;nchecks=0;channel_error=0.;expected_sgd_error=0.
for eta in [0.,.01,.1]:
    T=env['positive'](eta)
    exact=np.sort([1.,1-2*eta,1-2*eta,(1-2*eta)**2])
    channel_error=max(channel_error,float(np.max(abs(np.linalg.eigvalsh(T)-exact))))
    for seed in [77,2011,4027]:
        F=norm(np.random.default_rng(seed).normal(size=(4,4)))
        for q in [np.full((4,4),.25),Q0,env['qfun'](F)]:
            V=env['exactfield'](F,q,T)
            finite=np.empty_like(F)
            for index in np.ndindex(F.shape):
                E=np.zeros_like(F);E[index]=1e-6
                finite[index]=(scalar_loss(F+E,q,T)-scalar_loss(F-E,q,T))/2e-6
                nchecks+=1
            maxerr=max(maxerr,float(np.max(abs(finite+V))))
            if eta==0.:
                counts=q/4
                C=counts*expit(F@F.T-1)
                G=(C+C.T)@F
                G-=np.sum(G*F,axis=1)[:,None]*F
                expected_sgd_error=max(expected_sgd_error,float(np.max(abs(G+V))))
assert maxerr<1e-7,maxerr
assert channel_error<1e-12,channel_error
assert expected_sgd_error<1e-12,expected_sgd_error

square=env['evaluate'](BASE)
onefactor=np.zeros((4,4));onefactor[:,0]=BITS[:,0]
collapsed=env['evaluate'](onefactor)
assert min(square[0])>.99,square
assert abs(collapsed[0][1]-.5)<.02,collapsed
assert collapsed[0][0]>.99,collapsed
summary={'audit_type':'post-result independent scalar finite-difference and exact evaluation-rule audit',
         'root_source_sha256':hashlib.sha256(source.encode()).hexdigest(),'coordinate_checks':nchecks,
         'max_detached_population_gradient_error':maxerr,'positive_channel_eigenvalue_error':channel_error,
         'expected_sampled_gradient_error':expected_sgd_error,
         'square_evaluation':{'factor_accuracy':square[0],'min_pair_distance':square[1]},
         'onefactor_evaluation':{'factor_accuracy':collapsed[0],'min_pair_distance':collapsed[1]},
         'scope':'No final training vectors loaded; final SGD runs not independently rerun here. Gradient correctness and noisy Bayes classification rule verified.'}
(HERE/'results'/'independent_audit.json').write_text(json.dumps(summary,indent=2)+'\n')
print(json.dumps(summary,indent=2))
