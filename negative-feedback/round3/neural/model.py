from pathlib import Path
from itertools import product
import numpy as np
from oracle import normalize,loss_gradient,policy
BITS=np.array(list(product([-1.,1.],repeat=2)))
KEYS=('W1','b1','W2','b2')
SHAPES=((16,64),(64,),(64,8),(8,))
SIZES=[int(np.prod(s)) for s in SHAPES]
CUT=np.cumsum([0]+SIZES)
def unpack(v):return {k:v[CUT[i]:CUT[i+1]].reshape(s) for i,(k,s) in enumerate(zip(KEYS,SHAPES))}
def pack(p):return np.concatenate([p[k].ravel() for k in KEYS])
def dataset(m=4):
    rng=np.random.default_rng(3401);Q=np.linalg.qr(rng.normal(size=(16,16)))[0]
    bits=np.repeat(BITS,m,axis=0)
    source=np.concatenate([bits,rng.normal(scale=.25,size=(4*m,14))],axis=1)
    return source@Q.T,bits,Q
def construct(seed,m=4):
    x,bits,Q=dataset(m);rng=np.random.default_rng(seed)
    p={'W1':rng.normal(scale=.3,size=(16,64)),'b1':rng.normal(scale=.1,size=64),
       'W2':np.zeros((64,8)),'b2':np.zeros(8)}
    p['W1'][:,:2]=Q[:,:2];p['b1'][:2]=0
    p['W2'][0,0]=p['W2'][1,1]=1/(np.sqrt(2)*np.tanh(1))
    return pack(p)
def random(seed):
    rng=np.random.default_rng(seed)
    return pack({'W1':rng.normal(size=(16,64))/4,'b1':rng.normal(scale=.1,size=64),
                 'W2':rng.normal(size=(64,8))/8,'b2':rng.normal(scale=.02,size=8)})
def forward(x,v):
    p=unpack(v);h=np.tanh(x@p['W1']+p['b1']);y=h@p['W2']+p['b2'];n=np.linalg.norm(y,axis=1,keepdims=True)
    assert n.min()>1e-9
    f=y/n;return f,(x,h,f,n)
def backward(df,cache,v):
    p=unpack(v);x,h,f,n=cache;dy=(df-(df*f).sum(axis=1,keepdims=True)*f)/n
    dh=(dy@p['W2'].T)*(1-h*h)
    return pack({'W1':x.T@dh,'b1':dh.sum(axis=0),'W2':h.T@dy,'b2':dy.sum(axis=0)})
def value_gradient(v,x,P,K,q=None,L=64):
    f,c=forward(x,v);loss,g=loss_gradient(f,P,K,q,L)
    return loss,backward(g,c,v)
def output_jacobian(v,x):
    f,c=forward(x,v);J=np.zeros((f.size,len(v)))
    for j in range(f.size):
        e=np.zeros_like(f);e.flat[j]=1;J[j]=backward(e,c,v)
    return J
def geometry(f,m=4):
    means=f.reshape(4,m,-1).mean(axis=1);chars=np.column_stack([np.ones(4),BITS,np.prod(BITS,axis=1)])
    coef=chars.T@means/4;energy=(coef*coef).sum(axis=1)
    square=np.pad(BITS/np.sqrt(2),((0,0),(0,6)));G0=square@square.T;gram=means@means.T
    return {'energy_constant':float(energy[0]),'energy_a':float(energy[1]),'energy_b':float(energy[2]),'energy_ab':float(energy[3]),
            'weaker_energy':float(min(energy[1:3])),'interaction_fraction':float(energy[3]/max(sum(energy[1:]),1e-20)),
            'within_view_variance':float(np.mean(np.sum((f-means.repeat(m,axis=0))**2,axis=1))),
            'square_gram_relative_error':float(np.linalg.norm(gram-G0)/np.linalg.norm(G0)),
            'mean_gram':gram.tolist(),'mean_gram_eigenvalues':np.linalg.eigvalsh(gram).tolist()}
