# Mines-Ponts PSI — Mathématiques 2 2025 · Corrigé brut

*Corrigé rédigé par IA, non officiel. Signalez toute erreur.*

## Partie I — Linéarisation de (E)

### Question 1

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

### Question 2

La fonction constante de valeur $\gamma$ vérifie l’équation $(E_\ell)$ si et seulement si $(\gamma+1)/2=0$. Il y a donc une unique solution constante, de valeur **$\gamma=-1$**. La formule de Q1 donne bien $\lim_{x\to+\infty}u(x)=\gamma$.

### Question 3

Posons $F(t)=e^t/2-t-1$. L’équation donne $y'=F\circ y$. Par continuité, $y(x)\to c$ entraîne $y'(x)\to F(c)$.

Si cette limite était non nulle, $y'$ garderait au-delà d’un certain réel un signe constant et un module minoré par une constante strictement positive. En intégrant sur un intervalle partant de ce réel, on contredirait la convergence de $y$.

Ainsi $F(c)=0$ et la fonction constante de valeur $c$ est solution de $(E)$.

La dérivée $F'(t)=e^t/2-1$ est négative pour $t<\ln2$ et positive pour $t>\ln2$.

La fonction $F$ tend vers $+\infty$ aux deux extrémités de $\mathbb R$, et $F(0)=-1/2$.

Par continuité et stricte monotonie de part et d’autre de $\ln2$, elle admet exactement deux zéros, l’un $c_1<0$ et l’autre $c_2>\ln2>0$.

Puisque $y$ décroît à partir de $y(0)=0$, sa limite est au plus nulle. D’où **$c=c_1$**.

## Partie II — Séries de Dirichlet

### Question 4

Fixons $k\in\mathbb N$.

Comme $\lambda_n=O(n)$ et $\lambda_n>0$ pour $n\ge1$, on dispose d’une constante $C>0$ telle que $\lambda_n\le Cn$ pour tout $n\ge1$. Alors
$$
|\lambda_n^ka_n|\le MC^k n^k2^{-n}.
$$
La série de terme général $n^k2^{-n}$ converge par le critère de d’Alembert, car le quotient de deux termes consécutifs tend vers $1/2$. La série qui définit **$b_k=\sum_{n\ge1}\lambda_n^k a_n$** converge donc absolument.

### Question 5

Pour tout $x\ge0$ et tout $n\ge0$, on a $|f_n(x)|\le |a_n|\le M2^{-n}$, puisque $\lambda_n\ge0$.

La série géométrique $\sum_{n\ge0}M2^{-n}$ converge. La série de Dirichlet converge donc normalement et uniformément sur $\mathbb R_+$. Sa somme $f$ y est continue, comme limite uniforme de sommes partielles continues.

### Question 6

À l’origine, tous les facteurs exponentiels valent $1$. Ainsi **$f(0)=a_0+b_0$**. Pour $n\ge1$, $\lambda_n\ge\lambda_1>0$. On en déduit
$$
|f(x)-a_0|\le e^{-\lambda_1x}\sum_{n\ge1}|a_n|.
$$
La somme est finie et l’exponentielle tend vers zéro. Par conséquent, **$\lim_{x\to+\infty}f(x)=a_0$**.

### Question 7

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

### Question 8

Si $f$ est identiquement nulle, Q6 donne d’abord $a_0=0$. Supposons $a_0=\cdots=a_{m-1}=0$ pour un entier $m\ge1$. En multipliant l’égalité $f(x)=0$ par $e^{\lambda_mx}$, on obtient
$$
0=a_m+\sum_{n>m}a_ne^{-(\lambda_n-\lambda_m)x}.
$$
Le module de la somme est majoré par
$$
e^{-(\lambda_{m+1}-\lambda_m)x}\sum_{n>m}|a_n|.
$$
Cette borne tend vers zéro car $\lambda_{m+1}>\lambda_m$. Le passage à la limite donne $a_m=0$. Ainsi **tous les coefficients $a_n$ sont nuls**.

