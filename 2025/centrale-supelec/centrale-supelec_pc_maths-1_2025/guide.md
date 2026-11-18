# Centrale-Supélec PC — Mathématiques 1 2025 · Corrigé guidé

*Corrigé rédigé par IA, non officiel. Signalez toute erreur.*

## Présentation du sujet

Le sujet relie le principe d’incertitude pour des fonctions à un problème de dispersion sur un graphe. La partie A fait calculer des intégrales de Fourier pour les gaussiennes. La partie B introduit le laplacien d’un graphe et l’exprime à l’aide de sommes de carrés. La partie C étudie les valeurs que peuvent prendre ensemble deux mesures de dispersion. La partie D calcule le bord inférieur de cette région pour le graphe étoile.

Les premières questions sur les équations différentielles et le laplacien permettent de progresser dans deux parties distinctes. Dans la dernière partie, gardez les identités trigonométriques de Q32 à Q34 à portée de main. Q35 demande à la fois une minoration valable pour tous les vecteurs et une preuve que cette borne est atteinte.

## Partie A — Autour du principe d’incertitude d’Heisenberg

### A.I — Valeurs propres de l’opérateur dérivée seconde

### Question 1

> [!INDICATION]
> La dérivation seconde conserve-t-elle l'espace des fonctions indéfiniment dérivables ?

#### Solution

Pour $f\in E$, la fonction $-f''$ est encore indéfiniment dérivable et à valeurs complexes. Pour $f,g\in E$ et $u,v\in\mathbb C$, on a $-(uf+vg)''=-uf''-vg''$.

Ainsi $\ell$ est un endomorphisme complexe de $E$.

### Question 2

> [!INDICATION]
> Résoudre l’équation caractéristique en distinguant le cas de la racine double nulle.

#### Solution

L’équation $\ell(f)=\lambda f$ équivaut à $f''+\lambda f=0$. Si $\lambda=0$, une base de l’espace des solutions est le couple $(t\mapsto 1,\ t\mapsto t)$.

Pour $\lambda>0$, une base sur $\mathbb C$ est $(t\mapsto\cos(\sqrt\lambda\,t),\ t\mapsto\sin(\sqrt\lambda\,t))$. Ces deux fonctions correspondent à des données initiales indépendantes en zéro. Dans les deux cas il existe une solution non nulle, donc $\mathbb R_+\subset\mathrm{VP}(\ell)$.

### A.II — Cas des fonctions gaussiennes

### Question 3

> [!INDICATION]
> Prendre le module de l’intégrande avant toute comparaison.

#### Solution

Pour chaque $\xi\in\mathbb R$, la fonction $t\mapsto G_a(t)e^{-i\xi t}$ est continue et son module vaut $G_a(t)$. Cette dernière est intégrable sur $\mathbb R$ par la donnée de l'énoncé. L'intégrale de Fourier est donc absolument convergente.

### Question 4

> [!INDICATION]
> Vérifier séparément les hypothèses du théorème de classe $C^1$ pour une intégrale à paramètre.

#### Solution

Posons $F(\xi,t)=G_a(t)e^{-i\xi t}$. Pour tout $\xi$, $F(\xi,\cdot)$ est continue et intégrable par Q3.

Pour tout $t$, $F(\cdot,t)$ est $C^1$, de dérivée $-itG_a(t)e^{-i\xi t}$, continue aussi en $t$.

Son module est majoré uniformément en $\xi$ par $|t|G_a(t)$. Ce majorant est intégrable puisque $\int_0^\infty tG_a(t)\,dt=1/a$ par la primitive $-G_a/a$, puis par parité. Le théorème de dérivation sous le signe intégral, appliqué aux parties réelle et imaginaire, donne $\widehat G_a\in C^1$ et
$$
\widehat G_a'(\xi)=\int_{\mathbb R}-itG_a(t)e^{-i\xi t}\,dt.
$$

### Question 5

> [!INDICATION]
> Remplacer $tG_a(t)$ par un multiple de $G_a'(t)$, puis intégrer par parties sur un segment.

#### Solution

