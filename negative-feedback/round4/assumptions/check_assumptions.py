"""Exact population count sums and independent ordered-tuple field differences."""
from functools import lru_cache
from itertools import product
from pathlib import Path
import csv
import json
import numpy as np
from scipy.optimize import brentq
from scipy.special import gammaln

ROOT = Path(__file__).resolve().parent
OUT = ROOT/'results'
OUT.mkdir(exist_ok=True)
EPS = .3
T = np.log(4.)
BETA = 1.
S = np.array([-.6, 0., .6])
P = np.array([.2, .6, .2])
AMP = np.array([.4, 1., .7])
S6 = np.repeat(S, 2)
P6 = np.repeat(P/2, 2)
H6 = np.repeat(AMP, 2)*np.tile([-1., 1.], 3)

@lru_cache(None)
def compositions(n, groups):
    if groups == 1:
        return np.array([[n]], dtype=int)
    rows = []
    for first in range(n+1):
        rest = compositions(n-first, groups-1)
        rows.extend(np.column_stack([np.full(len(rest), first), rest]))
    return np.asarray(rows, dtype=int)

def law(scores, probabilities):
    tilted = probabilities*np.exp(-T*scores)
    tilted /= tilted.sum()
    q = EPS*probabilities+(1-EPS)*tilted
    rho = (1-EPS)*tilted/q
    return tilted, q, rho

def weights(counts, q, K):
    log_prob = gammaln(K+1)-gammaln(counts+1).sum(axis=1)+counts@np.log(q)
    return np.exp(log_prob)

def conditional_field(scores, means, variances, probabilities, K):
    tilted, q, rho = law(scores, probabilities)
    W = np.exp(scores-1)
    counts = compositions(K, len(scores))
    prob = weights(counts, q, K)
    D = BETA+counts@W
    M = counts@(W*means)
    b = tilted@means
    R = counts@(rho*(means-b))
    first = counts@(W*(variances+means**2))
    second_var = counts@(W**2*variances)
    response_var = counts@(W*rho*variances)
    G = prob@(M/D)
    H = prob@(first/D-(M*M+second_var)/(D*D)
              -T*(M*R+response_var)/D)
    return float(G), float(H)

def tuple_field(delta, scores, derivatives, probabilities, K):
    shifted = scores+delta*derivatives
    _, q, _ = law(shifted, probabilities)
    tuples = np.array(list(product(range(len(scores)), repeat=K)))
    prob = np.prod(q[tuples], axis=1)
    W = np.exp(shifted[tuples]-1)
    return float(prob@((W*derivatives[tuples]).sum(axis=1)/(BETA+W.sum(axis=1))))

def write_csv(name, rows):
    with (OUT/name).open('w', newline='') as stream:
        writer = csv.DictWriter(stream, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)

def main():
    rows = []
    a = S+.5
    for K in [1, 2, 4, 8, 16, 32, 64]:
        _, base_h = conditional_field(S, np.zeros(3), AMP**2, P, K)
        ga, ha = conditional_field(S, a, np.zeros(3), P, K)
        for tau in [0., .001, .01, .05, .1]:
            g, h = conditional_field(S, tau*a, AMP**2, P, K)
            rows.append({'K': K, 'tau': tau, 'G': g, 'H': h,
                         'baseline_H': base_h,
                         'drift_linear_residual': g-tau*ga,
                         'slope_quadratic_residual': h-base_h-tau*tau*ha,
                         'reference_stationary': abs(g)<1e-14})
    write_csv('conditional_mean_break.csv', rows)

    finite = []
    for K in [1, 2, 3]:
        for tau in [0., .01, .1]:
            derivatives = H6+tau*(S6+.5)
            g, h = conditional_field(S, tau*a, AMP**2, P, K)
            for step in [1e-5, 1e-6]:
                observed = (tuple_field(step, S6, derivatives, P6, K)
                            -tuple_field(-step, S6, derivatives, P6, K))/(2*step)
                finite.append({'K': K, 'tau': tau, 'step': step,
                               'H_formula': h, 'H_tuple_fd': observed,
                               'absolute_error': abs(h-observed),
                               'G_formula': g,
                               'G_tuple': tuple_field(0, S6, derivatives, P6, K)})
    write_csv('ordered_tuple_checks.csv', finite)

    jitters = []
    offset = np.array([.03, -.2, .4, .07, -.13, .25])
    for eta in [1e-4, 1e-3, .01]:
        scores = S6+eta*offset
        assert len(np.unique(scores)) == 6
        for K in [1, 4, 8]:
            def field(delta):
                return conditional_field(scores+delta*H6, H6, np.zeros(6), P6, K)
            g, h = field(0.)
            left, right = field(-.1)[0], field(.1)[0]
            bracketed = left*right <= 0
            root = brentq(lambda delta: field(delta)[0], -.1, .1,
                          xtol=1e-14) if bracketed else None
            gr, hr = field(root) if root is not None else (None, None)
            jitters.append({'jitter': eta, 'K': K,
                            'reference_G': g, 'reference_H': h,
                            'six_distinct_scores': True,
                            'conditional_mean_squared': float(P6@(H6*H6)),
                            'root_in_fixed_bracket': bracketed,
                            'root': root, 'root_G': gr, 'root_H': hr,
                            'root_attractive': hr > 0 if hr is not None else None})
    write_csv('distinct_score_roots.csv', jitters)

    # Conditioning diagnostic for the proved first-L-count implication.
    # Its exact invertibility is analytic; this diagnostic is not its proof.
    kernels = []
    for L in [2, 3, 6]:
        scores = np.linspace(-.6, .6, L)
        p = np.ones(L)/L
        _, q, _ = law(scores, p)
        w = np.exp(scores-1)
        F = np.zeros((L, L))
        for n in range(L):
            counts = compositions(n, L)
            prob = weights(counts, q, n)
            for i in range(L):
                F[i, n] = prob@(1/(BETA+w[i]+counts@w))
        singular = np.linalg.svd(F, compute_uv=False)
        kernels.append({'score_levels': L, 'singular_values': singular.tolist(),
                        'condition_number': float(singular[0]/singular[-1]),
                        'determinant_float': float(np.linalg.det(F)),
                        'interpretation': 'Exact invertibility does not provide a well-conditioned approximate-balance certificate.'})
    result = {
        'theory': 'general normalizer-aware curvature, conditional-mean decomposition, common-stationarity equivalence',
        'max_linear_drift_identity_error': max(abs(r['drift_linear_residual']) for r in rows),
        'max_quadratic_slope_identity_error': max(abs(r['slope_quadratic_residual']) for r in rows),
        'max_ordered_tuple_fd_error': max(r['absolute_error'] for r in finite),
        'max_formula_vs_tuple_drift_error': max(abs(r['G_formula']-r['G_tuple']) for r in finite),
        'jitter_roots_found': sum(r['root_in_fixed_bracket'] for r in jitters),
        'jitter_runs': len(jitters),
        'jitter_root_rows': jitters,
        'finite_kernel_conditioning': kernels,
        'stability_warning': 'Only root_H is an equilibrium restoring derivative. reference_H with nonzero reference_G is not a stability eigenvalue.',
        'scope_warning': 'Scalar score-law audit, not a generic realizable Gram geometry or a top-journal contribution.',
    }
    assert result['max_ordered_tuple_fd_error'] < 1e-7
    assert result['max_linear_drift_identity_error'] < 1e-12
    assert result['max_quadratic_slope_identity_error'] < 1e-12
    (OUT/'summary.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))

if __name__ == '__main__':
    main()
