# CCINP MP — Maths 2 2024 · Corrigé brut

*Corrigé rédigé par IA, non officiel. Signalez toute erreur.*

## Exercice 1

### Question 1

Posons $p_1=(1,1,0)^{\mathsf T}$, $p_2=(-1,0,1)^{\mathsf T}$ et $p_3=(2,6,1)^{\mathsf T}$.

La multiplication par $A$ donne $Ap_1=-2p_1$, $Ap_2=-2p_2$ et $Ap_3=p_3$. La matrice de colonnes $p_1,p_2,p_3$ a pour déterminant $-3$. Ces trois vecteurs propres forment donc une base.

$$
\boxed{P=\begin{pmatrix}1&-1&2\\1&0&6\\0&1&1\end{pmatrix},\qquad
P^{-1}AP=\operatorname{diag}(-2,-2,1).}
$$

### Question 2

Le système s’écrit $X_{n+1}=AX_n$. Ainsi $Y_{n+1}=\operatorname{diag}(-2,-2,1)Y_n$, d’où

$$
\boxed{Y_n=\begin{pmatrix}(-2)^n\alpha_0\\(-2)^n\beta_0\\\gamma_0\end{pmatrix}.}
$$

Comme $P$ et $P^{-1}$ définissent des applications linéaires continues, $X_n$ converge si et seulement si $Y_n$ converge. La suite $((-2)^n)_{n\ge0}$ est non bornée en valeur absolue.

La convergence équivaut donc à $\alpha_0=\beta_0=0$, c’est-à-dire à $X_0=\gamma_0p_3$. La dernière coordonnée donne $\gamma_0=w_0$.

$$
\boxed{\begin{cases}u_0=2w_0,\\v_0=6w_0.\end{cases}}
$$

Dans ce cas, **les trois suites sont constantes**, avec $u_n=2w_0$, $v_n=6w_0$ et $w_n=w_0$ pour tout $n$.

## Exercice 2

### Question 3

L’instruction qui lit l’image de $1$ est **`s[1]`**. La transposition échange $2$ et $3$ et fixe $0$ et $1$. Sa liste est **`[0, 1, 3, 2]`**.

### Question 4

Pour chaque indice $i$, on applique d’abord la permutation représentée par `s2`, puis celle représentée par `s1`.

```python
def comp(s1, s2):
    resultat = []
    for i in range(0, len(s2)):
        resultat.append(s1[s2[i]])
    return resultat
```

### Question 5

Si `s[i]` est l’image de $i$, alors $i$ est l’image de `s[i]` par la permutation inverse. Chaque indice est rempli une seule fois, puisque `s` représente une bijection.

```python
def inv(s):
    inverse = [0] * len(s)
    for i in range(0, len(s)):
        inverse[s[i]] = i
    return inverse
```

### Question 6

L’entrée représente une partie de $S_n$. On vérifie la présence de l’identité, puis la stabilité par inversion et par composition.

```python
def groupe(G):
    if G == []:
        return False

    identite = [i for i in range(0, len(G[0]))]
    if identite not in G:
        return False

    for s in G:
        if inv(s) not in G:
            return False
        for t in G:
            if comp(s, t) not in G:
                return False
    return True
```

Chaque test porte sur une condition nécessaire. Si tous réussissent, ces conditions caractérisent un sous-groupe de $S_n$. **La fonction renvoie donc la réponse attendue.**

### Question 7

On part de l’identité puis on compose successivement avec la permutation donnée. On s’arrête au premier retour à l’identité.

```python
def cyclique(s):
    identite = [i for i in range(0, len(s))]
    resultat = [identite]
    puissance = comp(s, identite)
    while puissance != identite:
        resultat.append(puissance)
        puissance = comp(s, puissance)
    return resultat
```

Les puissances de la permutation vivent dans le groupe fini $S_n$. Si deux puissances coïncident, en les composant par l’inverse de la puissance d’exposant le plus petit, on trouve une puissance strictement positive égale à l’identité. Le premier exposant positif $d$ pour lequel cela arrive est l’ordre de la permutation. Les puissances d’exposants $0$ à $d-1$ sont distinctes et représentent toutes les puissances entières, en réduisant l’exposant modulo $d$. **La liste renvoyée représente exactement le sous-groupe engendré.**

## Problème

### Question 8

Pour $X=(x,y)^{\mathsf T}$,

$$
X^{\mathsf T}AX=2x^2+2xy+y^2=x^2+(x+y)^2.
$$

Cette somme de carrés ne s’annule que si $x=0$ et $x+y=0$, donc si $X=0$. **$A$ est définie positive.**

## Caractérisation spectrale

### Question 9

**Une matrice symétrique réelle est définie positive si et seulement si toutes ses valeurs propres sont strictement positives.**

Si $M$ est définie positive et $V$ est un vecteur propre non nul associé à $\lambda$, alors

