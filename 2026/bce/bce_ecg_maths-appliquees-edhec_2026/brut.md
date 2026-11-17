# BCE ECG — Maths appliquées (EDHEC) 2026 · Corrigé brut

*Corrigé rédigé par IA, non officiel. Signalez toute erreur.*

Épreuve de 4 heures, sans calculatrice ni document. Les bibliothèques Python sont importées sous les noms `np`, `plt` et `rd`.

## Exercice 1

### Question 1

```python
def suite_u(a,n):
    u=a
    for k in range(1,n+1):
        u=u**2-u+1
    return u
```

Après le passage d'indice `k` dans la boucle, `u` contient $u_k$ ; la fonction renvoie donc $u_n$ (et $u_0=a$ si $n=0$).

### Question 2

Supposons que $(u_n)$ converge vers un réel $\ell$. La fonction $x\mapsto x^2-x+1$ est continue sur $\mathbb R$ ; en passant à la limite dans la relation de récurrence, on obtient $\ell=\ell^2-\ell+1$, soit $(\ell-1)^2=0$.

Donc $\boxed{\ell=1.}$

### Question 3

**a)** Pour tout $n\in\mathbb N$ :

$$\begin{aligned}
u_{n+1}-u_n&=u_n^2-2u_n+1\\
&=(u_n-1)^2\ge0.
\end{aligned}$$

**La suite $(u_n)$ est croissante.**

**b)** Par croissance, pour tout $n\in\mathbb N$, $\boxed{u_n\ge u_0=a.}$

**c)** Si $(u_n)$ convergeait, sa limite vérifierait $\ell\ge a$ par passage à la limite dans l'inégalité large de b), donc $\ell\ge a>1$. Or $\ell=1$ par la question 2 : c'est absurde. **La suite $(u_n)$ diverge.**

Elle est croissante. Une suite croissante majorée converge (théorème de la limite monotone) ; $(u_n)$ n'est donc pas majorée, et une suite croissante non majorée tend vers $+\infty$ :

$$\boxed{\lim_{n\to+\infty}u_n=+\infty.}$$

### Question 4

Comme $u_n\ge a>1$, on a $u_n\neq0$ et

$$\frac{u_{n+1}}{u_n^2}=1-\frac1{u_n}+\frac1{u_n^2}.$$

Comme $u_n\to+\infty$, ce quotient tend vers $1$ : **la proposition ❷ est vraie**, $\boxed{u_{n+1}\underset{+\infty}{\sim}u_n^2.}$

Les autres sont fausses : $\frac{u_{n+1}}{u_n}=u_n-1+\frac1{u_n}\to+\infty$ exclut ❶, et $u_{n+1}\to+\infty$ alors que $\frac1{u_n^2}$ et $\frac1{u_n}$ tendent vers $0$, ce qui exclut ❸ et ❹.

### Question 5

**a)** Par la question 3.b, $u_n-1\ge a-1>0$ et $u_{n+1}-1>0$ : l'expression existe. Par ailleurs

$$u_{n+1}-1=u_n^2-u_n=u_n(u_n-1).$$

Donc

$$\begin{aligned}
\frac1{u_n-1}-\frac1{u_{n+1}-1}&=\frac1{u_n-1}-\frac1{u_n(u_n-1)}\\
&=\frac{u_n-1}{u_n(u_n-1)}\\
&=\boxed{\frac1{u_n}.}
\end{aligned}$$

**b)** Par télescopage :

$$\begin{aligned}
\sum_{k=0}^n\frac1{u_k}&=\sum_{k=0}^n\Big(\frac1{u_k-1}-\frac1{u_{k+1}-1}\Big)\\
&=\boxed{\frac1{a-1}-\frac1{u_{n+1}-1}.}
\end{aligned}$$

**c)** Comme $u_{n+1}\to+\infty$, $\frac1{u_{n+1}-1}\to0$. Les sommes partielles convergent : **la série de terme général $\frac1{u_n}$ converge**, et

$$\boxed{\sum_{n=0}^{+\infty}\frac1{u_n}=\frac1{a-1}.}$$

### Question 6

On suppose $a=2$. On a alors $u_0=2$, $u_1=3$, $u_2=7$.

**a)** Pour tout $n\in\mathbb N$, $\frac1{u_n}>0$, et par la question 5.c avec $a=2$, $\sum_{n=0}^{+\infty}\frac1{u_n}=\frac1{2-1}=1$.

