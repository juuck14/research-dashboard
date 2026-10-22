"""Amendment1 neural controls. Original pilot/confirmation are untouched."""
import copy,json,pathlib,time
import numpy as np
from run_population import initialize,state,train,law,ROOT
start=time.time();rows=[];summary=[]
for seed in [0,1,2,3,101,102,103,104]:
    theta=initialize(seed);s0=state(theta);train(s0,law((.9,.9,0)),1500)
    for rho3 in [.8,1.]:
        s=copy.deepcopy(s0);tr,_=train(s,law((.9,.9,rho3)),15000)
        rows += [dict(seed=seed,rho3=rho3,policy='continue',**r) for r in tr]
        summary.append(dict(seed=seed,rho3=rho3,policy='continue',r2_3000=[r for r in tr if r['step']==3000][0]['f_r2_3'],r2_15000=tr[-1]['f_r2_3'],all_r2_final=[tr[-1][f'f_r2_{j}'] for j in [1,2,3]]))
    s=copy.deepcopy(s0);s['theta']['pred']=theta['pred'].copy();s['m']['pred']*=0;s['v']['pred']*=0;s['tblocks']={k:s['step'] for k in s['theta']};s['tblocks']['pred']=0
    tr,_=train(s,law((.9,.9,.9)),3000)
    rows += [dict(seed=seed,rho3=.9,policy='predictor_and_moments',**r) for r in tr]
    summary.append(dict(seed=seed,rho3=.9,policy='predictor_and_moments',r2_3000=tr[-1]['f_r2_3']))
    print(json.dumps(summary[-3:]),flush=True)
(ROOT/'results/spectral_summary.json').write_text(json.dumps(dict(seconds=time.time()-start,summary=summary),indent=2))
from trace_storage import store_traces
store_traces('spectral',rows)
