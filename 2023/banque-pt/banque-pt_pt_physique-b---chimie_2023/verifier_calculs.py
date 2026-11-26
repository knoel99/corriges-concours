"""Vérifications numériques du corrigé de chimie Banque PT 2023."""
from math import exp, isclose, log, log10, sqrt
from statistics import linear_regression


def proche(calcul, attendu, tolerance):
    assert abs(calcul - attendu) < tolerance, (calcul, attendu)


def main():
    print("Sites octaédrique et tétraédrique (pm)")
    octa, tetra = 420/2-140, sqrt(3)*420/4-140
    assert octa == 70
    proche(tetra, 41.87, .01)
    print(octa, tetra)
    temps_1 = [0, 20, 40, 60, 80]
    oxydant_1 = [10.8, 6.71, 4.17, 2.59, 1.61]
    r1 = linear_regression(temps_1, [log(v) for v in oxydant_1])
    temps_2 = [0, 40, 160, 270, 450]
    chrome_2 = [0, 2.87, 6.16, 7.31, 8.19]
    r2 = linear_regression(temps_2, [1/(.010-v/1000) for v in chrome_2])
    proche(r1.slope, -.0238, .00005)
    proche(r1.intercept, 2.3795, .00005)
    proche(r2.slope, 1.0057, .00005)
    proche(r2.intercept, 99.924, .0005)
    k1, k2 = -.5*r1.slope, .5*r2.slope
    gamma = log(.080*k2/(1.5*k1))/log(.405/.270)
    proche(gamma, 2, .01)
    assert isclose(k1/(.080*.270**2), k2/(1.5*.405**2), rel_tol=.003)
    print("Ajustements des tableaux 1 et 2, ordre en protons", r1, r2, gamma)
    dh = 3*(-240) - (-1140)
    ds = 2*25 + 3*190 - 80 - 3*130
    dg = dh - 1300*ds/1000
    assert (dh, ds, dg) == (420, 150, 225)
    k = exp(-1000*dg/(8.3*1300))
    proche(k, 1e-9, 2e-10)
    ratio = (1e-9)**(1/3)
    xi = .1*ratio/(3*(1+ratio))
    assert (3*xi/(.1-3*xi))**3 < 1.001e-9
    assert isclose((3*xi/(.1-3*xi))**3, 1e-9, rel_tol=1e-12)
    assert xi < .0005
    print("Équilibre, constante et quantités de matière (mol)", k, xi, 2*xi)
    e = 1.33 + .06/6*log10(1/.06) - .77
    proche(e, .57, .003)
    proche(6*(1.33-.77)/.06, 56, 1e-8)
    fer2 = .060
    xi_pile = fer2/6
    fin = (.060+6*xi_pile, .060-xi_pile, .060+2*xi_pile)
    assert all(isclose(x,y) for x,y in zip(fin,(.120,.050,.080)))
    print("Pile, f.é.m., solutés finaux et charge (C)", e, fin, 6*96500*xi_pile)
    conc = [i/100 for i in range(1,11)]
    absorb = [.122,.242,.375,.488,.616,.728,.851,.974,1.089,1.203]
    r3 = linear_regression(conc, absorb)
    proche(r3.slope, 12.033, .0005)
    proche(r3.intercept, .007, 1e-9)
    sample = (.620-r3.intercept)/r3.slope
    cuivre_mg = 1000*sample*.005*64
    zinc_pct = 100*(1-cuivre_mg/24)
    proche(zinc_pct, 32, .2)
    print("Étalonnage, cuivre (mg), zinc (%)", r3, cuivre_mg, zinc_pct)
    argent = 10**(2*(.80-.34)/.06)
    assert 2e15 < argent < 2.3e15
    print("Équilibre cuivre–argent", argent)


if __name__ == "__main__":
    main()