Une famille de réels positifs indexée par $\mathbb N$ et de somme 1 définit **la loi d'une variable aléatoire $X$ à valeurs dans $\mathbb N$**.

**b)** Pour $n\ge2$, posons $t=2^n\ge4$. Alors

$$\begin{aligned}
2^n(2^n-1)+1-2^{n+1}&=t^2-3t+1\\
&=t(t-3)+1.
\end{aligned}$$

Comme $t\ge4$, on a $t(t-3)\ge4$, donc cette quantité est strictement positive : $\boxed{2^n(2^n-1)+1\ge2^{n+1}.}$

**c)** Récurrence sur $n\ge2$.

*Initialisation.* $u_2=7\ge4=2^2$.

*Hérédité.* Supposons $u_n\ge2^n$ pour un $n\ge2$. La fonction $\psi:x\mapsto x(x-1)+1$ est croissante sur $[1,+\infty[$, car $\psi'(x)=2x-1>0$. Comme $u_n\ge2^n\ge1$ :

$$\begin{aligned}
u_{n+1}&=\psi(u_n)\ge\psi(2^n)\\
&=2^n(2^n-1)+1\ge2^{n+1},
\end{aligned}$$

la dernière inégalité par b). Par récurrence, $\boxed{u_n\ge2^n\text{ pour tout }n\ge2.}$

Pour $n=0$ et $n=1$ : $u_0=2\ge1=2^0$ et $u_1=3\ge2=2^1$. L'inégalité vaut donc pour tout $n\in\mathbb N$.

**d)** *Espérance.* Pour tout $n$, $0\le\frac n{u_n}\le\frac n{2^n}$. La série $\sum n\big(\frac12\big)^{n-1}$ converge (série géométrique dérivée, de raison $\frac12\in\,]-1,1[$), donc $\sum\frac n{2^n}$ aussi.

Par comparaison de séries à termes positifs, $\sum nP(X=n)$ converge absolument : **$X$ admet une espérance.**

*Variance.* De même, $0\le\frac{n^2}{u_n}\le\frac{n^2}{2^n}$, et $n^2\cdot\frac{n^2}{2^n}=\frac{n^4}{2^n}\to0$ par croissances comparées. Donc $\frac{n^2}{2^n}=o\big(\frac1{n^2}\big)$ et la série de Riemann $\sum\frac1{n^2}$ converge.

Par comparaison, $\sum n^2P(X=n)$ converge : $X$ admet un moment d'ordre 2, donc **$X$ admet une variance.**

## Exercice 2

### Question 1

**a)** Le système s'écrit $Y'=MY$ avec $Y=\begin{pmatrix}f\\g\end{pmatrix}$ et $M=\begin{pmatrix}1&-2\\2&5\end{pmatrix}$ : c'est un système différentiel linéaire à coefficients constants, avec la condition initiale $Y(0)={}^t(1,1)$. Par le théorème d'existence et d'unicité de la solution d'un problème de Cauchy, **ce problème possède un et un seul couple $(f,g)$ solution.**

**b)** $f$ et $g$ sont dérivables sur $\mathbb R$.

Donc $f'=f-2g$ et $g'=2f+5g$ sont dérivables comme combinaisons linéaires de fonctions dérivables : **$f$ et $g$ sont deux fois dérivables sur $\mathbb R$.**

### Question 2

**a)** On dérive la première équation (licite par 1.b) et on utilise la seconde :

$$\begin{aligned}
f''&=f'-2g'\\
&=f'-2(2f+5g)\\
&=f'-4f-10g.
\end{aligned}$$

La première équation donne $2g=f-f'$, donc $10g=5f-5f'$. Ainsi $f''=f'-4f-5f+5f'=6f'-9f$ :

$$\boxed{f''-6f'+9f=0.}$$

**b)** $f'(0)=f(0)-2g(0)=1-2=\boxed{-1.}$

**c)** L'équation caractéristique $r^2-6r+9=(r-3)^2=0$ a la racine double $3$. Les solutions de $(E)$ sont les fonctions $x\mapsto(\alpha x+\beta)e^{3x}$, $(\alpha,\beta)\in\mathbb R^2$.

On a $f(0)=\beta=1$ et $f'(x)=(\alpha+3\alpha x+3\beta)e^{3x}$, donc $f'(0)=\alpha+3=-1$, soit $\alpha=-4$ :

$$\boxed{f(x)=(1-4x)e^{3x}.}$$

