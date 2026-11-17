# ECRICOME ECG — Mathématiques appliquées 2026 · Corrigé guidé

*Corrigé rédigé par IA, non officiel. Signalez toute erreur.*

## Présentation du sujet

**Format.** Épreuve de 4 heures, sans document ni calculatrice. Trois exercices indépendants, 65 questions en comptant les sous-questions. Une annexe de quatre pages rappelle des fonctions Python (`numpy`, `numpy.random`, `numpy.linalg`, `matplotlib.pyplot`, dont `np.cov`) et des commandes SQL (`ORDER BY`, `COUNT()`, `AVG()`, `GROUP BY`, `INNER JOIN`).

**Découpage.**

| Exercice | Thème | Notions du programme ECG appliquées |
|---|---|---|
| 1 | Choix d'une compagnie d'assurances deux années de suite | loi uniforme, loi conjointe, sommes doubles, espérance, covariance, indépendance, simulation, coefficient de corrélation, droite des moindres carrés, équivalents, SQL (agrégation, `GROUP BY`, `ORDER BY`) |
| 2 | $f(x)=\ln\frac1{1-x}$ et la série $\sum\frac{x^k}k$ | domaine, limites, variations, développement limité, séries de Riemann et géométriques, suites adjacentes, intégration par parties, reste intégral, approximation de $\ln2$ |
| 3 | Systèmes différentiels $X'=AX$ avec $A$ non diagonalisable | dérivée nulle sur un intervalle, réduction $2\times2$, changement de variable $Y=P^{-1}X$, matrices nilpotentes, problème de Cauchy, Python |

