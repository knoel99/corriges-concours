# BCE ECG — Mathématiques appliquées (EDHEC) 2025 · Corrigé brut

*Corrigé rédigé par IA, non officiel. Signalez toute erreur.*

Épreuve de 4 heures (code sujet 298), calculatrice interdite. Trois exercices et un problème, 58 questions. Les bibliothèques sont importées par `import numpy as np`, `import numpy.random as rd` et `import numpy.linalg as al`.

---

## Exercice 1

Pour $n\in\mathbb{N}^*$ et $x\in[0,1]$, $f_n(x)=\displaystyle\sum_{k=1}^{n}k\,x^k$.

### 1) a)

$f_n$ est une fonction polynomiale, donc dérivable sur $[0,1]$, et pour tout $x\in[0,1]$ :

$$\begin{aligned}
f_n'(x) &=\sum_{k=1}^{n}k^2x^{k-1}\\
&=1+\sum_{k=2}^{n}k^2x^{k-1}\geqslant 1>0,
\end{aligned}$$

car chaque terme de la seconde somme est positif sur $[0,1]$. **$f_n$ est strictement croissante sur $[0,1]$.**

### 1) b)

$f_n$ est continue et strictement croissante sur l'intervalle $[0,1]$ : elle réalise une bijection de $[0,1]$ sur $[f_n(0),f_n(1)]$. Or $f_n(0)=0$ et

$$\begin{aligned}
f_n(1) &=\sum_{k=1}^{n}k\\
&=\frac{n(n+1)}{2}\geqslant 1 .
\end{aligned}$$

Donc $1\in[f_n(0),f_n(1)]$ et **l'équation $f_n(x)=1$ possède une unique solution $u_n\in[0,1]$.**

### 1) c)

$f_1(x)=x$, donc $f_1(x)=1\iff x=1$ : $\boxed{u_1=1}$.

### 2) a)

Pour tout $x\in[0,1]$ : $\boxed{f_{n+1}(x)=f_n(x)+(n+1)x^{n+1}}$.

### 2) b)

Avec $x=u_n$ et $f_n(u_n)=1$ :

$$f_{n+1}(u_n)=1+(n+1)u_n^{n+1}\geqslant 1,$$

puisque $u_n\geqslant 0$.

### 2) c)

On a $f_{n+1}(u_n)\geqslant 1=f_{n+1}(u_{n+1})$. Si l'on avait $u_n<u_{n+1}$, la stricte croissance de $f_{n+1}$ donnerait $f_{n+1}(u_n)<f_{n+1}(u_{n+1})=1$, ce qui est faux.

Donc $u_{n+1}\leqslant u_n$ pour tout $n\in\mathbb{N}^*$ : **la suite $(u_n)_{n\in\mathbb{N}^*}$ est décroissante.**

### 2) d)

La suite $(u_n)$ est décroissante et minorée par $0$ : par le théorème de la limite monotone, **elle converge** ; sa limite $\ell$ vérifie $0\leqslant \ell\leqslant 1$.

### 3) a)

Pour $x\neq 1$ : $\displaystyle\sum_{k=0}^{n}x^k=\frac{1-x^{n+1}}{1-x}$.

### 3) b)

Les deux membres de 3) a) sont des fonctions dérivables sur $\mathbb{R}\setminus\{1\}$ ; on dérive. À gauche, on obtient $\sum_{k=1}^{n}k\,x^{k-1}$ (le terme $k=0$ est constant). À droite :

$$\begin{aligned}
\frac{\mathrm d}{\mathrm dx}\left(\frac{1-x^{n+1}}{1-x}\right)
&=\frac{-(n+1)x^n(1-x)+(1-x^{n+1})}{(1-x)^2}\\
&=\frac{-(n+1)x^n+(n+1)x^{n+1}+1-x^{n+1}}{(1-x)^2}\\
&=\frac{n\,x^{n+1}-(n+1)x^n+1}{(1-x)^2}.
\end{aligned}$$

D'où, pour tout $x\neq 1$ : $\displaystyle\sum_{k=1}^{n}k\,x^{k-1}=\frac{n\,x^{n+1}-(n+1)x^n+1}{(1-x)^2}$.

### 3) c)

