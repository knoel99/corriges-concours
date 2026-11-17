# BCE ECT — Mathématiques T (conception ESCP) 2025 · Corrigé guidé

*Corrigé rédigé par IA, non officiel. Signalez toute erreur.*

## Présentation du sujet

Épreuve de **4 heures**, sans document ni calculatrice (règle graduée autorisée). Trois exercices indépendants, **65 questions**.

| Exercice | Questions | Contenu | Notions du programme ECT |
|---|---|---|---|
| 1 — Dynamique de population | 1 à 6, 35 questions | Partie I : système de suites $X_{n+1}=AX_n$, diagonalisation de $A$, limite des effectifs, puis SQL. Partie II : croissance à taux fixe (suite géométrique), puis croissance logistique $w_{n+1}=g(w_n)$ selon la position de $w_0$. | Polynôme annulateur, valeurs propres, diagonalisation $2\times2$, récurrence, suites géométriques, trinômes, suite récurrente étudiée pas à pas (intervalle stable, monotonie, limite monotone), SQL (`WHERE`, `AND`, `INNER JOIN`) |
| 2 — Marche d'un pion | 1 à 9, 16 questions | Simulation Python, lois de $X_1$ et $X_2$, relation entre les lois de $X_k$ et $X_{k+1}$, puis $E(X_{k+1})=1+\left(1-\frac2n\right)E(X_k)$ et limite $\frac n2$. | Python (`rd.randint`, tableaux), formule des probabilités totales, espérance, suites arithmético-géométriques, loi faible des grands nombres |
| 3 — Suites de densités | 1 à 11, 14 questions | $f_{n+1}(t)=tf_n'(t)$ sur $[0,1]$ : cas $f_0(t)=(\alpha+1)t^\alpha$ (toutes les $f_n$ sont proportionnelles), puis cas $f_0(t)=e^t$ (constante de normalisation par une récurrence sur les intégrales). | Densité, fonction de répartition, espérance et variance, intégration par parties, récurrence |

**Ce qu'en dit le jury.** Le rapport 2025 indique 1064 copies corrigées, une moyenne de 9,27 et un écart type de 5,84. Le barème donne 51 % des points à l'exercice 1, 23 % à l'exercice 2 et 26 % à l'exercice 3. Les questions qui rapportent le plus sont, pour l'exercice 1 : 1c, 3d, 4c, 5c, 6a)ii, 6b)i, 6b)ii, 6c)iii, 6d)ii ; pour l'exercice 2 : 3, 5, 7, 9 ; pour l'exercice 3 : 4, 5, 6 et 11.

**Difficulté et gestion du temps.** La partie I de l'exercice 1 est très classique et doit être faite vite. La partie II (logistique) demande de l'ordre : chaque cas (c), (d), (e) réutilise les tableaux de variations de $f$ et $g$. L'exercice 2 est court mais la question 7 (réindexation de sommes) est technique. L'exercice 3 alterne questions de cours (1, 3, 4, 5, 6) et raisonnements plus fins (2a, 7 à 11).

## Exercice 1, partie I — Deux classes d'âge

On écrit le système sous forme matricielle $X_{n+1}=AX_n$, on diagonalise $A$, puis on lit la limite des effectifs. La question 4 (SQL) est indépendante.

### Question 1(a)

> [!INDICATION]
> Calculez $A^2$ puis la combinaison demandée ; travaillez avec des fractions de même dénominateur.

#### Solution

$$A^2=\begin{pmatrix}\frac59&\frac43\\\frac4{27}&\frac59\end{pmatrix},\qquad A^2-\frac43A+\frac13I_2=\begin{pmatrix}0&0\\0&0\end{pmatrix}.$$

### Question 1(b)

> [!INDICATION]
> Factorisez le polynôme (somme et produit des racines), puis utilisez le lien entre valeurs propres et polynôme annulateur.

#### Solution

$X^2-\frac43X+\frac13=(X-1)\left(X-\frac13\right)$ : les valeurs propres possibles sont $1$ et $\frac13$.

> [!JURY]
> Rapport 2025 : « Plusieurs candidats ont calculé det(A − λI) pour déterminer les valeurs propres, alors que le jury attendait une justification utilisant la question précédente. »

### Question 1(c)

> [!INDICATION]
> Comparez chaque produit au vecteur de départ.

#### Solution

$A\begin{pmatrix}3\\1\end{pmatrix}=\begin{pmatrix}3\\1\end{pmatrix}$ et $A\begin{pmatrix}3\\-1\end{pmatrix}=\frac13\begin{pmatrix}3\\-1\end{pmatrix}$. Ces vecteurs sont non nuls, donc
$$\boxed{\mathrm{Sp}(A)=\left\{1,\ \frac13\right\}}$$

> [!PIEGE]
> La question 1(b) ne donne que des valeurs **possibles** : c'est le vecteur propre non nul qui prouve qu'une valeur est effectivement propre.

