# X-ENS MP — Mathématiques A 2021 · Corrigé guidé

*Corrigé rédigé par IA, non officiel. Signalez toute erreur.*

**Rédaction** · modèle exact non renseigné (famille GPT-6) · effort non renseigné · vitesse non renseignée

**Révision** · modèle exact non renseigné (famille GPT-6) · effort non renseigné · vitesse non renseignée

**Révision (tour 2)** · GPT-6.2 Astra Ultra · vitesse non renseignée

**Révision (tour 3)** · GPT-6.2 Astra Ultra · vitesse non renseignée · 26 novembre 2026

## Présentation du sujet

L’épreuve du 12 avril 2021 dure quatre heures. Elle étudie les sous-groupes finis de matrices entières inversibles sur les entiers. Elle aboutit à une borne sur leur cardinal qui dépend de la dimension et à une meilleure borne pour les groupes de cardinal une puissance première. [Sujet officiel](https://banques-ecoles.fr/cms/wp-content/uploads/2021/07/2021_MP_sujet_MathA.pdf)

> [!JURY]
> Le jury demande que chaque réutilisation d’un résultat antérieur identifie précisément la question et le résultat. Il signale aussi une confusion fréquente entre un déterminant entier non nul et un déterminant égal à 1 ou à −1, condition caractérisant ici un inverse entier. [Rapport officiel](https://banques-ecoles.fr/cms/wp-content/uploads/2021/10/21_MP_rap_eMathA.pdf)

## Préliminaires

Spectre des matrices de torsion et dénombrement des multiples d’une puissance première.

### Question P.1

> [!INDICATION]
> Écrire la définition d’une racine de l’unité et prendre les modules.

> [!INDICATION]
> Quelle puissance d’un réel positif peut être égale à un ?

#### Solution

Si $z^d=1$ pour un entier $d\ge1$, alors $|z|^d=1$. L’unique réel positif ayant cette puissance égale à un est $1$, donc $|z|=1$.

### Question P.2

> [!INDICATION]
> Chercher un polynôme annulateur à partir de l’ordre de g.

> [!INDICATION]
> Vérifier que ses racines sont simples avant de conclure sur la diagonalisation.

#### Solution

L’égalité $g^d=I_n$ fait de $X^d-1$ un polynôme annulateur. Ses racines complexes sont simples : une racine commune avec $dX^{d-1}$ serait nulle, or $0^d-1=-1$. Il est scindé à racines simples sur $\mathbb C$, donc $g$ est diagonalisable et chacune de ses valeurs propres est une racine $d$-ième de l’unité.

### Question P.3a

> [!INDICATION]
> Écrire un multiple positif sous la forme k=qj.

> [!INDICATION]
> Quelles sont les valeurs extrêmes possibles de j ?

#### Solution

Les multiples positifs de $q$ au plus égaux à $m$ sont $q,2q,\ldots,\lfloor m/q\rfloor q$. Il y en a $\lfloor m/q\rfloor$, et ce nombre vaut zéro si $m<q$.

### Question P.3b

> [!INDICATION]
> Écrire chaque valuation comme un nombre de puissances qui divisent le facteur.

> [!INDICATION]
> Compter à nouveau après avoir échangé l’ordre des deux sommes.

#### Solution

Pour $q$ premier, chaque entier $k$ de $1$ à $m$ contribue une unité à $v_q(m!)$ pour chaque puissance $q^i$, $i\ge1$, qui le divise. En comptant d’abord par puissance et en utilisant 3a,
$$v_q(m!)=\sum_{i\ge1}\#\{1\le k\le m:q^i\mid k\}=\sum_{i\ge1}\left\lfloor\frac m{q^i}\right\rfloor.$$
La somme est finie puisque tous les termes avec $q^i>m$ sont nuls. Pour $m=0$ elle vaut aussi zéro.

![Figure 1 — Dans 18 !, six facteurs multiples de 3 et deux multiples de 9 donnent une valuation en 3 égale à huit.](figures/valuation-factorielle.svg)

## I — Éléments d’ordre fini

Les polynômes caractéristiques entiers à racines de module un forment, en degré fixé, une famille finie.

### Question I.1

> [!INDICATION]
> Exprimer la trace à l’aide des deux valeurs propres.

> [!INDICATION]
> La norme du nombre complexe qui est leur somme se majore par la somme de deux modules.

#### Solution

La trace est la somme des deux valeurs propres comptées avec multiplicité. D’après les préliminaires 1 et 2, celles-ci ont module un. L’inégalité triangulaire donne $|\operatorname{Tr}g|\le2$.

### Question I.2

> [!INDICATION]
> Déterminer les racines réelles de l’unité.

> [!INDICATION]
> Utiliser la diagonalisabilité pour remonter des valeurs propres aux puissances de la matrice.

#### Solution

Une racine de l’unité réelle vaut $1$ ou $-1$. Comme $g$ est diagonalisable, $g^2=I_2$ ; l’ordre vaut $1$ si les deux valeurs propres sont $1$, et $2$ dès que $-1$ figure au spectre. Les matrices $I_2$ et $-I_2$ réalisent ces deux possibilités.

### Question I.3

> [!INDICATION]
> Le polynôme caractéristique a des coefficients réels et ses deux racines ne sont pas réelles.

> [!INDICATION]
> La trace de la matrice est entière. Le produit des deux valeurs propres conjuguées est un module au carré.

#### Solution

Le polynôme caractéristique a des coefficients entiers, donc ses deux racines non réelles sont conjuguées. Leur produit est $|z|^2=1$ et la trace $2\Re z$ est un entier strictement entre $-2$ et $2$, car $z\ne\pm1$. Le polynôme $X^2-(\operatorname{Tr}g)X+1$ vaut ainsi $X^2+X+1$, $X^2+1$ ou $X^2-X+1$.

### Question I.4

> [!INDICATION]
> Reconnaître les racines des polynômes de la question précédente dans des factorisations de puissances.

> [!INDICATION]
> L’ordre d’une matrice diagonalisable doit convenir à toutes ses valeurs propres.

#### Solution

Les trois polynômes précédents ont respectivement pour racines les racines primitives d’ordres $3$, $4$ et $6$, comme le montrent les factorisations de $X^3-1$, $X^4-1$ et $X^3+1$. Une matrice diagonalisable a pour ordre le PPCM des ordres de ses valeurs propres. Avec la question 2 on trouve $d\in\{1,2,3,4,6\}$. Les trois cas non réels sont réalisés, si on le souhaite, par les matrices $\bigl(\begin{smallmatrix}0&-1\\1&t\end{smallmatrix}\bigr)$ pour $t=-1,0,1$.

![Figure 2 — Les deux racines conjuguées non réelles sont à l’abscisse moitié de la trace. Leurs ordres valent trois, quatre ou six.](figures/spectres-en-dimension-deux.svg)

### Question I.5

> [!INDICATION]
> Développer le produit des facteurs de degré un.

> [!INDICATION]
> Combien de produits de n−i racines entrent dans le coefficient d’indice i ?

#### Solution

Dans $P=\prod_{j=1}^n(X-z_j)$, le coefficient de $X^i$ est la somme, au signe $(-1)^{n-i}$ près, des produits de $n-i$ racines prises à des indices distincts. Il y a $\binom n{n-i}=\binom ni$ termes, chacun de module au plus $\alpha^{n-i}$. L’inégalité triangulaire fournit la borne.

### Question I.6

> [!INDICATION]
> Combiner le caractère entier des coefficients et leur borne numérique.

> [!INDICATION]
> Une boîte bornée ne contient qu’un nombre fini de points à coordonnées entières.

#### Solution

Chaque $\chi_g$ est unitaire de degré $n$ à coefficients entiers. Pour $g$ d’ordre fini, toutes ses racines sont de module un. La question 5 donne pour son coefficient d’indice $i$ un entier de l’intervalle $[-\binom ni,\binom ni]$. Le produit, sur les $n$ indices, des nombres finis de choix reste fini.

### Question I.7

> [!INDICATION]
> Réunir les racines des polynômes effectivement obtenus à la question précédente.

> [!INDICATION]
> Le PPCM de leurs ordres fournit une puissance commune à toutes les matrices étudiées.

#### Solution

La réunion des racines de tous les polynômes caractéristiques effectivement obtenus en 6 est un ensemble fini de racines de l’unité. Soit $D$ le PPCM de leurs ordres. Pour toute matrice d’ordre fini, chacune des valeurs propres élevée à $D$ vaut un. La diagonalisabilité de la matrice donne $g^D=I_n$. Son ordre divise donc $D$ et il n’y a qu’un nombre fini de possibilités.

## II — Sous-groupes finis

La réduction modulo trois distingue les éléments de tout sous-groupe fini sans distinguer toutes les matrices entières entre elles.

### Question II.1a

> [!INDICATION]
> Exprimer A dans une base de diagonalisation de g.

> [!INDICATION]
> Quelle est la plus grande distance entre un point du cercle unité et le point 1 ?

#### Solution

Si $g=S\operatorname{diag}(\zeta_j)S^{-1}$, alors $A=(g-I_n)/m$ est diagonalisée par la même base et a pour valeurs propres $(\zeta_j-1)/m$. Chacune a pour module au plus $2/m<1$ puisque $m\ge3$. Le seuil est exact : pour $m=2$, $g=-I_n$ vérifie $g\equiv I_n\pmod2$ avec $g\ne I_n$ et $A=-I_n$. Ses puissances gardent une valeur propre de module un.

![Figure 3 — Les valeurs propres de la matrice divisée sont sur le petit cercle de diamètre deux tiers. Leur module est strictement inférieur à un.](figures/spectre-matrice-divisee.svg)

### Question II.1b

> [!INDICATION]
> Étudier les puissances de la matrice dans la base de diagonalisation.

> [!INDICATION]
> Revenir dans la base initiale, où les coefficients sont des entiers.

#### Solution

Les puissances de chaque valeur propre de $A$ tendent vers zéro. Conjuguer les puissances de la matrice diagonale montre donc que $A^k$ tend coefficient par coefficient vers zéro. Or $A$, et donc $A^k$, est à coefficients entiers. Pour $k$ assez grand, tous les $n^2$ coefficients sont simultanément de module strictement inférieur à un, donc nuls.

### Question II.1c

> [!INDICATION]
> Une matrice nilpotente diagonalisable a quelle forme diagonale ?

> [!INDICATION]
> Revenir ensuite à la définition de A.

#### Solution

La nilpotence impose que toutes les valeurs propres de $A$ soient nulles. Comme $A$ est aussi diagonalisable d’après 1a, elle est nulle. D’où $g=I_n+mA=I_n$.

### Question II.2a

> [!INDICATION]
> Si deux réductions sont égales, former un quotient des deux éléments du groupe.

> [!INDICATION]
> L’inverse de tout élément considéré a lui aussi des coefficients entiers.

#### Solution

La réduction des coefficients respecte les produits et envoie les inverses entiers sur des inverses modulo $m$. Si $g,h\in G$ ont la même réduction, $h^{-1}g$ est congru à $I_n$ modulo $m$. Cet élément appartient à un groupe fini et a donc un ordre fini. La question 1c appliquée à $h^{-1}g$ donne $g=h$, d’où l’injectivité.

### Question II.2b

> [!INDICATION]
> Choisir la plus petite valeur autorisée de m.

> [!INDICATION]
> Compter les possibilités pour les n² coefficients de la matrice réduite.

#### Solution

Choisir $m=3$. Il existe exactement $3^{n^2}$ matrices $n\times n$ modulo trois puisque leurs $n^2$ coefficients ont chacun trois choix. L’injection de 2a donne $|G|\le3^{n^2}$.

## III — Traces des éléments d’un p-sous-groupe

On suit la trace sous les puissances premières, d’abord modulo le premier, puis en égalité entière lorsque le premier est grand.

### Question III.1a

> [!INDICATION]
> Multiplier le coefficient binomial par son indice inférieur.

> [!INDICATION]
> Appliquer le lemme de Gauss au produit obtenu.

#### Solution

Pour $1\le k\le\ell-1$, $k\binom\ell k=\ell\binom{\ell-1}{k-1}$. Comme $k$ et le premier $\ell$ sont premiers entre eux, le lemme de Gauss donne $\ell\mid\binom\ell k$.

### Question III.1b

> [!INDICATION]
> Quelles hypothèses de la formule du binôme sont nécessaires dans un anneau quelconque ?

> [!INDICATION]
> Distinguer les deux termes extrêmes des termes intermédiaires.

#### Solution

L’hypothèse $xy=yx$ autorise la formule du binôme, même dans un anneau non commutatif. Les deux termes extrêmes sont $x^\ell$ et $y^\ell$. Tous les coefficients intermédiaires sont multiples de $\ell$ d’après 1a, donc leur somme appartient à $\ell R$.

### Question III.2

> [!INDICATION]
> Passer dans l’anneau quotient par l’idéal.

> [!INDICATION]
> Le déterminant est un polynôme à coefficients entiers des entrées de la matrice.

#### Solution

Réduisons les coefficients dans $R/I$. Les images de $A+B$ et de $A$ sont égales. La formule du déterminant comme somme signée de produits commute à cette réduction. On obtient l’égalité des deux déterminants modulo $I$, soit $\det(A+B)-\det A\in I$.

### Question III.3

> [!INDICATION]
> Réduire modulo ℓ et appliquer la formule de la question 1b aux monômes.

> [!INDICATION]
> Le petit théorème de Fermat simplifie la puissance du coefficient de chaque monôme.

#### Solution

Écrivons $P=\sum a_i X^i$. Par 1b, appliquée successivement aux monômes dans l’anneau commutatif $(\mathbb Z/\ell\mathbb Z)[X]$, $P(X)^\ell\equiv\sum a_i^\ell X^{i\ell}$. Le petit théorème de Fermat donne $a_i^\ell\equiv a_i\pmod\ell$, même si $\ell\mid a_i$. Le membre droit est donc $P(X^\ell)$ modulo $\ell$.

### Question III.4a

> [!INDICATION]
> Une matrice scalaire commute avec M même dans un anneau de matrices.

> [!INDICATION]
> Examiner séparément la parité du premier ℓ pour le signe du dernier terme.

#### Solution

Les matrices $XI_n$ et $-M$ commutent dans $M_n(\mathbb Z[X])$. La question 1b donne $(XI_n-M)^\ell\equiv X^\ell I_n+(-1)^\ell M^\ell$ modulo $\ell$. Pour $\ell$ impair on a $(-1)^\ell=-1$ ; pour $\ell=2$, $1\equiv-1\pmod 2$. Dans les deux cas chaque coefficient de la différence demandée est divisible par $\ell$, ce qui définit $A$ sur $\mathbb Z[X]$.

### Question III.4b

> [!INDICATION]
> Prendre le déterminant après réduction des coefficients.

> [!INDICATION]
> Identifier séparément le déterminant d’une puissance et celui d’un polynôme caractéristique évalué en une puissance de X.

#### Solution

Prendre le déterminant des deux matrices congrues en 4a et appliquer 2 avec l’idéal $\ell\mathbb Z[X]$. Par multiplicativité, le premier déterminant vaut $\chi_M(X)^\ell$, et le second $\det(X^\ell I_n-M^\ell)=\chi_{M^\ell}(X^\ell)$. Leur différence appartient à l’idéal.

### Question III.4c

> [!INDICATION]
> Faire intervenir la question 3 pour retrouver la même substitution dans les deux caractéristiques.

> [!INDICATION]
> Le coefficient immédiatement sous le terme dominant d’un polynôme caractéristique donne la trace au signe près.

#### Solution

Appliquer 3 à $P=\chi_M$ puis 4b : $\chi_{M^\ell}(X^\ell)\equiv\chi_M(X^\ell)\pmod\ell$. Dans chacun de ces polynômes, le coefficient de $X^{\ell(n-1)}$ est l’opposé de la trace de la matrice correspondante. La comparaison donne $\operatorname{Tr}(M^\ell)\equiv\operatorname{Tr}M\pmod\ell$.

### Question III.5

> [!INDICATION]
> L’ordre d’un élément divise le cardinal du groupe fini.

> [!INDICATION]
> Comparer successivement les puissances d’exposants 1, p, p², jusqu’à celle qui vaut l’identité.

#### Solution

L’ordre de $g$ divise $p^r=|G|$. Appliquer la congruence de 4c, avec $\ell=p$, à $g,g^p,\ldots,g^{p^{r-1}}$. Toutes les traces sont congrues à celle de $g^{p^r}=I_n$, donc à $n$ modulo $p$.

### Question III.6

> [!INDICATION]
> Majorer le module de chaque trace par n en utilisant le spectre.

> [!INDICATION]
> Combien de multiples du premier ℓ peuvent subsister dans l’intervalle obtenu ?

#### Solution

Les traces entières de $g$ et $g^\ell$ ont chacune pour module au plus $n$ par l’inégalité triangulaire appliquée aux valeurs propres de module un. Leur différence, multiple de $\ell$ par 4c, a donc un module au plus $2n<\ell$. Ce multiple est nécessairement nul.

### Question III.7a

> [!INDICATION]
> Tester un premier q inférieur ou égal à 2n et distinguer les cas où il divise k et où il ne le divise pas.

> [!INDICATION]
> Si q divise k, il est différent de p et absent du produit ajouté.

#### Solution

Soit $q\le2n$ un nombre premier. Si $q$ ne divise pas $k$, il figure dans le produit définissant $m$ et $m\equiv k\not\equiv0\pmod q$. Si $q\mid k$, alors $q\ne p$ puisque $p\nmid k$ et $q$ ne figure pas dans ce produit. L’additif $p^r\prod\ell$ est donc premier à $q$, ce qui interdit encore $q\mid m$. Ainsi tous les facteurs premiers de $m$ dépassent $2n$. Par exemple, pour $n=2$, prenons le groupe d’ordre $3$ engendré par la matrice de trace $-1$ construite en I.4. Avec $p=3$, $r=1$ et $k=2$, les petits premiers sont $2,3$ et seul $3$ intervient dans le produit. On obtient $m=2+3\cdot3=11>2n$. Dans ce groupe, $g^{11}=g^2$ car $g^3=I_2$ et les exposants diffèrent de $9$.

### Question III.7b

> [!INDICATION]
> Comparer les puissances de g d’exposants m et k.

> [!INDICATION]
> Décomposer m en facteurs premiers et appliquer la question 6 plusieurs fois.

#### Solution

Comme $m\equiv k\pmod{p^r}$ et $g^{p^r}=I_n$, on a $g^k=g^m$. Décomposer $m$ en facteurs premiers. Chacun est supérieur à $2n$ d’après 7a ; élever un élément de $G$ à l’un de ces facteurs conserve sa trace par 6. Une application successive donne $\operatorname{Tr}(g^k)=\operatorname{Tr}(g^m)=\operatorname{Tr}g$.

### Question III.8a

> [!INDICATION]
> Faire la division euclidienne par p.

> [!INDICATION]
> Le reste ne peut pas être nul et le quotient a une borne supérieure explicite.

#### Solution

Tout $k$ entre $1$ et $p^r-1$ non divisible par $p$ s’écrit de façon unique $k=ps+t$ par division euclidienne, avec $1\le t\le p-1$ et $0\le s\le p^{r-1}-1$. Réciproquement, tout nombre de cette forme appartient à $J_r$. L’union proposée est même disjointe et $|J_r|=p^{r-1}(p-1)$.

### Question III.8b

> [!INDICATION]
> Transformer la somme à l’aide du quotient et du reste obtenus en 8a.

> [!INDICATION]
> Le premier facteur est une somme géométrique de raison ζ à la puissance p.

#### Solution

La décomposition de 8a donne
$$\sum_{j\in J_r}\zeta^j=\left(\sum_{s=0}^{p^{r-1}-1}(\zeta^p)^s\right)\left(\sum_{t=1}^{p-1}\zeta^t\right).$$
Si $\zeta=1$, on obtient $p^{r-1}(p-1)$. Si son ordre est $p$, le premier facteur vaut $p^{r-1}$ et le second $-1$ par somme géométrique. Si son ordre divise $p^r$ et dépasse $p$, $\zeta^p\ne1$ et $(\zeta^p)^{p^{r-1}}=1$ ; le premier facteur est nul.

![Figure 4 — Pour p = 3 et r = 2, les six contributions s’annulent quand la racine est d’ordre neuf. Quand elle est d’ordre trois, elles donnent moins trois.](figures/sommes-des-racines.svg)

### Question III.9

> [!INDICATION]
> Additionner les traces de toutes les puissances indexées par les entiers premiers à p du bloc considéré.

> [!INDICATION]
> Intervertir ensuite la somme sur les indices et celle sur les valeurs propres.

#### Solution

Sommons $\operatorname{Tr}(g^j)$ pour $j\in J_r$. La question 7b donne $p^{r-1}(p-1)\operatorname{Tr}g$. En diagonalisant $g$, chaque valeur propre $\zeta$ contribue la somme de 8b. Les $n_0$ valeurs propres égales à un contribuent $n_0p^{r-1}(p-1)$, les $n_1$ valeurs propres d’ordre $p$ contribuent $-n_1p^{r-1}$ et les autres rien. Après division,
$$\operatorname{Tr}g=n_0-\frac{n_1}{p-1}.$$

### Question III.10

> [!INDICATION]
> La congruence de la question 5 fixe le pas entre deux traces possibles.

> [!INDICATION]
> La question 9 donne une meilleure borne inférieure que la seule borne en module par n.

#### Solution

D’après 5, $v=(n-\operatorname{Tr}g)/p$ est entier. Il est positif ou nul car $\operatorname{Tr}g\le n$. La question 9 donne $\operatorname{Tr}g\ge-n/(p-1)$ puisque $n_0\ge0$ et $n_1\le n$. Il en résulte $v\le(n+n/(p-1))/p=n/(p-1)$. Ainsi $\operatorname{Tr}g=n-pv$ avec $0\le v\le\lfloor n/(p-1)\rfloor$.

![Figure 5 — Pour n = 7 et p = 3, le raisonnement impose que la trace appartienne à une progression finie de quatre entiers.](figures/traces-admissibles.svg)

## IV — Cardinaux des p-sous-groupes

Le projecteur moyen donne une divisibilité de la somme des traces. Les puissances tensorielles la transportent à tous les monômes, puis un polynôme isole l’identité.

### Question IV.1a

> [!INDICATION]
> Multiplier la moyenne à gauche par un élément fixé de G.

> [!INDICATION]
> Établir les deux inclusions pour l’image, puis utiliser l’action de la moyenne sur cette image.

#### Solution

Posons $W=\{x\in\mathbb C^n:\forall g\in G,\ gx=x\}$. Pour $h\in G$, la multiplication $g\mapsto hg$ permute les éléments du groupe, donc $hf=f$. Ainsi $\operatorname{Im} f\subset W$. Réciproquement, si $x\in W$, chaque terme de la moyenne définissant $f(x)$ est égal à $x$, donc $f(x)=x$. Cela donne $\operatorname{Im}f=W$, et en appliquant cette identité à tout $f(x)\in W$ on obtient $f^2=f$. Il s’agit bien d’un projecteur sur $W$.

### Question IV.1b

> [!INDICATION]
> Quelle est la trace d’un projecteur de rang donné ?

> [!INDICATION]
> Revenir à la définition de la moyenne sur le groupe.

#### Solution

Un projecteur est diagonalisable avec des valeurs propres parmi $0,1$ et sa trace est son rang entier. Par linéarité, $\sum_{g\in G}\operatorname{Tr}g=|G|\operatorname{Tr}f=|G|\dim W$ est un entier divisible par $|G|$.

### Question IV.2i

> [!INDICATION]
> Repérer les blocs diagonaux du produit tensoriel.

> [!INDICATION]
> Additionner leurs traces.

#### Solution

Les blocs diagonaux de $g\otimes h$ sont les $g_{ii}h$. Additionner leurs traces donne $\operatorname{Tr}(g\otimes h)=\sum_i g_{ii}\operatorname{Tr}h=(\operatorname{Tr}g)(\operatorname{Tr}h)$.

### Question IV.2ii

> [!INDICATION]
> Écrire le bloc (i,j) du produit matriciel par blocs.

> [!INDICATION]
> Les coefficients de g et g′ sont des scalaires, qui peuvent sortir des produits.

#### Solution

Le bloc en position $(i,j)$ du produit $(g\otimes h)(g'\otimes h')$ vaut $\sum_k(g_{ik}h)(g'_{kj}h')=(gg')_{ij}\,hh'$. C’est le bloc correspondant de $(gg')\otimes(hh')$.

### Question IV.2iii

> [!INDICATION]
> Tester le produit tensoriel des deux inverses.

> [!INDICATION]
> Appliquer le calcul précédent dans les deux ordres.

#### Solution

En prenant $g'=g^{-1}$ et $h'=h^{-1}$ dans ii, on obtient $(g\otimes h)(g^{-1}\otimes h^{-1})=I_n\otimes I_k=I_{nk}$. Le produit dans l’ordre inverse donne aussi $I_{nk}$. Le produit tensoriel est donc inversible et son inverse est celui annoncé.

### Question IV.3a

> [!INDICATION]
> Fixer un antécédent si la fibre est non vide.

> [!INDICATION]
> À quelle condition le quotient de deux éléments appartient-il au noyau ?

#### Solution

Si $\gamma'$ est hors de l’image de $\varphi$, sa fibre est vide. Sinon, choisir $\gamma$ dans cette fibre. Pour $x\in\Gamma$, l’égalité $\varphi(x)=\gamma'$ équivaut à $\varphi(\gamma^{-1}x)=e'$, soit $\gamma^{-1}x\in H$. La fibre est exactement $\gamma H$.

### Question IV.3b

> [!INDICATION]
> Décomposer le groupe source en fibres disjointes.

> [!INDICATION]
> Utiliser une multiplication par un élément fixé pour compter le cardinal de chaque fibre.

#### Solution

Toute fibre non vide a $|H|$ éléments par la bijection $h\mapsto\gamma h$. Comme les fibres partitionnent $\Gamma$ et sont indexées, lorsqu’elles sont non vides, par $\varphi(\Gamma)$, on trouve $|\Gamma|=|\varphi(\Gamma)|\,|H|$.

### Question IV.4a

> [!INDICATION]
> Faire une récurrence simultanément pour les produits et pour les traces.

> [!INDICATION]
> Sommer par fibres dans l’image du morphisme restreint à G.

#### Solution

Par récurrence sur $s$, 2ii montre que $(gh)^{(s)}=g^{(s)}h^{(s)}$. L’identité se conserve et 2iii garantit l’inversibilité, donc $\varphi_s$ est un morphisme. La formule de 2i donne de même $\operatorname{Tr}(g^{(s)})=(\operatorname{Tr}g)^s$. En regroupant les termes selon les fibres du morphisme restreint à $G$, toutes de taille $|G\cap\ker\varphi_s|$ par 3a, on obtient
$$\sum_{g\in G}(\operatorname{Tr}g)^s=|G\cap\ker\varphi_s|\sum_{h\in\varphi_s(G)}\operatorname{Tr}h.$$

### Question IV.4b

> [!INDICATION]
> Appliquer le résultat sur la moyenne au groupe image.

> [!INDICATION]
> Relier le cardinal de l’image à celui du noyau de la restriction.

#### Solution

Le groupe $\varphi_s(G)$ est un sous-groupe fini de $\mathrm{GL}_{n^s}(\mathbb C)$. Par 1b, la somme de ses traces est un multiple entier de $|\varphi_s(G)|$. Or $|G\cap\ker\varphi_s|\cdot|\varphi_s(G)|=|G|$ par 3b. La somme des puissances considérée est donc un multiple entier de $|G|$. Pour $s=0$, on a directement $\sum_{g\in G}1=|G|$. Le facteur de taille des fibres peut être indispensable. Pour $G=\{I_n,-I_n\}$ et $s=2$, les deux matrices ont la même image $I_{n^2}$. La somme des carrés des traces initiales vaut bien $2n^2$ et la somme des traces dans l’image vaut $n^2$.

### Question IV.5a

> [!INDICATION]
> Évaluer le polynôme de l’énoncé sur toutes les traces et exploiter sa décomposition en monômes entiers.

> [!INDICATION]
> Justifier que seule l’identité a la trace n avant de simplifier la somme.

#### Solution

Comme $P\in\mathbb Z[X]$, la question 4b appliquée à chaque monôme (et la remarque sur le terme constant) montre que $|G|$ divise $\sum_{g\in G}P(\operatorname{Tr}g)$. D’après III.10, les traces autres que $n$ sont des racines de $P$. Si $\operatorname{Tr}g=n$, les $n$ valeurs propres de module un ont toutes partie réelle au plus un et leur somme a partie réelle $n$. Elles valent donc toutes un. La diagonalisabilité impose alors $g=I_n$. La somme vaut exactement $P(n)$ et $|G|\mid P(n)$. Si $a=0$, le produit vide vaut un et le raisonnement exclut tout sous-groupe non trivial.

### Question IV.5b

> [!INDICATION]
> Calculer chacun des facteurs de P(n).

> [!INDICATION]
> Pour convertir la divisibilité par le cardinal du groupe en inégalité sur r, prendre la valuation.

#### Solution

On a $P(n)=\prod_{j=1}^a(n-(n-pj))=p^a a!$. Comme $p^r\mid P(n)$, prendre la valuation en $p$ donne $r\le a+v_p(a!)$.

Pour $n=7$ et $p=3$, la borne donne $r\le3+v_3(3!)=4$. Elle est atteinte. Soit $C=\bigl(\begin{smallmatrix}0&-1\\1&-1\end{smallmatrix}\bigr)$, de polynôme caractéristique $X^2+X+1$ et d’ordre trois. Dans trois plans de coordonnées indépendants, les matrices $\operatorname{diag}(C^i,C^j,C^k,1)$ forment un sous-groupe $D$ d’ordre $27$, avec $0\le i,j,k<3$. Soit $T$ la matrice qui permute cycliquement les trois plans en respectant leurs bases et fixe le septième vecteur. Elle normalise $D$ en permutant ses trois exposants. Ni $T$ ni $T^2$ ne préserve chaque plan, donc les trois classes $D,DT,DT^2$ sont disjointes. Leur réunion est le groupe engendré par $D$ et $T$, de cardinal $81$. Les quatre traces de III.10 se lisent déjà sur $D$ : chaque bloc $C$ ou $C^2$ remplace une trace $2$ par $-1$, ce qui enlève trois.

![Figure — En dimension sept, trois blocs entiers d’ordre trois et une permutation cyclique des blocs engendrent un groupe d’ordre 81.](figures/groupe-ordre-81.svg)

### Question IV.6a

> [!INDICATION]
> Majorer chacune des parties entières de la formule de Legendre par son argument.

> [!INDICATION]
> Utiliser la somme d’une série géométrique puis la définition de a.

#### Solution

La formule des préliminaires donne $v_p(a!)\le\sum_{j\ge1}a/p^j=a/(p-1)$. Ainsi $r\le pa/(p-1)$. Or $a=\lfloor n/(p-1)\rfloor\le n/(p-1)$ ; il vient $r\le pn/(p-1)^2$.

### Question IV.6b

> [!INDICATION]
> Prendre les logarithmes et isoler une fonction réelle du premier p.

> [!INDICATION]
> Étudier sa décroissance pour x au moins 2 et calculer sa valeur en 2.

#### Solution

Il suffit de majorer $\log |G|=r\log p$ par $n\log4$. Pour $x\ge2$, posons $H(x)=x\log x/(x-1)^2$. Sa dérivée a le signe de $(x-1)-(x+1)\log x$. Comme $\log x=\int_1^x\mathrm dt/t\ge(x-1)/x$ pour $x\ge1$, ce numérateur est strictement négatif pour $x>1$. Ainsi $H(p)\le H(2)=2\log2=\log4$. En utilisant 6a, on trouve $\log|G|\le nH(p)\le n\log4$, d’où $|G|\le4^n$.

![Figure 6 — Parmi les premiers, la valeur maximale de la majoration logarithmique est atteinte au premier deux.](figures/majoration-des-cardinaux.svg)

## Bilan

La réduction modulo trois donne une borne générale en comptant des matrices. Pour un groupe de cardinal une puissance première, la trace prend peu de valeurs. La moyenne sur les puissances tensorielles transforme cette contrainte spectrale en une divisibilité sur le cardinal du groupe.
