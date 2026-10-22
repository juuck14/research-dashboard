"""Adversarial scope example; arbitrary score laws, not a learned geometry."""
from pathlib import Path
import csv
import json
import math
import numpy as np
from scipy.integrate import quad
from scipy.special import gammaln

OUT = Path(__file__).resolve().parent
T = math.log(4)
EPSILON = .3
SEED = 44107
N = 512
MAX_K = 24


def main():
    rng = np.random.default_rng(SEED)
    s = np.sort(rng.uniform(-1, 1, (N, 3)), axis=1)
    p = rng.dirichlet(np.ones(3), size=N)
    h2 = np.exp(rng.uniform(-3, 3, (N, 3)))
    soft = p * np.exp(-T * s)
    soft /= soft.sum(axis=1, keepdims=True)
    q = EPSILON * p + (1-EPSILON) * soft
    rho = (1-EPSILON) * soft / q
    W = np.exp(s-1)
    H = np.empty((N, MAX_K))
    for k in range(1, MAX_K+1):
        ct = np.array([(i, j, k-i-j) for i in range(k+1)
                       for j in range(k-i+1)], dtype=float)
        logc = gammaln(k+1) - gammaln(ct+1).sum(axis=1)
        prob = np.exp(logc[None, :] + np.log(q) @ ct.T)
        D = 1 + W @ ct.T
        term1 = (W*h2*(1-T*rho)) @ ct.T
        term2 = (W*W*h2) @ ct.T
        H[:, k-1] = (prob*(term1/D-term2/D**2)).sum(axis=1)

    limit = (q*h2*W*(1-T*rho)).sum(axis=1)/(q*W).sum(axis=1)
    pos = np.flatnonzero(np.all(H > 1e-8, axis=1) & (limit > 1e-6))
    neg = np.flatnonzero(np.all(H < -1e-8, axis=1) & (limit < -1e-6))
    # Search all feasible opposite-sign pairs at each earlier/later count,
    # rather than only laws positive/negative throughout the entire grid.
    best = None
    for j in range(MAX_K-1):
        for ell in range(j+1, MAX_K):
            aa = np.flatnonzero((H[:, j] > 1e-8) & (H[:, ell] > 1e-8))
            bb = np.flatnonzero((H[:, j] < -1e-8) & (H[:, ell] < -1e-8))
            if not len(aa) or not len(bb):
                continue
            ra = H[aa, j, None]/(-H[bb, j][None, :])
            rb = H[aa, ell, None]/(-H[bb, ell][None, :])
            i, k = np.unravel_index(np.argmax(ra-rb), ra.shape)
            drop = ra[i, k]-rb[i, k]
            if best is None or drop > best[0]:
                best = (float(drop), int(aa[i]), int(bb[k]), j, ell,
                        float(ra[i, k]), float(rb[i, k]))
    result = {'seed': SEED, 'population_count': N, 'K_max': MAX_K,
              'positive_laws': len(pos), 'negative_laws': len(neg),
              'search': 'all opposite-sign anchor pairs and ordered K pairs',
              'largest_feasible_ratio_drop': None if best is None else best[0]}
    if best is None or best[0] <= 0:
        result['found'] = False
        (OUT/'anchor_mixture_check.json').write_text(json.dumps(result, indent=2)+'\n')
        print(json.dumps(result, indent=2))
        return
    _, a, b, ka, kb, ratio_a, ratio_b = best
    coefficient = (ratio_a+ratio_b)/2
    curve = (H[a]+coefficient*H[b])/(1+coefficient)
    laws = []
    for idx in [a, b]:
        laws.append({'scores': s[idx].tolist(), 'p_score': p[idx].tolist(),
                     'h2': h2[idx].tolist(), 'q_score': q[idx].tolist(),
                     'curvature_limit': float(limit[idx])})

    def laplace_curvature(law, k):
        w = np.exp(np.array(law['scores'])-1)
        qq = np.array(law['q_score'])
        hh = np.array(law['h2'])
        pp = np.array(law['p_score'])
        rr = (qq-EPSILON*pp)/qq
        def integrand(z):
            phi = qq @ np.exp(-z*w)
            return (math.exp(-z) * phi**(k-1) *
                    (qq*hh*w*np.exp(-z*w) * (1-T*rr-z*w)).sum())
        return k*quad(integrand, 0, np.inf, epsabs=1e-11,
                      epsrel=1e-11, limit=300)[0]
    checks = []
    for kk in [ka+1, kb+1]:
        individual = [laplace_curvature(law, kk) for law in laws]
        independent = (individual[0]+coefficient*individual[1])/(1+coefficient)
        checks.append({'K': kk, 'multinomial': float(curve[kk-1]),
                       'laplace': independent,
                       'difference': abs(independent-curve[kk-1])})
    result.update({'found': True, 'law_indices': [a, b],
                   'laws': laws, 'anchor_probabilities': [1/(1+coefficient),
                                                         coefficient/(1+coefficient)],
                   'selected_counts': [ka+1, kb+1], 'checks': checks,
                   'interpretation': 'An existence construction outside identical-anchor-law assumption; no geometric realization claimed.'})
    assert checks[0]['multinomial'] > 1e-6
    assert checks[1]['multinomial'] < -1e-6
    assert max(c['difference'] for c in checks) < 1e-9
    (OUT/'anchor_mixture_check.json').write_text(json.dumps(result, indent=2)+'\n')
    with (OUT/'anchor_mixture_curve.csv').open('w') as file:
        writer = csv.writer(file)
        writer.writerow(['K', 'law_a_curvature', 'law_b_curvature', 'mixture_curvature'])
        for k in range(MAX_K):
            writer.writerow([k+1, H[a, k], H[b, k], curve[k]])
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
