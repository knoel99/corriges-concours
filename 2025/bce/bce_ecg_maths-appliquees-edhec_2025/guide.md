# BCE ECG — Mathématiques appliquées (EDHEC) 2025 · Corrigé guidé

*Corrigé rédigé par IA, non officiel. Signalez toute erreur.*

## Présentation du sujet

**Cadre.** Épreuve de mathématiques appliquées conçue par l'EDHEC (code sujet 298), 4 heures, calculatrice interdite. Le format est celui, très stable, de l'EDHEC : trois exercices et un problème, soit 58 questions courtes. D'après le rapport 2025, 3 878 candidats ont composé, avec une moyenne de 10,42 et un écart type de 6,07.

**Exercice 1 (analyse, 14 questions).** Suite implicite : $u_n$ est l'unique solution dans $[0,1]$ de $f_n(x)=1$, où $f_n(x)=\sum_{k=1}^nk\,x^k$.

On montre que $(u_n)$ décroît, on obtient une forme close de $f_n$ par dérivation de la somme géométrique, puis la limite $\ell=\frac{3-\sqrt5}{2}$.

**Exercice 2 (algèbre linéaire, 12 questions).** Sous-espace $E$ de $\mathcal M_3(\mathbb{R})$ de dimension 2, formé de matrices symétriques non inversibles. Diagonalisation d'un exemple $A$, puis observation que les mêmes vecteurs propres diagonalisent toute la famille $E$ ; trois questions de Python (une matrice, un rang, une puissance).

**Exercice 3 (probabilités à densité, 12 questions).** Une famille de densités $f_n$ sur $[0,n]$ ; espérance et variance par un changement de point de vue ($1-\frac{X_n}{n}$), fonction de répartition, convergence en loi vers $\mathcal E(1)$, puis réalisation de $X_n$ comme $n\min(U_1,\dots,U_n)$.

**Problème (probabilités discrètes et analyse, 20 questions).** On choisit une urne parmi $n+1$ (l'urne $k$ contient $k-1$ noires sur $n$ boules), puis on tire avec remise jusqu'à la première blanche.

Loi du rang $X_n$ par la formule des probabilités totales, sommes télescopiques, espérance $\frac{n}{n+1}\sum_{p=1}^n\frac1p$, et son équivalent $\ln n$ par comparaison série-intégrale.

**Notions mobilisées.** Théorème de la bijection, suites monotones, sommes géométriques et leurs dérivées, croissances comparées, équivalents ; sous-espaces vectoriels, bases, matrices symétriques, valeurs et vecteurs propres, théorème du rang ; densités, théorème de transfert, fonction de répartition, convergence en loi, minimum de variables indépendantes ; probabilités totales, loi géométrique, séries télescopiques et géométriques dérivées ; `numpy`, `numpy.linalg`, `numpy.random`.

**Difficulté.** Sujet long mais très guidé, où presque chaque question se traite en quelques lignes. Le rapport 2025 juge le problème et l'exercice 3 les moins bien réussis, et l'exercice 2 le mieux réussi. La difficulté est dans la rigueur : bien distinguer suite et fonction, vecteur et sous-espace, existence et calcul d'une espérance.

**Questions à ne pas laisser passer.** Ex. 1 : 1), 2) a), 3) a), 4) a). Ex. 2 : 1), 3), 4), 5) a) b), 7) a). Ex. 3 : 1), 3), 4) a), 5) a). Problème : 1), 2), 4), 7) a), 9) a) b) c).

**Gestion du temps.** Environ 50 minutes par exercice et 1 h 20 pour le problème. Le rapport le dit sans détour : « Dans la pratique, il ne faut pas rester plus de 4 ou 5 minutes sur une question, sauf pour terminer un long calcul. »

---

## Exercice 1 — Une suite définie implicitement

On étudie la fonction $f_n$ pour définir $u_n$, puis on compare $u_n$ et $u_{n+1}$ par les variations de $f_{n+1}$, et l'on obtient la limite grâce à une forme close de $f_n$.

### Question 1) a)

> [!INDICATION]
> Une fonction polynomiale : regarder le signe de sa dérivée sur $[0,1]$.

> [!INDICATION]
> Isoler le terme $k=1$ de la dérivée.

#### Solution

$f_n$ est polynomiale, donc dérivable sur $[0,1]$, et

$$\begin{aligned}
f_n'(x) &=\sum_{k=1}^{n}k^2x^{k-1}\\
&=1+\sum_{k=2}^{n}k^2x^{k-1}\geqslant 1>0
\end{aligned}$$

pour tout $x\in[0,1]$. Donc $f_n$ est strictement croissante sur $[0,1]$.

> [!PIEGE]
> On étudie ici la **fonction** $x\mapsto f_n(x)$ à $n$ fixé, et non la suite $(f_n(x))_n$. Le rapport 2025 relève que certains candidats « ont confondu l'étude de la fonction $f_n$ demandée avec l'étude de la suite $(f_n(x))_{n\in\mathbb N^*}$ qui ne l'était pas ».

### Question 1) b)

> [!INDICATION]
> Continuité, stricte monotonie sur un intervalle : quel théorème donne existence et unicité d'un antécédent ?

> [!INDICATION]
> Calculer $f_n(0)$ et $f_n(1)$, et situer $1$ entre les deux.

#### Solution

$f_n$ est continue et strictement croissante sur $[0,1]$ : elle réalise une bijection de $[0,1]$ sur $[f_n(0),f_n(1)]=\left[0,\frac{n(n+1)}{2}\right]$.

