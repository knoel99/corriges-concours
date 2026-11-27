"""Lancer avec Python, NumPy et Matplotlib. Option --proprietes : CoolProp."""
import argparse
from math import exp, isclose, pi, sqrt, tanh
from pathlib import Path
import tempfile

import matplotlib
matplotlib.use("Agg")
import numpy as np
from numpy.testing import assert_allclose

from programmes import (
    Euler_Explicite, affichage, affichage_couple, analyse_essais,
    caracteristiques, cout, descente_gradient, dichotomie,
    extraction_resultats_essai, gradient, matrice_explicative, modele,
    moyenne_sur_intervalle, nbre_ffu, point_de_fonctionnement,
    remplace_virgule_par_point, repartition, volume,
)


def verifier_thermique(complet):
    T_f, T_c, Q_f = 261.15, 317.15, 115.0
    for creation in (0, 0.1, 0.5):
        Q_c = -T_c * (Q_f / T_f + creation)
        W = -Q_f - Q_c
        assert W > 0 and Q_c < 0
        assert isclose(Q_f/T_f + Q_c/T_c + creation, 0, abs_tol=1e-12)
        assert Q_f / W <= T_f/(T_c-T_f) + 1e-12
    hA, hB, hC, hD = 380, 416, 265, 265
    assert hA - hD == 115 and hB - hA == 36
    assert isclose((hA-hD)/(hB-hA), 3.2, abs_tol=.01)
    assert isclose(T_f/(T_c-T_f), 4.7, abs_tol=.04)
    a, b, h, lam, ecart = .02, .05, 10, 210, 30
    p, S = 2*(a+b), a*b
    delta = sqrt(lam*S/(h*p))
    puissance = sqrt(2*h*lam*a*b*(a+b))*ecart
    assert isclose(puissance, h*p*ecart*delta)
    assert isclose(puissance, lam*S*ecart/delta)
    assert isclose(exp(-3), .05, abs_tol=.001)
    if complet:
        from CoolProp import __version__
        from CoolProp.CoolProp import PropsSI
        fluide = "R404A"
        A = ("P", 4e5, "T", 283.15, fluide)
        B = ("P", 2e6, "S", PropsSI("S", *A), fluide)
        C = ("P", 2e6, "T", 316.15, fluide)
        D = ("P", 4e5, "H", PropsSI("H", *C), fluide)
        enthalpies = [PropsSI("H", *etat)/1000 for etat in (A,B,C,D)]
        tB, tD = PropsSI("T", *B)-273.15, PropsSI("T", *D)-273.15
        xD = PropsSI("Q", *D)
        assert_allclose(enthalpies, [380,416,265,265], atol=1)
        assert isclose(tB,70,abs_tol=1) and isclose(tD,-12,abs_tol=1)
        assert isclose(xD,.47,abs_tol=.01)
        print("R404A, CoolProp", __version__, "h (kJ/kg)",enthalpies,
              "TB/TD (°C)", tB, tD, "titre D", xD)


def verifier_grille():
    assert volume(10,5,4) == 200
    for V, Q, taux in [(201,100,1), (10,2,1), (200,2000,50)]:
        n = nbre_ffu(V,Q,taux)
        assert (n-1)*Q < V*taux <= n*Q
    for L in (2,3,4,8,10,50):
        for l in (.5,1,2,5,25):
            for n in range(1,61):
                admissibles = []
                for ny in range(1,n+1):
                    nx=n//ny
                    if L >= 2*nx+1 and l >= ny:
                        admissibles.append((nx,ny))
                try:
                    nx,ny,u,v=repartition(L,l,n)
                except ValueError:
                    assert not admissibles
                else:
                    assert admissibles[0]==(nx,ny)
                    assert isclose((nx+1)*u+nx,L)
                    assert isclose((ny+1)*v+ny,l)
                    assert nx*ny<=n and u>=1 and v>=0
    assert repartition(10,5,11)==(3,3,1.75,.5)


