# BCE ECG — Mathématiques 2 appliquées (ESSEC) 2025 · Corrigé brut

*Corrigé rédigé par IA, non officiel. Signalez toute erreur.*

Épreuve de 4 heures (code sujet 287), calculatrice interdite. Un problème en quatre parties, 51 questions. Les bibliothèques sont importées par `import numpy as np, numpy.random as rd, matplotlib.pyplot as plt`.

---

## Partie 1 — Des résultats généraux

### 1.

Soit $\varphi(t)=\mathrm e^t-1-t$ sur $\mathbb{R}$. $\varphi$ est dérivable et $\varphi'(t)=\mathrm e^t-1$, du signe de $t$.

Donc $\varphi$ décroît sur $]-\infty,0]$, croît sur $[0,+\infty[$, et admet en $0$ son minimum $\varphi(0)=0$ :

$$\forall t\in\mathbb{R},\quad\mathrm e^t\geqslant1+t .$$

Pour $t>-1$, on applique cette inégalité à $u=\ln(1+t)$ : $1+t=\mathrm e^{u}\geqslant1+\ln(1+t)$, soit

$$\forall t>-1,\quad\ln(1+t)\leqslant t .$$

### 2. a)

$f$ est dérivable sur $[0,1]$ et

$$\begin{aligned}
f'(t)&=\mathrm e^{-t}-(1+t)\mathrm e^{-t}-1\\
&=-t\,\mathrm e^{-t}-1<0 .
\end{aligned}$$

$f$ est continue et strictement décroissante sur $[0,1]$, avec $f(0)=1>0$ et $f(1)=\frac2{\mathrm e}-1<0$ (car $\mathrm e>2$).

Par le théorème de la bijection, il existe un unique $\alpha\in\,]0,1[$ tel que $f(\alpha)=0$.

Par stricte décroissance, pour $t\in[0,1]$ : $f(t)>0=f(\alpha)\iff t<\alpha$.

### 2. b)

Par dichotomie, en gardant $f(a)>0\geqslant f(b)$ :

```python
def f(t):
    return (1+t)*np.exp(-t) - t

a = 0
b = 1
while b - a > 10**(-3):
    c = (a + b)/2
    if f(c) > 0:
        a = c
    else:
        b = c
print(a)
```

À la sortie, $a\leqslant\alpha\leqslant b$ et $b-a\leqslant10^{-3}$ : $a$ est une valeur approchée de $\alpha$ à $10^{-3}$ près.

(Exécuté : $0{,}8057$ ; $\alpha\approx0{,}8065$.)

### 2. c)

Soit $\psi(t)=1+2t-\mathrm e^t$ sur $[0,1]$ : $\psi'(t)=2-\mathrm e^t$ est positive sur $[0,\ln2]$ et négative sur $[\ln2,1]$. Donc $\psi$ croît puis décroît, et

$$\begin{aligned}
\min_{[0,1]}\psi &=\min\left(\psi(0),\psi(1)\right)\\
&=\min(0,\,3-\mathrm e)\\
&=0 .
\end{aligned}$$

Ainsi $\mathrm e^t\leqslant1+2t$ pour tout $t\in[0,1]$.

On en déduit $\mathrm e^{-t}\geqslant\frac{1}{1+2t}$ sur $[0,1]$, puis

$$\begin{aligned}
f(t)&\geqslant\frac{1+t}{1+2t}-t\\
&=\frac{1-2t^2}{1+2t}.
\end{aligned}$$

En $t_0=\frac1{\sqrt2}\in[0,1]$ : $f(t_0)\geqslant0$. Si l'on avait $t_0>\alpha$, la stricte décroissance donnerait $f(t_0)<f(\alpha)=0$. Donc $\boxed{\alpha\geqslant\frac1{\sqrt2}}$.

### 3. a)

On note $c_k=\sum_{i=0}^k\frac{p^i}{i!}\mathrm e^{-p}$ ; la suite $(c_k)$ est croissante et tend vers $1$ (série exponentielle).

```python
def minimum(x, p):
    k = 0
    terme = np.exp(-p)      # p^0 e^{-p} / 0!
    S = terme               # c_0
    while x > S:
        k = k + 1
        terme = terme * p / k
        S = S + terme       # c_k
    return k

def simulY(p):
    return minimum(rd.random(), p)
```

La boucle termine car $c_k\to1>x$. `rd.random()` simule $U\hookrightarrow\mathcal U([0,1[)$.

### 3. b)

Posons $c_{-1}=0$. Comme $0\leqslant U<1$ et $c_k\to1$, l'ensemble qui définit $Y$ est une partie non vide de $\mathbb{N}$ : $Y$ est bien défini.

Par croissance de $(c_k)$, on a, pour $k\geqslant1$ :

$$[Y=k]=[c_{k-1}<U\leqslant c_k],$$

et, pour $k=0$ :

$$[Y=0]=[U\leqslant c_0].$$

Pour $0\leqslant a\leqslant b\leqslant1$, $P(a<U\leqslant b)=b-a$ et $P(U\leqslant b)=b$. Donc

$$\begin{aligned}
P(Y=k) &=c_k-c_{k-1}\\
&=\frac{p^k}{k!}\mathrm e^{-p}.
\end{aligned}$$

**$Y$ suit la loi de Poisson de paramètre $p$.**

### 3. c)

On a $c_1=(1+p)\mathrm e^{-p}=\beta+p$. Soit $k\geqslant2$. Si $[Y=k]$ est réalisé, alors $U>c_{k-1}\geqslant c_1=\beta+p$, donc $U\notin\,]\beta,\beta+p]$ et $X=0$.

Ainsi $[Y=k]\subset[X=0]$ et

$$\begin{aligned}
P([X=0]\cap[Y=k]) &=P(Y=k)\\
&=\frac{p^k}{k!}\mathrm e^{-p}.
\end{aligned}$$

### 3. d)

Comme $\mathrm e^{-p}<1$ : $\beta=\mathrm e^{-p}+p\left(\mathrm e^{-p}-1\right)<\mathrm e^{-p}=c_0$. Et $\beta>0$ car $p<\alpha$ (2. a)).

Si $[Y=1]$ est réalisé, $\beta<c_0<U\leqslant c_1=\beta+p$, donc $X=1$ : $[X=0]\cap[Y=1]=\varnothing$. Par suite :

- $P([X=1]\cap[Y=1])=P(Y=1)-P([X=0]\cap[Y=1])=\boxed{p\,\mathrm e^{-p}}$ ;
- sur $[Y=0]=[U\leqslant c_0]$, on a $U\leqslant c_0<\beta+p$, donc $X=0\iff U\leqslant\beta$. Ainsi $[X=0]\cap[Y=0]=[U\leqslant\beta]$ et $P([X=0]\cap[Y=0])=\boxed{\beta}$ ;
- $P([X=1]\cap[Y=0])=P(Y=0)-\beta=\mathrm e^{-p}-(1+p)\mathrm e^{-p}+p=\boxed{p\left(1-\mathrm e^{-p}\right)}$.

### 3. e)

$X$ ne prend que les valeurs $0$ et $1$, donc $[X=Y]=([X=0]\cap[Y=0])\cup([X=1]\cap[Y=1])$, réunion disjointe :

$$\begin{aligned}
P(X\neq Y)&=1-\beta-p\,\mathrm e^{-p}\\
&=1-(1+p)\mathrm e^{-p}+p-p\,\mathrm e^{-p}\\
&=\boxed{1+p-(1+2p)\mathrm e^{-p}}.
\end{aligned}$$

Par la question 1 avec $t=-p$ : $\mathrm e^{-p}\geqslant1-p$, et $1+2p>0$, donc

$$\begin{aligned}
P(X\neq Y)&\leqslant1+p-(1+2p)(1-p)\\
&=1+p-(1+p-2p^2)=\boxed{2p^2}.
\end{aligned}$$

### 4. a)

$T(\omega)$ est le nombre d'indices $i$ tels que $\omega\in B_i$. Donc $T(\omega)\geqslant1$ si et seulement si $\omega$ appartient à au moins un $B_i$ :

$$[T\geqslant1]=\bigcup_{i=1}^kB_i,$$

d'où

$$P(T\geqslant1)=P\left(\bigcup_{i=1}^kB_i\right).$$

### 4. b)

**Inégalité de Markov.** Si $Z$ est une variable aléatoire à valeurs positives admettant une espérance, alors pour tout $a>0$, $P(Z\geqslant a)\leqslant\frac{E(Z)}{a}$.

$T$ est positive, à valeurs dans $[\![0,k]\!]$, donc admet une espérance ; par linéarité et $E(\mathbf 1_{B_i})=P(B_i)$, $E(T)=\sum_{i=1}^kP(B_i)$. Avec $a=1$ et 4. a) :

