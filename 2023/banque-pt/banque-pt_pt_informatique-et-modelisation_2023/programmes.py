import numpy as np
import matplotlib.pyplot as plt


# Q20
def somme(a):
    total = 0
    for valeur in a:
        total += valeur
    return total


# Q21
def moyenne(a):
    return somme(a) / len(a)


# Q22
def variance(a):
    centre = moyenne(a)
    ecart_carre = 0.0
    for valeur in a:
        ecart_carre += (valeur - centre) ** 2
    return ecart_carre / len(a)


# Q24
def regression_lineaire(x, y):
    if len(x) != len(y):
        raise ValueError("Les deux listes doivent avoir la même taille.")
    xm, ym = moyenne(x), moyenne(y)
    numerateur = denominateur = 0.0
    for xi, yi in zip(x, y):
        dx = xi - xm
        numerateur += dx * (yi - ym)
        denominateur += dx * dx
    if denominateur == 0:
        raise ValueError("Il faut au moins deux abscisses distinctes.")
    a1 = numerateur / denominateur
    return ym - a1 * xm, a1


# Q26
def tracer_regression(f, U):
    """Fréquences en Hz, mesures numériques U déjà exprimées en µV."""
    a0, a1 = regression_lineaire(f, U)
    bornes = [min(f), max(f)]
    fig, ax = plt.subplots()
    ax.plot(f, U, 'o', label='Mesures')
    ax.plot(bornes, [a0 + a1 * x for x in bornes], label='Ajustement')
    ax.set_xlabel('Fréquence (Hz)')
    ax.set_ylabel('Tension (µV)')
    ax.legend()
    return fig, ax

# Pour les listes f et U du sujet : tracer_regression(f, U), puis plt.show().


# Q27
def traitement(a):
    return [[moyenne(ligne), variance(ligne)] for ligne in a]


# Q28
def regression_lineaire_gen(x, yv, listf):
    n, m = len(x), len(listf)
    if len(yv) != n or not 0 < m < n:
        raise ValueError("Il faut n observations et 0 < m < n.")
    J = np.empty((n, m))
    y = np.empty(n)
    for i, (xi, (yi, vi)) in enumerate(zip(x, yv)):
        if vi <= 0:
            raise ValueError("Les variances doivent être positives.")
        y[i] = yi / vi
        for j, fonction in enumerate(listf):
            J[i, j] = fonction(xi) / vi
    # La division de chaque ligne par vi produit le poids 1 / vi**2.
    return np.linalg.solve(J.T @ J, J.T @ y)


# Q32
def aire(x, y):
    if len(x) != len(y):
        raise ValueError("Les deux listes doivent avoir la même taille.")
    total = 0.0
    for i in range(1, len(x)):
        largeur = x[i] - x[i - 1]
        if largeur <= 0:
            raise ValueError("Les abscisses doivent être croissantes.")
        total += largeur * (y[i] + y[i - 1]) / 2
    return total


# Q34
def G(f, a0, a1):
    return a0 / (a1**2 + f**2)


def dG_da0(f, a0, a1):
    return 1 / (a1**2 + f**2)


def dG_da1(f, a0, a1):
    return -2 * a0 * a1 / (a1**2 + f**2)**2


# Q36
def methode_gradient(G, dG_da0, dG_da1, Su, f, h, a00, a10, err):
    if len(Su) != len(f) or h <= 0 or err <= 0:
        raise ValueError("Tailles incompatibles, pas ou tolérance invalide.")
    a0, a1 = a00, a10
    for _ in range(100_000):
        g0 = g1 = 0.0
        for fi, si in zip(f, Su):
            residu = G(fi, a0, a1) - si
            g0 += 2 * residu * dG_da0(fi, a0, a1)
            g1 += 2 * residu * dG_da1(fi, a0, a1)
        d0, d1 = h * g0, h * g1
        amplitude = abs(d0) + abs(d1)
        if not np.isfinite(amplitude):
            raise ArithmeticError("La descente a divergé.")
        if amplitude <= err:
            return a0, a1
        a0, a1 = a0 - d0, a1 - d1
    raise RuntimeError("Le critère d’arrêt n’a pas été atteint.")


# Q38
def configurer_force(U, gamma, T, err):
    """Fixe la tension en V, le frottement en kg/s, T en K et la tolérance."""
    if gamma <= 0 or T <= 0 or err <= 0:
        raise ValueError("Le frottement, T et la tolérance doivent être positifs.")
    kB = 1.380649e-23

    def force(Su, f, h, a00, a10):
        A = aire(f, Su)
        if A <= 0 or a10 == 0:
            raise ValueError("Il faut A > 0 et une fréquence initiale non nulle.")
        _, a1 = methode_gradient(G, dG_da0, dG_da1, Su, f, h, a00, a10, err)
        fc = abs(a1)
        return U * np.sqrt(2 * np.pi * gamma * kB * T * fc / A)

    return force

# Avec les paramètres expérimentaux : force = configurer_force(U, gamma, T, err).
# La force en newtons est alors force(Su, f, h, a00, a10).
