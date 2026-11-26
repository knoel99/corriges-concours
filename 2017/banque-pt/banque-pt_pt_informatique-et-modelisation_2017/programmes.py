from math import isclose


# Q25
def vitesse_moteur(tdent):
    if tdent <= 0:
        raise ValueError("La durée entre fronts doit être positive")
    return 60 / (120 * tdent)


# Q31
def indice(A, val):
    if len(A) < 2 or not A[0] <= val < A[-1]:
        raise ValueError("Valeur hors des intervalles de la table")
    bas, haut = 0, len(A) - 1
    while haut - bas > 1:
        milieu = (bas + haut) // 2
        if A[milieu] <= val:
            bas = milieu
        else:
            haut = milieu
    return bas


# Q32
def extraire(T, P, Nm, i, j):
    return [[T[i][j], T[i][j + 1], P[j], Nm[i]],
            [T[i + 1][j], T[i + 1][j + 1], P[j + 1], Nm[i + 1]]]


# Q33
def sous_table(T, P, Nm, Pcol, Nmot):
    i = indice(Nm, Nmot)
    j = indice(P, Pcol)
    ST = extraire(T, P, Nm, i, j)
    return ST


# Q34
def gauss(A, c):
    n = len(c)
    M = [list(ligne) for ligne in A]
    rhs = list(c)
    if len(M) != n or any(len(ligne) != n for ligne in M):
        raise ValueError("Système carré requis")
    for k in range(n):
        pivot = max(range(k, n), key=lambda i: abs(M[i][k]))
        if M[pivot][k] == 0:
            raise ValueError("Matrice singulière")
        M[k], M[pivot] = M[pivot], M[k]
        rhs[k], rhs[pivot] = rhs[pivot], rhs[k]
        for i in range(k + 1, n):
            facteur = M[i][k] / M[k][k]
            M[i][k] = 0
            for j in range(k + 1, n):
                M[i][j] -= facteur * M[k][j]
            rhs[i] -= facteur * rhs[k]
    b = [0.0] * n
    for i in range(n - 1, -1, -1):
        suite = sum(M[i][j] * b[j] for j in range(i + 1, n))
        b[i] = (rhs[i] - suite) / M[i][i]
    return b


# Q37
def interpol(ST, Pcol, Nmot):
    a, b, p0, n0 = ST[0]
    c, d, p1, n1 = ST[1]
    x = (Pcol - p0) / (p1 - p0)
    y = (Nmot - n0) / (n1 - n0)
    return a + (b - a)*x + (c - a)*y + (d - b - c + a)*x*y


# Q38
def sonde(r):
    return 0.1 if r <= 1 else 0.9


# Q39
def duree_injection(Usonde, Kpp, Kpn, Ki, tinjc0, integi, dt):
    croissance = Usonde <= 0.5
    signe = 1 if croissance else -1
    if signe * integi < 0:
        integi = 0.0
    integrale = integi + signe * Ki * tinjc0 * dt
    proportion = tinjc0 * (Kpp if croissance else Kpn)
    return proportion + integrale, integrale


# Q41
def Euler(tau, K, dt, si, ei):
    return si + dt * (K * ei - si) / tau


# Q42
def richesse(tau1, tau2, K, dt, ri, wi, tinji):
    suivant_w = Euler(tau1, K, dt, wi, tinji)
    suivant_r = Euler(tau2, 1, dt, ri, wi)
    return suivant_r, suivant_w


# Q44
Tcycle = 60 / (4000 * 2)
dt = 2e-6
t0 = 0.0
tn = 100 * Tcycle


def base_temps(debut, fin, pas):
    intervalles = round((fin - debut) / pas)
    if pas <= 0 or intervalles < 0 or not isclose(debut + intervalles*pas, fin):
        raise ValueError("Les bornes doivent être espacées d'un nombre entier de pas")
    return [debut + i * pas for i in range(intervalles + 1)]


# Q45
def simuler(temps, dt, Tcycle, tau1, tau2, K, Kpp, Kpn, Ki, tinjc0):
    periode = round(Tcycle / dt)
    if periode < 1 or not isclose(periode * dt, Tcycle):
        raise ValueError("Nombre entier de pas par lecture requis")
    w = 0.9
    integ = 0.0
    liste_richesse = [0.9]
    liste_tinj = [tinjc0]
    liste_U = [sonde(liste_richesse[0])]
    for i in range(len(temps) - 1):
        r, w = richesse(tau1, tau2, K, dt, liste_richesse[i], w, liste_tinj[i])
        tinj, integ = duree_injection(liste_U[i], Kpp, Kpn, Ki, tinjc0, integ, dt)
        u = sonde(r) if (i + 1) % periode == 0 else liste_U[i]
        liste_richesse.append(r)
        liste_tinj.append(tinj)
        liste_U.append(u)
    return liste_richesse, liste_tinj, liste_U


def simulation_sujet():
    temps = base_temps(t0, tn, dt)
    tinjc0 = 0.0123
    donnees = simuler(temps, dt, Tcycle, 10*Tcycle, 20*Tcycle, 1/tinjc0,
                      1.03, 0.95, 0.8, tinjc0)
    return temps, *donnees


# Q46
def tracer(temps, liste_richesse):
    from matplotlib import pyplot as plt
    fig, ax = plt.subplots()
    ax.plot(temps, liste_richesse, label="richesse")
    ax.set_xlabel("Temps (s)")
    ax.set_ylabel("Richesse du mélange")
    ax.grid()
    ax.legend()
    return fig, ax


if __name__ == "__main__":
    from matplotlib import pyplot
    temps, liste_richesse, liste_tinj, liste_U = simulation_sujet()
    tracer(temps, liste_richesse)
    pyplot.show()
