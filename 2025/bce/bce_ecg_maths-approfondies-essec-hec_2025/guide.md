# BCE ECG — Maths approfondies (ESSEC-HEC) 2025 · Corrigé guidé

*Corrigé rédigé par IA, non officiel. Signalez toute erreur.*

## Présentation du sujet

**Cadre.** Épreuve de mathématiques approfondies conçue par ESSEC BS et HEC Paris, voie générale ECG, 4 heures, sans calculatrice ni document. Le sujet compte 46 questions (sous-questions comprises) et un formulaire Python en annexe. Selon le rapport 2025, 2 447 copies ont été corrigées, avec une moyenne de 10,79 et un écart type de 5,68.

**Thème.** On minimise $\frac12\|AX-Y\|^2+\mu\|BX\|$ sur $\mathbb{R}^p$, où $A\in\mathcal{M}_{n,p}(\mathbb{R})$ et $B\in\mathcal{M}_{m,p}(\mathbb{R})$.

Pour $\mu=0$, c'est le problème des moindres carrés ; pour $\mu=1$, on ajoute une pénalisation non différentiable en $X$ tel que $BX=0$ (une version simple des régularisations utilisées en statistique).

- **Partie I (Q1–Q11), autour de l'adjoint.** Représentation d'une forme linéaire par un produit scalaire, construction de l'adjoint $u^*$ (de matrice ${}^tA$), relations $\operatorname{Im}(u^*)=\ker(u)^\perp$ et $\ker(u^*\circ u)=\ker(u)$.
  Matrice $Q$ du projecteur orthogonal sur $\operatorname{Im}(A)$, formule $Q=AM^{-1}\,{}^tA$.
- **Partie II (Q12–Q16), moindres carrés.** Développement de $J_0(X+H)$, caractérisation des minimums par $D(X)=0$, solution de norme minimale, puis une longue question de probabilités : loi de l'erreur $T=\|A(X-U_0)\|^2$ quand $Y$ est bruité par un vecteur gaussien, conjectures par simulation Python, puis $\mathbb{E}(T)=p\sigma^2$ et $\mathbb{V}(T)=2p\sigma^4$.
- **Partie III (Q17–Q23), minimisation non différentiable.** Dérivée directionnelle de la norme, condition nécessaire et suffisante de minimum global $-D(X_0)\in\mathscr{N}(X_0)$, puis résolution explicite quand $A=I_n$ et $B$ diagonale, avec une dichotomie en Python.

**Notions du programme.** Espaces euclidiens, bases orthonormales, supplémentaire orthogonal, projection orthogonale, théorème du rang, rang de la transposée, trace (invariance par changement de base) ; inégalité de Cauchy-Schwarz ; loi normale, indépendance, lemme des coalitions, espérance et variance, inégalité de Bienaymé-Tchebychev ; théorème de la bijection ; dichotomie et simulation en Python.

**Barème (rapport 2025).** « Partie 1 : 24%, Partie 2 : 38% , Partie 3 : 38% . » L'informatique compte pour 17 %. Les questions les plus payantes sont 16(a), 16(g), 16(h), 16(i), 18, 21(a), 23(c) et 23(d)ii. Le rapport précise : « Pour avoir 20, il fallait traiter correctement au moins 40% du sujet et pour 16, 30%. »

**Questions abordables à ne pas laisser passer.** Q1 à Q6, Q9, Q11, Q12, Q15, 16(a) à 16(f), Q17, Q20, 23(a) et les fonctions Python 16(b), 16(c), 23(d)i.

**Gestion du temps.** Environ 50 minutes pour la partie I, 1 h 30 pour la partie II (dont une heure pour la question 16), 1 h 30 pour la partie III, et quelques minutes de relecture. Les parties II et III s'abordent en admettant les résultats de la partie I.

**Convention utilisée partout.** On applique la partie I avec $E=\mathbb{R}^p$ et $F=\mathbb{R}^n$ munis de leurs produits scalaires canoniques (les bases canoniques sont orthonormales) et $u:X\mapsto AX$.

Alors $u^*:Y\mapsto{}^tAY$ (question 4), $\ker u=\ker(A)$, $\operatorname{Im}(u^*)=\operatorname{Im}({}^tA)$, et $u^*\circ u$ a pour matrice $M$.

---

## Partie I — Autour de l'adjoint

On construit l'adjoint d'une application linéaire entre espaces euclidiens et on établit les relations entre noyaux et images qui servent ensuite à résoudre l'équation normale $MX={}^tAY$. Outils : bases orthonormales, théorème du rang, orthogonal d'un sous-espace.

### Question 1

> [!INDICATION]
> Il y a deux choses à montrer : l'unicité et l'existence. L'unicité est un argument de produit scalaire nul.

> [!INDICATION]
> Pour l'existence, cherchez $a_0$ sous la forme $\sum_i c_ie_i$ et calculez $\langle a_0,e_j\rangle_E$ : la base est orthonormale.

#### Solution

*Unicité.* Si $a_0$ et $a_0'$ conviennent, alors $\langle a_0-a_0',x\rangle_E=0$ pour tout $x\in E$.

Avec $x=a_0-a_0'$, on obtient $\|a_0-a_0'\|^2=0$, donc $a_0=a_0'$.

*Existence.* On pose $a_0=\sum_{i=1}^{p}\ell(e_i)\,e_i$. La base étant orthonormale, pour tout $j$ :

$$\begin{aligned}
\langle a_0,e_j\rangle_E&=\sum_{i=1}^{p}\ell(e_i)\langle e_i,e_j\rangle_E\\
&=\ell(e_j).
\end{aligned}$$

Les deux formes linéaires $\ell$ et $x\mapsto\langle a_0,x\rangle_E$ coïncident sur une base : elles sont égales.

> [!METHODE]
> Pour prouver qu'une application linéaire est égale à une autre, il suffit de vérifier l'égalité sur une base. Ici, l'orthonormalité rend le calcul de $\langle a_0,e_j\rangle$ immédiat.

