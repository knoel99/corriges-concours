# BCE ECT — Mathématiques T (conception BSB) 2025 · Corrigé brut

*Corrigé rédigé par IA, non officiel. Signalez toute erreur.*

Épreuve de 4 heures, sans document ni calculatrice (règle graduée seule autorisée). Quatre exercices, 52 questions.

## Exercice 1

### Première partie – Étude de $A$ et de ses puissances

**(1)**
$$A-I=\begin{pmatrix}-1&-1&0\\1&1&0\\4&4&0\end{pmatrix}.$$
Chaque ligne de $A-I$ est de la forme $(c,c,0)$ et chaque colonne de $A-I$ est de la forme $(x,-x,y)^T$ ou nulle ; le produit d'une ligne par une colonne vaut $-cx+cx+0=0$. Donc
$$\boxed{(A-I)^2=\begin{pmatrix}0&0&0\\0&0&0\\0&0&0\end{pmatrix}}$$

**(2)** $A$ et $I$ commutent, donc $(A-I)^2=A^2-2A+I$. La question 1 donne $A^2-2A+I=0$, soit
$$A(2I-A)=I.$$
$A$ est donc inversible et $A^{-1}=2I-A$, c'est-à-dire $A^{-1}=\alpha A+\beta I$ avec
$$\boxed{\begin{aligned}\alpha&=-1\\\beta&=2\end{aligned}}$$

**(3)**
$$\boxed{A^{-1}=2I-A=\begin{pmatrix}2&1&0\\-1&0&0\\-4&-4&1\end{pmatrix}}$$

**(4)** D'après la question 2, $A^2-2A+I=0$, donc $A^2=2A-I$.

**(5)** Pour $n\in\mathbb N$, notons $\mathcal P(n)$ : « $A^n=nA-(n-1)I$ ».

- **Initialisation** : $0\cdot A-(0-1)I=I=A^0$ : $\mathcal P(0)$ est vraie.
- **Hérédité** : supposons $\mathcal P(n)$ vraie pour un $n\in\mathbb N$. Avec la question 4 :
$$\begin{aligned}
A^{n+1}&=A\cdot A^n=nA^2-(n-1)A\\
&=n(2A-I)-(n-1)A\\
&=(n+1)A-nI.
\end{aligned}$$
$\mathcal P(n+1)$ est vraie.

Par récurrence, $A^n=nA-(n-1)I$ pour tout $n\in\mathbb N$.

**(6)** D'après la question 4, $A^2-2A+I=0$ : le polynôme $X^2-2X+1=(X-1)^2$ est un polynôme annulateur de $A$, de degré 2.

**(7)** Toute valeur propre de $A$ est racine d'un polynôme annulateur, donc de $(X-1)^2$, dont la seule racine est $1$. **$A$ admet au plus une valeur propre**, qui ne peut être que $1$.

**(8)**
$$A\begin{pmatrix}0\\0\\1\end{pmatrix}=\begin{pmatrix}0\\0\\1\end{pmatrix}=1\cdot\begin{pmatrix}0\\0\\1\end{pmatrix}.$$
Ce vecteur est **non nul** : c'est un vecteur propre de $A$, associé à la valeur propre $1$.

**(9)** D'après la question 7, la seule valeur propre possible est $1$. On cherche $(a,b)\neq(0,0)$ tel que
$$A\begin{pmatrix}a\\b\\0\end{pmatrix}=\begin{pmatrix}-b\\a+2b\\4a+4b\end{pmatrix}=\begin{pmatrix}a\\b\\0\end{pmatrix}.$$
Les trois équations $-b=a$, $a+2b=b$ et $4a+4b=0$ se réduisent toutes à $a=-b$. Par exemple
$$\boxed{\begin{aligned}a&=1\\b&=-1\end{aligned}}$$
Le vecteur $\begin{pmatrix}1\\-1\\0\end{pmatrix}$ est non nul et vérifie $A\begin{pmatrix}1\\-1\\0\end{pmatrix}=\begin{pmatrix}1\\-1\\0\end{pmatrix}$ : c'est un vecteur propre de $A$ associé à $1$, non colinéaire au précédent.

