"""Rational bounds for a zero-self-positive corollary of Theorem V1.

This verifies only the cycle gap bracket. The xi11/xi12 and balance
certificates live in their respective owners' directories.
Run: python negative-feedback/round3/journal/zero_self_cycle_certificate.py
"""
from fractions import Fraction as F
from pathlib import Path
import json

inner_lo, inner_hi = F(22360, 10000), F(22361, 10000)
outer_lo, outer_hi = F(38040, 10000), F(38044, 10000)
assert inner_lo**2 < 5 < inner_hi**2
assert outer_lo**2 < 10 + 2 * inner_lo
assert 10 + 2 * inner_hi < outer_hi**2
gap_lo, gap_hi = 1 - outer_hi / 4, 1 - outer_lo / 4
assert gap_lo == F(489, 10000)
assert gap_hi == F(49, 1000)
assert F(486, 10000) < gap_lo < gap_hi < F(52, 1000)
result = {
    "positive_graph": "unweighted undirected cycle with 20 vertices; P(i,i+-1)=1/2",
    "self_positive_probability": 0,
    "gap_exact": "1-sqrt(10+2*sqrt(5))/4",
    "gap_strict_rational_bounds": [str(gap_lo), str(gap_hi)],
    "comparisons": "xi11 < .0486 < gap < .0490 < .0520 < xi12, using separate xi certificates",
    "result": "Theorem V1 plus the prior K4/5 and K11/12 certificates gives full local attraction exactly K5..11",
    "scope": "This is a derived corollary, not an executed 80-node network experiment or a new independent contribution",
    "passed": True,
}
out = Path(__file__).resolve().parent / "zero_self_cycle_certificate.json"
out.write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps(result, indent=2))
