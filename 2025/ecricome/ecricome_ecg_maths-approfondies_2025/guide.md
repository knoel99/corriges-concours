# ECRICOME ECG — Mathématiques approfondies 2025 · Corrigé guidé

*Corrigé rédigé par IA, non officiel. Signalez toute erreur.*

## Présentation du sujet

**Format.** Épreuve de 4 heures, sans document ni calculatrice. Deux exercices et un problème indépendants, 72 questions en comptant les sous-questions.

**Découpage.**

| Partie | Thème | Notions du programme ECG approfondies |
|---|---|---|
| Exercice 1 | $\sum\frac1{n^2}=\frac{\pi^2}6$ par une méthode de type Riemann-Lebesgue | séries de Riemann, convergence absolue, trigonométrie, récurrence, intégration par parties, fonctions de classe $\mathcal C^1$, théorème du prolongement de la dérivée |
| Exercice 2, partie 1 | Matrice $M$ non diagonalisable | dimension de $\mathcal M_3(\mathbb R)$, polynôme annulateur, inverse, étude de fonction, Python |
| Exercice 2, parties 2–3 | Décomposition polaire $M=UR$ | matrice symétrique, théorème spectral, matrices orthogonales, racine carrée symétrique positive, unicité |
| Problème, partie 1 | Fonction bêta $B(x,y)$ | intégrales impropres, équivalents, changement de variable, intégration par parties, récurrence |
| Problème, partie 2 | Fonction $\Gamma$ et lois $\gamma$ | densités, moments, transformation affine, produit de convolution, $B=\frac{\Gamma\Gamma}{\Gamma}$ |
| Problème, partie 3 | Méthodes de Monte-Carlo | loi faible des grands nombres, estimateur sans biais et convergent, simulation |

**Difficulté.** Sujet long et dense. Les points délicats : 1.4.(b)–(c) (encadrement), 1.5.(c) (prolongement $\mathcal C^1$), 1.7.(a) (synthèse), 2.3.(b), 2.10, 2.14–2.16 (unicité de la décomposition polaire), pb 1.(d) et 4.(b) (intégrales doublement impropres), 10.(a) (convolution). La moyenne est de 11,2 sur 20, avec un écart-type de 5,6 (rapport 2025). L'énoncé admet en 11.(a) que $U^{x-1}(1-U)^{y-1}$ a une variance pour tous $x,y>0$ : c'est faux si $x\le\frac12$ ou $y\le\frac12$ (voir la question 11.(c)).

**Gestion du temps.** Environ 1 h pour l'exercice 1, 1 h 15 pour l'exercice 2, 1 h 45 pour le problème. Les questions de Python (2.2.(a), pb 11.(b), (d), 12.(c), (d)) sont rapides : ne pas les laisser.

## Exercice 1 — Calcul de la somme des 1/n²

On relie $A=\sum\frac1{n^2}$, $B=\sum\frac{(-1)^n}{n^2}$ et $C=\sum\frac1{(2n+1)^2}$, puis on calcule $C$ en intégrant contre $\pi-t$ une somme trigonométrique, le reste tendant vers $0$ grâce à un lemme de type Riemann-Lebesgue.

### Question 1.(a)

> [!INDICATION]
> Série de Riemann : quel est le critère exact ?

#### Solution

$\sum_{n\ge1}\frac1{n^2}$ est une série de Riemann de paramètre $2>1$ : **elle converge.**

### Question 1.(b)

> [!INDICATION]
> Étudiez la convergence absolue.

#### Solution

$\left|\frac{(-1)^n}{n^2}\right|=\frac1{n^2}$ et $\sum\frac1{n^2}$ converge (1.(a)) : la série $\sum\frac{(-1)^n}{n^2}$ est absolument convergente, donc **convergente**.

> [!JURY]
> Le rapport 2025 : « Rappelons que le critère des séries alternées est hors programme, il ne doit donc pas être utilisé ici. »

### Question 1.(c)

> [!INDICATION]
> Comparez $\frac1{(2n+1)^2}$ à $\frac1{n^2}$ pour $n\ge1$ (séries à termes positifs).

#### Solution

Pour $n\ge1$, $(2n+1)^2\ge4n^2$, donc $0<\frac1{(2n+1)^2}\le\frac1{4n^2}$. Par comparaison de séries à termes positifs et 1.(a), $\sum_{n\ge1}\frac1{(2n+1)^2}$ converge, donc aussi $\sum_{n\ge0}\frac1{(2n+1)^2}$ (ajout du terme $n=0$).

> [!PIEGE]
> $\frac1{(2n+1)^2}\sim\frac1{4n^2}$, et non $\frac1{2n^2}$ ou $\frac1{n^2}$. Et le « changement d'indice $k=2n+1$ » n'est pas licite : il ne parcourt que les impairs.

### Question 2

> [!INDICATION]
> Travaillez sur les sommes partielles d'indice $2N+1$ et séparez indices pairs et impairs.

#### Solution

Soit $N\in\mathbb N$. En séparant les indices pairs $n=2p$ ($1\le p\le N$) et impairs $n=2p+1$ ($0\le p\le N$) :
$$\begin{aligned}
\sum_{n=1}^{2N+1}\frac{1-(-1)^n}{n^2}&=\sum_{p=0}^N\frac2{(2p+1)^2}\\
\sum_{n=1}^{2N+1}\frac1{n^2}&=\sum_{p=0}^N\frac1{(2p+1)^2}+\frac14\sum_{p=1}^N\frac1{p^2}.
\end{aligned}$$
Les quatre sommes partielles convergent (question 1) ; en faisant tendre $N$ vers $+\infty$ :
$$\begin{aligned}
\boxed{A-B=2C}\\
\text{et}\\
\boxed{A=C+\tfrac14A}.
\end{aligned}$$

> [!JURY]
> Le rapport 2025 signale que la seconde égalité est souvent oubliée ou manquée, et que des changements d'indice comme $j=2n+1$ ne sont pas licites.

### Question 3.(a)

> [!INDICATION]
> Formules d'addition du cosinus.

#### Solution

$\cos(\alpha+\beta)=\cos\alpha\cos\beta-\sin\alpha\sin\beta$ et $\cos(\alpha-\beta)=\cos\alpha\cos\beta+\sin\alpha\sin\beta$. En additionnant : $\cos(\alpha+\beta)+\cos(\alpha-\beta)=2\cos\alpha\cos\beta$.

### Question 3.(b)