$$\begin{aligned}
P\left(\bigcup_{i=1}^kB_i\right)&=P(T\geqslant1)\\
&\leqslant\sum_{i=1}^kP(B_i).
\end{aligned}$$

### 5. a)

Pour tout $k$, $0\leqslant|P(X=k)-P(Y=k)|\leqslant P(X=k)+P(Y=k)$. Les séries $\sum P(X=k)$ et $\sum P(Y=k)$ convergent (de somme $1$), donc leur somme aussi ; par comparaison de séries à termes positifs, **la série définissant $\delta(X,Y)$ converge.**

### 5. b)

$[X=k]$ est la réunion disjointe de $[X=k]\cap[Y=k]$ et de $[X=k]\cap[Y\neq k]$, et $[X=k]\cap[Y=k]\subset[Y=k]$. Donc

$$\begin{aligned}
P(X=k)-P(Y=k)&=P([X=k]\cap[Y=k])+P([X=k]\cap[Y\neq k])-P(Y=k)\\
&\leqslant P([X=k]\cap[Y\neq k]).
\end{aligned}$$

Comme $P(X=k)\geqslant P(Y=k)$, le membre de gauche est $|P(X=k)-P(Y=k)|$.

### 5. c)

Si $P(X=k)\geqslant P(Y=k)$, 5. b) donne $|P(X=k)-P(Y=k)|\leqslant P([X=k]\cap[Y\neq k])$. Sinon, 5. b) appliquée en échangeant les rôles de $X$ et $Y$ donne $|P(X=k)-P(Y=k)|\leqslant P([X\neq k]\cap[Y=k])$. Dans les deux cas,

$$\begin{aligned}
&|P(X=k)-P(Y=k)|\\
&\qquad\leqslant P([X=k]\cap[Y\neq k])+P([X\neq k]\cap[Y=k]).
\end{aligned}$$

### 5. d)

Les événements $[X=k]\cap[Y\neq k]$, $k\in\mathbb{N}$, sont deux à deux incompatibles, et leur réunion est $[X\neq Y]$ (car $X$ est à valeurs dans $\mathbb{N}$).

Donc $\sum_kP([X=k]\cap[Y\neq k])=P(X\neq Y)$, et de même pour $\sum_kP([X\neq k]\cap[Y=k])$. En sommant 5. c) :

