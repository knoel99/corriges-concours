# Centrale-Supélec PC — Mathématiques 2 2024 · Corrigé guidé

*Corrigé rédigé par IA, non officiel. Signalez toute erreur.*

## Présentation du sujet

Le sujet étudie les produits infinis. Les premières parties établissent des estimations et la convergence uniforme. Ces outils mènent à la factorisation du sinus, à la somme des inverses des carrés et à deux formules pour la fonction gamma.

## Partie I — Résultats préliminaires

### I.A — Deux inégalités pour les produits

### Question 1

> [!INDICATION]
> Développez les produits en choisissant, dans chaque facteur, soit le terme constant, soit la variable.

#### Solution

La distributivité donne
$$
\prod_{k=1}^n(1+x_k)-1
=\sum_{\varnothing\ne J\subseteq\{1,\ldots,n\}}\prod_{j\in J} x_j.
$$
Par inégalité triangulaire, le module est au plus la somme des produits des $|x_j|$ sur les mêmes sous-ensembles. Cette somme est le développement de $\prod_{k=1}^n(1+|x_k|)-1$.

### Question 2

> [!INDICATION]
> Utilisez la tangente à l’exponentielle en zéro. Pouvez-vous multiplier les inégalités ?

#### Solution

Pour $x\in\mathbb R$, $1+x\leq e^x$. Si $x\geq-1$, le membre gauche est positif ou nul. On multiplie donc les $n$ inégalités pour obtenir
$$
\begin{aligned}
\prod_{k=1}^n(1+x_k)&\leq\prod_{k=1}^n e^{x_k}\\
&=\exp\left(\sum_{k=1}^n x_k\right).
\end{aligned}
$$

### I.B — Une limite exponentielle complexe

### Question 3

> [!INDICATION]
> Invoquez une représentation de l’exponentielle qui vaut pour un argument complexe.

#### Solution

La série de l’exponentielle converge absolument pour tout $t\in\mathbb C$. En retranchant les deux premiers termes puis en prenant les modules,
$$
\begin{aligned}
|e^t-1-t|&\leq |t|^2\sum_{j=0}^{+\infty}\frac{|t|^j}{(j+2)!}\\
&\leq |t|^2e^{|t|}.
\end{aligned}
$$
La dernière borne vient de $(j+2)!\geq j!$ et donne aussi le résultat pour $t=0$.

### Question 4

> [!INDICATION]
> Factorisez la différence de puissances. Combien de termes restent à majorer ?

#### Solution

L’identité
$$
a^n-b^n=(a-b)\sum_{k=0}^{n-1}a^{n-1-k}b^k
$$
donne la majoration, puisque chacun des $n$ monômes dans la somme a un module au plus $M^{n-1}$. Pour $n=1$, le facteur de degré zéro vaut 1 et l’inégalité est une égalité.

### Question 5

> [!INDICATION]
> Comparez les puissances de deux complexes voisins, dont l’un est une exponentielle.

#### Solution

Posons $a=1+z/n$ et $b=e^{z/n}$. On a $|a|\leq 1+|z|/n\leq e^{|z|/n}$, et $|b|=e^{\operatorname{Re}(z)/n}\leq e^{|z|/n}$. Par Q3, $|a-b|\leq |z|^2e^{|z|/n}/n^2$.

La Q4 donne
$$
|a^n-b^n|\leq n e^{(n-1)|z|/n}\frac{|z|^2e^{|z|/n}}{n^2}
=\frac{|z|^2 e^{|z|}}n.
$$
Comme $b^n=e^z$, c’est le résultat voulu.

### Question 6

> [!INDICATION]
> Dans la majoration précédente, seul le dénominateur dépend de l’indice.

#### Solution

Pour $z$ fixé, le majorant de Q5 tend vers zéro. La suite $((1+z/n)^n)_{n\geq1}$ converge donc vers $e^z$.

## Partie II — Exemples de produits infinis

### II.A — Deux produits télescopiques

### Question 7

> [!INDICATION]
> Factorisez le premier produit. Dans le second, regroupez les termes de rang impair avec ceux de rang pair qui les suivent.

#### Solution

Pour $N\geq2$, on a
$$
\begin{aligned}
\prod_{n=2}^N\left(1-\frac1{n^2}\right)&=\left(\prod_{n=2}^N\frac{n-1}{n}\right)
 \left(\prod_{n=2}^N\frac{n+1}{n}\right)\\
