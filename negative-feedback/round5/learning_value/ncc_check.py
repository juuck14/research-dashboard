"""Post-result counterhypothesis: four-way class-ID nearest centroid."""
from pathlib import Path
import csv,json,numpy as np
from evaluate import ROOT,REPO,C,M,N,supports

old=json.loads((REPO/'negative-feedback/round4/nonoracle/results/embeddings.json').read_text())
rows=[]
for key,item in old.items():
    if not key.endswith('/base'):continue
    F=np.array(item['embedding'])
    for k in [1,2]:
        S,T=supports(k)
        prototypes=F[S].reshape(len(S),C,k,-1).mean(axis=2)
        test=F[T]
        distance=((test[:,:,None,:]-prototypes[:,None,:,:])**2).sum(axis=3)
        minimum=distance.min(axis=2,keepdims=True)
        ties=np.abs(distance-minimum)<=1e-10
        labels=T//M
        prob=np.take_along_axis(ties,labels[:,:,None],axis=2)[:,:,0]/ties.sum(axis=2)
        acc=prob.mean(axis=1)
        rows.append({'representation':key,'labels_per_class':k,'support_sets':len(S),
                     'mean_class_accuracy':float(acc.mean()),'minimum_support_accuracy':float(acc.min()),
                     'support_accuracy_std':float(acc.std())})
with (ROOT/'results/ncc_class_id.csv').open('w') as f:
    w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
summary={'post_result_counterhypothesis':True,'target':'four-way class ID, nearest support centroid',
         'tie_band':1e-10,'rows':rows,
         'scope':'a different natural target/readout, not a replacement for the frozen primary binary-transfer protocol'}
(ROOT/'results/ncc_summary.json').write_text(json.dumps(summary,indent=2)+'\n')
print(json.dumps(summary,indent=2))
