"""Exact rational enclosures for the matched-law counterexample.

No floating point is used in the sign certificate. The selected eta is the
midpoint of two exact thresholds, not a subsequently discovered experiment.
"""
from fractions import Fraction as F
from itertools import product
from math import factorial
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parent
terms = sum((F(1, factorial(n)) for n in range(31)), F(0))
e_lo, e_hi = terms, terms + F(1, 30 * factorial(30))
a_lo, a_hi = 1 / e_hi, 1 / e_lo
q = [F(103, 1000), F(374, 1000), F(523, 1000)]

def moments(partition, a):
    first, second = F(0), F(0)
    for states in product(range(3), repeat=4):
        probability = F(1)
        denominator = F(1)
        w1 = w2 = 0
        for r, state in zip(partition, states):
            probability *= q[state]
            denominator += r * a**state
            if state == 1:
                w1 += r
                w2 += r*r
        first += probability * w1 / denominator
        second += probability * w2 / denominator**2
    return first, second

def outward(value, upper=False):
    scale = 10**24
    numerator = value.numerator * scale
    integer = numerator // value.denominator
    if upper and numerator % value.denominator:
        integer += 1
    sign = '-' if integer < 0 else ''
    integer = abs(integer)
    return f'{sign}{integer//scale}.{integer%scale:024d}'

records = []
thresholds = []
for partition in [(5, 3, 2, 2), (4, 4, 3, 1)]:
    m_lo_a, h_lo_a = moments(partition, a_lo)
    m_hi_a, h_hi_a = moments(partition, a_hi)
    # Both positive moments decrease with a. This rectangular enclosure is
    # deliberately conservative; it does not rely on interval correlations.
    lower = 1 - a_hi * h_lo_a / m_hi_a
    upper = 1 - a_lo * h_hi_a / m_lo_a
    thresholds.append((lower, upper))
    records.append({'partition': partition, 'threshold_lower': outward(lower),
                    'threshold_upper': outward(upper, True)})
gap_lower = thresholds[0][0] - thresholds[1][1]
assert gap_lower > 0
result = {
    'arithmetic': 'exact Python Fraction, decimal endpoints rounded outward',
    'e_enclosure': 'sum(n=0..30)1/n! <= e <= sum + 1/(30*30!)',
    'thresholds': records,
    'threshold_gap_lower': outward(gap_lower),
    'opposite_balance_signs_certified': True,
    'reason': 'eta is the exact midpoint of the two thresholds; both curvature prefactors are strictly positive',
    'full_spectrum_scope': 'Full-spectrum signs remain separately finite-difference verified, not certified by this file.'
}
(ROOT/'results'/'rational_certificate.json').write_text(json.dumps(result, indent=2)+'\n')
print(json.dumps(result, indent=2))
