from pathlib import Path
import json,csv,time
import numpy as np
from check_collapse import normalize,field,geometry
ROOT=Path(__file__).resolve().parent

def robust_radius(f):
    distances=np.linalg.norm(f[:,None,:]-f[None,:,:],axis=2)
    np.fill_diagonal(distances,np.inf)
    return float(distances.min()/2)

def run(C,K,seed):
    start=time.monotonic();rng=np.random.default_rng(seed);f=normalize(rng.normal(size=(C,C)))
    P=np.eye(C);q=(np.ones((C,C))-np.eye(C))/(C-1);stop='cap';last=0
    for step in range(20000):
        g=field(f,P,K,q,L=64);norm=float(np.linalg.norm(g))
        if step>=100 and step%20==0 and norm<1e-8:
            stop='field_tolerance';last=step;break
        f=normalize(f-2*g);last=step+1
    g64=field(f,P,K,q,L=64);g96=field(f,P,K,q,L=96)
    ETF=np.eye(C)-(np.ones((C,C))-np.eye(C))/(C-1)
    row={'C':C,'K':K,'seed':seed,'split':'primary' if seed==7301 else 'confirmation',
         'policy':'uniform_off_diagonal_frozen','steps':last,'stop':stop,
         'field_norm':float(np.linalg.norm(g96)),'quadrature_difference':float(np.max(np.abs(g64-g96))),
         'ETF_Gram_relative_error':float(np.linalg.norm(f@f.T-ETF)/np.linalg.norm(ETF)),
         'class_ID_robust_radius':robust_radius(f),'optimal_ETF_radius':float(np.sqrt(C/(2*(C-1)))),
         'elapsed_seconds':time.monotonic()-start}
    return row,f

def main():
    rows=[];embeddings={};adaptive=json.loads((ROOT/'collapse_summary.json').read_text())['rows']
    af=json.loads((ROOT/'collapse_embeddings.json').read_text())
    for C in [4,8]:
        for K in [1,8,32]:
            for seed in [7301,7401]:
                row,f=run(C,K,seed);rows.append(row);embeddings[f'{C}/{K}/{seed}']=f.tolist()
                a=next(x for x in adaptive if x['C']==C and x['K']==K and x['seed']==seed and x['arm']=='base')
                af_state=np.array(af[f'{C}/{K}/{seed}/base']['embedding'])
                row['paired_adaptive_radius']=robust_radius(af_state)
                row['paired_adaptive_antipodal_RMS']=a['rank1_antipodal_rms']
                print(json.dumps(row),flush=True)
    with (ROOT/'uniform_control.csv').open('w') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
    (ROOT/'uniform_embeddings.json').write_text(json.dumps(embeddings)+'\n')
    result={'rows':rows,'runs':len(rows),'maximum_Gram_error':max(r['ETF_Gram_relative_error'] for r in rows),
            'maximum_quadrature_difference':max(r['quadrature_difference'] for r in rows),
            'scope':'same starts and exact ETF-matched frozen law; task-neutral robust radius, not finite-time noiseless erasure'}
    (ROOT/'uniform_summary.json').write_text(json.dumps(result,indent=2)+'\n')
    assert result['maximum_quadrature_difference']<1e-6
if __name__=='__main__':main()