Comme $\frac{n(n+1)}{2}\geqslant 1$, le réel $1$ a un unique antécédent $u_n\in[0,1]$.

> [!METHODE]
> Théorème de la bijection : continuité **et** stricte monotonie sur un **intervalle**, puis calcul de l'image. Les trois éléments doivent figurer dans la copie.

### Question 1) c)

> [!INDICATION]
> Écrire $f_1$.

#### Solution

$f_1(x)=x$, donc $u_1=1$.

### Question 2) a)

> [!INDICATION]
> Que contient de plus la somme qui définit $f_{n+1}$ ?

#### Solution

$f_{n+1}(x)=f_n(x)+(n+1)x^{n+1}$ pour tout $x\in[0,1]$.

### Question 2) b)

> [!INDICATION]
> Évaluer la relation de 2) a) en $x=u_n$ et utiliser la définition de $u_n$.

#### Solution

$f_{n+1}(u_n)=f_n(u_n)+(n+1)u_n^{n+1}=1+(n+1)u_n^{n+1}\geqslant 1$ car $u_n\geqslant 0$.

### Question 2) c)

> [!INDICATION]
> Le réel $1$ s'écrit aussi $f_{n+1}(u_{n+1})$.

> [!INDICATION]
> Comparer deux images par une fonction strictement croissante, c'est comparer les antécédents. Raisonner par l'absurde si besoin.

#### Solution

On a $f_{n+1}(u_n)\geqslant 1=f_{n+1}(u_{n+1})$. Si l'on avait $u_n<u_{n+1}$, la stricte croissance de $f_{n+1}$ donnerait $f_{n+1}(u_n)<1$ : contradiction. Donc $u_{n+1}\leqslant u_n$, et $(u_n)$ est décroissante.

> [!METHODE]
> Pour une suite implicite $f_n(u_n)=c$ avec $f_n$ monotone, on compare $f_{n+1}(u_n)$ à $c=f_{n+1}(u_{n+1})$ : la monotonie de $f_{n+1}$ transforme l'inégalité sur les images en inégalité sur les antécédents.

> [!JURY]
> Le rapport 2025 note que « l'étude d'une suite implicite reste assez mystérieuse pour pas mal de candidats ».

### Question 2) d)

> [!INDICATION]
> Une suite décroissante : il faut un minorant. L'intervalle où vit $u_n$ en fournit un.

#### Solution

$(u_n)$ est décroissante et minorée par $0$ : elle converge (théorème de la limite monotone). Sa limite $\ell$ appartient à $[0,1]$.

> [!PIEGE]
> Une suite décroissante est **majorée** par son premier terme, pas minorée : le rapport 2025 cite parmi les erreurs de cours le fait de « penser qu'une suite décroissante soit minorée par son premier terme ».

### Question 3) a)

> [!INDICATION]
> Somme des termes d'une suite géométrique de raison $x\neq 1$.

#### Solution

$\displaystyle\sum_{k=0}^{n}x^k=\frac{1-x^{n+1}}{1-x}$ pour $x\neq 1$.

> [!PIEGE]
> C'est une somme **finie** : ne pas la confondre avec la somme de la série géométrique $\frac{1}{1-x}$, confusion signalée par le rapport 2025.

### Question 3) b)

> [!INDICATION]
> L'égalité de 3) a) est vraie pour tout $x\neq1$ : on peut la dériver.

> [!INDICATION]
> Dériver le quotient, puis regrouper les termes en $x^{n+1}$ au numérateur.

#### Solution

On dérive les deux membres de 3) a) sur $\mathbb{R}\setminus\{1\}$. À gauche on obtient $\sum_{k=1}^nk\,x^{k-1}$. À droite :

$$\begin{aligned}
\frac{\mathrm d}{\mathrm dx}\left(\frac{1-x^{n+1}}{1-x}\right)
&=\frac{-(n+1)x^n(1-x)+(1-x^{n+1})}{(1-x)^2}\\
&=\frac{n\,x^{n+1}-(n+1)x^n+1}{(1-x)^2}.
\end{aligned}$$

D'où l'égalité demandée.

> [!METHODE]
> Dériver une identité polynomiale valable sur un intervalle donne une nouvelle identité : c'est ainsi qu'on obtient $\sum k\,x^{k-1}$ et $\sum k(k-1)x^{k-2}$ à partir de $\sum x^k$.

### Question 3) c)

> [!INDICATION]
> Faire apparaître $x^{k-1}$ dans $k\,x^k$.

#### Solution

Pour $x\in[0,1[$, $f_n(x)=x\sum_{k=1}^nk\,x^{k-1}$, donc

$$f_n(x)=\frac{x\left(n\,x^{n+1}-(n+1)x^n+1\right)}{(1-x)^2}.$$

### Question 4) a)

> [!INDICATION]
> $f_2(x)=1$ est une équation du second degré.

> [!INDICATION]
> Pour l'encadrement, combiner la monotonie de $(u_n)$ et la valeur de $u_2$.

#### Solution

$f_2(x)=1\iff 2x^2+x-1=0$, de discriminant $9$ et de racines $-1$ et $\frac12$.

Dans $[0,1]$ : $u_2=\frac12$. Pour $n\geqslant 2$, la décroissance donne $u_n\leqslant u_2=\frac12$, et $u_n\geqslant 0$ par définition.

Donc $0\leqslant u_n\leqslant\frac12$.

> [!JURY]
> Le rapport 2025 s'étonne que certains candidats ne sachent pas « résoudre l'équation $x+2x^2=1$ ». Une question de ce type rapporte des points à coup sûr : elle doit être rédigée complètement.

### Question 4) b)

> [!INDICATION]
> Majorer $u_n$ par $\frac12$ dans les deux expressions.

> [!INDICATION]
> Conclure par encadrement et croissances comparées.

#### Solution

Pour $n\geqslant 2$ : $0\leqslant u_n^n\leqslant\frac1{2^n}$ et $0\leqslant n\,u_n^n\leqslant\frac{n}{2^n}$.

Comme $\frac{1}{2^n}\to0$ et $\frac{n}{2^n}\to0$ (croissances comparées), le théorème d'encadrement donne $u_n^n\to 0$ et $n\,u_n^n\to 0$.

> [!PIEGE]
> $(u_n^n)$ n'est pas une suite géométrique : la « raison » $u_n$ dépend de $n$. Le rapport 2025 cite cette erreur. On ne peut pas non plus écrire « $u_n\to\ell<1$ donc $u_n^n\to 0$ » sans un argument d'encadrement : c'est précisément ce que fournit la borne $\frac12$.

### Question 4) c)

> [!INDICATION]
> Pour $n\geqslant 2$, $u_n\neq 1$ : la forme close de 3) c) s'applique en $x=u_n$.