> [!JURY]
> Le rapport 2025 signale que « La première question de l'énoncé a été mal traitée par beaucoup de candidats, notamment concernant l'existence. » Il faut construire $a_0$ explicitement (ou invoquer un argument de dimension), pas seulement prouver l'unicité.

### Question 2

> [!INDICATION]
> Fixez $y$ et regardez $x\mapsto\langle u(x),y\rangle_F$ : de quel type d'application s'agit-il ?

#### Solution

Pour $y\in F$ fixé, $\ell_y:x\mapsto\langle u(x),y\rangle_F$ est linéaire (composée de $u$ et de la forme linéaire $z\mapsto\langle z,y\rangle_F$).

La question 1 appliquée à $\ell_y$ fournit un unique $z_y\in E$ tel que $\langle u(x),y\rangle_F=\langle z_y,x\rangle_E$ pour tout $x\in E$.

### Question 3

> [!INDICATION]
> Montrez que $z_y+\lambda z_{y'}$ vérifie la propriété qui définit $z_{y+\lambda y'}$, puis concluez par unicité.

#### Solution

Pour tout $x\in E$ :

$$\begin{aligned}
\langle u(x),y+\lambda y'\rangle_F&=\langle u(x),y\rangle_F+\lambda\langle u(x),y'\rangle_F\\
&=\langle z_y+\lambda z_{y'},x\rangle_E.
\end{aligned}$$

Par l'unicité de la question 2, $z_{y+\lambda y'}=z_y+\lambda z_{y'}$ : $u^*$ est linéaire.

> [!METHODE]
> « Définie par une propriété d'unicité » entraîne « linéaire » : on montre que la combinaison linéaire candidate vérifie la propriété caractéristique. Le même schéma sert pour la linéarité de la réciproque d'une bijection linéaire.

### Question 4

> [!INDICATION]
> Dans une base orthonormale, la $i$-ième coordonnée d'un vecteur $z$ est $\langle z,e_i\rangle_E$.

> [!INDICATION]
> Pour $(u^*)^*$, appliquez le résultat que vous venez d'obtenir à $u^*$ elle-même.

#### Solution

Le coefficient $(i,j)$ de $\operatorname{Mat}_{\mathscr{B}_E,\mathscr{B}_F}(u^*)$ vaut :

$$\langle u^*(f_j),e_i\rangle_E=\langle u(e_i),f_j\rangle_F=A_{j,i}.$$

Donc $\operatorname{Mat}_{\mathscr{B}_E,\mathscr{B}_F}(u^*)={}^tA$. Une matrice et sa transposée ont même rang, donc $\operatorname{rg}(u^*)=\operatorname{rg}(u)$.

Appliqué à $u^*:F\to E$, de matrice ${}^tA$, le même calcul montre que $(u^*)^*$ a pour matrice ${}^t({}^tA)=A$ dans les mêmes bases.

Donc $(u^*)^*=u$.

### Question 5

> [!INDICATION]
> Montrez une inclusion par le calcul, puis comparez les dimensions.

> [!INDICATION]
> Le théorème du rang relie $\dim\ker(u)$ à $\operatorname{rg}(u)$, et la question 4 relie $\operatorname{rg}(u)$ à $\operatorname{rg}(u^*)$.

#### Solution

Si $x\in\ker(u)$ et $y\in F$, alors $\langle x,u^*(y)\rangle_E=\langle u(x),y\rangle_F=0$ : $\operatorname{Im}(u^*)\subset\ker(u)^\perp$. Par la question 4 et le théorème du rang :

$$\begin{aligned}
\dim\operatorname{Im}(u^*)&=\operatorname{rg}(u)\\
&=p-\dim\ker(u)\\
&=\dim\ker(u)^\perp.
\end{aligned}$$

D'où $\operatorname{Im}(u^*)=\ker(u)^\perp$.

> [!METHODE]
> Inclusion plus égalité des dimensions : c'est la manière la plus rapide de prouver l'égalité de deux sous-espaces en dimension finie.

### Question 6

> [!INDICATION]
> Pour l'inclusion non évidente, calculez $\langle x,u^*(u(x))\rangle_E$.

> [!INDICATION]
> Pour les images, une inclusion est immédiate ; comparez les rangs grâce au résultat sur les noyaux.

#### Solution

$\ker(u)\subset\ker(u^*\circ u)$ est clair. Si $u^*(u(x))=0$, alors :

$$\|u(x)\|^2=\langle x,u^*(u(x))\rangle_E=0,$$

donc $u(x)=0$. Ainsi $\ker(u^*\circ u)=\ker(u)$.

Ensuite $\operatorname{Im}(u^*\circ u)\subset\operatorname{Im}(u^*)$, et par le théorème du rang puis la question 4, $\operatorname{rg}(u^*\circ u)=p-\dim\ker(u)=\operatorname{rg}(u)=\operatorname{rg}(u^*)$. D'où $\operatorname{Im}(u^*\circ u)=\operatorname{Im}(u^*)$.

> [!PIEGE]
> Le théorème du rang s'applique à $u^*\circ u$ comme endomorphisme de $E$ (dimension $p$), et à $u$ comme application de $E$ dans $F$ : dans les deux cas, c'est la dimension de l'espace de départ qui intervient.

### Question 7

> [!INDICATION]
> Vérifiez d'abord que $w$ est bien à valeurs dans $\operatorname{Im}(u^*)$. Pour un endomorphisme en dimension finie, quelle propriété suffit pour être bijectif ?

> [!INDICATION]
> Calculez $\ker(w)$ à l'aide des questions 5 et 6.

#### Solution

$w$ est bien définie car $u^*\circ u(x)\in\operatorname{Im}(u^*)$, et linéaire. Son noyau est :

$$\begin{aligned}
\ker(w)&=\ker(u^*\circ u)\cap\operatorname{Im}(u^*)\\
&=\ker(u)\cap\ker(u)^\perp\\
&=\{0\}.
\end{aligned}$$

Endomorphisme injectif d'un espace de dimension finie, $w$ est un isomorphisme.

*Interprétation.* Pour tout $b\in\operatorname{Im}({}^tA)$, et en particulier pour $b={}^tAY$, l'équation $MX=b$ admet une unique solution $X$ dans $\operatorname{Im}({}^tA)$.

> [!JURY]
> Le rapport 2025 relève que « dans la question 7, beaucoup ont écrit que l'application w est automatiquement surjective car l'ensemble d'arrivée est Im(u*). » Annoncer un ensemble d'arrivée ne prouve rien : il faut l'injectivité et la dimension finie (ou un calcul d'image).

