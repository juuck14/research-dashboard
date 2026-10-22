from pathlib import Path
import sys,json,csv
from itertools import product
import numpy as np
from scipy.linalg import null_space
ROOT=Path(__file__).resolve().parent;OUT=ROOT/'results';OUT.mkdir(exist_ok=True)
sys.path.insert(0,str(ROOT.parents[1]/'round2'/'theory'/'code'))
from verify_controls import moments
from verify_general import BITS,F0
A=np.exp(-1.);EPS=.3;T=np.log(4.);P=[(5,3,2,2),(4,4,3,1)]
def policy(f,alpha=0):
    s=f@f.T;z=np.exp(-T*s+alpha*s*(s*s-1));return EPS/4+(1-EPS)*z/z.sum(axis=1,keepdims=True)
def scalar(part):
    states=np.array(list(product(range(3),repeat=len(part))))
    q=np.array([.103,.374,.523]);prob=np.prod(q[states],axis=1)
    r=np.array(part);D=1+np.sum(r*np.array([1,A,A*A])[states],axis=1)
    adj=states==1;W1=adj@r;W2=adj@(r*r)
    M=float(prob@(W1/D));H=float(prob@(W2/D**2));return {'threshold':1-A*H/M,'scale':A*M}
def field(f,part,alpha):
    f=f/np.linalg.norm(f,axis=1,keepdims=True);q=policy(f,alpha);score=f@f.T
    tuples=np.array(list(product(range(4),repeat=len(part))))
    counts=np.eye(4)[tuples]*np.array(part)[None,:,None];cts=counts.sum(axis=1)
    co=np.zeros((4,4))
    for i in range(4):
        prob=np.prod(q[i,tuples],axis=1);e=np.exp(score[i]-1);D=1+cts@e
        co[i]=(prob[:,None]*cts*e/D[:,None]).sum(axis=0)/4
    g=(co+co.T)@f;return g-(g*f).sum(axis=1,keepdims=True)*f
def fd(part,alpha):
    basis=[null_space(z[None]) for z in F0];J=np.zeros((12,12));h=3e-6
    for col in range(12):
        i,j=divmod(col,3);v=np.zeros_like(F0);v[i]=basis[i][:,j]
        diff=(field(F0+h*v,part,alpha)-field(F0-h*v,part,alpha))/(2*h)
        J[:,col]=np.concatenate([basis[k].T@diff[k] for k in range(4)])
    eig=np.linalg.eigvals(J);t=np.pad(np.stack([-BITS[:,0],BITS[:,1]],axis=1)/np.sqrt(2),((0,0),(0,2)))
    dl=(field(F0+h*t,part,alpha)-field(F0-h*t,part,alpha))/(2*h)
    return {'balance_fd':float(np.sum(dl*t)/4),'eigenvalues':sorted(eig.real.tolist()),'max_imag':float(np.abs(eig.imag).max())}
base=[scalar(p) for p in P];eta=sum(x['threshold'] for x in base)/2
alpha=eta*.187/.112-T
result=[]
for p,s in zip(P,base):
    result.append({'partition':p,'K':sum(p),'L':len(p),'sum_squares':sum(x*x for x in p),
        'same_source_pair_probability':sum(x*(x-1) for x in p)/(12*11),
        'eta':eta,'alpha':alpha,'threshold':s['threshold'],'balance_analytic':s['scale']*(s['threshold']-eta),**fd(p,alpha)})
blocks=[]
for M in [1,2,4,8]:
    for r in [1,2,4,8]:
        m=moments(M,'natural',1/r)
        blocks.append({'M':M,'r':r,'K':M*r,'offset':1/r,'threshold':m['threshold'],'natural_eta':m['eta'],'balance_curvature':m['adaptive_balance']})
with (OUT/'uniform_blocks.csv').open('w') as f:
    w=csv.DictWriter(f,fieldnames=list(blocks[0]));w.writeheader();w.writerows(blocks)
derivative=-T+alpha*(3*np.linspace(-1,1,10001)**2-1)
summary={'moment_matched':result,'monotone_weight_max_log_derivative':float(derivative.max()),
         'threshold_difference':abs(base[0]['threshold']-base[1]['threshold']),
         'opposite_balance_signs':bool(result[0]['balance_analytic']*result[1]['balance_analytic']<0),
         'max_balance_fd_error':max(abs(x['balance_analytic']-x['balance_fd']) for x in result),
         'interpretation':'The fixed partitions are moment matched; selecting eta between computed thresholds is an explicit counterexample construction,not independent confirmation.'}
(OUT/'summary.json').write_text(json.dumps(summary,indent=2)+'\n');print(json.dumps(summary,indent=2))
