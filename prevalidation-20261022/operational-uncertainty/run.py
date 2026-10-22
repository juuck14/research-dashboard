"""Population Fourier density and singular-direction KL, no fitted encoder.

Run: OPENBLAS_NUM_THREADS=1 python prevalidation-20261022/operational-uncertainty/run.py
"""
from pathlib import Path
import csv
import json
import platform
import numpy as np
import scipy
from scipy.special import iv, ivp

ROOT = Path(__file__).resolve().parent
OUT = ROOT / 'results'
OUT.mkdir(exist_ok=True)


def coefficients(a, b, modes):
    m = np.arange(1, modes + 1)
    return (iv(m, a) / iv(0, a))**2 * iv(m, b) / iv(0, b)


def density(a, b, modes=64, grid=8192):
    theta = np.arange(grid) * (2*np.pi/grid)
    basis = np.cos(np.arange(1, modes+1)[:, None] * theta[None, :])
    p = (1 + 2*coefficients(a, b, modes) @ basis)/(2*np.pi)
    assert p.min() > 0
    return theta, p, basis


def log_bessel_derivatives(m, c):
    def derivatives(n):
        v = iv(n, c)
        r1, r2, r3 = [ivp(n, c, k)/v for k in (1, 2, 3)]
        return r1, r2-r1*r1, r3-3*r2*r1+2*r1**3
    d = np.array(derivatives(m)) - np.array(derivatives(0))[:, None]
    return d


def kl(p, q):
    # Remove an exactly zero first-order integral to avoid numerical cancellation.
    r = (p-q)/q
    g = (1+r)*np.log1p(r)-r
    small = np.abs(r) < 1e-3
    rs = r[small]
    g[small] = sum(((-1.)**k)/(k*(k-1))*rs**k for k in range(2, 10))
    return float(np.mean(q*g)*2*np.pi)


def constants(c, modes=64, grid=8192):
    _, p, basis = density(c, c, modes, grid)
    m = np.arange(1, modes+1)
    deriv = log_bessel_derivatives(m, c)
    coeff = coefficients(c, c, modes)
    A = (3*coeff*deriv[1]) @ basis/np.pi
    B = (-coeff*deriv[2]) @ basis/np.pi
    C4 = float(np.mean(A*A/p)*np.pi)
    C6 = float(np.mean(B*B/p)*4*np.pi)
    return C4, C6, A, B


def sample_loglr(a, b, other_a, other_b, n, seed):
    rng = np.random.default_rng(seed)
    angle = (rng.vonmises(0, a, n)+rng.vonmises(0, a, n)
             +rng.vonmises(0, b, n))
    angle = (angle+np.pi) % (2*np.pi)-np.pi
    m = np.arange(1, 33)
    cp, cq = coefficients(a, b, 32), coefficients(other_a, other_b, 32)
    total = 0.
    for start in range(0, n, 4096):
        basis = np.cos(angle[start:start+4096, None]*m[None, :])
        p, q = 1+2*basis@cp, 1+2*basis@cq
        total += np.log(p/q).sum()
    return float(total)


rows, convergence, checks = [], [], []
for c in (1., 2., 4.):
    C4, C6, A, B = constants(c)
    _, p0, _ = density(c, c)
    for modes, grid in ((32, 4096), (96, 16384)):
        a4, a6, _, _ = constants(c, modes, grid)
        convergence.append({'c': c, 'modes': modes, 'grid': grid,
                            'C4': a4, 'C6': a6,
                            'C4_relative_error': abs(a4/C4-1),
                            'C6_relative_error': abs(a6/C6-1)})
    for t in (.02, .04, .08, .12, .16):
        _, pp, _ = density(c+t, c-2*t)
        _, pm, _ = density(c-t, c+2*t)
        k4, k6 = kl(pp, p0), kl(pp, pm)
        rows.append({'c': c, 't': t, 'kl_to_diagonal': k4,
                     'kl_between_signs': k6, 'C4': C4, 'C6': C6,
                     'kl4_scaled': k4/t**4, 'kl6_scaled': k6/t**6,
                     'C4_ratio': k4/(C4*t**4),
                     'C6_ratio': k6/(C6*t**6),
                     'n_kl1_diagonal': 1/k4, 'n_kl1_signs': 1/k6})
    # Independent direct discrete convolution rather than Fourier analytic law.
    theta, analytic, _ = density(c+.12, c-.24)
    pa = np.exp((c+.12)*np.cos(theta))/(2*np.pi*iv(0, c+.12))
    pb = np.exp((c-.24)*np.cos(theta))/(2*np.pi*iv(0, c-.24))
    convolution = np.fft.ifft(np.fft.fft(pa)**2*np.fft.fft(pb)).real*(2*np.pi/len(theta))**2
    # The first derivative is structurally zero for every Fourier coefficient.
    deriv = log_bessel_derivatives(np.arange(1, 65), c)
    null_derivative = 2*deriv[0]-2*deriv[0]
    # Numerical Taylor check by symmetric differences, independent of KL.
    h = .001
    _, ph, _ = density(c+h, c-2*h)
    _, pnh, _ = density(c-h, c+2*h)
    est_A, est_B = (ph+pnh-2*p0)/(2*h*h), (ph-pnh)/(2*h**3)
    checks.append({'c': c, 'convolution_sup_error': float(np.max(np.abs(convolution-analytic))),
                   'null_derivative_max': float(np.max(np.abs(null_derivative))),
                   'A_taylor_relative_error': float(np.linalg.norm(est_A-A)/np.linalg.norm(A)),
                   'B_taylor_relative_error': float(np.linalg.norm(est_B-B)/np.linalg.norm(B)),
                   'density_min': float(p0.min())})