> [!INDICATION]
> Pour $t\in[0,\pi[$, $\cos\frac t2>0$. Multipliez les égalités par $2\cos\frac t2$ et utilisez 3.(a).

#### Solution

Soit $t\in[0,\pi[$ : $\frac t2\in\left[0,\frac\pi2\right[$, donc $c=\cos\frac t2>0$. Montrons par récurrence sur $n\ge1$ :
$$\begin{aligned}
\mathcal P(n):\\
\sum_{k=1}^n(-1)^k\cos(kt)&=-\frac12+(-1)^n\frac{\cos\left(\frac{2n+1}2t\right)}{2c}.
\end{aligned}$$
*Initialisation.* Par 3.(a), $2\cos t\cos\frac t2=\cos\frac{3t}2+\cos\frac t2$, donc
$$-\cos t=-\frac{\cos\frac{3t}2+\cos\frac t2}{2c}=-\frac12-\frac{\cos\frac{3t}2}{2c}.$$
C'est $\mathcal P(1)$.

*Hérédité.* Supposons $\mathcal P(n)$. Par 3.(a), $2\cos((n+1)t)\cos\frac t2=\cos\frac{(2n+3)t}2+\cos\frac{(2n+1)t}2$. Donc
$$\begin{aligned}
\sum_{k=1}^{n+1}(-1)^k\cos(kt)&=-\frac12+(-1)^n\frac{\cos\frac{(2n+1)t}2}{2c}+(-1)^{n+1}\cos((n+1)t)\\
&=-\frac12+(-1)^{n+1}\frac{-\cos\frac{(2n+1)t}2+2c\cos((n+1)t)}{2c}\\
&=-\frac12+(-1)^{n+1}\frac{\cos\frac{(2n+3)t}2}{2c}.
\end{aligned}$$
C'est $\mathcal P(n+1)$, ce qui conclut la récurrence.

### Question 4.(a)

> [!INDICATION]
> Une fonction continue sur un segment est bornée.

#### Solution

$f$ et $f'$ sont continues sur le segment $[a,b]$, donc bornées : il existe $M_1$, $M_2$ tels que $|f|\le M_1$ et $|f'|\le M_2$ sur $[a,b]$.

**$M=\max(M_1,M_2)$ convient.**

### Question 4.(b)

> [!INDICATION]
> Majorez la valeur absolue de l'intégrale, puis concluez par encadrement de la valeur absolue.

#### Solution

Pour $\lambda>0$, par l'inégalité triangulaire intégrale ($a<b$) :
$$\begin{aligned}
0&\le\left|\frac1\lambda\int_a^bf'(t)\sin(\lambda t)\,dt\right|\\
&\le\frac1\lambda\int_a^b|f'(t)|\,|\sin(\lambda t)|\,dt\\
&\le\frac{M(b-a)}\lambda.
\end{aligned}$$
Le majorant tend vers $0$ quand $\lambda\to+\infty$ ; par encadrement, $\displaystyle\lim_{\lambda\to+\infty}\frac1\lambda\int_a^bf'(t)\sin(\lambda t)\,dt=0$.

> [!JURY]
> Le rapport 2025 : « certains candidats concluent par encadrement alors qu’ils n’ont donné qu’une majoration: une minoration est indispensable. » Ici la minoration est $0\le|\cdot|$.

### Question 4.(c)

> [!INDICATION]
> Intégrez $\cos(\lambda t)$ et dérivez $f$.

#### Solution

Soit $\lambda>0$. $f$ et $t\mapsto\frac{\sin(\lambda t)}\lambda$ sont de classe $\mathcal C^1$ sur $[a,b]$ ; par intégration par parties :
$$\int_a^bf(t)\cos(\lambda t)\,dt=\frac{f(b)\sin(\lambda b)-f(a)\sin(\lambda a)}{\lambda}-\frac1\lambda\int_a^bf'(t)\sin(\lambda t)\,dt.$$
Le premier terme est majoré en valeur absolue par $\frac{2M}\lambda\to0$ ; le second tend vers $0$ (4.(b)). Donc $\displaystyle\lim_{\lambda\to+\infty}\int_a^bf(t)\cos(\lambda t)\,dt=0$.

> [!PIEGE]
> $f(a)\sin(\lambda a)$ dépend de $\lambda$ : il faut le borner ($|\sin|\le1$) avant de conclure.

### Question 5.(a)

> [!INDICATION]
> Quotient de fonctions de classe $\mathcal C^1$ : vérifiez que le dénominateur ne s'annule pas sur $]0,\pi]$.

#### Solution

Pour $t\in]0,\pi]$, $\frac t2\in]0,\frac\pi2]$ donc $\sin\frac t2>0$.

$t\mapsto t$ et $t\mapsto\sin\frac t2$ sont de classe $\mathcal C^1$ et le dénominateur ne s'annule pas : $\varphi$ est de classe $\mathcal C^1$ sur $]0,\pi]$, et
$$\varphi'(t)=\frac{\sin\frac t2-\frac t2\cos\frac t2}{\sin^2\frac t2}.$$

### Question 5.(b)

> [!INDICATION]
> Équivalent usuel de $\sin u$ en $0$.

#### Solution

$\sin u\underset{u\to0}{\sim}u$, donc $\sin\frac t2\underset{t\to0}{\sim}\frac t2$ et $\varphi(t)\to2$. **$\varphi$ se prolonge par continuité en $0$ en posant $\varphi(0)=2$.**

### Question 5.(c)

> [!INDICATION]
> Théorème du prolongement de la dérivée : il suffit que $\varphi$ soit continue sur $[0,\pi]$, de classe $\mathcal C^1$ sur $]0,\pi]$, et que $\varphi'$ ait une limite finie en $0$.

> [!INDICATION]
> Pour la limite de $\varphi'$, posez $u=\frac t2$ et faites un développement limité du numérateur à l'ordre $3$.

#### Solution

$\varphi$ est continue sur $[0,\pi]$ (5.(b)) et de classe $\mathcal C^1$ sur $]0,\pi]$ (5.(a)). Avec $u=\frac t2\to0$ :
$$\sin u-u\cos u=\left(u-\frac{u^3}6\right)-u\left(1-\frac{u^2}2\right)+o(u^3)=\frac{u^3}3+o(u^3),$$
et $\sin^2u\sim u^2$. Donc $\varphi'(t)\sim\frac u3\to0$. Par le théorème du prolongement de la dérivée, **$\varphi$ est de classe $\mathcal C^1$ sur $[0,\pi]$**, avec $\varphi'(0)=0$.

> [!JURY]
> Le rapport 2025 : le théorème de prolongement des fonctions de classe $\mathcal C^1$ est peu connu, et beaucoup cherchent la limite de $\varphi'$ sans savoir quel théorème l'exploite.

### Question 5.(d)

> [!INDICATION]
> $f(t)=\varphi(\pi-t)$ : composez $\varphi$ avec une fonction affine qui envoie $[0,\pi]$ dans $[0,\pi]$.

#### Solution

Posons $f(\pi)=\varphi(0)=2$.

Alors $f(t)=\varphi(\pi-t)$ pour tout $t\in[0,\pi]$.

La fonction $t\mapsto\pi-t$ est de classe $\mathcal C^1$ sur $[0,\pi]$ à valeurs dans $[0,\pi]$, et $\varphi$ est de classe $\mathcal C^1$ sur $[0,\pi]$ (5.(c)).

Par composition, **$f$ ainsi prolongée est de classe $\mathcal C^1$ sur $[0,\pi]$**.

> [!PIEGE]
> Dire seulement « $\pi-t\in[0,\pi]$ » ne suffit pas : il faut invoquer la composée de deux fonctions de classe $\mathcal C^1$.

### Question 6.(a)

> [!INDICATION]
> Intégration par parties : dérivez $\pi-t$, intégrez $\cos(kt)$.

#### Solution

Soit $k\in\mathbb N^*$. Par intégration par parties (fonctions de classe $\mathcal C^1$ sur $[0,\pi]$) :
$$\begin{aligned}
\int_0^\pi(\pi-t)\cos(kt)\,dt&=\left[(\pi-t)\frac{\sin(kt)}k\right]_0^\pi+\frac1k\int_0^\pi\sin(kt)\,dt\\
&=0+\frac1k\left[-\frac{\cos(kt)}k\right]_0^\pi=\frac{1-(-1)^k}{k^2}.
\end{aligned}$$
Cette quantité vaut **$0$ si $k$ est pair et $\frac2{k^2}$ si $k$ est impair.**

### Question 6.(b)

> [!INDICATION]
> Linéarité de l'intégrale, puis ne gardez que les $k$ impairs $k=2n+1$.

#### Solution

Par linéarité et 6.(a), seuls les $k$ impairs, $k=2n+1$ avec $0\le n\le N$, contribuent, avec $(-1)^k=-1$ :
$$\begin{aligned}
\int_0^\pi\sum_{k=1}^{2N+1}(-1)^k(\pi-t)\cos(kt)\,dt&=\sum_{n=0}^N(-1)\cdot\frac2{(2n+1)^2}\\
&=-2\sum_{n=0}^N\frac1{(2n+1)^2}.
\end{aligned}$$