$$\delta(X,Y)\leqslant2P(X\neq Y)=2d(X,Y)\leqslant2 .$$

---

## Partie 2 — Une inégalité d'après Hodge et Le Cam

L'énoncé renvoie à « la question 2 de la partie 1 » pour la définition de $X$ et $Y$ : il s'agit de la question 3.

### 6.

$S_n$ et $T_n$ sont à valeurs dans $\mathbb{N}$, donc $\delta(S_n,T_n)\leqslant2$ (5. d)).

Si $p_k\geqslant\alpha$ pour un $k$, alors $p_k\geqslant\alpha\geqslant\frac1{\sqrt2}$ (2. c)), donc $p_k^2\geqslant\frac12$ et

$$4\sum_{i=1}^np_i^2\geqslant4p_k^2\geqslant2\geqslant\delta(S_n,T_n).$$

**$(LC)$ est vérifiée.**

### 7.

Pour chaque $k$, $X_k$ (resp. $Y_k$) est une fonction de la seule variable $U_k$.

Les $U_k$ étant indépendantes, le lemme des coalitions donne l'indépendance de $X_1,\dots,X_n$ (resp. $Y_1,\dots,Y_n$).

### 8.

Par 3. b), $Y_k\hookrightarrow\mathcal P(p_k)$, et les $Y_k$ sont indépendantes (7). Par stabilité de la loi de Poisson (récurrence et lemme des coalitions) : $\boxed{T_n\hookrightarrow\mathcal P(\lambda)}$.

Comme $0<\beta_k=f(p_k)$ et $\beta_k+p_k=(1+p_k)\mathrm e^{-p_k}\leqslant1$ (question 1), $P(X_k=1)=P(\beta_k<U_k\leqslant\beta_k+p_k)=p_k$ : $X_k\hookrightarrow\mathcal B(p_k)$.

Si tous les $p_k$ valent $\frac\lambda n$, $S_n$ est la somme de $n$ variables de Bernoulli indépendantes de même paramètre :

$$\boxed{S_n\hookrightarrow\mathcal B\left(n,\frac\lambda n\right)}.$$

Avec $\lambda$ fixé, la suite $(S_n)$ converge en loi vers une variable de loi de Poisson $\mathcal P(\lambda)$ (approximation de la loi binomiale $\mathcal B(n,\frac\lambda n)$ par la loi de Poisson).

### 9. a)

Si $X_k(\omega)=Y_k(\omega)$ pour tout $k\in[\![1,n]\!]$, alors $S_n(\omega)=T_n(\omega)$. Par contraposée, si $S_n(\omega)\neq T_n(\omega)$, il existe $k$ tel que $X_k(\omega)\neq Y_k(\omega)$ :

$$[S_n\neq T_n]\subset\bigcup_{k=1}^n[X_k\neq Y_k].$$

### 9. b)

Par 5. d), 9. a), 4. b) puis 3. e) (applicable car $p_k\in\,]0,\alpha[$) :

$$\begin{aligned}
\delta(S_n,T_n)&\leqslant2P(S_n\neq T_n)\\
&\leqslant2P\left(\bigcup_{k=1}^n[X_k\neq Y_k]\right)\\
&\leqslant2\sum_{k=1}^nP(X_k\neq Y_k)\\
&\leqslant4\sum_{k=1}^np_k^2 .
\end{aligned}$$

### 10.

Avec $p_k=\frac\lambda n$ ($<\alpha$), 8 donne $S_n\hookrightarrow\mathcal B(n,\frac\lambda n)$ et $T_n\hookrightarrow\mathcal P(\lambda)$.

Les termes de la série $\delta(S_n,T_n)$ étant positifs, on minore par la somme des termes d'indices $0$ à $n$ ; avec 9. b) :

$$\begin{aligned}
\sum_{k=0}^n\left|\binom nk\left(\frac\lambda n\right)^k\left(1-\frac\lambda n\right)^{n-k}-\frac{\lambda^k}{k!}\mathrm e^{-\lambda}\right|&\leqslant\delta(S_n,T_n)\\
&\leqslant4n\left(\frac\lambda n\right)^2=\frac{4\lambda^2}n .
\end{aligned}$$

### 11. a)

Les probabilités de succès $p_k=\frac1{n+k}$ vérifient $p_k\leqslant\frac13<\frac1{\sqrt2}\leqslant\alpha$.

La loi du nombre de succès de $n$ expériences de Bernoulli indépendantes ne dépend que des $p_k$ : $S_n$ a la même loi que la somme $\sum_kX_k$ de la partie 2, construite avec ces $p_k$, et $\lambda=s_n$.

Par 8 et 9. b), avec $T_n\hookrightarrow\mathcal P(s_n)$ :

$$\delta(S_n,T_n)\leqslant4\sum_{k=1}^n\frac1{(n+k)^2}\leqslant4\cdot\frac{n}{(n+1)^2}\leqslant\frac4n .$$

Pour tout $k\in\mathbb{N}$, $|P(S_n=k)-P(T_n=k)|$ est l'un des termes de $\delta(S_n,T_n)$ :

$$\left|P(S_n=k)-\frac{s_n^k}{k!}\mathrm e^{-s_n}\right|\leqslant\frac4n .$$

### 11. b)