### Question 8(a)

> [!INDICATION]
> Traduisez ${}^tAQ={}^tA$ en une égalité d'applications linéaires : $u^*\circ\pi=u^*$.

> [!INDICATION]
> Caractérisez $\operatorname{Im}(u)^\perp$ à l'aide de $u^*$, en revenant à la définition de l'adjoint.

#### Solution

Pour $y\in F$ : $y\in\operatorname{Im}(u)^\perp$ si et seulement si $\langle x,u^*(y)\rangle_E=\langle u(x),y\rangle_F=0$ pour tout $x$, c'est-à-dire si et seulement si $u^*(y)=0$. Donc $\operatorname{Im}(u)^\perp=\ker(u^*)$.

Pour $y\in F$, $y-\pi(y)\in\operatorname{Im}(u)^\perp=\ker(u^*)$, donc $u^*(\pi(y))=u^*(y)$. Ainsi $u^*\circ\pi=u^*$, soit ${}^tAQ={}^tA$ en matrices.

### Question 8(b)

> [!INDICATION]
> Écrivez la matrice de $\pi$ dans une base adaptée à la décomposition $F=\operatorname{Im}(u)\oplus\operatorname{Im}(u)^\perp$.

#### Solution

Si $r=\operatorname{rg}(u)$, la matrice de $\pi$ dans une base adaptée est $\begin{pmatrix}I_r&0\\0&0\end{pmatrix}$, de trace $r$. La trace étant invariante par changement de base, $\operatorname{Tr}(Q)=\operatorname{rg}(u)$.

> [!METHODE]
> La trace d'un projecteur est son rang. Le programme ne contient que l'invariance de la trace par changement de base : on le redémontre en une ligne avec une base adaptée.

### Question 9

> [!INDICATION]
> $M$ est la matrice de $u^*\circ u$ : utilisez la question 6.

#### Solution

$M$ est inversible si et seulement si $\ker(u^*\circ u)=\{0\}$, c'est-à-dire $\ker(u)=\{0\}$ (question 6), c'est-à-dire $\operatorname{rg}(A)=p$ par le théorème du rang.

> [!JURY]
> Le rapport 2025 met en garde : « Beaucoup de candidats affirment que A est inversible juste parce que son rang est maximal, alors qu'elle n'est même pas supposée carrée... » Ici $A$ est de taille $n\times p$ : c'est $M$, carrée, qui est inversible.

### Question 10(a)

> [!INDICATION]
> Montrez que $P=AM^{-1}\,{}^tA$ envoie tout $Y$ sur son projeté orthogonal sur $\operatorname{Im}(A)$.

> [!INDICATION]
> Vérifiez que $PY\in\operatorname{Im}(A)$ et que $Y-PY\in\ker({}^tA)$, puis utilisez la caractérisation de $\operatorname{Im}(A)^\perp$ obtenue en 8(a).

#### Solution

$PY=A(M^{-1}\,{}^tAY)\in\operatorname{Im}(A)$ et :

$$\begin{aligned}
{}^tA(Y-PY)&={}^tAY-({}^tAA)M^{-1}\,{}^tAY\\
&=0.
\end{aligned}$$

Donc $Y-PY\in\ker({}^tA)=\operatorname{Im}(A)^\perp$, et $PY$ est le projeté orthogonal de $Y$ sur $\operatorname{Im}(A)$.

Ainsi $PY=QY$ pour tout $Y$, d'où $Q=AM^{-1}\,{}^tA$.

> [!METHODE]
> Pour identifier un projecteur orthogonal sur $G$, on vérifie les deux conditions : l'image est dans $G$, et le « reste » $Y-PY$ est orthogonal à $G$.

### Question 10(b)

> [!INDICATION]
> Le formulaire fournit `al.matrix_rank`, `al.inv`, `np.transpose` et `np.dot`.

#### Solution

```python
def Calcule_Q(A):
    n, p = np.shape(A)
    if al.matrix_rank(A) != p:
        print("Erreur : A n'est pas de rang p")
        return None
    M = np.dot(np.transpose(A), A)
    return np.dot(np.dot(A, al.inv(M)), np.transpose(A))
```

### Question 11

> [!INDICATION]
> Faites apparaître une norme.

#### Solution

$${}^tXMX={}^t(AX)(AX)=\|AX\|^2\geqslant0.$$

---

## Partie II — Minimisation d'une fonction quadratique

On étudie $J_0(X)=\frac12\|AX-Y\|^2$ : un développement exact à l'ordre 2 donne la condition de minimum $D(X)=0$ (équation normale), puis on étudie l'ensemble des solutions et, enfin, l'erreur commise quand les données sont bruitées. Outils : partie I, Pythagore, calculs d'espérance avec indépendance.

### Question 12

> [!INDICATION]
> Développez $\|(AX-Y)+AH\|^2$ et faites passer $A$ de l'autre côté du produit scalaire.

#### Solution

$$\begin{aligned}
J_0(X+H)-J_0(X)&=\langle AX-Y,AH\rangle+\tfrac12\|AH\|^2\\
&=\langle{}^tA(AX-Y),H\rangle+\tfrac12\,{}^tHMH\\
&=\langle D(X),H\rangle+\tfrac12\,{}^tHMH.
\end{aligned}$$