Comme $G_a'(t)=-atG_a(t)$, Q4 donne $\widehat G_a'(\xi)=\frac{i}{a}\int_{\mathbb R}G_a'(t)e^{-i\xi t}\,dt$. L'intégration par parties sur $[-R,R]$ puis la limite $R\to+\infty$ donnent
$$
\int_{\mathbb R}G_a'(t)e^{-i\xi t}\,dt=i\xi\widehat G_a(\xi).
$$
Le terme de bord tend vers zéro car chaque produit a pour module $G_a(\pm R)$, et les deux intégrales en jeu convergent absolument par Q3 et Q4. Ainsi $\widehat G_a'+\frac{\xi}{a}\widehat G_a=0$. Le produit $e^{\xi^2/(2a)}\widehat G_a(\xi)$ est constant et vaut $\widehat G_a(0)=\sqrt{2\pi/a}$. D'où $\widehat G_a=\sqrt{2\pi/a}\,G_{1/a}$.

### Question 6

> [!INDICATION]
> Exprimer la seconde intégrale à l’aide de la dérivée de $G_{2a}$.

#### Solution

Le premier intégrande est continu et l'intégrale admise avec le paramètre $2a$ donne $\int_{\mathbb R}G_{2a}=\sqrt{\pi/a}$. Le second est continu, positif et intégrable puisque $u^2e^{-au^2/2}$ est borné et $u^2G_{2a}(u)=(u^2e^{-au^2/2})G_a(u)$. Sur $[-R,R]$,
$$
\int_{-R}^R u^2G_{2a}(u)\,du
=-\frac{[uG_{2a}(u)]_{-R}^R}{2a}+\frac1{2a}\int_{-R}^R G_{2a}(u)\,du.
$$
Le crochet tend vers zéro par décroissance exponentielle. La seconde intégrale vaut donc $\frac1{2a}\sqrt{\pi/a}$.

### Question 7

> [!INDICATION]
> Appliquer le résultat précédent aux paramètres $a$ et $1/a$.

#### Solution

On a $G_a^2=G_{2a}$ et $\widehat G_a^2=(2\pi/a)G_{2/a}$. Par Q6,
$$
\begin{aligned}\sigma_T^2(G_a)&=\frac1{2a},\\
\sigma_F^2(G_a)&=\frac{(2\pi/a)(a/2)\sqrt{\pi a}}{2\pi\sqrt{\pi/a}}=\frac a2.\end{aligned}
$$
On obtient $\sigma_T^2(G_a)=1/(4\sigma_F^2(G_a))=\gamma(\sigma_F^2(G_a))$.

## Partie B — Laplacien d’une matrice

### B.I — Étude d’un élément de G

### Question 8

> [!INDICATION]
> Repérer deux colonnes indépendantes après avoir exprimé les deux autres.

#### Solution

Chaque ligne de $B$ a pour somme 1, donc $\delta(B)=I_4$ et
$$
L_B=I_4-B=
\begin{pmatrix}1&0&0&-1\\0&1&-1&0\\0&-1&1&0\\-1&0&0&1\end{pmatrix}.
$$
Les colonnes 3 et 4 sont les opposées des colonnes 2 et 1. Les deux premières sont indépendantes, par leurs deux premières coordonnées. Le rang vaut 2.

### Question 9

> [!INDICATION]
> Exploiter l’égalité $B^2=I_4$, puis utiliser aussi le rang.

#### Solution

La matrice $B$ échange les coordonnées 1 et 4 ainsi que 2 et 3, donc $B^2=I_4$. Il vient $L_B^2=I_4-2B+B^2=2L_B$. Une valeur propre $\lambda$ vérifie $\lambda^2=2\lambda$, donc appartient à $\{0,2\}$.

La matrice réelle symétrique $L_B$ possède une base orthonormée de vecteurs propres. Par Q8, $\dim E_0(L_B)=2$. Les deux dimensions restantes correspondent donc à $E_2(L_B)$, et $\mathrm{Sp}(L_B)=\{0,2\}$ avec $\dim E_2(L_B)=2$.

### Question 10

