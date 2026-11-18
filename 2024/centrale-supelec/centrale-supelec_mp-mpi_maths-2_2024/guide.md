# Centrale-Supélec MP/MPI — Mathématiques 2 2024 · Corrigé guidé

*Corrigé rédigé par IA, non officiel. Signalez toute erreur.*

## Présentation du sujet

L'épreuve commune MP/MPI dure quatre heures et compte vingt-neuf questions. Elle étudie l'équation de différence finie $f(x+1)-f(x)=h(x)$ pour une fonction polynomiale, puis pour une fonction entière, c'est-à-dire développable en série entière de rayon infini.

La partie I utilise le degré et le théorème du rang pour classer les solutions polynomiales. La partie II montre comment retrouver un coefficient de série entière en intégrant sur le cercle unité. La partie III applique cette méthode aux polynômes de Bernoulli et relie ces polynômes aux dérivées d'une fonction à deux variables. La partie IV change le rayon du cercle d'intégration avec le rang. Ce choix permet de construire une solution entière pour un second membre quelconque de rayon infini.

Les questions Q1–Q8, Q10, Q15 et Q21 sont des points d'entrée abordables. En Q9, Q13, Q14 et Q26, distinguez l'indice de série, la variable d'intégration et les paramètres fixés avant de choisir un majorant. La dernière partie demande un contrôle uniforme des dénominateurs, puis une preuve de sommabilité. Sur quatre heures, on peut réserver 35 minutes à I, 45 à II, 1 h 20 à III, 1 h 05 à IV et 15 minutes à la relecture.

## I — Étude de l’opérateur différence finie

Le degré donne une information sur le noyau et sur l'image en dimension finie. Il permet ensuite de revenir à l'espace de tous les polynômes.

### Question 1

> [!INDICATION]
> Vérifiez que la substitution dans un polynôme conserve la nature de l'objet et que la même opération commute aux combinaisons linéaires.

#### Solution

La substitution $X\mapsto X+1$ transforme tout polynôme en polynôme et commute aux combinaisons linéaires. La différence entre cette substitution et l’identité est donc **un endomorphisme de $\mathbb K[X]$**.

### Question 2

> [!INDICATION]
> Appliquez le binôme à chaque monôme. Repérez les deux premiers termes du développement de $(X+1)^m$ pour l'exposant dominant.

> [!INDICATION]
> Traitez les constantes séparément et expliquez pourquoi les monômes de degré inférieur ne peuvent annuler le coefficient dominant obtenu.

#### Solution

Si $P$ est constant, y compris nul, $\Delta(P)=0$ et $\deg\Delta(P)=-\infty$ avec la convention usuelle. Si $P$ est de degré $m\geq1$ et de coefficient dominant $a_m$, le binôme donne
$$
(X+1)^m-X^m=mX^{m-1}+\sum_{j=0}^{m-2}\binom mj X^j .
$$
Les termes de $P$ de degré strictement inférieur à $m$ donnent, après application de $\Delta$, des termes de degré au plus $m-2$ ou le polynôme nul. Comme $ma_m\ne0$, **$\deg\Delta(P)=m-1$**.

> [!JURY]
> Les rapports demandent d'exclure l'annulation du coefficient de plus haut degré. La différence du seul monôme dominant produit ce coefficient, les autres différences étant de degré inférieur.

### Question 3

> [!INDICATION]
> Utilisez la borne de degré de Q2 comme une propriété de stabilité de l'espace de départ.

#### Solution

Par Q2, pour $d\geq1$, l’image d’un polynôme de $\mathbb K_d[X]$ appartient à $\mathbb K_{d-1}[X]$. Elle appartient donc à $\mathbb K_d[X]$. **La restriction $\Delta_d$ est un endomorphisme de cet espace.**

### Question 4

> [!INDICATION]
> Pour le noyau, repérez quels degrés peuvent donner une différence nulle.

> [!INDICATION]
> Pour l'image, associez une inclusion donnée par Q2 à une égalité de dimensions obtenue par le théorème du rang.

#### Solution

