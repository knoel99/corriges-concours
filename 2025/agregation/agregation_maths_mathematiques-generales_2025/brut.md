# Agrégation Maths — Mathématiques générales 2025 · Corrigé brut

*Corrigé rédigé par IA, non officiel. Signalez toute erreur.*

Agrégation externe de mathématiques, session 2025 (composition de mathématiques générales, durée 6 heures, calculatrices et documents interdits). Le sujet comporte un exercice (questions 1 à 5) puis un problème en trois parties (questions 1 à 53 du problème) ; toutes les questions sont traitées ci-dessous, dans la numérotation du sujet.

## Exercice

### Question 1

*Voie 1 (critère d'Eisenstein).* Le polynôme $P = X^3 - 2$ est primitif dans $\mathbb{Z}[X]$.
Le nombre premier $2$ divise tous les coefficients non dominants ($-2$, $0$, $0$), ne divise pas le coefficient dominant $1$, et $2^2 = 4$ ne divise pas $-2$.
Par le critère d'Eisenstein, $P$ est irréductible dans $\mathbb{Z}[X]$ ; par le lemme de Gauss, il est irréductible dans $\mathbb{Q}[X]$.

*Voie 2 (degré 3).* Un polynôme de degré $3$ sur un corps est irréductible si et seulement s'il n'admet pas de racine dans ce corps.
Si $a/b \in \mathbb{Q}$, avec $a \in \mathbb{Z}$, $b \in \mathbb{N}^*$ et $\mathrm{pgcd}(a,b) = 1$, était racine de $P$, on aurait $a^3 = 2b^3$, donc $b \mid a^3$, donc $b = 1$ ;
il viendrait $a^3 = 2$, impossible pour $a \in \mathbb{Z}$ (ni $\pm 1$ ni $\pm 2$ ne conviennent).

$$
\boxed{X^3 - 2 \text{ est irréductible sur } \mathbb{Q}.}
$$

### Question 2

Notons $x = \sqrt[3]{2}$. Le polynôme $X^3 - 2$ annule $x$, donc le polynôme minimal $\mu_x$ divise $X^3 - 2$.
Comme $X^3 - 2$ est irréductible (question 1) et unitaire, on a $\mu_x = X^3 - 2$.

*Liberté.* Soit $(a,b,c) \in \mathbb{Q}^3$ tel que $a + b x + c x^2 = 0$. Le polynôme $P = a + bX + cX^2$ annule $x$, donc $\mu_x = X^3 - 2$ divise $P$ ;
comme $\deg P \leq 2 < 3$, on a $P = 0$, c'est-à-dire $a = b = c = 0$.

*Caractère générateur.* Tout élément de $\mathbb{Q}[x]$ s'écrit $P(x)$ avec $P \in \mathbb{Q}[X]$.
La division euclidienne $P = (X^3 - 2) Q + R$, avec $\deg R \leq 2$, donne, en évaluant en $x$, $P(x) = R(x) \in \mathrm{Vect}(1, x, x^2)$.

$$
\boxed{(1,\ \sqrt[3]{2},\ \sqrt[3]{4}) \text{ est une } \mathbb{Q}\text{-base de } \mathbb{Q}[\sqrt[3]{2}].}
$$

### Question 3

Avec $\alpha = 1 + \sqrt[3]{2} + \sqrt[3]{4}$, et en utilisant $\sqrt[3]{8} = 2$ et $\sqrt[3]{16} = 2\sqrt[3]{2}$ :

$$
\begin{aligned}
m_\alpha(1) &= 1 + \sqrt[3]{2} + \sqrt[3]{4},\\
m_\alpha(\sqrt[3]{2}) &= 2 + \sqrt[3]{2} + \sqrt[3]{4},\\
m_\alpha(\sqrt[3]{4}) &= 2 + 2\sqrt[3]{2} + \sqrt[3]{4}.
\end{aligned}
$$

La matrice de $m_\alpha$ dans la base $(1, \sqrt[3]{2}, \sqrt[3]{4})$ (images en colonnes) est donc :

$$
\boxed{M = \begin{pmatrix} 1 & 2 & 2 \\ 1 & 1 & 2 \\ 1 & 1 & 1 \end{pmatrix}.}
$$

### Question 4

On calcule $\chi_{m_\alpha}(X) = \det(X I_3 - M)$. Par l'opération $L_3 \leftarrow L_3 - L_2$, puis en développant selon la première colonne :

$$
\begin{aligned}
\chi_{m_\alpha}(X) &= \begin{vmatrix} X-1 & -2 & -2 \\ -1 & X-1 & -2 \\ 0 & -X & X+1 \end{vmatrix} \\
&= (X-1)\big((X-1)(X+1) - 2X\big) - 2\big((X+1) + X\big) \\
&= (X-1)(X^2 - 2X - 1) - 4X - 2.
\end{aligned}
$$

$$
\boxed{\chi_{m_\alpha}(X) = X^3 - 3X^2 - 3X - 1.}
$$

### Question 5

Par le théorème de Cayley-Hamilton, $\mu_{m_\alpha}$ divise $\chi_{m_\alpha} = X^3 - 3X^2 - 3X - 1$. Montrons que ce dernier est irréductible sur $\mathbb{Q}$ : étant de degré $3$, il suffit qu'il n'ait pas de racine rationnelle.
Si $a/b$ (avec $a, b \in \mathbb{Z}^*$, premiers entre eux) était racine, alors $a \mid b^3$ et $b \mid a^3$, donc $a, b \in \{\pm 1\}$ ;
or $\chi_{m_\alpha}(1) = -6 \neq 0$ et $\chi_{m_\alpha}(-1) = -2 \neq 0$.

Le polynôme minimal $\mu_{m_\alpha}$, diviseur unitaire non constant d'un polynôme irréductible, lui est égal :

$$
\boxed{\mu_{m_\alpha}(X) = X^3 - 3X^2 - 3X - 1.}
$$

## Partie I — Extensions monogènes, trace et norme (questions 1 à 10)

Dans toute la partie, $L/K$ est une extension de corps et $x \in L$.

### Question 1

**(a)** L'application $\Phi : K[X] \to K[x]$, $P \mapsto P(x)$, est un morphisme de $K$-algèbres (morphisme d'évaluation), avec $\Phi(X) = x$ et $\Phi_{|K} = \mathrm{id}_K$. Son noyau est par définition l'idéal annulateur :

$$
\boxed{\ker \Phi = \mathrm{Ann}_{x,K} = \{P \in K[X] \mid P(x) = 0\}.}
$$

**(b)** Si $x$ est transcendant sur $K$, $\ker \Phi = \{0\}$ : $\Phi$ est injectif, et il est surjectif par définition de $K[x]$.
C'est donc un isomorphisme de $K$-algèbres $K[X] \xrightarrow{\sim} K[x]$. Il se prolonge aux corps de fractions : $\widetilde{\Phi} : K(X) \to K(x)$, $P/Q \mapsto P(x)/Q(x)$, est bien définie (si $Q \neq 0$, alors $Q(x) \neq 0$ par transcendance), ne dépend pas du représentant, est un morphisme de corps surjectif ;
comme $K(X)$ est un corps, c'est un isomorphisme $K(X) \xrightarrow{\sim} K(x)$.

La famille $(X^k)_{k \in \mathbb{N}}$ est libre dans $K(X)$ (infinie), donc $(x^k)_{k \in \mathbb{N}}$ est libre dans $K(x)$ : $K(x)$ est de dimension infinie sur $K$.

**(c)** Supposons $x$ algébrique. Par le théorème de factorisation, $\Phi$ induit un isomorphisme de $K$-algèbres $K[X]/(\mu_x) \xrightarrow{\sim} K[x]$.
Comme $\mu_x$ est irréductible, l'idéal $(\mu_x)$ est maximal, donc $K[X]/(\mu_x)$ est un corps : **$K[x]$ est un corps**.

(Autre preuve, par Bézout : si $Q(x) \neq 0$, alors $\mu_x \nmid Q$, et comme $\mu_x$ est irréductible, $\mu_x \wedge Q = 1$ ;
Bézout donne $U Q + V \mu_x = 1$, d'où $U(x) Q(x) = 1$ : l'inverse de $Q(x)$ est $U(x) \in K[x]$.)

$K[x]$ est alors un sous-corps de $L$ contenant $K$ et $x$, donc $K(x) \subseteq K[x]$ ; l'inclusion réciproque est claire, d'où $K(x) = K[x]$.

Dans $K[X]/(\mu_x)$, la famille $(\overline{X^k})_{0 \leq k \leq d-1}$, avec $d = \deg \mu_x$, est une base : elle est génératrice par division euclidienne par $\mu_x$, et libre car une relation $\sum_{k < d} a_k \overline{X^k} = 0$ signifie $\mu_x \mid \sum_{k<d} a_k X^k$, donc ce polynôme est nul.
Par transport, $(1, x, \dots, x^{d-1})$ est une $K$-base de $K(x)$ :

$$
\boxed{K(x) = K[x], \dim_K K(x) = \deg \mu_x, \text{base } (1, x, \dots, x^{d-1}).}
$$

### Question 2

Soit $z$ une racine au moins double de $\mu_x$ dans un surcorps de $L$. On écrit $\mu_x = (X - z)^2 Q$ ; en dérivant et en évaluant en $z$, on obtient $\mu_x'(z) = 0$.
Comme $\mu_x(z) = 0$ et $\mu_x$ est irréductible et unitaire, $\mu_x$ est le polynôme minimal de $z$ sur $K$ : $\mu_z = \mu_x$.
Alors $\mu_z$ divise tout annulateur de $z$, en particulier $\mu_x'$ ; mais $\deg \mu_x' < \deg \mu_x$, donc :

