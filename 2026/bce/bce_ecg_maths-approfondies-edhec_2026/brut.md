# BCE ECG — Mathématiques approfondies (EDHEC) 2026 · Corrigé brut

*Corrigé rédigé par IA, non officiel. Signalez toute erreur.*

Épreuve de 4 h, sans document ni calculatrice. Trois exercices (produit de deux lois uniformes ; approximation de $\pi$ et méthode de Richardson ; un mobile aléatoire et une convergence en loi) et un problème (racine carrée d'une matrice symétrique positive).

## Exercice 1

### 1)

```python
def simulZ():
    return rd.random() * rd.random()
```

Les deux appels à `rd.random()` simulent deux variables indépendantes de loi uniforme sur $[0,1[$.

### 2)

$Z$ est à valeurs dans $]0,1]$ : elle est bornée, donc admet des moments de tout ordre, en particulier une espérance et une variance. Par indépendance de $X_1$ et $X_2$ :

$$\begin{aligned}
E(Z) &= E(X_1)\,E(X_2)=\frac14,\\
E(Z^2) &= E(X_1^2)\,E(X_2^2)=\frac19 .
\end{aligned}$$

Donc $V(Z)=\frac19-\frac1{16}$ :

$$\boxed{E(Z)=\frac14}$$

$$\boxed{V(Z)=\frac{7}{144}}$$

### 3) a)

Pour $x\in\mathbb{R}$, $F(x)=P(\ln(X_1)\leqslant x)=P(X_1\leqslant\mathrm{e}^x)$, car $\exp$ est strictement croissante.

- Si $x\leqslant0$, $\mathrm{e}^x\in\,]0,1]$ et $F(x)=\mathrm{e}^x$.
- Si $x>0$, $\mathrm{e}^x>1$ et $F(x)=1$.

$$\boxed{F(x)=\begin{cases}\mathrm{e}^x&\text{si }x\leqslant0\\1&\text{si }x>0\end{cases}}$$

### 3) b)

$F$ est continue sur $\mathbb{R}$ (en $0$, les deux expressions valent $1$) et de classe $\mathcal{C}^1$ sur $\mathbb{R}^*$. Une densité s'obtient en dérivant là où c'est possible :

$$\boxed{f(x)=\begin{cases}\mathrm{e}^x&\text{si }x\leqslant0\\0&\text{si }x>0\end{cases}}$$

### 4) a)

$Y_1$ et $Y_2$ sont indépendantes (fonctions de $X_1$ et $X_2$), de densité $f$ bornée. La somme admet donc pour densité le produit de convolution

$$h(x)=\int_{-\infty}^{+\infty}f(t)\,f(x-t)\,\mathrm{d}t .$$

L'intégrande est non nul si et seulement si $t\leqslant0$ et $x-t\leqslant0$, c'est-à-dire $x\leqslant t\leqslant0$.

- Si $x>0$, cet ensemble est vide et $h(x)=0$.
- Si $x\leqslant0$ :

$$\begin{aligned}
h(x) &= \int_x^0\mathrm{e}^t\,\mathrm{e}^{x-t}\,\mathrm{d}t\\
&= -x\,\mathrm{e}^x .
\end{aligned}$$

**La fonction $h$ de l'énoncé est une densité de $Y_1+Y_2$.**

### 4) b)

Pour $x>0$, $H(x)=1$.

Pour $x\leqslant0$, une primitive de $t\mapsto-t\,\mathrm{e}^t$ est $t\mapsto(1-t)\,\mathrm{e}^t$, et $(1-t)\,\mathrm{e}^t\to0$ quand $t\to-\infty$ (croissances comparées). Donc

$$\boxed{H(x)=\begin{cases}(1-x)\,\mathrm{e}^x&\text{si }x\leqslant0\\1&\text{si }x>0\end{cases}}$$

### 4) c)

$Z=X_1X_2=\mathrm{e}^{Y_1+Y_2}$ est à valeurs dans $]0,1]$.

- Si $x\leqslant0$, $F_Z(x)=0$ ; si $x\geqslant1$, $F_Z(x)=1$.
- Si $0<x<1$, par stricte croissance de $\ln$ :

$$\begin{aligned}
F_Z(x) &= P(Y_1+Y_2\leqslant\ln x)\\
&= H(\ln x)\\
&= x\,(1-\ln x).
\end{aligned}$$

$F_Z$ est continue sur $\mathbb{R}$ : $x(1-\ln x)\to0$ quand $x\to0^+$ et vaut $1$ en $x=1$.

Elle est de classe $\mathcal{C}^1$ sauf peut-être en $0$ et $1$, avec, pour $0<x<1$,

$$F_Z'(x)=(1-\ln x)-1=-\ln x .$$

$Z$ est donc à densité, et en prenant la valeur $-\ln(1)=0$ en $1$ :

