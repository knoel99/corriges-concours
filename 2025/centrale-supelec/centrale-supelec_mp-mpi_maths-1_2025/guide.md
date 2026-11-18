# Centrale-Supélec MP/MPI — Mathématiques 1 2025 · Corrigé guidé

*Corrigé rédigé par IA, non officiel. Signalez toute erreur.*

## Présentation du sujet

Ce problème commun aux filières MP et MPI comporte quarante questions pour une épreuve de quatre heures. Il combine l'arithmétique de première année, les estimations de suites, les séries de fonctions et l'intégration. L'objectif est d'obtenir des approximations rationnelles assez fines pour démontrer l'irrationalité de $\zeta(2)$.

La partie A encadre le nombre de premiers inférieurs à un réel. La partie B étudie le plus petit commun multiple des premiers entiers. Sa majoration asymptotique fait appel au théorème des nombres premiers admis par l'énoncé. La partie C construit un critère d'irrationalité, l'applique à un exemple décimal et montre les limites des sommes partielles de $\zeta(2)$.

La partie D transforme une intégrale itérée en série, puis en combinaison de fractions. La partie E combine cette étude arithmétique et une majoration analytique de l'intégrale. Le point délicat est de trouver à la fois une erreur assez petite et un contrôle des dénominateurs.

Une première lecture permet de repérer des points d'entrée autonomes, notamment Q3–Q7, Q14–Q18, Q20–Q22, Q24–Q25 et Q31. Gardez du temps pour la seconde moitié du problème. Une progression possible réserve environ une heure à A, 35 minutes à B, 35 à C, 40 à D, 55 à E et 15 à la relecture.

## Partie A — Un encadrement de la fonction $\pi$

Les coefficients binomiaux fournissent des entiers dont la valeur et les facteurs premiers peuvent être contrôlés séparément. Ce double contrôle mène aux deux bornes de la fonction de comptage.

### I — Calculs préliminaires


### Question 1

> [!INDICATION]
> Écrivez le coefficient binomial à l'aide d'un produit d'entiers et d'un quotient par $n!$.

> [!INDICATION]
> Pour la minoration, utilisez le lemme de Gauss pour chaque premier de l'intervalle. Pour la majoration, cherchez deux termes égaux dans la somme binomiale.

#### Solution

L'entier $B=\binom{2n+1}{n}$ vérifie $n! B=(n+2)\cdots(2n+1)$.

Tout premier $p$ compris entre $n+2$ et $2n+1$ divise le second membre et est premier avec $n!$.

Le lemme de Gauss donne $p\mid B$.

Ces nombres premiers étant distincts, leur produit divise $B$.

Les coefficients aux deux rangs distincts $n$ et $n+1$ dans le développement de $(1+1)^{2n+1}$ valent tous deux $B$. On a donc $2B\leq 2^{2n+1}$, ce qui donne **$\prod_{n+2\leq p\leq 2n+1}p\leq B\leq 4^n$**, le produit portant sur les nombres premiers.

> [!JURY]
> Les rapports MP et MPI recommandent le lemme de Gauss pour la minoration. Montrer que chaque premier divise le coefficient est plus précis que de comparer directement les deux produits.

### Question 2

> [!INDICATION]
> Utilisez une récurrence forte sur l'entier qui borne les facteurs premiers du produit.

> [!INDICATION]
> Au rang pair, traitez séparément le plus petit cas. Au rang impair, séparez les facteurs en utilisant la coupure de Q1.

#### Solution

Notons $P(m)=\prod_{p\leq m}p$ sur les premiers. Le produit vide vaut $1$, donc $P(1)=1<4$, et $P(2)=2<4^2$.

Supposons la majoration acquise à tous les rangs strictement inférieurs à $m\geq 3$. Si $m=2n\geq4$, il est composé, donc $P(m)=P(m-1)<4^{m-1}<4^m$. Si $m=2n+1$, on a $n+1<m$. La Q1 et l'hypothèse de récurrence donnent
$$
\begin{aligned}
P(m)&=P(n+1)\prod_{n+2\leq p\leq 2n+1}p\\
&<4^{n+1}4^n\\
&=4^m.
\end{aligned}
$$
**La récurrence forte établit $P(m)<4^m$ pour tout $m\geq1$.**

> [!PIEGE]
> L'hérédité au rang impair utilise une borne au rang $n+1$. Une hypothèse de récurrence forte la fournit, et le produit vide vaut $1$.

### Question 3

> [!INDICATION]
> Ramenez le seuil réel à un seuil entier et comparez les deux exposants.

#### Solution

Pour un nombre premier $p$, $p\leq x$ équivaut à $p\leq\lfloor x\rfloor$. D'après Q2 et la croissance de l'exponentielle de base $4$,
$$
\boxed{\prod_{p\leq x}p=P(\lfloor x\rfloor)<4^{\lfloor x\rfloor}\leq4^x.}
$$

### Question 4

> [!INDICATION]
> Repérez le plus grand coefficient de la ligne de rang $2n$ en étudiant le rapport entre coefficients consécutifs.

> [!INDICATION]
> Pour obtenir $2n$ termes à majorer, regroupez les deux termes extrêmes avant de comparer au terme central.

#### Solution

Posons $C_n=\binom{2n}{n}$.

Parmi les $2n+1$ termes de la somme binomiale, $C_n$ est maximal.

