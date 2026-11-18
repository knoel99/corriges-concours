# CCINP PC — Mathématiques 2024 · Corrigé brut

*Corrigé rédigé par IA, non officiel. Signalez toute erreur.*

## Exercice 1 — Racine cubique d’une matrice

### Partie I — Étude d’un exemple

### Question 1

La trace vaut 9 et le déterminant 8. Le polynôme caractéristique est donc $X^2-9X+8=(X-1)(X-8)$. Les deux valeurs propres sont réelles et distinctes. En prenant comme colonnes de $P$ deux vecteurs propres associés respectivement à 1 et 8, on obtient une matrice inversible et $A=PDP^{-1}$.

### Question 2

Pour toute matrice $B$, on a $\Delta^3=(P^{-1}BP)^3=P^{-1}B^3P$. Si $B^3=A$, alors $\Delta^3=P^{-1}AP=D$. Réciproquement, si $\Delta^3=D$, alors $B^3=PDP^{-1}=A$.

### Question 3

On a $D\Delta=\Delta^4=\Delta D$. Écrivons $\Delta=\begin{pmatrix}a&b\\c&d\end{pmatrix}$. Les deux produits ont pour termes hors diagonale respectivement $(b,8c)$ et $(8b,c)$, dans l'ordre des positions $(1,2)$ et $(2,1)$.

On a donc $b=c=0$ et $\Delta$ est diagonale.

### Question 4

Par Q3, une racine de $D$ est de la forme $\operatorname{diag}(a,d)$ et vérifie $a^3=1$ et $d^3=8$. Le cube étant bijectif sur $\mathbb R$, elle vaut nécessairement $\Delta_0=\operatorname{diag}(1,2)$.

Cette matrice a bien pour cube $D$. La bijection de Q2 donne donc l'unique racine réelle de $A$, à savoir $P\Delta_0P^{-1}$.

### Partie II — Dans un plan euclidien

### Question 5

Dans la base orthonormée directe $\mathcal B$, la matrice $M$ est celle de la rotation d'angle orienté $\theta$ modulo $2\pi$.

### Question 6

La composée de trois rotations d'angle $\theta/3$ est la rotation d'angle $\theta$. Une racine cubique demandée est donc
$$
\begin{pmatrix}\cos(\theta/3)&-\sin(\theta/3)\\
\sin(\theta/3)&\cos(\theta/3)\end{pmatrix}.
$$

### Question 7

Dans une base orthonormée du plan, $N$ représente une isométrie de déterminant $-1$, donc une réflexion par rapport à une droite. Une réflexion est involutive, d'où $N^2=I_2$, puis $N^3=N$. La matrice $N$ est ainsi sa propre racine cubique.

### Partie III — Racines cubiques et diagonalisation

#### III.1 — Existence d’une racine cubique polynomiale

### Question 8

Comme $H_p(\lambda)=\lambda I_p$, la matrice $\sqrt[3]{\lambda}\,I_p$ a pour cube $H_p(\lambda)$. La racine cubique réelle existe pour tout $\lambda\in\mathbb R$.

### Question 9

Soit $p_k$ la dimension de l'espace propre de $\lambda_k$.

Puisque $A$ est diagonalisable sur $\mathbb R$, il existe une matrice inversible $P$ et une matrice diagonale par blocs $D$ de blocs $\lambda_k I_{p_k}$ telles que $A=PDP^{-1}$.

Par Q8, remplaçons chaque bloc de $D$ par $\sqrt[3]{\lambda_k}I_{p_k}$ pour obtenir une matrice $R$. Les produits par blocs donnent $R^3=D$, d'où $(PRP^{-1})^3=PDP^{-1}=A$.

Cette racine s'écrit même $p(A)$, où $p$ est le polynôme d'interpolation
$$
p(X)=\sum_{k=1}^d\sqrt[3]{\lambda_k}\prod_{j\ne k}\frac{X-\lambda_j}{\lambda_k-\lambda_j}.
$$
En effet, $p$ prend la valeur $\sqrt[3]{\lambda_k}$ en $\lambda_k$, donc $p(D)=R$.

#### III.2 — Réduction d’une racine cubique

### Question 10