## Partie III — Relations sur les coefficients de la série de Dirichlet

### Question 9

La limite de $y$ vaut $c$ par hypothèse et $a_0$ par Q6. De plus, $y(0)=a_0+b_0=0$. On obtient **$a_0=c$ et $b_0=-c$**.

### Question 10

À l’origine, $(E)$ donne $y'(0)+1=1/2$. Or $y'(0)=-b_1$ d’après Q7. Ainsi **$b_1=1/2$**.

### Question 11

Posons $D_k=(-1)^k g^{(k)}(0)$ pour $k\ge0$. Alors $D_0=g(0)=1$. Comme $g'=y'g$, la formule de Leibniz appliquée à l’ordre $k-1$ donne, pour $k\ge1$,
$$
g^{(k)}(0)=\sum_{i=1}^{k}\binom{k-1}{i-1}y^{(i)}(0)g^{(k-i)}(0).
$$
En remplaçant $y^{(i)}(0)$ par $(-1)^i b_i$, tous les produits portent le même facteur $(-1)^k$. Il reste
$$
D_k=\sum_{i=1}^{k}\binom{k-1}{i-1}b_iD_{k-i}.
$$
La valeur initiale et la récurrence coïncident avec celles de $(d_k)$. Chaque coefficient étant déterminé par les précédents, $D_k=d_k$, soit **$g^{(k)}(0)=(-1)^kd_k$**.

### Question 12

Pour $k\ge1$, on dérive $(E)$ exactement $k$ fois. La constante $1$ disparaît. À l’origine, l’égalité devient
$$
(-1)^{k+1}b_{k+1}+(-1)^kb_k=\tfrac12(-1)^kd_k.
$$
On en déduit **$b_{k+1}=b_k-\tfrac12d_k$** pour tout $k\ge1$.

## Partie IV — Approximation de la solution y

### Question 13

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

Pour $1\le k,n\le N$, définissons **$V_{k,n}=\lambda_n^{k-1}$**. Alors la $k$-ième coordonnée de $VA$ vaut
$$
\begin{aligned}(VA)_k&=\sum_{n=1}^{N}\lambda_n^{k-1}a_n\\&=\beta_{k-1}=B_k.\end{aligned}
$$
Ainsi $VA=B$ avec la matrice de Vandermonde $V$ d’ordre $N$ ainsi définie.

### Question 15

Les $\lambda_n$ sont deux à deux distincts. Si $V^{\mathsf T}X=0$ pour $X=(x_1,\ldots,x_N)^{\mathsf T}$, le polynôme
$$
Q(T)=\sum_{k=1}^{N}x_kT^{k-1}
$$
s’annule en chacun des $N$ points $\lambda_n$. Son degré est au plus $N-1$, donc $Q=0$ et $X=0$.

La matrice carrée $V^{\mathsf T}$ est inversible et $V$ aussi. Par conséquent, **$A=V^{-1}B$ est l’unique solution**.

## Partie V — Modèle de propagation d’épidémie SIR

### Question 16

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

La première équation est $S'+IS=0$ avec $I$ continue. En posant $J(x)=\int_0^x I(t)\,\mathrm dt$, on obtient $(e^J S)'=0$. La valeur à l’origine impose donc
$$
\boxed{S(x)=S_0\exp\left(-\int_0^x I(t)\,\mathrm dt\right).}
$$
Si $S_0>0$, le produit est strictement positif pour tout $x\ge0$.

### Question 18