**(10)** Supposons par l'absurde $A$ diagonalisable : il existe $P$ inversible et $D$ diagonale telles que $D=P^{-1}AP$.

De $AP=PD$, chaque colonne $C_i$ de $P$ vérifie $AC_i=d_iC_i$, et $C_i$ est non nulle car $P$ est inversible.

Le coefficient diagonal $d_i$ de $D$ est donc une valeur propre de $A$.

Les coefficients diagonaux de $D$ ils valent tous $1$ (question 7), donc $D=I$. Alors
$$\begin{aligned}
A &= PDP^{-1}\\
&= PIP^{-1}\\
&= I,
\end{aligned}$$
ce qui est faux (par exemple le coefficient d'indice $(1,1)$ de $A$ vaut $0$). Donc **$A$ n'est pas diagonalisable**.

### Deuxième partie – Étude de suites

**(11)**
$$AX_0=\begin{pmatrix}0-2+0\\1+4+0\\4+8+3\end{pmatrix}=\begin{pmatrix}-2\\5\\15\end{pmatrix},\qquad X_1=AX_0+B=\begin{pmatrix}-3\\6\\19\end{pmatrix}.$$
Donc $u_1=-3$, $v_1=6$, $w_1=19$.

**(12)**
$$AF+B=\begin{pmatrix}1\\\omega-2\\4\omega-1\end{pmatrix}+\begin{pmatrix}-1\\1\\4\end{pmatrix}=\begin{pmatrix}0\\\omega-1\\4\omega+3\end{pmatrix}.$$
$F=AF+B$ équivaut à $\omega=0$, $-1=\omega-1$ et $3=4\omega+3$, c'est-à-dire
$$\boxed{\omega=0}$$

**(13)** Pour tout $n\in\mathbb N$, en retranchant $F=AF+B$ à $X_{n+1}=AX_n+B$ :
$$\begin{aligned}
X_{n+1}-F&=AX_n-AF\\
&=A(X_n-F).
\end{aligned}$$

**(14)** Récurrence : pour $n=0$, $A^0(X_0-F)=X_0-F$. Si $X_n-F=A^n(X_0-F)$, alors par la question 13,
$$X_{n+1}-F=A(X_n-F)=A^{n+1}(X_0-F).$$
Donc $X_n-F=A^n(X_0-F)$ pour tout $n\in\mathbb N$.

**(15)** Avec la question 5 et $X_0-F=\begin{pmatrix}1\\3\\0\end{pmatrix}$ :
$$A(X_0-F)=\begin{pmatrix}-3\\7\\16\end{pmatrix},$$
$$\begin{aligned}
X_n&=F+\big(nA-(n-1)I\big)(X_0-F)\\
&=\begin{pmatrix}0\\-1\\3\end{pmatrix}+n\begin{pmatrix}-3\\7\\16\end{pmatrix}-(n-1)\begin{pmatrix}1\\3\\0\end{pmatrix}.
\end{aligned}$$
Pour tout $n\in\mathbb N$ :
$$\boxed{\begin{aligned}u_n&=1-4n\\v_n&=2+4n\\w_n&=3+16n\end{aligned}}$$
(on retrouve $X_0$ pour $n=0$ et $X_1$ pour $n=1$).

## Exercice 2

$P_m(x)=2mx^3+(2-m)x^2+(1-2m)x+(m-1)$.

### Première partie – Le cas $m=-\frac12$

**(1)**
$$\begin{aligned}
f(2)&=-8+\frac52\cdot4+4-\frac32\\
&=6-\frac32=\boxed{\frac92}
\end{aligned}$$

**(2)** Pour $x\neq0$, $f(x)=x^3\left(-1+\frac5{2x}+\frac2{x^2}-\frac3{2x^3}\right)$, et la parenthèse tend vers $-1$ en $\pm\infty$.

Comme $x^3\to-\infty$ en $-\infty$ et $x^3\to+\infty$ en $+\infty$ :
$$\boxed{\begin{aligned}\lim_{x\to-\infty}f(x)&=+\infty\\\lim_{x\to+\infty}f(x)&=-\infty\end{aligned}}$$

**(3)** $f$ est dérivable sur $\mathbb R$ (polynôme) et
$$f'(x)=-3x^2+5x+2=-(3x+1)(x-2).$$
Le trinôme $-(3x+1)(x-2)$, de coefficient dominant $-3<0$, est négatif à l'extérieur de ses racines $-\frac13$ et $2$, positif entre elles. On calcule $f(2)=\frac92$ et
$$\begin{aligned}
f\left(-\tfrac13\right)&=\frac1{27}+\frac5{18}-\frac23-\frac32\\
&=\frac{2+15-36-81}{54}=-\frac{50}{27}.
\end{aligned}$$
**Erreur d'énoncé** : le sujet donne $f\left(-\frac13\right)=-\frac{11}6$ ; la valeur exacte est $-\frac{50}{27}$ (le rapport du jury le confirme). Cela ne change rien à la suite.

| $x$ | −∞ | | $-\frac13$ | | 2 | | +∞ |
|---|---|---|---|---|---|---|---|
| $f'(x)$ | | − | 0 | + | 0 | − | |
| $f$ | +∞ | ↘ | $-\frac{50}{27}$ | ↗ | $\frac92$ | ↘ | −∞ |

**(4)** $f(0)=-\frac32$. Sur $[0,2]\subset\left[-\frac13,2\right]$, $f$ est continue et strictement croissante, avec $f(0)=-\frac32<0$ et $f(2)=\frac92>0$.

D'après le théorème de la bijection (corollaire du théorème des valeurs intermédiaires), **$f$ s'annule exactement une fois sur $[0,2]$**. (Cette racine est $\frac12$ : $f\left(\frac12\right)=-\frac18+\frac58+1-\frac32=0$.)

**(5)** Les lignes 1 et 2 définissent la fonction Python `f` qui, à un réel `x`, associe $f(x)=-x^3+\frac52x^2+2x-\frac32$. Elle est passée en argument à `Racine`, qui doit pouvoir calculer les valeurs de $f$ aux points testés.

**(6)** Exécution de `Racine(0,2,f)` :

- $a=0$, $b=2$, $b-a=2>0{,}001$ : `m = 1.0`, affiché. $f(1)=-1+\frac52+2-\frac32=2\neq0$, et $f(0)f(1)=-\frac32\times2<0$ : on pose $b=1$.
- $a=0$, $b=1$, $b-a=1>0{,}001$ : `m = 0.5`, affiché. $f(0{,}5)=-0{,}125+0{,}625+1-1{,}5=0$ (calcul exact en machine, toutes ces valeurs étant des fractions dyadiques) : la fonction renvoie `m`.

Valeurs affichées : **`1.0` puis `0.5`** ; valeur renvoyée : **`0.5`**.

### Deuxième partie – Le cas $m=2$

**(7)** $g(-1)=-4+3+1=0$ : $-1$ est racine de $g$.

**(8)** On cherche $\varphi(x)=ax^2+bx+c$ avec $(x+1)(ax^2+bx+c)=ax^3+(a+b)x^2+(b+c)x+c=4x^3-3x+1$. Par identification :

$a=4$, $a+b=0$, $b+c=-3$, $c=1$, soit $b=-4$ (et $b+c=-3$ est bien vérifiée).
$$\boxed{\varphi(x)=4x^2-4x+1=(2x-1)^2}$$

**(9)** $g(x)=(x+1)(2x-1)^2=0\iff x=-1$ ou $x=\frac12$. Les racines de $g$ sont **$-1$ et $\frac12$** (racine double).

### Troisième partie – Étude des points communs

**(10)**
$$\begin{aligned}
\int_{-1}^{1/2}g(x)\,dx&=\Big[x^4-\frac32x^2+x\Big]_{-1}^{1/2}\\
&=\left(\frac1{16}-\frac38+\frac12\right)-\left(1-\frac32-1\right)\\
&=\frac3{16}+\frac32=\boxed{\frac{27}{16}}
\end{aligned}$$

**(11)** Pour tout réel $m$ :
$$\begin{aligned}
P_m(-1)&=-2m+(2-m)-(1-2m)+(m-1)=0,\\
P_m\left(\tfrac12\right)&=\frac m4+\frac{2-m}4+\frac{1-2m}2+m-1=0.
\end{aligned}$$
Les points $A=(-1,0)$ et $B=\left(\frac12,0\right)$ appartiennent donc à toutes les courbes $\mathscr C_m$.

**(12)** $P_1(x)=2x^3+x^2-x$ et $P_0(x)=2x^2+x-1$, donc
$$\begin{aligned}
h(x)&=2x^3-x^2-2x+1\\
&=x^2(2x-1)-(2x-1)\\
&=(2x-1)(x-1)(x+1).
\end{aligned}$$

| $x$ | −∞ | | −1 | | $\frac12$ | | 1 | | +∞ |
|---|---|---|---|---|---|---|---|---|---|
| $x+1$ | | − | 0 | + | | + | | + | |
| $2x-1$ | | − | | − | 0 | + | | + | |
| $x-1$ | | − | | − | | − | 0 | + | |
| $h(x)$ | | − | 0 | + | 0 | − | 0 | + | |

**(13)** Sur $\left[-1,\frac12\right]$, $h=P_1-P_0\geqslant0$ : la courbe $\mathscr C_1$ est au-dessus de $\mathscr C_0$. L'aire cherchée (en unités d'aire) vaut
$$\begin{aligned}
\int_{-1}^{1/2}h(x)\,dx&=\Big[\frac{x^4}2-\frac{x^3}3-x^2+x\Big]_{-1}^{1/2}\\
&=\left(\frac1{32}-\frac1{24}-\frac14+\frac12\right)-\left(\frac12+\frac13-1-1\right)\\
&=\frac{23}{96}+\frac{112}{96}=\boxed{\frac{45}{32}}
\end{aligned}$$

