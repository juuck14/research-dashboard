"""Prespecified reviewer-triggered scope attack under the new weak positive graph."""
from pathlib import Path
import json,csv,time,numpy as np
from model import *
from view_spectrum import positive
from oracle import policy
ROOT=Path(__file__).resolve().parent;OUT=ROOT/'results'
def flatten(g):return {k:v for k,v in g.items() if k not in ['mean_gram','mean_gram_eigenvalues']}
def main():
    x,bits,Q=dataset();P=.95*np.eye(16)+.05*positive(4);q_uniform=np.ones((len(x),len(x)))/len(x)
    rows=[];traces=[];initials=[];embeds={};start=time.time()
    for seed in [3801,3802,3901]:
        v=random(seed)
        for step in range(1000):
            loss,g=value_gradient(v,x,P,4,q_uniform);v-=.05*g
            if step in [0,99,499,999]:
                geom=geometry(forward(x,v)[0]);traces.append({'seed':seed,'K':4,'policy':'warmup_uniform','step':step+1,'loss':loss,**flatten(geom)})
        f0,_=forward(x,v);geom=geometry(f0);q0=policy(f0)
        gradients={K:float(np.linalg.norm(value_gradient(v,x,P,K)[1])) for K in [4,8,16]}
        applicable=geom['square_gram_relative_error']<.001 and max(gradients.values())<1e-6
        initials.append({'seed':seed,'geometry':geom,'adaptive_gradient_norms':gradients,'square_threshold_applicable':bool(applicable)})
        embeds[f'{seed}/warmup']=f0.tolist()
        for K in [4,8,16]:
            for pol in ['frozen','adaptive']:
                w=v.copy();qf=q0 if pol=='frozen' else None
                for step in range(1000):
                    loss,g=value_gradient(w,x,P,K,qf);w-=.05*g
                    if step in [0,99,499,999]:
                        ge=geometry(forward(x,w)[0]);traces.append({'seed':seed,'K':K,'policy':pol,'step':step+1,'loss':loss,**flatten(ge)})
                f,_=forward(x,w);final=geometry(f);embeds[f'{seed}/{K}/{pol}']=f.tolist()
                row={'seed':seed,'split':'primary' if seed<3900 else 'confirmation','K':K,'policy':pol,'loss':loss,
                     'square_threshold_applicable':bool(applicable),**flatten(final)}
                rows.append(row);print(json.dumps(row),flush=True)
    for name,data in [('weak_ordinary_runs.csv',rows),('weak_ordinary_traces.csv',traces)]:
        with (OUT/name).open('w') as f:
            writer=csv.DictWriter(f,fieldnames=list(data[0]));writer.writeheader();writer.writerows(data)
    summary={'positive_channel':'.95I+.05U_class','status':'reviewer-triggered scope test, reused seeds; not held-out confirmation','runs':len(rows),'warmup_seeds':3,'initials':initials,'threshold_applicable_seeds':sum(r['square_threshold_applicable'] for r in initials),'elapsed_seconds':time.time()-start,'rows':rows}
    (OUT/'weak_ordinary_summary.json').write_text(json.dumps(summary,indent=2)+'\n');(OUT/'weak_ordinary_final_embeddings.json').write_text(json.dumps(embeds)+'\n')
    print(json.dumps({k:v for k,v in summary.items() if k!='rows'},indent=2))
if __name__=='__main__':main()
