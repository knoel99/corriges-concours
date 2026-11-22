# ENS MP-MPI — Mathématiques C 2026 · Corrigé brut

*Corrigé rédigé par IA, non officiel.*

On travaille dans l'espace euclidien $\mathbb R^n$. Pour un fermé convexe non vide $C$, $\Pi_C$ désigne la projection sur $C$. On note $I$ l'application identité. Un point $s\in C$ est solution forte si $\langle G(s),x-s\rangle\geq0$ pour tout $x\in C$, et solution faible si $\langle G(x),x-s\rangle\geq0$ pour tout $x\in C$. La monotonie de $G$ signifie que $\langle G(v)-G(u),v-u\rangle\geq0$ pour tous $u,v$.

## Partie I — Inégalités variationnelles et projection sur un convexe fermé

### A — Inégalités variationnelles

### Question 1

Soit $x_\ast$ une solution forte. Pour tout $x\in C$, la monotonie donne

$$\langle G(x),x-x_\ast\rangle\geq\langle G(x_\ast),x-x_\ast\rangle\geq0.$$

Comme $x_\ast\in C$, c'est une **solution faible**.

### Question 2

**a)** Pour $0<\lambda\leq1$, le point $x_\lambda=x_\ast+\lambda(x-x_\ast)$ appartient à $C$ par convexité. L'inégalité faible en ce point s'écrit $0\leq\langle G(x_\lambda),x_\lambda-x_\ast\rangle=\lambda\langle G(x_\lambda),x-x_\ast\rangle$. On divise par $\lambda$.

**b)** Lorsque $\lambda\to0^+$, la continuité donne $G(x_\lambda)\to G(x_\ast)$. L'inégalité de a) devient $\langle G(x_\ast),x-x_\ast\rangle\geq0$ pour tout $x\in C$. Ainsi $x_\ast$ est une **solution forte**.

### Question 3

**a)** Un convexe compact non vide de $\mathbb R$ est un segment $[a,b]$. Si $G(a)\geq0$, le point $a$ est solution forte car $G(a)(x-a)\geq0$ sur ce segment. De même, si $G(b)\leq0$, $b$ convient. Dans le cas restant, $G(a)<0<G(b)$ et la continuité fournit une racine de $G$ dans le segment. En cette racine, le produit de l'inégalité forte est identiquement nul. Le cas $a=b$ est inclus dans les deux premiers cas.

**b)** Prenons $C=[-1,1]$ et $G(x)=-x$. Pour qu'un point $s\in C$ soit solution faible, le test $x=-1$ impose $1(-1-s)\geq0$, donc $s\leq-1$. Le test $x=1$ impose $-(1-s)\geq0$, donc $s\geq1$. Ces exigences sont incompatibles.

### Question 4

**a)** En dimension un, la monotonie signifie que $G$ est croissante au sens large. Écrivons $C=[a,b]$. Si $G$ ne prend aucune valeur négative sur $C$, le point $a$ vérifie $G(x)(x-a)\geq0$ pour tout $x\in C$. Sinon, posons $s=\sup\{u\in C:G(u)<0\}\in C$. Pour $x<s$, un point $u>x$ à valeur $G(u)<0$ existe, donc $G(x)\leq G(u)<0$. Pour $x>s$, on a $G(x)\geq0$ par définition de la borne supérieure. Au point $s$, le facteur $x-s$ s'annule. Dans tous les cas $G(x)(x-s)\geq0$, donc $s$ est solution faible.

**b)** Pour tout $n\geq1$, prenons le segment $C=\{te_1:-1\leq t\leq1\}$ et $G(x)=\sigma(x_1)e_1$, où $\sigma(t)=-1$ pour $t<0$ et $\sigma(t)=1$ pour $t\geq0$. Le produit de monotonie vaut $(\sigma(t)-\sigma(u))(t-u)\geq0$. Pour un candidat $se_1$ avec $s<0$, le test $x=e_1$ donne un produit strictement négatif. Si $s\geq0$, le test $x=-e_1$ fait de même. Il n'existe donc **aucune solution forte**.

![Figure 1 — Le saut de −1 à +1 conserve la monotonie. L’origine est solution faible. La valeur retenue au saut, σ(0) = 1, exclut une solution forte en zéro.](figures/q04-saut-monotone.svg)

### B — Projection sur un convexe fermé

### Question 5

Fixons $c\in C$ et $R=\|y-c\|$. Le sous-ensemble $K=C\cap\overline B(y,R)$ est non vide, fermé et borné. Il est compact en dimension finie. La fonction continue $x\mapsto\|y-x\|$ y atteint son minimum. Hors de $K$ sa valeur est strictement supérieure à $R$, qui est une valeur atteinte en $c$. Le minimum sur $K$ réalise donc l'infimum sur $C$.