$$\boxed{f_Z(x)=\begin{cases}-\ln(x)&\text{si }0<x\leqslant1\\0&\text{sinon}\end{cases}}$$

### 5) a)

Soit $n\in\mathbb{N}$ et $\varepsilon\in\,]0,1]$. Par intégration par parties (fonctions de classe $\mathcal{C}^1$ sur $[\varepsilon,1]$) :

$$\begin{aligned}
\int_\varepsilon^1x^n\ln(x)\,\mathrm{d}x &= \Big[\frac{x^{n+1}}{n+1}\ln(x)\Big]_\varepsilon^1-\int_\varepsilon^1\frac{x^n}{n+1}\,\mathrm{d}x\\
&= -\frac{\varepsilon^{n+1}\ln\varepsilon}{n+1}-\frac{1-\varepsilon^{n+1}}{(n+1)^2}.
\end{aligned}$$

Comme $\varepsilon^{n+1}\ln\varepsilon\to0$ quand $\varepsilon\to0^+$ (croissances comparées), l'intégrale converge et

$$\boxed{\int_0^1x^n\ln(x)\,\mathrm{d}x=-\frac1{(n+1)^2}}$$

### 5) b)

Les intégrales $\int_0^1x\,(-\ln x)\,\mathrm{d}x$ et $\int_0^1x^2(-\ln x)\,\mathrm{d}x$ convergent et leurs intégrandes sont positives : $Z$ admet un moment d'ordre $2$, et par 5.a avec $n=1$ et $n=2$ :

$$E(Z)=\frac14$$

$$E(Z^2)=\frac19 .$$

On retrouve $V(Z)=\frac19-\frac1{16}=\frac7{144}$.

## Exercice 2

### 1)

Montrons par récurrence la propriété $\mathcal{P}(n)$ : « $u_n$ et $v_n$ sont bien définis et $u_n\in[0,1]$ ».

*Initialisation.* $u_1=0\in[0,1]$ et $v_1=2$.

*Hérédité.* Si $\mathcal{P}(n)$ est vraie, alors $\frac{1+u_n}2\in\big[\frac12,1\big]$, donc $u_{n+1}=\sqrt{\frac{1+u_n}2}$ est bien défini et appartient à $\big[\frac{\sqrt2}2,1\big]\subset\,]0,1]$. Comme $u_{n+1}\neq0$, $v_{n+1}=\frac{v_n}{u_{n+1}}$ est bien défini.

**Les deux suites sont parfaitement définies, et $u_n\in[0,1]$ pour tout $n\in\mathbb{N}^*$.**

### 2)

```python
def suite_v(n):
    u = 0
    v = 2
    for k in range(2, n + 1):
        u = np.sqrt((1 + u) / 2)
        v = v / u
    return v
```

À la fin du tour d'indice `k`, `u` et `v` contiennent $u_k$ et $v_k$ ; pour $n=1$, la boucle est vide et la fonction renvoie $v_1=2$.

### 3) a)

La fonction $\cos$ est continue et strictement décroissante sur $\big[0,\frac\pi2\big]$, avec $\cos0=1$ et $\cos\frac\pi2=0$. C'est donc une bijection de $\big[0,\frac\pi2\big]$ sur $[0,1]$.

Comme $u_n\in[0,1]$ (question 1), il existe un unique $\alpha_n\in\big[0,\frac\pi2\big]$ tel que $u_n=\cos(\alpha_n)$.

**La suite $(\alpha_n)$ existe et est unique.**

### 3) b)

$u_1=0=\cos\frac\pi2$, donc $\alpha_1=\frac\pi2$. Pour $n\geqslant1$, avec $\cos(2a)=2\cos^2(a)-1$ :

$$\begin{aligned}
u_{n+1} &= \sqrt{\frac{1+\cos\alpha_n}2}\\
&= \sqrt{\cos^2\frac{\alpha_n}2}\\
&= \cos\frac{\alpha_n}2 ,
\end{aligned}$$

car $\frac{\alpha_n}2\in\big[0,\frac\pi4\big]$, où $\cos$ est positif. Comme $\frac{\alpha_n}2\in\big[0,\frac\pi2\big]$, l'unicité de 3.a donne $\alpha_{n+1}=\frac{\alpha_n}2$. La suite $(\alpha_n)$ est géométrique de raison $\frac12$ :

$$\boxed{\alpha_n=\frac{\pi}{2^n}}$$

### 3) c)

Récurrence. Pour $n=1$, $2\sin\frac\pi2=2=v_1$. Si $v_n=2^n\sin\frac\pi{2^n}$, alors avec $\sin(2a)=2\sin(a)\cos(a)$ :

$$\begin{aligned}
v_{n+1} &= \frac{2^n\sin\frac{\pi}{2^n}}{\cos\frac{\pi}{2^{n+1}}}\\
&= \frac{2^n\cdot2\sin\frac{\pi}{2^{n+1}}\cos\frac{\pi}{2^{n+1}}}{\cos\frac{\pi}{2^{n+1}}}\\
&= 2^{n+1}\sin\frac{\pi}{2^{n+1}} .
\end{aligned}$$