### Question 2(a)

> [!INDICATION]
> Produit matriciel direct.

#### Solution

$PQ=6I_2$.

### Question 2(b)

> [!INDICATION]
> Divisez l'égalité précédente par $6$.

#### Solution

$P\left(\frac16Q\right)=I_2$, donc $P$ est inversible et $P^{-1}=\frac16Q$.

### Question 2(c)

> [!INDICATION]
> Après le calcul, revenez à la définition d'une matrice diagonalisable.

#### Solution

$AP=PD=\begin{pmatrix}3&1\\1&-\frac13\end{pmatrix}$, donc $D=P^{-1}AP$ avec $D$ diagonale et $P$ inversible : $A$ est diagonalisable.

### Question 2(d)

> [!INDICATION]
> Hérédité : $A^{n+1}=A^nA$ et $P^{-1}P=I_2$ au milieu.

#### Solution

$A^0=I_2=PD^0P^{-1}$, et si $A^n=PD^nP^{-1}$ :
$$\begin{aligned}
A^{n+1}&=PD^nP^{-1}PDP^{-1}\\
&=PD^{n+1}P^{-1}.
\end{aligned}$$

### Question 2(e)

> [!INDICATION]
> $D^n$ est diagonale ; calculez $PD^n$, puis multipliez par $\frac16Q$.

> [!INDICATION]
> Pour retrouver la forme de l'énoncé : $3\left(\frac13\right)^n=\left(\frac13\right)^{n-1}$.

#### Solution

$$A^n=\frac16\begin{pmatrix}3+3\left(\frac13\right)^n&9-9\left(\frac13\right)^n\\1-\left(\frac13\right)^n&3+3\left(\frac13\right)^n\end{pmatrix},$$
ce qui est la formule de l'énoncé.

### Question 3(a)

> [!INDICATION]
> Écrivez le système (1) sous forme d'un produit matrice-vecteur.

#### Solution

$X_{n+1}=AX_n$.

> [!JURY]
> Rapport 2025 : « Dans la question 3a), le jury constate que trop de candidats confondent indices et puissances ». $X_{n+1}$ est le terme de rang $n+1$ de la suite, pas une puissance.

### Question 3(b)

> [!INDICATION]
> Récurrence immédiate.

#### Solution

$X_0=A^0X_0$ ; si $X_n=A^nX_0$, alors $X_{n+1}=AA^nX_0=A^{n+1}X_0$.

### Question 3(c)

> [!INDICATION]
> Produit de $A^n$ par $\begin{pmatrix}u_0\\v_0\end{pmatrix}$, sans oublier le facteur $\frac16$.

#### Solution

$$\begin{aligned}u_n&=\frac16\left[\left(3+\left(\tfrac13\right)^{n-1}\right)u_0+\left(9-\left(\tfrac13\right)^{n-2}\right)v_0\right],\\v_n&=\frac16\left[\left(1-\left(\tfrac13\right)^{n}\right)u_0+\left(3+\left(\tfrac13\right)^{n-1}\right)v_0\right].\end{aligned}$$

> [!JURY]
> Rapport 2025 : les questions 3b), 3c) et 3d) ont été réussies dans les meilleures copies, « bien que dans certaines, le coefficient ⅙ ait été oublié. »

### Question 3(d)

> [!INDICATION]
> Que deviennent les puissances de $\frac13$ ? Comparez les limites à $0$ et à $+\infty$.

#### Solution

Comme $0<\frac13<1$, les puissances de $\frac13$ tendent vers $0$, donc
$$\begin{aligned}\lim u_n&=\frac{3u_0+9v_0}6=\frac{u_0+3v_0}2,\\\lim v_n&=\frac{u_0+3v_0}6.\end{aligned}$$
Ces limites sont strictement positives : la population **survit**, ni extinction ni explosion, avec à terme trois fois plus d'enfants que d'adultes.

### Question 4(a)

> [!INDICATION]
> Relisez la phrase « Dans un enclos on trouve une seule catégorie d'une espèce d'animal ».

#### Solution

Chaque enclos correspond à une seule ligne : `Enclos` peut être la clé primaire. `Espèce` apparaît sur au moins deux lignes (enfants et adultes).

> [!JURY]
> Rapport 2025 : « La question 4 a été très peu abordée, un faible nombre de candidats sait ce qu’est une clé primaire. »

### Question 4(b)

> [!INDICATION]
> Les types d'alimentation sont dans ALIMENTATION ; évitez les doublons.

#### Solution

```sql
SELECT DISTINCT Type FROM ALIMENTATION;
```

### Question 4(c)

> [!INDICATION]
> Deux conditions dans le `WHERE`, reliées par un opérateur logique.

#### Solution

```sql
SELECT Espèce FROM ANIMAUX
WHERE Categorie = 'adulte' AND Effectif >= 6;
```

### Question 4(d)

> [!INDICATION]
> L'information est répartie sur deux tables : jointure sur l'attribut commun.

