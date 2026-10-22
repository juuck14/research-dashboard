from pathlib import Path
from itertools import product
import sys,json,csv,numpy as np
from scipy.linalg import null_space
from oracle import field,policy
ROOT=Path(__file__).resolve().parent;OUT=ROOT/'results'
sys.path.insert(0,str(ROOT.parents[1]/'round2'/'theory'/'code'))
from verify_controls import moments
BITS=np.array(list(product([-1.,1.],repeat=2)))

def reference(m,d=8):return np.repeat(np.pad(BITS/np.sqrt(2),((0,0),(0,d-2))),m,axis=0)
def positive(m):return np.kron(np.eye(4),np.ones((m,m))/m)
def tangent(f):
    n,d=f.shape;T=np.zeros((n*d,n*(d-1)))
    for i,row in enumerate(f):
        b=np.zeros((d,d-1));b[:2,0]=[-row[1],row[0]];b[2:,1:]=np.eye(d-2)
        T[i*d:(i+1)*d,i*(d-1):(i+1)*(d-1)]=b
    return T
def jacobian(f,P,K,q=None,h=3e-6):
    T=tangent(f);dim=T.shape[1];H=np.empty((dim,dim))
    for j in range(dim):
        z=T[:,j].reshape(f.shape)
        df=(field(f+h*z,P,K,q)-field(f-h*z,P,K,q))/(2*h)
        H[:,j]=T.T@df.ravel()
    return H,T
def projection(m,d=8):
    U=np.kron(np.eye(4),np.ones((m,1))/np.sqrt(m))
    V=np.kron(np.eye(4),null_space(np.ones((1,m))))
    return np.kron(U,np.eye(d-1)),np.kron(V,np.eye(d-1))
def main():
    rows=[]
    for m in [2,4]:
        f=reference(m);P=positive(m);C,V=projection(m)
        for K in [1,2,4,5,8,16]:
            mom=moments(K,'natural',1)
            for policy_name in ['frozen','adaptive']:
                q=policy(f) if policy_name=='frozen' else None
                H,T=jacobian(f,P,K,q)
                ev=np.linalg.eigvalsh((H+H.T)/2)
                ec=np.linalg.eigvalsh(C.T@H@C);ew=np.linalg.eigvalsh(V.T@H@V)
                expected=np.sort([mom[policy_name+'_balance']]+[mom[policy_name+'_ab']]*2+[mom['normal_one']]*6+[mom['normal_ab']]*6+[0]*13)/m
                wc_nonzero=np.unique(np.round(ew,10))
                rows.append({'m':m,'N':len(f),'K':K,'policy':policy_name,'stationary_residual':float(np.max(np.abs(field(f,P,K,q)))),
                             'symmetry_error':float(np.max(np.abs(H-H.T))),'mean_spectrum_error':float(np.max(np.abs(ec-expected))),
                             'cross_block_error':float(np.max(np.abs(C.T@H@V))),'within_min':float(ew.min()),'within_max':float(ew.max()),
                             'within_unique':';'.join(map(str,wc_nonzero)),'full_negative_count':int(np.sum(ev< -1e-7)),
                             'full_zero_count':int(np.sum(np.abs(ev)<1e-7)),'full_min':float(ev.min())})
    with (OUT/'view_spectrum.csv').open('w') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
    summary={'settings':len(rows),'max_mean_spectrum_error':max(r['mean_spectrum_error'] for r in rows),
             'max_cross_block_error':max(r['cross_block_error'] for r in rows),'max_symmetry_error':max(r['symmetry_error'] for r in rows),
             'min_within_mode':min(r['within_min'] for r in rows),'rows':rows}
    (OUT/'view_spectrum.json').write_text(json.dumps(summary,indent=2)+'\n')
    print(json.dumps({k:v for k,v in summary.items() if k!='rows'},indent=2))
    assert summary['max_mean_spectrum_error']<1e-7

if __name__=='__main__':main()
