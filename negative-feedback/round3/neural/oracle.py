"""Expected joint-negative contrastive loss by Laplace quadrature.
No sampled-negative-index or optimizer noise is used by this oracle.
"""
from functools import lru_cache
import numpy as np
from scipy.special import roots_laguerre,logsumexp,gammaln

def normalize(f):return f/np.linalg.norm(f,axis=1,keepdims=True)
def policy(f,eps=.3,t=np.log(4.)):
    s=f@f.T;z=np.exp(-t*s)
    return eps/len(f)+(1-eps)*z/z.sum(axis=1,keepdims=True)
@lru_cache(None)
def quadrature(L):
    x,w=roots_laguerre(L);return x,np.log(w)

def loss_gradient(f,P,K,q=None,L=96):
    """Return value and gradient w.r.t. unconstrained embedding rows.
    q is treated as detached, including when computed from f here.
    P is a row-stochastic positive channel.
    """
    n=len(f);q=policy(f) if q is None else q
    s=f@f.T;z=np.exp(s);x,lw=quadrature(L);r=(K+1)/np.e;t=x/r
    E=np.exp(-z[:,:,None]*t[None,None,:])
    M=np.einsum('ij,ijl->il',q,E);lm=np.log(M)
    EP=np.einsum('ij,ijl->il',P,E)
    # Combined logs avoid enormous exp(x) times tiny quadrature weights.
    W=np.exp(lw[None,:]+x[None,:]+(K-1)*lm-np.log(r))
    neg=K*q*z*np.einsum('il,il,ijl->ij',W,EP,E)
    QZ=np.einsum('ij,ij,ijl->il',q,z,E)
    pos=-K*P*np.einsum('il,il,ijl->ij',W,QZ,E)
    coeff=(neg+pos)/n
    grad=(coeff+coeff.T)@f
    lep=np.full_like(EP,-np.inf);np.log(EP,out=lep,where=EP>0)
    factor=np.exp(x[None,:]+lep+K*lm)
    value=np.log(r)+np.mean(np.sum(np.exp(lw)[None,:]*(1-factor)/x[None,:],axis=1))-np.sum(P*s)/n
    return float(value),grad

def field(f,P,K,q=None,L=96):
    f=normalize(f);_,g=loss_gradient(f,P,K,q,L)
    return g-(g*f).sum(axis=1,keepdims=True)*f

def direct4(f,P,K,q):
    n=4
    ct=np.array([(u,v,w,K-u-v-w) for u in range(K+1) for v in range(K-u+1) for w in range(K-u-v+1)],float)
    lc=gammaln(K+1)-gammaln(ct+1).sum(axis=1)
    s=f@f.T;z=np.exp(s);coef=np.zeros((n,n));value=0.
    for i in range(n):
        prob=np.exp(lc+ct@np.log(q[i]))
        for p in range(n):
            if not P[i,p]:continue
            D=z[i,p]+ct@z[i]
            weights=P[i,p]*prob/n
            value+=weights@(np.log(D)-s[i,p])
            neg=(weights[:,None]*ct*z[i]/D[:,None]).sum(axis=0)
            coef[i]+=neg;coef[i,p]-=neg.sum()
    return float(value),(coef+coef.T)@f
