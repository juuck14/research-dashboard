"""Exact finite-population support enumeration; fixed before reading risk outputs."""
from pathlib import Path
from itertools import combinations, product
import json,csv,time,sys
import numpy as np
from scipy.sparse.csgraph import connected_components

ROOT=Path(__file__).resolve().parent
REPO=ROOT.parents[2]
OUT=ROOT/'results';OUT.mkdir(exist_ok=True)
C=4;M=4;N=C*M
BITS=np.array([[-1.,-1.],[-1.,1.],[1.,-1.],[1.,1.]])
TASKS=np.column_stack([BITS,np.prod(BITS,axis=1)])
LABELS=np.repeat(TASKS,M,axis=0)
LAMBDAS=[0.,.01,.1]

def from_gram(G):
    e,V=np.linalg.eigh(G)
    return V*np.sqrt(np.maximum(e,0))[None,:]

def supports(k):
    subsets=list(combinations(range(M),k))
    S=np.array([[c*M+r for c,rs in enumerate(choice) for r in rs]
                for choice in product(subsets,repeat=C)])
    T=np.array([[i for i in range(N) if i not in row] for row in S])
    return S,T

def batch_risk(F,k):
    S,T=supports(k)
    X=F[S];Xt=F[T];Y=LABELS[S];Yt=LABELS[T]
    meanX=X.mean(axis=1,keepdims=True);meanY=Y.mean(axis=1,keepdims=True)
    Xc=X-meanX;Xtc=Xt-meanX;Yc=Y-meanY
    U,s,Vh=np.linalg.svd(Xc,full_matrices=False)
    Uy=np.einsum('bji,bjk->bik',U,Yc)
    cross=np.einsum('btd,bsd->bts',Xtc,Xc)
    rows=[];saved={}
    for lam in LAMBDAS:
        if lam==0:
            inv=np.divide(1,s*s,out=np.zeros_like(s),where=s>s[:,:1]*1e-12)
        else:inv=1/(s*s+X.shape[1]*lam)
        alpha=np.einsum('bij,bjk->bik',U,inv[:,:,None]*Uy)
        pred=np.einsum('bts,bsk->btk',cross,alpha)+meanY
        train=np.einsum('bid,bjd->bij',Xc,Xc)@alpha+meanY
        mse=((pred-Yt)**2).mean(axis=1)
        correct=np.where(pred*Yt>1e-10,1.,np.where(pred*Yt< -1e-10,0.,.5))
        acc=correct.mean(axis=(0,1))
        w=np.einsum('bsd,bsk->bdk',Xc,alpha)
        row={'labels_per_class':k,'support_sets':len(S),'lambda':lam,
             'mean_task_mse':float(mse.mean()),'worst_task_mse':float(mse.mean(axis=0).max()),
             'support_average_mse_std':float(mse.mean(axis=1).std()),
             'a_mse':float(mse[:,0].mean()),'b_mse':float(mse[:,1].mean()),'ab_mse':float(mse[:,2].mean()),
             'mean_task_accuracy':float(acc.mean()),'worst_task_accuracy':float(acc.min()),
             'train_mse':float(((train-Y)**2).mean()),'readout_frobenius_mean':float(np.linalg.norm(w,axis=(1,2)).mean())}
        rows.append(row);saved[lam]=(pred[0],Xc[0],Xtc[0],Yc[0],meanY[0])
    return rows,saved

def class_geometry(F):
    mu=F.reshape(C,M,-1).mean(axis=1)
    within=float(np.mean(np.sum((F-np.repeat(mu,M,axis=0))**2,axis=1)))
    G=mu@mu.T;e=np.linalg.eigvalsh(G)
    return {'within_class_variance':within,'class_mean_gram_eigenvalues':e.tolist()}

