from pathlib import Path
import json,time
import numpy as np
from check_collapse import field,normalize,moments,EPS,T,geometry
ROOT=Path(__file__).resolve().parent
C=4;V=2;N=C*V;D=N
labels=np.repeat(np.arange(C),V)
mask=labels[:,None]!=labels[None,:]
base=mask/(N-V)
P=np.zeros((N,N))
for i in range(N):P[i,i^1]=1

def qfun(f):
    w=np.exp(-T*(f@f.T))*mask
    return EPS*base+(1-EPS)*w/w.sum(axis=1,keepdims=True)

def check(K,frozen):
    f=np.zeros((N,D));f[:N//2,0]=1;f[N//2:,0]=-1
    q0=qfun(f);J=np.zeros((N*(D-1),)*2);h=1e-5
    for j in range(J.shape[1]):
        v=np.zeros_like(f);i,k=divmod(j,D-1);v[i,k+1]=h
        fp=normalize(f+v);fm=normalize(f-v)
        gp=field(fp,P,K,q0 if frozen else qfun(fp),L=96)
        gm=field(fm,P,K,q0 if frozen else qfun(fm),L=96)
        J[:,j]=((gp-gm)/(2*h))[:,1:].ravel()
    ev=np.linalg.eigvalsh((J+J.T)/2);_,As,Ao=moments(C,K);m=C//2;Btot=As+Ao
    lamshape=(Ao-m*As/(m-1))/(m*V);lamconst=2*Ao/(m*V)
    lamview=(Ao-As+2*Btot)/(m*V) # Pswap nonconstant mu=-1
    pred=np.sort([0]*(D-1)+[lamconst]*(D-1)+[lamshape]*((C-2)*(D-1))+[lamview]*(C*(V-1)*(D-1)))
    return {'K':K,'frozen':frozen,'tangent_dimension':len(ev),
            'maximum_full_spectrum_error':float(np.max(np.abs(ev-pred))),
            'min_nonrotation_eigenvalue':float(ev[D-1]),'predicted_min':float(min(lamshape,lamconst,lamview))}

def run(K,seed):
    start=time.monotonic();rng=np.random.default_rng(seed);f=normalize(rng.normal(size=(N,D)));last=0;stop='cap'
    for step in range(20000):
        g=field(f,P,K,qfun(f),L=64);norm=float(np.linalg.norm(g))
        if step>=100 and step%20==0 and norm<1e-8:
            last=step;stop='field_tolerance';break
        f=normalize(f-2*g);last=step+1
    means=f.reshape(C,V,D).mean(axis=1);viewvariance=float(np.mean(np.sum((f-means.repeat(V,axis=0))**2,axis=1)))
    g64=field(f,P,K,qfun(f),L=64);g96=field(f,P,K,qfun(f),L=96)
    return {'K':K,'seed':seed,'steps':last,'stop':stop,'field_norm':float(np.linalg.norm(g96)),
            'quadrature_difference':float(np.max(np.abs(g64-g96))),
            'within_class_view_variance':viewvariance,**geometry(f),
            'elapsed_seconds':time.monotonic()-start,'embedding':f.tolist()}

def main():
    checks=[check(K,frozen) for K in [1,8,32] for frozen in [False,True]]
    assert max(x['maximum_full_spectrum_error'] for x in checks)<1e-7
    assert min(x['min_nonrotation_eigenvalue'] for x in checks)>0
    rows=[run(K,seed) for K in [8,32] for seed in [7301,7401]]
    result={'C':C,'views':V,'d':D,'positive_self_probability':0,
            'negative_same_class_probability':0,'full_spectrum_checks':checks,'trajectories':rows,
            'scope':'filtered finite class/view model; full local theorem and fixed random trajectories, not generic global convergence'}
    (ROOT/'nonidentity_summary.json').write_text(json.dumps(result,indent=2)+'\n')
    assert max(x['quadrature_difference'] for x in rows)<1e-6
    print(json.dumps({'max_spectrum_error':max(x['maximum_full_spectrum_error'] for x in checks),
                      'trajectories':[{k:v for k,v in x.items() if k not in ['embedding','top_eigenvalues']} for x in rows]},indent=2))
if __name__=='__main__':main()