Donc $v_n=2^n\sin\big(\frac\pi{2^n}\big)$ pour tout $n\in\mathbb{N}^*$. Comme $\sin x\sim x$ en $0$ et $\frac\pi{2^n}\to0$, on a $v_n\sim2^n\cdot\frac\pi{2^n}$ :

$$\boxed{\lim_{n\to+\infty}v_n=\pi}$$

### 4)

Posons $x_n=\frac\pi{2^n}\to0$, de sorte que $v_n=\pi\,\frac{\sin x_n}{x_n}$. Le développement limité du sinus donne

$$\frac{\sin x}{x}=1-\frac{x^2}6+\frac{x^4}{120}+o(x^4).$$

Avec $x_n^2=\frac{\pi^2}{4^n}$ et $x_n^4=\frac{\pi^4}{4^{2n}}$ :

$$v_n=\pi-\frac{\pi^3}{6\cdot4^n}+\frac{\pi^5}{120\cdot4^{2n}}+o\Big(\frac1{4^{2n}}\Big).$$

$$\boxed{\begin{aligned}a&=\pi\\b&=-\frac{\pi^3}6\\c&=\frac{\pi^5}{120}\end{aligned}}$$

### 5) a)

```python
def suite_w(n):
    return (4 * suite_v(n + 1) - suite_v(n)) / 3
```

### 5) b)

Par opérations sur les limites, $w_n\to\frac{4\pi-\pi}3$ : $\boxed{\lim_{n\to+\infty}w_n=\pi}$.

### 5) c)

En appliquant 4 au rang $n+1$, avec $4^{n+1}=4\cdot4^n$ et $4^{2(n+1)}=16\cdot4^{2n}$ :

$$4v_{n+1}=4\pi-\frac{\pi^3}{6\cdot4^n}+\frac{\pi^5}{480\cdot4^{2n}}+o\Big(\frac1{4^{2n}}\Big).$$

En retranchant $v_n$, les termes en $\frac1{4^n}$ se compensent :

$$\begin{aligned}
4v_{n+1}-v_n &= 3\pi+\Big(\frac{1}{480}-\frac1{120}\Big)\frac{\pi^5}{4^{2n}}+o\Big(\frac1{4^{2n}}\Big)\\
&= 3\pi-\frac{3\pi^5}{480\cdot4^{2n}}+o\Big(\frac1{4^{2n}}\Big).
\end{aligned}$$

En divisant par $3$ :

$$\boxed{w_n=\pi-\frac{\pi^5}{480\times4^{2n}}+o\Big(\frac1{4^{2n}}\Big)}$$

Ainsi $w_n-\pi\sim-\frac{\pi^5}{480\cdot4^{2n}}$ et, par 4, $v_n-\pi\sim-\frac{\pi^3}{6\cdot4^n}$ (ces quantités sont non nulles pour $n$ grand). Par quotient d'équivalents :

$$\frac{w_n-\pi}{v_n-\pi}\sim\frac{\pi^5}{480\cdot4^{2n}}\cdot\frac{6\cdot4^n}{\pi^3}$$

$$\boxed{\frac{w_n-\pi}{v_n-\pi}\underset{n\to+\infty}{\sim}\frac{\pi^2}{80\cdot4^n}}$$

### 5) d)

L'erreur $w_n-\pi$ est négligeable devant l'erreur $v_n-\pi$ : leur quotient tend vers $0$ (comme $\frac1{4^n}$).

Pour un coût de calcul quasi identique ($w_n$ ne demande que $v_n$ et $v_{n+1}$), la suite $(w_n)$ donne une bien meilleure valeur approchée de $\pi$.

Son erreur est de l'ordre de $\frac{1}{16^n}$ au lieu de $\frac1{4^n}$.

Par exemple, $w_5\approx3{,}1415920$ alors que $v_5\approx3{,}1365$.

### 6) a)

Cherchons $y_n=\frac{x_{n+1}-qx_n}{1-q}$ (le coefficient de $x_n$ est choisi pour éliminer le terme en $q^n$, puis on normalise pour garder la limite $a$). Comme $o(r^{n+1})=o(r^n)$ :

$$\begin{aligned}
x_{n+1}-qx_n &= a(1-q)+b(q^{n+1}-q\,q^n)+c(r^{n+1}-q\,r^n)+o(r^n)\\
&= a(1-q)+c\,(r-q)\,r^n+o(r^n).
\end{aligned}$$

Donc, avec $y_n=\frac{x_{n+1}-qx_n}{1-q}$ :

$$\boxed{y_n=a+d\,r^n+o(r^n)}$$

avec

