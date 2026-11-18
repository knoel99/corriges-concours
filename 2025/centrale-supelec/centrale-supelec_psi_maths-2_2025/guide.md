# Centrale-Supélec PSI — Mathématiques 2 2025 · Corrigé guidé

*Corrigé rédigé par IA, non officiel. Signalez toute erreur.*

## Présentation du sujet

La série de terme général $n$ diverge au sens usuel. Le problème étudie deux développements asymptotiques dans lesquels apparaît le même terme constant, puis définit une manière de comparer une somme partielle à une intégrale. Il termine par la formule d'Euler-Boole pour les sommes alternées.

| Partie | Questions | Objectif et outils |
|---|---|---|
| A | Q1–Q20 | Extraire le terme constant d'abord par une série géométrique et des développements limités, puis par des sommes de Riemann et Taylor avec reste intégral. |
| B | Q21–Q29 | Construire la formule d'Euler-Maclaurin par intégrations par parties, puis étudier les restes à l'infini et la constante de Ramanujan. |
| C | Q30–Q44 | Construire une famille de polynômes normalisés par une forme linéaire continue, déterminer sa série génératrice et établir la formule d'Euler-Boole. |

Sur cette épreuve de quatre heures, Q1–Q2, Q5–Q9 et Q21–Q25 mobilisent des outils familiers. Il est possible de commencer la partie B sans avoir fini A. En C, Q30 et Q31 donnent un point d'entrée indépendant. Garder du temps pour vérifier les signes en Q15–Q20 et les valeurs aux bornes en Q24–Q26 et Q43–Q44.

Chercher chaque question avant d'ouvrir la première indication. Pour les calculs d'erreur, écrire d'abord quelle quantité le raisonnement doit majorer, puis rouvrir la solution pour comparer les ordres obtenus.

## Partie A — Deux approches pour une valeur à $1+2+\cdots+n+\cdots$

Deux méthodes fournissent une expansion près de zéro. La première part d'une somme exacte. La seconde mesure l'écart entre des rectangles de largeur $x$ et l'intégrale d'une fonction à support compact.

**I — Une première approche**

### Question 1

> [!INDICATION]
> Reconnaître le type de série en prenant $x$ fixé.

#### Solution