$t\mapsto\frac1{n+t}$ est décroissante sur $[0,+\infty[$. Pour $t\in[k,k+1]$, $\frac1{n+t}\leqslant\frac1{n+k}$ ; pour $t\in[k-1,k]$, $\frac1{n+t}\geqslant\frac1{n+k}$.

En intégrant sur des intervalles de longueur $1$ :

$$\int_k^{k+1}\frac{\mathrm dt}{n+t}\leqslant\frac1{n+k}\leqslant\int_{k-1}^k\frac{\mathrm dt}{n+t}.$$

### 11. c)

En sommant pour $k\in[\![1,n]\!]$ (relation de Chasles) :

$$\int_1^{n+1}\frac{\mathrm dt}{n+t}\leqslant s_n\leqslant\int_0^n\frac{\mathrm dt}{n+t},$$

$$\ln\left(\frac{2n+1}{n+1}\right)\leqslant s_n\leqslant\ln(2n)-\ln(n)=\ln2 .$$

Comme $\frac{2n+1}{n+1}\to2$ et que $\ln$ est continue en $2$, l'encadrement donne $\boxed{\lim\limits_{n\to+\infty}s_n=\ln2}$.

### 11. d)

Soit $S\hookrightarrow\mathcal P(\ln2)$ et $k\in\mathbb{N}$. Par l'inégalité triangulaire et 11. a) :

$$\left|P(S_n=k)-P(S=k)\right|\leqslant\frac4n+\left|\frac{s_n^k}{k!}\mathrm e^{-s_n}-\frac{(\ln2)^k}{k!}\mathrm e^{-\ln2}\right|.$$

Par continuité de $x\mapsto\frac{x^k}{k!}\mathrm e^{-x}$ et 11. c), le second terme tend vers $0$. Donc $P(S_n=k)\to P(S=k)$ pour tout $k\in\mathbb{N}$ (et pour $k<0$, les deux sont nuls).

Les variables étant à valeurs entières, **$(S_n)_{n\geqslant2}$ converge en loi vers $S\hookrightarrow\mathcal P(\ln2)$.**

---

## Partie 3 — Étude du maximum d'une fonction

### 12.

Sur $]0,+\infty[$, $h$ est un quotient de fonctions de classe $\mathcal C^1$ dont le dénominateur ne s'annule pas : elle y est $\mathcal C^1$ et

$$h'(x)=\frac{x\,\mathrm e^x-(\mathrm e^x-1)}{x^2}=\frac{(x-1)\mathrm e^x+1}{x^2}.$$

En $0$, on utilise le développement limité $\mathrm e^x=1+x+\frac{x^2}2+x^2\varepsilon(x)$, avec $\varepsilon(x)\to0$ quand $x\to0$.

- **Continuité** : $h(x)=1+\frac x2+x\varepsilon(x)\to1=h(0)$.
- **Dérivabilité** : $\frac{h(x)-h(0)}{x}=\frac12+\varepsilon(x)\to\frac12$, donc $h$ est dérivable (à droite) en $0$ et $\boxed{h'(0)=\frac12}$.
- **Continuité de $h'$ en $0$** : $(x-1)\mathrm e^x+1=\frac{x^2}2+\frac{x^3}2+(x-1)x^2\varepsilon(x)$, donc $h'(x)=\frac12+\frac x2+(x-1)\varepsilon(x)\to\frac12=h'(0)$.

**$h$ est de classe $\mathcal C^1$ sur $\mathbb{R}^+$**, avec $h'(0)=\frac12$.

### 13. a)

$h$ est continue sur $\mathbb{R}^+$, donc $x\mapsto\int_0^xh(t)\,\mathrm dt$ est de classe $\mathcal C^1$, de dérivée $h$. Par produit, $g$ est dérivable et

$$g'(x)=-\mathrm e^{-x}\int_0^xh(t)\,\mathrm dt+\mathrm e^{-x}h(x).$$

Comme $h$ est $\mathcal C^1$, $h(x)=h(0)+\int_0^xh'(t)\,\mathrm dt=1+\int_0^xh'(t)\,\mathrm dt$. Donc

$$g'(x)=\mathrm e^{-x}\left(1-\int_0^x\big(h(t)-h'(t)\big)\,\mathrm dt\right).$$

### 13. b)

Pour $t>0$ :

$$\begin{aligned}
h(t)-h'(t)&=\frac{t(\mathrm e^t-1)-(t-1)\mathrm e^t-1}{t^2}\\
&=\frac{\mathrm e^t-1-t}{t^2}.
\end{aligned}$$

### 13. c)

Soit $\chi(t)=\mathrm e^t-1-t-\frac{t^2}2$ sur $\mathbb{R}^+$ : $\chi'(t)=\mathrm e^t-1-t\geqslant0$ (question 1) et $\chi(0)=0$, donc $\chi\geqslant0$, c'est-à-dire $\mathrm e^t-1-t\geqslant\frac{t^2}{2}$.

Par 13. b), pour $t>0$, $h(t)-h'(t)\geqslant\frac12>0$ ; et $h(0)-h'(0)=\frac12>0$.

Ainsi **$h-h'>0$ sur $\mathbb{R}^+$**, et

