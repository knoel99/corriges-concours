# Centrale-Supélec MP/MPI — Mathématiques 2 2024 · Corrigé brut

*Corrigé rédigé par IA, non officiel. Signalez toute erreur.*

## I — Étude de l’opérateur différence finie

### Question 1

La substitution $X\mapsto X+1$ transforme tout polynôme en polynôme et commute aux combinaisons linéaires. La différence entre cette substitution et l’identité est donc **un endomorphisme de $\mathbb K[X]$**.

### Question 2

Si $P$ est constant, y compris nul, $\Delta(P)=0$ et $\deg\Delta(P)=-\infty$ avec la convention usuelle. Si $P$ est de degré $m\geq1$ et de coefficient dominant $a_m$, le binôme donne
$$
(X+1)^m-X^m=mX^{m-1}+\sum_{j=0}^{m-2}\binom mj X^j .
$$
Les termes de $P$ de degré strictement inférieur à $m$ donnent, après application de $\Delta$, des termes de degré au plus $m-2$ ou le polynôme nul. Comme $ma_m\ne0$, **$\deg\Delta(P)=m-1$**.

### Question 3

Par Q2, pour $d\geq1$, l’image d’un polynôme de $\mathbb K_d[X]$ appartient à $\mathbb K_{d-1}[X]$. Elle appartient donc à $\mathbb K_d[X]$. **La restriction $\Delta_d$ est un endomorphisme de cet espace.**

### Question 4

Q2 montre que **$\ker\Delta_d=\mathbb K_0[X]$**. Par le théorème du rang, l’image a pour dimension $(d+1)-1=d$. Elle est incluse dans $\mathbb K_{d-1}[X]$, de même dimension. Ainsi **$\operatorname{Im}\Delta_d=\mathbb K_{d-1}[X]$**.

### Question 5

D’après Q2, **$\ker\Delta=\mathbb K_0[X]$**. Pour tout polynôme $H$ de degré $m\geq0$, Q4 appliquée à $d=m+1$ donne un antécédent de $H$. Le polynôme nul admet aussi un antécédent. On a donc **$\operatorname{Im}\Delta=\mathbb K[X]$**.

Si $h$ est la fonction associée à $H$, un polynôme $P_0$ tel que $\Delta(P_0)=H$ donne une solution de $(E_h)$.

Comme $\mathbb K$ est infini, l’identité de fonctions polynomiales équivaut à celle de leurs polynômes.

Toute autre solution polynomiale diffère de $P_0$ d’un élément de $\ker\Delta$.

Réciproquement, ajouter une constante laisse la différence inchangée.

**Les solutions polynomiales sont les $P_0+c$ avec $c\in\mathbb K$.**

### Question 6

Pour $P_0(X)=X(X-1)/2$, le calcul donne
$$
P_0(X+1)-P_0(X)=\tfrac12 X\bigl((X+1)-(X-1)\bigr)=X.
$$
Par Q5, **les solutions polynomiales sont $P_0+c$, avec $c\in\mathbb K$**.

### Question 7

Chaque application de $\Delta_d$ abaisse le degré d’au moins une unité jusqu’à annulation.

Ainsi $\Delta_d^{\,d+1}=0$ et **$X^{d+1}$ est annulateur**.

Toute valeur propre $\lambda$ vérifierait $\lambda^{d+1}=0$.

Si $\Delta_d$ était diagonalisable, sa diagonale serait donc nulle.

Or $\Delta_d(X)=1$ pour $d\geq1$.

**$\Delta_d$ n’est pas diagonalisable.**

## II — Fonctions entières

### II.A — Généralités

### Question 8

Écrivons $f(z)=\sum_{n\geq0}a_nz^n$ et $g(z)=\sum_{n\geq0}b_nz^n$. Pour tout $z$, les deux séries convergent absolument. Leur combinaison linéaire est représentée par la série de coefficients $\lambda a_n+\mu b_n$, absolument convergente pour tout $z$.

Le théorème du produit de Cauchy des séries absolument convergentes donne
$$
f(z)g(z)=\sum_{n\geq0}\left(\sum_{j=0}^{n}a_jb_{n-j}\right)z^n .
$$
La série est absolument convergente pour tout $z$, donc son rayon est infini. **$\lambda f+\mu g$ et $fg$ appartiennent à $\mathcal E$.**

### Question 9

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

### II.B — Une intégrale

### Question 10

Les zéros de $e^z-1$ sont les $2\mathrm i\pi k$ avec $k\in\mathbb Z$.

Aucun n’a pour module $1$.

Comme $\omega(t)$ a module $1$, le dénominateur est partout non nul et toutes les puissances entières de $\omega(t)$ sont continues.

**L’intégrande est continue sur $[0,1]$ et $I_p$ est bien définie.**

### Question 11

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

Sur $\mathbb U$, $|\zeta\beta(\zeta)|\leq C<1$. La série géométrique de raison $-\zeta\beta(\zeta)$ est donc convergente et sa somme vaut $(1+\zeta\beta(\zeta))^{-1}$. Avec la factorisation de Q11 et $\zeta\ne0$, on obtient
$$
\boxed{\frac{\zeta^p}{e^\zeta-1}
=\sum_{j=0}^{\infty}(-1)^j\zeta^{j+p-1}\beta(\zeta)^j.}
$$
Pour chaque $p\in\mathbb Z$, le module du terme de rang $j$ est au plus $C^j$ sur $\mathbb U$.

