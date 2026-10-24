"""New 2026-10-25 rerun after loss of unpublished raw files; see protocol.md."""
from pathlib import Path
import json,sys,time,platform
import numpy as np
from scipy.linalg import null_space
HERE=Path(__file__).resolve().parent
REPO=HERE.parents[2]
sys.path.insert(0,str(REPO/'negative-feedback/round3/neural'))
from oracle import normalize,field
EPS=.01;T=.9

def policy(F):
 C=len(F);w=np.exp(-T*(F@F.T));np.fill_diagonal(w,0)
 return EPS*(np.ones((C,C))-np.eye(C))/(C-1)+(1-EPS)*w/w.sum(1,keepdims=True)

def metrics(F):
 C=len(F);X=F@F.T;mask=~np.eye(C,dtype=bool);r=-1/(C-1)
 pair=np.linalg.norm(F[:,None]-F[None,:],axis=-1)
 u=np.linalg.svd(F,full_matrices=False)[2][0]
 for _ in range(5):
  a=np.where(F@u>=0,1.,-1.);u=(a[:,None]*F).sum(0);u/=np.linalg.norm(u)
 return {'off_Gram_MSE':float(np.mean((X[mask]-r)**2)),
         'robust_radius':float(np.min(pair[mask])/2),
         'coarse_RMS':float(np.sqrt(np.mean(np.sum((F-a[:,None]*u)**2,1)))),
         'group_sizes':[int(np.sum(a==1)),int(np.sum(a==-1))]}

def bounds(C,K):
 r=-1/(C-1);b=np.exp(-2);c=(1-np.exp(-.2))/2;M=(1+r)*(2-b)/(b*c)
 E=np.sqrt(C*(C-1)*M/(2*K))
 return {'M':float(M),'MSE_upper':float(M/K),
         'radius_lower':float(np.sqrt(max(0,1-r-E)/2)),
         'first_guaranteed_no_collision_K':int(np.floor(M*(C-1)**3/(2*C))+1)}

def full_fd(F,K):
 C,d=F.shape;bases=[null_space(F[i:i+1]) for i in range(C)]
 V=[]
 for i in range(C):
  for j in range(d-1):
   a=np.zeros_like(F);a[i]=bases[i][:,j];V.append(a)
 V=np.asarray(V);h=3e-6;J=np.zeros((len(V),len(V)));P=np.eye(C)
 for k,Z in enumerate(V):
  Fp=normalize(F+h*Z);Fm=normalize(F-h*Z)
  dg=(field(Fp,P,K,policy(Fp),L=96)-field(Fm,P,K,policy(Fm),L=96))/(2*h)
  J[:,k]=np.einsum('aij,ij->a',V,dg)
 ev=np.linalg.eigvals(J)
 return {'C':C,'K':K,'eigenvalues_real':np.sort(ev.real).tolist(),
         'max_imaginary':float(np.max(abs(ev.imag))),
         'negative_resolved_count':int(np.sum(ev.real < -1e-6)),
         'zero_count_at_1e-6':int(np.sum(abs(ev.real)<1e-6)),
         'minimum_resolved_positive':float(np.min(ev.real[ev.real>1e-6])),
         'tolerance':1e-6}

def run(C,K,seed,family):
 rng=np.random.default_rng(seed)
 if family=='Gaussian':F=normalize(rng.normal(size=(C,C)))
 else:
  F=np.zeros((C,C));F[:C//2,0]=1;F[C//2:,0]=-1
  F=normalize(F+.01*rng.normal(size=(C,C)))
 P=np.eye(C);history=[];start=time.monotonic();stop='cap'
 for step in range(20000):
  G=field(F,P,K,policy(F),L=64)
  if step%1000==0:history.append({'step':step,'field64':float(np.linalg.norm(G)),**metrics(F)})
  if step>=100 and step%20==0:
   if np.linalg.norm(G)<1e-8:
    G96=field(F,P,K,policy(F),L=96)
    if np.linalg.norm(G96)<1e-8:stop='field_tolerance';break
  F=normalize(F-2*G)
 G64=field(F,P,K,policy(F),L=64);G96=field(F,P,K,policy(F),L=96)
 row={'C':C,'K':K,'seed':seed,'initialization':family,'steps':step,'stop':stop,
      'field96':float(np.linalg.norm(G96)),
      'quadrature_difference':float(np.max(abs(G64-G96))),
      **metrics(F),'bounds':bounds(C,K),'embedding':F.tolist(),'snapshots':history,
      'elapsed_seconds':time.monotonic()-start}
 if C==6 and seed==7701 and family=='coarse_perturbed':row['full_spectrum']=full_fd(F,K)
 return row

def main():
 rows=[];started=time.monotonic()
 for C in [4,6]:
  for K in [1,4096]:
   for seed in [7701,7702]:
    for family in ['Gaussian','coarse_perturbed']:
     row=run(C,K,seed,family);rows.append(row)
     print(json.dumps({k:v for k,v in row.items() if k not in ['embedding','snapshots','full_spectrum']}),flush=True)
 result={'provenance':'New execution 2026-10-25 after original unpublished files were pruned; not recovered original bytes',
         'python':platform.python_version(),'numpy':np.__version__,'epsilon':EPS,'t':T,
         'rows':rows,'elapsed_seconds':time.monotonic()-started,
         'scope':'All-stable-equilibrium theorem checked with converged candidates; no global-convergence claim'}
 (HERE/'population_rerun.json').write_text(json.dumps(result,indent=2)+'\n')
 assert all(x['stop']=='field_tolerance' for x in rows)
 assert all(x['quadrature_difference']<1e-9 for x in rows)
 assert all(x['off_Gram_MSE']<=x['bounds']['MSE_upper']+1e-9 and x['robust_radius']>=x['bounds']['radius_lower']-1e-7 for x in rows if x['K']==4096)
 assert all(x['full_spectrum']['negative_resolved_count']==0 for x in rows if 'full_spectrum' in x)
 print(json.dumps({'all_declared_runs':len(rows),'all_converged':True,'elapsed_seconds':result['elapsed_seconds']}))
if __name__=='__main__':main()