### Question 7.(a)

> [!INDICATION]
> Remplacez la somme trigonométrique par l'expression de 3.(b) avec $n=2N+1$ : faites apparaître la fonction $f$ de 5.(d).

> [!INDICATION]
> Le terme qui reste tend vers $0$ par 4.(c).

#### Solution

Soit $N\in\mathbb N$. Par 3.(b) avec $n=2N+1$ (impair), pour $t\in[0,\pi[$ :
$$\begin{aligned}
(\pi-t)\sum_{k=1}^{2N+1}(-1)^k\cos(kt)&=-\frac{\pi-t}2-\frac12f(t)\cos(\lambda_Nt)\\
\lambda_N&=\frac{4N+3}2.
\end{aligned}$$
Les deux membres sont continus sur $[0,\pi]$ (avec $f$ prolongée), ils sont égaux sur $[0,\pi[$ donc aussi en $\pi$ par continuité. En intégrant sur $[0,\pi]$, avec $\int_0^\pi(\pi-t)\,dt=\frac{\pi^2}2$ et 6.(b) :
$$-2\sum_{n=0}^N\frac1{(2n+1)^2}=-\frac{\pi^2}4-\frac12\int_0^\pi f(t)\cos(\lambda_Nt)\,dt.$$
$f$ est de classe $\mathcal C^1$ sur $[0,\pi]$ (5.(d)) et $\lambda_N\to+\infty$ : par 4.(c), la dernière intégrale tend vers $0$. Donc $2C=\frac{\pi^2}4$ :
$$\boxed{C=\sum_{n=0}^{+\infty}\frac1{(2n+1)^2}=\frac{\pi^2}8}.$$

### Question 7.(b)

> [!INDICATION]
> Utilisez les deux relations de la question 2.

#### Solution

D'après 2, $\frac34A=C$, donc $A=\frac43\cdot\frac{\pi^2}8$, puis $B=A-2C$ :
$$\begin{aligned}
\boxed{A=\frac{\pi^2}6}\\
\boxed{B=\frac{\pi^2}6-\frac{\pi^2}4=-\frac{\pi^2}{12}}.
\end{aligned}$$

## Exercice 2 — Partie 1 : une matrice non diagonalisable

Un argument de dimension donne un polynôme annulateur ; on utilise ensuite celui fourni par l'énoncé pour inverser $M$ et localiser ses valeurs propres.

### Question 1.(a)

> [!INDICATION]
> Comparez le nombre d'éléments à la dimension de $\mathcal M_3(\mathbb R)$.

#### Solution

$\mathcal M_3(\mathbb R)$ est de dimension $9$. La famille $(I_3,M,\dots,M^9)$ en compte $10$ éléments, plus que la dimension : **elle est liée.**

### Question 1.(b)

> [!INDICATION]
> Traduisez « liée » par une combinaison linéaire nulle à coefficients non tous nuls.

#### Solution

Il existe des réels $a_0,\dots,a_9$ **non tous nuls** tels que $\sum_{k=0}^9a_kM^k=0_3$. Le polynôme $Q(X)=\sum_{k=0}^9a_kX^k$ est non nul, de degré au plus $9$, et $Q(M)=0_3$ : c'est un polynôme annulateur non nul de $M$.

### Question 2.(a)

> [!INDICATION]
> Puissances matricielles avec `np.dot`, puis test d'égalité de **tous** les coefficients.

#### Solution

```python
import numpy as np

def PolyAnn(M):
    M2 = np.dot(M, M)
    M3 = np.dot(M2, M)
    R = M3 - 4*M2 - 12*M - 28*np.eye(3)
    return np.all(R == 0)
```
`R == 0` est un tableau de booléens ; `np.all` renvoie `True` si et seulement si tous les coefficients sont nuls. Essai : `True` pour $M$, `False` pour $I_3$.

> [!JURY]
> Le rapport 2025 : « Le test d’égalité est presque toujours faux », car `A==0` renvoie un tableau ; et `np.dot` ou `matrix_power` sont mal connus.

### Question 2.(b)

> [!INDICATION]
> Isolez $28I_3$ dans $\varphi(M)=0_3$ et factorisez par $M$.

#### Solution

$\varphi(M)=0_3$ s'écrit $M^3-4M^2-12M=28I_3$, soit
$$M\cdot\frac1{28}\left(M^2-4M-12I_3\right)=I_3.$$
**$M$ est inversible et $M^{-1}=\frac1{28}\left(M^2-4M-12I_3\right)$.**

### Question 3.(a)

> [!INDICATION]
> Partez d'un vecteur propre $X\neq0$ et calculez $\varphi(M)X$.

#### Solution

Soit $\lambda$ une valeur propre et $X\neq0$ tel que $MX=\lambda X$. Par récurrence, $M^kX=\lambda^kX$ pour tout $k\in\mathbb N$. Donc
$$\begin{aligned}
0&=\varphi(M)X\\
&=\left(\lambda^3-4\lambda^2-12\lambda-28\right)X\\
&=\varphi(\lambda)X.
\end{aligned}$$
Comme $X\neq0$, $\varphi(\lambda)=0$.

> [!JURY]
> Le rapport 2025 : « on demandait au candidat de démontrer le résultat » ; citer le cours ne suffisait pas.

### Question 3.(b)

> [!INDICATION]
> Étudiez les variations de $\varphi$ : racines de $\varphi'$, valeur du maximum local.

> [!INDICATION]
> Sur l'intervalle où $\varphi$ est strictement croissante, appliquez le théorème de la bijection, puis situez la racine par rapport à $4$.

#### Solution

$\varphi'(x)=3x^2-8x-12$, de discriminant $64+144=208=16\times13$ ; ses racines sont $x_1=\frac{4-2\sqrt{13}}3$ et $x_2=\frac{4+2\sqrt{13}}3$.

Comme $3<\sqrt{13}<4$, $x_1<0$ et $x_2<4$.

$\varphi$ est croissante sur $]-\infty,x_1]$, décroissante sur $[x_1,x_2]$, strictement croissante sur $[x_2,+\infty[$.
- Sur $]-\infty,x_2]$, $\varphi\le\varphi(x_1)<0$ (valeur admise) : pas de racine.
- Sur $[x_2,+\infty[$, $\varphi$ est continue et strictement croissante, $\varphi(x_2)<0$ et $\varphi\to+\infty$ : par le théorème de la bijection, $\varphi$ s'annule une seule fois, en un réel $\alpha$. Comme $\varphi(4)=64-64-48-28=-76<0$ et que $4\in[x_2,+\infty[$, la stricte croissance donne $\alpha>4$.

$\varphi$ a donc une seule racine réelle, $\alpha>4$. Par 3.(a), **$M$ admet au plus une valeur propre réelle, et elle est strictement supérieure à $4$.**

### Question 3.(c)

> [!INDICATION]
> Si $M$ était diagonalisable, à quelle matrice diagonale serait-elle semblable ?

#### Solution

Supposons $M$ diagonalisable : $M=QDQ^{-1}$ avec $D$ diagonale réelle dont les coefficients sont des valeurs propres de $M$, donc tous égaux à $\alpha$ (3.(b)).

Alors $D=\alpha I_3$ et $M=Q(\alpha I_3)Q^{-1}=\alpha I_3$, ce qui est faux (par exemple $m_{1,1}=0\ne m_{2,2}=2$).

**$M$ n'est pas diagonalisable.**

> [!JURY]
> Le rapport 2025 souhaite l'étape intermédiaire $M=Q(\alpha I_3)Q^{-1}=\alpha I_3$, souvent omise.

## Exercice 2 — Partie 2 : la matrice S = ᵗMM et sa racine carrée

$S={}^tMM$ est symétrique à valeurs propres strictement positives ; on construit $R$ symétrique avec $R^2=S$, puis $U=MR^{-1}$ orthogonale : c'est la décomposition polaire $M=UR$.

### Question 4

> [!INDICATION]
> Transposée d'un produit.

#### Solution

${}^tS={}^tM\,{}^t({}^tM)={}^tMM=S$ : **$S$ est symétrique.**

### Question 5

> [!INDICATION]
> Pour $SX=\lambda X$ avec $X\neq0$, calculez ${}^tXSX$ de deux façons.

#### Solution

Soit $\lambda$ une valeur propre de $S$ et $X\neq0$ tel que $SX=\lambda X$.

D'une part ${}^tXSX=\lambda\,{}^tXX=\lambda\|X\|^2$.

D'autre part ${}^tXSX={}^t(MX)(MX)=\|MX\|^2$.

Comme $M$ est inversible (2.(b)) et $X\neq0$, $MX\neq0$, donc $\|MX\|^2>0$ ; et $\|X\|^2>0$.

Ainsi $\lambda=\frac{\|MX\|^2}{\|X\|^2}>0$.

> [!PIEGE]
> Une matrice symétrique quelconque peut avoir des valeurs propres négatives : c'est la forme ${}^tMM$ avec $M$ inversible qui donne la stricte positivité.

### Question 6

> [!INDICATION]
> Théorème spectral.

#### Solution

$S$ est symétrique réelle (question 4). Par le théorème spectral, **il existe $P$ orthogonale et $D$ diagonale telles que $S=PD\,{}^tP$.**

### Question 7.(a)

> [!INDICATION]
> Une matrice diagonale $\Delta$ vérifie $\Delta^2=D$ si et seulement si chacun de ses coefficients diagonaux a pour carré le coefficient correspondant de $D$.

#### Solution

$\Delta=\operatorname{diag}(\delta_1,\delta_2,\delta_3)$ vérifie $\Delta^2=D$ si et seulement si $\delta_1^2=1$, $\delta_2^2=16$, $\delta_3^2=49$, soit $\delta_1=\pm1$, $\delta_2=\pm4$, $\delta_3=\pm7$.

**Il y a $2^3=8$ telles matrices.**

> [!JURY]
> Le rapport 2025 : « La bonne réponse n’est malheureusement pas la plus fréquente. »

### Question 7.(b)

> [!INDICATION]
> Quand une matrice diagonale est-elle inversible ?

#### Solution

$\Delta$ est diagonale et ses coefficients diagonaux $\delta_i$ sont non nuls ($\delta_i^2=d_i>0$) : **$\Delta$ est inversible**, d'inverse $\operatorname{diag}\left(\frac1{\delta_1},\frac1{\delta_2},\frac1{\delta_3}\right)$.

> [!PIEGE]
> « Diagonale donc inversible » est faux : il faut des coefficients diagonaux non nuls.

### Question 8

> [!INDICATION]
> Essayez $R=P\Delta\,{}^tP$ ; vérifiez **les deux** propriétés.

#### Solution

Posons $R=P\Delta\,{}^tP$. ${}^tR=P\,{}^t\Delta\,{}^tP=P\Delta\,{}^tP=R$ : $R$ est symétrique réelle. Et, comme ${}^tPP=I_3$,
$$\begin{aligned}
R^2&=P\Delta\,{}^tPP\Delta\,{}^tP\\
&=P\Delta^2\,{}^tP\\
&=PD\,{}^tP\\
&=S.
\end{aligned}$$

> [!JURY]
> Le rapport 2025 : beaucoup posent la bonne matrice et vérifient $R^2=S$, mais « trop peu pensent à vérifier que R est bien symétrique ».

### Question 9

> [!INDICATION]
> Inverse d'un produit : $(ABC)^{-1}=C^{-1}B^{-1}A^{-1}$ ; et ${}^tP=P^{-1}$.

#### Solution

$R=P\Delta\,{}^tP$ est un produit de matrices inversibles ($P$ et ${}^tP=P^{-1}$ orthogonales, $\Delta$ par 7.(b)) : **$R$ est inversible** et
$$R^{-1}=({}^tP)^{-1}\Delta^{-1}P^{-1}=\boxed{P\Delta^{-1}\,{}^tP}.$$

### Question 10

> [!INDICATION]
> Calculez ${}^tUU$ ; que vaut ${}^t(R^{-1})$ ?

#### Solution

$R$ étant symétrique, ${}^t(R^{-1})=({}^tR)^{-1}=R^{-1}$. Alors
$$\begin{aligned}
{}^tUU&={}^t(R^{-1})\,{}^tMM\,R^{-1}\\
&=R^{-1}SR^{-1}=R^{-1}R^2R^{-1}\\
&=I_3.
\end{aligned}$$
**$U$ est orthogonale.**

## Exercice 2 — Partie 3 : unicité de la décomposition polaire

On montre que si $M=VT$ avec $V$ orthogonale et $T$ symétrique à valeurs propres strictement positives, alors $T=R$ et $V=U$.

L'argument clé : $T$ commute avec $S$, donc laisse stables ses droites propres.

### Question 11

> [!INDICATION]
> $R$ est semblable à une matrice diagonale connue.

#### Solution

$R=P\Delta\,{}^tP=P\Delta P^{-1}$ est semblable à $\Delta=\operatorname{diag}(1,4,7)$ : ses valeurs propres sont $1$, $4$ et $7$, **strictement positives.**

### Question 12

> [!INDICATION]
> Transposez $M=VT$ ; puis développez $N^2$.

#### Solution

$S={}^tMM={}^tT\,{}^tVVT=T\cdot I_3\cdot T=T^2$ car ${}^tT=T$ et ${}^tVV=I_3$. Puis, comme $P\,{}^tP=I_3$ et ${}^tPSP=D$ (question 6) :
$$\begin{aligned}
N^2&={}^tPTP\,{}^tPTP\\
&={}^tPT^2P\\
&={}^tPSP\\
&=D.
\end{aligned}$$

### Question 13

> [!INDICATION]
> Utilisez $S=T^2$.

#### Solution

$TS=T\cdot T^2=T^3=T^2\cdot T=ST$ : **$T$ et $S$ commutent.**

### Question 14.(a)

> [!INDICATION]
> Calculez le produit coefficient par coefficient.

#### Solution

Le coefficient de la ligne $j$ de $PE_i$ vaut $\sum_{k=1}^3p_{j,k}(E_i)_k=p_{j,i}$, coefficient de la ligne $j$ de la $i$-ème colonne de $P$.

Donc $PE_i=C_i$.

> [!JURY]
> Le rapport 2025 : « Le produit par bloc n’est pas au programme » ; une écriture du type $(C_1|C_2|C_3)E_1=C_1$ n'est pas acceptée.

### Question 14.(b)

> [!INDICATION]
> Utilisez $S=PD\,{}^tP$ et 14.(a).

#### Solution

${}^tP=P^{-1}$, donc $SC_i=PD\,{}^tPPE_i=PDE_i=P(d_iE_i)=d_iC_i$, où $d_i$ est le $i$-ème coefficient diagonal de $D$.

Et $C_i\neq0$ car $P$ est inversible.

**$C_i$ est un vecteur propre de $S$ associé à $\lambda_i=d_i$** ($\lambda_1=1$, $\lambda_2=16$, $\lambda_3=49$).

### Question 14.(c)

> [!INDICATION]
> Faites commuter $S$ et $T$.

#### Solution

D'après 13 et 14.(b), $S(TC_i)=T(SC_i)=\lambda_i\,TC_i$. Donc $TC_i\in\ker(S-\lambda_iI_3)$, **le sous-espace propre de $S$ associé à $\lambda_i$.**

### Question 14.(d)

> [!INDICATION]
> Quelle est la dimension des sous-espaces propres de $S$ ?

#### Solution

$S$ a trois valeurs propres distinctes $1$, $16$, $49$ en dimension $3$ : chaque sous-espace propre est de dimension au moins $1$ et la somme des dimensions est au plus $3$, donc chacun est de dimension $1$, égal à $\operatorname{Vect}(C_i)$.

Par 14.(c), il existe $\mu_i\in\mathbb R$ tel que $TC_i=\mu_iC_i$ : **$TC_i$ et $C_i$ sont colinéaires.**

### Question 15

> [!INDICATION]
> Calculez $NE_i$, c'est-à-dire la $i$-ème colonne de $N$.

#### Solution

Pour $i\in[\![1,3]\!]$ :
$$\begin{aligned}
NE_i&={}^tPTPE_i\\
&={}^tPTC_i\\
&=\mu_i\,{}^tPC_i\\
&=\mu_i\,{}^tPPE_i\\
&=\mu_iE_i.
\end{aligned}$$
La $i$-ème colonne de $N$ est $\mu_iE_i$ : **$N=\operatorname{diag}(\mu_1,\mu_2,\mu_3)$ est diagonale.**

> [!PIEGE]
> « $N^2$ est diagonale donc $N$ l'est » est faux en général : c'est la colinéarité de 14.(d) qui conclut.

### Question 16

> [!INDICATION]
> Les $\mu_i$ sont les valeurs propres de $T$ ; utilisez $N^2=D$ et leur signe.

#### Solution

$N={}^tPTP=P^{-1}TP$ est semblable à $T$ : ses coefficients diagonaux $\mu_i$ sont les valeurs propres de $T$, donc $\mu_i>0$.

De plus $N^2=D$ (12) donne $\mu_i^2=d_i$, donc $\mu_i=\sqrt{d_i}$, coefficient diagonal de $\Delta$ (choisi strictement positif).

**$N=\Delta$**, puis $T=PN\,{}^tP=P\Delta\,{}^tP=R$.

### Question 17

> [!INDICATION]
> Utilisez 16 et l'inversibilité de $R$.

#### Solution

$M=VT=VR$ et $R$ est inversible : $V=MR^{-1}=U$.

## Problème — Partie 1 : la fonction bêta

On définit $B(x,y)=\int_0^1t^{x-1}(1-t)^{y-1}\,dt$, on prouve sa symétrie, une relation de récurrence, et sa valeur aux entiers.

### Question 1.(a)

> [!INDICATION]
> Que devient $(1-t)^{y-1}$ en $0$ ?

#### Solution

Quand $t\to0$, $(1-t)^{y-1}\to1$, donc $\boxed{t^{x-1}(1-t)^{y-1}\underset{t\to0}{\sim}t^{x-1}}$.

### Question 1.(b)

> [!INDICATION]
> Continuité et positivité sur $]0,\frac12]$, équivalent, intégrale de Riemann en $0$.

#### Solution

La fonction $g:t\mapsto t^{x-1}(1-t)^{y-1}$ est continue et strictement positive sur $\left]0,\frac12\right]$ : l'intégrale n'est impropre qu'en $0$.