### Question 13

> [!INDICATION]
> Un sens découle directement de (2) et de la question 11.

> [!INDICATION]
> Pour l'autre sens, appliquez (2) à $H=tD(X)$ et faites tendre $t$ vers $0$ par valeurs négatives.

#### Solution

Si $D(X)=0$, (2) donne $J_0(X+H)-J_0(X)=\frac12\,{}^tHMH\geqslant0$ pour tout $H$ : minimum global.

Réciproquement, si $X$ réalise un minimum global, pour $t\in\mathbb{R}$, avec $c={}^tD(X)MD(X)$ :

$$0\leqslant t\|D(X)\|^2+\frac{t^2}{2}c.$$

Pour $t<0$, en divisant par $t$ puis en faisant tendre $t$ vers $0^-$ : $\|D(X)\|^2\leqslant0$, donc $D(X)=0$.

> [!METHODE]
> Pour exploiter un minimum, on perturbe le point dans une direction bien choisie, on divise par $t$ en surveillant le signe, puis on passe à la limite. On pouvait aussi dire que $J_0$ est de classe $C^1$ et que son gradient vaut $D(X)$ (lu sur (2)), donc qu'un extremum est un point critique.

### Question 14

> [!INDICATION]
> Réécrivez $\mathbb{S}_0\cap\ker(A)^\perp$ à l'aide de $\operatorname{Im}({}^tA)$ et de l'application $w$ de la question 7.

#### Solution

Par la question 5, $\ker(A)^\perp=\operatorname{Im}({}^tA)$, et $D(X)=0$ équivaut à $MX={}^tAY$. Donc $\mathbb{S}_0\cap\ker(A)^\perp$ est l'ensemble des $X\in\operatorname{Im}({}^tA)$ tels que $w(X)={}^tAY$.

Comme $w$ est une bijection de $\operatorname{Im}({}^tA)$ et que ${}^tAY\in\operatorname{Im}({}^tA)$, cet ensemble est le singleton $\{w^{-1}({}^tAY)\}$.

### Question 15(a)

> [!INDICATION]
> Traduisez $D(X)=0$ : le vecteur $Y-AX$ est dans le noyau d'une matrice que vous connaissez.

#### Solution

$D(X)={}^tA(AX-Y)=0$, donc $Y-AX\in\ker({}^tA)=\operatorname{Im}(A)^\perp$.

Avec $AX\in\operatorname{Im}(A)$, l'écriture $Y=AX+(Y-AX)$ montre que $AX$ est le projeté orthogonal de $Y$ sur $\operatorname{Im}(A)$ : $AX=QY$.

### Question 15(b)

> [!INDICATION]
> Appliquez (3) à $X$ et à $X_0$, puis utilisez le théorème de Pythagore.

#### Solution

$AX=QY=AX_0$, donc $X-X_0\in\ker(A)$. Comme $X_0\in\ker(A)^\perp$ :

$$\|X\|^2=\|X_0\|^2+\|X-X_0\|^2.$$

Si $X\neq X_0$, $\|X\|>\|X_0\|$ : $X_0$ est la solution de norme minimale.

### Question 15(c)

> [!INDICATION]
> Que dit la question 9 quand $\operatorname{rg}(A)=p$ ?

#### Solution

$M$ est inversible, donc $D(X)=0\iff X=M^{-1}\,{}^tAY$ : $\mathbb{S}_0=\{M^{-1}\,{}^tAY\}$.

### Question 16(a)

> [!INDICATION]
> Remplacez $Y$ par $AU_0+Z$ dans la formule (4) : $X-U_0$ se simplifie.

> [!INDICATION]
> Pour passer de $\|QZ\|^2$ à ${}^tZQZ$, montrez que $Q$ est symétrique et que $Q^2=Q$.

#### Solution

$X=U_0+M^{-1}\,{}^tAZ$, donc $A(X-U_0)=AM^{-1}\,{}^tAZ=QZ$ et $T=\|QZ\|^2={}^tZ\,{}^tQQZ$.

$M$ est symétrique, donc $M^{-1}$ aussi, et ${}^tQ=Q$. De plus :

$$\begin{aligned}
Q^2&=AM^{-1}({}^tAA)M^{-1}\,{}^tA\\
&=AM^{-1}\,{}^tA\\
&=Q.
\end{aligned}$$

D'où $T={}^tZQZ$.

> [!PIEGE]
> $Q$ est un projecteur *orthogonal* : c'est la symétrie de $Q$ qui permet ${}^tQQ=Q^2$. Un projecteur quelconque vérifie $Q^2=Q$ mais pas ${}^tQ=Q$.

### Question 16(b)

> [!INDICATION]
> Le formulaire donne `rd.normal(m, d, n)` pour $n$ tirages indépendants de loi $\mathcal{N}(m,d^2)$.

#### Solution

```python
def simuleT(A, sigma):
    n, p = np.shape(A)
    Q = Calcule_Q(A)
    Z = rd.normal(0, sigma, n)
    return np.dot(Z, np.dot(Q, Z))
```

### Question 16(c)

> [!INDICATION]
> Quel théorème justifie d'approcher une espérance par une moyenne de simulations ?

#### Solution

La loi faible des grands nombres justifie d'approcher $\mathbb{E}(T)$ par la moyenne de nombreuses simulations indépendantes. L'énoncé nomme la fonction `esperance` en (c), puis `esperanceT` dans le programme de (d) ; on retient ce second nom.

```python
def esperanceT(A, sigma):
    N = 10000
    s = 0
    for k in range(N):
        s = s + simuleT(A, sigma)
    return s / N
```

### Question 16(d)

> [!INDICATION]
> Calculez le rang de $A_1$, $A_2$ et $A_3$, et comparez-le aux trois valeurs obtenues.

> [!INDICATION]
> Sur le graphique, lisez les ordonnées pour $\sigma=1,\dots,6$ et comparez-les à $\sigma^2$.