def verifier_essais():
    assert remplace_virgule_par_point("-0,884\t0,041")=="-0.884\t0.041"
    assert moyenne_sur_intervalle([0,2,4,9],1,3)==3
    with tempfile.TemporaryDirectory() as temp:
        racine=Path(temp)
        # Six premières lignes de mesures données en exemple à la page 12.
        extrait=["0\t22\t-0,884\t0","0,1\t22\t-9,96\t0,041",
            "0,2\t22\t-12,924\t0,057","0,3\t44\t-12,924\t0,079",
            "0,4\t44\t-9,96\t0,144","0,5\t44\t-0,884\t0,151"]
        fichier=racine/"extrait.txt"
        fichier.write_text("Entete\n"*13 + "\n".join(extrait))
        d=extraction_resultats_essai(fichier)
        assert list(d)==["temps","consigne","vitesse","courant"]
        assert_allclose(d["temps"],np.arange(6)/10)
        assert_allclose(d["vitesse"],[-.884,-9.96,-12.924,-12.924,-9.96,-.884])
        assert_allclose(d["courant"],[0,.041,.057,.079,.144,.151])
        courbe = affichage(d)
        assert_allclose(courbe.get_xdata(),d["temps"])
        assert_allclose(courbe.get_ydata(),d["vitesse"])
        for j in range(1,19):
            # Données artificielles, ici un plateau dont le dernier point
            # diffère pour mettre à l'épreuve les deux bornes incluses.
            lign=[]
            for i in range(702):
                n=100*j if 500<=i<=700 else -10
                intensite=j+(i==700) if 500<=i<=700 else -10
                lign.append(f"{i/10}\t0\t{n}\t{intensite}".replace(".",","))
            (racine/f"essai{j}.txt").write_text("Entete\n"*13+"\n".join(lign))
        N,Cr=analyse_essais(racine)
        assert_allclose(N,100*np.arange(1,19))
        assert_allclose(Cr,.13*(np.arange(1,19)+1/201))
        assert point_de_fonctionnement(extraction_resultats_essai(racine/"essai1.txt"))[0]==100


def verifier_regression():
    x=np.linspace(.1,1,18)
    X=matrice_explicative(x)
    theta=np.array([[1.73],[-.2]])
    Y=X@theta
    assert X.shape==(18,2)
    assert_allclose(X[:,0],x)
    assert_allclose(X[:,1],1)
    assert_allclose(modele(X,theta),Y)
    assert cout(X,Y,theta)==0
    init=np.array([[.3],[.5]])
    grad=gradient(X,Y,init)
    pas=1e-6
    for i in range(2):
        d=np.zeros((2,1));d[i,0]=pas
        estime=(cout(X,Y,init+d)-cout(X,Y,init-d))/(2*pas)
        assert isclose(estime,grad[i,0],abs_tol=1e-7)
    alpha=.9/np.linalg.eigvalsh(X.T@X)[-1]
    resultat=descente_gradient(X,Y,init,alpha,600)
    assert_allclose(resultat,theta,atol=1e-9)
    assert_allclose(init,[[.3],[.5]])
    assert_allclose(descente_gradient(X,Y,init,alpha,0),init)


def verifier_moteur():
    courbe=affichage_couple(.05,5.3e-6)
    assert_allclose(courbe.get_xdata(),np.arange(26)*10)
    assert isclose(courbe.get_ydata()[-1],.38125)
    for U in (50,100,146,200,250):
        w,u=dichotomie(U,0,250,1e-5)
        sol=np.roots([5.3e-6,.839*1.17,.05-.839*U]).max()
        assert abs(w-sol)<=1e-5 and u==U
    assert dichotomie(.05/.839,0,2,1e-3)==(0,.05/.839)
    w,U=dichotomie(146,0,250,1e-8)
    w1250=1250*pi/30
    v1250=1.17*w1250+(5.3e-6*w1250**2+.05)/.839
    print("Équilibre 146 V",w,"rad/s,",w*30/pi,"tr/min ; 1250 tr/min",v1250,"V")
    LT,Lw=Euler_Explicite(lambda w,t: 2+t,3,0,1,.3)
    assert_allclose(LT,[0,.3,.6,.9,1])
    assert_allclose(Lw,[3,3.6,4.29,5.07,5.36])
    assert Euler_Explicite(lambda w,t:1,4,2,2,.3)==([2],[4])
    assert len(Euler_Explicite(lambda w,t:1,0,0,40,.1)[0])==401
    # Données dynamiques synthétiques : w'=1-w², solution tanh(t).
    err=[]
    for T in [.1,.05,.025]:
        LT,Lw=Euler_Explicite(lambda w,t:1-w*w,0,0,4,T)
        err.append(abs(Lw[-1]-tanh(4)))
    assert err[0] > err[1] > err[2] > 0
    assert caracteristiques([4,5,6,7,8],[0,99,109,104,100])==(3,100)
    assert caracteristiques([4,5,6],[2,2,2])==(0,2)
    print("Euler, erreurs à t=4 (pas successivement divisés par 2)",err)


if __name__=="__main__":
    options=argparse.ArgumentParser()
    options.add_argument("--proprietes",action="store_true")
    verifier_thermique(options.parse_args().proprietes)
    verifier_grille()
    verifier_essais()
    verifier_regression()
    verifier_moteur()
    print("Bilans, ailette, 1 800 implantations, extrait officiel, 18 fichiers synthétiques, régression, équilibres, Euler et temps de réponse contrôlés.")