> [!INDICATION]
> Chasser le dénominateur et développer $(1-u_n)^2$.

#### Solution

Comme $u_n\in[0,1[$ pour $n\geqslant 2$, $f_n(u_n)=1$ s'écrit $u_n\left(n\,u_n^{n+1}-(n+1)u_n^n+1\right)=(1-u_n)^2$. En développant :

$$n\,u_n^{n+2}-(n+1)u_n^{n+1}+u_n=1-2u_n+u_n^2,$$

soit $u_n^2-3u_n+1=n\,u_n^{n+2}-(n+1)u_n^{n+1}$.

### Question 4) d)

> [!INDICATION]
> Montrer que le membre de droite de 4) c) tend vers $0$ en l'écrivant à l'aide de $n\,u_n^n$ et de $u_n^n$.

> [!INDICATION]
> On obtient une équation du second degré en $\ell$ ; l'encadrement de 4) a) départage les racines.

#### Solution

$n\,u_n^{n+2}-(n+1)u_n^{n+1}=u_n^2\cdot n\,u_n^n-u_n\cdot n\,u_n^n-u_n\cdot u_n^n\to 0$, car $(u_n)$ est bornée et $n\,u_n^n\to0$, $u_n^n\to0$.

En passant à la limite dans 4) c) : $\ell^2-3\ell+1=0$, donc $\ell=\frac{3\pm\sqrt5}{2}$. Comme $0\leqslant\ell\leqslant\frac12$ et $\frac{3+\sqrt5}{2}>1$ :

$$\ell=\frac{3-\sqrt5}{2}\approx 0{,}382 .$$

> [!METHODE]
> Pour la limite d'une suite implicite : obtenir une relation exacte entre $u_n$ et des termes qui tendent vers $0$, passer à la limite, puis éliminer les racines parasites grâce à un encadrement déjà établi.

---

## Exercice 2 — Une famille de matrices simultanément diagonalisables

On identifie $E$ comme un sous-espace de dimension 2, on diagonalise l'exemple $A$, puis on constate que ses vecteurs propres conviennent pour toute matrice de $E$.

### Question 1) a)

> [!INDICATION]
> Écrire $M(a,b)$ comme combinaison linéaire de deux matrices fixes.

#### Solution

$M(a,b)=aB+bC$ avec $B=\begin{pmatrix}1&0&1\\0&2&0\\1&0&1\end{pmatrix}$ et $C=\begin{pmatrix}0&1&0\\1&-1&1\\0&1&0\end{pmatrix}$. Donc $E=\mathrm{Vect}(B,C)$, qui est un sous-espace vectoriel de $\mathcal M_3(\mathbb{R})$.

### Question 1) b)

> [!INDICATION]
> La famille $(B,C)$ est génératrice ; reste la liberté.

#### Solution

Si $aB+bC=0$, les coefficients $(1,1)$ et $(1,2)$ de $M(a,b)$ donnent $a=b=0$.

La famille $(B,C)$ est libre et génératrice : c'est une base de $E$, et $\dim E=2$.

> [!JURY]
> Le rapport 2025 signale qu'« il a beaucoup été lu que » $M(a,b)$ est égal à $\mathrm{Vect}(B,C)$, « ou que $\mathrm{Vect}(B, C)$ est une base de E, et parfois pire ! ».
>
> Une matrice est un vecteur de $E$, $\mathrm{Vect}(B,C)$ est le sous-espace $E$ lui-même, et la base est la **famille** $(B,C)$.

### Question 2)

> [!INDICATION]
> « Sans calcul » : regarder la forme des matrices de $E$ (symétrie, colonnes).

> [!INDICATION]
> Un résultat de cours donne la diagonalisabilité ; une relation entre colonnes donne la non-inversibilité.

#### Solution

Toute matrice de $E$ est symétrique, donc diagonalisable. Sa première et sa troisième colonne sont égales : ses colonnes sont liées, son rang est au plus 2, donc elle n'est pas inversible.

### Question 3)

> [!INDICATION]
> Trouver $a$ et $b$, puis vérifier le coefficient central.

#### Solution

Avec $a=1$, $b=3$ : $2a-b=-1$. Donc $A=M(1,3)\in E$.

### Question 4)

> [!INDICATION]
> Une fonction sans argument qui renvoie un `np.array`.

#### Solution

```python
def matA():
    return np.array([[1, 3, 1], [3, -1, 3], [1, 3, 1]])
```

### Question 5) a)

> [!INDICATION]
> Une matrice non inversible a une valeur propre particulière.

