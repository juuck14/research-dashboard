"""Regenerate the figure from recorded population CSV, without rerunning data."""
from pathlib import Path
import csv
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

out = Path(__file__).resolve().parent/'results'
rows = [{k:float(v) for k,v in r.items()} for r in csv.DictReader((out/'population.csv').open())]
fig, axes = plt.subplots(1, 2, figsize=(9, 3.5))
for c in (1., 2., 4.):
    sub = [r for r in rows if r['c'] == c]
    ts = np.array([r['t'] for r in sub])
    for ax, key, power, constant in [(axes[0], 'kl_to_diagonal', 4, 'C4'), (axes[1], 'kl_between_signs', 6, 'C6')]:
        ax.loglog(ts, [r[key] for r in sub], 'o-', label=f'c={c:g}')
        ax.loglog(ts, sub[0][constant]*ts**power, '--', alpha=.4)
for ax, title in zip(axes, ['Null path versus equal channels', 'Opposite signs along null path']):
    ax.set(xlabel='perturbation t', ylabel='population KL per pair', title=title)
    ax.set_xticks([.02, .04, .08, .16], labels=['0.02', '0.04', '0.08', '0.16'])
    ax.xaxis.set_minor_locator(matplotlib.ticker.NullLocator())
    ax.grid(alpha=.2); ax.legend()
fig.tight_layout()
tmp = out/'singular_kl.tmp.png'
fig.savefig(tmp, dpi=150)
plt.close(fig)
tmp.replace(out/'singular_kl.png')