**d)** $g=\frac12(f-f')$, avec $f'(x)=(-1-12x)e^{3x}$. Donc

$$\begin{aligned}
g(x)&=\frac12\big((1-4x)-(-1-12x)\big)e^{3x}\\
&=\boxed{(1+4x)e^{3x}.}
\end{aligned}$$

Vérification : $g(0)=1$, et $g'(x)=(7+12x)e^{3x}=2f(x)+5g(x)$.

### Question 3

**a)** *Sens direct.* Si $(f,g)$ vérifie $(S)$, alors $h'=f'+g'=3f+3g=3h$.

*Réciproque.* Si $f'=f-2g$ et $h'=3h$, alors

$$\begin{aligned}
g'&=h'-f'=3f+3g-(f-2g)\\
&=2f+5g.
\end{aligned}$$

Donc

$$\boxed{(S)\iff\forall x\in\mathbb R,\ \begin{cases}f'(x)=f(x)-2g(x)\\h'(x)=3h(x).\end{cases}}$$

**b)** $h(0)=f(0)+g(0)=2$. Les solutions de $h'=3h$ sont les $x\mapsto Ce^{3x}$, et $h(0)=C=2$ :

$$\boxed{h(x)=2e^{3x}.}$$

**c)** Avec les conditions initiales $f(0)=g(0)=1$, la condition $h'=3h$ équivaut, par b), à $f+g=2e^{3x}$. Dans ce cas $g=2e^{3x}-f$ et

$$\begin{aligned}
f-2g&=f-4e^{3x}+2f\\
&=3f-4e^{3x}.
\end{aligned}$$

L'équation $f'=f-2g$ équivaut donc à $f'=3f-4e^{3x}$. Avec a) :

$$\boxed{(S)\iff\forall x\in\mathbb R,\ \begin{cases}f'(x)=3f(x)-4e^{3x}\\(f+g)(x)=2e^{3x}.\end{cases}}$$

### Question 4

**a)** $f_a$ est dérivable et

$$\begin{aligned}
f_a'(x)&=ae^{3x}+3axe^{3x}\\
&=3f_a(x)+ae^{3x}.
\end{aligned}$$

$f_a$ est solution de $(ED)$ si et seulement si $ae^{3x}=-4e^{3x}$ pour tout $x$, soit $\boxed{a=-4.}$

**b)** Les solutions de $(ED)$ sont la somme de la solution particulière $f_{-4}$ et des solutions de l'équation homogène $y'=3y$ :

$$y(x)=Ce^{3x}-4xe^{3x},\quad C\in\mathbb R.$$

La condition $f(0)=1$ impose $C=1$ :

$$\boxed{f(x)=(1-4x)e^{3x}.}$$

**c)** Par 3.c, $g=2e^{3x}-f$, et on retrouve :

$$\boxed{\begin{aligned}f(x)&=(1-4x)e^{3x},\\g(x)&=(1+4x)e^{3x}.\end{aligned}}$$

### Question 5

**a)**

```python
def f(x):
    return (1-4*x)*np.exp(3*x)

def g(x):
    return (1+4*x)*np.exp(3*x)
```

**b)**

```python
X = np.linspace(-1/2, 1/2, 200)
plt.plot(X, f(X))
plt.plot(X, g(X))
plt.show()
```

`np.exp` agissant terme à terme, `f(X)` et `g(X)` sont les tableaux des images.

## Exercice 3

### Question 1

**a)**

$$F(x)=\begin{cases}0&\text{si }x<0,\\[1mm]\dfrac x\theta&\text{si }0\le x\le\theta,\\[1mm]1&\text{si }x>\theta.\end{cases}$$

**b)** $\boxed{E(X)=\frac\theta2}$ et $\boxed{V(X)=\frac{\theta^2}{12}.}$

### Question 2

**a)** Pour $x\in\mathbb R$, $Y_n\le x$ si et seulement si tous les $X_i$ sont inférieurs ou égaux à $x$. Par indépendance mutuelle des $X_i$, qui ont tous la fonction de répartition $F$ :

$$\begin{aligned}F_n(x)&=P\Big(\bigcap_{i=1}^n[X_i\le x]\Big)\\&=\prod_{i=1}^nP(X_i\le x)=F(x)^n.\end{aligned}$$

Donc

$$\boxed{F_n(x)=\begin{cases}0&\text{si }x<0,\\[1mm]\Big(\dfrac x\theta\Big)^n&\text{si }0\le x\le\theta,\\[1mm]1&\text{si }x>\theta.\end{cases}}$$

