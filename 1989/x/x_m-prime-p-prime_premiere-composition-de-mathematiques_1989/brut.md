# École polytechnique — Première composition de mathématiques · M′ et P′ 1989 · Corrigé brut

*Corrigé rédigé par IA, non officiel. Signalez toute erreur.*

**Rédaction** · GPT-6.2 Astra Ultra · vitesse non renseignée

Dans l’espace euclidien réel $E$ de dimension $n\ge2$, on écrit $a^*$ pour l’adjoint. On notera $|a|$ la norme issue de la trace et $\|a\|_{\mathrm{op}}$ la norme d’opérateur. Les lettres $F,G$ désignent les images des projecteurs $f,g$ sauf dans les écritures matricielles de la dernière partie.

Les compléments réservés à M′ et la précision propre à P′ sont signalés dans les réponses concernées. [Fac-similé UPS](https://prepas.org/index.php?module=Sujets&voir=get&file=doc-f87d10e5710a4b3899f2) · [Notice annuelle](https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000000884199).

## I. Deux normes sur les endomorphismes

### Question 1.a

Dans une telle base, $\operatorname{tr}(a^*b)=\sum_{i,j}a_{ij}b_{ij}$. Cette expression est bilinéaire et symétrique. Pour $a=b$, elle est positive ou nulle et ne s’annule que si tous les coefficients de $a$ sont nuls. C’est donc un produit scalaire.

### Question 1.b

Dans la même base, $|a|^2=\sum_{i,j}a_{ij}^2=\sum_{i,j}a_{ji}^2=|a^*|^2$. Les normes étant positives, $|a|=|a^*|$.

### Question 1.c

Écrivons $L_i$ pour les lignes de $a$ et $C_j$ pour les colonnes de $b$, vues comme vecteurs de $\mathbb R^n$. Chaque coefficient de $ab$ vaut $\langle L_i,C_j\rangle$. En sommant les inégalités de Cauchy–Schwarz au carré, on obtient $|ab|^2\le\sum_{i,j}\|L_i\|^2\|C_j\|^2=|a|^2|b|^2$.

### Question 1.d

**M′ seulement.** Si $a=0$ ou $b=0$, l’égalité est acquise. Sinon elle impose l’égalité pour chaque paire $(L_i,C_j)$. Une ligne et une colonne non nulles fixent alors une même droite, qui contient toutes les lignes de $a$ et toutes les colonnes de $b$. Cela revient à $\operatorname{Im}a^*=\operatorname{Im}b$ de dimension un. Réciproquement cette condition rend toutes les paires colinéaires et donne l’égalité.

### Question 2.a

Soient $\mu_1,\ldots,\mu_n\ge0$ ses valeurs propres, comptées avec multiplicité. Sa trace donne $|a|=\sqrt{\sum_i\mu_i}$. Pour $x$ unitaire de coordonnées $x_i$ dans une base propre, $\|ax\|^2=\sum_i\mu_i x_i^2\le\max_i\mu_i$, avec égalité sur un vecteur propre de la plus grande valeur. Ainsi $\|a\|_{\mathrm{op}}=\sqrt{\max_i\mu_i}$.

### Question 2.b

De $\sum_i\mu_i/n\le\max_i\mu_i\le\sum_i\mu_i$ on tire $|a|/\sqrt n\le\|a\|_{\mathrm{op}}\le |a|$. Pour l’identité, $|I|=\sqrt n$ et $\|I\|_{\mathrm{op}}=1$. La meilleure constante inférieure est donc $K=1/\sqrt n$.

### Question 2.c

**M′ seulement.** Dans une base orthonormale, prenons $a_t=\operatorname{diag}(1,t,\ldots,t)$ avec $0\le t\le1$. Le quotient vaut $(1+(n-1)t^2)^{-1/2}$. Continu, il décroît de $1$ à $1/\sqrt n$ et prend toutes les valeurs du segment.

### Question 3.a

On a $\|a\|_{\mathrm{op}}=\sup_{\|x\|=\|y\|=1}|\langle ax,y\rangle|$. En passant à l’adjoint et en échangeant les variables, on obtient le même supremum pour $a^*$. Ainsi $\|a\|_{\mathrm{op}}=\|a^*\|_{\mathrm{op}}$.

### Question 3.b

Dans une base orthonormale $(e_j)$, $|ab|^2=\sum_j\|a(be_j)\|^2\le\|a\|_{\mathrm{op}}^2|b|^2$. La même inégalité pour $b^*a^*$, jointe à 1.b et 3.a, donne $|ab|\le |a|\|b\|_{\mathrm{op}}$.

## II. Projections et transport d’un sous-espace

### Question 4.a

Un projecteur orthogonal vérifie $f=f^*=f^2$, comme le montre sa matrice diagonale de zéros et de uns dans une base adaptée. Réciproquement, $f^2=f$ décompose $E$ en $\operatorname{Im}f\oplus\ker f$, et $f^*=f$ rend ces espaces orthogonaux. Les relations caractérisent donc les projecteurs orthogonaux.

### Question 4.b

Pour un projecteur orthogonal de rang $p$, $|f|^2=\operatorname{tr}f=p$. Tout entier de zéro à $n$ est le rang de la projection sur un sous-espace de dimension correspondante. Les valeurs cherchées sont donc les $\sqrt p$ pour $0\le p\le n$.

### Question 5

Soient $u,v$ de norme un et d’angle $\alpha$, choisis avec $\langle u,v\rangle=\cos\alpha$. Puisque $f(x)=\langle x,u\rangle u$ et $g(x)=\langle x,v\rangle v$, on a $\operatorname{tr}(fg)=\langle u,v\rangle^2$. En développant $|f-g|^2$ on obtient $2-2\cos^2\alpha$, donc $|f-g|=\sqrt2\sin\alpha$.
![Deux droites engendrant un angle de 30 degrés et la projection du vecteur unitaire sur la première.](figures/angle-projections.svg)

### Question 6.a

On a alors $(f-g)f(x)=f(x)$, d’où $\|f(x)\|\le |f-g|\,\|f(x)\|$ par 2.b. Comme $|f-g|<1$, cela impose $f(x)=0$. Pour $y\in F\cap\ker g$, prendre $x=y$ donne $y=0$. La somme de $F$ et de $\ker g$ est donc directe.

### Question 6.b

L’injectivité de $g$ sur $F$ donne $\dim F\le\dim G$. La symétrie des rôles donne l’inégalité inverse et $G\cap\ker f=0$. Les rangs étant égaux, chacune des sommes directes $F\oplus\ker g$ et $G\oplus\ker f$ a dimension $n$. Chacune est égale à $E$.

### Question 6.c

Les deux images ont même dimension, un ou deux. Pour deux droites, 5 donne $|f-g|<1$ si et seulement si leur angle aigu (éventuellement nul) est inférieur à $\pi/4$. Pour deux plans, $|(I-f)-(I-g)|=|f-g|$, et l’angle des droites normales est l’angle aigu des plans. La même borne stricte de $45$ degrés vaut donc dans les deux cas.

### Question 7.a

Les projections sur deux droites perpendiculaires ont le même rang un et vérifient $|f-g|=\sqrt2$ par 5. L’inégalité stricte demandée ne découle donc pas de l’égalité des rangs.

### Question 7.b

Comme les dimensions de $F,G$ sont égales ainsi que celles de leurs orthogonaux, on peut apparier les vecteurs de ces bases en respectant les deux blocs. L’application $u$ correspondante est orthogonale. L’endomorphisme $ufu^{-1}$ est l’identité sur $G=u(F)$ et nul sur $G^\perp=u(F^\perp)$. Il est donc égal à $g$.

### Question 7.c

L’endomorphisme $a$ est nul sur $\ker f$ et transporte $F$ isométriquement sur $G$ par $u$. Son adjoint s’annule sur $\ker g$, puisque $u^{-1}(\ker g)=\ker f$. Sur $G$, $a^*$ est l’isométrie inverse $u^{-1}:G\to F$.

### Question 7.d

On obtient $a^*a=fu^{-1}uf=f^2=f$, tandis que $aa^*=uf^2u^{-1}=ufu^{-1}=g$. Chaque composition rend l’identité sur le sous-espace initial ou final approprié.

### Question 8.a

Posons $s=I-f+fgf$. Il est symétrique et $\langle sx,x\rangle=\|(I-f)x\|^2+\|gfx\|^2\le\|x\|^2$. Si cette forme est nulle, $x=fx\in F$ et $gx=0$. L’hypothèse $E=F\oplus\ker g$ entraîne $x=0$. Sur un vecteur propre unitaire, ces deux bornes montrent que la valeur propre appartient à $]0,1]$.

