"""Amendment3: extend all original equal-spectrum continuations uniformly."""
import json,time
from run_population import ROOT,initialize,state,train,law
from trace_storage import store_traces
start=time.time();rows=[];summary=[]
for seed in [0,1,2,3,101,102,103,104]:
 s=state(initialize(seed));train(s,law((.9,.9,0)),1500);tr,_=train(s,law((.9,.9,.9)),15000)
 rows +=[dict(seed=seed,policy='continue_equal_long',**r) for r in tr]
 summary.append(dict(seed=seed,r2_3000=[r for r in tr if r['step']==3000][0]['f_r2_3'],r2_15000=tr[-1]['f_r2_3'],all_r2_final=[tr[-1][f'f_r2_{j}'] for j in [1,2,3]]));print(json.dumps(summary[-1]),flush=True)
(ROOT/'results/long_equal_summary.json').write_text(json.dumps(dict(seconds=time.time()-start,summary=summary),indent=2));store_traces('long_equal',rows)