#### Solution

```sql
SELECT ANIMAUX.Espèce, ANIMAUX.Effectif
FROM ANIMAUX INNER JOIN ALIMENTATION ON ANIMAUX.Espèce = ALIMENTATION.Espèce
WHERE ALIMENTATION.Tarif < 15;
```

## Exercice 1, partie II — Croissance à taux fixe et croissance logistique

La question 5 traite un modèle géométrique ; la question 6 étudie $w_{n+1}=g(w_n)$ avec $g(x)=x+\alpha x\left(1-\frac x\beta\right)$, en distinguant trois positions de $w_0$. Tout repose sur les tableaux de variations de $f$ et de $g$ : soignez-les.

### Question 5(a)

> [!INDICATION]
> Isolez $w_{n+1}$.

#### Solution

$w_{n+1}=(1+r)w_n$ : suite géométrique de raison $1+r$, et $w_n=(1+r)^nw_0$.

> [!JURY]
> Rapport 2025 : « La question 5 n’a pas été beaucoup abordée, les candidats n’ont pas su reconnaitre la raison de la suite géométrique définie. »

### Question 5(b)

> [!INDICATION]
> Que vaut le signe de $1+r$ si $r<-1$, et qu'en résulterait-il pour $w_1$ ?

#### Solution

Il faut $1+r\geqslant0$ pour que la population reste positive : une population ne peut pas perdre plus de $100\,\%$ de son effectif.

### Question 5(c)

> [!INDICATION]
> Limite de $q^n$ selon la position de $q=1+r$ par rapport à $1$.

#### Solution

- $r\in[-1,0[$ : $0\leqslant1+r<1$, $w_n\to0$, **extinction**.
- $r=0$ : $w_n=w_0$, **survie** à effectif constant.
- $r>0$ : $1+r>1$, $w_n\to+\infty$, **explosion**.

Une croissance illimitée n'est pas réaliste (ressources finies) : d'où le modèle logistique.

### Question 6(a)i

> [!INDICATION]
> Un produit est nul si et seulement si…

#### Solution

$f(x)=0\iff x=0$ ou $x=\beta$.

> [!JURY]
> Rapport 2025 : « La résolution des équations du type x(1−bx) = 0 a posé problème. » Ne développez pas : la forme factorisée donne directement les solutions.

### Question 6(a)ii

> [!INDICATION]
> $f$ est un trinôme du second degré : coefficient dominant, sommet.

#### Solution

$f'(x)=\alpha\left(1-\frac{2x}\beta\right)$ :

$f$ croît sur $\left[0,\frac\beta2\right]$, décroît ensuite, de maximum $\frac{\alpha\beta}4$, avec $f(0)=f(\beta)=0$ et $f(x)\to-\infty$ en $+\infty$.

| $x$ | $0$ | | $\frac\beta2$ | | $\beta$ | | $+\infty$ |
|---|---|---|---|---|---|---|---|
| $f$ | $0$ | ↗ | $\frac{\alpha\beta}4$ | ↘ | $0$ | ↘ | $-\infty$ |

> [!JURY]
> Rapport 2025 : « les candidats n’ont pas pensé à utiliser leurs connaissances sur les fonctions du second degré » et « Beaucoup d’entre eux justifient la dérivabilité en invoquant la continuité. » Un polynôme est dérivable sur $\mathbb R$ ; la continuité n'implique pas la dérivabilité.

### Question 6(b)i

> [!INDICATION]
> $g(x)=x$ se ramène à une équation déjà résolue.

> [!INDICATION]
> Pour $g(x)=\beta$, une racine évidente se lit dans la question précédente ; le produit des racines donne l'autre.

#### Solution

- $g(x)=x\left(1+\alpha-\frac\alpha\beta x\right)=0\iff x\in\left\{0,\frac{(\alpha+1)\beta}\alpha\right\}$.
- $g(x)=x\iff f(x)=0\iff x\in\{0,\beta\}$.
- $g(x)=\beta\iff x^2-\frac{(1+\alpha)\beta}\alpha x+\frac{\beta^2}\alpha=0\iff x\in\left\{\beta,\frac\beta\alpha\right\}$ (racine $\beta$ et produit $\frac{\beta^2}\alpha$).

### Question 6(b)ii

> [!INDICATION]
> Chaque inégalité se simplifie par $\frac\beta\alpha>0$ et se ramène à une condition sur $\alpha$.

#### Solution

Les trois inégalités équivalent respectivement à $\alpha<1$, $\alpha<1$ et $\alpha>0$, vraies car $\alpha\in\,]0,1[$.

### Question 6(b)iii

> [!INDICATION]
> Sommet du trinôme $g$, puis placez les réels de 6(b)i dans le tableau grâce à 6(b)ii.

#### Solution

$g$ croît sur $[0,x^*]$ et décroît sur $[x^*,+\infty[$, avec $x^*=\frac{(\alpha+1)\beta}{2\alpha}$ et $g(x^*)=\frac{(\alpha+1)^2\beta}{4\alpha}$.

| x | 0 | | β | | x* | | $\frac\beta\alpha$ | | $\frac{(\alpha+1)\beta}\alpha$ | | +∞ |
|---|---|---|---|---|---|---|---|---|---|---|---|
| $g$ | 0 | ↗ | β | ↗ | $g(x^*)$ | ↘ | β | ↘ | 0 | ↘ | −∞ |

> [!METHODE]
> Pour une suite $w_{n+1}=g(w_n)$ : repérer les **points fixes** ($g(x)=x$) et les intervalles **stables** par $g$, que le tableau de variations de $g$ permet de lire.

### Question 6(c)i

> [!INDICATION]
> Sur $[0,\beta]$, $g$ est croissante : appliquez-la à l'encadrement de $w_n$.

#### Solution

On montre un peu plus fort : $w_n\in\,]0,\beta]$ pour tout $n\in\mathbb N$.

- **Initialisation** : $w_0\in\,]0,\beta]$ par hypothèse.
- **Hérédité** : si $w_n\in\,]0,\beta]$, comme $[0,\beta]\subset[0,x^*]$ (question 6(b)ii), $g$ est strictement croissante sur $[0,\beta]$, donc $0=g(0)<g(w_n)\leqslant g(\beta)=\beta$, c'est-à-dire $w_{n+1}\in\,]0,\beta]$.