$$
0<V^{\mathsf T}MV=\lambda\|V\|^2.
$$

Ainsi $\lambda>0$. Réciproquement, le théorème spectral donne une matrice orthogonale $O$ telle que $O^{\mathsf T}MO=\operatorname{diag}(\lambda_1,\ldots,\lambda_n)$. Pour $X\ne0$, le vecteur $Y=O^{\mathsf T}X$ est non nul et

$$
X^{\mathsf T}MX=\sum_{i=1}^n\lambda_i y_i^2.
$$

Si chaque $\lambda_i>0$, au moins un terme est strictement positif et tous sont positifs ou nuls. Cela démontre la réciproque.

### Question 10

On a $P(0)=-3$, $P(1)=1$, $P(3)=-3$ et $P(4)=1$.

Le polynôme $P$ est continu. Par le théorème des valeurs intermédiaires, il possède au moins une racine dans chacun des trois intervalles disjoints $]0,1[$, $]1,3[$ et $]3,4[$. Comme son degré est trois, **ces trois racines sont distinctes, simples et strictement positives**.

Le développement du déterminant de $XI_3-B$ donne

$$
\det(XI_3-B)=(X-1)(X-2)(X-3)-(X-1)-(X-2).
$$

Cette expression vaut $P(X)$. La matrice $B$ est symétrique réelle et ses valeurs propres sont les trois racines positives de $P$. **$B$ est définie positive par la question 9.**

## Un critère en dimension 2

### Question 11

Par les questions précédentes et le théorème spectral, une matrice définie positive est semblable à une diagonale de termes $\lambda_1,\ldots,\lambda_n>0$, chacun compté avec sa multiplicité. En utilisant l’invariance de la trace et du déterminant par similitude, on obtient

$$
\boxed{\begin{gathered}
\operatorname{Tr}M=\sum_{i=1}^n\lambda_i>0\\
\det M=\prod_{i=1}^n\lambda_i>0.
\end{gathered}}
$$

### Question 12

Le théorème spectral donne deux valeurs propres réelles $\lambda_1,\lambda_2$, comptées avec multiplicité. Leur produit vaut $\det M>0$, donc elles sont non nulles et de même signe. Leur somme vaut $\operatorname{Tr}M>0$, donc elles sont toutes deux strictement positives. La question 9 donne **$M$ définie positive**.

### Question 13

**Non.** La matrice symétrique $\operatorname{diag}(-1,-1,3)$ a pour trace $1$ et pour déterminant $3$, mais admet $-1$ comme valeur propre. Elle n’est donc pas définie positive.

### Question 14

On applique le critère de la question 12, en dimension deux. La fonction est de classe $\mathcal C^2$ sur l’ouvert $]0,+\infty[^2$. Ses dérivées premières sont

$$
\begin{gathered}
\partial_x f=1-\frac{1}{x^2y}\\
\partial_y f=1-\frac{1}{xy^2}.
\end{gathered}
$$

L’annulation de ces dérivées impose $x^2y=xy^2=1$. Comme $xy>0$, on obtient $x=y$, puis $x=y=1$. La hessienne est

$$
H_f(x,y)=
\begin{pmatrix}
2/(x^3y)&1/(x^2y^2)\\
1/(x^2y^2)&2/(xy^3)
\end{pmatrix}.
$$

En $(1,1)$, elle a pour trace $4$ et pour déterminant $3$, donc elle est définie positive d’après la question 12.

Plus précisément, sa forme quadratique sur $(h,k)$ vaut $2h^2+2hk+2k^2$, qui est au moins $h^2+k^2$ puisque leur différence est $(h+k)^2$. La formule de Taylor-Young à l’ordre deux en ce point critique donne

$$
f(1+h,1+k)-f(1,1)
=\tfrac12(2h^2+2hk+2k^2)+o(h^2+k^2).
$$

Le terme quadratique domine le reste au voisinage de $(0,0)$. **$f$ admet donc un minimum local strict en $(1,1)$, de valeur $3$.**

## Le critère de Sylvester

### Question 15

On complète $X_k$ par des zéros, soit $X=(x_1,\ldots,x_k,0,\ldots,0)^{\mathsf T}$. Alors

$$
\begin{gathered}
X^{\mathsf T}MX=\sum_{1\le i,j\le k} x_i m_{i,j} x_j\\
X_k^{\mathsf T}M_kX_k=\sum_{1\le i,j\le k} x_i m_{i,j} x_j.
\end{gathered}
$$

**Ce choix est non nul dès que $X_k\ne0$.** L’énoncé doit supposer $X_k\ne0$ pour garantir l’existence de $X\ne0$. En effet, si $X_k=0$ et $M=I_n$, l’égalité demandée imposerait $\|X\|^2=0$.

### Question 16

Soit $M$ symétrique réelle définie positive. Pour chaque $k$, le bloc $M_k$ est symétrique réel. Pour tout $X_k\ne0$, le vecteur $X$ de la question 15 est non nul. On a donc $X_k^{\mathsf T}M_kX_k=X^{\mathsf T}MX>0$.

Le bloc $M_k$ est défini positif, et la question 11 donne $\det M_k>0$. **Tous les mineurs principaux demandés sont strictement positifs.**

### Question 17

Notons $H=M_{n-1}$. Elle est définie positive, donc $\det H>0$ par la question 11. Elle est inversible et la seule solution de $HV+U=0$ est $V=-H^{-1}U$.

Par multiplication par blocs et par symétrie de $H$, on obtient

$$
MQ=\begin{pmatrix}H&0\\U^{\mathsf T}&\alpha+U^{\mathsf T}V\end{pmatrix},
\qquad
V^{\mathsf T}H+U^{\mathsf T}=(HV+U)^{\mathsf T}=0.
$$

Il s’ensuit que

$$
\boxed{Q^{\mathsf T}MQ=\begin{pmatrix}H&0\\0&\beta\end{pmatrix},
\qquad\beta=\alpha+U^{\mathsf T}V.}
$$

Comme $Q$ est triangulaire de diagonale unité, $\det Q=1$. Ainsi $\det(Q^{\mathsf T}MQ)=\det M=(\det H)\beta$. Les deux déterminants de $M$ et $H$ étant strictement positifs, **$\beta=\det M/\det H>0$**.

### Question 18

En taille $1$, le critère donne l’unique coefficient strictement positif, ce qui implique la définie-positivité.

Supposons l’implication vraie en taille $n-1$ et soit $M$ symétrique réelle de taille $n$ vérifiant le critère.

Les mineurs principaux du bloc $M_{n-1}$ sont les $n-1$ premiers de $M$, donc $M_{n-1}$ est définie positive par l’hypothèse de récurrence. D’autre part, $\det M>0$.

On peut appliquer la question 17. Pour $Y=(Z,t)^{\mathsf T}\ne0$,

$$
Y^{\mathsf T}(Q^{\mathsf T}MQ)Y
=Z^{\mathsf T}M_{n-1}Z+\beta t^2>0.
$$

En effet, les deux termes sont positifs ou nuls et l’un au moins est strictement positif. Puisque $Q$ est inversible, tout $X\ne0$ s’écrit $X=QY$ avec $Y\ne0$. On a donc $X^{\mathsf T}MX>0$. La récurrence démontre **la réciproque du critère de Sylvester en toute dimension non nulle**.

### Question 19

Les deux premiers mineurs principaux de $C(x)$ valent $2$ et $1$. Par développement suivant la première ligne,

$$
\det C(x)=2(1-x^2)-1=1-2x^2.
$$

La matrice étant symétrique, le critère de Sylvester donne

$$
\boxed{C(x)\text{ est définie positive si et seulement si } |x|<1/\sqrt2.}
$$

### Question 20

Le troisième mineur principal vaut

$$
\begin{vmatrix}2&2&1\\2&3&-1\\1&-1&1\end{vmatrix}
=2(3-1)-2(2+1)+(-2-3)=-7.
$$

Puisqu’un mineur principal est strictement négatif, **la matrice n’est pas définie positive**.

### Question 21

Le membre de gauche est la forme quadratique, au vecteur $(x,y,z)^{\mathsf T}$, de la matrice symétrique

$$
M=\begin{pmatrix}
4&1&-3/2\\
1&1&0\\
-3/2&0&1
\end{pmatrix}.
$$

Ses deux premiers mineurs principaux valent $4$ et $3$. Le troisième vaut $4-1-9/4=3/4$. Ils sont tous strictement positifs, donc $M$ est définie positive par le critère de Sylvester. **L’expression est par conséquent strictement positive pour tout vecteur non nul.**

### Question 22

Notons $D_n=\det S_n$ pour $n\ge1$ et posons $D_0=1$. On a $D_1=3$ et $D_2=8$.

Pour $n\ge3$, le développement par la première ligne donne un terme $3D_{n-1}$ et un terme négatif provenant de la deuxième colonne.

Dans le mineur de ce dernier terme, la première colonne a pour seul coefficient non nul un $1$ en première ligne. Son développement donne $D_{n-2}$. La formule suivante vaut donc aussi dès $n=2$ par le calcul de $D_2$.

$$
D_n=3D_{n-1}-D_{n-2}.
$$

On a $D_1>D_0>0$. Si $D_{n-1}>D_{n-2}>0$, alors

$$
D_n=2D_{n-1}+(D_{n-1}-D_{n-2})>D_{n-1}>0.
$$

Tous les déterminants $D_k$ sont ainsi strictement positifs. Les blocs principaux de $S_n$ sont précisément les $S_k$ pour $1\le k\le n$. Le critère de Sylvester s’applique à cette matrice symétrique. **$S_n$ est définie positive pour tout entier $n\ge1$.**

FIN
