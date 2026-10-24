"""New 2026-10-25 independent recovery run; no author scientific imports.

Direct ordered tuples and separately tagged tuples check the global certificate.
Exact binomial coarse controls are distinct from a search over all equilibria.
"""
from pathlib import Path
from itertools import product
import csv
import json
import platform
import time
import numpy as np
import scipy
from scipy.stats import binom

ROOT = Path(__file__).resolve().parent
TOL = 1e-11


def normalize(F):
    return F / np.linalg.norm(F, axis=1, keepdims=True)


def tuples(n, K):
    if K == 0:
        return np.empty((1, 0), dtype=int)
    return np.asarray(list(product(range(n), repeat=K)), dtype=int)


def row_coefficients(s, q, K, tau):
    """Two actual finite sums, not two names for one implementation."""
    z = np.exp((s-1)/tau)
    idx = tuples(len(s), K)
    prob = np.prod(q[idx], axis=1)
    counts = np.eye(len(s))[idx].sum(axis=1)
    denom = 1 + z[idx].sum(axis=1)
    direct = np.sum(prob[:, None] * counts * z[None, :] / denom[:, None], axis=0)
    other = tuples(len(s), K-1)
    other_prob = np.prod(q[other], axis=1)
    other_sum = z[other].sum(axis=1)
    tagged = np.asarray([K*q[j]*z[j]*np.sum(other_prob/(1+z[j]+other_sum))
                         for j in range(len(s))])
    return direct, tagged, q*z/np.dot(q, z)


def model(F, K, tau, eps, g, amplitude=0.):
    C = len(F)
    S = F@F.T
    beta = np.zeros((C, C))
    pis = np.zeros_like(beta)
    max_tag_error = 0.
    row_stats = []
    b = np.exp(-2/tau)
    rho = K*b/(2+(K-1)*b)
    gamma = g + abs(amplitude)
    alpha = (1-gamma)/tau
    c = -np.expm1(-2*alpha)/2
    r = -1/(C-1)
    for i in range(C):
        keep = np.arange(C) != i
        s = S[i, keep]
        logw = (-g*s + amplitude*np.sin(np.pi*s)/np.pi)/tau
        w = np.exp(logw-logw.max())
        q = eps/(C-1)+(1-eps)*w/w.sum()
        direct, tagged, pi = row_coefficients(s, q, K, tau)
        beta[i, keep] = direct
        pis[i, keep] = pi
        tag_error = float(np.max(np.abs(direct-tagged)))
        max_tag_error = max(max_tag_error, tag_error)
        m = s.mean()
        var = np.mean((s-m)**2)
        residual = direct-rho*pi
        lower_gap = float(direct@(s-r)-rho*(pi@(s-r))+(1-rho)*(1+r))
        row_stats.append({'tag_error':tag_error,
                          'pointwise_slack':float(residual.min()),
                          'residual_mass_slack':float(1-rho-residual.sum()),
                          'beta_mass':float(direct.sum()),
                          'tilt_slack':float(pi@s-m-c*var),
                          'finite_count_row_slack':lower_gap})
    A = (beta+beta.T)/(2*C*tau)
    H = A-np.diag(np.sum((A@F)*F,axis=1))
    G = 2*H@F
    return S, beta, pis, H, G, row_stats, max_tag_error


def geometry_case(C, seed, tau, eps, K, g, amp):
    F = normalize(np.random.default_rng(seed).normal(size=(C,C-1)))
    S,beta,pis,H,G,rows,tag_error = model(F,K,tau,eps,g,amp)
    mask = ~np.eye(C,dtype=bool)
    score_rows = S[mask].reshape(C,C-1)
    r = -1/(C-1)
    gamma = g+amp
    c = -np.expm1(-2*(1-gamma)/tau)/2
    means = score_rows.mean(axis=1)
    V = np.mean(np.var(score_rows,axis=1))
    A0 = np.dot(F.sum(axis=0),F.sum(axis=0))/(C*(C-1))
    Egram = np.mean((score_rows-r)**2)
    Xstar = np.full_like(S,r)
    np.fill_diagonal(Xstar,1.)
    Asym = (beta+beta.T)/(2*C*tau)
    trace_error = abs(np.sum(Asym*(Xstar-S))-np.sum(H*Xstar))
    score_trace_error = abs(np.sum(beta*(S-Xstar))/(C*tau)+np.sum(H*Xstar))
    mean_identity_error = abs(np.mean(means-r)-A0)
    gram_identity_error = abs(Egram-V-np.mean((means-r)**2))
    conversion_slack = (A0+c*V)/c-Egram
    assert tag_error<TOL
    assert min(x['pointwise_slack'] for x in rows)>-TOL
    assert min(x['residual_mass_slack'] for x in rows)>-TOL
    assert max(x['beta_mass'] for x in rows)<1
    assert min(x['tilt_slack'] for x in rows)>-TOL
    assert min(x['finite_count_row_slack'] for x in rows)>-TOL
    assert max(trace_error,score_trace_error,mean_identity_error,gram_identity_error)<TOL
    assert conversion_slack>-TOL
    return {'C':C,'seed':seed,'tau':tau,'epsilon':eps,'K':K,'g':g,'amplitude':amp,
            'gamma':gamma,'maximum_direct_tagged_error':tag_error,
            'minimum_pointwise_slack':min(x['pointwise_slack'] for x in rows),
            'minimum_residual_mass_slack':min(x['residual_mass_slack'] for x in rows),
            'minimum_tilt_slack':min(x['tilt_slack'] for x in rows),
            'minimum_finite_count_row_slack':min(x['finite_count_row_slack'] for x in rows),
            'maximum_beta_mass':max(x['beta_mass'] for x in rows),
            'trace_identity_error':float(trace_error),'score_trace_identity_error':float(score_trace_error),
            'mean_identity_error':float(mean_identity_error),'gram_identity_error':float(gram_identity_error),
            'gram_conversion_slack':float(conversion_slack),
            'stress_minimum_eigenvalue':float(np.linalg.eigvalsh(H)[0]),
            'field_norm':float(np.linalg.norm(G))}


