# Mines-Ponts MPI — Mathématiques 2 2024 · Corrigé brut

*Corrigé rédigé par IA, non officiel. Signalez toute erreur.*

## Partie I — Quelques propriétés algébriques des matrices d’adjacence

### Question 1

Soit $u$ l'endomorphisme de matrice $M$ dans la base canonique $(e_1,\ldots,e_n)$.

La famille $(e_{\rho(1)},\ldots,e_{\rho(n)})$ est une base.

Pour chaque $j$, le coefficient de $e_{\rho(i)}$ dans $u(e_{\rho(j)})$ vaut $m_{\rho(i),\rho(j)}$.

La matrice dans cette autre base est donc $(m_{\rho(i),\rho(j)})_{i,j}$, **semblable à $M$** puisque les deux représentent $u$.

Pour les indexations du graphe, posons $\rho=\sigma^{-1}\circ\sigma'$. Alors $\sigma'(i)=\sigma(\rho(i))$. La définition de l'adjacence donne $(M_{G,\sigma'})_{i,j}=(M_{G,\sigma})_{\rho(i),\rho(j)}$. **Les deux matrices d'adjacence sont donc semblables.**

### Question 2

La matrice d'adjacence est réelle symétrique, car une arête est une paire non ordonnée. **Le théorème spectral donne sa diagonalisation dans une base orthonormée.**

### Question 3

En l'absence d'arête, la matrice est nulle et de rang zéro. Si une arête relie les sommets d'indices $i$ et $j$, la sous-matrice sur ces deux lignes et ces deux colonnes est

$$
\begin{pmatrix}0&1\\1&0\end{pmatrix}.
$$

Elle est inversible, donc les colonnes $i,j$ sont indépendantes. **Le rang est alors au moins deux et ne vaut jamais un.**

### Question 4

En plaçant le centre en premier, la colonne du centre vaut $v$, somme des vecteurs canoniques des feuilles. Toutes les colonnes des feuilles valent le vecteur du centre $e$, et les colonnes des sommets isolés sont nulles. Les vecteurs $e,v$ sont non nuls et à supports disjoints. **Le rang est deux.**

Considérons maintenant le cycle $1-2-3-4-1$.

![Figure 1 — Cycle à quatre sommets. Chaque sommet a exactement deux voisins.](figures/q4-cycle-quatre-sommets.svg)

Ses colonnes $1$ et $3$ valent $e_2+e_4$, tandis que ses colonnes $2$ et $4$ valent $e_1+e_3$. Ces deux vecteurs sont indépendants, donc le rang est encore deux. Tous les sommets ont degré deux, tandis qu'une étoile à quatre sommets présente trois feuilles de degré un. **Ce cycle fournit l'exemple demandé.**

### Question 5

