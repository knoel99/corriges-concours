# CCINP MP — Mathématiques 1 2024 · Corrigé guidé

*Corrigé rédigé par IA, non officiel. Signalez toute erreur.*

## Présentation du sujet

Cette épreuve de quatre heures sans calculatrice comporte deux exercices indépendants et un problème. L'exercice I relie l'espérance d'une variable à valeurs dans $\mathbb N$ à ses probabilités de queue, puis applique cette formule au maximum de tirages avec remise. L'exercice II combine le théorème de Cauchy linéaire et les séries entières pour résoudre une équation différentielle dont le coefficient de $y''$ s'annule en $0$.

Le problème calcule deux fois la somme des inverses des carrés des entiers positifs. Les deux voies passent par la sous-série des indices impairs, reliée à la somme totale en Q8. La partie I associe le développement de $\operatorname{Arcsin}$ aux intégrales de Wallis. La partie II utilise le développement géométrique et une intégrale à paramètre. Elle peut se travailler indépendamment de la partie I.

Les calculs sont courts. Les points délicats sont le passage à la limite en Q1, la singularité en Q7, les interversions en Q12 et Q14 et la domination de la dérivée en Q16. Q2, Q4, Q8, Q9 et le calcul direct de $f(1)$ en Q18 donnent des points d'entrée rapides. Sur quatre heures, comptez environ 35 minutes pour le premier exercice, 50 pour le second, une heure par partie du problème et 15 minutes de relecture.