$$\int_0^x\big(h(t)-h'(t)\big)\,\mathrm dt\geqslant\frac x2\xrightarrow[x\to+\infty]{}+\infty .$$

### 13. d)

Soit $G(x)=\int_0^x(h-h')$. $G$ est de classe $\mathcal C^1$, de dérivée $h-h'>0$, donc strictement croissante sur $\mathbb{R}^+$.

De plus $G(0)=0$ et $G(x)\to+\infty$ (13. c)).

Par le théorème de la bijection, il existe un unique $\gamma>0$ tel que $G(\gamma)=1$, et $1-G(x)>0$ sur $[0,\gamma[$, $<0$ sur $]\gamma,+\infty[$.

Comme $\mathrm e^{-x}>0$, $g'(x)$ a le signe de $1-G(x)$ :

| $x$ | $0$ | | $\gamma$ | | $+\infty$ |
|---|---|---|---|---|---|
| $g'(x)$ | | $+$ | $0$ | $-$ | |
| $g$ | $0$ | croissante | $g(\gamma)$ | décroissante | |

**$g$ admet un maximum sur $\mathbb{R}^+$, atteint en l'unique réel $\gamma>0$.**

### 14. a)

La minoration a été établie en 13. c). Pour la majoration, soit $\omega(t)=\frac{t^2}2\mathrm e^t-\mathrm e^t+1+t$ sur $\mathbb{R}^+$ :

$$\begin{aligned}
\omega'(t) &=t\,\mathrm e^t+\frac{t^2}2\mathrm e^t-\mathrm e^t+1\\
\omega''(t) &=2t\,\mathrm e^t+\frac{t^2}2\mathrm e^t\geqslant0 .
\end{aligned}$$

$\omega'$ est croissante avec $\omega'(0)=0$, donc $\omega'\geqslant0$ ; $\omega$ est croissante avec $\omega(0)=0$, donc $\omega\geqslant0$.

Ainsi $\mathrm e^t-1-t\leqslant\frac{t^2}2\mathrm e^t$, et pour $t>0$ :

$$\frac12\leqslant\frac{\mathrm e^t-1-t}{t^2}\leqslant\frac12\mathrm e^t .$$

### 14. b)

L'encadrement $\frac12\leqslant h(t)-h'(t)\leqslant\frac12\mathrm e^t$ vaut aussi en $t=0$ (les trois termes valent $\frac12$). En intégrant sur $[0,x]$ ($x\geqslant0$) :

$$\frac x2\leqslant\int_0^x\big(h-h'\big)\leqslant\frac{\mathrm e^x-1}2 .$$

Avec 13. a), et $\mathrm e^{-x}>0$ :

$$\mathrm e^{-x}\left(1-\frac{\mathrm e^x-1}{2}\right)\leqslant g'(x)\leqslant\mathrm e^{-x}\left(1-\frac x2\right),$$

soit $\mathrm e^{-x}\dfrac{3-\mathrm e^x}{2}\leqslant g'(x)\leqslant\mathrm e^{-x}\left(1-\dfrac x2\right)$.

### 14. c)

En $x=\ln3$ : $g'(\ln3)\geqslant\frac13\cdot\frac{3-3}2=0$. Comme $g'<0$ sur $]\gamma,+\infty[$, on a $\ln3\leqslant\gamma$.

En $x=2$ : $g'(2)\leqslant\mathrm e^{-2}(1-1)=0$. Comme $g'>0$ sur $[0,\gamma[$, on a $2\geqslant\gamma$.

$$\boxed{\gamma\in[\ln3,2]}$$

### 15. a)

Soit $x\in[0,n]$. La série exponentielle est à termes positifs : sa somme $\mathrm e^x$ majore la somme partielle d'indice $n$. Pour $k\geqslant n+1$,

$$\frac{x^k}{k!}=\frac{x^n}{n!}\cdot\frac{x^{k-n}}{(n+1)(n+2)\cdots k}\leqslant\frac{x^n}{n!}\left(\frac{x}{n+1}\right)^{k-n},$$

car chacun des $k-n$ facteurs du dénominateur est au moins $n+1$. En sommant (séries à termes positifs convergentes) :

$$\mathrm e^x\leqslant\sum_{k=0}^n\frac{x^k}{k!}+\frac{x^n}{n!}\sum_{k=n+1}^{+\infty}\left(\frac x{n+1}\right)^{k-n}.$$

Avec $q=\frac x{n+1}\in[0,1[$, la série géométrique vaut $\frac{q}{1-q}=\frac{x}{n+1-x}\leqslant x$, puisque $n+1-x\geqslant1$. D'où

$$\begin{aligned}
\sum_{k=0}^n\frac{x^k}{k!}&\leqslant\mathrm e^x\\
&\leqslant\sum_{k=0}^n\frac{x^k}{k!}+\frac{x^n}{n!}\sum_{k=n+1}^{+\infty}\left(\frac{x}{n+1}\right)^{k-n}\\
&\leqslant\sum_{k=0}^n\frac{x^k}{k!}+\frac{x^{n+1}}{n!}.
\end{aligned}$$

Pour $x\in\,]0,n]$, on retranche $1$ (terme $k=0$) et on divise par $x>0$ :

$$\sum_{k=1}^n\frac{x^{k-1}}{k!}\leqslant h(x)\leqslant\sum_{k=1}^n\frac{x^{k-1}}{k!}+\frac{x^n}{n!}.$$

En $x=0$, les trois membres valent $1$ (seul le terme $k=1$ est non nul, et $n\geqslant1$) : l'encadrement vaut sur $[0,n]$.

### 15. b)

Soit $x\in[0,n]$. On intègre 15. a) sur $[0,x]\subset[0,n]$, avec $\int_0^x\frac{t^{k-1}}{k!}\,\mathrm dt=\frac{x^k}{k!\,k}$ et $\int_0^x\frac{t^n}{n!}\,\mathrm dt=\frac{x^{n+1}}{(n+1)!}$, puis on multiplie par $\mathrm e^{-x}>0$ :

$$\mathrm e^{-x}\left(\sum_{k=1}^n\frac{x^k}{k!\,k}\right)\leqslant g(x)\leqslant\mathrm e^{-x}\left(\sum_{k=1}^n\frac{x^k}{k!\,k}\right)+\mathrm e^{-x}\frac{x^{n+1}}{(n+1)!}.$$

Soit $x\geqslant0$ fixé. Pour tout entier $n\geqslant\max(1,x)$, en notant $A_n=\mathrm e^{-x}\sum_{k=1}^n\frac{x^k}{k!\,k}$ :

$$g(x)-\mathrm e^{-x}\frac{x^{n+1}}{(n+1)!}\leqslant A_n\leqslant g(x).$$

$\frac{x^{n+1}}{(n+1)!}$ est le terme général d'une série convergente (série exponentielle), donc tend vers $0$. Par encadrement, $A_n\to g(x)$ :

Pour tout $x\geqslant0$ :

$$\boxed{g(x)=\mathrm e^{-x}\sum_{k=1}^{+\infty}\frac{x^k}{k!\,k}}$$

### 16.

D'après 15. b), si $s$ est la somme partielle d'indice $n$ et $d=\frac{x^{n+1}}{(n+1)!}$, alors $0\leqslant g(x)-\mathrm e^{-x}s\leqslant\mathrm e^{-x}d$ (valable car $x\leqslant2\leqslant n$).

On ajoute des termes tant que ce majorant dépasse $10^{-4}$. Au passage de $n$ à $n+1$, le terme ajouté à $s$ est $\frac{x^{n+1}}{(n+1)!\,(n+1)}$, c'est-à-dire `d/n` après l'incrémentation de `n`.

Le majorant $d$ est, lui, multiplié par $\frac{x}{n+2}$, c'est-à-dire `x/(n+1)` après l'incrémentation.

```python
X = np.linspace(np.log(3), 2, 100)
Y = []
for x in X:
    n = 2; s = x + x**2/4; d = x**3/6
    while d * np.exp(-x) > 0.0001:
        n = n + 1
        s = s + d/n
        d = d*x/(n+1)
    Y.append(s*np.exp(-x))
plt.plot(X, Y)
plt.grid()
plt.show()
```

(Exécuté : écart à $g$ inférieur à $1{,}5\cdot10^{-5}$ ; maximum $\approx0{,}5173$ vers $x\approx1{,}50$, conforme au graphique de l'énoncé.)

---

## Partie 4 — Le problème du meilleur choix

### 17. a)

Supposons $[K_{n,s}=1]$ réalisé : un seul indice $k_0$ vérifie $X_{k_0}>s$.

Alors $a_{n,s}=k_0$ (c'est le premier, et le seul, indice où le seuil est dépassé), donc $Y_{n,s}=X_{k_0}$. Les autres $X_k$ sont $\leqslant s<X_{k_0}$, donc $Z_n=X_{k_0}=Y_{n,s}$.

Ainsi $[K_{n,s}=1]\subset[Y_{n,s}=Z_n]$ et

$$P(Y_{n,s}=Z_n)\geqslant P(K_{n,s}=1).$$

### 17. b)

Par indépendance des $X_k$ :

$$\begin{aligned}
\theta &=P\left(\bigcap_{k=1}^n[X_k\leqslant s]\right)\\
&=\prod_{k=1}^n(1-p_k)>0,
\end{aligned}$$

car $p_k\neq1$. L'événement $[K_{n,s}=1]$ est la réunion disjointe, pour $k\in[\![1,n]\!]$, des événements $[X_k>s]\cap\bigcap_{i\neq k}[X_i\leqslant s]$. Par indépendance :

$$\begin{aligned}
P(K_{n,s}=1)&=\sum_{k=1}^np_k\prod_{i\neq k}(1-p_i)\\
&=\sum_{k=1}^np_k\,\frac{\theta}{1-p_k}=\theta\sum_{k=1}^n\frac{p_k}{1-p_k}.
\end{aligned}$$

### 17. c)

Pour chaque $k$, $\frac{p_k}{1-p_k}>-1$ et, par la question 1,

$$-\ln(1-p_k)=\ln\left(1+\frac{p_k}{1-p_k}\right)\leqslant\frac{p_k}{1-p_k}.$$

En sommant : $-\ln\theta=-\sum_k\ln(1-p_k)\leqslant\sum_k\frac{p_k}{1-p_k}$. En multipliant par $\theta>0$ et avec 17. a), 17. b) :

$$P(Y_{n,s}=Z_n)\geqslant P(K_{n,s}=1)\geqslant-\theta\ln(\theta).$$

### 17. d)

On a $\theta=P(Z_n\leqslant s)=F_n(s)$, où $F_n=\prod_kF_{X_k}$.

Cette fonction est continue (les $X_k$ sont à densité), croissante, de limite $0$ en $-\infty$ et $1$ en $+\infty$.

Par le théorème des valeurs intermédiaires, il existe $s$ tel que $F_n(s)=\frac1{\mathrm e}$.

Pour ce $s$, aucun $p_k$ ne vaut $1$ : sinon $F_{X_k}(s)=0$ et $F_n(s)=0$.

Avec $\theta=\frac1{\mathrm e}$, $-\theta\ln\theta=\frac1{\mathrm e}$, et 17. c) donne

$$P(Y_{n,s}=Z_n)\geqslant\frac1{\mathrm e}$$

pour tout $s$ tel que $F_n(s)=\frac1{\mathrm e}$.

### 18. a)

$p=P(X_k>s)=1-F(s)\in\,]0,1[$, donc $F(s)\in\,]0,1[$. Pour la loi uniforme sur $[0,1[$, cela impose $s\in\,]0,1[$, où $F(s)=s$. Donc $\boxed{s=1-p}$.

### 18. b)

```python
def simulCouple(n, p):
    s = 1 - p
    X = rd.random(n)          # X_1, ..., X_n
    Z = np.max(X)
    k = 1
    while k < n and X[k-1] <= s:
        k = k + 1             # premier indice où le seuil est dépassé, sinon n
    Y = X[k-1]
    return (Z, Y)
```

### 18. c)

```python
N = 10000
c = 0
for i in range(N):
    Z, Y = simulCouple(10, 0.15)
    if Y == Z:
        c = c + 1
print(c/N)
```

La fréquence de l'événement $[Y_{10,s}=Z_{10}]$ sur $N$ simulations indépendantes estime $r_{10}$ (loi faible des grands nombres). (Exécuté avec $N=10^5$ : $0{,}560$ ; la formule de 19. e) donne $r_{10}\approx0{,}5603$.)

### 19. a)

$P(A_j)=p^k(1-p)^{n-k}>0$ par indépendance. Soit $i\in I_j$ et $x\in\mathbb{R}$. Par indépendance des $X_l$ :

$$P([X_i\leqslant x]\cap A_j)=P(s<X_i\leqslant x)\,p^{k-1}(1-p)^{n-k}.$$

Si $x\leqslant s$, $P(s<X_i\leqslant x)=0$ ; si $x>s$, il vaut $F(x)-F(s)$. En divisant par $P(A_j)$ :

$$P_{A_j}(X_i\leqslant x)=\begin{cases}\dfrac{F(x)-F(s)}{p}&\text{si }x>s\\[6pt] 0&\text{sinon.}\end{cases}$$

**Indépendance.** Soient des intervalles $J_i$, $i\in I_j$. Par indépendance des $X_l$ pour $P$ :

$$\begin{aligned}
P_{A_j}\left(\bigcap_{i\in I_j}[X_i\in J_i]\right)&=\frac{\prod_{i\in I_j}P\left(X_i\in J_i\cap\,]s,+\infty[\right)\,(1-p)^{n-k}}{p^k(1-p)^{n-k}}\\
&=\prod_{i\in I_j}\frac{P\left(X_i\in J_i\cap\,]s,+\infty[\right)}{p}.
\end{aligned}$$

Le même calcul avec un seul intervalle donne $P_{A_j}(X_i\in J_i)=\frac{P(X_i\in J_i\cap\,]s,+\infty[)}{p}$. Le produit ci-dessus est donc $\prod_{i\in I_j}P_{A_j}(X_i\in J_i)$ : **les $X_i$, $i\in I_j$, sont indépendantes pour $P_{A_j}$.**

### 19. b)

Pour $P_{A_j}$, les $X_i$ ($i\in I_j$) sont indépendantes, de même fonction de répartition $G$ donnée en 19. a).

Cette loi admet pour densité $g_s=\frac fp$ sur $]s,+\infty[$ et $0$ ailleurs.

Si $k=1$, $X_r$ est le seul élément et la probabilité vaut $1$, ce que donne aussi la formule.

Si $k\geqslant2$, soit $W=\max_{i\in I_j,\,i\neq r}X_i$. Par indépendance, $W$ a pour fonction de répartition $G^{k-1}$, et $W$ est indépendante de $X_r$ (lemme des coalitions).

Comme $[X_r=\max_{i\in I_j}X_i]=[W\leqslant X_r]$, le résultat admis donne

$$\begin{aligned}
P_{A_j}\left(X_r=\max_{i\in I_j}X_i\right)&=\int_{-\infty}^{+\infty}G(t)^{k-1}g_s(t)\,\mathrm dt\\
&=\frac1{p^k}\int_s^{+\infty}\big(F(t)-F(s)\big)^{k-1}f(t)\,\mathrm dt .
\end{aligned}$$

$F$ est continue et de classe $\mathcal C^1$ sauf en un nombre fini de points, de dérivée $f$ ailleurs : $t\mapsto\frac{(F(t)-F(s))^k}k$ est une primitive de l'intégrande sur chacun des intervalles où $F$ est $\mathcal C^1$, et elle est continue.

Pour $A>s$ :

$$\int_s^A\big(F(t)-F(s)\big)^{k-1}f(t)\,\mathrm dt=\frac{\big(F(A)-F(s)\big)^k}{k}\xrightarrow[A\to+\infty]{}\frac{(1-F(s))^k}{k}=\frac{p^k}{k}.$$

D'où $P_{A_j}\left(X_r=\max_{i\in I_j}X_i\right)=\dfrac1k$.

### 19. c)

$[K_{n,s}=k]$ est la réunion disjointe des $A_j$, $j\in[\![1,\binom nk]\!]$ (l'ensemble des indices où le seuil est dépassé est l'un des $I_j$). Donc

$$\begin{aligned}
&P([Y_{n,s}=Z_n]\cap[K_{n,s}=k])\\
&\qquad=\sum_{j=1}^{\binom nk}P([Y_{n,s}=Z_n]\cap A_j).
\end{aligned}$$

Sur $A_j$ ($k\geqslant1$), le premier indice où le seuil est dépassé est $r=\min I_j$, donc $Y_{n,s}=X_r$.

De plus $Z_n=\max_{i\in I_j}X_i$, car les autres $X_i$ sont $\leqslant s$.

Ainsi $[Y_{n,s}=Z_n]\cap A_j=[X_r=\max_{i\in I_j}X_i]\cap A_j$, et par 19. b) :

$$P_{A_j}(Y_{n,s}=Z_n)=\frac1k .$$

### 19. d)

$A_0=[K_{n,s}=0]=\bigcap_{i=1}^n[X_i\leqslant s]$, de probabilité $(1-p)^n>0$. Sur $A_0$, $a_{n,s}=n$ et $Y_{n,s}=X_n$.

Comme en 19. a), pour $P_{A_0}$ les $X_i$ sont indépendantes, de fonction de répartition $\frac{F(x)}{F(s)}$ pour $x\leqslant s$ (et $1$ pour $x>s$).

Cette loi a pour densité $\frac f{1-p}$ sur $]-\infty,s]$.