### Question 8.b

Le théorème spectral fournit une base orthonormale de vecteurs propres de $s$. Dans cette base, prenons pour $r$ la diagonale des $\sqrt\mu$ où $\mu>0$ parcourt la diagonale de $s$. Ainsi $r$ est symétrique, inversible, à valeurs propres positives et vérifie $r^2=s$.

### Question 8.c

**M′ seulement.** Si $t$ est symétrique à valeurs propres positives et $t^2=s$, alors $ts=st$. Sur chaque espace propre de $s$ pour $\mu$, la restriction de $t$ est symétrique de carré $\mu I$. Toute valeur propre de cette restriction est positive et vaut $\sqrt\mu$. Elle est donc scalaire sur cet espace. On retrouve exactement $r$, d’où l’unicité.

### Question 8.d

Sur $\ker f$, $s$ agit comme l’identité. La construction spectrale donne $r^{-1}x=x$ sur tout l’espace propre de $s$ pour $1$, donc sur $\ker f$. L’endomorphisme symétrique $r^{-1}$ préserve aussi son orthogonal $F$. Cette stabilité des deux blocs est exactement la commutation avec leur projecteur $f$.

### Question 8.e

Pour $b=gr^{-1}f$, on peut insérer $f$ de chaque côté de $g$ dans $b^*b$ en utilisant 8.d. Ainsi $b^*b=r^{-1}fgfr^{-1}=r^{-1}sfr^{-1}=f$. Cela donne $\|bx\|=\|fx\|$ et $b$ est nul sur $\ker f$, isométrique sur $F$. Par la somme directe de 8.a, $\dim F=\dim G$. Comme $b(F)\subseteq G$, on a $b(F)=G$. Sur $G$, $b^*$ agit par l’isométrie inverse et il s’annule sur $G^\perp$. Par conséquent $bb^*=g$.

