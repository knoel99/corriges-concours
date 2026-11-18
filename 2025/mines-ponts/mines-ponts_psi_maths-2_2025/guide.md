# Mines-Ponts PSI — Mathématiques 2 2025 · Corrigé guidé

*Corrigé rédigé par IA, non officiel. Signalez toute erreur.*

## Présentation du sujet

Le sujet étudie un modèle continu de propagation d’épidémie au moyen d’une équation différentielle et de séries d’exponentielles. Il examine ensuite un modèle discret fondé sur des rencontres aléatoires.

- **Parties I et II.** Résoudre l’équation linéarisée, déterminer la limite du modèle non linéaire et établir les propriétés des séries de Dirichlet.
- **Parties III et IV.** Relier les dérivées à l’origine aux coefficients de la série, puis étudier une approximation par troncature.
- **Parties V et VI.** Retrouver l’équation dans le système SIR et calculer les espérances d’évolution du modèle probabiliste.

L’épreuve dure trois heures sans calculatrice. Les Q1, Q2 et Q4 à Q6 mobilisent des outils de cours directs. Prévoyez du temps pour la limite en Q3, l’isolement des coefficients en Q8, la récurrence de Q11 et les conditionnements de la dernière partie.

Essayez d’abord chaque question, puis ouvrez les indications dans l’ordre. Consultez la solution après avoir repris votre calcul ou votre preuve.

## Partie I — Linéarisation de (E)

### Question 1

> [!INDICATION]
> Réunissez le terme constant et la fonction inconnue dans la même parenthèse.

> [!INDICATION]
> Cherchez un facteur intégrant. Déterminez la constante par la condition initiale, puis étudiez le signe de la dérivée sur le bon intervalle.

#### Solution

L’équation linéarisée est $u'+(u+1)/2=0$. Elle équivaut à
$$
\frac{\mathrm d}{\mathrm dx}\bigl(e^{x/2}(u(x)+1)\bigr)=0.
$$
Sur $\mathbb R_+$, le produit $e^{x/2}(u(x)+1)$ est donc constant. La condition $u(0)=0$ impose que cette constante soit $1$. Réciproquement, **$u(x)=e^{-x/2}-1$** satisfait l’équation et la condition initiale. C’est l’unique solution cherchée. Comme $u'(x)=-e^{-x/2}/2$, son tableau de variation est
$$
\begin{array}{c|ccc}
x & 0 && +\infty\\ \hline
u'(x) && - &\\ \hline
u(x) & 0 & \searrow & -1
\end{array}
$$

> [!JURY]
> Le rapport conseille une résolution directe lorsque le facteur intégrant est immédiat. Le tableau doit rester sur le domaine de l’énoncé.

### Question 2

> [!INDICATION]
> Substituez directement une fonction de valeur constante dans l’équation, puis comparez avec la limite de la solution de Q1.

#### Solution

La fonction constante de valeur $\gamma$ vérifie l’équation $(E_\ell)$ si et seulement si $(\gamma+1)/2=0$. Il y a donc une unique solution constante, de valeur **$\gamma=-1$**. La formule de Q1 donne bien $\lim_{x\to+\infty}u(x)=\gamma$.

### Question 3

> [!INDICATION]
> L’équation détermine une limite pour la dérivée. Examinez les conséquences d’une telle limite si elle était non nulle.

> [!INDICATION]
> Étudiez les variations de la fonction dont les zéros sont les équilibres. Le signe de la limite de y se lit avec la condition initiale.

#### Solution

Posons $F(t)=e^t/2-t-1$. L’équation donne $y'=F\circ y$. Par continuité, $y(x)\to c$ entraîne $y'(x)\to F(c)$.

Si cette limite était non nulle, $y'$ garderait au-delà d’un certain réel un signe constant et un module minoré par une constante strictement positive. En intégrant sur un intervalle partant de ce réel, on contredirait la convergence de $y$.

Ainsi $F(c)=0$ et la fonction constante de valeur $c$ est solution de $(E)$.

La dérivée $F'(t)=e^t/2-1$ est négative pour $t<\ln2$ et positive pour $t>\ln2$.

La fonction $F$ tend vers $+\infty$ aux deux extrémités de $\mathbb R$, et $F(0)=-1/2$.