[Sujet officiel MP](https://www.concours-commun-inp.fr/_resource/annales%20%C3%A9crits/2024/MP/2024_MP1M1.pdf?download=true) · [Rapport MP 2024](https://www.concours-commun-inp.fr/_resource/annales%20%C3%A9crits/2024/MP/MP_ECRIT_Maths_1_2024.pdf?download=true) · [BO MP](https://www.education.gouv.fr/bo/21/Hebdo31/ESRS2111702A.htm) · [BO MPSI](https://www.education.gouv.fr/bo/21/Special1/ESRS2035779A.htm)

## Exercice I

La loi du maximum se trouve par sa fonction de répartition. Une fois cette loi connue, la formule des probabilités de queue transforme l'espérance en une somme de Riemann.

### Question 1

> [!INDICATION]
> Décomposez l'événement $\{X>k-1\}$ en distinguant le cas $X=k$. Procédez ensuite sur une somme finie.

> [!INDICATION]
> Pour passer à la limite, comparez $n\mathbb P(X>n)$ au reste de la série qui définit $\mathbb E(X)$.

#### Solution

Pour tout entier $k\geqslant 1$, l'événement $\{X>k-1\}$ est la réunion disjointe de $\{X=k\}$ et de $\{X>k\}$. Ainsi,
$$
\boxed{\mathbb P(X=k)=\mathbb P(X>k-1)-\mathbb P(X>k).}
$$
Posons $q_j=\mathbb P(X>j)$. Pour $n\geqslant1$,
$$
\begin{aligned}
\sum_{k=1}^{n} k\mathbb P(X=k)
&=\sum_{j=0}^{n-1}(j+1)q_j-\sum_{j=1}^{n}j q_j\\
&=\sum_{j=0}^{n-1}q_j-nq_n.
\end{aligned}
$$
L'identité vaut aussi pour $n=0$, par la convention sur les sommes vides.

L'espérance est finie, donc le reste $\sum_{k>n}k\mathbb P(X=k)$ tend vers zéro. Or
$$
0\leqslant n q_n\leqslant\sum_{k>n}k\mathbb P(X=k).
$$
L'identité précédente donne alors, en passant à la limite,
$$
\boxed{\mathbb E(X)=\sum_{k=0}^\infty \mathbb P(X>k).}
$$

> [!JURY]
> Le rapport 2024 relève que la limite de $n\mathbb P(X>n)$ a posé difficulté. La seule convergence de $\mathbb P(X>n)$ vers zéro ne contrôle pas ce produit. Écrivez le majorant issu de l'espérance finie.

### Question 2

> [!INDICATION]
> Traduisez la condition sur le maximum en une condition commune à chacun des tirages.

> [!INDICATION]
> Comptez les suites possibles avec remise. Pour isoler $X=k$, comparez deux événements de seuil consécutifs.

#### Solution

On suppose $p\geqslant1$, comme l'exige la définition du maximum. Pour $0\leqslant k\leqslant n$, l'événement $\{X\leqslant k\}$ signifie que chacun des $p$ tirages donne une boule de numéro au plus $k$.

Les $n^p$ suites de tirages avec remise sont équiprobables et $k^p$ satisfont cette condition. Ainsi, pour $k\in\mathbb N$,
$$
\boxed{
\mathbb P(X\leqslant k)=
\begin{cases}
(k/n)^p & \text{si } 0\leqslant k\leqslant n,\\
1 & \text{si } k>n.
\end{cases}}
$$
En prenant la différence de deux valeurs consécutives de cette fonction, on obtient, pour $1\leqslant k\leqslant n$,
$$
\boxed{\mathbb P(X=k)=\frac{k^p-(k-1)^p}{n^p}.}
$$
La probabilité est nulle en dehors de $\{1,\ldots,n\}$.

> [!JURY]
> Le rapport relève des lois données sans justification. Le comptage des suites équiprobables établit la fonction de répartition, puis la différence de deux seuils explique la loi ponctuelle.

### Question 3

> [!INDICATION]
> Repérez la subdivision régulière de $[0,1]$ et la fonction dont on évalue les valeurs aux extrémités gauches.

> [!INDICATION]
> Écrivez d'abord une égalité pour $\mathbb E(X)/n$ en utilisant Q1 et Q2. Passez à la limite dans cette égalité.

#### Solution

Pour $p$ fixé, la fonction $u\mapsto u^p$ est continue sur $[0,1]$. La somme demandée est la somme de Riemann aux extrémités gauches de la subdivision régulière en $n$ intervalles. Par conséquent,
$$
\begin{aligned}
\lim_{n\to\infty}\frac1n\sum_{k=0}^{n-1}(k/n)^p
&=\int_0^1 u^p\,\mathrm du\\
&=\boxed{\frac1{p+1}}.
\end{aligned}
$$
La question 1 s'applique à $X$, qui est bornée. Par la question 2 et puisque $\mathbb P(X>k)=0$ pour $k\geqslant n$,
$$
\begin{aligned}
\frac{\mathbb E(X)}{n}
&=\frac1n\sum_{k=0}^{n-1}\bigl(1-(k/n)^p\bigr)\\
&=1-\frac1n\sum_{k=0}^{n-1}(k/n)^p\\
&\longrightarrow \frac{p}{p+1}.
\end{aligned}
$$
Cette limite étant strictement positive, **$\mathbb E(X)\sim \dfrac{p}{p+1}n$ lorsque $n\to+\infty$.**

> [!JURY]
> Le rapport relève l'oubli de la continuité dans l'usage des sommes de Riemann et la soustraction d'équivalents. L'égalité normalisée permet de soustraire des quantités qui ont chacune une limite, puis de conclure grâce à une limite strictement positive.

## Exercice II

Sur $I$, on peut normaliser l'équation et appliquer le théorème de Cauchy. La dernière question demande un autre raisonnement au point $0$, où cette normalisation cesse d'être possible.

### Question 4

> [!INDICATION]
> Mettez l'équation sous forme résolue en $y''$ sur $I$, puis considérez les conditions initiales en un point intérieur à $I$.

#### Solution

Sur $I=]0,+\infty[$, on divise par $x^2$. L'équation homogène devient
$$
y''+\frac4x y'+\left(\frac2{x^2}-1\right)y=0.
$$
Ses coefficients sont continus sur $I$.

Par le théorème de Cauchy linéaire, pour tout $(a,b)\in\mathbb R^2$, il existe une unique solution sur $I$ telle que $y(1)=a$ et $y'(1)=b$.

L'application linéaire $y\mapsto(y(1),y'(1))$ est donc un isomorphisme de $S_I(H)$ sur $\mathbb R^2$. Ainsi, **$\dim S_I(H)=2$.**