&=\frac{N+1}{2N}.
\end{aligned}
$$
La limite est $1/2$.

Dans le second produit, le terme de rang 2 vaut $1/2$. Pour chaque $k\geq2$, les facteurs de rangs $2k-1$ et $2k$ sont réciproques.

Le produit jusqu’à $2N$ vaut donc $1/2$, et celui jusqu’à $2N+1$ vaut $(1+1/(2N+1))/2$. Les deux sous-suites ont la même limite, donc ce second produit vaut également $1/2$.

### II.B — Produit de Wallis

### Question 8

> [!INDICATION]
> Intégrez par parties un facteur cosinus, puis remplacez le carré du sinus.

#### Solution

Dans $W_{n+2}$, intégrons $\cos u$ et dérivons $\cos^{n+1}u$. Le terme de bord $[\cos^{n+1}u\sin u]_0^{\pi/2}$ est nul. Il reste
$$
W_{n+2}=(n+1)\int_0^{\pi/2}\cos^n u\sin^2 u\,\mathrm du
=(n+1)(W_n-W_{n+2}).
$$
Cela donne la relation demandée. Comme $W_1=1$, on en déduit, avec le produit vide pour $n=0$,
$$
\begin{aligned}
W_{2n+1}&=\prod_{j=1}^n\frac{2j}{2j+1}\\
&=\frac{2^{2n}(n!)^2}{(2n+1)!}.
\end{aligned}
$$

### Question 9

> [!INDICATION]
> Appliquez Stirling à la formule de Q8. Ensuite, exprimez le produit de Wallis à l’aide du carré de cette expression.

#### Solution

Réécrivons le dénominateur en $(2n+1)(2n)!$. La formule de Stirling donne
$$
\frac{4^n(n!)^2}{(2n)!}\sim\sqrt{\pi n}.
$$
En divisant par $2n+1$, on obtient $W_{2n+1}\sim\sqrt\pi/(2\sqrt n)$.

Pour $N\geq1$, séparons les deux facteurs du dénominateur.
$$
\begin{aligned}
\prod_{k=1}^N\left(1+\frac1{4k^2-1}\right)&=\left(\prod_{k=1}^N\frac{2k}{2k+1}\right)\\
&\quad \times\left(\prod_{k=1}^N\frac{2k}{2k-1}\right).
\end{aligned}
$$
Le premier produit est $W_{2N+1}$. Le rapport du second au premier est le produit télescopique des $(2k+1)/(2k-1)$, égal à $2N+1$. Le produit partiel vaut donc $(2N+1)W_{2N+1}^2$, de limite $\pi/2$.

### II.C — Événements indépendants

### Question 10

> [!INDICATION]
> Appliquez Q2 à un produit partiel en exploitant le signe des probabilités.

#### Solution

Pour $m\geq n$, Q2 appliquée aux $-\mathbb P(A_p)\in[-1,0]$ donne
$$
\begin{aligned}
0&\leq\prod_{p=n}^m(1-\mathbb P(A_p))\\
&\leq\exp\left(-\sum_{p=n}^m\mathbb P(A_p)\right).
\end{aligned}
$$
La somme positive diverge, même après suppression de ses premiers termes. Le majorant tend vers zéro et le produit infini demandé vaut zéro.

### Question 11

> [!INDICATION]
> Passez aux complémentaires pour exploiter l’indépendance d’une famille finie.

#### Solution

Les complémentaires $A_p^c$ sont mutuellement indépendants. Pour tout $m\geq n$, la probabilité de $\bigcap_{p=n}^m A_p^c$ est le produit partiel de Q10. Ces événements décroissent en $m$. Par continuité décroissante de la probabilité et Q10,
$$
\mathbb P\left(\bigcap_{p\geq n}A_p^c\right)=0.
$$
Ainsi chaque $\bigcup_{p\geq n}A_p$ a probabilité 1. Leur intersection dénombrable a encore probabilité 1, car son complémentaire est une union dénombrable d’événements négligeables.

## Partie III — Fonctions définies par un produit infini

### III.A — Convergence uniforme et continuité

### Question 12

> [!INDICATION]
> La somme des modules est une fonction continue sur un segment. Utilisez-la pour majorer le produit partiel.

#### Solution

