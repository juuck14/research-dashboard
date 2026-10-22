"""Independent ordered-tuple field and sphere-spectrum audit.

Does not import the theory author's implementation. Each tuple receives its iid
probability directly. This differs from the multinomial count implementation.
"""
from pathlib import Path
from itertools import product
from math import comb, exp, fsum
import csv
import json
import numpy as np

HERE = Path(__file__).resolve().parent
OUT = HERE / 'results'
OUT.mkdir(exist_ok=True)
A = exp(-1)
B = exp(-2)
EPS = .1
BITS = np.array(list(product([-1., 1.], repeat=2)))
F = np.column_stack([BITS / np.sqrt(2), np.zeros((4, 2))])
TB = np.zeros((4, 4, 3))
TB[:, 0, 0] = -BITS[:, 1] / np.sqrt(2)
TB[:, 1, 0] = BITS[:, 0] / np.sqrt(2)
TB[:, 2, 1] = 1
TB[:, 3, 2] = 1

def qfun(x, alpha, slope=2., eps=EPS):
    scores = x @ x.T
    unnorm = np.exp(-slope * scores + alpha * scores * (scores**2-1))
    return eps/4 + (1-eps)*unnorm/unnorm.sum(axis=1)[:, None]

def ordered_field(x, k, alpha, fixed=None, slope=2., eps=EPS, positive=1.):
    x = x/np.linalg.norm(x, axis=1)[:, None]
    q = qfun(x, alpha, slope, eps) if fixed is None else fixed
    score = x @ x.T
    tuples = np.array(list(product(range(4), repeat=k)), dtype=int)
    coeff = np.zeros((4, 4))
    for anchor in range(4):
        probabilities = np.prod(q[anchor, tuples], axis=1)
        logits = np.exp(score[anchor, tuples]-1)
        weights = probabilities[:, None]*logits/(positive+logits.sum(axis=1))[:, None]/4
        for j in range(4):
            coeff[anchor, j] = weights[tuples == j].sum()
    euclidean = (coeff + coeff.T) @ x
    return euclidean - (euclidean*x).sum(axis=1)[:, None]*x

def exact_moments(k, slope=2., eps=EPS, positive=1.):
    z = exp(-slope) + 2 + exp(slope)
    p = np.array([exp(-slope), 1., exp(slope)])/z
    u = eps/4 + (1-eps)*p[0]
    v = eps/4 + (1-eps)*p[1]
    w = eps/4 + (1-eps)*p[2]
    terms = {n: [] for n in ['A','B','C','N2D2','N2D','NSD','mass']}
    for self_n in range(k+1):
        for adj_n in range(k-self_n+1):
            opp_n = k-self_n-adj_n
            pr = comb(k,self_n)*comb(k-self_n,adj_n)*u**self_n*(2*v)**adj_n*w**opp_n
            den = positive+self_n + A*adj_n+B*opp_n
            terms['mass'].append(pr)
            terms['A'].append(pr*adj_n/den)
            terms['B'].append(pr*adj_n/den**2)
            terms['C'].append(pr*opp_n/den)
            terms['N2D2'].append(pr*(adj_n**2+adj_n)/den**2)
            terms['N2D'].append(pr*(adj_n**2+adj_n)/den)
            terms['NSD'].append(pr*adj_n*(self_n*p[0]/u+adj_n*p[1]/v+opp_n*p[2]/w)/den)
    result = {key: fsum(vals) for key,vals in terms.items()}
    result.update(u=u,v=v,w=w,softadj=p[1])
    result['R'] = result['B']/result['A']
    result['T'] = 1-A*result['R']
    return result