Pour $x\in[0,1[$, $f_n(x)=x\sum_{k=1}^{n}k\,x^{k-1}$, donc

$$\boxed{f_n(x)=\frac{x\left(n\,x^{n+1}-(n+1)x^n+1\right)}{(1-x)^2}}.$$

### 4) a)

$f_2(x)=x+2x^2$, et $2x^2+x-1=0$ a pour discriminant $9$ et pour racines $-1$ et $\frac12$.

La seule racine dans $[0,1]$ est $\frac12$ : $\boxed{u_2=\tfrac12}$.

La suite $(u_n)$ étant décroissante, pour $n\geqslant 2$ : $u_n\leqslant u_2=\frac12$. Avec $u_n\geqslant 0$ :

$$\forall n\geqslant 2,\quad 0\leqslant u_n\leqslant\frac12 .$$

### 4) b)

Pour $n\geqslant 2$, par croissance de $t\mapsto t^n$ sur $\mathbb{R}_+$ :

$$0\leqslant u_n^n\leqslant\frac{1}{2^n}
\qquad\text{et}\qquad
0\leqslant n\,u_n^n\leqslant\frac{n}{2^n}.$$

Or $\frac{1}{2^n}\to 0$ et $\frac{n}{2^n}\to 0$ (croissances comparées). Par encadrement :

$$\boxed{\lim_{n\to+\infty}u_n^n=0}$$

$$\boxed{\lim_{n\to+\infty}n\,u_n^n=0}$$

### 4) c)

Pour $n\geqslant 2$, $u_n\leqslant\frac12$, donc $u_n\in[0,1[$ et 3) c) s'applique : $f_n(u_n)=1$ s'écrit

$$u_n\left(n\,u_n^{n+1}-(n+1)u_n^n+1\right)=(1-u_n)^2 .$$

En développant : $n\,u_n^{n+2}-(n+1)u_n^{n+1}+u_n=1-2u_n+u_n^2$, soit

$$\boxed{u_n^2-3u_n+1=n\,u_n^{n+2}-(n+1)u_n^{n+1}}.$$

### 4) d)

Le membre de droite s'écrit $u_n^2\cdot n\,u_n^n-u_n\cdot n\,u_n^n-u_n\cdot u_n^n$. Comme $(u_n)$ est bornée et que $n\,u_n^n\to 0$ et $u_n^n\to 0$ (4) b)), il tend vers $0$. Le membre de gauche tend vers $\ell^2-3\ell+1$. Donc

$$\ell^2-3\ell+1=0,\qquad \ell\in\left\{\frac{3-\sqrt5}{2},\ \frac{3+\sqrt5}{2}\right\}.$$

Or $0\leqslant u_n\leqslant\frac12$ pour $n\geqslant 2$, donc $0\leqslant\ell\leqslant\frac12$, alors que $\frac{3+\sqrt5}{2}>1$. Ainsi

$$\boxed{\ell=\frac{3-\sqrt5}{2}}\qquad(\approx 0{,}382).$$

---

## Exercice 2

$E$ est l'ensemble des matrices $M(a,b)=\begin{pmatrix}a&b&a\\ b&2a-b&b\\ a&b&a\end{pmatrix}$, $(a,b)\in\mathbb{R}^2$.

### 1) a)

Posons $B=\begin{pmatrix}1&0&1\\0&2&0\\1&0&1\end{pmatrix}$ et $C=\begin{pmatrix}0&1&0\\1&-1&1\\0&1&0\end{pmatrix}$. Pour tous réels $a,b$, $M(a,b)=aB+bC$, donc

$$E=\{aB+bC,\ (a,b)\in\mathbb{R}^2\}=\mathrm{Vect}(B,C).$$

Un sous-espace engendré par une famille de matrices est un sous-espace vectoriel : **$E$ est un sous-espace vectoriel de $\mathcal{M}_3(\mathbb{R})$.**

### 1) b)

$(B,C)$ engendre $E$. Elle est libre : si $aB+bC=0$, alors $M(a,b)=0$.

Les coefficients d'indices $(1,1)$ et $(1,2)$ donnent alors $a=0$ et $b=0$.

Donc **$(B,C)$ est une base de $E$ et $\dim E=2$.**

### 2)

Toute matrice de $E$ est **symétrique** : $M(a,b)$ est égale à sa transposée, comme on le lit sur sa définition. Elle est donc diagonalisable.

Toute matrice de $E$ a **sa première et sa troisième colonne égales** : ses colonnes forment une famille liée, son rang est au plus $2<3$, donc **elle n'est pas inversible.**

### 3)

$A=M(1,3)$ : avec $a=1$, $b=3$, on a bien $2a-b=-1$. Donc **$A\in E$.**

### 4)

```python
def matA():
    return np.array([[1, 3, 1], [3, -1, 3], [1, 3, 1]])
```

### 5) a)

$A$ n'est pas inversible (question 2)), donc **$0$ est valeur propre de $A$.**

### 5) b)

$A-5I=\begin{pmatrix}-4&3&1\\3&-6&3\\1&3&-4\end{pmatrix}$ : la somme des trois colonnes est nulle, les colonnes sont liées, donc $A-5I$ n'est pas inversible.

$A+4I=\begin{pmatrix}5&3&1\\3&3&3\\1&3&5\end{pmatrix}$ : $C_1-2C_2+C_3=0$, donc $A+4I$ n'est pas inversible.

Ainsi **$5$ et $-4$ sont valeurs propres de $A$**, et $\mathrm{Sp}(A)=\{0,5,-4\}$ (trois valeurs propres distinctes en dimension 3).

### 5) c)

- $E_0(A)$ : $AX=0$ équivaut à $x+3y+z=0$ et $3x-y+3z=0$ (la troisième ligne est la première).

  $3L_1-L_2$ donne $10y=0$, d'où $y=0$ et $z=-x$.

  $E_0(A)=\mathrm{Vect}(U)$ avec $U=\begin{pmatrix}1\\0\\-1\end{pmatrix}$.
- $E_5(A)$ : $(A-5I)X=0$ ; la somme des colonnes nulle donne $V=\begin{pmatrix}1\\1\\1\end{pmatrix}\in E_5(A)$ (vérification : $AV=5V$).
- $E_{-4}(A)$ : $C_1-2C_2+C_3=0$ donne $W=\begin{pmatrix}1\\-2\\1\end{pmatrix}\in E_{-4}(A)$ (vérification : $AW=\begin{pmatrix}-4\\8\\-4\end{pmatrix}=-4W$).

Les trois sous-espaces propres sont de dimension au moins 1 ; la concaténation de bases de sous-espaces propres associés à des valeurs propres distinctes est libre dans $\mathcal{M}_{3,1}(\mathbb{R})$, donc la somme de leurs dimensions est au plus $3$ : chacun est de dimension exactement $1$ et

$$\begin{aligned}
E_0(A) &=\mathrm{Vect}(U)\\
E_5(A) &=\mathrm{Vect}(V)\\
E_{-4}(A) &=\mathrm{Vect}(W).
\end{aligned}$$

La famille $(U,V,W)$ est libre (même théorème) et formée de 3 vecteurs : **c'est une base de $\mathcal{M}_{3,1}(\mathbb{R})$ formée de vecteurs propres de $A$.**

### 6)

D'après le théorème du rang, $\mathrm{rg}(A-5I)=3-\dim E_5(A)=2$ et $\mathrm{rg}(A+4I)=3-\dim E_{-4}(A)=2$. Le script affiche

```text
r1= 2
r2= 2
```

### 7) a)

Pour $M=M(a,b)$ :

$$MU=\begin{pmatrix}a-a\\ b-b\\ a-a\end{pmatrix}=0\cdot U,\qquad
MV=\begin{pmatrix}2a+b\\ 2a+b\\ 2a+b\end{pmatrix}=(2a+b)V,$$

$$MW=\begin{pmatrix}a-2b+a\\ b-2(2a-b)+b\\ a-2b+a\end{pmatrix}=\begin{pmatrix}2a-2b\\ -4a+4b\\ 2a-2b\end{pmatrix}=(2a-2b)W.$$

Les vecteurs $U$, $V$, $W$ étant non nuls, **ce sont des vecteurs propres de toute matrice de $E$**.

Ils sont associés respectivement aux valeurs propres $0$, $2a+b$ et $2a-2b$.

### 7) b)

$P=\begin{pmatrix}1&1&1\\0&1&-2\\-1&1&1\end{pmatrix}$ est inversible (ses colonnes forment une base) et, d'après 7) a), $MP=PD$ avec $D=\mathrm{diag}(0,\,2a+b,\,2a-2b)$, donc $M=PDP^{-1}$. Par récurrence sur $n$ :

$$\begin{aligned}
M(a,b)^n &=P\,D^n\,P^{-1}\\
D^n &=\mathrm{diag}\left(0,\,(2a+b)^n,\,(2a-2b)^n\right)\quad(n\geqslant 1).
\end{aligned}$$

Il suffit donc de calculer $P^{-1}$ une fois pour toutes, puis le produit $PD^nP^{-1}$.

### 7) c)

```python
def puissanceM(a, b, n):
    P = np.array([[1, 1, 1], [0, 1, -2], [-1, 1, 1]])
    D = np.diag([0, (2*a + b)**n, (2*a - 2*b)**n])
    return np.dot(np.dot(P, D), al.inv(P))
```

(Comme $n\geqslant 1$, le premier coefficient de $D^n$ est bien $0^n=0$. On peut aussi écrire `D = np.zeros((3,3))` puis remplir `D[1,1]` et `D[2,2]`.)

---

## Exercice 3

### 1)

- **Positivité.** Si $0\leqslant x\leqslant n$, $1-\frac xn\in[0,1]$ donc $f_n(x)\geqslant 0$ ; ailleurs $f_n(x)=0$.
- **Continuité.** $f_n$ est nulle hors de $[0,n]$ et polynomiale sur $[0,n]$ : elle est continue sur $\mathbb{R}$ sauf éventuellement en $0$ et en $n$.

  Elle est discontinue en $0$, où $f_n(0)=1$. En $n$, elle est continue si $n\geqslant 2$ et discontinue si $n=1$.
- **Intégrale.** $f_n$ est nulle hors de $[0,n]$, donc $\int_{-\infty}^{+\infty}f_n$ converge et vaut $\int_0^n f_n$. Comme $x\mapsto-\left(1-\frac xn\right)^n$ a pour dérivée $\left(1-\frac xn\right)^{n-1}$ :

$$\begin{aligned}
\int_0^n\left(1-\frac xn\right)^{n-1}\mathrm dx &=\left[-\left(1-\frac xn\right)^n\right]_0^n\\
&=0+1\\
&=1 .
\end{aligned}$$

**$f_n$ est une densité de probabilité.**

### 2) a)

$f_n$ est nulle en dehors de $]-1,n+1[$ et $g:x\mapsto 1-\frac xn$ est continue sur cet intervalle : le théorème de transfert s'applique avec $a=-1$ et $b=n+1$.

Comme $\int_{-1}^{n+1}g\,f_n=\int_0^ng\,f_n$ est l'intégrale sur un segment d'une fonction continue, elle converge absolument : $g(X_n)$ admet une espérance. De même pour $g^2$.

Comme $x\mapsto -\frac{n}{n+1}\left(1-\frac xn\right)^{n+1}$ a pour dérivée $\left(1-\frac xn\right)^{n}$ :

$$\begin{aligned}
E\left(1-\frac{X_n}{n}\right) &=\int_0^n\left(1-\frac xn\right)^n\mathrm dx\\
&=\left[-\frac{n}{n+1}\left(1-\frac xn\right)^{n+1}\right]_0^n\\
&=\boxed{\frac{n}{n+1}},
\end{aligned}$$

$$\begin{aligned}
E\left(\left(1-\frac{X_n}{n}\right)^2\right) &=\int_0^n\left(1-\frac xn\right)^{n+1}\mathrm dx\\
&=\left[-\frac{n}{n+2}\left(1-\frac xn\right)^{n+2}\right]_0^n\\
&=\boxed{\frac{n}{n+2}}.
\end{aligned}$$

### 2) b)

Posons $Y_n=1-\frac{X_n}{n}$, qui admet un moment d'ordre 2 d'après 2) a). Alors $X_n=n-nY_n$ admet une espérance et une variance, et par linéarité :