$$\boxed{d=\frac{c\,(r-q)}{1-q}}$$

### 6) b)

Comme $0<r<q$, $\frac{r^n}{q^n}=\big(\frac rq\big)^n\to0$, donc $r^n=o(q^n)$, et $o(r^n)=o(q^n)$. Ainsi

$$\boxed{x_n=a+b\,q^n+o(q^n)}$$

### 6) c)

Comme $b\neq0$, $x_n-a\sim b\,q^n$ ; comme $c\neq0$ et $r\neq q$, $d\neq0$ et $y_n-a\sim d\,r^n$.

Ces quantités sont non nulles pour $n$ grand, et

$$\frac{y_n-a}{x_n-a}\sim\frac db\Big(\frac rq\Big)^n\xrightarrow[n\to+\infty]{}0 .$$

**$y_n-a=o(x_n-a)$ : la suite $(y_n)$ converge vers $a$ plus rapidement que $(x_n)$.**

La question 5 est le cas $q=\frac14$, $r=\frac1{16}$, où $y_n=\frac{4x_{n+1}-x_n}3$.

## Exercice 3

### Partie 1

#### 1) a)

Pour $k\in\mathbb{N}^*$, le mobile choisit de façon équiprobable l'un des $k+1$ points $0,1,\dots,k$ : $X_k$ suit la loi uniforme sur $[\![0;k]\!]$,

$$\forall i\in[\![0;k]\!]$$

$$P(X_k=i)=\frac1{k+1}.$$

#### 1) b)

$X_k$ est finie, donc admet une espérance et une variance. On a $X_k+1\hookrightarrow\mathcal{U}([\![1;k+1]\!])$, d'espérance $\frac{k+2}2$ et de variance $\frac{(k+1)^2-1}{12}$. Donc

$$\boxed{E(X_k)=\frac k2}$$

$$\boxed{V(X_k)=\frac{k(k+2)}{12}}$$

#### 2) a)

Le premier retour à l'origine a lieu à l'instant $n$ si et seulement si le mobile n'est pas en $0$ aux instants $1,\dots,n-1$ et y est à l'instant $n$ :

$$\begin{aligned}
(Y=n)&=\Big(\bigcap_{k=1}^{n-1}(X_k\neq0)\Big)\\
&\quad\cap(X_n=0),
\end{aligned}$$

avec la convention qu'une intersection vide vaut $\Omega$ (pour $n=1$, $(Y=1)=(X_1=0)$).

#### 2) b)

Par indépendance mutuelle des $X_k$ :

$$\begin{aligned}
P(Y=n) &= \prod_{k=1}^{n-1}\Big(1-\frac1{k+1}\Big)\cdot\frac1{n+1}\\
&= \prod_{k=1}^{n-1}\frac{k}{k+1}\cdot\frac1{n+1}\\
&= \frac1n\cdot\frac1{n+1}.
\end{aligned}$$

(Le produit est télescopique.) Comme $\frac1{n(n+1)}=\frac1n-\frac1{n+1}$ :

$$\boxed{\forall n\in\mathbb{N}^*,\ P(Y=n)=\frac1n-\frac1{n+1}}$$

#### 2) c)

Pour $N\in\mathbb{N}^*$, la somme est télescopique :

$$\begin{aligned}
\sum_{n=1}^NP(Y=n)&=1-\frac1{N+1}\\
&\xrightarrow[N\to+\infty]{}1 .
\end{aligned}$$

Donc $\boxed{\sum_{n=1}^{+\infty}P(Y=n)=1}$. Les événements $(Y=n)$, $n\in\mathbb{N}$, forment un système complet, d'où $P(Y=0)=1-1$ : $\boxed{P(Y=0)=0}$.

#### 2) d)

$Y$ est positive, et $nP(Y=n)=\frac{1}{n+1}$, terme général d'une série divergente (série harmonique). **$Y$ n'admet pas d'espérance.**

### Partie 2

#### 3)

```python
def var_Z(n):
    U = rd.randint(0, n)          # uniforme sur [[0, n-1]]
    Z = rd.geometric(1 - U / n)   # géométrique de paramètre 1 - U/n
    return Z
```

`rd.randint(0, n)` renvoie un entier uniforme de $[\![0;n-1]\!]$ (borne supérieure exclue). Pour $U=0$, le paramètre vaut $1$ et `rd.geometric(1)` renvoie $1$.

#### 4) a)

Les événements $(U_n=k)$, $k\in[\![0;n-1]\!]$, forment un système complet d'événements de probabilités non nulles. Par la formule des probabilités totales, pour $i\in\mathbb{N}^*$ :

$$\begin{aligned}
P(Z_n=i) &= \sum_{k=0}^{n-1}P(U_n=k)\,P_{(U_n=k)}(Z_n=i)\\
&= \frac1n\sum_{k=0}^{n-1}\Big(\frac kn\Big)^{i-1}\Big(1-\frac kn\Big).
\end{aligned}$$

