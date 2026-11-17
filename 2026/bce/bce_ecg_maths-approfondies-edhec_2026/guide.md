# BCE ECG — Mathématiques approfondies (EDHEC) 2026 · Corrigé guidé

*Corrigé rédigé par IA, non officiel. Signalez toute erreur.*

## Présentation du sujet

**Cadre.** Épreuve de 4 heures, conception EDHEC BS, sans document ni calculatrice. Trois exercices et un problème, 64 questions au niveau le plus fin. Selon le rapport 2026, le barème (220 points, plus 5 points de bonus de présentation) se répartit en 19,6 % pour l'exercice 1, 23,2 % pour l'exercice 2, 18,6 % pour l'exercice 3 et 38,6 % pour le problème. 2980 copies ont été corrigées, avec une moyenne de 11,24 et un écart-type de 5,40.

**Exercice 1 (probabilités, 9 questions).** Produit $Z=X_1X_2$ de deux variables uniformes indépendantes : moments par indépendance, loi de $\ln X_1$, densité de $Y_1+Y_2$ par convolution, fonction de répartition et densité de $Z=\mathrm{e}^{Y_1+Y_2}$, intégrales $\int_0^1x^n\ln x\,\mathrm{d}x$.

**Exercice 2 (analyse, 13 questions).** Suites $u_{n+1}=\sqrt{(1+u_n)/2}$ et $v_{n+1}=v_n/u_{n+1}$ : on montre $v_n=2^n\sin(\pi/2^n)\to\pi$ (méthode d'Archimède par les polygones), on obtient le développement asymptotique de $v_n$, puis on accélère la convergence par la méthode de Richardson, présentée ensuite en général.

**Exercice 3 (probabilités, 14 questions).** Un mobile qui, à l'instant $k$, se place uniformément sur $\{0,\dots,k\}$ ; loi du premier retour en $0$ (sans espérance) ; puis une variable $Z_n$, géométrique de paramètre aléatoire, qui converge en loi vers ce temps de retour, avec $E(Z_n)=\sum_{k\leqslant n}\frac1k\sim\ln n$.

**Problème (algèbre bilinéaire, 28 questions).** Matrices symétriques positives : caractérisation spectrale, existence et unicité de la racine carrée positive (par un polynôme d'interpolation de Lagrange et la co-diagonalisation de deux endomorphismes qui commutent), puis la décroissance de $S\mapsto S^{-1}$ pour l'ordre des matrices positives.

**Notions du programme.** Variables à densité (fonction de répartition, transformation, convolution), espérance et variance, formule de l'espérance totale, loi géométrique, convergence en loi pour des variables à valeurs entières ; suites récurrentes, bijection continue strictement monotone, développements limités, équivalents, sommes de Riemann, comparaison série-intégrale ; théorème spectral, endomorphismes symétriques, sous-espaces stables, polynômes de matrices ; Python.

**Difficulté.** Le sujet est long mais très guidé. Les exercices 1 et 3 sont classiques ; la fin de l'exercice 2 et les parties 3 et 4 du problème sont plus exigeantes. Le rapport juge que le problème a été « très peu réussi, tant les connaissances en algèbre bilinéaire semblent fragiles ».

**Questions à ne pas laisser passer.** Ex1 : 1, 2, 3.a–b, 5.a. Ex2 : 1, 2, 3.c, 5.a–b. Ex3 : 1.a–b, 2.a–d, 3, 6.a–b. Problème : 1.a–b, 2.a–c, 4.a–b, 5, 6.b, 7.a, 10.a.

**Gestion du temps.** Environ 40 minutes pour l'exercice 1, 55 minutes pour l'exercice 2, 45 minutes pour l'exercice 3 et 1 h 30 pour le problème, avec une relecture.

> [!JURY]
> Le rapport 2026 conseille : « il ne faut pas consacrer plus de 3 ou 4 minutes de réflexion sur une question et accepter de ne pas avoir les moyens de la traiter. En revanche, il faut prendre son temps pour rédiger correctement une solution et pour terminer un long calcul. »

---

## Exercice 1 — Produit de deux variables uniformes

On obtient la loi de $Z=X_1X_2$ en passant au logarithme : le produit devient une somme, dont la densité est une convolution.

### Question 1

> [!INDICATION]
> `rd.random()` simule une variable de loi uniforme sur $[0,1[$ ; deux appels sont indépendants.

#### Solution

```python
def simulZ():
    return rd.random() * rd.random()
```

### Question 2

> [!INDICATION]
> Pourquoi $Z$ a-t-elle des moments de tout ordre ? Pour les calculer, l'indépendance permet de factoriser.

> [!INDICATION]
> $E(X_1X_2)=E(X_1)E(X_2)$ et $E(Z^2)=E(X_1^2)E(X_2^2)$, toujours par indépendance.

#### Solution

$Z$ est bornée (valeurs dans $]0,1]$), donc admet espérance et variance. Par indépendance, $E(Z)=\frac12\cdot\frac12=\frac14$ et $E(Z^2)=\frac13\cdot\frac13=\frac19$, donc

$$E(Z)=\frac14$$

$$\begin{aligned}
V(Z) &= \frac19-\frac1{16}\\
&= \frac7{144}.
\end{aligned}$$

> [!PIEGE]
> $V(X_1X_2)\neq V(X_1)V(X_2)$ : on passe par $E(Z^2)$. Et l'égalité $E(X_1X_2)=E(X_1)E(X_2)$ demande l'indépendance, qu'il faut citer.

### Question 3(a)

> [!INDICATION]
> Écrire $(\ln X_1\leqslant x)=(X_1\leqslant\mathrm{e}^x)$ et distinguer selon la position de $\mathrm{e}^x$ par rapport à $1$.

#### Solution

$F(x)=P(X_1\leqslant\mathrm{e}^x)$, qui vaut $\mathrm{e}^x$ si $x\leqslant0$ (car $\mathrm{e}^x\in\,]0,1]$) et $1$ si $x>0$.