#### Solution

Les trois matrices sont de rang $p$ égal à 2, 3 et 5 ; les valeurs 1,99 ; 3,01 ; 4,97 suggèrent $\mathbb{E}(T)\approx p$ pour $\sigma=1$.

Pour $A_1$, les points valent environ 2, 8, 18, 32, 50, 72, soit $2\sigma^2$.

On conjecture $\mathbb{E}(T)=p\sigma^2$.

> [!PIEGE]
> $A_3$ est de taille $6\times5$ : la troisième valeur se compare à $p=5$, pas à $n=6$. Le rang (et non le nombre de lignes) est la bonne grandeur.

### Question 16(e)

> [!INDICATION]
> Écrivez $z_1=\sigma N$ avec $N$ de loi normale centrée réduite, et utilisez le théorème de transfert.

> [!INDICATION]
> Pour le moment d'ordre 4, une intégration par parties avec $\varphi'(x)=-x\varphi(x)$ ramène au moment d'ordre 2.

#### Solution

$N$ admet des moments de tout ordre. $\mathbb{E}(N^2)=1$, $\mathbb{E}(N^3)=0$ par imparité, et par intégration par parties sur $[-B,B]$ :

$$\int_{-B}^{B}x^3\cdot x\varphi(x)\,\mathrm{d}x=\big[-x^3\varphi(x)\big]_{-B}^{B}+3\int_{-B}^{B}x^2\varphi(x)\,\mathrm{d}x\longrightarrow3.$$

D'où $\mathbb{E}(z_1^2)=\sigma^2$, $\mathbb{E}(z_1^3)=0$ et $\mathbb{E}(z_1^4)=3\sigma^4$.

### Question 16(f)

> [!INDICATION]
> Développez ${}^tZQZ$ en double somme, puis séparez les termes $i=j$ et $i\neq j$.

> [!INDICATION]
> Pour l'espérance, seuls les termes diagonaux survivent ; reconnaissez une trace.

#### Solution

$$\begin{aligned}
T&=\sum_{i,j}Q_{i,j}z_iz_j\\
&=\sum_iQ_{i,i}z_i^2+\sum_{i\neq j}Q_{i,j}z_iz_j\\
&=T_1+2T_2,
\end{aligned}$$

en regroupant $(i,j)$ et $(j,i)$ grâce à la symétrie de $Q$. Pour $i\neq j$, $\mathbb{E}(z_iz_j)=\mathbb{E}(z_i)\mathbb{E}(z_j)=0$ par indépendance. Donc, par 8(b) :

$$\begin{aligned}
\mathbb{E}(T)&=\sigma^2\operatorname{Tr}(Q)\\
&=\sigma^2\operatorname{rg}(A)\\
&=p\sigma^2.
\end{aligned}$$

Les deux conjectures sont confirmées.

> [!JURY]
> Le rapport 2025 note que « Dans les questions 16 e) à 16 f), les candidats ont montré des lacunes dans la manipulation des sommes, et n'ont pas su décomposer les sommes qui apparaissaient. » Écrire explicitement la séparation diagonale / hors diagonale, et justifier chaque espérance nulle par l'indépendance.

### Question 16(g)

> [!INDICATION]
> Développez le produit en une somme de termes $Q_{k,k}Q_{i,j}\,\mathbb{E}(z_k^2z_iz_j)$ avec $i<j$, puis discutez la position de $k$ par rapport à $i$ et $j$.

#### Solution

Pour $i<j$ et $k$ quelconque, l'un des indices $i$ ou $j$ diffère de $k$ et apparaît avec l'exposant 1. Par indépendance (lemme des coalitions) :

- si $k\notin\{i,j\}$ : $\mathbb{E}(z_k^2)\mathbb{E}(z_i)\mathbb{E}(z_j)=0$ ;
- si $k=i$ : $\mathbb{E}(z_i^3)\mathbb{E}(z_j)=0$ ;
- si $k=j$ : $\mathbb{E}(z_i)\mathbb{E}(z_j^3)=0$.

Donc $\mathbb{E}(T_1T_2)=0$.

### Question 16(h)

> [!INDICATION]
> Pour $T_1^2$, la valeur de $\mathbb{E}(z_i^2z_k^2)$ dépend de l'égalité $i=k$. Exprimez $\sum_{i\neq k}Q_{i,i}Q_{k,k}$ avec $\operatorname{Tr}(Q)$ et $q$.

> [!INDICATION]
> Pour $T_2^2$, seuls les couples $(k,l)=(i,j)$ donnent une espérance non nulle. Il restera $\sum_{i<j}Q_{i,j}^2$, à relier à $\operatorname{Tr}({}^tQQ)$.

#### Solution

$\mathbb{E}(z_i^2z_k^2)$ vaut $3\sigma^4$ si $i=k$ et $\sigma^4$ sinon, donc :

$$\begin{aligned}
\mathbb{E}(T_1^2)&=3\sigma^4q+\sigma^4\big(\operatorname{Tr}(Q)^2-q\big)\\
&=\sigma^4(2q+p^2).
\end{aligned}$$

Pour $T_2^2$ : si $(i,j)\neq(k,l)$ (avec $i<j$ et $k<l$), un indice apparaît une seule fois dans $z_iz_jz_kz_l$ et l'espérance est nulle. Il reste $\mathbb{E}(T_2^2)=\sigma^4\sum_{i<j}Q_{i,j}^2$.

Par symétrie de $Q$ et ${}^tQQ=Q$ :

$$\begin{aligned}
\sum_{i<j}Q_{i,j}^2&=\frac12\Big(\sum_{i,j}Q_{i,j}^2-q\Big)\\
&=\frac12\big(\operatorname{Tr}(Q)-q\big)\\
&=\frac12(p-q).
\end{aligned}$$

D'où $\mathbb{E}(T_2^2)=\frac{\sigma^4}{2}(p-q)$.