(Pour $k=0$ et $i=1$, la convention $0^0=1$ donne bien $P_{(U_n=0)}(Z_n=1)=1$.) En développant :

$$\begin{aligned}
P(Z_n=i)&=\frac1n\sum_{k=0}^{n-1}\Big(\frac kn\Big)^{i-1}\\
&\quad-\frac1n\sum_{k=0}^{n-1}\Big(\frac kn\Big)^i .
\end{aligned}$$

#### 4) b)

Ce sont des sommes de Riemann des fonctions continues $x\mapsto x^{i-1}$ et $x\mapsto x^i$ sur $[0,1]$. Elles convergent vers les intégrales correspondantes :

$$\lim_{n\to+\infty}P(Z_n=i)=\int_0^1x^{i-1}\,\mathrm{d}x-\int_0^1x^i\,\mathrm{d}x$$

$$\boxed{\lim_{n\to+\infty}P(Z_n=i)=\frac1i-\frac1{i+1}}$$

#### 4) c)

Les variables $Z_n$ sont à valeurs dans $\mathbb{N}^*\subset\mathbb{N}$, et $Y$ est à valeurs dans $\mathbb{N}$.

Pour $i\in\mathbb{N}^*$, $P(Z_n=i)\to P(Y=i)$ (2.b et 4.b), et $P(Z_n=0)=0=P(Y=0)$.

Pour des variables à valeurs dans $\mathbb{N}$, c'est une caractérisation de la convergence en loi : **$(Z_n)$ converge en loi vers $Y$.**

#### 5)

Le système complet $\big((U_n=k)\big)_{0\leqslant k\leqslant n-1}$ est **fini**, et pour chaque $k$, la loi conditionnelle de $Z_n$ sachant $(U_n=k)$ est géométrique de paramètre $p_k=1-\frac kn\in\,]0,1]$, qui admet l'espérance $\frac1{p_k}=\frac{n}{n-k}$. La formule de l'espérance totale s'applique donc (la somme à considérer est finie) :

$$\begin{aligned}
E(Z_n) &= \sum_{k=0}^{n-1}P(U_n=k)\,E(Z_n\mid U_n=k)\\
&= \frac1n\sum_{k=0}^{n-1}\frac{n}{n-k}\\
&= \sum_{k=0}^{n-1}\frac1{n-k}.
\end{aligned}$$

Avec le changement d'indice $j=n-k$ :

$$\boxed{E(Z_n)=\sum_{k=1}^n\frac1k}$$

#### 6) a)

Pour $k\in\mathbb{N}^*$ et $t\in[k,k+1]$, $\frac1{k+1}\leqslant\frac1t\leqslant\frac1k$. En intégrant sur $[k,k+1]$ (intervalle de longueur $1$) :

$$\frac1{k+1}\leqslant\int_k^{k+1}\frac{\mathrm{d}t}t\leqslant\frac1k,$$

et $\int_k^{k+1}\frac{\mathrm{d}t}t=\ln(k+1)-\ln(k)$.

#### 6) b)

Soit $n\geqslant2$. En sommant 6.a pour $k=1,\dots,n-1$, la somme centrale est télescopique et vaut $\ln n$ :

$$\sum_{k=2}^n\frac1k\leqslant\ln(n)\leqslant\sum_{k=1}^{n-1}\frac1k .$$

Avec $E(Z_n)=\sum_{k=1}^n\frac1k$, l'inégalité de gauche donne $E(Z_n)-1\leqslant\ln n$, et celle de droite donne $\ln n\leqslant E(Z_n)-\frac1n$. D'où

$$\boxed{\ln(n)+\frac1n\leqslant E(Z_n)\leqslant\ln(n)+1}$$

#### 6) c)

Pour $n\geqslant2$, $\ln n>0$ ; en divisant par $\ln n$ :

$$1+\frac1{n\ln n}\leqslant\frac{E(Z_n)}{\ln n}\leqslant1+\frac1{\ln n}.$$

Les deux bornes tendent vers $1$ ; par encadrement, $\frac{E(Z_n)}{\ln n}\to1$ : $\boxed{E(Z_n)\underset{n\to+\infty}{\sim}\ln(n)}$.

## Problème

### Partie 1 : caractérisation des matrices symétriques positives

#### 1) a)

$\lambda$ est valeur propre de $A$ : il existe $X\in\mathcal{M}_{n,1}(\mathbb{R})$ non nul tel que $AX=\lambda X$.

Alors ${}^tXAX=\lambda\,{}^tXX$, et ${}^tXX=\|X\|^2>0$ car $X\neq0$. Donc

$$\boxed{\lambda=\frac{{}^tXAX}{{}^tXX}}$$

#### 1) b)

$A$ est positive, donc ${}^tXAX\geqslant0$, et ${}^tXX>0$ : $\boxed{\lambda\geqslant0}$.

