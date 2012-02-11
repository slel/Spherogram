import sys
sys.path.append('/Users/dunfield/work/SnapPy/dev')
sys.path.append('/Users/dunfield/work/python')
import snappy, ntools, census, lookup, nsagetools
from tangles import RationalTangle

knots = ntools.DataInFile('montesinos_knots')

def count_hyperbolic():   # ANS: 167
    knot_exteriors = [snappy.Manifold(K[0]) for K in knots]
    return len([M for M in knot_exteriors if census.appears_hyperbolic(M)])

def knot(fractions):
    if len(fractions) == 1:
        return RationalTangle(*fractions[0]).denominator_closure()
    else:
        A, B, C = [RationalTangle(*f) for f in fractions]
        T = A + B + C
        return T.numerator_closure()

def test_knot( (K, fractions) ):
    M = knot(fractions).exterior()
    if census.appears_hyperbolic(M):
        N = lookup.LinkExteriorDB.identify(M)
        assert N.name() == K
        return 1
    return 0 

def first_test():
    total = 0
    for K in knots:
        total += test_knot(K)
    assert totat == 167

mathematica.execute('<<KnotTheory`')
mathematica.execute('Off[KnotTheory::loading]')
mathematica.execute('Off[KnotTheory::credits]')
mathematica.execute('MyAlex[L_] := CoefficientList[t^100*Alexander[L][t], t]')

def alex_by_KnotTheory(L):
    p = mathematica.MyAlex(L.PD_code(True)).sage()
    i = min( [i for i,c in enumerate(p) if c != 0])
    R = PolynomialRing(ZZ, 'a')
    return R(p[i:])

def alex_match(L):
    p1 = alex_by_KnotTheory(L)
    p2 = nsagetools.alexander_polynomial(L.exterior())
    return 0 in [p1 - p2, p1 + p2]

def second_test():
    for K, fractions in knots:
        L = knot(fractions)
        assert alex_match(L)

# first_test()