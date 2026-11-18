# Centrale-Supélec PSI — Maths 2 2024 · Corrigé brut

*Corrigé rédigé par IA, non officiel. Signalez toute erreur.*

## I — Convergence de la suite $(a_n)_{n\in\mathbb N^*}$

### Question 1

La différence vaut $1/(n+1)-\ln(1+1/n)$. Les deux développements limités sont

$$
\frac1{n+1}=\frac1n-\frac1{n^2}+O(n^{-3}).
$$

$$
\ln(1+1/n)=\frac1n-\frac1{2n^2}+O(n^{-3}).
$$

Ainsi **$a_{n+1}-a_n\sim-1/(2n^2)$**. La valeur absolue est équivalente au terme d’une série de Riemann convergente. **La série des différences converge absolument.**

### Question 2

La somme des différences pour $1\le k<n$ vaut $a_n-a_1$. Elle converge d’après la question 1, donc $a_n\to\gamma$ pour un certain réel $\gamma$. En revenant à la définition de $a_n$,

$$
\boxed{\sum_{k=1}^n\frac1k=\ln n+\gamma+o(1).}
$$

## II — Application au problème du collectionneur de vignettes

On modélise les paquets successifs par des tirages indépendants, uniformes parmi les $n$ modèles. Dans les questions 3 à 5, $N_k$ désigne, pour un nombre de modèles fixé, le nombre de paquets nécessaires pour posséder $k$ modèles distincts. La variable $N_n$ est le temps requis pour compléter la collection.

### Question 3

Le premier paquet apporte le premier modèle distinct. **$N_1=1$ presque sûrement.**

### Question 4

Pour $n\ge1$ et $m\ge2$, l’événement s’écrit comme l’union disjointe suivante.

$$
C=\bigsqcup_{i\in\{1,\ldots,n\}}\ \bigcap_{j\in\{1,\ldots,m\}} C_j^{(i)}.
$$

Chaque intersection a pour probabilité $n^{-m}$ par indépendance des paquets. On obtient **$\mathbb P(C)=n^{1-m}$**. Cette probabilité vaut notamment $1$ s’il n’existe qu’un seul modèle.

Supposons désormais $n\ge2$. Avoir besoin de plus de $m$ paquets pour découvrir deux modèles revient à n’avoir vu qu’un même modèle dans les $m$ premiers. Pour $m=1$, $N_2>1$ est certain et la formule vaut encore.

$$
\boxed{\mathbb P(N_2>m)=n^{1-m}\qquad(m\ge1).}
$$

### Question 5

La probabilité que $N_2$ vaille $m\ge2$ est la différence des probabilités $\mathbb P(N_2>m-1)$ et $\mathbb P(N_2>m)$.

$$
\boxed{\mathbb P(N_2=m)=(1-1/n)n^{-(m-2)}.}
$$

Elle est nulle pour $m<2$. La queue tend vers zéro, donc le temps est fini presque sûrement. C’est $N_2-1$ qui suit une loi géométrique de paramètre $1-1/n$.

### Question 6

Fixons $1\le k\le n$. Une fois $k-1$ modèles obtenus, conditionnons par leur historique complet jusqu’à cet instant. Chaque paquet suivant est indépendant de cet historique et, jusqu’au premier nouveau modèle, l’ensemble des modèles déjà obtenus ne change pas. Le nombre de modèles nouveaux possibles est $n-k+1$. Pour $r\ge1$, la probabilité conditionnelle de $r-1$ échecs puis un succès vaut $(1-p_k)^{r-1}p_k$, avec

$$
\boxed{p_k=\frac{n-k+1}{n}.}
$$

Pour justifier le conditionnement, on peut fixer un historique précis de longueur finie $s$ où le $(k-1)$-ième modèle a été obtenu au rang $s$. On utilise seulement l’indépendance des paquets de rang supérieur à $s$ et des $s$ premiers. La probabilité calculée est la même pour chacun de ces historiques.