En effet, le rapport du coefficient suivant au coefficient de rang $k$ vaut $(2n-k)/(k+1)$. Il est au moins égal à $1$ pour $k<n$ et inférieur à $1$ pour $k\geq n$.

Les deux termes extrêmes, de somme $2$, peuvent être regroupés en un seul terme majoré par $C_n$, puisque $C_n\geq\binom{2n}{1}=2n$. Ainsi $4^n\leq 2n C_n$. La somme binomiale contient d'autres termes strictement positifs que $C_n$, d'où $C_n<4^n$. Finalement,
$$
\boxed{\frac{4^n}{2n}\leq\binom{2n}{n}<4^n.}
$$

> [!PIEGE]
> Majorer chacun des coefficients par le coefficient central fournit immédiatement un facteur $2n+1$. Le regroupement des deux extrêmes permet d'atteindre le facteur demandé.

### Question 5

> [!INDICATION]
> Une puissance $p^k$ contribue à la valuation du produit une fois pour chaque facteur multiple de cette puissance.

> [!INDICATION]
> Faites le compte pour chaque $k$ en utilisant les multiples de $p^k$ compris entre $1$ et $n$.

#### Solution

Par additivité de la valuation sur les produits, $v_p(n!)=\sum_{j=1}^n v_p(j)$.

Dans cette somme, chaque entier $j$ compte une fois pour chaque puissance $p^k$ qui le divise, où $k\geq1$.

En changeant l'ordre de ce dénombrement fini, on compte pour chaque $k$ les multiples de $p^k$ compris entre $1$ et $n$.

Ainsi,
$$
\boxed{v_p(n!)=\sum_{k\geq1}\left\lfloor\frac{n}{p^k}\right\rfloor.}
$$
Les termes sont nuls lorsque $p^k>n$. Pour $n=0$, la somme est nulle et $0!=1$.

> [!METHODE]
> Le même dénombrement peut se lire par lignes ou par colonnes. Dans une lecture, on décompose la valuation de chaque facteur. Dans l'autre, on compte les multiples de chaque puissance première.

### Question 6

> [!INDICATION]
> Écrivez la valuation comme une différence de valuations de factorielles avec Q5.

> [!INDICATION]
> Pour étudier $\lfloor 2u\rfloor-2\lfloor u\rfloor$, faites apparaître la partie fractionnaire de $u$.

#### Solution

Le coefficient $C_n$ vérifie $(n!)^2 C_n=(2n)!$. Par Q5,
$$
v_p(C_n)=\sum_{j\geq1}\left(\left\lfloor\frac{2n}{p^j}\right\rfloor-2\left\lfloor\frac{n}{p^j}\right\rfloor\right).
$$
Écrire $u=\lfloor u\rfloor+\theta$ avec $0\leq\theta<1$ donne $\lfloor2u\rfloor-2\lfloor u\rfloor=\lfloor2\theta\rfloor\in\{0,1\}$.

Les termes d'indice $j$ pour lesquels $p^j>2n$ sont nuls.

La valuation vaut donc au plus le nombre d'entiers $j\geq1$ tels que $p^j\leq2n$.

**Si $p^k\mid C_n$, on a bien $p^k\leq2n$**, y compris pour $k=0$.

### II — Majoration de $\pi(x)$


### Question 7

> [!INDICATION]
> Écrivez le premier produit comme le second multiplié par les facteurs omis.

#### Solution

Le premier produit est le second multiplié par le produit des premiers $p\leq\sqrt n$. Chaque facteur est supérieur à $1$ et le produit vide vaut $1$. **Le premier produit est donc supérieur ou égal au second.**

### Question 8

> [!INDICATION]
> Comptez les facteurs de Q7 strictement supérieurs à $\sqrt n$, puis appliquez Q2.

> [!INDICATION]
> Traitez aussi le cas où il n'y a aucun facteur dans ce produit.

#### Solution

Il y a $m=\pi(n)-\pi(\sqrt n)$ facteurs dans le second produit de Q7, chacun supérieur à $\sqrt n$. Ce produit est donc au moins $(\sqrt n)^m$, y compris quand $m=0$. Par Q7 et Q2,
$$
\boxed{n^{(\pi(n)-\pi(\sqrt n))/2}<4^n.}
$$

### Question 9

> [!INDICATION]
> Étudiez le minimum de $t\mapsto\sqrt t-\ln t$ avant de prendre le logarithme dans Q8.

> [!INDICATION]
> Testez la seconde inégalité imprimée sur un petit entier. Pour retrouver la constante de l'encadrement annoncé en tête de partie, estimez le terme logarithmique provenant de Q8 à l'aide de quelques termes positifs de la série exponentielle.

#### Solution

Les premiers au plus $\sqrt n$ sont parmi les entiers de $1$ à $\lfloor\sqrt n\rfloor$, d'où $\pi(\sqrt n)\leq\sqrt n$.