Si $G$ est vide, sa copie est vide et les deux polynômes valent $1$. Sinon, transportons une indexation de $G$ vers $G'$ par la bijection qui préserve les arêtes. Les matrices obtenues sont égales coefficient par coefficient. Comme le polynôme caractéristique ne dépend pas de l'indexation, **$\chi_G=\chi_{G'}$**.

### Question 6

Notons $M$ la matrice d’adjacence du graphe et $\lambda_1,\ldots,\lambda_n$ ses valeurs propres comptées avec multiplicité. Le coefficient de $X^{n-1}$ vaut $-\sum_i\lambda_i=-\operatorname{Tr}M=0$ puisque la diagonale est nulle. Le coefficient de $X^{n-2}$ vaut $\sum_{i<j}\lambda_i\lambda_j$. En développant le carré de leur somme, qui est nulle,

$$
2\sum_{i<j}\lambda_i\lambda_j=-\sum_i\lambda_i^2=-\operatorname{Tr}(M^2).
$$

Pour chaque $i$, $(M^2)_{i,i}=\sum_j M_{i,j}^2$ est le nombre de voisins du sommet. Chaque arête est comptée deux fois dans la somme des degrés. Ainsi **$a_{n-1}=0$ et $a_{n-2}=-|A|$**.

### Question 7

Par Q2 et Q4, la matrice est diagonalisable de rang deux, donc le facteur $X$ a multiplicité $n-2$ dans le polynôme caractéristique. Comme une étoile à $d$ branches a $d$ arêtes, Q6 donne

$$
\boxed{\chi_G(X)=X^{n-2}(X^2-d).}
$$

Notons $e$ le vecteur canonique du centre et $v$ la somme de ceux des feuilles.

La matrice envoie $e$ sur $v$ et $v$ sur $de$.

Les espaces propres pour $\sqrt d$ et $-\sqrt d$ sont donc respectivement les droites engendrées par $\sqrt d\,e+v$ et $-\sqrt d\,e+v$.

Le noyau est constitué des vecteurs dont la coordonnée au centre est nulle et dont les coordonnées aux feuilles ont une somme nulle. Les coordonnées des sommets isolés sont libres. Lorsque $n=2$, ce noyau est réduit à zéro et zéro n'est pas valeur propre.

### Question 8

Indexons d'abord les sommets de $G_1$, puis ceux de $G_2$.

Dans $XI-M_G$, les deux blocs diagonaux sont $XI-M_{G_1}$ et $XI-M_{G_2}$.

Les seuls coefficients non nuls hors de ces blocs sont deux $-1$, aux positions $(s_1,s_2)$ et $(s_2,s_1)$ avec les indices de cette indexation.

Dans le développement du déterminant par permutations, les termes qui n'utilisent aucun de ces deux coefficients donnent $\chi_{G_1}\chi_{G_2}$. Un terme non nul qui en utilise un doit utiliser l'autre, car une permutation envoie autant d'indices du premier bloc vers le second que du second vers le premier. Elle échange donc $s_1$ et $s_2$ et conserve séparément les autres indices de chaque bloc. La transposition donne un signe moins et les deux coefficients $-1$ ont un produit égal à un. Les termes ainsi obtenus sont les produits des déterminants des blocs amputés, avec ce signe moins. La convention du déterminant vide convient si une composante n'a qu'un sommet. Ainsi,

$$
\boxed{\chi_G=\chi_{G_1}\chi_{G_2}-\chi_{G_1\setminus s_1}\chi_{G_2\setminus s_2}.}
$$

### Question 9

Chaque étoile à $d_i\ge1$ branches a le polynôme $X^{d_i-1}(X^2-d_i)$ par Q7. Après suppression du centre, ses $d_i$ feuilles isolées donnent le polynôme $X^{d_i}$. Par Q8,

$$
\boxed{\chi_G(X)
=X^{d_1+d_2-2}\bigl(X^4-(d_1+d_2+1)X^2+d_1d_2\bigr).}
$$

Comme $d_1d_2>0$, la multiplicité de zéro est $d_1+d_2-2$. La matrice, réelle symétrique, est diagonalisable. Son ordre est $d_1+d_2+2$, donc **son rang vaut quatre**.

### Question 10

Pour un graphe donné $G$ à $a$ arêtes, l'événement $\{G\}$ fixe à un les $a$ indicatrices de ses arêtes et à zéro les $N-a$ autres.

Par indépendance, **$\mathbb P(\{G\})=p_n^a q_n^{N-a}$**.

Il y a $\binom Na$ graphes ayant $a$ arêtes, puisqu'on choisit $a$ paires parmi $N$.

En sommant sur les graphes puis en utilisant le binôme,

$$
\begin{aligned}
\mathbb P(\Omega_n)&=\sum_{a=0}^N\binom Na p_n^a q_n^{N-a}\\
&=(p_n+q_n)^N\\
&=1,
\end{aligned}
$$

où $\Omega_n$ désigne l'ensemble des graphes de sommets $\llbracket1,n\rrbracket$.

## Partie II — Une première fonction de seuil

**Section A — Deux inégalités**

### Question 11

Comme $X$ prend ses valeurs dans $\mathbb N$, l'indicatrice de $\{X>0\}$ est inférieure ou égale à $X$. Par croissance de l'espérance, **$\mathbb P(X>0)\le\mathbb E(X)$**.

### Question 12

Si $\mathbb E(X)\ne0$, cette espérance est strictement positive puisque $X\ge0$. L'événement $\{X=0\}$ est contenu dans $\{|X-\mathbb E(X)|\ge\mathbb E(X)\}$. Comme $X$ a une variance finie, Bienaymé-Tchebychev donne

$$
\boxed{\mathbb P(X=0)\le\frac{\operatorname{Var}(X)}{\mathbb E(X)^2}.}
$$

**Section B — Une fonction de seuil**

### Question 13

Le nombre d'arêtes $A_n$ est la somme des $N$ indicatrices de paires, indépendantes et toutes de loi de Bernoulli de paramètre $p_n$. **$A_n$ suit donc la loi binomiale $\mathcal B(N,p_n)$.**

### Question 14

Si $p_n=o(n^{-2})$, alors $Np_n\le n^2p_n/2\to0$. Par Q11 appliquée à $A_n$ de moyenne $Np_n$, **$\mathbb P(A_n>0)\to0$**.

### Question 15

Si $n^{-2}=o(p_n)$, alors $Np_n\to+\infty$ car $N\sim n^2/2$. Par Q13, $\operatorname{Var}(A_n)=Np_nq_n$. La moyenne est non nulle et Q12 donne

$$
\begin{aligned}
0&\le\mathbb P(A_n=0)\\
&\le\frac{q_n}{Np_n}\\
&\le\frac1{Np_n}\longrightarrow0.
\end{aligned}
$$

Donc **$\mathbb P(A_n>0)\to1$**.

### Question 16

La propriété $\mathcal P_n$ est « le graphe contient au moins une arête ». Les deux régimes de Q14 et Q15 montrent que **$t_n=n^{-2}$ est une fonction de seuil** au sens de l'énoncé.

## Partie III — Fonction de seuil de la copie d’un graphe

### Question 17

L'événement $H\subset G$ impose la présence des $a_H$ arêtes de $H$, sans imposer l'absence des autres arêtes de $G$.

Les sommets de $H$ appartiennent déjà à ceux de $G$.

Par indépendance des indicatrices d'arêtes et puisque $X_H=\mathbf1_{\{H\subset G\}}$, **$\mathbb E(X_H)=p_n^{a_H}$**.

Cela vaut aussi pour $a_H=0$, où l'événement est certain.

### Question 18

Sur un ensemble fixé de $s_0$ sommets, le nombre $c_0$ ne dépend pas de cet ensemble. Toute bijection entre deux tels ensembles transporte les copies. Ainsi, pour $n\ge s_0$,

$$
\boxed{|\mathcal C_0|=c_0\binom n{s_0}.}
$$

Chaque copie sur un ensemble de $s_0$ sommets s'obtient par au moins une des $s_0!$ bijections depuis les sommets de $G_0$. Donc $c_0\le s_0!$, et $|\mathcal C_0|\le n(n-1)\cdots(n-s_0+1)\le n^{s_0}$. Si $n<s_0$, aucune copie n'est possible. **La majoration vaut dans tous les cas.**

### Question 19

Chaque copie candidate contribue un exactement quand elle est contenue dans $G$. Ainsi, $X_n^0=\sum_{H\in\mathcal C_0} X_H$. Par linéarité de l'espérance, Q17 et Q18,

$$
\boxed{\begin{aligned}
\mathbb E(X_n^0)
&=\sum_{H\in\mathcal C_0}\mathbb P(H\subset G)\\
&=|\mathcal C_0|p_n^{a_0}\\
&\le n^{s_0}p_n^{a_0}.
\end{aligned}}
$$

### Question 20

Choisissons un sous-graphe $H_0\subset G_0$ qui atteint le minimum de la définition de $\omega_0$. Il existe, car la famille de sous-graphes d'au moins une arête est finie et non vide. Une copie de $G_0$ dans $G$ contient l'image de $H_0$ par un isomorphisme, donc une copie de $H_0$.

En appliquant Q19 au graphe fixé $H_0$, puis Q11 au nombre de ses copies, on obtient

$$
\begin{aligned}
\mathbb P(X_n^0>0)
&\le n^{s_{H_0}}p_n^{a_{H_0}}\\
&=(n^{\omega_0}p_n)^{a_{H_0}},
\end{aligned}
$$

puisque $s_{H_0}/a_{H_0}=\omega_0$. Sous l'hypothèse $p_n=o(n^{-\omega_0})$, cette borne tend vers zéro. **$\mathbb P(X_n^0>0)\to0$.**

### Question 21

Dans le carré de la somme de Q19, les couples de copies sont ordonnés. Le produit $X_HX_{H'}$ indique que les deux copies sont contenues dans $G$, donc que leur union de sommets et d'arêtes y est contenue. Cette union a $2a_0-a_{H\cap H'}$ arêtes, par la formule du cardinal d'une union. Par Q17,

$$
\boxed{\begin{aligned}
\mathbb E((X_n^0)^2)
&=\sum_{(H,H')\in\mathcal C_0^2}\mathbb P(H\cup H'\subset G)\\
&=\sum_{(H,H')\in\mathcal C_0^2}p_n^{2a_0-a_{H\cap H'}}.
\end{aligned}}
$$

### Question 22

Si les ensembles de sommets de $H$ et $H'$ sont disjoints, leur intersection n'a aucune arête. D'après Q21, chaque couple de ce type contribue $p_n^{2a_0}$. Il y a au plus $|\mathcal C_0|^2$ couples ordonnés. Par Q19,

$$
\boxed{\Sigma_0\le|\mathcal C_0|^2p_n^{2a_0}=\mathbb E(X_n^0)^2.}
$$

### Question 23

Fixons $H\in\mathcal C_0$ et $1\le k\le s_0$.

Pour construire l'ensemble des sommets de $H'$, on choisit d'abord $k$ sommets de $H$. On complète par $s_0-k$ sommets dans le complémentaire, de taille $n-s_0$.

Chaque ensemble ainsi choisi porte $c_0$ copies, par Q18.

Pour chacun de ces couples, le graphe $H\cap H'$ a $k$ sommets.

Il est inclus dans $H$, donc isomorphe à un sous-graphe de $G_0$.

S'il a des arêtes, la définition de $\omega_0$ donne $\omega_0 a_{H\cap H'}\le k$.

L'inégalité reste vraie s'il n'a aucune arête.

Comme $0<p_n<1$, le terme de Q21 est majoré par $p_n^{2a_0-k/\omega_0}$.

On obtient, pour $n\ge s_0$,

$$
\boxed{\Sigma_k\le
\sum_{H\in\mathcal C_0}\binom{s_0}k\binom{n-s_0}{s_0-k}
c_0p_n^{2a_0-k/\omega_0}.}
$$

Un coefficient binomial vaut zéro si le nombre d'éléments demandés dépasse celui des éléments disponibles.

### Question 24

Pour $1\le q\le r$, chaque facteur $r-j$ du numérateur de $\binom rq$ vérifie, pour $0\le j\le q-1$,

$$
r-j\ge r-(q-1)\ge r\left(1-\frac{q-1}{q}\right),
$$

car $r\ge q$. En multipliant et en divisant par $q!r^q$,

$$
\boxed{\binom rq r^{-q}\ge\frac1{q!}\left(1-\frac{q-1}{q}\right)^q.}
$$

Pour $n\ge s_0$, on a $\mathbb E(X_n^0)=|\mathcal C_0|p_n^{a_0}>0$ par Q19. En divisant Q23 par le carré de cette expression puis en utilisant $|\mathcal C_0|=c_0\binom n{s_0}$, on obtient

$$
\frac{\Sigma_k}{\mathbb E(X_n^0)^2}
\le \binom{s_0}k\frac{\binom{n-s_0}{s_0-k}}{\binom n{s_0}}
p_n^{-k/\omega_0}.
$$

Le numérateur du quotient de coefficients est au plus $n^{s_0-k}/(s_0-k)!$.

La première inégalité, appliquée à $r=n$ et $q=s_0$, minore son dénominateur par une constante strictement positive fois $n^{s_0}$.

Ainsi le membre de droite est majoré par une constante indépendante de $n$ fois $(n^{\omega_0}p_n)^{-k/\omega_0}$.

Cette expression tend vers zéro par l'hypothèse de la sous-partie.

**Pour chaque $1\le k\le s_0$, $\Sigma_k=o(\mathbb E(X_n^0)^2)$.**

### Question 25

Par Q21, $\mathbb E((X_n^0)^2)=\sum_{k=0}^{s_0}\Sigma_k$. La contribution $\Sigma_0$ est au plus $\mathbb E(X_n^0)^2$ par Q22. Ainsi,

$$
\begin{aligned}
0&\le\frac{\operatorname{Var}(X_n^0)}{\mathbb E(X_n^0)^2}\\
&\le\sum_{k=1}^{s_0}\frac{\Sigma_k}{\mathbb E(X_n^0)^2}.
\end{aligned}
$$

Les $s_0$ termes tendent tous vers zéro par Q24 et $s_0$ est fixé. **Le quotient de variance tend donc vers zéro.**

### Question 26

Si $p_n=o(n^{-\omega_0})$, Q20 donne $\mathbb P(X_n^0>0)\to0$.

Si $n^{-\omega_0}=o(p_n)$, alors $n^{\omega_0}p_n\to+\infty$ et Q25 s'applique.

Pour $n\ge s_0$, la moyenne est strictement positive et Q12 majore $\mathbb P(X_n^0=0)$ par le quotient de Q25.

Donc $\mathbb P(X_n^0>0)\to1$.

**La suite $t_n=n^{-\omega_0}$ est bien une fonction de seuil.**

### Question 27

Prenons d'abord $G_0$ égal à l'unique arête sur deux sommets. Le seul sous-graphe de $G_0$ ayant au moins une arête a deux sommets et une arête. L'exposant de Q26 vaut donc $2$, ce qui redonne **$t_n=n^{-2}$** pour la présence d'au moins une arête.

Pour une étoile à $d$ branches, un sous-graphe ayant $a\ge1$ arêtes contient le centre et au moins $a$ feuilles distinctes. Il a donc au moins $a+1$ sommets et son rapport sommets sur arêtes est au moins $(a+1)/a\ge(d+1)/d$. La dernière valeur est atteinte par l'étoile entière. Par Q26, **une fonction de seuil est $t_n=n^{-(d+1)/d}$**.
