# ECRICOME ECT — Mathématiques technologiques 2025 · Corrigé guidé

*Corrigé rédigé par IA, non officiel. Signalez toute erreur.*

## Présentation du sujet

**Format.** Épreuve de 4 heures, sans document ni calculatrice. Trois exercices indépendants, 81 questions élémentaires en comptant les sous-questions. Les seules données numériques sont $e\simeq 2{,}7$ et $e^{-1}\simeq 0{,}4$ (exercice 2, question 11).

**Découpage.**

| Exercice | Thème | Notions du programme ECT |
|---|---|---|
| 1, parties 1–2 | Puissances d'une matrice $3\times3$ par polynôme annulateur et par diagonalisation | calcul matriciel, inverse, valeurs et vecteurs propres, suites géométriques, récurrence |
| 1, partie 3 | Chat qui change de maison : chaîne de Markov à trois états | probabilités conditionnelles, formule des probabilités totales, formule de Bayes, espérance, variance |
| 1, partie 4 | Base de données vétérinaire | SQL : `SELECT … WHERE`, `UPDATE`, `INSERT INTO`, `INNER JOIN … ON` |
| 2, partie 1 | Fonctions $f=e^x+e^{-x}$ et $g=e^x-e^{-x}$ | limites, variations, convexité, tangente, intégrale et aire |
| 2, partie 2 | Suite définie implicitement par $g(u_n)=1/n$ | théorème de la bijection, monotonie, limite monotone, dichotomie en Python |
| 3 | Loi exponentielle, intégrales $\int_0^{+\infty}x^{n-1}e^{-x}\,dx$, moyenne empirique | densité, fonction de répartition, simulation, intégration par parties, intégrales impropres, Bienaymé-Tchebychev |

