# CCINP MPI — Mathématiques 1 2024 · Corrigé brut

*Corrigé rédigé par IA, non officiel. Signalez toute erreur.*

## Exercice I

### Question 1

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

### Question 2

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

### Question 3

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

## Exercice II

### Question 4

Sur $I=]0,+\infty[$, on divise par $x^2$. L'équation homogène devient
$$
y''+\frac4x y'+\left(\frac2{x^2}-1\right)y=0.
$$
Ses coefficients sont continus sur $I$.

Par le théorème de Cauchy linéaire, pour tout $(a,b)\in\mathbb R^2$, il existe une unique solution sur $I$ telle que $y(1)=a$ et $y'(1)=b$.

L'application linéaire $y\mapsto(y(1),y'(1))$ est donc un isomorphisme de $S_I(H)$ sur $\mathbb R^2$. Ainsi, **$\dim S_I(H)=2$.**

### Question 5

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

### Question 6

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

### Question 7

Soit $y$ une solution sur $\mathbb R$. Pour $z(x)=x^2y(x)$,
$$
z''(x)-z(x)=x^2y''(x)+4xy'(x)+(2-x^2)y(x)=0.
$$
De plus, $z(0)=z'(0)=0$.

Le théorème de Cauchy linéaire appliqué à $z''-z=0$ sur $\mathbb R$ entraîne $z=0$.

Donc $y(x)=0$ pour $x\ne0$, et $y(0)=0$ par continuité. **$S_{\mathbb R}(H)=\{0\}$ et sa dimension vaut $0$.**

## Problème

### Question 8 — Question préliminaire

Posons $S=\sum_{n=1}^\infty 1/n^2$ et $O=\sum_{n=0}^\infty 1/(2n+1)^2$. La série de Riemann définissant $S$ converge.

En séparant les rangs pairs et impairs,
$$
\begin{aligned}
S&=O+\sum_{n=1}^\infty\frac1{(2n)^2}\\
&=O+\frac14S.
\end{aligned}
$$
Ainsi $S=\frac43 O$. Sous l'hypothèse de la question, $O=\pi^2/8$, donc **$S=\pi^2/6$.**

### Partie I

#### Question 9

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

#### Question 10

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

#### Question 11

Pour $0\leqslant x<\pi/2$, on a $0\leqslant\sin x<1$. Le développement précédent s'applique donc à $\sin x$. Sur $[-\pi/2,\pi/2]$, $\operatorname{Arcsin}$ est la réciproque de la restriction de $\sin$. Ainsi,
$$
\boxed{x=\sum_{n=0}^\infty
\frac{(2n)!}{2^{2n}(n!)^2(2n+1)}(\sin x)^{2n+1}.}
$$

#### Question 12

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

#### Question 13

D'après la question 12, la somme est continue sur $[0,\pi/2]$ par convergence uniforme de la série de fonctions continues. L'identité de la question 11 s'étend donc à $\pi/2$ par continuité.

Le membre de gauche de l'identité de la question 12 vaut alors $\int_0^{\pi/2}x\,\mathrm dx=\pi^2/8$. Par la question 9,
$$
b_n W_{2n+1}=\frac{(2n)!}{(2n+1)(2n+1)!}=\frac1{(2n+1)^2}.
$$
On a donc **$O=\pi^2/8$**. La relation $S=\frac43 O$ établie à la question 8 donne **$S=\pi^2/6$.**

### Partie II

#### Question 14

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

#### Question 15

Pour chaque $t\geqslant0$, $x\mapsto\operatorname{Arctan}(xt)/(1+t^2)$ est continue sur $[0,+\infty[$. Pour chaque $x$, l'intégrande est continue en $t$. Sur tout le domaine,
$$
\left|\frac{\operatorname{Arctan}(xt)}{1+t^2}\right|
\leqslant\frac{\pi}{2(1+t^2)}.
$$
Ce majorant indépendant de $x$ est continu en $0$ et est en $O(t^{-2})$ à l'infini. Il est donc intégrable sur $[0,+\infty[$. **$f$ est bien définie et continue sur $[0,+\infty[$**, par le théorème de continuité des intégrales à paramètre.

#### Question 16

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

#### Question 17

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

#### Question 18

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