#### Solution

$A$ n'est pas inversible, donc $0$ est valeur propre de $A$.

### Question 5) b)

> [!INDICATION]
> Chercher une relation simple entre les colonnes de $A-5I$, puis de $A+4I$.

> [!INDICATION]
> Pour $A-5I$, additionner les colonnes ; pour $A+4I$, essayer une combinaison à coefficients $1,-2,1$.

#### Solution

Dans $A-5I=\begin{pmatrix}-4&3&1\\3&-6&3\\1&3&-4\end{pmatrix}$, la somme des colonnes est nulle. Dans $A+4I=\begin{pmatrix}5&3&1\\3&3&3\\1&3&5\end{pmatrix}$, $C_1-2C_2+C_3=0$. Les deux matrices ont des colonnes liées : elles ne sont pas inversibles, et $5$ et $-4$ sont valeurs propres de $A$.

> [!METHODE]
> Une relation $\alpha C_1+\beta C_2+\gamma C_3=0$ entre les colonnes de $A-\lambda I$ fournit à la fois la non-inversibilité **et** un vecteur propre : $\begin{pmatrix}\alpha\\\beta\\\gamma\end{pmatrix}$.

### Question 5) c)

> [!INDICATION]
> Les relations entre colonnes de la question précédente donnent déjà des vecteurs propres.

> [!INDICATION]
> Pour la dimension des sous-espaces propres, utiliser le théorème de concaténation : trois valeurs propres distinctes en dimension 3.

#### Solution

- $AX=0\iff x+3y+z=0$ et $3x-y+3z=0$ ; $3L_1-L_2$ donne $y=0$, puis $z=-x$. $U=\begin{pmatrix}1\\0\\-1\end{pmatrix}$.
- $V=\begin{pmatrix}1\\1\\1\end{pmatrix}$ vérifie $AV=5V$.
- $W=\begin{pmatrix}1\\-2\\1\end{pmatrix}$ vérifie $AW=-4W$.

La concaténation de bases des sous-espaces propres associés aux valeurs propres distinctes $0$, $5$, $-4$ est libre dans $\mathcal M_{3,1}(\mathbb{R})$. Chacun étant de dimension au moins 1, chacun est de dimension exactement 1 :

$$\begin{aligned}
E_0(A)&=\mathrm{Vect}(U)\\
E_5(A)&=\mathrm{Vect}(V)\\
E_{-4}(A)&=\mathrm{Vect}(W).
\end{aligned}$$

La famille $(U,V,W)$, libre et de cardinal 3, est une base de $\mathcal M_{3,1}(\mathbb{R})$ formée de vecteurs propres de $A$.

> [!JURY]
> Sur ce point, le rapport 2025 est net : « Quant au théorème de concaténation de familles libres de vecteurs propres associés à des valeurs propres distinctes, il est très loin d'être maîtrisé par l'ensemble des candidats. »

### Question 6)

> [!INDICATION]
> Le rang de $A-\lambda I$ se lit sur la dimension du noyau.

#### Solution

Par le théorème du rang : $\mathrm{rg}(A-5I)=3-\dim E_5(A)=2$ et $\mathrm{rg}(A+4I)=3-\dim E_{-4}(A)=2$. Le script affiche `r1= 2` puis `r2= 2`.

### Question 7) a)

> [!INDICATION]
> Calculer $M(a,b)U$, $M(a,b)V$, $M(a,b)W$ et reconnaître un multiple du vecteur.

#### Solution

$M(a,b)U=0$, $M(a,b)V=(2a+b)V$ et $M(a,b)W=(2a-2b)W$ (calcul ligne par ligne : la deuxième composante de $MW$ vaut $b-2(2a-b)+b=-2(2a-2b)$).

Ces vecteurs étant non nuls, ce sont des vecteurs propres de toute matrice de $E$, pour les valeurs propres $0$, $2a+b$ et $2a-2b$.

### Question 7) b)

> [!INDICATION]
> La même matrice de passage $P$ diagonalise toutes les matrices de $E$.

> [!INDICATION]
> Que devient $(PDP^{-1})^n$ ?

#### Solution

Avec $P=\begin{pmatrix}1&1&1\\0&1&-2\\-1&1&1\end{pmatrix}$ (inversible) et $D=\mathrm{diag}(0,2a+b,2a-2b)$, on a $MP=PD$, donc $M=PDP^{-1}$.

Par récurrence, $M^n=PD^nP^{-1}$ avec $D^n=\mathrm{diag}\left(0,(2a+b)^n,(2a-2b)^n\right)$ pour $n\geqslant1$.

On calcule $P^{-1}$ une fois pour toutes.

> [!METHODE]
> Calcul de puissances par diagonalisation : $M=PDP^{-1}\Rightarrow M^n=PD^nP^{-1}$, à démontrer par récurrence (les $P^{-1}P$ intermédiaires se simplifient).

### Question 7) c)

> [!INDICATION]
> Construire $P$ et $D^n$ en Python, puis faire les produits avec `np.dot`.

#### Solution

```python
def puissanceM(a, b, n):
    P = np.array([[1, 1, 1], [0, 1, -2], [-1, 1, 1]])
    D = np.diag([0, (2*a + b)**n, (2*a - 2*b)**n])
    return np.dot(np.dot(P, D), al.inv(P))
```

Vérifié sur $M(2,-1)^3$, comparé à `al.matrix_power` : écart de l'ordre de $10^{-14}$.

> [!PIEGE]
> En Python, `P*D` est le produit **coefficient par coefficient** ; le produit matriciel s'écrit `np.dot(P, D)`.