Donc $w_n\in\,]0,\beta]\subset[0,\beta]$ pour tout $n$.

### Question 6(c)ii

> [!INDICATION]
> Signe de $f$ sur $[0,\beta]$, lu dans le tableau de 6(a)ii.

#### Solution

$f\geqslant0$ sur $[0,\beta]$, donc $w_{n+1}-w_n=f(w_n)\geqslant0$ : $(w_n)$ est croissante.

### Question 6(c)iii

> [!INDICATION]
> Théorème de la limite monotone.

#### Solution

Croissante et majorée par $\beta$ : $(w_n)$ converge vers un réel $\ell$.

### Question 6(c)iv

> [!INDICATION]
> Une suite croissante est minorée par son premier terme.

#### Solution

$w_n\geqslant w_0$ pour tout $n$, donc $\ell\geqslant w_0$ par passage à la limite.

### Question 6(c)v

> [!INDICATION]
> Passez à la limite dans $w_{n+1}=g(w_n)$ en écrivant $g(w_n)$ explicitement (opérations sur les limites).

#### Solution

On a $w_{n+1}=g(w_n)$ pour tout $n$. Quand $n\to+\infty$, $w_{n+1}\to\ell$, et $g(w_n)=w_n+\alpha w_n-\frac\alpha\beta w_n^2$ tend vers $g(\ell)$ par opérations sur les limites (sommes et produits).

Par unicité de la limite, $\ell=g(\ell)$.

D'après 6(b)i, $\ell\in\{0,\beta\}$ ; comme $\ell\geqslant w_0>0$,
$$\boxed{\ell=\beta}$$
La population croît et se stabilise à $\beta$, la capacité d'accueil du milieu : c'est une **survie**.

> [!PIEGE]
> Conclure $\ell=\beta$ sans éliminer $\ell=0$ : c'est l'inégalité $\ell\geqslant w_0>0$ (question 6(c)iv) qui l'exclut.

### Question 6(d)i

> [!INDICATION]
> Calculez $g(x^*)$ (tableau de 6(b)iii) et comparez-le à $\frac\beta\alpha$.

> [!INDICATION]
> Pour la récurrence : sur $\left[\beta,\frac\beta\alpha\right]$, quel est le minimum et quel est le maximum de $g$ ?

#### Solution

$g(x^*)=\frac{(\alpha+1)^2\beta}{4\alpha}<\frac\beta\alpha\iff(\alpha+1)^2<4$, vrai.

Sur $\left[\beta,\frac\beta\alpha\right]$, $g$ vaut $\beta$ aux deux bornes et atteint son maximum $g(x^*)$ en $x^*$, donc $\beta\leqslant g(x)\leqslant g(x^*)<\frac\beta\alpha$.

Par récurrence, $w_n\in\left[\beta,\frac\beta\alpha\right]$ pour tout $n$.

### Question 6(d)ii