## III. Distances extrémales et spectre du produit

### Question 9.a

Après complexification si nécessaire, si $fgx=\mu x$ avec $\mu\ne0$, alors $fx=x$. D’où $\mu\|x\|^2=\langle gx,x\rangle=\|gx\|^2$ (produit hermitien linéaire à gauche). Ainsi $\mu$ est réel et $0<\mu\le1$. La valeur éventuelle zéro appartient déjà au segment.

### Question 9.b

**M′ seulement.** Pour $u,v$ unitaires de produit scalaire $\sqrt\mu$, le produit des projections de 5 envoie $u$ sur $\langle u,v\rangle^2u=\mu u$. Ces vecteurs existent puisque $n\ge2$. Cela réalise chaque $\mu\in[0,1]$, extrémités comprises.

### Question 9.c

Puisque $f,g$ sont symétriques et idempotents, $|f-g|^2=\operatorname{tr}((f-g)^2)=\operatorname{tr}f+\operatorname{tr}g-2\operatorname{tr}(fg)=p+q-2\operatorname{tr}(fg)$.

### Question 9.d

En effet $(fg)^*=gf=fg$ et $(fg)^2=f^2g^2=fg$. Son image est incluse dans $F\cap G$, sur lequel il est l’identité. Son noyau est donc $(F\cap G)^\perp=F^\perp+G^\perp$. En posant $m=\dim(F\cap G)$, la valeur $1$ a multiplicité $m$ et $0$ a multiplicité $n-m$ (une multiplicité nulle signifie que la valeur est absente). Sa trace vaut $m$ et $|f-g|^2=p+q-2m$.

### Question 10.a

L’ensemble $\mathcal P_p$ est défini par $f=f^*$, $f^2=f$ et $\operatorname{tr}f=p$. Ces conditions continues donnent un fermé. Il est borné puisque $|f|=\sqrt p$. La dimension étant finie, il est compact, et les normes équivalentes de l’espace des endomorphismes définissent la même compacité.

### Question 10.b