$$\begin{aligned}
E(X_n) &=n-n\,E(Y_n)\\
&=n-\frac{n^2}{n+1}\\
&=\boxed{\frac{n}{n+1}}.
\end{aligned}$$

Par la formule de Koenig-Huygens, $V(Y_n)=\frac{n}{n+2}-\frac{n^2}{(n+1)^2}=\frac{n\left[(n+1)^2-n(n+2)\right]}{(n+2)(n+1)^2}=\frac{n}{(n+1)^2(n+2)}$, et $V(X_n)=n^2V(Y_n)$ :

$$\boxed{V(X_n)=\frac{n^3}{(n+1)^2(n+2)}}.$$

(Contrôle : pour $n=1$, $X_1\hookrightarrow\mathcal U[0,1]$, $E(X_1)=\frac12$ et $V(X_1)=\frac1{12}$.)

### 3)

$F_n(x)=\int_{-\infty}^xf_n(t)\,\mathrm dt$.

- Si $x<0$ : $F_n(x)=0$.
- Si $0\leqslant x\leqslant n$ : $F_n(x)=\int_0^x\left(1-\frac tn\right)^{n-1}\mathrm dt=\left[-\left(1-\frac tn\right)^n\right]_0^x=1-\left(1-\frac xn\right)^n$.
- Si $x>n$ : $F_n(x)=\int_0^nf_n=1$.

