"""Solutions exécutables, Banque PT 2024, informatique et modélisation."""
from math import ceil, isclose
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


# Q23
def volume(L, l, h):
    return L * l * h


# Q24
def nbre_ffu(V, Q, tx_renew):
    return ceil(V * tx_renew / Q)


# Q27
def repartition(L, l, n):
    nx, ny = n, 1
    u = (L - nx) / (nx + 1)
    v = (l - ny) / (ny + 1)
    while u < 1 and ny < n:
        ny += 1
        nx = n // ny
        u = (L - nx) / (nx + 1)
        v = (l - ny) / (ny + 1)
    if n < 1 or u < 1 or v < 0:
        raise ValueError("Aucune implantation admissible")
    return nx, ny, u, v


# Q28
def remplace_virgule_par_point(chaine):
    return chaine.replace(",", ".")


# Q29
def lire_colonnes(chemin_fichier):
    Ltemps, Lconsigne, Lvitesse, Lcourant = [], [], [], []
    with open(chemin_fichier, encoding="utf-8-sig") as fichier:
        for _ in range(13):
            next(fichier)
        for ligne in fichier:
            liste = remplace_virgule_par_point(ligne).split("\t")
            Ltemps.append(float(liste[0]))
            Lconsigne.append(float(liste[1]))
            Lvitesse.append(float(liste[2]))
            Lcourant.append(float(liste[3]))
    return Ltemps, Lconsigne, Lvitesse, Lcourant


# Q30
def extraction_resultats_essai(nom_fichier):
    t, c, v, i = lire_colonnes(nom_fichier)
    dico = {"temps": t, "consigne": c, "vitesse": v, "courant": i}
    return dico


# Q32
def affichage(donnees):
    fig, ax = plt.subplots()
    courbe, = ax.plot(donnees["temps"], donnees["vitesse"])
    ax.set(xlabel="Temps (s)", ylabel="Vitesse (tr/min)")
    return courbe


# Q33
def moyenne_sur_intervalle(Liste, deb, fin):
    if not 0 <= deb < fin <= len(Liste):
        raise ValueError("Intervalle vide ou hors de la liste")
    return sum(Liste[deb:fin]) / (fin - deb)


# Q34
def point_de_fonctionnement(donnees):
    N = moyenne_sur_intervalle(donnees["vitesse"], 500, 701)
    I = moyenne_sur_intervalle(donnees["courant"], 500, 701)
    return N, 0.13 * I


# Q35
def analyse_essais(dossier="."):
    L_vit, L_Cr = [], []
    for j in range(1, 19):
        nom = Path(dossier) / f"essai{j}.txt"
        N, Cr = point_de_fonctionnement(extraction_resultats_essai(nom))
        L_vit.append(N)
        L_Cr.append(Cr)
    return L_vit, L_Cr


# Q38
def matrice_explicative(V_N2):
    x = np.asarray(V_N2, dtype=float).reshape(-1, 1)
    return np.hstack((x, np.ones((len(x), 1))))


# Q39
def modele(X, theta):
    return X @ theta


# Q42
def cout(X, Y, theta):
    r = modele(X, theta) - Y
    return float(np.sum(r * r))


# Q45
def gradient(X, Y, theta):
    return 2 * X.T @ (modele(X, theta) - Y)


# Q46
def descente_gradient(X, Y, theta_init, alpha, n):
    theta = np.array(theta_init, dtype=float, copy=True)
    for _ in range(n):
        theta = theta - alpha * gradient(X, Y, theta)
    return theta


# Q47
def affichage_couple(a0, a1):
    w = np.arange(0, 251, 10)
    fig, ax = plt.subplots()
    courbe, = ax.plot(w, a1 * w**2 + a0)
    ax.set(xlabel="Vitesse (rad/s)", ylabel="Couple (N m)")
    return courbe


# Q48
def f(w, U):
    return 5.3e-6 * w**2 + 0.05 - 0.839 * (U - 1.17 * w)


def dichotomie(U, deb, fin, e):
    if e <= 0 or deb > fin:
        raise ValueError("Intervalle ou precision incorrect")
    fd, ff = f(deb, U), f(fin, U)
    if fd == 0:
        return deb, U
    if ff == 0:
        return fin, U
    if fd * ff > 0:
        raise ValueError("Changement de signe requis")
    while fin - deb > 2 * e:
        milieu = (deb + fin) / 2
        fm = f(milieu, U)
        if fm == 0:
            return milieu, U
        if fd * fm < 0:
            fin = milieu
        else:
            deb, fd = milieu, fm
    return (deb + fin) / 2, U


# Q52
def Euler_Explicite(g, w0, t0, t1, T):
    if T <= 0 or t1 < t0:
        raise ValueError("Bornes ou pas incorrects")
    LT, Lw = [t0], [w0]
    i = 0
    while LT[-1] < t1:
        i += 1
        suivant = min(t0 + i * T, t1)
        if isclose(suivant, t1, rel_tol=0, abs_tol=1e-12 * T):
            suivant = t1
        dt = suivant - LT[-1]
        Lw.append(Lw[-1] + dt * g(Lw[-1], LT[-1]))
        LT.append(suivant)
    return LT, Lw


# Q53
def caracteristiques(LT, Lw):
    # Le dernier point est pris sur un plateau établi.
    w_inf = Lw[-1]
    largeur = 0.05 * abs(w_inf)
    i = len(Lw) - 1
    while i > 0 and abs(Lw[i - 1] - w_inf) <= largeur:
        i -= 1
    return LT[i] - LT[0], w_inf