> [!METHODE]
> $\sum_{i,j}Q_{i,j}^2=\operatorname{Tr}({}^tQQ)$ : la somme des carrés des coefficients d'une matrice est une trace. Avec $Q$ projecteur orthogonal, elle vaut le rang.

### Question 16(i)

> [!INDICATION]
> Développez $T^2=(T_1+2T_2)^2$ et utilisez (g) et (h).

> [!INDICATION]
> Pour l'inégalité, ramenez l'événement à un écart à l'espérance.

#### Solution

$$\begin{aligned}
\mathbb{E}(T^2)&=\mathbb{E}(T_1^2)+4\mathbb{E}(T_1T_2)+4\mathbb{E}(T_2^2)\\
&=\sigma^4(p^2+2p),
\end{aligned}$$

donc $\mathbb{V}(T)=\sigma^4(p^2+2p)-p^2\sigma^4=2p\sigma^4$.

Pour $\alpha>0$, $\big(T>(1+\alpha)p\sigma^2\big)\subset\big(|T-\mathbb{E}(T)|\geqslant\alpha p\sigma^2\big)$, et par Bienaymé-Tchebychev :

$$\mathbb{P}\big(T>(1+\alpha)p\sigma^2\big)\leqslant\frac{2p\sigma^4}{\alpha^2p^2\sigma^4}=\frac{2}{p\alpha^2}.$$

> [!PIEGE]
> Bienaymé-Tchebychev majore $\mathbb{P}(|T-\mathbb{E}(T)|\geqslant\varepsilon)$ : il faut écrire l'inclusion d'événements avant de l'appliquer, et non l'appliquer directement à un écart unilatéral.

---

## Partie III — Minimisation d'une fonction non différentiable

La norme $X\mapsto\|BX\|$ n'est pas dérivable là où $BX=0$. On remplace la condition « gradient nul » par une condition d'appartenance $-D(X_0)\in\mathscr{N}(X_0)$, dont on montre qu'elle est nécessaire et suffisante. On la vérifie ensuite sur un cas explicite. Outils : limites, Cauchy-Schwarz, partie I, théorème de la bijection.

### Question 17

> [!INDICATION]
> Multipliez par la quantité conjuguée $\|u+tv\|+\|u\|$.

#### Solution

$$\frac{\|u+tv\|-\|u\|}{t}=\frac{2\langle u,v\rangle+t\|v\|^2}{\|u+tv\|+\|u\|}.$$

Par continuité de $t\mapsto\|u+tv\|$ et puisque $\|u\|>0$, la limite en $0$ vaut $\dfrac{\langle u,v\rangle}{\|u\|}$.

### Question 18

> [!INDICATION]
> Écrivez $J(X_0+tH)-J(X_0)\geqslant0$, divisez par $t$ et faites tendre $t$ vers $0$ des deux côtés.

> [!INDICATION]
> Vous obtenez qu'une forme linéaire en $H$ est à la fois positive et négative : elle est nulle. Prenez ensuite $H$ égal au vecteur qui la représente.

#### Solution

Pour $t\neq0$ :

$$0\leqslant t\langle D(X_0),H\rangle+\frac{t^2}{2}\,{}^tHMH+\|BX_0+tBH\|-\|BX_0\|.$$

Après division par $t$, la question 17 (dans $\mathbb{R}^m$, $u=BX_0\neq0$, $v=BH$) donne, en passant à la limite pour $t>0$ puis $t<0$, que :

$$\Big\langle D(X_0)+{}^tB\frac{BX_0}{\|BX_0\|},H\Big\rangle$$

est à la fois positif et négatif, donc nul pour tout $H$. Avec $H$ égal à ce vecteur, il est nul, donc $-D(X_0)={}^tB\dfrac{BX_0}{\|BX_0\|}$.

Avec $V=BX_0/\|BX_0\|$ : $\|V\|=1$ et $\|BX_0\|V-BX_0=0$, donc $-D(X_0)\in\mathscr{N}(X_0)$.

> [!PIEGE]
> Le quotient change de signe avec $t$ : un minimum donne une inégalité pour $t>0$ et l'inégalité inverse pour $t<0$. Ne garder que $t>0$ ne donne qu'une inégalité.

### Question 19(a)

> [!INDICATION]
> Puisque $BX_0=0$, $\|B(X_0+tH)\|$ se calcule exactement. Choisissez le signe de $t$ qui donne l'inégalité demandée.

#### Solution

L'énoncé écrit $H\in\mathcal{M}_{n,1}(\mathbb{R})$ ; il faut lire $H\in\mathcal{M}_{p,1}(\mathbb{R})$. Pour $t<0$, $\|B(X_0+tH)\|=-t\|BH\|$, donc :

$$0\leqslant t\langle D(X_0),H\rangle+\frac{t^2}{2}\,{}^tHMH-t\|BH\|.$$

En divisant par $t<0$ puis en faisant tendre $t$ vers $0^-$ : $\langle D(X_0),H\rangle\leqslant\|BH\|$.

> [!PIEGE]
> Signalez la coquille de dimension ($H$ doit être dans $\mathcal{M}_{p,1}(\mathbb{R})$) plutôt que de la recopier : l'énoncé invite à signaler les erreurs repérées.

### Question 19(b)

> [!INDICATION]
> Appliquez (a) à $H$ et à $-H$ pour $H\in\ker(B)$.

#### Solution

Pour $H\in\ker(B)$, $\|BH\|=0$, donc $\langle D(X_0),H\rangle\leqslant0$ et $-\langle D(X_0),H\rangle\leqslant0$ : $\langle D(X_0),H\rangle=0$.

### Question 19(c)

> [!INDICATION]
> Réutilisez la question 5 avec $B$ à la place de $A$.

#### Solution

La question 5, appliquée à $X\mapsto BX$ de $\mathbb{R}^p$ dans $\mathbb{R}^m$, donne $\ker(B)^\perp=\operatorname{Im}({}^tB)$ : il existe $W$ tel que $D(X_0)={}^tBW$.