Pour $k=1$, l’historique est vide et le succès est immédiat. Par récurrence, chaque nouveau modèle est atteint presque sûrement, puisque le paramètre est strictement positif.

**Pour $k\ge2$, $\tau_k$ suit la loi géométrique de paramètre $p_k$ sur $\mathbb N^*$.**

Le cas $k=1$ correspond à la loi dégénérée en $1$, qui prolonge la formule au paramètre $p_1=1$.

### Question 7

Les espérances $1/p_k$ sont finies. La formule vaut aussi pour $\tau_1$, constante égale à $1$. Par linéarité de l’espérance, puis par la question 2,

$$
\mathbb E(N_n)=n\sum_{j=1}^n\frac1j.
$$

$$
\boxed{\mathbb E(N_n)=n(\ln n+\gamma+o(1)).}
$$

### Question 8

Pour $r_1,\ldots,r_k\ge1$, l’événement $\tau_i=r_i$ pour $i<k$ ne fixe que des informations sur les $s=\sum_{i<k}r_i$ premiers paquets. Décomposons-le en historiques précis de longueur $s$.

Sur chacun, l’argument de la question 6 donne la même probabilité de l’événement $\tau_k=r_k$, à savoir $\mathbb P(\tau_k=r_k)$.

En sommant sur ces historiques, on obtient la factorisation de la probabilité conjointe au rang $k$ en la probabilité conjointe au rang $k-1$ multipliée par $\mathbb P(\tau_k=r_k)$. En posant $E_k=\{\tau_k=r_k\}$, la récurrence donne ainsi

$$
\mathbb P(E_1\cap\cdots\cap E_n)=\mathbb P(E_1)\cdots\mathbb P(E_n).
$$

Les variables étant discrètes, cette factorisation sur tous les choix de valeurs prouve **leur indépendance mutuelle**.

### Question 9

Chaque variable géométrique a un moment d’ordre deux et une variance $(1-p_k)/p_k^2$. Pour $\tau_1$, cette formule donne bien la variance nulle de la constante. La somme finie a donc un moment d’ordre deux. Par indépendance mutuelle,

$$
\mathbb V(N_n)=\sum_{k=1}^n\frac{1-p_k}{p_k^2}.
$$

Chaque terme est majoré par $1/p_k^2$. La somme de ces majorants vaut $n^2\sum_{j=1}^n1/j^2$. Avec la somme donnée,

$$
\boxed{\mathbb V(N_n)\le\frac{n^2\pi^2}{6}.}
$$

### Question 10

Fixons $\varepsilon>0$. Pour $n\ge2$, le seuil $\varepsilon n\ln n$ est positif. L’inégalité de Bienaymé-Tchebychev s’applique à $N_n$, qui a un moment d’ordre deux.

$$
0\le\mathbb P\bigl(|N_n-\mathbb E(N_n)|>\varepsilon n\ln n\bigr)
\le\frac{\pi^2}{6\varepsilon^2\ln^2 n}.
$$

Le majorant tend vers zéro, donc **la probabilité tend vers zéro**.

### Question 11

D’après la question 7, $\mathbb E(N_n)/(n\ln n)\to1$. Pour $\varepsilon>0$ et $n$ assez grand, l’écart déterministe entre ce quotient et $1$ est au plus $\varepsilon/2$. Par inégalité triangulaire,

$$
\left\{\left|\frac{N_n}{n\ln n}-1\right|>\varepsilon\right\}
\subset
\left\{|N_n-\mathbb E(N_n)|>\tfrac{\varepsilon}{2}n\ln n\right\}.
$$

La probabilité du second événement tend vers zéro par la question 10 appliquée à $\varepsilon/2$. **La probabilité demandée tend donc vers zéro.**

## III — Une première expression intégrale de $\gamma$

### Question 12

