from pathlib import Path
from itertools import permutations
import json,sys,numpy as np
ROOT=Path(__file__).resolve().parent;REPO=ROOT.parents[2]
sys.path.insert(0,str(REPO/'negative-feedback/round3/neural'))
from oracle import field,policy,normalize,loss_gradient
M=4;N=16;D=16;P=.95*np.eye(N)+.05*np.kron(np.eye(4),np.ones((M,M))/M)
rng=np.random.default_rng(6001);f=normalize(rng.normal(size=(N,D)));q=policy(f)
errors=[];value_errors=[]
for K in [4,8,16]:
 for mode in ['frozen','adaptive']:
  oldq=q if mode=='frozen' else None;g=field(f,P,K,oldq,L=64);value=loss_gradient(f,P,K,oldq,L=64)[0]
  for perm in permutations(range(4)):
   order=np.concatenate([np.arange(c*M,(c+1)*M) for c in perm]);newq=q[order][:,order] if mode=='frozen' else None
   h=field(f[order],P,K,newq,L=64);v=loss_gradient(f[order],P,K,newq,L=64)[0]
   errors.append(float(np.max(np.abs(h-g[order]))));value_errors.append(float(abs(value-v)))
bits=np.array([[-1.,-1.],[-1.,1.],[1.,-1.],[1.,1.]])
labels=np.column_stack([bits,np.prod(bits,axis=1)])
squares=[]
for matching,order in [(0,[0,3,1,2]),(1,[0,1,3,2]),(2,[0,1,2,3])]:
 v=bits[order]/np.sqrt(2);design=np.column_stack([np.ones(4),v]);coef=np.linalg.pinv(design)@labels
 residual=np.max(np.abs(design@coef-labels),axis=0)
 squares.append({'matching':matching,'coordinates':v.tolist(),'balanced_partitions':['a','b','ab'],
                 'affine_readout_max_residuals':residual.tolist(),
                 'linearly_separable':(residual<1e-12).tolist(),
                 'exact_factor_information_bits':[1,1,1],
                 'explanation':'four distinct class vertices permit exact nonlinear decoding; the remaining balanced partition is XOR and has optimal affine classifier accuracy3/4 at the exact reference'})
result={'posthoc_algebraic_diagnostic':True,'field_max_equivariance_error':max(errors),'value_max_equivariance_error':max(value_errors),
        'settings':len(errors),'squares':squares,'conditional_matching_probability': '1/3 each, if an equivariant deterministic algorithm with iid class-symmetric initialization reaches one of three square classes',
        'scope':'standard relabeling symmetry; not a new theorem of learning quality or a global convergence result'}
(ROOT/'results/symmetry_check.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
assert max(errors)<1e-12 and max(value_errors)<1e-12
assert all(sum(x['linearly_separable'])==2 for x in squares)