La somme $R_0$ est continue comme limite uniforme de sommes partielles continues. Elle est bornée sur le segment. Prenons $M=1+\max_{\mathcal S}R_0>0$. Par Q2,
$$
\begin{aligned}
Q_n(x)&\leq\exp\left(\sum_{k=1}^n|f_k(x)|\right)\\
&\leq e^M.
\end{aligned}
$$
Or $Q_{n+1}-Q_n=Q_n|f_{n+1}|$. On obtient la majoration demandée avec un $M$ indépendant de $x$ et de $n$.

### Question 13

> [!INDICATION]
> Factorisez chaque différence, puis comparez les modules des facteurs.

#### Solution

La différence $P_{n+1}-P_n$ vaut $P_n f_{n+1}$. Puisque $|1+f_k|\leq1+|f_k|$, on a $|P_n|\leq Q_n$. Il vient
$$
|P_{n+1}-P_n|\leq Q_n|f_{n+1}|=Q_{n+1}-Q_n.
$$

### Question 14

> [!INDICATION]
> Faites télescoper les différences successives et utilisez le reste uniforme de la série.

#### Solution

Pour $m>n$, les Q12 et Q13 donnent
$$
\begin{aligned}
|P_m(x)-P_n(x)|&\leq e^M\sum_{k=n+1}^m|f_k(x)|\\
&\leq e^M R_n(x).
\end{aligned}
$$
Le reste $R_n$ tend uniformément vers zéro par hypothèse. Pour chaque $x$, les produits partiels sont de Cauchy dans $\mathbb R$ et définissent $P(x)$. En passant à la limite en $m$, on obtient $\lVert P-P_n\rVert_\infty\leq e^M\lVert R_n\rVert_\infty$, donc la convergence uniforme.

### Question 15

> [!INDICATION]
> La limite uniforme donne la continuité. Pour la non-annulation, regardez la somme des logarithmes.

#### Solution

Chaque $P_n$ est continue, donc $P$ l’est par Q14. Fixons $x$. Les facteurs sont strictement positifs.

Comme $\sum |f_k(x)|$ converge, $f_k(x)$ tend vers zéro et, à partir d’un certain rang, $|\ln(1+f_k(x))|\leq2|f_k(x)|$. Cette borne suit de l’inégalité des accroissements finis sur $[-1/2,1/2]$ pour $u\mapsto\ln(1+u)$.

La série des logarithmes converge donc absolument. Les produits partiels sont les exponentielles de ses sommes partielles. Leur limite est une exponentielle réelle et est strictement positive.

### III.B — Un exemple de produit

### Question 16

> [!INDICATION]
> Choisissez un segment dont la borne inférieure est strictement positive, puis cherchez une série numérique majorante.

#### Solution

Sur tout segment $[a,b]\subset]0,+\infty[$, les fonctions $f_n(x)=-e^{-nx^2}$ sont continues à valeurs dans $]-1,0[$.

Elles vérifient $|f_n(x)|\leq e^{-na^2}$, et cette suite géométrique est sommable. La convergence normale entraîne la convergence uniforme de la série des valeurs absolues. Les Q14 et Q15 donnent donc l’existence et la continuité de $f$ sur chaque tel segment, et ainsi sur $]0,+\infty[$. De plus $f(x)>0$.

### Question 17

> [!INDICATION]
> Isolez le premier facteur pour établir la croissance stricte et la limite en zéro. À l’infini, majorez l’écart entre le produit et 1.

#### Solution

Pour deux points positifs $x<y$, chaque facteur est croissant. Le produit des facteurs d’indices au moins 2 est donc croissant par passage à la limite. Il est strictement positif par Q15 appliquée à la suite commençant au second terme. Le premier facteur est strictement croissant et positif. Leur produit $f$ est donc strictement croissant.

Tous les facteurs sont au plus 1 et $0<f(x)\leq1-e^{-x^2}$, donc $f(x)\to0$ pour $x\to0^+$. Les Q1 et Q2 appliquées au produit partiel donnent, puis on passe à la limite,
$$
0\leq1-f(x)\leq\exp\left(\sum_{k\geq1}e^{-kx^2}\right)-1.
$$
La somme vaut $e^{-x^2}/(1-e^{-x^2})$, qui tend vers zéro à l’infini. Donc $f(x)\to1$ pour $x\to+\infty$.

$$
\begin{array}{c|ccc}
x&0^+&&+\infty\\
\hline
f(x)&0&\nearrow&1
\end{array}
$$

### III.C — Dérivation du produit

### Question 18

> [!INDICATION]
> Dérivez la somme des logarithmes des facteurs du produit fini.

#### Solution

Tous les facteurs sont strictement positifs. Pour chaque $n$,
$$
\ln P_n(x)=\sum_{k=1}^n\ln(1+f_k(x)).
$$
En dérivant puis en multipliant par $P_n(x)$, on obtient
$$
P'_n(x)=P_n(x)\sum_{k=1}^n\frac{f_k'(x)}{1+f_k(x)}.
$$