### Question 13

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

### III.A — Lien avec l’équation $(E_h)$

### Question 14

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

### Question 15

On dérive le polynôme de Q14 puis on pose $j=k-1$.
$$
\begin{aligned}
B'_n(z)&=n!\sum_{k=1}^{n}\frac{z^{k-1}}{(k-1)!}I_{k-n}\\
&=\boxed{n B_{n-1}(z)}.
\end{aligned}
$$

### Question 16

Dans l’expression intégrale de la différence, on factorise $e^{(z+1)\omega(t)}-e^{z\omega(t)}$ par $e^{\omega(t)}-1$. On obtient
$$
B_n(z+1)-B_n(z)
=n!\int_0^1 e^{z\omega(t)}\omega(t)^{-(n-1)}\,\mathrm dt.
$$
La fonction $w\mapsto e^{zw}$ est entière, et son coefficient de rang $n-1$ vaut $z^{n-1}/(n-1)!$. Q9 donne donc **$B_n(z+1)-B_n(z)=n z^{n-1}$**.

### Question 17

Si $h(z)=\sum_{k=0}^m h_k z^k$, Q16 donne, par linéarité, la solution polynomiale
$$
\boxed{f(z)=\sum_{k=0}^m \frac{h_k}{k+1} B_{k+1}(z).}
$$
En effet, le terme de rang $k$ a pour différence finie $h_k z^k$. Pour $h=0$, la solution nulle convient.

### III.B — Unicité

### Question 18

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

### Question 19

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

La fonction $v(x)=\sum_{j\geq0} x^j/(j+1)!$ est de classe $\mathcal C^\infty$ sur $\mathbb R$, comme somme d’une série entière de rayon infini.

Elle vaut $(e^x-1)/x$ pour $x\ne0$ et $1$ en $0$.

Elle est strictement positive, puisque l’exponentielle est strictement croissante sur $\mathbb R$.

Ainsi $\psi=1/v$ est de classe $\mathcal C^\infty$ sur $\mathbb R$.

La fonction $(x,t)\mapsto tx$ est polynomiale et l’exponentielle est de classe $\mathcal C^\infty$.

Par composition et produit, **$u$ est de classe $\mathcal C^\infty$ sur $\mathbb R^2$**.

### Question 21

Pour tout $(x,t)$, **$\partial_t u(x,t)=xu(x,t)$**.

Comme $u$ est de classe $\mathcal C^\infty$, le théorème de Schwarz permet de permuter $\partial_t$ et $\partial_x^n$.

Par la formule de Leibniz, toutes les dérivées en $x$ de l’ordre au moins deux du facteur $x$ sont nulles.

Il reste
$$
\boxed{\partial_t\partial_x^n u(x,t)
=x\partial_x^n u(x,t)+n\partial_x^{n-1}u(x,t).}
$$

### Question 22

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

## IV — Solution entière de l’équation $(E_h)$

### IV.A — Une inégalité de contrôle

### Question 23

Nier $\mathcal P$ signifie que, pour tout $c>0$, il existe un entier naturel $n$ et un complexe $z$ tels que
$$
\begin{aligned}
|z|&=(2n+1)\pi,\\
|e^z-1|&<c.
\end{aligned}
$$
Pour chaque $p\geq0$, choisissons un tel couple $(n_p,z_p)$ avec $c=1/(p+1)$. **Les $z_p$ ont les modules imposés et $e^{z_p}\to1$.**

### Question 24

On a $e^{a_p}=|e^{z_p}|\to1$, et le logarithme est continu en $1$. Ainsi **$a_p\to0$**. Comme $|b_p|=|\mathrm ib_p|$, l’inégalité triangulaire inversée donne
$$
0\leq |z_p|-|b_p|\leq |a_p|.
$$
Le majorant tend vers zéro, donc **$|z_p|-|b_p|\to0$**.

### Question 25

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

### Question 27

En soustrayant les deux intégrales, la factorisation de Q16 supprime le facteur $e^{\gamma_n(t)}-1$. Comme $\gamma_n=R_n\omega$,
$$
Q_n(z+1)-Q_n(z)
=\frac{n!}{R_n^{\,n-1}}\int_0^1 e^{zR_n\omega(t)}\omega(t)^{-(n-1)}\,\mathrm dt .
$$
Par Q9, l’intégrale vaut le coefficient de rang $n-1$ de $w\mapsto e^{zR_nw}$, soit $(zR_n)^{n-1}/(n-1)!$. Donc **$Q_n(z+1)-Q_n(z)=nz^{n-1}$**.

### Question 28

Puisque $\operatorname{Re}(z\gamma_n(t))\leq R_n|z|$, la propriété $\mathcal P$ donne
$$
|Q_n(z)|\leq\frac{n!}{cR_n^{\,n-1}}e^{R_n|z|}.
$$
Pour $n\geq1$, on a $n!\leq n^n$ et $R_n\geq2\pi n$.

Comme $n\leq2^{n-1}$ par récurrence, on obtient $n!/R_n^{\,n-1}\leq n/(2\pi)^{n-1}\leq1$.

Enfin, $R_n\leq3\pi n$.

**La borne demandée vaut avec $a=1/c$ et $b=3\pi$.**

### Question 29

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