> [!INDICATION]
> Signe de $f$ sur $[\beta,+\infty[$.

#### Solution

$f\leqslant0$ sur $[\beta,+\infty[$, donc $w_{n+1}\leqslant w_n$ : $(w_n)$ est décroissante.

### Question 6(d)iii

> [!INDICATION]
> Même démarche qu'en 6(c)iii et 6(c)v.

#### Solution

Décroissante et minorée par $\beta$, $(w_n)$ converge vers $\ell\geqslant\beta$, avec $\ell=g(\ell)$ : $\ell=\beta$. Une population trop nombreuse décroît vers $\beta$.

### Question 6(e)i

> [!INDICATION]
> Sur l'intervalle de $w_0$, $g$ est décroissante : lisez les valeurs aux bornes.

#### Solution

D'après 6(b)ii, $x^*<\frac\beta\alpha$ : sur $\left[\frac\beta\alpha,\frac{(\alpha+1)\beta}\alpha\right]$, $g$ est strictement décroissante, avec $g\left(\frac\beta\alpha\right)=\beta$ et $g\left(\frac{(\alpha+1)\beta}\alpha\right)=0$. Comme $\frac\beta\alpha\leqslant w_0<\frac{(\alpha+1)\beta}\alpha$,
$$0<g(w_0)\leqslant\beta,$$
c'est-à-dire $w_1\in\,]0,\beta]$.

### Question 6(e)ii

> [!INDICATION]
> À partir du rang 1, on est ramené à un cas déjà traité.

#### Solution

La suite $(w'_n)=(w_{n+1})_{n\in\mathbb N}$ vérifie $w'_{n+1}=g(w'_n)$ et $w'_0=w_1\in\,]0,\beta]$ : l'étude 6(c) s'applique, et $(w'_n)$ converge vers $\beta$. Une suite et sa suite décalée ont la même limite : $w_n\to\beta$.

> [!METHODE]
> Ramener un cas nouveau à un cas déjà traité en décalant les indices : il suffit de vérifier qu'un terme de la suite tombe dans la zone déjà étudiée.

### Question 6(f)

> [!INDICATION]
> Que vaut $w_1$ si $w_0\geqslant\frac{(\alpha+1)\beta}\alpha$ ?

#### Solution

Non : si $w_0=\frac{(\alpha+1)\beta}\alpha$, $w_1=0$ (extinction immédiate) ; si $w_0>\frac{(\alpha+1)\beta}\alpha$, $w_1<0$, ce qui n'a pas de sens pour une population.

## Exercice 2 — La marche du pion

En $0$ le pion avance toujours, en $n$ il recule toujours. On établit une relation entre les lois de $X_k$ et $X_{k+1}$, puis une récurrence arithmético-géométrique sur les espérances.

### Question 1(a)

> [!INDICATION]
> Dans chaque branche, la nouvelle position s'obtient à partir de `position[j]`.

#### Solution

```python
                if position[j] < bille:
                        position[j+1] = position[j]+1
                else:
                        position[j+1] = position[j]-1
        return(position)
```

> [!JURY]
> Rapport 2025 : « Peu de candidats ont traité la question 1) relative aux instructions Python et la syntaxe est souvent partiellement maitrisée. »

### Question 1(b)

> [!INDICATION]
> La position finale est le dernier élément du tableau renvoyé (indice $10$).

#### Solution

```python
position = deplacement_pion(20,10)
print(position[10])
```

### Question 1(c)

> [!INDICATION]
> `Test` renvoie une moyenne : de quelles valeurs ? Quel théorème relie une moyenne empirique à une espérance ?

#### Solution

`Test(10,100,1000)` est la moyenne de $1000$ réalisations indépendantes de $X_{100}$ (avec $n=10$) : par la loi faible des grands nombres, $5{,}054$ estime $E(X_{100})$, proche de $5=\frac n2$.

### Question 2

> [!INDICATION]
> Depuis la position $0$, quelles billes font avancer le pion ?

#### Solution

Toutes : $X_1=1$ est certaine, $E(X_1)=1$.

### Question 3

> [!INDICATION]
> Depuis la position $1$, comptez les billes qui font avancer et celles qui font reculer.

#### Solution

$P(X_2=2)=\frac{n-1}n$, $P(X_2=0)=\frac1n$, donc
$$\boxed{E(X_2)=\frac{2(n-1)}n}$$

### Question 4

> [!INDICATION]
> Récurrence : examinez à part les positions $0$ et $n$.

#### Solution

$X_0=0$.

Si $X_k\in[\![0,n]\!]$ : depuis $0$ on va en $1$, depuis $n$ en $n-1$, sinon on reste dans $[\![0,n]\!]$ en bougeant d'une unité.

Donc $X_{k+1}(\Omega)\subset[\![0,n]\!]$.

### Question 5

> [!INDICATION]
> D'où peut-on arriver en $0$ ? En $n$ ? Quelle bille faut-il tirer ?

#### Solution

On n'arrive en $0$ que depuis $1$ en tirant la bille $1$, et en $n$ que depuis $n-1$ en tirant la bille $n$. Le tirage est indépendant de la position, donc
$$\begin{aligned}P(X_{k+1}=0)&=\frac1nP(X_k=1)\\P(X_{k+1}=n)&=\frac1nP(X_k=n-1)\end{aligned}.$$

> [!JURY]
> Rapport 2025 : « Les justifications de la question 5 ont manqué de rigueur, le résultat étant donné dans l’énoncé. »

### Question 6(a)

> [!INDICATION]
> Billes strictement supérieures à $\ell-1$.

#### Solution

$\frac{n-\ell+1}n$.

### Question 6(b)

> [!INDICATION]
> Billes inférieures ou égales à $\ell+1$.

#### Solution

$\frac{\ell+1}n$.

> [!JURY]
> Rapport 2025 : « Quand les questions 6a) et 6b) ont été abordées, les candidats ont souvent affirmé le résultat sans justifications, en ayant été inspirés par la question 6c). » Il faut compter les billes favorables.

### Question 6(c)

> [!INDICATION]
> Système complet $(X_k=j)_{j\in[\![0,n]\!]}$ : seules deux positions permettent d'arriver en $\ell$.

#### Solution

Les événements $(X_k=j)$, $j\in[\![0,n]\!]$, forment un système complet (question 4). Le pion arrive en $\ell$ à l'étape $k+1$ si et seulement s'il était en $\ell-1$ et avance, ou s'il était en $\ell+1$ et recule ; depuis toute autre position, c'est impossible. Ces deux cas sont incompatibles.

Le tirage de l'étape $k+1$ est indépendant de la position $X_k$ (tirages avec remise) : la probabilité d'être en $\ell-1$ **et** d'avancer est le produit $P(X_k=\ell-1)\cdot\frac{n-\ell+1}n$, et de même pour l'autre cas. D'où
$$\begin{aligned}P(X_{k+1}=\ell)={}&\frac{n-\ell+1}nP(X_k=\ell-1)\\&+\frac{\ell+1}nP(X_k=\ell+1).\end{aligned}$$

> [!PIEGE]
> Rapport 2025 : « plusieurs candidats justifient que ((Xk = ℓ+1), (Xk = ℓ−1)) forme un système complet d’événements ». C'est faux : le système complet est $(X_k=j)_{0\leqslant j\leqslant n}$ ; les autres termes de la formule des probabilités totales sont nuls.

### Question 7

> [!INDICATION]
> Écrivez $E(X_{k+1})=\sum\ell P(X_{k+1}=\ell)$ et remplacez par les formules des questions 5 et 6(c).

> [!INDICATION]
> Réindexez chaque somme en fonction de la position $j$ à l'instant $k$, puis regroupez le coefficient de $P(X_k=j)$.

#### Solution

D'après la question 4, $E(X_{k+1})=\sum_{\ell=0}^n\ell\,P(X_{k+1}=\ell)$. Le terme $\ell=0$ est nul ; on utilise 6(c) pour $1\leqslant\ell\leqslant n-1$ et la question 5 pour $\ell=n$ :
$$\begin{aligned}E(X_{k+1})={}&\sum_{\ell=1}^{n-1}\ell\,\frac{n-\ell+1}nP(X_k=\ell-1)\\&+\sum_{\ell=1}^{n-1}\ell\,\frac{\ell+1}nP(X_k=\ell+1)\\&+n\cdot\frac1nP(X_k=n-1).\end{aligned}$$
On pose $j=\ell-1$ dans la première somme et $j=\ell+1$ dans la seconde.

- Le dernier terme est le terme $j=n-1$ de la première somme : pour $j=n-1$, $(j+1)(n-j)=n$.
- On peut ajouter le terme $j=n$ à la première somme, car $(n+1)(n-n)=0$.
- On peut ajouter les termes $j=0$ et $j=1$ à la seconde, car $(j-1)j=0$.

On obtient
$$\begin{aligned}E(X_{k+1})&=\sum_{j=0}^n\frac{(j+1)(n-j)}nP(X_k=j)+\sum_{j=0}^n\frac{(j-1)j}nP(X_k=j)\\&=\sum_{j=0}^n\frac{(j+1)(n-j)+j(j-1)}nP(X_k=j).\end{aligned}$$
Or $(j+1)(n-j)+j(j-1)=nj+n-2j$, donc le coefficient vaut $1+\left(1-\frac2n\right)j$. Comme $\sum_jP(X_k=j)=1$ et $\sum_jjP(X_k=j)=E(X_k)$ :
$$E(X_{k+1})=1+\left(1-\frac2n\right)E(X_k).$$

> [!METHODE]
> Le coefficient de $P(X_k=j)$ s'interprète : depuis $j$, la position suivante vaut $j+1$ avec probabilité $\frac{n-j}n$ et $j-1$ avec probabilité $\frac jn$.
>
> Son espérance $\frac{(j+1)(n-j)+(j-1)j}n$ est le « pas moyen » depuis $j$.

### Question 8(a)

> [!INDICATION]
> Forme $u_{m+1}=au_m+b$.

#### Solution

Suite arithmético-géométrique.

### Question 8(b)

> [!INDICATION]
> Équation du premier degré.

#### Solution

$x=\frac n2$.

### Question 8(c)

> [!INDICATION]
> Soustrayez l'équation du point fixe à la relation de récurrence.

#### Solution

$x_{k+1}=\left(1-\frac2n\right)x_k$, donc $x_k=\left(1-\frac2n\right)^{k-n}x_n$ pour $k\geqslant n$.

> [!JURY]
> Rapport 2025 : « Peu de candidats ont abordé les questions 8c) et 8d), ne faisant pas le lien avec les questions précédentes. »