$$\boxed{F_n(x)=\begin{cases}0&\text{si }x<0\\[2pt] 1-\left(1-\frac xn\right)^n&\text{si }0\leqslant x\leqslant n\\[2pt] 1&\text{si }x>n\end{cases}}$$

### 4) a)

Pour $x<0$, $F_n(x)=0$ pour tout $n$, donc $\lim_{n\to+\infty}F_n(x)=0$.

### 4) b)

Soit $x\geqslant 0$ et $n\geqslant\lfloor x\rfloor+1$. Comme $x<\lfloor x\rfloor+1\leqslant n$, on a $0\leqslant x\leqslant n$ et la question 3) donne $F_n(x)=1-\left(1-\frac xn\right)^n$.

### 4) c)

Si $x=0$, la suite est nulle et sa limite vaut $0$.

Si $x>0$, pour $n>x$ on a $-\frac xn\in\,]-1,0[$. L'équivalent $\ln(1+u)\underset{u\to0}{\sim}u$, appliqué à $u=-\frac xn\to 0$, donne

$$n\ln\left(1-\frac xn\right)\underset{n\to+\infty}{\sim}n\cdot\left(-\frac xn\right)=-x .$$

Dans les deux cas : $\boxed{\lim_{n\to+\infty}n\ln\left(1-\frac xn\right)=-x}$.

### 4) d)

Pour $x\geqslant 0$ et $n>x$, $\left(1-\frac xn\right)^n=\exp\left(n\ln\left(1-\frac xn\right)\right)\to\mathrm e^{-x}$ par continuité de l'exponentielle, donc $F_n(x)\to 1-\mathrm e^{-x}$ (4) b)).

Pour $x<0$, $F_n(x)\to 0$ (4) a)). La limite est la fonction de répartition $F$ de la loi exponentielle de paramètre $1$, qui est continue sur $\mathbb{R}$ :