**(14)** Pour tout $m$ et tout $x$, $P_m(x)=P_0(x)+m\,h(x)$ (le coefficient de $m$ dans $P_m(x)$ est $2x^3-x^2-2x+1=h(x)$).

Un point d'abscisse $x$ est commun à toutes les courbes si et seulement si $P_m(x)$ ne dépend pas de $m$, c'est-à-dire $h(x)=0$ : $x\in\left\{-1,\frac12,1\right\}$.

Les deux premiers donnent $A$ et $B$ ; pour $x=1$, $P_m(1)=P_0(1)=2$. Le troisième point commun est
$$\boxed{C=(1,\,2)}$$

**(15)** $P_0(x)=2x^2+x-1=(x+1)(2x-1)$, et avec la question 12 :
$$\begin{aligned}
P_m(x)&=(x+1)(2x-1)+m(x+1)(2x-1)(x-1)\\
&=(x+1)(2x-1)\big(mx-m+1\big).
\end{aligned}$$
Pour $m>0$, la troisième racine est $\alpha_m=\frac{m-1}m=1-\frac1m$ (elle diffère de $-1$ et de $\frac12$ sauf pour $m=\frac12$ et $m=2$, où elle coïncide avec l'une d'elles). Donc
$$\boxed{\lim_{m\to+\infty}\alpha_m=1}$$