def coarse(C,K):
    tau=1.;eps=.01;t=.9;m=C//2;b=np.exp(-2.)
    opposite = eps*m/(C-1)+(1-eps)*m*np.exp(2*t)/((m-1)+m*np.exp(2*t))
    W=np.arange(K+1);prob=binom.pmf(W,K,opposite);U=K-W
    denom=1+U+b*W
    As=float(prob@(U/denom));Ao=float(b*(prob@(W/denom)))
    F=np.zeros((C,C-1));F[:m,0]=1;F[m:,0]=-1
    signs=F[:,0];S=F@F.T
    beta=np.where(signs[:,None]==signs[None,:],As/(m-1),Ao/m)
    np.fill_diagonal(beta,0.)
    A=(beta+beta.T)/(2*C*tau)
    H=A-np.diag(np.sum((A@F)*F,axis=1))
    ev=np.linalg.eigvalsh(2*H)
    predicted=np.sort([0.,2*Ao/m]+[(Ao-m*As/(m-1))/m]*(C-2))
    error=float(np.max(np.abs(ev-predicted)))
    assert error<TOL
    assert np.linalg.norm(2*H@F)<TOL
    r=-1/(C-1);c=-np.expm1(-.2)/2;M=(1+r)*(2-b)/(b*c)
    Egram=float(np.mean((S[~np.eye(C,dtype=bool)]-r)**2))
    psd=bool(ev[0]>=-TOL)
    if psd: assert Egram<=M/K+TOL
    return {'C':C,'K':K,'tau':tau,'epsilon':eps,'global_gamma':t,'opposite_mass':opposite,
            'same_total_coefficient':As,'opposite_total_coefficient':Ao,
            'restoring_eigenvalues_per_unused_coordinate':ev.tolist(),
            'stress_PSD':psd,'stationarity_error':float(np.linalg.norm(2*H@F)),
            'graph_spectrum_error':error,'off_Gram_MSE':Egram,'M_over_K':float(M/K),
            'bound_applied_only_if_PSD':psd,
            'K8_simplex_also_locally_attractive':bool(K==8 and .99*t<1-np.exp(-C/(C-1))/(1+K*np.exp(-C/(C-1))))}


def normal_checks():
    ans=[]
    for C in [4,6]:
        F=np.zeros((C,C-1));F[:C//2,0]=1;F[C//2:,0]=-1
        for K in [1,2,3]:
            *_,H,G,rows,err=model(F,K,1.,.01,.9)
            ev,U=np.linalg.eigh(H)
            for label,x in [('lowest_stress_eigenvector',U[:,0]),
                            ('fixed_class_direction',np.arange(1,C+1,dtype=float))]:
                x=x/np.linalg.norm(x);Z=np.zeros_like(F);Z[:,-1]=x;h=3e-6
                gp=model(normalize(F+h*Z),K,1.,.01,.9)[4]
                gm=model(normalize(F-h*Z),K,1.,.01,.9)[4]
                error=float(np.max(np.abs((gp-gm)/(2*h)-2*H@Z)))
                assert error<1e-8
                ans.append({'C':C,'K':K,'direction':label,'step':h,
                            'stationarity_error':float(np.linalg.norm(G)),
                            'closed_loop_normal_block_error':error})
    return ans


def main():
    start=time.monotonic()
    cases=[geometry_case(C,seed,tau,eps,K,g,amp)
           for C in [4,5,6] for seed in [8851,8852]
           for tau in [.7,1.,1.4] for eps in [.01,.13]
           for K in [1,2,3] for g,amp in [(.6,.25),(.85,.05)]]
    stationary=[coarse(C,K) for C in [4,6] for K in [1,2,8,16,4096]]
    normals=normal_checks()
    summary={'date':'2026-10-25','provenance':'new recovery execution; not original raw bytes',
             'general_geometry_cases':len(cases),'stationary_controls':len(stationary),
             'closed_loop_normal_checks':len(normals),
             'maximum_direct_tagged_error':max(x['maximum_direct_tagged_error'] for x in cases),
             'minimum_pointwise_slack':min(x['minimum_pointwise_slack'] for x in cases),
             'minimum_tilt_slack':min(x['minimum_tilt_slack'] for x in cases),
             'maximum_geometry_identity_error':max(max(x['mean_identity_error'],x['gram_identity_error']) for x in cases),
             'maximum_stress_trace_identity_error':max(max(x['trace_identity_error'],x['score_trace_identity_error']) for x in cases),
             'maximum_graph_spectrum_error':max(x['graph_spectrum_error'] for x in stationary),
             'maximum_closed_loop_normal_error':max(x['closed_loop_normal_block_error'] for x in normals),
             'python':platform.python_version(),'numpy':np.__version__,'scipy':scipy.__version__,
             'elapsed_seconds':time.monotonic()-start,
             'scope':'checks of a separately proved global all-stable-equilibria theorem; random points are not equilibrium enumeration'}
    output={'summary':summary,'general_geometry':cases,'stationary_coarse_controls':stationary,'normal_blocks':normals}
    (ROOT/'independent_check.json').write_text(json.dumps(output,indent=2)+'\n')
    with (ROOT/'independent_cases.csv').open('w',newline='') as f:
        writer=csv.DictWriter(f,fieldnames=list(cases[0]));writer.writeheader();writer.writerows(cases)
    print(json.dumps(summary,indent=2),flush=True)


if __name__=='__main__': main()