---

## Exercice 3 — Vers la loi exponentielle

On reconnaît d'abord que $f_n$ est une densité, on calcule les moments par la variable auxiliaire $1-\frac{X_n}{n}$, puis on passe à la limite dans les fonctions de répartition.

### Question 1)

> [!INDICATION]
> Trois points : positivité, continuité sauf en un nombre fini de points, intégrale égale à 1.

> [!INDICATION]
> Une primitive de $\left(1-\frac xn\right)^{n-1}$ se devine en dérivant $\left(1-\frac xn\right)^n$.

#### Solution

Sur $[0,n]$, $1-\frac xn\in[0,1]$ donc $f_n\geqslant 0$ ; ailleurs $f_n=0$.

$f_n$ est continue sur $\mathbb{R}$ sauf éventuellement en $0$ et en $n$.

Elle est discontinue en $0$, où elle vaut $1$ ; en $n$, elle est continue si $n\geqslant2$ (pour $n=1$, discontinue en $1$).

Enfin

$$\begin{aligned}
\int_{-\infty}^{+\infty}f_n &=\int_0^n\left(1-\frac xn\right)^{n-1}\mathrm dx\\
&=\left[-\left(1-\frac xn\right)^n\right]_0^n\\
&=1 .
\end{aligned}$$

> [!JURY]
> Le rapport 2025 reproche d'avoir répondu « en affirmant sans preuve que $f_n$ est positive et continue sauf en 0 ». Il faut justifier la positivité (le signe de $1-\frac xn$ sur $[0,n]$) et regarder le point $n$.

### Question 2) a)

> [!INDICATION]
> Théorème de transfert : la densité est nulle hors de $[0,n]$, les intégrales sont sur un segment.

> [!INDICATION]
> $\left(1-\frac xn\right)f_n(x)=\left(1-\frac xn\right)^n$ : même méthode de primitive qu'en 1).

#### Solution

$f_n$ est nulle en dehors de $]-1,n+1[$, et $g(x)=1-\frac xn$ ou $g(x)=\left(1-\frac xn\right)^2$ est continue sur cet intervalle : le théorème de transfert s'applique avec $a=-1$, $b=n+1$.

L'intégrale $\int_{-1}^{n+1}g\,f_n=\int_0^ng\,f_n$ porte sur un segment et une fonction continue : elle converge absolument, les deux espérances existent et

$$\begin{aligned}
E\left(1-\frac{X_n}{n}\right) &=\int_0^n\left(1-\frac xn\right)^n\mathrm dx\\
&=\frac{n}{n+1}\\
E\left(\left(1-\frac{X_n}{n}\right)^2\right) &=\int_0^n\left(1-\frac xn\right)^{n+1}\mathrm dx\\
&=\frac{n}{n+2}.
\end{aligned}$$

> [!JURY]
> Le rapport 2025 reproche de négliger « l'existence d'une espérance » en ne privilégiant que le calcul. Une phrase d'existence, même brève, est attendue avant toute valeur.

### Question 2) b)

> [!INDICATION]
> $X_n$ est une fonction affine de $Y_n=1-\frac{X_n}{n}$.

> [!INDICATION]
> Pour la variance : Koenig-Huygens sur $Y_n$, puis $V(aY+b)=a^2V(Y)$.

#### Solution

$X_n=n-nY_n$ avec $Y_n$ admettant un moment d'ordre 2, donc $X_n$ admet espérance et variance. $E(X_n)=n-\frac{n^2}{n+1}=\frac{n}{n+1}$. Puis

$$\begin{aligned}
V(Y_n) &=\frac{n}{n+2}-\frac{n^2}{(n+1)^2}\\
&=\frac{n}{(n+1)^2(n+2)}\\
V(X_n) &=n^2V(Y_n)\\
&=\frac{n^3}{(n+1)^2(n+2)}.
\end{aligned}$$

> [!PIEGE]
> Une variance négative signale une erreur de calcul : le rapport 2025 juge cela « de l'ordre de l'insupportable ». Contrôle utile ici : pour $n=1$, $X_1$ suit la loi uniforme sur $[0,1]$ et l'on doit retrouver $\frac12$ et $\frac1{12}$.

### Question 3)

> [!INDICATION]
> Trois cas selon la position de $x$ par rapport à $0$ et à $n$.

#### Solution

$F_n(x)=0$ si $x<0$ ; $F_n(x)=\int_0^x\left(1-\frac tn\right)^{n-1}\mathrm dt=1-\left(1-\frac xn\right)^n$ si $0\leqslant x\leqslant n$ ; $F_n(x)=1$ si $x>n$.

> [!PIEGE]
> Le rapport 2025 cite une fonction de répartition « nulle sur $[n,+\infty[$, ce qui est inenvisageable ! » : une fonction de répartition est croissante et tend vers 1 en $+\infty$.

### Question 4) a)

> [!INDICATION]
> Lire la question 3).

#### Solution

Pour $x<0$, $F_n(x)=0$ pour tout $n$ : la limite vaut $0$.

### Question 4) b)

> [!INDICATION]
> Vérifier que $x$ est bien dans $[0,n]$.

#### Solution

$x<\lfloor x\rfloor+1\leqslant n$, donc $0\leqslant x\leqslant n$ et la question 3) donne $F_n(x)=1-\left(1-\frac xn\right)^n$.

### Question 4) c)

> [!INDICATION]
> Un équivalent usuel de $\ln(1+u)$ quand $u\to0$.

#### Solution

Pour $x=0$ la suite est nulle. Pour $x>0$, $-\frac xn\to0$ et $\ln\left(1-\frac xn\right)\sim-\frac xn$, donc $n\ln\left(1-\frac xn\right)\sim -x$ : la limite vaut $-x$ dans tous les cas.

### Question 4) d)

> [!INDICATION]
> Écrire $\left(1-\frac xn\right)^n$ sous forme exponentielle.

> [!INDICATION]
> Reconnaître la limite des $F_n$, puis appliquer la définition de la convergence en loi.

#### Solution

Pour $x\geqslant0$ : $\left(1-\frac xn\right)^n=\exp\left(n\ln\left(1-\frac xn\right)\right)\to\mathrm e^{-x}$ par continuité de $\exp$, donc $F_n(x)\to1-\mathrm e^{-x}$.

Pour $x<0$, $F_n(x)\to0$. La limite est la fonction de répartition de la loi $\mathcal E(1)$, continue sur $\mathbb{R}$ : $(X_n)$ converge en loi vers $X\hookrightarrow\mathcal E(1)$.

> [!PIEGE]
> Le rapport 2025 juge « un peu naïf » de croire que $\left(1-\frac xn\right)^n\to1$ parce que $1-\frac xn\to1$ : c'est une forme indéterminée $1^\infty$, que l'on lève toujours par le passage à l'exponentielle.

### Question 5) a)

> [!INDICATION]
> Fonction de répartition de la loi uniforme sur $[0,1]$.

#### Solution

$G(x)=0$ si $x<0$, $G(x)=x$ si $0\leqslant x\leqslant1$, $G(x)=1$ si $x>1$.

### Question 5) b)

> [!INDICATION]
> Le minimum dépasse un seuil si et seulement si toutes les variables le dépassent.

> [!INDICATION]
> Utiliser l'indépendance mutuelle, puis distinguer trois cas pour $\frac xn$.

#### Solution

$[Z_n>x]=\bigcap_{i=1}^n\left[U_i>\frac xn\right]$, donc par indépendance $P(Z_n>x)=\left(1-G\left(\frac xn\right)\right)^n$.

D'où $F_{Z_n}(x)=0$ si $x<0$, puis $F_{Z_n}(x)=1-\left(1-\frac xn\right)^n$ si $0\leqslant x\leqslant n$.

Enfin $F_{Z_n}(x)=1$ si $x>n$.

> [!METHODE]
> Loi du minimum : passer par $P(\min>t)$, intersection d'événements indépendants. Loi du maximum : passer par $P(\max\leqslant t)$.

### Question 5) c)

> [!INDICATION]
> Comparer avec la question 3).