Par continuité et stricte monotonie de part et d’autre de $\ln2$, elle admet exactement deux zéros, l’un $c_1<0$ et l’autre $c_2>\ln2>0$.

Puisque $y$ décroît à partir de $y(0)=0$, sa limite est au plus nulle. D’où **$c=c_1$**.

> [!JURY]
> Le rapport rappelle que la convergence de y ne suffit pas à établir la convergence de sa dérivée. L’équation donne ici la limite de cette dérivée.

## Partie II — Séries de Dirichlet

### Question 4

> [!INDICATION]
> Traduisez la croissance de la suite d’exposants en une majoration exploitable.

> [!INDICATION]
> Comparez en valeur absolue à un produit d’une puissance de n par une suite géométrique.

#### Solution

Fixons $k\in\mathbb N$.

Comme $\lambda_n=O(n)$ et $\lambda_n>0$ pour $n\ge1$, on dispose d’une constante $C>0$ telle que $\lambda_n\le Cn$ pour tout $n\ge1$. Alors
$$
|\lambda_n^ka_n|\le MC^k n^k2^{-n}.
$$
La série de terme général $n^k2^{-n}$ converge par le critère de d’Alembert, car le quotient de deux termes consécutifs tend vers $1/2$. La série qui définit **$b_k=\sum_{n\ge1}\lambda_n^k a_n$** converge donc absolument.

### Question 5

> [!INDICATION]
> Majorez le module du terme général indépendamment de x sur la demi-droite. Quel théorème donne alors la continuité de la somme ?

#### Solution

Pour tout $x\ge0$ et tout $n\ge0$, on a $|f_n(x)|\le |a_n|\le M2^{-n}$, puisque $\lambda_n\ge0$.

La série géométrique $\sum_{n\ge0}M2^{-n}$ converge. La série de Dirichlet converge donc normalement et uniformément sur $\mathbb R_+$. Sa somme $f$ y est continue, comme limite uniforme de sommes partielles continues.

### Question 6

> [!INDICATION]
> Isolez le terme dont l’exposant est nul. Un même facteur exponentiel peut majorer tous les autres termes quand x augmente.

#### Solution

À l’origine, tous les facteurs exponentiels valent $1$. Ainsi **$f(0)=a_0+b_0$**. Pour $n\ge1$, $\lambda_n\ge\lambda_1>0$. On en déduit
$$
|f(x)-a_0|\le e^{-\lambda_1x}\sum_{n\ge1}|a_n|.
$$
La somme est finie et l’exponentielle tend vers zéro. Par conséquent, **$\lim_{x\to+\infty}f(x)=a_0$**.

### Question 7

> [!INDICATION]
> Dérivez un terme exponentiel à un ordre quelconque.

> [!INDICATION]
> Vérifiez la convergence des séries de dérivées à tous les ordres nécessaires avant de dériver terme à terme.

#### Solution

Pour $j\ge1$, le terme d’indice zéro est constant et, pour $n\ge1$,
$$
f_n^{(j)}(x)=(-1)^j\lambda_n^j a_n e^{-\lambda_n x}.
$$
Pour chaque ordre $j$, la série des dérivées correspondante converge normalement sur $\mathbb R_+$, car $\sum_{n\ge1}\lambda_n^j|a_n|$ converge d’après Q4. On part de la convergence de la série initiale en Q5 et on applique successivement le théorème de dérivation terme à terme, sur chaque segment $[0,A]$.

Ainsi $f$ est de classe $\mathcal C^k$ sur $\mathbb R_+$ et, pour $1\le j\le k$,
$$
\boxed{f^{(j)}(x)=(-1)^j\sum_{n\ge1}\lambda_n^j a_n e^{-\lambda_nx}.}
$$
À l’origine, **$f^{(k)}(0)=(-1)^k b_k$**.

> [!JURY]
> Le rapport conseille de contrôler les séries dérivées à chaque ordre utile pour appliquer le théorème de proche en proche.

### Question 8

> [!INDICATION]
> Retrouvez le premier coefficient en passant à la limite à l’infini.

> [!INDICATION]
> Une fois les premiers coefficients annulés, multipliez par l’exponentielle qui rend constant le premier terme restant.

#### Solution

