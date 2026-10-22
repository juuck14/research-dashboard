from pathlib import Path
import csv,json,numpy as np
from mixing import predicted,moments
from view_spectrum import reference,jacobian
ROOT=Path(__file__).resolve().parent;OUT=ROOT/'results'

def graph(kind,s):
    if kind=='cycle':
        A=np.array([[0,1,0,1],[1,0,1,0],[0,1,0,1],[1,0,1,0]],float);L=2*np.eye(4)-A
    else:
        A=np.array([[0,1,0,0],[1,0,1,0],[0,1,0,1],[0,0,1,0]],float);L=np.diag(A.sum(axis=1))-A
    return np.eye(4)-s*L/2
rows=[];f=reference(4)
for kind in ['cycle','path']:
    for scale in [.05,.2]:
        P0=graph(kind,scale);mu=np.linalg.eigvalsh(P0)[:-1]
        for K in [5,8,16]:
            mo=moments(K,'natural',1);r,ev=predicted(K,1)
            mass=r['negative_softmax_mass'];lp=mo['normal_one'];lb=mo['adaptive_balance']
            mean=np.sort([lb]+[mo['adaptive_ab']]*2+[lp]*6+[mo['normal_ab']]*6+[0]*13)/4
            view=[]
            for lam in mu:
                normal=(lp-.5*mass*lam)/4;plane=normal+lb/8
                view.extend([normal]*24+[plane]*4)
            expected=np.sort(np.concatenate([mean,view]));H,T=jacobian(f,np.kron(np.eye(4),P0),K)
            actual=np.linalg.eigvalsh((H+H.T)/2);error=float(np.max(abs(expected-actual)))
            rows.append({'graph':kind,'scale':scale,'K':K,'gap':float(1-mu.max()),'max_spectrum_error':error,
                         'negative_modes_actual':int(np.sum(actual< -1e-7)),'negative_modes_predicted':int(np.sum(expected< -1e-7))})
with (OUT/'graph_fd.csv').open('w') as f:
    wr=csv.DictWriter(f,fieldnames=list(rows[0]));wr.writeheader();wr.writerows(rows)
summary={'settings':len(rows),'max_spectrum_error':max(r['max_spectrum_error'] for r in rows),'rows':rows}
(OUT/'graph_summary.json').write_text(json.dumps(summary,indent=2)+'\n');print(json.dumps(summary,indent=2))
assert summary['max_spectrum_error']<1e-7