La série est géométrique de raison $e^{-x}$. Elle converge exactement lorsque $|e^{-x}|<1$, soit $x>0$. Ainsi, **$D_f=]0,+\infty[$ et $f(x)=(1-e^{-x})^{-1}$** sur $D_f$.

### Question 2

> [!INDICATION]
> Utiliser directement la somme fermée trouvée en Q1.

> [!INDICATION]
> Dériver le dénominateur avant d'appliquer la formule de dérivation d'un inverse.

#### Solution

Sur $D_f$, $1-e^{-x}$ est de classe $\mathcal C^1$ et ne s'annule pas. Son inverse est donc de classe $\mathcal C^1$ et la dérivée de $1-e^{-x}$ est $e^{-x}$. On obtient

$$
\boxed{f'(x)=-\frac{e^{-x}}{(1-e^{-x})^2}.}
$$

### Question 3

> [!INDICATION]
> Simplifier la fraction avant de développer.

> [!INDICATION]
> Multiplier numérateur et dénominateur par $e^x$, puis exploiter la symétrie des deux exponentielles au dénominateur.

#### Solution

En multipliant le numérateur et le dénominateur de la fraction par $e^x$, on obtient l'inverse de $e^x+e^{-x}-2$. Les développements des exponentielles à l'ordre quatre donnent

$$
e^x+e^{-x}-2=x^2+\frac{x^4}{12}+o(x^4).
$$

On factorise $x^2$, puis on utilise $(1+u)^{-1}=1-u+o(u)$ avec $u=x^2/12+o(x^2)$. Ainsi,

$$
\begin{aligned}
\frac{e^{-x}}{(1-e^{-x})^2}
&=\frac{1}{x^2}\left(1-\frac{x^2}{12}+o(x^2)\right)\\
&=\frac{1}{x^2}-\frac1{12}+o(1).
\end{aligned}
$$

Les coefficients sont uniques, par identification successive après multiplication par $x^2$, puis par $x$ après retrait du terme en $x^{-2}$. **$a=1$, $b=0$ et $c=-1/12$.**

> [!JURY]
> Le rapport relève que le reste du dénominateur est souvent négligé. Ici, le facteur $x^2$ explique pourquoi le dénominateur doit être développé jusqu'à l'ordre quatre avant l'inversion.

### Question 4

> [!INDICATION]
> Relier la série demandée à la dérivée de la série de Q1.

> [!INDICATION]
> Pour les dérivées sur $[a,b]$ avec $a>0$, prendre le majorant au bord gauche, puis étudier le rapport de deux majorants successifs.

#### Solution

Les fonctions $x\mapsto e^{-nx}$ sont de classe $\mathcal C^1$ et leur série converge simplement sur $D_f$ d'après Q1.

Sur tout segment $[a,b]\subset D_f$, les dérivées sont majorées en valeur absolue par $ne^{-na}$.

La série de ces majorants converge par la règle de d'Alembert, car le rapport des termes successifs tend vers $e^{-a}<1$.

La série des dérivées converge donc normalement, puis uniformément, sur tout segment de $D_f$.

Le théorème de dérivation des séries de fonctions donne $\sum_{n\ge0}ne^{-nx}=-f'(x)$.

Par Q2 et Q3,

$$
\boxed{\lim_{x\to0^+}\left(\sum_{n=0}^{+\infty}ne^{-nx}-\frac1{x^2}\right)=-\frac1{12}.}
$$

> [!JURY]
> Le rapport demande de justifier la convergence uniforme de la série des dérivées sur chaque segment. Cette justification porte sur les dérivées et concerne les segments inclus dans le domaine.

**II — Une deuxième approche**

**II.1 — Une généralisation du théorème des sommes de Riemann pour les fonctions de classe $\mathcal C^1$**

### Question 5

> [!INDICATION]
> Transformer l'appartenance à l'intervalle en un encadrement de $n$. Vérifier le signe du nombre par lequel on divise.

#### Solution

Comme $x>0$, $a<a+nx\le b$ équivaut à $0<n\le (b-a)/x$.

Pour $n$ entier, cette dernière condition équivaut à $1\le n\le \lfloor(b-a)/x\rfloor$.

**L'ensemble est celui des entiers de $1$ à $\lfloor(b-a)/x\rfloor$**, vide si cette partie entière est nulle.

> [!JURY]
> Le rapport attend des équivalences entre l'appartenance et les inégalités, avec la mention du signe de $x$. Un argument de nécessité à lui seul ne suffit pas à identifier l'ensemble.

### Question 6

> [!INDICATION]
> Écrire l'encadrement qui définit la partie entière de $L/x$ et multiplier par $x$.

#### Solution

La définition de la partie entière donne $L/x-1<\lfloor L/x\rfloor\le L/x$. Comme $x>0$, on en déduit

$$
\boxed{0\le L-\lfloor L/x\rfloor x<x.}
$$

### Question 7

> [!INDICATION]
> Découper l'intégrale aux points $a+nx$ inclus dans le segment.

> [!INDICATION]
> Sur chaque intervalle complet, écrire $xf(a+nx)$ sous la forme d'une intégrale.

#### Solution

Posons $N=\lfloor(b-a)/x\rfloor$.

La relation de Chasles décompose $\int_a^b f$ en les intégrales sur les $N$ intervalles $[a+(n-1)x,a+nx]$, puis sur $[a+Nx,b]$.

Sur le $n$-ième intervalle, $xf(a+nx)$ est l'intégrale de la constante $f(a+nx)$.

Par linéarité,

$$
\begin{aligned}
x\sum_{n=1}^N f(a+nx)-\int_a^b f(t)\,dt
&=\sum_{n=1}^N\int_{a+(n-1)x}^{a+nx}\bigl(f(a+nx)-f(t)\bigr)\,dt\\
&\quad-\int_{a+Nx}^b f(t)\,dt .
\end{aligned}
$$

### Question 8

> [!INDICATION]
> Majorer séparément l'erreur sur les intervalles complets et sur l'intervalle terminal.

> [!INDICATION]
> Appliquer l'inégalité des accroissements finis sur chaque intervalle complet et employer Q6 pour la longueur restante. Compter les intervalles complets avant de passer à la limite.

#### Solution

Les fonctions $f$ et $f'$ sont continues sur le segment, donc bornées. Notons $M=\|f'\|_\infty$ et $F=\|f\|_\infty$. Sur chaque intervalle de Q7, l'inégalité des accroissements finis donne $|f(a+nx)-f(t)|\le Mx$. La valeur absolue de l'intégrale terminale est au plus $F(b-a-Nx)\le Fx$ d'après Q6. Ainsi,

$$
\begin{aligned}
\left|x\sum_{n=1}^N f(a+nx)-\int_a^b f(t)\,dt\right|
&\le NMx^2+Fx\\
&\le \bigl(M(b-a)+F\bigr)x .
\end{aligned}
$$

**La somme pondérée converge vers $\int_a^b f(t)\,dt$ quand $x\to0^+$.**

> [!METHODE]
> Quand le nombre d'intervalles dépend de $x$, majorer d'abord la somme entière. Une erreur de taille $x^2$ sur chaque intervalle complet permet ici un contrôle d'ordre $x$ après sommation.

**II.2 — Un développement asymptotique lorsque $x$ tend vers $0$ de $\sum_{n=1}^{+\infty}n\varphi(nx)$**

Dans cette sous-partie, $N=\lfloor K/x\rfloor$, $I_n=[(n-1)x,nx]$ et toutes les limites en $x=0$ sont prises à droite.

### Question 9

> [!INDICATION]
> Identifier une primitive pour chacun des deux intégrandes et calculer aux bornes avec $\psi(t)=t\varphi(t)$.

#### Solution

On a $\psi(0)=0$ et $\psi'(0)=\varphi(0)=1$ par la formule de dérivation du produit. Comme $\psi(K)=\psi'(K)=0$, le calcul par primitive donne

$$
\begin{aligned}
\int_0^K\psi'(t)\,dt&=0\\
\int_0^K\psi''(t)\,dt&=-1.
\end{aligned}
$$

### Question 10

> [!INDICATION]
> Appliquer le résultat de Q8 aux trois fonctions $\psi$, $\psi'$ et $\psi''$, puis utiliser Q9.

#### Solution

Les fonctions $\psi$, $\psi'$ et $\psi''$ sont de classe $\mathcal C^1$ sur $[0,K]$. On applique Q8 à chacune d'elles, puis Q9 aux deux dernières intégrales. Comme $\psi(nx)=nx\varphi(nx)$,

$$
\begin{aligned}
x\sum_{n=1}^N nx\varphi(nx)&\longrightarrow\int_0^K\psi(t)\,dt,\\
x\sum_{n=1}^N\psi'(nx)&\longrightarrow0,\\
x\sum_{n=1}^N\psi''(nx)&\longrightarrow-1.
\end{aligned}
$$

### Question 11

> [!INDICATION]
> Développer $\psi^{(l)}$ autour de $K$.

> [!INDICATION]
> Repérer quels termes du développement de Taylor subsistent lorsque toutes les dérivées s'annulent au point de départ.

#### Solution

On applique la formule de Taylor avec reste intégral à $\psi^{(l)}$, qui est de classe $\mathcal C^{k+1}$, entre $K$ et $t$ à l'ordre $k$.

Ses dérivées d'ordre $0$ à $k$ s'annulent toutes en $K$.

L'intégrale orientée restante donne, pour tout $t\ge0$,

$$
\boxed{\psi^{(l)}(t)=\int_K^t \frac{(t-s)^k}{k!}\psi^{(k+l+1)}(s)\,ds.}
$$

> [!PIEGE]
> Appliquer Taylor directement à $\psi^{(l)}$ donne le reste demandé. Dériver une intégrale où le paramètre intervient à la fois dans la borne et dans le noyau demanderait d'autres justifications.

### Question 12

> [!INDICATION]
> Estimer l'intégrale avec une puissance de la largeur de l'intervalle terminal.

> [!INDICATION]
> Dans Q11, borner $\psi^{(k+l+1)}$ sur $[0,K]$. Intégrer ensuite la puissance de $K-t$ obtenue.

#### Solution

Fixons $k,l\in\mathbb N$ et posons $M=\max_{[0,K]}|\psi^{(k+l+1)}|$. Pour $Nx\le t\le K$, Q11 donne

$$
|\psi^{(l)}(t)|\le \frac{M}{(k+1)!}(K-t)^{k+1}.
$$

D'après Q6, $K-Nx\le x$. En intégrant la majoration, on obtient

$$
\left|\frac{1}{x^k}\int_{Nx}^K \psi^{(l)}(t)\,dt\right|
\le \frac{M}{(k+2)!}x^2 .
$$

**La limite demandée vaut $0$.**

> [!JURY]
> Le rapport souligne que l'intégrale qui tend vers zéro est multipliée par un facteur potentiellement divergent. L'estimation doit donc porter sur le quotient complet.

### Question 13

> [!INDICATION]
> Commencer par borner la valeur absolue du reste intérieur.

> [!INDICATION]
> Sur le domaine d'intégration intérieur, majorer la dérivée et intégrer la puissance de $s-t$. Tenir compte de la largeur du second intervalle et du nombre d'intervalles.

#### Solution

Posons $M=\max_{[0,K]}|\psi^{(k+l)}|$. Sur $I_n$, la valeur absolue de l'intégrale intérieure définissant $R_{k,l}$ est majorée par $M(nx-t)^{k+1}/(k+1)!$. En intégrant sur $I_n$ puis en utilisant $Nx\le K$, on obtient

$$
\begin{aligned}
\left|\frac{R_{k,l}(x)}{x^k}\right|
&\le \frac{NMx^{k+2}}{(k+2)!\,x^k}\\
&\le \frac{KM}{(k+2)!}x.
\end{aligned}
$$

**La limite demandée vaut $0$.**

### Question 14

> [!INDICATION]
> Écrire Taylor avec reste intégral pour $\psi^{(l)}$ à l'extrémité droite de chaque intervalle.

> [!INDICATION]
> Après intégration, comparer le noyau du reste et l'ordre de dérivation avec la définition de $R_{k,l}$.

#### Solution

Pour $t\in I_n$, la fonction $\psi^{(l)}$ est de classe $\mathcal C^{p+1}$. Taylor à l'ordre $p$ au point $nx$ donne, après retrait du terme d'ordre zéro,

$$
\begin{aligned}
\psi^{(l)}(t)-\psi^{(l)}(nx)
&=\sum_{k=1}^p \frac{(t-nx)^k}{k!}\psi^{(k+l)}(nx)\\
&\quad+\int_{nx}^t\frac{(t-s)^p}{p!}\psi^{(p+l+1)}(s)\,ds.
\end{aligned}
$$

On intègre sur $I_n$ et on somme. **On obtient l'identité de Q14**, puisque la somme des intégrales des restes est par définition $R_{p,l+1}(x)$.

### Question 15

> [!INDICATION]
> Spécialiser Q14 à $\psi$ et s'arrêter au deuxième ordre.

> [!INDICATION]
> Pour les coefficients de la somme, intégrer séparément les deux monômes après la translation $u=t-nx$.

#### Solution

Dans Q14, on prend $l=0$ et $p=2$.

En posant $u=t-nx$, on intègre $u$ et $u^2/2$ sur $[-x,0]$.

On trouve respectivement $-x^2/2$ et $x^3/6$.

Après division par $x^2$,

$$
\begin{aligned}
\frac1{x^2}\sum_{n=1}^N \int_{I_n}(\psi(t)-\psi(nx))\,dt
&=-\frac12\sum_{n=1}^N\psi'(nx)+\frac{x}{6}\sum_{n=1}^N\psi''(nx)\\
&\quad+\frac{R_{2,1}(x)}{x^2}.
\end{aligned}
$$

> [!METHODE]
> En décalant l'origine en $nx$, les bornes deviennent les mêmes pour tous les termes. Le signe négatif vient de l'intégrale du monôme de degré un sur $[-x,0]$.

### Question 16

> [!INDICATION]
> Dans Q7, choisir l'intégrande de façon à retrouver la somme de $\psi'(nx)$.

> [!INDICATION]
> Vérifier avec Q9 la contribution de l'intégrale complète sur $[0,K]$.

#### Solution

On applique Q7 avec $a=0$, $b=K$ et $f=\psi'$ de classe $\mathcal C^1$. En utilisant $\int_0^K\psi'=0$ par Q9, on obtient

$$
\begin{aligned}
x\sum_{n=1}^N\psi'(nx)&=\sum_{n=1}^N\int_{I_n}(\psi'(nx)-\psi'(t))\,dt\\
&\quad-\int_{Nx}^K\psi'(t)\,dt.
\end{aligned}
$$

### Question 17

> [!INDICATION]
> Développer $\psi'$ au premier ordre par Q14 et l'introduire dans Q16.

> [!INDICATION]
> Comparer l'ordre de la soustraction dans les intégrales des deux questions avant d'effectuer la substitution.

#### Solution

On prend $l=1$ et $p=1$ dans Q14. L'intégrale de $t-nx$ sur $I_n$ vaut $-x^2/2$. La somme d'intégrales figurant en Q16 est l'opposée de celle de Q14. En la substituant puis en divisant par $x$, on obtient

$$
\begin{aligned}
\sum_{n=1}^N\psi'(nx)&=\frac{x}{2}\sum_{n=1}^N\psi''(nx)-\frac{R_{1,2}(x)}x\\
&\quad-\frac1x\int_{Nx}^K\psi'(t)\,dt.
\end{aligned}
$$

### Question 18

> [!INDICATION]
> Utiliser Q17 avant Q15 pour traiter la somme non pondérée des $\psi'(nx)$.

> [!INDICATION]
> Appliquer Q12 et Q13 avec les indices correspondant à chaque reste, puis faire intervenir les sommes pondérées de Q10.

#### Solution

Dans Q17, le premier terme à droite tend vers $-1/2$ d'après Q10.

Le deuxième tend vers zéro d'après Q13 avec $k=1$ et $l=2$, et le dernier d'après Q12 avec $k=l=1$.

Par conséquent $\sum_{n=1}^N\psi'(nx)\longrightarrow-1/2$.

Dans Q15, on applique alors cette limite au premier terme, Q10 au deuxième et Q13 avec $k=2$ et $l=1$ au dernier.

Cela donne

$$
\begin{aligned}
\lim_{x\to0^+}\frac1{x^2}\sum_{n=1}^N\int_{I_n}(\psi(t)-\psi(nx))\,dt
&=\frac14-\frac16\\
&=\boxed{\frac1{12}}.
\end{aligned}
$$

> [!PIEGE]
> La limite nulle de la somme pondérée des $\psi'$ en Q10 ne renseigne pas sur la limite de la somme non pondérée. Q17 fournit l'information d'ordre supérieur nécessaire.

### Question 19

> [!INDICATION]
> Repartir de Q7 avec $\psi$ et isoler la somme pondérée.

> [!INDICATION]
> Exprimer ensuite $\psi(nx)$ à partir de $\varphi(nx)$ pour choisir le bon facteur de division.

#### Solution

On applique Q7 à $\psi$ sur $[0,K]$. On isole $x\sum_{n=1}^N\psi(nx)$, puis on divise par $x^2$ et on utilise $\psi(nx)=nx\varphi(nx)$, ce qui donne

$$
\begin{aligned}
\sum_{n=1}^N n\varphi(nx)
&=\frac1{x^2}\int_0^K\psi(t)\,dt\\
&\quad-\frac1{x^2}\sum_{n=1}^N\int_{I_n}(\psi(t)-\psi(nx))\,dt
-\frac1{x^2}\int_{Nx}^K\psi(t)\,dt.
\end{aligned}
$$

### Question 20

> [!INDICATION]
> Identifier les indices pour lesquels $\varphi(nx)$ s'annule exactement.

> [!INDICATION]
> Dans Q19, distinguer l'intégrale fixe, l'erreur sur les intervalles complets calculée en Q18 et l'intégrale terminale contrôlée par Q12.

#### Solution

Pour $n>N$, on a $nx>K$, donc $\varphi(nx)=0$.

La série est ainsi égale à la somme finie de Q19.

Par Q18 et Q12 (avec $k=2,l=0$), les deux termes soustraits tendent respectivement vers $1/12$ et $0$.

En posant $A=\int_0^K t\varphi(t)\,dt$, on obtient

$$
\boxed{\sum_{n=1}^{+\infty}n\varphi(nx)=\frac{A}{x^2}-\frac1{12}+o(1).}
$$

> [!JURY]
> Le rapport demande à la fois la justification de la troncature exacte et l'identification des résultats qui déterminent le terme constant.

## Partie B — Les sommes infinies au sens de Ramanujan

On combine une relation de dérivation des polynômes de Bernoulli avec une intégration par parties sur chaque intervalle de longueur un. Les identités obtenues à distance finie permettent ensuite de passer à l'infini.

**I — La formule d’Euler-Maclaurin**

### Question 21

> [!INDICATION]
> Intégrer les équations de dérivation successivement. À chaque fois, fixer la constante par l'intégrale sur $[0,1]$.

#### Solution

On intègre $B_1'=1$, puis on fixe la constante par $\int_0^1 B_1=0$. Il vient $B_1(X)=X-1/2$. On intègre ensuite $B_2'=2X-1$, d'où $B_2(X)=X^2-X+c$. La condition d'intégrale nulle donne $c=1/2-1/3=1/6$. Ainsi,

$$
\begin{aligned}
B_1(X)&=X-\frac12\\
B_2(X)&=X^2-X+\frac16.
\end{aligned}
$$

### Question 22

> [!INDICATION]
> Raisonner par récurrence et comparer les dérivées au rang suivant.

> [!INDICATION]
> Pour déterminer la différence constante, intégrer sur $[0,1]$ avec le changement de variable $u=1-t$.

#### Solution

Pour $p=0$, $B_0=1$ vérifie la relation.

Supposons-la vraie au rang $p$ et posons $D(X)=B_{p+1}(1-X)-(-1)^{p+1}B_{p+1}(X)$.

En dérivant et en utilisant l'hypothèse de récurrence, on obtient $D'=0$.

Le changement de variable $u=1-t$ montre que $\int_0^1 D(t)\,dt=0$, car $B_{p+1}$ est d'intégrale nulle.

La constante $D$ est donc nulle.

**Pour tout $p\in\mathbb N$, $B_p(1-X)=(-1)^p B_p(X)$.**

> [!METHODE]
> Des dérivées égales donnent une différence constante. Une condition de moyenne nulle suffit ensuite à identifier cette constante.

### Question 23

> [!INDICATION]
> Exprimer la différence entre valeurs aux bornes par l'intégrale de la dérivée.

> [!INDICATION]
> Pour un indice impair, combiner le résultat aux bornes avec la relation de symétrie de Q22.

#### Solution

Si $p\ge2$, alors $p-1\ge1$ et

$$
B_p(1)-B_p(0)=p\int_0^1 B_{p-1}(t)\,dt=0.
$$

Pour $p\ge3$ impair, Q22 donne $B_p(1)=-B_p(0)$. **On a donc $B_p(1)=b_p$ pour $p\ge2$ et $b_p=0$ pour $p\ge3$ impair.**

### Question 24

> [!INDICATION]
> Sur $[k,k+1[$, remplacer $\widetilde B_p$ par un polynôme en $t-k$.

> [!INDICATION]
> Pour l'intégration par parties, prendre comme primitive le polynôme d'indice suivant divisé par la factorielle adéquate. Calculer ses valeurs aux deux bords.

#### Solution

Sur $[k,k+1[$, on a $\widetilde B_j(t)=B_j(t-k)$.

On peut remplacer $\widetilde B_j$ par ce polynôme dans les intégrales sur $[k,k+1]$, car la valeur au point $k+1$ n'affecte pas l'intégrale.

Le polynôme $B_{p+1}(t-k)/(p+1)!$ est une primitive de $B_p(t-k)/p!$ sur ce segment.

Par intégration par parties,

$$
\begin{aligned}
\int_k^{k+1}\frac{\widetilde B_p(t)}{p!} f^{(p)}(t)\,dt
&=\frac{B_{p+1}(1)f^{(p)}(k+1)-B_{p+1}(0)f^{(p)}(k)}{(p+1)!}\\
&\quad-\int_k^{k+1}\frac{\widetilde B_{p+1}(t)}{(p+1)!} f^{(p+1)}(t)\,dt .
\end{aligned}
$$

> [!JURY]
> Le rapport insiste sur le remplacement de la périodisée par un polynôme sur chaque intervalle. La valeur de bord $B_{p+1}(1)$ vient du polynôme prolongé sur le segment fermé, dont l'intégrale est la même.

### Question 25

> [!INDICATION]
> Partir de Q24 au rang zéro et joindre les intervalles.

> [!INDICATION]
> Compter les demi-contributions aux nœuds intérieurs et aux deux extrémités.

#### Solution

On prend $p=0$ dans Q24 et on somme pour $k=1,\dots,n-1$. D'après Q21, le terme de bord sur $[k,k+1]$ vaut $(f(k+1)+f(k))/2$. Par Chasles,

$$
\int_1^n f(t)\,dt=\sum_{k=1}^{n-1}\frac{f(k+1)+f(k)}{2}-r_{1,n}.
$$

La demi-somme vaut $\sum_{k=1}^n f(k)-(f(1)+f(n))/2$, y compris pour $n=1$. **On en déduit la formule de Q25.**

### Question 26

> [!INDICATION]
> Sommer Q24 sur les intervalles unitaires en exploitant les valeurs de bord de Q23.

> [!INDICATION]
> Grouper deux rangs successifs de la relation entre les restes. Observer l'effet du coefficient de Bernoulli d'indice impair.

#### Solution

Pour tout $j\ge2$, on applique Q24 avec l'indice $p=j-1$, puis on somme de $k=1$ à $n-1$. Les valeurs aux deux extrémités de $B_j$ coïncident par Q23. Les termes de bord se télescopent et donnent

$$
r_{j-1,n}=\frac{b_j}{j!}\bigl(f^{(j-1)}(n)-f^{(j-1)}(1)\bigr)-r_{j,n}.
$$

Pour $l\ge1$, on applique cette identité aux indices $2l$ et $2l+1$. Comme $b_{2l+1}=0$, on obtient

$$
r_{2l-1,n}=\frac{b_{2l}}{(2l)!}\bigl(f^{(2l-1)}(n)-f^{(2l-1)}(1)\bigr)+r_{2l+1,n}.
$$

En sommant de $l=1$ à $p$ et en reportant le résultat dans Q25,

$$
\begin{aligned}
\sum_{k=1}^n f(k)
&=\int_1^n f(t)\,dt+\frac{f(1)+f(n)}2\\
&\quad+\sum_{l=1}^p\frac{b_{2l}}{(2l)!}\bigl(f^{(2l-1)}(n)-f^{(2l-1)}(1)\bigr)+r_{2p+1,n}.
\end{aligned}
$$

> [!METHODE]
> Le télescopage en $k$ consomme les bords intérieurs. Celui en $l$ consomme les restes intermédiaires. Écrire les deux étapes séparément permet de suivre les signes.

**II — La constante de Ramanujan**

### Question 27

> [!INDICATION]
> Pour l'existence de l'intégrale, identifier dans le produit le facteur borné et le facteur intégrable.

> [!INDICATION]
> Pour l'indépendance, comparer les restes d'ordre $2p+1$ et $2p+3$ sur $[1,n]$ avant de passer à la limite. Repérer la dérivée qui intervient en $n$.

#### Solution

Pour $p\ge q$, $\widetilde B_{2p+1}$ est bornée par périodicité et continuité de $B_{2p+1}$ sur $[0,1]$.

Son produit par $f^{(2p+1)}$ est continu par morceaux et absolument intégrable sur $[1,+\infty[$.

Ainsi, $r_{2p+1,n}$ a une limite finie $r_{2p+1,\infty}$ et **$C_p$ est bien définie**, y compris pour $p=0$ si $q=0$.

Par la relation obtenue en Q26 au rang $l=p+1$,

$$
r_{2p+1,n}-r_{2p+3,n}
=\frac{b_{2p+2}}{(2p+2)!}\bigl(f^{(2p+1)}(n)-f^{(2p+1)}(1)\bigr).
$$

On fait tendre $n$ vers l'infini. L'hypothèse $f^{(2p+1)}(n)\to0$ donne

$$
r_{2p+1,\infty}-r_{2p+3,\infty}
=-\frac{b_{2p+2}}{(2p+2)!}f^{(2p+1)}(1).
$$

En reportant dans la différence des définitions de $C_p$ et $C_{p+1}$, les deux termes se compensent. Cette comparaison pour tout $p\ge q$ établit **l'indépendance de $C_p$**.

> [!JURY]
> Le rapport attire l'attention sur le produit intégré. La périodisée est bornée et la dérivée est intégrable par hypothèse. Une dérivée qui tend seulement vers zéro ne suffit pas à conclure.

### Question 28

> [!INDICATION]
> Choisir une même valeur de $p$ pour laquelle le reste des trois polynômes s'annule.

> [!INDICATION]
> Relever le coefficient utile en Q21 et calculer les données de chaque fonction sur $[0,1]$.

#### Solution

Pour $f(t)=1$, $t$ ou $t^2$, toutes les dérivées d'ordre $2p+1$ sont nulles pour $p\ge1$.

On peut donc prendre $q=1$ et calculer $C_1$, dont le reste intégral est nul.

Par Q21, $b_2/2!=1/12$.

La formule à appliquer est

$$
C_1=\frac{f(1)}2-\int_0^1 f(t)\,dt-\frac{f'(1)}{12}.
$$

Pour $1$, les trois contributions valent $1/2$, $-1$ et $0$.

Pour $t$, elles valent $1/2$, $-1/2$ et $-1/12$.

Pour $t^2$, elles valent $1/2$, $-1/3$ et $-1/6$.

On trouve

$$
\begin{aligned}
\sum_{k\ge1}^{R}1&=-\frac12\\
\sum_{k\ge1}^{R}k&=-\frac1{12}\\
\sum_{k\ge1}^{R}k^2&=0.
\end{aligned}
$$

> [!JURY]
> Le rapport attend un rang admissible et le calcul de la constante définie par l'énoncé. Il faut vérifier pourquoi le reste nul correspond bien à un rang où la définition s'applique.

### Question 29

> [!INDICATION]
> Partir de la formule de Q25, puis changer la borne inférieure de l'intégrale par Chasles.

> [!INDICATION]
> Isoler l'expression de Q25 qui devient $C_0$ à la limite. Vérifier quel autre terme disparaît sous les hypothèses de cette question.

#### Solution

Puisque $q=0$, la somme de Ramanujan vaut $C_0$. D'après Q25 et la relation de Chasles,

$$
\sum_{k=1}^n f(k)-\int_0^n f(t)\,dt
=\frac{f(1)+f(n)}2-\int_0^1 f(t)\,dt+r_{1,n}.
$$

Par hypothèse $f(n)\to0$ et, d'après Q27 au rang $0$, $r_{1,n}\to r_{1,\infty}$. Le membre de droite tend donc vers $C_0$, ce qui prouve l'égalité demandée. Si l'intégrale sur $[0,+\infty[$ converge, la suite des sommes partielles converge elle aussi. En passant à la limite,

$$
\boxed{\sum_{k\ge1}^{R}f(k)=\sum_{k=1}^{+\infty}f(k)-\int_0^{+\infty}f(t)\,dt .}
$$

## Partie C — Développements tayloriens généralisés

La condition imposée par la forme linéaire fixe les constantes d'intégration de la famille polynomiale. Une série de fonctions donne la fonction génératrice, puis un reste intégral permet de traiter les sommes alternées.

**I — Les formules de Taylor généralisés**

### Question 30

> [!INDICATION]
> Pour construire $P_{n+1}$, prendre une primitive polynomiale, puis contrôler la constante.

> [!INDICATION]
> Comparer les valeurs de $\varphi$ sur deux primitives qui diffèrent d'une constante.

#### Solution

On part de $P_0=1$.

Si $P_n$ est connu, alors $G_n(X)=(n+1)\int_0^X P_n(s)\,ds$ est un polynôme obtenu en intégrant les monômes de $P_n$.

Tout polynôme de dérivée $(n+1)P_n$ s'écrit $G_n+c$.

Comme $\varphi(1)=1$, $\varphi(G_n+c)=\varphi(G_n)+c$.

L'unique choix qui annule cette valeur est

$$
\boxed{P_{n+1}=G_n-\varphi(G_n).}
$$

On obtient par récurrence l'existence et l'unicité de la suite entière.

### Question 31

> [!INDICATION]
> Reprendre la primitive qui s'annule en zéro et la majorer sur $[0,1]$.

> [!INDICATION]
> Appliquer l'inégalité de continuité à cette primitive pour borner la constante imposée par $\varphi$.

#### Solution

Par continuité de $\varphi$, on choisit $C\ge0$ tel que $|\varphi(g)|\le C\|g\|_\infty$ pour tout $g\in E$.

Pour $x\in[0,1]$, l'intégrale dans $G_n(x)$ est de longueur au plus $1$, donc $\|G_n\|_\infty\le(n+1)\|P_n\|_\infty$.

Par Q30,

$$
\begin{aligned}
\|P_{n+1}\|_\infty
&\le \|G_n\|_\infty+|\varphi(G_n)|\\
&\le \boxed{(n+1)(1+C)\|P_n\|_\infty}.
\end{aligned}
$$

> [!METHODE]
> Évaluer la constante d'intégration via la forme linéaire exploite exactement l'hypothèse de continuité. Une norme uniforme permet ensuite d'obtenir un même majorant en tout point.

### Question 32

> [!INDICATION]
> Itérer l'estimation de Q31 plutôt que de chercher un rapport entre deux coefficients pris en un point.

> [!INDICATION]
> Après division par la factorielle, comparer à une série géométrique par une borne indépendante de $x$.

#### Solution

Comme $\|P_0\|_\infty=1$, Q31 donne par récurrence $\|P_k\|_\infty\le k!(1+C)^k$. Posons $R=1/(1+C)>0$. Si $|t|<R$, alors pour tout $x\in[0,1]$,

$$
\left|\frac{P_k(x)}{k!}t^k\right|\le \bigl((1+C)|t|\bigr)^k .
$$

La série des majorants est géométrique convergente. **Pour chaque $|t|<R$, la série définissant $S$ converge normalement sur $[0,1]$.**

> [!JURY]
> Le rapport met en garde contre la majoration simultanée du numérateur et du dénominateur d'un rapport. Une majoration directe du terme par une puissance géométrique évite cette difficulté.

### Question 33

> [!INDICATION]
> Fixer $t$ et traiter la série comme une série de fonctions de $x$.

> [!INDICATION]
> Dériver le terme d'indice $k\ge1$ puis le comparer au terme d'indice précédent pour contrôler la série dérivée.

#### Solution

Fixons $|t|<R$.

Les termes de la série sont de classe $\mathcal C^1$ et la série converge simplement d'après Q32.

Pour $k\ge1$, le terme dérivé est $t$ fois le terme d'indice $k-1$, puisque $P_k'=kP_{k-1}$.

Par Q32, la série des dérivées converge donc normalement et uniformément sur $[0,1]$.

Le théorème de dérivation des séries de fonctions montre que $x\mapsto S(x,t)$ est de classe $\mathcal C^1$ et donne

$$
\boxed{\frac{\partial S}{\partial x}(x,t)=tS(x,t).}
$$

> [!JURY]
> Le rapport distingue la série entière en $t$ de la série de fonctions que l'on dérive en $x$. Le contrôle des dérivées en $x$ justifie le calcul.

### Question 34

> [!INDICATION]
> Interpréter la relation issue de la dérivation comme une équation différentielle en $x$.

> [!INDICATION]
> Multiplier la fonction par le facteur intégrant approprié.

#### Solution

D'après Q33, la dérivée de $x\mapsto e^{-tx}S(x,t)$ est nulle sur $[0,1]$. Cette fonction est donc constante, de valeur $S(0,t)$. **Il existe ainsi $\alpha(t)=S(0,t)$ tel que $S(x,t)=\alpha(t)e^{tx}$.**

### Question 35

> [!INDICATION]
> Appliquer d'abord $\varphi$ aux sommes partielles et passer à la limite dans la norme de $E$.

> [!INDICATION]
> Reprendre ensuite l'expression de Q34 et isoler $\alpha(t)$ par linéarité.

#### Solution

Par Q32, les sommes partielles convergent vers $S(\cdot,t)$ pour la norme uniforme. La continuité de $\varphi$ et la linéarité donnent

$$
\begin{aligned}
\varphi(S(\cdot,t))&=\lim_{N\to+\infty}\sum_{k=0}^N\frac{t^k}{k!}\varphi(P_k)\\
&=1,
\end{aligned}
$$

car seul le terme de rang $0$ contribue. Par Q34, $\alpha(t)\varphi(x\mapsto e^{tx})=1$. En particulier, le dénominateur est non nul et

$$
\boxed{\alpha(t)=\frac{1}{\varphi(x\mapsto e^{tx})}.}
$$

### Question 36

> [!INDICATION]
> Choisir la forme linéaire dont la normalisation donne les polynômes de Bernoulli.

> [!INDICATION]
> Calculer sa valeur sur l'exponentielle et traiter le point $t=0$ séparément.

#### Solution

La forme $\varphi(g)=\int_0^1g(u)\,du$ est linéaire, vérifie $\varphi(1)=1$ et $|\varphi(g)|\le\|g\|_\infty$.

Elle est donc continue.

Ses polynômes $P_k$ sont exactement les $B_k$ par Q30, ce qui prouve leur existence et leur unicité.

Pour $t\ne0$, $\int_0^1 e^{tu}\,du=(e^t-1)/t$, tandis que l'intégrale vaut $1$ pour $t=0$.

D'après Q32, Q34 et Q35, sur $]-R,R[$ la série entière converge et sa somme vaut

$$
\boxed{
\sum_{k=0}^{+\infty}\frac{B_k(x)}{k!}t^k=
\begin{cases}
\dfrac{te^{tx}}{e^t-1}, & t\ne0,\\[4pt]
1, & t=0 .
\end{cases}}
$$

### Question 37

> [!INDICATION]
> Nommer le reste intégral et essayer de diminuer l'ordre de la dérivée de $f$ par intégration par parties.

> [!INDICATION]
> Évaluer le noyau aux deux bornes et utiliser sa dérivée en $t$ pour faire réapparaître le reste d'ordre précédent.

#### Solution

Pour $x,y\in\mathbb R$ et $p\ge0$, posons

$$
J_p(x,y)=\int_y^x\frac{P_p(x+y-t)}{p!}f^{(p+1)}(t)\,dt.
$$

Comme $P_0=1$, $J_0(x,y)=f(x)-f(y)$.

Pour $p\ge1$, une intégration par parties entre $y$ et $x$ donne, en utilisant $P_p'=pP_{p-1}$ et la dérivée de $x+y-t$,

$$
J_p(x,y)=\frac{P_p(y)}{p!}f^{(p)}(x)-\frac{P_p(x)}{p!}f^{(p)}(y)+J_{p-1}(x,y).
$$

On somme ces différences de $1$ à $p$ et on remplace $J_0$ par $f(x)-f(y)$. En isolant $f(x)$,

$$
\begin{aligned}
f(x)
&=f(y)+\sum_{k=1}^p\left(\frac{P_k(x)}{k!}f^{(k)}(y)-\frac{P_k(y)}{k!}f^{(k)}(x)\right)\\
&\quad+\int_y^x\frac{P_p(x+y-t)}{p!}f^{(p+1)}(t)\,dt .
\end{aligned}
$$

La somme est vide pour $p=0$, et les intégrales restent orientées quand $x<y$.

> [!METHODE]
> Nommer un reste et le ramener au rang précédent isole le calcul délicat de l'intégration par parties. Vérifier le signe de la dérivée du noyau et l'ordre des bornes.

### Question 38

> [!INDICATION]
> Voir les deux membres de Q37 comme des fonctions de $y$ avant de leur appliquer $\varphi$.

> [!INDICATION]
> Développer le noyau polynomial en puissances de $t$ pour justifier la continuité du reste à borne variable.

#### Solution

Fixons $x$.

Tous les termes de Q37 sont continus en $y$ sur $[0,1]$.

Pour le reste $J_p(x,y)$, on peut développer le polynôme $P_p(x+y-t)$ en puissances de $t$, à coefficients polynomiaux en $y$.

Chaque intégrale résultante de $t^j f^{(p+1)}(t)$ entre $y$ et $x$ est continue en $y$ par le théorème fondamental de l'analyse.

On applique donc $\varphi$ à Q37.

Elle conserve $f(x)$, constant en $y$, et annule chaque $P_k(y)$ pour $k\ge1$.

Ainsi,

$$
\boxed{
f(x)=\sum_{k=0}^p\frac{P_k(x)}{k!}\varphi(y\mapsto f^{(k)}(y))
+\varphi\bigl(y\mapsto J_p(x,y)\bigr).}
$$

### Question 39

> [!INDICATION]
> Comparer la valeur absolue d'une évaluation à la norme uniforme.

> [!INDICATION]
> Déterminer par récurrence les polynômes qui vérifient la normalisation en zéro, puis revenir à Q38.

#### Solution

L'évaluation en $0$ est linéaire et $|g(0)|\le\|g\|_\infty$, donc elle est continue sur $E$.

Ici $P_n(0)=0$ pour $n\ge1$.

Partant de $P_0=1$, la relation $P_n'=nP_{n-1}$ donne par récurrence $P_n(X)=X^n$.

En évaluant les fonctions de $y$ en $0$ dans Q38, on retrouve la formule de Taylor à l'origine avec reste intégral,

$$
\boxed{f(x)=\sum_{k=0}^p\frac{x^k}{k!}f^{(k)}(0)+\int_0^x\frac{(x-t)^p}{p!}f^{(p+1)}(t)\,dt.}
$$

### Question 40

> [!INDICATION]
> Appliquer Q38 à la translatée proposée au point qui fait réapparaître $f(j)$.

> [!INDICATION]
> Dans le reste, déplacer les bornes par changement de variable, puis regarder le sens de l'intégrale.

#### Solution

On applique Q38 en $x=0$ à $F_j:u\mapsto f(u+j)$, de classe $\mathcal C^\infty$ sur $\mathbb R$.

Pour le reste, le changement de variable $t=u+j$ transforme l'intégrale entre $y$ et $0$ en une intégrale entre $y+j$ et $j$.

En inversant les bornes,

$$
\begin{aligned}
f(j)
&=\sum_{k=0}^p\frac{P_k(0)}{k!}\varphi(y\mapsto f^{(k)}(y+j))\\
&\quad-\varphi\left(y\mapsto \int_j^{y+j}\frac{P_p(y+j-t)}{p!}f^{(p+1)}(t)\,dt\right).
\end{aligned}
$$

### Question 41

**II — Formule d’Euler-Boole**

> [!INDICATION]
> Vérifier que la nouvelle forme satisfait les hypothèses de Q30–Q35.

> [!INDICATION]
> Évaluer la fonction exponentielle en chacun des deux points utilisés par la forme.

#### Solution

La demi-somme des évaluations en $0$ et $1$ est linéaire, vaut $1$ sur la constante $1$ et vérifie $|\varphi(g)|\le\|g\|_\infty$.

Q32, Q34 et Q35 s'appliquent avec $\varphi(x\mapsto e^{tx})=(1+e^t)/2$.

**Il existe $R>0$ tel que**, pour tout $x\in[0,1]$ et $|t|<R$,

$$
\boxed{\sum_{k=0}^{+\infty}\frac{E_k(x)}{k!}t^k=\frac{2e^{tx}}{1+e^t}.}
$$

### Question 42

> [!INDICATION]
> Remplacer $x$ par $1-x$ dans Q41, puis comparer avec un changement de signe de $t$.

> [!INDICATION]
> Une fois les coefficients identifiés sur $[0,1]$, utiliser l'identité polynomiale.

#### Solution

Pour $x\in[0,1]$, l'expression de Q41 en $(1-x,t)$ coïncide avec son expression en $(x,-t)$, car

$$
\frac{2e^{t(1-x)}}{1+e^t}=\frac{2e^{-tx}}{1+e^{-t}}.
$$

L'unicité des coefficients d'une série entière donne $E_n(1-x)=(-1)^nE_n(x)$ sur $[0,1]$. Les deux polynômes coïncident sur une infinité de points, donc **$E_n(1-X)=(-1)^nE_n(X)$**.

### Question 43

> [!INDICATION]
> Dans Q40, calculer séparément les contributions aux deux évaluations, notamment les longueurs d'intégration.

> [!INDICATION]
> Utiliser Q42 pour changer l'argument du polynôme d'Euler dans l'intégrale non nulle.

#### Solution

On applique Q40 à la demi-somme des évaluations aux deux extrémités. Dans le reste, le terme en $y=0$ est nul, et pour $y=1$, Q42 donne $E_p(1-(t-j))=(-1)^pE_p(t-j)$. On obtient

$$
\begin{aligned}
f(j)
&=\frac12\sum_{k=0}^p\frac{e_k}{k!}\bigl(f^{(k)}(j)+f^{(k)}(j+1)\bigr)\\
&\quad-\frac12\int_j^{j+1}\frac{(-1)^p E_p(t-j)}{p!}f^{(p+1)}(t)\,dt.
\end{aligned}
$$

### Question 44

> [!INDICATION]
> Alterner les signes dans Q43 avant de sommer sur les intervalles unitaires.

> [!INDICATION]
> Pour le reste, vérifier que le signe de Q43 et celui de la sommation donnent bien le facteur de $\widetilde E_p$ sur chaque intervalle.

#### Solution

Pour $j=1,\dots,n$, on multiplie Q43 par $(-1)^{j-1}$ et on somme.

Pour chaque $k$, les coefficients de $f^{(k)}(j)$ se compensent pour $2\le j\le n$.

Il reste les contributions en $1$ et $n+1$, de signes respectifs $+$ et $(-1)^{n-1}$.

Dans le reste, pour $t\in[j,j+1[$, on a $\lfloor t\rfloor=j$ et $-(-1)^{j-1}(-1)^p E_p(t-j)=\widetilde E_p(t)$.

Cette fonction est continue par morceaux sur le segment et les valeurs aux entiers n'affectent pas les intégrales.

Par Chasles,

$$
\begin{aligned}
\sum_{j=1}^n(-1)^{j-1}f(j)
&=\frac12\sum_{k=0}^p\frac{e_k}{k!}f^{(k)}(1)\\
&\quad+\frac{(-1)^{n-1}}2\sum_{k=0}^p\frac{e_k}{k!}f^{(k)}(n+1)\\
&\quad+\frac12\int_1^{n+1}\frac{\widetilde E_p(t)}{p!}f^{(p+1)}(t)\,dt.
\end{aligned}
$$

> [!PIEGE]
> Les valeurs aux nœuds intérieurs s'annulent dans les termes de bord seulement. Le reste sur chaque intervalle garde sa contribution avec un signe inclus dans la fonction prolongée.

## Bilan

- Pour déterminer un terme constant après division par $x^2$, conserver un reste d'ordre suffisant avant la division.
- Pour une somme approchant une intégrale, séparer les écarts sur les intervalles complets de l'intégrale terminale. Appliquer ensuite les bornes avec le nombre effectif d'intervalles.
- Pour une fonction périodisée définie sur un intervalle semi-ouvert, travailler avec le polynôme translaté sur chaque segment avant l'intégration par parties.
- Pour une série de fonctions, vérifier les hypothèses dans la variable effectivement dérivée. La normalisation par une forme linéaire continue se transmet à la somme grâce à la convergence uniforme.
- Refaire Q3–Q4 et Q23–Q26 pour travailler les règles de convergence et les termes de bord. Reprendre Q30–Q35 pour s'entraîner à construire une série génératrice à partir d'une relation de dérivation.
