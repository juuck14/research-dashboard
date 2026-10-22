# Endpoint falsification of the old semantic-loss interpretation

**Status: original interpretation rejected; auxiliary local results retained.** See the [preregistered analyses and flow extension](protocol.md), [nonlinear branch code](run.py), [actual flow code](flow.py), and [coarse-attractor proof](coarse_cluster_lemma.md).

At K4, the old balanced square is unstable but an attracting rectangular geometry has weak-factor energy.46914073346 rather than.5. It remains injective. With the declared Gaussian measurement noise sigma.2, optimal weak-factor accuracy is.99969225 rather than.99979652. Calling this a semantic-erasure boundary is unsupported.

K1 has a genuinely coarse attracting manifold. Its full tangent spectrum and open local basin can be proved, but the first-score sampler response vanishes there. It is not an exclusively adaptive-feedback collapse. A stable coarse endpoint does not establish large probability of reaching it from an arbitrary initialization.

The 24actual near-reference flows (K1/4/5/8 ×6seeds) all meet the endpoint-distance criterion. See [branches](results/branches.csv), [raw flow rows](results/endpoint_flows.csv), [summary](results/flow_summary.json). K1 finite-time weak energy around8.3e-20 is not mathematically exact zero information at finite time. Exact collapse concerns the limiting attractor. Independent direct-tuple checks are in [review](../review/endpoint_check.py).

This result changed the proposed paper: the representative question is now finite-count local feasibility, not an information-loss transition. The old endpoint analysis is a falsification, not a success arm selected for the revised paper.
