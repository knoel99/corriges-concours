# CCINP MPI — Maths 2 2024 · Corrigé guidé

*Corrigé rédigé par IA, non officiel. Signalez toute erreur.*

## Présentation du sujet

L’épreuve dure quatre heures, sans calculatrice. Elle propose deux exercices et un problème indépendants qui couvrent la réduction des matrices, les séries de fonctions et les matrices symétriques définies positives.

- **Q1–Q2.** Diagonaliser une matrice, puis étudier une récurrence vectorielle dans la base propre.
- **Q3–Q7.** Déterminer le domaine et la continuité de la somme d’une série, puis étudier ses limites par convergence uniforme et comparaison série-intégrale.
- **Q8–Q14.** Caractériser la définie-positivité par le spectre et en déduire un test par trace et déterminant en dimension deux. Appliquer ce test à une hessienne.
- **Q15–Q22.** Prouver le critère de Sylvester et l’utiliser sur des matrices et des formes quadratiques, jusqu’au cas d’une famille tridiagonale.

Les outils du programme MPI sont la réduction, le théorème spectral, les déterminants, la convergence normale d’une série de fonctions, les intégrales impropres et la formule de Taylor-Young à deux variables. Le rapport juge le sujet abordable et de longueur raisonnable. Dans les deux exercices, sécurisez d’abord la base propre et le domaine de convergence. Dans le problème, réservez du temps à la récurrence de Q17–Q18 et aux deux développements de déterminant de Q22. Si ce dernier calcul vous arrête, la vérification directe d’une forme quadratique reste envisageable.