Pour une base orthonormale de $F$ complétée à $E$, $\operatorname{tr}(fg)=\sum_{i=1}^p\|ge_i\|^2\le p$. Par symétrie, cette trace est aussi au plus $q$. Ainsi $\delta(f)\ge\sqrt{|p-q|}$. On atteint la borne en emboîtant les sous-espaces.
**Précision P′.** Si $p\le q$, le minimum vaut $\sqrt{q-p}$, atteint exactement pour $F\subseteq G$, ou $\ker g\subseteq\ker f$, puisque chaque terme de la somme doit valoir $1$. Si $q\le p$, il vaut $\sqrt{p-q}$ et il faut et suffit que $G\subseteq F$, ou $\ker f\subseteq\ker g$. L’inclusion des images implique la commutation dans les deux cas. Pour $p=q$ il faut $f=g$. La demande de minimum et de caractérisation est commune aux deux options.

### Question 10.c

La trace de $fg$ est positive ou nulle. Comme $\operatorname{tr}(f(I-g))\le n-q$, on a aussi $\operatorname{tr}(fg)\ge p+q-n$. La plus petite trace possible est donc au moins $m_0=\max(0,p+q-n)$. Elle est atteinte par des projections coordonnées en prenant le minimum de directions communes. Le maximum de $\delta$ vaut $\sqrt{p+q-2m_0}$.
Si $p+q\le n$, l’égalité exige et suffit que $F\subseteq G^\perp=\ker g$, soit $G\subseteq\ker f$, par la somme de carrés de 10.b. Si $p+q\ge n$, appliquer le même résultat aux complémentaires, car $|(I-f)-(I-g)|=|f-g|$. Il faut et suffit que $F^\perp\subseteq G$, ou $G^\perp\subseteq F$. Dans les deux configurations, $f$ et $g$ commutent et la dimension $m$ de 9.d vaut $m_0$. Le renvoi de l’imprimé à 9.c désigne cette définition de 9.d.

### Question 11.a

Écrivons désormais $F=\left(\begin{smallmatrix} A&B\\ C&D\end{smallmatrix}\right)$ pour la matrice de $f$. La symétrie exige $A=A^*$, $D=D^*$, $C=B^*$. Sous ces conditions, l’idempotence équivaut à $A^2+BB^*=A$, $AB+BD=B$ et $B^*B+D^2=D$. La quatrième équation est l’adjointe de celle du bloc supérieur droit. Ces relations sont nécessaires et suffisantes.

### Question 11.b

La matrice de $fg$ a pour blocs $(A,0;B^*,0)$, donc son polynôme caractéristique est $X^{n-q}\det(XI_q-A)$. Comme $A$ est symétrique, son spectre appartient à $\{0,1\}$ si et seulement si $A^2=A$. Par 11.a, cela équivaut à $BB^*=0$, soit $B=0$ car $\langle BB^*x,x\rangle=\|B^*x\|^2$. Dans ce cas les deux produits $fg,gf$ sont égaux, de blocs diagonaux $A,0$.

### Question 11.c

Non. Les cas d’égalité de 10.b et 10.c obligent à l’une des inclusions entre images ou orthogonaux qui y sont énoncées. Les projections correspondantes commutent. Cela couvre aussi les rangs nuls ou pleins, pour lesquels l’un des projecteurs est scalaire.

### Question 12.a

**M′ seulement.** Pour $0<q<n$, la condition est $Au=\mu u$, $B^*u=\mu v$. Si $\mu\ne0$, tout vecteur propre est de la forme $(u,\mu^{-1}B^*u)$ pour un vecteur propre non nul de $A$. Si $\mu=0$, $u\in\ker A$ implique $\|B^*u\|^2=\langle(A-A^2)u,u\rangle=0$. Ainsi $\ker(fg)=\ker A\oplus\ker g$ dans cette décomposition. Les vecteurs propres pour zéro en sont les éléments non nuls. Si $q=0$ le produit est nul. Si $q=n$, il est $f$, dont les espaces propres sont connus.

### Question 12.b

**M′ seulement.** Prenons une base propre de $A$. Pour chaque vecteur associé à une valeur non nulle, utilisons le relèvement de 12.a. Pour chaque vecteur $u\in\ker A$ de la base, prenons $(u,0)$. Les premières composantes constituent la base de $\operatorname{Im}g$, et l’ajout d’une base de $\ker g$ donne $n$ vecteurs propres indépendants de $fg$. Ainsi $fg$ est diagonalisable sur $\mathbb R$ pour tous les rangs, y compris les cas $q=0,n$.