Si un $\lambda_k$ était nul, un vecteur propre non nul associé appartiendrait à $\ker A$. Cela contredirait l'inversibilité de $A$. Ainsi tous les $\lambda_k$ sont non nuls.

### Question 11

Pour $z=re^{i\varphi}$, l'équation impose $r^3=\rho$ et $3\varphi\equiv\theta\pmod{2\pi}$. Elle donne les trois nombres suivants, indexés par $k=0,1,2$
$$
z_k=\rho^{1/3}\exp\!\left(i\,\frac{\theta+2k\pi}{3}\right).
$$
Ils vérifient tous l'équation et sont distincts, car $\rho>0$ et leurs arguments sont distincts modulo $2\pi$. Les autres valeurs entières de $k$ redonnent ces trois nombres.

### Question 12

Par Q10 et Q11, chaque facteur $X^3-\lambda_k$ possède trois racines complexes distinctes, toutes simples. Si un nombre $z$ annulait deux facteurs d'indices distincts, on aurait $z^3=\lambda_j=\lambda_k$, ce qui est impossible. Le produit $Q$ est donc scindé à racines simples sur $\mathbb C$.

### Question 13

Le polynôme $q(X)=\prod_{k=1}^d(X-\lambda_k)$ annule $A$, car il s'annule sur chaque coefficient diagonal dans une diagonalisation de $A$. Si $B^3=A$, alors $Q(B)=q(B^3)=q(A)=0$.

Par Q12, $B$ admet ainsi un polynôme annulateur scindé à racines simples sur $\mathbb C$. Le critère de diagonalisation donne le résultat sur $\mathbb C$.

## Exercice 2 — La fonction logarithme de Gamma

### Partie I — Existence

### Question 14

Pour $x>0$ fixé, le développement limité $\ln(1+t)=t+O(t^2)$ en zéro donne
$$
\begin{aligned}x\ln(1+1/n)&=\frac{x}{n}+O_x(n^{-2}),\\
\ln(1+x/n)&=\frac{x}{n}+O_x(n^{-2}).\end{aligned}
$$
Ainsi $|u_n(x)|=O_x(n^{-2})$, et la série converge absolument pour chaque $x>0$. Elle converge donc simplement sur l'intervalle demandé.

### Question 15

Chaque $u_n$ est de classe $C^1$ sur $]0,+\infty[$ par composition. On a
$$
\begin{aligned}u_n'(x)&=\ln(1+1/n)-\frac1{n+x}\\
&=\frac{x}{n(n+x)}+\varepsilon_n,\\
\varepsilon_n&=\ln(1+1/n)-1/n.\end{aligned}
$$
La suite $\varepsilon_n$ est indépendante de $x$. Le développement limité de Q14 donne $\varepsilon_n=O(n^{-2})$, d'où la convergence absolue.

### Question 16

Pour $x\in[a,b]\subset]0,+\infty[$, Q15 donne $|u_n'(x)|\le b/n^2+|\varepsilon_n|$. La série de ces majorants converge d'après Q15 et le critère des séries de Riemann. La série des dérivées converge donc normalement sur chaque segment.

### Question 17

Par Q14, la série des $u_n$ converge simplement. Chaque terme est $C^1$ par Q15, et la série dérivée converge uniformément sur chaque segment par Q16. Le théorème de dérivation terme à terme donne $\phi\in C^1$ et
$$
\phi'(x)=-1/x+\sum_{n\ge1}\bigl(\ln(1+1/n)-1/(n+x)\bigr).
$$
Chaque terme de la somme, ainsi que la fonction $x\mapsto-1/x$, est croissant. En comparant les sommes partielles en deux abscisses et en passant à la limite, on obtient la croissance de $\phi'$.

Pour la relation de récurrence, posons $\phi_N(x)=-\ln x+\sum_{n=1}^Nu_n(x)$. La différence des termes d'indice $n$ vaut $\ln((n+1)/n)-\ln((n+x+1)/(n+x))$. Ces deux sommes télescopent, ce qui donne
$$
\begin{aligned}
\phi_N(x+1)-\phi_N(x)
&=-\ln(x+1)+\ln x+\ln(N+1)-\ln\frac{N+x+1}{x+1}\\
&=\ln x+\ln\frac{N+1}{N+x+1}.
\end{aligned}
$$
En passant à la limite, on trouve $\phi(x+1)-\phi(x)=\ln x$. Enfin, $u_n(1)=0$ pour tout $n$ et $\ln 1=0$, donc $\phi(1)=0$. Les quatre conditions sont vérifiées.

### Partie II — Unicité

### Question 18

Comme $\phi$ et $g$ vérifient la condition (ii), on a $h(x+1)-h(x)=\ln x-\ln x=0$. Les deux fonctions étant $C^1$, la dérivation donne $h'(x+1)=h'(x)$ pour tout $x>0$.

### Question 19

Comme $p\le p+x\le p+1$ et que $\phi'$ et $g'$ sont croissantes, on a
$$
\phi'(p)-g'(p+1)\le h'(p+x)\le\phi'(p+1)-g'(p).
$$
La dérivation de (ii) pour $g$ donne $g'(p+1)=g'(p)+1/p$. La borne inférieure est donc $h'(p)-1/p$. La même dérivation pour $\phi$ donne $\phi'(p+1)=\phi'(p)+1/p$. La borne supérieure vaut donc $h'(p)+1/p$.

On obtient $|h'(p+x)-h'(p)|\le1/p$.

### Question 20

Pour $x\in]0,1]$, Q18 donne $h'(x+p)=h'(x)$ et $h'(p)=h'(1)$ pour tout entier $p\ge1$. Par Q19, $|h'(x)-h'(1)|\le1/p$.

