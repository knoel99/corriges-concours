# BCE ECT — Mathématiques T (conception BSB) 2026 · Corrigé brut

*Corrigé rédigé par IA, non officiel. Signalez toute erreur.*

Épreuve de 4 heures, sans document ni calculatrice (règle graduée seule autorisée). Trois exercices, 67 questions.

## Exercice 1

Pour $n\in\mathbb N$ et $x\in\mathbb R$, $f_n(x)=\dfrac{x^n}{n!}e^{1-x}$.

### Partie I : Quelques exemples

**(1)(a)** $f_1$ est dérivable sur $\mathbb R$ (produit de fonctions dérivables). Pour tout réel $x$ :
$$\begin{aligned}
f_1'(x)&=e^{1-x}+x\cdot\left(-e^{1-x}\right)\\
&=(1-x)e^{1-x}.
\end{aligned}$$

**(1)(b)** Comme $e^{1-x}>0$, $f_1'(x)$ a le signe de $1-x$.

Ainsi $f_1'>0$ sur $]-\infty,1[$ et $f_1'<0$ sur $]1,+\infty[$.

**$f_1$ est strictement croissante sur $]-\infty,1]$ et strictement décroissante sur $[1,+\infty[$**, de maximum $f_1(1)=1$.

**(1)(c)** $f_1'$ est dérivable sur $\mathbb R$ et
$$\begin{aligned}
f_1''(x)&=-e^{1-x}+(1-x)\left(-e^{1-x}\right)\\
&=(-1-1+x)e^{1-x}\\
&=(x-2)e^{1-x}.
\end{aligned}$$
$f_1''(x)$ a le signe de $x-2$ : elle est strictement négative sur $]-\infty,2[$ et strictement positive sur $]2,+\infty[$.

La dérivée seconde s'annule en changeant de signe en $2$ et seulement en $2$ : $f_1$ admet **exactement un point d'inflexion**, de coordonnées
$$\boxed{\left(2,\ \frac2e\right)}$$
car $f_1(2)=2e^{-1}$.

**(2)(a)** $\displaystyle\lim_{x\to+\infty}e^x=+\infty$. Quand $x\to-\infty$, $1-x\to+\infty$, donc $e^{1-x}\to+\infty$, et $x\to-\infty$. Par produit,
$$\boxed{\lim_{x\to-\infty}f_1(x)=-\infty}$$

**(2)(b)** Pour tout réel $x$, $e^{1-x}=e\cdot e^{-x}=\dfrac e{e^x}$, donc $f_1(x)=e\,\dfrac x{e^x}$.

**(2)(c)** Par croissances comparées, $\dfrac{x}{e^x}\xrightarrow[x\to+\infty]{}0$. Donc
$$\boxed{\lim_{x\to+\infty}f_1(x)=0}$$

**(3)** Tableau de variations de $f_1$ :

| $x$ | $-\infty$ | | $1$ | | $+\infty$ |
|---|---|---|---|---|---|
| $f_1'(x)$ | | $+$ | $0$ | $-$ | |
| $f_1$ | $-\infty$ | ↗ | $1$ | ↘ | $0$ |

**(4)(a)** $f_2$ est dérivable sur $\mathbb R$ et, pour tout réel $x$,
$$\begin{aligned}
f_2'(x)&=xe^{1-x}-\frac{x^2}2e^{1-x}\\
&=\frac{x(2-x)}2e^{1-x}.
\end{aligned}$$

**(4)(b)** $e^{1-x}>0$, donc $f_2'(x)$ a le signe de $x(2-x)$, trinôme de racines $0$ et $2$, négatif à l'extérieur des racines. Donc :

- $f_2$ est strictement décroissante sur $]-\infty,0]$ ;
- $f_2$ est strictement croissante sur $[0,2]$ ;
- $f_2$ est strictement décroissante sur $[2,+\infty[$.

Valeurs : $f_2(0)=0$ et $f_2(2)=2e^{-1}=\frac2e$.

**(5)(a)** Quand $x\to-\infty$, $\frac{x^2}2\to+\infty$ et $e^{1-x}\to+\infty$. Par produit,
$$\boxed{\lim_{x\to-\infty}f_2(x)=+\infty}$$

**(5)(b)** Pour tout réel $x$, $f_2(x)=\dfrac e2\cdot\dfrac{x^2}{e^x}$. Par croissances comparées, $\dfrac{x^2}{e^x}\xrightarrow[x\to+\infty]{}0$, donc
$$\boxed{\lim_{x\to+\infty}f_2(x)=0}$$

**(6)** Tableau de variations de $f_2$ :

| $x$ | $-\infty$ | | $0$ | | $2$ | | $+\infty$ |
|---|---|---|---|---|---|---|---|
| $f_2'(x)$ | | $-$ | $0$ | $+$ | $0$ | $-$ | |
| $f_2$ | $+\infty$ | ↘ | $0$ | ↗ | $\frac2e$ | ↘ | $0$ |

### Partie II : Quelques utilisations de l'informatique

**(7)**
```python
def fact(n):
    f = 1
    for k in range(1,n+1):
        f = f*k
    return f
```
Pour $n=0$, la boucle n'est pas exécutée et la fonction renvoie $1=0!$.

**(8)**
```python
def f(n,x):
    return x**n/fact(n)*np.exp(1-x)
```
Cette fonction accepte aussi un tableau `x` (calcul terme à terme), ce qu'utilise le script de la question 9.

**(9)** On compare aux études de la partie I.

- $f_1(-1)=-e^2\approx-7{,}4<0$, $f_1$ a pour maximum $1$, atteint en $1$, et tend vers $0$ en $+\infty$.
  Le **graphique 3** part d'environ $-7{,}4$, atteint un maximum égal à $1$ vers $x=1$ et décroît vers $0$ : c'est la courbe de $f_1$.
- $f_2(-1)=\frac{e^2}2\approx3{,}7$, $f_2$ décroît jusqu'à $f_2(0)=0$, croît jusqu'à $f_2(2)=\frac2e\approx0{,}74$, puis décroît vers $0$. C'est le **graphique 1**.
- Le graphique 2 n'est ni l'un ni l'autre : il présente un maximum vers $x=5$ et prend une valeur négative en $-1$, ce qui ne convient ni à $f_1$ (maximum en $1$) ni à $f_2$ (positive).
  C'est en fait la courbe de $f_5$, dont le maximum $\frac{5^5}{5!}e^{-4}\approx0{,}48$ est atteint en $5$.

Conclusion : **le graphique 3 représente $f_1$ et le graphique 1 représente $f_2$.**

### Partie III : Intégrales définies à partir des fonctions $f_n$

**(10)(a)** Une primitive de $t\mapsto e^{1-t}$ est $t\mapsto-e^{1-t}$. Pour tout $A\geqslant0$ :
$$I_0(A)=\Big[-e^{1-t}\Big]_0^A=e-e^{1-A}.$$

**(10)(b)** $e^{1-A}\xrightarrow[A\to+\infty]{}0$, donc $I_0(A)$ admet une limite finie quand $A\to+\infty$ : l'intégrale $I_0$ converge et
$$\boxed{I_0=e}$$

**(11)(a)** Soit $A\geqslant0$. On pose $u(t)=t$ et $v(t)=-e^{1-t}$, dérivables à dérivées continues sur $[0,A]$.

Avec $u'(t)=1$ et $v'(t)=e^{1-t}$, par intégration par parties :
$$\begin{aligned}
I_1(A)&=\int_0^Ate^{1-t}\,dt\\
&=\Big[-te^{1-t}\Big]_0^A+\int_0^Ae^{1-t}\,dt\\
&=-Ae^{1-A}+I_0(A).
\end{aligned}$$

**(11)(b)** Avec la question 10(a) :
$$I_1(A)=-Ae^{1-A}-e^{1-A}+e.$$

**(11)(c)** $Ae^{1-A}=e\,\dfrac A{e^A}\xrightarrow[A\to+\infty]{}0$ par croissances comparées, et $e^{1-A}\to0$. Donc $I_1(A)\to e$ : l'intégrale $I_1$ converge et
$$\boxed{I_1=e}$$

### Partie IV : Une variable à densité

**(12)** On vérifie les trois conditions.

- **Positivité** : $g(t)=0$ si $t<0$ et $g(t)=\frac1ete^{1-t}\geqslant0$ si $t\geqslant0$.
- **Continuité** : $g$ est continue sur $]-\infty,0[$ et sur $[0,+\infty[$ ; elle est donc continue sur $\mathbb R$ sauf peut-être en $0$.
  Elle l'est en fait aussi en $0$, car $g(0)=0$.
- **Intégrale** : $\int_{-\infty}^0g(t)\,dt=0$ et $\int_0^{+\infty}g(t)\,dt=\frac1eI_1=1$ (question 11(c)). Donc $\int_{-\infty}^{+\infty}g(t)\,dt$ converge et vaut $1$.

**$g$ est une densité de probabilité.**

**(13)(a)** $G(x)=\int_{-\infty}^xg(t)\,dt$.

- Si $x<0$ : $G(x)=0$.
- Si $x\geqslant0$ : $G(x)=\frac1eI_1(x)$, et avec la question 11(b),
$$\begin{aligned}
G(x)&=\frac1e\left(-xe^{1-x}-e^{1-x}+e\right)\\
&=1-(x+1)e^{-x}.
\end{aligned}$$

$$\boxed{G(x)=\begin{cases}0&\text{si }x<0\\1-(x+1)e^{-x}&\text{si }x\geqslant0\end{cases}}$$

**(13)(b)** $X$ admet une espérance si $\int_{-\infty}^{+\infty}tg(t)\,dt$ converge. Ici l'intégrande est nulle sur $]-\infty,0[$, et sur $[0,+\infty[$
$$tg(t)=\frac1et^2e^{1-t}=\frac2e\,f_2(t).$$
D'après la partie III, $I_2=\int_0^{+\infty}f_2(t)\,dt$ converge et vaut $e$. Donc l'intégrale converge et
$$\boxed{E(X)=\frac2e\,I_2=2}$$

## Exercice 2

$u_0=1$, $v_0=2$ et, pour tout $n\in\mathbb N$, $u_{n+1}=5u_n+2v_n$ et $v_{n+1}=3u_n+6v_n$.

### Partie I : Variations des suites $(u_n)$ et $(v_n)$

**(1)** Récurrence sur $n$.

- **Initialisation** : $u_0=1$ et $v_0=2$ sont des entiers strictement positifs : $\mathcal P_0$ est vraie.
- **Hérédité** : si $u_n$ et $v_n$ sont des entiers strictement positifs, alors $u_{n+1}=5u_n+2v_n$ et $v_{n+1}=3u_n+6v_n$ sont des entiers (sommes et produits d'entiers) strictement positifs (sommes de termes strictement positifs). $\mathcal P_{n+1}$ est vraie.

Par récurrence, **$\mathcal P_n$ est vraie pour tout $n\in\mathbb N$**.

**(2)** Pour tout $n\in\mathbb N$, d'après la question 1 :
$$\begin{aligned}
u_{n+1}-u_n&=4u_n+2v_n>0,\\
v_{n+1}-v_n&=3u_n+5v_n>0.
\end{aligned}$$
Les suites $(u_n)$ et $(v_n)$ sont **strictement croissantes**.

### Partie II : Terme général à l'aide de deux suites auxiliaires

**(3)** $x_0=u_0+v_0=3$ et $y_0=3u_0-2v_0=3-4=-1$.

**(4)** Pour tout $n\in\mathbb N$ :
$$\begin{aligned}
x_{n+1}&=(5u_n+2v_n)+(3u_n+6v_n)\\
&=8u_n+8v_n\\
&=8x_n.
\end{aligned}$$
$(x_n)$ est géométrique de raison $8$ et de premier terme $3$ :
$$\boxed{x_n=3\cdot8^n}$$

**(5)** Pour tout $n\in\mathbb N$ :
$$\begin{aligned}
y_{n+1}&=3(5u_n+2v_n)-2(3u_n+6v_n)\\
&=9u_n-6v_n\\
&=3y_n.
\end{aligned}$$
$(y_n)$ est géométrique de raison $3$ et de premier terme $-1$ :
$$\boxed{y_n=-3^n}$$

**(6)** Soit $n\in\mathbb N$. En ajoutant à la seconde équation le double de la première, on obtient $5u_n=2x_n+y_n$. Puis $v_n=x_n-u_n$. Le système a une unique solution :
$$\boxed{\begin{aligned}u_n&=\frac{2x_n+y_n}5\\v_n&=\frac{3x_n-y_n}5\end{aligned}}$$

**(7)** Avec les questions 4 et 5, pour tout $n\in\mathbb N$ :
$$\begin{aligned}
u_n&=\frac{6\cdot8^n-3^n}5=-\frac15\,3^n+\frac65\,8^n,\\
v_n&=\frac{9\cdot8^n+3^n}5=\frac15\,3^n+\frac95\,8^n.
\end{aligned}$$

### Partie III : Terme général à l'aide d'une relation de récurrence d'ordre 2

**(8)** $u_1=5u_0+2v_0=5+4=9$ et $v_1=3u_0+6v_0=3+12=15$.

**(9)** La relation $(\ast)$ découle de $u_{n+1}=5u_n+2v_n$. Pour tout $n\in\mathbb N$, en utilisant la définition de $u_{n+2}$, celle de $v_{n+1}$, puis $(\ast)$ :
$$\begin{aligned}
u_{n+2}&=5u_{n+1}+2v_{n+1}\\
&=5u_{n+1}+6u_n+12v_n\\
&=5u_{n+1}+6u_n+6(u_{n+1}-5u_n)\\
&=11u_{n+1}-24u_n.
\end{aligned}$$

**(10)** Le discriminant de $X^2-11X+24$ vaut $121-96=25=5^2$. Les racines sont $\frac{11-5}2$ et $\frac{11+5}2$ :
$$\boxed{\begin{aligned}x_1&=3\\x_2&=8\end{aligned}}$$

**(11)** On a $u_n=a\,3^n+b\,8^n$. Pour $n=0$ et $n=1$ :
$$\begin{cases}a+b=1\\3a+8b=9\end{cases}$$
En retranchant trois fois la première équation à la seconde : $5b=6$, donc $b=\frac65$ et $a=1-b=-\frac15$.
$$\boxed{\begin{aligned}a&=-\frac15\\b&=\frac65\end{aligned}}$$

**(12)** Donc, pour tout $n\in\mathbb N$, $u_n=-\frac15\,3^n+\frac65\,8^n$. Par $(\ast)$ :
$$\begin{aligned}
v_n&=\frac12\left(u_{n+1}-5u_n\right)\\
&=\frac12\left(-\frac35\,3^n+\frac{48}5\,8^n+3^n-6\cdot8^n\right)\\
&=\frac12\left(\frac25\,3^n+\frac{18}5\,8^n\right)\\
&=\frac15\,3^n+\frac95\,8^n.
\end{aligned}$$

### Partie IV : Terme général à l'aide des puissances d'une matrice

**(13)(a)** Pour tout $n\in\mathbb N$ :
$$MX_n=\begin{pmatrix}5u_n+2v_n\\3u_n+6v_n\end{pmatrix}=\begin{pmatrix}u_{n+1}\\v_{n+1}\end{pmatrix}=X_{n+1}.$$

**(13)(b)** Récurrence. Pour $n=0$ : $M^0X_0=I_2X_0=X_0$. Si $X_n=M^nX_0$, alors $X_{n+1}=MX_n=M\cdot M^nX_0=M^{n+1}X_0$. Donc $X_n=M^nX_0$ pour tout $n\in\mathbb N$.

**(14)(a)**
$$M^2=\begin{pmatrix}31&22\\33&42\end{pmatrix},$$
$$M^2-11M+24I_2=\begin{pmatrix}31-55+24&22-22\\33-33&42-66+24\end{pmatrix}=\begin{pmatrix}0&0\\0&0\end{pmatrix}.$$

**(14)(b)** Le polynôme $X^2-11X+24$ est un **polynôme annulateur** de $M$.

**(14)(c)** Toute valeur propre de $M$ est racine d'un polynôme annulateur. D'après la question 10, les valeurs propres possibles de $M$ sont **$3$ et $8$**.

**(15)**
$$M\begin{pmatrix}1\\-1\end{pmatrix}=\begin{pmatrix}3\\-3\end{pmatrix}=3\begin{pmatrix}1\\-1\end{pmatrix},\qquad M\begin{pmatrix}2\\3\end{pmatrix}=\begin{pmatrix}16\\24\end{pmatrix}=8\begin{pmatrix}2\\3\end{pmatrix}.$$
Ces deux vecteurs sont non nuls : ce sont des vecteurs propres de $M$, associés respectivement aux valeurs propres **$3$ et $8$**.

**(16)(a)** $P=\begin{pmatrix}1&2\\-1&3\end{pmatrix}$ et $1\times3-2\times(-1)=5\neq0$ : $P$ est inversible et
$$\boxed{P^{-1}=\frac15\begin{pmatrix}3&-2\\1&1\end{pmatrix}}$$

**(16)(b)**
$$MP=\begin{pmatrix}3&16\\-3&24\end{pmatrix}=PD.$$
En multipliant à droite par $P^{-1}$ : $M=PDP^{-1}$, soit $D=P^{-1}MP$ avec $D$ diagonale et $P$ inversible. **$M$ est diagonalisable.**

**(16)(c)** Pour $n=0$ : $PD^0P^{-1}=PP^{-1}=I_2=M^0$. Si $M^n=PD^nP^{-1}$, alors
$$\begin{aligned}
M^{n+1}&=M^nM\\
&=PD^nP^{-1}PDP^{-1}\\
&=PD^{n+1}P^{-1}.
\end{aligned}$$
Par récurrence, $M^n=PD^nP^{-1}$ pour tout $n\in\mathbb N$.

**(17)(a)** $D$ est diagonale, donc $D^n=\begin{pmatrix}3^n&0\\0&8^n\end{pmatrix}$ (coefficients non diagonaux nuls). Puis
$$\begin{aligned}
M^n&=\frac15\begin{pmatrix}1&2\\-1&3\end{pmatrix}\begin{pmatrix}3^n&0\\0&8^n\end{pmatrix}\begin{pmatrix}3&-2\\1&1\end{pmatrix}\\
&=\frac15\begin{pmatrix}3^n&2\cdot8^n\\-3^n&3\cdot8^n\end{pmatrix}\begin{pmatrix}3&-2\\1&1\end{pmatrix}\\
&=\frac15\begin{pmatrix}3^{n+1}+2\cdot8^n&-2\cdot3^n+2\cdot8^n\\-3^{n+1}+3\cdot8^n&2\cdot3^n+3\cdot8^n\end{pmatrix}.
\end{aligned}$$

**(17)(b)** $X_n=M^nX_0$ avec $X_0=\begin{pmatrix}1\\2\end{pmatrix}$ :
$$\begin{aligned}
u_n&=\frac15\left(3^{n+1}+2\cdot8^n-4\cdot3^n+4\cdot8^n\right)=-\frac15\,3^n+\frac65\,8^n,\\
v_n&=\frac15\left(-3^{n+1}+3\cdot8^n+4\cdot3^n+6\cdot8^n\right)=\frac15\,3^n+\frac95\,8^n.
\end{aligned}$$
On retrouve les expressions des questions 7 et 12.

## Exercice 3

### Partie I : Tirage d'un jeton dans l'urne dans le cas $n=4$

**(1)** Pour chaque $k\in\{1,2,3,4\}$, l'urne contient exactement $k$ jetons de numéro bleu $k$, dont les faces rouges portent les numéros $1$ à $k$ : ce sont $(k,1),\dots,(k,k)$.

On obtient $(1,1)$ ; $(2,1),(2,2)$ ; $(3,1),(3,2),(3,3)$ ; $(4,1),(4,2),(4,3),(4,4)$.

Cela fait $1+2+3+4=10$ jetons.

**(2)(a)** $B(\Omega)=\{1,2,3,4\}$ et $R(\Omega)=\{1,2,3,4\}$.

**(2)(b)** Le jeton est tiré au hasard : les $10$ jetons sont équiprobables. L'événement $(B=1)\cap(R=1)$ correspond au seul jeton $(1,1)$, d'où $P((B=1)\cap(R=1))=\frac1{10}$. Aucun jeton n'est $(1,2)$, donc $P((B=1)\cap(R=2))=0$.

**(2)(c)** De même, $P((B=i)\cap(R=j))=\frac1{10}$ si $j\leqslant i$ (un seul jeton $(i,j)$) et $0$ si $j>i$.

| $j\in R(\Omega)$ \\ $i\in B(\Omega)$ | $1$ | $2$ | $3$ | $4$ |
|---|---|---|---|---|
| $1$ | $\frac1{10}$ | $\frac1{10}$ | $\frac1{10}$ | $\frac1{10}$ |
| $2$ | $0$ | $\frac1{10}$ | $\frac1{10}$ | $\frac1{10}$ |
| $3$ | $0$ | $0$ | $\frac1{10}$ | $\frac1{10}$ |
| $4$ | $0$ | $0$ | $0$ | $\frac1{10}$ |

**(3)(a)** On somme chaque colonne : $P(B=i)=\frac i{10}$, soit
$$\begin{aligned}P(B=1)&=\frac1{10}\\P(B=2)&=\frac2{10}\\P(B=3)&=\frac3{10}\\P(B=4)&=\frac4{10}\end{aligned}.$$

**(3)(b)**
$$\begin{aligned}
E(B)&=\frac{1\cdot1+2\cdot2+3\cdot3+4\cdot4}{10}=\frac{30}{10}=3,\\
E(B^2)&=\frac{1+8+27+64}{10}=10.
\end{aligned}$$
Par la formule de Koenig-Huygens,
$$\begin{aligned}V(B)&=E(B^2)-E(B)^2\\&=10-9=\boxed{1}\end{aligned}$$

**(4)(a)** On somme chaque ligne : $P(R=j)=\frac{5-j}{10}$, soit
$$\begin{aligned}P(R=1)&=\frac4{10}\\P(R=2)&=\frac3{10}\\P(R=3)&=\frac2{10}\\P(R=4)&=\frac1{10}\end{aligned}.$$

**(4)(b)**
$$\begin{aligned}
E(R)&=\frac{4+6+6+4}{10}=2,\\
E(R^2)&=\frac{4+12+18+16}{10}=5.
\end{aligned}$$
$$\boxed{\begin{aligned}E(R)&=2\\V(R)&=5-4=1\end{aligned}}$$

**(5)(a)**
$$\begin{aligned}
E(BR)&=\sum_{1\leqslant j\leqslant i\leqslant4}ij\,P((B=i)\cap(R=j))\\
&=\frac1{10}\left(1\cdot1+2\cdot3+3\cdot6+4\cdot10\right)\\
&=\frac{65}{10}=\frac{13}2,
\end{aligned}$$
car $\sum_{j=1}^ij=\frac{i(i+1)}2$ vaut $1,3,6,10$ pour $i=1,2,3,4$.

**(5)(b)** $\mathrm{Cov}(B,R)=E(BR)-E(B)E(R)$, donc
$$\boxed{\mathrm{Cov}(B,R)=\frac{13}2-3\times2=\frac12}$$

**(5)(c)** Si $B$ et $R$ étaient indépendantes, leur covariance serait nulle. Comme $\mathrm{Cov}(B,R)\neq0$, **$B$ et $R$ ne sont pas indépendantes**. (On peut aussi remarquer que $P((B=1)\cap(R=2))=0\neq P(B=1)P(R=2)=\frac3{100}$.)

**(6)** Par linéarité de l'espérance :
$$\begin{aligned}E(G)&=E(B)-E(R)\\&=3-2=\boxed{1}\end{aligned}$$

### Partie II : Temps d'attente du premier et du second tirage du jeton numéroté 1 en bleu

**(7)** Le seul jeton dont le numéro bleu est $1$ est le jeton $(1,1)$. Obtenir le numéro bleu $1$ au $k$-ième tirage, c'est donc tirer ce jeton, ce qui équivaut à $(B_k=1)$ et aussi à $(B_k=1)\cap(R_k=1)$ :
$$\begin{aligned}
S_k &= (B_k=1)\\
&= (B_k=1)\cap(R_k=1).
\end{aligned}$$
Les tirages se font avec remise : à chaque tirage, l'urne contient les mêmes $10$ jetons équiprobables, et d'après la partie I,
$$\begin{aligned}
P(S_k) &= P((B_k=1)\cap(R_k=1))\\
&= \frac1{10}.
\end{aligned}$$

**(8)** Les tirages, avec remise, sont indépendants ; chacun est une épreuve de Bernoulli de succès $S_k$, de probabilité $\frac1{10}$. $T_1$ est le rang du premier succès :
$$\begin{aligned}T_1\hookrightarrow\mathcal G\left(\frac1{10}\right)\\P(T_1=k)&=\left(\frac9{10}\right)^{k-1}\frac1{10}\ \ (k\in\mathbb N^*)\end{aligned}.$$
$$\boxed{\begin{aligned}E(T_1)&=10\\V(T_1)&=\frac{1-\frac1{10}}{\left(\frac1{10}\right)^2}=90\end{aligned}}$$

**(9)(a)** Il faut au moins deux tirages pour obtenir deux fois le jeton : $T_2(\Omega)=\{2,3,4,\dots\}=[\![2,+\infty[\![$.

**(9)(b)** Les $m$ premiers tirages sont $m$ épreuves de Bernoulli indépendantes et de même probabilité de succès $\frac1{10}$. $X_m$ compte le nombre de succès, donc
$$X_m\hookrightarrow\mathcal B\left(m,\frac1{10}\right).$$

**(9)(c)** Soit $k\geqslant2$. Le second succès a lieu au $k$-ième tirage si et seulement si le $k$-ième tirage est un succès et qu'il y a eu exactement un succès lors des $k-1$ premiers tirages. Donc $(T_2=k)=(X_{k-1}=1)\cap S_k$.

**(9)(d)** L'événement $(X_{k-1}=1)$ ne dépend que des $k-1$ premiers tirages et $S_k$ du $k$-ième : ils sont indépendants. Pour tout $k\geqslant2$ :
$$\begin{aligned}
P(T_2=k)&=P(X_{k-1}=1)\,P(S_k)\\
&=\binom{k-1}1\frac1{10}\left(\frac9{10}\right)^{k-2}\cdot\frac1{10}\\
&=\frac{k-1}{100}\left(\frac9{10}\right)^{k-2}.
\end{aligned}$$

### Partie III : Une série statistique

**(10)** Un même joueur joue en général plusieurs parties : son nom apparaît alors sur plusieurs lignes de la table, et `NomJoueur` ne peut pas identifier une ligne. L'attribut **`IdPartie`**, identifiant unique de chaque partie, peut servir de clé primaire.

**(11)** La question nomme la table `Partie` (l'énoncé l'appelle `Parties` plus haut) ; on garde le nom de la question :
```sql
CREATE TABLE Partie (
    IdPartie INT PRIMARY KEY,
    NomJoueur TEXT,
    B INT,
    R INT
);
```

**(12)** Le numéro bleu est l'attribut `B` :
```sql
SELECT DISTINCT NomJoueur FROM Partie WHERE B = 1;
```
(`DISTINCT` évite qu'un joueur apparaisse plusieurs fois ; avec la table `Parties` de l'énoncé, on remplace `Partie` par `Parties`.)

**FIN**