> [!INDICATION]
> Passer du spectre à la forme quadratique en utilisant la symétrie.

#### Solution

La matrice $L_B$ est symétrique réelle. Dans une base orthonormée de vecteurs propres, sa forme quadratique est une somme de carrés pondérés par 0 et 2. Elle est positive, et un vecteur propre non nul pour 0 annule cette forme. Ainsi $L_B\in S_4^+(\mathbb R)$ et $L_B\notin S_4^{++}(\mathbb R)$.

### B.II — Étude du noyau du laplacien

### Question 11

> [!INDICATION]
> Calculer $A1_N$ et $\delta(A)1_N$, puis chercher un exemple avec un noyau plus grand.

#### Solution

Les coordonnées de $A1_N$ et de $\delta(A)1_N$ sont dans les deux cas les sommes des lignes de $A$. Donc $L_A1_N=0$ et $\mathrm{Vect}(1_N)\subset\ker L_A$. L'égalité n'est pas automatique.

Pour la matrice nulle de taille $N\ge2$, le noyau de $L_A$ est $\mathbb R^N$.

### Question 12

> [!INDICATION]
> Développer la forme quadratique d’une matrice diagonale.

#### Solution

Le coefficient diagonal d'indice $i$ de $\delta(A)$ vaut $\sum_{j=1}^N a_{ij}$. Il en résulte
$$
\begin{aligned}x^T\delta(A)x&=\sum_{i=1}^N x_i^2\sum_{j=1}^Na_{ij}\\&=\sum_{i,j=1}^Na_{ij}x_i^2.\end{aligned}
$$

### Question 13

> [!INDICATION]
> Développer le carré et regrouper les deux termes obtenus par échange des indices.

#### Solution

La symétrie de $A$ donne $a_{ij}=a_{ji}$. Comme le carré est nul pour $i=j$, la somme pour $i<j$ vaut la moitié de la somme sur tous les couples. Cette dernière, après division par 2, s'écrit
$$
\begin{aligned}\frac12\sum_{i,j=1}^N a_{ij}(x_i-x_j)^2&=\sum_{i,j=1}^Na_{ij}x_i^2-\sum_{i,j=1}^Na_{ij}x_ix_j\\&=x^T\delta(A)x-x^TAx\\&=x^TL_Ax.\end{aligned}
$$
On a utilisé Q12 pour le premier terme.

### Question 14

> [!INDICATION]
> Vérifier la symétrie avant d’appliquer la formule de Q13.

#### Solution

La différence $\delta(A)-A$ est symétrique réelle. Pour tout $x\in\mathbb R^N$, la formule de Q13 donne $x^TL_Ax\ge0$ puisque chaque $a_{ij}$ est positif ou nul. Donc $L_A\in S_N^+(\mathbb R)$.

### Question 15

> [!INDICATION]
> Propager l’égalité des coordonnées le long d’un chemin donné par $(\Gamma)$.

#### Solution

Si $x\in\ker L_A$, alors $x^TL_Ax=0$. Dans la somme de Q13, tous les termes sont positifs ou nuls, donc $x_i=x_j$ chaque fois que $a_{ij}=1$. Pour deux indices distincts, $(\Gamma)$ fournit une chaîne le long de laquelle les coordonnées sont égales de proche en proche. Toutes les coordonnées de $x$ sont donc égales.

Réciproquement, Q11 assure que tout multiple de $1_N$ appartient au noyau.

## Partie C — Région de faisabilité et courbe d’incertitude

### C.I — Définitions des deux dispersions

### Question 16

> [!INDICATION]
> Relier deux indices périphériques en passant par l’indice 1.

#### Solution

La matrice $A$ est symétrique, à coefficients dans $\{0,1\}$ et à diagonale nulle. Tout sommet distinct de 1 est relié à 1. Pour deux indices périphériques distincts $i,j$, la suite $(i,1,j)$ vérifie $(\Gamma)$. Lorsque l'un des indices est 1, le lien direct suffit.

### Question 17

> [!INDICATION]
> Combiner le théorème spectral, la positivité et la dimension du noyau.

#### Solution

