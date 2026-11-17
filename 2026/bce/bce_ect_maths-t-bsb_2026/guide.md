# BCE ECT — Mathématiques T (conception BSB) 2026 · Corrigé guidé

*Corrigé rédigé par IA, non officiel. Signalez toute erreur.*

## Présentation du sujet

Épreuve de **4 heures**, sans document ni calculatrice (règle graduée autorisée). Trois exercices indépendants, **67 questions** courtes et très proches du cours.

| Exercice | Questions | Contenu | Notions du programme ECT |
|---|---|---|---|
| 1 — Les fonctions $f_n(x)=\frac{x^n}{n!}e^{1-x}$ | (1) à (13), 23 questions | Études de $f_1$ et $f_2$ (dérivées, inflexion, limites), Python (factorielle, tracé), intégrales impropres $I_0$, $I_1$, puis une densité et son espérance. | Dérivation, convexité, croissances comparées, intégration par parties, intégrales sur $[0,+\infty[$, densité, fonction de répartition, espérance |
| 2 — Deux suites imbriquées | (1) à (17), 23 questions | Termes généraux de $(u_n)$ et $(v_n)$ trouvés trois fois : suites auxiliaires géométriques, récurrence d'ordre 2, puissances d'une matrice diagonalisable. | Récurrence, suites géométriques, systèmes, équation du second degré, polynôme annulateur, diagonalisation $2\times2$ |
| 3 — Urne à jetons bicolores | (1) à (12), 21 questions | Couple $(B,R)$ pour $n=4$ : loi conjointe, marginales, covariance ; temps d'attente du premier et du second succès ; trois questions SQL. | Couples de variables finies, covariance, loi géométrique, loi binomiale, indépendance, SQL (`CREATE TABLE`, `WHERE`) |

**Ce qu'en dit le jury.** Le rapport 2026 indique 459 copies, une moyenne de 9,98, un écart type de 4,22 et une médiane de 9,85. Chaque question est notée sur 4 puis pondérée par un coefficient de 1 à 4. Les coefficients 4 portent sur (1) et (10) de l'exercice 2, (17)(a) et (17)(b), et sur (3)(b), (8), (9)(b) et (9)(d) de l'exercice 3. Une note de présentation et de rédaction sur 4, de coefficient 4, s'y ajoute.

Les histogrammes du rapport montrent les questions les moins réussies : (7) de l'exercice 1 (la factorielle en Python), (2), (9), (11) et (12) de l'exercice 2, (9)(a), (9)(c) et (9)(d) de l'exercice 3. La partie IV de l'exercice 2 (matrices) est la mieux réussie.

**Gestion du temps.** Le sujet est « volontairement long » d'après le rapport, mais chaque question est courte. Priorité : ne rien laisser d'élémentaire de côté (dérivées, limites, premiers termes, lois marginales), rédiger proprement les récurrences, et vérifier les calculs sur les premiers termes ($u_1=9$, $v_1=15$).

## Exercice 1 — Partie I : Quelques exemples

On étudie $f_1(x)=xe^{1-x}$ et $f_2(x)=\frac{x^2}2e^{1-x}$ : dérivées, signe, limites aux bornes.

### Question 1(a)

> [!INDICATION]
> Dérivée d'un produit ; la dérivée de $x\mapsto e^{1-x}$ est $x\mapsto-e^{1-x}$.

#### Solution

$$\begin{aligned}
f_1'(x)&=e^{1-x}-xe^{1-x}\\
&=(1-x)e^{1-x}.
\end{aligned}$$

> [!PIEGE]
> Oublier le signe moins de la dérivée de $e^{1-x}$ (dérivée d'une composée $e^{u}$ : $u'e^{u}$ avec $u'=-1$).

### Question 1(b)

> [!INDICATION]
> Une exponentielle est strictement positive : le signe de $f_1'$ est celui d'un facteur simple.

#### Solution

$f_1'(x)$ a le signe de $1-x$. **$f_1$ est strictement croissante sur $]-\infty,1]$ et strictement décroissante sur $[1,+\infty[$**, de maximum $f_1(1)=1$.

> [!JURY]
> Rapport 2026 : « Le calcul de dérivées est très peu réussi, peu d'élèves font le lien entre signe de la dérivée et variation de la fonction (le signe de la fonction donne les variations de la fonction...). » C'est bien le signe de $f_1'$, et non celui de $f_1$, qui donne les variations.

### Question 1(c)

> [!INDICATION]
> Dérivez $f_1'$ comme un produit, puis factorisez par $e^{1-x}$.

> [!INDICATION]
> Un point d'inflexion est un point où la dérivée seconde s'annule **en changeant de signe**.

#### Solution

$$\begin{aligned}
f_1''(x)&=-e^{1-x}-(1-x)e^{1-x}\\
&=(x-2)e^{1-x}.
\end{aligned}$$
$f_1''$ s'annule en changeant de signe en $2$ et seulement en $2$ : $f_1$ a exactement un point d'inflexion,
$$\boxed{\left(2,\ \frac2e\right)}$$

### Question 2(a)

> [!INDICATION]
> Que deviennent $1-x$, puis $e^{1-x}$, quand $x\to-\infty$ ?

#### Solution

$\lim_{x\to+\infty}e^x=+\infty$. Quand $x\to-\infty$, $e^{1-x}\to+\infty$ et $x\to-\infty$ : par produit, $\lim_{x\to-\infty}f_1(x)=-\infty$.

### Question 2(b)

> [!INDICATION]
> Propriété algébrique de l'exponentielle : $e^{a+b}=e^ae^b$.

#### Solution

$e^{1-x}=\frac e{e^x}$, donc $f_1(x)=e\,\frac x{e^x}$.

### Question 2(c)

> [!INDICATION]
> Quelle croissance comparée concerne $\frac x{e^x}$ en $+\infty$ ?

#### Solution

$\frac x{e^x}\to0$ en $+\infty$ par croissances comparées, donc $\lim_{x\to+\infty}f_1(x)=0$.

> [!METHODE]
> Forme indéterminée « $\infty\times0$ » avec une exponentielle : on réécrit pour faire apparaître un quotient $\frac{x^k}{e^x}$, puis on cite les croissances comparées.

### Question 3

> [!INDICATION]
> Rassemblez le signe de $f_1'$, la valeur du maximum et les deux limites.

#### Solution

| $x$ | $-\infty$ | | $1$ | | $+\infty$ |
|---|---|---|---|---|---|
| $f_1'(x)$ | | $+$ | $0$ | $-$ | |
| $f_1$ | $-\infty$ | ↗ | $1$ | ↘ | $0$ |

### Question 4(a)

> [!INDICATION]
> Même méthode qu'en 1(a), puis factorisez par $xe^{1-x}$.

#### Solution

$$\begin{aligned}
f_2'(x)&=xe^{1-x}-\frac{x^2}2e^{1-x}\\
&=\frac{x(2-x)}2e^{1-x}.
\end{aligned}$$

### Question 4(b)

> [!INDICATION]
> Le signe d'un trinôme du second degré se lit à partir de ses racines.

#### Solution

$f_2'(x)$ a le signe de $x(2-x)$ : négatif sur $]-\infty,0[$, positif sur $]0,2[$, négatif sur $]2,+\infty[$.

$f_2$ est décroissante sur $]-\infty,0]$, croissante sur $[0,2]$, décroissante sur $[2,+\infty[$, avec $f_2(0)=0$ et $f_2(2)=\frac2e$.

> [!PIEGE]
> Factoriser seulement par $e^{1-x}$ et étudier $x-\frac{x^2}2$ sans le factoriser : on se trompe facilement de signe. Mettre la dérivée sous forme de produit avant d'en étudier le signe.

### Question 5(a)

> [!INDICATION]
> Pas de forme indéterminée ici.

#### Solution

$\frac{x^2}2\to+\infty$ et $e^{1-x}\to+\infty$ quand $x\to-\infty$ : $\lim_{x\to-\infty}f_2(x)=+\infty$.

### Question 5(b)

> [!INDICATION]
> Réécrivez $f_2(x)$ comme en 2(b).

#### Solution

$f_2(x)=\frac e2\cdot\frac{x^2}{e^x}$ et $\frac{x^2}{e^x}\to0$ par croissances comparées : $\lim_{x\to+\infty}f_2(x)=0$.

### Question 6

> [!INDICATION]
> Trois intervalles de monotonie, deux extremums locaux.

#### Solution

| $x$ | $-\infty$ | | $0$ | | $2$ | | $+\infty$ |
|---|---|---|---|---|---|---|---|
| $f_2'(x)$ | | $-$ | $0$ | $+$ | $0$ | $-$ | |
| $f_2$ | $+\infty$ | ↘ | $0$ | ↗ | $\frac2e$ | ↘ | $0$ |

## Exercice 1 — Partie II : Quelques utilisations de l'informatique

### Question 7

> [!INDICATION]
> Variable d'accumulation d'un produit : quelle valeur initiale ne change pas un produit ?

#### Solution

```python
def fact(n):
    f = 1
    for k in range(1,n+1):
        f = f*k
    return f
```
Pour $n=0$, la boucle est vide et la fonction renvoie $1=0!$.

> [!PIEGE]
> Initialiser `f = 0` : le produit reste nul. D'après les histogrammes du rapport 2026, c'est la question la moins réussie de l'exercice 1.

### Question 8

> [!INDICATION]
> Une seule ligne `return` suffit, en traduisant $\frac{x^n}{n!}e^{1-x}$.

#### Solution

```python
def f(n,x):
    return x**n/fact(n)*np.exp(1-x)
```

### Question 9

> [!INDICATION]
> Calculez $f_1(-1)$ et $f_2(-1)$, et repérez les maximums trouvés en partie I.

> [!INDICATION]
> Un des trois graphiques ne correspond à aucune des deux fonctions : dites pourquoi.

#### Solution

- $f_1(-1)=-e^2\approx-7{,}4$, maximum $1$ en $1$, limite $0$ en $+\infty$ : c'est le **graphique 3**.
- $f_2(-1)=\frac{e^2}2\approx3{,}7$, minimum $0$ en $0$, maximum $\frac2e\approx0{,}74$ en $2$ : c'est le **graphique 1**.
- Le graphique 2 a son maximum vers $5$ et une valeur négative en $-1$ : ce n'est ni $f_1$ ni $f_2$ (c'est $f_5$).

> [!METHODE]
> Pour reconnaître une courbe : comparer des valeurs particulières (bornes, extremums) et les variations, plutôt que l'allure générale.

## Exercice 1 — Partie III : Intégrales définies à partir des $f_n$

### Question 10(a)

> [!INDICATION]
> Trouvez une primitive de $t\mapsto e^{1-t}$ (attention au signe).

#### Solution

$$I_0(A)=\Big[-e^{1-t}\Big]_0^A=e-e^{1-A}.$$

### Question 10(b)

> [!INDICATION]
> Faites tendre $A$ vers $+\infty$.

#### Solution

$e^{1-A}\to0$, donc $I_0(A)\to e$ : $I_0$ converge et $I_0=e$.

### Question 11(a)

> [!INDICATION]
> Dérivez $t$ et primitivez $e^{1-t}$.

#### Solution

Avec $u(t)=t$, $v(t)=-e^{1-t}$ (dérivables à dérivées continues sur $[0,A]$) :
$$\begin{aligned}
I_1(A)&=\Big[-te^{1-t}\Big]_0^A+\int_0^Ae^{1-t}\,dt\\
&=-Ae^{1-A}+I_0(A).
\end{aligned}$$

> [!METHODE]
> Intégration par parties : on dérive le facteur polynomial (son degré baisse) et on primitive l'exponentielle. Préciser $u$, $v$ et la continuité de $u$, $v$, $u'$, $v'$.

### Question 11(b)

> [!INDICATION]
> Remplacez $I_0(A)$.

#### Solution

$I_1(A)=-Ae^{1-A}-e^{1-A}+e$.

### Question 11(c)

> [!INDICATION]
> $Ae^{1-A}$ est une forme indéterminée : réécrivez-la comme en 2(b).

#### Solution

$Ae^{1-A}=e\frac A{e^A}\to0$ et $e^{1-A}\to0$, donc $I_1(A)\to e$ : $I_1$ converge et vaut $e$.

## Exercice 1 — Partie IV : Une variable à densité

### Question 12

> [!INDICATION]
> Trois conditions à vérifier : lesquelles ?

> [!INDICATION]
> L'intégrale de $g$ sur $[0,+\infty[$ s'exprime avec l'une des intégrales de la partie III.

#### Solution

- $g\geqslant0$ : nulle sur $]-\infty,0[$, et $\frac1ete^{1-t}\geqslant0$ pour $t\geqslant0$.
- $g$ est continue sur $\mathbb R$ sauf peut-être en $0$.
- $\int_{-\infty}^{+\infty}g(t)\,dt=0+\frac1eI_1=1$.

**$g$ est une densité de probabilité.**

### Question 13(a)

> [!INDICATION]
> Pour $x\geqslant0$, $G(x)$ s'écrit avec $I_1(x)$.

#### Solution

$G(x)=0$ si $x<0$ ; si $x\geqslant0$,
$$\begin{aligned}
G(x)&=\frac1eI_1(x)\\
&=1-(x+1)e^{-x}.
\end{aligned}$$

> [!PIEGE]
> Pour $x<0$, $G(x)$ n'est pas « non défini » : c'est $0$, car la densité est nulle à gauche de $0$.

### Question 13(b)

> [!INDICATION]
> Écrivez $tg(t)$ à l'aide de $f_2(t)$.

#### Solution

Pour $t\geqslant0$, $tg(t)=\frac1et^2e^{1-t}=\frac2ef_2(t)\geqslant0$, et $tg(t)=0$ pour $t<0$. L'intégrale converge car $I_2$ converge, et
$$\boxed{E(X)=\frac2eI_2=2}$$

## Exercice 2 — Partie I : Variations des suites

Le but de l'exercice est d'obtenir trois fois les mêmes formules pour $u_n$ et $v_n$ : c'est aussi un moyen de vérifier ses calculs.

### Question 1

> [!INDICATION]
> Récurrence : initialisation, puis hérédité en utilisant les relations de définition.

#### Solution

$u_0=1$ et $v_0=2$ sont des entiers strictement positifs.

Si $u_n$ et $v_n$ le sont, alors $u_{n+1}=5u_n+2v_n$ et $v_{n+1}=3u_n+6v_n$ sont des entiers (sommes de produits d'entiers) strictement positifs (sommes de termes strictement positifs).

Par récurrence, $\mathcal P_n$ est vraie pour tout $n$.

> [!JURY]
> Rapport 2026 : « Même les questions ultra classiques, notamment les récurrences, sont parcellaires, bancales, voire absentes de nombreuses copies. » Cette question a un coefficient 4 : énoncer la propriété, l'initialisation, l'hérédité et la conclusion.

### Question 2

> [!INDICATION]
> Étudiez le signe de $u_{n+1}-u_n$ et de $v_{n+1}-v_n$.

#### Solution

$$\begin{aligned}
u_{n+1}-u_n&=4u_n+2v_n>0,\\
v_{n+1}-v_n&=3u_n+5v_n>0.
\end{aligned}$$
Les deux suites sont strictement croissantes.

> [!PIEGE]
> « En déduire » : la positivité de la question 1 est l'argument clé. Conclure seulement « car les coefficients sont positifs » ne suffit pas.

## Exercice 2 — Partie II : Suites auxiliaires

### Question 3

> [!INDICATION]
> Remplacez $u_0$ et $v_0$.

#### Solution

$x_0=3$ et $y_0=-1$.

> [!JURY]
> Rapport 2026 : « Même les calculs très basiques ($x_0$, $y_0$, puis $u_0$ et $u_1$) posent problème à de nombreux candidats. »

### Question 4

> [!INDICATION]
> Exprimez $x_{n+1}$ en fonction de $u_n$ et $v_n$, puis reconnaissez $x_n$.

#### Solution

$$\begin{aligned}
x_{n+1}&=8u_n+8v_n\\
&=8x_n,
\end{aligned}$$
donc $x_n=3\cdot8^n$.

### Question 5

> [!INDICATION]
> Même méthode avec $y_{n+1}=3u_{n+1}-2v_{n+1}$.

#### Solution

$$\begin{aligned}
y_{n+1}&=15u_n+6v_n-6u_n-12v_n\\
&=9u_n-6v_n\\
&=3y_n,
\end{aligned}$$
donc $y_n=-3^n$.

### Question 6

> [!INDICATION]
> Éliminez $v_n$ par une combinaison des deux équations.

#### Solution

$2\times$(première) $+$ (seconde) : $5u_n=2x_n+y_n$. Puis $v_n=x_n-u_n$ :
$$\begin{aligned}u_n&=\frac{2x_n+y_n}5\\v_n&=\frac{3x_n-y_n}5\end{aligned}.$$

### Question 7

> [!INDICATION]
> Remplacez $x_n$ et $y_n$ par leurs expressions.

#### Solution

$$\begin{aligned}
u_n&=\frac{6\cdot8^n-3^n}5=-\frac15\,3^n+\frac65\,8^n,\\
v_n&=\frac{9\cdot8^n+3^n}5=\frac15\,3^n+\frac95\,8^n.
\end{aligned}$$
Vérification : $u_0=1$ et $v_0=2$.

## Exercice 2 — Partie III : Récurrence d'ordre 2

### Question 8

> [!INDICATION]
> Appliquez les relations de récurrence pour $n=0$.

#### Solution

$u_1=9$ et $v_1=15$.

### Question 9

> [!INDICATION]
> Écrivez $u_{n+2}$ avec la définition, développez $v_{n+1}$, puis éliminez $v_n$ grâce à $(\ast)$.

#### Solution

$$\begin{aligned}
u_{n+2}&=5u_{n+1}+2(3u_n+6v_n)\\
&=5u_{n+1}+6u_n+6(u_{n+1}-5u_n)\\
&=11u_{n+1}-24u_n.
\end{aligned}$$

> [!METHODE]
> Pour passer d'un système de deux suites à une récurrence d'ordre 2 sur une seule : exprimer $v_n$ en fonction de $u_n$ et $u_{n+1}$, puis substituer dans l'expression de $u_{n+2}$.

### Question 10

> [!INDICATION]
> Discriminant.

#### Solution

$\Delta=121-96=25$, d'où les racines $x_1=3$ et $x_2=8$.

> [!JURY]
> Rapport 2026 : « Toujours sur des problèmes calculatoires, la moitié des candidats n'arrivent pas à calculer correctement les solutions d'une équation du second degré. » Vérifier en remplaçant : $9-33+24=0$ et $64-88+24=0$.

### Question 11

> [!INDICATION]
> Écrivez la formule pour $n=0$ et $n=1$ : système de deux équations à deux inconnues.

#### Solution

$a+b=1$ et $3a+8b=9$, d'où $5b=6$, puis
$$\begin{aligned}a&=-\frac15\\b&=\frac65\end{aligned}.$$

### Question 12

> [!INDICATION]
> Pour $v_n$, calculez $u_{n+1}-5u_n$ en regroupant les termes en $3^n$ et en $8^n$.

#### Solution

$u_n=-\frac15\,3^n+\frac65\,8^n$, et
$$\begin{aligned}
v_n&=\frac12\left(-\frac35\,3^n+\frac{48}5\,8^n+3^n-6\cdot8^n\right)\\
&=\frac15\,3^n+\frac95\,8^n.
\end{aligned}$$

> [!PIEGE]
> $u_{n+1}$ fait apparaître $3^{n+1}=3\cdot3^n$ et $8^{n+1}=8\cdot8^n$ : factoriser par $3^n$ et $8^n$ avant de simplifier.

## Exercice 2 — Partie IV : Puissances d'une matrice

### Question 13(a)

> [!INDICATION]
> Calculez le produit $MX_n$.

#### Solution

$MX_n=\begin{pmatrix}5u_n+2v_n\\3u_n+6v_n\end{pmatrix}=X_{n+1}$.

### Question 13(b)

> [!INDICATION]
> Récurrence immédiate à partir de 13(a).

#### Solution

$X_0=M^0X_0$, et si $X_n=M^nX_0$, alors $X_{n+1}=MX_n=M^{n+1}X_0$.

### Question 14(a)

> [!INDICATION]
> Produit ligne par colonne.

#### Solution

$$M^2=\begin{pmatrix}31&22\\33&42\end{pmatrix},\qquad M^2-11M+24I_2=\begin{pmatrix}0&0\\0&0\end{pmatrix}.$$

### Question 14(b)

> [!INDICATION]
> Relisez le résultat précédent.

#### Solution

$X^2-11X+24$ est un polynôme annulateur de $M$.

### Question 14(c)

> [!INDICATION]
> Lien entre valeurs propres et racines d'un polynôme annulateur, et question 10.

#### Solution

Les valeurs propres possibles de $M$ sont les racines de $X^2-11X+24$ : **$3$ et $8$**.

### Question 15

> [!INDICATION]
> Calculez $M$ fois chaque vecteur et comparez au vecteur.

#### Solution

$$M\begin{pmatrix}1\\-1\end{pmatrix}=3\begin{pmatrix}1\\-1\end{pmatrix},\qquad M\begin{pmatrix}2\\3\end{pmatrix}=8\begin{pmatrix}2\\3\end{pmatrix}.$$
Ces vecteurs non nuls sont propres, pour les valeurs propres $3$ et $8$.

### Question 16(a)

> [!INDICATION]
> Critère d'inversibilité d'une matrice d'ordre 2 et formule de l'inverse.

#### Solution

$ad-bc=3+2=5\neq0$, donc $P$ est inversible et
$$P^{-1}=\frac15\begin{pmatrix}3&-2\\1&1\end{pmatrix}.$$

### Question 16(b)

> [!INDICATION]
> Calculez $MP$ et $PD$ ; pour conclure, revenez à la définition d'une matrice diagonalisable.

#### Solution

$MP=PD=\begin{pmatrix}3&16\\-3&24\end{pmatrix}$, donc $D=P^{-1}MP$ avec $D$ diagonale et $P$ inversible : $M$ est diagonalisable.

### Question 16(c)

> [!INDICATION]
> Hérédité : $M^{n+1}=M^nM$, et $P^{-1}P=I_2$ au milieu.

#### Solution

$PD^0P^{-1}=I_2=M^0$. Si $M^n=PD^nP^{-1}$, alors
$$\begin{aligned}
M^{n+1}&=PD^nP^{-1}PDP^{-1}\\
&=PD^{n+1}P^{-1}.
\end{aligned}$$

### Question 17(a)

> [!INDICATION]
> Puissance d'une matrice diagonale, puis deux produits matriciels.

#### Solution

$D^n=\begin{pmatrix}3^n&0\\0&8^n\end{pmatrix}$ et
$$M^n=\frac15\begin{pmatrix}3^{n+1}+2\cdot8^n&-2\cdot3^n+2\cdot8^n\\-3^{n+1}+3\cdot8^n&2\cdot3^n+3\cdot8^n\end{pmatrix}.$$
Contrôle : pour $n=0$, on retrouve $I_2$ ; pour $n=1$, on retrouve $M$.

### Question 17(b)

> [!INDICATION]
> $X_n=M^nX_0$ avec $X_0=\begin{pmatrix}1\\2\end{pmatrix}$.

#### Solution

$$\begin{aligned}
u_n&=\frac15\left(3^{n+1}+2\cdot8^n-4\cdot3^n+4\cdot8^n\right)=-\frac15\,3^n+\frac65\,8^n,\\
v_n&=\frac15\left(-3^{n+1}+3\cdot8^n+4\cdot3^n+6\cdot8^n\right)=\frac15\,3^n+\frac95\,8^n.
\end{aligned}$$

> [!JURY]
> Rapport 2026 : « À part la partie 4 de l'exercice 2 (partie sur les matrices), les copies proposées sont très en deçà du niveau espéré en fin de deuxième année d'ECT. »

## Exercice 3 — Partie I : Le couple $(B,R)$ pour $n=4$

### Question 1

> [!INDICATION]
> Listez, pour chaque numéro bleu $k$, les jetons correspondants.

#### Solution

Pour $k\in\{1,2,3,4\}$, les jetons de numéro bleu $k$ sont $(k,1),\dots,(k,k)$ : $1+2+3+4=10$ jetons, ceux de la liste.

### Question 2(a)

> [!INDICATION]
> Lisez les deux coordonnées de la liste.

#### Solution

$B(\Omega)=R(\Omega)=\{1,2,3,4\}$.

### Question 2(b)

> [!INDICATION]
> Les jetons sont équiprobables : comptez les jetons favorables.

#### Solution

Seul $(1,1)$ réalise $(B=1)\cap(R=1)$ : probabilité $\frac1{10}$. Aucun jeton n'est $(1,2)$ : $P((B=1)\cap(R=2))=0$.

### Question 2(c)

> [!INDICATION]
> Le jeton $(i,j)$ existe si et seulement si $j\leqslant i$.

#### Solution

$P((B=i)\cap(R=j))=\frac1{10}$ si $j\leqslant i$, $0$ sinon :

| $j$ \\ $i$ | $1$ | $2$ | $3$ | $4$ |
|---|---|---|---|---|
| $1$ | $\frac1{10}$ | $\frac1{10}$ | $\frac1{10}$ | $\frac1{10}$ |
| $2$ | $0$ | $\frac1{10}$ | $\frac1{10}$ | $\frac1{10}$ |
| $3$ | $0$ | $0$ | $\frac1{10}$ | $\frac1{10}$ |
| $4$ | $0$ | $0$ | $0$ | $\frac1{10}$ |

### Question 3(a)

> [!INDICATION]
> Loi marginale : on somme sur l'autre variable.

#### Solution

$P(B=i)=\frac i{10}$ pour $i=1,2,3,4$.

### Question 3(b)

> [!INDICATION]
> Calculez $E(B)$ et $E(B^2)$, puis Koenig-Huygens.

#### Solution

$E(B)=\frac{1+4+9+16}{10}=3$, $E(B^2)=\frac{1+8+27+64}{10}=10$, donc $V(B)=10-9=1$.

### Question 4(a)

> [!INDICATION]
> Même méthode, en sommant cette fois sur $i$.

#### Solution

$P(R=j)=\frac{5-j}{10}$ : $\frac4{10},\frac3{10},\frac2{10},\frac1{10}$ pour $j=1,2,3,4$.

### Question 4(b)

> [!INDICATION]
> Comme en 3(b).

#### Solution

$E(R)=\frac{4+6+6+4}{10}=2$, $E(R^2)=\frac{4+12+18+16}{10}=5$, donc $V(R)=1$.

### Question 5(a)

> [!INDICATION]
> $E(BR)=\sum_{i,j}ij\,P((B=i)\cap(R=j))$ : seules les cases non nulles du tableau comptent.

#### Solution

$$\begin{aligned}
E(BR)&=\frac1{10}\sum_{i=1}^4i\sum_{j=1}^ij\\
&=\frac{1+6+18+40}{10}=\frac{13}2.
\end{aligned}$$

### Question 5(b)

> [!INDICATION]
> Formule de Koenig-Huygens pour la covariance.

#### Solution

$\mathrm{Cov}(B,R)=E(BR)-E(B)E(R)=\frac{13}2-6=\frac12$.

### Question 5(c)

> [!INDICATION]
> Que vaut la covariance de deux variables indépendantes ?

#### Solution

Des variables indépendantes ont une covariance nulle ; ici $\mathrm{Cov}(B,R)=\frac12\neq0$, donc $B$ et $R$ ne sont pas indépendantes.

> [!PIEGE]
> La réciproque est fausse : une covariance nulle ne prouverait pas l'indépendance. Ici, c'est la contraposée qui sert.

### Question 6

> [!INDICATION]
> Linéarité de l'espérance.

#### Solution

$E(G)=E(B)-E(R)=1$.

## Exercice 3 — Partie II : Temps d'attente

### Question 7

> [!INDICATION]
> Combien de jetons portent le numéro bleu $1$ ?

#### Solution

Le seul jeton de numéro bleu $1$ est $(1,1)$, d'où $S_k=(B_k=1)=(B_k=1)\cap(R_k=1)$. Les tirages se font avec remise, l'urne est la même à chaque tirage : $P(S_k)=\frac1{10}$.

### Question 8

> [!INDICATION]
> Reconnaissez le rang du premier succès dans une suite d'épreuves de Bernoulli indépendantes.

#### Solution

$T_1\hookrightarrow\mathcal G\left(\frac1{10}\right)$, donc $E(T_1)=10$ et $V(T_1)=\frac{0{,}9}{0{,}01}=90$.

> [!METHODE]
> Justifier une loi géométrique : épreuves de Bernoulli **indépendantes** (ici grâce à la remise), de **même** probabilité de succès, variable égale au **rang du premier succès**.

### Question 9(a)

> [!INDICATION]
> Quel est le plus petit nombre de tirages possible ?

#### Solution

$T_2(\Omega)=\{2,3,4,\dots\}$.

### Question 9(b)

> [!INDICATION]
> Nombre de succès dans $m$ épreuves de Bernoulli indépendantes de même paramètre.

#### Solution

$X_m\hookrightarrow\mathcal B\left(m,\frac1{10}\right)$.

### Question 9(c)

> [!INDICATION]
> Que doit-il se passer au $k$-ième tirage, et avant ?

#### Solution

Le second succès a lieu au tirage $k$ si et seulement si le tirage $k$ est un succès et qu'il y a eu exactement un succès parmi les $k-1$ premiers : $(T_2=k)=(X_{k-1}=1)\cap S_k$.

### Question 9(d)

> [!INDICATION]
> Les deux événements de 9(c) portent sur des tirages différents.

> [!INDICATION]
> $P(X_{k-1}=1)$ se lit sur la loi binomiale de 9(b).

#### Solution

Par indépendance des tirages, pour $k\geqslant2$,
$$\begin{aligned}
P(T_2=k)&=(k-1)\frac1{10}\left(\frac9{10}\right)^{k-2}\cdot\frac1{10}\\
&=\frac{k-1}{100}\left(\frac9{10}\right)^{k-2}.
\end{aligned}$$

> [!PIEGE]
> Oublier le coefficient binomial $\binom{k-1}1=k-1$ : le premier succès peut avoir lieu à n'importe lequel des $k-1$ premiers tirages. D'après les histogrammes du rapport 2026, les questions 9(a), 9(c) et 9(d) sont les moins réussies de l'exercice.

## Exercice 3 — Partie III : Base de données

### Question 10

> [!INDICATION]
> Une clé primaire doit identifier chaque ligne : un joueur joue-t-il une seule partie ?

#### Solution

Un joueur peut jouer plusieurs parties : son nom apparaît sur plusieurs lignes. `IdPartie`, identifiant unique, peut servir de clé primaire.

### Question 11

> [!INDICATION]
> Donnez chaque attribut avec son type et désignez la clé primaire.

#### Solution

```sql
CREATE TABLE Partie (
    IdPartie INT PRIMARY KEY,
    NomJoueur TEXT,
    B INT,
    R INT
);
```
L'énoncé nomme la table `Parties` plus haut et `Partie` dans la question ; on suit la question.

### Question 12

> [!INDICATION]
> Une sélection avec une condition sur l'attribut du numéro bleu.

#### Solution

```sql
SELECT DISTINCT NomJoueur FROM Partie WHERE B = 1;
```

## Bilan

**Méthodes à retenir.**

- Étude de fonction : dérivée sous forme factorisée, signe de la dérivée (pas de la fonction), limites par croissances comparées après réécriture.
- Intégrales sur $[0,+\infty[$ : calcul sur $[0,A]$ (primitive ou intégration par parties), puis limite quand $A\to+\infty$.
- Densité : positivité, continuité sauf en un nombre fini de points, intégrale égale à $1$ ; espérance par convergence de $\int tg(t)\,dt$.
- Suites imbriquées : suites auxiliaires géométriques, récurrence d'ordre 2 et équation caractéristique, ou puissances d'une matrice diagonalisable ; les trois méthodes doivent donner le même résultat.
- Couples finis : loi conjointe en tableau, marginales par sommation, covariance par Koenig-Huygens, non-indépendance par la contraposée.
- Temps d'attente : premier succès (loi géométrique), $r$-ième succès par décomposition $(X_{k-1}=r-1)\cap S_k$.

**Prérequis à revoir.** Dérivée de $e^{u}$, croissances comparées, équation du second degré, inverse d'une matrice $2\times2$, lois géométrique et binomiale, syntaxe `CREATE TABLE` avec `PRIMARY KEY`.

**Questions transposables.** La recherche du terme général de deux suites couplées par trois méthodes, et la loi du temps d'attente du second succès, reviennent souvent dans les sujets de la voie technologique.