## Exercice 3

Notons, pour chaque jeton, $1$ la face bleue (numéro 1) ; l'univers est l'ensemble des $2^3=8$ triplets de faces, équiprobables (faces équiprobables et indépendantes).

**(1)** $X$ est la somme de trois variables de Bernoulli indépendantes de paramètre $\frac12$ (« le jeton montre sa face bleue ») :
$$\begin{aligned}X\hookrightarrow\mathcal B\left(3,\frac12\right)\\E(X)&=\frac32\\V(X)&=3\cdot\frac12\cdot\frac12=\frac34\end{aligned}.$$

**(2)** Les faces non bleues sont rouge, jaune et vert : trois couleurs différentes entre elles et différentes du bleu. Donc :

- si $X=3$, seule la couleur bleue est visible : $Y=1$ ;
- si $X=2$, on voit le bleu et une autre couleur : $Y=2$ ;
- si $X=1$, on voit le bleu et deux autres couleurs : $Y=3$ ;
- si $X=0$, on voit rouge, jaune et vert : $Y=3$.

$$\boxed{Y(\Omega)=\{1,2,3\}}$$

**(3)** D'après la question 2, $Y=1$ si et seulement si les trois faces visibles sont bleues : $(Y=1)=(X=3)$, et
$$\begin{aligned}
P(Y=1) &= P(X=3)\\
&= \frac18.
\end{aligned}$$