Par Q14, $L_A$ est réelle symétrique positive. Le théorème spectral donne une base orthonormée réelle de vecteurs propres, dont les valeurs propres sont toutes positives ou nulles. Par Q15 et Q16, $\ker L_A$ est de dimension 1. En rangeant les $N$ valeurs propres comptées avec multiplicité, il vient $0=\lambda_1<\lambda_2\le\cdots\le\lambda_N$.

### Question 18

> [!INDICATION]
> Utiliser des blocs puis déterminer la valeur propre manquante par la trace.

#### Solution

Avec $u=1_{N-1}$, on a
$$
L_A=\begin{pmatrix}N-1&-u^T\\-u&I_{N-1}\end{pmatrix},\qquad
L_A-I_N=\begin{pmatrix}N-2&-u^T\\-u&0\end{pmatrix}.
$$
Dans la seconde matrice, les $N-1$ dernières colonnes sont identiques et non nulles, colinéaires au premier vecteur de la base canonique. La première colonne est indépendante de celles-ci, car ses dernières coordonnées valent $-1$. Le rang vaut donc 2, et l'espace propre pour 1 est de dimension $N-2$. Avec 0 simple, il reste une valeur propre. La trace vaut $2(N-1)$, donc cette valeur vaut $2(N-1)-(N-2)=N$.

Ainsi $\mathrm{Sp}(L_A)=\{0,1,N\}$ et $E_N(L_A)$ est de dimension 1.

### Question 19

> [!INDICATION]
> Décomposer $x$ dans une base orthonormée de vecteurs propres et regarder les coefficients de la moyenne.

#### Solution

Soit $(u_i)_{i=1}^N$ une base orthonormée telle que $L_Au_i=\lambda_i u_i$, et écrivons $x=\sum_{i=1}^N c_i u_i$. Alors
$$
\sigma_S^2(x)=\frac{\sum_i\lambda_i c_i^2}{\sum_i c_i^2}.
$$
Il s'agit d'une moyenne pondérée comprise entre $\lambda_1$ et $\lambda_N$. Pour $\mu\ne0$, le numérateur et le dénominateur sont tous deux multipliés par $\mu^2$, ce qui donne l'invariance.

Si $\sigma_S^2(x)=\lambda_1$, alors $\sum_i(\lambda_i-\lambda_1)c_i^2=0$, donc $c_i=0$ pour chaque $\lambda_i>\lambda_1$. Ainsi $x\in E_{\lambda_1}(L_A)$.

Réciproquement, pour $x$ dans ce sous-espace, $L_Ax=\lambda_1x$ donne directement l'égalité.

### C.II — Région de faisabilité

### Question 20

> [!INDICATION]
> Écrire $x^TDx$ comme une somme partielle des carrés des coordonnées.

#### Solution

Q19 encadre $s$ par 0 et $\lambda_N$. Pour tout $x\ne0$, la dispersion $\sigma_M^2(x)=(\sum_{i=2}^Nx_i^2)/(\sum_{i=1}^Nx_i^2)$ appartient à $[0,1]$. Ainsi $\mathcal R\subset[0,\lambda_N]\times[0,1]$.

### Question 21

> [!INDICATION]
> Identifier les vecteurs qui atteignent l’extrémité gauche du spectre.

#### Solution

Si $\sigma_S^2(x)=0$, Q19 et Q15 donnent $x=c1_N$ avec $c\ne0$. Alors $\sigma_M^2(x)=(N-1)c^2/(Nc^2)=(N-1)/N$. Le vecteur $1_N$ réalise cette valeur. L'unique point d'intersection a donc pour coordonnées $(0,(N-1)/N)$.

### Question 22

> [!INDICATION]
> Trouver un générateur de $E_N(L_A)$ puis traduire $\sigma_M^2(x)=0$ en conditions sur les coordonnées.

#### Solution

Pour $s=N=\lambda_N$, l'égalité spectrale admise impose $x\in E_N(L_A)$. D'après la matrice de Q18, le vecteur $v=(N-1,-1,\ldots,-1)^T$ vérifie $L_Av=Nv$. Comme l'espace propre est de dimension 1, tous les vecteurs admissibles sont des multiples non nuls de $v$. Ils donnent $\sigma_M^2(v)=(N-1)/((N-1)^2+N-1)=1/N$.