Par Q17, on peut diviser la première équation par $S$. Elle donne $I=-S'/S$. En dérivant puis en utilisant la deuxième équation du système,
$$
\begin{aligned}-\left(\frac{S'}S\right)'&=I'=IS-I\\&=-S'+\frac{S'}S.\end{aligned}
$$
C’est la relation demandée.

### Question 19

Comme $h=\ln(S/S_0)$, on a $h'=S'/S=-I$. D’autre part, le système donne $S'+I'=-I$. Donc $(S+I-h)'=0$.

À l’origine, $S(0)+I(0)=1$ et $h(0)=0$, d’où $S+I-h=1$ sur $\mathbb R_+$.

En substituant $I=-h'$ et $S=\tfrac12e^h$, il vient **$h'+h+1=\tfrac12e^h$**. Avec $h(0)=0$, cela donne le problème $(C)$. Par l’unicité admise, $h=y$.

### Question 20

Les deux fonctions $y_N$ et $y$ prennent leurs valeurs dans $[-2M,2M]$, puisque la somme des modules de leurs termes est majorée par $\sum_{n\ge0}M2^{-n}=2M$. L’inégalité des accroissements finis pour l’exponentielle sur ce segment donne
$$
|e^{y_N(x)}-e^{y(x)}|\le e^{2M}|y_N(x)-y(x)|.
$$
Comme $S=\tfrac12e^y$ d’après Q19, la borne de Q13 entraîne
$$
\boxed{\|S_N-S\|_{\infty,\mathbb R_+}\le\frac{M e^{2M}}{2^{N+1}}.}
$$
Le majorant tend vers zéro, ce qui donne la convergence uniforme.


## Partie VI — Modèle probabiliste

### Question 21

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

### Question 22

Pour un jour $n$ fixé, notons $A_{s,i,r}=\{(\widetilde S_n,\widetilde I_n,\widetilde R_n)=(s,i,r)\}$. Ces événements sont disjoints et leur union est certaine. On applique la formule des probabilités totales à $\{Z=k\}$, puis on multiplie par $k$ et on somme. Les deux sommes sont finies, d’où
$$
\begin{aligned}\mathbb E[Z]&=\sum_{k=0}^{M}k\,\mathbb P(Z=k)\\
&=\sum_{(s,i,r)\in E}\left(\sum_{k=0}^{M} k\,\mathbb P(Z=k\mid A_{s,i,r})\right)\mathbb P(A_{s,i,r}).\end{aligned}
$$
Les termes associés à un état de probabilité nulle sont comptés pour zéro.

### Question 23

Les trois effectifs sont des entiers compris entre $0$ et $M$. Leurs accroissements sont des différences de deux tels entiers, donc appartiennent à $[-M,M]$. Ces six variables aléatoires sont bornées et possèdent une espérance finie.

### Question 24

Conditionnellement à un état $A_{s,i,r}$ de probabilité positive, $\Delta\widetilde R_n$ compte les guérisons parmi les $i$ personnes infectées le matin. La probabilité que chacune guérisse est $\rho$. En écrivant le nombre de guérisons comme somme des indicatrices correspondantes, la moyenne conditionnelle vaut donc $i\rho$ par linéarité.

La formule de Q22, appliquée au nombre de guérisons, donne
$$
\boxed{\mathbb E[\Delta\widetilde R_n]
=\sum_{(s,i,r)\in E}\rho i\,\mathbb P(A_{s,i,r})
=\rho\,\mathbb E[\widetilde I_n].}
$$

### Question 25

Sous la condition $A_{s,i,r}$ de probabilité positive, les $s$ personnes susceptibles sont exposées indépendamment, chacune avec probabilité $p(i)$ d’être infectée.

Le nombre de nouvelles infections suit donc la loi binomiale de paramètres $s$ et $p(i)$. Il vaut $-\Delta\widetilde S_n$. Par conséquent, pour $0\le k\le s$,
$$
\boxed{\mathbb P(\Delta\widetilde S_n=-k\mid A_{s,i,r})
=\binom sk p(i)^k[1-p(i)]^{s-k}.}
$$
La formule comprend les lois concentrées en $0$ ou en $s$ lorsque $p(i)$ vaut respectivement $0$ ou $1$.

### Question 26

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

FIN