#### Solution

$F_{Z_n}=F_n$ ; la fonction de répartition caractérise la loi, donc $Z_n$ suit la même loi que $X_n$.

### Question 5) d)

> [!INDICATION]
> Simuler $n$ uniformes indépendantes avec `rd.random`, puis prendre le minimum.

#### Solution

```python
def simulX(n):
    U = rd.random(n)
    return n * np.min(U)
```

Contrôle numérique ($10^5$ simulations, $n=5$) : moyenne empirique $0{,}833$ pour $\frac56$, variance $0{,}493$ pour $\frac{125}{252}\approx0{,}496$.

---

## Problème — Première boule blanche dans une urne choisie au hasard

Tout repose sur la formule des probabilités totales avec le système complet $(U_1,\dots,U_{n+1})$ ; conditionnellement à $U_k$, le rang de la première blanche est géométrique.

### Question 1)

> [!INDICATION]
> Que se passe-t-il dans l'urne $n+1$ ? dans l'urne $1$ ?

> [!INDICATION]
> Dans l'urne $k$, une boule numérotée au hasard dans $[\![1,n]\!]$ est noire si son numéro est au plus $k-1$.

#### Solution

```python
def varX(n):
    k = rd.randint(1, n+2)       # choix de l'urne
    if k == n+1:
        X = 0
    elif k == 1:
        X = 1
    else:
        X = 1
        while rd.randint(1, n+1) <= k-1:
            X = X + 1
    return(X)
```

Tant qu'on tire une noire, on passe au tirage suivant ; `X` compte le rang du tirage en cours.

### Question 2)

> [!INDICATION]
> Choix équiprobable.

#### Solution

$P(U_k)=\frac1{n+1}$ pour tout $k\in[\![1,n+1]\!]$.

> [!JURY]
> Le rapport 2025 signale qu'« un grand nombre de candidats confondent un événement tel que $U_k$ avec une variable aléatoire en écrivant $P(U_k = k) = \frac{1}{n+1}$ ». $U_k$ est un événement : on écrit $P(U_k)$.

### Question 3) a)

> [!INDICATION]
> Sachant l'urne, les tirages avec remise sont indépendants et identiques : on attend le premier succès.

#### Solution

Sachant $U_k$ ($1\leqslant k\leqslant n$), $X_n$ est le rang du premier succès dans des épreuves de Bernoulli indépendantes de paramètre $\frac{n-k+1}{n}$.

Ainsi $X_n$ suit la loi géométrique $\mathcal G\left(\frac{n-k+1}{n}\right)$, soit $P_{U_k}(X_n=j)=\left(\frac{k-1}{n}\right)^{j-1}\frac{n-k+1}{n}$ pour $j\geqslant1$.

Pour $k=1$ : $X_n=1$ presque sûrement.

### Question 3) b)

> [!INDICATION]
> La commande `rd.geometric(p)` est rappelée par l'énoncé.

#### Solution

```python
    else:
        X = rd.geometric((n+1-k)/n)
    return(X)
```

