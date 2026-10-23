from pathlib import Path
import json
import numpy as np
import check_nonidentity as source

ROOT=Path(__file__).resolve().parent
source.qfun=lambda f:source.base.copy()
original=json.loads((ROOT/'nonidentity_summary.json').read_text())['trajectories']
rows=[]
for K in [8,32]:
    for seed in [7301,7401]:
        row=source.run(K,seed);f=np.array(row['embedding'])
        means=f.reshape(source.C,source.V,source.D).mean(axis=1)
        ETF=np.eye(source.C)-(np.ones((source.C,source.C))-np.eye(source.C))/(source.C-1)
        row['ETF_Gram_error']=float(np.linalg.norm(means@means.T-ETF)/np.linalg.norm(ETF))
        distances=np.linalg.norm(f[:,None,:]-f[None,:,:],axis=2)
        distances[~source.mask]=np.inf
        row['class_ID_robust_radius']=float(distances.min()/2)
        previous=next(x for x in original if x['K']==K and x['seed']==seed)
        af=np.array(previous['embedding']);ad=np.linalg.norm(af[:,None,:]-af[None,:,:],axis=2)
        ad[~source.mask]=np.inf
        row['paired_adaptive_radius']=float(ad.min()/2)
        rows.append(row)
result={'policy':'fixed uniform over other classes, same starts/caps/positive channel',
        'positive_self_probability':0,'negative_same_class_probability':0,
        'rows':rows,'max_Gram_error':max(x['ETF_Gram_error'] for x in rows),
        'scope':'paired multiview finite model; no unseen-data claim'}
(ROOT/'nonidentity_uniform_summary.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'max_Gram_error':result['max_Gram_error'],
                  'radii':[x['class_ID_robust_radius'] for x in rows],
                  'paired_adaptive_radii':[x['paired_adaptive_radius'] for x in rows]},indent=2))