**b)** $F_n$ est continue sur $\mathbb R$ : elle l'est sur chacun des trois intervalles, et les raccords en $0$ (valeur $0$) et en $\theta$ (valeur $1$) sont continus.

Elle est de classe $\mathcal C^1$ sur $\mathbb R$ privé de $0$ et $\theta$. **$Y_n$ est donc une variable à densité**, et une densité s'obtient en dérivant $F_n$ là où elle est dérivable :

$$\boxed{f_n(x)=\begin{cases}\dfrac{n\,x^{n-1}}{\theta^n}&\text{si }0\le x\le\theta,\\[1mm]0&\text{sinon.}\end{cases}}$$

### Question 3

**a)** Soit $U\hookrightarrow\mathcal U([0,1])$ et $x\in\mathbb R$. Comme $\theta>0$, les événements $[\theta U\le x]$ et $[U\le\frac x\theta]$ sont égaux.

La probabilité $P(\theta U\le x)$ est donc la valeur en $\frac x\theta$ de la fonction de répartition de $U$ :

- elle vaut $0$ si $x<0$ ;
- elle vaut $\frac x\theta$ si $0\le x\le\theta$ ;
- elle vaut $1$ si $x>\theta$.

C'est la fonction $F$ de la question 1.a : **$\theta U$ suit la loi uniforme sur $[0,\theta]$.**

**b)**

```python
def var_Y(theta,n):
    X=theta*rd.random(n)
    Y=np.max(X)
    return Y
```

Par a), `X` simule $n$ variables indépendantes de loi $\mathcal U([0,\theta])$, et `Y` est leur maximum.

### Question 4

**a)** $f_n$ est nulle hors de $[0,\theta]$ : l'intégrale $\int_{-\infty}^{+\infty}|t|f_n(t)\,dt$ se réduit à une intégrale sur un segment, donc converge. $Y_n$ admet une espérance et

$$\begin{aligned}
E(Y_n)&=\int_0^\theta t\,\frac{n\,t^{n-1}}{\theta^n}\,dt\\
&=\frac n{\theta^n}\cdot\frac{\theta^{n+1}}{n+1}=\boxed{\frac{n\theta}{n+1}.}
\end{aligned}$$

**b)** De même, $Y_n$ admet un moment d'ordre 2 :

$$\begin{aligned}
E(Y_n^2)&=\int_0^\theta t^2\,\frac{n\,t^{n-1}}{\theta^n}\,dt\\
&=\frac{n\theta^2}{n+2}.
\end{aligned}$$

Donc $Y_n$ admet une variance et, par la formule de König-Huygens :

$$\begin{aligned}
V(Y_n)&=\frac{n\theta^2}{n+2}-\frac{n^2\theta^2}{(n+1)^2}\\
&=n\theta^2\,\frac{(n+1)^2-n(n+2)}{(n+1)^2(n+2)}\\
&=\boxed{\frac{n\theta^2}{(n+1)^2(n+2)}.}
\end{aligned}$$

### Question 5

**a)** $Z_n=\frac{n+1}n\max(X_1,\dots,X_n)$ est une fonction de l'échantillon $(X_1,\dots,X_n)$ qui ne dépend pas de $\theta$ : **c'est un estimateur de $\theta$.** Par linéarité de l'espérance et 4.a :

$$\begin{aligned}
E(Z_n)&=\frac{n+1}n\cdot\frac{n\theta}{n+1}\\
&=\boxed{\theta.}
\end{aligned}$$

**b)** Par 4.b :

$$\begin{aligned}
V(Z_n)&=\frac{(n+1)^2}{n^2}\cdot\frac{n\theta^2}{(n+1)^2(n+2)}\\
&=\boxed{\frac{\theta^2}{n(n+2)}.}
\end{aligned}$$

### Question 6

**a)** On a $0<5\le\theta\le7$. Les deux membres étant positifs, $\theta^2\le49$. Pour $n\ge47$, $n+2\ge49$, donc

$$\boxed{\frac{\theta^2}{n+2}\le\frac{49}{49}=1.}$$

**b)** $Z_n$ admet une espérance $\theta$ et une variance. Pour tout $\varepsilon>0$, l'inégalité de Bienaymé-Tchebychev s'écrit

$$P\big(|Z_n-\theta|\ge\varepsilon\big)\le\frac{V(Z_n)}{\varepsilon^2}.$$

Pour $n\ge47$, par 5.b et a) :

$$\begin{aligned}
\frac{V(Z_n)}{\varepsilon^2}&=\frac1{n\varepsilon^2}\cdot\frac{\theta^2}{n+2}\\
&\le\frac1{n\varepsilon^2}.
\end{aligned}$$