Q2 montre que **$\ker\Delta_d=\mathbb K_0[X]$**. Par le théorème du rang, l’image a pour dimension $(d+1)-1=d$. Elle est incluse dans $\mathbb K_{d-1}[X]$, de même dimension. Ainsi **$\operatorname{Im}\Delta_d=\mathbb K_{d-1}[X]$**.

> [!JURY]
> Les rapports insistent sur le théorème du rang et sur la caractérisation des polynômes de différence nulle. L'argument par le degré s'applique sur les deux corps du sujet.

### Question 5

> [!INDICATION]
> Pour une fonction polynomiale fixée, choisissez un espace de dimension finie dans lequel Q4 donne un antécédent.

> [!INDICATION]
> Comparez deux antécédents par soustraction et utilisez le noyau déjà calculé.

#### Solution

D’après Q2, **$\ker\Delta=\mathbb K_0[X]$**. Pour tout polynôme $H$ de degré $m\geq0$, Q4 appliquée à $d=m+1$ donne un antécédent de $H$. Le polynôme nul admet aussi un antécédent. On a donc **$\operatorname{Im}\Delta=\mathbb K[X]$**.

Si $h$ est la fonction associée à $H$, un polynôme $P_0$ tel que $\Delta(P_0)=H$ donne une solution de $(E_h)$.

Comme $\mathbb K$ est infini, l’identité de fonctions polynomiales équivaut à celle de leurs polynômes.

Toute autre solution polynomiale diffère de $P_0$ d’un élément de $\ker\Delta$.

Réciproquement, ajouter une constante laisse la différence inchangée.

**Les solutions polynomiales sont les $P_0+c$ avec $c\in\mathbb K$.**

> [!METHODE]
> Une fois le second membre fixé, il suffit de travailler dans une seule dimension finie choisie selon son degré.

### Question 6

> [!INDICATION]
> Cherchez un polynôme de degré deux et comparez les coefficients de sa différence avec ceux du monôme donné. Réutilisez ensuite le noyau.

#### Solution

Pour $P_0(X)=X(X-1)/2$, le calcul donne
$$
P_0(X+1)-P_0(X)=\tfrac12 X\bigl((X+1)-(X-1)\bigr)=X.
$$
Par Q5, **les solutions polynomiales sont $P_0+c$, avec $c\in\mathbb K$**.

### Question 7

> [!INDICATION]
> Comptez le nombre d'applications nécessaire pour faire disparaître un polynôme de degré au plus donné.

> [!INDICATION]
> Si l'endomorphisme s'écrivait dans une base propre, que deviendrait une diagonale dont une puissance est nulle ? Testez aussi son action sur un monôme.

#### Solution

Chaque application de $\Delta_d$ abaisse le degré d’au moins une unité jusqu’à annulation.

Ainsi $\Delta_d^{\,d+1}=0$ et **$X^{d+1}$ est annulateur**.

Toute valeur propre $\lambda$ vérifierait $\lambda^{d+1}=0$.

Si $\Delta_d$ était diagonalisable, sa diagonale serait donc nulle.

Or $\Delta_d(X)=1$ pour $d\geq1$.

**$\Delta_d$ n’est pas diagonalisable.**

> [!JURY]
> Le rapport demande de justifier le lien entre nilpotence et diagonalisabilité. La diagonale d'un endomorphisme nilpotent ne pourrait contenir que des zéros.

## II — Fonctions entières

Les fonctions exponentielles sur le cercle unité isolent les coefficients d'une série. La majoration géométrique d'un inverse fournit une première application de cette extraction.

### II.A — Généralités


### Question 8

> [!INDICATION]
> À variable complexe fixée, utilisez les propriétés des séries absolument convergentes et donnez les coefficients du produit de Cauchy.

#### Solution

Écrivons $f(z)=\sum_{n\geq0}a_nz^n$ et $g(z)=\sum_{n\geq0}b_nz^n$. Pour tout $z$, les deux séries convergent absolument. Leur combinaison linéaire est représentée par la série de coefficients $\lambda a_n+\mu b_n$, absolument convergente pour tout $z$.

Le théorème du produit de Cauchy des séries absolument convergentes donne
$$
f(z)g(z)=\sum_{n\geq0}\left(\sum_{j=0}^{n}a_jb_{n-j}\right)z^n .
$$
La série est absolument convergente pour tout $z$, donc son rayon est infini. **$\lambda f+\mu g$ et $fg$ appartiennent à $\mathcal E$.**