Comme en 19. b), avec $W=\max_{i<n}X_i$ :

$$\begin{aligned}
P_{A_0}(Y_{n,s}=Z_n)&=\frac1{(1-p)^n}\int_{-\infty}^sF(t)^{n-1}f(t)\,\mathrm dt\\
&=\frac1{(1-p)^n}\cdot\frac{F(s)^n}n=\frac1n,
\end{aligned}$$

car $F(s)=1-p$ et $F(t)^n\to0$ en $-\infty$ (pour $n=1$, la probabilité vaut directement $1$). Donc

$$\begin{aligned}
&P([Y_{n,s}=Z_n]\cap[K_{n,s}=0])\\
&\qquad=\frac1n(1-p)^n .
\end{aligned}$$

### 19. e)

Les événements $[K_{n,s}=k]$, $k\in[\![0,n]\!]$, forment un système complet. Avec 19. c) et $P([Y_{n,s}=Z_n]\cap A_j)=P(A_j)\,P_{A_j}(Y_{n,s}=Z_n)=\frac{p^k(1-p)^{n-k}}{k}$ :

$$\boxed{r_n=\frac1n(1-p)^n+\sum_{k=1}^n\frac1k\binom nkp^k(1-p)^{n-k}}$$

(Vérifié par simulation pour $n\in\{3,7\}$ et $p\in\{0{,}2;\,0{,}5\}$.)