### Question 19

> [!INDICATION]
> Identifiez la limite uniforme des dérivées en contrôlant les deux facteurs de la formule précédente.

#### Solution

Notons $S_n$ la somme partielle des quotients de Q18 et $S$ sa limite uniforme. Par Q14, $P_n$ converge uniformément vers $P$. Les suites sont uniformément bornées sur le segment, car leurs limites sont continues.

En écrivant $P_nS_n-PS=P_n(S_n-S)+(P_n-P)S$, on obtient la convergence uniforme de $P_n'$ vers $PS$.

Le théorème de dérivation des suites de fonctions s’applique. Les fonctions $P_n$ sont de classe $\mathcal C^1$, convergent au moins en un point et leurs dérivées convergent uniformément.

Donc $P$ est de classe $\mathcal C^1$ et $P'=PS$. La Q15 donne $P>0$, ce qui autorise la division par $P$.

## Partie IV — Produit infini pour le sinus

### IV.A — Polynômes d’approximation

### Question 20

> [!INDICATION]
> Calculez le coefficient de la plus haute puissance dans les deux développements.

#### Solution

Posons $m=2n+1$. Les deux puissances entrant dans $P_n$ sont des polynômes de degré $m$. Comme $m$ est impair, le coefficient de $X^m$ dans leur différence divisée par $2i$ est
$$
\frac{i^m-(-i)^m}{2i m^m}=\frac{(-1)^n}{m^m}\ne0.
$$
Donc $P_n$ est de degré $2n+1$.

### Question 21

> [!INDICATION]
> Exprimez les deux nombres comportant une tangente à l’aide d’exponentielles d’angles opposés.

#### Solution

Pour $0\leq k<m$, posons $\theta_k=k\pi/m$. Comme $m$ est impair, $\cos\theta_k\ne0$. Au point $x_k=m\tan\theta_k$,
$$
1\pm i\frac{x_k}{m}=\frac{e^{\pm i\theta_k}}{\cos\theta_k}.
$$
Les puissances d’ordre $m$ coïncident puisque $e^{im\theta_k}=e^{-im\theta_k}=(-1)^k$. Ainsi chaque $x_k$ est racine. Les tangentes sont distinctes car les angles sont distincts modulo $\pi$. Cela fournit $m$ racines distinctes pour un polynôme de degré $m$, donc toutes ses racines.

### Question 22

> [!INDICATION]
> Associez les angles dont la somme vaut $\pi$, puis regroupez les facteurs des deux racines correspondantes.

#### Solution

On a $x_0=0$. Pour $1\leq j\leq n$, l’angle d’indice $m-j$ vaut $\pi-\theta_j$, donc $x_{m-j}=-x_j$.

Ces paires épuisent les racines non nulles. La factorisation de $P_n$ est donc proportionnelle à $X\prod_{j=1}^n(X-x_j)(X+x_j)$. En extrayant le facteur constant $-x_j^2$ de chaque produit quadratique, il existe $\lambda$ tel que
$$
P_n(X)=\lambda X\prod_{j=1}^n\left(1-\frac{X^2}{x_j^2}\right).
$$

### Question 23

> [!INDICATION]
> Identifiez le coefficient de degré un dans les deux expressions du polynôme.

#### Solution

La dérivée en zéro de $P_n$ dans sa définition vaut
$$
P_n'(0)=\frac{1}{2i}\left(m\frac{i}{m}-m\frac{-i}{m}\right)=1.
$$
Dans la factorisation de Q22, le produit vaut 1 en zéro. Par conséquent $\lambda=P_n'(0)=1$, d’où la formule voulue.

### Question 24

> [!INDICATION]
> Appliquez la limite exponentielle complexe aux deux puissances de la définition.

#### Solution