Contrôle : sur $2\cdot10^5$ simulations avec $n=4$, les deux fonctions donnent une moyenne de $1{,}66$ environ, pour $E(X_4)=\frac53$.

### Question 4) a)

> [!INDICATION]
> Composition de l'urne $n+1$.

#### Solution

$P_{U_{n+1}}(X_n=1)=0$.

### Question 4) b)

> [!INDICATION]
> Proportion de blanches dans l'urne $k$.

#### Solution

$P_{U_k}(X_n=1)=\frac{n-k+1}{n}$.

### Question 4) c)

> [!INDICATION]
> Formule des probabilités totales, puis une somme d'entiers après changement d'indice.

#### Solution

$$\begin{aligned}
P(X_n=1) &=\frac1{n+1}\sum_{k=1}^n\frac{n-k+1}{n}\\
&=\frac{1}{n(n+1)}\sum_{i=1}^ni\\
&=\frac12 .
\end{aligned}$$

> [!METHODE]
> Formule des probabilités totales : nommer le système complet, vérifier que ses probabilités sont non nulles, puis écrire $P(B)=\sum_kP(U_k)P_{U_k}(B)$.

### Question 5) a)

> [!INDICATION]
> Même raisonnement qu'en 4) a).

#### Solution

$P_{U_{n+1}}(X_n=j)=0$.

### Question 5) b)

> [!INDICATION]
> Loi géométrique de 3) a).

#### Solution

$P_{U_k}(X_n=j)=\left(\frac{k-1}{n}\right)^{j-1}\left(1-\frac{k-1}{n}\right)$, qui vaut bien $0$ pour $k=1$ puisque $j\geqslant2$.

### Question 5) c)

> [!INDICATION]
> Probabilités totales, puis décalage d'indice $i=k-1$.

#### Solution

$$\begin{aligned}
P(X_n=j) &=\frac1{n+1}\sum_{k=1}^{n}\left(\frac{k-1}{n}\right)^{j-1}\left(1-\frac{k-1}{n}\right)\\
&=\frac1{n+1}\sum_{i=0}^{n-1}\left[\left(\frac in\right)^{j-1}-\left(\frac in\right)^{j}\right].
\end{aligned}$$

### Question 6) a)

> [!INDICATION]
> Série télescopique : calculer la somme partielle jusqu'à un rang $N$.

#### Solution

Avec $q=\frac kn\in[0,1[$ : $\sum_{j=2}^N\left(q^{j-1}-q^j\right)=q-q^N\to q$, donc la série converge et a pour somme $\frac kn$.

> [!METHODE]
> Une série télescopique $\sum(a_{j-1}-a_j)$ se traite toujours par sa somme partielle, égale à $a_{\text{début}}-a_N$.

### Question 6) b)

> [!INDICATION]
> $[X_n\geqslant2]$ est une réunion dénombrable d'événements incompatibles.

> [!INDICATION]
> Échanger la somme finie sur $k$ et la série sur $j$, puis utiliser 6) a).

#### Solution

$$\begin{aligned}
P(X_n\geqslant2) &=\sum_{j\geqslant2}P(X_n=j)\\
&=\frac1{n+1}\sum_{k=0}^{n-1}\frac kn\\
&=\frac{n-1}{2(n+1)} .
\end{aligned}$$

L'échange est licite : c'est la linéarité de la somme pour une somme **finie** de séries convergentes.

### Question 7) a)

> [!INDICATION]
> Un système complet adapté aux valeurs de $X_n$.

#### Solution

$P(X_n=0)=1-P(X_n=1)-P(X_n\geqslant2)=1-\frac12-\frac{n-1}{2(n+1)}=\frac1{n+1}$.

> [!JURY]
> Le rapport 2025 rappelle qu'« il aurait été bien vu de trouver des probabilités positives et inférieures ou égales à 1 ». Ici, le résultat se contrôle par la question suivante.

### Question 7) b)

> [!INDICATION]
> Dans une urne qui contient au moins une blanche, peut-on ne jamais tirer de blanche ?

#### Solution

Oui : dans l'urne $k\leqslant n$, la probabilité de n'avoir que des noires aux $N$ premiers tirages est $\left(\frac{k-1}{n}\right)^N\to0$. Ne jamais tirer de blanche revient (presque sûrement) à avoir choisi l'urne $n+1$, d'où $P(X_n=0)=P(U_{n+1})=\frac1{n+1}$.

### Question 8) a)

> [!INDICATION]
> Existence d'abord : $X_n$ est à valeurs dans $\mathbb{N}$, il s'agit de la convergence de $\sum j\,P(X_n=j)$.

> [!INDICATION]
> Pour chaque $k$, reconnaître une série géométrique dérivée $\sum j\,q^{j-1}$ avec $q=\frac kn<1$.

> [!INDICATION]
> Après calcul, un terme $\frac12$ se simplifie ; terminer par le changement d'indice $p=n-k$.

#### Solution

