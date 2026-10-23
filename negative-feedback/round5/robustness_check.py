"""Read saved embeddings; compute exact distances and decoder-independent bounds."""
from pathlib import Path
import csv,json
import numpy as np
from scipy.special import ndtr

ROOT=Path(__file__).resolve().parent
DATA=ROOT/'global_mechanism'
adaptive=json.loads((DATA/'collapse_embeddings.json').read_text())
uniform=json.loads((DATA/'uniform_embeddings.json').read_text())

def radius(f):
    distances=np.linalg.norm(f[:,None,:]-f[None,:,:],axis=2)
    np.fill_diagonal(distances,np.inf)
    return float(distances.min()/2)

def fit_two(f):
    u=np.linalg.svd(f,full_matrices=False)[2][0]
    for _ in range(8):
        signs=np.where(f@u>=0,1.,-1.)
        u=np.mean(signs[:,None]*f,axis=0);u/=np.linalg.norm(u)
    signs=np.where(f@u>=0,1.,-1.)
    assert set(signs)=={-1.,1.}
    delta=float(np.sqrt(np.mean(np.sum((f-signs[:,None]*u)**2,axis=1))))
    return delta

rows=[]
for key,value in adaptive.items():
    C,K,seed,arm=key.split('/');C=int(C)
    f=np.array(value['embedding']);u=np.array(uniform[f'{C}/{K}/{seed}'])
    r=radius(f);ru=radius(u);delta=fit_two(f)
    assert abs(np.linalg.norm(f,axis=1)-1).max()<1e-12
    for sigma in [.05,.1,.25]:
        upper=min(1.,2/C+delta/(2*sigma))
        lower=max(0.,1-(C-1)*float(ndtr(-ru/sigma)))
        rows.append({'C':C,'K':int(K),'seed':int(seed),'arm':arm,'sigma':sigma,
                     'adaptive_radius':r,'uniform_radius':ru,
                     'simplex_optimal_radius':float(np.sqrt(C/(2*(C-1)))),
                     'adaptive_two_value_rms':delta,
                     'adaptive_Bayes_accuracy_upper':upper,
                     'uniform_NN_accuracy_lower':lower,'certified_accuracy_gap':lower-upper})
summary={'rows':rows,'minimum_accuracy_gap':min(x['certified_accuracy_gap'] for x in rows),
         'maximum_adaptive_radius':max(x['adaptive_radius'] for x in rows),
         'minimum_uniform_radius':min(x['uniform_radius'] for x in rows),
         'maximum_two_value_rms':max(x['adaptive_two_value_rms'] for x in rows),
         'scope':'deterministic geometric measurements and analytical bounds on saved finite-time embeddings; no exact finite-time information-erasure claim or Monte Carlo accuracy estimate'}
assert summary['minimum_accuracy_gap']>.49
with (ROOT/'robustness_rows.csv').open('w') as f:
    writer=csv.DictWriter(f,fieldnames=list(rows[0]));writer.writeheader();writer.writerows(rows)
(ROOT/'robustness_summary.json').write_text(json.dumps(summary,indent=2)+'\n')
print(json.dumps({k:v for k,v in summary.items() if k!='rows'},indent=2))