L'événement $[|Z_n-\theta|\le\varepsilon]$ contient $[|Z_n-\theta|<\varepsilon]$, qui est le contraire de $[|Z_n-\theta|\ge\varepsilon]$. Donc

$$\begin{aligned}
P\big(|Z_n-\theta|\le\varepsilon\big)&\ge1-P\big(|Z_n-\theta|\ge\varepsilon\big)\\
&\ge\boxed{1-\frac1{n\varepsilon^2}.}
\end{aligned}$$

**c)** Avec $\varepsilon=\frac1{10}$ et $n\ge2000\ge47$ :

$$\begin{aligned}
1-\frac1{n\varepsilon^2}&=1-\frac{100}n\\
&\ge1-\frac{100}{2000}=0{,}95.
\end{aligned}$$

Or $|Z_n-\theta|\le\frac1{10}$ équivaut à $Z_n-\frac1{10}\le\theta\le Z_n+\frac1{10}$. Les bornes $Z_n\pm\frac1{10}$ sont des estimateurs, qui ne dépendent pas de $\theta$, et

$$P\Big(Z_n-\frac1{10}\le\theta\le Z_n+\frac1{10}\Big)\ge0{,}95.$$

**L'intervalle $\big[Z_n-\frac1{10},Z_n+\frac1{10}\big]$ est un intervalle de confiance pour $\theta$ au niveau de confiance au moins $0{,}95$.**

### Question 7

La fonction `mystere(theta)` répète $1000$ fois l'expérience suivante :

- simuler $Y_{2000}$ pour la valeur `theta` du paramètre ;
- calculer `z = 2001*y/2000`, c'est-à-dire une réalisation de $Z_{2000}=\frac{2001}{2000}Y_{2000}$ ;
- incrémenter le compteur `c` si $|z-\theta|\le0{,}1$, c'est-à-dire si $\theta$ appartient à l'intervalle $\big[z-\frac1{10},z+\frac1{10}\big]$.

Elle renvoie `c/1000`, la fréquence des simulations pour lesquelles l'intervalle de confiance de la question 6.c contient la vraie valeur $\theta=6$.

**Le résultat affiché est une valeur approchée de $P\big(|Z_{2000}-6|\le0{,}1\big)$**, qui est au moins $0{,}95$ par 6.c. En fait, cette probabilité vaut $1-\big(\frac{5{,}9\times2000}{2001\times6}\big)^{2000}$, très proche de 1 : on obtient en pratique `1.0`. La majoration de Bienaymé-Tchebychev est très pessimiste ici.

## Problème — Partie 1 : préliminaires

### Question 1

**a)** Le coefficient $(i,j)$ de $J_n^2$ vaut $\sum_{k=1}^n1\times1=n$, donc $J_n^2=nJ_n$.

Ainsi $P(J_n)=J_n^2-nJ_n=0$ : **$P$ est un polynôme annulateur de $J_n$.**

**b)** $J_n$ est une matrice symétrique (réelle), donc **elle est diagonalisable.** Ses valeurs propres sont racines du polynôme annulateur $P(x)=x(x-n)$ : elles sont dans $\{0,n\}$.

On suppose $n\ge2$ (un graphe connexe d'ordre 1 n'a pas d'intérêt ici).

- Si $0$ était la seule valeur propre, $J_n$, diagonalisable, serait semblable à la matrice nulle, donc nulle : absurde.
- Si $n$ était la seule valeur propre, $J_n$ serait semblable à $nI_n$, donc égale à $nI_n$ ; or ses coefficients hors diagonale valent $1\neq0$ : absurde.

**$J_n$ possède donc deux valeurs propres, $0$ et $n$.**

**c)** Notons $S=x_1+\dots+x_n$. Chaque coefficient de $J_nX$ vaut $S$. Donc $J_nX=nX$ si et seulement si $x_i=\frac Sn$ pour tout $i$.

- Si $J_nX=nX$, tous les $x_i$ sont égaux à $\frac Sn$, donc égaux à $x_1$.
- Réciproquement, si $x_2=\dots=x_n=x_1$, alors $S=nx_1$ et $J_nX=nx_1U=nX$.

D'où l'équivalence demandée.

**d)** Par c), le sous-espace propre de $J_n$ associé à $n$ est $\{x_1U,\ x_1\in\mathbb R\}=\mathrm{Vect}(U)$, avec $U\neq0$ : **il est de dimension 1 et engendré par $U$.**