### 20. a)

On applique la question 10 (partie 2), où les $p_k$ valent $\frac\lambda n$ : pour $\frac\lambda n<\alpha$,

$$\sum_{k=0}^n\left|\binom nk\left(\frac\lambda n\right)^k\left(1-\frac\lambda n\right)^{n-k}-\frac{\lambda^k}{k!}\mathrm e^{-\lambda}\right|\leqslant\frac{4\lambda^2}{n}.$$

Pour $k\geqslant1$, on a $\frac1k\leqslant1$ ; et l'on peut ajouter le terme positif d'indice $0$.

La somme pondérée par $\frac1k$, pour $k$ de $1$ à $n$, est donc majorée par la même quantité.

Comme $p=\frac\lambda n$ est une probabilité, on a $n>\lambda$. Si $\alpha\leqslant\frac\lambda n<1$, la somme est au plus $\sum_k\binom nkp^k(1-p)^{n-k}+\sum_k\frac{\lambda^k}{k!}\mathrm e^{-\lambda}\leqslant2$, et $\frac{4\lambda^2}n=4n\left(\frac\lambda n\right)^2\geqslant4\alpha^2\geqslant2$. L'inégalité vaut donc pour tout $n>\lambda$.

Pour $n\leqslant\lambda$, $p=\frac\lambda n$ n'est plus une probabilité et l'inégalité de l'énoncé est fausse : avec $n=5$ et $\lambda=15$, la somme vaut environ $1\,211$, pour une borne $\frac{4\lambda^2}n=180$.