#### 2) a)

$A$ est symétrique réelle : par le théorème spectral, elle est diagonalisable avec une matrice de passage orthogonale. Il existe $P$ orthogonale et $D$ diagonale telles que $D=P^{-1}AP={}^tPAP$, c'est-à-dire $A=PD\,{}^tP$.

#### 2) b)

Avec $Y={}^tPX$, on a ${}^tY={}^tXP$, donc

$$\begin{aligned}
{}^tYDY &= {}^tX\,PD\,{}^tP\,X\\
&= {}^tXAX .
\end{aligned}$$

#### 2) c)

En notant $y_1,\dots,y_n$ les coefficients de $Y$, et les $\lambda_i$ étant positifs :

$$\begin{aligned}
{}^tXAX &= {}^tYDY\\
&= \sum_{i=1}^n\lambda_iy_i^2\geqslant0.
\end{aligned}$$

#### 3)

Les coefficients diagonaux $\lambda_1,\dots,\lambda_n$ de $D$ sont les valeurs propres de $A$ ($A$ et $D$ sont semblables).

- Si $A$ est positive, toutes ses valeurs propres sont positives (question 1).
- Si toutes les valeurs propres de $A$ sont positives, alors les $\lambda_i$ le sont et $A$ est positive (question 2).

**Une matrice $A\in\mathcal{S}_n(\mathbb{R})$ est positive si et seulement si ses valeurs propres sont positives.**

### Partie 2 : « racine carrée » d'une matrice symétrique positive

#### 4) a)

$A$ est symétrique positive, donc ses valeurs propres $\lambda_1,\dots,\lambda_n$ sont positives (partie 1). Les réels $\sqrt{\lambda_i}$ sont bien définis : **$\Delta$ est correctement définie.**

#### 4) b)

${}^tB={}^t({}^tP)\,{}^t\Delta\,{}^tP=P\Delta\,{}^tP=B$ car $\Delta$ est diagonale : $B$ est symétrique.

Comme ${}^tP=P^{-1}$, $B=P\Delta P^{-1}$ est semblable à $\Delta$, et ses valeurs propres $\sqrt{\lambda_1},\dots,\sqrt{\lambda_n}$ sont positives : $B$ est positive (partie 1). Enfin

$$\begin{aligned}
B^2 &= P\Delta\,{}^tP\,P\Delta\,{}^tP\\
&= P\Delta^2\,{}^tP\\
&= PD\,{}^tP=A .
\end{aligned}$$

**$B\in\mathcal{S}_n^+(\mathbb{R})$ et $B^2=A$.**

#### 5)

Les $\mu_k$ sont deux à deux distincts, donc les dénominateurs $\mu_i-\mu_k$ ($k\neq i$) sont non nuls et $L_i$ est bien défini. On a

$$L_i(\mu_i)=\prod_{k\neq i}\frac{\mu_i-\mu_k}{\mu_i-\mu_k}=1 .$$

Si $j\neq i$, le produit $L_i(\mu_j)$ contient le facteur d'indice $k=j$, qui vaut $\frac{\mu_j-\mu_j}{\mu_i-\mu_j}=0$ : $L_i(\mu_j)=0$.

(Si $p=1$, $L_1=1$ est le produit vide et le résultat est immédiat.)

#### 6) a)

Par 5, $S(\mu_k)=\sum_{i=1}^p\sqrt{\mu_i}\,L_i(\mu_k)=\sqrt{\mu_k}$. Chaque $\lambda_i$ est l'un des $\mu_k$, donc

$$\boxed{\forall i\in[\![1;n]\!],\quad S(\lambda_i)=\sqrt{\lambda_i}}$$

#### 6) b)

Récurrence sur $k$. Pour $k=0$, $A^0=I_n=P\,{}^tP=PD^0\,{}^tP$. Si $A^k=PD^k\,{}^tP$, alors, comme ${}^tPP=I_n$ :

$$\begin{aligned}
A^{k+1} &= PD^k\,{}^tP\,PD\,{}^tP\\
&= PD^{k+1}\,{}^tP .
\end{aligned}$$

#### 6) c)

Écrivons $S=\sum_{k=0}^ms_kX^k$. Par 6.b et linéarité :

$$\begin{aligned}
S(A) &= \sum_{k=0}^ms_kPD^k\,{}^tP\\
&= P\,S(D)\,{}^tP .
\end{aligned}$$

$D^k$ est diagonale de coefficients $\lambda_i^k$, donc $S(D)$ est diagonale de coefficients $S(\lambda_i)=\sqrt{\lambda_i}$ (6.a) : $S(D)=\Delta$.

Ainsi $S(A)=P\Delta\,{}^tP$, c'est-à-dire $\boxed{B=S(A)}$.

### Partie 3 : unicité de la « racine carrée » d'une matrice symétrique positive