**Difficulté.** Le sujet est long mais très progressif. Les questions de cours (exercice 3, 1.(a), 1.(b), 2.(a)) et les calculs directs (exercice 1, parties 1 et 2 ; exercice 2, questions 1 à 6) rapportent beaucoup : le rapport 2025 regrette que « de nombreux candidats ne traitent pas, ou faussement, les nombreuses questions de cours ». Les questions plus délicates sont 1.10.(a) (formule des probabilités totales bien écrite), 2.5.(b) (convexité et tangente), 2.9.(b)/(d), 3.2.(d) et 3.5–3.6 (convergence d'intégrales). La moyenne de l'épreuve est de 11,2 sur 20 avec un écart-type de 5,36 (rapport 2025).

**Gestion du temps.** Environ 1 h 40 pour l'exercice 1 (dont 10 minutes de SQL), 1 h 20 pour l'exercice 2, 1 h pour l'exercice 3. Ne pas sacrifier les questions de cours de l'exercice 3 en fin d'épreuve : commencer par elles si l'exercice 1 traîne.

## Exercice 1 — Partie 1 : réduction de la matrice M

On écrit $M=2I+J$ avec $J$ la matrice pleine de $1$ : on en tire un polynôme annulateur, les valeurs propres possibles, puis une diagonalisation explicite qui donne $M^n$.

### Question 1.(a)

> [!INDICATION]
> Retranchez $2$ aux seuls coefficients diagonaux.

#### Solution

$$J=M-2I=\begin{pmatrix}1&1&1\\1&1&1\\1&1&1\end{pmatrix}.$$
Tous les coefficients de $J$ valent $1$.

### Question 1.(b)

> [!INDICATION]
> Chaque coefficient de $J^2$ est le produit d'une ligne de $J$ par une colonne de $J$.

#### Solution

Le coefficient $(i,j)$ de $J^2$ vaut $\sum_{k=1}^{3}1\times1=3$. Donc
$$J^2=\begin{pmatrix}3&3&3\\3&3&3\\3&3&3\end{pmatrix},\qquad \boxed{J^2=3J}.$$

> [!PIEGE]
> Le carré d'une matrice n'est pas la matrice des carrés des coefficients : $J^2\neq J$.

### Question 1.(c)

> [!INDICATION]
> Écrivez $M=2I+J$ et développez : $I$ et $J$ commutent.

#### Solution

Comme $M=2I+J$ et que $I$ commute avec toute matrice, on peut développer :
$$\begin{aligned}
M^2&=(2I+J)^2\\
&=4I+4J+J^2\\
&=4I+4J+3J.
\end{aligned}$$
$$\boxed{M^2=4I+7J}.$$

> [!PIEGE]
> L'identité $(A+B)^2=A^2+2AB+B^2$ n'est vraie que si $A$ et $B$ commutent ; c'est le cas ici car l'une des deux est $2I$. Le préciser.

### Question 1.(d)

> [!INDICATION]
> Exprimez $7M-10I$ à l'aide de $I$ et $J$ et comparez avec la question précédente.

#### Solution

$$\begin{aligned}
7M-10I&=7(2I+J)-10I\\
&=4I+7J\\
&=M^2.
\end{aligned}$$
Donc $\boxed{M^2=7M-10I}$.

### Question 2.(a)

> [!INDICATION]
> Évaluez $R$ en $M$ en remplaçant $X^2$ par $M^2$ et la constante $10$ par $10I$.

#### Solution

$$R(M)=M^2-7M+10I=0$$
d'après la question 1.(d). **$R$ est un polynôme annulateur de $M$.**

### Question 2.(b)

> [!INDICATION]
> Calculez $R(2)$, puis utilisez la somme (ou le produit) des racines d'un trinôme.

#### Solution

$R(2)=4-14+10=0$, donc $2$ est racine de $R$.

Le produit des racines de $X^2-7X+10$ vaut $10$, donc l'autre racine est $10/2=5$ (vérification : $R(5)=25-35+10=0$).

Ainsi
$$R(X)=(X-2)(X-5).$$
**Les racines de $R$ sont $2$ et $5$.**

### Question 2.(c)

> [!INDICATION]
> Toute valeur propre d'une matrice est racine de tout polynôme annulateur de cette matrice.

#### Solution

Les valeurs propres de $M$ sont parmi les racines de tout polynôme annulateur. **Les seules valeurs propres possibles de $M$ sont $2$ et $5$.** À ce stade rien ne garantit que ces deux nombres soient effectivement valeurs propres.

> [!PIEGE]
> Une racine d'un polynôme annulateur n'est pas forcément une valeur propre : c'est une valeur propre *possible*. Les questions 3 et 4 vérifient qu'ici les deux le sont.

> [!JURY]
> Le rapport 2025 relève qu'une partie non négligeable des candidats donne les racines comme étant forcément des valeurs propres.

### Question 3

> [!INDICATION]
> Calculez $MU$ et exprimez le résultat en fonction de $U$.

> [!INDICATION]
> N'oubliez pas la condition qui fait d'un vecteur un vecteur propre.

#### Solution

$$MU=\begin{pmatrix}3+1+1\\1+3+1\\1+1+3\end{pmatrix}=\begin{pmatrix}5\\5\\5\end{pmatrix}=5U.$$
Comme $U\neq0$, **$5$ est valeur propre de $M$ et $U$ est un vecteur propre associé.**

> [!JURY]
> Le rapport 2025 note que beaucoup calculent $MU$ sans faire apparaître $5U$, ou oublient de vérifier que $U$ est non nul (ou le font trop tard).

### Question 4

> [!INDICATION]
> Même démarche qu'à la question 3, pour chacun des deux vecteurs.

#### Solution

$$MV=\begin{pmatrix}3-1\\1-1\\1-3\end{pmatrix}=\begin{pmatrix}2\\0\\-2\end{pmatrix}=2V,
\qquad
MW=\begin{pmatrix}1-1\\3-1\\1-3\end{pmatrix}=\begin{pmatrix}0\\2\\-2\end{pmatrix}=2W.$$
$V$ et $W$ sont non nuls, donc **$V$ et $W$ sont des vecteurs propres de $M$ associés à la valeur propre $2$.**

### Question 5.(a)

> [!INDICATION]
> Calcul direct ligne par colonne ; le résultat est un multiple simple de $I$.

#### Solution

$$QP=\begin{pmatrix}1&1&1\\2&-1&-1\\-1&2&-1\end{pmatrix}\begin{pmatrix}1&1&0\\1&0&1\\1&-1&-1\end{pmatrix}=\begin{pmatrix}3&0&0\\0&3&0\\0&0&3\end{pmatrix}=3I.$$

### Question 5.(b)

> [!INDICATION]
> Trouvez une matrice dont le produit avec $P$ donne $I$.

#### Solution

D'après 5.(a), $\left(\tfrac13Q\right)P=I$. Une matrice carrée qui admet un inverse à gauche est inversible et cet inverse est son inverse. Donc **$P$ est inversible et $P^{-1}=\tfrac13Q$.**

> [!JURY]
> Le rapport 2025 : « Pour prouver que P est inversible, seuls quelques uns pensent à mettre en évidence une matrice dont le produit avec P est l’identité. » Il rappelle aussi qu'il faut répondre aux deux demandes : inversibilité **et** expression de $P^{-1}$.

### Question 5.(c)

> [!INDICATION]
> Comparez les colonnes : les colonnes de $P$ sont $U$, $V$, $W$.

#### Solution

Les colonnes de $P$ sont $U$, $V$, $W$.

Les colonnes de $MP$ sont donc $MU=5U$, $MV=2V$, $MW=2W$.

Les colonnes de $PD$ sont $5U$, $2V$, $2W$ (multiplier à droite par une matrice diagonale multiplie chaque colonne par le coefficient correspondant).

D'où
$$PD=MP=\begin{pmatrix}5&2&0\\5&0&2\\5&-2&-2\end{pmatrix}.$$

### Question 5.(d)

> [!INDICATION]
> Déduisez d'abord de 5.(b) et 5.(c) une écriture de $M$ à l'aide de $P$, $D$ et $Q$.

> [!INDICATION]
> Récurrence : pour l'hérédité, écrivez $M^{n+1}=M^n\,M$ et simplifiez le produit central $Q P$.

#### Solution

En multipliant $PD=MP$ à droite par $P^{-1}=\tfrac13Q$, on obtient $M=\tfrac13PDQ$.

Montrons par récurrence sur $n$ la propriété $\mathcal P(n)$ : $M^n=\tfrac13PD^nQ$.

*Initialisation.* $D^0=I$ et $\tfrac13PD^0Q=\tfrac13PQ=PP^{-1}=I=M^0$ : $\mathcal P(0)$ est vraie.

*Hérédité.* Soit $n\in\mathbb N$ tel que $\mathcal P(n)$ soit vraie. Alors
$$\begin{aligned}
M^{n+1}&=M^nM\\
&=\tfrac13PD^nQ\times\tfrac13PDQ\\
&=\tfrac19PD^n(QP)DQ\\
&=\tfrac19PD^n(3I)DQ\\
&=\tfrac13PD^{n+1}Q.
\end{aligned}$$
$\mathcal P(n+1)$ est vraie.

*Conclusion.* Par récurrence, $\boxed{\forall n\in\mathbb N,\ M^n=\tfrac13PD^nQ}$.

> [!PIEGE]
> Ne pas faire commuter les matrices : seuls les scalaires $\tfrac13$ peuvent être déplacés librement. L'initialisation demande de justifier $PQ=3I$ (via $Q=3P^{-1}$), pas seulement $QP=3I$.

> [!JURY]
> Le rapport 2025 signale que l'égalité d'initialisation est rarement justifiée rigoureusement et que certains écrivent $M^0=1$ ou $0$ : $M^0$ est la matrice $I$.

## Exercice 1 — Partie 2 : puissances de M par suites récurrentes

On retrouve $M^n$ par une autre voie : le polynôme annulateur donne $M^n=a_nM+b_nI$, et les suites $(a_n)$, $(b_n)$ se calculent grâce à deux suites géométriques auxiliaires.

### Question 6.(a)

> [!INDICATION]
> Exprimez $u_{n+1}$ à l'aide de $a_{n+1}$ et $b_{n+1}$, puis remplacez-les par leurs expressions en fonction de $a_n$ et $b_n$.

#### Solution

Soit $n\in\mathbb N$.
$$\begin{aligned}
u_{n+1}&=5a_{n+1}+b_{n+1}\\
&=5(7a_n+b_n)-10a_n\\
&=25a_n+5b_n\\
&=5u_n.
\end{aligned}$$
La suite $(u_n)$ est géométrique de raison $5$, de premier terme $u_0=5a_0+b_0=1$. Donc $\boxed{u_n=5^n}$.

> [!METHODE]
> Pour prouver qu'une suite est géométrique, on établit $u_{n+1}=q\,u_n$ **pour tout $n$**, jamais sur quelques termes. Puis on donne le premier terme.

> [!JURY]
> Le rapport 2025 : « Beaucoup de candidats ont de grandes difficultés à prouver qu’une suite est géométrique. » Il cite le calcul de quelques termes et la confusion avec l'étude de $u_{n+1}-u_n$.

### Question 6.(b)

> [!INDICATION]
> Même méthode ; développez soigneusement $-2(7a_n+b_n)$.

#### Solution

Soit $n\in\mathbb N$.
$$\begin{aligned}
v_{n+1}&=-2a_{n+1}-b_{n+1}\\
&=-2(7a_n+b_n)+10a_n\\
&=-4a_n-2b_n\\
&=2v_n.
\end{aligned}$$
$(v_n)$ est géométrique de raison $2$, de premier terme $v_0=-2a_0-b_0=-1$. Donc $\boxed{v_n=-2^n}$.

### Question 6.(c)

> [!INDICATION]
> Les deux relations $u_n=5a_n+b_n$ et $v_n=-2a_n-b_n$ forment un système linéaire d'inconnues $a_n$, $b_n$.

> [!INDICATION]
> Additionnez-les pour éliminer $b_n$.

#### Solution

Soit $n\in\mathbb N$. En additionnant $u_n=5a_n+b_n$ et $v_n=-2a_n-b_n$ : $u_n+v_n=3a_n$, donc
$$a_n=\frac13(u_n+v_n)=\frac13\left(5^n-2^n\right).$$
Puis
$$\begin{aligned}
b_n&=u_n-5a_n\\
&=5^n-\tfrac53\left(5^n-2^n\right)\\
&=\tfrac13\left(5\times2^n-2\times5^n\right).
\end{aligned}$$
$$\boxed{\begin{aligned}a_n&=\tfrac13(5^n-2^n)\\ b_n&=\tfrac13(5\times2^n-2\times5^n)\end{aligned}}$$

### Question 7

> [!INDICATION]
> Hérédité : $M^{n+1}=M\,M^n$, puis remplacez $M^2$ par $7M-10I$.

#### Solution

Montrons par récurrence $\mathcal P(n)$ : $M^n=a_nM+b_nI$.

*Initialisation.* $a_0M+b_0I=0\cdot M+1\cdot I=I=M^0$.

*Hérédité.* Soit $n\in\mathbb N$ tel que $\mathcal P(n)$ soit vraie. Alors
$$\begin{aligned}
M^{n+1}&=M\,M^n=a_nM^2+b_nM\\
&=a_n(7M-10I)+b_nM\\
&=(7a_n+b_n)M-10a_nI\\
&=a_{n+1}M+b_{n+1}I.
\end{aligned}$$
*Conclusion.* $\boxed{\forall n\in\mathbb N,\ M^n=a_nM+b_nI}$.

> [!JURY]
> Le rapport 2025 dénonce « beaucoup de bluff sur l’hérédité » et la confusion entre indices et puissances ($a_{n+1}$ n'est pas $a_n\,a$). Il précise aussi que l'expression admise de $M^n$ ne doit pas servir à cette récurrence.

## Exercice 1 — Partie 3 : le chat et les trois maisons

On modélise les déplacements d'un chat par une chaîne de Markov ; la matrice de transition est $\tfrac15M$, ce qui permet d'utiliser les puissances de $M$ calculées plus haut.

### Question 8.(a)

> [!INDICATION]
> Le premier jour, le chat est dans la maison 1 ; traduisez l'énoncé pour le deuxième jour.

#### Solution

Le jour 1, le chat est dans la maison 1. Le jour 2, il reste dans la maison 1 avec probabilité $\tfrac35$, donc $\mathbb P(X_2=1)=\tfrac35$. Sinon (probabilité $\tfrac25$), il va dans l'une des maisons 2 ou 3 de façon équiprobable, donc
$$\begin{aligned}
\mathbb P(X_2=2)&=\mathbb P(X_2=3)\\
&=\frac12\times\frac25\\
&=\frac15.
\end{aligned}$$

### Question 8.(b)

> [!INDICATION]
> Formule de l'espérance d'une variable finie.

#### Solution

$$\begin{aligned}
\mathbb E(X_2)&=1\times\frac35+2\times\frac15+3\times\frac15\\
&=\frac{3+2+3}{5}\\
&=\boxed{\frac85}.
\end{aligned}$$

### Question 8.(c)

> [!INDICATION]
> Formule de König-Huygens : calculez d'abord $\mathbb E(X_2^2)$.

#### Solution

$$\mathbb E(X_2^2)=1\times\frac35+4\times\frac15+9\times\frac15=\frac{16}5.$$
Par la formule de König-Huygens,
$$\begin{aligned}
\mathbb V(X_2)&=\mathbb E(X_2^2)-\mathbb E(X_2)^2\\
&=\frac{16}5-\frac{64}{25}\\
&=\frac{80-64}{25}\\
&=\frac{16}{25}.
\end{aligned}$$
L'écart type vaut $\sigma(X_2)=\sqrt{16/25}=\boxed{\tfrac45}$.

> [!PIEGE]
> $\mathbb V(X)\ne\mathbb E(X^2)$ ; et $X_2$ ne suit pas une loi binomiale.

### Question 9.(a)

> [!INDICATION]
> Utilisez le système complet d'événements $\{[X_2=1],[X_2=2],[X_2=3]\}$.

> [!INDICATION]
> Les probabilités conditionnelles $\mathbb P_{[X_2=i]}(X_3=j)$ valent $\tfrac35$ si $i=j$ et $\tfrac15$ sinon.

#### Solution

$X_3(\Omega)=\{1,2,3\}$. La famille $([X_2=1],[X_2=2],[X_2=3])$ est un système complet d'événements de probabilités non nulles. Par la formule des probabilités totales, pour $j\in\{1,2,3\}$ :
$$\mathbb P(X_3=j)=\sum_{i=1}^{3}\mathbb P(X_2=i)\,\mathbb P_{[X_2=i]}(X_3=j).$$
- $\mathbb P(X_3=1)=\frac35\cdot\frac35+\frac15\cdot\frac15+\frac15\cdot\frac15=\frac{11}{25}$ ;
- $\mathbb P(X_3=2)=\frac35\cdot\frac15+\frac15\cdot\frac35+\frac15\cdot\frac15=\frac{7}{25}$ ;
- $\mathbb P(X_3=3)=\frac35\cdot\frac15+\frac15\cdot\frac15+\frac15\cdot\frac35=\frac{7}{25}$.

**Loi de $X_3$ : $\mathbb P(X_3=1)=\tfrac{11}{25}$, $\mathbb P(X_3=2)=\mathbb P(X_3=3)=\tfrac7{25}$** (la somme vaut bien $1$).

> [!JURY]
> Le rapport 2025 regrette que l'incompatibilité des événements et les probabilités conditionnelles ne soient pas écrites, et que certains y voient une loi uniforme ou binomiale.

### Question 9.(b)

> [!INDICATION]
> La probabilité demandée est $\mathbb P_{[X_3=3]}(X_2=2)$ : c'est une probabilité « des causes ».

> [!INDICATION]
> Formule de Bayes, avec le résultat de 9.(a) au dénominateur.

#### Solution

On cherche $\mathbb P_{[X_3=3]}(X_2=2)$. Comme $\mathbb P(X_3=3)\neq0$, la formule de Bayes donne
$$\begin{aligned}
\mathbb P_{[X_3=3]}(X_2=2)&=\frac{\mathbb P(X_2=2)\,\mathbb P_{[X_2=2]}(X_3=3)}{\mathbb P(X_3=3)}\\
&=\frac{\frac15\times\frac15}{\frac7{25}}\\
&=\boxed{\frac17}.
\end{aligned}$$

> [!PIEGE]
> $X_2$ et $X_3$ ne sont pas indépendantes : $\mathbb P([X_3=3]\cap[X_2=2])\neq\mathbb P(X_3=3)\,\mathbb P(X_2=2)$. Et une intersection porte sur des événements, jamais sur des probabilités.

### Question 10.(a)

> [!INDICATION]
> Reprenez exactement le raisonnement de 9.(a) avec $X_n$ et $X_{n+1}$.

> [!INDICATION]
> Écrivez les trois lignes, puis reconnaissez le produit matriciel $\tfrac15MC_n$.

#### Solution

Soit $n\in\mathbb N^*$.

Les événements $[X_n=1]$, $[X_n=2]$, $[X_n=3]$ forment un système complet d'événements.

Sachant $[X_n=i]$, le chat reste en $i$ avec probabilité $\tfrac35$ et va dans chacune des deux autres maisons avec probabilité $\tfrac15$.

La formule des probabilités totales donne (en convenant qu'un terme $\mathbb P(X_n=i)\,\mathbb P_{[X_n=i]}(\cdot)$ est nul si $\mathbb P(X_n=i)=0$) :
$$\begin{aligned}
\mathbb P(X_{n+1}=1)&=\tfrac35\mathbb P(X_n=1)+\tfrac15\mathbb P(X_n=2)+\tfrac15\mathbb P(X_n=3),\\
\mathbb P(X_{n+1}=2)&=\tfrac15\mathbb P(X_n=1)+\tfrac35\mathbb P(X_n=2)+\tfrac15\mathbb P(X_n=3),\\
\mathbb P(X_{n+1}=3)&=\tfrac15\mathbb P(X_n=1)+\tfrac15\mathbb P(X_n=2)+\tfrac35\mathbb P(X_n=3).
\end{aligned}$$
Matriciellement, avec $\tfrac15M=\tfrac15\begin{pmatrix}3&1&1\\1&3&1\\1&1&3\end{pmatrix}$ : $\boxed{C_{n+1}=\tfrac15MC_n}$.

> [!JURY]
> Le rapport 2025 : pour beaucoup, prouver cette égalité « revient à développer le produit » ; peu réutilisent le raisonnement fait sur $X_3$ et rares sont ceux qui écrivent proprement la formule des probabilités totales.

### Question 10.(b)

> [!INDICATION]
> Récurrence immédiate à partir de 10.(a).

#### Solution

*Initialisation* ($n=1$) : $\frac1{5^0}M^0C_1=C_1$.

*Hérédité.* Si $C_n=\frac1{5^{n-1}}M^{n-1}C_1$ pour un $n\in\mathbb N^*$, alors
$$\begin{aligned}
C_{n+1}&=\tfrac15MC_n\\
&=\tfrac15M\cdot\tfrac1{5^{n-1}}M^{n-1}C_1\\
&=\tfrac1{5^n}M^nC_1.
\end{aligned}$$
*Conclusion.* $\boxed{\forall n\in\mathbb N^*,\ C_n=\tfrac1{5^{n-1}}M^{n-1}C_1}$.

### Question 10.(c)

> [!INDICATION]
> $C_1$ est le premier vecteur de la base canonique : $M^{n-1}C_1$ est la première colonne de $M^{n-1}$.

> [!INDICATION]
> Utilisez l'expression admise de $M^n$ en remplaçant $n$ par $n-1$.

#### Solution

$C_1=\begin{pmatrix}1\\0\\0\end{pmatrix}$, donc $M^{n-1}C_1$ est la première colonne de $M^{n-1}$, soit d'après l'expression admise
$$M^{n-1}C_1=\frac13\begin{pmatrix}5^{n-1}+2^{n}\\5^{n-1}-2^{n-1}\\5^{n-1}-2^{n-1}\end{pmatrix}.$$
En divisant par $5^{n-1}$ : pour tout $n\in\mathbb N^*$, $X_n(\Omega)=\{1,2,3\}$ et
$$\boxed{\begin{aligned}\mathbb P(X_n=1)&=\frac13+\frac23\left(\frac25\right)^{n-1}\\ \mathbb P(X_n=2)=\mathbb P(X_n=3)&=\frac13-\frac13\left(\frac25\right)^{n-1}\end{aligned}}$$
Contrôles : $n=1$ donne $(1,0,0)$, $n=2$ donne $(\tfrac35,\tfrac15,\tfrac15)$ et $n=3$ donne $(\tfrac{11}{25},\tfrac7{25},\tfrac7{25})$.

> [!JURY]
> Le rapport 2025 note que de nombreux candidats cherchent absolument une loi usuelle (binomiale, uniforme, géométrique) : la loi est donnée par ses trois probabilités, qu'il faut simplifier.

### Question 11.(a)

> [!INDICATION]
> $\mathbb E(X_n)=\mathbb P(X_n=1)+2\mathbb P(X_n=2)+3\mathbb P(X_n=3)$ ; posez $q_n=(2/5)^{n-1}$.

#### Solution

Posons $q_n=(2/5)^{n-1}$.
$$\begin{aligned}
\mathbb E(X_n)&=\left(\tfrac13+\tfrac23q_n\right)+5\left(\tfrac13-\tfrac13q_n\right)\\
&=2-q_n.
\end{aligned}$$
$$\boxed{\mathbb E(X_n)=2-\left(\tfrac25\right)^{n-1}}$$
(contrôle : $n=2$ donne $\tfrac85$, comme en 8.(b)).

### Question 11.(b)

> [!INDICATION]
> Limite d'une suite géométrique de raison comprise strictement entre $-1$ et $1$.

#### Solution

Comme $-1<\tfrac25<1$, $(2/5)^{n-1}\to0$, donc $\boxed{\lim_{n\to+\infty}\mathbb E(X_n)=2}$. Les trois probabilités tendent vers $\tfrac13$ : à long terme, le chat fréquente les trois maisons de façon équilibrée.

## Exercice 1 — Partie 4 : base de données SQL

Quatre requêtes de base : projection-sélection, mise à jour, insertion, jointure. Toutes figurent au programme d'ECT (jointure en deuxième année).

### Question 12

> [!INDICATION]
> Lisez séparément la clause `SELECT` (colonnes affichées) et la clause `WHERE` (lignes retenues).

#### Solution

La requête renvoie, **pour chaque chat de couleur grise et de sexe femelle de la table `chats`, son nom et son numéro de puce.**

> [!JURY]
> Le rapport 2025 : parmi les réponses cohérentes, « la moitié oublie de mentionner que l’on projette aussi le numéro de la puce ».

### Question 13

> [!INDICATION]
> On modifie un enregistrement existant : instruction `UPDATE … SET … WHERE …`.

> [!INDICATION]
> La ligne à modifier est repérée par la clé `idprop` ; il faut changer deux attributs.

#### Solution

```sql
UPDATE propriétaires
SET nomchat = 'Niels', pucechat = 987654321
WHERE idprop = 1234;
```

> [!PIEGE]
> Sans clause `WHERE`, toute la table serait modifiée.

### Question 14

> [!INDICATION]
> On ajoute une ligne : `INSERT INTO … VALUES (…)`, valeurs dans l'ordre des attributs de la table.

#### Solution

Dans l'ordre des attributs `(idchat, nomchat, race, sexe, couleur, age, poids, puce)` :
```sql
INSERT INTO chats
VALUES (457, 'Niels', 'birmane', 'M', 'blanche', 1, 2, 987654321);
```
Le sexe est codé `'M'`, sur le modèle du `'F'` de la question 12.

### Question 15

> [!INDICATION]
> Il s'agit d'une jointure entre les deux tables.

#### Solution

```sql
SELECT chats.nomchat, race, puce, nomprop, adresse
FROM chats INNER JOIN propriétaires
ON chats.puce = propriétaires.pucechat;
```
L'énoncé écrit `chat.puce` dans la condition `ON` : il s'agit d'une coquille pour `chats.puce`, le nom de la table. Le préfixe `chats.` est nécessaire devant `nomchat`, attribut présent dans les deux tables.

> [!JURY]
> Le rapport 2025 constate que « la plupart des candidats inventent une syntaxe SQL qui leur est visiblement inconnue » : `FROM chats, propriétaires` ou `FROM chats AND propriétaires` ne conviennent pas ici, puisque la suite impose `ON`.

## Exercice 2 — Partie 1 : étude de f et g

Étude complète de $f(x)=e^x+e^{-x}$ et $g(x)=e^x-e^{-x}$ : variations, convexité, tangente, aire, puis deux inégalités polynomiales obtenues par étude de fonctions auxiliaires.

### Question 1

> [!INDICATION]
> La dérivée de $x\mapsto e^{-x}$ est $x\mapsto -e^{-x}$.

#### Solution

Pour tout $x\in\mathbb R$ :
$$\begin{aligned}
f'(x)&=e^x-e^{-x}\\
&=g(x)\\
g'(x)&=e^x+e^{-x}\\
&=f(x).
\end{aligned}$$

### Question 2.(a)

> [!INDICATION]
> Étudiez séparément les limites de $e^x$ et de $e^{-x}$.

#### Solution

En $+\infty$ : $e^x\to+\infty$ et $e^{-x}\to0$, donc $\lim_{x\to+\infty}g(x)=+\infty$.

En $-\infty$ : $e^x\to0$ et $e^{-x}\to+\infty$, donc $\lim_{x\to-\infty}g(x)=-\infty$.

> [!PIEGE]
> On n'écrit pas « $e^{+\infty}=+\infty$ » ni « $+\infty+0$ » : on énonce les limites de chaque terme, puis la limite de la somme.

### Question 2.(b)

> [!INDICATION]
> Le signe de $g'=f$ est évident.

#### Solution

Pour tout $x$, $g'(x)=f(x)=e^x+e^{-x}>0$ (somme de deux exponentielles strictement positives). **$g$ est strictement croissante sur $\mathbb R$.**

| $x$ | $-\infty$ | | $+\infty$ |
|---|---|---|---|
| $g'(x)$ | | $+$ | |
| $g$ | $-\infty$ | $\nearrow$ | $+\infty$ |

### Question 3.(a)

> [!INDICATION]
> Multipliez par $e^x>0$ ou utilisez la stricte croissance de l'exponentielle.

#### Solution

$$\begin{aligned}
g(x)=0&\iff e^x=e^{-x}\\
&\iff x=-x\\
&\iff x=0
\end{aligned}$$
la deuxième équivalence par injectivité de l'exponentielle. **L'unique solution est $x=0$.**

> [!PIEGE]
> $\ln(0)$ n'existe pas : on ne passe pas au logarithme dans $e^x-e^{-x}=0$.

### Question 3.(b)

> [!INDICATION]
> $g$ est strictement croissante et s'annule en $0$.

#### Solution

$g$ est strictement croissante et $g(0)=0$ : $g(x)<0$ si $x<0$, $g(0)=0$, $g(x)>0$ si $x>0$.

| $x$ | $-\infty$ | | $0$ | | $+\infty$ |
|---|---|---|---|---|---|
| $g(x)$ | | $-$ | $0$ | $+$ | |

### Question 3.(c)

> [!INDICATION]
> $f'=g$ : utilisez le tableau de signes précédent. Pour les limites, raisonnez comme en 2.(a).

#### Solution

Comme $f'=g$, $f$ est strictement décroissante sur $]-\infty,0]$ et strictement croissante sur $[0,+\infty[$, avec $f(0)=2$.

En $\pm\infty$, l'une des exponentielles tend vers $+\infty$ et l'autre vers $0$ : $\lim_{\pm\infty}f=+\infty$.

| $x$ | $-\infty$ | | $0$ | | $+\infty$ |
|---|---|---|---|---|---|
| $f'(x)=g(x)$ | | $-$ | $0$ | $+$ | |
| $f$ | $+\infty$ | $\searrow$ | $2$ | $\nearrow$ | $+\infty$ |

### Question 3.(d)

> [!INDICATION]
> Calculez $f''$ grâce à la question 1.

#### Solution

$f''=g'=f>0$ sur $\mathbb R$, donc **$f$ est convexe sur $\mathbb R$.**

### Question 4

> [!INDICATION]
> $g''=f'=g$, dont le signe est connu.

#### Solution

$g''=f'=g$.

D'après 3.(b), $g''<0$ sur $]-\infty,0[$ et $g''>0$ sur $]0,+\infty[$.

**$g$ est concave sur $]-\infty,0]$ et convexe sur $[0,+\infty[$** ; la courbe $\mathcal C_g$ admet un point d'inflexion en $(0,0)$.

### Question 5.(a)

> [!INDICATION]
> Équation de la tangente en $a$ : $y=g'(a)(x-a)+g(a)$.

#### Solution

$g(0)=0$ et $g'(0)=f(0)=2$, donc $\boxed{(T):\ y=2x}$.

### Question 5.(b)

> [!INDICATION]
> Une fonction convexe sur un intervalle a sa courbe au-dessus de ses tangentes sur cet intervalle ; concave : en dessous.

#### Solution

Sur $[0,+\infty[$, $g$ est convexe, donc $\mathcal C_g$ est au-dessus de ses tangentes, en particulier de $(T)$.

Sur $]-\infty,0]$, $g$ est concave, donc $\mathcal C_g$ est en dessous de $(T)$.

**$\mathcal C_g$ est sous $(T)$ pour $x\le0$, au-dessus pour $x\ge0$, et la traverse en l'origine (point d'inflexion).**

> [!JURY]
> Le rapport 2025 : « Le lien entre convexité et position relative courbe / tangente est visiblement très peu connu. »

> [!METHODE]
> Convexité et tangente : position courbe/tangente sans calcul. À défaut, étudier le signe de $x\mapsto g(x)-2x$ par sa dérivée $f(x)-2\ge0$ (car $f$ a pour minimum $2$) donne le même résultat.

### Question 5.(c)

> [!INDICATION]
> Traduisez la position relative de 5.(b) en inégalités.

#### Solution

« $\mathcal C_g$ en dessous de $(T)$ sur $]-\infty,0]$ » s'écrit $g(x)\le 2x$ pour $x\le0$ ; « au-dessus sur $[0,+\infty[$ » s'écrit $g(x)\ge 2x$ pour $x\ge0$.