> [!JURY]
> Le rapport signale l'emploi d'équations caractéristiques avec des coefficients variables. Le théorème de Cauchy donne ici la dimension via les deux données initiales libres, après vérification de la continuité des coefficients sur $I$.

### Question 5

> [!INDICATION]
> Introduisez des coefficients $a_k$ et utilisez la dérivation des séries entières à l'intérieur du rayon de convergence.

> [!INDICATION]
> Dans le coefficient de $x^k$, faites apparaître séparément la contribution de $-x^2y$. Examinez d'abord $k=0$ et $k=1$, puis étudiez chaque parité.

#### Solution

Cherchons $y(x)=\sum_{k=0}^{\infty}a_kx^k$ de rayon de convergence infini, et posons $a_{-1}=a_{-2}=0$. La dérivation terme à terme et la multiplication par les monômes donnent
$$
x^2y''+4xy'+(2-x^2)y
=\sum_{k=0}^\infty\bigl((k+1)(k+2)a_k-a_{k-2}\bigr)x^k.
$$
Si $y$ est solution sur $I$, cette série vaut $1$ pour tout $x>0$.

Les deux membres sont $\mathcal C^\infty$ au voisinage de $0$. La différence est nulle sur un intervalle à droite de $0$, donc ses dérivées s'annulent en $0$ par continuité.

L'identification donne
$$
\begin{aligned}
a_0&=\tfrac12,\\
a_1&=0,\\
a_k&=\frac{a_{k-2}}{(k+1)(k+2)}\quad(k\geqslant2).
\end{aligned}
$$
Par récurrence, $a_{2m}=1/(2m+2)!$ et $a_{2m+1}=0$ pour tout $m\geqslant0$.

La série obtenue converge pour tout $x\in\mathbb R$ par le critère de d'Alembert appliqué aux termes pairs pour $x\ne0$. Ses coefficients vérifient les relations précédentes, donc elle fournit bien une solution sur $I$, unique parmi celles de rayon infini.

Le développement de $\operatorname{ch}$ donne
$$
\begin{aligned}
f(x)&=\sum_{m=0}^\infty\frac{x^{2m}}{(2m+2)!}\\
&=\boxed{\frac{\operatorname{ch}x-1}{x^2}}\quad(x>0).
\end{aligned}
$$

> [!METHODE]
> Pour une recherche par série entière, séparez deux étapes. Les coefficients sont d'abord imposés par l'équation. La convergence de la série obtenue et la vérification de l'équation prouvent ensuite l'existence.

> [!JURY]
> Le rapport signale de nombreuses erreurs aux rangs 0 et 1. Dans ces deux rangs, le terme issu du produit par le monôme de degré deux est absent.

### Question 6

> [!INDICATION]
> Une différence de deux solutions de $(E)$ appartient à l'espace des solutions de $(H)$. Utilisez les deux solutions connues de $(E)$.

> [!INDICATION]
> Pour tester l'indépendance avec $h$, multipliez une relation linéaire par $x^2$ et étudiez son comportement en $0^+$.

#### Solution

Les fonctions $f$ et $g$ étant solutions de $(E)$, $f-g$ appartient à $S_I(H)$.

Par la question 5 et la définition de $g$, on a $(f-g)(x)=\operatorname{ch}x/x^2$. La fonction $h$ appartient aussi à $S_I(H)$ d'après l'énoncé.

Les deux fonctions sont indépendantes.