fits = []
for c in (1., 2., 4.):
    sub = [r for r in rows if r['c'] == c and r['t'] <= .08]
    for key in ('kl_to_diagonal', 'kl_between_signs'):
        selected = [r for r in sub if r[key] > 1e-13]
        slope = np.polyfit(np.log([r['t'] for r in selected]),
                           np.log([r[key] for r in selected]), 1)[0] if len(selected)>1 else None
        fits.append({'c': c, 'quantity': key, 'small_t_log_slope': slope, 'points': len(selected)})

lrt, skipped = [], []
used = 0
CAP = 2_000_000
for t in (.08, .12, .16):
    row = next(r for r in rows if r['c'] == 2. and r['t'] == t)
    for typ, key in [('diagonal', 'kl_to_diagonal'), ('signs', 'kl_between_signs')]:
        n = int(np.ceil(1/row[key]))
        required = n*24  # 12 seeds, 2 true laws.
        if required+used > CAP:
            skipped.append({'t': t, 'contrast': typ, 'n_per_law_seed': n,
                            'required_pairs': required, 'reason': 'prerecorded two-million-pair cap'})
            continue
        alt = (2., 2.) if typ == 'diagonal' else (2-t, 2+2*t)
        for phase, seeds in [('primary', range(3401, 3407)), ('confirmation', range(9401, 9407))]:
            for seed in seeds:
                pos = sample_loglr(2+t, 2-2*t, *alt, n, seed)
                neg = sample_loglr(*alt, 2+t, 2-2*t, n, seed+100000)
                lrt.append({'t': t, 'contrast': typ, 'phase': phase, 'seed': seed, 'n': n,
                            'true_plus_loglr': pos, 'true_alt_loglr_favors_alt': neg,
                            'correct_plus': int(pos > 0), 'correct_alt': int(neg > 0)})
        used += required

for name, data in [('population', rows), ('convergence', convergence), ('checks', checks), ('slopes', fits), ('lrt', lrt)]:
    if data:
        with (OUT/f'{name}.csv').open('w') as f:
            w = csv.DictWriter(f, fieldnames=list(data[0])); w.writeheader(); w.writerows(data)
summary = {'environment': {'python': platform.python_version(), 'numpy': np.__version__, 'scipy': scipy.__version__},
           'population_conditions': len(rows), 'checks': checks, 'slopes': fits,
           'lrt_runs': len(lrt), 'generated_pair_count': used, 'skipped_lrt': skipped,
           'minimum_population_kl': min(r['kl_between_signs'] for r in rows)}
(OUT/'summary.json').write_text(json.dumps(summary, indent=2))
print(json.dumps(summary, indent=2))

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
fig, ax = plt.subplots(1, 2, figsize=(9, 3.5))
for c in (1., 2., 4.):
    sub = [r for r in rows if r['c'] == c]
    ts = np.array([r['t'] for r in sub])
    for a, key, power in [(ax[0], 'kl_to_diagonal', 4), (ax[1], 'kl_between_signs', 6)]:
        ys = [r[key] for r in sub]
        a.loglog(ts, ys, 'o-', label=f'c={c:g}')
        const = sub[0]['C4' if power == 4 else 'C6']
        a.loglog(ts, const*ts**power, '--', alpha=.4)
for a, title in zip(ax, ['Null path versus equal channels', 'Opposite signs along null path']):
    a.set(xlabel='perturbation t', ylabel='population KL per pair', title=title)
    a.set_xticks([.02, .04, .08, .16], labels=['0.02', '0.04', '0.08', '0.16'])
    a.xaxis.set_minor_locator(matplotlib.ticker.NullLocator())
    a.grid(alpha=.2); a.legend()
fig.tight_layout()
plot_tmp = OUT/'singular_kl.tmp.png'
fig.savefig(plot_tmp, dpi=150)
plt.close(fig)
plot_tmp.replace(OUT/'singular_kl.png')