Par 1.(a), $g(t)\sim t^{x-1}=\frac1{t^{1-x}}$ en $0$.

Les fonctions étant positives, $\int_0^{1/2}g$ et $\int_0^{1/2}\frac{dt}{t^{1-x}}$ sont de même nature.

Cette intégrale de Riemann en $0$ converge si et seulement si $1-x<1$.

**$\int_0^{1/2}t^{x-1}(1-t)^{y-1}\,dt$ converge si et seulement si $x>0$.**

> [!JURY]
> Le rapport 2025 : « la continuité et/ou la positivité des fonctions comparées est oubliée très très souvent ».

### Question 1.(c)

> [!INDICATION]
> Le changement de variable affine $s=1-t$ est une bijection de classe $\mathcal C^1$ strictement monotone.

#### Solution

$t\mapsto1-t$ est une bijection de classe $\mathcal C^1$, strictement décroissante, de $\left[\frac12,1\right[$ sur $\left]0,\frac12\right]$. Par le théorème de changement de variable pour les intégrales impropres, $\int_{1/2}^1t^{x-1}(1-t)^{y-1}\,dt$ et $\int_0^{1/2}(1-s)^{x-1}s^{y-1}\,ds$ **sont de même nature** (et égales en cas de convergence).

> [!JURY]
> Le rapport 2025 : « On ne peut pas écrire l’égalité des intégrales par changement de variable tant qu’on n’a pas montré la convergence. »