En faisant tendre $p$ vers l'infini, on a donc $h'(x)=h'(1)$ sur $]0,1]$. Chaque réel strictement positif est la somme d'un élément de $]0,1]$ et d'un entier naturel. La périodicité prolonge cette égalité à tout $]0,+\infty[$.

### Question 21

Par Q20, $h$ est affine sur l'intervalle. Si $h(x)=ax+b$, la périodicité de Q18 implique $a=0$. Comme $\phi(1)=g(1)=0$, on obtient $b=0$, donc $g=\phi$.

### Partie III — Formule de duplication

### Question 22

Par les propriétés de l'exponentielle et du logarithme,
$$
\begin{aligned}
\exp\left(\sum_{n=1}^{N}u_n(1/2)\right)
&=\prod_{n=1}^N \exp\bigl(u_n(1/2)\bigr)\\
&=\left(\prod_{n=1}^N\sqrt{\frac{n+1}{n}}\right)
\left(\prod_{n=1}^N\frac{2n}{2n+1}\right).
\end{aligned}
$$
Le premier produit vaut $\sqrt{N+1}$ par télescopage. Le produit des entiers pairs de 2 à $2N$ vaut $2^NN!$. Le produit des impairs de 3 à $2N+1$ est donc $(2N+1)!/(2^NN!)$, le facteur 1 étant sans effet. On obtient la valeur demandée
$$
\frac{\sqrt{N+1}}{2N+1}\,\frac{(2^NN!)^2}{(2N)!}.
$$

### Question 23

La formule de Stirling donne, pour des termes strictement positifs,
$$
\frac{(2^NN!)^2}{(2N)!}
\sim\frac{4^N(2\pi N)(N/e)^{2N}}{\sqrt{4\pi N}(2N/e)^{2N}}
=\sqrt{\pi N}.
$$
Ainsi le membre droit de Q22 tend vers $\sqrt\pi/2$. La série de Q14 converge en $1/2$, donc l'exponentielle de sa somme vaut $\sqrt\pi/2$. Puisque $-\ln(1/2)=\ln 2$, la définition de $\phi$ donne $\phi(1/2)=\ln 2+\ln(\sqrt\pi/2)=\tfrac12\ln\pi$.

Enfin, $\phi(1)=0$ par Q17, donc $\psi(1)=0$.

### Question 24

La fonction $\psi$ est $C^1$ par composition, et
$$
\psi'(x)=\ln 2+\tfrac12\phi'(x/2)+\tfrac12\phi'((x+1)/2).
$$
La dérivée $\psi'$ est croissante en tant que somme à coefficients positifs de fonctions croissantes et d'une constante.

