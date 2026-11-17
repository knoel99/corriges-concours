# ECRICOME ECG — Mathématiques approfondies 2026 · Corrigé guidé

*Corrigé rédigé par IA, non officiel. Signalez toute erreur.*

## Présentation du sujet

**Format.** Épreuve de 4 heures, sans document ni calculatrice. Deux exercices et un problème indépendants, 81 questions en comptant les sous-questions.

**Découpage.**

| Partie | Thème | Notions du programme ECG approfondies |
|---|---|---|
| Exercice 1 | Intégrale de Frullani $\int_0^{+\infty}\frac{e^{-t}-e^{-at}}t\,dt=\ln a$, puis $\int_0^1\frac{u-1}{\ln u}\,du=\ln2$ | intégrales impropres, critères de comparaison, changement de variable, sommes de Riemann, méthode de Monte-Carlo |
| Exercice 2 | Endomorphisme $\varphi(P)=(x^2-1)P''+5xP'$ et polynômes orthogonaux (de Gegenbauer) | matrice d'un endomorphisme, valeurs propres, diagonalisation, parité, produit scalaire, endomorphisme symétrique, base orthogonale, relation de récurrence à trois termes, Python |
| Problème, I | Attente de $r$ zéros consécutifs avec un dé à $d+1$ faces | loi géométrique, espérance conditionnelle, formule de l'espérance totale |
| Problème, II | Premier instant où la somme des lancers atteint $d$ | convolution discrète, simulation, $\mathbb E(V)=\sum\mathbb P(V\ge n)$, formule de Taylor avec reste intégral, limite $e$ |
| Problème, III | Même question pour des lancers uniformes sur $[0,d]$ | densité d'une somme (convolution), récurrence, $\mathbb E(T)=e$ |

**Difficulté.** Exercices de difficulté moyenne, problème plus exigeant. Les questions qui demandent du soin : 1.2.(a)–(b) (signe de l'intégrande), 1.3, 1.4 (changement de variable), 2.4.(d)–(g), 2.9.(c)–(d), pb 2.(b), 3.(a), 7, 8.(c)–(d), 10.(b). Moyenne 11,2 sur 20, écart-type 5,6 (rapport 2026). Le rapport regrette que, faute de temps, le problème soit souvent traité superficiellement : il contient pourtant des questions faciles (1.(c), 4, 5.(a), 9.(a), 11, 12.(a)).

**Gestion du temps.** Environ 50 minutes pour l'exercice 1, 1 h 30 pour l'exercice 2, 1 h 40 pour le problème.

## Exercice 1 — Intégrale de Frullani

On montre que $G(a)=\int_0^{+\infty}\frac{e^{-t}-e^{-at}}t\,dt$ vaut $\ln a$, on en déduit $\int_0^1\frac{u-1}{\ln u}\,du=\ln2$, puis on compare deux méthodes d'approximation numérique.

### Question 1.(a)

> [!INDICATION]
> L'intégrande a-t-il une limite finie en $0$ ?

#### Solution

$t\mapsto\frac{1-e^{-t}}t$ est continue sur $]0,1]$.

Comme $e^{-t}=1-t+o(t)$ en $0$, $\frac{1-e^{-t}}t\to1$ quand $t\to0$ : la fonction se prolonge par continuité en $0$.

L'intégrale est faussement impropre en $0$ : **$\int_0^1\frac{1-e^{-t}}t\,dt$ converge.**

> [!JURY]
> Le rapport 2026 : « La continuité de l’intégrande est bien trop souvent oubliée. »

### Question 1.(b)