[Sujet officiel](https://www.concours-commun-inp.fr/_resource/annales%20%C3%A9crits/2024/MPI/2024_MPI3M2.pdf?download=true) · [Rapport du jury 2024](https://www.concours-commun-inp.fr/_resource/annales%20%C3%A9crits/2024/MPI/MPI_ECRIT_Maths_2_2024.pdf?download=true) · [Programme MPI, annexe officielle](https://cache.media.education.gouv.fr/file/31/21/2/ensecsup756_annexes_1417212.pdf)


## Exercice 1

Une base propre découple le système de récurrences. Les coordonnées dans cette base permettent de distinguer les composantes compatibles avec une limite.

### Question 1

> [!INDICATION]
> Cherchez des valeurs entières candidates, puis calculez les espaces propres associés.

> [!INDICATION]
> Une opération sur les lignes de $A-\lambda I$ peut rendre visible la dimension du noyau. Vérifiez ensuite l’indépendance des colonnes de la matrice de passage.

#### Solution

Posons $p_1=(1,1,0)^{\mathsf T}$, $p_2=(-1,0,1)^{\mathsf T}$ et $p_3=(2,6,1)^{\mathsf T}$.

La multiplication par $A$ donne $Ap_1=-2p_1$, $Ap_2=-2p_2$ et $Ap_3=p_3$. La matrice de colonnes $p_1,p_2,p_3$ a pour déterminant $-3$. Ces trois vecteurs propres forment donc une base.

$$
\boxed{P=\begin{pmatrix}1&-1&2\\1&0&6\\0&1&1\end{pmatrix},\qquad
P^{-1}AP=\operatorname{diag}(-2,-2,1).}
$$

> [!JURY]
> Le rapport 2024 conseille de contrôler le calcul du spectre avec la trace. Additionnez les valeurs propres comptées avec leur multiplicité.

> [!METHODE]
> Pour retrouver les deux premiers vecteurs, remarquez que les lignes de $A+2I_3$ sont proportionnelles. Une seule équation suffit à décrire son noyau. Ensuite, la trace $-3$ et les deux occurrences de $-2$ donnent la valeur propre restante.

### Question 2

> [!INDICATION]
> Écrivez le système sous forme matricielle et passez aux coordonnées de l’énoncé.

> [!INDICATION]
> Séparez les coordonnées dont les suites géométriques peuvent converger. Traduisez la condition directement sur la position de $X_0$ dans la base de vecteurs propres.

#### Solution

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

> [!JURY]
> Le rapport 2024 signale des calculs d’inverse coûteux. L’égalité $X_0=PY_0$ suffit pour revenir aux conditions sur les coordonnées initiales.

## Exercice 2

La série a des comportements très différents près de zéro et vers l’infini. On travaille d’abord à distance de zéro, puis un encadrement par une intégrale fournit l’ordre de grandeur près de zéro.

### Question 3

> [!INDICATION]
> Commencez par regarder si le terme général tend vers zéro.

> [!INDICATION]
> Quand $x>0$, testez la comparaison avec une série de Riemann en posant $u=\sqrt n$.

#### Solution

Si $x=0$, le terme général vaut $1$. Si $x<0$, il tend vers $+\infty$. Dans les deux cas, il ne tend pas vers zéro, donc la série diverge.

Si $x>0$, on a, par croissances comparées,

$$
n^2e^{-x\sqrt n}=(\sqrt n)^4e^{-x\sqrt n}\longrightarrow 0.
$$

Pour $n$ assez grand, on a donc $0\le e^{-x\sqrt n}\le n^{-2}$. La série de Riemann correspondante converge. Par comparaison, **$D=]0,+\infty[$**.

> [!JURY]
> Le rapport 2024 relève que des copies omettent de justifier la divergence en dehors du domaine proposé. Traitez explicitement $x=0$ et $x<0$.

### Question 4

> [!INDICATION]
> Pour majorer le terme indépendamment de $x$, travaillez à distance positive de zéro.

> [!INDICATION]
> Sur $[a,+\infty[$, utilisez la monotonie de chaque terme par rapport à $x$ et la convergence de la série trouvée précédemment.

#### Solution

Fixons $a>0$. Toute fonction $x\mapsto e^{-x\sqrt n}$ est continue et, pour $x\ge a$, elle vérifie $|e^{-x\sqrt n}|\le e^{-a\sqrt n}$.

La série des majorants converge par la question 3. La série de fonctions converge donc normalement, donc uniformément, sur $[a,+\infty[$. Sa somme y est continue. Tout $x>0$ appartient à l’intérieur d’un tel intervalle. **$f$ est continue sur $D$.**

> [!JURY]
> Le rapport 2024 signale des affirmations injustifiées de convergence uniforme sur tout le domaine. Pour la continuité, chaque abscisse positive peut être entourée d’un intervalle où la convergence normale est démontrée.

> [!PIEGE]
> Sur tout $D$, le supremum de $e^{-x\sqrt n}$ vaut $1$ pour chaque $n$. Les termes ne tendent donc pas uniformément vers zéro, ce qui exclut la convergence uniforme de la série sur $D$.

### Question 5

> [!INDICATION]
> Utilisez un intervalle sur lequel la convergence uniforme est acquise avant de chercher la limite de la somme.

> [!INDICATION]
> Inspectez séparément le comportement du premier terme.

#### Solution

Sur $[a,+\infty[$, avec $a>0$, la convergence uniforme établie à la question 4 et l’existence des limites de chaque terme autorisent le passage à la limite dans la somme. Le terme d’indice zéro vaut $1$, et chacun des autres termes tend vers $0$.

$$
\boxed{\lim_{x\to+\infty}f(x)=1.}
$$

> [!JURY]
> Le rapport 2024 relève des oublis du terme d’indice zéro et rappelle l’importance du domaine de convergence uniforme employé.

### Question 6

> [!INDICATION]
> Sur un intervalle de longueur un, comparez la fonction aux deux valeurs prises à ses extrémités.

> [!INDICATION]
> Sommez les inégalités jusqu’à un entier fini. Repérez ensuite quel terme ne se retrouve que d’un côté.

#### Solution

Pour $x>0$, la fonction $g(t)=e^{-x\sqrt t}$ est décroissante sur $[0,+\infty[$. Pour tout $k\ge0$,

$$
g(k+1)\le\int_k^{k+1}g(t)\,\mathrm dt\le g(k).
$$

En sommant de $k=0$ à $N-1$, on obtient

$$
\begin{gathered}
\sum_{k=1}^{N}g(k)\le\int_0^Ng(t)\,\mathrm dt\\
\int_0^Ng(t)\,\mathrm dt\le\sum_{k=0}^{N-1}g(k).
\end{gathered}
$$

L’intégrale est croissante en sa borne supérieure et majorée par $f(x)$ aux entiers $N$, donc aussi à toute borne réelle positive. Elle converge. En passant à la limite dans l’encadrement, puis en utilisant $g(0)=1$, on trouve

$$
\boxed{\int_0^{+\infty}e^{-x\sqrt t}\,\mathrm dt
\le f(x)\le 1+\int_0^{+\infty}e^{-x\sqrt t}\,\mathrm dt.}
$$

> [!JURY]
> Le rapport 2024 demande une preuve précise, puisque l’encadrement est donné. Le passage à la limite requiert en particulier de justifier la convergence de l’intégrale.

### Question 7

> [!INDICATION]
> Éliminez la racine carrée de l’exponentielle par un changement de variable.

> [!INDICATION]
> Faites apparaître le paramètre $x$ comme un facteur devant une intégrale indépendante de $x$. Une intégration par parties donne la valeur de celle-ci.

#### Solution

Le changement de variable $t=u^2/x^2$, d’abord sur un intervalle borné, ramène l’intégrale de la question 6 à

$$
\int_0^{+\infty}e^{-x\sqrt t}\,\mathrm dt
=\frac{2}{x^2}\int_0^{+\infty}u e^{-u}\,\mathrm du.
$$

Une primitive de $u e^{-u}$ est $-(u+1)e^{-u}$. Comme $(u+1)e^{-u}\to0$ quand $u\to+\infty$, l’intégrale en $u$ vaut $1$.

La question 6 donne alors $1\le (x^2/2)f(x)\le1+x^2/2$. Par encadrement,

$$
\boxed{f(x)\sim\frac{2}{x^2}\qquad(x\to0^+).}
$$

> [!JURY]
> Le rapport 2024 insiste sur le calcul de l’intégrale. Pour obtenir l’équivalent, normalisez ensuite l’encadrement pour que les deux bornes aient la même limite.

## Problème

La question 8 part de la définition. Elle prépare trois manières de tester la définie-positivité en fonction des informations disponibles sur la matrice.

### Question 8

> [!INDICATION]
> Développez la forme quadratique, puis complétez un carré.

#### Solution

Pour $X=(x,y)^{\mathsf T}$,

$$
X^{\mathsf T}AX=2x^2+2xy+y^2=x^2+(x+y)^2.
$$

Cette somme de carrés ne s’annule que si $x=0$ et $x+y=0$, donc si $X=0$. **$A$ est définie positive.**

> [!JURY]
> Le rapport 2024 relève des justifications qui concluent seulement à une inégalité large. Pour exclure zéro, examinez les conditions d’annulation simultanée des carrés.

## Caractérisation spectrale

Les coordonnées dans une base orthonormée propre transforment la forme quadratique en somme de carrés pondérés.

### Question 9

> [!INDICATION]
> Pour le sens nécessaire, choisissez un vecteur particulier sur lequel évaluer la forme quadratique.

> [!INDICATION]
> Pour le sens suffisant, employez le théorème spectral dans une base orthonormée et regardez la forme sur un vecteur quelconque.

#### Solution

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

> [!JURY]
> Le rapport 2024 relève l’oubli de la réciproque. Quand vous écrivez la somme de carrés pondérés, expliquez pourquoi un vecteur non nul donne au moins un terme strictement positif.

### Question 10

> [!INDICATION]
> Cherchez des valeurs positives auxquelles le polynôme change de signe.

> [!INDICATION]
> Après avoir localisé des racines dans des intervalles disjoints, comparez leur nombre au degré du polynôme. Développez ensuite le déterminant caractéristique de $B$.

#### Solution

On a $P(0)=-3$, $P(1)=1$, $P(3)=-3$ et $P(4)=1$.

Le polynôme $P$ est continu. Par le théorème des valeurs intermédiaires, il possède au moins une racine dans chacun des trois intervalles disjoints $]0,1[$, $]1,3[$ et $]3,4[$. Comme son degré est trois, **ces trois racines sont distinctes, simples et strictement positives**.

Le développement du déterminant de $XI_3-B$ donne

$$
\det(XI_3-B)=(X-1)(X-2)(X-3)-(X-1)-(X-2).
$$

Cette expression vaut $P(X)$. La matrice $B$ est symétrique réelle et ses valeurs propres sont les trois racines positives de $P$. **$B$ est définie positive par la question 9.**

> [!JURY]
> Le rapport 2024 demande de nommer le théorème qui garantit l’existence d’une racine. Ici, la continuité et les changements de signe permettent d’appliquer le théorème des valeurs intermédiaires.

## Un critère en dimension 2

La trace et le déterminant fournissent la somme et le produit des valeurs propres. La hessienne d’une fonction de deux variables offre une application directe.

### Question 11

> [!INDICATION]
> Utilisez une matrice diagonale semblable à $M$ pour lire sa trace et son déterminant.

#### Solution

Par les questions précédentes et le théorème spectral, une matrice définie positive est semblable à une diagonale de termes $\lambda_1,\ldots,\lambda_n>0$, chacun compté avec sa multiplicité. En utilisant l’invariance de la trace et du déterminant par similitude, on obtient

$$
\boxed{\begin{gathered}
\operatorname{Tr}M=\sum_{i=1}^n\lambda_i>0\\
\det M=\prod_{i=1}^n\lambda_i>0.
\end{gathered}}
$$

> [!JURY]
> Le rapport 2024 demande de tenir compte des multiplicités. Une écriture indexée par les positions sur la diagonale compte chaque occurrence.

### Question 12

> [!INDICATION]
> Traduisez les deux hypothèses en une somme et un produit.

> [!INDICATION]
> Commencez par le produit pour lier les signes, puis utilisez la somme pour déterminer le signe commun.

#### Solution

Le théorème spectral donne deux valeurs propres réelles $\lambda_1,\lambda_2$, comptées avec multiplicité. Leur produit vaut $\det M>0$, donc elles sont non nulles et de même signe. Leur somme vaut $\operatorname{Tr}M>0$, donc elles sont toutes deux strictement positives. La question 9 donne **$M$ définie positive**.

> [!METHODE]
> Les relations entre somme, produit et signe évitent tout calcul explicite de racine ou de discriminant.

### Question 13

> [!INDICATION]
> Construisez un contre-exemple diagonal pour choisir directement les signes des valeurs propres.

> [!INDICATION]
> Cherchez combien de valeurs propres négatives peuvent donner un produit positif, puis ajustez la trace.

#### Solution

**Non.** La matrice symétrique $\operatorname{diag}(-1,-1,3)$ a pour trace $1$ et pour déterminant $3$, mais admet $-1$ comme valeur propre. Elle n’est donc pas définie positive.

> [!METHODE]
> Pour tester un critère spectral en dimension supérieure, une matrice diagonale isole exactement les contraintes numériques posées aux valeurs propres.

### Question 14

> [!INDICATION]
> Annulez le gradient avant d’étudier la hessienne.

> [!INDICATION]
> Les deux équations de stationnarité partagent un facteur strictement positif. Pour la hessienne, revenez au critère de dimension deux.

#### Solution

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

> [!JURY]
> Le rapport 2024 signale des erreurs de calcul du gradient et de la hessienne. Vérifiez notamment le signe et le coefficient de la dérivée croisée.

## Le critère de Sylvester

On étudie les blocs principaux dans l’ordre de leurs tailles. Pour passer d’une taille à la suivante, un changement de variables élimine les coefficients de liaison avec la dernière coordonnée.

### Question 15

> [!INDICATION]
> Choisissez les coordonnées après la $k$-ième pour faire disparaître les termes extérieurs au bloc.

> [!INDICATION]
> Vérifiez la condition sur le caractère non nul du vecteur obtenu, y compris si toutes les données initiales sont nulles.

#### Solution

On complète $X_k$ par des zéros, soit $X=(x_1,\ldots,x_k,0,\ldots,0)^{\mathsf T}$. Alors

$$
\begin{gathered}
X^{\mathsf T}MX=\sum_{1\le i,j\le k} x_i m_{i,j} x_j\\
X_k^{\mathsf T}M_kX_k=\sum_{1\le i,j\le k} x_i m_{i,j} x_j.
\end{gathered}
$$

**Ce choix est non nul dès que $X_k\ne0$.** L’énoncé doit supposer $X_k\ne0$ pour garantir l’existence de $X\ne0$. En effet, si $X_k=0$ et $M=I_n$, l’égalité demandée imposerait $\|X\|^2=0$.

> [!PIEGE]
> La restriction à un bloc principal s’obtient en plongeant un vecteur dans un sous-espace de coordonnées. Le caractère non nul du prolongement dépend de celui du vecteur de départ.

### Question 16

> [!INDICATION]
> Comparez les formes quadratiques sur le sous-espace des $k$ premières coordonnées.

> [!INDICATION]
> Une fois la définie-positivité du bloc établie, utilisez un résultat antérieur sur son déterminant.

#### Solution

Soit $M$ symétrique réelle définie positive. Pour chaque $k$, le bloc $M_k$ est symétrique réel. Pour tout $X_k\ne0$, le vecteur $X$ de la question 15 est non nul. On a donc $X_k^{\mathsf T}M_kX_k=X^{\mathsf T}MX>0$.

Le bloc $M_k$ est défini positif, et la question 11 donne $\det M_k>0$. **Tous les mineurs principaux demandés sont strictement positifs.**

> [!METHODE]
> La propriété se transmet aux blocs principaux par restriction de la forme quadratique. Le spectre d’un bloc principal n’est pas nécessairement inclus dans celui de la matrice entière.

### Question 17

> [!INDICATION]
> Pour choisir la dernière colonne de $Q$, traduisez l’annulation du bloc en haut à droite par une équation linéaire.

> [!INDICATION]
> Une fois les blocs hors diagonale éliminés, comparez les déterminants avant et après la transformation.

#### Solution

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

> [!JURY]
> Le rapport 2024 signale que l’existence de $V$ et le signe strict de $\beta$ ont souvent été mal justifiés. Associez l’existence à l’inversibilité du bloc, puis le signe à un quotient de déterminants.

### Question 18

> [!INDICATION]
> Identifiez les mineurs du bloc de taille $n-1$ et appliquez-lui l’hypothèse de récurrence.

> [!INDICATION]
> Une fois la forme transformée par $Q$, utilisez son inversibilité pour revenir à un vecteur arbitraire de l’espace initial.

#### Solution

En taille $1$, le critère donne l’unique coefficient strictement positif, ce qui implique la définie-positivité.

Supposons l’implication vraie en taille $n-1$ et soit $M$ symétrique réelle de taille $n$ vérifiant le critère.

Les mineurs principaux du bloc $M_{n-1}$ sont les $n-1$ premiers de $M$, donc $M_{n-1}$ est définie positive par l’hypothèse de récurrence. D’autre part, $\det M>0$.

On peut appliquer la question 17. Pour $Y=(Z,t)^{\mathsf T}\ne0$,

$$
Y^{\mathsf T}(Q^{\mathsf T}MQ)Y
=Z^{\mathsf T}M_{n-1}Z+\beta t^2>0.
$$

En effet, les deux termes sont positifs ou nuls et l’un au moins est strictement positif. Puisque $Q$ est inversible, tout $X\ne0$ s’écrit $X=QY$ avec $Y\ne0$. On a donc $X^{\mathsf T}MX>0$. La récurrence démontre **la réciproque du critère de Sylvester en toute dimension non nulle**.

> [!JURY]
> Le rapport 2024 relève la fausse inclusion des spectres d’un bloc principal et de la matrice initiale. Ici, l’hypothèse de récurrence porte sur les déterminants des blocs, et $Q$ agit par congruence.

### Question 19

> [!INDICATION]
> Calculez les mineurs principaux dans l’ordre et repérez lesquels dépendent de $x$.

#### Solution

Les deux premiers mineurs principaux de $C(x)$ valent $2$ et $1$. Par développement suivant la première ligne,

$$
\det C(x)=2(1-x^2)-1=1-2x^2.
$$

La matrice étant symétrique, le critère de Sylvester donne

$$
\boxed{C(x)\text{ est définie positive si et seulement si } |x|<1/\sqrt2.}
$$

> [!PIEGE]
> Une inégalité stricte sur le carré d’un réel et une borne sur sa valeur absolue sont équivalentes. Les extrémités de l’intervalle doivent être examinées.

### Question 20

> [!INDICATION]
> Pour rejeter la définie-positivité, recherchez un seul mineur principal qui ne satisfait pas l’inégalité requise.

#### Solution

Le troisième mineur principal vaut

$$
\begin{vmatrix}2&2&1\\2&3&-1\\1&-1&1\end{vmatrix}
=2(3-1)-2(2+1)+(-2-3)=-7.
$$

Puisqu’un mineur principal est strictement négatif, **la matrice n’est pas définie positive**.

> [!METHODE]
> Commencez par les plus petits blocs. Dès qu’un mineur échoue au test, le calcul des déterminants suivants est superflu.

### Question 21

> [!INDICATION]
> Associez à chaque terme mixte les deux coefficients symétriques qui le produisent.

> [!INDICATION]
> Appliquez le test de Sylvester à la matrice obtenue.

#### Solution

Le membre de gauche est la forme quadratique, au vecteur $(x,y,z)^{\mathsf T}$, de la matrice symétrique

$$
M=\begin{pmatrix}
4&1&-3/2\\
1&1&0\\
-3/2&0&1
\end{pmatrix}.
$$

Ses deux premiers mineurs principaux valent $4$ et $3$. Le troisième vaut $4-1-9/4=3/4$. Ils sont tous strictement positifs, donc $M$ est définie positive par le critère de Sylvester. **L’expression est par conséquent strictement positive pour tout vecteur non nul.**

> [!JURY]
> Le rapport 2024 admet une preuve directe, tout en relevant des réponses qui se limitent à la positivité au sens large. Dans une preuve par carrés, vérifiez quels vecteurs annulent tous les termes.

### Question 22

> [!INDICATION]
> Partez du déterminant de taille $n$ et développez selon une ligne ou colonne pauvre en coefficients non nuls.

> [!INDICATION]
> Dans le mineur provenant du coefficient hors diagonale, cherchez une colonne qui ramène à une taille encore plus petite. La différence entre déterminants successifs aide à étudier le signe.

#### Solution

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

> [!JURY]
> Le rapport 2024 signale des récurrences de déterminants mal conduites. Faites apparaître le signe du cofacteur et le second développement, puis vérifiez les tailles initiales.

> [!METHODE]
> On peut aussi revenir à la forme quadratique. Chaque produit entre deux coordonnées voisines vérifie $2x_ix_{i+1}\ge-x_i^2-x_{i+1}^2$. Chaque carré est soustrait au plus deux fois. Il reste donc au moins la somme des carrés, strictement positive pour un vecteur non nul.

## Bilan

- Dans une récurrence vectorielle, passez dans la base propre, étudiez chaque mode et revenez aux données initiales par la matrice de passage. Contrôlez au besoin le spectre par la trace.
- Pour une série de fonctions, distinguez les ensembles sur lesquels vous pouvez établir la convergence normale et les limites où un encadrement quantitatif est nécessaire. Une comparaison série-intégrale part toujours d’une inégalité sur un intervalle de longueur un et d’une somme finie.
- Pour une matrice symétrique, choisissez le test adapté aux données disponibles. Le spectre permet de lire le signe, la somme et le produit suffisent en dimension deux, et les blocs principaux donnent un test en toute dimension.
- Dans une preuve par changement de variables, justifiez l’inversibilité et suivez séparément la forme quadratique et le déterminant. Dans un déterminant tridiagonal, chaque développement doit faire apparaître précisément le bloc de taille réduite.