Si $f$ est identiquement nulle, Q6 donne d’abord $a_0=0$. Supposons $a_0=\cdots=a_{m-1}=0$ pour un entier $m\ge1$. En multipliant l’égalité $f(x)=0$ par $e^{\lambda_mx}$, on obtient
$$
0=a_m+\sum_{n>m}a_ne^{-(\lambda_n-\lambda_m)x}.
$$
Le module de la somme est majoré par
$$
e^{-(\lambda_{m+1}-\lambda_m)x}\sum_{n>m}|a_n|.
$$
Cette borne tend vers zéro car $\lambda_{m+1}>\lambda_m$. Le passage à la limite donne $a_m=0$. Ainsi **tous les coefficients $a_n$ sont nuls**.

> [!JURY]
> Le rapport distingue une série d’exponentielles d’une combinaison linéaire finie. Le passage à la limite isole les coefficients successifs.

## Partie III — Relations sur les coefficients de la série de Dirichlet

### Question 9

> [!INDICATION]
> Utilisez à la fois la valeur à l’origine et la limite calculées en Q6.

#### Solution

La limite de $y$ vaut $c$ par hypothèse et $a_0$ par Q6. De plus, $y(0)=a_0+b_0=0$. On obtient **$a_0=c$ et $b_0=-c$**.

### Question 10

> [!INDICATION]
> Évaluez l’équation différentielle à l’origine, puis utilisez l’identité de Q7.

#### Solution

À l’origine, $(E)$ donne $y'(0)+1=1/2$. Or $y'(0)=-b_1$ d’après Q7. Ainsi **$b_1=1/2$**.

### Question 11

> [!INDICATION]
> Écrivez la première dérivée de g comme un produit de deux fonctions.

> [!INDICATION]
> Appliquez Leibniz à ce produit. Comparez la récurrence pour les dérivées signées de g avec celle des coefficients donnés.

#### Solution

Posons $D_k=(-1)^k g^{(k)}(0)$ pour $k\ge0$. Alors $D_0=g(0)=1$. Comme $g'=y'g$, la formule de Leibniz appliquée à l’ordre $k-1$ donne, pour $k\ge1$,
$$
g^{(k)}(0)=\sum_{i=1}^{k}\binom{k-1}{i-1}y^{(i)}(0)g^{(k-i)}(0).
$$
En remplaçant $y^{(i)}(0)$ par $(-1)^i b_i$, tous les produits portent le même facteur $(-1)^k$. Il reste
$$
D_k=\sum_{i=1}^{k}\binom{k-1}{i-1}b_iD_{k-i}.
$$
La valeur initiale et la récurrence coïncident avec celles de $(d_k)$. Chaque coefficient étant déterminé par les précédents, $D_k=d_k$, soit **$g^{(k)}(0)=(-1)^kd_k$**.

> [!JURY]
> Le rapport attend que le facteur de signe commun soit extrait et que la valeur initiale soit comparée.

### Question 12

> [!INDICATION]
> Dérivez l’équation à l’ordre demandé. Évaluez ensuite à zéro en utilisant les deux formules pour les dérivées.

#### Solution

Pour $k\ge1$, on dérive $(E)$ exactement $k$ fois. La constante $1$ disparaît. À l’origine, l’égalité devient
$$
(-1)^{k+1}b_{k+1}+(-1)^kb_k=\tfrac12(-1)^kd_k.
$$
On en déduit **$b_{k+1}=b_k-\tfrac12d_k$** pour tout $k\ge1$.

## Partie IV — Approximation de la solution y

### Question 13

> [!INDICATION]
> Fixez x et majorez le reste de la série terme à terme.

> [!INDICATION]
> Si x est minoré par un réel strictement positif, utilisez aussi le plus petit exposant du reste.

#### Solution

Pour chaque $x\ge0$, la troncature donne
$$
\begin{aligned}|y_N(x)-y(x)|&\le\sum_{n>N}|a_n|e^{-\lambda_nx}\\
&\le M\sum_{n>N}2^{-n}=\frac{M}{2^N}.\end{aligned}
$$
Le majorant est indépendant de $x$. Ainsi **$\|y_N-y\|_{\infty,\mathbb R_+}\le M/2^N$**, et $y_N$ converge uniformément vers $y$ sur $\mathbb R_+$.