## Problème — Partie 2 : quelques généralités

### Question 2

**a)** Le graphe a pour arêtes $\{1,2\}$, $\{2,3\}$, $\{3,4\}$ et $\{4,1\}$ : c'est le cycle $1-2-3-4-1$. Il est simple, connexe, d'ordre $4$.

- Chaque sommet a exactement deux voisins : le degré maximal est $d=2$.
- Les paires de sommets adjacents sont à distance 1. Les deux paires non adjacentes $\{1,3\}$ et $\{2,4\}$ sont à distance 2, par les chaînes $1-2-3$ et $2-1-4$.

Le diamètre vaut donc $2$ : **ce graphe est élément de $E_4(2)$.**

**b)** **Les graphes $G_1$ et $G_3$ sont éléments de $E_5(2)$** :

- $G_1$ est le cycle $1-2-3-4-5-1$. Tous les degrés valent 2. Deux sommets non adjacents ont un voisin commun (par exemple $1-2-3$), donc sont à distance 2 : $D=2$.
- $G_3$ (l'étoile) a pour arêtes $\{1,3\},\{3,5\},\{5,2\},\{2,4\},\{4,1\}$ : c'est le cycle $1-3-5-2-4-1$. Pour la même raison, $d=2$ et $D=2$.
- $G_2$ n'en fait pas partie : le sommet 1 est relié à 2, 3, 4 et 5, donc son degré vaut $4$ et $d=4\neq2$.
- $G_4$ n'en fait pas partie : c'est la chaîne $3-2-1-4-5$, et la distance de 3 à 5 vaut 4, donc $D=4\neq2$.

### Question 3

**a)** Le graphe est simple : chaque voisin de $s$ correspond à exactement une arête d'extrémité $s$. Le nombre de voisins de $s$ est donc son degré, au plus égal au degré maximal : **$s$ possède au plus $d$ voisins.**

**b)** Comme $D=2$, tout sommet $t\neq s$ est à distance 1 ou 2 de $s$.

- Les sommets à distance 1 sont les voisins de $s$ : il y en a au plus $d$.
- Un sommet à distance 2 de $s$ est voisin d'un voisin $v$ de $s$.
- Or $v$ a au plus $d$ voisins, dont $s$ lui-même : il en a au plus $d-1$ autres.
- Comme $s$ a au plus $d$ voisins, il y a au plus $d(d-1)$ sommets à distance 2.

Le nombre de sommets autres que $s$ est donc au plus $\boxed{d+d(d-1).}$ (L'énoncé note $n$ ce nombre ; il vaut $n-1$, ce qui donne bien $n\le d^2+1$ en c.)

**c)** En ajoutant $s$ : $n\le1+d+d(d-1)$, soit $\boxed{n\le d^2+1.}$

## Problème — Partie 3 : étude de la matrice d'adjacence d'un graphe de Moore

### Question 4

Le graphe n'est pas orienté : le nombre d'arêtes reliant $i$ et $j$ est celui des arêtes reliant $j$ et $i$, donc $a_{i,j}=a_{j,i}$ pour tous $i,j$.

**$A$ est symétrique.**

### Question 5

**a)** Le graphe est simple, donc sans arêtes multiples : deux sommets sont reliés par au plus une arête, et $\boxed{a_{i,j}\in\{0,1\}.}$

**b)** Le graphe est sans boucle : aucune arête ne relie un sommet à lui-même, donc $\boxed{a_{i,i}=0.}$

### Question 6

**a)** Par la définition du produit matriciel avec $E=F=A$, puis la symétrie de $A$ ($a_{k,j}=a_{j,k}$) :

$$\boxed{\begin{aligned}b_{i,j}&=\sum_{k=1}^na_{i,k}a_{k,j}\\&=\sum_{k=1}^na_{i,k}a_{j,k}.\end{aligned}}$$

**b)** Avec $j=i$, $b_{i,i}=\sum_ka_{i,k}^2$, et $a_{i,k}^2=a_{i,k}$ puisque $a_{i,k}\in\{0,1\}$. Donc $\boxed{b_{i,i}=\sum_{k=1}^na_{i,k}.}$

Cette somme compte les sommets $k$ reliés à $i$, c'est-à-dire le degré de $i$, qui vaut $d$ : $\boxed{b_{i,i}=d.}$

### Question 7

**a)** Soit $i\neq j$. Par l'hypothèse admise, $i$ et $j$ sont reliés par exactement une chaîne de longueur 1 ou 2.

