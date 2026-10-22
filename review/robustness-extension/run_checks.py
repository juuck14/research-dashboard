from pathlib import Path
from itertools import product
import json,csv
import numpy as np
from scipy.linalg import null_space
from scipy.special import expit,softmax,logsumexp

OUT=Path(__file__).resolve().parent/'results';OUT.mkdir(exist_ok=True)
BITS=np.array(list(product([-1.,1.],repeat=2)))
BASE=np.pad(BITS/np.sqrt(2),((0,0),(0,2)))
EPS=.1;KAPPA=-2.
EMBEDDINGS={}
def norm(z): return z/np.linalg.norm(z,axis=1,keepdims=True)
def qfun(z): return (1-EPS)*softmax(KAPPA*z@z.T,axis=1)+EPS/4
Q0=qfun(BASE)
def positive(eta):
    dist=np.sum(BITS[:,None,:]!=BITS[None,:,:],axis=-1)
    return eta**dist*(1-eta)**(2-dist)
def exactfield(z,q,t):
    z=norm(z);s=z@z.T
    # indices are anchor i, positive p, negative j
    coeff=t[:,:,None]*q[:,None,:]*expit(s[:,None,:]-s[:,:,None])/4
    c=coeff.sum(axis=1)-coeff.sum(axis=2)
    g=(c+c.T)@z
    return -g+(g*z).sum(axis=1,keepdims=True)*z
def jacobian(eta,policy,h):
    t=positive(eta);basis=[null_space(zi[None,:]) for zi in BASE]
    def f(z): return exactfield(z,Q0 if policy=='frozen' else qfun(norm(z)),t)
    jac=np.zeros((12,12))
    for col in range(12):
        i,j=divmod(col,3);v=np.zeros_like(BASE);v[i]=basis[i][:,j]
        diff=(f(BASE+h*v)-f(BASE-h*v))/(2*h)
        jac[:,col]=np.concatenate([basis[k].T@diff[k] for k in range(4)])
    eig=np.linalg.eigvals(jac);nonzero=eig.real[np.abs(eig.real)>1e-7]
    return {'eta':eta,'policy':policy,'h':h,'min_channel_eigenvalue':float(np.linalg.eigvalsh(t).min()),
            'residual':float(np.max(np.abs(f(BASE)))),'positive_eigenvalues':int(np.sum(eig.real>1e-7)),
            'zeros':int(np.sum(np.abs(eig.real)<=1e-7)),'max_nonzero':float(nonzero.max()),
            'max_imag':float(np.abs(eig.imag).max())}
noise_rows=[jacobian(eta,p,h) for eta in [0.,.001,.01,.05,.1] for p in ['frozen','adaptive'] for h in [1e-5,3e-6]]
with (OUT/'positive_channel.csv').open('w') as f:
    w=csv.DictWriter(f,fieldnames=noise_rows[0]);w.writeheader();w.writerows(noise_rows)

def evaluate(z):
    rng=np.random.default_rng(90210)
    samples=(z[:,None,:]+.05*rng.normal(size=(4,2500,4))).reshape(-1,4)
    labels=np.repeat(BITS,2500,axis=0)
    scores=-np.sum((samples[:,None,:]-z[None,:,:])**2,axis=-1)/(2*.05**2)
    acc=[]
    for bit in range(2):
        a=logsumexp(scores[:,BITS[:,bit]>0],axis=1)
        b=logsumexp(scores[:,BITS[:,bit]<0],axis=1)
        acc.append(float(np.mean((a>b)==(labels[:,bit]>0))))
    dist=np.sqrt(np.sum((z[:,None,:]-z[None,:,:])**2,axis=-1)+np.eye(4)*100)
    return acc,float(dist.min())
def train(seed,policy):
    rng=np.random.default_rng(seed)
    z=norm(BASE+1e-4*rng.normal(size=BASE.shape))
    lr=.1;batch=64
    for step in range(6000):
        q=np.full((4,4),.25) if policy=='uniform' else Q0 if policy=='frozen' else qfun(z)
        anchors=rng.integers(0,4,size=batch);u=rng.random(batch)
        negatives=np.minimum(np.sum(u[:,None]>np.cumsum(q[anchors],axis=1),axis=1),3)
        counts=np.bincount(4*anchors+negatives,minlength=16).reshape(4,4)/batch
        c=counts*expit(z@z.T-1)
        g=(c+c.T)@z;g-=np.sum(g*z,axis=1,keepdims=True)*z
        z=norm(z-lr*g)
    acc,mindist=evaluate(z)
    EMBEDDINGS[f'{seed}/{policy}']=z.tolist()
    return {'seed':seed,'split':'primary' if seed<2000 else 'confirmation','policy':policy,
            'steps':6000,'batch':64,'lr':lr,'accuracy_a_noise05':acc[0],'accuracy_b_noise05':acc[1],
            'worst_accuracy':min(acc),'min_pair_distance':mindist}
rows=[train(seed,p) for seed in list(range(1001,1007))+list(range(3001,3005)) for p in ['uniform','frozen','adaptive']]
with (OUT/'sgd.csv').open('w') as f:
    w=csv.DictWriter(f,fieldnames=rows[0]);w.writeheader();w.writerows(rows)
replications={}
for split in ['primary','confirmation']:
    seeds=sorted({r['seed'] for r in rows if r['split']==split})
    success=0
    for seed in seeds:
        d={r['policy']:r for r in rows if r['seed']==seed}
        success+=d['adaptive']['worst_accuracy']<.65 and d['frozen']['worst_accuracy']>.95
    replications[split]={'success':int(success),'total':len(seeds)}
summary={'sgd_runs':len(rows),'criterion':replications,'positive_channel_rows':noise_rows,
         'sgd_worst_accuracy_by_policy':{p:[min(r['worst_accuracy'] for r in rows if r['policy']==p),max(r['worst_accuracy'] for r in rows if r['policy']==p)] for p in ['uniform','frozen','adaptive']}}
(OUT/'summary.json').write_text(json.dumps(summary,indent=2)+'\n')
(OUT/'final_embeddings.json').write_text(json.dumps(EMBEDDINGS,indent=2)+'\n')
print(json.dumps(summary,indent=2))