L'intersection avec $s=N$ est donc le point $(N,1/N)$.

Pour $m=0$, toutes les coordonnées sauf la première sont nulles. Si $x=ce_1$ avec $c\ne0$ et $e_1$ premier vecteur canonique, alors $\sigma_S^2(x)=N-1$. Tous ces vecteurs réalisent donc le seul point $(N-1,0)$.

### C.III — Courbe d’incertitude

### Question 23

> [!INDICATION]
> Les vecteurs propres des deux extrémités du spectre sont orthogonaux. Appliquer le théorème des valeurs intermédiaires.

#### Solution

Les vecteurs unitaires $e_1$ et $e_N$ sont orthogonaux car ils correspondent à des valeurs propres distinctes d'une matrice symétrique. Ainsi $\|x_t\|^2=(1-t)^2+t^2>0$, donc $\phi$ est définie et continue sur $[0,1]$. Elle prend les valeurs 0 et $\lambda_N$ aux deux extrémités.

Le théorème des valeurs intermédiaires donne un $t$ pour chaque $s$ demandé.

### Question 24

> [!INDICATION]
> Considérer le sous-ensemble de la sphère unité imposé par la contrainte sur $s$.

#### Solution

Pour $s\in[0,\lambda_N]$, l'ensemble $K_s=\{x:\|x\|=1,\ x^TL_Ax=s\}$ est non vide par Q23 après normalisation, qui conserve $\sigma_S^2$ par Q19. Il est fermé comme intersection de deux ensembles de niveau de fonctions continues et borné comme partie de la sphère unité. Il est donc compact dans $\mathbb R^N$. La fonction continue $x\mapsto x^TDx$ y atteint son minimum.

### Question 25

> [!INDICATION]
> Former un segment entre deux points du bord inférieur, puis comparer son ordonnée au minimum.

#### Solution

Pour $s_1,s_2\in[0,\lambda_N]$, les points $(s_1,\gamma_-(s_1))$ et $(s_2,\gamma_-(s_2))$ appartiennent à $\mathcal R$ par Q24. Pour $t\in[0,1]$, leur combinaison convexe appartient à $\mathcal R$ par hypothèse.

À l'abscisse $(1-t)s_1+ts_2$, son ordonnée majore le minimum $\gamma_-((1-t)s_1+ts_2)$. C'est l'inégalité de convexité de $\gamma_-$.


## Partie D — Formule explicite pour la courbe d’incertitude

### Question 26

> [!INDICATION]
> Comparer les quotients de Rayleigh de $M(\alpha)$ à dispersion $s$ fixée.

#### Solution

Posons $s=\sigma_S^2(y)$. Pour tout $x\in K_s$, le théorème spectral donne $x^TM(\alpha)x\ge\mu_\alpha^-$ et l'égalité est atteinte pour $y$ puisque $\|y\|=1$.

Comme $x^TM(\alpha)x=\sigma_M^2(x)-\alpha s$ sur $K_s$, on en tire $\sigma_M^2(x)\ge\sigma_M^2(y)$. Ainsi $\sigma_M^2(y)=\gamma_-(s)$.

### Question 27

> [!INDICATION]
> Reprendre le raisonnement par les colonnes de Q18 et repérer où $\alpha\ne0$ intervient.

#### Solution

Avec $u=1_{N-1}$, on a
$$
M(\alpha)-(1-\alpha)I_N
=\begin{pmatrix}-1-\alpha(N-2)&\alpha u^T\\\alpha u&0\end{pmatrix}.
$$
Les dernières colonnes sont identiques et non nulles car $\alpha\ne0$. La première est indépendante d'elles puisque la partie basse vaut $\alpha u\ne0$. Le rang vaut 2. Ainsi $1-\alpha$ est une valeur propre de multiplicité géométrique $N-2>0$, donc $\mu_\alpha^-\le1-\alpha\le\mu_\alpha^+$.