Ensuite, les termes en $\phi((x+1)/2)$ s'annulent dans la différence $\psi(x+1)-\psi(x)$. Il reste $\ln 2+\phi(x/2+1)-\phi(x/2)=\ln 2+\ln(x/2)=\ln x$ par Q17. Enfin, Q23 donne $\psi(1)=0$. Les quatre conditions portent sur $\psi$ et sa dérivée. L'unicité de Q21 donne $\psi=\phi$, ce qui est la formule demandée après report du terme constant au membre droit.

## Exercice 3 — Temps d’attente avant une collision

### Partie I — Une expression de l’espérance

### Question 25

Deux tirages sont nécessaires pour observer une répétition. Parmi $n+1$ tirages, au moins deux coïncident par le principe des tiroirs. Pour tout entier $j$ entre 2 et $n+1$, la suite de tirages $1,2,\ldots,j-1,1$ réalise une première collision au rang $j$ et a une probabilité positive.

L'image de $T_n$ est donc $\{2,\ldots,n+1\}$.

### Question 26

Les valeurs de $Z$ appartiennent à $\{1,\ldots,n\}^k$. Pour tout $(a_1,\ldots,a_k)$ de cet ensemble, l'indépendance des $X_i$ donne
$$
\begin{aligned}\mathbb P\bigl(Z=(a_1,\ldots,a_k)\bigr)&=\prod_{i=1}^{k}\mathbb P(X_i=a_i)\\&=n^{-k}.\end{aligned}
$$
Cette probabilité est positive et identique pour chacun des $n^k$ tuples. La loi est donc uniforme sur cet ensemble, qui est aussi l'image de $Z$.

### Question 27

Le premier terme a $n$ choix, le deuxième $n-1$, et au rang $k$ il reste $n-k+1$ choix. Ainsi $|A|=n!/(n-k)!$.

L'événement $\{T_n>k\}$ signifie que les $k$ premiers tirages sont distincts, donc c'est $\{Z\in A\}$. Par Q26, sa probabilité vaut $|A|/n^k$, soit $n!/((n-k)!n^k)$.

### Question 28

La variable est bornée par $n+1$ d'après Q25, donc intégrable. Pour toute issue, $T_n=\sum_{\ell=0}^n\mathbf 1_{\{T_n>\ell\}}$, puisque exactement $T_n$ des indices satisfont l'inégalité. Par linéarité de l'espérance et par Q27, y compris $\ell=0$,
$$
\begin{aligned}\mathbb E(T_n)&=\sum_{\ell=0}^n\mathbb P(T_n>\ell)\\&=\sum_{\ell=0}^n\frac{n!}{(n-\ell)!\,n^\ell}.\end{aligned}
$$

### Partie II — Une expression intégrale de l’espérance

### Question 29

Pour tout $k\in\mathbb N$, l'intégrande $t^ke^{-t}$ est continu sur $[0,+\infty[$, en lisant $t^0=1$ si $k=0$.

À l'infini, $t^ke^{-t/2}$ tend vers zéro, donc $0\le t^ke^{-t}\le e^{-t/2}$ pour $t$ assez grand. L'intégrale converge par comparaison.

### Question 30

Pour $k=0$, l'intégrale vaut $[-e^{-t}]_0^{+\infty}=1=0!$. Supposons $I_k=k!$ pour un entier $k\ge0$. Sur $[0,R]$, l'intégration par parties donne
$$
\int_0^R t^{k+1}e^{-t}\,dt=-R^{k+1}e^{-R}+(k+1)\int_0^Rt^ke^{-t}\,dt.
$$
La contribution au bord 0 est nulle et celle en $R$ tend vers zéro par croissance comparée. Les deux intégrales convergent par Q29. En passant à la limite, $I_{k+1}=(k+1)I_k=(k+1)!$, ce qui termine la récurrence.

### Question 31

Le développement du binôme exprime l'intégrande comme somme finie de multiples des fonctions intégrables de Q29. L'intégrale converge et par linéarité et Q30,
$$
\begin{aligned}
\int_0^{+\infty}(1+t/n)^ne^{-t}\,dt
&=\sum_{k=0}^n\binom nk n^{-k}\int_0^{+\infty}t^ke^{-t}\,dt\\
&=\sum_{k=0}^n\binom nk n^{-k}k!
=\mathbb E(T_n),
\end{aligned}
$$
la dernière égalité résultant de Q28.