### Question 19(d)

> [!INDICATION]
> Réutilisez la question 6 avec $B$ à la place de $A$.

#### Solution

Par la question 6, $\operatorname{Im}({}^tBB)=\operatorname{Im}({}^tB)$ ; donc $D(X_0)={}^tBBV$ pour un certain $V\in\mathcal{M}_{p,1}(\mathbb{R})$.

### Question 19(e)

> [!INDICATION]
> Appliquez l'inégalité de (a) au vecteur $H=V$.

> [!INDICATION]
> Pour conclure, il faut un vecteur de $\mathcal{M}_{m,1}(\mathbb{R})$ dont l'image par ${}^tB$ est $-D(X_0)$.

#### Solution

Par (a) avec $H=V$ : $\|BV\|^2=\langle{}^tBBV,V\rangle=\langle D(X_0),V\rangle\leqslant\|BV\|$, d'où $\|BV\|\leqslant1$ (immédiat si $BV=0$).

Avec $V'=-BV$ : $-D(X_0)={}^tBV'$, $\|V'\|\leqslant1$, et $\|BX_0\|V'-BX_0=0$ puisque $BX_0=0$. Donc $-D(X_0)\in\mathscr{N}(X_0)$.

> [!PIEGE]
> Le vecteur qui convient dans la définition de $\mathscr{N}(X_0)$ est $-BV\in\mathcal{M}_{m,1}(\mathbb{R})$, et non $V\in\mathcal{M}_{p,1}(\mathbb{R})$ : vérifiez les tailles.

### Question 20(a)

> [!INDICATION]
> Développez les deux carrés.

#### Solution

$$\begin{aligned}
\|u+v\|^2-\Big(\|u\|+\frac{\langle u,v\rangle}{\|u\|}\Big)^2&=\|v\|^2-\frac{\langle u,v\rangle^2}{\|u\|^2}\\
&=\frac{\|u\|^2\|v\|^2-\langle u,v\rangle^2}{\|u\|^2}.
\end{aligned}$$

### Question 20(b)

> [!INDICATION]
> Quel est le signe du membre de droite de (a) ?

#### Solution

Par Cauchy-Schwarz, il est positif, donc $\|u+v\|\geqslant\big|\|u\|+\frac{\langle u,v\rangle}{\|u\|}\big|\geqslant\|u\|+\frac{\langle u,v\rangle}{\|u\|}$, ce qui est (7).

> [!PIEGE]
> De $a^2\geqslant b^2$ avec $a\geqslant0$, on déduit $a\geqslant|b|\geqslant b$ : le passage à la racine fait apparaître une valeur absolue, qu'il faut écrire.

### Question 21(a)

> [!INDICATION]
> Écrivez $W={}^tBV$ et faites passer ${}^tB$ de l'autre côté du produit scalaire. Distinguez $BX_0\neq0$ et $BX_0=0$.

> [!INDICATION]
> Si $BX_0\neq0$, la condition $\|BX_0\|V=BX_0$ détermine $V$ ; appliquez alors (7) avec $u=BX_0$ et $v=B(X-X_0)$. Sinon, Cauchy-Schwarz suffit.

#### Solution

$\langle W,X-X_0\rangle=\langle V,B(X-X_0)\rangle$.

*Si $BX_0\neq0$* : $\|V\|=1$ et $V=BX_0/\|BX_0\|$. Par (7) :

$$\|BX\|-\|BX_0\|\geqslant\frac{\langle BX_0,B(X-X_0)\rangle}{\|BX_0\|}=\langle W,X-X_0\rangle.$$

*Si $BX_0=0$* : $\langle W,X-X_0\rangle=\langle V,BX\rangle\leqslant\|V\|\,\|BX\|\leqslant\|BX\|-\|BX_0\|$.

### Question 21(b)

> [!INDICATION]
> Combinez (2) avec $H=X-X_0$, la question 11 et le (a).

#### Solution

Par (2) et la question 11, $J_0(X)-J_0(X_0)\geqslant\langle D(X_0),X-X_0\rangle$. En ajoutant (a), on obtient $J(X)-J(X_0)\geqslant\langle D(X_0)+W,X-X_0\rangle$.

> [!METHODE]
> (8) est une inégalité de « sous-gradient » : $D(X_0)+W$ joue le rôle du gradient d'une fonction convexe, et la fonction est au-dessus de son « plan tangent ».

### Question 22

> [!INDICATION]
> Le sens direct a été fait. Pour la réciproque, choisissez bien $W$ dans (8).

#### Solution

Sens direct : questions 18 ($BX_0\neq0$) et 19 ($BX_0=0$). Réciproque : (8) avec $W=-D(X_0)$ donne $J(X)\geqslant J(X_0)$ pour tout $X$.

### Question 23(a)

> [!INDICATION]
> Comparez $(\lambda+a)^2$ et $4\lambda a$ pour $a>0$.

#### Solution

$(\lambda+\alpha_i^2)^2-4\lambda\alpha_i^2=(\lambda-\alpha_i^2)^2\geqslant0$, donc chaque terme est majoré par $\dfrac{y_i^2}{4\lambda}$ ; on somme.

### Question 23(b)

