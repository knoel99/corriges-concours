"""Vérifications reproductibles de l'autofocus — Python 3, bibliothèque standard."""
from collections import Counter
from copy import deepcopy
from math import cos, isclose, pi, sin, sqrt
from pathlib import Path
import re
import sqlite3
import programmes as c


def verifier_optique():
    f0, x0 = .1, -2
    dp = f0*x0/(x0+f0)
    assert isclose(dp, 2/19) and isclose(dp/x0*.1, -.1/19)
    demi_tache = .05*.005/dp
    pas_pixel = sqrt(.020*.030/6e6)
    assert isclose(demi_tache,.002375)
    assert isclose(pas_pixel,1e-5)
    assert isclose(pas_pixel*dp/(2*.05), 1.0526315789473684e-5)
    d0, d, a = 20.,20.,3.
    f = d0*d/(d+d0)
    for p in [-12.,-4.,0.,2.,5.]:
        x1 = f*(d0-p)/(d0-p-f)
        y1 = a*(1+x1/(d0-p))
        y_ray_horizontal = a*x1/f
        assert isclose(y1,y_ray_horizontal)
        bords = [b+(y1-b)*d/x1 for b in [0,2*a]]
        # Mesurer les points hauts sur les deux capteurs réfléchis.
        delta = max(bords)-max(-y for y in bords)
        assert isclose(delta,2*a+2*a*d/(d0-p))
        D = delta-2*a*(1+d/d0)
        assert isclose(D*d0*d0/(2*a*d+D*d0),p,abs_tol=1e-12)
    D=.66
    p=D*d0*d0/(2*a*d+D*d0)
    assert isclose(p,1.981981981981982)
    print("Optique : plan net",dp,"m, rayon",demi_tache,"m, pixel",pas_pixel,"m, déplacement mesuré",p,"cm.")
    # Coordonnées du support de réponse dans une unité de dessin commune.
    d0, d, p, a = 14.2, 15.1, -9.2, 5.
    f = d0*d/(d0+d)
    x1 = f*(d0-p)/(d0-p-f)
    y1 = a*(1+x1/(d0-p))
    assert x1 < d and isclose(y1, a*x1/f)
    assert d*y1/x1 > 2*a+(y1-2*a)*d/x1
    print("Document réponse : x1, y1, d mesurés dans les unités de reconstruction",x1,y1,d)


def verifier_moteur_physique():
    # Rayon vers le fil supérieur vu du centre = (sin t, cos t).
    # Pour un courant sortant, z × rayon du fil vers le centre = (cos t, -sin t).
    for theta in (0,pi/6):
        X,Y=sin(theta),cos(theta)
        bx,by=Y,-X
        assert isclose(bx,cos(theta)) and isclose(by,-sin(theta))
    N, i, a, b, Br, Bt, w=12,.4,.07,.02,-.3,.2,17.
    forces_theta=[i*a*Br,-i*a*Br]
    couple=N*sum(r*F for r,F in zip([-b/2,b/2],forces_theta))
    assert isclose(couple,-N*i*a*b*Br)
    e=N*a*b*Br*w
    assert isclose(couple*w+e*i,0,abs_tol=1e-15)


def verifier_images():
    assert 48_000_000*3==144_000_000
    assert isclose(144e6/1024**2,137.3291015625)
    assert c.Clinear(.04045)==.04045/12.92
    for v in range(256):
        assert round(255*c.Y([v]*3))==v
    assert c.NiveauxGris([[[255,0,0],[0,255,0],[0,0,255]]])==[[127,220,76]]
    assert c.convolution([[1,2,3],[4,5,6],[7,8,9]],c.Gx)==8
    assert c.convolution([[1,2,3],[4,5,6],[7,8,9]],c.Gy)==24
    assert c.contraste([[8]*5 for _ in range(4)])==0
    img=[[i+3*j for j in range(6)] for i in range(4)]
    assert c.contraste(img)==25
    img=[[[r*10+j]*3 for j in range(3)] for r in range(2)]
    orig=deepcopy(img)
    demi,quart=c.rotation_180(img),c.rotation_90(img)
    assert [[el[0] for el in row] for row in quart]==[[2,12],[1,11],[0,10]]
    assert c.rotation_90(quart)==demi
    assert c.rotation_180(demi)==orig
    assert c.rotation_90(c.rotation_90(demi))==orig
    quart[0][0][1]=200
    assert img==orig
    # Essais de mise au point sur images RVB synthétiques.
    for bord,attendu in [(0,0),(3,3),(1000,1000)]:
        positions=[]
        def deplacer(t):positions.append(t)
        def lire():
            n=positions[-1]
            # Pour la butée, plateau maximal de 256 à 1000.
            v=min(n,255) if bord==1000 else max(0,100-abs(n-bord))
            return [[[k]*3 for k in (0,0,v)] for _ in range(3)]
        assert c.reglage(deplacer,lire)==attendu
        assert positions[0]==0 and positions[-1]==attendu
        assert 0<=min(positions)<=max(positions)<=1000