### Question 6

Posons $x=\Pi_C(y)$, $x'=\Pi_C(y')$, $d=x-x'$ et $E=\|x\|^2-\|x'\|^2-2\langle y',d\rangle$. En utilisant l'inégalité de projection au point $x'$ avec test $x$, on a $\langle x'-y',d\rangle\geq0$. Ainsi $E=\|d\|^2+2\langle x'-y',d\rangle\geq0$.

Au point $x$ avec test $x'$, on obtient $\langle x-y,d\rangle\leq0$. Or $E=2\langle x-y',d\rangle-\|d\|^2$. Par suite

$$E\leq2\langle y-y',d\rangle-\|d\|^2=\|y-y'\|^2-\|(y-y')-d\|^2\leq\|y-y'\|^2.$$

## Partie II — Un cas d'existence de solution et théorème du minimax de von Neumann

### Question 7

On a $y_{j+1}=y_j-\eta G(x_j)$ et $x_j=\Pi_C(y_j)$. La monotonie de $G$ donne $\langle G(x),x_j-x\rangle\leq\langle G(x_j),x_j-x\rangle$. Pour l'égalité, reprenons les expressions du sujet, avec $D_j(x)=\|x\|^2-\|x_j\|^2-2\langle y_j,x-x_j\rangle$ et $B_j=\|x_j\|^2-\|x_{j+1}\|^2-2\langle y_{j+1},x_j-x_{j+1}\rangle$. En développant $D_j(x)-D_{j+1}(x)+B_j$, les termes de normes se simplifient, laissant

$$2\langle y_{j+1}-y_j,x-x_j\rangle=2\eta\langle G(x_j),x_j-x\rangle.$$

### Question 8

Puisque $C$ est compact et $G$ continue, $R=\max_{x\in C}\|x\|$ et $M=\max_{x\in C}\|G(x)\|$ sont finis. La question 6 appliquée à $y_j,y_{j+1}$ donne $B_j\leq\|y_j-y_{j+1}\|^2\leq\eta^2M^2$. De plus $D_j(x)=\|x-y_j\|^2-\|x_j-y_j\|^2\geq0$ par minimalité du projeté. Comme $y_1=0$, $D_1(x)\leq R^2$.

Pour $\bar x_N=N^{-1}\sum_{j=1}^Nx_j\in C$ par convexité, sommons 7. La somme des différences de $D_j$ se télescope. Il vient pour tout $x\in C$

$$\langle G(x),\bar x_N-x\rangle\leq\frac{R^2+N\eta^2M^2}{2N\eta}.$$

Choisissons $\eta=N^{-1/2}$ dans la construction de la suite. Le membre de droite vaut $(R^2+M^2)/(2\sqrt N)$, indépendamment de $x$. Pour $N$ assez grand, $\widetilde x_\varepsilon=\bar x_N$ convient.

### Question 9

Appliquons 8 avec $\varepsilon=1/k$. La suite obtenue dans $C$ possède une sous-suite convergente vers un point $s\in C$ par compacité. Fixons $x\in C$ et passons à la limite le long de cette sous-suite dans $\langle G(x),\widetilde x_{1/k}-x\rangle\leq1/k$. On trouve $\langle G(x),x-s\rangle\geq0$. La sous-suite ayant été choisie avant $x$, cette inégalité vaut pour tout $x\in C$. Ainsi $s$ est faible et, par la question 2, **solution forte**.

### Question 10

**a)** $G(a,b)=(-Ab,A^{\mathsf T}a)$ est linéaire en dimension finie, donc continue. Pour $u=a'-a$, $v=b'-b$, le produit de monotonie vaut $-\langle Av,u\rangle+\langle A^{\mathsf T}u,v\rangle=0$. L'opérateur est donc monotone.

**b)** Le produit des simplexes $\Delta_m\times\Delta_n$ est non vide, convexe, fermé et borné, donc compact. La question 9 fournit une solution forte $(a_\ast,b_\ast)$. Notons $P(a,b)=\langle a,Ab\rangle$. L'inégalité forte donne $P(a,b_\ast)\leq P(a_\ast,b)$ pour tout $(a,b)$. En fixant successivement $b=b_\ast$ et $a=a_\ast$, on obtient

$$P(a,b_\ast)\leq v=P(a_\ast,b_\ast)\leq P(a_\ast,b).$$