Sur tout intervalle $J=[\delta,+\infty[$ avec $\delta>0$, l’exponentielle dans la somme est au plus $e^{-\lambda_{N+1}\delta}$. On obtient la borne plus fine
$$
\|y_N-y\|_{\infty,J}\le\frac{M}{2^N}e^{-\lambda_{N+1}\delta}.
$$

### Question 14

> [!INDICATION]
> La ligne k doit calculer le moment d’indice k−1. Identifiez le coefficient associé à la n-ième inconnue.

#### Solution

Pour $1\le k,n\le N$, définissons **$V_{k,n}=\lambda_n^{k-1}$**. Alors la $k$-ième coordonnée de $VA$ vaut
$$
\begin{aligned}(VA)_k&=\sum_{n=1}^{N}\lambda_n^{k-1}a_n\\&=\beta_{k-1}=B_k.\end{aligned}
$$
Ainsi $VA=B$ avec la matrice de Vandermonde $V$ d’ordre $N$ ainsi définie.

> [!JURY]
> Le rapport insiste sur les indices de la matrice, dont la première ligne calcule le moment d’ordre zéro.

### Question 15

> [!INDICATION]
> Cherchez une raison d’utiliser le caractère deux à deux distinct des exposants.

> [!INDICATION]
> Vous pouvez interpréter le noyau de la transposée par un polynôme évalué en ces exposants.

#### Solution

Les $\lambda_n$ sont deux à deux distincts. Si $V^{\mathsf T}X=0$ pour $X=(x_1,\ldots,x_N)^{\mathsf T}$, le polynôme
$$
Q(T)=\sum_{k=1}^{N}x_kT^{k-1}
$$
s’annule en chacun des $N$ points $\lambda_n$. Son degré est au plus $N-1$, donc $Q=0$ et $X=0$.

La matrice carrée $V^{\mathsf T}$ est inversible et $V$ aussi. Par conséquent, **$A=V^{-1}B$ est l’unique solution**.

## Partie V — Modèle de propagation d’épidémie SIR

### Question 16

> [!INDICATION]
> Essayez un triplet dont la première composante est identiquement nulle, puis vérifiez toutes les équations et conditions initiales.

#### Solution

Pour $S_0=0$, le triplet
$$
\boxed{\begin{aligned}
S(x)&=0,\\
I(x)&=I_0e^{-x},\\
R(x)&=R_0+I_0(1-e^{-x})
\end{aligned}}
$$
satisfait toutes les équations du système $(F)$ et les conditions initiales. Il est donc le triplet solution par l’unicité admise au théorème 1.

### Question 17

> [!INDICATION]
> Voyez la première équation comme une équation linéaire en S, avec I comme coefficient connu.

> [!INDICATION]
> Introduisez la primitive de I qui s’annule à l’origine pour construire un facteur intégrant.

#### Solution

La première équation est $S'+IS=0$ avec $I$ continue. En posant $J(x)=\int_0^x I(t)\,\mathrm dt$, on obtient $(e^J S)'=0$. La valeur à l’origine impose donc
$$
\boxed{S(x)=S_0\exp\left(-\int_0^x I(t)\,\mathrm dt\right).}
$$
Si $S_0>0$, le produit est strictement positif pour tout $x\ge0$.

### Question 18

> [!INDICATION]
> Isolez I dans la première équation grâce à la positivité de S. Différenciez cette relation et utilisez la deuxième équation.

#### Solution

Par Q17, on peut diviser la première équation par $S$. Elle donne $I=-S'/S$. En dérivant puis en utilisant la deuxième équation du système,
$$
\begin{aligned}-\left(\frac{S'}S\right)'&=I'=IS-I\\&=-S'+\frac{S'}S.\end{aligned}
$$
C’est la relation demandée.

### Question 19

> [!INDICATION]
> Exprimez la dérivée de h puis celle de la somme de S et I.

> [!INDICATION]
> Identifiez la constante de leur différence par les conditions initiales et réexprimez S en fonction de h.

#### Solution

Comme $h=\ln(S/S_0)$, on a $h'=S'/S=-I$. D’autre part, le système donne $S'+I'=-I$. Donc $(S+I-h)'=0$.

À l’origine, $S(0)+I(0)=1$ et $h(0)=0$, d’où $S+I-h=1$ sur $\mathbb R_+$.

En substituant $I=-h'$ et $S=\tfrac12e^h$, il vient **$h'+h+1=\tfrac12e^h$**. Avec $h(0)=0$, cela donne le problème $(C)$. Par l’unicité admise, $h=y$.

> [!JURY]
> Le rapport attend un calcul de la constante après avoir identifié deux expressions de même dérivée.

### Question 20

> [!INDICATION]
> Trouvez un segment commun contenant les valeurs des deux fonctions dans les exponentielles.

> [!INDICATION]
> Majorez la dérivée de l’exponentielle sur ce segment avant de réutiliser la norme du reste de Q13.

#### Solution

Les deux fonctions $y_N$ et $y$ prennent leurs valeurs dans $[-2M,2M]$, puisque la somme des modules de leurs termes est majorée par $\sum_{n\ge0}M2^{-n}=2M$. L’inégalité des accroissements finis pour l’exponentielle sur ce segment donne
$$
|e^{y_N(x)}-e^{y(x)}|\le e^{2M}|y_N(x)-y(x)|.
$$
Comme $S=\tfrac12e^y$ d’après Q19, la borne de Q13 entraîne
$$
\boxed{\|S_N-S\|_{\infty,\mathbb R_+}\le\frac{M e^{2M}}{2^{N+1}}.}
$$
Le majorant tend vers zéro, ce qui donne la convergence uniforme.

> [!JURY]
> Le rapport recommande l’inégalité des accroissements finis avec une borne commune sur les deux arguments.

## Partie VI — Modèle probabiliste

### Question 21

> [!INDICATION]
> Comptez les groupes de personnes que peut rencontrer une personne susceptible.

> [!INDICATION]
> Calculez la probabilité de l’événement contraire en ne comptant que les groupes sans personne infectée.

#### Solution

Fixons un état de départ $(s,i,r)\in E$ où $s>0$. Dans le tirage uniforme d’un groupe de $K$ personnes distinctes parmi les $M$ de la population, annoncé par l’énoncé, il y a $\binom MK$ groupes possibles.

Une personne susceptible échappe à l’infection exactement si le groupe ne contient aucun des $i$ infectés. Il y a $\binom{M-i}{K}$ groupes de ce type. Ainsi
$$
\boxed{p(i)=1-\frac{\binom{M-i}{K}}{\binom MK}.}
$$
Cette convention vaut pour tout $K$ autorisé dans l’énoncé. Si l’on exclut la personne susceptible elle-même des rencontres possibles et que $K\le M-1$, on trouve
$$
p(i)=1-\frac{\binom{M-1-i}{K}}{\binom{M-1}{K}}
.
$$
Les identités suivantes utilisent la probabilité $p(i)$ du modèle de tirage retenu. Quand $s=0$, aucune infection nouvelle ne peut se produire. Dans la seconde convention, on peut poser $p(M)=0$ pour compléter la définition, car $i=M$ impose $s=0$.

> [!JURY]
> Le rapport donne la préférence au décompte parmi les autres personnes et accepte le décompte parmi les M personnes mentionnées dans l’énoncé.

### Question 22

> [!INDICATION]
> Fixez d’abord une valeur de Z et décomposez sa probabilité suivant l’état de la population.

> [!INDICATION]
> Repérez pourquoi les deux sommes peuvent être interverties.

#### Solution

Pour un jour $n$ fixé, notons $A_{s,i,r}=\{(\widetilde S_n,\widetilde I_n,\widetilde R_n)=(s,i,r)\}$. Ces événements sont disjoints et leur union est certaine. On applique la formule des probabilités totales à $\{Z=k\}$, puis on multiplie par $k$ et on somme. Les deux sommes sont finies, d’où
$$
\begin{aligned}\mathbb E[Z]&=\sum_{k=0}^{M}k\,\mathbb P(Z=k)\\
&=\sum_{(s,i,r)\in E}\left(\sum_{k=0}^{M} k\,\mathbb P(Z=k\mid A_{s,i,r})\right)\mathbb P(A_{s,i,r}).\end{aligned}
$$
Les termes associés à un état de probabilité nulle sont comptés pour zéro.

> [!JURY]
> Le rapport demande de nommer les événements qui partitionnent l’univers et de justifier l’interversion par la finitude des sommes.

### Question 23

> [!INDICATION]
> Encadrez chaque effectif, puis encadrez la différence entre deux effectifs successifs.

#### Solution

Les trois effectifs sont des entiers compris entre $0$ et $M$. Leurs accroissements sont des différences de deux tels entiers, donc appartiennent à $[-M,M]$. Ces six variables aléatoires sont bornées et possèdent une espérance finie.

### Question 24

> [!INDICATION]
> Dans un état fixé, comptez les personnes pouvant guérir ce jour-là.

> [!INDICATION]
> Écrivez le nombre de guérisons comme une somme d’indicatrices, puis utilisez Q22.

#### Solution

Conditionnellement à un état $A_{s,i,r}$ de probabilité positive, $\Delta\widetilde R_n$ compte les guérisons parmi les $i$ personnes infectées le matin. La probabilité que chacune guérisse est $\rho$. En écrivant le nombre de guérisons comme somme des indicatrices correspondantes, la moyenne conditionnelle vaut donc $i\rho$ par linéarité.

La formule de Q22, appliquée au nombre de guérisons, donne
$$
\boxed{\mathbb E[\Delta\widetilde R_n]
=\sum_{(s,i,r)\in E}\rho i\,\mathbb P(A_{s,i,r})
=\rho\,\mathbb E[\widetilde I_n].}
$$

### Question 25

> [!INDICATION]
> Sous la condition de l’état initial, identifiez les essais indépendants et leur probabilité de succès.

> [!INDICATION]
> Vérifiez le signe qui lie le nombre de succès à l’accroissement du nombre de susceptibles.

#### Solution

Sous la condition $A_{s,i,r}$ de probabilité positive, les $s$ personnes susceptibles sont exposées indépendamment, chacune avec probabilité $p(i)$ d’être infectée.

Le nombre de nouvelles infections suit donc la loi binomiale de paramètres $s$ et $p(i)$. Il vaut $-\Delta\widetilde S_n$. Par conséquent, pour $0\le k\le s$,
$$
\boxed{\mathbb P(\Delta\widetilde S_n=-k\mid A_{s,i,r})
=\binom sk p(i)^k[1-p(i)]^{s-k}.}
$$
La formule comprend les lois concentrées en $0$ ou en $s$ lorsque $p(i)$ vaut respectivement $0$ ou $1$.

> [!JURY]
> Le rapport attire l’attention sur le conditionnement par l’état du matin.

### Question 26

> [!INDICATION]
> Utilisez l’espérance de la loi binomiale puis sommez sur les états.

> [!INDICATION]
> Écrivez la conservation de l’effectif en termes d’accroissements et remplacez les espérances déjà calculées.

#### Solution

La loi binomiale de Q25 a pour moyenne $s\,p(i)$ sous la condition $A_{s,i,r}$. La formule de Q22 appliquée à $-\Delta\widetilde S_n$ donne
$$
\begin{aligned}
\mathbb E[-\Delta\widetilde S_n]
&=\sum_{(s,i,r)\in E}s\,p(i)\,\mathbb P(A_{s,i,r})\\
&=\mathbb E[\widetilde S_n\,p(\widetilde I_n)].
\end{aligned}
$$
On obtient ainsi la première identité demandée. Par conservation de l’effectif total, la somme des trois accroissements est nulle. En utilisant aussi Q24,
$$
\boxed{\mathbb E[\Delta\widetilde I_n]
=\mathbb E[\widetilde S_n\,p(\widetilde I_n)]
-\rho\,\mathbb E[\widetilde I_n].}
$$

## Bilan

- Une équation différentielle peut donner une limite pour la dérivée lorsque la fonction converge. Exploitez ensuite cette limite avec une intégration ou un accroissement fini.
- Pour une série d’exponentielles, une majoration indépendante de la variable justifie les passages à la somme. Pour isoler un coefficient, comparez les exposants restants.
- Dans le modèle discret, effectuez le calcul à effectifs fixés. La formule des probabilités totales permet de revenir aux espérances sur l’ensemble des états.