### Question 1.(d)

> [!INDICATION]
> Définition de la convergence d'une intégrale impropre aux deux bornes : coupez en $\frac12$.

#### Solution

L'intégrale sur $]0,1[$ (impropre aux deux bornes) converge si et seulement si $\int_0^{1/2}$ et $\int_{1/2}^1$ convergent.

La première converge si et seulement si $x>0$ (1.(b)).

Par 1.(c), la seconde a la nature de $\int_0^{1/2}s^{y-1}(1-s)^{x-1}\,ds$, qui converge si et seulement si $y>0$ (1.(b) en échangeant $x$ et $y$).

**$\int_0^1t^{x-1}(1-t)^{y-1}\,dt$ converge si et seulement si $x>0$ et $y>0$.**

### Question 2

> [!INDICATION]
> Même changement de variable qu'en 1.(c), sur tout $]0,1[$.

#### Solution

Soient $x,y>0$. Par le changement de variable $s=1-t$ (bijection $\mathcal C^1$ strictement décroissante de $]0,1[$ sur lui-même), l'intégrale convergente $B(x,y)$ vaut
$$B(x,y)=\int_0^1(1-s)^{x-1}s^{y-1}\,ds=B(y,x).$$

### Question 3

> [!INDICATION]
> Attention : la borne $0$ peut être impropre.

#### Solution

$B(x,1)=\int_0^1t^{x-1}\,dt$, impropre en $0$ si $x<1$.