def predicted(k, alpha, slope=2., eps=EPS, positive=1.):
    m = exact_moments(k,slope,eps,positive)
    v=m['v']; g=(1-eps)*m['softadj']*(-slope-alpha)
    frozen_balance=A*m['A']-A*A*m['B']
    adaptive_balance=frozen_balance+A*g/v*m['A']
    frozen_ab=A*m['A']/2-A*A*m['N2D2']/4+B*m['C']
    adaptive_ab=frozen_ab+A*g*(m['N2D']/(4*v)-m['NSD']/2)
    normal_constant=A*m['A']/2+B*m['C']
    normal_ab=-A*m['A']/2+B*m['C']
    d = dict(frozen_balance=frozen_balance, adaptive_balance=adaptive_balance,
             frozen_ab=frozen_ab,adaptive_ab=adaptive_ab,
             normal_constant=normal_constant,normal_ab=normal_ab,eta=-g/v,T=m['T'])
    spectra = {}
    for policy in ['frozen','adaptive']:
        spectra[policy] = np.sort([d[policy+'_balance']]+[d[policy+'_ab']]*2+
                                [normal_constant]*2+[normal_ab]*2+[0.]*5)
    return d,spectra

def finite_difference(k, alpha, h, rotate, slope=2., eps=EPS, positive=1.):
    x=F.copy(); basis=TB.copy()
    if rotate:
        rotation = np.linalg.qr(np.random.default_rng(271828).normal(size=(4,4)))[0]
        x=x@rotation
        basis=np.einsum('ji,njk->nik',rotation,basis)
    fixed=qfun(x,alpha,slope,eps)
    _,expected=predicted(k,alpha,slope,eps,positive)
    rows=[]
    for policy in ['frozen','adaptive']:
        def field(y):
            return ordered_field(y,k,alpha,fixed if policy=='frozen' else None,slope,eps,positive)
        jac=np.zeros((12,12))
        for column in range(12):
            state,local=divmod(column,3)
            direction=np.zeros_like(x);direction[state]=basis[state,:,local]
            diff=(field(x+h*direction)-field(x-h*direction))/(2*h)
            jac[:,column]=np.einsum('ndk,nd->nk',basis,diff).ravel()
        ev=np.linalg.eigvals(jac)
        rows.append(dict(K=k,alpha=alpha,h=h,rotate=rotate,policy=policy,
                         stationary_residual=float(np.abs(field(x)).max()),
                         eigen_imaginary=float(np.abs(ev.imag).max()),
                         max_eigen_error=float(np.abs(np.sort(ev.real)-expected[policy]).max()),
                         jacobian_asymmetry=float(np.abs(jac-jac.T).max())))
    return rows

def save_csv(name,rows):
    with (OUT/name).open('w') as handle:
        out=csv.DictWriter(handle,fieldnames=list(rows[0]));out.writeheader();out.writerows(rows)

def main():
    fd=[]
    for k in [1,2,3,4,5]:
        for alpha in [-1.5,-.9,0.]:
            for h in [1e-5,3e-6]:
                fd.extend(finite_difference(k,alpha,h,False))
    fd.extend(finite_difference(3,-.9,1e-5,True))
    moments=[]
    for k in [1,2,3,4,5,8,9,16,64,128]:
        m=exact_moments(k); sp,_=predicted(k,-.9)
        moments.append({'K':k,**m,**sp})
    save_csv('ordered_tuple_fd.csv',fd)
    save_csv('independent_moments.csv',moments)
    summary={
        'ordered_tuple_fd_checks':len(fd),
        'max_eigen_error':max(x['max_eigen_error'] for x in fd),
        'max_imaginary_part':max(x['eigen_imaginary'] for x in fd),
        'max_stationary_residual':max(x['stationary_residual'] for x in fd),
        'K8':next(x for x in moments if x['K']==8),
        'K9':next(x for x in moments if x['K']==9),
        'min_q_at_square':float(qfun(F,-.9).min()),
        'same_q_error':max(float(np.abs(qfun(F,a)-qfun(F,0)).max()) for a in [-1.5,-.9,0,.5]),
    }
    (OUT/'summary.json').write_text(json.dumps(summary,indent=2)+'\n')
    print(json.dumps(summary,indent=2))
    assert summary['max_eigen_error']<2e-7
    assert summary['max_imaginary_part']<1e-7
    assert summary['max_stationary_residual']<1e-12

if __name__=='__main__':main()