$$
\boxed{\mu_x' = 0.}
$$

### Question 3

Soit $P = \sum_{i=0}^{n} a_i X^i \in K[X]$. On a $P' = \sum_{i=1}^{n} i a_i X^{i-1}$, donc $P' = 0$ si et seulement si $i a_i = 0$ pour tout $i \geq 1$.

- Si $K$ est de caractéristique nulle : $i a_i = 0$ entraîne $a_i = 0$ pour $i \geq 1$, donc $P$ est constant.
- Si $K$ est de caractéristique $p > 0$ : $i a_i = 0$ équivaut à $p \mid i$ ou $a_i = 0$, donc $P' = 0$ si et seulement si $P = Q(X^p)$ avec $Q \in K[X]$.

$$
\boxed{\ker(P \mapsto P') = K \text{ (car. nulle)}, \ker(P \mapsto P') = \{Q(X^p) \mid Q \in K[X]\} \text{ (car. } p > 0).}
$$

En déduisons que si $K$ est de caractéristique nulle ou un corps fini, $\mu_x$ est à racines simples. Raisonnons par l'absurde : si $\mu_x$ n'est pas à racines simples, la question 2 donne $\mu_x' = 0$.

- En caractéristique nulle, $\mu_x$ serait constant, impossible (un polynôme minimal est non constant).
- Si $K$ est fini de cardinal $q = p^k$, on écrirait $\mu_x = Q(X^p) = \sum_i a_i X^{ip}$ avec $Q$ non constant.
L'application de Frobenius $y \mapsto y^p$ est un morphisme de corps, donc injectif, donc surjectif sur le corps fini $K$ : chaque $a_i$ s'écrit $a_i = b_i^p$, d'où

$$
\mu_x = \sum_i b_i^p X^{ip} = \Big(\sum_i b_i X^i\Big)^p,
$$

ce qui contredit l'irréductibilité de $\mu_x$ (puisque $p \geq 2$). Dans tous les cas, contradiction : $\mu_x$ est à racines simples.

### Question 4

Notons $\psi : L \to \mathcal{L}_K(L)$, $x \mapsto m_x$. Vérifions les axiomes d'un morphisme de $K$-algèbres (le produit dans $\mathcal{L}_K(L)$ est la composition) :

$$
\begin{aligned}
\psi(1) &= m_1 = \mathrm{id}_L,\\
\psi(x + x') &= m_{x+x'} = m_x + m_{x'},\\
\psi(xx') &= m_{xx'} = m_x \circ m_{x'} = \psi(x) \circ \psi(x'),\\
\psi(\lambda x) &= \lambda \psi(x) \quad (\lambda \in K).
\end{aligned}
$$

Donc $\psi$ est un morphisme de $K$-algèbres. Il est injectif : si $\psi(x) = 0$, alors $x = m_x(1) = 0$.

Pour $P = \sum_i a_i X^i \in K[X]$ et $x \in L$ :

$$

\begin{aligned}
P(m_x) = \sum_i a_i m_x^i \\
= \sum_i a_i \psi(x)^i \\
= \psi\Big(\sum_i a_i x^i\Big) \\
= m_{P(x)}.
\end{aligned}

$$

Si $x$ est algébrique, $P(m_x) = 0 \iff m_{P(x)} = 0 \iff P(x) = 0$ (injectivité de $\psi$) : $m_x$ et $x$ ont le même idéal annulateur, donc le même polynôme minimal :

$$
\boxed{\forall x \in L,\ \forall P \in K[X],\ m_{P(x)} = P(m_x), \mu_{m_x} = \mu_x \text{ si } x \text{ algébrique}.}
$$

### Question 5

Ici $L = K(x)$ avec $x$ algébrique, $d = \deg \mu_x$ et $\mu_x = X^d + \sum_{i=0}^{d-1} a_i X^i$.
Par la question 1(c), $(1, x, \dots, x^{d-1})$ est une $K$-base de $L$.
On a $m_x(x^k) = x^{k+1}$ pour $0 \leq k \leq d-2$, et $m_x(x^{d-1}) = x^d = -\sum_{i=0}^{d-1} a_i x^i$ puisque $\mu_x(x) = 0$. La matrice de $m_x$ dans cette base est donc la matrice compagnon :

$$
\boxed{C = \begin{pmatrix} 0 & \cdots & 0 & -a_0 \\ 1 & \ddots & & -a_1 \\ \vdots & \ddots & \ddots & \vdots \\ 0 & \cdots & 1 & -a_{d-1} \end{pmatrix}.}
$$

### Question 6

L'endomorphisme $m_x$ est $K$-linéaire ; sa matrice dans une $K$-base de $L$ est à coefficients dans $K$, donc sa trace et son déterminant sont dans $K$ :

$$
\boxed{\mathrm{tr}_{L/K}(x) = \mathrm{tr}(m_x) \in K, \mathrm{N}_{L/K}(x) = \det(m_x) \in K.}
$$

### Question 7

**(a)** $\mathrm{tr}_{L/K} = \mathrm{tr} \circ \psi$ est composée d'applications $K$-linéaires (question 4), donc $K$-linéaire. Pour $(x,y) \in L^2$, $m_{xy} = m_x \circ m_y$, donc

$$

\begin{aligned}
\mathrm{N}_{L/K}(xy) = \det(m_x \circ m_y) \\
= \det(m_x) \det(m_y) \\
= \mathrm{N}_{L/K}(x)\,\mathrm{N}_{L/K}(y).
\end{aligned}

$$

Pour $x \in L^*$, $m_x$ est inversible d'inverse $m_{x^{-1}}$, donc $\det(m_x) \neq 0$.

**(b)** Pour $u \in K$, $m_u = u\,\mathrm{id}_L$. Avec $n = \dim_K L$ :

$$
\boxed{\mathrm{tr}_{L/K}(u) = n u, \mathrm{N}_{L/K}(u) = u^n.}
$$

### Question 8

L'extension $K(x)/K$ est finie (car $K(x) \subseteq L$ et $L/K$ est finie), donc $\dim_K K(x) < \infty$. Par la contraposée de la question 1(b) (un élément transcendant donne une extension de dimension infinie), $x$ est algébrique sur $K$.

$$
\boxed{x \text{ est algébrique sur } K.}
$$

### Question 9

Posons $d = \deg \mu_x$ et $a = \dim_{K(x)} L$, et soit $(\ell_1, \dots, \ell_a)$ une $K(x)$-base de $L$. Par multiplicativité des degrés et la question 1(c) :

$$
\dim_K L = \dim_K K(x) \cdot \dim_{K(x)} L = d \, a.
$$

La famille $(\ell_i x^{j-1})_{1 \leq i \leq a,\ 1 \leq j \leq d}$ a donc $da = \dim_K L$ éléments ; il suffit de montrer qu'elle est $K$-libre.
Soit $(c_{i,j})$ des éléments de $K$ tels que $\sum_{i,j} c_{i,j} \ell_i x^{j-1} = 0$, c'est-à-dire $\sum_{i=1}^{a} \big(\sum_{j=1}^{d} c_{i,j} x^{j-1}\big) \ell_i = 0$. Chaque coefficient $\sum_j c_{i,j} x^{j-1}$ appartient à $K(x)$ ;
la $K(x)$-liberté des $\ell_i$ donne $\sum_j c_{i,j} x^{j-1} = 0$ pour tout $i$, puis la $K$-liberté de $(x^{j-1})_{1 \leq j \leq d}$ (question 1(c)) donne $c_{i,j} = 0$ pour tous $i, j$.

$$
\boxed{(\ell_i x^{j-1})_{1 \leq i \leq a,\ 1 \leq j \leq d} \text{ est une } K\text{-base de } L.}
$$

### Question 10

Ordonnons la base de la question 9 par blocs : $\mathcal{B} = (\ell_1, \ell_1 x, \dots, \ell_1 x^{d-1},\ \ell_2, \dots)$. Pour chaque $i$ et $1 \leq j \leq d-1$, $m_x(\ell_i x^{j-1}) = \ell_i x^j$, et $m_x(\ell_i x^{d-1}) = -\sum_{k=0}^{d-1} a_k \ell_i x^k$ (question 5).
La matrice de $m_x$ dans $\mathcal{B}$ est donc diagonale par blocs, formée de $a = n/d$ blocs égaux à la matrice compagnon $C$ :

$$
\mathrm{Mat}_{\mathcal{B}}(m_x) = \begin{pmatrix} C & & 0 \\ & \ddots & \\ 0 & & C \end{pmatrix}.
$$

On en déduit $\mathrm{tr}_{L/K}(x) = \frac{n}{d} \mathrm{tr}(C)$ et $\mathrm{N}_{L/K}(x) = \det(C)^{n/d}$. Or $\mathrm{tr}(C) = -a_{d-1}$ et $\det(C) = (-1)^d a_0$. Avec les relations coefficients-racines $\sum_i x_i = -a_{d-1}$ et $\prod_i x_i = (-1)^d a_0$ :

$$
\boxed{\mathrm{tr}_{L/K}(x) = \frac{n}{d} \sum_{i=1}^{d} x_i, \mathrm{N}_{L/K}(x) = \Big(\prod_{i=1}^{d} x_i\Big)^{n/d}.}
$$

## Partie II — Dérivations (questions 11 à 28)

Dans toute la partie II, $(K, D)$ est un corps différentiel fixé. On note $K_{\mathrm{cst}} = \{x \in K \mid D(x) = 0\}$.

**II.1 — Formulaire de calcul (questions 11 à 14).**

### Question 11

De la règle de Leibniz appliquée à $1 = 1 \cdot 1$ : $D(1) = D(1) + D(1)$, donc $D(1) = 0$. Pour $x \in K^*$, appliquons Leibniz à $x \cdot x^{-1} = 1$ :

$$
0 = D(1) = D(x)\, x^{-1} + x\, D(x^{-1}),
$$

d'où :

$$
\boxed{D(1) = 0, D\Big(\frac{1}{x}\Big) = -\frac{D(x)}{x^2} \ \ (x \in K^*).}
$$

### Question 12

Soit $P_n$ le prédicat « $D(x^n) = n x^{n-1} D(x)$ », pour $n \in \mathbb{N}^*$.

*Initialisation :* $P_1$ est $D(x) = 1 \cdot x^0 D(x)$, vraie.

*Hérédité :* si $P_n$ est vrai, alors par Leibniz :

$$

\begin{aligned}
D(x^{n+1}) = D(x^n \cdot x) \\
= D(x^n) x + x^n D(x) \\
= n x^{n-1} D(x) \cdot x + x^n D(x) \\
= (n+1) x^n D(x),
\end{aligned}

$$

donc $P_{n+1}$ est vrai.

*Conclusion :* $P_n$ est vrai pour tout $n \geq 1$.
Pour $x \neq 0$, la formule vaut aussi pour $n = 0$ (car $D(1) = 0$) et pour $n < 0$ : avec $m = -n > 0$,

$$

\begin{aligned}
D(x^n) = D\big((x^{-1})^{m}\big) \\
= m (x^{-1})^{m-1} D(x^{-1}) \\
= -n\, x^{n+1} \Big(-\frac{D(x)}{x^2}\Big) \\
= n x^{n-1} D(x).
\end{aligned}

$$

Enfin, pour $(x, y) \in K \times K^*$ :

$$

\begin{aligned}
D\Big(\frac{x}{y}\Big) = D\Big(x \cdot \frac{1}{y}\Big) \\
= D(x) \frac{1}{y} + x D\Big(\frac{1}{y}\Big) \\
= \frac{D(x)}{y} - \frac{x D(y)}{y^2}.
\end{aligned}

$$

$$
\boxed{\forall n \in \mathbb{Z},\ D(x^n) = n x^{n-1} D(x) \ (x \neq 0), D\Big(\frac{x}{y}\Big) = \frac{D(x) y - x D(y)}{y^2}.}
$$

### Question 13

$K_{\mathrm{cst}} = \ker D$ (pour l'addition) est un sous-groupe additif de $K$. Il contient $1$ (question 11). Si $u, v \in K_{\mathrm{cst}}$, alors $D(uv) = D(u) v + u D(v) = 0$ : stabilité par produit.
Si $u \in K_{\mathrm{cst}}^*$, alors $D(u^{-1}) = -D(u)/u^2 = 0$ : stabilité par inverse. Donc $K_{\mathrm{cst}}$ est un sous-corps de $K$.

$D$ est additive ; pour $\lambda \in K_{\mathrm{cst}}$ et $u \in K$, $D(\lambda u) = D(\lambda) u + \lambda D(u) = \lambda D(u)$ : $D$ est $K_{\mathrm{cst}}$-linéaire.

$$
\boxed{K_{\mathrm{cst}} \text{ est un sous-corps de } K \text{ et } D \text{ est } K_{\mathrm{cst}}\text{-linéaire}.}
$$

### Question 14

**(a)** Pour $u, v \in K^*$ :

$$

\begin{aligned}
L_D(uv) = \frac{D(uv)}{uv} \\
= \frac{D(u) v + u D(v)}{uv} \\
= \frac{D(u)}{u} + \frac{D(v)}{v} \\
= L_D(u) + L_D(v),
\end{aligned}

$$

donc $L_D : (K^*, \times) \to (K, +)$ est un morphisme de groupes. Son noyau : $u \in \ker L_D \iff D(u) = 0 \iff u \in K_{\mathrm{cst}}^*$.

**(b)** Soit $R = c \prod_{i=1}^{r} (X - \alpha_i)^{\beta_i}$ avec $c \in k^*$, $\alpha_i \in k$, $\beta_i \in \mathbb{Z}$, dans $K = k(X)$ muni de la dérivation usuelle. En appliquant le morphisme $L_D$ aux deux membres de la factorisation :

$$
\boxed{\frac{D(R)}{R} = \frac{D(c)}{c} + \sum_{i=1}^{r} \beta_i \frac{D(X - \alpha_i)}{X - \alpha_i} = \frac{D(c)}{c} + \sum_{i=1}^{r} \frac{\beta_i}{X - \alpha_i}.}
$$

**II.2 — Construction et extension de dérivations (questions 15 à 28).**

### Question 15

Le polynôme $P = X^2 + X + 1 \in \mathbb{F}_2[X]$ est de degré $2$ sans racine dans $\mathbb{F}_2$ (car $P(0) = P(1) = 1$), donc irréductible ; $\mathbb{F}_2[X]/(P)$ est un corps de cardinal $2^2 = 4$.
Posons $j = \overline{X}$ : on a $j^2 + j + 1 = 0$ et $\mathbb{F}_4 = \mathbb{F}_2(j)$, de base $(1, j)$.

De l'identité remarquable $X^3 - 1 = (X-1)(X^2 + X + 1)$, évaluée en $j$ : $j^3 - 1 = 0$, soit $j^3 = 1$. Alors, par la question 12 :

$$

\begin{aligned}
0 = D(1) \\
= D(j^3) \\
= 3 j^2 D(j) \\
= j^2 D(j) , (\text{car } 3 \\
= 1 \text{ dans } \mathbb{F}_2),
\end{aligned}

$$

donc $D(j) = 0$. On a aussi $D(0) = 0$, $D(1) = 0$ et $D(j+1) = D(j) + D(1) = 0$ : $D$ s'annule sur les quatre éléments de $\mathbb{F}_4 = \mathbb{F}_2(j)$. La dérivation nulle convient, donc :

$$
\boxed{\mathrm{Der}(\mathbb{F}_4) = \{0\}.}
$$

### Question 16

Soit $q = p^k$ et $x \in \mathbb{F}_q$. Le polynôme $X^q - X$ annule tous les éléments de $\mathbb{F}_q$, donc $x^q = x$. Par la question 12 :

$$

\begin{aligned}
D(x) = D(x^q) \\
= q x^{q-1} D(x) \\
= 0 , (\text{car } q \\
= 0 \text{ dans } \mathbb{F}_q).
\end{aligned}

$$

$$
\boxed{\mathrm{Der}(\mathbb{F}_q) = \{0\}.}
$$

### Question 17

Posons $D' = \Phi^{-1} \circ D \circ \Phi$. C'est une composée d'applications additives, donc additive. Pour $u, v \in K'$, en utilisant que $\Phi$ et $\Phi^{-1}$ sont des morphismes de corps :

$$
\begin{aligned}
D'(uv) &= \Phi^{-1}\big(D(\Phi(u) \Phi(v))\big) \\
&= \Phi^{-1}\big(D(\Phi(u)) \Phi(v) + \Phi(u) D(\Phi(v))\big) \\
&= D'(u) v + u D'(v).
\end{aligned}
$$

Donc $D'$ est une dérivation sur $K'$. Enfin $u \in K'_{\mathrm{cst}} \iff D'(u) = 0 \iff D(\Phi(u)) = 0 \iff \Phi(u) \in K_{\mathrm{cst}}$ :

$$
\boxed{D' = \Phi^{-1} \circ D \circ \Phi \text{ est une dérivation sur } K', K'_{\mathrm{cst}} = \Phi^{-1}(K_{\mathrm{cst}}).}
$$

### Question 18

*Unicité.* Si $\widetilde{D}$ est une dérivation sur $B$ prolongeant $D$, la question 12 impose, pour $a, b \in A$, $b \neq 0$ :

$$
\widetilde{D}\Big(\frac{a}{b}\Big) = \frac{D(a) b - a D(b)}{b^2},
$$

la formule est forcée.

*Existence et bonne définition.* Posons $D_B(a/b) = \dfrac{D(a) b - a D(b)}{b^2}$. Cette définition ne dépend pas du représentant : si $a/b = p/q$, alors $a q = b p$, et l'on peut écrire $a/b = (aq)/(bq) = (bp)/(bq) = p/q$ ; il suffit donc de vérifier l'invariance par multiplication des deux termes par un même élément $c \in A \setminus \{0\}$ :

$$
\frac{D(ac)\, bc - ac\, D(bc)}{(bc)^2} = \frac{(D(a) c + a D(c)) b c - a c (D(b) c + b D(c))}{b^2 c^2} = \frac{D(a) b - a D(b)}{b^2}.
$$

*Dérivation.* Pour $u = a/c$ et $v = b/c$ (même dénominateur) :

$$
\begin{aligned}
D_B(u + v) &= \frac{D(a+b) c - (a+b) D(c)}{c^2} = D_B(u) + D_B(v),\\
D_B(uv) &= D_B\Big(\frac{ab}{c^2}\Big) = \frac{D(ab) c^2 - ab D(c^2)}{c^4} = D_B(u) v + u D_B(v).
\end{aligned}
$$

Donc $D_B$ est l'unique dérivation sur $B$ prolongeant $D$.

$$
\boxed{D_B\Big(\frac{a}{b}\Big) = \frac{D(a) b - a D(b)}{b^2} \text{ est l'unique prolongement de } D \text{ à } B.}
$$

### Question 19

L'application $P \mapsto P^D$ (où $P^D = \sum_i D(a_i) X^i$) est une dérivation de $K[X]$ : l'additivité est claire, et pour $P = \sum_j a_j X^j$, $Q = \sum_k b_k X^k$, le coefficient de $X^i$ dans $(PQ)^D$ est $\sum_{j+k=i} D(a_j b_k) = \sum_{j+k=i} (D(a_j) b_k + a_j D(b_k))$, qui est celui de $P^D Q + P Q^D$.

Par la question 18, $P \mapsto P^D$ se prolonge de manière unique en une dérivation $D_1$ de $K(X)$.
Par la question 1(b) ($x$ transcendant), il existe un isomorphisme de $K$-algèbres $\widetilde{\Phi} : K(X) \xrightarrow{\sim} K(x) = L$, avec $\widetilde{\Phi}(X) = x$.
Par la question 17, $\widehat{D} = \widetilde{\Phi} \circ D_1 \circ \widetilde{\Phi}^{-1}$ est une dérivation sur $L$, et pour $P \in K[X]$ :

$$

\begin{aligned}
\widehat{D}(P(x)) = \widetilde{\Phi}(D_1(P)) \\
= \widetilde{\Phi}(P^D) \\
= P^D(x).
\end{aligned}

$$

En particulier, pour $P \in K$ constant, $\widehat{D}(P) = D(P)$ : $\widehat{D}$ prolonge $D$.

### Question 20

Le polynôme minimal $\mu_x$ est séparable, puisque $K$ est de caractéristique nulle. Ainsi $\gcd(\mu_x,\mu_x')=1$. Par Bézout, il existe $A,B\in K[X]$ tels que

$$A\mu_x'+B\mu_x=1.$$

Posons $Q=-A\mu_x^D\in K[X]$, où $\mu_x^D$ s'obtient en appliquant $D$ aux coefficients de $\mu_x$. En évaluant l'identité de Bézout en $x$, on trouve $A(x)\mu_x'(x)=1$, donc

$$Q(x)=-\frac{\mu_x^D(x)}{\mu_x'(x)},\qquad
\boxed{\mu_x^D(x)+Q(x)\mu_x'(x)=0.}$$

On peut remplacer $Q$ par son reste modulo $\mu_x$. Le quotient rationnel $-\mu_x^D/\mu_x'$ n'est en général pas lui-même un polynôme : c'est sa valeur en $x$ que représente $Q(x)$.

### Question 21

Pour $P \in K[X]$, on a $(\mu_x P)^D = \mu_x^D P + \mu_x P^D$ et $(\mu_x P)' = \mu_x' P + \mu_x P'$. En évaluant en $x$ (où $\mu_x(x) = 0$) :

$$

\begin{aligned}
\big((\mu_x P)^D + Q (\mu_x P)'\big)(x) = \mu_x^D(x) P(x) + Q(x) \mu_x'(x) P(x) \\
= \big(\mu_x^D(x) + Q(x) \mu_x'(x)\big) P(x) \\
= 0
\end{aligned}

$$

par la question 20. Donc $(\mu_x P)^D + Q(\mu_x P)' \in \mathrm{Ann}_{x,K} = (\mu_x)$ : l'idéal $\mu_x K[X]$ est stable par l'application $P \mapsto P^D + Q P'$.

Celle-ci induit donc une application sur le quotient $K[X]/(\mu_x)$, qui est une dérivation (combinaison de deux dérivations). Via l'isomorphisme $K[X]/(\mu_x) \xrightarrow{\sim} K[x] = L$ (question 1(c)), on obtient une dérivation $D'$ sur $L$, définie par $D'(P(x)) = P^D(x) + Q(x) P'(x)$.
Pour $u \in K$ (polynôme constant), $D'(u) = u^D = D(u)$ : $D'$ prolonge $D$.

### Question 22

Soient $D_1, D_2$ deux dérivations sur $K(x)$ avec $D_{1|K} = D_{2|K} = D$. Posons $\Delta = D_1 - D_2$ ;
c'est une dérivation (espace vectoriel) nulle sur $K$, donc $K \subseteq K(x)_{\mathrm{cst}}$ et $\Delta$ est $K$-linéaire (question 13).
Par la question 12, pour tout $P \in K[X]$, $\Delta(P(x)) = P'(x) \Delta(x)$ (les deux applications $K$-linéaires $P \mapsto \Delta(P(x))$ et $P \mapsto P'(x)\Delta(x)$ coïncident sur la base $(X^n)_n$).
Avec $P = \mu_x$ : $\Delta(x) \mu_x'(x) = 0$.
En caractéristique nulle, $\mu_x'(x) \neq 0$ (question 3), donc $\Delta(x) = 0$, puis $\Delta(P(x)) = 0$ pour tout $P$, et $\Delta = 0$.

$$
\boxed{D_1 = D_2.}
$$

### Question 23

Montrons par récurrence sur $n = \dim_K L$ qu'une dérivation $D$ sur $K$ admet un unique prolongement à $L$.
Soit $P_n$ : « pour tout sous-corps $K$ de $L$ avec $\dim_K L \leq n$ et toute dérivation $D$ sur $K$, il existe une unique dérivation $\widehat{D}$ sur $L$ prolongeant $D$ ».

*Initialisation :* si $\dim_K L \leq 1$, alors $L = K$ (car $(1)$ engendre $L$), et $P_1$ est trivial.

*Hérédité :* supposons $P_n$, et soit $K$ avec $\dim_K L \leq n+1$. Si $K = L$, c'est fini. Sinon, prenons $x \in L \setminus K$ et posons $K' = K(x)$.
Par les questions 21 et 22 (ou 19 et 22 si $x$ est transcendant), $D$ admet un unique prolongement $D'$ à $K'$. Comme $K \subsetneq K'$, $\dim_K K' \geq 2$, donc par multiplicativité des degrés :

$$

\begin{aligned}
\dim_{K'} L = \frac{\dim_K L}{\dim_K K'} \\
\leq \frac{n+1}{2} \\
\leq n.
\end{aligned}

$$

Par $P_n$, $D'$ admet un unique prolongement $\widehat{D}$ à $L$. *Existence* acquise.
*Unicité* : si $\widetilde{D}$ prolonge $D$ à $L$, sa restriction à $K'$ prolonge $D$, donc vaut $D'$ (question 22), puis $\widetilde{D} = \widehat{D}$ (unicité dans $P_n$).
Donc $P_{n+1}$.

*Conclusion :* par récurrence, le prolongement existe et est unique.

### Question 24

Soit $(a_1, \dots, a_n)$ une $K$-base de $L$.
Chaque $a_i$ est algébrique sur $K$ (question 8, car $K(a_i) \subseteq L$ finie), donc sur $K(X)$. Ainsi $L(X) = K(X)(a_1, \dots, a_n)$ est une extension finie de $K(X)$.
Par la question 23, la dérivation $D$ sur $K(X)$ admet une unique prolongation à $L(X)$.

### Question 25

$K$ est de caractéristique nulle et de dimension finie sur $\mathbb{Q}$, donc $\mathbb{Q} \subseteq K$ et $\dim_{\mathbb{Q}} K < \infty$.
On a $\mathbb{Q} \subseteq K_{\mathrm{cst}}$ (car $D(1) = 0$, puis $D(n) = 0$ et $D(1/n) = 0$ pour $n \in \mathbb{N}^*$), donc $D|_{\mathbb{Q}} = 0$.
La dérivation nulle sur $\mathbb{Q}$ admet deux prolongements à $K$ : $D$ et $0$ ; par l'unicité (question 23), $D = 0$.

$$
\boxed{\mathrm{Der}(K) = \{0\} \text{ si } \dim_{\mathbb{Q}} K < \infty.}
$$

### Question 26

Soit $\sigma \in \mathrm{Aut}_K(L)$. Par la question 17, $\sigma^{-1} \circ D \circ \sigma$ est une dérivation sur $L$.
Sur $K$, $\sigma$ fixe les éléments et $D(K) \subseteq K$ (extension différentielle), donc $\sigma^{-1} \circ D \circ \sigma$ coïncide avec $D$ sur $K$.
Par unicité du prolongement (question 23), $\sigma^{-1} \circ D \circ \sigma = D$, c'est-à-dire :

$$
\boxed{\sigma \circ D = D \circ \sigma.}
$$

### Question 27

Le polynôme $T^q - X^q \in \mathbb{F}_q(X^q)[T]$ annule $X$, donc $X$ est algébrique sur $\mathbb{F}_q(X^q)$ ;
par la question 1(c), $\mathbb{F}_q(X^q)(X) = \mathbb{F}_q(X)$ est de dimension finie sur $\mathbb{F}_q(X^q)$ (de degré $\leq q$).

La dérivation nulle $0_{\mathrm{Der}}$ sur $\mathbb{F}_q(X^q)$ admet deux prolongements distincts à $\mathbb{F}_q(X)$ : l'application nulle, et la dérivation usuelle $\partial$.
En effet, $\partial(X^q) = q X^{q-1} = 0$, donc $\partial$ s'annule sur $\mathbb{F}_q(X^q)$ (et sur $\mathbb{F}_q(X^p) \supseteq \mathbb{F}_q(X^q)$), mais $\partial(X) = 1 \neq 0$. Il n'y a donc pas unicité du prolongement.

$$
\boxed{\mathbb{F}_q(X)/\mathbb{F}_q(X^q) \text{ finie, et le prolongement de } 0_{\mathrm{Der}} \text{ n'est pas unique.}}
$$

### Question 28

L'application $\Psi : \mathrm{Der}(\mathbb{F}_q(X)) \to \mathbb{F}_q(X)$, $D \mapsto D(X)$, est $\mathbb{F}_q(X)$-linéaire (les dérivations forment un espace vectoriel, et $D \mapsto D(X)$ est linéaire).

*Injectivité :* si $D(X) = 0$, alors par la question 12, $D(X^n) = n X^{n-1} D(X) = 0$ pour tout $n \in \mathbb{Z}$, et $D$ est $\mathbb{F}_q$-linéaire (car $\mathbb{F}_q \subseteq \mathbb{F}_q(X)_{\mathrm{cst}}$) : $D$ est nulle sur $\mathbb{F}_q(X)$ (question 18).
Donc $\ker \Psi = \{0\}$.

*Surjectivité :* pour $R \in \mathbb{F}_q(X)$, l'application $D_R$ définie par $D_R(P) = R \cdot P'$ sur $\mathbb{F}_q(X)$ est une dérivation (combinaison de la dérivation usuelle), et $D_R(X) = R$.

Donc $\Psi$ est un isomorphisme d'espaces vectoriels :

$$
\boxed{\dim_{\mathbb{F}_q(X)} \mathrm{Der}(\mathbb{F}_q(X)) = 1, \qquad \text{base } \partial.}
$$

## Partie III — Primitives élémentaires et théorème de Liouville (questions 29 à 53)

Dans toute la partie III, $(K, D)$ est un corps différentiel de caractéristique nulle ; pour toute extension différentielle $L$ de $K$, on note encore $D$ l'unique prolongement.
Une *somme de Liouville* dans $K$ est un élément de la forme $D(g) + \sum_{i \in I} c_i L_D(f_i)$ avec $g \in K$, $c_i \in K_{\mathrm{cst}}$, $f_i \in K^*$.

**III.1 — Transcendance des exponentielles et logarithmes (questions 29 à 31).**

### Question 29

**(a)** Soit $v$ une exponentielle de $u \in K$ (donc $v \neq 0$ et $D(v) = D(u) v$) supposée algébrique sur $K$, de polynôme minimal $\mu_v = X^n + \sum_{i=0}^{n-1} a_i X^i$.
En dérivant $\mu_v(v) = 0$ :

$$

\begin{aligned}
0 = D\Big(\sum_i a_i v^i\Big) \\
= \sum_i D(a_i) v^i + \sum_i a_i i v^{i-1} D(v) \\
= \mu_v^D(v) + D(u) v\, \mu_v'(v).
\end{aligned}

$$

Le polynôme $D(u) X \mu_v' + \mu_v^D \in K[X]$ annule donc $v$, d'où $\mu_v \mid D(u) X \mu_v' + \mu_v^D$. Les deux membres ont degré $\leq n$ et le coefficient de $X^n$ du second est $n D(u)$, donc :

$$
\boxed{n D(u)\, \mu_v = D(u) X \mu_v' + \mu_v^D.}
$$

En comparant les coefficients constants : $n D(u) a_0 = D(a_0)$, soit $L_D(a_0) = n D(u)$. Or $L_D(v^n) = n L_D(v) = n D(u)$ (car $L_D(v) = D(v)/v = D(u)$) ;
comme $\ker L_D = K_{\mathrm{cst}}^*$ (question 14), $v^n / a_0 \in K_{\mathrm{cst}}^*$ (noter $a_0 \neq 0$, sinon $X \mid \mu_v$ irréductible impliquerait $\mu_v = X$, absurde car $v \neq 0$).
Ainsi $v^n \in K$.

**(b)** Réciproquement, si $v^n = a \in K$ pour un entier $n \geq 1$, alors $X^n - a$ annule $v$ : $v$ est algébrique sur $K$.

$$
\boxed{v \text{ transcendant sur } K \iff \forall n \in \mathbb{N}^*,\ v^n \notin K.}
$$

### Question 30

**(a)** Soit $R \in \mathbb{C}(T) \setminus \mathbb{C}$. Raisonnons par l'absurde : supposons qu'il existe $S \in \mathbb{C}(T)$ avec $R'/R = S'$. Comme $R$ n'est pas constante, $R' \neq 0$, donc $S' \neq 0$.
Écrivons la décomposition en éléments simples $S = P + \sum_{i} \sum_{j \geq 1} \frac{s_{i,j}}{(T - a_i)^j}$ : alors

$$
S' = P' - \sum_{i} \sum_{j \geq 1} \frac{j\, s_{i,j}}{(T - a_i)^{j+1}},
$$

dont tous les pôles sont d'ordre $\geq 2$ : **$S'$ n'admet pas de pôle simple**. Or par la question 14(b), $R'/R = \sum_i \frac{\beta_i}{T - \alpha_i}$ n'admet que des pôles simples (et au moins un, car $R'/R \neq 0$). Par unicité de la décomposition en éléments simples, l'égalité $R'/R = S'$ est impossible.

**(b)** Soit $S \in \mathbb{C}(T) \setminus \mathbb{C}$ et supposons $(e^S)^n = R \in \mathbb{C}(T)$ pour un $n \geq 1$.
Alors $R \neq 0$, et $R$ n'est pas constante : sinon $(nS)' = R'/R = 0$, donc $S' = 0$ (caractéristique nulle), donc $S \in \mathbb{C}$, contradiction.
On a $(e^S)' = S' e^S$, donc $L_\partial((e^S)^n) = n S' = R'/R$, c'est-à-dire $(nS)' = R'/R$ avec $R \in \mathbb{C}(T) \setminus \mathbb{C}$ : cela contredit (a). Donc $(e^S)^n \notin \mathbb{C}(T)$ pour tout $n \geq 1$, et par la question 29 :

$$
\boxed{e^S \text{ est transcendant sur } \mathbb{C}(T) \text{ pour tout } S \in \mathbb{C}(T) \setminus \mathbb{C}.}
$$

### Question 31

Soit $v$ un logarithme de $u \in K^*$ ($D(v) = D(u)/u \in K$) supposé algébrique sur $K$, de polynôme minimal $\mu_v = X^n + \sum_{i=0}^{n-1} a_i X^i$.
Comme en question 29(a), le polynôme $D(v) \mu_v' + \mu_v^D \in K[X]$ annule $v$ ; il est de degré $< n$, donc il est nul (car $\mu_v$ le divise) :

$$
D(v) \mu_v' + \mu_v^D = 0.
$$

Le coefficient de $X^{n-1}$ donne $n D(v) + D(a_{n-1}) = 0$, soit $D(n v + a_{n-1}) = 0$ : $n v + a_{n-1} \in L_{\mathrm{cst}} = K_{\mathrm{cst}} \subseteq K$.
Comme $a_{n-1} \in K$ et $n \neq 0$ (caractéristique nulle), on conclut $v \in K$.

$$
\boxed{\text{Si } v \text{ est un logarithme d'un élément de } K^* \text{ et est algébrique sur } K, \text{ alors } v \in K.}
$$

**III.2 — Primitives élémentaires et théorème principal (questions 32 à 33).**

### Question 32

**(a)** On a la décomposition en éléments simples $\dfrac{1}{1+T^2} = \dfrac{1}{2i}\Big(\dfrac{1}{T-i} - \dfrac{1}{T+i}\Big)$. Par le résultat admis, il existe des logarithmes $\ell_1 = \ln(T-i)$ et $\ell_2 = \ln(T+i)$ dans une extension élémentaire de $(\mathbb{C}(T), \partial)$, et $\ell_j' = \frac{1}{T - (\pm i)}$. Alors :

$$
\Big(\frac{1}{2i}(\ell_1 - \ell_2)\Big)' = \frac{1}{2i}\Big(\frac{1}{T-i} - \frac{1}{T+i}\Big) = \frac{1}{1+T^2}.
$$

La tour $\mathbb{C}(T) \subseteq \mathbb{C}(T, \ell_1) \subseteq \mathbb{C}(T, \ell_1, \ell_2)$ est formée d'extensions logarithmiques, donc $\frac{1}{2i}(\ell_1 - \ell_2)$ est une primitive élémentaire de $\frac{1}{1+T^2}$.

Posons $\cos T = \frac{e^{iT} + e^{-iT}}{2}$ et $\sin T = \frac{e^{iT} - e^{-iT}}{2i}$, éléments de $\mathbb{C}(T, e^{iT})$ (car $e^{-iT} = 1/e^{iT}$), extension exponentielle de $\mathbb{C}(T)$.
Soit $\ell_3 = \frac{1}{2i} \ln\Big(\frac{\cos T + i}{\cos T - i}\Big)$ (logarithme dans une extension élémentaire de $\mathbb{C}(T, e^{iT})$). Alors :

$$

\begin{aligned}
\ell_3' = \frac{1}{2i}\Big(\frac{(\cos T)'}{\cos T + i} - \frac{(\cos T)'}{\cos T - i}\Big) \\
= \frac{(\cos T)'}{2i} \cdot \frac{-2i}{1 + (\cos T)^2} \\
= \frac{\sin T}{1 + (\cos T)^2},
\end{aligned}

$$

car $(\cos T)' = -\sin T$. Donc $\frac{\sin T}{1 + (\cos T)^2}$ admet une primitive élémentaire sur $\mathbb{C}(T, e^{iT})$.

**(b)** Notons $F = \mathrm{Arctan}(\cos T)$, élément d'une extension élémentaire tel que $F' = \frac{\sin T}{1 + (\cos T)^2}$. Par (a), $F' $ admet une primitive élémentaire, donc un tel $F$ existe dans une extension élémentaire de $\mathbb{C}(T)$ (à savoir $\mathbb{C}(T, e^{iT}, \ell_3)$).
Soit $M$ le corps de décomposition de $X^2 - F$ sur $\mathbb{C}(T, e^{iT}, \ell_3)$ : $M$ est une extension finie de $\mathbb{C}(T, e^{iT}, \ell_3)$, et $\sqrt{F} \in M$. La tour

$$
\mathbb{C}(T) \subseteq \mathbb{C}(T, e^{iT}) \subseteq \mathbb{C}(T, e^{iT}, \ell_3) \subseteq M
$$

est formée d'extensions exponentielle, logarithmiques puis finie : $\sqrt{\mathrm{Arctan}(\cos T)}$ appartient à une extension élémentaire de $(\mathbb{C}(T), \partial)$.

### Question 33

Soit $f \in K$ admettant une primitive élémentaire : il existe une tour $K = K_0 \subseteq K_1 \subseteq \dots \subseteq K_m = L$, chaque étage $K_{i+1}/K_i$ fini, logarithmique ou exponentiel, et $g \in L$ avec $D(g) = f$.

*Chaque étage est différentiel.* Montrons par récurrence que $D(K_i) \subseteq K_i$. C'est vrai pour $i = 0$. Si $D(K_i) \subseteq K_i$ :

- étage fini : $D|_{K_i}$ admet un unique prolongement à $K_{i+1}$ (question 23) ; la restriction $D|_{K_{i+1}}$ en est un prolongement, donc $D(K_{i+1}) \subseteq K_{i+1}$ ;
- étage logarithmique ou exponentiel : $K_{i+1} = K_i(v)$ avec $D(v) = D(u)/u \in K_i$ (log) ou $D(v) = D(u) v$ (exp), $u \in K_i$. Dans les deux cas $D(v) \in K_{i+1}$, et $D(v^n) = n v^{n-1} D(v) \in K_{i+1}$ (resp.
$= n D(u) v^n \in K_{i+1}$) ; par additivité et Leibniz, $D(K_{i+1}) \subseteq K_{i+1}$.

De plus $K_{\mathrm{cst}} \subseteq K_{i,\mathrm{cst}} \subseteq K_{i+1,\mathrm{cst}} \subseteq L_{\mathrm{cst}} = K_{\mathrm{cst}}$, donc $K_{i,\mathrm{cst}} = K_{\mathrm{cst}}$ pour tout $i$ : chaque étage est une extension différentielle.

*Descente.* Soit $Q_i$ le prédicat « $f$ est une somme de Liouville dans $K_{m-i}$ ». $Q_0$ est vrai car $f = D(g)$ avec $g \in L = K_m$.
Si $Q_i$ est vrai, le lemme principal appliqué à l'extension différentielle $K_{m-i}/K_{m-i-1}$ (finie, logarithmique ou exponentielle) donne $Q_{i+1}$. Par récurrence, $Q_m$ est vrai : $f$ est une somme de Liouville dans $K_0 = K$.

$$
\boxed{\text{Le lemme principal implique le théorème principal.}}
$$

**III.3 — Le lemme principal pour les extensions finies (questions 34 à 39).**

### Question 34

Notons $\alpha_1,\ldots,\alpha_n$ les racines, répétées selon leur multiplicité, du polynôme unitaire $P\in K[X]$ dont $M$ est le corps de décomposition. Puisque les $\alpha_i$ sont algébriques sur $K$, l'algèbre $K[\alpha_1,\ldots,\alpha_n]$ est un corps : à chaque adjonction algébrique, $F[\alpha]=F(\alpha)$. Ainsi, pour $x\in M$, il existe un **polynôme** $Q\in K[X_1,\ldots,X_n]$ tel que $x=Q(\alpha_1,\ldots,\alpha_n)$.

Le polynôme

$$R_{\rm gen}(T,X_1,\ldots,X_n)=\prod_{\sigma\in\mathfrak S_n}
\bigl(T-Q(X_{\sigma(1)},\ldots,X_{\sigma(n)})\bigr)$$

est symétrique en les $X_i$. Chacun de ses coefficients en $T$ est donc un polynôme sur $K$ en les fonctions symétriques élémentaires. Après substitution $X_i=\alpha_i$, ces fonctions sont les coefficients signés de $P$, donc

$$R(T)=\prod_{\sigma\in\mathfrak S_n}
\bigl(T-Q(\alpha_{\sigma(1)},\ldots,\alpha_{\sigma(n)})\bigr)\in K[T].$$

Ce polynôme unitaire est scindé dans $M[T]$ et annule $x$ (facteur associé à l'identité). Le polynôme minimal $\mu_{x,K}$ divise $R$, donc il est lui aussi scindé dans $M[T]$. Toutes ses racines appartiennent à $M$. La représentation polynomiale de $x$ garantit que toutes les substitutions ci-dessus sont définies.

### Question 35

Soit $\sigma : K(x) \to M$ un morphisme de corps. En appliquant $\sigma$ à l'égalité $\mu_{x,K}(x) = \sum_i a_i x^i = 0$ :

$$

\begin{aligned}
\mu_{x,K}^{\sigma}(\sigma(x)) = \sum_i \sigma(a_i) \sigma(x)^i \\
= \sigma\Big(\sum_i a_i x^i\Big) \\
= \sigma(0) \\
= 0,
\end{aligned}

$$

donc $\sigma(x)$ est une racine de $\mu_{x,K}^{\sigma}$.

### Question 36

Soit $\tau : K \to M$ un morphisme de corps, $K^\tau = \tau(K)$, et $y$ une racine de $\mu_{x,K}^{\tau}$ dans le corps de décomposition de ce polynôme sur $K^\tau$.
L'application $\widetilde{\sigma} : K[X] \to K^\tau(y)$, $Q \mapsto Q^\tau(y) = \sum_i \tau(a_i) y^i$ (pour $Q = \sum a_i X^i$), est un morphisme de $K$-algèbres envoyant $X$ sur $y$.
Son noyau est l'idéal $(\mu_{x,K})$ : en effet, $Q^\tau(y) = 0 \iff \mu_{x,K}^{\tau} \mid Q^\tau$ (car $\mu_{x,K}^{\tau}$ est irréductible et annule $y$, c'est le polynôme minimal de $y$ sur $K^\tau$) $\iff \mu_{x,K} \mid Q$.
Donc $\ker \widetilde{\sigma} = (\mu_{x,K})$ ; par factorisation et l'isomorphisme $K[X]/(\mu_{x,K}) \xrightarrow{\sim} K(x)$, on obtient un unique morphisme $\sigma : K(x) \to K^\tau(y)$ tel que $\sigma_{|K} = \tau$ et $\sigma(x) = y$.

### Question 37

Soit $y$ une racine de $\mu_{x,K}$ dans $M$. La question 36 fournit un unique $K$-isomorphisme $\sigma_0:K(x)\to K(y)$ envoyant $x$ sur $y$.

Écrivons $M=K(\alpha_1,\ldots,\alpha_r)$, où les $\alpha_j$ sont les racines d'un polynôme $P\in K[T]$ scindé dans $M$. Posons $F_0=K(x)$ puis $F_j=F_{j-1}(\alpha_j)$, de sorte que $F_r=M$. Soit $\nu_j$ le polynôme minimal de $\alpha_j$ sur $F_{j-1}$, de degré $d_j=[F_j:F_{j-1}]$.

Pour tout $K$-plongement $\tau:F_{j-1}\to M$ prolongeant $\sigma_0$, on a $\nu_j\mid P$ dans $F_{j-1}[T]$. Puisque $\tau$ fixe les coefficients de $P$, on a $\nu_j^\tau\mid P$ dans $M[T]$. Ainsi $\nu_j^\tau$ est scindé dans $M$. Il est irréductible sur $\tau(F_{j-1})$, donc possède exactement $d_j$ racines distinctes (caractéristique nulle). La question 36 associe à chacune un unique prolongement $F_j\to M$ de $\tau$, et tous les prolongements sont obtenus ainsi.

Le nombre de prolongements à $M$ est donc

$$\prod_{j=1}^r d_j=[M:K(x)].$$

Chaque prolongement $M\to M$ est injectif et $K$-linéaire ; la dimension de $M$ sur $K$ étant finie, il est surjectif. Ce sont exactement les automorphismes de $M$ fixant $K$ et envoyant $x$ sur $y$. Donc

$$\boxed{\#\{\sigma\in\operatorname{Aut}_K(M):\sigma(x)=y\}=[M:K(x)].}$$

### Question 38

Soit $d = \deg \mu_{x,K}$ et $x_1, \dots, x_d$ les racines de $\mu_{x,K}$ dans $M$.
Par la question 35, tout $\sigma \in \mathrm{Aut}_K(M)$ envoie $x$ sur l'un des $x_i$ ; par la question 37, chaque $x_i$ est atteint par exactement $\dim_{K(x)} M$ automorphismes. Avec $\dim_{K(x)} M = \frac{\dim_K M}{d}$ (question 1(c)) et la question 10 :

$$
\boxed{\mathrm{tr}_{M/K}(x) = \sum_{\sigma \in \mathrm{Aut}_K(M)} \sigma(x), \mathrm{N}_{M/K}(x) = \prod_{\sigma \in \mathrm{Aut}_K(M)} \sigma(x).}
$$

### Question 39

Soit $M$ le corps de décomposition sur $K$ de $\mu_{g,K} \prod_{i \in I} \mu_{f_i, K}$. Alors $g, f_i \in M$.
Soit $D'$ l'unique prolongement de $D_{|K}$ à $M$ (question 23) ;
comme $D(K) \subseteq K$, on a $D'(f_i) = D(f_i)$ et $\sigma \circ D' = D' \circ \sigma$ pour tout $\sigma \in \mathrm{Aut}_K(M)$ (question 26). Par la question 38 :

$$

\begin{aligned}
\mathrm{tr}_{M/K}(L_D(f_i)) = \sum_{\sigma} \frac{\sigma(D(f_i))}{\sigma(f_i)} \\
= \sum_{\sigma} L_{D'}(\sigma(f_i)) \\
= L_{D'}\Big(\prod_{\sigma} \sigma(f_i)\Big) \\
= L_{D'}(\mathrm{N}_{M/K}(f_i)) \\
= L_D(\mathrm{N}_{M/K}(f_i)),
\end{aligned}

$$

la dernière égalité car $\mathrm{N}_{M/K}(f_i) \in K$. De même, $\mathrm{tr}_{M/K}(D(g)) = \sum_\sigma \sigma(D(g)) = D'(\sum_\sigma \sigma(g)) = D'(\mathrm{tr}_{M/K}(g)) = D(\mathrm{tr}_{M/K}(g))$ (car $\mathrm{tr}_{M/K}(g) \in K$).

Partons de $f = D(g) + \sum_{i \in I} c_i L_D(f_i)$ avec $c_i \in L_{\mathrm{cst}} = K_{\mathrm{cst}} \subseteq K$. Appliquons $\mathrm{tr}_{M/K}$, qui est $K$-linéaire ; comme $f \in K$, $\mathrm{tr}_{M/K}(f) = (\dim_K M) f$ (question 7(b)).
En divisant par $\dim_K M$ (non nul, caractéristique nulle) :

$$
f = D\Big(\frac{\mathrm{tr}_{M/K}(g)}{\dim_K M}\Big) + \sum_{i \in I} \frac{c_i}{\dim_K M}\, L_D(\mathrm{N}_{M/K}(f_i)),
$$

avec $\frac{\mathrm{tr}_{M/K}(g)}{\dim_K M} \in K$, $\frac{c_i}{\dim_K M} \in K_{\mathrm{cst}}$ (car $\mathbb{Q} \subseteq K_{\mathrm{cst}}$) et $\mathrm{N}_{M/K}(f_i) \in K^*$ : $f$ est une somme de Liouville dans $K$.

**III.4 — Le lemme principal pour les extensions logarithmiques ou exponentielles (questions 40 à 49).**

Dans les questions 40 à 49, $L/K$ est logarithmique ou exponentielle : $L = K(v)$ avec $D(v) = D(u)/u$ (log) ou $D(v) = D(u) v$ (exp), $u \in K$.
On suppose $f \in K$ somme de Liouville dans $L$.

### Question 40

Si $v$ est algébrique sur $K$, $L/K$ est finie et la question 39 conclut. On suppose donc $v$ transcendant (sans perte de généralité).
Par la question 1(b), il existe un isomorphisme de $K$-algèbres $\widetilde{\Phi} : K(X) \xrightarrow{\sim} L$ fixant $K$, avec $\widetilde{\Phi}(X) = v$.
Par la question 17, $D_1 = \widetilde{\Phi}^{-1} \circ D \circ \widetilde{\Phi}$ est une dérivation sur $K(X)$, vérifiant $\widetilde{\Phi} \circ D_1 = D \circ \widetilde{\Phi}$, et :

$$
D_1(X) = \widetilde{\Phi}^{-1}(D(v)) = \begin{cases} D(u)/u & \text{(cas logarithmique)},\\ D(u) X & \text{(cas exponentiel)}, \end{cases}
$$

soit, avec $\alpha = D_1(X)$ (log) ou $\alpha = D_1(X)/X = D(u)$ (exp), $\alpha \in K$. De plus $D_1(K) = D(K) \subseteq K$ et $K(X)_{\mathrm{cst}} = \widetilde{\Phi}^{-1}(L_{\mathrm{cst}}) = \widetilde{\Phi}^{-1}(K_{\mathrm{cst}}) = K_{\mathrm{cst}}$ : $(K(X)/K, D_1)$ est une extension différentielle.
On dit que $D_1$ est une *dérivation logarithmique* (resp. *exponentielle*) dans le premier (resp. second) cas.

### Question 41

Écrivons $f = D(g) + \sum_{i \in I} c_i L_D(f_i)$ dans $L$, avec $c_i \in L_{\mathrm{cst}} = K_{\mathrm{cst}}$.
En appliquant $\widetilde{\Phi}^{-1}$ (qui fixe $K$, donc $f$, et vérifie $\widetilde{\Phi}^{-1} \circ D = D_1 \circ \widetilde{\Phi}^{-1}$), avec $g' = \widetilde{\Phi}^{-1}(g)$, $f_i' = \widetilde{\Phi}^{-1}(f_i) \in K(X)^*$ :

$$
\boxed{f = D_1(g') + \sum_{i \in I} c_i L_{D_1}(f_i') \ :\ f \text{ est une somme de Liouville dans } (K(X), D_1).}
$$

### Question 42

Quitte à réduire $I$, on suppose les $c_i$ non nuls. Soit $J \subseteq I$ une sous-famille $\mathbb{Q}$-libre maximale de $(c_i)_{i \in I}$.
Pour $i \in I \setminus J$, écrivons $c_i = \sum_{j \in J} r_{i,j} c_j$ avec $r_{i,j} = n_{i,j}/n \in \mathbb{Q}$ (dénominateur commun $n \in \mathbb{N}^*$). Par morphisme de $L_{D_1}$ (question 14) :

$$
\sum_{i \in I} c_i L_{D_1}(R_i) = \sum_{j \in J} \frac{c_j}{n} L_{D_1}\Big(R_j^{n} \prod_{i \in I \setminus J} R_i^{n_{i,j}}\Big),
$$

d'où, avec $c_j' = c_j/n \in K_{\mathrm{cst}}$ et $R_j' = R_j^n \prod_{i \neq j} R_i^{n_{i,j}} \in K(X)^*$ :

$$
\boxed{f = D_1(R) + \sum_{j \in J} c_j' L_{D_1}(R_j'), \quad (c_j')_{j \in J} \text{ libre sur } \mathbb{Q}.}
$$

### Question 43

Quitte à prendre un dénominateur commun, écrivons $f = D_1(P_0/Q) + \sum_{i} c_i L_{D_1}(P_i/Q)$ avec $P_0, P_i, Q \in K[X]$. La division euclidienne $P_0 = P Q + R$ ($\deg R < \deg Q$) donne $f = D_1(P) + D_1(R/Q) + \sum_i c_i L_{D_1}(P_i/Q)$.
Soit $M$ le corps de décomposition sur $K$ de $Q \prod_i P_i$, de racines $\{\lambda_j\}_{j \in J}$ (distinctes).
Alors $P_i/Q = a_i \prod_j (X - \lambda_j)^{m_{i,j}}$ avec $a_i \in K^*$, $m_{i,j} \in \mathbb{Z}$, et par la question 14(b) appliquée à $D_2$, unique prolongement de $D_1$ à $M(X)$ (question 24) :

$$
\sum_i c_i L_{D_1}(P_i/Q) = \sum_i c_i L_{D_2}(a_i) + \sum_{(i,j)} c_i m_{i,j} \frac{D_2(X) - D_2(\lambda_j)}{X - \lambda_j}.
$$

Enfin, la décomposition en éléments simples de $R/Q$ dans $M(X)$ s'écrit $R/Q = \sum_{(j,s) \in J \times S} \frac{n_{j,s}}{(X - \lambda_j)^s}$. On obtient bien l'écriture annoncée, avec $P \in K[X]$ et $D_2{}_{|K(X)} = D_1$.

### Question 44

Fixons $j \in J$. *Cas logarithmique* ($D_1(X) = \alpha \in K^*$). Si la fraction $\frac{\alpha - D_2(\lambda_j)}{X - \lambda_j}$ était nulle, on aurait $D_2(\lambda_j) = \alpha$. Alors, par la question 26 et la question 38 :

$$
\dim_K M \cdot \alpha = \mathrm{tr}_{M/K}(D_2(\lambda_j)) = D_1\big(\mathrm{tr}_{M/K}(\lambda_j)\big),
$$

donc avec $\beta = \frac{\mathrm{tr}_{M/K}(\lambda_j)}{\dim_K M} \in K$, on a $D_1(X - \beta) = 0$, soit $X - \beta \in K(X)_{\mathrm{cst}} = K_{\mathrm{cst}} \subseteq K$, d'où $X \in K$ : absurde. La fraction est donc non nulle ; son numérateur est constant non nul, donc elle est sous forme irréductible.

*Cas exponentiel* ($D_1(X) = \alpha X$, $\alpha \in K$). Si $\lambda_j = 0$, la fraction vaut $\frac{\alpha X}{X} = \alpha \in K$.
Si $\lambda_j \neq 0$, la fraction $\frac{\alpha X - D_2(\lambda_j)}{X - \lambda_j}$ est réductible si et seulement si $\alpha \lambda_j = D_2(\lambda_j)$, c'est-à-dire $\alpha = L_{D_2}(\lambda_j)$. Si c'était le cas, avec $n = \dim_K M$ et $u = \mathrm{N}_{M/K}(\lambda_j) \in K^*$ :

$$
n \alpha = L_{D_1}(u) = L_{D_1}(X^n),
$$

donc $L_{D_1}(X^n/u)=0$. Ainsi $X^n/u\in K_{\mathrm{cst}}^*$, et $X^n\in K$ : absurde (car $X$ est transcendant). La fraction est donc non nulle et irréductible.

### Question 45

Pour $n_{j,s} \neq 0$ :

$$
D_2\Big(\frac{n_{j,s}}{(X-\lambda_j)^s}\Big) = \frac{D_2(n_{j,s})}{(X-\lambda_j)^s} - s\, n_{j,s} \frac{D_1(X) - D_2(\lambda_j)}{(X-\lambda_j)^{s+1}}.
$$

Hors cas exceptionnel ($D_1$ exponentielle et $\lambda_j = 0$), le numérateur $D_1(X) - D_2(\lambda_j)$ n'est pas divisible par $X - \lambda_j$ (question 44), donc le second terme a un pôle d'ordre $s+1 \geq 2$ en $\lambda_j$, non compensé par le premier (ordre $s$) : le plus grand exposant de $\frac{1}{X-\lambda_j}$ dans la décomposition de $D_2\big(\frac{n_{j,s}}{(X-\lambda_j)^s}\big)$ est $\geq 2$.

*Cas exceptionnel* ($D_1$ exponentielle, $\lambda_j = 0$, $D_1(X) = \alpha X$) :

$$
D_2\Big(\frac{n_{j,s}}{X^s}\Big) = \frac{D_2(n_{j,s}) - s\, n_{j,s} \alpha}{X^s},
$$

et $D_2(n_{j,s}) - s\, n_{j,s} \alpha \neq 0$ (sinon $L_{D_2}(n_{j,s})=s\alpha$. En prenant la norme $u=\mathrm N_{M/K}(n_{j,s})\in K^*$, on obtiendrait $L_{D_1}(u)=[M:K]s\alpha=L_{D_1}(X^{[M:K]s})$, donc $X^{[M:K]s}/u\in K_{\mathrm{cst}}^*$, puis $X^{[M:K]s}\in K$, absurde) : le pôle en $0$ est exactement d'ordre $s$.

### Question 46

Pour $P = \sum_i a_i X^i \in K[X]$, on a $D_1(P) = P^{D_1} + D_1(X) P'$. Que $D_1(X) = \alpha \in K$ (log) ou $\alpha X$ (exp), on obtient $D_1(P) \in K[X]$. Comme $f \in K \subseteq K[X]$, la question 43 donne :

$$
\sum_{(j,s)} D_2\Big(\frac{n_{j,s}}{(X-\lambda_j)^s}\Big) + \sum_{(i,j)} c_i m_{i,j} \frac{D_1(X) - D_2(\lambda_j)}{X-\lambda_j} = f - D_1(P) \in K[X],
$$

qui est sans pôle. Par la question 45, les pôles d'ordre $\geq 2$ (hors cas exceptionnel) ne peuvent venir que de la première somme : $s\, n_{j,s} = 0$, donc $n_{j,s} = 0$ pour tout $(j,s)$ (car $s \neq 0$).
Il reste $\big(\sum_i c_i m_{i,j}\big) \frac{D_1(X)-D_2(\lambda_j)}{X-\lambda_j}$ : par la question 44 (fraction non nulle à pôle simple, hors cas exp et $\lambda_j = 0$), l'absence de pôle impose $\sum_i c_i m_{i,j} = 0$, et la $\mathbb{Q}$-liberté des $c_i$ (question 42) donne $m_{i,j} = 0$, sauf si $D_1$ est exponentielle et $\lambda_j = 0$.

### Question 47

Supposons $D_1$ logarithmique, $D_1(X) = \alpha \in K$. Écrivons $P = \sum_{i=0}^{n} b_i X^i$ ; alors :

$$
D_1(P) = D_1(b_n) X^n + \sum_{i=0}^{n-1} \big(D_1(b_i) + \alpha (i+1) b_{i+1}\big) X^i.
$$

Si $D_1(P) \in K$ (polynôme constant), alors $D_1(b_n) = 0$ et $D_1(b_i) + \alpha(i+1) b_{i+1} = 0$ pour $1 \leq i \leq n-1$. Si $n\ge2$, on a $D_1(b_n)=0$ et $D_1(b_{n-1})+n\alpha b_n=0$. Par conséquent $D_1(b_{n-1}+n b_nX)=0$, donc $b_{n-1}+n b_nX\in K_{\mathrm{cst}}\subseteq K$, ce qui impose $b_n=0$. En répétant cet argument après suppression du terme dominant, on obtient $b_i=0$ pour tout $i\ge2$. Pour le terme de degré $1$, l'égalité $D_1(P)\in K$ impose $D_1(b_1)=0$. Finalement :

$$
\boxed{D_1(P) \in K \implies P = b_0 + b_1 X \text{ avec } b_1 \in K_{\mathrm{cst}}.}
$$

### Question 48

Supposons $D_1$ exponentielle, $D_1(X) = \alpha X$ avec $\alpha \in K$. Alors $D_1(P) = \sum_i \big(D_1(b_i) + \alpha i b_i\big) X^i$.
Si $D_1(P) \in K$, alors pour $i \geq 1$, $D_1(b_i) + \alpha i b_i = 0$, soit $D_1(b_i X^i) = 0$ (après multiplication par $X^i$), donc $b_i X^i \in K_{\mathrm{cst}} \subseteq K$, impossible pour $i \geq 1$ sauf si $b_i = 0$.
Donc $P$ est constant. Si $D_1(P)$ est seulement de degré $\leq 1$, le même calcul donne $b_i = 0$ pour $i \geq 2$.

$$
\boxed{D_1 \text{ exp. : } D_1(P) \in K \implies P \in K, \deg D_1(P) \leq 1 \implies \deg P \leq 1.}
$$

### Question 49

Par la question 46, on a $f = D_1(P) + \sum_i c_i L_{D_1}(a_i)$ (cas log) ou $f = D_1(P) + \sum_i c_i L_{D_1}(a_i) + \sum_i c_i m_{i,j_0} \frac{D_1(X)}{X}$ (cas exp, où $j_0$ est l'éventuel indice tel que $\lambda_{j_0} = 0$) ; dans les deux cas $D_1(P) = f - \sum_i c_i L_{D_1}(a_i) - \dots \in K$.

- *Cas logarithmique* : par la question 47, $P = b + a X$ avec $a \in K_{\mathrm{cst}}$, et $D_1(X) = D(u)/u = L_D(u)$ avec $u \in K^*$. Alors :

$$
f = D(b) + a L_D(u) + \sum_i c_i L_D(a_i),
$$

somme de Liouville dans $K$ (par $K_{\mathrm{cst}}$-linéarité de $D$).

- *Cas exponentiel* : par la question 48, $P \in K$, et $D_1(X)/X = D(u)$ avec $u \in K$. Alors :

$$
f = D\Big(P + \sum_i c_i m_{i,j_0} u\Big) + \sum_i c_i L_D(a_i),
$$

somme de Liouville dans $K$. Le lemme principal est démontré dans tous les cas ; par la question 33, le théorème principal l'est aussi.

**III.5 — Primitives élémentaires de $f e^g$ et de $\frac{\ln T}{T-\lambda}$ (questions 50 à 53).**

### Question 50

Soit $D$ une dérivation exponentielle sur $K(X)$, c'est-à-dire $D(X)/X = \alpha \in K$, et $f \in K$.
Supposons $X f$ somme de Liouville dans $K(X)$ : par les questions 41 à 46 (valides car $X f \in K[X]$), il existe $P \in K[X]$, $a_i, c_i, c \in K$ avec :

$$
X f = D(P) + \sum_i c_i L_D(a_i) + c\, \frac{D(X)}{X}.
$$

Comme $D(X)/X = \alpha \in K$, le membre $D(P) = X f - \sum_i c_i L_D(a_i) - c\alpha$ est un polynôme de degré $\leq 1$. Par la question 48, $\deg P \leq 1$ : écrivons $P = a X + b$, $a, b \in K$.
Avec $d = \sum_i c_i L_D(a_i) \in K$ :

$$
\begin{aligned}
X f &= D(a) X + a D(X) + D(b) + d + c\alpha \\
&= \big(D(a) + a\alpha\big) X + \big(D(b) + d + c\alpha\big).
\end{aligned}
$$

En identifiant le coefficient de $X$ : $f = D(a) + a\alpha = D(a) + a \frac{D(X)}{X}$, soit $X f = D(a) X + a D(X) = D(aX)$. Réciproquement, si $X f = D(aX)$ pour un $a \in K$, c'est bien une somme de Liouville dans $K(X)$.

$$
\boxed{X f \text{ est une somme de Liouville dans } K(X) \iff \exists a \in K,\ X f = D(aX).}
$$

### Question 51

Posons $K = \mathbb{C}(T)$. Supposons $f e^g$ (avec $f, g \in \mathbb{C}(T)$, $g \notin \mathbb{C}$) admet une primitive élémentaire sur $\mathbb{C}(T)(e^g)$.
Par le théorème principal, $f e^g$ est une somme de Liouville dans $\mathbb{C}(T)(e^g)$.
Comme $e^g$ est transcendant sur $\mathbb{C}(T)$ (question 30(b)), les questions 40 et 41 (avec l'isomorphisme $\widetilde{\Phi} : K(X) \xrightarrow{\sim} K(e^g)$ envoyant $X$ sur $e^g$) montrent que $X f$ est une somme de Liouville dans $(K(X), D_1)$, où $D_1$ est la dérivation exponentielle $D_1(X) = g' X$.
Par la question 50, il existe $a \in K$ tel que $X f = D_1(X a)$. Posons $b = \widetilde{\Phi}(a) \in K$ ; alors :

$$

\begin{aligned}
f e^g = \widetilde{\Phi}(X f) \\
= \widetilde{\Phi}(D_1(X a)) \\
= \partial(e^g b) \\
= e^g b' + g' e^g b,
\end{aligned}

$$

d'où, en simplifiant par $e^g \neq 0$, $f = b' + b g'$.
Réciproquement, si $f = b' + b g'$ avec $b \in \mathbb{C}(T)$, alors $f e^g = (b e^g)'$ : $f e^g$ admet la primitive élémentaire $b e^g \in \mathbb{C}(T)(e^g)$.

$$
\boxed{f e^g \text{ admet une primitive élémentaire sur } \mathbb{C}(T)(e^g) \iff \exists b \in \mathbb{C}(T),\ f = b' + b g'.}
$$

### Question 52

Soit $n \geq 2$. Raisonnons par l'absurde : si $e^{T^n}$ admettait une primitive élémentaire, la question 51 (avec $f = 1$, $g = T^n$) donnerait $b \in \mathbb{C}(T)$ avec $1 = b' + n T^{n-1} b$.
On a $b \neq 0$ ; si $b$ n'était pas un polynôme, sa décomposition en éléments simples ferait apparaître dans $b'$ un pôle d'ordre $\geq 2$ (question 30(a)) non compensé par $n T^{n-1} b$ : donc $b \in \mathbb{C}[T]$. Mais alors :

$$
\deg(n T^{n-1} b) = n - 1 + \deg b \geq 1 + \deg b > \deg b',
$$

donc $\deg(b' + n T^{n-1} b) = n - 1 + \deg b \geq 1$, ce qui contredit $b' + n T^{n-1} b = 1$ (constant). Absurde.

Passons à $\frac{e^T}{T}$ : si elle admettait une primitive élémentaire, la question 51 (avec $f = 1/T$, $g = T$) donnerait $b \in \mathbb{C}(T)$ avec $\frac{1}{T} = b' + b$. Si $b$ possède un pôle en $a$ d'ordre $r\ge1$, $b'$ possède en $a$ un pôle d'ordre $r+1$, que $b$ ne peut compenser. Ainsi $b'+b$ possède en $a$ un pôle d'ordre $r+1\ge2$, incompatible avec $1/T$ (sans pôle hors de $0$, et à pôle simple en $0$). Donc $b$ est un polynôme ; alors $b'+b$ aussi et ne peut valoir $1/T$. Contradiction.

$$
\boxed{e^{T^n}\ (n \geq 2) \text{ et } \frac{e^T}{T} \text{ n'admettent pas de primitive élémentaire sur } \mathbb{C}(T)(e^{T^n}) \text{ et } \mathbb{C}(T)(e^T).}
$$

### Question 53

Posons $K = \mathbb{C}(T)$. Le logarithme $\ln T$ est transcendant sur $K$ : sinon, par la question 30(a), il n'existerait pas de $S \in K$ avec $S' = 1/T$, donc $\ln T \notin K$ (question 31).
Supposons $\frac{\ln T}{T - \lambda}$ admet une primitive élémentaire sur $K(\ln T)$.
Par le théorème principal et les questions 40-41 (isomorphisme envoyant $X$ sur $\ln T$), avec $D$ dérivation logarithmique sur $K(X)$ telle que $D(X) = 1/T$, l'élément $\frac{X}{T-\lambda}$ est une somme de Liouville dans $(K(X), D)$.
Par les questions 41 à 46, il existe $P \in K[X]$, $(c_i) \in K_{\mathrm{cst}}^I$, $(a_i) \in (K^*)^I$ tels que :

$$
\frac{X}{T-\lambda} = D(P) + \sum_i c_i L_D(a_i).
$$

Le membre $D(P) = \frac{X}{T-\lambda} - \sum_i c_i L_D(a_i)$ est un polynôme en $X$ de degré $\leq 1$ (les $L_D(a_i)$ sont dans $K$).
En écrivant $P = \sum_i b_i X^i$ et $D(X) = \alpha = 1/T$, le coefficient de $X^i$ dans $D(P)$ est $D(b_i) + \alpha (i+1) b_{i+1}$ ;
la relation $D(b_i) + \alpha(i+1) b_{i+1} = 0$ pour $i \geq 2$ donne, par récurrence descendante comme en question 47, $b_i = 0$ pour $i \geq 3$ et $b_2 \in K_{\mathrm{cst}}$.
Donc $P = a + b X + c X^2$ avec $a, b \in K$, $c \in K_{\mathrm{cst}}$. Alors :

$$
\frac{X}{T-\lambda} = D(a) + D(b) X + b D(X) + 2 c X D(X) + \sum_i c_i L_D(a_i).
$$

En identifiant le coefficient de $X$ (avec $D(X) = 1/T$) :

$$
\frac{1}{T-\lambda} = D(b) + \frac{2c}{T} = b' + \frac{2c}{T}.
$$

Si $\lambda \neq 0$ : par unicité de la décomposition en éléments simples, $c = 0$ (car $b'$ n'admet pas de pôle simple, question 30(a), donc le pôle simple en $\lambda$ de $\frac{1}{T-\lambda}$ ne peut pas venir de $b'$) ;
mais alors $\frac{1}{T-\lambda} = b'$ est impossible pour la même raison. Donc $\lambda = 0$. Réciproquement, si $\lambda = 0$, alors $\big(\frac{1}{2} (\ln T)^2\big)' = \frac{\ln T}{T}$, et $\frac{1}{2}(\ln T)^2$ appartient au même corps différentiel que $\frac{\ln T}{T}$ : primitive élémentaire.

$$
\boxed{\frac{\ln T}{T-\lambda} \text{ admet une primitive élémentaire sur } \mathbb{C}(T)(\ln T) \iff \lambda = 0.}
$$