#### 7) a)

$AC=C^2C=C^3=CC^2=CA$.

#### 7) b)

Récurrence : $A^0C=C=CA^0$, et si $A^kC=CA^k$, alors

$$\begin{aligned}
A^{k+1}C &= A(A^kC)=A(CA^k)\\
&= (AC)A^k=CA^{k+1}.
\end{aligned}$$

Par 6.c, $B=S(A)=\sum_ks_kA^k$, donc $BC=\sum_ks_kA^kC=\sum_ks_kCA^k=CB$ : **$B$ et $C$ commutent.**

#### 8) a)

$b\circ c$ et $c\circ b$ sont les endomorphismes canoniquement associés à $BC$ et $CB$, qui sont égales (7.b) : $b\circ c=c\circ b$.

#### 8) b)

Soit $x\in E_i$, c'est-à-dire $b(x)=\sqrt{\mu_i}\,x$. Alors

$$\begin{aligned}
b\big(c(x)\big) &= c\big(b(x)\big)\\
&= \sqrt{\mu_i}\,c(x),
\end{aligned}$$

donc $c(x)\in E_i$ : **$E_i$ est stable par $c$.**

#### 8) c)

$E_i$ est un sous-espace de l'espace euclidien $\mathbb{R}^n$, donc euclidien pour le produit scalaire induit, et $c_i$ est un endomorphisme de $E_i$ (8.b). Pour $x,y\in E_i$, comme $c$ est symétrique :

$$\begin{aligned}
\langle c_i(x),y\rangle &= \langle c(x),y\rangle\\
&= \langle x,c(y)\rangle\\
&= \langle x,c_i(y)\rangle.
\end{aligned}$$

**$c_i$ est un endomorphisme symétrique de $E_i$.**

#### 8) d)

Les valeurs propres de $B$ sont les $\sqrt{\lambda_j}$, c'est-à-dire les $\sqrt{\mu_i}$ : $E_i$ est un sous-espace propre de $b$, non réduit à $\{0\}$.

L'endomorphisme symétrique $c_i$ de l'espace euclidien $E_i$ admet une base orthonormée $\mathcal{B}_i$ de vecteurs propres (théorème spectral).

Tout vecteur non nul de $E_i$ est vecteur propre de $b$ (pour $\sqrt{\mu_i}$).

Donc **$\mathcal{B}_i$ est une base orthonormée de $E_i$ formée de vecteurs propres de $c_i$ (donc de $c$) et de $b$.**

#### 8) e)

$b$ est un endomorphisme symétrique, donc diagonalisable, de sous-espaces propres deux à deux orthogonaux. Ses valeurs propres sont les $\sqrt{\mu_1},\dots,\sqrt{\mu_p}$, deux à deux distinctes (car les $\mu_i\geqslant0$ le sont et $\sqrt{\cdot}$ est injective sur $\mathbb{R}_+$). Donc $\mathbb{R}^n=E_1\oplus\dots\oplus E_p$.

En concaténant $\mathcal{B}_1,\dots,\mathcal{B}_p$, on obtient une base $\mathcal{B}$ de $\mathbb{R}^n$ (orthonormée), formée de vecteurs propres à la fois de $b$ et de $c$.

**Dans $\mathcal{B}$, les matrices de $b$ et de $c$ sont diagonales.**

#### 8) f)

Notons $\mathrm{diag}(\beta_1,\dots,\beta_n)$ et $\mathrm{diag}(\gamma_1,\dots,\gamma_n)$ les matrices de $b$ et $c$ dans $\mathcal{B}$.

Les $\beta_j$ sont des valeurs propres de $B$, les $\gamma_j$ des valeurs propres de $C$ : ils sont positifs ($B$ et $C$ sont symétriques positives, partie 1).

Comme $B^2=A=C^2$, on a $b^2=c^2$, donc $\beta_j^2=\gamma_j^2$, et par positivité $\beta_j=\gamma_j$.

Ainsi $b=c$, donc $C=B$, ce qui contredit l'hypothèse que $C$ est une autre matrice que $B$.

**$B$ est l'unique matrice de $\mathcal{S}_n^+(\mathbb{R})$ telle que $B^2=A$.**

### Partie 4 : un résultat sur l'inversibilité et la positivité

#### 9)

Soit $A\in\mathcal{S}_n(\mathbb{R})$, $A=PD\,{}^tP$ comme en 2.a.

- Si $A$ est définie positive et $\lambda$ une valeur propre, le vecteur $X\neq0$ de 1.a donne $\lambda=\frac{{}^tXAX}{{}^tXX}>0$.
- Si toutes les valeurs propres $\lambda_i$ sont strictement positives, soit $X\neq0$ et $Y={}^tPX$. Comme ${}^tP$ est inversible, $Y\neq0$ : l'un de ses coefficients est non nul, d'où ${}^tXAX=\sum_i\lambda_iy_i^2>0$ par 2.b.