def verifier_phase():
    n=100
    base=list(range(n))
    assert c.extraction(list("abcdefghij"),list("yzabcdefgh"),2)==(
        list("abcdefgh"),list("abcdefgh"))
    assert c.extraction(list("abcdefghij"),list("defghijklm"),-3)==(
        list("defghij"),list("defghij"))
    for dec in range(-80,81):
        autre=[k-dec for k in base]
        origine=deepcopy(autre)
        assert c.recherche_decalage(base,autre)==dec
        bruit=[v+.06*((j%5)-2) for j,v in enumerate(autre)]
        assert c.recherche_decalage_2(base,bruit)==dec
        a,b=c.extraction(base,autre,dec)
        assert c.comparaison(a,b) and len(a)==n-abs(dec)
        assert autre==origine
    assert not c.comparaison([1],[1,2])
    assert c.comparaison([],[])
    assert c.erreur([0,2],[2,4])==4
    assert c.recherche_decalage([1]*100,[7]*100) is None
    assert c.recherche_decalage([4]*100,[4]*100)==-80
    assert c.recherche_decalage_2([4]*100,[5]*100)==-80
    class Compteur:
        comparaisons=0
        def __init__(self,val):self.val=val
        def __ne__(self,autre):
            type(self).comparaisons+=1
            return self.val!=autre.val
    def compte(s,t):
        Compteur.comparaisons=0
        resultat=c.recherche_decalage(list(map(Compteur,s)),list(map(Compteur,t)))
        return resultat,Compteur.comparaisons
    assert compte([0]*99+[1],[0]*99+[2])==(None,9620)
    assert compte([0]*100,[0]*100)==(-80,20)
    print("Phase : 161 signes et amplitudes exacts puis bruités, 20 comparaisons au meilleur cas garanti, 9 620 au pire.")


def verifier_demi_pas():
    table=[(1,0,0,0),(1,0,1,0),(0,0,1,0),(0,1,1,0),
           (0,1,0,0),(0,1,0,1),(0,0,0,1),(1,0,0,1)]
    c.IN1,c.IN2,c.IN3,c.IN4=range(4)
    etat=list(table[0]);ordres=[]
    def ecrire(k,v):
        assert bool(etat[k])!=v
        etat[k]=int(v)
        ordres.append((k,v))
    def negatif(n):
        for k,(v,prochain) in enumerate(zip(table[n%8],table[(n-1)%8])):
            if v!=prochain:ecrire(k,bool(prochain))
        return n-1
    c.modif_sortie=ecrire
    c.faire_un_pas_negatif=negatif
    c.pas_courant=0
    for i in range(1000):
        assert c.position_objectif(i+1)==i+1
        assert tuple(etat)==table[(i+1)%8]
    assert len(ordres)==1000
    assert c.position_objectif(0)==0 and len(ordres)==2000
    assert c.position_objectif(0)==0 and len(ordres)==2000
    for mauvais in (-1,1001,1.5):
        try:c.position_objectif(mauvais)
        except ValueError:pass
        else:raise AssertionError(mauvais)
    assert len(ordres)==2000 and c.pas_courant==0
    print("Moteur simulé : 1 000 demi-pas avant, 1 000 arrière et butées contrôlées.")


def verifier_sql():
    path=Path(__file__).with_name('requetes.sql')
    queries=re.split(r'^-- Q\d+\n',path.read_text(),flags=re.M)[1:]
    with sqlite3.connect(':memory:') as db:
        db.executescript("""
          CREATE TABLE PHOTOS(id INTEGER PRIMARY KEY, date TEXT, heure TEXT, idp INTEGER);
          CREATE TABLE PHOTOGRAPHES(id INTEGER PRIMARY KEY, nom TEXT, prenom TEXT);
          INSERT INTO PHOTOGRAPHES VALUES(1,'Dumas','Zoé'),(2,'Dumas','Zoé'),(3,'Yan','Lou');
          INSERT INTO PHOTOS VALUES(1,'20181111','11:00',1),(2,'20181111','11:00',1),
             (3,'20181111','12:00',2),(4,'20181112','09:00',3);
        """)
        assert {x[0] for x in db.execute(queries[0])}=={1,2,3}
        assert list(db.execute(queries[1]))==[('Dumas','Zoé')]*2
        assert Counter(db.execute(queries[2]))==Counter(
            [('Dumas','Zoé','11:00')]*2+[('Dumas','Zoé','12:00')])
    print("SQL : trois requêtes exécutées, auteurs homonymes, clichés simultanés et exclusion d'une autre date.")


if __name__=='__main__':
    verifier_optique()
    verifier_moteur_physique()
    verifier_images()
    verifier_phase()
    verifier_demi_pas()
    verifier_sql()
    print("Optique, moment et puissance, luminance, Sobel, premier maximum, phase, rotations, demi-pas et SQL vérifiés.")