**(4)** De même, $(Y=2)=(X=2)$, donc
$$\begin{aligned}
P(Y=2) &= P(X=2)\\
&= \binom32\frac18\\
&= \frac38.
\end{aligned}$$

**(5)** $P(Y=3)=1-\frac18-\frac38=\frac12$.

| $y$ | 1 | 2 | 3 |
|---|---|---|---|
| $P(Y=y)$ | $\frac18$ | $\frac38$ | $\frac12$ |

**(6)**
$$\begin{aligned}
E(Y) &= 1\cdot\frac18+2\cdot\frac38+3\cdot\frac48\\
&= \frac{1+6+12}8\\
&= \frac{19}8.
\end{aligned}$$

**(7)**
$$\begin{aligned}
E(Y^2)&=\frac18+4\cdot\frac38+9\cdot\frac48=\frac{49}8,\\
V(Y)&=E(Y^2)-E(Y)^2=\frac{392-361}{64}=\boxed{\frac{31}{64}}
\end{aligned}$$

**(8)** $(X=1)$ : exactement une face bleue ; alors $Y=3$ automatiquement. En notant la face visible de $A$, de $B$, puis de $C$, les événements élémentaires sont :
$$(\text{bleu}_1,\ \text{jaune}_3,\ \text{vert}_4),\quad(\text{rouge}_2,\ \text{bleu}_1,\ \text{vert}_4),\quad(\text{rouge}_2,\ \text{jaune}_3,\ \text{bleu}_1).$$
Chacun a pour probabilité $\frac18$, donc $P((X=1)\cap(Y=3))=\frac38$.

**(9)** D'après la question 2, chaque valeur de $X$ détermine celle de $Y$ :
$$\begin{aligned}\mathbf A&=P(X=0)=\frac18\\\mathbf B&=P(X=1)=\frac38\\\mathbf C&=P(X=2)=\frac38\\\mathbf D&=P(X=3)=\frac18\end{aligned}.$$

**(10)**
$$\begin{aligned}
E(XY)&=1\cdot3\cdot\frac38+2\cdot2\cdot\frac38+3\cdot1\cdot\frac18\\
&=\frac{9+12+3}8=3,
\end{aligned}$$
d'où, par la formule de Koenig-Huygens,
$$\begin{aligned}
\mathrm{Cov}(X,Y) &= E(XY)-E(X)E(Y)\\
&= 3-\frac32\cdot\frac{19}8\\
&= \boxed{-\frac9{16}}
\end{aligned}$$

**(11)** Si $X$ et $Y$ étaient indépendantes, leur covariance serait nulle. Comme $\mathrm{Cov}(X,Y)\neq0$, **$X$ et $Y$ ne sont pas indépendantes**. (Par exemple $P((X=0)\cap(Y=1))=0\neq P(X=0)P(Y=1)=\frac1{64}$.)

**(12)** Le jeton $A$ montre le numéro 1 ou 2, le jeton $B$ le numéro 1 ou 3, le jeton $C$ le numéro 1 ou 4.

Les $8$ produits possibles sont 1, 2, 3, 4, $6=2\cdot3$, $8=2\cdot4$, $12=3\cdot4$ et $24=2\cdot3\cdot4$, tous distincts. Chacun correspond à un seul triplet de faces, de probabilité $\frac18$ :
$$Z(\Omega)=\{1,2,3,4,6,8,12,24\},$$
et $P(Z=z)=\frac18$ pour tout $z\in Z(\Omega)$ : $Z$ suit la loi uniforme sur ces huit valeurs.

