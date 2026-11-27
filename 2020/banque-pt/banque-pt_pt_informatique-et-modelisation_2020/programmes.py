from math import cos, exp, pi
from cmath import exp as exp_complexe
import struct
import wave


# Q21
tps = [i / 100 for i in range(1001)]


# Q22
def sigh(t):
    return [cos(2 * pi * 12 * ti) * exp(-ti) for ti in t]


# Q23
def sigx(t):
    amplitudes = [1, 0.5, 0.2, 0.1]
    frequences = [0.5, 5, 10, 20]
    return [sum(a * cos(2 * pi * f * ti + k * pi)
                for k, (a, f) in enumerate(zip(amplitudes, frequences)))
            for ti in t]


# Q24
def tracer(t):
    from matplotlib import pyplot as plt
    fig, ax = plt.subplots()
    ax.plot(t, sigx(t), color="blue", label="x(t)")
    ax.plot(t, sigh(t), color="green", label="h(t)")
    ax.set(xlabel="temps (s)", xlim=(0, 10), ylim=(-1.5, 2))
    ax.set_yticks([i / 2 for i in range(-3, 5)])
    ax.legend(loc="upper right")
    return fig, ax

if __name__ == "__main__":
    from matplotlib import pyplot
    tracer(tps)
    pyplot.show()


# Q25
def convolution(x, h, t):
    n = len(t)
    if len(x) != n or len(h) != n or n < 2:
        raise ValueError("Trois listes de même longueur, au moins deux points")
    dt = t[1] - t[0]
    return [dt * sum(x[j] * h[(i - j) % n] for j in range(n - 1))
            for i in range(n)]


# Q29
def Fourier_directe(x):
    n = len(x)
    return [sum(x[l] * exp_complexe(-2j * pi * k * l / n)
                for l in range(n)) for k in range(n)]


# Q31
def Fourier_directe_inverse(X):
    n = len(X)
    return [sum(X[k] * exp_complexe(2j * pi * k * l / n)
                for k in range(n)) / n for l in range(n)]


# Q32
def produit(x, h):
    if len(x) != len(h):
        raise ValueError("Dimensions différentes")
    return [a * b for a, b in zip(x, h)]


# Q33
def convolution_tfd(x, h, dt=1.0, dernier_rectangle=True):
    entree = list(x)
    if not dernier_rectangle:
        entree[-1] = 0
    spectre = produit(Fourier_directe(entree), Fourier_directe(h))
    return [v * dt for v in Fourier_directe_inverse(spectre)]


# Q35
def Fourier_rapide(x, N):
    if N < 1 or N & (N - 1) or len(x) != N:
        raise ValueError("La taille doit être une puissance de deux")
    if N == 1:
        return list(x)
    demi = N // 2
    pairs = Fourier_rapide(x[::2], demi)
    impairs = Fourier_rapide(x[1::2], demi)
    racine = exp_complexe(-2j * pi / N)
    phase = 1
    y = [0j] * N
    for k in range(demi):
        terme = phase * impairs[k]
        y[k] = pairs[k] + terme
        y[k + demi] = pairs[k] - terme
        phase *= racine
    return y


def Fourier_rapide_inverse(X, N):
    conjugues = [complex(v).conjugate() for v in X]
    return [complex(z).conjugate() / N for z in Fourier_rapide(conjugues, N)]


# Q36
def nextpow2(n):
    if n < 1:
        raise ValueError("Entier positif requis")
    N = 1
    while N * 2 <= n:
        N *= 2
    return N


# Q45
def coder_paire(gauche, droite, maxi):
    g = round(32767 * gauche / maxi) if maxi else 0
    d = round(32767 * droite / maxi) if maxi else 0
    gbyte = g.to_bytes(2, byteorder="little", signed=True)
    dbyte = d.to_bytes(2, byteorder="little", signed=True)
    return gbyte, dbyte


# Q46
def creawave_2oct(voieG, voieD, destination):
    if len(voieG) != len(voieD):
        raise ValueError("Les voies doivent avoir la même durée")
    maxi = max((abs(v) for voie in (voieG, voieD) for v in voie), default=0)
    with wave.open(str(destination), "wb") as sortie:
        sortie.setparams((2, 2, 44100, len(voieG), "NONE", "PCM"))
        for gauche, droite in zip(voieG, voieD):
            gbyte, dbyte = coder_paire(gauche, droite, maxi)
            sortie.writeframesraw(gbyte + dbyte)


# Q47
def addzeros(voie, N):
    if len(voie) > N:
        raise ValueError("La taille demandée est trop petite")
    return list(voie) + [0] * (N - len(voie))


# Q48
def extrawave_2oct(fichier):
    with wave.open(str(fichier), "rb") as entree:
        p = entree.getparams()
        if (p.nchannels, p.sampwidth, p.framerate) != (2, 2, 44100):
            raise ValueError("PCM stéréo, 16 bits, 44 100 Hz requis")
        brut = entree.readframes(p.nframes)
    gauche, droite = [], []
    for g, d in struct.iter_unpack("<hh", brut):
        gauche.append(g)
        droite.append(d)
    return gauche, droite


def convolution_reverb(fichier1, fichier2, fichier3):
    xg, xd = extrawave_2oct(fichier1)
    hg, hd = extrawave_2oct(fichier2)
    if not xg or not hg:
        raise ValueError("Les deux enregistrements doivent être non vides")
    longueur = len(xg) + len(hg) - 1
    N = nextpow2(longueur)
    if N < longueur:
        N *= 2

    def traiter(x, h):
        X = Fourier_rapide(addzeros(x, N), N)
        H = Fourier_rapide(addzeros(h, N), N)
        y = Fourier_rapide_inverse(produit(X, H), N)
        return [v.real for v in y[:longueur]]

    creawave_2oct(traiter(xg, hg), traiter(xd, hd), fichier3)