> [!INDICATION]
> Étudiez les variations de $F$ et ses valeurs aux bornes de $[0,+\infty[$.

> [!INDICATION]
> Pour l'inégalité, évaluez la majoration de (a) en $\lambda_0$.

#### Solution

$\rho(Y)>1$ impose qu'un $y_i$ ($i\leqslant k$) soit non nul, donc :

$$F'(\lambda)=-2\sum_{i=1}^{k}\frac{\alpha_i^2y_i^2}{(\lambda+\alpha_i^2)^3}<0.$$

$F$ est continue, strictement décroissante, $F(0)=\rho(Y)-1>0$ et $F(\lambda)\to-1$ en $+\infty$. Par le théorème de la bijection, $F$ s'annule en un unique $\lambda_0>0$.

Ensuite $0=F(\lambda_0)\leqslant-1+\frac{1}{4\lambda_0}\sum_{i\leqslant k}y_i^2$, d'où $\lambda_0\leqslant\frac14\sum_{i\leqslant k}y_i^2$.

### Question 23(c)

> [!INDICATION]
> Par la question 22, il suffit de prouver $-D(X_0)\in\mathscr{N}(X_0)$. Ici $D(X)=X-Y$ et ${}^tB=B$.

> [!INDICATION]
> Calculez $BX_0$ composante par composante : il est proportionnel à $V$. Calculez aussi $\|V\|^2$ et reconnaissez $F$.

#### Solution

$-D(X_0)=Y-X_0=BV={}^tBV$. Pour $i\leqslant k$ :

$$(BX_0)_i=\alpha_iy_i\Big(1-\frac{\alpha_i^2}{\beta+\alpha_i^2}\Big)=\beta v_i,$$

et $(BX_0)_i=0=\beta v_i$ pour $i>k$ : $BX_0=\beta V$. De plus $\|V\|^2=1+F(\beta)$.

- Si $\rho(Y)\leqslant1$ : $\beta=0$, $\|V\|^2=\rho(Y)\leqslant1$ et $BX_0=0$.
- Si $\rho(Y)>1$ : $\beta=\lambda_0$, $\|V\|=1$ et $BX_0=\lambda_0V$, donc $\|BX_0\|V=\lambda_0V=BX_0$.

Dans les deux cas $-D(X_0)\in\mathscr{N}(X_0)$, et $X_0$ réalise un minimum global de $J$.

> [!METHODE]
> La fonction $F$ n'était pas parachutée : $F(\beta)=\|V\|^2-1$. Repérer ce lien rend la vérification immédiate.

### Question 23(d)i

> [!INDICATION]
> Une boucle sur les $k$ premiers indices suffit ; attention à l'indexation Python à partir de 0.

#### Solution

```python
def FoncSom(alpha, Y, lda):
    k = len(alpha)
    s = -1
    for i in range(k):
        s = s + alpha[i]**2 * Y[i]**2 / (lda + alpha[i]**2)**2
    return s
```

### Question 23(d)ii

> [!INDICATION]
> $F$ est décroissante : quel est le signe de $F$ aux deux bornes de l'intervalle de départ ? Gardez cet invariant à chaque étape.

#### Solution

On maintient $F(a)>0\geqslant F(b)$ ; au départ $F(0)>0$ et $F(b)\leqslant0$ pour $b=\frac14\sum_{i\leqslant k}y_i^2$ par 23(a). On renvoie $0$ si $\rho(Y)\leqslant1$, pour servir en iii.

```python
def CalcBeta(alpha, Y, epsilon):
    k = len(alpha)
    rho = 0
    for i in range(k):
        rho = rho + Y[i]**2 / alpha[i]**2
    if rho <= 1:
        return 0
    a = 0
    b = 0
    for i in range(k):
        b = b + Y[i]**2
    b = b / 4
    while b - a > epsilon:
        c = (a + b) / 2
        if FoncSom(alpha, Y, c) > 0:
            a = c
        else:
            b = c
    return (a + b) / 2
```

> [!PIEGE]
> Le test doit suivre le sens de variation : $F$ est *décroissante*, donc si $F(c)>0$ la racine est à droite de $c$ ($a$ prend la valeur $c$).

### Question 23(d)iii

> [!INDICATION]
> Calculez $\beta$, puis les $v_i$ et enfin $X_0=Y-BV$ ; les composantes d'indice supérieur à $k$ ne changent pas.

#### Solution

```python
def CalcSolution(alpha, Y, epsilon):
    n = len(Y)
    k = len(alpha)
    beta = CalcBeta(alpha, Y, epsilon)
    X0 = np.zeros(n)
    for i in range(n):
        X0[i] = Y[i]
    for i in range(k):
        v = alpha[i] * Y[i] / (beta + alpha[i]**2)
        X0[i] = Y[i] - alpha[i] * v
    return X0
```

---

## Bilan

- **Adjoint et équation normale.** Les relations $\operatorname{Im}({}^tA)=\ker(A)^\perp$, $\ker({}^tA)=\operatorname{Im}(A)^\perp$, $\ker({}^tAA)=\ker(A)$ et $\operatorname{Im}({}^tAA)=\operatorname{Im}({}^tA)$ reviennent dans tous les sujets de moindres carrés. Elles se démontrent par inclusion et égalité des dimensions.
- **Projection orthogonale.** Pour identifier un projecteur orthogonal, on vérifie l'appartenance à $G$ et l'orthogonalité du reste. La matrice $Q=AM^{-1}\,{}^tA$ est symétrique et idempotente ; sa trace vaut son rang.
- **Exploiter un minimum.** Perturber $X_0$ en $X_0+tH$, diviser par $t$ en tenant compte de son signe, passer à la limite. Le même schéma donne la condition $\nabla f=0$ dans le cas différentiable et l'inégalité 19(a) dans le cas non différentiable.
- **Calculs d'espérance de formes quadratiques gaussiennes.** Séparer diagonale et hors-diagonale, annuler par indépendance tout terme où un indice apparaît une seule fois, utiliser $\mathbb{E}(N^4)=3$.
- **À revoir.** Théorème du rang, rang de la transposée, trace d'un projecteur, moments de la loi normale, lemme des coalitions, inégalité de Bienaymé-Tchebychev, dichotomie (invariant et sens de variation).
- **Questions transposables.** Q5–Q6 (noyaux et images de ${}^tAA$), Q10 (matrice de projection), 16(f)–16(i) (espérance et variance d'une forme quadratique gaussienne), Q20 (minoration de $\|u+v\|$), 23(d)ii (dichotomie).
- **Conseil du rapport 2025.** « Rendez une copie le plus propre possible. Entourez les résultats, soulignez les théorèmes utilisés. »