L'énoncé suppose implicitement $n>\lambda$.

### 20. b)

Avec $p=\frac\lambda n$, 19. e) donne $r_n=\frac1n\left(1-\frac\lambda n\right)^n+\sum_{k=1}^n\frac1k\binom nk\left(\frac\lambda n\right)^k\left(1-\frac\lambda n\right)^{n-k}$.

- $0\leqslant\frac1n\left(1-\frac\lambda n\right)^n\leqslant\frac1n\to0$.
- Par 20. a), la seconde somme diffère de $\mathrm e^{-\lambda}\sum_{k=1}^n\frac{\lambda^k}{k!\,k}$ d'au plus $\frac{4\lambda^2}n\to0$.
- $\mathrm e^{-\lambda}\sum_{k=1}^n\frac{\lambda^k}{k!\,k}\to\mathrm e^{-\lambda}\sum_{k=1}^{+\infty}\frac{\lambda^k}{k!\,k}$ (série convergente, 15. b)).

Donc

$$\boxed{\lim_{n\to+\infty}r_n=\left(\sum_{k=1}^{+\infty}\frac{\lambda^k}{k!\,k}\right)\mathrm e^{-\lambda}}$$

### 21.

D'après 15. b), cette limite vaut $g(\lambda)$. D'après 13. d), $g$ atteint son maximum sur $\mathbb{R}^+$ en $\gamma\in[\ln3,2]$ uniquement.

Il faut donc prendre $\lambda=\gamma$, c'est-à-dire $p=\frac\gamma n$.

**On choisit le seuil $s$ tel que $P(X_k>s)=\frac{\gamma}{n}$, soit $F(s)=1-\frac\gamma n$** (un tel $s$ existe par le théorème des valeurs intermédiaires, $F$ étant continue).

La probabilité de choisir le maximum vaut alors environ $g(\gamma)\approx0{,}517$ (lecture du graphique : $\gamma\approx1{,}5$). Pour la loi uniforme sur $[0,1[$, $s=1-\frac\gamma n$.
