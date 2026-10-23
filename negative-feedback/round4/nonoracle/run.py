"""Fixed non-oracle scope test; see protocol before interpreting outputs."""
from pathlib import Path
import sys,json,csv,time,platform
import numpy as np
ROOT=Path(__file__).resolve().parent;REPO=ROOT.parents[2]
sys.path.insert(0,str(REPO/'negative-feedback/round3/neural'))
from oracle import field,loss_gradient,normalize,policy
OUT=ROOT/'results';OUT.mkdir(exist_ok=True)
M=4;N=16;D=16
P=.95*np.eye(N)+.05*np.kron(np.eye(4),np.ones((M,M))/M)
BITS=np.repeat(np.array([[-1.,-1.],[-1.,1.],[1.,-1.],[1.,1.]]),M,axis=0)
MATCHINGS=[[(0,1),(2,3)],[(0,2),(1,3)],[(0,3),(1,2)]]
TARGETS=[]
for matching in MATCHINGS:
    G=np.eye(4)
    for i,j in matching:G[i,j]=G[j,i]=-1
    TARGETS.append(G)

def metrics(f):
    means=f.reshape(4,M,D).mean(axis=1);gram=means@means.T
    errors=[np.linalg.norm(gram-G)/np.linalg.norm(G) for G in TARGETS]
    nuisance=float(np.mean(np.sum((f-np.repeat(means,M,axis=0))**2,axis=1)))
    sv=np.linalg.svd(f,compute_uv=False);w=np.linalg.pinv(f,rcond=1e-12)@BITS
    pred=f@w;pair=np.maximum(0,2-2*f@f.T);pair[np.diag_indices(N)]=np.inf
    return {'best_square_error':float(min(errors)),'best_matching':int(np.argmin(errors)),
            'view_variance':nuisance,'mean_eigenvalues':np.linalg.eigvalsh(gram).tolist(),
            'minimum_pair_distance':float(np.sqrt(pair.min())),
            'numeric_rank_rcond_1e12':int(np.sum(sv>sv[0]*1e-12)),
            'smallest_singular_value':float(sv[-1]),
            'factor_a_linear_accuracy':float(np.mean((pred[:,0]>0)==(BITS[:,0]>0))),
            'factor_b_linear_accuracy':float(np.mean((pred[:,1]>0)==(BITS[:,1]>0))),
            'factor_linear_max_residual':float(np.max(np.abs(pred-BITS))),
            'factor_readout_norm':float(np.linalg.norm(w)),
            'min_class_distance':float(np.sqrt(np.min(np.sum((means[:,None,:]-means[None,:,:])**2,axis=2)+np.eye(4)*100)))}

def flat(m):return {k:v for k,v in m.items() if k!='mean_eigenvalues'}

def run(seed,K,mode,dt,steps,arm):
    rng=np.random.default_rng(seed);f=normalize(rng.normal(size=(N,D)));q0=policy(f)
    q=q0 if mode=='frozen' else None
    history=[];start=time.monotonic();stop='cap';last_step=0
    for step in range(steps):
        g=field(f,P,K,q,L=64)
        norm=float(np.linalg.norm(g))
        if step in [0,99] or step%200==0:
            history.append({'seed':seed,'K':K,'policy':mode,'arm':arm,'step':step,'modeltime':step*dt,'field_norm':norm,**flat(metrics(f))})
        if step>=100 and step%20==0 and norm<1e-7:
            stop='stationary_tolerance';last_step=step;break
        f=normalize(f-dt*g);last_step=step+1
    g64=field(f,P,K,q,L=64);g96=field(f,P,K,q,L=96)
    value64=loss_gradient(f,P,K,q,L=64)[0];value96=loss_gradient(f,P,K,q,L=96)[0]
    m=metrics(f);full_norm=float(np.linalg.norm(g96));quaderr=float(np.max(np.abs(g64-g96)))
    applicable=m['best_square_error']<.001 and m['view_variance']<.001 and full_norm<1e-6
    row={'seed':seed,'split':'primary' if seed<6200 else 'confirmation','K':K,'policy':mode,'arm':arm,
         'dt':dt,'steps':last_step,'modeltime':last_step*dt,'stop':stop,'elapsed_seconds':time.monotonic()-start,
         'full_field_norm':full_norm,'max_row_field_norm':float(np.max(np.linalg.norm(g96,axis=1))),
         'quadrature_gradient_error':quaderr,'quadrature_value_error':float(abs(value64-value96)),
         'theorem_applicable':bool(applicable),**flat(m)}
    history.append({'seed':seed,'K':K,'policy':mode,'arm':arm,'step':last_step,'modeltime':last_step*dt,'field_norm':full_norm,**flat(m)})
    return row,history,{'embedding':f.tolist(),'class_mean_eigenvalues':m['mean_eigenvalues'],'initial_q':q0.tolist()}