### Question 28

> [!INDICATION]
> Traiter le discriminant comme un trinôme en $\lambda$ et en calculer le minimum.

#### Solution

Le discriminant en $x$ vaut
$$
\Delta(\lambda)
=(\lambda-a-b)^2-4(ab-\lambda c)
=(\lambda+2c-a-b)^2-4(c-a)(c-b).
$$
Il est supposé positif ou nul pour tout réel $\lambda$. En prenant $\lambda=a+b-2c$, on obtient $(c-a)(c-b)\le0$, ce qui équivaut à $a\le c\le b$.

### Question 29

> [!INDICATION]
> Développer le déterminant par rapport au coefficient modifié, puis écarter l’égalité en $X=1-\alpha$.

#### Solution

Posons $c=1-\alpha$ et $\chi_H(X)=\det(XI_N-H)$ pour toute matrice $H$ de taille $N$. Le seul coefficient modifié dans $XI_N-N(\lambda)$ est le premier coefficient diagonal, qui augmente de $\lambda$.

Son cofacteur vaut $(X-c)^{N-1}$ car le bloc inférieur droit vaut $(X-c)I_{N-1}$. On obtient
$$
\chi_{N(\lambda)}(X)=\chi_{M(\alpha)}(X)+\lambda(X-c)^{N-1}.
$$
Par Q27 et le théorème spectral, la multiplicité algébrique de $c$ est exactement $N-2$. On peut donc écrire $\chi_{M(\alpha)}(X)=(X-c)^{N-2}(X-a)(X-b)$ pour deux valeurs propres réelles $a\le b$ distinctes de $c$.

Puisque $N(\lambda)$ est réelle symétrique pour tout $\lambda$, le facteur $(X-a)(X-b)+\lambda(X-c)$ a toujours ses racines réelles. Q28 donne $a\le c\le b$, et l'exactitude de la multiplicité impose $a<c<b$.

On a donc $a=\mu_\alpha^-$ et $b=\mu_\alpha^+$, d'où l'encadrement strict.

### Question 30

> [!INDICATION]
> Paramétrer les coordonnées $v_2,\dots,v_{N-1}$ et exprimer la dernière.

#### Solution

L'ensemble $V$ est l'intersection des noyaux des deux formes linéaires $v\mapsto v_1$ et $v\mapsto\sum_{i=2}^Nv_i$.

Si $(e_i)_{i=1}^N$ est la base canonique, alors tout $v\in V$ s'écrit $\sum_{i=2}^{N-1}v_i(e_i-e_N)$, car $v_N=-\sum_{i=2}^{N-1}v_i$. La famille $(e_i-e_N)_{2\le i\le N-1}$ est libre par lecture des coordonnées 2 à $N-1$.

C'est une base et $d=N-2$.

### Question 31

> [!INDICATION]
> Identifier $V$ à l’espace propre intermédiaire et prendre son orthogonal.

#### Solution

Avec le bloc de Q27, tout $v\in V$ vérifie $(M(\alpha)-(1-\alpha)I_N)v=0$. Les deux espaces ont dimension $N-2$, donc $V=E_{1-\alpha}(M(\alpha))$. La décomposition spectrale orthogonale et Q29 montrent que la somme des deux espaces propres extrêmes est $V^\perp$.

Par Q30, l'orthogonalité aux $e_i-e_N$ équivaut à $x_i=x_N$ pour chaque $2\le i\le N-1$. D'où le plan demandé, que l'on note $W$.

### Question 32

> [!INDICATION]
> Dans la somme de Q13, seules les paires contenant l’indice 1 contribuent.

#### Solution

Le vecteur $x(\theta)$ est de norme 1. La formule de Q13 donne
$$
\sigma_S^2(x(\theta))
=(N-1)\left(\cos\theta-\frac{\sin\theta}{\sqrt{N-1}}\right)^2
=(N-1)\cos^2\theta+\sin^2\theta-\sqrt{N-1}\sin(2\theta).
$$
En remplaçant les carrés par $(1+\cos(2\theta))/2$ et $(1-\cos(2\theta))/2$, on obtient $\sigma_S^2(x(\theta))=N/2+(N-2)\cos(2\theta)/2-\sqrt{N-1}\sin(2\theta)$.