def main():
    started=time.monotonic()
    old=json.loads((REPO/'negative-feedback/round4/nonoracle/results/embeddings.json').read_text())
    representations={key:np.array(value['embedding']) for key,value in old.items() if key.endswith('/base')}
    groups={key:'learned' for key in representations}
    # The baseline sees precisely the same population positive matrix.
    P=.95*np.eye(N)+.05*np.kron(np.eye(C),np.ones((M,M))/M)
    components,z=connected_components(P>0,directed=False)
    assert components==C
    simplex=np.eye(C)-np.ones((C,C))/C;simplex/=np.linalg.norm(simplex,axis=1,keepdims=True)
    representations['positive_graph_components_simplex']=simplex[z]
    groups['positive_graph_components_simplex']='same_information_baseline'
    representations['exact_square']=np.repeat(BITS/np.sqrt(2),M,axis=0);groups['exact_square']='canonical'
    Gs=simplex@simplex.T
    for nu in [0.,.05,.1,.3,.6,.9]:
        G=(1-nu)*np.kron(Gs,np.ones((M,M)))+nu*np.kron(np.eye(C),Gs)
        name=f'canonical_simplex_nuisance_{nu:g}'
        representations[name]=from_gram(G);groups[name]='canonical_nuisance'
    # Remove view spread without changing the learned class means. Both raw
    # means and renormalized means are declared geometry controls, not methods.
    for key in list(groups):
        if groups[key]!='learned':continue
        mean=representations[key].reshape(C,M,-1).mean(axis=1)
        for mode in ['raw','unit']:
            mu=mean if mode=='raw' else mean/np.linalg.norm(mean,axis=1,keepdims=True)
            name=f'{key}/mean_only_{mode}';representations[name]=np.repeat(mu,M,axis=0)
            groups[name]='geometry_control'
    rows=[];primal=[];canonical=[];geometries=[]
    for name,F in representations.items():
        geo=class_geometry(F);geometries.append({'representation':name,'group':groups[name],**geo})
        for k in [1,2]:
            risk,saved=batch_risk(F,k)
            for row in risk:rows.append({'representation':name,'group':groups[name],**row,'within_class_variance':geo['within_class_variance']})
            # A separate primal linear solve checks the centered dual formula.
            for lam in [.01,.1]:
                pred,Xc,Xtc,Yc,meanY=saved[lam]
                w=np.linalg.solve(Xc.T@Xc+len(Xc)*lam*np.eye(F.shape[1]),Xc.T@Yc)
                primal.append({'representation':name,'labels_per_class':k,'lambda':lam,
                               'absolute_error':float(np.max(np.abs(Xtc@w+meanY-pred)))})
            if name.startswith('canonical_simplex_nuisance_') and k==1:
                nu=float(name.rsplit('_',1)[1])
                for row in risk:
                    lam=row['lambda'];kappa=(4-5*nu)/(4-nu+12*lam)
                    canonical.append({'nu':nu,'lambda':lam,'prediction_coefficient':kappa,
                                      'closed_form_mse':(1-kappa)**2,'observed_mse':row['mean_task_mse'],
                                      'absolute_error':abs((1-kappa)**2-row['mean_task_mse'])})
    with (OUT/'all_risks.csv').open('w') as f:
        writer=csv.DictWriter(f,fieldnames=list(rows[0]));writer.writeheader();writer.writerows(rows)
    summary={'setting':'all three balanced class tasks, exact support enumeration',
             'representations':len(representations),'risk_rows':len(rows),
             'support_sets_per_representation':{'one_per_class':256,'two_per_class':1296},
             'primary_lambda':.01,'primary_rows':[r for r in rows if r['lambda']==.01 and r['labels_per_class']==1 and r['group'] in ['learned','same_information_baseline','canonical']],
             'max_primal_dual_error':max(x['absolute_error'] for x in primal),
             'max_canonical_closed_form_error':max(x['absolute_error'] for x in canonical),
             'elapsed_seconds':time.monotonic()-started,
             'interpretation':'a fixed task-based attempted rescue; count/feedback causality and top-journal novelty require separate evidence'}
    (OUT/'summary.json').write_text(json.dumps(summary,indent=2)+'\n')
    (OUT/'primal_checks.json').write_text(json.dumps(primal,indent=2)+'\n')
    (OUT/'canonical_checks.json').write_text(json.dumps(canonical,indent=2)+'\n')
    (OUT/'geometry.json').write_text(json.dumps(geometries,indent=2)+'\n')
    print(json.dumps(summary,indent=2))
    assert summary['max_primal_dual_error']<1e-8
    assert summary['max_canonical_closed_form_error']<1e-8

if __name__=='__main__':main()
