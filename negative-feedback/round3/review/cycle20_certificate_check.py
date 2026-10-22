"""Exact-rational no-self-positive control; no scientific project-code import."""
from fractions import Fraction as F
from math import comb, factorial, isqrt
from pathlib import Path
import json
from window_certificate_check import Bound


def sqrt_enclosure(value, digits=80):
    scale = 10**digits
    floor = isqrt(value.numerator*scale*scale//value.denominator)
    return Bound(F(floor, scale), F(floor+1, scale))


def main():
    sqrt5 = sqrt_enclosure(F(5))
    inside = 10+2*sqrt5
    outer = Bound(sqrt_enclosure(inside.lo).lo, sqrt_enclosure(inside.hi).hi)
    gap = 1-outer/4
    n = 70
    e0 = sum((F(1, factorial(j)) for j in range(n+1)), F(0))
    e = Bound(e0, e0+F(1, n*factorial(n)))
    a, b = 1/e, (1/e)*(1/e)
    rows = []
    for k in [11, 12]:
        b0 = b1 = b2 = Bound(0)
        for u in range(k+1):
            for nn in range(k-u+1):
                w = k-u-nn
                probability = (comb(k,u)*comb(k-u,nn)*F(103,1000)**u *
                               F(374,1000)**nn*F(523,1000)**w)
                d = 1+u+a*nn+b*w
                b0 = b0+probability*u/d
                b1 = b1+probability*a*nn/(2*d)
                b2 = b2+probability*b*w/d
        xi = (b0-b2)/(b0+2*b1+b2)
        margin = gap-xi
        if k == 11: assert margin.lo > 0
        if k == 12: assert margin.hi < 0
        rows.append({'K':k, 'xi':xi.serial(), 'cycle_gap_minus_xi':margin.serial()})
    output = {'positive_graph':'simple cycle on20 views per class, neighbor weights1/2',
              'positive_self_probability':0, 'gap':gap.serial(),
              'rows':rows, 'passed':True,
              'scope':'With previously certified lower boundary and the two monotonicity proofs, the exact full window remains K5..11. This is not a new graph spectral principle.'}
    path = Path(__file__).resolve().parent/'cycle20_certificate_check.json'
    path.write_text(json.dumps(output, indent=2)+'\n')
    print(json.dumps(output, indent=2))


if __name__ == '__main__': main()