### Question 33

> [!INDICATION]
> Calculer $\sigma_M^2(x(\theta))$ et isoler le sinus.

#### Solution

Les dernières coordonnées donnent $\sigma_M^2(x(\theta))=\sin^2\theta=m$. En notant $s=\sigma_S^2(x(\theta))$, la première égalité développée de Q32 donne $s=N-1-(N-2)m-\sqrt{N-1}\sin(2\theta)$. Donc
$$
-\sin(2\theta)=\frac{s+(N-2)m-(N-1)}{\sqrt{N-1}}.
$$

### Question 34

> [!INDICATION]
> Exprimer aussi le cosinus et utiliser l’identité trigonométrique fondamentale.

#### Solution

Comme $\cos(2\theta)=1-2m$, l'identité $\cos^2(2\theta)+\sin^2(2\theta)=1$ fournit, avec Q33,
$$
(N-1)(1-2m)^2+\bigl(s+(N-2)m-(N-1)\bigr)^2=N-1.
$$

### Question 35

> [!INDICATION]
> Étendre l’égalité de Q34 en une inégalité pour les vecteurs quelconques. Pour l’atteinte, retrouver un angle à partir du cosinus et du sinus.

> [!INDICATION]
> Vérifier la valeur en $s=0$ avec Q21 pour contrôler le signe du terme constant du numérateur.

#### Solution

Les deux quotients sont invariants par multiplication par un scalaire non nul. Normalisons donc un vecteur quelconque $x$ et posons $s=\sigma_S^2(x)$ et $m=\sigma_M^2(x)$. On a $x_1^2=1-m$ et $\sum_{i=2}^Nx_i^2=m$. Dans la matrice par blocs de Q18,
$$
s=(N-1)(1-m)+m-2x_1\sum_{i=2}^Nx_i.
$$
L'inégalité de Cauchy–Schwarz donne $\bigl(s+(N-2)m-(N-1)\bigr)^2\le4(N-1)m(1-m)$. Autrement dit,
$$
P_s(m)=N^2m^2+2\bigl((N-2)s-N(N-1)\bigr)m+(s-(N-1))^2\le0.
$$
Pour $s\in[0,N]$, le discriminant vaut $16s(N-1)(N-s)$, donc tout point admissible d'abscisse $s$ a une ordonnée au moins égale à la petite racine $m_-(s)$. Cette racine satisfait l'égalité de Q34, car celle-ci est équivalente à $P_s(m)=0$.

Les nombres $1-2m_-(s)$ et $-(s+(N-2)m_-(s)-(N-1))/\sqrt{N-1}$ forment ainsi un couple de norme 1. Il existe $\theta$ ayant ce couple pour $(\cos(2\theta),\sin(2\theta))$. Par Q32 et Q33, $x(\theta)$ réalise le couple $(s,m_-(s))$.

L'argument couvre aussi $s=0$ et $s=N$, où les deux racines coïncident. Finalement, pour $s\in[0,N]$,
$$
\boxed{\gamma_-(s)=\frac{-s(N-2)+N(N-1)-2\sqrt{s(N-1)(N-s)}}{N^2}.}
$$
Le sujet imprime un signe moins devant $N(N-1)$. Ce signe donnerait une valeur négative en $s=0$, tandis que Q21 donne $\gamma_-(0)=(N-1)/N$. Le signe correct est le signe plus de la formule démontrée.

## Bilan

- Pour dériver une intégrale à paramètre, cherchez un majorant intégrable indépendant du paramètre sur le domaine considéré.
- Sur un graphe, écrivez la forme quadratique du laplacien comme une somme sur les arêtes. Cette écriture donne son signe et permet de caractériser l’annulation.
- Pour déterminer le bord d’une région de valeurs, fixez la première coordonnée, minorez la seconde sur toute la fibre, puis construisez un vecteur qui réalise l’égalité. Les valeurs aux extrémités servent aussi à vérifier la formule obtenue.