Pour $x\in\mathbb R$ fixé, la Q6 appliquée à $ix$ et $-ix$ le long des indices $m=2n+1$ donne la convergence des deux puissances vers $e^{ix}$ et $e^{-ix}$.

Leur différence divisée par $2i$ tend vers $\sin x$. La convergence est simple sur $\mathbb R$.

### IV.B — Passage au produit infini

### Question 25

> [!INDICATION]
> Vérifiez d’abord le raccordement des deux définitions lorsque $t<k$. Dans la seconde zone, utilisez $\tan u\geq u$.

#### Solution

Posons $m=\lfloor t\rfloor$. Si $m<k-1$, les deux valeurs sont $P_m(x)$. Si $m=k-1$, la valeur $v_{k-1}(t)$ est le produit entier de Q23, donc vaut encore $P_m(x)=v_k(t)$.

Si $m\geq k$, les produits diffèrent uniquement par le dernier facteur.
$$
v_k(t)-v_{k-1}(t)
=-\frac{x^2}{((2m+1)\tan(k\pi/(2m+1)))^2}\,v_{k-1}(t).
$$
L’angle est entre 0 et $\pi/2$. Sur cet intervalle, $\tan u\geq u$ car la dérivée de $\tan u-u$ est positive ou nulle. On obtient donc la majoration par $x^2|v_{k-1}(t)|/(k\pi)^2$, valable dans toutes les zones.

### Question 26

> [!INDICATION]
> Dans les deux branches, réécrivez $v_k$ comme un produit tronqué et estimez le module de chaque facteur.

#### Solution

Avec $m=\lfloor t\rfloor$, la Q23 montre que $v_k(t)$ est dans les deux cas le produit des premiers $\min(k,m)$ facteurs, multiplié par $x$. Pour chaque indice $j$ du produit, l’argument de Q25 donne
$$
\left|1-\frac{x^2}{((2m+1)\tan(j\pi/(2m+1)))^2}\right|
\leq 1+\frac{x^2}{(j\pi)^2}.
$$
On complète la majoration jusqu’à $k$ avec des facteurs au moins égaux à 1. Par Q2, il vient
$$
|v_k(t)|\leq |x|\exp\left(\sum_{j=1}^k\frac{x^2}{(j\pi)^2}\right).
$$
Pour $m=0$, le produit vide vaut 1, comme dans Q23.

### Question 27

> [!INDICATION]
> Remplacez la somme finie qui contrôle $v_{k-1}$ par une somme numérique indépendante de $k$ et $t$.

#### Solution

La somme $S=\sum_{j\geq1}x^2/(j\pi)^2$ est finie. Par Q25 et Q26, pour $k\geq2$,
$$
\sup_{t\geq0}|v_k(t)-v_{k-1}(t)|
\leq\frac{|x|^3e^S}{(k\pi)^2}.
$$
La série de ces majorants converge. La série des différences converge normalement, donc uniformément. Par télescopage, la suite $(v_k)$ converge uniformément sur $\mathbb R_+$.

### Question 28

> [!INDICATION]
> Dans la première limite, le produit est de longueur fixe. Dans la seconde, l’indice finit par dépasser $t$.

#### Solution

À $k$ fixé, pour $t$ assez grand la première branche s’applique. L’équivalent $\tan u\sim u$ en zéro donne, facteur par facteur,
$$
\begin{aligned}
L_k&=\lim_{t\to+\infty}v_k(t)\\
&=x\prod_{j=1}^k\left(1-\frac{x^2}{(j\pi)^2}\right).
\end{aligned}
$$
À $t$ fixé, pour tout $k>t$ on a $v_k(t)=P_{\lfloor t\rfloor}(x)$. C’est donc sa limite en $k$.

### Question 29

> [!INDICATION]
> Utilisez la convergence uniforme pour contrôler l’écart après les deux passages à la limite.

#### Solution

Notons $v(t)=P_{\lfloor t\rfloor}(x)$. D’après Q24, $v(t)$ tend vers $\sin x$ quand $t$ tend vers l’infini. Par Q28 et l’inégalité $|v_k(t)-v(t)|\leq\lVert v_k-v\rVert_\infty$, le passage à la limite en $t$ donne
$$
|L_k-\sin x|\leq\lVert v_k-v\rVert_\infty.
$$
La Q27 montre que le membre droit tend vers zéro. Pour $x\ne0$, on divise par $x$ afin d’obtenir la convergence du produit partiel et la formule
$$
\sin x=x\prod_{j=1}^{+\infty}\left(1-\frac{x^2}{(j\pi)^2}\right).
$$
Pour $x=0$, tous les facteurs valent 1 et l’égalité est immédiate.