### Question 8(d)

> [!INDICATION]
> $E(X_k)=x_k+\frac n2$.

#### Solution

$$E(X_k)=\frac n2+\left(1-\frac2n\right)^{k-n}\left(E(X_n)-\frac n2\right).$$

### Question 9

> [!INDICATION]
> Position de $1-\frac2n$ par rapport à $-1$ et $1$.

#### Solution

$0\leqslant1-\frac2n<1$, donc $E(X_k)\to\frac n2$ : en moyenne, le pion finit au milieu de l'axe, ce que confirme la simulation ($5{,}054$ pour $n=10$).

## Exercice 3, partie I — $f_0$ fonction puissance

### Question 1

> [!INDICATION]
> Trois conditions d'une densité.

#### Solution

$f_0\geqslant0$, continue sauf peut-être en $0$ et $1$, et $\int_0^1(\alpha+1)t^\alpha\,dt=1$.

### Question 2(a)

> [!INDICATION]
> Appliquez la définition donnée en début d'exercice : dérivabilité sur $]0,1[$, puis limites de la dérivée en $0^+$ et en $1^-$.

> [!INDICATION]
> En $0^+$, le comportement de $t^{\alpha-1}$ dépend de $\alpha$ : distinguez $\alpha=1$ et $\alpha>1$.

