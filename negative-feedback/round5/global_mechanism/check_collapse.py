from pathlib import Path
import sys,json,csv,time
import numpy as np
from scipy.stats import binom
ROOT=Path(__file__).resolve().parent
REPO=ROOT.parents[2]
sys.path.insert(0,str(REPO/'negative-feedback/round3/neural'))
from oracle import field,normalize

EPS=.05;T=np.log(4.);B=np.exp(-2.)

def qfun(f):
    C=len(f);s=f@f.T;w=np.exp(-T*s);np.fill_diagonal(w,0)
    base=(np.ones((C,C))-np.eye(C))/(C-1)
    return EPS*base+(1-EPS)*w/w.sum(axis=1,keepdims=True)

def moments(C,K):
    m=C//2;R=np.exp(2*T)
    p=EPS*m/(C-1)+(1-EPS)*m*R/((m-1)+m*R)
    W=np.arange(K+1);pr=binom.pmf(W,K,p);U=K-W;D=1+U+B*W
    As=float(pr@(U/D));Ao=float(B*(pr@(W/D)))
    return p,As,Ao

def fd_check(K,frozen):
    C=4;d=4;f=np.zeros((C,d));f[:2,0]=1;f[2:,0]=-1
    q0=qfun(f);P=np.eye(C);J=np.zeros((C*(d-1),)*2);h=1e-5
    for j in range(J.shape[1]):
        v=np.zeros_like(f);i,k=divmod(j,d-1);v[i,k+1]=h
        fp=normalize(f+v);fm=normalize(f-v)
        gp=field(fp,P,K,q0 if frozen else qfun(fp),L=96)
        gm=field(fm,P,K,q0 if frozen else qfun(fm),L=96)
        J[:,j]=((gp-gm)/(2*h))[:,1:].ravel()
    ev=np.linalg.eigvalsh((J+J.T)/2);p,As,Ao=moments(C,K);m=C//2
    pred=np.sort(np.array([0]*(d-1)+[2*Ao/m]*(d-1)+[(Ao-m*As/(m-1))/m]*((C-2)*(d-1))))
    return {'C':C,'K':K,'frozen':frozen,'opposite_mass':p,
            'max_eigenvalue_error':float(np.max(np.abs(ev-pred))),
            'min_nonrotation_eigenvalue':float(ev[d-1]),
            'predicted_min_nonrotation':float(min(2*Ao/m,(Ao-m*As/(m-1))/m)),
            'antisymmetry':float(np.max(np.abs(J-J.T)))}

def geometry(f):
    _,_,vt=np.linalg.svd(f,full_matrices=False);u=vt[0]
    for _ in range(5):
        signs=np.where(f@u>=0,1.,-1.);u=(signs[:,None]*f).sum(axis=0);u/=np.linalg.norm(u)
    residual=float(np.mean(np.sum((f-signs[:,None]*u)**2,axis=1)))
    return {'rank1_antipodal_rms':float(np.sqrt(residual)),'positive_group':int(np.sum(signs>0)),
            'negative_group':int(np.sum(signs<0)),
            'top_eigenvalues':np.linalg.eigvalsh(f@f.T)[-3:].tolist()}

def run(C,K,seed,dt,steps,arm):
    start=time.monotonic();rng=np.random.default_rng(seed);f=normalize(rng.normal(size=(C,C)));P=np.eye(C)
    history=[];stop='cap';last=0
    for step in range(steps):
        q=qfun(f);g=field(f,P,K,q,L=64);norm=float(np.linalg.norm(g))
        if step in [0,99] or step%500==0:
            history.append({'C':C,'K':K,'seed':seed,'arm':arm,'step':step,'field_norm':norm,**geometry(f)})
        if step>=100 and step%20==0 and norm<1e-8:
            stop='field_tolerance';last=step;break
        f=normalize(f-dt*g);last=step+1
    q=qfun(f);g64=field(f,P,K,q,L=64);g96=field(f,P,K,q,L=96)
    geo=geometry(f)
    row={'C':C,'K':K,'seed':seed,'split':'primary' if seed==7301 else 'confirmation','arm':arm,
         'dt':dt,'steps':last,'stop':stop,'model_time':last*dt,
         'field_norm':float(np.linalg.norm(g96)),'quadrature_difference':float(np.max(np.abs(g64-g96))),
         **{k:v for k,v in geo.items() if k!='top_eigenvalues'},'elapsed_seconds':time.monotonic()-start}
    return row,history,{'embedding':f.tolist(),**geo}

def main():
    checks=[fd_check(K,frozen) for K in [1,8,32] for frozen in [False,True]]
    assert max(x['max_eigenvalue_error'] for x in checks)<1e-7
    assert min(x['min_nonrotation_eigenvalue'] for x in checks)>0
    (ROOT/'coarse_fd.json').write_text(json.dumps(checks,indent=2)+'\n')
    rows=[];traces=[];embeddings={};started=time.monotonic()
    configs=[(C,K,seed,2.,20000,'base') for C in [4,8] for K in [1,8,32] for seed in [7301,7401]]
    configs += [(8,32,7401,1.,40000,'halfstep')]
    for C,K,seed,dt,steps,arm in configs:
        row,trace,embedding=run(C,K,seed,dt,steps,arm);rows.append(row);traces+=trace
        embeddings[f'{C}/{K}/{seed}/{arm}']=embedding
        (ROOT/'collapse_progress.json').write_text(json.dumps(rows,indent=2)+'\n')
        print(json.dumps(row),flush=True)
    with (ROOT/'collapse_runs.csv').open('w') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
    with (ROOT/'collapse_traces.json').open('w') as f:json.dump(traces,f,indent=2)
    (ROOT/'collapse_embeddings.json').write_text(json.dumps(embeddings)+'\n')
    result={'epsilon':EPS,'t':T,'negatives':'exclude anchor prototype; no class collision',
            'runs':len(rows),'elapsed_seconds':time.monotonic()-started,'rows':rows,
            'max_quadrature_discrepancy':max(x['quadrature_difference'] for x in rows),
            'scope':'finite-model trajectories and exact local basin; finite small residual is not exact noiseless information loss'}
    (ROOT/'collapse_summary.json').write_text(json.dumps(result,indent=2)+'\n')
    assert result['max_quadrature_discrepancy']<1e-6

if __name__=='__main__':main()