- Si $i$ et $j$ sont voisins, alors $a_{i,j}=1$ et la chaîne unique est l'arête qui les relie. Il n'existe donc aucune chaîne de longueur 2 entre eux, et $b_{i,j}=0$.
- Sinon, $a_{i,j}=0$, et la chaîne unique est de longueur 2 : $b_{i,j}=1$.

D'où $\boxed{(a_{i,j},b_{i,j})=(0,1)\text{ ou }(1,0).}$

**b)** Dans les deux cas, $\boxed{b_{i,j}+a_{i,j}=1}$ pour $i\neq j$.

**c)** Par 6.b et 5.b, $\boxed{b_{i,i}+a_{i,i}=d.}$

### Question 8

Le coefficient $(i,j)$ de $A^2+A=B+A$ vaut $1$ si $i\neq j$ et $d$ si $i=j$ (questions 7.b et 7.c).

Celui de $(d-1)I_n+J_n$ vaut $0+1=1$ si $i\neq j$ et $(d-1)+1=d$ si $i=j$. Les deux matrices ont les mêmes coefficients :

$$\boxed{A^2+A=(d-1)I_n+J_n.}$$

## Problème — Partie 4 : valeurs propres possibles de A

### Question 9

$A$ est une matrice symétrique réelle (question 4), donc **$A$ est diagonalisable.**

### Question 10

**a)** Par le rappel sur le produit matriciel, la $i$-ème composante de $AU$ est $\sum_{k=1}^na_{i,k}\times1=\sum_{k=1}^na_{i,k}$, qui vaut $d$ par la question 6.b. Donc $\boxed{AU=dU.}$

**b)** $U\neq0$ et $AU=dU$ : **$d$ est valeur propre de $A$**, et $U$ est un vecteur propre associé.

### Question 11

**a)** $AX=\lambda X$ donne $A^2X=\lambda AX=\lambda^2X$. Par la question 8 :

$$\begin{aligned}
J_nX&=(A^2+A)X-(d-1)X\\
&=\boxed{(\lambda^2+\lambda-d+1)X.}
\end{aligned}$$

**b)** Si $\lambda=d$, alors $\lambda^2+\lambda-d+1=d^2+1=n$, donc $J_nX=nX$. Par la question 1.d, $X\in\mathrm{Vect}(U)$.

Ainsi tout vecteur propre de $A$ associé à $d$ est dans $\mathrm{Vect}(U)$, donc $E_d(A)\subset\mathrm{Vect}(U)$. Inversement $U\in E_d(A)$ (question 10).

Donc $E_d(A)=\mathrm{Vect}(U)$ : **le sous-espace propre associé à $d$ est de dimension 1.**

**c)** Avec $n=d^2+1$ :

$$\begin{aligned}
\lambda^2+\lambda-d+1=n&\iff\lambda^2+\lambda-d-d^2=0\\
&\iff(\lambda-d)(\lambda+d+1)=0.
\end{aligned}$$

Les solutions sont $d$ et $-d-1$.

Supposons que $-d-1$ soit valeur propre de $A$, de vecteur propre $X$. Par a), $J_nX=nX$, donc $X=\alpha U$ par 1.d, et $AX=\alpha dU=dX$.

Alors $(-d-1)X=dX$ avec $X\neq0$, donc $-d-1=d$, ce qui est impossible car $d\ge1$. **Seule la solution $\lambda=d$ est valeur propre de $A$.**

**d)** Soit $\lambda\neq d$ une valeur propre de $A$ et $X$ un vecteur propre associé.

Par a), $X\neq0$ est vecteur propre de $J_n$ pour la valeur propre $\mu=\lambda^2+\lambda-d+1$, donc $\mu\in\{0,n\}$ (question 1.b).

Si $\mu=n$, alors $\lambda\in\{d,-d-1\}$ par c), ce qui est exclu ($\lambda\neq d$, et $-d-1$ n'est pas valeur propre). Donc $\mu=0$ :

$$\boxed{\lambda^2+\lambda-d+1=0.}$$

**e)** Le discriminant de $\lambda^2+\lambda-(d-1)$ vaut $1+4(d-1)=4d-3\ge1>0$. Les racines sont $\frac{-1\pm\sqrt{4d-3}}2$. Les valeurs propres de $A$ autres que $d$ sont donc parmi

$$\begin{aligned}b&=\frac{-1+\sqrt{4d-3}}2,\\c&=\frac{-1-\sqrt{4d-3}}2.\end{aligned}$$