#### Solution

$f_0'(t)=\alpha(\alpha+1)t^{\alpha-1}$ sur $]0,1[$, de limite $\alpha(\alpha+1)$ en $1^-$.

En $0^+$, la limite vaut $0$ si $\alpha>1$ et $2$ si $\alpha=1$. Ces limites sont finies :

$f_0$ est dérivable sur $[0,1]$.

> [!JURY]
> Rapport 2025 : « La question 2a) a posé problème aux candidats n’ayant pas compris la définition donnée en début d’énoncé. »

### Question 2(b)

> [!INDICATION]
> Récurrence ; vérifiez la formule en $t=0$ séparément.

#### Solution

Si $f_n=\alpha^nf_0$, alors pour $t\in\,]0,1]$, $f_{n+1}(t)=t\alpha^n\alpha(\alpha+1)t^{\alpha-1}=\alpha^{n+1}f_0(t)$ ; en $t=0$ les deux membres sont nuls ; hors de $[0,1]$ aussi.

### Question 2(c)

> [!INDICATION]
> Quel coefficient ramène $f_n$ à $f_0$ ?

#### Solution

$c_n=\frac1{\alpha^n}$.

### Question 2(d)

> [!INDICATION]
> Comparez les densités.

#### Solution

$X_n$ et $X_0$ ont la même densité $f_0$, donc la même fonction de répartition : même loi.

### Question 3

> [!INDICATION]
> Trois cas selon la position de $x$ par rapport au support $[0,1]$.

#### Solution

$F_{X_\alpha}(x)=0$ si $x\leqslant0$, $x^{\alpha+1}$ si $x\in\,]0,1]$, $1$ si $x>1$.

### Question 4

> [!INDICATION]
> $E(X_\alpha)$ et $E(X_\alpha^2)$, puis Koenig-Huygens ; développez $(\alpha+2)^2-(\alpha+1)(\alpha+3)$.

#### Solution

Les intégrandes sont nulles hors de $[0,1]$ et continues sur $[0,1]$ : les moments existent.
$$\begin{aligned}E(X_\alpha)&=\int_0^1(\alpha+1)t^{\alpha+1}\,dt=\frac{\alpha+1}{\alpha+2},\\E(X_\alpha^2)&=\int_0^1(\alpha+1)t^{\alpha+2}\,dt=\frac{\alpha+1}{\alpha+3}.\end{aligned}$$
Par Koenig-Huygens, avec $(\alpha+2)^2-(\alpha+1)(\alpha+3)=1$ :
$$\begin{aligned}V(X_\alpha)&=\frac{(\alpha+1)\left[(\alpha+2)^2-(\alpha+1)(\alpha+3)\right]}{(\alpha+3)(\alpha+2)^2}\\&=\boxed{\frac{\alpha+1}{(\alpha+3)(\alpha+2)^2}}\end{aligned}$$

> [!PIEGE]
> Réduire au même dénominateur trop tôt : en factorisant d'abord par $\alpha+1$, le numérateur se simplifie en $1$.

## Exercice 3, partie II — $f_0$ fonction exponentielle

### Question 5

> [!INDICATION]
> Calculez $\int_0^1e^t\,dt$ (attention à $e^0$).

#### Solution

$\int_0^1e^t\,dt=e-1$, donc $c_0=\frac1{e-1}$.