$$\forall x\in\mathbb{R},\quad \lim_{n\to+\infty}F_n(x)=F(x)=\begin{cases}0&\text{si }x<0\\ 1-\mathrm e^{-x}&\text{si }x\geqslant 0\end{cases}$$

**$(X_n)$ converge en loi vers une variable $X$ de loi $\mathcal E(1)$.**

### 5) a)

$$G(x)=\begin{cases}0&\text{si }x<0\\ x&\text{si }0\leqslant x\leqslant 1\\ 1&\text{si }x>1\end{cases}$$

### 5) b)

Pour $x\in\mathbb{R}$, $[Z_n>x]=[M_n>\frac xn]=\bigcap_{i=1}^n[U_i>\frac xn]$, car le minimum dépasse $\frac xn$ si et seulement si tous les $U_i$ le dépassent. Par indépendance mutuelle :

$$\begin{aligned}
P(Z_n>x) &=\prod_{i=1}^nP\left(U_i>\frac xn\right)\\
&=\left(1-G\left(\frac xn\right)\right)^n .
\end{aligned}$$

D'où $F_{Z_n}(x)=1-\left(1-G\left(\frac xn\right)\right)^n$ et, avec 5) a) :

- si $x<0$ : $G(\frac xn)=0$ et $F_{Z_n}(x)=0$ ;
- si $0\leqslant x\leqslant n$ : $\frac xn\in[0,1]$ et $F_{Z_n}(x)=1-\left(1-\frac xn\right)^n$ ;
- si $x>n$ : $G(\frac xn)=1$ et $F_{Z_n}(x)=1$.