Pour $\varepsilon\in]0,1[$, $\int_\varepsilon^1t^{x-1}\,dt=\frac{1-\varepsilon^x}x\to\frac1x$ car $x>0$.

$\boxed{B(x,1)=\frac1x}$.

> [!JURY]
> Le rapport 2025 : « Très peu de candidats constatent que 0 est une borne impropre. »

### Question 4.(a)

> [!INDICATION]
> Factorisez par $t^{x-1}(1-t)^{y-1}$.

#### Solution

Les trois intégrales convergent (1.(d)) ; par linéarité,
$$B(x+1,y)+B(x,y+1)=\int_0^1t^{x-1}(1-t)^{y-1}\big(t+(1-t)\big)\,dt=B(x,y).$$

### Question 4.(b)

> [!INDICATION]
> Intégration par parties sur un segment $[\varepsilon,\eta]\subset]0,1[$, puis passage à la limite.

#### Solution

Soient $0<\varepsilon<\eta<1$.

Les fonctions $u(t)=(1-t)^y$ et $v(t)=\frac{t^x}x$ sont de classe $\mathcal C^1$ sur $[\varepsilon,\eta]$, avec $u'(t)=-y(1-t)^{y-1}$ et $v'(t)=t^{x-1}$ :
$$\int_\varepsilon^\eta t^{x-1}(1-t)^y\,dt=\left[\frac{t^x(1-t)^y}x\right]_\varepsilon^\eta+\frac yx\int_\varepsilon^\eta t^x(1-t)^{y-1}\,dt.$$
Quand $\varepsilon\to0$ et $\eta\to1$, le crochet tend vers $0$ (car $x>0$ et $y>0$), et les intégrales tendent vers $B(x,y+1)$ et $B(x+1,y)$.

Donc $B(x,y+1)=\frac yxB(x+1,y)$, soit $\boxed{xB(x,y+1)=yB(x+1,y)}$.

> [!JURY]
> Le rapport 2025 : « Très peu de candidats ont réalisé l’intégration par parties sur un segment. »

### Question 4.(c)

> [!INDICATION]
> Éliminez $B(x,y+1)$ entre 4.(a) et 4.(b).

#### Solution

D'après 4.(b), $B(x,y+1)=\frac yxB(x+1,y)$. En reportant dans 4.(a) :
$$\begin{aligned}
B(x+1,y)\left(1+\frac yx\right)&=B(x,y)\\
\text{donc}\\
\boxed{B(x+1,y)=\frac x{x+y}B(x,y)}.
\end{aligned}$$

### Question 5

> [!INDICATION]
> Récurrence sur $p$, pour $q$ quelconque fixé ; initialisation par 2 et 3.

#### Solution

Fixons $q\in\mathbb N^*$ et montrons par récurrence sur $p\ge1$ : $\mathcal P(p)$ : $B(p,q)=\frac{(p-1)!(q-1)!}{(p+q-1)!}$.

*Initialisation.* Par 2 et 3, $B(1,q)=B(q,1)=\frac1q=\frac{0!\,(q-1)!}{q!}$.

*Hérédité.* Si $\mathcal P(p)$ est vraie, par 4.(c) :
$$B(p+1,q)=\frac p{p+q}\cdot\frac{(p-1)!(q-1)!}{(p+q-1)!}=\frac{p!\,(q-1)!}{(p+q)!}.$$
*Conclusion.* Pour tous $p,q\in\mathbb N^*$, $B(p,q)=\frac{(p-1)!(q-1)!}{(p+q-1)!}$.

> [!JURY]
> Le rapport 2025 demande de préciser l'entier sur lequel porte la récurrence et l'hypothèse de récurrence, avec ses quantificateurs.

## Problème — Partie 2 : fonction Γ et lois γ

On calcule $\Gamma(n+1)$ et $\Gamma(\frac12)$, on étudie les lois de densité $f_{a,b}$ (lois gamma de paramètre d'échelle $\frac1b$), et la convolution donne $B(x,y)=\frac{\Gamma(x)\Gamma(y)}{\Gamma(x+y)}$.

### Question 6.(a)

> [!INDICATION]
> Récurrence avec $\Gamma(\nu+1)=\nu\Gamma(\nu)$ ; calculez $\Gamma(1)$.

#### Solution

Montrons par récurrence $\Gamma(n+1)=n!$. $\Gamma(1)=\int_0^{+\infty}e^{-t}\,dt=1=0!$. Si $\Gamma(n+1)=n!$, alors $\Gamma(n+2)=(n+1)\Gamma(n+1)=(n+1)!$. **$\Gamma(n+1)=n!$ pour tout $n\in\mathbb N$.**

> [!JURY]
> Le rapport 2025 : « Le sujet demandait de démontrer le résultat du cours et pas seulement de l’énoncer. »

### Question 6.(b)

> [!INDICATION]
> Avec $u=\sqrt{2t}$, faites apparaître la densité de la loi normale centrée réduite.

> [!INDICATION]
> Pour passer de $\int_{-\infty}^{+\infty}$ à $\int_0^{+\infty}$, faites le changement de variable $u\mapsto-u$ sur $]-\infty,0]$.

#### Solution

$\Gamma\left(\frac12\right)=\int_0^{+\infty}t^{-1/2}e^{-t}\,dt$ (convergente).

La fonction $u\mapsto\frac{u^2}2$ est une bijection de classe $\mathcal C^1$ strictement croissante de $]0,+\infty[$ sur $]0,+\infty[$ ; avec $t=\frac{u^2}2$, $dt=u\,du$ et $t^{-1/2}=\frac{\sqrt2}u$ :
$$\Gamma\left(\tfrac12\right)=\int_0^{+\infty}\frac{\sqrt2}ue^{-u^2/2}u\,du=\sqrt2\int_0^{+\infty}e^{-u^2/2}\,du.$$
Or $\int_{-\infty}^{+\infty}\frac{e^{-u^2/2}}{\sqrt{2\pi}}\,du=1$ (densité de $\mathcal N(0,1)$), et le changement de variable $u\mapsto-u$ donne $\int_{-\infty}^0e^{-u^2/2}\,du=\int_0^{+\infty}e^{-u^2/2}\,du$. Donc $\int_0^{+\infty}e^{-u^2/2}\,du=\frac{\sqrt{2\pi}}2$ et
$$\boxed{\Gamma\left(\tfrac12\right)=\sqrt2\cdot\frac{\sqrt{2\pi}}2=\sqrt\pi}.$$

> [!JURY]
> Le rapport 2025 : « L’argument de parité ne pouvait être utilisé car il est hors programme. » D'où le changement de variable $u\mapsto-u$ écrit explicitement.

### Question 7.(a)

> [!INDICATION]
> Sur $]0,+\infty[$, faites le changement de variable $u=bt$ pour vous ramener à $\Gamma(a)$. L'intégrale est impropre en $0$ et en $+\infty$.

#### Solution

$f_{a,b}$ est nulle sur $]-\infty,0]$.