> [!JURY]
> Rapport 2025 : « des erreurs de calculs du type e0 = 0 n’ont pas permis à tous les candidats d’obtenir la bonne valeur de c0. »

### Question 6

> [!INDICATION]
> Intégration par parties sur $\int_0^1te^t\,dt$.

#### Solution

$\int_0^1te^t\,dt=\big[te^t\big]_0^1-\int_0^1e^t\,dt=1$, donc $E(X_0)=\frac1{e-1}$.

> [!JURY]
> Rapport 2025 : « La question 6 n’a pas été souvent abordée correctement puisque la formule d’intégration par parties ainsi que ses hypothèses sont mal maitrisées. »
>
> Citez les fonctions $u$ et $v$, et justifiez que ces fonctions et leurs dérivées sont continues sur $[0,1]$.

### Question 7

> [!INDICATION]
> Intégration par parties avec $u(t)=t$ et $v=f_n$ ; les hypothèses viennent des résultats admis.

#### Solution

$$\int_0^1f_{n+1}(t)\,dt=\Big[tf_n(t)\Big]_0^1-\int_0^1f_n(t)\,dt=f_n(1)-\int_0^1f_n(t)\,dt.$$

### Question 8

> [!INDICATION]
> Récurrence : dérivez $P_n(t)e^t$.

#### Solution

- **Initialisation** : $f_0(t)=e^t=P_0(t)e^t$ sur $[0,1]$.
- **Hérédité** : si $f_n(t)=P_n(t)e^t$ sur $[0,1]$, cette expression est dérivable sur $\mathbb R$ de dérivée continue $(P_n'(t)+P_n(t))e^t$.
  Les limites de $f_n'$ en $0^+$ et $1^-$ sont donc les valeurs de cette expression en $0$ et $1$.
  Pour $t\in[0,1]$, $f_{n+1}(t)=tf_n'(t)=t(P_n'(t)+P_n(t))e^t=P_{n+1}(t)e^t$.

Donc $f_n(t)=P_n(t)e^t$ pour tout $n$ et tout $t\in[0,1]$.

### Question 9

> [!INDICATION]
> Évaluez la question 8 en $t=1$ et utilisez la relation définissant $P_{n+1}$.

#### Solution

$f_{n+1}(1)=(P_n'(1)+P_n(1))e=f_n(1)+eP_n'(1)\geqslant f_n(1)$ car $P_n'(1)\geqslant0$.

### Question 10

> [!INDICATION]
> Raisonnez par récurrence sur $n$ à l'aide de la relation de la question 7.

> [!INDICATION]
> L'hérédité utilise les deux inégalités de l'hypothèse de récurrence, puis la question 9.

#### Solution

Avec $J_n=\int_0^1f_n$ : $0<J_0=e-1<e=f_0(1)$. Si $0<J_n<f_n(1)$, alors $J_{n+1}=f_n(1)-J_n>0$ et $J_{n+1}<f_n(1)\leqslant f_{n+1}(1)$.

> [!METHODE]
> Une relation de récurrence entre intégrales ($J_{n+1}=f_n(1)-J_n$) se prête à une récurrence sur un encadrement : c'est souvent plus simple qu'un calcul explicite.

### Question 11

> [!INDICATION]
> Normalisez par l'intégrale, dont la question 10 garantit qu'elle est strictement positive.

#### Solution

$c_n=\dfrac1{\int_0^1f_n(t)\,dt}>0$ ; $c_nf_n$ est positive ($P_n\geqslant0$), continue sauf en $0$ et $1$, d'intégrale $1$ : c'est une densité.

## Bilan

**Méthodes à retenir.**

- Polynôme annulateur, valeurs propres possibles, vecteurs propres, $A=PDP^{-1}$ et $A^n=PD^nP^{-1}$ : la chaîne complète du calcul des puissances d'une matrice $2\times2$.
- Système de suites : écriture $X_{n+1}=AX_n$, puis $X_n=A^nX_0$.
- Suite $w_{n+1}=g(w_n)$ : points fixes, intervalle stable, monotonie par le signe de $g(x)-x$, limite monotone, passage à la limite par opérations sur les limites (sommes et produits) et unicité de la limite.
- Chaîne de Markov simple : formule des probabilités totales sur le système complet $(X_k=j)_j$, puis récurrence sur les espérances (suite arithmético-géométrique).
- Densités : vérification des trois conditions, normalisation, fonction de répartition par morceaux, intégration par parties.

**Prérequis à revoir.** Trinôme du second degré (racines, signe, sommet), dérivabilité d'un polynôme, intégration par parties et ses hypothèses, syntaxe SQL avec `AND` et `INNER JOIN`, indices de tableaux en Python.

**Questions transposables.** Le modèle logistique et la marche aléatoire sur un segment (modèle d'Ehrenfest) sont des classiques ; la méthode « point fixe puis suite géométrique » sert pour toute suite arithmético-géométrique.