Ainsi $\inf_b P(a_\ast,b)=v$ et, pour tout $a$, $\inf_b P(a,b)\leq P(a,b_\ast)\leq v$. Par suite $\sup_a\inf_b P(a,b)=v$. De même $\sup_a P(a,b_\ast)=v$ et, pour tout $b$, $\sup_a P(a,b)\geq P(a_\ast,b)\geq v$. Donc **$\sup_a\inf_b P(a,b)=\inf_b\sup_a P(a,b)=v$**.

![Figure 2 — Pour la matrice diagonale de coefficients 2 et 1, le maximum de l’enveloppe inférieure et le minimum de l’enveloppe supérieure valent tous deux 2/3.](figures/q10-minimax.svg)

## Partie III — Itérations de Krasnoselskii–Mann

### Question 11

En dimension un, la translation $F(x)=x+1$ préserve les distances, donc est $1$-lipschitzienne, et l'équation $x+1=x$ n'a pas de solution.

### Question 12

En dimension un, $F(x)=-x$ préserve les distances et fixe $x_\ast=0$. L'itération directe partant de $x_1=1$ donne $x_k=(-1)^{k-1}$, qui possède les deux valeurs d'adhérence distinctes $1$ et $-1$.

### Question 13

Puisque $F(x_\ast)=x_\ast$, on a $\|F(x_k)-x_\ast\|\leq\|x_k-x_\ast\|$. La relation $x_{k+1}=(1-\theta)x_k+\theta F(x_k)$, où $0<\theta<1$, et l'inégalité triangulaire donnent

$$\|x_{k+1}-x_\ast\|\leq(1-\theta)\|x_k-x_\ast\|+\theta\|F(x_k)-x_\ast\|\leq\|x_k-x_\ast\|.$$

### Question 14

Pour deux vecteurs $u,v$, le développement des carrés scalaires donne

$$\|(1-\theta)u+\theta v\|^2=(1-\theta)\|u\|^2+\theta\|v\|^2-\theta(1-\theta)\|u-v\|^2.$$

En prenant $u=x_k-x_\ast$ et $v=F(x_k)-x_\ast$, le membre de gauche vaut $\|x_{k+1}-x_\ast\|^2$ et $u-v=x_k-F(x_k)$. C'est l'égalité demandée.

### Question 15

La borne $\|F(x_k)-x_\ast\|\leq\|x_k-x_\ast\|$ et 14 donnent, après sommation,

$$\theta(1-\theta)\sum_{k=1}^N\|F(x_k)-x_k\|^2\leq\|x_1-x_\ast\|^2-\|x_{N+1}-x_\ast\|^2\leq\|x_1-x_\ast\|^2.$$

La série à termes positifs converge car $\theta(1-\theta)>0$. Son terme général tend donc vers zéro et $\|x_{k+1}-x_k\|=\theta\|F(x_k)-x_k\|\to0$.

### Question 16

Par 13, la suite est bornée, donc possède une sous-suite $x_{k_j}\to z$ en dimension finie. Par 15, le résidu $F(x_{k_j})-x_{k_j}$ tend vers zéro. La continuité de $F$ montre que $F(z)=z$. En appliquant 13 à ce point fixe $z$, la suite des distances $\|x_k-z\|$ est décroissante et positive ou nulle. Une de ses sous-suites converge vers zéro, donc sa limite est zéro. Ainsi **toute la suite converge vers le point fixe $z$**.

## Partie IV — Théorème de Baillon–Haddad et descente de gradient

### Question 17

Pour $u,x\in\mathbb R^n$ et $0<t\leq1$, la convexité donne $(f(u+t(x-u))-f(u))/t\leq f(x)-f(u)$. Lorsque $t\to0^+$, on obtient $\langle\nabla f(u),x-u\rangle\leq f(x)-f(u)$. Avec $u=x_\ast$ et $\nabla f(x_\ast)=0$, il vient $f(x_\ast)\leq f(x)$ pour tout $x$. Le minimum est global.

### Question 18

Pour $f$ de classe $C^2$, la hessienne est symétrique par le théorème de Schwarz. Pour $x,v$ fixés, la restriction $t\mapsto f(x+tv)$ est convexe et de classe $C^2$. Sa dérivée seconde en zéro est positive ou nulle, donc $v^{\mathsf T}\nabla^2 f(x)v\geq0$ pour tout $v$. La hessienne est symétrique positive.

### Question 19

**a)** Posons $d=x'-x$. Le théorème fondamental du calcul donne