Pour $t>0$, la somme partielle de rang $N$ à droite vaut $(1-e^{-(N+1)t})/t$ par télescopage. Comme $e^{-t}\in]0,1[$, **sa limite est $1/t$**.

### Question 13

La série de terme $e^{-(n+1)t}$, pour $t>0$, est géométrique de raison $e^{-t}$ et de somme $e^{-t}/(1-e^{-t})$. En multipliant l’égalité de la question 12 par $e^{-t}$, on obtient la somme de la seconde série. Les deux séries convergent, donc leur différence donne **l’égalité demandée**, avec le terme général

$$
F_n(t)=e^{-(n+1)t}-\frac{e^{-(n+1)t}-e^{-(n+2)t}}{t}.
$$

### Question 14

Pour $t>0$, on a $0\le1-e^{-t}\le t$, par exemple en intégrant $e^{-u}$ sur $[0,t]$.

Donc $F_n(t)$ est positive ou nulle et majorée par $e^{-(n+1)t}$. Elle est continue et intégrable sur $]0,+\infty[$. Grâce à la formule admise,

$$
\int_0^{+\infty}|F_n(t)|\,\mathrm dt
=\frac1{n+1}-\ln\!\left(\frac{n+2}{n+1}\right).
$$

La somme de ces intégrales pour $0\le n\le N$ vaut

$$
\sum_{k=1}^{N+1}\frac1k-\ln(N+2).
$$

Cette quantité tend vers $\gamma$ par la question 2, car $\ln((N+2)/(N+1))\to0$. La série des intégrales des valeurs absolues converge. La série des fonctions converge simplement vers la fonction continue donnée en Q13. Le théorème d’intégration terme à terme s’applique donc et donne à la fois l’intégrabilité et

$$
\boxed{\gamma=\int_0^{+\infty}e^{-t}
\left(\frac1{1-e^{-t}}-\frac1t\right)\,\mathrm dt.}
$$

## IV — Une deuxième expression intégrale de $\gamma$

### Question 15

Pour $t\ne0$, la formule de la somme géométrique donne

$$
\frac{1-(1-t)^n}{t}=\sum_{j=0}^{n-1}(1-t)^j.
$$

Le polynôme de droite vaut $n$ en zéro. **Le quotient se prolonge par continuité avec la valeur $n$ en zéro.**

### Question 16

En intégrant la somme finie de la question 15 sur $[0,1]$ et en utilisant la primitive de chaque puissance, on obtient

$$
\sum_{k=1}^n\frac1k=\int_0^1\frac{1-(1-t)^n}{t}\,\mathrm dt.
$$

Avec $u=nt$, le membre de droite devient l’intégrale de $[1-(1-u/n)^n]/u$ sur $[0,n]$.

On coupe cet intervalle en $0$ à $1$ et $1$ à $n$.

Dans le second morceau, l’intégrale de $1/u$ vaut $\ln n$, qui se retranche dans $a_n$. Ainsi

$$
\boxed{a_n=\int_0^1\frac{1-(1-u/n)^n}{u}\,\mathrm du
-\int_1^n\frac{(1-u/n)^n}{u}\,\mathrm du.}
$$

### Question 17

Pour $x$ fixé et $n>x$, la base est strictement positive. Comme $\ln(1-v)=-v+o(v)$ en zéro, $n\ln(1-x/n)\to-x$. Par continuité de l’exponentielle,

$$
\boxed{(1-x/n)^n\longrightarrow e^{-x}=\int_x^{+\infty}e^{-u}\,\mathrm du.}
$$

L’égalité donnant la limite en exponentielle vaut aussi pour tout $x\ge0$ fixé. On pourra donc l’utiliser sur $[0,1]$.

### Question 18

Pour tout $t\ge1$ fixé, on a $n\ge t$ à partir d’un certain rang. La question 17 donne **$f_n(t)\to e^{-t}/t$**.

### Question 19

Sur $[0,1[$, la fonction $v(t)=\ln(1-t)+t$ vérifie $v(0)=0$ et $v'(t)=-t/(1-t)\le0$. Elle est décroissante, donc **$\ln(1-t)\le-t$ pour tout $t\in[0,1[$**.

### Question 20

Sur $[1,+\infty[$, la fonction $e^{-u}/u$ est continue et vérifie $0\le e^{-u}/u\le e^{-u}$. La majorante est intégrable sur cet intervalle. **L’intégrale converge.**

### Question 21

Pour chaque $n\ge1$, $f_n$ est continue sur $[1,n]$ et vaut zéro sur $]n,+\infty[$. Elle est continue au raccord $n$ car sa valeur et sa limite à droite y sont nulles.

**Elle est intégrable sur $[1,+\infty[$**, étant continue et nulle hors de $[1,n]$.

### Question 22

Pour $1\le u<n$, la question 19 appliquée à $u/n$ donne $(1-u/n)^n\le e^{-u}$. Pour $u\ge n$, $f_n(u)=0$, y compris en $n$. Ainsi

$$
0\le f_n(u)\le\frac{e^{-u}}u.
$$

La majorante est intégrable par la question 20. Les fonctions $f_n$ sont intégrables d’après la question 21, et la limite simple de la question 18 est continue. Le théorème de convergence dominée sur l’intervalle fixe $[1,+\infty[$ fournit

$$
\boxed{\int_1^n\frac{(1-u/n)^n}{u}\,\mathrm du
\longrightarrow\int_1^{+\infty}\frac{e^{-u}}u\,\mathrm du.}
$$

### Question 23

La fonction $(1-e^{-u})/u$ est continue sur $]0,1]$ et tend vers $1$ en zéro, car $1-e^{-u}=u+o(u)$. Son prolongement continu sur $[0,1]$ montre que **l’intégrale converge**.

### Question 24

Pour $0\le v\le t\le1$, la fonction $b_n(v)=(1-v/n)^n$ est continue et dérivable à l’intérieur, avec $b'_n(v)=-(1-v/n)^{n-1}$.

Pour $n=1$ la dérivée vaut $-1$, et pour $n\ge2$ elle est comprise entre $-1$ et $0$.

La fonction est donc décroissante. L’inégalité des accroissements finis donne $|b_n(t)-b_n(0)|\le t$.

Puisque $b_n(0)=1$, la différence $1-b_n(t)$ est positive ou nulle. Ainsi, pour $0<t\le1$,

$$
\boxed{0\le\frac{1-(1-t/n)^n}{t}\le1.}
$$

### Question 25

Sur $]0,1]$, la limite simple du quotient de la question 24 est $(1-e^{-u})/u$ d’après la question 17. Les quotients se prolongent continûment en zéro avec la valeur $1$ d’après la question 15 appliquée à $u/n$. La limite admet le même prolongement par la question 23. La domination uniforme par la fonction constante $1$ sur $[0,1]$ autorise le théorème de convergence dominée.

$$
\boxed{\int_0^1\frac{1-(1-u/n)^n}{u}\,\mathrm du
\longrightarrow\int_0^1\frac{1-e^{-u}}u\,\mathrm du.}
$$

### Question 26

Dans l’égalité de la question 16, $a_n\to\gamma$ d’après la question 2. Les deux intégrales ont pour limites celles des questions 25 et 22, respectivement. Par passage à la limite,

$$
\boxed{\gamma=\int_0^1\frac{1-e^{-u}}u\,\mathrm du
-\int_1^{+\infty}\frac{e^{-u}}u\,\mathrm du.}
$$

## V — Deux autres expressions intégrales de $\gamma$

### Question 27

Pour $x>0$, l’intégrande $t^{x-1}e^{-t}$ est continue et positive sur $]0,+\infty[$. Sur $]0,1]$ elle est majorée par $t^{x-1}$, intégrable puisque $x-1>-1$.

À l’infini, les croissances comparées donnent $t^{x-1}e^{-t/2}\to0$, donc l’intégrande est majorée, pour $t$ assez grand, par $e^{-t/2}$. **L’intégrale définit $\Gamma(x)$ pour tout $x>0$.**

### Question 28

Sur tout segment $[a,b]\subset]0,+\infty[$, l’intégrande et sa dérivée partielle en $x$ sont continues. L’intégrabilité de l’intégrande pour chaque $x$ est acquise par Q27. On a

$$
\partial_x u(x,t)=t^{x-1}\ln(t)e^{-t}.
$$

Sur $]0,1]$, sa valeur absolue est majorée par $t^{a-1}|\ln t|$. Ce majorant est lui-même majoré par une constante fois $t^{a/2-1}$ puisque $t^{a/2}|\ln t|$ est bornée.

Sur $[1,+\infty[$, on majore par $t^{b-1}\ln(t)e^{-t}$, intégrable car $t^{b-1}\ln(t)e^{-t/2}$ est bornée.

La domination est indépendante de $x\in[a,b]$. Le théorème de dérivation sous le signe intégral, sur de tels segments autour de tout $x>0$, montre que $\Gamma$ est de classe $\mathcal C^1$ sur $]0,+\infty[$ et

$$
\boxed{\Gamma'(x)=\int_0^{+\infty}t^{x-1}\ln(t)e^{-t}\,\mathrm dt.}
$$

### Question 29

Pour $x>0$, intégrons par parties sur un segment $[\eta,T]\subset]0,+\infty[$.

$$
\int_\eta^T t^x e^{-t}\,\mathrm dt
=[-t^x e^{-t}]_\eta^T+x\int_\eta^T t^{x-1}e^{-t}\,\mathrm dt.
$$

Les deux intégrales convergent par Q27. Le crochet tend vers zéro, car $t^x e^{-t}$ tend vers zéro aux deux bornes. **On obtient $\Gamma(x+1)=x\Gamma(x)$.**

### Question 30

Comme $\Gamma(x)>0$ pour $x>0$, on peut prendre le logarithme de la formule de Weierstrass en passant à la limite des logarithmes des produits partiels positifs. On trouve

$$
\ln\Gamma(x)=-\ln x-\gamma x
+\sum_{n=1}^{+\infty}\left(\frac{x}{n}-\ln(1+x/n)\right).
$$

Pour tout $x>0$, la série converge, puisque son terme général est équivalent à $x^2/(2n^2)$ par développement limité. Chaque terme est de classe $\mathcal C^1$ et sa dérivée vaut

$$
\frac1n-\frac1{n+x}=\frac{x}{n(n+x)}.
$$

Sur tout segment $[a,b]\subset]0,+\infty[$, cette dérivée est positive et majorée par $b/n^2$. La série des dérivées converge normalement, donc uniformément sur chaque segment. Le théorème de dérivation terme à terme donne

$$
\boxed{\frac{\Gamma'(x)}{\Gamma(x)}
=-\frac1x-\gamma+\sum_{n=1}^{+\infty}
\left(\frac1n-\frac1{n+x}\right).}
$$

### Question 31

On a $\Gamma(1)=\int_0^{+\infty}e^{-t}\,\mathrm dt=1$. En $x=1$, la série de la question 30 est télescopique, de somme $1$. Ainsi **$\Gamma'(1)=-\gamma$**.

En dérivant la formule de la question 29, on obtient $\Gamma'(x+1)=\Gamma(x)+x\Gamma'(x)$. En $x=1$, cela donne **$\Gamma'(2)=1-\gamma$**.

### Question 32

D’après les questions 28 et 31, $-\gamma=\int_0^{+\infty}\ln(u)e^{-u}\,\mathrm du$, avec intégrabilité absolue. Le changement de variable $t=e^{-u}$, d’abord sur des segments, donne $u=-\ln t$ et $\mathrm dt=-e^{-u}\,\mathrm du$. En passant aux bornes, on obtient

$$
\boxed{\gamma=-\int_0^1\ln(-\ln t)\,\mathrm dt.}
$$

## VI — Recherche d’une valeur approchée de $\gamma$

### Question 33

D’après la question 26, on peut reporter le point de coupure de $1$ à $A$ par les relations de Chasles, avec des intégrales orientées si $A<1$.

Les deux nouveaux morceaux entre $1$ et $A$ s’ajoutent dans l’expression avec l’intégrande $[(1-e^{-u})+e^{-u}]/u=1/u$. Leur somme vaut $\ln A$. Ainsi

$$
\boxed{\gamma=-\ln A+\int_0^A\frac{1-e^{-u}}u\,\mathrm du
-\int_A^{+\infty}\frac{e^{-u}}u\,\mathrm du.}
$$

### Question 34

Pour $0\le u\le A$, le prolongement continu de $(1-e^{-u})/u$ est la somme de la série entière

$$
\sum_{k=0}^{+\infty}\frac{(-1)^k u^k}{(k+1)!}.
$$

La série converge normalement sur $[0,A]$. En effet, pour les majorants $A^k/(k+1)!$, le rapport successif $A/(k+2)$ tend vers zéro, donc leur série converge par le critère de d’Alembert. On peut intégrer terme à terme. La série numérique ainsi obtenue converge absolument, ses termes en valeur absolue étant majorés par $A\cdot A^k/(k+1)!$. Sa somme est

$$
\boxed{\sum_{k=0}^{+\infty}\frac{(-1)^kA^{k+1}}{(k+1)(k+1)!}
=\int_0^A\frac{1-e^{-u}}u\,\mathrm du.}
$$

### Question 35

Pour $x>0$, les fonctions $e^{-u}/u$ et $e^{-u}/u^2$ sont continues, positives et majorées par des constantes fois $e^{-u}$ sur $[x,+\infty[$.

Une intégration par parties sur $[x,T]$, suivie du passage à la limite avec $e^{-T}/T\to0$, donne

$$
\boxed{\int_x^{+\infty}\frac{e^{-u}}u\,\mathrm du
=\frac{e^{-x}}x-\int_x^{+\infty}\frac{e^{-u}}{u^2}\,\mathrm du.}
$$

### Question 36

Pour $p=1,2,3$, avec $I_p(x)=\int_x^{+\infty}e^{-u}u^{-p}\,\mathrm du$, le même calcul donne

$$
I_p(x)=\frac{e^{-x}}{x^p}-pI_{p+1}(x).
$$

Les intégrales convergent par comparaison avec $x^{-p}e^{-u}$ et les crochets à l’infini s’annulent. En remplaçant successivement $I_2$ puis $I_3$ dans l’expression de $I_1$,

$$
I_1(x)=\frac{e^{-x}}x-\frac{e^{-x}}{x^2}
+\frac{2e^{-x}}{x^3}-6I_4(x).
$$

On obtient **$R(x)=x^2-x+2$**.

### Question 37

Notons $S_n$ la somme de la question 34 jusqu’à l’indice $n$. Les questions 33, 34 et 36 donnent

$$
\gamma=-\ln A+S_\infty-\frac{R(A)e^{-A}}{A^3}+6I_4(A).
$$

Le signe devant $R(A)e^{-A}/A^3$ dans la valeur absolue imprimée doit donc être **positif**. Pour majorer le reste de série, notons $b_k=A^{k+1}/[(k+1)(k+1)!]$. On a $b_k\to0$. Pour $k\ge n+1$ avec $n>A+1$, le quotient

$$
\frac{b_{k+1}}{b_k}=\frac{A(k+1)}{(k+2)^2}<1
$$

montre la décroissance des termes en valeur absolue. Le reste de la série alternée vaut au plus $b_{n+1}\le b_n$. De plus, $0\le I_4(A)\le e^{-A}/A^4$ par comparaison sous l’intégrale. L’inégalité triangulaire donne donc la version corrigée.

$$
\boxed{
\left|\gamma-S_n+\frac{R(A)e^{-A}}{A^3}+\ln A\right|
\le \frac{A^{n+1}}{(n+1)(n+1)!}+\frac{6e^{-A}}{A^4}.
}
$$

Avec le signe imprimé et $A=4$, le membre de gauche tend, quand $n\to+\infty$, vers $\left|6I_4(4)-2R(4)e^{-4}/4^3\right|$.

Par l’estimation sur $I_4(4)$ et $R(4)=14$, cette limite est strictement supérieure à $6e^{-4}/4^4$, limite du membre de droite. La version imprimée échoue donc pour $n$ assez grand.

## VII — Étude d’une série entière aux bornes de son disque ouvert de convergence

### VII.A — Rayon de convergence et première expression de la somme

#### Question 38

Pour $n\ge2$, le quotient $\ln(n+1)/\ln n$ tend vers $1$, car $\ln(n+1)-\ln n=\ln(1+1/n)\to0$ et $\ln n\to+\infty$.

Pour $x\ne0$, le quotient des valeurs absolues des termes successifs tend donc vers $|x|$.

La série converge absolument si $|x|<1$ et diverge si $|x|>1$.

En $x=1$ et en $x=-1$, les termes ne tendent pas vers zéro. **Le rayon vaut $1$ et le domaine réel est $]-1,1[$.**

### VII.B — Étude de $f$ en $1$

#### Question 39

Pour $0\le x<1$, tous les termes sont positifs ou nuls. Pour $n\ge2$, $\ln n\ge\ln2$, ce qui donne

$$
f(x)\ge\frac{(\ln2)x^2}{1-x}.
$$

La borne inférieure tend vers $+\infty$. **$f(x)\to+\infty$ lorsque $x\to1^-$.**

#### Question 40

Si $H_n=\sum_{k=1}^n1/k$, alors $1\le H_n\le n$. Pour $|x|<1$, la série $\sum n|x|^n$ converge, donc $\sum H_nx^n$ converge absolument.

Pour $|x|\ge1$, le terme ne tend pas vers zéro. **Le rayon est $1$.**

#### Question 41

Pour $|x|<1$, les deux séries indiquées sont absolument convergentes.

Le produit de Cauchy de $\sum_{j\ge0}x^j$ et $\sum_{k\ge1}x^k/k$ a pour coefficient de $x^n$ le nombre $H_n$ pour les degrés strictement positifs, et zéro en degré zéro.

La série géométrique a pour somme $1/(1-x)$. La primitive de la série géométrique sur $]-1,1[$, prise nulle en zéro, donne $\sum_{k\ge1}x^k/k=-\ln(1-x)$. Ainsi

$$
\boxed{g(x)=\frac{\ln(1-x)}{x-1}\qquad(|x|<1).}
$$

#### Question 42

Par la question 2, $(H_n-\ln n)_{n\ge1}$ est convergente, donc bornée en valeur absolue par un réel $M>0$. Pour $0\le x<1$, l’inégalité triangulaire appliquée aux séries convergentes donne

$$
|f(x)-g(x)|\le\frac{M}{1-x}.
$$

#### Question 43

Pour $0<x<1$, $g(x)=-\ln(1-x)/(1-x)>0$. D’après la question 42,

$$
\left|\frac{f(x)}{g(x)}-1\right|
\le \frac{M}{-\ln(1-x)}.
$$

Ce majorant tend vers zéro. Donc **$f(x)\sim g(x)$ lorsque $x\to1^-$**.

### VII.C — Étude de $f$ en $-1$

#### Question 44

Par développement limité, $-\ln(1-1/n)=1/n+1/(2n^2)+o(n^{-2})$. Ainsi $c_n\sim 1/(2n^2)$. La série $\sum |c_n|$ converge par comparaison, d’où la convergence absolue de $\sum c_nx^n$ pour $|x|\le1$.

Si $|x|>1$, la valeur absolue de son terme général est équivalente à $|x|^n/(2n^2)$ et tend vers $+\infty$. **Le rayon est $1$ et le domaine réel de $h$ est $[-1,1]$.**

#### Question 45

Pour $n\ge2$, on peut écrire $c_n=\ln n-\ln(n-1)-1/n$. Avec $c_1=-1$, le télescopage donne $\sum_{k=1}^n c_k=\ln n-H_n$. Par la question 2, **la somme de la série vaut $-\gamma$**.

#### Question 46

Sur $[-1,1]$, on a $\sup |c_n x^n|=|c_n|$. Ces majorants sont sommables d’après la question 44. La série converge donc normalement, donc uniformément.

Ses termes sont continus sur ce segment, d’où la continuité de $h$ sur $[-1,1]$. **En particulier, $h$ est continue en $1$ et $h(1)=-\gamma$.**

#### Question 47

Pour $k\ge2$, on décompose $c_k$ comme à la question 45. Le terme $k=1$ de la somme vaut $1$ et appartient à la somme harmonique alternée. La contribution logarithmique est donc

$$
\ln\left(\prod_{j=1}^{p}\frac{2j}{2j-1}\,
\prod_{j=1}^{p-1}\frac{2j}{2j+1}\right).
$$

Le second produit est le premier divisé par $2p$. Le premier vaut $2^{2p}(p!)^2/(2p)!$, en séparant facteurs pairs et impairs dans $(2p)!$. En notant $W_p$ le produit des deux facteurs, on obtient

$$
\boxed{\begin{gathered}
W_p=\frac{2^{4p}(p!)^4}{2p\,((2p)!)^2}\\
\sum_{k=1}^{2p}(-1)^k c_k=\ln W_p+\sum_{k=1}^{2p}\frac{(-1)^{k-1}}k.
\end{gathered}}
$$

#### Question 48

Pour $|x|<1$, la convergence absolue permet de décaler les indices dans $f$. Par les coefficients calculés à la question 45 et la formule logarithmique de la question 41,

$$
h(x)=(1-x)f(x)+\ln(1-x).
$$

Par continuité de $h$ en $-1$ démontrée à la question 46, la limite de $f$ en $-1^+$ est $(h(-1)-\ln 2)/2$. Il reste à déterminer le premier terme.

Posons $J_m=\int_0^{\pi/2}\sin^m(t)\,\mathrm dt$. On a $J_0=\pi/2$ et $J_1=1$.

Pour $m\ge2$, intégrons par parties en écrivant $\sin^m t=\sin^{m-1}t\,\sin t$. Le crochet est nul aux bornes et $\cos^2 t=1-\sin^2 t$, d’où $mJ_m=(m-1)J_{m-2}$. Les produits obtenus en itérant sont

$$
\begin{gathered}
J_{2p}=\frac{\pi}{2}\,\frac{(2p)!}{2^{2p}(p!)^2}\\
J_{2p-1}=\frac{2^{2p-1}p!(p-1)!}{(2p)!}.
\end{gathered}
$$

Comme $0\le\sin t\le1$, $J_{2p+1}\le J_{2p}\le J_{2p-1}$. En outre, $J_{2p+1}/J_{2p-1}=2p/(2p+1)\to1$. Par encadrement, $J_{2p-1}/J_{2p}\to1$. Le quotient des formules précédentes montre que

$$
\frac{2^{4p}(p!)^4}{2p\,((2p)!)^2}
=\frac{\pi}{2}\,\frac{J_{2p-1}}{J_{2p}}
\longrightarrow\frac{\pi}{2}.
$$

Dans l’identité de la question 47, le membre de gauche tend vers $h(-1)$ par convergence absolue et la somme alternée tend vers $\ln 2$ par le rappel de l’énoncé. On obtient $h(-1)=\ln(\pi/2)+\ln2$, donc

$$
\boxed{\lim_{x\to-1^+} f(x)=\frac12\ln\!\left(\frac{\pi}{2}\right).}
$$

FIN