> [!JURY]
> Les rapports attendent la définition du produit de Cauchy et la justification de sa convergence. En général, la borne sur le rayon du produit est une minoration.

### Question 9

> [!INDICATION]
> Développez l'intégrande et fixez l'indice $k$. Cherchez un majorant du terme indépendant du point du cercle.

> [!INDICATION]
> Calculez séparément l'intégrale pour une fréquence nulle et pour une fréquence entière non nulle.

#### Solution

Pour $k$ fixé, l’intégrande est la somme des fonctions continues $t\mapsto a_n e^{2\mathrm i\pi(n-k)t}$. Chacune est majorée en module par $|a_n|$ sur $[0,1]$. La série de ces majorants converge, par convergence absolue de la série entière au point $1$. La convergence normale autorise l’intégration terme à terme.

Pour $m\in\mathbb Z$, l’intégrale sur $[0,1]$ de $e^{2\mathrm i\pi mt}$ vaut $1$ si $m=0$.

Si $m\ne0$, la primitive $e^{2\mathrm i\pi mt}/(2\mathrm i\pi m)$ a les mêmes valeurs aux bornes et l’intégrale vaut $0$.

On obtient
$$
\boxed{\int_0^1 f(\omega(t))\omega(t)^{-k}\,\mathrm dt
=\begin{cases}
a_k & \text{si }k\geq0,\\
0 & \text{si }k<0.
\end{cases}}
$$

> [!JURY]
> Le rapport demande d'identifier la suite des fonctions à intégrer et la majoration qui autorise l'interversion. Il distingue aussi explicitement les cas de fréquence nulle et non nulle.

### II.B — Une intégrale


### Question 10

> [!INDICATION]
> Déterminez quels modules peuvent avoir les zéros de l'exponentielle moins un. Vérifiez aussi que les puissances négatives du numérateur sont définies.

#### Solution

Les zéros de $e^z-1$ sont les $2\mathrm i\pi k$ avec $k\in\mathbb Z$.

Aucun n’a pour module $1$.

Comme $\omega(t)$ a module $1$, le dénominateur est partout non nul et toutes les puissances entières de $\omega(t)$ sont continues.

**L’intégrande est continue sur $[0,1]$ et $I_p$ est bien définie.**

> [!JURY]
> Le rapport relève une confusion entre les exponentielles réelle et complexe. Dans le plan complexe, le dénominateur a une infinité de zéros, dont aucun n'est sur le cercle unité.

### Question 11

> [!INDICATION]
> Dans la série de l'exponentielle, retirez les termes constant et linéaire avant de factoriser.

> [!INDICATION]
> Sur le cercle unité, comparez la série des modules à une série géométrique et repérez une inégalité stricte.

#### Solution