> [!INDICATION]
> Majorez par $e^{-t}$ sur $[1,+\infty[$.

#### Solution

Sur $[1,+\infty[$, $t\mapsto\frac{e^{-t}}t$ est continue et $0\le\frac{e^{-t}}t\le e^{-t}$. Comme $\int_1^{+\infty}e^{-t}\,dt$ converge, par comparaison de fonctions positives, **$\int_1^{+\infty}\frac{e^{-t}}t\,dt$ converge.**

### Question 2.(a)

> [!INDICATION]
> Étudiez séparément les bornes $0$ et $+\infty$. En $0$, cherchez une limite finie.

> [!INDICATION]
> En $+\infty$, l'intégrande n'est pas de signe constant a priori : étudiez la convergence absolue.

#### Solution

Soit $a>0$ et $g_a(t)=\frac{e^{-t}-e^{-at}}t$, continue sur $]0,+\infty[$.
- En $0$ : $e^{-t}-e^{-at}=(1-t)-(1-at)+o(t)=(a-1)t+o(t)$, donc $g_a(t)\to a-1$ : faussement impropre, $\int_0^1g_a$ converge.
- En $+\infty$ : pour $t\ge1$, $|g_a(t)|\le e^{-t}+e^{-at}$, et $\int_1^{+\infty}e^{-t}\,dt$, $\int_1^{+\infty}e^{-at}\,dt$ convergent ($a>0$). Par comparaison, $\int_1^{+\infty}|g_a|$ converge, donc $\int_1^{+\infty}g_a$ converge (absolument).

**$\int_0^{+\infty}\frac{e^{-t}-e^{-at}}t\,dt$ converge.**

> [!JURY]
> Le rapport 2026 : « Beaucoup de copies ne remarquent pas que la fonction étudiée n’est pas positive (ou de signe constant). » D'où la convergence absolue.

### Question 2.(b)

> [!INDICATION]
> Pour $a\le0$ et $t\ge1$, minorez $e^{-at}-e^{-t}$ par une constante strictement positive.

#### Solution

Soit $a\le0$. Pour $t\ge1$, $e^{-at}\ge1$ (car $-at\ge0$) et $e^{-t}\le e^{-1}$, donc
$$-g_a(t)=\frac{e^{-at}-e^{-t}}t\ge\frac{1-e^{-1}}t>0.$$
$\int_1^{+\infty}\frac{dt}t$ diverge (Riemann) ; par comparaison de fonctions positives, $\int_1^{+\infty}(-g_a)$ diverge. **Pour $a\le0$ (y compris $a=0$), l'intégrale diverge.**

> [!JURY]
> Le rapport 2026 : « Le fait qu’un critère de comparaison ne fonctionne pas ne permet pas d’affirmer que l’intégrale diverge. » et « La distinction a = 0 et a < 0 est peu faite. » La minoration ci-dessus couvre les deux cas.

### Question 3.(a)

> [!INDICATION]
> Avec l'indication, écrivez l'intégrale comme différence de deux intégrales **convergentes** sur $]0,x]$, puis changement de variable $u=at$ dans la première.

#### Solution

Soit $x>0$.

Pour $c>0$, $t\mapsto\frac{1-e^{-ct}}t$ est continue sur $]0,+\infty[$ et tend vers $c$ en $0$ : $\int_0^y\frac{1-e^{-ct}}t\,dt$ converge pour tout $y>0$.

Par linéarité (intégrales convergentes) :
$$\int_0^x\frac{e^{-t}-e^{-at}}t\,dt=\int_0^x\frac{1-e^{-at}}t\,dt-\int_0^x\frac{1-e^{-t}}t\,dt.$$
Le changement de variable affine $u=at$ ($a>0$) donne $\int_0^x\frac{1-e^{-at}}t\,dt=\int_0^{ax}\frac{1-e^{-u}}u\,du$. Par la relation de Chasles :
$$\begin{aligned}
\int_0^x\frac{e^{-t}-e^{-at}}t\,dt&=\int_x^{ax}\frac{1-e^{-u}}u\,du\\
&=\int_x^{ax}\frac{du}u-\int_x^{ax}\frac{e^{-u}}u\,du\\
&=\ln(a)-\int_x^{ax}\frac{e^{-t}}t\,dt.
\end{aligned}$$

> [!JURY]
> Le rapport 2026 : peu de copies justifient la convergence avant d'utiliser la linéarité, ce qui conduit certains à séparer $\int_0^1\frac{e^{-t}}t\,dt$, qui diverge.

### Question 3.(b)

> [!INDICATION]
> Faites tendre $x$ vers $+\infty$ et majorez $\left|\int_x^{ax}\frac{e^{-t}}t\,dt\right|$.

#### Solution

Pour $x\ge\max\left(1,\frac1a\right)$, tout $t$ entre $x$ et $ax$ vérifie $t\ge1$, donc $0\le\frac{e^{-t}}t\le e^{-t}$ et
$$\left|\int_x^{ax}\frac{e^{-t}}t\,dt\right|\le\left|\int_x^{ax}e^{-t}\,dt\right|=\left|e^{-x}-e^{-ax}\right|\xrightarrow[x\to+\infty]{}0.$$
En faisant tendre $x$ vers $+\infty$ dans 3.(a) : $\boxed{G(a)=\ln(a)}$.

### Question 4

> [!INDICATION]
> $t\mapsto e^{-t}$ est une bijection de classe $\mathcal C^1$ strictement monotone : de quel intervalle sur quel intervalle ?

> [!INDICATION]
> Après changement de variable, reconnaissez $G(2)$.

#### Solution

La fonction $t\mapsto e^{-t}$ est de classe $\mathcal C^1$, strictement décroissante, bijective de $]0,+\infty[$ sur $]0,1[$.

Avec $u=e^{-t}$, $du=-e^{-t}\,dt$ et $\ln u=-t$ :
$$\frac{u-1}{\ln u}\,du=\frac{e^{-t}-1}{-t}\cdot(-e^{-t})\,dt=-\frac{e^{-t}-e^{-2t}}t\,dt.$$
Par le théorème de changement de variable (les bornes s'échangent : $t\to0$ donne $u\to1$, $t\to+\infty$ donne $u\to0$), $\int_0^1\frac{u-1}{\ln u}\,du$ et $\int_0^{+\infty}\frac{e^{-t}-e^{-2t}}t\,dt=G(2)$ sont de même nature, donc convergentes (question 2.(a)), et égales :
$$\boxed{\int_0^1\frac{u-1}{\ln u}\,du=G(2)=\ln2}.$$

> [!JURY]
> Le rapport 2026 : « Une rédaction propre et rigoureuse du changement de variable est attendue. » Préciser classe, monotonie stricte, intervalles de départ et d'arrivée.

### Question 5.(a)

> [!INDICATION]
> Question de cours.

#### Solution

Ce sont des sommes de Riemann : pour $\varphi$ continue sur $[0,1]$, $\displaystyle\lim_{n\to+\infty}\frac1n\sum_{k=0}^{n-1}\varphi\left(\frac kn\right)=\int_0^1\varphi(u)\,du$.

### Question 5.(b)

> [!INDICATION]
> Attention au terme $k=0$ : $f(0)=0$ et $\ln 0$ n'existe pas.

#### Solution

```python
import numpy as np

def Rect(n):
    s = 0
    for k in range(n):
        u = k/n
        if u == 0:
            s = s + 0          # f(0) = 0
        else:
            s = s + (u-1)/np.log(u)
    return s/n
```
Pour $0\le k\le n-1$, $u=\frac kn<1$ : seul le cas $u=0$ est particulier. Essai : `Rect(1000)` $\approx0{,}6926$ ($\ln2\approx0{,}6931$).

### Question 5.(c)

> [!INDICATION]
> Quelle est la loi des `U[k]` ? Que calcule la moyenne des $f(U_k)$ ?

#### Solution

`U` contient $n$ simulations indépendantes de la loi uniforme sur $[0,1[$, et `s` la somme des $f(U_k)$ (le test traite les valeurs $0$ et $1$ où $f(u)=u$).

La fonction renvoie $\frac1n\sum_{k=1}^nf(U_k)$, une réalisation de la moyenne empirique de $n$ copies indépendantes de $f(U)$, où $U\hookrightarrow\mathcal U([0,1])$.

Par le théorème de transfert, $\mathbb E(f(U))=\int_0^1f(u)\,du=\ln2$, et $f(U)$ est bornée ($f$ continue sur $[0,1]$), donc admet une variance.

Par la loi faible des grands nombres, cette moyenne converge en probabilité vers $\ln2$ : **`prog(n)` renvoie une approximation de $\int_0^1\frac{u-1}{\ln u}\,du=\ln2$ par la méthode de Monte-Carlo.**

> [!JURY]
> Le rapport 2026 regrette que si peu de copies comprennent cette méthode de Monte-Carlo, explicitement au programme, et la loi des grands nombres qu'elle met en jeu.

### Question 5.(d)

> [!INDICATION]
> Comparez la régularité et la vitesse de stabilisation des deux courbes.

#### Solution

La suite en pointillés (sommes de Riemann, question 5.(b)) se stabilise très vite et régulièrement près de $\ln2\approx0{,}693$ ; la suite en trait plein (Monte-Carlo, 5.(c)) oscille encore nettement (entre $0{,}68$ et $0{,}70$) pour $n$ de l'ordre de $1000$.

**La méthode des rectangles donne la meilleure approximation.** C'est attendu : $f$ est monotone et régulière, l'erreur des sommes de Riemann est de l'ordre de $\frac1n$, alors que l'écart aléatoire de Monte-Carlo est de l'ordre de $\frac1{\sqrt n}$ (Bienaymé-Tchebychev).

## Exercice 2 — Un endomorphisme de polynômes et ses vecteurs propres

On diagonalise $\varphi(P)=(x^2-1)P''+5xP'$ sur $\mathbb R_n[x]$ ; ses vecteurs propres unitaires $G_k$ sont orthogonaux pour un produit scalaire à poids $(1-t^2)^{3/2}$ et vérifient une relation de récurrence à trois termes.

### Question 1.(a)

> [!INDICATION]
> Forme de la matrice.

#### Solution

$A$ est triangulaire supérieure : ses valeurs propres sont ses coefficients diagonaux. $\boxed{\operatorname{Sp}(A)=\{0,5,12\}}$.

### Question 1.(b)

> [!INDICATION]
> Nombre de valeurs propres distinctes et taille de la matrice.

#### Solution

$A\in\mathcal M_3(\mathbb R)$ admet $3$ valeurs propres distinctes : **$A$ est diagonalisable.**

> [!PIEGE]
> « Triangulaire donc diagonalisable » est faux (penser à $\begin{pmatrix}0&1\\0&0\end{pmatrix}$).

### Question 1.(c)

> [!INDICATION]
> Cherchez un vecteur propre pour chaque valeur propre.

#### Solution

- $\lambda=0$ : $AX=0$ donne $-2z=0$, $5y=0$, soit $X=(1,0,0)^T$ à un facteur près.
- $\lambda=5$ : $(A-5I)X=0$ donne $-5x-2z=0$, $7z=0$, soit $X=(0,1,0)^T$.
- $\lambda=12$ : $(A-12I)X=0$ donne $-12x-2z=0$, $-7y=0$, soit $X=(1,0,-6)^T$.
$$\boxed{V=\begin{pmatrix}1&0&1\\0&1&0\\0&0&-6\end{pmatrix},\qquad D=\begin{pmatrix}0&0&0\\0&5&0\\0&0&12\end{pmatrix}},\qquad A=VDV^{-1},$$
$V$ étant inversible (ses colonnes sont des vecteurs propres associés à des valeurs propres distinctes ; ou $\det V=-6\neq0$).

### Question 2.(a)

> [!INDICATION]
> Dérivez $x^k$ deux fois et développez.

#### Solution

$\varphi(P_0)=0$, $\varphi(P_1)=5x=5P_1$, et pour $k\in[\![2,n]\!]$ :
$$\begin{aligned}
\varphi(P_k)&=(x^2-1)k(k-1)x^{k-2}+5kx^k\\
&=k(k+4)x^k-k(k-1)x^{k-2}.
\end{aligned}$$
$$\boxed{\varphi(P_k)=k(k+4)P_k-k(k-1)P_{k-2}}$$

### Question 2.(b)

> [!INDICATION]
> Écrivez $P=x^d+\sum_{j<d}c_jx^j$ et utilisez 2.(a) par linéarité.

#### Solution

Soit $P=x^d+\sum_{j=0}^{d-1}c_jx^j$.

Par linéarité de la dérivation, $\varphi$ est linéaire, donc $\varphi(P)=\varphi(P_d)+\sum_{j<d}c_j\varphi(P_j)$.

D'après 2.(a), chaque $\varphi(P_j)$, $j<d$, est de degré au plus $j<d$, et $\varphi(P_d)=d(d+4)x^d+(\text{degré}<d)$.
- Si $d\ge1$ : **$\varphi(P)$ est de degré $d$, de coefficient dominant $d(d+4)$.**
- Si $d=0$ : $P=1$ et $\varphi(P)=0$ (polynôme nul).

> [!JURY]
> Le rapport 2026 : « le cas d = 0 a souvent été oublié ».

### Question 3.(a)

> [!INDICATION]
> Linéarité de la dérivation ; degré de $\varphi(P)$ par 2.(b).

#### Solution

- *Linéarité.* Pour $P,Q\in\mathbb R_n[x]$ et $\lambda\in\mathbb R$, $(\lambda P+Q)'=\lambda P'+Q'$ et $(\lambda P+Q)''=\lambda P''+Q''$, donc $\varphi(\lambda P+Q)=\lambda\varphi(P)+\varphi(Q)$.
- *Stabilité.* Si $P\in\mathbb R_n[x]$ est non nul de degré $d\le n$, $\frac1{c}P$ est unitaire ($c$ coefficient dominant) et par 2.(b), $\varphi(P)$ est de degré au plus $d\le n$ ; et $\varphi(0)=0$.

**$\varphi$ est un endomorphisme de $\mathbb R_n[x]$.**

### Question 3.(b)

> [!INDICATION]
> Placez en colonne $k$ les coordonnées de $\varphi(P_k)$ (question 2.(a)).

#### Solution

Numérotons lignes et colonnes de $0$ à $n$. D'après 2.(a), dans la base $(P_0,\dots,P_n)$, la matrice $M=(m_{i,k})$ de $\varphi$ a pour coefficients
$$\begin{aligned}
m_{k,k}&=k(k+4)\ (0\le k\le n)\\
m_{k-2,k}&=-k(k-1)\ (2\le k\le n)
\end{aligned}$$
tous les autres étant nuls. Elle est triangulaire supérieure, de diagonale $\big(k(k+4)\big)_{0\le k\le n}$, avec une seule « surdiagonale » non nulle, deux rangs au-dessus. Par exemple, pour $n=4$ :
$$\begin{pmatrix}0&0&-2&0&0\\0&5&0&-6&0\\0&0&12&0&-12\\0&0&0&21&0\\0&0&0&0&32\end{pmatrix}.$$

### Question 3.(c)

> [!INDICATION]
> Utilisez 2.(b) pour un polynôme quelconque de degré au plus $k$.

#### Solution

Soit $k\in[\![0,n]\!]$ et $P\in\mathbb R_k[x]$.

Si $P=0$, $\varphi(P)=0\in\mathbb R_k[x]$.

Sinon, $P=c\,Q$ avec $Q$ unitaire de degré $d\le k$, et $\varphi(P)=c\,\varphi(Q)$ est, par 2.(b), de degré au plus $d\le k$.

**$\mathbb R_k[x]$ est stable par $\varphi$.**

### Question 3.(d)

> [!INDICATION]
> Cas $n=2$ de 3.(b).

#### Solution

$\Psi(1)=0$, $\Psi(x)=5x$, $\Psi(x^2)=12x^2-2$. Dans la base $(1,x,x^2)$ :
$$\operatorname{Mat}(\Psi)=\begin{pmatrix}0&0&-2\\0&5&0\\0&0&12\end{pmatrix}=A.$$

### Question 4.(a)

> [!INDICATION]
> Matrice triangulaire.

#### Solution

La matrice de $\varphi$ dans la base canonique est triangulaire supérieure (3.(b)) : ses valeurs propres sont ses coefficients diagonaux. $\boxed{\operatorname{Sp}(\varphi)=\{k(k+4),\ k\in[\![0,n]\!]\}}$.

### Question 4.(b)

> [!INDICATION]
> Injectivité de $x\mapsto x(x+4)$ sur $\mathbb R_+$.

#### Solution

$h:x\mapsto x(x+4)$ a pour dérivée $2x+4>0$ sur $\mathbb R_+$ : elle est strictement croissante, donc injective sur $\mathbb R_+$.

Les $n+1$ réels $k(k+4)$, $k\in[\![0,n]\!]$, sont donc deux à deux distincts : **$\varphi$ admet $n+1$ valeurs propres distinctes.**

### Question 4.(c)

> [!INDICATION]
> Comparez le nombre de valeurs propres distinctes à la dimension.

#### Solution

$\varphi$ est un endomorphisme de $\mathbb R_n[x]$, espace de dimension $n+1$, et admet $n+1$ valeurs propres distinctes : **$\varphi$ est diagonalisable**, et chacun de ses sous-espaces propres est de dimension $1$.

> [!JURY]
> Le rapport 2026 : préciser $\dim\mathbb R_n[x]=n+1$ est attendu ; « Dire seulement que φ est diagonalisable parce qu’elle admet n + 1 valeurs propres distinctes n’est pas suffisant. »

### Question 4.(d)

> [!INDICATION]
> Le sous-espace propre est une droite : il est engendré par un polynôme non nul. Normalisez-le.

> [!INDICATION]
> Pour l'unicité : deux polynômes unitaires colinéaires sont égaux.

#### Solution

Soit $k\in[\![0,n]\!]$.

D'après 4.(c), $E_{k(k+4)}(\varphi)$ est de dimension $1$ : il existe $Q\neq0$ tel que $E_{k(k+4)}(\varphi)=\operatorname{Vect}(Q)$.

Soit $c\neq0$ le coefficient dominant de $Q$ ;

$G_k=\frac1cQ$ est unitaire et $\operatorname{Vect}(G_k)=\operatorname{Vect}(Q)$ : **existence**.

*Unicité.* Si $G$ et $G'$ sont unitaires avec $\operatorname{Vect}(G)=\operatorname{Vect}(G')$, alors $G'=\mu G$ ; en comparant les coefficients dominants (même degré), $\mu=1$ et $G'=G$.

### Question 4.(e)

> [!INDICATION]
> Utilisez 2.(a) et l'unicité de 4.(d).

#### Solution

$\varphi(1)=0=0\cdot1$ et $1$ est unitaire : $G_0=1$. $\varphi(x)=5x=1\cdot(1+4)x$ et $x$ est unitaire : $G_1=x$.

### Question 4.(f)

> [!INDICATION]
> Calculez $\varphi\left(x^2-\frac16\right)$ ; n'oubliez pas l'unicité.

#### Solution

$\varphi\left(x^2-\frac16\right)=12x^2-2=12\left(x^2-\frac16\right)$ : $x^2-\frac16$ est un vecteur propre (non nul) associé à $12=2(2+4)$, et il est unitaire. Par l'unicité de 4.(d), $G_2(x)=x^2-\frac16$.

> [!JURY]
> Le rapport 2026 : « Beaucoup oublient de préciser que G2 est unitaire et d’utiliser l’unicité de la question 4.(d). »

### Question 4.(g)

> [!INDICATION]
> Comparez le degré et le coefficient dominant des deux membres de $\varphi(G_k)=k(k+4)G_k$ (question 2.(b)).

#### Solution

Soit $d$ le degré de $G_k$ (non nul, unitaire).

Si $d\ge1$, par 2.(b) le coefficient dominant de $\varphi(G_k)$ est $d(d+4)$, celui de $k(k+4)G_k$ est $k(k+4)$ ; donc $d(d+4)=k(k+4)$ et $d=k$ par injectivité (4.(b)).

Si $d=0$, $G_k=1$ et $\varphi(G_k)=0=k(k+4)G_k$, d'où $k=0=d$.

**$\deg G_k=k$.**

### Question 5.(a)

> [!INDICATION]
> Dérivée d'une composée avec $x\mapsto-x$.

#### Solution

$Q'(x)=-P'(-x)$ et $Q''(x)=P''(-x)$.

### Question 5.(b)

> [!INDICATION]
> Calculez $\varphi(Q)(x)$ et reconnaissez $\varphi(P)(-x)$. N'oubliez pas $Q\neq0$.

#### Solution

$$\begin{aligned}
\varphi(Q)(x)&=(x^2-1)P''(-x)-5xP'(-x)\\
&=\big((-x)^2-1\big)P''(-x)+5(-x)P'(-x)\\
&=\varphi(P)(-x)=k(k+4)P(-x)=k(k+4)Q(x).
\end{aligned}$$
$Q\neq0$ car $P\neq0$ ($P(-x)$ a le même degré que $P$).

**$Q$ est un vecteur propre de $\varphi$ associé à $k(k+4)$.**

> [!JURY]
> Le rapport 2026 : « La non-nullité de Q n’a presque jamais été évoquée. »

### Question 5.(c)

> [!INDICATION]
> Par 5.(b) et 4.(d), $G_k(-x)$ est colinéaire à $G_k(x)$ ; identifiez le coefficient avec le terme dominant.

#### Solution

Par 5.(b) avec $P=G_k$, $x\mapsto G_k(-x)$ appartient à $E_{k(k+4)}(\varphi)=\operatorname{Vect}(G_k)$ : $G_k(-x)=\mu G_k(x)$.

Le coefficient dominant de $G_k(-x)$ est $(-1)^k$ (degré $k$, 4.(g)), donc $\mu=(-1)^k$.

**$G_k$ est pair si $k$ est pair, impair si $k$ est impair.**

### Question 6

> [!INDICATION]
> Vérifiez : bien défini, symétrique, bilinéaire, positif, défini ; pour le caractère défini, une intégrale nulle d'une fonction continue positive.

#### Solution

Pour $P,Q\in\mathbb R_n[x]$, $t\mapsto P(t)Q(t)(1-t^2)^{3/2}$ est continue sur le segment $[-1,1]$ : $\langle P,Q\rangle$ est bien défini.
- *Symétrie* : $P(t)Q(t)=Q(t)P(t)$, donc $\langle P,Q\rangle=\langle Q,P\rangle$.
- *Linéarité à gauche* : pour $\lambda\in\mathbb R$, $(\lambda P_1+P_2)Q\,w=\lambda P_1Q\,w+P_2Q\,w$ avec $w(t)=(1-t^2)^{3/2}$, et l'intégrale est linéaire ; avec la symétrie, $\langle\,,\rangle$ est bilinéaire.
- *Positivité* : $P(t)^2w(t)\ge0$ sur $[-1,1]$, et $-1<1$, donc $\langle P,P\rangle\ge0$.
- *Défini* : si $\langle P,P\rangle=0$, la fonction $P^2w$, **continue** et positive sur $[-1,1]$, est d'intégrale nulle, donc nulle sur $[-1,1]$. Comme $w>0$ sur $]-1,1[$, $P$ s'annule sur $]-1,1[$ : il a une infinité de racines, donc $P=0$.

**$\langle\,,\rangle$ est un produit scalaire sur $\mathbb R_n[x]$.**

> [!JURY]
> Le rapport 2026 : « Pour le caractère défini du produit scalaire, la continuité de l’intégrande est trop souvent oubliée. »

### Question 7.(a)

> [!INDICATION]
> La fonction $\sin$ est-elle une bijection $\mathcal C^1$ strictement monotone ? Sur quel intervalle ?

#### Solution

$s\mapsto\sin s$ est de classe $\mathcal C^1$ et strictement croissante sur $\left[-\frac\pi2,\frac\pi2\right]$, bijective sur $[-1,1]$.

Avec $t=\sin s$, $dt=\cos s\,ds$ et, comme $\cos s\ge0$ sur cet intervalle, $(1-\sin^2s)^{3/2}=(\cos^2s)^{3/2}=\cos^3s$.

Donc
$$\int_{-1}^1(1-t^2)^{3/2}\,dt=\int_{-\pi/2}^{\pi/2}\cos^3s\cdot\cos s\,ds=\int_{-\pi/2}^{\pi/2}\cos^4s\,ds.$$

> [!JURY]
> Le rapport 2026 : la classe $\mathcal C^1$ et la stricte monotonie sont peu évoquées, et les intervalles de départ et d'arrivée de $\sin$ souvent faux.

### Question 7.(b)

> [!INDICATION]
> Linéarisez avec $\cos^2u=\frac{1+\cos 2u}2$.

#### Solution

Avec $\cos^2u=\frac{1+\cos(2u)}2$ (deux fois) :
$$\begin{aligned}
\cos^4s&=\frac{\big(1+\cos(2s)\big)^2}4=\frac{1+2\cos(2s)+\cos^2(2s)}4\\
&=\frac14\left(1+2\cos(2s)+\frac{1+\cos(4s)}2\right)\\
&=\frac18\big(\cos(4s)+4\cos(2s)+3\big).
\end{aligned}$$

### Question 7.(c)

> [!INDICATION]
> $\|G_0\|^2=\int_{-1}^1(1-t^2)^{3/2}\,dt$.

#### Solution

$G_0=1$, donc par 7.(a) et 7.(b) :
$$\begin{aligned}
\|G_0\|^2&=\int_{-\pi/2}^{\pi/2}\frac{\cos(4s)+4\cos(2s)+3}8\,ds\\
&=\frac18\left(\left[\frac{\sin(4s)}4\right]_{-\pi/2}^{\pi/2}+4\left[\frac{\sin(2s)}2\right]_{-\pi/2}^{\pi/2}+3\pi\right)=\boxed{\frac{3\pi}8}.
\end{aligned}$$

### Question 8.(a)

> [!INDICATION]
> Dérivée d'un produit et de $u^{5/2}$ composée avec $1-t^2$.

#### Solution

$u\mapsto u^{5/2}$ est de classe $\mathcal C^1$ sur $[0,+\infty[$, donc $t\mapsto(1-t^2)^{5/2}$ est de classe $\mathcal C^1$ sur $[-1,1]$, de dérivée $\frac52(1-t^2)^{3/2}(-2t)$.

Par dérivation d'un produit :
$$\begin{aligned}
\left(P'(t)(1-t^2)^{5/2}\right)'&=P''(t)(1-t^2)^{5/2}-5tP'(t)(1-t^2)^{3/2}\\
&=(1-t^2)^{3/2}\big((1-t^2)P''(t)-5tP'(t)\big)\\
&=-(1-t^2)^{3/2}\varphi(P)(t).
\end{aligned}$$

### Question 8.(b)

> [!INDICATION]
> Écrivez $\varphi(P)(t)(1-t^2)^{3/2}$ grâce à 8.(a), puis intégration par parties sur $[-1,1]$.

#### Solution

D'après 8.(a), $\langle\varphi(P),Q\rangle=-\int_{-1}^1\left(P'(t)(1-t^2)^{5/2}\right)'Q(t)\,dt$. Les fonctions $t\mapsto P'(t)(1-t^2)^{5/2}$ et $Q$ sont de classe $\mathcal C^1$ sur le segment $[-1,1]$ ; par intégration par parties :
$$\langle\varphi(P),Q\rangle=-\Big[P'(t)(1-t^2)^{5/2}Q(t)\Big]_{-1}^1+\int_{-1}^1P'(t)Q'(t)(1-t^2)^{5/2}\,dt.$$
Le crochet est nul car $1-t^2=0$ en $\pm1$. D'où le résultat.

### Question 8.(c)

> [!INDICATION]
> Échangez $P$ et $Q$ dans 8.(b).

#### Solution

L'expression de 8.(b) est symétrique en $P$ et $Q$, donc $\langle\varphi(P),Q\rangle=\langle\varphi(Q),P\rangle=\langle P,\varphi(Q)\rangle$ : **$\varphi$ est un endomorphisme symétrique** de l'espace euclidien $\mathbb R_n[x]$.

### Question 8.(d)

> [!INDICATION]
> Deux vecteurs propres d'un endomorphisme symétrique associés à des valeurs propres **distinctes** sont orthogonaux.

#### Solution

Soit $k\in[\![1,n]\!]$.

Les $G_i$, $0\le i\le k$, sont des vecteurs propres de l'endomorphisme symétrique $\varphi$ associés aux valeurs propres $i(i+4)$, deux à deux distinctes (4.(b)) : ils sont deux à deux orthogonaux.

Non nuls, ils forment une famille libre.

Ils sont dans $\mathbb R_k[x]$ ($\deg G_i=i$) et sont au nombre de $k+1=\dim\mathbb R_k[x]$.

**$(G_0,\dots,G_k)$ est une base orthogonale de $\mathbb R_k[x]$.**

> [!JURY]
> Le rapport 2026 : « Ici le fait que les vecteurs propres soient associés à des valeurs propres deux à deux distinctes est très important et rarement précisé. »

### Question 8.(e)

> [!INDICATION]
> Base de $\mathbb R_{k-1}[x]$ par 8.(d).

#### Solution

Soit $k\in[\![1,n]\!]$.

Par 8.(d) (ou directement pour $k=1$), $\mathbb R_{k-1}[x]=\operatorname{Vect}(G_0,\dots,G_{k-1})$, et $G_k$ est orthogonal à chaque $G_i$, $i<k$.

Par bilinéarité, **$G_k$ est orthogonal à tout élément de $\mathbb R_{k-1}[x]$.**

### Question 9.(a)

> [!INDICATION]
> Associativité du produit des fonctions.

#### Solution

$\langle PQ,R\rangle=\int_{-1}^1\big(P(t)Q(t)\big)R(t)w(t)\,dt=\int_{-1}^1P(t)\big(Q(t)R(t)\big)w(t)\,dt=\langle P,QR\rangle$ (les produits restent de degré quelconque : l'intégrale a un sens pour tous polynômes).

### Question 9.(b)

> [!INDICATION]
> Décomposition dans une base orthogonale.

#### Solution

Si $d\ge1$, $P\in\mathbb R_d[x]$, qui admet la base orthogonale $(G_0,\dots,G_d)$ (8.(d)) ; si $d=0$, $P\in\mathbb R_0[x]=\operatorname{Vect}(G_0)$.

Les coordonnées d'un vecteur dans une base orthogonale sont $\frac{\langle P,G_i\rangle}{\|G_i\|^2}$ (on écrit $P=\sum c_iG_i$ et on fait le produit scalaire avec $G_j$).

Donc $P=\sum_{i=0}^d\frac{\langle P,G_i\rangle}{\|G_i\|^2}G_i$.

### Question 9.(c)

> [!INDICATION]
> Appliquez 9.(b) à $xG_k$ ; montrez que les coefficients d'indice $i\le k-2$ sont nuls avec 9.(a) et 8.(e).

#### Solution

Soit $k\in[\![1,n-1]\!]$. $xG_k$ est de degré $k+1\le n$ ; par 9.(b) :
$$xG_k=\sum_{i=0}^{k+1}\frac{\langle xG_k,G_i\rangle}{\|G_i\|^2}G_i.$$
Pour $i\le k-2$, par 9.(a), $\langle xG_k,G_i\rangle=\langle G_k,xG_i\rangle=0$ par 8.(e), car $xG_i\in\mathbb R_{k-1}[x]$. Il reste $xG_k=\alpha_kG_{k+1}+\beta_kG_k+\gamma_kG_{k-1}$ : **existence**. **Unicité** : la famille $(G_{k-1},G_k,G_{k+1})$ est orthogonale de vecteurs non nuls, donc libre, et la décomposition est unique.

> [!JURY]
> Le rapport 2026 : les rares copies qui traitent la question « oublient souvent de justifier l’unicité des coefficients ».

### Question 9.(d)

> [!INDICATION]
> $\alpha_k$ : coefficients dominants. $\beta_k$ : parité (5.(c)) et unicité de 9.(c).

#### Solution

*$\alpha_k=1$.* $xG_k$ est unitaire de degré $k+1$ ; dans le membre de droite, seul $G_{k+1}$ (unitaire, degré $k+1$, 4.(g)) contribue au terme de degré $k+1$.

Donc $\alpha_k=1$.

*$\beta_k=0$.* Changeons $x$ en $-x$. Par 5.(c), $G_j(-x)=(-1)^jG_j(x)$, donc
$$(-1)^{k+1}xG_k(x)=(-1)^{k+1}\alpha_kG_{k+1}(x)+(-1)^k\beta_kG_k(x)+(-1)^{k-1}\gamma_kG_{k-1}(x).$$
En multipliant par $(-1)^{k+1}$ : $xG_k=\alpha_kG_{k+1}-\beta_kG_k+\gamma_kG_{k-1}$. Par unicité (9.(c)), $\beta_k=-\beta_k$, donc $\beta_k=0$.

### Question 9.(e)

> [!INDICATION]
> Appliquez 9.(c) avec la bonne valeur de $k$, et les valeurs de $\alpha_k$ et $\beta_k$.

#### Solution

Avec $k=2$ : $\gamma_2=\frac{2\times5}{4\times4\times3}=\frac5{24}$ et $G_3=xG_2-\gamma_2G_1$ :
$$G_3(x)=x^3-\frac16x-\frac5{24}x=\boxed{x^3-\frac38x}.$$
Vérification : $\varphi\left(x^3-\frac38x\right)=21x^3-6x-\frac{15}8x=21\left(x^3-\frac38x\right)$, et $21=3(3+4)$.

> [!JURY]
> Le rapport 2026 : beaucoup prennent à tort $k=3$ dans la relation de 9.(c).

### Question 10.(a)

> [!INDICATION]
> Multiplier par $x$ décale chaque coefficient d'un rang vers les puissances supérieures.

#### Solution

```python
def Prod(P, n):
    Q = np.zeros(n+1)
    for k in range(n):
        Q[k+1] = P[k]
    return Q
```
(On suppose $\deg P\le n-1$, pour que $xP\in\mathbb R_n[x]$.)

### Question 10.(b)

> [!INDICATION]
> Utilisez la récurrence $G_{k+1}=xG_k-\gamma_kG_{k-1}$ avec $G_0=1$, $G_1=x$, en conservant les deux derniers termes.

#### Solution

```python
def VP(n, k):
    G0 = np.zeros(n+1)
    G0[0] = 1                      # G_0 = 1
    if k == 0:
        return G0
    G1 = np.zeros(n+1)
    G1[1] = 1                      # G_1 = x
    for j in range(1, k):
        gam = j*(j+3)/(4*(j+2)*(j+1))
        G0, G1 = G1, Prod(G1, n) - gam*G0   # (G_j, G_{j+1})
    return G1
```
Après le tour d'indice $j$, `G1` contient $G_{j+1}$ ; la fonction renvoie donc $G_k$ ($0\le k\le n$).

Essai : `VP(5, 3)` donne `[0, -0.375, 0, 1, 0, 0]`, soit $x^3-\frac38x$, et `VP(5, 4)` donne $x^4-\frac35x^2+\frac3{80}$ (vecteur propre de $\varphi$ pour $32$, vérifié).

## Problème — Partie I : attendre r zéros consécutifs

On calcule l'espérance de $X$ en conditionnant par le rang $Y$ du premier lancer non nul : si $Y\le r$, l'expérience « repart de zéro ».

### Question 1.(a)

> [!INDICATION]
> Somme géométrique qui commence à $k=1$.

#### Solution

$x\neq1$, donc $\displaystyle\sum_{k=1}^rx^k=x\,\frac{1-x^r}{1-x}$.

### Question 1.(b)

> [!INDICATION]
> Calculez $(1-x)\sum kx^{k-1}$ en décalant l'indice, puis multipliez encore par $1-x$.

#### Solution

Notons $S=\sum_{k=1}^rkx^{k-1}$.
$$\begin{aligned}
(1-x)S&=\sum_{k=1}^rkx^{k-1}-\sum_{k=2}^{r+1}(k-1)x^{k-1}\\
&=\sum_{k=1}^{r}x^{k-1}-rx^r=\frac{1-x^r}{1-x}-rx^r.
\end{aligned}$$
Donc $(1-x)^2S=1-x^r-rx^r(1-x)=\boxed{1-(r+1)x^r+rx^{r+1}}$, et
$$\sum_{k=1}^rkx^{k-1}=\frac{1-(r+1)x^r+rx^{r+1}}{(1-x)^2}.$$

### Question 1.(c)

> [!INDICATION]
> Succès = face non nulle. Quelle probabilité ?

#### Solution

Les lancers sont indépendants et chacun donne une face non nulle avec probabilité $p=\frac d{d+1}$ ; $Y$ est le rang du premier succès. **$Y\hookrightarrow\mathcal G\left(\frac d{d+1}\right)$** : $\mathbb P(Y=k)=\left(\frac1{d+1}\right)^{k-1}\frac d{d+1}$ pour $k\ge1$, et
$$\begin{aligned}
\mathbb E(Y)&=\frac{d+1}d\\
\mathbb V(Y)&=\frac{1-p}{p^2}\\
&=\frac{d+1}{d^2}.
\end{aligned}$$

### Question 1.(d)

> [!INDICATION]
> Traduisez l'événement en termes des $r$ premiers lancers ; indépendance.

#### Solution

$[Y>r]$ signifie que les $r$ premiers lancers donnent $0$. Par indépendance des lancers, $\mathbb P(Y>r)=\left(\frac1{d+1}\right)^r$.

### Question 2.(a)

> [!INDICATION]
> Que vaut $X$ lorsque les $r$ premiers lancers sont nuls ?

#### Solution

Sur $[Y>r]$, les $r$ premiers lancers sont des $0$ : on a obtenu $r$ zéros consécutifs dès le $r$-ième lancer, et pas avant.

Donc $X=r$ sur cet événement et $\mathbb E(X\mid[Y>r])=\boxed{r}$.

### Question 2.(b)

> [!INDICATION]
> Sur $[Y=i]$ avec $i\le r$, le $i$-ème lancer est non nul : la série de zéros est interrompue. Que se passe-t-il ensuite ?

#### Solution

Soit $i\in[\![1,r]\!]$.

Sur $[Y=i]$, les $i-1$ premiers lancers sont nuls et le $i$-ème ne l'est pas : on n'a pas encore $r$ zéros consécutifs (car $i-1<r$), et le compteur repart à zéro après le lancer $i$.

Le nombre de lancers supplémentaires nécessaires, $X'$, ne dépend que des lancers $i+1,i+2,\dots$, indépendants des $i$ premiers et de même loi que la suite initiale : $X'$ a la même loi que $X$ et est indépendant de $[Y=i]$.

Comme $X=i+X'$ sur $[Y=i]$ :
$$\begin{aligned}
\mathbb E(X\mid[Y=i])&=i+\mathbb E(X')\\
&=i+\mathbb E(X).
\end{aligned}$$

> [!JURY]
> Le rapport 2026 : « la « réinitialisation » du processus n’a pas été comprise ».

### Question 3.(a)

> [!INDICATION]
> Formule de l'espérance totale avec le système complet $([Y=1],\dots,[Y=r],[Y>r])$.

#### Solution

$([Y=1],\dots,[Y=r],[Y>r])$ est un système complet d'événements de probabilités non nulles. Par la formule de l'espérance totale et la question 2 :
$$\begin{aligned}
\mathbb E(X)&=\sum_{i=1}^r\mathbb P(Y=i)\big(i+\mathbb E(X)\big)+\mathbb P(Y>r)\,r\\
&=\sum_{i=1}^ri\,\mathbb P(Y=i)+\mathbb E(X)\big(1-\mathbb P(Y>r)\big)+r\,\mathbb P(Y>r),
\end{aligned}$$
car $\sum_{i=1}^r\mathbb P(Y=i)=1-\mathbb P(Y>r)$.

> [!JURY]
> Le rapport 2026 : « Le bon système complet d’événements à utiliser est rarement vu. »

### Question 3.(b)

> [!INDICATION]
> Isolez $\mathbb E(X)\,\mathbb P(Y>r)$ et calculez $\sum_{i=1}^ri\,\mathbb P(Y=i)$ avec 1.(b) pour $x=\frac1{d+1}$.

#### Solution

Posons $q=\frac1{d+1}$ et $p=1-q=\frac d{d+1}$. D'après 3.(a) : $\mathbb E(X)\,q^r=\sum_{i=1}^ri\,pq^{i-1}+rq^r$. Par 1.(b) avec $x=q$ et $(1-q)^2=p^2$ :
$$\sum_{i=1}^ri\,pq^{i-1}=\frac{1-(r+1)q^r+rq^{r+1}}p.$$
Donc
$$\begin{aligned}
\mathbb E(X)\,q^r&=\frac{1-(r+1)q^r+rq^{r+1}+rpq^r}p\\
&=\frac{1-(r+1)q^r+rq^{r+1}+rq^r-rq^{r+1}}p=\frac{1-q^r}p.
\end{aligned}$$
Ainsi $\mathbb E(X)=\frac{1-q^r}{pq^r}=\frac{d+1}d\left((d+1)^r-1\right)$, soit
$$\boxed{\mathbb E(X)=\frac1d\left((d+1)^{r+1}-d-1\right)}.$$
(Contrôle par simulation : $d=2$, $r=2$ donne $\approx11{,}96$ pour $12$.)

## Problème — Partie II : atteindre la valeur d

$T$ est le premier instant où la somme des lancers atteint $d$. On calcule $\mathbb E(T)=\left(\frac{d+1}d\right)^d$, qui tend vers $e$.

### Question 4

> [!INDICATION]
> Dé équilibré à $d+1$ faces numérotées de $0$ à $d$.

#### Solution

$U_n$ suit la **loi uniforme sur $[\![0,d]\!]$**, et $\mathbb E(U_n)=\frac{0+d}2=\boxed{\frac d2}$.

> [!JURY]
> Le rapport 2026 rappelle de ne pas confondre $[0,d]$ et $[\![0,d]\!]$, et de ne pas répondre à des questions non posées (la variance n'est pas demandée).

### Question 5.(a)

> [!INDICATION]
> Somme de deux entiers de $[\![0,d]\!]$.

#### Solution

$\boxed{S_2(\Omega)=[\![0,2d]\!]}$ (toute valeur de $0$ à $2d$ est atteinte, par exemple $k=\min(k,d)+(k-\min(k,d))$).

### Question 5.(b)

> [!INDICATION]
> Système complet $([U_1=i])_{0\le i\le d}$, puis indépendance de $U_1$ et $U_2$.

#### Solution

Soit $k\in[\![0,2d]\!]$. Les événements $[U_1=i]$, $i\in[\![0,d]\!]$, forment un système complet, donc
$$\begin{aligned}
\mathbb P(S_2=k)&=\sum_{i=0}^d\mathbb P([U_1=i]\cap[U_2=k-i])\\
&=\sum_{i=0}^d\mathbb P(U_1=i)\,\mathbb P(U_2=k-i)
\end{aligned}$$
par indépendance de $U_1$ et $U_2$ (avec $\mathbb P(U_2=j)=0$ si $j\notin[\![0,d]\!]$).

> [!JURY]
> Le rapport 2026 : « Il faut citer l’indépendance! » et préciser les valeurs prises par l'indice $i$.

### Question 5.(c)

> [!INDICATION]
> Comptez les $i\in[\![0,d]\!]$ tels que $k-i\in[\![0,d]\!]$.

#### Solution

Chaque terme non nul vaut $\frac1{(d+1)^2}$ ; il est non nul si et seulement si $0\le i\le d$ et $0\le k-i\le d$, c'est-à-dire $\max(0,k-d)\le i\le\min(d,k)$.
- Si $0\le k<d$ : $i\in[\![0,k]\!]$, soit $k+1$ valeurs, et $\mathbb P(S_2=k)=\frac{k+1}{(d+1)^2}$.
- Si $d\le k\le2d$ : $i\in[\![k-d,d]\!]$, soit $2d-k+1$ valeurs, et $\mathbb P(S_2=k)=\frac{2d+1-k}{(d+1)^2}$.

### Question 5.(d)

> [!INDICATION]
> Sommez 5.(c) pour $k$ de $d$ à $2d$ ; changez d'indice $j=2d+1-k$.

#### Solution

$$\begin{aligned}
\mathbb P(S_2\ge d)&=\sum_{k=d}^{2d}\frac{2d+1-k}{(d+1)^2}=\frac1{(d+1)^2}\sum_{j=1}^{d+1}j\\
&=\frac{(d+1)(d+2)}{2(d+1)^2}=\boxed{\frac{d+2}{2(d+1)}}.
\end{aligned}$$

### Question 6.(a)

> [!INDICATION]
> Boucle `while` tant que la somme est strictement inférieure à $d$.

#### Solution

```python
def Atteinte(d):
    S = 0
    n = 0
    while S < d:
        S = S + rd.randint(0, d+1)    # lancer uniforme sur [[0, d]]
        n = n + 1
    return n
```

### Question 6.(b)

> [!INDICATION]
> Moyenne de $N$ simulations indépendantes de $T$.

#### Solution

```python
def EspT(d, N):
    E = 0
    for k in range(N):
        E = E + Atteinte(d)
    return 1/N*E
```
On utilise la **loi faible des grands nombres** : la moyenne empirique de $N$ simulations indépendantes de $T$ converge en probabilité vers $\mathbb E(T)$ (la loi faible des grands nombres du programme suppose que $T$ admette une variance ; l'énoncé ne l'établit pas à ce stade, on l'admet : elle découle de la formule de $\mathbb P(T\ge n)$ admise après 6.(c)).

Essais : $d=2$ donne $\approx2{,}26$ ($\frac94=2{,}25$), $d=5$ donne $\approx2{,}48$ ($\left(\frac65\right)^5\approx2{,}488$).

### Question 6.(c)

> [!INDICATION]
> Quelle grandeur varie en abscisse ? Vers quelle droite les points se rapprochent-ils ?

#### Solution

Les valeurs approchées de $\mathbb E(T)$ croissent avec $d$ et se rapprochent de la droite d'ordonnée $e\approx2{,}718$.

**On conjecture que $\mathbb E(T)$ tend vers $e$ quand $d$ tend vers $+\infty$** (en croissant).

> [!JURY]
> Le rapport 2026 : il faut préciser « quelle variable tendait vers quoi » ; écrire « $\mathbb E(T)$ converge vers $e$ » ne suffit pas.

### Question 7.(a)

> [!INDICATION]
> Écrivez $\mathbb P(V\ge n)=\sum_{i=n}^N\mathbb P(V=i)+\mathbb P(V\ge N+1)$ et intervertissez les sommes finies.

#### Solution

Soit $N\in\mathbb N^*$. Pour $1\le n\le N$, $\mathbb P(V\ge n)=\sum_{i=n}^N\mathbb P(V=i)+\mathbb P(V\ge N+1)$. En sommant :
$$\begin{aligned}
\sum_{n=1}^N\mathbb P(V\ge n)&=\sum_{n=1}^N\sum_{i=n}^N\mathbb P(V=i)+N\,\mathbb P(V\ge N+1)\\
&=\sum_{i=1}^N\sum_{n=1}^i\mathbb P(V=i)+N\,\mathbb P(V\ge N+1)\\
&=\sum_{i=1}^Ni\,\mathbb P(V=i)+N\,\mathbb P(V\ge N+1).
\end{aligned}$$

### Question 7.(b)

> [!INDICATION]
> Majorez les sommes partielles de $\sum i\,\mathbb P(V=i)$ (série à termes positifs).

#### Solution

D'après 7.(a), et $N\,\mathbb P(V\ge N+1)\ge0$ :
$$\begin{aligned}
0&\le\sum_{i=1}^Ni\,\mathbb P(V=i)\\
&\le\sum_{n=1}^N\mathbb P(V\ge n)\\
&\le\sum_{n=1}^{+\infty}\mathbb P(V\ge n).
\end{aligned}$$
Les sommes partielles de la série à termes positifs $\sum i\,\mathbb P(V=i)$ sont majorées : elle converge (absolument). Comme $V(\Omega)\subset\mathbb N$, **$V$ admet une espérance.**

### Question 7.(c)

> [!INDICATION]
> Écrivez $\mathbb P(V\ge N+1)$ comme une somme et comparez $N$ à $i$.

#### Solution

$$\begin{aligned}
0&\le N\,\mathbb P(V\ge N+1)\\
&=\sum_{i=N+1}^{+\infty}N\,\mathbb P(V=i)\\
&\le\sum_{i=N+1}^{+\infty}i\,\mathbb P(V=i).
\end{aligned}$$
Le majorant est le reste d'une série convergente (7.(b)) : il tend vers $0$. Par encadrement, $\displaystyle\lim_{N\to+\infty}N\,\mathbb P(V\ge N+1)=0$.

### Question 7.(d)

> [!INDICATION]
> Passage à la limite dans 7.(a) avec 7.(b) et 7.(c).

#### Solution

On fait tendre $N$ vers $+\infty$ dans 7.(a) : le membre de gauche tend vers $\sum_{n=1}^{+\infty}\mathbb P(V\ge n)$, et à droite $\sum_{i=1}^Ni\,\mathbb P(V=i)\to\mathbb E(V)$ et $N\,\mathbb P(V\ge N+1)\to0$. Donc $\boxed{\mathbb E(V)=\sum_{n=1}^{+\infty}\mathbb P(V\ge n)}$.

### Question 8.(a)

> [!INDICATION]
> Dérivez $(1-t)^{-m}$ : attention au signe.

#### Solution

$h(t)=r!\,(1-t)^{-(r+1)}$ avec $1-t\ge\frac12>0$ : $h$ est de classe $\mathcal C^\infty$ sur $\left[0,\frac12\right]$.

Par récurrence immédiate sur $k$ (chaque dérivation multiplie par l'exposant changé de signe, et la dérivée de $1-t$ vaut $-1$) :
$$\boxed{h^{(k)}(t)=\frac{(r+k)!}{(1-t)^{r+k+1}}}.$$
(Initialisation $k=0$ ; si $h^{(k)}(t)=(r+k)!(1-t)^{-(r+k+1)}$, alors $h^{(k+1)}(t)=(r+k)!(r+k+1)(1-t)^{-(r+k+2)}$.)

> [!JURY]
> Le rapport 2026 signale un facteur $(-1)^k$ erroné qui apparaît souvent : les deux signes moins se compensent à chaque dérivation.

### Question 8.(b)

> [!INDICATION]
> Pour $t\in[0,x]$, minorez $1-t$ par $\frac12$.

#### Solution

Soient $n\ge1$ et $x\in\left[0,\frac12\right]$. Pour $t\in[0,x]$, $1-t\ge\frac12$, donc $0\le\frac{(x-t)^{n-1}}{(1-t)^{r+n+1}}\le2^{r+n+1}(x-t)^{n-1}$. Par croissance de l'intégrale ($0\le x$) :
$$0\le\int_0^x\frac{(x-t)^{n-1}}{(1-t)^{r+n+1}}\,dt\le2^{r+n+1}\int_0^x(x-t)^{n-1}\,dt=2^{r+n+1}\frac{x^n}n.$$

### Question 8.(c)

> [!INDICATION]
> Formule de Taylor avec reste intégral à l'ordre $n-1$ en $0$ ; majorez le reste avec 8.(b).

> [!INDICATION]
> Le majorant est de la forme $C\,n^{r}(2x)^n$ avec $2x<1$ : croissances comparées.

#### Solution

Soit $x\in\left[0,\frac12\right[$ et $n\ge1$. Par la formule de Taylor avec reste intégral ($h$ de classe $\mathcal C^n$) :
$$h(x)=\sum_{k=0}^{n-1}\frac{h^{(k)}(0)}{k!}x^k+\int_0^x\frac{(x-t)^{n-1}}{(n-1)!}h^{(n)}(t)\,dt.$$
Par 8.(a), $\frac{h^{(k)}(0)}{k!}=\frac{(k+r)!}{k!}=(k+r)\cdots(k+1)$. Le reste $R_n$ vérifie, par 8.(b) :
$$\begin{aligned}
0&\le R_n\\
&=\frac{(r+n)!}{(n-1)!}\int_0^x\frac{(x-t)^{n-1}}{(1-t)^{r+n+1}}\,dt\\
&\le\frac{(r+n)!}{n!}2^{r+1}(2x)^n.
\end{aligned}$$
Or $\frac{(r+n)!}{n!}=(n+1)\cdots(n+r)\le(n+r)^r$ et $0\le2x<1$, donc par croissances comparées $(n+r)^r(2x)^n\to0$ : $R_n\to0$. Ainsi la série $\sum(n+r)\cdots(n+1)x^n$ converge et
$$\begin{aligned}
\sum_{n=0}^{+\infty}(n+r)\cdots(n+1)x^n&=h(x)\\
&=\frac{r!}{(1-x)^{r+1}}.
\end{aligned}$$

### Question 8.(d)

> [!INDICATION]
> Utilisez 7 avec $V=T$ : il suffit que $\sum\mathbb P(T\ge n)$ converge. Faites apparaître 8.(c) avec $r=d-1$ et $x=\frac1{d+1}$.

#### Solution

$T(\Omega)\subset\mathbb N^*$. Pour $n\ge1$, posons $m=n-1$ :
$$\begin{aligned}
\mathbb P(T\ge n)&=\frac{\binom{m+d-1}m}{(d+1)^m}\\
&=\frac{(m+d-1)\cdots(m+1)}{(d-1)!}\,x^m\\
x&=\frac1{d+1}.
\end{aligned}$$
Comme $d\ge2$, $x\le\frac13<\frac12$.

Par 8.(c) avec $r=d-1$, la série $\sum_m(m+r)\cdots(m+1)x^m$ converge et vaut $\frac{(d-1)!}{(1-x)^d}$.

Donc $\sum_{n\ge1}\mathbb P(T\ge n)$ converge et, par 7.(b) et 7.(d), $T$ admet une espérance :
$$\begin{aligned}
\mathbb E(T)&=\sum_{n=1}^{+\infty}\mathbb P(T\ge n)\\
&=\frac1{(d-1)!}\cdot\frac{(d-1)!}{(1-x)^d}\\
&=\left(\frac{d+1}d\right)^d.
\end{aligned}$$

### Question 8.(e)

> [!INDICATION]
> Forme exponentielle et $\ln(1+u)\sim u$.

#### Solution

$\mathbb E(T)=\exp\left(d\ln\left(1+\frac1d\right)\right)$ et $d\ln\left(1+\frac1d\right)\sim d\cdot\frac1d=1$. Par continuité de l'exponentielle, $\boxed{\lim_{d\to+\infty}\mathbb E(T)=e}$, ce qui confirme la conjecture de 6.(c).

## Problème — Partie III : version continue

Les lancers deviennent uniformes sur $[0,d]$ ; la densité de $S_n$ sur $[0,d]$ est $\frac{x^{n-1}}{(n-1)!\,d^n}$, et l'on retrouve exactement $\mathbb E(T)=e$.

### Question 9.(a)

> [!INDICATION]
> Question de cours sur la loi uniforme.

#### Solution

$S_1=U_1\hookrightarrow\mathcal U([0,d])$ : une densité est $f_1(x)=\frac1d$ si $x\in[0,d]$, $0$ sinon ; $\mathbb E(S_1)=\frac d2$, $\mathbb V(S_1)=\frac{d^2}{12}$.

### Question 9.(b)

> [!INDICATION]
> Densité de $S_2=U_1+U_2$ par produit de convolution ($f_1$ bornée, $U_1$, $U_2$ indépendantes).

#### Solution

$U_1$ et $U_2$ sont indépendantes et $f_1$ est bornée : une densité de $S_2$ est donnée par le produit de convolution $f_2(x)=\int_{-\infty}^{+\infty}f_1(t)f_1(x-t)\,dt$.

L'intégrande est non nul seulement si $t\in[0,d]$ et $x-t\in[0,d]$.
- Si $x<0$ : $x-t<0$ pour tout $t\ge0$, l'intégrande est nul.
- Si $x>2d$ : $x-t>d$ pour tout $t\le d$, l'intégrande est nul.
- Si $x=2d$ : l'intégrande n'est non nul qu'en $t=d$, l'intégrale est nulle.

Donc $f_2(x)=0$ pour $x\in]-\infty,0[\cup[2d,+\infty[$.

### Question 9.(c)

> [!INDICATION]
> Déterminez l'ensemble des $t$ pour lesquels $f_1(t)f_1(x-t)\neq0$.

#### Solution

Soit $x\in[0,d]$.

$t\in[0,d]$ et $x-t\in[0,d]$ équivaut à $t\in[0,x]$ (car $x\le d$).

Sur cet intervalle l'intégrande vaut $\frac1{d^2}$ : $f_2(x)=\int_0^x\frac1{d^2}\,dt$ $\left(=\frac x{d^2}\right)$.

> [!JURY]
> Le rapport 2026 : « Le produit de convolution ne semble pas maîtrisé », et l'indépendance est rarement évoquée.

### Question 9.(d)

> [!INDICATION]
> Il reste le cas $x\in[d,2d[$.

#### Solution

Pour $x\in[d,2d[$, la condition équivaut à $t\in[x-d,d]$, d'où $f_2(x)=\frac{2d-x}{d^2}$. Finalement
$$\boxed{f_2(x)=\begin{cases}\dfrac x{d^2}&\text{si }0\le x\le d\\[4pt]\dfrac{2d-x}{d^2}&\text{si }d\le x<2d\\[4pt]0&\text{sinon}\end{cases}}$$
(loi « triangulaire » ; les deux expressions coïncident en $d$).

### Question 10.(a)

> [!INDICATION]
> $S_{n+1}=S_n+U_{n+1}$ avec $S_n$ et $U_{n+1}$ indépendantes (lemme des coalitions).

#### Solution

Par le lemme des coalitions, $S_n$ et $U_{n+1}$ sont indépendantes ;

$f_1$ est bornée, donc une densité de $S_{n+1}$ est $f_{n+1}(x)=\int_{-\infty}^{+\infty}f_n(t)f_1(x-t)\,dt$.

Si $x<0$, $f_1(x-t)\neq0$ impose $t\le x<0$, où $f_n(t)=0$ : **$f_{n+1}(x)=0$.**

### Question 10.(b)

> [!INDICATION]
> Pour $x\in[0,d]$, $f_1(x-t)\neq0$ impose $t\in[x-d,x]$ ; seule la partie $t\in[0,x]$ compte.

#### Solution

Soit $x\in[0,d]$.

$f_1(x-t)=\frac1d$ si $t\in[x-d,x]$, $0$ sinon.

Sur $[x-d,0[$, $f_n(t)=0$ ; sur $[0,x]\subset[0,d]$, l'hypothèse donne $f_n(t)=\frac{t^{n-1}}{(n-1)!\,d^n}$.

Donc
$$\begin{aligned}
f_{n+1}(x)&=\int_0^x\frac{t^{n-1}}{(n-1)!\,d^n}\cdot\frac1d\,dt\\
&=\frac{x^n}{n\cdot(n-1)!\,d^{n+1}}\\
&=\frac{x^n}{n!\,d^{n+1}}.
\end{aligned}$$

> [!JURY]
> Le rapport 2026 : « Bien trop de copies pensent que l’hypothèse est faite pour tout entier n » : l'hypothèse porte sur un $n$ fixé, et l'on n'utilise $f_n$ que sur $]-\infty,d]$.

### Question 11

> [!INDICATION]
> Récurrence avec 9.(a) et 10 pour obtenir $f_n$ sur $[0,d]$, puis intégrez.

#### Solution

Par récurrence, la propriété « $f_n=0$ sur $]-\infty,0[$ et $f_n(x)=\frac{x^{n-1}}{(n-1)!\,d^n}$ sur $[0,d]$ » est vraie pour tout $n\ge1$ : pour $n=1$ c'est 9.(a), l'hérédité est la question 10. Alors
$$\begin{aligned}
\mathbb P(S_n<d)&=\int_0^d\frac{x^{n-1}}{(n-1)!\,d^n}\,dx\\
&=\frac{d^n}{n\,(n-1)!\,d^n}\\
&=\boxed{\frac1{n!}}.
\end{aligned}$$

### Question 12.(a)

> [!INDICATION]
> $U_1$ prend ses valeurs dans $[0,d]$.

#### Solution

$[T=1]=[S_1\ge d]=[U_1\ge d]=[U_1=d]$ (car $U_1\le d$), de probabilité nulle ($U_1$ à densité) : $\boxed{\mathbb P(T=1)=0}$.

### Question 12.(b)

> [!INDICATION]
> La suite $(S_k)$ est croissante.

#### Solution

Les $U_i$ sont positives, donc $(S_k)$ est croissante.

$[T>n]$ signifie que $S_k<d$ pour tout $k\le n$, ce qui équivaut à $S_n<d$ (puisque $S_k\le S_n$).

$\boxed{[T>n]=[S_n<d]}$.

### Question 12.(c)

> [!INDICATION]
> Utilisez la question 7 avec $V=T$ et $\mathbb P(T\ge n)=\mathbb P(T>n-1)$.

#### Solution

Par 12.(b) et 11, $\mathbb P(T>n)=\frac1{n!}\to0$, donc $T$ est presque sûrement fini et $T(\Omega)\subset\mathbb N^*$ (quitte à négliger un événement de probabilité nulle).

Pour $n\ge2$, $\mathbb P(T\ge n)=\mathbb P(T>n-1)=\frac1{(n-1)!}$, et $\mathbb P(T\ge1)=1=\frac1{0!}$.

La série $\sum_{n\ge1}\frac1{(n-1)!}$ converge (série exponentielle).

Par 7.(b) et 7.(d), $T$ admet une espérance et
$$\begin{aligned}
\mathbb E(T)&=\sum_{n=1}^{+\infty}\frac1{(n-1)!}\\
&=\sum_{m=0}^{+\infty}\frac1{m!}\\
&=\boxed{e}.
\end{aligned}$$
C'est la limite obtenue en 8.(e) pour la version discrète.

## Bilan

**Méthodes à retenir.**
- Intégrales impropres : traiter chaque borne ; fausse impropreté par prolongement ; convergence absolue quand l'intégrande change de signe ; divergence par minoration positive (ne pas conclure d'un critère qui « échoue »).
- Intégrale de Frullani : écrire la différence d'intégrales **convergentes**, changement de variable affine, Chasles.
- Changement de variable dans une intégrale impropre : classe $\mathcal C^1$, stricte monotonie, intervalles exacts.
- Sommes de Riemann ($O(\frac1n)$ pour une fonction monotone) contre Monte-Carlo ($O(\frac1{\sqrt n})$).
- Endomorphisme de $\mathbb R_n[x]$ triangulaire dans la base canonique : valeurs propres sur la diagonale ; $n+1$ valeurs propres distinctes en dimension $n+1$ ⇒ diagonalisable, droites propres.
- Endomorphisme symétrique : par intégration par parties ; vecteurs propres de valeurs propres distinctes orthogonaux ; polynômes orthogonaux et relation à trois termes (parité pour annuler $\beta_k$).
- Espérance totale avec réinitialisation du processus ; $\mathbb E(V)=\sum\mathbb P(V\ge n)$ ; série $\sum(n+r)\cdots(n+1)x^n$ par Taylor avec reste intégral.
- Densité d'une somme de variables uniformes par convolution, récurrence ; $\mathbb P(S_n<d)=\frac1{n!}$ et $\mathbb E(T)=e$.

**À revoir si besoin.** Produit scalaire (caractère défini avec continuité) ; formule de Taylor avec reste intégral ; convolution discrète et continue (indépendance à citer) ; boucles `while` et récurrences en Python.

**Questions transposables.** Intégrales de Frullani ; polynômes de Gegenbauer ou de Legendre ; temps d'attente d'un motif (« $r$ piles consécutifs ») ; nombre de variables uniformes à sommer pour dépasser $1$ (espérance $e$).