> [!JURY]
> Le rapport 2026 relève, pour cet exercice, « la gestion calamiteuse des différentes facettes des fonctions de répartition ». Une fonction de répartition se définit sur tout $\mathbb{R}$ : chaque cas doit être traité.

### Question 3(b)

> [!INDICATION]
> Vérifier que $F$ est continue sur $\mathbb{R}$ et de classe $\mathcal{C}^1$ sauf en un nombre fini de points, puis dériver.

#### Solution

$F$ est continue sur $\mathbb{R}$, de classe $\mathcal{C}^1$ sur $\mathbb{R}^*$.

Une densité est donnée par $f(x)=\mathrm{e}^x$ pour $x\leqslant0$ et $f(x)=0$ pour $x>0$.

(C'est la loi de $-E$, avec $E\hookrightarrow\mathcal{E}(1)$.)

### Question 4(a)

> [!INDICATION]
> $Y_1$ et $Y_2$ sont indépendantes et à densité : la densité de leur somme est un produit de convolution.

> [!INDICATION]
> Déterminer l'ensemble des $t$ pour lesquels $f(t)f(x-t)\neq0$, selon le signe de $x$.

#### Solution

$h(x)=\int_{\mathbb{R}}f(t)f(x-t)\,\mathrm{d}t$, l'intégrande étant non nul exactement pour $x\leqslant t\leqslant0$.

- Si $x>0$ : $h(x)=0$.
- Si $x\leqslant0$ :

$$\begin{aligned}
h(x) &= \int_x^0\mathrm{e}^t\mathrm{e}^{x-t}\,\mathrm{d}t\\
&= -x\,\mathrm{e}^x .
\end{aligned}$$

> [!JURY]
> Le rapport 2026 critique « la mise en place peu rigoureuse du produit de convolution de deux variables indépendantes ». Il faut citer l'indépendance, et justifier les bornes de l'intégrale par l'étude du support de l'intégrande.

### Question 4(b)

> [!INDICATION]
> Intégrer $h$ de $-\infty$ à $x$ ; une intégration par parties donne une primitive de $t\mapsto-t\,\mathrm{e}^t$.

#### Solution

Une primitive de $-t\,\mathrm{e}^t$ est $(1-t)\,\mathrm{e}^t$, de limite nulle en $-\infty$.

Donc $H(x)=(1-x)\,\mathrm{e}^x$ si $x\leqslant0$, et $H(x)=1$ si $x>0$.

### Question 4(c)

> [!INDICATION]
> $Z=\mathrm{e}^{Y_1+Y_2}$. Pour $0<x<1$, traduire $(Z\leqslant x)$ en un événement sur $Y_1+Y_2$.

> [!INDICATION]
> Pour la densité : continuité de $F_Z$ sur $\mathbb{R}$, caractère $\mathcal{C}^1$ sauf en $0$ et $1$, puis dérivation.

#### Solution

$F_Z(x)=0$ si $x\leqslant0$, $F_Z(x)=1$ si $x\geqslant1$, et pour $0<x<1$ :

$$\begin{aligned}
F_Z(x) &= H(\ln x)\\
&= x\,(1-\ln x).
\end{aligned}$$

$F_Z$ est continue : sa limite à droite en $0$ est nulle et sa valeur en $1$ est $1$. Elle est de classe $\mathcal{C}^1$ sauf en ces deux points.

Sur $]0,1[$, $F_Z'(x)=-\ln x$.

D'où la densité $f_Z$ de l'énoncé.

> [!METHODE]
> Pour la loi de $g(Y)$ avec $g$ strictement croissante, on écrit $F_{g(Y)}(x)=F_Y(g^{-1}(x))$ sur l'image de $g$, et l'on traite à part les $x$ hors de cette image.

### Question 5(a)

> [!INDICATION]
> Intégrer par parties sur $[\varepsilon,1]$, en dérivant $\ln$.

> [!INDICATION]
> La limite de $\varepsilon^{n+1}\ln\varepsilon$ en $0^+$ relève des croissances comparées ; ne pas oublier le cas $n=0$.

#### Solution

$$\int_\varepsilon^1x^n\ln x\,\mathrm{d}x=-\frac{\varepsilon^{n+1}\ln\varepsilon}{n+1}-\frac{1-\varepsilon^{n+1}}{(n+1)^2}\xrightarrow[\varepsilon\to0^+]{}-\frac1{(n+1)^2}.$$

L'intégrale converge et vaut $-\frac1{(n+1)^2}$.

> [!PIEGE]
> Pour $n=0$, la fonction $\ln$ n'est pas prolongeable par continuité en $0$ : l'intégrale est bien impropre, et c'est l'intégration par parties qui en donne la convergence. La formule reste valable : $\int_0^1\ln x\,\mathrm{d}x=-1$.

### Question 5(b)

> [!INDICATION]
> Théorème de transfert pour une variable à densité, puis 5.a avec $n=1$ et $n=2$.

#### Solution

$E(Z)=\int_0^1x(-\ln x)\,\mathrm{d}x=\frac14$ et $E(Z^2)=\int_0^1x^2(-\ln x)\,\mathrm{d}x=\frac19$ (intégrales convergentes de fonctions positives), d'où $V(Z)=\frac7{144}$.

---

## Exercice 2 — Approximation de $\pi$ et méthode de Richardson

On reconnaît dans $(v_n)$ les demi-périmètres de polygones réguliers à $2^n$ côtés inscrits dans le cercle unité (méthode d'Archimède). Le développement asymptotique de $v_n-\pi$ permet d'éliminer le terme d'erreur principal.

### Question 1

> [!INDICATION]
> Récurrence sur une propriété qui contient à la fois l'existence des termes et un encadrement de $u_n$.

> [!INDICATION]
> Il faut $1+u_n\geqslant0$ pour la racine et $u_{n+1}\neq0$ pour la division.

#### Solution

On montre par récurrence : « $u_n,v_n$ sont définis et $u_n\in[0,1]$ ». Si c'est vrai au rang $n$, $\frac{1+u_n}2\in\big[\frac12,1\big]$, donc $u_{n+1}\in\big[\frac{\sqrt2}2,1\big]$ est défini et non nul, et $v_{n+1}$ est défini.

> [!JURY]
> Le rapport 2026 note que « Peu de questions ont été réellement réussies (y compris la récurrence du début) ». La propriété de récurrence doit être énoncée avant d'être démontrée, et doit contenir l'information qui fait marcher l'hérédité ($u_n\geqslant0$, donc $u_{n+1}>0$).

### Question 2

> [!INDICATION]
> Dans la boucle, mettre à jour $u$ avant $v$, puisque $v_{k}$ s'exprime avec $u_{k}$.

#### Solution

```python
def suite_v(n):
    u = 0
    v = 2
    for k in range(2, n + 1):
        u = np.sqrt((1 + u) / 2)
        v = v / u
    return v
```

Testée : `suite_v(5)` renvoie environ $3{,}13655$, égal à $2^5\sin(\pi/32)$.

> [!PIEGE]
> Inverser les deux lignes de la boucle calculerait $v_k=v_{k-1}/u_{k-1}$, avec une division par $u_1=0$ au premier tour.

### Question 3(a)

> [!INDICATION]
> Théorème de la bijection pour $\cos$ sur $[0,\pi/2]$.

#### Solution

$\cos$ est continue et strictement décroissante de $\big[0,\frac\pi2\big]$ sur $[0,1]$ : c'est une bijection. Comme $u_n\in[0,1]$, $\alpha_n$ existe et est unique.

### Question 3(b)

> [!INDICATION]
> Exprimer $u_{n+1}$ en fonction de $\alpha_n$ avec la formule de $\cos(2a)$, puis utiliser l'unicité de 3.a.

#### Solution

$\alpha_1=\frac\pi2$. Comme $1+\cos\alpha_n=2\cos^2\frac{\alpha_n}2$ et $\cos\frac{\alpha_n}{2}\geqslant0$ :

$$u_{n+1}=\cos\frac{\alpha_n}2,\qquad\frac{\alpha_n}2\in\Big[0,\frac\pi2\Big],$$

donc $\alpha_{n+1}=\frac{\alpha_n}2$ par unicité, et $\boxed{\alpha_n=\frac\pi{2^n}}$.

> [!PIEGE]
> $\sqrt{\cos^2a}=|\cos a|$ : il faut justifier que $\cos\frac{\alpha_n}{2}\geqslant0$, et que $\frac{\alpha_n}2$ est dans l'intervalle où l'unicité s'applique.

### Question 3(c)

> [!INDICATION]
> Récurrence, avec $\sin(2a)=2\sin a\cos a$ appliquée à $a=\frac\pi{2^{n+1}}$.

#### Solution

$v_1=2$, et si $v_n=2^n\sin\frac\pi{2^n}$ :

$$\begin{aligned}
v_{n+1} &= \frac{2^n\cdot2\sin\frac\pi{2^{n+1}}\cos\frac\pi{2^{n+1}}}{\cos\frac\pi{2^{n+1}}}\\
&= 2^{n+1}\sin\frac\pi{2^{n+1}} .
\end{aligned}$$

Comme $\sin x\sim x$ en $0$, $v_n\to\pi$.

### Question 4

> [!INDICATION]
> Écrire $v_n=\pi\frac{\sin x_n}{x_n}$ avec $x_n=\frac\pi{2^n}\to0$, et diviser le développement limité du sinus par $x$.

#### Solution

$\frac{\sin x}x=1-\frac{x^2}6+\frac{x^4}{120}+o(x^4)$, et $x_n^2=\frac{\pi^2}{4^n}$, $x_n^4=\frac{\pi^4}{4^{2n}}$, donc

$$v_n=\pi-\frac{\pi^3}{6\cdot4^n}+\frac{\pi^5}{120\cdot4^{2n}}+o\Big(\frac1{4^{2n}}\Big),$$

soit $a=\pi$, $b=-\frac{\pi^3}6$, $c=\frac{\pi^5}{120}$.

### Question 5(a)

> [!INDICATION]
> Deux appels à `suite_v`.

#### Solution

```python
def suite_w(n):
    return (4 * suite_v(n + 1) - suite_v(n)) / 3
```

### Question 5(b)

> [!INDICATION]
> Opérations sur les limites.

#### Solution

$w_n\to\frac{4\pi-\pi}3=\pi$.

### Question 5(c)

> [!INDICATION]
> Écrire le développement de 4 au rang $n+1$, multiplier par $4$ et retrancher $v_n$ : quel terme disparaît ?

> [!INDICATION]
> Pour l'équivalent du quotient, prendre un équivalent du numérateur et du dénominateur, puis faire le quotient.

#### Solution

Avec $4^{n+1}=4\cdot4^n$ et $4^{2n+2}=16\cdot4^{2n}$ :

$$4v_{n+1}=4\pi-\frac{\pi^3}{6\cdot4^n}+\frac{\pi^5}{480\cdot4^{2n}}+o\Big(\frac1{4^{2n}}\Big).$$

Les termes en $\frac1{4^n}$ se compensent avec ceux de $v_n$, et $\frac1{480}-\frac1{120}=-\frac3{480}$ :

$$w_n=\pi-\frac{\pi^5}{480\cdot4^{2n}}+o\Big(\frac1{4^{2n}}\Big).$$

Alors $w_n-\pi\sim-\frac{\pi^5}{480\cdot4^{2n}}$ et $v_n-\pi\sim-\frac{\pi^3}{6\cdot4^n}$, donc

$$\frac{w_n-\pi}{v_n-\pi}\sim\frac{\pi^2}{80\cdot4^n}.$$

> [!JURY]
> Le rapport 2026 indique que la fin de l'exercice « a eu raison d'un grand nombre de candidats, notamment la recherche d'un équivalent de » ce quotient. La méthode est pourtant mécanique : un développement donne un équivalent dès que son premier coefficient est non nul.

> [!METHODE]
> On ne divise pas deux développements limités terme à terme ; on passe aux équivalents (compatibles avec le quotient), ce qui exige des coefficients principaux non nuls.

### Question 5(d)

> [!INDICATION]
> Que dit la limite du quotient de 5.c sur la précision de $w_n$ par rapport à celle de $v_n$ ?

#### Solution

$\frac{w_n-\pi}{v_n-\pi}\to0$ : l'erreur de $w_n$, de l'ordre de $16^{-n}$, est négligeable devant celle de $v_n$, de l'ordre de $4^{-n}$, pour un coût de calcul presque identique.

Numériquement, $w_5\approx3{,}1415920$ contre $v_5\approx3{,}1365$.

### Question 6(a)

> [!INDICATION]
> Chercher $y_n=\alpha x_{n+1}+\beta x_n$ ; imposer $\alpha+\beta=1$ pour garder la limite $a$, et éliminer le terme en $q^n$.

#### Solution

$y_n=\frac{x_{n+1}-qx_n}{1-q}$. Le terme en $q^n$ disparaît ($bq^{n+1}-q\cdot bq^n=0$) et

$$y_n=a+\frac{c(r-q)}{1-q}\,r^n+o(r^n)$$

$$d=\frac{c(r-q)}{1-q}.$$

> [!PIEGE]
> $o(r^{n+1})=o(r^n)$ car $r^{n+1}=r\cdot r^n$ : il faut le dire avant de regrouper les restes.

### Question 6(b)

> [!INDICATION]
> Comparer $r^n$ à $q^n$ quand $r<q$.

#### Solution

$\big(\frac rq\big)^n\to0$, donc $cr^n+o(r^n)=o(q^n)$ et $x_n=a+bq^n+o(q^n)$.

### Question 6(c)

> [!INDICATION]
> Montrer que $\frac{y_n-a}{x_n-a}\to0$ à l'aide d'équivalents ; vérifier que les coefficients $b$ et $d$ sont non nuls.

#### Solution

$x_n-a\sim bq^n$ et $y_n-a\sim dr^n$ ($b\neq0$, $d\neq0$ car $c\neq0$ et $r\neq q$).

Donc $\frac{y_n-a}{x_n-a}\sim\frac db\big(\frac rq\big)^n\to0$ : $(y_n)$ converge plus vite vers $a$. La question 5 en est le cas $q=\frac14$, $r=\frac1{16}$.

---

## Exercice 3 — Un mobile aléatoire et une convergence en loi

Partie 1 : loi du premier retour en $0$, qui n'a pas d'espérance. Partie 2 : une variable géométrique de paramètre aléatoire, qui converge en loi vers ce temps de retour.

### Question 1(a)

> [!INDICATION]
> À l'instant $k$, combien de points sont possibles ?

#### Solution

$X_k$ suit la loi uniforme sur $[\![0;k]\!]$ : $P(X_k=i)=\frac1{k+1}$ pour $i\in[\![0;k]\!]$.

> [!JURY]
> Le rapport 2026 : « la loi uniforme du début a laissé pas mal d'entre eux sur le carreau et un nombre incroyable de confusions se sont fait jour entre indices et variables pour l'écriture de $P(X_k = i)$ même en ayant reconnu la bonne loi. »

### Question 1(b)

> [!INDICATION]
> Se ramener à la loi uniforme sur $[\![1;k+1]\!]$, dont l'espérance et la variance sont au programme.

#### Solution

$X_k+1\hookrightarrow\mathcal{U}([\![1;k+1]\!])$, donc $E(X_k)=\frac{k+2}2-1=\frac k2$ et $V(X_k)=\frac{(k+1)^2-1}{12}=\frac{k(k+2)}{12}$.

### Question 2(a)

> [!INDICATION]
> Le premier retour à l'instant $n$ : absent de $0$ avant, présent à l'instant $n$.

#### Solution

$$\begin{aligned}
(Y=n)&=\Big(\bigcap_{k=1}^{n-1}(X_k\neq0)\Big)\\
&\quad\cap(X_n=0).
\end{aligned}$$

### Question 2(b)

> [!INDICATION]
> L'indépendance mutuelle transforme la probabilité de l'intersection en produit ; le produit obtenu est télescopique.

#### Solution

$$\begin{aligned}
P(Y=n) &= \prod_{k=1}^{n-1}\frac{k}{k+1}\cdot\frac1{n+1}\\
&= \frac1{n(n+1)}=\frac1n-\frac1{n+1}.
\end{aligned}$$

### Question 2(c)

> [!INDICATION]
> Somme télescopique ; puis système complet d'événements.

#### Solution

$\sum_{n=1}^NP(Y=n)=1-\frac1{N+1}\to1$, donc $P(Y=0)=0$ : presque sûrement, le mobile revient en $0$.

### Question 2(d)

> [!INDICATION]
> Étudier la série de terme général $nP(Y=n)$.

#### Solution

$nP(Y=n)=\frac1{n+1}$ : série harmonique divergente, **$Y$ n'a pas d'espérance**.

> [!METHODE]
> Retour presque sûr mais temps de retour d'espérance infinie : c'est le même phénomène que pour la marche aléatoire simple sur $\mathbb{Z}$.

### Question 3

> [!INDICATION]
> `rd.randint(a, b)` renvoie un entier uniforme de $[\![a;b-1]\!]$ ; `rd.geometric(p)` simule la loi géométrique de paramètre $p$.

#### Solution

```python
def var_Z(n):
    U = rd.randint(0, n)
    Z = rd.geometric(1 - U / n)
    return Z
```

Testée avec $n=50$ sur $100\,000$ tirages : les fréquences de $1,2,3$ sont proches de $\frac12,\frac16,\frac1{12}$.

> [!PIEGE]
> `rd.randint(0, n - 1)` ne prendrait jamais la valeur $n-1$ : la borne supérieure est exclue.

### Question 4(a)

> [!INDICATION]
> Formule des probabilités totales avec le système complet $\big((U_n=k)\big)_{0\leqslant k\leqslant n-1}$.

#### Solution

$$\begin{aligned}
P(Z_n=i)&=\frac1n\sum_{k=0}^{n-1}\Big(\frac kn\Big)^{i-1}\\
&\qquad\times\Big(1-\frac kn\Big) ,
\end{aligned}$$

et l'on développe $\big(1-\frac kn\big)$. Pour $k=0$, $i=1$, la convention $0^0=1$ correspond à $P_{(U_n=0)}(Z_n=1)=1$.

### Question 4(b)

> [!INDICATION]
> Reconnaître des sommes de Riemann sur $[0,1]$.

#### Solution

$\frac1n\sum_{k=0}^{n-1}g\big(\frac kn\big)\to\int_0^1g$ pour $g$ continue sur $[0,1]$, d'où

$$\lim_{n\to+\infty}P(Z_n=i)=\frac1i-\frac1{i+1}.$$

### Question 4(c)

> [!INDICATION]
> Comparer avec la loi de $Y$ (question 2.b) ; quelle caractérisation de la convergence en loi pour des variables à valeurs entières ?

#### Solution

Pour tout $i\in\mathbb{N}$, $P(Z_n=i)\to P(Y=i)$ (y compris $i=0$, où les deux valent $0$). Pour des variables à valeurs dans $\mathbb{N}$, cela équivaut à la convergence en loi :

**$Z_n$ converge en loi vers $Y$.**

> [!METHODE]
> Remarquer que la limite en loi $Y$ n'a pas d'espérance, alors que chaque $Z_n$ en a une : la convergence en loi ne dit rien de la convergence des espérances. La question 6 montre d'ailleurs que $E(Z_n)\to+\infty$.

### Question 5

> [!INDICATION]
> Le système complet est fini : que reste-t-il à vérifier pour appliquer la formule de l'espérance totale ?

> [!INDICATION]
> L'espérance de la loi géométrique de paramètre $p$ est $\frac1p$ ; réindexer la somme obtenue.

#### Solution

Le système $\big((U_n=k)\big)_k$ est fini et chaque loi conditionnelle (géométrique de paramètre $1-\frac kn>0$) a une espérance $\frac n{n-k}$. Donc

$$\begin{aligned}
E(Z_n) &= \frac1n\sum_{k=0}^{n-1}\frac{n}{n-k}\\
&= \sum_{j=1}^n\frac1j .
\end{aligned}$$

### Question 6(a)

> [!INDICATION]
> Encadrer $\frac1t$ sur $[k,k+1]$ et intégrer.

#### Solution

Pour $t\in[k,k+1]$, $\frac1{k+1}\leqslant\frac1t\leqslant\frac1k$ ; en intégrant, $\frac1{k+1}\leqslant\ln(k+1)-\ln k\leqslant\frac1k$.

### Question 6(b)

> [!INDICATION]
> Sommer pour $k$ de $1$ à $n-1$ : la somme centrale est télescopique.

#### Solution

$\sum_{k=2}^n\frac1k\leqslant\ln n\leqslant\sum_{k=1}^{n-1}\frac1k$, soit $E(Z_n)-1\leqslant\ln n\leqslant E(Z_n)-\frac1n$, d'où

$$\ln(n)+\frac1n\leqslant E(Z_n)\leqslant\ln(n)+1 .$$

### Question 6(c)

> [!INDICATION]
> Diviser par $\ln n>0$ et encadrer.

#### Solution

$1+\frac1{n\ln n}\leqslant\frac{E(Z_n)}{\ln n}\leqslant1+\frac1{\ln n}$, donc $E(Z_n)\sim\ln n$.

---

## Problème — Racine carrée d'une matrice symétrique positive

Partie 1 : positivité $\iff$ valeurs propres positives. Partie 2 : existence de $B=P\Delta\,{}^tP$ et écriture $B=S(A)$ avec un polynôme $S$. Partie 3 : unicité par co-diagonalisation. Partie 4 : si $S_2-S_1$ est positive, alors $S_1^{-1}-S_2^{-1}$ l'est aussi.

> [!JURY]
> Le rapport 2026 : le problème « a été abordé par de nombreux candidats, mais presque jamais dans son intégralité certainement par manque de temps ». Les parties 1 et 2 sont pourtant des questions de cours.

### Question 1(a)

> [!INDICATION]
> Prendre un vecteur propre et calculer ${}^tXAX$.

#### Solution

Si $AX=\lambda X$ avec $X\neq0$, alors ${}^tXAX=\lambda\,{}^tXX$ et ${}^tXX=\|X\|^2>0$, d'où $\lambda=\frac{{}^tXAX}{{}^tXX}$.

### Question 1(b)

> [!INDICATION]
> Signe du numérateur et du dénominateur.

#### Solution

${}^tXAX\geqslant0$ et ${}^tXX>0$, donc $\lambda\geqslant0$.

### Question 2(a)

> [!INDICATION]
> Théorème spectral.

#### Solution

$A$ est symétrique réelle : il existe $P$ orthogonale et $D$ diagonale avec ${}^tPAP=D$, soit $A=PD\,{}^tP$.

### Question 2(b)

> [!INDICATION]
> Transposer $Y={}^tPX$.

#### Solution

${}^tY={}^tXP$, donc ${}^tYDY={}^tXPD\,{}^tPX={}^tXAX$.

### Question 2(c)

> [!INDICATION]
> Développer ${}^tYDY$ pour $D$ diagonale.

#### Solution

${}^tXAX={}^tYDY=\sum_i\lambda_iy_i^2\geqslant0$.

### Question 3

> [!INDICATION]
> Les deux implications sont démontrées ; il reste à relier les $\lambda_i$ de $D$ aux valeurs propres de $A$.

#### Solution

$D$ est semblable à $A$, donc ses coefficients diagonaux sont les valeurs propres de $A$. Par 1 et 2 : **$A$ est positive si et seulement si ses valeurs propres sont positives.**

### Question 4(a)

> [!INDICATION]
> Signe des $\lambda_i$ quand $A$ est positive.

#### Solution

Par la partie 1, les $\lambda_i\geqslant0$, donc les $\sqrt{\lambda_i}$ existent.

### Question 4(b)

> [!INDICATION]
> Symétrie par transposition ; positivité par les valeurs propres ; puis calculer $B^2$ en utilisant ${}^tPP=I_n$.

#### Solution

${}^tB=P\,{}^t\Delta\,{}^tP=B$ ; $B$ est semblable à $\Delta$, de valeurs propres $\sqrt{\lambda_i}\geqslant0$, donc positive ; et

$$\begin{aligned}
B^2 &= P\Delta^2\,{}^tP\\
&= PD\,{}^tP=A .
\end{aligned}$$

### Question 5

> [!INDICATION]
> Évaluer chaque facteur du produit ; pour $j\neq i$, un facteur est nul.

#### Solution

$L_i(\mu_i)$ est un produit de facteurs égaux à $1$. Pour $j\neq i$, le facteur d'indice $k=j$ de $L_i(\mu_j)$ est nul. Les dénominateurs sont non nuls car les $\mu_k$ sont distincts.

> [!METHODE]
> Les $L_i$ sont les polynômes d'interpolation de Lagrange : $\sum_i y_iL_i$ est le polynôme de degré au plus $p-1$ qui prend la valeur $y_i$ en $\mu_i$.

### Question 6(a)

> [!INDICATION]
> Utiliser 5, puis le fait que chaque $\lambda_i$ est l'un des $\mu_k$.

#### Solution

$S(\mu_k)=\sum_i\sqrt{\mu_i}L_i(\mu_k)=\sqrt{\mu_k}$, et donc $S(\lambda_i)=\sqrt{\lambda_i}$.

### Question 6(b)

> [!INDICATION]
> Récurrence, en utilisant ${}^tPP=I_n$.

#### Solution

$A^0=I_n=PD^0\,{}^tP$, et $A^{k+1}=PD^k\,{}^tP\,PD\,{}^tP=PD^{k+1}\,{}^tP$.

### Question 6(c)

> [!INDICATION]
> Écrire $S=\sum s_kX^k$ et utiliser 6.b ; $S(D)$ est diagonale de coefficients $S(\lambda_i)$.

#### Solution

$S(A)=\sum_ks_kPD^k\,{}^tP=P\,S(D)\,{}^tP$, et $S(D)=\mathrm{diag}(S(\lambda_i))=\Delta$, donc $S(A)=B$.

> [!PIEGE]
> $S(D)$ n'est pas « $S$ appliqué à chaque coefficient » en général ; c'est vrai ici parce que $D$ est diagonale, donc $D^k$ aussi, de coefficients $\lambda_i^k$.

### Question 7(a)

> [!INDICATION]
> Exprimer $A$ en fonction de $C$.

#### Solution

$AC=C^3=CA$.

### Question 7(b)

> [!INDICATION]
> Récurrence pour $A^kC=CA^k$, puis linéarité avec $B=S(A)$.

#### Solution

Si $A^kC=CA^k$, alors $A^{k+1}C=A\,CA^k=CA^{k+1}$. Comme $B=\sum s_kA^k$, $BC=CB$.

### Question 8(a)

> [!INDICATION]
> Matrices des composées dans la base canonique.

#### Solution

$b\circ c$ et $c\circ b$ ont pour matrices $BC=CB$ : elles sont égales.

### Question 8(b)

> [!INDICATION]
> Pour $x\in E_i$, calculer $b(c(x))$ en utilisant 8.a.

#### Solution

$b(c(x))=c(b(x))=\sqrt{\mu_i}\,c(x)$, donc $c(x)\in E_i$.

> [!METHODE]
> Deux endomorphismes qui commutent : chacun laisse stables les sous-espaces propres de l'autre. C'est la clé de toute co-diagonalisation.

### Question 8(c)

> [!INDICATION]
> Vérifier la définition d'un endomorphisme symétrique sur l'espace euclidien $E_i$ (produit scalaire induit).

#### Solution

Pour $x,y\in E_i$ : $\langle c_i(x),y\rangle=\langle c(x),y\rangle=\langle x,c(y)\rangle=\langle x,c_i(y)\rangle$.

### Question 8(d)

> [!INDICATION]
> Théorème spectral pour $c_i$ dans $E_i$ ; que sont les vecteurs non nuls de $E_i$ pour $b$ ?

#### Solution

$c_i$ symétrique sur l'espace euclidien $E_i$ (non nul, car $\sqrt{\mu_i}$ est valeur propre de $B$) admet une base orthonormée $\mathcal{B}_i$ de vecteurs propres.

Ses vecteurs, non nuls et dans $E_i$, sont vecteurs propres de $b$ pour $\sqrt{\mu_i}$.

### Question 8(e)

> [!INDICATION]
> Les $E_i$ sont les sous-espaces propres de $b$ : leur somme est-elle $\mathbb{R}^n$ ?

#### Solution

$b$ est symétrique donc diagonalisable, de valeurs propres $\sqrt{\mu_1},\dots,\sqrt{\mu_p}$ distinctes : $\mathbb{R}^n=E_1\oplus\dots\oplus E_p$.

La concaténation $\mathcal{B}$ des $\mathcal{B}_i$ est une base de vecteurs propres communs : les matrices de $b$ et $c$ y sont diagonales.

### Question 8(f)

> [!INDICATION]
> Dans $\mathcal{B}$, comparer les carrés des coefficients diagonaux de $b$ et $c$, et utiliser leur signe.

#### Solution

Soient $\mathrm{diag}(\beta_j)$ et $\mathrm{diag}(\gamma_j)$ les matrices de $b$ et $c$ dans $\mathcal{B}$.

On a $\beta_j^2=\gamma_j^2$ car $B^2=C^2=A$, et $\beta_j,\gamma_j\geqslant0$ (valeurs propres de matrices positives).

Donc $\beta_j=\gamma_j$, $b=c$ et $C=B$ : contradiction, d'où l'unicité.

> [!PIEGE]
> La positivité de $C$ est indispensable : $-B$ vérifie aussi $(-B)^2=A$. C'est exactement l'étape $\beta_j^2=\gamma_j^2\Rightarrow\beta_j=\gamma_j$ qui l'utilise.

### Question 9

> [!INDICATION]
> Reprendre 1.a pour le sens direct, et 2.b–2.c pour la réciproque, en suivant les inégalités strictes.

> [!INDICATION]
> Pour la réciproque, il faut $Y\neq0$ quand $X\neq0$ : pourquoi ?

#### Solution

Sens direct : $\lambda=\frac{{}^tXAX}{{}^tXX}>0$ avec $X$ vecteur propre. Réciproque : pour $X\neq0$, $Y={}^tPX\neq0$ (${}^tP$ inversible), donc $\sum\lambda_iy_i^2>0$.

### Question 10(a)

> [!INDICATION]
> Transposer.

#### Solution

${}^tN={}^tM-I_n=N$.

### Question 10(b)

> [!INDICATION]
> Si $MX=\lambda X$, que vaut $NX$ ? Puis diagonaliser $M$ orthogonalement pour étudier $I_n-M^{-1}$.

#### Solution

$NX=(\lambda-1)X$ : $\lambda-1$ est valeur propre de la matrice positive $N$, donc $\lambda\geqslant1$. Ainsi $0\notin\operatorname{Sp}(M)$ et $M$ est inversible.

Avec $M=QD'\,{}^tQ$ ($D'$ diagonale de coefficients $\nu_i\geqslant1$), $I_n-M^{-1}=Q(I_n-D'^{-1})\,{}^tQ$ est symétrique de valeurs propres $1-\frac1{\nu_i}\geqslant0$ : elle est positive.

### Question 11(a)

> [!INDICATION]
> Écrire $S_2=S_1+(S_2-S_1)$.

#### Solution

Pour $X\neq0$, ${}^tXS_2X={}^tXS_1X+{}^tX(S_2-S_1)X>0$ : $S_2$ est définie positive.

### Question 11(b)

> [!INDICATION]
> Valeurs propres de $S_1^{1/2}$ (question 9) ; puis $S_1^{-1/2}S_1S_1^{-1/2}=I_n$.

#### Solution

Les valeurs propres de $S_1^{1/2}$ sont les $\sqrt{\lambda_i}>0$ : elle est inversible. Et

$$S_1^{-1/2}(S_2-S_1)S_1^{-1/2}=S_1^{-1/2}S_2S_1^{-1/2}-I_n .$$

### Question 11(c)

> [!INDICATION]
> L'inverse d'une matrice symétrique est symétrique. Pour la positivité, poser $Y=S_1^{-1/2}X$.

#### Solution

$L$ est symétrique, donc $L-I_n$ aussi. Avec $Y=S_1^{-1/2}X$ et 11.b, ${}^tX(L-I_n)X={}^tY(S_2-S_1)Y\geqslant0$.

### Question 11(d)

> [!INDICATION]
> Appliquer la question 10 à une matrice bien choisie.

#### Solution

La question 10 avec $M=L$ ($N=L-I_n$ positive) donne : $L$ inversible et $I_n-L^{-1}$ positive.

### Question 11(e)

> [!INDICATION]
> Calculer $L^{-1}$ (inverse d'un produit) et développer $S_1^{1/2}(S_1^{-1}-S_2^{-1})S_1^{1/2}$.

> [!INDICATION]
> Pour conclure, revenir à $S_1^{-1}-S_2^{-1}$ par le changement $X=S_1^{1/2}Y$.

#### Solution

$L^{-1}=S_1^{1/2}S_2^{-1}S_1^{1/2}$ et $S_1^{1/2}S_1^{-1}S_1^{1/2}=I_n$, donc

$$S_1^{1/2}\big(S_1^{-1}-S_2^{-1}\big)S_1^{1/2}=I_n-L^{-1},$$

positive par 11.d. Pour $X$ quelconque et $Y=S_1^{-1/2}X$ :

$$\begin{aligned}
{}^tX\big(S_1^{-1}-S_2^{-1}\big)X &= {}^tY\big(I_n-L^{-1}\big)Y\\
&\geqslant 0 .
\end{aligned}$$

**$S_1^{-1}-S_2^{-1}$ est positive** : l'inversion est décroissante pour l'ordre des matrices symétriques positives.

> [!JURY]
> Le rapport 2026 rappelle « qu'un argument inadapté (voire même l'absence d'argument) ainsi que le manque de précision lors d'un calcul rendent la réponse irrecevable ! » Dans cette partie, chaque égalité matricielle repose sur la symétrie ou l'inversibilité d'une racine carrée : les citer.

---

## Bilan

**Méthodes à retenir.**

- Loi d'une fonction d'une variable à densité : passer par la fonction de répartition, traiter tous les cas, vérifier continuité et caractère $\mathcal{C}^1$ par morceaux avant de dériver.
- Densité d'une somme de variables indépendantes : convolution, avec étude soigneuse du support de l'intégrande.
- Accélération de Richardson : une combinaison $\frac{x_{n+1}-qx_n}{1-q}$ supprime le terme d'erreur principal en $q^n$.
- Équivalent d'un quotient : passer par les équivalents du numérateur et du dénominateur.
- Formule des probabilités totales et de l'espérance totale avec un système complet fini ; sommes de Riemann ; comparaison série-intégrale pour la série harmonique.
- Algèbre bilinéaire : caractérisation spectrale de la positivité, racine carrée $P\Delta\,{}^tP$, polynômes de Lagrange pour écrire $B$ comme polynôme en $A$, co-diagonalisation de deux endomorphismes symétriques qui commutent.

**Prérequis à revoir.** Convolution, lois usuelles (uniforme discrète, géométrique), convergence en loi, développements limités, théorème spectral et endomorphismes induits.

**Questions transposables.** Ex1-Q4 (densité d'une somme), Ex2-Q5–6 (Richardson), Ex3-Q6 (encadrement de la série harmonique), Problème Q5–Q8 (racine carrée, unicité par co-diagonalisation), Q11 (décroissance de l'inverse).

> [!JURY]
> Le rapport 2026 conclut que « Une bonne réponse est une réponse construite rigoureusement et honnêtement. »
