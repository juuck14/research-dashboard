"""Pure-anchor count versus amplitude-weighted surrogate, protocol amendment 4."""
import itertools,json
from pathlib import Path
import numpy as np
c=2**-.5;tt=np.linspace(0,np.pi/4,10001)
Rs=np.array([[np.cos(tt),-np.sin(tt)],[np.sin(tt),np.cos(tt)]]).transpose(2,0,1)

def sparse_score(M):
    dirs=[]
    for r in M:
        u=np.array([-r[1],r[0]])/np.linalg.norm(r)
        if not any(abs(u@v)>1-1e-12 for v in dirs):dirs.append(u)
    vals=[]
    for u,v in itertools.combinations(dirs,2):
        U=np.column_stack([u,v])
        if abs(np.linalg.det(U))<1e-10:continue
        l0=int(np.sum(np.abs(M@U)>1e-11*np.linalg.norm(M,axis=1,keepdims=True)))
        aligned=all(min(abs(x[0]),abs(x[1]))<1e-10 for x in (u,v))
        vals.append((l0,aligned))
    return min(x[0] for x in vals),min(x[0] for x in vals if not x[1])

rows=[]
for p in (2,3,5):
    for w in (1.,2.,3.):
        A=np.vstack([np.tile([1.,0],(p,1)),np.tile([0,1.],(p,1)),w*np.array([[c,c],[c,-c]])])
        C=np.einsum('ij,njk->nik',A,Rs)
        direct=np.abs(C[:,:,0]*C[:,:,1]).sum(1)
        formula=p*np.abs(np.sin(2*tt))+w*w*np.abs(np.cos(2*tt))
        minimum,nonalign=sparse_score(A)
        rows.append(dict(p=p,q=2,w=w,support_overlap=2/(p+2),min_row_norm=float(np.min(np.linalg.norm(A,axis=1))),
                         Gram_error=float(np.linalg.norm(A.T@A-(p+w*w)*np.eye(2),2)),
                         true_l0=minimum,nonaligned_l0=nonalign,predicted_l0=2*p+4,predicted_nonaligned_l0=3*p+3,
                         true_surrogate=float(direct[0]),wrong_surrogate=float(direct[-1]),
                         normalized_true=float(direct[0]/(p+w*w)),normalized_wrong=float(direct[-1]/(p+w*w)),
                         grid_min=float(direct.min()),predicted_rotation_min=float(min(p,w*w)),
                         true_is_worse=bool(w*w>p),formula_error=float(np.max(np.abs(direct-formula)))))
(Path(__file__).parent/'results'/'weighted_surrogate_audit.json').write_text(json.dumps(rows,indent=2)+'\n')
print(json.dumps(rows,indent=2))
