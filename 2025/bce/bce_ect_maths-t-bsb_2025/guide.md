# BCE ECT — Mathématiques T (conception BSB) 2025 · Corrigé guidé

*Corrigé rédigé par IA, non officiel. Signalez toute erreur.*

## Présentation du sujet

Épreuve de **4 heures**, sans document ni calculatrice (règle graduée autorisée). **Quatre exercices**, **52 questions**, qui parcourent les deux années du programme de la voie technologique.

| Exercice | Questions | Contenu | Notions du programme ECT |
|---|---|---|---|
| 1 — Une matrice non diagonalisable | (1) à (15) | $(A-I)^2=0$ donne $A^{-1}$, $A^n=nA-(n-1)I$, une seule valeur propre, non-diagonalisabilité par l'absurde ; puis la suite $X_{n+1}=AX_n+B$ par un point fixe $F$. | Calcul matriciel, inverse, récurrence, polynôme annulateur, valeurs et vecteurs propres, diagonalisabilité |
| 2 — Une famille de polynômes | (1) à (15) | Étude d'une cubique et dichotomie en Python ; factorisation de $g=P_2$ ; points communs des courbes $\mathscr C_m$, aire entre deux courbes, racine $\alpha_m\to1$. | Limites, dérivée, tableau de variations, théorème de la bijection, Python (`while`), factorisation, intégrales, aires |
| 3 — Trois jetons | (1) à (13) | Nombre $X$ de faces bleues, nombre $Y$ de couleurs, produit $Z$ des numéros : lois, espérances, variance, loi conjointe, covariance. | Loi binomiale, loi d'une variable finie, couple, covariance, indépendance |
| 4 — Une densité | (1) à (9) | Étude de $G(x)=(x+1)e^{-x}$, densité $f(t)=te^{-t}$ sur $[0,+\infty[$, fonction de répartition, espérance par intégration par parties. | Croissances comparées, point d'inflexion, densité, intégrales sur $[0,+\infty[$, IPP, espérance |

**Ce qu'en dit le jury.** Le rapport 2025 indique une moyenne de 9,65/20, un écart type de 3,87, une médiane de 9,95 et un troisième quartile de 11,8 (534 copies). Chaque question est notée sur 4 avec un coefficient 2, 3 ou 4 ; les totaux sont 180 (exercice 1), 156 (exercice 2), 152 (exercice 3), 108 (exercice 4) et 16 pour la présentation, sur 612. Les questions de coefficient 4 sont : (1), (3), (5), (12), (14) de l'exercice 1 ; (1), (7), (8) de l'exercice 2 ; (1), (8) de l'exercice 3 ; (1), (5) de l'exercice 4.

**Erreur d'énoncé.** À la question (3) de l'exercice 2, l'énoncé donne $f\left(-\frac13\right)=-\frac{11}6$ ; la valeur exacte est $-\frac{50}{27}$, comme le précise le rapport 2025. C'est sans conséquence pour la suite.

**Gestion du temps.** Les quatre exercices ont des poids voisins et commencent tous par des questions faciles à fort coefficient : les aborder tous. Les fins d'exercice ((10) et (15) de l'exercice 1, (14)–(15) de l'exercice 2, (10) à (13) de l'exercice 3, (8)–(9) de l'exercice 4) sont plus discriminantes.

## Exercice 1 — Première partie : $A$ et ses puissances

Une seule relation, $(A-I)^2=0$, donne presque tout : l'inverse, les puissances, le polynôme annulateur, et la non-diagonalisabilité.

### Question (1)

> [!INDICATION]
> Calcul matriciel direct ; observez la forme des lignes et des colonnes de $A-I$.

#### Solution

$$A-I=\begin{pmatrix}-1&-1&0\\1&1&0\\4&4&0\end{pmatrix},\qquad(A-I)^2=\begin{pmatrix}0&0&0\\0&0&0\\0&0&0\end{pmatrix}.$$

### Question (2)

> [!INDICATION]
> Développez $(A-I)^2$ (les matrices $A$ et $I$ commutent), puis isolez $I$.

#### Solution

$A^2-2A+I=0$, donc $A(2I-A)=I$ : $A$ est inversible et $A^{-1}=2I-A$, soit $\alpha=-1$ et $\beta=2$.

> [!METHODE]
> Si $A\,B=I$ pour une matrice carrée $B$, alors $A$ est inversible d'inverse $B$ : il suffit de faire apparaître $I$ seul d'un côté et de factoriser par $A$ de l'autre.

### Question (3)

> [!INDICATION]
> Calculez $2I-A$.

#### Solution

$$A^{-1}=\begin{pmatrix}2&1&0\\-1&0&0\\-4&-4&1\end{pmatrix}.$$

On vérifie que $AA^{-1}=I$.

### Question (4)

> [!INDICATION]
> Relisez le développement de la question (2).

#### Solution

$A^2-2A+I=0$, donc $A^2=2A-I$.

### Question (5)

> [!INDICATION]
> Hérédité : $A^{n+1}=A\cdot A^n$, puis remplacez $A^2$ grâce à la question (4).

#### Solution

Pour $n=0$ : $0\cdot A+I=I=A^0$. Si $A^n=nA-(n-1)I$, alors
$$\begin{aligned}
A^{n+1}&=nA^2-(n-1)A\\
&=n(2A-I)-(n-1)A\\
&=(n+1)A-nI.
\end{aligned}$$
Par récurrence, $A^n=nA-(n-1)I$ pour tout $n\in\mathbb N$.

> [!JURY]
> Rapport 2025 : la candidate virtuelle à 13,3/20 réussit la récurrence de la question (5) partiellement, ce qui « signifie initialisation correcte et hypothèse de récurrence bien rédigée ». Ces deux étapes rapportent déjà des points.

### Question (6)

> [!INDICATION]
> Traduisez la question (4) en polynôme.

#### Solution

$X^2-2X+1=(X-1)^2$ est un polynôme annulateur de $A$.

### Question (7)

> [!INDICATION]
> Lien entre valeurs propres et racines d'un polynôme annulateur.

#### Solution

Les valeurs propres de $A$ sont racines de $(X-1)^2$ : seule $1$ est possible, donc $A$ a au plus une valeur propre.

### Question (8)

> [!INDICATION]
> Calculez le produit, comparez au vecteur, et n'oubliez pas une condition de la définition d'un vecteur propre.

#### Solution

$A\begin{pmatrix}0\\0\\1\end{pmatrix}=\begin{pmatrix}0\\0\\1\end{pmatrix}$ et ce vecteur est **non nul** : c'est un vecteur propre associé à la valeur propre $1$.

> [!JURY]
> Rapport 2025 : beaucoup de copies ont fait le bon produit, mais « une proportion importante des copies n’a pas mentionné la valeur propre associée (alors que c’est évidemment un attendu ici) et presque aucune n’a remarqué que le vecteur était non nul. »

### Question (9)

> [!INDICATION]
> Quelle valeur propre doit être associée à ce vecteur ? Écrivez le système correspondant.

#### Solution

On résout $A\begin{pmatrix}a\\b\\0\end{pmatrix}=\begin{pmatrix}a\\b\\0\end{pmatrix}$ : $-b=a$, $a+2b=b$, $4a+4b=0$, soit $a=-b$.

Par exemple $a=1$, $b=-1$ : le vecteur $\begin{pmatrix}1\\-1\\0\end{pmatrix}$ est non nul et propre pour la valeur propre $1$.

> [!PIEGE]
> Rapport 2025 : à cette question, « beaucoup de copies ont donné… le vecteur nul ! » Un vecteur propre est **non nul** par définition.

### Question (10)

> [!INDICATION]
> Si $A$ était diagonalisable, que vaudrait la matrice diagonale $D$ ?

> [!INDICATION]
> Déduisez-en $A$, puis comparez avec la vraie matrice $A$.

#### Solution

Si $A=PDP^{-1}$ avec $D$ diagonale, les coefficients de $D$ sont des valeurs propres, donc tous égaux à $1$ : $D=I$ et $A=PIP^{-1}=I$, ce qui est faux.

$A$ n'est pas diagonalisable.

> [!METHODE]
> Une matrice qui n'a qu'une valeur propre $\lambda$ et qui est diagonalisable vaut $\lambda I$. C'est l'argument standard pour prouver qu'une matrice n'est pas diagonalisable.

## Exercice 1 — Deuxième partie : étude de suites

### Question (11)

> [!INDICATION]
> Calculez $AX_0$ puis ajoutez $B$.

#### Solution

$AX_0=\begin{pmatrix}-2\\5\\15\end{pmatrix}$, donc $u_1=-3$, $v_1=6$, $w_1=19$.

### Question (12)

> [!INDICATION]
> Écrivez $AF+B$ en fonction de $\omega$ et identifiez coordonnée par coordonnée.

#### Solution

$AF+B=\begin{pmatrix}0\\\omega-1\\4\omega+3\end{pmatrix}$ ; l'égalité avec $F$ impose $\omega=0$ (les trois équations sont compatibles).

### Question (13)

> [!INDICATION]
> Soustrayez membre à membre $F=AF+B$ et $X_{n+1}=AX_n+B$.

#### Solution

$$\begin{aligned}
X_{n+1}-F&=AX_n+B-(AF+B)\\
&=A(X_n-F).
\end{aligned}$$

> [!METHODE]
> C'est la version matricielle de la méthode des suites arithmético-géométriques : on soustrait un « point fixe » $F$ pour se ramener à une relation $Y_{n+1}=AY_n$.

### Question (14)

> [!INDICATION]
> Récurrence identique à celle qui donne $X_n=A^nX_0$.

#### Solution

$X_0-F=A^0(X_0-F)$, et si $X_n-F=A^n(X_0-F)$, la question (13) donne $X_{n+1}-F=A^{n+1}(X_0-F)$.

### Question (15)

> [!INDICATION]
> Remplacez $A^n$ par la formule de la question (5).

#### Solution

$X_0-F=\begin{pmatrix}1\\3\\0\end{pmatrix}$ et $A(X_0-F)=\begin{pmatrix}-3\\7\\16\end{pmatrix}$, d'où
$$\begin{aligned}
X_n&=F+n\,A(X_0-F)-(n-1)(X_0-F),\\
u_n&=1-4n,\quad v_n=2+4n,\quad w_n=3+16n.
\end{aligned}$$
Contrôle : on retrouve $X_0$ et $X_1$.

## Exercice 2 — Première partie : le cas $m=-\frac12$

### Question (1)

> [!INDICATION]
> Remplacez $x$ par $2$ et réduisez au même dénominateur.

#### Solution

$f(2)=-8+10+4-\frac32=\frac92$.

### Question (2)

> [!INDICATION]
> Factorisez par le terme de plus haut degré.

#### Solution

$f(x)=x^3\left(-1+\frac5{2x}+\frac2{x^2}-\frac3{2x^3}\right)$ : la parenthèse tend vers $-1$, donc $f\to+\infty$ en $-\infty$ et $f\to-\infty$ en $+\infty$.

> [!PIEGE]
> Écrire « $-\infty+\infty$ » et conclure au hasard : c'est une forme indéterminée, il faut factoriser par $x^3$.

### Question (3)

> [!INDICATION]
> Dérivez, puis factorisez $f'$ à l'aide de ses racines.

#### Solution

$f'(x)=-3x^2+5x+2=-(3x+1)(x-2)$ : $f$ décroît sur $\left]-\infty,-\frac13\right]$, croît sur $\left[-\frac13,2\right]$, décroît sur $[2,+\infty[$.

$f\left(-\frac13\right)=-\frac{50}{27}$ (et non $-\frac{11}6$ comme imprimé) et $f(2)=\frac92$.

| $x$ | −∞ | | $-\frac13$ | | 2 | | +∞ |
|---|---|---|---|---|---|---|---|
| $f$ | +∞ | ↘ | $-\frac{50}{27}$ | ↗ | $\frac92$ | ↘ | −∞ |

> [!JURY]
> Rapport 2025 : « Une erreur malencontreuse mais sans conséquence s’est glissée à la question (3) de l’exercice 2 ». Le rapport ajoute que « le simple fait de penser à dériver f pour trouver ses variations apportait des points ».

### Question (4)

> [!INDICATION]
> Sur $[0,2]$, $f$ est continue et strictement monotone : quel théorème donne l'unicité de la racine ?

#### Solution

$f(0)=-\frac32<0<f(2)=\frac92$, et $f$ est continue strictement croissante sur $[0,2]$ : par le théorème de la bijection, $f$ s'annule une seule fois sur $[0,2]$ (en $\frac12$).

### Question (5)

> [!INDICATION]
> Pourquoi `Racine` a-t-elle besoin d'un argument `f` ?

#### Solution

Les lignes 1 et 2 définissent la fonction Python `f`, qui calcule $f(x)$ ; elle est passée à `Racine`, qui doit évaluer $f$ aux points testés.

### Question (6)

> [!INDICATION]
> Déroulez la boucle à la main : à chaque tour, calculez `m`, puis $f(m)$ et le signe de $f(a)f(m)$.

> [!INDICATION]
> Pensez au test `f(m)==0` : la racine exacte peut être atteinte.

#### Solution

Premier tour : `m = 1.0` (affiché), $f(1)=2$, $f(0)f(1)<0$, donc $b=1$. Deuxième tour : `m = 0.5` (affiché), $f(0{,}5)=0$, la fonction renvoie `0.5`. Affichages : `1.0` et `0.5` ; valeur renvoyée : `0.5`.

> [!PIEGE]
> Continuer la boucle jusqu'à la précision $0{,}001$ : le `return` de la ligne 8 l'interrompt dès que $f(m)=0$, ce qui arrive ici car $f\left(\frac12\right)=0$ est calculé exactement.

## Exercice 2 — Deuxième partie : le cas $m=2$

### Question (7)

> [!INDICATION]
> Calcul direct.

#### Solution

$g(-1)=-4+3+1=0$.

### Question (8)

> [!INDICATION]
> Développez $(x+1)(ax^2+bx+c)$ et identifiez les coefficients.

#### Solution

$a=4$, $a+b=0$, $b+c=-3$, $c=1$ : $\varphi(x)=4x^2-4x+1=(2x-1)^2$.

### Question (9)

> [!INDICATION]
> Un produit est nul si et seulement si l'un des facteurs l'est.

#### Solution

$g(x)=(x+1)(2x-1)^2$ : racines $-1$ et $\frac12$ (double).

## Exercice 2 — Troisième partie : points communs

### Question (10)

> [!INDICATION]
> Primitive d'un polynôme, puis évaluation aux bornes.

#### Solution

$$\begin{aligned}
\int_{-1}^{1/2}g(x)\,dx &= \Big[x^4-\frac32x^2+x\Big]_{-1}^{1/2}\\
&= \frac3{16}+\frac32\\
&= \frac{27}{16}.
\end{aligned}$$

### Question (11)

> [!INDICATION]
> Calculez $P_m(-1)$ et $P_m\left(\frac12\right)$ pour $m$ quelconque.

#### Solution

$P_m(-1)=-2m+2-m-1+2m+m-1=0$ et $P_m\left(\frac12\right)=\frac m4+\frac{2-m}4+\frac{1-2m}2+m-1=0$ : $A$ et $B$ sont sur toutes les courbes.

### Question (12)

> [!INDICATION]
> Calculez $h$ et cherchez des racines évidentes (les abscisses de $A$ et $B$, par exemple).

#### Solution

$h(x)=2x^3-x^2-2x+1=(2x-1)(x-1)(x+1)$ :

Le signe de $h$ alterne entre ses racines :

- $h<0$ sur $]-\infty,-1[$ ;
- $h>0$ sur $\left]-1,\frac12\right[$ ;
- $h<0$ sur $\left]\frac12,1\right[$ ;
- $h>0$ sur $]1,+\infty[$.

### Question (13)

> [!INDICATION]
> L'aire entre deux courbes est l'intégrale de « la plus haute moins la plus basse » : la question (12) dit laquelle.

#### Solution

$h\geqslant0$ sur $\left[-1,\frac12\right]$, donc l'aire vaut
$$\int_{-1}^{1/2}h(x)\,dx=\Big[\frac{x^4}2-\frac{x^3}3-x^2+x\Big]_{-1}^{1/2}=\frac{45}{32}\ \text{unités d'aire.}$$

> [!PIEGE]
> Intégrer $P_0-P_1$ et trouver une aire négative : une aire est positive, le signe de $h$ indique l'ordre des courbes.

### Question (14)

> [!INDICATION]
> Écrivez $P_m(x)$ sous la forme $P_0(x)+m\times(\dots)$ : à quelle condition sur $x$ la valeur ne dépend-elle pas de $m$ ?

#### Solution

$P_m(x)=P_0(x)+m\,h(x)$ : les abscisses communes sont les racines de $h$, soit $-1$, $\frac12$ et $1$.

Pour $x=1$, $P_m(1)=P_0(1)=2$ : $C=(1,2)$.

### Question (15)

> [!INDICATION]
> Suivez l'indication : $P_0(x)=(x+1)(2x-1)$ et $h(x)=(x+1)(2x-1)(x-1)$.

#### Solution

$P_m(x)=(x+1)(2x-1)(mx-m+1)$, donc $\alpha_m=1-\frac1m\to1$ quand $m\to+\infty$.

Pour $m=\frac12$ et $m=2$, cette racine coïncide avec $-1$ ou avec $\frac12$, sans effet sur la limite.

## Exercice 3 — Trois jetons

L'univers est formé des $8$ triplets de faces visibles, équiprobables. La clé est la question (2) : chaque valeur de $X$ détermine la valeur de $Y$.

### Question (1)

> [!INDICATION]
> Chaque jeton montre sa face bleue avec probabilité $\frac12$, indépendamment des autres.

#### Solution

$X\hookrightarrow\mathcal B\left(3,\frac12\right)$, $E(X)=\frac32$, $V(X)=\frac34$.

> [!METHODE]
> Justifier une loi binomiale : $n$ épreuves de Bernoulli **indépendantes**, de **même** paramètre, et $X$ compte les succès.

### Question (2)

> [!INDICATION]
> Selon le nombre de faces bleues, combien de couleurs voit-on ? Les couleurs non bleues sont toutes différentes.

#### Solution

$X=3\Rightarrow Y=1$ ; $X=2\Rightarrow Y=2$ ; $X=1\Rightarrow Y=3$ ; $X=0\Rightarrow Y=3$ (rouge, jaune, vert). Donc $Y(\Omega)=\{1,2,3\}$.

### Question (3)

> [!INDICATION]
> Une seule couleur visible : laquelle peut-ce être ?

#### Solution

$(Y=1)=(X=3)$, donc $P(Y=1)=\frac18$.

### Question (4)

> [!INDICATION]
> Même raisonnement pour deux couleurs.

#### Solution

$(Y=2)=(X=2)$, donc $P(Y=2)=\frac38$.

### Question (5)

> [!INDICATION]
> Complémentaire.

#### Solution

$P(Y=3)=1-\frac18-\frac38=\frac12$.

### Question (6)

> [!INDICATION]
> Définition de l'espérance d'une variable finie.

#### Solution

$E(Y)=\frac18+\frac68+\frac{12}8=\frac{19}8$.

### Question (7)

> [!INDICATION]
> Koenig-Huygens.

#### Solution

$E(Y^2)=\frac{1+12+36}8=\frac{49}8$, donc $V(Y)=\frac{49}8-\frac{361}{64}=\frac{31}{64}$.

### Question (8)

> [!INDICATION]
> Exactement une face bleue : laquelle ? Écrivez les triplets.

#### Solution

Les trois issues sont (bleu, jaune, vert), (rouge, bleu, vert), (rouge, jaune, bleu) ; elles réalisent toutes $Y=3$. Donc $P((X=1)\cap(Y=3))=\frac38$.

### Question (9)

> [!INDICATION]
> Utilisez les égalités d'événements de la question (2).

#### Solution

$\mathbf A=\frac18$, $\mathbf B=\frac38$, $\mathbf C=\frac38$, $\mathbf D=\frac18$.

### Question (10)

> [!INDICATION]
> $E(XY)$ se calcule sur les cases non nulles du tableau.

#### Solution

$$\begin{aligned}
E(XY)&=\frac{9}8+\frac{12}8+\frac38=3,\\
\mathrm{Cov}(X,Y)&=3-\frac32\cdot\frac{19}8=-\frac9{16}.
\end{aligned}$$

### Question (11)

> [!INDICATION]
> Que vaut la covariance de deux variables indépendantes ?

#### Solution

$\mathrm{Cov}(X,Y)\neq0$ : $X$ et $Y$ ne sont pas indépendantes.

> [!PIEGE]
> La réciproque « covariance nulle $\Rightarrow$ indépendance » est fausse ; ici on utilise la contraposée du sens vrai.

### Question (12)

> [!INDICATION]
> Chaque jeton montre $1$ ou un numéro qui lui est propre ($2$, $3$ ou $4$) : énumérez les $8$ cas.

#### Solution

$Z(\Omega)=\{1,2,3,4,6,8,12,24\}$, chaque valeur correspondant à un seul triplet : $P(Z=z)=\frac18$ pour chacune.

> [!JURY]
> Rapport 2025 : « le support de Z dans la question (12) a finalement été souvent trouvé ». La loi, elle, demande de vérifier que les $8$ produits sont distincts.

### Question (13)

> [!INDICATION]
> Moyenne des $8$ valeurs, puisque la loi est uniforme.

#### Solution

$E(Z)=\frac{60}8=\frac{15}2$.

## Exercice 4 — Une variable à densité

### Question (1)

> [!INDICATION]
> En $+\infty$, séparez $G(x)$ en deux termes et utilisez les croissances comparées.

#### Solution

En $-\infty$ : produit de $x+1\to-\infty$ et $e^{-x}\to+\infty$, d'où $-\infty$. En $+\infty$ : $G(x)=\frac x{e^x}+e^{-x}\to0$.

### Question (2)

> [!INDICATION]
> Dérivée d'un produit, avec $(e^{-x})'=-e^{-x}$.

#### Solution

$G'(x)=e^{-x}-(x+1)e^{-x}=-xe^{-x}$.

### Question (3)

> [!INDICATION]
> Signe de $-x$.

#### Solution

$G$ croît sur $]-\infty,0]$ et décroît sur $[0,+\infty[$, de maximum $G(0)=1$ ; limites $-\infty$ et $0$.

### Question (4)

> [!INDICATION]
> Calculez $G''$ et étudiez son signe autour de $1$.

#### Solution

$G''(x)=(x-1)e^{-x}$ change de signe en $1$ : point d'inflexion d'abscisse $1$.

> [!PIEGE]
> Annulation de $G''$ ne suffit pas : il faut un **changement de signe**.

### Question (5)

> [!INDICATION]
> Trois conditions ; pour l'intégrale, une primitive de $te^{-t}$ se lit à la question (2).

#### Solution

$f\geqslant0$, continue sauf peut-être en $0$. Comme $(-G)'(t)=te^{-t}$,
$$\int_0^Ate^{-t}\,dt=1-G(A)\xrightarrow[A\to+\infty]{}1,$$
donc $\int_{-\infty}^{+\infty}f=1$ : $f$ est une densité.

> [!METHODE]
> Reconnaître une primitive dans une question précédente évite une intégration par parties : ici $-G$ est une primitive de $te^{-t}$.

### Question (6)

> [!INDICATION]
> Calculez $\int_{-\infty}^xf(t)\,dt$ en distinguant $x<0$ et $x\geqslant0$.

#### Solution

Pour $x<0$, l'intégrale est nulle ; pour $x\geqslant0$, elle vaut $1-G(x)=1-(x+1)e^{-x}$. C'est $F$.

### Question (7)

> [!INDICATION]
> Événement contraire.

#### Solution

$P(X>1)=1-F(1)=\frac2e$.

### Question (8)

> [!INDICATION]
> Dérivez $t^2$ et primitivez $e^{-t}$.

#### Solution

Avec $u(t)=t^2$, $v(t)=-e^{-t}$ (dérivables à dérivées continues sur $[0,x]$) :
$$\int_0^xt^2e^{-t}\,dt=\Big[-t^2e^{-t}\Big]_0^x+2\int_0^xte^{-t}\,dt=-x^2e^{-x}+2\int_0^xte^{-t}\,dt.$$

### Question (9)

> [!INDICATION]
> $tf(t)=t^2e^{-t}$ pour $t\geqslant0$ : faites tendre $x$ vers $+\infty$ dans la question (8).

#### Solution

$\int_0^xte^{-t}\,dt\to1$ (question 5) et $x^2e^{-x}\to0$ (croissances comparées), donc $\int_0^{+\infty}t^2e^{-t}\,dt$ converge et vaut $2$. Donc $E(X)=2$.

> [!JURY]
> Rapport 2025 : « Lorsque le résultat attendu est donné par l‘énoncé, n’essayez pas de l’obtenir à tout prix en masquant vos erreurs par un calcul ou un raisonnement faux. Faites preuve d’honnêteté ! »

## Bilan

**Méthodes à retenir.**

- Une relation polynomiale sur une matrice ($(A-I)^2=0$) donne l'inverse, les puissances par récurrence, et les valeurs propres possibles.
- Non-diagonalisabilité : une seule valeur propre $\lambda$ et $A\neq\lambda I$.
- Suite $X_{n+1}=AX_n+B$ : point fixe $F$, puis $X_n-F=A^n(X_0-F)$.
- Étude de fonction : dérivée factorisée, tableau, théorème de la bijection pour l'unicité d'une racine ; dichotomie déroulée à la main.
- Polynômes dépendant d'un paramètre : écrire $P_m=P_0+m\,h$ pour trouver les points communs.
- Probabilités finies : décrire l'univers, relier les variables entre elles (ici $Y$ fonction de $X$), covariance par Koenig-Huygens.
- Densité : primitive repérée dans une question antérieure, IPP pour le moment d'ordre $1$.

**Prérequis à revoir.** Définition d'un vecteur propre (non nul !), loi binomiale, croissances comparées, intégration par parties, aire entre deux courbes.

**Questions transposables.** Matrice $A=I+N$ avec $N^2=0$, suites matricielles avec point fixe, dichotomie en Python, densité $te^{-t}$ (loi gamma de paramètre $2$) : des classiques des sujets de la voie technologique.