### 5) c)

$F_{Z_n}=F_n$ : $Z_n$ et $X_n$ ont la même fonction de répartition. La fonction de répartition caractérisant la loi, **$Z_n$ suit la même loi que $X_n$.**

### 5) d)

`rd.random(n)` renvoie $n$ réalisations indépendantes de la loi uniforme sur $[0,1[$ :

```python
def simulX(n):
    U = rd.random(n)        # U_1, ..., U_n
    return n * np.min(U)    # Z_n = n min(U_1, ..., U_n)
```

---

## Problème

Urnes numérotées de $1$ à $n+1$ ; l'urne $k$ contient $k-1$ boules noires et $n-k+1$ boules blanches.

### 1)

`rd.randint(a, b+1)` simule la loi uniforme sur $[\![a,b]\!]$. On choisit l'urne $k$ uniformément dans $[\![1,n+1]\!]$.

- L'urne $n+1$ ne contient que des noires : $X_n=0$.
- L'urne $1$ ne contient que des blanches : $X_n=1$.
- Sinon, une boule tirée uniformément parmi $[\![1,n]\!]$ est noire si et seulement si son numéro est au plus $k-1$.

```python
def varX(n):
    k = rd.randint(1, n+2)       # choix de l'urne
    if k == n+1:
        X = 0
    elif k == 1:
        X = 1
    else:
        X = 1
        while rd.randint(1, n+1) <= k-1:
            X = X + 1
    return(X)
```

### 2)

L'urne est choisie au hasard parmi $n+1$ urnes : pour tout $k\in[\![1,n+1]\!]$, $\boxed{P(U_k)=\frac{1}{n+1}}$.

### 3) a)

Sachant $U_k$ ($1\leqslant k\leqslant n$), les tirages avec remise dans l'urne $k$ sont des épreuves de Bernoulli indépendantes de même paramètre $p_k=\frac{n-k+1}{n}>0$ (succès : tirer une blanche), et $X_n$ est le rang du premier succès.

**Pour $2\leqslant k\leqslant n$, conditionnellement à $U_k$, $X_n$ suit la loi géométrique $\mathcal G\left(\frac{n-k+1}{n}\right)$** ; la formule ci-dessous vaut aussi pour $k=1$ :

Pour tout $j\in\mathbb{N}^*$ :

$$P_{U_k}(X_n=j)=\left(\frac{k-1}{n}\right)^{j-1}\frac{n-k+1}{n}.$$

Pour $k=1$, $p_1=1$ : $X_n=1$ (variable certaine).

### 3) b)

Les six premières lignes traitent $k=n+1$ et $k=1$ ; pour $2\leqslant k\leqslant n$, on simule directement la loi géométrique :

```python
    else:
        X = rd.geometric((n+1-k)/n)
    return(X)
```

### 4) a)

Sachant $U_{n+1}$, on ne tire que des noires : $P_{U_{n+1}}(X_n=1)=0$.

### 4) b)

Pour $k\in[\![1,n]\!]$ : $P_{U_k}(X_n=1)=\dfrac{n-k+1}{n}$ (proportion de blanches dans l'urne $k$).

### 4) c)

$(U_1,\dots,U_{n+1})$ est un système complet d'événements de probabilités non nulles. Par la formule des probabilités totales :

$$\begin{aligned}
P(X_n=1)&=\sum_{k=1}^{n+1}P(U_k)\,P_{U_k}(X_n=1)=\frac{1}{n+1}\sum_{k=1}^{n}\frac{n-k+1}{n}\\
&=\frac{1}{n(n+1)}\sum_{i=1}^{n}i=\frac{1}{n(n+1)}\cdot\frac{n(n+1)}{2}=\boxed{\frac12}.
\end{aligned}$$

### 5) a)

Pour $j\geqslant 2$ : $P_{U_{n+1}}(X_n=j)=0$ (aucune blanche dans l'urne $n+1$).

### 5) b)

Pour $k\in[\![1,n]\!]$ et $j\geqslant 2$, d'après 3) a) :

$$P_{U_k}(X_n=j)=\left(\frac{k-1}{n}\right)^{j-1}\left(1-\frac{k-1}{n}\right).$$

(Pour $k=1$, cela vaut bien $0$ puisque $j-1\geqslant 1$.)

### 5) c)

Par la formule des probabilités totales, puis en posant $i=k-1$ :

$$\begin{aligned}
P(X_n=j)&=\frac{1}{n+1}\sum_{k=1}^{n}\left(\frac{k-1}{n}\right)^{j-1}\left(1-\frac{k-1}{n}\right)+\frac{1}{n+1}\cdot 0\\
&=\frac{1}{n+1}\sum_{i=0}^{n-1}\left[\left(\frac{i}{n}\right)^{j-1}-\left(\frac{i}{n}\right)^{j}\right],
\end{aligned}$$

ce qui est l'égalité demandée (indice de sommation renommé $k$).

### 6) a)

Soit $k\in[\![0,n-1]\!]$ et $q=\frac kn\in[0,1[$. Pour $N\geqslant 2$, la somme partielle est télescopique :

$$\sum_{j=2}^{N}\left(q^{j-1}-q^{j}\right)=q-q^{N}\xrightarrow[N\to+\infty]{}q,$$

car $0\leqslant q<1$. La série converge et $\displaystyle\sum_{j=2}^{+\infty}\left[\left(\frac kn\right)^{j-1}-\left(\frac kn\right)^{j}\right]=\frac kn$.

### 6) b)

$[X_n\geqslant 2]$ est la réunion des événements deux à deux incompatibles $[X_n=j]$, $j\geqslant 2$. Par $\sigma$-additivité, puis par linéarité (somme finie de séries convergentes) :

$$\begin{aligned}
P(X_n\geqslant 2)&=\sum_{j=2}^{+\infty}P(X_n=j)=\frac{1}{n+1}\sum_{k=0}^{n-1}\sum_{j=2}^{+\infty}\left[\left(\frac kn\right)^{j-1}-\left(\frac kn\right)^{j}\right]\\
&=\frac{1}{n+1}\sum_{k=0}^{n-1}\frac kn=\frac{1}{n(n+1)}\cdot\frac{(n-1)n}{2}=\boxed{\frac{n-1}{2(n+1)}}.
\end{aligned}$$

### 7) a)

$X_n(\Omega)\subset\mathbb{N}$, donc $[X_n=0]$, $[X_n=1]$ et $[X_n\geqslant 2]$ forment un système complet :

$$\begin{aligned}
P(X_n=0) &=1-\frac12-\frac{n-1}{2(n+1)}\\
&=\frac{(n+1)-(n-1)}{2(n+1)}\\
&=\boxed{\frac{1}{n+1}}.
\end{aligned}$$

### 7) b)

Oui. Si l'urne choisie est l'urne $k\leqslant n$, elle contient au moins une blanche ; la probabilité de n'obtenir que des noires lors des $N$ premiers tirages vaut $\left(\frac{k-1}{n}\right)^N$, qui tend vers $0$ : presque sûrement une blanche finit par sortir. Ne jamais obtenir de blanche revient donc (presque sûrement) à avoir choisi l'urne $n+1$, et $P(X_n=0)=P(U_{n+1})=\frac{1}{n+1}$.

### 8) a)

$X_n$ est à valeurs dans $\mathbb{N}$ : elle admet une espérance si et seulement si la série à termes positifs $\sum_j j\,P(X_n=j)$ converge. Pour $j\geqslant 2$, d'après 5) c) :

$$\begin{aligned}
j\,P(X_n=j) &=\frac{1}{n+1}\sum_{k=0}^{n-1}j\,q_k^{\,j-1}(1-q_k)\\
q_k &=\frac kn\in[0,1[ .
\end{aligned}$$

Pour $q\in[0,1[$, la série $\sum_{j\geqslant1}j\,q^{j-1}$ converge et vaut $\frac{1}{(1-q)^2}$ (série géométrique dérivée), donc

$$\begin{aligned}
\sum_{j=2}^{+\infty}j\,q^{j-1}(1-q) &=(1-q)\left(\frac{1}{(1-q)^2}-1\right)\\
&=\frac{1}{1-q}-(1-q).
\end{aligned}$$

La série $\sum_j j\,P(X_n=j)$ est une combinaison linéaire finie de séries convergentes : elle converge, et $X_n$ admet une espérance. Avec $P(X_n=1)=\frac12$ :

$$E(X_n)=\frac12+\frac{1}{n+1}\sum_{k=0}^{n-1}\left[\frac{1}{1-\frac kn}-\left(1-\frac kn\right)\right].$$

Or $\sum_{k=0}^{n-1}\left(1-\frac kn\right)=n-\frac{n-1}{2}=\frac{n+1}{2}$, d'où un terme $-\frac12$ qui compense le premier, et

en posant $p=n-k$ :

$$\begin{aligned}
E(X_n)&=\frac{1}{n+1}\sum_{k=0}^{n-1}\frac{n}{n-k}\\
&=\frac{n}{n+1}\sum_{p=1}^{n}\frac1p .
\end{aligned}$$

$$\boxed{E(X_n)=\frac{n}{n+1}\sum_{p=1}^{n}\frac1p}.$$

### 8) b)

```python
n = int(input('entrez la valeur de n :'))
v = np.arange(1, n+1)
E = n/(n+1) * np.sum(1/v)
print(E)
```

(Pour $n=4$, on obtient $\frac45\cdot\frac{25}{12}=\frac53\approx 1{,}667$.)

### 9) a)

Soit $p\in\mathbb{N}^*$. Pour $t\in[p,p+1]$, par décroissance de $t\mapsto\frac1t$ sur $\mathbb{R}_+^*$ : $\frac{1}{p+1}\leqslant\frac1t\leqslant\frac1p$.

Par croissance de l'intégrale (bornes $p<p+1$), sur un intervalle de longueur $1$ :

$$\frac{1}{p+1}\leqslant\int_p^{p+1}\frac{\mathrm dt}{t}\leqslant\frac1p .$$

### 9) b)

Soit $n\geqslant 2$. On somme 9) a) pour $p\in[\![1,n-1]\!]$ ; par la relation de Chasles, $\sum_{p=1}^{n-1}\int_p^{p+1}\frac{\mathrm dt}{t}=\int_1^n\frac{\mathrm dt}{t}=\ln n$, et

$$\begin{aligned}
\sum_{p=1}^{n-1}\frac{1}{p+1}&=\sum_{p=2}^{n}\frac1p\\
&\leqslant\ln(n)\\
&\leqslant\sum_{p=1}^{n-1}\frac1p .
\end{aligned}$$

### 9) c)

Pour $n\geqslant 2$, en ajoutant $1$ à l'inégalité de gauche : $\sum_{p=1}^{n}\frac1p=1+\sum_{p=2}^{n}\frac1p\leqslant\ln(n)+1$. En ajoutant $\frac1n$ à celle de droite : $\ln(n)+\frac1n\leqslant\sum_{p=1}^{n-1}\frac1p+\frac1n=\sum_{p=1}^{n}\frac1p$. Donc

$$\forall n\geqslant 2,\quad \ln(n)+\frac1n\leqslant\sum_{p=1}^{n}\frac1p\leqslant\ln(n)+1 .$$

### 9) d)

Pour $n\geqslant 2$, $\ln n>0$ et, en divisant :

$$1+\frac{1}{n\ln n}\leqslant\frac{1}{\ln n}\sum_{p=1}^{n}\frac1p\leqslant 1+\frac{1}{\ln n}.$$

Les deux bornes tendent vers $1$ : par encadrement, $\sum_{p=1}^{n}\frac1p\sim\ln n$. Comme $\frac{n}{n+1}\to 1$, et que l'équivalence est compatible avec le produit :

$$\boxed{E(X_n)\underset{n\to+\infty}{\sim}\ln n}.$$