### Question 6.(a)

> [!INDICATION]
> Calculez $f(x)-g(x)$.

#### Solution

$f(x)-g(x)=2e^{-x}>0$, donc **$f(x)>g(x)$, en particulier $f(x)\ge g(x)$ pour tout réel $x$.**

### Question 6.(b)

> [!INDICATION]
> Interprétez graphiquement l'inégalité de 6.(a).

#### Solution

**$\mathcal C_f$ est strictement au-dessus de $\mathcal C_g$ sur $\mathbb R$.** De plus $f(x)-g(x)=2e^{-x}\to0$ en $+\infty$ : les deux courbes se rapprochent en $+\infty$.

### Question 7

> [!INDICATION]
> Placez les éléments sûrs : minimum de $f$ en $(0,2)$, point d'inflexion de $\mathcal C_g$ en l'origine, tangente $y=2x$, position relative des trois courbes.

#### Solution

Allure (axes gradués) : $\mathcal C_f$ en « U », minimum $(0,2)$, symétrique par rapport à l'axe des ordonnées ($f$ est paire) ;

$\mathcal C_g$ croissante, symétrique par rapport à l'origine ($g$ est impaire), sous $\mathcal C_f$, traversant $(T)$ en l'origine.

![Figure 1 — Courbes Cf (eˣ + e⁻ˣ) et Cg (eˣ − e⁻ˣ), tangente (T) d'équation y = 2x à Cg en 0, et aire A hachurée entre (T) et Cf pour x entre 0 et 1](figures/ex2-q7-courbes-f-g-tangente.svg)

> [!JURY]
> Le rapport 2025 : « Dans un tracé de courbe, les axes devraient être gradués et fléchés. » La droite $(T)$ doit être tangente à $\mathcal C_g$ en l'origine.

### Question 8.(a)

> [!INDICATION]
> La surface est entre la droite $(T)$ (en bas) et $\mathcal C_f$ (en haut), pour $x$ entre $0$ et $1$.

#### Solution

C'est la zone hachurée de la figure 1 : comprise entre la droite $y=2x$ en dessous, $\mathcal C_f$ au-dessus, et les droites $x=0$ et $x=1$.

### Question 8.(b)

> [!INDICATION]
> L'aire sous une courbe positive est une intégrale ; une primitive de $f$ est $g$.

#### Solution

$f$ est continue et positive sur $[0,1]$, donc l'aire cherchée vaut
$$\begin{aligned}
\int_0^1f(x)\,dx&=\big[g(x)\big]_0^1\\
&=g(1)-g(0)\\
&=\boxed{e-e^{-1}}\ \text{u.a.}
\end{aligned}$$

> [!JURY]
> Le rapport 2025 : « La positivité de f n’a jamais été évoquée par les quelques candidats qui ont lancé un calcul intégral. »

### Question 8.(c)

> [!INDICATION]
> Il faut savoir laquelle des deux courbes est au-dessus de l'autre sur $[0,1]$.

> [!INDICATION]
> Pour $x\in[0,1]$, combinez les inégalités des questions 5.(c) et 6.(a).

#### Solution

Pour $x\in[0,1]$, $f(x)\ge g(x)\ge 2x$ (questions 6.(a) et 5.(c)). L'aire entre $(T)$ et $\mathcal C_f$ vaut donc
$$\begin{aligned}
A&=\int_0^1\big(f(x)-2x\big)\,dx\\
&=\int_0^1f(x)\,dx-\big[x^2\big]_0^1\\
&=e-e^{-1}-1.
\end{aligned}$$
$$\boxed{A=e-\tfrac1e-1\ \text{u.a.}}\quad(\approx1{,}35)$$

### Question 9.(a)

> [!INDICATION]
> Utilisez $f'=g$.

#### Solution

$h'(x)=f'(x)-2x=\boxed{g(x)-2x}$.

### Question 9.(b)

> [!INDICATION]
> Le signe de $h'$ vient de 5.(c).

> [!INDICATION]
> Dressez le tableau de variations de $h$ et calculez $h(0)$.

#### Solution

D'après 5.(c), $h'(x)=g(x)-2x\le0$ pour $x\le0$ et $h'(x)\ge0$ pour $x\ge0$.

Donc $h$ est décroissante sur $]-\infty,0]$ et croissante sur $[0,+\infty[$ : elle admet en $0$ un minimum global, $h(0)=f(0)-2=0$.

Ainsi $h(x)\ge0$ pour tout $x$, c'est-à-dire $\boxed{f(x)\ge 2+x^2}$.

> [!JURY]
> Le rapport 2025 : quand elle est traitée, la question « se résume à une succession d’inégalités sans lien entre elles ». Il faut passer par les variations de $h$.

### Question 9.(c)

> [!INDICATION]
> $g'=f$ et la dérivée de $\tfrac13x^3$ est $x^2$.

#### Solution

$$\begin{aligned}
k'(x)&=g'(x)-2-\tfrac13\times3x^2\\
&=\boxed{f(x)-2-x^2=h(x)}.
\end{aligned}$$

### Question 9.(d)

> [!INDICATION]
> Le signe de $k'$ vient de 9.(b) ; calculez $k(0)$.

#### Solution

D'après 9.(b), $k'=h\ge0$ : $k$ est croissante sur $\mathbb R$, et $k(0)=g(0)=0$.

Donc $k(x)\le0$ pour $x\le0$ et $k(x)\ge0$ pour $x\ge0$, soit
$$\begin{aligned}
\forall x\le0,\ g(x)&\le 2x+\tfrac13x^3\\
\forall x\ge0,\ g(x)&\ge 2x+\tfrac13x^3.
\end{aligned}$$

## Exercice 2 — Partie 2 : la suite définie par g(uₙ) = 1/n

Une suite définie implicitement : existence par le théorème de la bijection, encadrement, monotonie par la croissance de $g$, puis approximation par dichotomie.

### Question 10

> [!INDICATION]
> Théorème de la bijection : continuité, stricte monotonie, et image de $\mathbb R$ par $g$.

#### Solution

$g$ est continue et strictement croissante sur l'intervalle $\mathbb R$, avec $\lim_{-\infty}g=-\infty$ et $\lim_{+\infty}g=+\infty$.

Par le théorème de la bijection, $g$ réalise une bijection de $\mathbb R$ sur $]-\infty,+\infty[=\mathbb R$.

Comme $\frac1n\in\mathbb R$, **l'équation $g(x)=\frac1n$ admet une unique solution réelle.**

> [!JURY]
> Le rapport 2025 : « Beaucoup ne voient pas qu’on attend ici le théorème de la bijection ». Les arguments oubliés sont la stricte monotonie et l'appartenance de $\frac1n$ à $g(\mathbb R)$.

### Question 11

> [!INDICATION]
> Comparez $g(0)$, $g(u_1)=1$ et $g(1)$, puis utilisez la stricte croissance de $g$.

#### Solution

$g(0)=0$, $g(u_1)=1$ et $g(1)=e-e^{-1}\simeq2{,}7-0{,}4=2{,}3$. Ainsi $g(0)<g(u_1)<g(1)$. Comme $g$ est strictement croissante, sa bijection réciproque l'est aussi, d'où $\boxed{0<u_1<1}$.

### Question 12

> [!INDICATION]
> Même argument : comparez $g(u_n)$ à $g(0)$.

#### Solution

Soit $n\in\mathbb N^*$. $g(u_n)=\frac1n>0=g(0)$, et $g$ est strictement croissante, donc $u_n>0$.

> [!PIEGE]
> Une récurrence est inutile : l'argument vaut directement pour chaque $n$.

### Question 13.(a)

> [!INDICATION]
> Comparez $g(u_{n+1})$ et $g(u_n)$, pas $u_{n+1}$ et $u_n$ directement.

#### Solution

Soit $n\in\mathbb N^*$. $g(u_{n+1})=\frac1{n+1}<\frac1n=g(u_n)$. Comme $g$ est strictement croissante, $u_{n+1}<u_n$. **La suite $(u_n)$ est (strictement) décroissante.**

> [!JURY]
> Le rapport 2025 signale la confusion entre $u_{n+1}-u_n$ et $g(u_{n+1})-g(u_n)$.

### Question 13.(b)

> [!INDICATION]
> Théorème de la limite monotone.

#### Solution

$(u_n)$ est décroissante et minorée par $0$ (question 12). Par le théorème de la limite monotone, **$(u_n)$ converge** (vers une limite $\ell\ge0$).

### Question 14.(a)

> [!INDICATION]
> Structure `def … : return …` ; l'exponentielle est `np.exp`.

#### Solution

```python
def d(x, n):
    return np.exp(x) - np.exp(-x) - 1/n
```

> [!JURY]
> Le rapport 2025 : « La syntaxe def / return est largement ignorée. »

### Question 14.(b)

> [!INDICATION]
> La $k$-ième case (indice `k`) contient $u_{k+1}$, solution de $d(x,k+1)=0$ ; d'après 11 et 13.(a), elle est dans $]0,1[$.

> [!INDICATION]
> Dichotomie : si $d$ change de signe entre `a` et `c`, la racine est dans $[a,c]$ ; sinon elle est dans $[c,b]$.

#### Solution

```python
def SuiteU(n):
    U = np.zeros(n)
    for k in range(n):
        a = 0 ; b = 1
        while b - a > 10**(-3):
            c = (a + b)/2
            if d(a, k+1)*d(c, k+1) < 0:
                b = c
            else:
                a = c
        U[k] = (a + b)/2
    return U
```
Justification : pour $k+1\ge1$, $u_{k+1}\in]0,1[$ (questions 11, 12 et 13.(a)), et $x\mapsto d(x,k+1)$ est strictement croissante, négative en $0$, positive en $1$.

L'invariant « $u_{k+1}\in[a,b]$ » est conservé ; à la sortie $b-a\le10^{-3}$, donc $\frac{a+b}2$ approche $u_{k+1}$ à $10^{-3}$ près (et même $5\times10^{-4}$).

Essai pour $n=5$ : `[0.481, 0.248, 0.166, 0.125, 0.100]`, conforme aux valeurs exactes $u_n=\ln\!\big(\tfrac1{2n}+\sqrt{1+\tfrac1{4n^2}}\big)$ à $10^{-3}$ près.

La fonction renvoie un tableau `numpy`, ce que l'énoncé appelle une liste.

### Question 14.(c)

> [!INDICATION]
> Lisez le graphique : vers quelle ordonnée les points se rapprochent-ils ?

#### Solution

Les points se rapprochent de l'axe des abscisses : **on conjecture que $\lim_{n\to+\infty}u_n=0$.** (C'est bien le cas : si $u_n\to\ell$, la continuité de $g$ donne $g(\ell)=\lim\frac1n=0$, donc $\ell=0$ par 3.(a).)

## Exercice 3 — Partie 1 : loi exponentielle et simulation

Rappels de cours sur les lois exponentielle et uniforme, puis la méthode d'inversion : $-\ln U$ suit la loi $\mathcal E(1)$.

### Question 1.(a)

> [!INDICATION]
> Question de cours : loi $\mathcal E(\lambda)$ avec $\lambda=1$.

#### Solution

Une densité de $T$ est
$$f_T(x)=\begin{cases}e^{-x}&\text{si }x\ge0\\0&\text{si }x<0\end{cases}$$
et $\mathbb E(T)=1$, $\mathbb V(T)=1$ (pour $\mathcal E(\lambda)$ : $\frac1\lambda$ et $\frac1{\lambda^2}$).

> [!JURY]
> Le rapport 2025 : « Cette question de cours n’est pas réussi à la hauteur des attentes. »

### Question 1.(b)

> [!INDICATION]
> Question de cours.

#### Solution

$$F_T(x)=\begin{cases}0&\text{si }x<0\\1-e^{-x}&\text{si }x\ge0\end{cases}$$

### Question 1.(c)

> [!INDICATION]
> Utilisez $F_T$.

#### Solution

$$\mathbb P(T\le3)=F_T(3)=\boxed{1-e^{-3}}.$$

### Question 1.(d)

> [!INDICATION]
> L'événement conditionnant est $[T\ge1]$ ; l'événement étudié est $[T\ge2]$.

#### Solution

On cherche $\mathbb P_{[T\ge1]}(T\ge2)$. Comme $[T\ge2]\subset[T\ge1]$ et $\mathbb P(T\ge1)=e^{-1}\neq0$ :
$$\begin{aligned}
\mathbb P_{[T\ge1]}(T\ge2)&=\frac{\mathbb P(T\ge2)}{\mathbb P(T\ge1)}\\
&=\frac{e^{-2}}{e^{-1}}\\
&=\boxed{e^{-1}}.
\end{aligned}$$
C'est aussi $\mathbb P(T\ge1)$ : la loi exponentielle est « sans mémoire ».

> [!JURY]
> Le rapport 2025 : « Une réaction des candidats est attendue quand ils trouvent une probabilité négative. »

### Question 2.(a)

> [!INDICATION]
> Loi uniforme sur $]a,b[$ avec $a=0$, $b=1$.

#### Solution

$$f_U(x)=\begin{cases}1&\text{si }x\in]0,1[\\0&\text{sinon}\end{cases},\qquad F_U(x)=\begin{cases}0&\text{si }x<0\\x&\text{si }0\le x\le1\\1&\text{si }x>1\end{cases}$$

### Question 2.(b)

> [!INDICATION]
> $U$ prend ses valeurs dans $]0,1[$, donc $\ln U$ est défini. Utilisez la croissance stricte de l'exponentielle.

#### Solution

Soit $x\in\mathbb R$. Comme $U>0$ :
$$\begin{aligned}
X\le x&\iff-\ln U\le x\\
&\iff\ln U\ge-x\\
&\iff U\ge e^{-x}
\end{aligned}$$
la dernière équivalence parce que $\exp$ et $\ln$ sont strictement croissantes. Les événements sont égaux, d'où $\mathbb P(X\le x)=\mathbb P(U\ge e^{-x})$.

> [!JURY]
> Le rapport 2025 : « Certains confondent la positivité de la fonction exponentielle et sa croissance (utilisée ici). »

### Question 2.(c)

> [!INDICATION]
> Comparez $e^{-x}$ à $1$.

#### Solution

Si $x<0$, $e^{-x}>1$. Comme $U<1$, l'événement $[U\ge e^{-x}]$ est impossible : $\mathbb P(X\le x)=0$.

### Question 2.(d)

> [!INDICATION]
> Pour $x\ge0$, passez à l'événement contraire et utilisez $F_U$ en $e^{-x}\in]0,1]$.

#### Solution

Soit $x\ge0$. Alors $e^{-x}\in]0,1]$ et, $U$ étant à densité, $\mathbb P(U=e^{-x})=0$ :
$$\begin{aligned}
\mathbb P(X\le x)&=1-\mathbb P(U<e^{-x})\\
&=1-F_U(e^{-x})\\
&=1-e^{-x}.
\end{aligned}$$
Donc $F_X(x)=0$ si $x<0$ et $F_X(x)=1-e^{-x}$ si $x\ge0$ : **$X$ suit la loi exponentielle de paramètre $1$**, de densité $x\mapsto e^{-x}$ sur $[0,+\infty[$ et $0$ ailleurs (dérivée de $F_X$ sauf en $0$).

### Question 2.(e)

> [!INDICATION]
> D'après 2.(d), $-\ln U$ a la même loi que $T$ ; `rd.random()` simule une loi uniforme.

#### Solution

```python
def SimulT():
    U = rd.random()
    return -np.log(1 - U)
```
`rd.random()` renvoie un réel de $[0,1[$ ;

$1-U$ suit aussi une loi uniforme et ne vaut jamais $0$, ce qui évite $\ln 0$.

D'après 2.(d), le résultat suit la loi $\mathcal E(1)$, comme $T$. (Essai : la moyenne de $10^5$ simulations vaut environ $1{,}00$.) On peut aussi écrire `return rd.exponential(1)`.

## Exercice 3 — Partie 2 : les intégrales Iₙ

Par intégration par parties et passage à la limite, on montre que $I_n=\int_0^{+\infty}x^{n-1}e^{-x}\,dx$ converge et vaut $(n-1)!$.

### Question 3.(a)

> [!INDICATION]
> Une primitive de $e^{-x}$ est $-e^{-x}$.

#### Solution

$$\begin{aligned}
I_1(A)&=\int_0^Ae^{-x}\,dx\\
&=\big[-e^{-x}\big]_0^A\\
&=\boxed{1-e^{-A}}.
\end{aligned}$$

> [!JURY]
> Le rapport 2025 : « Il n’y avait pas de limite à calculer à cette question. »

### Question 3.(b)

> [!INDICATION]
> Définition d'une intégrale impropre convergente : limite finie de $I_1(A)$.

#### Solution

$e^{-A}\to0$ quand $A\to+\infty$, donc $I_1(A)\to1$ : **l'intégrale $I_1$ converge et vaut $1$.**

### Question 4

> [!INDICATION]
> Partez de $I_{n+1}(A)=\int_0^Ax^ne^{-x}\,dx$ ; dérivez $x^n$ et primitivez $e^{-x}$.

#### Solution

Soit $A>0$ et $n\in\mathbb N^*$.

On pose $u(x)=x^n$, $v(x)=-e^{-x}$, de classe $\mathcal C^1$ sur $[0,A]$, avec $u'(x)=nx^{n-1}$ et $v'(x)=e^{-x}$.

Par intégration par parties :
$$\begin{aligned}
I_{n+1}(A)&=\big[-x^ne^{-x}\big]_0^A+n\int_0^Ax^{n-1}e^{-x}\,dx\\
&=-A^ne^{-A}+0+nI_n(A),
\end{aligned}$$
car $0^n=0$ pour $n\ge1$. Donc $\boxed{I_{n+1}(A)=-\dfrac{A^n}{e^A}+nI_n(A)}$.

### Question 5

> [!INDICATION]
> Croissances comparées pour $\frac{A^n}{e^A}$.

#### Solution

Supposons que $I_n(A)\to L\in\mathbb R$ quand $A\to+\infty$. Par croissances comparées, $\frac{A^n}{e^A}\to0$. D'après la question 4, $I_{n+1}(A)\to 0+nL=nL$ : **$I_{n+1}(A)$ admet une limite finie.**

> [!PIEGE]
> Il s'agit de la limite en $A$ (convergence de l'intégrale), pas d'une limite de la suite $(I_n)$ quand $n\to+\infty$.

### Question 6

> [!INDICATION]
> Récurrence : l'initialisation est 3.(b), l'hérédité est 5.

#### Solution

*Initialisation.* $I_1$ converge (3.(b)).

*Hérédité.* Si $I_n$ converge pour un $n\in\mathbb N^*$, alors $I_n(A)$ a une limite finie quand $A\to+\infty$, donc $I_{n+1}(A)$ aussi (question 5) : $I_{n+1}$ converge.

*Conclusion.* Pour tout $n\in\mathbb N^*$, $I_n$ converge. En passant à la limite $A\to+\infty$ dans la relation de la question 4 (les trois termes ont une limite finie) :
$$\boxed{\forall n\in\mathbb N^*,\ I_{n+1}=nI_n}.$$

### Question 7

> [!INDICATION]
> Récurrence avec la relation de la question 6.

#### Solution

Récurrence. $I_1=1=0!$. Si $I_n=(n-1)!$, alors $I_{n+1}=nI_n=n\,(n-1)!=n!$. Donc $\boxed{\forall n\in\mathbb N^*,\ I_n=(n-1)!}$.

## Exercice 3 — Partie 3 : lois gamma et estimation

Les fonctions $f_n$ sont les densités des lois gamma d'entier $n$ ; on calcule l'espérance, puis on estime $n$ par une moyenne empirique contrôlée par l'inégalité de Bienaymé-Tchebychev.

### Question 8

> [!INDICATION]
> Trois points : positivité, continuité sauf en un nombre fini de points, intégrale égale à $1$.

> [!INDICATION]
> L'intégrale sur $[0,+\infty[$ se ramène à $I_n$.

#### Solution

Soit $n\in\mathbb N^*$.
- $f_n\ge0$ sur $\mathbb R$ ($x^{n-1}\ge0$ et $e^{-x}>0$ pour $x\ge0$).
- $f_n$ est continue sur $]-\infty,0[$ (nulle) et sur $]0,+\infty[$ (produit de fonctions continues) : elle est continue sur $\mathbb R$ sauf peut-être en $0$.
- $\int_{-\infty}^0f_n=0$ et, d'après 6 et 7, $\int_0^{+\infty}f_n(x)\,dx=\frac{I_n}{(n-1)!}=1$ : l'intégrale $\int_{-\infty}^{+\infty}f_n$ converge et vaut $1$.

**$f_n$ est une densité de probabilité.**

> [!PIEGE]
> Pour $n=1$, $f_1$ est discontinue en $0$ : on ne peut pas affirmer la continuité sur $\mathbb R$ entier, et ce n'est d'ailleurs pas nécessaire.

> [!JURY]
> Le rapport 2025 relève que trop de candidats affirment la continuité sur $\mathbb R$ sans rien vérifier en $0$, et que quasiment aucun candidat ne fait le lien entre l'intégrale et la valeur de $I_n$ obtenue à la question 7.

### Question 9.(a)

> [!INDICATION]
> Il faut montrer la convergence de $\int_{-\infty}^{+\infty}xf_n(x)\,dx$ ; sur $[0,+\infty[$, reconnaissez $I_{n+1}$.

#### Solution

$xf_n(x)=0$ pour $x<0$ et, pour $x\ge0$, $xf_n(x)=\frac{1}{(n-1)!}x^ne^{-x}\ge0$.

D'après 6, $I_{n+1}$ converge, donc $\int_{-\infty}^{+\infty}xf_n(x)\,dx$ converge (absolument, l'intégrande étant positif) : $Y$ admet une espérance, et
$$\begin{aligned}
\mathbb E(Y)&=\frac{I_{n+1}}{(n-1)!}\\
&=\frac{n!}{(n-1)!}\\
&=\boxed{n}.
\end{aligned}$$

### Question 9.(b)

> [!INDICATION]
> Linéarité de l'espérance ; pour la variance, indépendance des $Y_k$ et $\mathbb V(aZ)=a^2\mathbb V(Z)$.

#### Solution

Par linéarité de l'espérance :
$$\begin{aligned}
\mathbb E(F_N)&=\frac1N\sum_{k=1}^N\mathbb E(Y_k)\\
&=\frac1N\times Nn\\
&=\boxed{n}.
\end{aligned}$$
Les $Y_k$ étant indépendantes, la variance de leur somme est la somme des variances :
$$\begin{aligned}
\mathbb V(F_N)&=\frac1{N^2}\sum_{k=1}^N\mathbb V(Y_k)\\
&=\frac{Nn}{N^2}\\
&=\boxed{\frac nN}.
\end{aligned}$$

> [!JURY]
> Le rapport 2025 : des candidats « négligent de préciser les propriétés utilisées (linéarité de l’espérance, indépendance des variables) ».

> [!PIEGE]
> Ne pas confondre $n$ (paramètre de la loi) et $N$ (taille de l'échantillon).

### Question 9.(c)

> [!INDICATION]
> Appliquez l'inégalité rappelée à $X=F_N$ avec les résultats de 9.(b).

#### Solution

$F_N$ admet une espérance $n$ et une variance $\frac nN$. Par l'inégalité de Bienaymé-Tchebychev, pour tout $\varepsilon>0$ :
$$\boxed{\mathbb P\big(|F_N-n|\ge\varepsilon\big)\le\frac{n}{N\varepsilon^2}}.$$

### Question 9.(d)

> [!INDICATION]
> D'après 9.(c), $F_N$ se concentre autour de $n$ quand $N$ grandit.

#### Solution

D'après 9.(c), $\mathbb P(|F_N-n|\ge\varepsilon)\to0$ quand $N\to+\infty$ : pour $N$ grand, $F_N$ est proche de $n$ avec une forte probabilité.

Sur le graphique, $F_N$ se stabilise autour de $3$.

On estime donc $\boxed{n=3}$ (c'est un entier, ce qui conforte la lecture).

### Question 9.(e)

> [!INDICATION]
> Ces intervalles sont aléatoires : quel est le niveau de confiance garanti par 9.(c) ?

> [!INDICATION]
> Calculez $\frac{n}{N\varepsilon^2}$ pour $n=3$, $N=600$, $\varepsilon=\frac1{10}$.

#### Solution

Chaque intervalle est $[F_N-\varepsilon,F_N+\varepsilon]$, calculé à partir d'une réalisation de $F_N$ : c'est un intervalle **aléatoire**. Il contient $n$ si et seulement si $|F_N-n|\le\varepsilon$. D'après 9.(c), la probabilité qu'il ne contienne pas $n$ vérifie
$$\mathbb P\big(|F_N-n|>\varepsilon\big)\le\frac{3}{600\times\frac1{100}}=\frac12.$$
Le niveau de confiance garanti n'est que de $50\,\%$ : il est normal que certains intervalles ne contiennent pas $n=3$. Sur le graphique, trois intervalles sur dix (le 5ᵉ, le 6ᵉ et le 9ᵉ) sont entièrement au-dessus de $3$, ce qui est compatible avec cette majoration. Pour diminuer ce risque, il faut augmenter $N$ ou élargir l'intervalle.

> [!JURY]
> Le rapport 2025 : question « très peu traitée et avec un baratin incompréhensible ». Une réponse courte s'appuyant sur 9.(c) suffit.

## Bilan

**Méthodes à retenir.**
- Polynôme annulateur : il donne les valeurs propres *possibles* ; on confirme avec des vecteurs propres explicites. Inversibilité : exhiber une matrice $Q$ telle que $QP=\lambda I$.
- Récurrence matricielle : $M^{n+1}=M^nM$, en ne faisant commuter que les scalaires ; initialisation avec $M^0=I$.
- Suites couplées : combinaisons géométriques $u_n$, $v_n$, puis résolution d'un système $2\times2$.
- Chaîne de Markov : formule des probabilités totales sur le système complet $([X_n=i])_i$, écriture matricielle $C_{n+1}=AC_n$, puis $C_n=A^{n-1}C_1$.
- Convexité et tangente : position courbe/tangente sans calcul ; inégalités par étude d'une fonction différence.
- Suite implicite $g(u_n)=\frac1n$ : bijection, comparaison des images, limite monotone, dichotomie.
- Intégrales $\int_0^{+\infty}x^{n-1}e^{-x}\,dx$ : intégration par parties sur $[0,A]$, croissances comparées, passage à la limite, récurrence.
- Moyenne empirique : $\mathbb E(F_N)=n$, $\mathbb V(F_N)=\frac nN$, puis Bienaymé-Tchebychev.

**À revoir si besoin.** Syntaxe SQL (`UPDATE`, `INSERT INTO`, `INNER JOIN … ON`), syntaxe Python `def`/`return`, densités et fonctions de répartition des lois usuelles, rédaction d'une récurrence en trois étapes titrées.

**Questions transposables.** Puissances d'une matrice $aI+bJ$ ; marche aléatoire sur trois états ; simulation par inversion $-\ln U$ ; fonction gamma et lois gamma ; intervalle de confiance par Bienaymé-Tchebychev.