Posons $\beta(z)=\sum_{j\geq0} z^j/(j+2)!$. Cette série entière a un rayon infini et, en regroupant les termes de l’exponentielle,
$$
e^z-1=z\bigl(1+z\beta(z)\bigr).
$$
Si $|\zeta|=1$, alors
$$
|\beta(\zeta)|\leq\sum_{j\geq0}\frac1{(j+2)!}.
$$
Pour $j\geq0$, $(j+2)!\geq 2^{j+1}$, avec inégalité stricte dès $j\geq1$. La somme des majorants $2^{-j-1}$ vaut $1$, et l’inégalité stricte sur au moins un terme donne **$C=\sum_{j\geq0}1/(j+2)!\in]0,1[$**, ce qui convient.

### Question 12

> [!INDICATION]
> Réécrivez l'inverse du facteur donné en Q11 comme la somme d'une série géométrique. Vérifiez le module de sa raison.

#### Solution

Sur $\mathbb U$, $|\zeta\beta(\zeta)|\leq C<1$. La série géométrique de raison $-\zeta\beta(\zeta)$ est donc convergente et sa somme vaut $(1+\zeta\beta(\zeta))^{-1}$. Avec la factorisation de Q11 et $\zeta\ne0$, on obtient
$$
\boxed{\frac{\zeta^p}{e^\zeta-1}
=\sum_{j=0}^{\infty}(-1)^j\zeta^{j+p-1}\beta(\zeta)^j.}
$$
Pour chaque $p\in\mathbb Z$, le module du terme de rang $j$ est au plus $C^j$ sur $\mathbb U$.

> [!METHODE]
> Après factorisation, le contrôle strict du module donne la formule géométrique et une domination uniforme. Cette seconde information permet de l'intégrer à la question suivante.

### Question 13

> [!INDICATION]
> Appliquez Q12 à la puissance qui figure dans l'intégrale. Cherchez une domination par une série géométrique pour permuter somme et intégrale.

> [!INDICATION]
> Pour chaque intégrale obtenue, utilisez Q9 à la fréquence zéro et examinez le coefficient constant.

#### Solution

Pour $p\geq0$, appliquons Q12 à $\zeta=\omega(t)$ et à l’exposant $p+1$. Les termes continus sont majorés par $C^j$ sur $[0,1]$. La convergence normale donne
$$
I_p=\sum_{j=0}^{\infty}(-1)^j
 \int_0^1\omega(t)^{j+p}\beta(\omega(t))^j\,\mathrm dt.
$$
La fonction $z\mapsto z^{j+p}\beta(z)^j$ appartient à $\mathcal E$ par Q8.

Par Q9 au rang $0$, son intégrale ci-dessus vaut son coefficient constant.

Ce coefficient vaut $1$ pour $j=p=0$, et $0$ dans tous les autres cas.

Ainsi **$I_0=1$ et $I_p=0$ pour $p\geq1$**.

## III — Polynômes de Bernoulli

L'expression intégrale et l'expression polynomiale jouent des rôles différents. On choisit l'une ou l'autre selon que l'on dérive ou que l'on étudie une différence finie.

### III.A — Lien avec l’équation $(E_h)$


### Question 14

> [!INDICATION]
> Développez l'exponentielle en série pour un paramètre fixé. Le module du dénominateur est continu et ne s'annule pas sur le segment.

> [!INDICATION]
> Identifiez l'intégrale associée à chaque puissance du paramètre et utilisez les annulations de Q13.

#### Solution

Sur $[0,1]$, la fonction positive $t\mapsto|e^{\omega(t)}-1|$ admet un minimum $\delta>0$, par Q10 et compacité.

Fixons $n\geq0$ et $z\in\mathbb C$.

Après développement de $e^{z\omega(t)}$, les termes continus de l’intégrande sont majorés par $|z|^k/(\delta k!)$.

La convergence normale permet l’intégration terme à terme et donne
$$
B_n(z)=n!\sum_{k=0}^{\infty}\frac{z^k}{k!}I_{k-n}.
$$
Par Q13, les termes $k>n$ sont nuls et $I_0=1$. Ainsi,
$$
\boxed{B_n(z)=n!\sum_{k=0}^n\frac{z^k}{k!}I_{k-n}.}
$$
Le coefficient de $z^n$ est $1$. **$B_n$ est un polynôme unitaire de degré $n$.**

> [!METHODE]
> Lorsque le paramètre $z$ est fixé, un minorant uniforme du module du dénominateur sur le trajet suffit pour exploiter la série exponentielle.

### Question 15

> [!INDICATION]
> Dérivez l'expression polynomiale de Q14, puis abaissez l'indice de sommation d'une unité.

#### Solution

On dérive le polynôme de Q14 puis on pose $j=k-1$.
$$
\begin{aligned}
B'_n(z)&=n!\sum_{k=1}^{n}\frac{z^{k-1}}{(k-1)!}I_{k-n}\\
&=\boxed{n B_{n-1}(z)}.
\end{aligned}
$$

> [!JURY]
> Le rapport analyse l'intérêt de dériver l'expression polynomiale. La dérivation sous l'intégrale en un paramètre complexe n'est pas un théorème du programme.

### Question 16

> [!INDICATION]
> Utilisez les deux expressions intégrales de la différence. Cherchez quel facteur se simplifie après avoir soustrait les exponentielles.

> [!INDICATION]
> Appliquez ensuite Q9 à l'exponentielle pour lire le coefficient qui reste.

#### Solution

Dans l’expression intégrale de la différence, on factorise $e^{(z+1)\omega(t)}-e^{z\omega(t)}$ par $e^{\omega(t)}-1$. On obtient
$$
B_n(z+1)-B_n(z)
=n!\int_0^1 e^{z\omega(t)}\omega(t)^{-(n-1)}\,\mathrm dt.
$$
La fonction $w\mapsto e^{zw}$ est entière, et son coefficient de rang $n-1$ vaut $z^{n-1}/(n-1)!$. Q9 donne donc **$B_n(z+1)-B_n(z)=n z^{n-1}$**.

### Question 17

> [!INDICATION]
> Pour chaque monôme du second membre, choisissez le polynôme de Bernoulli dont la différence a le degré voulu, puis ajustez le coefficient.

#### Solution

Si $h(z)=\sum_{k=0}^m h_k z^k$, Q16 donne, par linéarité, la solution polynomiale
$$
\boxed{f(z)=\sum_{k=0}^m \frac{h_k}{k+1} B_{k+1}(z).}
$$
En effet, le terme de rang $k$ a pour différence finie $h_k z^k$. Pour $h=0$, la solution nulle convient.

### III.B — Unicité


### Question 18

> [!INDICATION]
> Pour vérifier la condition intégrale, cherchez une primitive parmi les polynômes de Bernoulli et calculez sa différence entre les deux bornes.

> [!INDICATION]
> Pour l'unicité, supposez deux suites égales au rang précédent et examinez la dérivée et l'intégrale de leur différence au rang courant.

#### Solution

Q14 donne $B_0=1$ et Q15 donne la condition de dérivation. Pour $n\geq1$, Q15 appliquée à $n+1$, puis Q16 en $z=0$, donnent
$$
\begin{aligned}
\int_0^1 B_n(t)\,\mathrm dt
&=\frac{B_{n+1}(1)-B_{n+1}(0)}{n+1}\\
&=0.
\end{aligned}
$$
Les trois conditions sont donc satisfaites.

Soit $(P_n)$ une autre suite satisfaisant ces conditions. On a $P_0=B_0$. Si $P_{n-1}=B_{n-1}$ pour $n\geq1$, alors $(P_n-B_n)'=0$, donc la différence est constante. Comme son intégrale sur $[0,1]$ est nulle, cette constante est nulle. **La récurrence établit l’unicité.**

> [!JURY]
> Le rapport demande de vérifier séparément l'existence et l'unicité. Dans l'unicité, l'intégrale nulle fixe une constante obtenue par dérivation.

### Question 19

> [!INDICATION]
> Vérifiez les trois conditions de Q18 après composition par la symétrie du segment. Suivez le signe de la dérivée et celui du changement de variable.

#### Solution

On a $H_0=1$. Pour $n\geq1$, la dérivation de la composée et Q15 donnent
$$
\begin{aligned}
H'_n(X)&=(-1)^{n+1}n B_{n-1}(1-X)\\
&=nH_{n-1}(X).
\end{aligned}
$$
Le changement de variable $s=1-t$ montre que $\int_0^1H_n(t)\,\mathrm dt=(-1)^n\int_0^1 B_n(s)\,\mathrm ds=0$. Par unicité en Q18, **$H_n=B_n$ pour tout $n$**.

### III.C — Une application analytique


### Question 20

> [!INDICATION]
> À l'origine, étudiez l'inverse du quotient qui définit la fonction prolongée. Écrivez cet inverse comme une série entière.

> [!INDICATION]
> Une fois la régularité à une variable établie, utilisez un produit et une composition de fonctions de plusieurs variables.

#### Solution

La fonction $v(x)=\sum_{j\geq0} x^j/(j+1)!$ est de classe $\mathcal C^\infty$ sur $\mathbb R$, comme somme d’une série entière de rayon infini.

Elle vaut $(e^x-1)/x$ pour $x\ne0$ et $1$ en $0$.

Elle est strictement positive, puisque l’exponentielle est strictement croissante sur $\mathbb R$.

Ainsi $\psi=1/v$ est de classe $\mathcal C^\infty$ sur $\mathbb R$.

La fonction $(x,t)\mapsto tx$ est polynomiale et l’exponentielle est de classe $\mathcal C^\infty$.

Par composition et produit, **$u$ est de classe $\mathcal C^\infty$ sur $\mathbb R^2$**.

> [!JURY]
> Les rapports rappellent que la régularité séparée en chaque variable ne suffit pas. La fonction est construite ici par composition et produit de fonctions globalement régulières.

### Question 21

> [!INDICATION]
> Dérivez d'abord par le paramètre qui apparaît linéairement dans l'exposant. Pour obtenir l'autre identité, permutez les dérivations puis utilisez Leibniz.

#### Solution

Pour tout $(x,t)$, **$\partial_t u(x,t)=xu(x,t)$**.

Comme $u$ est de classe $\mathcal C^\infty$, le théorème de Schwarz permet de permuter $\partial_t$ et $\partial_x^n$.

Par la formule de Leibniz, toutes les dérivées en $x$ de l’ordre au moins deux du facteur $x$ sont nulles.

Il reste
$$
\boxed{\partial_t\partial_x^n u(x,t)
=x\partial_x^n u(x,t)+n\partial_x^{n-1}u(x,t).}
$$

### Question 22

> [!INDICATION]
> Évaluez Q21 en zéro et montrez par récurrence que les fonctions obtenues sont polynomiales.

> [!INDICATION]
> Calculez d'abord l'intégrale de $u$ en la seconde variable. Justifiez la dérivation de cette intégrale avant de prendre la valeur en zéro.

#### Solution

On a $A_0(t)=u(0,t)=1$. En $x=0$, Q21 donne $A'_n=nA_{n-1}$ pour $n\geq1$. Par récurrence, chaque $A_n$ est un polynôme, car une primitive d’un polynôme diffère d’une primitive polynomiale par une constante.

Pour $x\ne0$, on calcule
$$
\begin{aligned}
\int_0^1u(x,t)\,\mathrm dt&=\psi(x)\frac{e^x-1}{x}\\
&=1 .
\end{aligned}
$$
Cette intégrale vaut aussi $1$ en $x=0$.

Sur chaque rectangle compact en $(x,t)$ avec $t\in[0,1]$, toutes les dérivées partielles en $x$ sont continues et bornées par des constantes intégrables en $t$.

Les hypothèses du théorème de dérivation sous l’intégrale sont donc vérifiées à tout ordre, localement en $x$.

En dérivant à l’ordre $n\geq1$ et en prenant $x=0$, on trouve $\int_0^1 A_n(t)\,\mathrm dt=0$.

Les trois conditions de Q18 sont ainsi satisfaites. **$A_n=B_n$ pour tout $n$**.

> [!PIEGE]
> L'égalité de la moyenne de $u$ à une constante fournit la normalisation après dérivation. Il faut contrôler les dérivées en $x$ sur le segment d'intégration pour justifier ce passage.

## IV — Solution entière de l’équation $(E_h)$

On cherche des antécédents entiers de monômes qui ne croissent pas trop vite avec leur indice. La propriété de minoration du dénominateur sert à obtenir cette borne sur des cercles de rayons différents.

### IV.A — Une inégalité de contrôle


### Question 23

> [!INDICATION]
> Niez les quantificateurs de la propriété dans leur ordre. Choisissez ensuite une suite de seuils positifs qui tend vers zéro.

#### Solution

Nier $\mathcal P$ signifie que, pour tout $c>0$, il existe un entier naturel $n$ et un complexe $z$ tels que
$$
\begin{aligned}
|z|&=(2n+1)\pi,\\
|e^z-1|&<c.
\end{aligned}
$$
Pour chaque $p\geq0$, choisissons un tel couple $(n_p,z_p)$ avec $c=1/(p+1)$. **Les $z_p$ ont les modules imposés et $e^{z_p}\to1$.**

### Question 24

> [!INDICATION]
> Prenez le module de l'exponentielle complexe pour contrôler la partie réelle.

> [!INDICATION]
> Comparez ensuite les normes du complexe et de sa seule partie imaginaire avec l'inégalité triangulaire inversée.

#### Solution

On a $e^{a_p}=|e^{z_p}|\to1$, et le logarithme est continu en $1$. Ainsi **$a_p\to0$**. Comme $|b_p|=|\mathrm ib_p|$, l’inégalité triangulaire inversée donne
$$
0\leq |z_p|-|b_p|\leq |a_p|.
$$
Le majorant tend vers zéro, donc **$|z_p|-|b_p|\to0$**.

> [!JURY]
> Le rapport met en garde contre l'usage d'une réciproque globale de l'exponentielle complexe. Le module ramène la première limite à l'exponentielle réelle.

### Question 25

> [!INDICATION]
> Avec Q24, examinez d'abord la limite de l'argument de l'exponentielle proposée.

> [!INDICATION]
> Factorisez ensuite cette exponentielle et utilisez le caractère impair du multiple de $\pi$.

#### Solution

Puisque $b_p=\varepsilon_p|b_p|$, on a
$$
z_p-\mathrm i\varepsilon_p|z_p|
=a_p+\mathrm i\varepsilon_p\bigl(|b_p|-|z_p|\bigr)\longrightarrow0
$$
par Q24. Son exponentielle tend donc vers $1$.

Or $|z_p|$ est un multiple impair de $\pi$.

Pour chacun des signes possibles de $\varepsilon_p$, l’exponentielle de $-\mathrm i\varepsilon_p|z_p|$ vaut $-1$.

Ainsi $\exp(z_p-\mathrm i\varepsilon_p|z_p|)=-e^{z_p}\to-1$ par Q23.

Cette contradiction prouve **la propriété $\mathcal P$**.

### IV.B — Une solution à $(E_h)$


### Question 26

> [!INDICATION]
> Développez l'exponentielle et appliquez la minoration de IV.A au dénominateur.

> [!INDICATION]
> Faites intervenir une borne arbitraire sur le module du paramètre. Justifiez l'intégration terme à terme et identifiez les coefficients de la série obtenue.

#### Solution

Posons $R_n=(2n+1)\pi$.

D’après $\mathcal P$, il existe $c>0$ tel que $|e^{\gamma_n(t)}-1|\geq c$ pour tout $n$ et tout $t$.

En particulier, l’intégrale qui définit $Q_n(z)$ est une intégrale de fonction continue sur $[0,1]$.

Pour $n$ fixé, développons l’exponentielle en série entière. Si $|z|\leq R$ avec $R>0$, le module du terme de rang $k$ de l’intégrande, facteur $n!$ compris, est borné par
$$
\frac{n!}{cR_n^{\,n-1}}\frac{(R_nR)^k}{k!}.
$$
La série de ces majorants converge. On intègre alors terme à terme pour obtenir
$$
\begin{aligned}
Q_n(z)&=\sum_{k=0}^{\infty} q_{n,k}z^k,\\
q_{n,k}&=\frac{n!}{k!}\int_0^1
\frac{\gamma_n(t)^{k-n+1}}{e^{\gamma_n(t)}-1}\,\mathrm dt .
\end{aligned}
$$
L’estimation précédente assure la convergence absolue pour tout $z$, donc **$Q_n\in\mathcal E$**. Elle vaut aussi pour $n=0$, puisque $R_0>0$.

> [!METHODE]
> Le développement sous l'intégrale donne plus que l'appartenance à l'espace des fonctions entières. Il fournit un majorant coefficient par coefficient réutilisable à la dernière question.

### Question 27

> [!INDICATION]
> Reprenez la simplification de Q16, puis écrivez la courbe d'intégration comme un rayon multiplié par le cercle unité.

> [!INDICATION]
> Appliquez Q9 en absorbant le rayon dans le paramètre de l'exponentielle.

#### Solution

En soustrayant les deux intégrales, la factorisation de Q16 supprime le facteur $e^{\gamma_n(t)}-1$. Comme $\gamma_n=R_n\omega$,
$$
Q_n(z+1)-Q_n(z)
=\frac{n!}{R_n^{\,n-1}}\int_0^1 e^{zR_n\omega(t)}\omega(t)^{-(n-1)}\,\mathrm dt .
$$
Par Q9, l’intégrale vaut le coefficient de rang $n-1$ de $w\mapsto e^{zR_nw}$, soit $(zR_n)^{n-1}/(n-1)!$. Donc **$Q_n(z+1)-Q_n(z)=nz^{n-1}$**.

### Question 28

> [!INDICATION]
> Majorez séparément l'exponentielle et la puissance du rayon dans l'expression intégrale.

> [!INDICATION]
> Comparez le rayon à une quantité linéaire en l'indice et la factorielle à une puissance de cet indice.

#### Solution

Puisque $\operatorname{Re}(z\gamma_n(t))\leq R_n|z|$, la propriété $\mathcal P$ donne
$$
|Q_n(z)|\leq\frac{n!}{cR_n^{\,n-1}}e^{R_n|z|}.
$$
Pour $n\geq1$, on a $n!\leq n^n$ et $R_n\geq2\pi n$.

Comme $n\leq2^{n-1}$ par récurrence, on obtient $n!/R_n^{\,n-1}\leq n/(2\pi)^{n-1}\leq1$.

Enfin, $R_n\leq3\pi n$.

**La borne demandée vaut avec $a=1/c$ et $b=3\pi$.**

### Question 29

> [!INDICATION]
> Formalisez la linéarité de la construction en associant à chaque monôme de $h$ son antécédent de Q27.

> [!INDICATION]
> Pour établir un rayon infini, majorez la famille double des coefficients pondérés sur un disque arbitraire en utilisant Q26 et Q28 avant de permuter les sommes.

#### Solution

Soit $h(z)=\sum_{j\geq0}h_j z^j$ une fonction de $\mathcal E$. On cherche la solution sous la forme
$$
f(z)=\sum_{j=0}^\infty\frac{h_j}{j+1}Q_{j+1}(z).
$$
Pour montrer que cette somme est entière, fixons $R>0$. Le majorant de Q26 s’applique aux coefficients en module pondérés par $R^k$. En le sommant sur $k$ puis en utilisant les estimations de Q28, on obtient, pour $n\geq1$,
$$
\begin{aligned}
\sum_{k\geq0}|q_{n,k}|R^k
&\leq\frac{n!}{cR_n^{\,n-1}}e^{R_nR}\\
&\leq a e^{bnR}.
\end{aligned}
$$
Par conséquent,
$$
\sum_{j,k\geq0}\left|\frac{h_j}{j+1}q_{j+1,k}\right|R^k
\leq a e^{bR}\sum_{j\geq0}|h_j|(e^{bR})^j<+\infty.
$$
La dernière série converge car le rayon de la série entière de $h$ est infini.

Le théorème de sommation par paquets des familles absolument sommables permet donc de regrouper par puissances de $z$ pour $|z|\leq R$.

Les coefficients obtenus sont $\sum_{j\geq0}h_jq_{j+1,k}/(j+1)$.

Comme $R$ est arbitraire, cette série entière a un rayon infini et représente $f$ sur tout $\mathbb C$.

Les deux séries définissant $f(z+1)$ et $f(z)$ sont convergentes. Par Q27 et par soustraction terme à terme,
$$
f(z+1)-f(z)=\sum_{j\geq0}h_jz^j=h(z).
$$
**La fonction $f$ est une solution entière de $(E_h)$.**

> [!PIEGE]
> Une limite ponctuelle de fonctions entières peut perdre la régularité. Ici la sommabilité des coefficients sur tout disque prouve directement l'existence d'une série entière de rayon infini.

## Bilan

- Pour étudier une application qui abaisse le degré, identifiez le coefficient qui subsiste et exploitez la dimension finie avant de passer à tout l'espace.
- Pour extraire un coefficient sur le cercle unité, établissez la convergence normale sur le trajet et intégrez les exponentielles en distinguant la fréquence zéro.
- Les polynômes de Bernoulli se manipulent à partir de la représentation adaptée au calcul. L'expression polynomiale se dérive directement et l'intégrale simplifie la différence finie.
- Pour sommer des séries entières dont l'indice intervient dans les estimations, établissez la sommabilité absolue de la famille des coefficients sur chaque disque. Elle justifie le regroupement et le rayon de convergence.