## Problème — Partie 5 : confirmation des valeurs propres de A

### Question 12

**a)** Si $N=P^{-1}MP$ avec $P$ inversible, alors, en appliquant $\mathrm{Tr}(MN)=\mathrm{Tr}(NM)$ aux matrices $P^{-1}$ et $MP$ :

$$\begin{aligned}
\mathrm{Tr}(N)&=\mathrm{Tr}\big(P^{-1}(MP)\big)\\
&=\mathrm{Tr}\big((MP)P^{-1}\big)=\mathrm{Tr}(M).
\end{aligned}$$

**Deux matrices semblables ont la même trace.**

**b)** Supposons que ni $b$ ni $c$ ne soit valeur propre de $A$. Par la question 11, $d$ est alors la seule valeur propre de $A$.

Comme $A$ est diagonalisable (question 9), elle est semblable à $dI_n$, donc égale à $dI_n$. Ses coefficients diagonaux vaudraient $d\ge1$, alors que $a_{i,i}=0$ (question 5.b) : contradiction.

**Au moins un des réels $b$ ou $c$ est valeur propre de $A$.**

### Question 13

Notons $\Delta$ (au lieu de $D$, lettre déjà prise par le diamètre) la matrice diagonale semblable à $A$, et $P$ inversible telle que $\Delta=P^{-1}AP$.

$\Delta$ est diagonale ; ses coefficients diagonaux sont ses valeurs propres, qui sont celles de $A$ (matrices semblables). Ils sont donc égaux à $d$, $b$ ou $c$ (question 11).

L'application $X\mapsto P^{-1}X$ est une bijection linéaire de $E_d(A)$ sur $E_d(\Delta)$, donc $\dim E_d(\Delta)=\dim E_d(A)=1$ (question 11.b). Pour une matrice diagonale, la dimension du sous-espace propre associé à $d$ est le nombre de coefficients diagonaux égaux à $d$.

**$\Delta$ comporte donc un seul coefficient diagonal égal à $d$, les $n-1$ autres étant égaux à $b$ ou à $c$.**

### Question 14

Si $d=1$, alors $n=d^2+1=2$. Le graphe, connexe à deux sommets, est formé d'une arête : la seule paire de sommets distincts est à distance 1, et le diamètre vaut $1\neq2$. **On ne peut donc pas avoir $d=1$** : $d\ge2$.

### Question 15

**a)** Supposons que $b$ soit la seule valeur propre de $A$ autre que $d$.

Par la question 13, la matrice $\Delta$ a un coefficient diagonal égal à $d$, et $n-1$ égaux à $b$.

Par 12.a et 5.b :

$$\begin{aligned}
d+(n-1)b&=\mathrm{Tr}(\Delta)=\mathrm{Tr}(A)\\
&=\sum_{i=1}^na_{i,i}=0.
\end{aligned}$$

**b)** Avec $n-1=d^2$ et la valeur de $b$ : $d+d^2\,\frac{-1+\sqrt{4d-3}}2=0$. On multiplie par $\frac2d$ ($d>0$) :

$$2-d+d\sqrt{4d-3}=0,$$

soit $\boxed{d-2=d\sqrt{4d-3}.}$

**c)** En élevant au carré :

$$\begin{aligned}
(d-2)^2=d^2(4d-3)&\iff d^2-4d+4=4d^3-3d^2\\
&\iff4(d^3-d^2+d-1)=0\\
&\iff(d-1)(d^2+1)=0.
\end{aligned}$$

Comme $d^2+1>0$, on obtient $d=1$, ce qui contredit la question 14. **L'hypothèse de la question 15 est donc fausse.**

### Question 16

Par 12.b, au moins un des réels $b$, $c$ est valeur propre. Par 15, $b$ ne peut pas être la seule valeur propre autre que $d$.

Supposons que $c$ soit la seule valeur propre autre que $d$. Comme en 15.a, $d+(n-1)c=0$, soit $d+d^2c=0$, donc $c=-\frac1d$.

Or $\sqrt{4d-3}\ge1$, donc $c\le-1$, tandis que $-\frac1d\ge-\frac12$ puisque $d\ge2$ : contradiction.

Donc $b$ et $c$ sont tous deux valeurs propres, et il n'y en a pas d'autre que $d$ (question 11). Comme $b<d$ (car $\sqrt{4d-3}<2d+1$) et $c<b$, ce sont trois valeurs distinctes :

$$\boxed{\mathrm{Sp}(A)=\{d,b,c\}.}$$
