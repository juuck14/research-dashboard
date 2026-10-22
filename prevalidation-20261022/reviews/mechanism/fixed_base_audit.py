"""Fixed-true-generator audit; protocol amendment 3."""
import itertools,json
from pathlib import Path
import numpy as np
c=2**-.5
R=np.array([[c,-c],[c,c]])
A6=np.array([[1.,0],[0,1],[c,c],[c,-c],[1,0],[0,1]])
A=np.vstack([A6,np.zeros((4,2))]);C=A@R

def score(M,U):
    rownorm=np.linalg.norm(M,axis=1)
    return int(np.sum(np.abs(M@U)>1e-11*rownorm[:,None]))

def enumerate_bases(M):
    dirs=[]
    for row in M:
        n=np.linalg.norm(row)
        if n==0:continue
        u=np.array([-row[1],row[0]])/n
        if not any(abs(u@v)>1-1e-12 for v in dirs):dirs.append(u)
    dirs += [np.array([np.cos(t),np.sin(t)]) for t in (.123,.456,.987,1.234)]
    vals=[]
    for u,v in itertools.combinations(dirs,2):
        U=np.column_stack([u,v])
        if abs(np.linalg.det(U))<1e-10:continue
        aligned=all(min(abs(x[0]),abs(x[1]))<1e-10 for x in (u,v))
        vals.append((score(M,U),aligned))
    return dict(minimum=min(x[0] for x in vals),nonaligned_minimum=min(x[0] for x in vals if not x[1]),
                all_optima_aligned=all(x[1] for x in vals if x[0]==min(t[0] for t in vals)))

rows=[]
for e in 10.**-np.arange(1,11):
    B=np.vstack([A6@R,e*np.eye(2),e*np.eye(2)])
    rows.append(dict(epsilon=float(e),candidate_reference_audit=enumerate_bases(B),
                     distance=float(np.linalg.norm(C-B,2)),predicted_distance=float(np.sqrt(2)*e),
                     svals=np.linalg.svd(B,compute_uv=False).tolist(),
                     predicted_sigma=float(np.sqrt(3+2*e*e)),
                     exact_same_observation_covariance_error=float(np.linalg.norm(A@A.T-C@C.T,2))))
out=dict(true_audit=enumerate_bases(A),true_svals=np.linalg.svd(A,compute_uv=False).tolist(),
         observation_dimension=10,true_reference_fixed=True,candidate_actual_fixed=True,rows=rows)
(Path(__file__).parent/'results'/'fixed_base_audit.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