Sur $]0,+\infty[$, $t\mapsto bt$ est une bijection de classe $\mathcal C^1$ strictement croissante de $]0,+\infty[$ sur lui-même ; l'intégrale $\int_0^{+\infty}u^{a-1}e^{-u}\,du=\Gamma(a)$ converge, donc
$$\int_0^{+\infty}t^{a-1}e^{-bt}\,dt=\frac1{b^a}\int_0^{+\infty}u^{a-1}e^{-u}\,du=\frac{\Gamma(a)}{b^a}$$
converge. **$\int_{-\infty}^{+\infty}f_{a,b}(t)\,dt$ converge.**

> [!JURY]
> Le rapport 2025 : $f_{a,b}$ n'est pas directement une densité de loi $\gamma$ (à cause du $b$) ; et l'intégrale est impropre en $0$ comme en $+\infty$.

### Question 7.(b)

> [!INDICATION]
> Trois conditions : positivité, continuité sauf en un nombre fini de points, intégrale égale à $1$.

#### Solution

$f_{a,b}\ge0$ ; elle est continue sur $\mathbb R$ sauf peut-être en $0$ ; et par 7.(a), $\int_{-\infty}^{+\infty}f_{a,b}=\frac{b^a}{\Gamma(a)}\cdot\frac{\Gamma(a)}{b^a}=1$. **$f_{a,b}$ est une densité de probabilité.**

### Question 8.(a)

> [!INDICATION]
> Reconnaissez la loi ; prouvez l'existence des moments à l'aide de $\Gamma(a+1)$ et $\Gamma(a+2)$.

#### Solution

$f_{a,1}(t)=\frac1{\Gamma(a)}t^{a-1}e^{-t}$ pour $t>0$ : **$X$ suit la loi $\gamma(a)$.** Les intégrales $\int_0^{+\infty}t\,f_{a,1}(t)\,dt=\frac{\Gamma(a+1)}{\Gamma(a)}$ et $\int_0^{+\infty}t^2f_{a,1}(t)\,dt=\frac{\Gamma(a+2)}{\Gamma(a)}$ convergent (intégrandes positifs) :
$$\begin{aligned}
\mathbb E(X)&=\frac{\Gamma(a+1)}{\Gamma(a)}\\
&=a\\
\mathbb E(X^2)&=\frac{(a+1)a\Gamma(a)}{\Gamma(a)}\\
&=a(a+1)
\end{aligned}$$
donc $X$ admet une variance et $\boxed{\mathbb V(X)=a(a+1)-a^2=a}$, $\boxed{\mathbb E(X)=a}$.

> [!JURY]
> Le rapport 2025 : « la variance de la loi γ n’est pas explicitement au programme. Il fallait démontrer le résultat. »

### Question 8.(b)

> [!INDICATION]
> Calculez $\mathbb E(X^2)$ en vous ramenant à 7.(a).

#### Solution

$f_{1,b}(t)=be^{-bt}$ pour $t>0$ : **$X$ suit la loi exponentielle $\mathcal E(b)$**, d'espérance $\frac1b$.

Pour la variance, avec 7.(a) (pour $a=3$) l'intégrale $\int_0^{+\infty}t^2be^{-bt}\,dt=b\cdot\frac{\Gamma(3)}{b^3}=\frac2{b^2}$ converge : $X$ admet un moment d'ordre $2$, donc une variance, et $\mathbb V(X)=\frac2{b^2}-\frac1{b^2}=\boxed{\frac1{b^2}}$.

### Question 9.(a)

> [!INDICATION]
> Fonction de répartition de $bX$ ; le signe de $b$ compte.

#### Solution

Comme $b>0$, pour $x\in\mathbb R$, $\mathbb P(bX\le x)=\mathbb P\left(X\le\frac xb\right)=F_X\left(\frac xb\right)$.

$F_X$ est de classe $\mathcal C^1$ sauf peut-être en $0$, donc $bX$ est à densité, de densité
$$x\mapsto\frac1bf_{a,b}\left(\frac xb\right)=\begin{cases}\dfrac{x^{a-1}e^{-x}}{\Gamma(a)}&\text{si }x>0\\0&\text{sinon}\end{cases}=f_{a,1}(x).$$
**$bX$ suit la loi $\gamma(a)$.**

> [!JURY]
> Le rapport 2025 : « Il est important de préciser que b > 0 ».

### Question 9.(b)

> [!INDICATION]
> Utilisez 9.(a) et 8.(a).

#### Solution

$X=\frac1b(bX)$ avec $bX\hookrightarrow\gamma(a)$ qui admet espérance $a$ et variance $a$ (8.(a)). Par linéarité, $X$ admet une espérance et une variance :
$$\begin{aligned}
\boxed{\mathbb E(X)=\frac ab}\\
\boxed{\mathbb V(X)=\frac a{b^2}}.
\end{aligned}$$

### Question 10.(a)

> [!INDICATION]
> Produit de convolution : $h(x)=\int_{-\infty}^{+\infty}f_{a_1,b}(t)f_{a_2,b}(x-t)\,dt$. Identifiez où l'intégrande est non nul.

> [!INDICATION]
> Pour $x>0$, le changement de variable $t=xs$ fait apparaître $B(a_1,a_2)$.

#### Solution

Posons $h(x)=\int_{-\infty}^{+\infty}f_{a_1,b}(t)f_{a_2,b}(x-t)\,dt$. L'intégrande est non nul seulement si $t>0$ et $x-t>0$.
- Si $x\le0$ : l'intégrande est nul, $h(x)=0$.
- Si $x>0$ : pour $t\in]0,x[$,
$$f_{a_1,b}(t)f_{a_2,b}(x-t)=\frac{b^{a_1+a_2}}{\Gamma(a_1)\Gamma(a_2)}e^{-bx}\,t^{a_1-1}(x-t)^{a_2-1}.$$
Le changement de variable $t=xs$ ($s\in]0,1[$, bijection affine strictement croissante) donne
$$\int_0^xt^{a_1-1}(x-t)^{a_2-1}\,dt=x^{a_1+a_2-1}\int_0^1s^{a_1-1}(1-s)^{a_2-1}\,ds=x^{a_1+a_2-1}B(a_1,a_2),$$
intégrale convergente par 1.(d).

Donc $h(x)=\frac{b^{a_1+a_2}B(a_1,a_2)}{\Gamma(a_1)\Gamma(a_2)}x^{a_1+a_2-1}e^{-bx}$ pour $x>0$ et $h(x)=0$ sinon.

$h$ est définie partout et continue sauf peut-être en $0$.

$X_1$ et $X_2$ étant indépendantes à densité, **$h$ est une densité de $X_1+X_2$.**

> [!JURY]
> Le rapport 2025 : certains « croient que les densités sont bornées pour justifier la convergence du produit de convolution » ; ici $f_{a,b}$ n'est pas bornée si $a<1$, d'où le calcul direct et la continuité de $h$.

### Question 10.(b)

> [!INDICATION]
> Écrivez que $h$ est une densité (intégrale égale à $1$) et calculez cette intégrale avec 7.(a).

#### Solution

$h$ est une densité, donc d'intégrale $1$. Par 7.(a) avec $a=a_1+a_2$ :
$$\begin{aligned}
1&=\frac{b^{a_1+a_2}B(a_1,a_2)}{\Gamma(a_1)\Gamma(a_2)}\cdot\frac{\Gamma(a_1+a_2)}{b^{a_1+a_2}}\\
\text{donc}\\
B(a_1,a_2)&=\frac{\Gamma(a_1)\Gamma(a_2)}{\Gamma(a_1+a_2)}.
\end{aligned}$$
Ceci vaut pour tous $a_1,a_2>0$ (avec $b=1$ par exemple) : $\boxed{B(x,y)=\dfrac{\Gamma(x)\Gamma(y)}{\Gamma(x+y)}}$.

### Question 10.(c)

> [!INDICATION]
> 6.(b) et 10.(b).

#### Solution

$$\begin{aligned}
B\left(\tfrac12,\tfrac12\right)&=\frac{\Gamma\left(\frac12\right)^2}{\Gamma(1)}\\
&=\frac{\sqrt\pi\times\sqrt\pi}1\\
&=\boxed{\pi}.
\end{aligned}$$

> [!PIEGE]
> $\sqrt\pi\times\sqrt\pi=\pi$, pas $2\sqrt\pi$ ; le rapport 2025 invite à vérifier la cohérence avec $\Gamma(\frac12)$ trouvé en 6.(b).

## Problème — Partie 3 : approximations de Monte-Carlo

On approche $B(x,y)$ et $\Gamma(a)$ par des moyennes empiriques ; la loi faible des grands nombres en assure la convergence.

### Question 11.(a)

> [!INDICATION]
> Théorème de transfert : l'espérance est une intégrale sur $]0,1[$ contre la densité uniforme.

#### Solution

$U$ a pour densité $\mathbf 1_{]0,1[}$. Par le théorème de transfert, $Z=U^{x-1}(1-U)^{y-1}$ admet une espérance si et seulement si $\int_0^1u^{x-1}(1-u)^{y-1}\,du$ converge absolument ; l'intégrande est positif et l'intégrale converge (1.(d)). Donc $\boxed{\mathbb E(Z)=B(x,y)}$.

### Question 11.(b)

> [!INDICATION]
> Un seul tirage uniforme.

#### Solution

```python
def Simul(x, y):
    U = rd.random()
    return U**(x-1) * (1-U)**(y-1)
```
On ne tire qu'**un seul** nombre `U`, utilisé dans les deux facteurs. (`rd.random()` peut en théorie renvoyer $0$ ; cet événement de probabilité négligeable est ignoré.)

> [!JURY]
> Le rapport 2025 : certains utilisent deux appels à `rd.random()`, alors que « U les deux fois désigne la même variable et donc prend la même valeur ».

### Question 11.(c)

> [!INDICATION]
> Loi faible des grands nombres pour les $Z_k=U_k^{x-1}(1-U_k)^{y-1}$ ; justifiez leur indépendance.

#### Solution

Les $U_k$ sont indépendantes, donc, par le lemme des coalitions, les $Z_k=U_k^{x-1}(1-U_k)^{y-1}$ sont indépendantes ; elles ont la même loi que $Z$, d'espérance $B(x,y)$ (11.(a)) et de variance $\sigma^2$ (admise par l'énoncé).