**Difficulté.** Le sujet est long (65 questions) mais régulier. Les points délicats : 1.3 et 1.5–1.6 (sommes doubles), 1.8.(c), 1.9.(c)–(e), 2.8.(c)–(d), 2.13.(a), 3.10–3.11, et la partie III de l'exercice 3, qui sort du cadre diagonalisable du cours. Le rapport 2026 note que le cours est en général connu, avec « une certaine aisance en Python et en SQL », mais que l'argumentation reste souvent creuse (« par théorème », « d'après le cours »).

**Gestion du temps.** Environ 1 h 30 pour l'exercice 1 (dont 15 minutes de SQL), 1 h 20 pour l'exercice 2 et 1 h 10 pour l'exercice 3. Les parties I et II de l'exercice 3 sont courtes et rapportent : ne pas les sacrifier.

## Exercice 1 — Choix d'une compagnie d'assurances

On étudie le couple $(X,Y)$ : $X$ uniforme sur $[\![1,n]\!]$, puis $Y$ uniforme sur $[\![1,X]\!]$. Les calculs reposent sur des sommes doubles triangulaires, dont on intervertit l'ordre de sommation.

### Question 1

> [!INDICATION]
> Le choix est équiprobable parmi $n$ compagnies numérotées de $1$ à $n$.

#### Solution

$X$ prend ses valeurs dans $[\![1,n]\!]$ avec équiprobabilité : **$X$ suit la loi uniforme sur $[\![1,n]\!]$**, et
$$\begin{aligned}
\mathbb E(X)&=\frac{n+1}2\\
\mathbb V(X)&=\frac{n^2-1}{12}.
\end{aligned}$$

### Question 2

> [!INDICATION]
> Formule des probabilités composées : $\mathbb P([X=j]\cap[Y=k])=\mathbb P(X=j)\,\mathbb P_{[X=j]}(Y=k)$.

> [!INDICATION]
> Sachant $[X=j]$, parmi combien de compagnies le particulier choisit-il ?

#### Solution

Soit $(j,k)\in[\![1,n]\!]^2$. Comme $\mathbb P(X=j)=\frac1n\neq0$, la formule des probabilités composées donne
$$\mathbb P([X=j]\cap[Y=k])=\mathbb P(X=j)\,\mathbb P_{[X=j]}(Y=k).$$
Sachant $[X=j]$, la seconde année le particulier choisit avec équiprobabilité une compagnie parmi les $j$ compagnies $1,\dots,j$ (au moins aussi bien classées que la $j$-ième).

Donc $\mathbb P_{[X=j]}(Y=k)=\frac1j$ si $k\le j$ et $0$ si $k\ge j+1$.

D'où
$$\mathbb P([X=j]\cap[Y=k])=\begin{cases}\dfrac1{nj}&\text{si }k\le j,\\[4pt]0&\text{si }k\ge j+1.\end{cases}$$

> [!JURY]
> Le rapport 2026 : « La formule des probabilités composée est rarement donnée », et la justification de $\mathbb P_{[X=j]}(Y=k)=\frac1j$ est généralement passée sous silence.

### Question 3

> [!INDICATION]
> La somme de toutes les probabilités de la loi conjointe vaut $1$.

#### Solution

Les événements $[X=j]\cap[Y=k]$, $(j,k)\in[\![1,n]\!]^2$, forment un système complet d'événements, donc
$$\begin{aligned}
1&=\sum_{k=1}^n\sum_{j=1}^n\mathbb P([X=j]\cap[Y=k])\\
&=\sum_{k=1}^n\sum_{j=k}^n\frac1{nj}.
\end{aligned}$$
En multipliant par $n$ :
$$\boxed{\sum_{k=1}^n\sum_{j=k}^n\frac1j=n}.$$

### Question 4

> [!INDICATION]
> Loi marginale : formule des probabilités totales avec le système complet $([X=j])_{1\le j\le n}$.

#### Solution

Soit $k\in[\![1,n]\!]$. Par la formule des probabilités totales avec le système complet $([X=j])_{1\le j\le n}$ et la question 2 :
$$\boxed{\mathbb P(Y=k)=\sum_{j=1}^n\mathbb P([X=j]\cap[Y=k])=\sum_{j=k}^n\frac1{nj}}.$$

### Question 5.(a)

> [!INDICATION]
> Intervertissez les deux sommes : le domaine est $\{(j,k)\mid1\le k\le j\le n\}$.

#### Solution

Le domaine de sommation est $\{(j,k)\mid1\le k\le j\le n\}$ ; en sommant d'abord sur $k$ :
$$\begin{aligned}
\sum_{k=1}^n\sum_{j=k}^n\frac kj&=\sum_{j=1}^n\frac1j\sum_{k=1}^jk\\
&=\sum_{j=1}^n\frac1j\cdot\frac{j(j+1)}2\\
&=\frac12\sum_{j=1}^n(j+1).
\end{aligned}$$

### Question 5.(b)

> [!INDICATION]
> $Y$ est une variable finie. Pour le calcul, utilisez 4 puis 5.(a).

#### Solution

$Y$ prend un nombre fini de valeurs ($Y(\Omega)\subset[\![1,n]\!]$) : **$Y$ admet une espérance**. D'après 4 et 5.(a) :
$$\begin{aligned}
\mathbb E(Y)&=\sum_{k=1}^nk\,\mathbb P(Y=k)=\frac1n\sum_{k=1}^n\sum_{j=k}^n\frac kj\\
&=\frac1{2n}\sum_{j=1}^n(j+1)=\frac1{2n}\left(\frac{n(n+1)}2+n\right)\\
&=\frac{n+1}4+\frac12=\boxed{\frac{n+3}4}.
\end{aligned}$$

> [!PIEGE]
> « $Y$ prend des valeurs finies » ne suffit pas (c'est vrai de toute variable réelle) : c'est le **nombre** de valeurs qui est fini.

### Question 6.(a)

> [!INDICATION]
> $XY$ est une variable finie ; pour le calcul, théorème de transfert pour le couple $(X,Y)$.

#### Solution

$XY$ prend un nombre fini de valeurs, donc admet une espérance. Par le théorème de transfert et la question 2 :
$$\begin{aligned}
\mathbb E(XY)&=\sum_{j=1}^n\sum_{k=1}^njk\,\mathbb P([X=j]\cap[Y=k])\\
&=\sum_{j=1}^n\sum_{k=1}^j\frac{jk}{nj}=\frac1n\sum_{j=1}^n\sum_{k=1}^jk\\
&=\frac1{2n}\sum_{j=1}^nj(j+1).
\end{aligned}$$

> [!JURY]
> Le rapport 2026 : « il ne suffit pas que X et Y admettent une espérance pour que XY en admette une! » Ici c'est la finitude de $XY$ qui conclut.

### Question 6.(b)

> [!INDICATION]
> $\sum j(j+1)=\sum j^2+\sum j$ ; factorisez par $n(n+1)$.

#### Solution

$$\begin{aligned}
\sum_{j=1}^nj(j+1)&=\frac{n(n+1)(2n+1)}6+\frac{n(n+1)}2\\
&=\frac{n(n+1)(2n+4)}6=\frac{n(n+1)(n+2)}3.
\end{aligned}$$
Donc
$$\boxed{\mathbb E(XY)=\frac{(n+1)(n+2)}6}.$$

### Question 6.(c)

> [!INDICATION]
> Formule de König-Huygens pour la covariance, puis factorisez par $n+1$.

#### Solution

$$\begin{aligned}
\operatorname{Cov}(X,Y)&=\mathbb E(XY)-\mathbb E(X)\mathbb E(Y)\\
&=\frac{(n+1)(n+2)}6-\frac{(n+1)(n+3)}8\\
&=(n+1)\cdot\frac{4(n+2)-3(n+3)}{24}\\
&=\boxed{\frac{(n+1)(n-1)}{24}}.
\end{aligned}$$

### Question 7

> [!INDICATION]
> Deux variables indépendantes ont une covariance nulle ; ou exhibez un couple $(j,k)$ qui contredit la définition.

#### Solution

Si $X$ et $Y$ étaient indépendantes, leur covariance serait nulle.

Or $n\ge2$, donc $\operatorname{Cov}(X,Y)=\frac{n^2-1}{24}>0$.

**$X$ et $Y$ ne sont pas indépendantes.** (Autre preuve : $\mathbb P([X=1]\cap[Y=2])=0$ alors que $\mathbb P(X=1)\mathbb P(Y=2)>0$.)

> [!PIEGE]
> La covariance nulle n'entraîne pas l'indépendance : on utilise seulement la contraposée de « indépendantes ⇒ covariance nulle ».

### Question 8.(a)

> [!INDICATION]
> `rd.randint(a, b)` simule la loi uniforme sur $[\![a,b-1]\!]$.

#### Solution

```python
import numpy.random as rd

def simulXY(n):
    X = rd.randint(1, n+1)     # uniforme sur [[1, n]]
    Y = rd.randint(1, X+1)     # uniforme sur [[1, X]]
    return X, Y
```

### Question 8.(b)

> [!INDICATION]
> Identifiez chaque coefficient de la matrice renvoyée par `np.cov` (annexe).

#### Solution

`M = np.cov(Tab)` contient $v_x$, $v_y$ et $s_{x,y}$. La fonction renvoie
$$R=\frac{s_{x,y}}{\sqrt{v_x\,v_y}},$$
**le coefficient de corrélation linéaire empirique de la série $(x,y)$** (le facteur de normalisation de `np.cov` se simplifie dans le quotient). Pour $1000$ simulations avec $n=100$, on obtient environ $0{,}64$.

### Question 8.(c)

> [!INDICATION]
> Deux propriétés de la droite des moindres carrés : elle passe par le point moyen, et sa pente est $\frac{s_{x,y}}{v_x}$.

#### Solution

La droite d'ajustement affine de $y$ en $x$ par les moindres carrés a pour équation $y-\bar y=\frac{s_{x,y}}{v_x}(x-\bar x)$ : **elle passe par le point moyen $(\bar x,\bar y)$ et sa pente a le signe de la covariance empirique $s_{x,y}$**, ici positive (la covariance théorique vaut $\frac{n^2-1}{24}>0$ et le nuage est clairement croissant).
- Tracé 1 : ligne brisée, ce n'est pas une droite.
- Tracé 3 : droite passant par l'origine mais pas par la croix rouge (elle passe au-dessus du point moyen).
- Tracé 4 : droite passant par le point moyen mais de pente négative.
- **Tracé 2** : droite de pente positive passant par le point moyen. **C'est la droite des moindres carrés.**

> [!JURY]
> Le rapport 2026 : « Rappelons qu’une droite d’ajustement affine par la méthode des moindres carrés ne passe pas forcément par l’origine! »

### Question 9.(a)

> [!INDICATION]
> C'est un événement, pas une probabilité : décomposez selon la valeur commune de $X$ et $Y$.

#### Solution

$$\begin{aligned}
A_n&=[X=Y]\\
&=\bigcup_{k=1}^n\big([X=k]\cap[Y=k]\big).
\end{aligned}$$

> [!JURY]
> Le rapport 2026 : « Il n’était ici nullement question de probabilité. » L'écriture $A_n=[X=k]\cap[Y=k]$ est fausse : $A_n$ ne dépend pas de $k$.

### Question 9.(b)

> [!INDICATION]
> Additivité sur une union d'événements incompatibles, puis la loi conjointe.

#### Solution

Les événements $[X=k]\cap[Y=k]$ sont deux à deux incompatibles, donc par 9.(a) et la question 2 (cas $k\le j$ avec $j=k$) :
$$\begin{aligned}
\mathbb P(A_n)&=\sum_{k=1}^n\mathbb P([X=k]\cap[Y=k])\\
&=\sum_{k=1}^n\frac1{nk}\\
&=\frac1n\sum_{j=1}^n\frac1j.
\end{aligned}$$

### Question 9.(c)

> [!INDICATION]
> Écrivez $\ln(j+1)-\ln(j)$ comme une intégrale et encadrez l'intégrande.

#### Solution

Soit $j\in\mathbb N^*$. On a $\ln(j+1)-\ln(j)=\int_j^{j+1}\frac{dt}t$. Pour $t\in[j,j+1]$, $\frac1{j+1}\le\frac1t\le\frac1j$. Par croissance de l'intégrale sur $[j,j+1]$ (de longueur $1$) :
$$\frac1{j+1}\le\ln(j+1)-\ln(j)\le\frac1j.$$

> [!JURY]
> Le rapport 2026 : « Rappelons que l’inégalité des accroissements finis est hors programme. » (Le programme officiel d'ECG1 appliquées mentionne pourtant les inégalités des accroissements finis ; l'encadrement par $\int_j^{j+1}\frac{dt}t$ évite toute contestation.)

### Question 9.(d)

> [!INDICATION]
> Sommez l'inégalité de droite pour $j$ de $1$ à $n$ ; celle de gauche pour $j$ de $1$ à $n-1$ (somme télescopique).

#### Solution

*Minoration.* En sommant $\frac1j\ge\ln(j+1)-\ln(j)$ pour $j=1,\dots,n$ (somme télescopique) : $\sum_{j=1}^n\frac1j\ge\ln(n+1)-\ln1=\ln(n+1)$.

*Majoration.* En sommant $\frac1{j+1}\le\ln(j+1)-\ln(j)$ pour $j=1,\dots,n-1$ : $\sum_{j=2}^n\frac1j\le\ln(n)$, donc $\sum_{j=1}^n\frac1j\le1+\ln(n)$ (vrai aussi pour $n=1$).

En divisant par $n$ et avec 9.(b) :
$$\frac{\ln(n+1)}n\le\mathbb P(A_n)\le\frac1n+\frac{\ln(n)}n.$$

### Question 9.(e)

> [!INDICATION]
> Divisez l'encadrement par $\frac{\ln n}n$ (pour $n\ge2$) et montrez que les deux bornes tendent vers $1$.

#### Solution

Pour $n\ge2$, $\ln n>0$ ; en divisant par $\frac{\ln n}n$ :
$$\frac{\ln(n+1)}{\ln n}\le\frac{\mathbb P(A_n)}{\ln(n)/n}\le\frac1{\ln n}+1.$$
À droite, $\frac1{\ln n}\to0$. À gauche, $\frac{\ln(n+1)}{\ln n}=1+\frac{\ln(1+\frac1n)}{\ln n}\to1$. Par encadrement, le quotient tend vers $1$ : $\boxed{\mathbb P(A_n)\underset{n\to+\infty}{\sim}\frac{\ln n}n}$.

> [!JURY]
> Le rapport 2026 : « Rappelons que le théorème d’encadrement concerne les limites, pas les équivalents. » On encadre donc le **quotient**.

### Question 10.(a)

> [!INDICATION]
> Fonction `COUNT(*)` avec une condition `WHERE` comparant deux colonnes.

#### Solution

```sql
SELECT COUNT(*)
FROM adherent
WHERE id_2025 = id_2026;
```

### Question 10.(b)

> [!INDICATION]
> Que relie la condition `ON` ? Quelles colonnes sont affichées ?

#### Solution

La requête réalise la jointure des tables `adherent` et `compagnie` en associant à chaque assuré la compagnie dont l'identifiant est son `id_2026`. **Elle affiche, pour chaque assuré, son numéro et le nom de la compagnie à laquelle il a souscrit en 2026.**

### Question 10.(c)

> [!INDICATION]
> Regroupez les avis par compagnie avec `GROUP BY`, puis appliquez `AVG` dans chaque groupe.

#### Solution

```sql
SELECT compagnie, AVG(note) AS note
FROM avis
GROUP BY compagnie;
```

> [!JURY]
> Le rapport 2026 : « La commande GROUP BY a rarement été comprise par les candidats », et l'oubli de l'attribut `compagnie` dans le `SELECT` est presque systématique.

### Question 10.(d)

> [!INDICATION]
> On interroge la table `moyenne` et on trie par note décroissante.

#### Solution

```sql
SELECT compagnie
FROM moyenne
ORDER BY note DESC;
```
(`SELECT *` convient aussi si l'on veut afficher les notes moyennes.)

> [!JURY]
> Le rapport 2026 : « Les candidats qui comprennent que l’on peut invoquer la table moyenne sont rares », et « DESC est souvent oublié ».

## Exercice 2 — Partie I : étude de f

Étude de $f(x)=\ln\frac1{1-x}=-\ln(1-x)$ : domaine, variations, développement limité en $0$ et position par rapport à la tangente.

### Question 1

> [!INDICATION]
> Il faut $\frac1{1-x}$ défini et strictement positif.

#### Solution

$f(x)$ est défini si et seulement si $1-x\neq0$ et $\frac1{1-x}>0$, c'est-à-dire $1-x>0$. **$I=]-\infty,1[$.**

### Question 2

> [!INDICATION]
> Pour $x\in I$, $f(x)=-\ln(1-x)$ ; étudiez la limite de $1-x$ aux bornes.

#### Solution

Pour $x\in I$, $f(x)=-\ln(1-x)$.
- Quand $x\to-\infty$, $1-x\to+\infty$, donc $\ln(1-x)\to+\infty$ et $\boxed{\lim_{x\to-\infty}f(x)=-\infty}$.
- Quand $x\to1^-$, $1-x\to0^+$, donc $\ln(1-x)\to-\infty$ et $\boxed{\lim_{x\to1^-}f(x)=+\infty}$ (asymptote verticale $x=1$).

### Question 3

> [!INDICATION]
> Dérivée de $x\mapsto\ln(u(x))$ : $\frac{u'}{u}$.

#### Solution

$f$ est dérivable sur $I$ et $f'(x)=-\frac{-1}{1-x}=\frac1{1-x}>0$. $f$ est strictement croissante.

| $x$ | $-\infty$ | | $0$ | | $1$ |
|---|---|---|---|---|---|
| $f'(x)$ | | $+$ | $1$ | $+$ | |
| $f$ | $-\infty$ | $\nearrow$ | $0$ | $\nearrow$ | $+\infty$ |

### Question 4.(a)

> [!INDICATION]
> Développement usuel de $\ln(1+u)$ à l'ordre $2$, avec $u=-x$.

#### Solution

$\ln(1+u)\underset{u\to0}{=}u-\frac{u^2}2+o(u^2)$. Avec $u=-x$ :
$$\boxed{f(x)=-\ln(1-x)\underset{x\to0}{=}x+\frac{x^2}2+o(x^2)}.$$

### Question 4.(b)

> [!INDICATION]
> La partie affine du développement donne la tangente ; le signe du terme suivant donne la position.

#### Solution

D'après 4.(a), la tangente en $0$ a pour équation $\boxed{y=x}$. De plus $f(x)-x=\frac{x^2}2+o(x^2)\underset{x\to0}{\sim}\frac{x^2}2$, qui est positif pour $x\neq0$ voisin de $0$ : **au voisinage de $0$, la courbe est au-dessus de sa tangente.**

### Question 5

> [!INDICATION]
> Asymptote verticale $x=1$, passage par l'origine avec la tangente $y=x$, branche qui descend lentement vers $-\infty$ en $-\infty$.

#### Solution

Éléments du tracé : $f$ croissante, $f(0)=0$, tangente $y=x$ en $0$ avec la courbe au-dessus ($f$ est même convexe, $f''(x)=\frac1{(1-x)^2}>0$), asymptote verticale $x=1$, $f(x)\to-\infty$ lentement en $-\infty$ (comme $-\ln|x|$).

![Figure 1 — Courbe de f(x) = ln(1/(1 − x)) pour x < 1, sa tangente y = x à l'origine et l'asymptote verticale x = 1](figures/ex2-q5-courbe-f-tangente.svg)

## Exercice 2 — Partie II : la série des xᵏ/k

On étudie la convergence de $\sum\frac{x^k}k$ selon $x$ : divergence pour $x=1$ et $x>1$, convergence absolue pour $|x|<1$, convergence de la série alternée pour $x=-1$ par des suites adjacentes, avec une majoration de l'erreur.

### Question 6.(a)

> [!INDICATION]
> Série de Riemann : quel paramètre, et quelle conclusion ?

#### Solution

C'est la série de Riemann $\sum\frac1{k^\alpha}$ avec $\alpha=1\le1$ : **elle diverge.**

### Question 6.(b)

> [!INDICATION]
> Calculez $S_{n+1}(1)-S_n(1)$.

#### Solution

Pour $n\ge1$, $S_{n+1}(1)-S_n(1)=\frac1{n+1}>0$. **La suite $(S_n(1))$ est strictement croissante.**

### Question 6.(c)

> [!INDICATION]
> Une suite croissante converge ou tend vers $+\infty$.

#### Solution

$(S_n(1))$ est croissante. Si elle était majorée, elle convergerait (théorème de la limite monotone), donc la série $\sum\frac1k$ convergerait, ce qui contredit 6.(a). Elle n'est donc pas majorée et, étant croissante, $\boxed{\lim_{n\to+\infty}S_n(1)=+\infty}$.

### Question 7

> [!INDICATION]
> Majorez $\left|\frac{x^k}k\right|$ par le terme général d'une série géométrique.

#### Solution

Soit $x\in]-1,1[$.

Pour $k\ge1$, $0\le\left|\frac{x^k}k\right|\le|x|^k$.

La série géométrique $\sum|x|^k$ converge car $0\le|x|<1$.

Par comparaison de séries à termes positifs, $\sum\left|\frac{x^k}k\right|$ converge : **$\sum\frac{x^k}k$ converge absolument.**

> [!JURY]
> Le rapport 2026 : « Certains candidats pensent encore à tort qu’il suffit que le terme général d’une série tende vers 0 pour conclure à la convergence de la série » ; la question 6.(a) en est un contre-exemple.

### Question 8.(a)

> [!INDICATION]
> Calculez $S_{2n+2}(-1)-S_{2n}(-1)$, $S_{2n+3}(-1)-S_{2n+1}(-1)$ et $S_{2n+1}(-1)-S_{2n}(-1)$.

#### Solution

Notons $u_n=S_{2n}(-1)$ et $w_n=S_{2n+1}(-1)$ pour $n\ge1$. Le terme d'indice $k$ est $\frac{(-1)^k}k$.
$$\begin{aligned}
u_{n+1}-u_n&=-\frac1{2n+1}+\frac1{2n+2}<0,\\
w_{n+1}-w_n&=\frac1{2n+2}-\frac1{2n+3}>0,\\
w_n-u_n&=-\frac1{2n+1}\xrightarrow[n\to+\infty]{}0.
\end{aligned}$$
$(u_n)$ est décroissante, $(w_n)$ croissante, et $w_n-u_n\to0$ : **les deux suites sont adjacentes.**

> [!JURY]
> Le rapport 2026 : « Pour quelques uns l’adjacence se résume à la limite de la différence qui est nulle. » Il faut aussi les deux monotonies.

### Question 8.(b)

> [!INDICATION]
> Deux suites adjacentes convergent vers la même limite ; que dire alors de $(S_n(-1))$ ?

#### Solution

Deux suites adjacentes convergent vers une même limite $\ell$. Ainsi $(S_{2n}(-1))$ et $(S_{2n+1}(-1))$ convergent toutes deux vers $\ell$. Les termes d'indice pair et ceux d'indice impair tendent vers la même limite : **$(S_n(-1))$ converge (vers $\ell$).**

> [!PIEGE]
> $S_n(-1)$ n'est pas égal à $S_{2n}(-1)+S_{2n+1}(-1)$ ; c'est le résultat de cours sur les suites $(u_{2n})$ et $(u_{2n+1})$ qui conclut.

### Question 8.(c)

> [!INDICATION]
> La limite de deux suites adjacentes est comprise entre elles.

#### Solution

$(u_n)$ décroît vers $\ell=-\ln2$ et $(w_n)$ croît vers $\ell$, donc pour tout $n\ge1$, $w_n\le-\ln2\le u_n$.

Ainsi $0\le u_n+\ln2\le u_n-w_n$, c'est-à-dire
$$\big|\ln2+S_{2n}(-1)\big|\le S_{2n}(-1)-S_{2n+1}(-1).$$

### Question 8.(d)

> [!INDICATION]
> Distinguez $n$ pair et $n$ impair ; calculez $S_{2m}(-1)-S_{2m+1}(-1)$.

#### Solution

Notons d'abord $u_m-w_m=\frac1{2m+1}$ et $w_m\le-\ln2\le u_m$ pour $m\ge1$.
- $n=2m$ pair ($m\ge1$) : par 8.(c), $|\ln2+S_n(-1)|\le\frac1{2m+1}\le\frac1{2m}=\frac1n$.
- $n=2m+1$ impair avec $m\ge1$ : $0\le-\ln2-w_m\le u_m-w_m=\frac1{2m+1}=\frac1n$, donc $|\ln2+S_n(-1)|\le\frac1n$.
- $n=1$ : $|\ln2-1|=1-\ln2\le1$.

**Pour tout $n\in\mathbb N^*$, $|\ln2+S_n(-1)|\le\frac1n$.**

> [!JURY]
> Le rapport 2026 : les rares réponses « ne sont restés que sur le cas pair et n’ont pas pensé au cas impair ».

### Question 9.(a)

> [!INDICATION]
> Regardez la limite du terme général.

#### Solution

Soit $x>1$. Par croissances comparées, $\frac{x^k}k\to+\infty$ quand $k\to+\infty$. Le terme général ne tend pas vers $0$ : **la série $\sum\frac{x^k}k$ diverge grossièrement.**

### Question 9.(b)

> [!INDICATION]
> Comparez $S_n(x)$ à $S_n(1)$.

#### Solution

Les termes sont positifs, donc $(S_n(x))$ est croissante ; de plus $S_n(x)\ge S_n(1)$ puisque $\frac{x^k}k\ge\frac1k$. Par 6.(c) et comparaison, $\boxed{\lim_{n\to+\infty}S_n(x)=+\infty}$.

> [!JURY]
> Le rapport 2026 : « La croissance de la suite ou la positivité des termes est souvent oubliée pour justifier la limite. »

## Exercice 2 — Partie III : reste intégral et calcul de S

On établit $f(a)=S_n(a)+R_n(a)$ avec un reste intégral, puis on majore ce reste pour $a\in[0,1[$, ce qui donne $S(a)=f(a)$ et une approximation de $\ln2$.

### Question 10.(a)

> [!INDICATION]
> Primitives : $-\ln(1-t)$ pour $\frac1{1-t}$, et $\frac1{1-t}$ pour $\frac1{(1-t)^2}$.

#### Solution

Pour $a\in]-1,1[$, $1-t>0$ entre $0$ et $a$.
$$\begin{aligned}
\int_0^a\frac{dt}{1-t}&=\big[-\ln(1-t)\big]_0^a\\
&=-\ln(1-a)\\
&=f(a)
\end{aligned}$$
$$\begin{aligned}
\int_0^a\frac{dt}{(1-t)^2}&=\left[\frac1{1-t}\right]_0^a\\
&=\frac1{1-a}-1\\
&=\frac{a}{1-a}.
\end{aligned}$$

### Question 10.(b)

> [!INDICATION]
> Avec l'indication, scindez $R_1(a)$ en deux intégrales calculées en 10.(a).

#### Solution

$$\begin{aligned}
R_1(a)&=\int_0^a\frac{(a-1)+(1-t)}{(1-t)^2}\,dt\\
&=(a-1)\int_0^a\frac{dt}{(1-t)^2}+\int_0^a\frac{dt}{1-t}\\
&=(a-1)\cdot\frac a{1-a}+f(a)\\
&=-a+f(a).
\end{aligned}$$
Donc $\boxed{f(a)=a+R_1(a)}$.

### Question 11

> [!INDICATION]
> Partez de $R_{n+1}(a)$ : dérivez $(a-t)^{n+1}$ et primitivez $(1-t)^{-(n+2)}$.

#### Solution

Soit $n\ge1$.

Posons $u(t)=(a-t)^{n+1}$ et $v(t)=\frac1{(n+1)(1-t)^{n+1}}$, de classe $\mathcal C^1$ entre $0$ et $a$ (car $1-t>0$), avec $u'(t)=-(n+1)(a-t)^n$ et $v'(t)=\frac1{(1-t)^{n+2}}$.

Par intégration par parties :
$$\begin{aligned}
R_{n+1}(a)&=\left[\frac{(a-t)^{n+1}}{(n+1)(1-t)^{n+1}}\right]_0^a+\int_0^a\frac{(a-t)^n}{(1-t)^{n+1}}\,dt\\
&=0-\frac{a^{n+1}}{n+1}+R_n(a).
\end{aligned}$$
Donc $\boxed{R_n(a)=\dfrac{a^{n+1}}{n+1}+R_{n+1}(a)}$.

### Question 12

> [!INDICATION]
> Récurrence : initialisation par 10.(b), hérédité par 11.

#### Solution

Montrons par récurrence $\mathcal P(n)$ : $f(a)=S_n(a)+R_n(a)$.

*Initialisation.* $S_1(a)=a$, et 10.(b) donne $f(a)=a+R_1(a)$.

*Hérédité.* Si $\mathcal P(n)$ est vraie pour un $n\ge1$, alors par 11 :
$$\begin{aligned}
f(a)&=S_n(a)+\frac{a^{n+1}}{n+1}+R_{n+1}(a)\\
&=S_{n+1}(a)+R_{n+1}(a).
\end{aligned}$$
*Conclusion.* Pour tout $n\in\mathbb N^*$, $f(a)=S_n(a)+R_n(a)$.

### Question 13.(a)

> [!INDICATION]
> Traitez séparément les deux inégalités. Pour la seconde, étudiez le signe de $a-\frac{a-t}{1-t}$.

#### Solution

Soit $t\in[0,a]$ (avec $0\le a<1$). Alors $a-t\ge0$ et $1-t\ge1-a>0$, donc $\frac{a-t}{1-t}\ge0$. Ensuite
$$\begin{aligned}
a-\frac{a-t}{1-t}&=\frac{a(1-t)-(a-t)}{1-t}\\
&=\frac{t(1-a)}{1-t}\ge0,
\end{aligned}$$
car $t\ge0$, $1-a>0$ et $1-t>0$. Donc $0\le\frac{a-t}{1-t}\le a$.

> [!JURY]
> Le rapport 2026 : « Beaucoup de candidats semblent ignorer que l’on n’a pas le droit de diviser deux inégalités membre à membre. » L'étude du signe de la différence est la méthode efficace.

### Question 13.(b)

> [!INDICATION]
> Écrivez l'intégrande comme $\left(\frac{a-t}{1-t}\right)^n\cdot\frac1{1-t}$.

#### Solution

Pour $t\in[0,a]$ :
$$\begin{aligned}
0&\le\frac{(a-t)^n}{(1-t)^{n+1}}\\
&=\left(\frac{a-t}{1-t}\right)^n\frac1{1-t}\\
&\le\frac{a^n}{1-a}
\end{aligned}$$
d'après 13.(a) et $\frac1{1-t}\le\frac1{1-a}$. Par croissance de l'intégrale sur $[0,a]$ ($a\ge0$) :
$$\begin{aligned}
0&\le R_n(a)\\
&\le a\cdot\frac{a^n}{1-a}\\
&=\frac{a^{n+1}}{1-a}.
\end{aligned}$$

### Question 13.(c)

> [!INDICATION]
> Faites tendre $n$ vers $+\infty$ dans 12, avec 13.(b).

#### Solution

Comme $0\le a<1$, $a^{n+1}\to0$, donc $R_n(a)\to0$ par encadrement. Par 12, $S_n(a)=f(a)-R_n(a)\to f(a)$, c'est-à-dire $\boxed{S(a)=f(a)}$.

### Question 14.(a)

> [!INDICATION]
> Appliquez 12 et 13.(b) avec $a=\frac12$ ; que vaut $f\left(\frac12\right)$ ?

#### Solution

Avec $a=\frac12\in[0,1[$ : $f\left(\frac12\right)=\ln2$ et $S_n\left(\frac12\right)=\sum_{k=1}^n\frac1{k2^k}$. D'après 12 et 13.(b) :
$$\begin{aligned}
0&\le\ln2-\sum_{k=1}^n\frac1{k2^k}\\
&=R_n\left(\tfrac12\right)\\
&\le\frac{(1/2)^{n+1}}{1/2}\\
&=\frac1{2^n}.
\end{aligned}$$
Donc $\left|\ln2-\sum_{k=1}^n\frac1{k2^k}\right|\le\frac1{2^n}$.

### Question 14.(b)

> [!INDICATION]
> Calculez $S_n\left(\frac12\right)$ en augmentant $n$ jusqu'à ce que la majoration $\frac1{2^n}$ passe sous $\varepsilon$.

#### Solution

```python
def Val(eps):
    n = 1
    S = 1/2                  # S_1(1/2)
    while 1/2**n > eps:
        n = n + 1
        S = S + 1/(n*2**n)
    return S
```
À la sortie, $\frac1{2^n}\le\varepsilon$ et `S` vaut $S_n\left(\frac12\right)$, donc $|\ln2-S|\le\varepsilon$ par 14.(a). Essai : `Val(1e-6)` donne $0{,}69314714$, à $4\times10^{-8}$ de $\ln2$.

### Question 14.(c)

> [!INDICATION]
> Calculez les premiers termes de chaque suite : $S_1\left(\frac12\right)$, $S_2\left(\frac12\right)$, et $-S_1(-1)$, $-S_2(-1)$.

#### Solution

- $-S_n(-1)=\sum_{k=1}^n\frac{(-1)^{k+1}}k$ vaut $1$, $0{,}5$, $0{,}833$, $0{,}583$… : elle **oscille** autour de $\ln2$, en s'en approchant lentement (erreur au plus $\frac1n$, question 8.(d)). Ce sont **les croix bleues**.
- $S_n\left(\frac12\right)$ vaut $0{,}5$, $0{,}625$, $0{,}667$, $0{,}682$… : elle **croît** et se stabilise très vite près de $\ln2\approx0{,}693$ (erreur au plus $\frac1{2^n}$). Ce sont **les points orange**.

> [!JURY]
> Le rapport 2026 relève que certains ont cru voir trois suites (croix du dessus, croix du dessous) : il n'y en a que deux, l'une alternée.

## Exercice 3 — Partie I : un problème de Cauchy

Le système n'est pas diagonalisable ; on le résout ici directement grâce à la somme $s=x+y$.

### Question 1

> [!INDICATION]
> Additionnez les deux équations.

#### Solution

$s'(t)=x'(t)+y'(t)=(x(t)+y(t))+(-x(t)-y(t))=\boxed{0}$.

### Question 2

> [!INDICATION]
> Une fonction de dérivée nulle sur un intervalle y est constante ; utilisez les conditions initiales.

#### Solution

$s'=0$ sur l'intervalle $\mathbb R$, donc $s$ est constante : $s(t)=s(0)=x(0)+y(0)=2$. Pour tout $t$, $\boxed{x(t)+y(t)=2}$.

### Question 3

> [!INDICATION]
> Reportez $x+y=2$ dans la première équation.

#### Solution

D'après 2, $x'(t)=x(t)+y(t)=2$ pour tout $t$, donc $x(t)=2t+x(0)=1+2t$, puis $y(t)=2-x(t)=1-2t$.

Réciproquement, ce couple vérifie $x'=2=x+y$, $y'=-2=-(x+y)$, $x(0)=y(0)=1$.

**L'unique solution est $x(t)=1+2t$, $y(t)=1-2t$.**

> [!JURY]
> Le rapport 2026 : « Que de solutions exponentielles! » La matrice du système n'étant pas diagonalisable (partie II), les solutions sont ici affines.

## Exercice 3 — Partie II : réduction de A et système (S)

$A$ n'est pas diagonalisable, mais elle est semblable à $J=\begin{pmatrix}0&1\\0&0\end{pmatrix}$ ; le système $Y'=JY$ se résout en cascade.

### Question 4

> [!INDICATION]
> Matrice triangulaire : quand est-elle inversible ? Devinez l'inverse et vérifiez.

#### Solution

$P$ est triangulaire inférieure à coefficients diagonaux non nuls ($1$ et $1$), donc inversible. On vérifie que
$$P\begin{pmatrix}1&0\\1&1\end{pmatrix}=\begin{pmatrix}1&0\\-1&1\end{pmatrix}\begin{pmatrix}1&0\\1&1\end{pmatrix}=I_2,$$
donc $\boxed{P^{-1}=\begin{pmatrix}1&0\\1&1\end{pmatrix}}$.

### Question 5

> [!INDICATION]
> Calculez $A^2$ : vous obtenez un polynôme annulateur.

> [!INDICATION]
> Montrez ensuite que $0$ est effectivement valeur propre.

#### Solution

$$A^2=\begin{pmatrix}1&1\\-1&-1\end{pmatrix}^2=\begin{pmatrix}0&0\\0&0\end{pmatrix}.$$
$X^2$ est un polynôme annulateur de $A$, donc $\operatorname{Sp}(A)\subset\{0\}$.

De plus $A\begin{pmatrix}1\\-1\end{pmatrix}=\begin{pmatrix}0\\0\end{pmatrix}$ avec $\begin{pmatrix}1\\-1\end{pmatrix}\neq0$ : $0$ est valeur propre.

**$\operatorname{Sp}(A)=\{0\}$.**

### Question 6

> [!INDICATION]
> Raisonnez par l'absurde : à quoi serait semblable $A$ ?

#### Solution

Si $A$ était diagonalisable, il existerait $Q$ inversible et $\Delta$ diagonale telles que $A=Q\Delta Q^{-1}$, les coefficients diagonaux de $\Delta$ étant les valeurs propres de $A$, donc nuls.

Alors $\Delta=0$ et $A=0$, ce qui est faux.

**$A$ n'est pas diagonalisable.**

> [!JURY]
> Le rapport 2026 : raisonner sur la dimension des sous-espaces propres n'est « pas explicitement au programme » ; le raisonnement par l'absurde ci-dessus suffit.

### Question 7

> [!INDICATION]
> Calculez $AP$, puis $P^{-1}(AP)$.

#### Solution

$$AP=\begin{pmatrix}1&1\\-1&-1\end{pmatrix}\begin{pmatrix}1&0\\-1&1\end{pmatrix}=\begin{pmatrix}0&1\\0&-1\end{pmatrix},$$
$$P^{-1}AP=\begin{pmatrix}1&0\\1&1\end{pmatrix}\begin{pmatrix}0&1\\0&-1\end{pmatrix}=\begin{pmatrix}0&1\\0&0\end{pmatrix}=J.$$

### Question 8

> [!INDICATION]
> Un état d'équilibre est une solution constante : $X'=0$.

#### Solution

Les états d'équilibre sont les solutions constantes, c'est-à-dire les $X$ tels que $AX=0$ : $x+y=0$. **Ce sont les couples $(x,y)=(c,-c)$, $c\in\mathbb R$** (fonctions constantes).

### Question 9

> [!INDICATION]
> $X=PY$ et $P$ est constante, donc $X'=PY'$.

#### Solution

Comme $P$ est constante, $X(t)=PY(t)$ donne $X'(t)=PY'(t)$. Alors
$$\begin{aligned}
(x,y)\text{ solution de }(S)&\iff\forall t,\ X'(t)=AX(t)\\
&\iff\forall t,\ PY'(t)=APY(t)\\
&\iff\forall t,\ Y'(t)=P^{-1}APY(t)=JY(t),
\end{aligned}$$
la dernière équivalence en multipliant à gauche par $P^{-1}$ ou par $P$.

### Question 10

> [!INDICATION]
> Écrivez les deux équations : la seconde donne $v$, puis la première donne $u$.

#### Solution

$Y'=JY$ s'écrit $u'(t)=v(t)$ et $v'(t)=0$.

Donc $v$ est constante, $v(t)=c_2$, puis $u'(t)=c_2$ et $u(t)=c_2t+c_1$.

Réciproquement, ces fonctions conviennent.

**Les solutions sont $Y(t)=\begin{pmatrix}c_1+c_2t\\c_2\end{pmatrix}$, $(c_1,c_2)\in\mathbb R^2$.**

> [!JURY]
> Le rapport 2026 : « majoritairement les candidats s’arrêtent à v(t) = cste et u(t) = cste × t » ; la constante additive de $u$ est oubliée.

### Question 11

> [!INDICATION]
> $X=PY$.

#### Solution

D'après 9, les solutions de $(S)$ sont les $X=PY$ avec $Y$ solution de 10 :
$$\begin{pmatrix}x(t)\\y(t)\end{pmatrix}=\begin{pmatrix}1&0\\-1&1\end{pmatrix}\begin{pmatrix}c_1+c_2t\\c_2\end{pmatrix}=\begin{pmatrix}c_1+c_2t\\c_2-c_1-c_2t\end{pmatrix},\qquad(c_1,c_2)\in\mathbb R^2.$$
(Avec $x(0)=y(0)=1$ : $c_1=1$, $c_2=2$, on retrouve la partie I.)

## Exercice 3 — Partie III : systèmes nilpotents

On généralise : pour $N$ nilpotente, la solution de $X'=NX$ est une somme **finie** $\sum\frac{t^k}{k!}N^kX_0$ (l'exponentielle de matrice n'est pas au programme, mais ici la somme s'arrête).

### Question 12

> [!INDICATION]
> Calculez successivement $M, M^2,\dots,M^n$ ; l'indice $p$ est le premier exposant donnant la matrice nulle, et il vaut au plus $n$.

#### Solution

```python
import numpy as np

def Nil(M):
    n = len(M)
    Z = np.zeros([n, n])
    P = M                       # P contient M**k
    for k in range(1, n+1):
        if (P == Z).all():
            return k
        P = np.dot(P, M)
    return 0
```
Si $M$ est nilpotente d'indice $p$, $M^k\neq0$ pour $k<p$ et $M^p=0$ avec $p\le n$ : la fonction renvoie $p$.

Sinon, aucune puissance $M^k$ avec $k\le n$ n'est nulle (sinon $M$ serait nilpotente) et la fonction renvoie $0$.

Essais : `Nil` vaut $3$ pour $\begin{pmatrix}0&1&2\\0&0&3\\0&0&0\end{pmatrix}$, $2$ pour $J$, $0$ pour $\begin{pmatrix}1&0\\0&0\end{pmatrix}$.

> [!PIEGE]
> `M**p` calcule les puissances coefficient par coefficient, pas la puissance matricielle ; et `M = np.dot(M, M)` élève au carré à chaque tour au lieu de multiplier par $M$.

### Question 13

> [!INDICATION]
> Polynôme annulateur $X^p$ ; puis montrez que $N$ n'est pas inversible.

#### Solution

$N^p=0$, donc $X^p$ est un polynôme annulateur de $N$ et $\operatorname{Sp}(N)\subset\{0\}$.

Si $N$ était inversible, $N^p$ le serait aussi (produit de matrices inversibles), alors que $N^p=0_n$.

Donc $N$ n'est pas inversible, et $0$ est valeur propre.

**$\operatorname{Sp}(N)=\{0\}$.**

> [!JURY]
> Le rapport 2026 : beaucoup prouvent $\operatorname{Sp}(N)\subset\{0\}$ mais rarement l'égalité ; et la nilpotence n'étant pas au programme, rien ne peut en être tiré « du cours ».

### Question 14

> [!INDICATION]
> Même raisonnement qu'à la question 6.

#### Solution

Supposons $N$ diagonalisable : $N=QDQ^{-1}$ avec $D$ diagonale portant les valeurs propres de $N$, toutes nulles (question 13).

Alors $D=0_n$ et $N=0_n$, ce qui contredit l'hypothèse $N\neq0_n$.

**$N$ n'est pas diagonalisable.**

### Question 15

> [!INDICATION]
> Chaque coordonnée de $X(t)$ est un polynôme en $t$ ; dérivez terme à terme, en isolant le terme $k=0$.

#### Solution

$X(t)=\sum_{k=0}^{p-1}\frac{t^k}{k!}N^kX_0$ : chaque coordonnée est une combinaison linéaire (à coefficients constants) des fonctions $t\mapsto\frac{t^k}{k!}$, donc dérivable. Le terme $k=0$ est constant, de dérivée nulle, et pour $k\ge1$, la dérivée de $\frac{t^k}{k!}$ est $\frac{t^{k-1}}{(k-1)!}$. Par linéarité de la dérivation :
$$X'(t)=\sum_{k=1}^{p-1}\frac{t^{k-1}}{(k-1)!}N^kX_0.$$

### Question 16

> [!INDICATION]
> Calculez $NX(t)$, changez d'indice, et utilisez $N^p=0$. Pour l'unicité, citez le théorème de Cauchy pour les systèmes linéaires.

#### Solution

$$\begin{aligned}
NX(t)&=\sum_{k=0}^{p-1}\frac{t^k}{k!}N^{k+1}X_0=\sum_{j=1}^{p}\frac{t^{j-1}}{(j-1)!}N^jX_0\\
&=\sum_{j=1}^{p-1}\frac{t^{j-1}}{(j-1)!}N^jX_0+\frac{t^{p-1}}{(p-1)!}N^pX_0\\
&=X'(t)+0,
\end{aligned}$$
d'après 15 et $N^p=0_n$. De plus $X(0)=B(0)X_0=N^0X_0=X_0$ (seul le terme $k=0$ subsiste). Donc $X$ est solution du problème de Cauchy $X'=NX$, $X(0)=X_0$. Par le théorème d'existence et d'unicité de la solution d'un problème de Cauchy pour un système différentiel linéaire à coefficients constants (admis au programme), **c'est l'unique solution.**

### Question 17

> [!INDICATION]
> $T$ doit valoir $\frac{t^k}{k!}N^k$ après le $k$-ième passage : passez de $k-1$ à $k$ en multipliant par $\frac tk$ et par $N$.

#### Solution

```python
def B(N, t):
    if Nil(N) == 0:
        return("N n'est pas nilpotente")
    else:
        T = np.eye(len(N))
        S = T
        for k in range(1, Nil(N)):
            T = t/k * np.dot(T, N)
            S = S + T
        return S
```
Invariant : après le tour $k$, $T=\frac{t^k}{k!}N^k$ et $S=\sum_{i=0}^{k}\frac{t^i}{i!}N^i$ ; la boucle s'arrête à $k=p-1$, donc `S` vaut $B(t)$. (Comme $T$ est un polynôme en $N$, l'ordre des facteurs dans `np.dot` est indifférent.) Essai : pour la matrice $3\times3$ de la question 12 et $t=0{,}7$, le résultat coïncide avec $e^{0{,}7N}$ calculée par `scipy`.

> [!JURY]
> Le rapport 2026 : beaucoup utilisent une factorielle (`t**k/np.fact(k)`) sans voir l'intérêt de la boucle, et peu complètent le dernier item par `np.dot(T,N)`.

## Bilan

**Méthodes à retenir.**
- Couple défini en deux étapes : loi conjointe par les probabilités composées ; marginales par les probabilités totales ; sommes doubles triangulaires $\sum_{k=1}^n\sum_{j=k}^n=\sum_{j=1}^n\sum_{k=1}^j$.
- Espérance d'une variable finie : existence immédiate, théorème de transfert pour $\mathbb E(XY)$ ; covariance non nulle ⇒ non-indépendance.
- Droite des moindres carrés : passe par le point moyen, pente $\frac{s_{x,y}}{v_x}$, du signe de la covariance.
- Encadrer $\ln(j+1)-\ln j$ par une intégrale ; sommes télescopiques ; équivalent par encadrement du quotient.
- SQL : `COUNT(*)`, `AVG(...) … GROUP BY`, `ORDER BY … DESC`, `INNER JOIN … ON`.
- Séries : Riemann, comparaison à une série géométrique, divergence grossière ; suites adjacentes pour une série alternée et majoration de l'erreur.
- Reste intégral par intégration par parties répétée ; majoration du reste pour obtenir la somme d'une série.
- Systèmes $X'=AX$ : solutions constantes, changement de variable $Y=P^{-1}X$, résolution en cascade quand la matrice réduite est triangulaire ; matrices nilpotentes (spectre $\{0\}$, non diagonalisables si non nulles).

**À revoir si besoin.** Suites adjacentes et suites des termes pairs et impairs ; théorème d'existence et d'unicité de Cauchy ; puissances matricielles en Python (`np.dot`, `al.matrix_power`).

**Questions transposables.** Lois « en cascade » (uniforme puis uniforme sur un sous-ensemble) ; série harmonique et $\ln n$ ; développement de $-\ln(1-x)$ en série ; systèmes différentiels non diagonalisables.