En effet, une relation $\alpha(f-g)+\beta h=0$, multipliée par $x^2$, donne $\alpha\operatorname{ch}x+\beta\operatorname{sh}x=0$ sur $I$.

En faisant tendre $x$ vers $0^+$, on obtient $\alpha=0$, puis $\beta=0$ puisque $\operatorname{sh}x>0$ sur $I$.

D'après la question 4, ces deux fonctions forment une base de $S_I(H)$. Toute solution de $(E)$ diffère de $g$ d'une solution de $(H)$, et réciproquement. Ainsi,
$$
\boxed{S_I(E)=
\left\{x\longmapsto\frac{-1+\alpha\operatorname{ch}x+\beta\operatorname{sh}x}{x^2}
\ \middle|\ (\alpha,\beta)\in\mathbb R^2\right\}.}
$$

> [!PIEGE]
> $S_I(H)$ est un espace vectoriel. $S_I(E)$ est un espace affine passant par $g$ et sa description ci-dessus traduit précisément cette structure.

### Question 7

> [!INDICATION]
> Le coefficient de $y''$ s'annule à l'origine. Cherchez à reconnaître les trois premiers termes de l'expression comme une dérivée seconde de produit.

> [!INDICATION]
> Une fois la nouvelle inconnue choisie, écrivez ses conditions initiales à l'origine en partant d'une solution définie sur $\mathbb R$.

#### Solution

Soit $y$ une solution sur $\mathbb R$. Pour $z(x)=x^2y(x)$,
$$
z''(x)-z(x)=x^2y''(x)+4xy'(x)+(2-x^2)y(x)=0.
$$
De plus, $z(0)=z'(0)=0$.

Le théorème de Cauchy linéaire appliqué à $z''-z=0$ sur $\mathbb R$ entraîne $z=0$.

Donc $y(x)=0$ pour $x\ne0$, et $y(0)=0$ par continuité. **$S_{\mathbb R}(H)=\{0\}$ et sa dimension vaut $0$.**

> [!METHODE]
> En posant $z=x^2y$, le point singulier fournit les deux données initiales de la nouvelle équation. Cette approche traite les deux demi-droites dans une preuve commune.

## Problème

La question préliminaire isole la relation entre la série complète et sa sous-série impaire. Gardez cette relation pour les conclusions des deux parties.

### Question 8 — Question préliminaire

> [!INDICATION]
> Séparez les entiers positifs selon leur parité. Dans la série des termes pairs, factorisez le carré du facteur $2$.

#### Solution

Posons $S=\sum_{n=1}^\infty 1/n^2$ et $O=\sum_{n=0}^\infty 1/(2n+1)^2$. La série de Riemann définissant $S$ converge.

En séparant les rangs pairs et impairs,
$$
\begin{aligned}
S&=O+\sum_{n=1}^\infty\frac1{(2n)^2}\\
&=O+\frac14S.
\end{aligned}
$$
Ainsi $S=\frac43 O$. Sous l'hypothèse de la question, $O=\pi^2/8$, donc **$S=\pi^2/6$.**

> [!PIEGE]
> Gardez l'équation $S=\frac43O$. Les parties I et II établissent chacune la valeur de $O$, provisoirement supposée dans cette question.

## Partie I

Les coefficients du développement de l'arcsinus et les intégrales de Wallis se simplifient lors de l'intégration terme à terme. L'extrémité du segment d'intégration demande une justification particulière.

### Question 9

> [!INDICATION]
> Écrivez $\sin^{n+2}$ comme le produit de $\sin^{n+1}$ et de $\sin$, puis intégrez par parties.

> [!INDICATION]
> Ramenez le facteur $\cos^2$ à une expression en $\sin^2$. Pour les indices impairs, partez de $W_1$.

#### Solution