$R_n$ est leur moyenne empirique.

Par la loi faible des grands nombres (ou l'inégalité de Bienaymé-Tchebychev), pour tout $\varepsilon>0$ :
$$\mathbb P\big(|R_n-B(x,y)|\ge\varepsilon\big)\le\frac{\sigma^2}{n\varepsilon^2}\xrightarrow[n\to+\infty]{}0.$$
**$(R_n)$ converge en probabilité vers la variable certaine $B(x,y)$.**

*Remarque sur l'énoncé.* $\mathbb E(Z^2)=\int_0^1u^{2x-2}(1-u)^{2y-2}\,du$ converge si et seulement si $2x-1>0$ et $2y-1>0$ (question 1.(d)).

La variance admise n'existe donc que si $x>\frac12$ et $y>\frac12$ ; pour $x=y=\frac12$ (question 11.(e)), elle est infinie.

La convergence en probabilité reste vraie avec la seule existence de l'espérance (loi faible des grands nombres de Khintchine), mais ce résultat est hors programme ; la preuve ci-dessus vaut pour $x,y>\frac12$.

### Question 11.(d)

> [!INDICATION]
> Un tableau de $n$ tirages uniformes, puis la moyenne (`np.mean`).

#### Solution

```python
def Rn(x, y, n):
    U = rd.random(n)
    return np.mean(U**(x-1) * (1-U)**(y-1))
```
Essai : `Rn(2, 3, 100000)` donne $\approx0{,}0831$, pour $B(2,3)=\frac{1!\,2!}{4!}=\frac1{12}\approx0{,}0833$.

### Question 11.(e)

> [!INDICATION]
> Vers quelle valeur les courbes se stabilisent-elles ? Quelle question de la partie 2 donne cette valeur ?

#### Solution

Les trajectoires de $R_n$ se stabilisent autour de $\pi\approx3{,}14$.

La figure illustre le résultat de 10.(c) : **$B\left(\frac12,\frac12\right)=\Gamma\left(\frac12\right)^2=\pi$**, valeur vers laquelle $R_n$ converge par 11.(c).

Les sauts brusques des trajectoires s'expliquent par la variance infinie de $Z$ pour $x=y=\frac12$ : un tirage de $U$ très proche de $0$ ou de $1$ produit une valeur très grande.

> [!JURY]
> Le rapport 2025 : « Il est attendu une phrase ayant du sens. » Écrire que « la figure illustre $\pi$ » ne suffit pas.

### Question 12.(a)

> [!INDICATION]
> Théorème de transfert : $\mathbb E(X^{a-1})$ et $\mathbb E(X^{2a-2})$ s'écrivent avec $\Gamma$.

#### Solution

Par le théorème de transfert (intégrandes positifs) :
$$\begin{aligned}
\mathbb E(X^{a-1})&=\int_0^{+\infty}t^{a-1}e^{-t}\,dt\\
&=\Gamma(a)\\
\mathbb E\left(X^{2(a-1)}\right)&=\int_0^{+\infty}t^{2a-2}e^{-t}\,dt\\
&=\Gamma(2a-1)
\end{aligned}$$
convergentes car $a>0$ et $2a-1\ge1>0$. $X^{a-1}$ admet donc un moment d'ordre $2$, et
$$\begin{aligned}
\boxed{\mathbb E(X^{a-1})=\Gamma(a)}\\
\boxed{\mathbb V(X^{a-1})=\Gamma(2a-1)-\Gamma(a)^2}.
\end{aligned}$$

### Question 12.(b)

> [!INDICATION]
> Sans biais : linéarité de l'espérance. Convergent : variance et Bienaymé-Tchebychev (ou loi faible des grands nombres).

#### Solution

Les $X_k^{a-1}$ sont indépendantes (lemme des coalitions) et de même loi que $X^{a-1}$. Par linéarité, $\mathbb E(M_n)=\Gamma(a)$ : **$M_n$ est sans biais.** Par indépendance, $\mathbb V(M_n)=\frac{\Gamma(2a-1)-\Gamma(a)^2}n$, et par l'inégalité de Bienaymé-Tchebychev, pour $\varepsilon>0$,
$$\mathbb P\big(|M_n-\Gamma(a)|\ge\varepsilon\big)\le\frac{\Gamma(2a-1)-\Gamma(a)^2}{n\varepsilon^2}\xrightarrow[n\to+\infty]{}0.$$
**$(M_n)$ est un estimateur convergent de $\Gamma(a)$.**

### Question 12.(c)

> [!INDICATION]
> Quelle est la loi de $-\ln(1-U)$ ? Quelle est la taille de `U` ?

#### Solution

`U` est un tableau de $n$ simulations indépendantes de la loi uniforme sur $[0,1[$ ;

$1-U$ suit la loi uniforme sur $]0,1]$ et $-\ln(1-U)$ suit la loi $\mathcal E(1)$ (méthode d'inversion : $\mathbb P(-\ln(1-U)\le x)=1-e^{-x}$ pour $x\ge0$).

**`Myst(n)` renvoie un tableau de $n$ simulations indépendantes de la loi exponentielle de paramètre $1$.**

> [!JURY]
> Le rapport 2025 : peu reconnaissent la loi exponentielle, « Et encore moins réalisent qu’une liste de longueur n est renvoyée. »

### Question 12.(d)

> [!INDICATION]
> Calculez la moyenne des $X_k^{a-1}$.

#### Solution

```python
def Approx(n, a):
    X = Myst(n)
    return np.mean(X**(a-1))
```
La fonction renvoie une réalisation de $M_n$, qui approche $\Gamma(a)$ pour $n$ grand (12.(b)). Essai : `Approx(200000, 3.5)` donne $\approx3{,}32$ pour $\Gamma(3{,}5)\approx3{,}323$.

## Bilan

**Méthodes à retenir.**
- Séries : Riemann, convergence absolue (le critère des séries alternées est hors programme), découpage pair/impair sur des sommes partielles $2N+1$.
- Lemme de Riemann-Lebesgue version $\mathcal C^1$ : intégration par parties et majoration en $\frac1\lambda$ ; théorème du prolongement de la dérivée via un développement limité.
- Polynôme annulateur : obtenu par un argument de dimension ; valeurs propres incluses dans ses racines (preuve à savoir refaire) ; une matrice diagonalisable à une seule valeur propre est scalaire.
- Décomposition polaire : $S={}^tMM$ symétrique définie positive, théorème spectral, racine carrée $R=P\Delta\,{}^tP$, $U=MR^{-1}$ orthogonale ; unicité par commutation avec $S$ et stabilité des droites propres.
- Intégrales impropres à paramètres : équivalent en chaque borne, changement de variable affine, intégration par parties sur un segment puis limite.
- Fonctions $\Gamma$ et $B$ : $\Gamma(n+1)=n!$, $\Gamma(\frac12)=\sqrt\pi$, $B(p,q)=\frac{(p-1)!(q-1)!}{(p+q-1)!}$, $B=\frac{\Gamma\Gamma}{\Gamma}$ par convolution de lois gamma.
- Monte-Carlo : moyenne empirique, lemme des coalitions, loi faible des grands nombres — en vérifiant l'existence de la variance.

**À revoir si besoin.** Théorème du prolongement de la dérivée ; changement de variable dans une intégrale impropre ; densité d'une somme de variables indépendantes ; `np.dot`, `np.all`, tableaux de simulations.

**Questions transposables.** Problème de Bâle ($\zeta(2)=\frac{\pi^2}6$) ; décomposition polaire et racine carrée d'une matrice symétrique positive ; fonction bêta et lois bêta ; estimation de $\pi$ par simulation.