$$f(x')-f(x)-\langle\nabla f(x),d\rangle=\int_0^1\langle\nabla f(x+td)-\nabla f(x),d\rangle\,dt.$$

Si $\nabla f$ est $L$-lipschitzienne, l'intégrande est majoré par $Lt\|d\|^2$ par Cauchy-Schwarz. L'intégration donne la propriété (P), c'est-à-dire une majoration par $L\|d\|^2/2$.

**b)** Appliquons (P) en prenant $x'=x-\nabla f(x)/L$. La substitution donne $f(x')\leq f(x)-\|\nabla f(x)\|^2/(2L)$. Comme $f(x_\ast)\leq f(x')$, on obtient $\|\nabla f(x)\|^2\leq2L(f(x)-f(x_\ast))$.

**c)** Fixons $x$ et considérons $g(u)=f(u)-\langle\nabla f(x),u\rangle$. Elle est convexe, de classe $C^1$, et $\nabla g(x)=0$. Son minimum est réalisé en $x$ par 17. L'ajout d'une fonction linéaire ne change pas le reste $g(v)-g(u)-\langle\nabla g(u),v-u\rangle$, donc $g$ vérifie (P). Appliquons b) à $g$ au point $x'$ et à son minimum $x$. On trouve

$$f(x')\geq f(x)+\langle\nabla f(x),x'-x\rangle+\frac1{2L}\|\nabla f(x')-\nabla f(x)\|^2.$$

**d)** En additionnant c) et l'inégalité obtenue par échange de $x$ et $x'$, on trouve, avec $w=\nabla f(x')-\nabla f(x)$ et $d=x'-x$,

$$\|w\|^2\leq L\langle w,d\rangle\leq L\|w\|\,\|d\|.$$

Si $w\ne0$, on divise par sa norme. Si $w=0$, la borne cherchée est immédiate. Cela prouve que (P) implique la propriété $L$-lipschitzienne du gradient. L'implication réciproque est a).

### Question 20

Notons $H(x)=\nabla^2 f(x)$. Si (i) est vraie, pour tout vecteur $v$ et tout $t>0$, le quotient $(\nabla f(x+tv)-\nabla f(x))/t$ est de norme au plus $L\|v\|$. Par dérivation, $\|H(x)v\|\leq L\|v\|$. D'après 18, $H(x)$ est symétrique positive. En appliquant la borne à un vecteur propre non nul, on obtient (iii).

Par le théorème spectral, $H(x)$ admet une base orthonormée propre. Dans cette base, $LI_n-H(x)$ est diagonale avec coefficients $L-\lambda_i$. Elle est positive exactement lorsque $\lambda_i\leq L$ pour tout $i$. La positivité de $H(x)$ donne déjà $\lambda_i\geq0$, donc (ii) et (iii) sont équivalentes.

Enfin, sous (iii), développer $v$ dans la base propre donne $\|H(x)v\|^2=\sum_i\lambda_i^2v_i^2\leq L^2\|v\|^2$. Pour $d=x'-x$, le théorème fondamental appliqué composante par composante donne $\nabla f(x')-\nabla f(x)=\int_0^1H(x+td)d\,dt$. La norme est au plus $L\|d\|$. On retrouve (i).

### Question 21

La question 19(d) donne $\|w\|^2\leq L\langle w,d\rangle$ avec les mêmes notations. Pour $F=I-(2/L)\nabla f$, il vient

$$\|F(x')-F(x)\|^2=\|d\|^2-\frac4L\langle w,d\rangle+\frac4{L^2}\|w\|^2\leq\|d\|^2.$$

Ainsi **$I-(2/L)\nabla f$ est $1$-lipschitzienne** sous les seules hypothèses $C^1$, convexité et gradient $L$-lipschitzien.

### Question 22

Le point $x_\ast$ annule le gradient, donc est fixe pour $F=I-(2/L)\nabla f$. Avec $\theta=1/2$, on a $x_k+\theta(F(x_k)-x_k)=x_k-\nabla f(x_k)/L$. La suite de descente est exactement l'itération de la partie III. Par 16 et 21, elle converge vers un point fixe $z$ de $F$. La relation $F(z)=z$ signifie $\nabla f(z)=0$, donc, par 17, $z$ minimise $f$. La continuité donne finalement

$$\boxed{x_k\to z,\qquad f(x_k)\to f(z)=\inf_{\mathbb R^n}f.}$$

![Figure 3 — Pour f(x,y) = (x² + 3y²)/2 et L = 4, chaque pas multiplie la première coordonnée par 3/4 et la seconde par 1/4. Les courbes grises représentent les niveaux de f.](figures/q22-descente.svg)
