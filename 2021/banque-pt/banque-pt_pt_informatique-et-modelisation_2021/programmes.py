"""Banque PT 2021. Les appels matériels de Q33 et Q34 sont fournis par le sujet."""
from copy import deepcopy
from math import hypot


# Q19
def Clinear(val):
    if val <= 0.04045:
        return val / 12.92
    return ((val + 0.055) / 1.055) ** 2.4


# Q20
def Y(pix):
    r, v, b = [Clinear(c / 255) for c in pix]
    ylin = 0.2126 * r + 0.7152 * v + 0.0722 * b
    if ylin <= 0.0031308:
        return 12.92 * ylin
    return 1.055 * ylin ** (1 / 2.4) - 0.055


# Q21
def NiveauxGris(I):
    return [[round(255 * Y(pix)) for pix in ligne] for ligne in I]


# Q22
def convolution(A, B):
    return sum(A[r][c] * B[r][c] for r in range(3) for c in range(3))


# Q23
Gx = ((-1, 0, 1), (-2, 0, 2), (-1, 0, 1))
Gy = ((-1, -2, -1), (0, 0, 0), (1, 2, 1))


def contraste_pixel(I, i, j):
    bloc = [I[r][j-1:j+2] for r in range(i-1, i+2)]
    return int(hypot(convolution(bloc, Gx), convolution(bloc, Gy)))


# Q24
def contraste(I):
    h, l = len(I), len(I[0]) if len(I) else 0
    if h < 3 or l < 3:
        raise ValueError("Pas de pixel interieur")
    somme = sum(contraste_pixel(I, i, j)
                for i in range(1, h-1) for j in range(1, l-1))
    return somme / ((h-2) * (l-2))


# Q25
def reglage(position_objectif, prise):
    position_objectif(0)
    precedent = contraste(NiveauxGris(prise()))
    for pas in range(1, 1001):
        position_objectif(pas)
        actuel = contraste(NiveauxGris(prise()))
        if actuel < precedent:
            position_objectif(pas - 1)
            return pas - 1
        precedent = actuel
    return 1000


# Q26
def extraction(L1, L2, dec):
    n = len(L1)
    if len(L2) != n or abs(dec) >= n:
        raise ValueError("Recouvrement non vide de capteurs egaux requis")
    if dec >= 0:
        return L1[:n-dec], L2[dec:]
    return L1[-dec:], L2[:n+dec]


# Q27
def comparaison(L1, L2):
    if len(L1) != len(L2):
        return False
    for x, y in zip(L1, L2):
        if x != y:
            return False
    return True


# Q28
def recherche_decalage(L1, L2):
    borne = min(80, len(L1)-1)
    for dec in range(-borne, borne+1):
        a, b = extraction(L1, L2, dec)
        if comparaison(a, b):
            return dec
    return None


# Q30
def erreur(L1, L2):
    n = len(L1)
    if n == 0 or n != len(L2):
        raise ValueError("Deux listes non vides de meme longueur requises")
    return sum((float(x)-float(y))**2 for x, y in zip(L1, L2)) / n


# Q31
def recherche_decalage_2(L1, L2):
    borne = min(80, len(L1)-1)
    if borne < 0 or len(L1) != len(L2):
        raise ValueError("Capteurs vides ou incompatibles")
    meilleur, minimum = None, float("inf")
    for dec in range(-borne, borne+1):
        a, b = extraction(L1, L2, dec)
        score = erreur(a, b)
        if score < minimum:
            meilleur, minimum = dec, score
    return meilleur


# Q33
def faire_un_pas_positif(pas_actuel):
    # Pour la transition de la phase k a la phase k+1,
    # une seule sortie change (chronogramme).
    transitions = ((IN3, True), (IN1, False), (IN2, True),
                   (IN3, False), (IN4, True), (IN2, False),
                   (IN1, True), (IN4, False))
    sortie, etat = transitions[pas_actuel % 8]
    modif_sortie(sortie, etat)
    return pas_actuel + 1


# Q34
def position_objectif(pas):
    global pas_courant
    if not isinstance(pas, int) or not 0 <= pas <= 1000:
        raise ValueError("Position demandee hors course")
    while pas_courant < pas:
        pas_courant = faire_un_pas_positif(pas_courant)
    while pas_courant > pas:
        pas_courant = faire_un_pas_negatif(pas_courant)
    return pas_courant


# Q39
def rotation_180(image):
    return [[deepcopy(pix) for pix in reversed(ligne)]
            for ligne in reversed(image)]


# Q40
def rotation_90(image):
    h = len(image)
    l = len(image[0]) if h else 0
    return [[deepcopy(image[r][l-1-c]) for r in range(h)]
            for c in range(l)]