**(13)**
$$\begin{aligned}
E(Z) &= \frac{1+2+3+4+6+8+12+24}8\\
&= \frac{60}8\\
&= \boxed{\frac{15}2}
\end{aligned}$$

## Exercice 4

$G(x)=(x+1)e^{-x}$.

**(1)** En $-\infty$ : $x+1\to-\infty$ et $e^{-x}\to+\infty$, donc par produit $\lim_{x\to-\infty}G(x)=-\infty$.

En $+\infty$ : $G(x)=\dfrac x{e^x}+e^{-x}$ ; par croissances comparées $\dfrac x{e^x}\to0$, et $e^{-x}\to0$, donc $\lim_{x\to+\infty}G(x)=0$.

**(2)** $G$ est dérivable sur $\mathbb R$ et
$$\begin{aligned}
G'(x)&=e^{-x}-(x+1)e^{-x}\\
&=-xe^{-x}.
\end{aligned}$$

**(3)** $e^{-x}>0$, donc $G'(x)$ a le signe de $-x$.

| $x$ | −∞ | | 0 | | +∞ |
|---|---|---|---|---|---|
| $G'(x)$ | | + | 0 | − | |
| $G$ | −∞ | ↗ | 1 | ↘ | 0 |

**(4)** $G'$ est dérivable et
$$\begin{aligned}
G''(x)&=-e^{-x}+xe^{-x}\\
&=(x-1)e^{-x}.
\end{aligned}$$
$G''$ s'annule en $1$ en changeant de signe (négative avant, positive après) : la courbe de $G$ admet un point d'inflexion d'abscisse $1$, le point $\left(1,\frac2e\right)$.

**(5)** $f$ est positive ($te^{-t}\geqslant0$ pour $t\geqslant0$), continue sur $\mathbb R$ sauf peut-être en $0$ (elle y est en fait continue, $f(0)=0$).

La fonction $t\mapsto-(t+1)e^{-t}=-G(t)$ a pour dérivée $-G'(t)=te^{-t}$ (question 2). Pour $A\geqslant0$ :
$$\int_0^Ate^{-t}\,dt=\Big[-G(t)\Big]_0^A=1-G(A)\xrightarrow[A\to+\infty]{}1$$
(question 1). Donc $\int_{-\infty}^{+\infty}f(t)\,dt=0+1=1$ : **$f$ est une densité de probabilité**.

**(6)** La fonction de répartition de $X$ est $x\mapsto\int_{-\infty}^xf(t)\,dt$. Si $x<0$, elle vaut $0$. Si $x\geqslant0$, elle vaut
$$\int_0^xte^{-t}\,dt=1-G(x)=1-(x+1)e^{-x}.$$
C'est la fonction $F$ : **$F$ est la fonction de répartition de $X$**.

**(7)**
$$\begin{aligned}
P(X>1) &= 1-F(1)\\
&= 2e^{-1}\\
&= \boxed{\frac2e}
\end{aligned}$$

**(8)** Soit $x\geqslant0$.

Avec $u(t)=t^2$ et $v(t)=-e^{-t}$, dérivables à dérivées continues sur $[0,x]$, $u'(t)=2t$, $v'(t)=e^{-t}$ :
$$\begin{aligned}
\int_0^xt^2e^{-t}\,dt&=\Big[-t^2e^{-t}\Big]_0^x+\int_0^x2te^{-t}\,dt\\
&=-x^2e^{-x}+2\int_0^xte^{-t}\,dt.
\end{aligned}$$

**(9)** $X$ admet une espérance si $\int_{-\infty}^{+\infty}tf(t)\,dt$ converge. Cette fonction est nulle sur $]-\infty,0[$ et égale à $t^2e^{-t}\geqslant0$ sur $[0,+\infty[$. Par la question 8 et la question 5 :
$$\int_0^xt^2e^{-t}\,dt=-x^2e^{-x}+2\left(1-(x+1)e^{-x}\right).$$
Par croissances comparées, $x^2e^{-x}=\frac{x^2}{e^x}\to0$ et $(x+1)e^{-x}\to0$ en $+\infty$. L'intégrale converge et vaut $2$ :
$$\boxed{E(X)=2}$$

**FIN**
