"""Independent exact-rational interval reconstruction; imports no project code."""
from fractions import Fraction as F
from math import comb, factorial
from decimal import Decimal, localcontext
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parent


class Bound:
    def __init__(self, lo, hi=None):
        self.lo = F(lo)
        self.hi = F(lo if hi is None else hi)

    def __add__(self, other):
        if not isinstance(other, Bound): other = Bound(other)
        return Bound(self.lo+other.lo, self.hi+other.hi)
    __radd__ = __add__

    def __neg__(self): return Bound(-self.hi, -self.lo)
    def __sub__(self, other): return self+-coerce(other)
    def __rsub__(self, other): return coerce(other)+-self

    def __mul__(self, other):
        other = coerce(other)
        values = [a*b for a in [self.lo, self.hi] for b in [other.lo, other.hi]]
        return Bound(min(values), max(values))
    __rmul__ = __mul__

    def __truediv__(self, other):
        other = coerce(other)
        assert other.lo > 0
        return self*Bound(1/other.hi, 1/other.lo)
    def __rtruediv__(self, other): return coerce(other)/self

    def serial(self):
        # These decimals display exact-rational bounds; validity of sign tests
        # below uses Fractions directly, not their rounded display.
        with localcontext() as context:
            context.prec = 55
            return {'lower_display': str(Decimal(self.lo.numerator)/Decimal(self.lo.denominator)),
                    'upper_display': str(Decimal(self.hi.numerator)/Decimal(self.hi.denominator)),
                    'exact_width_float': float(self.hi-self.lo)}


def coerce(value): return value if isinstance(value, Bound) else Bound(value)


def main():
    terms = 70
    e_lo = sum((F(1, factorial(j)) for j in range(terms+1)), F(0))
    e = Bound(e_lo, e_lo+F(1, terms*factorial(terms)))
    a, b = 1/e, (1/e)*(1/e)
    log_terms = 90
    x = F(1, 3)
    log_lo = 4*sum((x**(2*j+1)/F(2*j+1) for j in range(log_terms+1)), F(0))
    log_hi = log_lo+4*x**(2*log_terms+3)/F(2*log_terms+3)/(1-x*x)
    eta = F(112, 187)*Bound(log_lo, log_hi)
    rows = []
    for k in [4, 5, 11, 12]:
        b0 = b1 = b2 = m1 = m2 = Bound(0)
        for u in range(k+1):
            for n in range(k-u+1):
                w = k-u-n
                probability = (comb(k, u)*comb(k-u, n)*F(103,1000)**u *
                               F(374,1000)**n*F(523,1000)**w)
                d = 1+u+a*n+b*w
                b0 = b0+probability*u/d
                b1 = b1+probability*a*n/(2*d)
                b2 = b2+probability*b*w/d
                m1 = m1+probability*n/d
                m2 = m2+probability*n/(d*d)
        total = b0+2*b1+b2
        xi = (b0-b2)/total
        margin = 1-a*m2/m1-eta
        gap_margin = F(1,20)-xi
        rows.append({'K':k, 'xi':xi.serial(), 'balance_margin':margin.serial(),
                     'gap_margin':gap_margin.serial()})
        if k == 4: assert margin.hi < 0
        if k == 5: assert margin.lo > 0
        if k == 11: assert gap_margin.lo > 0
        if k == 12: assert gap_margin.hi < 0
    output = {'e_factorial_terms': terms+1, 'log4_atanh_terms':log_terms+1,
              'arithmetic':'exact rational interval operations; signs tested before decimal display',
              'imports_project_code':False, 'passed':True, 'rows':rows,
              'scope':'Certifies K4/5 lower and K11/12 upper brackets. All-K claim additionally uses the two analytic monotonicity proofs.'}
    (ROOT/'window_certificate_check.json').write_text(json.dumps(output, indent=2)+'\n')
    print(json.dumps(output, indent=2))


if __name__ == '__main__': main()