### IV.C — Dérivation et somme des inverses des carrés

### Question 30

> [!INDICATION]
> Appliquez le théorème de dérivation au produit de Q29 sur le segment indiqué. Vérifiez les deux convergences uniformes.

#### Solution

Sur $[-\pi/2,\pi/2]$, posons $f_j(x)=-x^2/(j\pi)^2$. On a $|f_j(x)|\leq1/(4j^2)$. Les facteurs sont strictement positifs et les $f_j$ sont de classe $\mathcal C^1$. Pour les quotients dérivés,
$$
\left|\frac{f_j'(x)}{1+f_j(x)}\right|
=\left|\frac{-2x}{(j\pi)^2-x^2}\right|
\leq\frac4{3\pi j^2}.
$$
Les deux séries sont normalement convergentes. Par Q19, la dérivée logarithmique de leur produit $P$ est la somme des quotients. Pour $x\ne0$, Q29 donne $P(x)=\sin(x)/x$. En dérivant ce quotient puis en divisant par $P(x)$, on obtient
$$
\frac{\cos x}{\sin x}
=\frac1x-\sum_{j=1}^{+\infty}\frac{2x}{(j\pi)^2-x^2}.
$$

### Question 31

> [!INDICATION]
> Après division par $x$, vérifiez que la série à droite peut être évaluée en zéro, puis développez le membre gauche.

#### Solution

La série des fonctions $x\mapsto ((j\pi)^2-x^2)^{-1}$ converge normalement sur le segment, par majoration de chaque terme par $4/(3\pi^2j^2)$. Sa somme est continue en zéro. Par Q30, pour $x\ne0$,
$$
\frac{x\cos x-\sin x}{x^2\sin x}
=-2\sum_{j=1}^{+\infty}\frac1{(j\pi)^2-x^2}.
$$
Le développement au voisinage de zéro donne $x\cos x-\sin x=-x^3/3+o(x^3)$, et $x^2\sin x\sim x^3$. La limite vaut $-1/3$. En identifiant avec la limite du membre droit, on trouve $\sum_{j\geq1}1/j^2=\pi^2/6$.

## Partie V — Autour de la fonction Γ

### V.A — Intégrale et limite d’Euler

### Question 32

> [!INDICATION]
> Sur un segment de paramètres positifs, choisissez des exposants différents de part et d’autre de $t=1$.

#### Solution

Fixons un segment $[a,b]\subset]0,+\infty[$ de paramètres. Pour $0<t\leq1$, $t^{x-1}e^{-t}\leq t^{a-1}$, intégrable puisque $a>0$. Pour $t\geq1$, l’intégrande est majoré par $t^{b-1}e^{-t}$, intégrable par décroissance exponentielle.

L’intégrande est continu en $t>0$ et en $x$. Ces deux bornes fournissent une domination intégrable, indépendante de $x\in[a,b]$. Le théorème de continuité des intégrales à paramètre s’applique. L’intégrale est donc bien définie et continue sur tout $]0,+\infty[$.

### Question 33

> [!INDICATION]
> Intégrez la puissance de $u$ et dérivez celle de $1-u$. Repérez la valeur de départ.

#### Solution

Posons aussi $g_0(x)=1/x$. Pour tout $x>0$, les intégrales convergent au voisinage de 0 puisque $u^{x-1}$ y est intégrable. Pour $n\geq1$, la primitive $u^x/x$ s’annule en 0 et le facteur $(1-u)^n$ s’annule en 1. Une intégration par parties, effectuée d’abord à partir d’une borne positive puis prolongée à 0, donne
$$
g_n(x)=\frac n x g_{n-1}(x+1).
$$
En itérant jusqu’à $g_0(x+n)=1/(x+n)$, on trouve
$$
g_n(x)=\frac{n!}{\prod_{k=0}^n(x+k)}.
$$

### Question 34

> [!INDICATION]
> Prolongez les intégrandes par zéro en dehors de leur intervalle, puis cherchez une domination commune sur la demi-droite.

#### Solution

Pour $x>0$ fixé, définissons sur $]0,+\infty[$ la fonction $F_n(t)$ égale à $t^{x-1}(1-t/n)^n$ si $t\leq n$, et nulle sinon.

À $t$ fixé, Q6 avec $z=-t$ donne $F_n(t)\to t^{x-1}e^{-t}$.

Pour $0<t\leq n$, on a $0\leq 1-t/n\leq e^{-t/n}$. Dans tous les cas,
$$
0\leq F_n(t)\leq t^{x-1}e^{-t}.
$$
Le majorant est intégrable par Q32. Le théorème de convergence dominée donne la limite de l’intégrale de $F_n$, égale à $\Gamma(x)$.

### Question 35

> [!INDICATION]
> Dans l’intégrale de Q34, changez d’échelle pour retrouver l’intervalle de Q33.

#### Solution

En posant $t=nu$, on obtient
$$
\int_0^n t^{x-1}(1-t/n)^n\,\mathrm dt
=n^x g_n(x).
$$
La valeur de Q33 et la limite de Q34 donnent
$$
\Gamma(x)=\lim_{n\to+\infty}\frac{n^x n!}{\prod_{k=0}^n(x+k)}.
$$

### V.B — Formule de réflexion

### Question 36

> [!INDICATION]
> Multipliez les deux approximations de Q35 au même rang, en décalant d’un cran l’un des produits.

#### Solution

Pour $x\in]0,1[$, notons $A_n(x)=n^x n!/\prod_{k=0}^n(x+k)$. En isolant le facteur $x$ dans le dénominateur de $A_n(x)$ et $n+1-x$ dans celui de $A_n(1-x)$, les facteurs restants s’apparient.
$$
A_n(x)A_n(1-x)
=\frac{n}{x(n+1-x)}\prod_{j=1}^n\left(1-\frac{x^2}{j^2}\right)^{-1}.
$$
Par Q29 appliquée à $\pi x$, le produit sans inversion converge vers $\sin(\pi x)/(\pi x)>0$. On peut donc inverser sa limite. Le préfacteur tend vers $1/x$. Par Q35, il vient
$$
\Gamma(x)\Gamma(1-x)=\frac{\pi}{\sin(\pi x)}.
$$

### V.C — Constante d’Euler et produit pour Γ

### Question 37

> [!INDICATION]
> Étudiez la monotonie de la différence entre la somme harmonique et le logarithme. Comparez la somme à une intégrale.

#### Solution

Posons $H_n=\sum_{k=1}^n1/k$. Pour $n\geq1$,
$$
(H_{n+1}-\ln(n+1))-(H_n-\ln n)
=\frac1{n+1}-\int_n^{n+1}\frac{\mathrm dt}{t}\leq0.
$$
D’autre part, $H_n\geq\int_1^{n+1}\mathrm dt/t=\ln(n+1)$, en comparant chaque terme à l’intégrale sur l’intervalle qui le suit. La suite $(H_n-\ln n)$ décroît et est minorée par zéro. Elle converge donc vers un réel $\gamma$, d’où l’asymptotique demandée.

### Question 38

> [!INDICATION]
> Faites apparaître la somme harmonique en multipliant puis en divisant par des exponentielles.

#### Solution

Pour $x>0$, la fraction de Q35 se réécrit
$$
\begin{aligned}
\frac{n^x n!}{\prod_{k=0}^n(x+k)}&=\frac{e^{x(\ln n-H_n)}}{x}\\
&\quad \times\prod_{k=1}^n e^{x/k}\left(1+\frac{x}{k}\right)^{-1}.
\end{aligned}
$$
Par Q37, le préfacteur converge vers $e^{-\gamma x}/x>0$. D’après Q35, le membre gauche converge vers $\Gamma(x)$. En divisant par le préfacteur, les produits partiels convergent donc, et on obtient
$$
\Gamma(x)=\frac{e^{-\gamma x}}{x}
\prod_{k=1}^{+\infty} e^{x/k}\left(1+\frac{x}{k}\right)^{-1}.
$$

## Bilan

- Pour étudier un produit infini, contrôlez d’abord les produits partiels et les différences entre eux.
- Avant de dériver un produit à facteurs positifs, vérifiez la convergence uniforme du produit et de la somme des dérivées logarithmiques.
- Dans un échange de limites, repérez la variable sur laquelle le contrôle doit être uniforme.