Pour tout $n\geqslant0$,
$$
\boxed{\frac{\mathrm d}{\mathrm dx}(\sin x)^{n+1}
=(n+1)(\sin x)^n\cos x.}
$$
Une intégration par parties sur $[0,\pi/2]$ donne
$$
\begin{aligned}
W_{n+2}
&=\int_0^{\pi/2}(\sin x)^{n+1}\sin x\,\mathrm dx\\
&=\bigl[-(\sin x)^{n+1}\cos x\bigr]_0^{\pi/2}
 +(n+1)\int_0^{\pi/2}(\sin x)^n\cos^2 x\,\mathrm dx\\
&=(n+1)(W_n-W_{n+2}).
\end{aligned}
$$
Par conséquent, **$W_{n+2}=\dfrac{n+1}{n+2}W_n$.** Puisque $W_1=1$, les récurrences aux indices impairs donnent
$$
\begin{aligned}
W_{2n+1}
&=\prod_{j=1}^{n}\frac{2j}{2j+1}\\
&=\boxed{\frac{2^{2n}(n!)^2}{(2n+1)!}}.
\end{aligned}
$$
Le produit vide vaut $1$ pour $n=0$.

### Question 10

> [!INDICATION]
> Choisissez une substitution dans le développement binomial de $(1+u)^\alpha$.

> [!INDICATION]
> Pour obtenir celui de $\operatorname{Arcsin}$, identifiez sa dérivée et utilisez la convergence uniforme sur le segment qui joint $0$ à $x$.

#### Solution