def main():
    smoke=json.loads((OUT/'timing_smoke.json').read_text())
    seeds=[6101,6201] if smoke['projected384000_evaluations_seconds']>180 else [6101,6102,6103,6201,6202,6203]
    rows=[];traces=[];embeddings={};start=time.monotonic()
    configs=[(s,k,p,2.,8000,'base') for s in seeds for k in [4,8,16] for p in ['frozen','adaptive']]
    configs += [(6201,k,p,1.,16000,'halfstep') for k in [4,8,16] for p in ['frozen','adaptive']]
    for seed,K,mode,dt,steps,arm in configs:
        row,trace,embedding=run(seed,K,mode,dt,steps,arm);rows.append(row);traces+=trace
        embeddings[f'{seed}/{K}/{mode}/{arm}']=embedding
        print(json.dumps(row),flush=True)
        (OUT/'progress_rows.json').write_text(json.dumps(rows,indent=2)+'\n')
    half=[]
    for row in rows:
        if row['arm']!='halfstep':continue
        base=next(r for r in rows if r['seed']==row['seed'] and r['K']==row['K'] and r['policy']==row['policy'] and r['arm']=='base')
        half.append({'K':row['K'],'policy':row['policy'],
                     'square_error_delta':row['best_square_error']-base['best_square_error'],
                     'variance_delta':row['view_variance']-base['view_variance'],
                     'field_norm_delta':row['full_field_norm']-base['full_field_norm']})
    for name,data in [('runs.csv',rows),('traces.csv',traces)]:
        with (OUT/name).open('w') as f:
            writer=csv.DictWriter(f,fieldnames=list(data[0]));writer.writeheader();writer.writerows(data)
    summary={'question':'nonoracle reachability of the declared square/view reference in this finite free-embedding model',
             'N':N,'d':D,'warmup':False,'positive':'.95I+.05U_class','seeds_run':seeds,
             'seeds_unexecuted':[s for s in [6101,6102,6103,6201,6202,6203] if s not in seeds],
             'base_runs':sum(r['arm']=='base' for r in rows),'halfstep_runs':len(half),
             'theorem_applicable_base':sum(r['arm']=='base' and r['theorem_applicable'] for r in rows),
             'maximum_quadrature_gradient_error':max(r['quadrature_gradient_error'] for r in rows),
             'halfstep_comparisons':half,'elapsed_seconds':time.monotonic()-start,'rows':rows,
             'python':platform.python_version(),'numpy':np.__version__,
             'scope':'finite modeltime and free embeddings only; not generic convergence, shared encoder visitation, semantic erasure or practical importance'}
    (OUT/'summary.json').write_text(json.dumps(summary,indent=2)+'\n');(OUT/'embeddings.json').write_text(json.dumps(embeddings)+'\n')
    print(json.dumps({k:v for k,v in summary.items() if k!='rows'},indent=2),flush=True)
    assert summary['maximum_quadrature_gradient_error']<1e-6
if __name__=='__main__':main()