La dérivée de $t\mapsto\sqrt t-\ln t$ sur $[2,+\infty[$ est $(\sqrt t-2)/(2t)$. Le minimum est en $4$ et vaut $2-\ln4>0$. Ainsi, **$\sqrt n<n/\ln n$**.

La seconde inégalité imprimée comporte une inversion de fraction. Par exemple, en $n=8$ elle demanderait $4\leq(\ln8)/2$, ce qui est faux. La majoration à établir est celle de la partie A, $\pi(n)\leq4n/\ln n$, confirmée par les rapports MP et MPI.

Par Q8 et la croissance de $\ln$,
$$
\pi(n)<\pi(\sqrt n)+\frac{2n\ln4}{\ln n}.
$$
Il faut une borne plus fine que $\ln4<2$. La série de l'exponentielle à l'argument $3/2$ donne
$$
e^{3/2}>1+\frac32+\frac98+\frac9{16}>4.
$$
Ainsi $\ln4<3/2$. En utilisant $\pi(\sqrt n)<n/\ln n$ dans la majoration précédente, on obtient **$\pi(n)\leq4n/\ln n$**.

> [!JURY]
> Les rapports MP et MPI corrigent la fraction et relèvent que $\ln4<2$ ne suffit qu'à obtenir la constante $5$. La preuve ci-dessus établit une borne plus précise et produit la constante demandée.

### Question 10

> [!INDICATION]
> Appliquez Q9 à $\lfloor x\rfloor$. Avant d'utiliser la croissance fournie, vérifiez que cet entier appartient au bon intervalle.

#### Solution

Pour $x\geq3$, on a $x\geq\lfloor x\rfloor\geq3>e$ et $\pi(x)=\pi(\lfloor x\rfloor)$.

La dérivée de $t/\ln t$ vaut $(\ln t-1)/(\ln t)^2$, positive ou nulle pour $t\geq e$.

La majoration de Q9 s'applique à $\lfloor x\rfloor$, puis cette croissance donne
$$
\boxed{\pi(x)\leq 4\frac{\lfloor x\rfloor}{\ln\lfloor x\rfloor}\leq4\frac{x}{\ln x}.}
$$

> [!JURY]
> Les rapports rappellent qu'il faut vérifier $x\geq\lfloor x\rfloor\geq e$ pour appliquer la croissance de $t/\ln t$. Ici, le seuil entier $3$ donne cet encadrement.

### III — Minoration de $\pi(x)$


### Question 11

> [!INDICATION]
> Décomposez le coefficient binomial en facteurs premiers. Bornez chaque puissance maximale avec Q6, puis comptez les premiers concernés.

#### Solution

Par Q6, chaque facteur $p^{v_p(C_n)}$ dans la décomposition de $C_n$ est au plus $2n$. Les nombres premiers qui y interviennent sont donc au plus $2n$. En incluant ceux de valuation nulle, on a au plus $\pi(2n)$ facteurs, d'où
$$
\boxed{\binom{2n}{n}\leq(2n)^{\pi(2n)}.}
$$

### Question 12

> [!INDICATION]
> Ramenez la première inégalité à une comparaison entre $2^n$ et $2n$ et établissez-la par récurrence.

> [!INDICATION]
> Combinez ensuite Q4 et Q11 avant de prendre le logarithme.

#### Solution

On a $2^n\geq2n$ pour $n\geq1$. Il y a égalité pour $n=1$ et, dès que $2^n\geq2n$, on a $2^{n+1}\geq4n\geq2(n+1)$. En prenant les logarithmes, $n\ln2\geq\ln(2n)$. On en déduit
$$
\frac{2n\ln2}{\ln(2n)}-1\geq \frac{n\ln2}{\ln(2n)}.
$$
Par Q4 et Q11, $4^n/(2n)\leq(2n)^{\pi(2n)}$. Le logarithme puis la division par $\ln(2n)>0$ donnent
$$
\begin{aligned}
\pi(2n)&\geq \frac{2n\ln2}{\ln(2n)}-1\\
&\geq \boxed{\frac{n\ln2}{\ln(2n)}}.
\end{aligned}
$$

### Question 13

> [!INDICATION]
> Posez $n=\lfloor x/2\rfloor$ et rendez explicites les bornes sur $n$ et $2n$. Dans Q12, comparez séparément le numérateur et le dénominateur à des expressions en $x$.

#### Solution

Posons $n=\lfloor x/2\rfloor\geq1$. On a $2n\leq x$ et $n>x/2-1\geq x/6$ lorsque $x\geq3$. Puisque $\pi$ et $\ln$ sont croissantes, Q12 donne
$$
\begin{aligned}
\pi(x)&\geq\pi(2n)\\
&\geq \frac{n\ln2}{\ln(2n)}\\
&\geq \boxed{\frac{\ln2}{6}\frac{x}{\ln x}}.
\end{aligned}
$$

> [!PIEGE]
> Les parties entières ne commutent pas avec la multiplication par deux. L'encadrement $x/2-1<n\leq x/2$ suffit.

## Partie B — Une majoration d’un PPCM

L'intersection de sous-groupes additifs définit le PPCM. La décomposition en puissances premières permet de comparer sa croissance à celle d'une suite géométrique.

### I — Une première majoration


### Question 14

> [!INDICATION]
> L'intersection hérite de la structure des ensembles de multiples. Montrez qu'elle possède un plus petit élément positif.

> [!INDICATION]
> Divisez un élément de l'intersection par ce candidat et étudiez le reste.

#### Solution

Chaque $a_i\mathbb Z$ est un sous-groupe additif de $\mathbb Z$, donc leur intersection $G$ aussi.

Elle contient le produit positif des $a_i$.

Soit $d$ le plus petit entier strictement positif de $G$.

Pour $b\in G$, la division euclidienne par $d$ donne $b=dq+r$ avec $0\leq r<d$.

Comme $r=b-dq$ appartient à $G$, la minimalité de $d$ impose $r=0$.

On a donc $G\subset d\mathbb Z$.

L'inclusion inverse vient de $d\in G$.

Tout générateur naturel de $G$ est positif et est le plus petit élément positif de $G$.

Ainsi **il existe un unique $d\in\mathbb N$ tel que $G=d\mathbb Z$**.

### Question 15

> [!INDICATION]
> Traduisez la divisibilité simultanée par une appartenance à l'intersection de Q14.

#### Solution

Être divisible par tous les $a_i$ équivaut à appartenir à $G=d\mathbb Z$. Ses éléments strictement positifs sont les $kd$ avec $k\geq1$. **Le plus petit d'entre eux est $d$.**

> [!JURY]
> Les rapports rappellent que la comparaison usuelle entre un entier positif et son multiple exige que le multiple soit non nul. On considère ici les éléments strictement positifs de l'intersection.

### Question 16

> [!INDICATION]
> Pour les petits rangs, repérez quelles contraintes de divisibilité s'impliquent. Pour le cas général, cherchez un multiple commun positif construit en multipliant les entiers concernés.

#### Solution

On obtient **$d_2=2$, $d_3=6$ et $d_4=12$**.

En effet, $2$ et $3$ sont premiers entre eux, puis un multiple commun à $3$ et $4$ est un multiple de $12$, déjà divisible par $2$.

Comme $n!$ est un multiple commun strictement positif des entiers de $1$ à $n$, Q15 donne **$d_n\leq n!$**.

### II — Une majoration plus fine


### Question 17

> [!INDICATION]
> Montrez que tous les entiers de la liste divisent le produit proposé en comparant les valuations.

> [!INDICATION]
> Pour la divisibilité inverse, vérifiez que chaque puissance première maximale est l'un des entiers dont on prend le PPCM.

#### Solution

Posons $D=\prod_{p\leq n}p^{k_p}$, avec $p$ premier.

Pour tout entier $1\leq m\leq n$, la condition $p^{v_p(m)}\leq m\leq n$ implique $v_p(m)\leq k_p$.

Par décomposition en facteurs premiers, $m\mid D$, donc $d_n\mid D$ par Q14.

Pour chaque $p\leq n$, le nombre $p^{k_p}$ appartient à $\{1,\ldots,n\}$ et divise $d_n$. Ces puissances étant deux à deux premières entre elles, $D\mid d_n$. Ainsi,
$$
\boxed{d_n=\prod_{p\leq n}p^{k_p}.}
$$

### Question 18

> [!INDICATION]
> Prenez le logarithme de $p^k\leq n$, puis bornez chacun des facteurs de Q17 par un même nombre.

#### Solution

La condition $p^k\leq n$ équivaut à $k\leq\ln n/\ln p$ puisque $p>1$.

Donc **$k_p=\lfloor\ln n/\ln p\rfloor$**.

Chacun des $\pi(n)$ facteurs du produit de Q17 est au plus $n$.

Ainsi **$d_n\leq n^{\pi(n)}$**.

### Question 19

> [!INDICATION]
> Prenez le logarithme de la borne de Q18. Le théorème admis donne une limite après division par $n$.

> [!INDICATION]
> Comparez cette limite avec le logarithme de la base visée avant de revenir à l'exponentielle.

#### Solution

Le théorème des nombres premiers admis dans l'énoncé donne $\pi(n)\ln n/n\to1$. On a $\ln3>1$ puisque $3>e$. Il existe donc $N\geq2$ tel que, pour $n\geq N$, $\pi(n)\ln n\leq n\ln3$. Par Q18 et croissance de l'exponentielle,
$$
\boxed{d_n\leq e^{\pi(n)\ln n}\leq3^n.}
$$

> [!JURY]
> Les rapports signalent que l'équivalence de deux exposants ne donne pas celle de leurs exponentielles. Une inégalité entre les exposants obtenue à partir d'une limite suffit ici.

## Partie C — Un critère d’irrationalité

Le critère ramène l'irrationalité à l'impossibilité pour une suite d'entiers non nuls de tendre vers zéro. La taille de l'erreur se mesure après multiplication par le dénominateur.

### Question 20

> [!INDICATION]
> Supposez la limite rationnelle. Multipliez l'écart par le dénominateur fixe de cette limite et par le dénominateur de l'approximation.

> [!INDICATION]
> Utilisez à la fois la non-nullité et le caractère entier des écarts ainsi obtenus.

#### Solution

Si $\alpha=a/b$ est rationnel, avec $a\in\mathbb N$ et $b\in\mathbb N^\ast$, l'entier $a q_n-b p_n$ est non nul pour tout $n$. L'hypothèse de petit $o$ impose pourtant
$$
|a q_n-b p_n|=bq_n\left|\alpha-\frac{p_n}{q_n}\right|\longrightarrow0.
$$
Cela contredit $|a q_n-bp_n|\geq1$. **$\alpha$ est irrationnel.**

> [!METHODE]
> Transformer une approximation rationnelle en entier non nul permet d'utiliser une minoration uniforme. L'écriture de la limite sous la forme d'une fraction irréductible est facultative.

### Question 21

> [!INDICATION]
> Pour écrire une somme partielle sous forme de quotient, choisissez comme dénominateur la plus grande puissance de dix qui y intervient.

> [!INDICATION]
> Dans le reste, majorez la somme en autorisant toutes les puissances négatives de dix à partir du premier exposant qui apparaît.

#### Solution

Comme $n!\geq n$ pour $n\geq1$, la série qui définit $\beta$ converge par comparaison à $\sum_{n\geq1}10^{-n}$.

Posons $q_n=10^{n!}$ et $p_n=\sum_{j=1}^n 10^{n!-j!}$ pour $n\geq1$.

Ces entiers positifs donnent la somme partielle $p_n/q_n$.

Le reste $R_n=\beta-p_n/q_n$ est strictement positif.

Les factorielles $j!$ pour $j>n$ forment une suite strictement croissante d'entiers qui commence à $(n+1)!$.

Ainsi,
$$
\begin{aligned}
0<R_n&\leq\sum_{k=(n+1)!}^{\infty}10^{-k}\\
&=\frac{10}{9}\,10^{-(n+1)!}.
\end{aligned}
$$
Donc $q_nR_n\leq(10/9)10^{-n\,n!}\to0$. Les sommes partielles convergent vers $\beta$ et lui sont strictement inférieures. Les hypothèses de Q20 sont satisfaites après un décalage d'indice. **$\beta$ est irrationnel.**

### Question 22

> [!INDICATION]
> Pour chaque $k\leq n$, comparez la divisibilité de $k^2$ avec celle de $k$ dans la définition de $d_n$.

#### Solution

La série $\sum_{k\geq1}1/k^2$ est une série de Riemann convergente. Pour $k\leq n$, $k\mid d_n$, donc $k^2\mid d_n^2$. En posant $q_n=d_n^2$ et $p_n=\sum_{k=1}^n(d_n/k)^2\in\mathbb N^\ast$, on obtient
$$
\boxed{\sum_{k=1}^n\frac1{k^2}=\frac{p_n}{q_n}.}
$$

### Question 23

> [!INDICATION]
> Le critère exige une estimation de l'erreur multipliée par le dénominateur, même si les sommes partielles convergent.

> [!INDICATION]
> Pour minorer le reste, comparez la série et l'intégrale de $t^{-2}$. Minorez aussi le PPCM par un des entiers dont il est multiple.

#### Solution

La fonction positive $t\mapsto t^{-2}$ est décroissante, donc
$$
\zeta(2)-\frac{p_n}{q_n}\geq\int_{n+1}^{+\infty}\frac{\mathrm dt}{t^2}=\frac1{n+1}.
$$
Comme $n\mid d_n$, on a $q_n=d_n^2\geq n^2$. Le produit de l'erreur par $q_n$ est donc minoré par $n^2/(n+1)$, qui tend vers $+\infty$. **L'hypothèse de petit $o$ de Q20 échoue pour ces suites.**

> [!PIEGE]
> Les approximations convergent, mais le dénominateur croît trop vite par rapport à l'erreur. Testez exactement le produit qui intervient dans le critère.

## Partie D — Calcul d’une intégrale double

Le développement géométrique du noyau conduit à une série à termes positifs. Hors de la diagonale, les sommes partielles de cette série se calculent par télescopage.

### I — Une intégrale double


### Question 24

> [!INDICATION]
> Pour $y$ fixé, cherchez une borne inférieure strictement positive de $1-xy$ sur tout le segment en $x$.

#### Solution

Pour $0<y<1$ et $0\leq x\leq1$, le dénominateur $1-xy$ est au moins $1-y>0$. Le quotient est continu sur le segment $[0,1]$, donc **il y est intégrable**.

### Question 25

> [!INDICATION]
> Pour la continuité en $y$, fixez une borne supérieure locale strictement inférieure à $1$.

> [!INDICATION]
> Pour l'intégrabilité en $y$, majorez avant d'intégrer en $x$ en ne gardant que le noyau, puis étudiez les deux extrémités.

#### Solution

Pour chaque $x\in[0,1]$, l'intégrande est continue en $y$ sur $]0,1[$.

Pour $0<y<b<1$, sa valeur absolue est majorée sur $[0,1]$ par la constante intégrable $1/(1-b)$.

Le théorème de continuité des intégrales à paramètre s'applique sur $]0,b[$ pour tout $b<1$.

Ainsi **$f_{r,s}$ est continue sur $]0,1[$**.

De plus, pour $0<y<1$,
$$
\begin{aligned}
0\leq f_{r,s}(y)&\leq \int_0^1 \frac{\mathrm dx}{1-xy}\\
&=-\frac{\ln(1-y)}{y}.
\end{aligned}
$$
Cette dernière fonction tend vers $1$ en $0$.

Pour $y\geq1/2$, elle est majorée par $-2\ln(1-y)$, intégrable au voisinage de $1$.

Ainsi **$f_{r,s}$ est intégrable sur $]0,1[$**.

> [!JURY]
> Les rapports signalent les difficultés de domination. La continuité se prouve avec une borne locale en paramètre, tandis que l'intégrabilité globale requiert une autre estimation.

### Question 26

> [!INDICATION]
> Pour $y$ fixé, développez le noyau géométrique et établissez une majoration uniforme en $x$.

> [!INDICATION]
> Pour la seconde interversion, calculez la série des intégrales absolues des termes en $y$ et comparez-la à une série de Riemann.

#### Solution

Pour $y\in]0,1[$ fixé, la série géométrique conduit à
$$
\frac{x^r y^s}{1-xy}=\sum_{k=0}^\infty x^{r+k}y^{s+k}.
$$
Sur $[0,1]$ ses termes continus sont majorés par $y^k$. La convergence normale permet d'intégrer terme à terme en $x$ et donne $f_{r,s}(y)=\sum_{k\geq0} y^{s+k}/(r+k+1)$.

Pour intégrer en $y$, les termes sont positifs et continus. La somme est continue sur $]0,1[$ d'après Q25 et les intégrales des valeurs absolues valent $1/((r+k+1)(s+k+1))$. Leur série converge par comparaison à $\sum_{k\geq0}(k+1)^{-2}$. Le théorème d'intégration terme à terme sur $]0,1[$ donne
$$
\boxed{J_{r,s}=\sum_{k=0}^\infty\frac{1}{(r+k+1)(s+k+1)}.}
$$

> [!METHODE]
> Les deux interversions s'appuient sur des critères distincts. En $x$, une majoration uniforme sur le segment suffit. En $y$, la série des intégrales absolues est convergente.

### II — Une écriture sous forme de quotients


### Question 27

> [!INDICATION]
> Réduisez la différence de fractions au même dénominateur et examinez le numérateur.

#### Solution

Pour $r>s$, la réduction au même dénominateur donne
$$
\frac{1}{s+k+1}-\frac{1}{r+k+1}
=\frac{r-s}{(s+k+1)(r+k+1)}.
$$
La division par $r-s>0$ donne **l'identité demandée**.

### Question 28

> [!INDICATION]
> Substituez l'identité de Q27 dans les sommes partielles de la série de Q26.

#### Solution

On applique Q27 dans chaque terme de la série convergente de Q26. On obtient
$$
\boxed{J_{r,s}=\frac1{r-s}\sum_{k=0}^\infty
\left(\frac1{s+k+1}-\frac1{r+k+1}\right).}
$$

### Question 29

> [!INDICATION]
> Travaillez d'abord sur les sommes jusqu'à un entier fini.

> [!INDICATION]
> Après le changement d'indice, repérez les deux blocs qui ne se compensent pas et bornez celui dont les indices tendent vers l'infini.

#### Solution

Pour $N\geq r-s$, en décalant les indices dans les sommes finies,
$$
\begin{aligned}
&\sum_{k=0}^N\left(\frac1{s+k+1}-\frac1{r+k+1}\right)\\
&\qquad=\sum_{k=s+1}^{r}\frac1k-\sum_{k=s+N+2}^{r+N+1}\frac1k.
\end{aligned}
$$
La seconde somme a $r-s$ termes et est majorée par $(r-s)/(s+N+2)$, qui tend vers zéro. D'après Q28,
$$
\boxed{J_{r,s}=\frac1{r-s}\sum_{k=s+1}^r\frac1k.}
$$

> [!JURY]
> Les rapports insistent sur le calcul à borne finie. Scinder l'expression en deux séries harmoniques donnerait deux séries divergentes.

### Question 30

> [!INDICATION]
> Dans Q29, les dénominateurs sont des produits de deux facteurs. Vérifiez que chacun de ces facteurs divise le même PPCM.

#### Solution

Pour $s+1\leq k\leq r$, on a $k\mid d_r$ et $r-s\mid d_r$. Ainsi
$$
(r-s)k\mid d_r^2.
$$
Par Q29, $d_r^2J_{r,s}$ est donc un entier positif. On peut prendre **$p_{r,s}=d_r^2 J_{r,s}$ et $q_{r,s}=d_r^2$**. Ce dernier divise aussi le carré de tout $d_m$ pour $m\geq r$, puisque $d_r\mid d_m$ par Q14.

> [!PIEGE]
> Deux entiers divisant $d_r$ ont un produit qui divise $d_r^2$. Le produit n'est pas nécessairement un diviseur de $d_r$.

## Partie E — Une démonstration de l’irrationalité de $\zeta(2)$

Il faut obtenir deux descriptions du même nombre. L'écriture par polynomialité contrôle son dénominateur et les intégrations par parties donnent une expression adaptée à la majoration.

### Question 31

> [!INDICATION]
> Développez la puissance par le binôme de Newton avant de dériver.

> [!INDICATION]
> Après division par $n!$, reconnaissez la valeur d'un coefficient binomial dans le facteur obtenu en dérivant le monôme.

#### Solution

Le binôme de Newton donne $x^n(1-x)^n=\sum_{k=0}^n(-1)^k\binom nk x^{n+k}$. Après $n$ dérivations et division par $n!$,
$$
\boxed{P_n(x)=\sum_{k=0}^n(-1)^k\binom nk\binom{n+k}{n}x^k.}
$$
Tous les coefficients sont entiers et celui de $x^n$ vaut $(-1)^n\binom{2n}n\ne0$. **Le degré est $n$.**

### Question 32

> [!INDICATION]
> Avant de développer les polynômes, vérifiez que la définition intégrale de la partie D reste valable avec des indices nuls ou inversés.

> [!INDICATION]
> Développez le numérateur, utilisez la linéarité de chaque intégrale et séparez les indices égaux.

#### Solution

La définition de $J_{r,s}$ par l'intégrale itérée se prolonge à tous les entiers $r,s\geq0$. En effet, les preuves de Q24 et Q25 n'utilisent que les bornes $0\leq x^r\leq1$ et $0\leq y^s\leq1$ sur les intervalles considérés. La preuve de Q26 reste également valable, puisqu'elle utilise les mêmes deux séries majorantes. Elle montre en particulier que $J_{r,s}=J_{s,r}$ et $J_{0,0}=\zeta(2)$.

Pour $y<1$, l'intégrande de $I_n$ est continue en $x$ sur $[0,1]$.

Son intégrale intérieure est une combinaison linéaire finie de fonctions $f_{r,s}$ intégrables en $y$, d'après le développement des deux polynômes et la linéarité.

Cela prouve l'existence de $I_n$.

En intégrant cette combinaison et en séparant la diagonale,
$$
\boxed{I_n
=\sum_{\substack{0\leq r,s\leq n\\r\ne s}}a_r b_s J_{r,s}
+\sum_{r=0}^n a_r b_r J_{r,r}.}
$$

> [!METHODE]
> Lorsque les indices introduits dépassent le domaine initial d'une notation, revenez à la définition et vérifiez les hypothèses qui servent vraiment dans la preuve.

### Question 33

> [!INDICATION]
> Séparez les termes de Q32 entre diagonale et hors diagonale. Utilisez la symétrie pour remettre les indices dans l'ordre utile.

> [!INDICATION]
> Pour chaque terme rationnel, comparez son dénominateur possible à $d_n^2$.

#### Solution

Pour $r\ne s$, posons $m=\max(r,s)$ et $u=\min(r,s)$.

Par symétrie et Q27–Q30, dont les calculs restent valables si $u=0$, on a $d_m^2J_{r,s}\in\mathbb Z$.

Comme $m\leq n$, $d_m\mid d_n$, donc $d_n^2 J_{r,s}\in\mathbb Z$.

Pour $0\leq r\leq n$, Q26 donne $J_{r,r}=\zeta(2)-\sum_{k=1}^r1/k^2$, y compris pour $r=0$. Par Q22, chaque somme finie ainsi retranchée a pour dénominateur possible $d_n^2$. Les coefficients $a_r,b_s$ étant entiers, Q32 montre que
$$
\boxed{I_n=\frac{p_n+q_n\zeta(2)}{d_n^2},\qquad p_n,q_n\in\mathbb Z.}
$$
Ici le coefficient de $\zeta(2)$ au numérateur est $q_n=d_n^2\sum_{r=0}^n a_r b_r$.

### Question 34

> [!INDICATION]
> Reportez le symbole de dérivation sur le noyau en intégrant plusieurs fois par parties.

> [!INDICATION]
> Pour les termes de bord, utilisez l'ordre des zéros de $x^n(1-x)^n$. Calculez séparément la dérivée d'ordre $n$ du noyau.

#### Solution

Posons $U(x)=x^n(1-x)^n$.

Comme $0$ et $1$ sont des racines d'ordre $n$ de $U$, $U^{(j)}$ s'annule aux deux extrémités pour $0\leq j<n$.

Pour $0<y<1$, le noyau $(1-xy)^{-1}$ est de classe $\mathcal C^\infty$ sur $[0,1]$.

Sa dérivée d'ordre $n$ en $x$ vaut $n!y^n/(1-xy)^{n+1}$, par récurrence sur $n$.

Après $n$ intégrations par parties, tous les termes de bord s'annulent.

Ainsi,
$$
\begin{aligned}
\int_0^1\frac{P_n(x)}{1-xy}\,\mathrm dx
&=\frac{(-1)^n}{n!}\int_0^1 U(x)\frac{\mathrm d^n}{\mathrm dx^n}\frac{1}{1-xy}\,\mathrm dx\\
&=\boxed{(-y)^n\int_0^1\frac{x^n(1-x)^n}{(1-xy)^{n+1}}\,\mathrm dx}.
\end{aligned}
$$

> [!JURY]
> Les rapports relèvent que la multiplicité des racines aux deux extrémités est rarement indiquée. Elle justifie l'annulation de tous les termes de bord.

### Question 35

> [!INDICATION]
> Réintroduisez le facteur dépendant seulement de $y$ et intégrez l'identité de Q34.

#### Solution

On multiplie l'identité de Q34 par $(1-y)^n$ et on intègre en $y$. L'intégrabilité de la fonction résultante découle de l'identité des intégrales intérieures et de Q32. On obtient
$$
\boxed{I_n=(-1)^n\int_0^1\int_0^1
\frac{x^n(1-x)^n y^n(1-y)^n}{(1-xy)^{n+1}}\,\mathrm dx\,\mathrm dy.}
$$

### Question 36

> [!INDICATION]
> À produit $xy$ fixé, comparez $x+y$ à $2\sqrt{xy}$.

> [!INDICATION]
> Posez $u=\sqrt{xy}$, simplifiez le majorant, puis cherchez son maximum par dérivation.

#### Solution

Posons $u=\sqrt{xy}\in]0,1[$. L'inégalité $x+y\geq2u$ résulte de $(\sqrt x-\sqrt y)^2\geq0$. Ainsi $(1-x)(1-y)\leq(1-u)^2$. Le quotient demandé est donc au plus
$$
F(u)=\frac{u^2(1-u)}{1+u}.
$$
Sur $]0,1[$,
$$
F'(u)=\frac{2u(1-u-u^2)}{(1+u)^2}.
$$
Le facteur $1-u-u^2$ décroît et s'annule en $v=(\sqrt5-1)/2$.

Ainsi $F$ atteint son maximum en $v$.

Les identités $1-v=v^2$ et $v(1+v)=1$ donnent $F(v)=v^5$.

En réduisant la puissance par $v^2=1-v$, on obtient $v^5=5v-3$.

Finalement,
$$
\boxed{\frac{x(1-x)y(1-y)}{1-xy}\leq \frac{5\sqrt5-11}{2}.}
$$

> [!METHODE]
> La quantité $1-xy$ dépend seulement du produit. À produit fixé, le numérateur est maximal lorsque $x=y$. Cette réduction permet d'utiliser une étude de fonction d'une seule variable.

### Question 37

> [!INDICATION]
> Séparez une puissance $n$ et un facteur $(1-xy)^{-1}$ dans l'intégrande de Q35. Reliez l'intégrale de ce dernier facteur à Q26 étendue aux indices nuls.

#### Solution

Posons $\gamma=(5\sqrt5-11)/2$. L'intégrande positive de Q35 est le produit de $(1-xy)^{-1}$ par la puissance $n$ du quotient de Q36, qui est majorée par $\gamma^n$. L'intégrale itérée du noyau $(1-xy)^{-1}$ vaut $J_{0,0}=\zeta(2)$ par Q32. Par conséquent,
$$
\boxed{|I_n|\leq\gamma^n\zeta(2).}
$$

### Question 38

> [!INDICATION]
> Examinez le signe de l'intégrande de Q35 sur un carré intérieur pour en déduire si $|I_n|$ s'annule. Reliez ensuite le membre central de l'inégalité à $|I_n|$ grâce à Q33.

> [!INDICATION]
> Combiner Q19 et Q37 avant d'employer la comparaison numérique admise.

#### Solution

L'intégrande de Q35 est continue et strictement positive sur le carré intérieur $[1/4,3/4]^2$. Son minimum y est strictement positif, donc $|I_n|>0$. Par Q33, le module demandé vaut $d_n^2 |I_n|$. Pour $n\geq N$ comme dans Q19, $d_n^2\leq9^n$. Q37 et l'inégalité numérique admise $9\gamma\leq 5/6$ donnent
$$
\boxed{0<|p_n+\zeta(2)q_n|\leq \zeta(2)(5/6)^n.}
$$

> [!JURY]
> Les rapports signalent que beaucoup de copies omettent la stricte positivité. Elle est indispensable pour Q39 et vient de l'intégrande positive à l'intérieur du carré.

### Question 39

> [!INDICATION]
> Faites apparaître des approximations rationnelles de $\zeta(2)$ à partir de Q38.

> [!INDICATION]
> Pour appliquer Q20, contrôlez le signe des deux entiers et vérifiez la condition sur l'erreur après multiplication par le dénominateur.

#### Solution

Les entiers $q_n$ sont non nuls par l'énoncé. Posons $Q_n=|q_n|$ et $A_n=-\operatorname{sgn}(q_n)p_n$. D'après Q38,
$$
0< Q_n\left|\zeta(2)-\frac{A_n}{Q_n}\right|
=|p_n+\zeta(2)q_n|\longrightarrow0.
$$
Comme $Q_n\geq1$, les fractions tendent vers $\zeta(2)>0$, donc $A_n>0$ pour $n$ assez grand. Après suppression d'un nombre fini d'indices et réindexation, Q20 s'applique à ces deux suites d'entiers strictement positifs. **$\zeta(2)$ est irrationnel.**

> [!JURY]
> Les rapports demandent de revenir explicitement à Q20. Dans la solution ci-dessus, on normalise les signes pour obtenir des suites d'entiers positifs à partir d'un certain rang.

### Question 40

> [!INDICATION]
> Supposez $\pi$ rationnel et utilisez la stabilité de $\mathbb Q$ par les opérations qui interviennent dans l'identité admise.

#### Solution

Si $\pi$ était rationnel, $\pi^2/6$ serait rationnel par stabilité de $\mathbb Q$ par produit et division par $6$. Cela contredirait Q39 puisque $\zeta(2)=\pi^2/6$ dans cette question. **$\pi$ est irrationnel.**

> [!JURY]
> Les rapports attendent que le lien entre les deux irrationalités soit justifié. La stabilité des rationnels donne une preuve par l'absurde en une phrase.

## Bilan

- Pour encadrer un entier, combinez une expression analytique de sa taille et sa décomposition en facteurs premiers. Un coefficient binomial fournit ici les deux points de vue.
- Pour appliquer un critère d'irrationalité, mesurez l'erreur après multiplication par le dénominateur et établissez que cette quantité est strictement positive.
- Pour intégrer une série sur un intervalle, distinguez la convergence sur un segment et la sommabilité des intégrales absolues. En présence d'un télescopage, conservez une borne finie jusqu'à l'identification du reste.
- Une intégration par parties itérée demande un contrôle de toutes les dérivées qui apparaissent au bord. Les multiplicités des zéros donnent ici ce contrôle.
- Q5–Q6, Q17–Q20 et Q25–Q26 constituent de bons exercices de reprise indépendamment de la démonstration finale.
