from pathlib import Path
import json,csv,numpy as np

ROOT=Path(__file__).resolve().parent
GLOBAL=ROOT.parent/'global_mechanism'

def radius(F,labels):
    delta=F[:,None,:]-F[None,:,:]
    distance=np.linalg.norm(delta,axis=2)
    distance[labels[:,None]==labels[None,:]]=np.inf
    return float(distance.min()/2)

rows=[]
adaptive=json.loads((GLOBAL/'collapse_embeddings.json').read_text())
uniform=json.loads((GLOBAL/'uniform_embeddings.json').read_text())
for name,entry in adaptive.items():
    C,K,seed,arm=name.split('/')
    if arm!='base':continue
    C=int(C);F=np.array(entry['embedding']);r=radius(F,np.arange(C))
    comp=np.array(uniform[f'{C}/{K}/{seed}']);u=radius(comp,np.arange(C))
    optimum=np.sqrt(C/(2*(C-1)))
    rows.append({'setting':'identity_prototype','C':C,'K':int(K),'seed':int(seed),
                 'adaptive_radius':r,'uniform_radius':u,'unit_norm_optimal_radius':float(optimum),
                 'uniform_to_optimal_ratio':float(u/optimum),
                 'adaptive_to_optimal_ratio':float(r/optimum)})
multi=json.loads((GLOBAL/'nonidentity_summary.json').read_text())['trajectories']
other=json.loads((GLOBAL/'nonidentity_uniform_summary.json').read_text())['rows']
for row in multi:
    F=np.array(row['embedding']);labels=np.repeat(np.arange(4),2)
    matched=next(x for x in other if x['K']==row['K'] and x['seed']==row['seed'])
    u=radius(np.array(matched['embedding']),labels);r=radius(F,labels);opt=np.sqrt(2/3)
    rows.append({'setting':'two_distinct_positive_views','C':4,'K':row['K'],'seed':row['seed'],
                 'adaptive_radius':r,'uniform_radius':u,'unit_norm_optimal_radius':float(opt),
                 'uniform_to_optimal_ratio':float(u/opt),'adaptive_to_optimal_ratio':float(r/opt)})
with (ROOT/'results/newrepair_radii.csv').open('w') as f:
    w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
summary={'audited_paired_endpoints':len(rows),
         'max_adaptive_radius':max(r['adaptive_radius'] for r in rows),
         'min_uniform_to_optimal_ratio':min(r['uniform_to_optimal_ratio'] for r in rows),
         'finite_time_information_claim':'none; exact erasure refers only to proved limiting coarse representation',
         'data_source':'parent-completed fixed configurations; no newly trained models',
         'scope':'independent metric computation and task-meaning audit, not a new mathematical or publication novelty result'}
(ROOT/'results/newrepair_summary.json').write_text(json.dumps(summary,indent=2)+'\n')
print(json.dumps(summary,indent=2))