**$A$ est définie positive si et seulement si ses valeurs propres sont strictement positives.**

#### 10) a)

${}^tN={}^tM-{}^tI_n=M-I_n=N$ : $N$ est symétrique.

#### 10) b)

Soit $\lambda\in\operatorname{Sp}(M)$ et $X\neq0$ tel que $MX=\lambda X$.

Alors $NX=(\lambda-1)X$ : $\lambda-1$ est valeur propre de $N$, positive car $N$ est positive (partie 1). Donc $\lambda\geqslant1$ : $\boxed{\operatorname{Sp}(M)\subset[1,+\infty[}$.

En particulier $0\notin\operatorname{Sp}(M)$ : **$M$ est inversible.**

Écrivons $M=QD'\,{}^tQ$ avec $Q$ orthogonale et $D'=\mathrm{diag}(\nu_1,\dots,\nu_n)$, $\nu_i\geqslant1$. Alors

$$I_n-M^{-1}=Q\,(I_n-D'^{-1})\,{}^tQ .$$

Cette matrice est symétrique, de valeurs propres $1-\frac1{\nu_i}\geqslant0$ : par la partie 1, **$I_n-M^{-1}$ est positive.**

#### 11) a)

$S_2$ est symétrique ($S_2=S_1+(S_2-S_1)$). Pour $X\neq0$ :

$${}^tXS_2X={}^tXS_1X+{}^tX(S_2-S_1)X>0,$$

car le premier terme est $>0$ et le second $\geqslant0$. **$S_2$ est définie positive.**

#### 11) b)

$S_1$ est définie positive, donc ses valeurs propres $\lambda_i$ sont $>0$ (question 9).

$S_1^{1/2}=P\Delta\,{}^tP$ a pour valeurs propres les $\sqrt{\lambda_i}>0$ : $0$ n'en est pas une, **$S_1^{1/2}$ est inversible.**

Comme $S_1=S_1^{1/2}S_1^{1/2}$, on a $S_1^{-1/2}S_1S_1^{-1/2}=I_n$. Donc

$$\begin{aligned}
S_1^{-1/2}(S_2-S_1)S_1^{-1/2} &= S_1^{-1/2}S_2S_1^{-1/2}-S_1^{-1/2}S_1S_1^{-1/2}\\
&= S_1^{-1/2}S_2S_1^{-1/2}-I_n .
\end{aligned}$$

#### 11) c)

$S_1^{-1/2}$ est symétrique (inverse d'une matrice symétrique : ${}^t(M^{-1})=({}^tM)^{-1}$). Donc ${}^tL={}^tS_1^{-1/2}\,{}^tS_2\,{}^tS_1^{-1/2}=L$, et $L-I_n$ est symétrique.

Pour $X\in\mathcal{M}_{n,1}(\mathbb{R})$, posons $Y=S_1^{-1/2}X$, de sorte que ${}^tY={}^tXS_1^{-1/2}$. Par 11.b :

$${}^tX(L-I_n)X={}^tX\,S_1^{-1/2}(S_2-S_1)S_1^{-1/2}X={}^tY(S_2-S_1)Y\geqslant0 .$$

**$L-I_n$ est positive.**

#### 11) d)

On applique la question 10 à $M=L\in\mathcal{S}_n(\mathbb{R})$ : $N=L-I_n$ est positive (11.c), donc **$L$ est inversible et $I_n-L^{-1}$ est positive.**

#### 11) e)

$S_2$ est inversible (définie positive, 11.a et 9). Donc

$$L^{-1}=\big(S_1^{-1/2}S_2S_1^{-1/2}\big)^{-1}=S_1^{1/2}S_2^{-1}S_1^{1/2}.$$

Comme $S_1^{-1}=S_1^{-1/2}S_1^{-1/2}$, on a $S_1^{1/2}S_1^{-1}S_1^{1/2}=I_n$, d'où

$$\begin{aligned}
S_1^{1/2}\big(S_1^{-1}-S_2^{-1}\big)S_1^{1/2} &= I_n-S_1^{1/2}S_2^{-1}S_1^{1/2}\\
&= I_n-L^{-1},
\end{aligned}$$

qui est positive (11.d). Enfin $S_1^{-1}-S_2^{-1}$ est symétrique et, pour $X\in\mathcal{M}_{n,1}(\mathbb{R})$, avec $Y=S_1^{-1/2}X$ :

$$\begin{aligned}
{}^tX\big(S_1^{-1}-S_2^{-1}\big)X &= {}^tY\,S_1^{1/2}\big(S_1^{-1}-S_2^{-1}\big)S_1^{1/2}\,Y\\
&= {}^tY\big(I_n-L^{-1}\big)Y\geqslant0 .
\end{aligned}$$

**$S_1^{-1}-S_2^{-1}$ est positive.**