Pour $j\geqslant2$, $j\,P(X_n=j)=\frac1{n+1}\sum_{k=0}^{n-1}j\,q_k^{j-1}(1-q_k)$ avec $q_k=\frac kn\in[0,1[$. Pour $q\in[0,1[$, $\sum_{j\geqslant1}j\,q^{j-1}$ converge et vaut $\frac1{(1-q)^2}$, donc

$$\sum_{j=2}^{+\infty}j\,q^{j-1}(1-q)=\frac1{1-q}-(1-q).$$

La série $\sum j\,P(X_n=j)$, combinaison linéaire finie de séries convergentes à termes positifs, converge : $X_n$ admet une espérance, et

$$\begin{aligned}
E(X_n) &=\frac12+\frac1{n+1}\sum_{k=0}^{n-1}\left[\frac{n}{n-k}-\left(1-\frac kn\right)\right]\\
&=\frac1{n+1}\sum_{k=0}^{n-1}\frac{n}{n-k}\\
&=\frac{n}{n+1}\sum_{p=1}^n\frac1p,
\end{aligned}$$

car $\sum_{k=0}^{n-1}\left(1-\frac kn\right)=\frac{n+1}2$.

> [!PIEGE]
> La formule de 5) c) n'est établie que pour $j\geqslant2$ : on ajoute à part le terme $1\cdot P(X_n=1)=\frac12$. (Avec la convention $0^0=1$, elle redonne d'ailleurs $P(X_n=1)=\frac12$.)

> [!METHODE]
> Pour une variable obtenue par mélange de lois géométriques, on peut contrôler le résultat (formule de l'espérance totale, hors programme de maths appliquées : simple vérification, non rédigeable en copie) : sachant $U_k$, l'espérance vaut $\frac{n}{n-k+1}$, et la moyenne de ces valeurs pondérées par $\frac1{n+1}$ (avec $0$ pour l'urne $n+1$) redonne $\frac{n}{n+1}\sum_{p=1}^n\frac1p$.

### Question 8) b)

> [!INDICATION]
> Opérations coefficient par coefficient sur le vecteur `v`, puis `np.sum`.

#### Solution

```python
n = int(input('entrez la valeur de n :'))
v = np.arange(1, n+1)
E = n/(n+1) * np.sum(1/v)
print(E)
```

### Question 9) a)

> [!INDICATION]
> Encadrer $\frac1t$ sur $[p,p+1]$, puis intégrer.

#### Solution

Pour $t\in[p,p+1]$, $\frac1{p+1}\leqslant\frac1t\leqslant\frac1p$ (décroissance de $t\mapsto\frac1t$). Par croissance de l'intégrale, bornes dans l'ordre et intervalle de longueur 1 : $\frac1{p+1}\leqslant\int_p^{p+1}\frac{\mathrm dt}t\leqslant\frac1p$.

### Question 9) b)

> [!INDICATION]
> Sommer pour $p$ de $1$ à $n-1$ et utiliser la relation de Chasles.

#### Solution

$\sum_{p=1}^{n-1}\int_p^{p+1}\frac{\mathrm dt}t=\int_1^n\frac{\mathrm dt}t=\ln n$, d'où $\sum_{p=2}^n\frac1p\leqslant\ln n\leqslant\sum_{p=1}^{n-1}\frac1p$.

### Question 9) c)

> [!INDICATION]
> Ajouter le terme qui manque à chacune des deux sommes de 9) b).

#### Solution

$\sum_{p=1}^n\frac1p=1+\sum_{p=2}^n\frac1p\leqslant1+\ln n$ et $\sum_{p=1}^n\frac1p=\sum_{p=1}^{n-1}\frac1p+\frac1n\geqslant\ln n+\frac1n$.

### Question 9) d)

> [!INDICATION]
> Diviser l'encadrement par $\ln n$.

#### Solution

$1+\frac1{n\ln n}\leqslant\frac{1}{\ln n}\sum_{p=1}^n\frac1p\leqslant1+\frac1{\ln n}$ pour $n\geqslant2$ ; par encadrement, $\sum_{p=1}^n\frac1p\sim\ln n$. Comme $\frac n{n+1}\to1$ et que l'équivalence passe au produit :

$$E(X_n)\underset{n\to+\infty}{\sim}\ln n .$$

> [!METHODE]
> Comparaison série-intégrale : encadrer $f$ sur $[p,p+1]$ par $f(p)$ et $f(p+1)$, intégrer, sommer. C'est la méthode standard pour un équivalent de $\sum_{p\leqslant n}f(p)$ avec $f$ monotone.

---

## Bilan

**Méthodes à retenir.**

- Suite implicite $f_n(u_n)=c$ : bijection pour l'existence, comparaison de $f_{n+1}(u_n)$ et $f_{n+1}(u_{n+1})$ pour la monotonie, relation exacte puis passage à la limite pour la valeur.
- Sommes $\sum k\,x^{k-1}$ : dériver la somme géométrique finie.
- Algèbre linéaire « sans calcul » : symétrie $\Rightarrow$ diagonalisable ; colonnes liées $\Rightarrow$ non inversible et vecteur propre pour $0$ ; une relation entre colonnes de $A-\lambda I$ donne un vecteur propre.
- Densités : positivité justifiée, points de discontinuité en nombre fini, intégrale 1 ; existence avant calcul pour toute espérance.
- Convergence en loi : limite simple des fonctions de répartition aux points de continuité de la limite ; forme $1^\infty$ par l'exponentielle.
- Loi du minimum par $P(\min>t)$ ; probabilités totales sur le choix de l'urne ; séries télescopiques et géométriques dérivées ; comparaison série-intégrale pour un équivalent de la série harmonique.

**Prérequis à revoir.** Théorème de la bijection, limite monotone, croissances comparées, équivalent de $\ln(1+u)$ ; théorème de concaténation des familles libres de vecteurs propres ; théorème de transfert pour une densité ; lois géométrique et exponentielle ; commandes `np.dot`, `al.inv`, `rd.random`, `rd.geometric`, `np.sum`.

**Questions transposables.** Limite d'une suite implicite (sujet EDHEC classique) ; diagonalisation simultanée d'une famille de matrices ; $n\min(U_1,\dots,U_n)\to\mathcal E(1)$ en loi ; équivalent $H_n\sim\ln n$.