On applique le développement binomial de $(1+u)^{-1/2}$ pour $|u|<1$ avec $u=-x^2$. Le coefficient de $x^{2n}$ est
$$
(-1)^n\binom{-1/2}{n}
=\frac{1\cdot3\cdots(2n-1)}{2^n n!}
=\frac{(2n)!}{2^{2n}(n!)^2}.
$$
Il vaut $1$ en rang $0$. Il vient pour $|x|<1$,
$$
\boxed{\frac1{\sqrt{1-x^2}}
=\sum_{n=0}^\infty\frac{(2n)!}{2^{2n}(n!)^2}x^{2n}.}
$$
Sur $]-1,1[$, $\operatorname{Arcsin}$ est la primitive de cette fonction qui s'annule en $0$.

La série entière converge uniformément sur tout segment inclus dans $]-1,1[$, donc on peut l'intégrer terme à terme de $0$ à $x$.

Pour $|x|<1$, on obtient
$$
\boxed{\operatorname{Arcsin}x
=\sum_{n=0}^\infty\frac{(2n)!}{2^{2n}(n!)^2(2n+1)}x^{2n+1}
.}
$$

> [!JURY]
> Le rapport demande le domaine de validité et la justification des coefficients. Le développement binomial s'applique à l'intérieur du rayon, puis la convergence uniforme sur chaque segment autorise la primitivation.

### Question 11

> [!INDICATION]
> Vérifiez que $\sin x$ appartient au domaine de validité de Q10 et que $x$ est dans l'intervalle où $\sin$ et $\operatorname{Arcsin}$ sont réciproques.

#### Solution

Pour $0\leqslant x<\pi/2$, on a $0\leqslant\sin x<1$. Le développement précédent s'applique donc à $\sin x$. Sur $[-\pi/2,\pi/2]$, $\operatorname{Arcsin}$ est la réciproque de la restriction de $\sin$. Ainsi,
$$
\boxed{x=\sum_{n=0}^\infty
\frac{(2n)!}{2^{2n}(n!)^2(2n+1)}(\sin x)^{2n+1}.}
$$

### Question 12

> [!INDICATION]
> Les termes sont positifs sur le segment. Majorez une somme partielle en vous servant de l'identité de Q11 à l'intérieur de l'intervalle.

> [!INDICATION]
> Passez à l'extrémité dans cette somme finie. Comparez le nombre obtenu à la somme des normes uniformes des mêmes termes.

#### Solution

Notons $b_n=(2n)!/[2^{2n}(n!)^2(2n+1)]$. Les termes de la série de la question 11 sont positifs ou nuls sur $[0,\pi/2[$. Pour tout $N$ et tout $x$ dans cet intervalle,
$$
\sum_{n=0}^{N}b_n(\sin x)^{2n+1}\leqslant x.
$$
En faisant tendre $x$ vers $\pi/2$ à gauche dans la somme finie, on obtient $\sum_{n=0}^{N}b_n\leqslant\pi/2$.

Les sommes partielles de $\sum b_n$ sont donc croissantes et majorées.

Comme $\|b_n(\sin \cdot)^{2n+1}\|_{\infty,[0,\pi/2]}=b_n$, la série de fonctions converge normalement, donc uniformément, sur le segment.

Ses termes sont continus, d'où
$$
\begin{aligned}
\int_0^{\pi/2}\sum_{n=0}^\infty b_n(\sin x)^{2n+1}\,\mathrm dx&\\
&=\boxed{\sum_{n=0}^\infty b_n W_{2n+1}}.
\end{aligned}
$$

> [!JURY]
> Le rapport relève des convergences uniformes ou normales annoncées sans preuve. Ici la positivité donne la majoration de la somme finie, et cette majoration subsiste à l'extrémité par continuité. La convergence normale en découle.

### Question 13

> [!INDICATION]
> Calculez les deux membres de l'égalité de Q12 en utilisant Q11 à gauche et Q9 à droite. Revenez ensuite à la relation entre les séries établie en Q8.

#### Solution

D'après la question 12, la somme est continue sur $[0,\pi/2]$ par convergence uniforme de la série de fonctions continues. L'identité de la question 11 s'étend donc à $\pi/2$ par continuité.

Le membre de gauche de l'identité de la question 12 vaut alors $\int_0^{\pi/2}x\,\mathrm dx=\pi^2/8$. Par la question 9,
$$
b_n W_{2n+1}=\frac{(2n)!}{(2n+1)(2n+1)!}=\frac1{(2n+1)^2}.
$$
On a donc **$O=\pi^2/8$**. La relation $S=\frac43 O$ établie à la question 8 donne **$S=\pi^2/6$.**

> [!JURY]
> Le rapport souligne que la valeur admise en Q8 doit être démontrée ici. Seule la relation algébrique entre la série complète et sa sous-série impaire est réutilisée.

## Partie II

Une même intégrale apparaît d'abord par développement géométrique, puis comme intégrale de la dérivée d'une fonction de paramètre. Il faut établir la régularité de cette fonction avant de relier les deux expressions.

### Question 14

> [!INDICATION]
> Développez la fraction par une série géométrique de raison $x^2$, puis multipliez par $\ln x$.

> [!INDICATION]
> Sur $[\varepsilon,1]$, calculez l'intégrale d'un terme par parties. Après le passage à la limite en $\varepsilon$, examinez la série des intégrales des valeurs absolues.

#### Solution

Pour $|x|<1$, la série géométrique de raison $x^2$ donne
$$
\boxed{\frac1{x^2-1}=-\sum_{n=0}^\infty x^{2n}.}
$$
Pour $n\geqslant0$, posons $u_n(x)=-x^{2n}\ln x$ sur $]0,1[$. Cette fonction positive et continue est intégrable, car $0\leqslant u_n(x)\leqslant-\ln x$ et $-\ln$ est intégrable sur $]0,1[$.

L'intégration par parties sur $[\varepsilon,1]$, avec $\varepsilon>0$, donne à la limite
$$
\int_0^1u_n(x)\,\mathrm dx=\frac1{(2n+1)^2}.
$$
Le terme de bord en $\varepsilon$ tend vers zéro puisque $\varepsilon^{2n+1}\ln\varepsilon\to0$, et le terme restant est $\frac1{2n+1}\int_0^1x^{2n}\,\mathrm dx$.

La somme des $u_n$ est la fonction continue $x\mapsto\ln x/(x^2-1)$ sur $]0,1[$. De plus, $\sum_n \int_0^1|u_n(x)|\,\mathrm dx$ converge par comparaison à une série de Riemann. Le théorème d'intégration terme à terme donne donc
$$
\boxed{\int_0^1\frac{\ln x}{x^2-1}\,\mathrm dx
=\sum_{n=0}^\infty\frac1{(2n+1)^2}.}
$$

> [!METHODE]
> Sur un intervalle ouvert avec des extrémités impropres, le critère par la somme des intégrales absolues dispense d'établir la convergence uniforme sur tout l'intervalle. Vérifiez aussi la convergence simple et la continuité de la somme.

### Question 15

> [!INDICATION]
> Utilisez une borne globale de $\operatorname{Arctan}$. Étudiez l'intégrabilité du majorant à chacune des deux extrémités du domaine en $t$.

#### Solution

Pour chaque $t\geqslant0$, $x\mapsto\operatorname{Arctan}(xt)/(1+t^2)$ est continue sur $[0,+\infty[$. Pour chaque $x$, l'intégrande est continue en $t$. Sur tout le domaine,
$$
\left|\frac{\operatorname{Arctan}(xt)}{1+t^2}\right|
\leqslant\frac{\pi}{2(1+t^2)}.
$$
Ce majorant indépendant de $x$ est continu en $0$ et est en $O(t^{-2})$ à l'infini. Il est donc intégrable sur $[0,+\infty[$. **$f$ est bien définie et continue sur $[0,+\infty[$**, par le théorème de continuité des intégrales à paramètre.

> [!JURY]
> Le rapport relève des erreurs d'intégrabilité en $0$. Une étude en deux zones suffit ici. Le majorant est borné au voisinage de $0$ et décroît comme $t^{-2}$ à l'infini.

### Question 16

> [!INDICATION]
> Dérivez l'intégrande par rapport au paramètre $x$. L'estimation en $t$ peut être faite en tenant $x$ à distance de $0$.

> [!INDICATION]
> Pour $x\geqslant a>0$ fixé comme domaine de variation, remplacez dans le dénominateur le facteur dépendant de $x$ par un facteur ne dépendant que de $a$ et de $t$.

#### Solution

Pour $t\geqslant0$, la dérivée partielle selon $x$ est continue et vaut
$$
\frac{\partial}{\partial x}\left(\frac{\operatorname{Arctan}(xt)}{1+t^2}\right)
=\frac{t}{(1+t^2)(1+x^2t^2)}.
$$
Pour chaque $x>0$, cette dérivée est aussi continue en $t$ sur $[0,+\infty[$.

Fixons $a>0$.

Pour $x\geqslant a$, la valeur absolue est majorée par $t/[(1+t^2)(1+a^2t^2)]$.

Ce majorant est continu en $0$ et en $O(t^{-3})$ à l'infini, donc intégrable sur $[0,+\infty[$.

L'intégrabilité de l'intégrande pour chaque $x$ est acquise par la question 15.

Le théorème de dérivation sous l'intégrale appliqué sur $]a,+\infty[$, pour tout $a>0$, établit que $f$ est $\mathcal C^1$ sur $]0,+\infty[$, donc sur $]0,1]$, et
$$
\boxed{f'(x)=\int_0^{+\infty}\frac{t}{(1+t^2)(1+x^2t^2)}\,\mathrm dt
\quad(x>0).}
$$

> [!JURY]
> Le rapport relève des dérivations selon $t$ et des majorants qui dépendent de $x$. Le paramètre varie dans $]a,+\infty[$ alors que le domaine d'intégration en $t$ reste $[0,+\infty[$. Le choix de $a$ donne un majorant commun à tous les paramètres de cet intervalle.

### Question 17

> [!INDICATION]
> Au numérateur, les termes en $t^3$ se simplifient. Repérez le facteur à extraire pour retrouver l'intégrande de $f'$.

> [!INDICATION]
> Intégrez d'abord jusqu'à une borne finie $T$. Regroupez les logarithmes avant d'envoyer $T$ vers l'infini.

#### Solution

Pour $0<x<1$ et $t\geqslant0$,
$$
\boxed{\frac{t}{1+t^2}-\frac{x^2t}{1+x^2t^2}
=\frac{(1-x^2)t}{(1+t^2)(1+x^2t^2)}.}
$$
On intègre cette différence sur $[0,T]$ avant de passer à la limite. Le résultat est
$$
\int_0^T\left(\frac{t}{1+t^2}-\frac{x^2t}{1+x^2t^2}\right)\mathrm dt
=\frac12\ln\!\left(\frac{1+T^2}{1+x^2T^2}\right)
\longrightarrow -\ln x.
$$
Par la question 16, la limite du membre de gauche est $(1-x^2)f'(x)$. Par conséquent,
$$
\boxed{f'(x)=\frac{\ln x}{x^2-1}\quad(0<x<1).}
$$

> [!PIEGE]
> Les deux fractions ont chacune une intégrale divergente à l'infini. Leur différence s'intègre grâce à l'annulation des termes dominants. Gardez la même borne finie dans les deux primitives.

### Question 18

> [!INDICATION]
> À $x=1$, reconnaissez le produit d'une fonction et de sa dérivée.

> [!INDICATION]
> Intégrez $f'$ entre $\varepsilon$ et $1$. Utilisez la continuité en $0$ et la valeur de $f(0)$ pour passer à la limite, puis revenez à Q14.

#### Solution

Une primitive de $\operatorname{Arctan}(t)/(1+t^2)$ est $\frac12(\operatorname{Arctan}t)^2$. Ainsi,
$$
\boxed{f(1)=\left[\tfrac12(\operatorname{Arctan}t)^2\right]_0^{+\infty}
=\frac{\pi^2}{8}.}
$$
Pour $0<\varepsilon<1$, la question 16 et le théorème fondamental de l'analyse donnent $f(1)-f(\varepsilon)=\int_\varepsilon^1 f'(x)\,\mathrm dx$.

D'après la question 15, $f$ est continue en $0$ et $f(0)=0$ par définition.

Les questions 17 et 14 permettent de passer à la limite et d'écrire
$$
\begin{aligned}
f(1)&=\int_0^1 \frac{\ln x}{x^2-1}\,\mathrm dx\\
&=\sum_{n=0}^\infty \frac1{(2n+1)^2}.
\end{aligned}
$$
Cette seconde méthode donne **$O=\pi^2/8$**, puis **$S=\pi^2/6$** par la relation de la question 8.

> [!JURY]
> Le rapport souligne l'oubli de $f(0)=0$. Cette valeur et la continuité en $0$ donnent la valeur du terme de bord au passage à la limite.

## Bilan

- Relier une espérance à la queue de la loi demande de contrôler le reste de la série qui définit cette espérance. Pour un maximum de tirages avec remise, la fonction de répartition donne directement les probabilités utiles.
- Une équation linéaire d'ordre deux donne deux conditions initiales libres sur un intervalle où sa forme résolue a des coefficients continus. Au point singulier, cherchez une transformation dont l'équation résultante garde un sens.
- Pour intégrer une série, choisissez un critère que vous pouvez vérifier sur le domaine entier. En Q12, la positivité des coefficients donne la convergence normale jusque sur le bord. En Q14, les intégrales absolues des termes forment une série convergente.
- Pour dériver une intégrale à paramètre, cherchez une domination intégrable de la dérivée locale en paramètre. Pour intégrer ensuite cette dérivée jusqu'au bord, utilisez la continuité de la fonction et une limite d'intégrales sur des segments.