### Partie III — Un équivalent de l’espérance

#### III.1 — Étude de la suite $J_n$

### Question 32

Le changement de variable $t=n+v$ transforme la borne inférieure $n$ en 0, laisse la borne supérieure infinie et donne $dt=dv$. On a donc
$$
J_n=e^{-n}\int_0^{+\infty}(2+v/n)^n e^{-v}\,dv.
$$
On peut effectuer la substitution sur un segment et passer à la limite puisque l'intégrale initiale converge.

### Question 33

Pour tout $v\ge0$, l'inégalité donnée fournit $1+v/(2n)\le e^{v/(2n)}$. Les deux membres sont positifs. À la puissance $n$ et après multiplication par $e^{-v}$, on obtient une majoration par $e^{-v/2}$. Il vient $0\le K_n\le\int_0^{+\infty}e^{-v/2}dv=2$.

### Question 34

Par Q32, $J_n=(2/e)^nK_n$. Comme $0<2/e<1$, la suite géométrique tend vers zéro. Q33 donne $0\le J_n\le2(2/e)^n$, donc $J_n\to0$.

#### III.2 — Étude de la suite $I_n$

### Question 35

Le changement de variable transforme les bornes 0 et $n$ en 0 et $\sqrt n$ et donne $dt=\sqrt n\,du$. Par définition de $f_n$,
$$
I_n=\sqrt n\int_0^{\sqrt n}(1+u/\sqrt n)^ne^{-u\sqrt n}\,du
=\sqrt n\int_0^{+\infty}f_n(u)\,du.
$$
La valeur de l'intégrande au point de raccord n'affecte pas l'intégrale.

### Question 36

Pour $0<u<\sqrt n$, le logarithme vaut $n\ln(1+u/\sqrt n)-u\sqrt n$. Or $u/\sqrt n\in]0,1[$, à l'intérieur du rayon de convergence de la série entière de $\ln(1+v)$. En remplaçant par $\sum_{k\ge1}(-1)^{k-1}v^k/k$, le terme d'indice 1 annule $u\sqrt n$. Il reste
$$
\ln(f_n(u))=\sum_{k=2}^{+\infty}\frac{(-1)^{k-1}u^k}{k\,n^{k/2-1}}.
$$

### Question 37

Pour $0<u<\sqrt n$, les termes en valeur absolue de Q36 sont $n(u/\sqrt n)^k/k$. Ils décroissent vers zéro. Le reste après le terme $-u^2/2$ est donc compris entre 0 et $u^3/(3\sqrt n)$ par le critère des séries alternées. On obtient la première inégalité demandée. Comme $u/\sqrt n<1$, il en résulte
$$
\begin{aligned}\ln(f_n(u))&\le -u^2/2+u^3/(3\sqrt n)\\&\le -u^2/6.\end{aligned}
$$

### Question 38

La fonction $u\mapsto e^{-u^2/2}$ est continue et, pour $u\ge1$, majorée par $e^{-u/2}$. Elle est donc intégrable sur $[0,+\infty[$.

Pour tout $u>0$ fixé, on a $u<\sqrt n$ à partir d'un certain rang, et Q37 donne alors $\ln(f_n(u))\to-u^2/2$. Par continuité de l'exponentielle, $f_n(u)\to e^{-u^2/2}$.

Les $f_n$ sont continues par morceaux. Q37 donne $0\le f_n(u)\le e^{-u^2/6}$ pour $u<\sqrt n$, et la même inégalité vaut au-delà puisque $f_n$ est nulle.

Le majorant indépendant de $n$ est intégrable par comparaison à $e^{-u/6}$ pour $u\ge1$. Le théorème de convergence dominée donne la convergence des intégrales vers $\int_0^{+\infty}e^{-u^2/2}\,du$.

#### III.3 — Conclusion

### Question 39

Q31 donne $\mathbb E(T_n)=I_n+J_n$. Par Q35 et Q38, $I_n/\sqrt n$ tend vers l'intégrale gaussienne, de valeur admise $\sqrt{\pi/2}$. Par Q34, $J_n/\sqrt n$ tend vers zéro. La limite du quotient est strictement positive, donc
$$
\boxed{\mathbb E(T_n)\sim\sqrt{\frac{\pi n}{2}}.}
$$
