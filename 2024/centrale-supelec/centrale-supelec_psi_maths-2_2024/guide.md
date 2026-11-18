# Centrale-Supélec PSI — Maths 2 2024 · Corrigé guidé

*Corrigé rédigé par IA, non officiel. Signalez toute erreur.*

## Présentation du sujet

Le sujet « Autour de la série harmonique et de la constante d’Euler » comporte 48 questions en quatre heures, calculatrice autorisée. Le fil conducteur est la limite de la différence entre somme harmonique et logarithme. Le problème enchaîne une application probabiliste, des représentations intégrales, une approximation avec contrôle d’erreur et l’étude d’une série entière.

- **I–II.** Établir l’existence de la constante d’Euler, puis étudier l’attente de nouvelles vignettes et la concentration du temps de collecte.
- **III–IV.** Obtenir deux intégrales par interversion série-intégrale, puis par convergence dominée.
- **V–VI.** Étudier la fonction Gamma, déplacer une borne de coupure et donner un encadrement d’erreur pour une approximation.
- **VII.** Exploiter une série entière auxiliaire pour analyser les deux limites au bord de l’intervalle de convergence.

Les notions mobilisées relèvent des programmes PCSI et PSI. Commencez par les questions courtes de calcul et par celles qui débloquent plusieurs étapes, notamment Q1–Q2, Q12–Q13, Q19–Q21 et Q27. Le jury relève en particulier la difficulté de Q11 et les hypothèses souvent omises dans les applications des théorèmes de convergence. Avant d’invoquer un théorème, identifiez l’objet étudié et l’intervalle sur lequel il est défini. Q17 et Q37 comportent des erreurs signalées dans le rapport. La solution de Q17 donne la limite attendue et une écriture intégrale possible. Celle de Q37 explicite et démontre l’inégalité corrigée.

[Sujet officiel](https://www.concours-centrale-supelec.fr/sites/default/files/2025-01/M071.pdf) · [Rapport PSI 2024, section Maths 2](https://www.concours-centrale-supelec.fr/sites/default/files/documents/Rapport%20CCS%202024%20PSI_0.pdf) · [BO PSI](https://www.education.gouv.fr/bo/21/Hebdo31/ESRS2111748A.htm) · [BO PCSI](https://www.education.gouv.fr/bo/21/Special1/ESRS2035780A.htm)

## I — Convergence de la suite $(a_n)_{n\in\mathbb N^*}$

La différence entre deux termes consécutifs révèle l’ordre du terme dominant après compensation.

### Question 1

> [!INDICATION]
> Développez les deux termes de la différence au même ordre. Vérifiez quel ordre subsiste après soustraction.

> [!INDICATION]
> Posez $u=1/n$. Les développements de $(1+u)^{-1}$ et de $\ln(1+u)$ n’interviennent pas de la même façon puisque le premier est multiplié par $u$.

#### Solution

La différence vaut $1/(n+1)-\ln(1+1/n)$. Les deux développements limités sont

$$
\frac1{n+1}=\frac1n-\frac1{n^2}+O(n^{-3}).
$$

$$
\ln(1+1/n)=\frac1n-\frac1{2n^2}+O(n^{-3}).
$$

Ainsi **$a_{n+1}-a_n\sim-1/(2n^2)$**. La valeur absolue est équivalente au terme d’une série de Riemann convergente. **La série des différences converge absolument.**

> [!JURY]
> Le rapport relève le remplacement abusif de $1/(n+1)$ par $1/n$ à l’ordre deux. Pour conclure sur la série, appliquez le critère de comparaison aux valeurs absolues ou établissez un signe constant à partir d’un certain rang.

### Question 2

> [!INDICATION]
> Reliez les sommes partielles des différences à un terme de la suite.

#### Solution

La somme des différences pour $1\le k<n$ vaut $a_n-a_1$. Elle converge d’après la question 1, donc $a_n\to\gamma$ pour un certain réel $\gamma$. En revenant à la définition de $a_n$,

$$
\boxed{\sum_{k=1}^n\frac1k=\ln n+\gamma+o(1).}
$$

> [!PIEGE]
> La convergence du terme général des différences vers zéro ne suffit pas. C’est la convergence des sommes partielles télescopiques qui donne la limite.

## II — Application au problème du collectionneur de vignettes

La probabilité de recevoir un nouveau modèle dépend du nombre déjà obtenu. Le calcul doit expliquer pourquoi l’identité de ces modèles et leur ordre d’apparition ne changent pas le paramètre.

On modélise les paquets successifs par des tirages indépendants, uniformes parmi les $n$ modèles. Dans les questions 3 à 5, $N_k$ désigne, pour un nombre de modèles fixé, le nombre de paquets nécessaires pour posséder $k$ modèles distincts. La variable $N_n$ est le temps requis pour compléter la collection.

### Question 3

> [!INDICATION]
> Demandez-vous combien de paquets il faut ouvrir pour voir un premier modèle.

#### Solution

Le premier paquet apporte le premier modèle distinct. **$N_1=1$ presque sûrement.**

> [!METHODE]
> Une loi déterminée par une unique valeur certaine est une loi à part entière. Précisez à quoi correspond la variable.

### Question 4

> [!INDICATION]
> Décomposez l’événement selon le numéro du modèle répété.

> [!INDICATION]
> Pour relier les deux événements, formulez ce qui doit s’être passé dans chacun des premiers achats si le deuxième modèle distinct manque encore.

#### Solution

Pour $n\ge1$ et $m\ge2$, l’événement s’écrit comme l’union disjointe suivante.

$$
C=\bigsqcup_{i\in\{1,\ldots,n\}}\ \bigcap_{j\in\{1,\ldots,m\}} C_j^{(i)}.
$$

Chaque intersection a pour probabilité $n^{-m}$ par indépendance des paquets. On obtient **$\mathbb P(C)=n^{1-m}$**. Cette probabilité vaut notamment $1$ s’il n’existe qu’un seul modèle.

Supposons désormais $n\ge2$. Avoir besoin de plus de $m$ paquets pour découvrir deux modèles revient à n’avoir vu qu’un même modèle dans les $m$ premiers. Pour $m=1$, $N_2>1$ est certain et la formule vaut encore.

$$
\boxed{\mathbb P(N_2>m)=n^{1-m}\qquad(m\ge1).}
$$

> [!JURY]
> Le jury demande de distinguer les intersections pour un modèle donné et leur union disjointe. Traitez à part le cas d’un achat, absent de la première consigne.

### Question 5

> [!INDICATION]
> Exprimez l’événement où le temps est exactement égal à un entier par différence de deux événements de queue.

#### Solution

La probabilité que $N_2$ vaille $m\ge2$ est la différence des probabilités $\mathbb P(N_2>m-1)$ et $\mathbb P(N_2>m)$.

$$
\boxed{\mathbb P(N_2=m)=(1-1/n)n^{-(m-2)}.}
$$

Elle est nulle pour $m<2$. La queue tend vers zéro, donc le temps est fini presque sûrement. C’est $N_2-1$ qui suit une loi géométrique de paramètre $1-1/n$.

> [!METHODE]
> Déterminez d’abord le support. Ensuite, vérifiez que la différence fait intervenir les deux événements emboîtés dans le bon ordre.

### Question 6

> [!INDICATION]
> Figez l’historique au moment où le modèle précédent a été obtenu. Comptez les modèles qui constitueraient un succès.

#### Solution

Fixons $1\le k\le n$. Une fois $k-1$ modèles obtenus, conditionnons par leur historique complet jusqu’à cet instant. Chaque paquet suivant est indépendant de cet historique et, jusqu’au premier nouveau modèle, l’ensemble des modèles déjà obtenus ne change pas. Le nombre de modèles nouveaux possibles est $n-k+1$. Pour $r\ge1$, la probabilité conditionnelle de $r-1$ échecs puis un succès vaut $(1-p_k)^{r-1}p_k$, avec

$$
\boxed{p_k=\frac{n-k+1}{n}.}
$$

Pour justifier le conditionnement, on peut fixer un historique précis de longueur finie $s$ où le $(k-1)$-ième modèle a été obtenu au rang $s$. On utilise seulement l’indépendance des paquets de rang supérieur à $s$ et des $s$ premiers. La probabilité calculée est la même pour chacun de ces historiques.

Pour $k=1$, l’historique est vide et le succès est immédiat. Par récurrence, chaque nouveau modèle est atteint presque sûrement, puisque le paramètre est strictement positif.

**Pour $k\ge2$, $\tau_k$ suit la loi géométrique de paramètre $p_k$ sur $\mathbb N^*$.**

Le cas $k=1$ correspond à la loi dégénérée en $1$, qui prolonge la formule au paramètre $p_1=1$.

> [!JURY]
> Le rapport relève l’oubli de l’indépendance des paquets et des paramètres impossibles. Le paramètre d’une attente géométrique doit correspondre à une probabilité de succès.

### Question 7

> [!INDICATION]
> Utilisez la linéarité avant de chercher une approximation. Transformez ensuite l’ordre de sommation des paramètres.

#### Solution

Les espérances $1/p_k$ sont finies. La formule vaut aussi pour $\tau_1$, constante égale à $1$. Par linéarité de l’espérance, puis par la question 2,

$$
\mathbb E(N_n)=n\sum_{j=1}^n\frac1j.
$$

$$
\boxed{\mathbb E(N_n)=n(\ln n+\gamma+o(1)).}
$$

> [!JURY]
> Le jury rappelle qu’il n’est pas nécessaire de démontrer l’indépendance pour calculer l’espérance d’une somme, ni de redémontrer l’espérance géométrique du cours.

### Question 8

> [!INDICATION]
> Considérez des durées précises pour toutes les étapes déjà achevées. Quel nombre de paquets ont-elles consommé ?

> [!INDICATION]
> Sur chaque historique compatible de cette longueur, comparez la probabilité du prochain temps d’attente à sa probabilité sans condition.

#### Solution

Pour $r_1,\ldots,r_k\ge1$, l’événement $\tau_i=r_i$ pour $i<k$ ne fixe que des informations sur les $s=\sum_{i<k}r_i$ premiers paquets. Décomposons-le en historiques précis de longueur $s$.

Sur chacun, l’argument de la question 6 donne la même probabilité de l’événement $\tau_k=r_k$, à savoir $\mathbb P(\tau_k=r_k)$.

En sommant sur ces historiques, on obtient la factorisation de la probabilité conjointe au rang $k$ en la probabilité conjointe au rang $k-1$ multipliée par $\mathbb P(\tau_k=r_k)$. En posant $E_k=\{\tau_k=r_k\}$, la récurrence donne ainsi

$$
\mathbb P(E_1\cap\cdots\cap E_n)=\mathbb P(E_1)\cdots\mathbb P(E_n).
$$

Les variables étant discrètes, cette factorisation sur tous les choix de valeurs prouve **leur indépendance mutuelle**.

> [!JURY]
> Le rapport distingue indépendance mutuelle et indépendance deux à deux. La preuve doit factoriser une probabilité portant sur toutes les durées.

### Question 9

> [!INDICATION]
> Réutilisez les moments des lois géométriques et l’indépendance mutuelle. Comparez ensuite à la série numérique donnée.

#### Solution

Chaque variable géométrique a un moment d’ordre deux et une variance $(1-p_k)/p_k^2$. Pour $\tau_1$, cette formule donne bien la variance nulle de la constante. La somme finie a donc un moment d’ordre deux. Par indépendance mutuelle,

$$
\mathbb V(N_n)=\sum_{k=1}^n\frac{1-p_k}{p_k^2}.
$$

Chaque terme est majoré par $1/p_k^2$. La somme de ces majorants vaut $n^2\sum_{j=1}^n1/j^2$. Avec la somme donnée,

$$
\boxed{\mathbb V(N_n)\le\frac{n^2\pi^2}{6}.}
$$

> [!METHODE]
> La variance est additive sous indépendance, sous réserve que les variables aient un moment d’ordre deux. L’existence de ce moment précède la majoration.

### Question 10

> [!INDICATION]
> Cherchez une inégalité qui borne la probabilité d’un écart à la moyenne en fonction de la variance.

#### Solution

Fixons $\varepsilon>0$. Pour $n\ge2$, le seuil $\varepsilon n\ln n$ est positif. L’inégalité de Bienaymé-Tchebychev s’applique à $N_n$, qui a un moment d’ordre deux.

$$
0\le\mathbb P\bigl(|N_n-\mathbb E(N_n)|>\varepsilon n\ln n\bigr)
\le\frac{\pi^2}{6\varepsilon^2\ln^2 n}.
$$

Le majorant tend vers zéro, donc **la probabilité tend vers zéro**.

> [!JURY]
> Le rapport demande de faire apparaître les deux côtés de l’encadrement, y compris la positivité de la probabilité.

### Question 11

> [!INDICATION]
> Décomposez l’écart à la constante autour du quotient de l’espérance, puis transformez cette estimation en inclusion d’événements.

> [!INDICATION]
> Réservez une fraction de $\varepsilon$ à l’écart déterministe. Cherchez alors quel seuil utiliser dans Q10.

#### Solution

D’après la question 7, $\mathbb E(N_n)/(n\ln n)\to1$. Pour $\varepsilon>0$ et $n$ assez grand, l’écart déterministe entre ce quotient et $1$ est au plus $\varepsilon/2$. Par inégalité triangulaire,

$$
\left\{\left|\frac{N_n}{n\ln n}-1\right|>\varepsilon\right\}
\subset
\left\{|N_n-\mathbb E(N_n)|>\tfrac{\varepsilon}{2}n\ln n\right\}.
$$

La probabilité du second événement tend vers zéro par la question 10 appliquée à $\varepsilon/2$. **La probabilité demandée tend donc vers zéro.**

> [!JURY]
> Le rapport souligne les passages à la limite injustifiés. Distinguez la fluctuation aléatoire, traitée à la question 10, de l’écart déterministe contrôlé par Q7.

## III — Une première expression intégrale de $\gamma$

Écrivez d’abord chaque série à $t$ fixé, puis étudiez l’intégrabilité en $t$ avant d’intervertir les opérations.

### Question 12

> [!INDICATION]
> Commencez par une somme finie. Les exponentielles s’y annulent par paires.

#### Solution

Pour $t>0$, la somme partielle de rang $N$ à droite vaut $(1-e^{-(N+1)t})/t$ par télescopage. Comme $e^{-t}\in]0,1[$, **sa limite est $1/t$**.

> [!JURY]
> La limite du dernier terme du télescopage doit être justifiée pour chaque valeur du paramètre.

### Question 13

> [!INDICATION]
> Reconnaissez une série géométrique dans une partie du membre de droite. La seconde partie relève de la question précédente.

#### Solution

La série de terme $e^{-(n+1)t}$, pour $t>0$, est géométrique de raison $e^{-t}$ et de somme $e^{-t}/(1-e^{-t})$. En multipliant l’égalité de la question 12 par $e^{-t}$, on obtient la somme de la seconde série. Les deux séries convergent, donc leur différence donne **l’égalité demandée**, avec le terme général

$$
F_n(t)=e^{-(n+1)t}-\frac{e^{-(n+1)t}-e^{-(n+2)t}}{t}.
$$

> [!JURY]
> Le rapport attire l’attention sur la séparation de deux séries avant d’avoir justifié leur convergence.

### Question 14

> [!INDICATION]
> Factorisez l’exponentielle dans chaque terme. Étudiez d’abord le signe du second facteur, puis intégrez le terme à l’aide de la formule admise.

> [!INDICATION]
> Après avoir intégré, calculez d’abord une somme partielle. Cherchez une différence de logarithmes qui se simplifie terme à terme.

#### Solution

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

> [!JURY]
> Le théorème d’intégration terme à terme demande notamment la convergence de la série des intégrales en valeur absolue. Identifiez le rôle de chaque hypothèse.

## IV — Une deuxième expression intégrale de $\gamma$

Un changement d’échelle sépare les contributions des points proches de zéro et des grandes valeurs. Les majorants utiles sont différents sur les deux intervalles.

### Question 15

> [!INDICATION]
> Appliquez une identité de somme finie avant d’examiner la limite.

#### Solution

Pour $t\ne0$, la formule de la somme géométrique donne

$$
\frac{1-(1-t)^n}{t}=\sum_{j=0}^{n-1}(1-t)^j.
$$

Le polynôme de droite vaut $n$ en zéro. **Le quotient se prolonge par continuité avec la valeur $n$ en zéro.**

> [!PIEGE]
> L’identité polynomiale donne directement le prolongement. Une somme d’équivalents peut perdre le premier ordre lors d’une compensation.

### Question 16

> [!INDICATION]
> Intégrez la somme finie, dilatez l’intervalle par un changement de variable, puis repérez où le logarithme apparaît.

> [!INDICATION]
> Après le changement de variable, écrivez le logarithme comme une intégrale avant de simplifier.

#### Solution

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

> [!METHODE]
> Une différence d’intégrales se simplifie une fois les domaines découpés aux mêmes bornes.

### Question 17

> [!INDICATION]
> Fixez la variable réelle. Pour un indice assez grand, prenez le logarithme avant d’utiliser le développement limité.

#### Solution

Pour $x$ fixé et $n>x$, la base est strictement positive. Comme $\ln(1-v)=-v+o(v)$ en zéro, $n\ln(1-x/n)\to-x$. Par continuité de l’exponentielle,

$$
\boxed{(1-x/n)^n\longrightarrow e^{-x}=\int_x^{+\infty}e^{-u}\,\mathrm du.}
$$

L’égalité donnant la limite en exponentielle vaut aussi pour tout $x\ge0$ fixé. On pourra donc l’utiliser sur $[0,1]$.

> [!JURY]
> Le rapport confirme que la demande d’une forme intégrale est une coquille. Il attendait la limite exponentielle et une justification qui passe par le logarithme.

### Question 18

> [!INDICATION]
> Déterminez quelle branche de la définition est active à partir d’un certain rang quand la variable est fixée.

#### Solution

Pour tout $t\ge1$ fixé, on a $n\ge t$ à partir d’un certain rang. La question 17 donne **$f_n(t)\to e^{-t}/t$**.

> [!JURY]
> Le jury relève des réponses qui font varier le point en même temps que l’indice. Une limite simple s’étudie à point fixé.

### Question 19

> [!INDICATION]
> Étudiez la différence des deux membres par dérivation et comparez sa valeur à celle en zéro.

#### Solution

Sur $[0,1[$, la fonction $v(t)=\ln(1-t)+t$ vérifie $v(0)=0$ et $v'(t)=-t/(1-t)\le0$. Elle est décroissante, donc **$\ln(1-t)\le-t$ pour tout $t\in[0,1[$**.

> [!JURY]
> Le jury attend une démonstration explicite de l’inégalité, au-delà d’une invocation générale de la convexité.

### Question 20

> [!INDICATION]
> Sur l’intervalle d’intégration, comparez le facteur inverse de la variable à une constante.

#### Solution

Sur $[1,+\infty[$, la fonction $e^{-u}/u$ est continue et vérifie $0\le e^{-u}/u\le e^{-u}$. La majorante est intégrable sur cet intervalle. **L’intégrale converge.**

> [!JURY]
> Pour une comparaison d’intégrales, le rapport demande de préciser l’intervalle, la régularité de l’intégrande et son signe.

### Question 21

> [!INDICATION]
> Pour un indice donné, localisez l’intervalle où la fonction peut être non nulle.

#### Solution

Pour chaque $n\ge1$, $f_n$ est continue sur $[1,n]$ et vaut zéro sur $]n,+\infty[$. Elle est continue au raccord $n$ car sa valeur et sa limite à droite y sont nulles.

**Elle est intégrable sur $[1,+\infty[$**, étant continue et nulle hors de $[1,n]$.

> [!JURY]
> L’intégrabilité se vérifie fonction par fonction. Le rapport relève des applications prématurées d’un théorème de passage à la limite.

### Question 22

> [!INDICATION]
> Réécrivez les intégrales sur un domaine commun. Pour la domination, distinguez la zone active et la zone où les fonctions sont nulles.

> [!INDICATION]
> Utilisez l’inégalité logarithmique sur la branche non nulle. Vérifiez séparément le raccord au point de coupure.

#### Solution

Pour $1\le u<n$, la question 19 appliquée à $u/n$ donne $(1-u/n)^n\le e^{-u}$. Pour $u\ge n$, $f_n(u)=0$, y compris en $n$. Ainsi

$$
0\le f_n(u)\le\frac{e^{-u}}u.
$$

La majorante est intégrable par la question 20. Les fonctions $f_n$ sont intégrables d’après la question 21, et la limite simple de la question 18 est continue. Le théorème de convergence dominée sur l’intervalle fixe $[1,+\infty[$ fournit

$$
\boxed{\int_1^n\frac{(1-u/n)^n}{u}\,\mathrm du
\longrightarrow\int_1^{+\infty}\frac{e^{-u}}u\,\mathrm du.}
$$

> [!JURY]
> La convergence dominée s’applique à un intervalle fixe. Le rapport demande aussi de vérifier le majorant sur la zone de prolongement par zéro.

### Question 23

> [!INDICATION]
> Étudiez le comportement du numérateur près de zéro au premier ordre.

#### Solution

La fonction $(1-e^{-u})/u$ est continue sur $]0,1]$ et tend vers $1$ en zéro, car $1-e^{-u}=u+o(u)$. Son prolongement continu sur $[0,1]$ montre que **l’intégrale converge**.

> [!METHODE]
> Le quotient a une singularité apparente. Pour prouver la convergence, cherchez d’abord si un prolongement continu suffit.

### Question 24

> [!INDICATION]
> Appliquez l’inégalité des accroissements finis à la puissance, entre zéro et la borne variable.

#### Solution

Pour $0\le v\le t\le1$, la fonction $b_n(v)=(1-v/n)^n$ est continue et dérivable à l’intérieur, avec $b'_n(v)=-(1-v/n)^{n-1}$.

Pour $n=1$ la dérivée vaut $-1$, et pour $n\ge2$ elle est comprise entre $-1$ et $0$.

La fonction est donc décroissante. L’inégalité des accroissements finis donne $|b_n(t)-b_n(0)|\le t$.

Puisque $b_n(0)=1$, la différence $1-b_n(t)$ est positive ou nulle. Ainsi, pour $0<t\le1$,

$$
\boxed{0\le\frac{1-(1-t/n)^n}{t}\le1.}
$$

> [!JURY]
> Le rapport relève des suppressions de valeurs absolues injustifiées. Séparez la borne sur la dérivée de l’étude du signe du numérateur.

### Question 25

> [!INDICATION]
> Rassemblez la convergence simple et la majoration obtenues séparément. Prolongez au besoin la fonction en zéro.

#### Solution

Sur $]0,1]$, la limite simple du quotient de la question 24 est $(1-e^{-u})/u$ d’après la question 17. Les quotients se prolongent continûment en zéro avec la valeur $1$ d’après la question 15 appliquée à $u/n$. La limite admet le même prolongement par la question 23. La domination uniforme par la fonction constante $1$ sur $[0,1]$ autorise le théorème de convergence dominée.

$$
\boxed{\int_0^1\frac{1-(1-u/n)^n}{u}\,\mathrm du
\longrightarrow\int_0^1\frac{1-e^{-u}}u\,\mathrm du.}
$$

> [!METHODE]
> Sur un intervalle borné, un majorant constant est intégrable. Mentionnez l’intervalle et la limite avant d’appliquer le théorème.

### Question 26

> [!INDICATION]
> Reprenez la différence d’intégrales obtenue au départ de la partie. Chaque terme a maintenant une limite.

#### Solution

Dans l’égalité de la question 16, $a_n\to\gamma$ d’après la question 2. Les deux intégrales ont pour limites celles des questions 25 et 22, respectivement. Par passage à la limite,

$$
\boxed{\gamma=\int_0^1\frac{1-e^{-u}}u\,\mathrm du
-\int_1^{+\infty}\frac{e^{-u}}u\,\mathrm du.}
$$

> [!JURY]
> Le rapport attend de rattacher précisément chaque passage à la limite aux questions où les hypothèses ont été établies.

## V — Deux autres expressions intégrales de $\gamma$

L’étude de la fonction Gamma fait intervenir des dominations uniformes en paramètre, puis la dérivation d’une série obtenue à partir d’un produit.

### Question 27

> [!INDICATION]
> Contrôlez séparément l’intégrande près de zéro et près de l’infini.

#### Solution

Pour $x>0$, l’intégrande $t^{x-1}e^{-t}$ est continue et positive sur $]0,+\infty[$. Sur $]0,1]$ elle est majorée par $t^{x-1}$, intégrable puisque $x-1>-1$.

À l’infini, les croissances comparées donnent $t^{x-1}e^{-t/2}\to0$, donc l’intégrande est majorée, pour $t$ assez grand, par $e^{-t/2}$. **L’intégrale définit $\Gamma(x)$ pour tout $x>0$.**

> [!METHODE]
> Une puissance peut servir de majorant à zéro. À l’infini, réservez une partie du facteur exponentiel pour dominer la puissance.

### Question 28

> [!INDICATION]
> Figez un segment de paramètres positifs. Près de zéro et vers l’infini, quelle extrémité du segment donne le plus grand majorant ?

> [!INDICATION]
> Au voisinage de zéro, absorbez la valeur absolue du logarithme dans une petite puissance. À l’infini, absorbez-la dans un facteur exponentiel.

#### Solution

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

> [!JURY]
> Le rapport relève que l’intégrabilité de l’intégrande et celle du majorant de la dérivée sont souvent mal justifiées. Vérifiez les deux séparément.

### Question 29

> [!INDICATION]
> Intégrez par parties sur un segment intérieur à l’intervalle. Vérifiez ensuite ce qui se passe aux deux bornes.

#### Solution

Pour $x>0$, intégrons par parties sur un segment $[\eta,T]\subset]0,+\infty[$.

$$
\int_\eta^T t^x e^{-t}\,\mathrm dt
=[-t^x e^{-t}]_\eta^T+x\int_\eta^T t^{x-1}e^{-t}\,\mathrm dt.
$$

Les deux intégrales convergent par Q27. Le crochet tend vers zéro, car $t^x e^{-t}$ tend vers zéro aux deux bornes. **On obtient $\Gamma(x+1)=x\Gamma(x)$.**

> [!JURY]
> Le rapport demande d’établir les convergences nécessaires avant d’écrire la formule avec les bornes impropres.

### Question 30

> [!INDICATION]
> Passez du produit à une somme en utilisant le logarithme des produits partiels. Étudiez sur un segment la série des dérivées.

> [!INDICATION]
> Simplifiez la différence des deux fractions obtenues par dérivation avant de chercher un majorant sommable.

#### Solution

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

> [!JURY]
> La série des termes et celle des dérivées jouent des rôles distincts. Le rapport relève des dérivations terme à terme avec des hypothèses manquantes.

### Question 31

> [!INDICATION]
> Évaluez d’abord la dérivée logarithmique, puis utilisez la relation fonctionnelle dérivée.

#### Solution

On a $\Gamma(1)=\int_0^{+\infty}e^{-t}\,\mathrm dt=1$. En $x=1$, la série de la question 30 est télescopique, de somme $1$. Ainsi **$\Gamma'(1)=-\gamma$**.

En dérivant la formule de la question 29, on obtient $\Gamma'(x+1)=\Gamma(x)+x\Gamma'(x)$. En $x=1$, cela donne **$\Gamma'(2)=1-\gamma$**.

> [!METHODE]
> Dans la formule de Q30, la série en ce point est télescopique. Avant de retrouver la dérivée, calculez la valeur de la fonction elle-même.

### Question 32

> [!INDICATION]
> Cherchez un changement de variable dont la différentielle absorbe le facteur exponentiel.

#### Solution

D’après les questions 28 et 31, $-\gamma=\int_0^{+\infty}\ln(u)e^{-u}\,\mathrm du$, avec intégrabilité absolue. Le changement de variable $t=e^{-u}$, d’abord sur des segments, donne $u=-\ln t$ et $\mathrm dt=-e^{-u}\,\mathrm du$. En passant aux bornes, on obtient

$$
\boxed{\gamma=-\int_0^1\ln(-\ln t)\,\mathrm dt.}
$$

> [!PIEGE]
> Le signe de la différentielle et l’inversion des bornes se compensent. Le signe extérieur venant de la constante doit encore être conservé.

## VI — Recherche d’une valeur approchée de $\gamma$

L’approximation combine une série alternée sur un intervalle borné et une majoration du reste d’intégrations par parties sur une demi-droite.

### Question 33

> [!INDICATION]
> Déplacez la coupure dans les deux intégrales simultanément et combinez les nouveaux termes.

#### Solution

D’après la question 26, on peut reporter le point de coupure de $1$ à $A$ par les relations de Chasles, avec des intégrales orientées si $A<1$.

Les deux nouveaux morceaux entre $1$ et $A$ s’ajoutent dans l’expression avec l’intégrande $[(1-e^{-u})+e^{-u}]/u=1/u$. Leur somme vaut $\ln A$. Ainsi

$$
\boxed{\gamma=-\ln A+\int_0^A\frac{1-e^{-u}}u\,\mathrm du
-\int_A^{+\infty}\frac{e^{-u}}u\,\mathrm du.}
$$

> [!METHODE]
> Utilisez des intégrales orientées pour appliquer la même preuve lorsque le nouveau point de coupure est inférieur à l’ancien.

### Question 34

> [!INDICATION]
> Développez l’exponentielle et divisez par la variable après simplification du terme constant.

#### Solution

Pour $0\le u\le A$, le prolongement continu de $(1-e^{-u})/u$ est la somme de la série entière

$$
\sum_{k=0}^{+\infty}\frac{(-1)^k u^k}{(k+1)!}.
$$

La série converge normalement sur $[0,A]$. En effet, pour les majorants $A^k/(k+1)!$, le rapport successif $A/(k+2)$ tend vers zéro, donc leur série converge par le critère de d’Alembert. On peut intégrer terme à terme. La série numérique ainsi obtenue converge absolument, ses termes en valeur absolue étant majorés par $A\cdot A^k/(k+1)!$. Sa somme est

$$
\boxed{\sum_{k=0}^{+\infty}\frac{(-1)^kA^{k+1}}{(k+1)(k+1)!}
=\int_0^A\frac{1-e^{-u}}u\,\mathrm du.}
$$

> [!JURY]
> Sur le segment fixé, majorez les termes par une série numérique sommable. Le rapport relève que la valeur de la somme est souvent donnée sans interversion justifiée.

### Question 35

> [!INDICATION]
> Pour l’intégration par parties, prenez une primitive du facteur exponentiel et dérivez le facteur inverse.

#### Solution

Pour $x>0$, les fonctions $e^{-u}/u$ et $e^{-u}/u^2$ sont continues, positives et majorées par des constantes fois $e^{-u}$ sur $[x,+\infty[$.

Une intégration par parties sur $[x,T]$, suivie du passage à la limite avec $e^{-T}/T\to0$, donne

$$
\boxed{\int_x^{+\infty}\frac{e^{-u}}u\,\mathrm du
=\frac{e^{-x}}x-\int_x^{+\infty}\frac{e^{-u}}{u^2}\,\mathrm du.}
$$

> [!METHODE]
> Vérifiez la convergence des deux intégrales et la limite du crochet. Vous pouvez d’abord écrire l’identité sur un segment.

### Question 36

> [!INDICATION]
> Appliquez la même intégration par parties aux puissances suivantes du facteur inverse. Conservez le dernier reste sous forme d’intégrale.

#### Solution

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

> [!METHODE]
> Une relation indicée par l’exposant permet de contrôler les coefficients et l’alternance des signes.

### Question 37

> [!INDICATION]
> Écrivez l’identité exacte avant de majorer les deux restes. Comparez les termes de la série à partir de l’indice où commence la queue.

> [!INDICATION]
> Comparez la valeur absolue de deux termes consécutifs du reste de série. Dans le reste intégral, remplacez le facteur de puissance par un majorant constant.

#### Solution

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

> [!JURY]
> Le rapport confirme l’erreur de signe dans la valeur absolue. Une fois corrigée, séparez le reste alterné et le reste intégral.

## VII — Étude d’une série entière aux bornes de son disque ouvert de convergence

Les coefficients harmoniques donnent un modèle pour le bord positif. Les différences successives de logarithmes permettent de traiter le bord négatif.

## VII.A — Rayon de convergence et première expression de la somme

Comparez le comportement des termes à l’intérieur et aux extrémités du domaine.

### Question 38

> [!INDICATION]
> Écartez les tout premiers indices si un quotient n’est pas défini, puis limitez le quotient des valeurs absolues.

#### Solution

Pour $n\ge2$, le quotient $\ln(n+1)/\ln n$ tend vers $1$, car $\ln(n+1)-\ln n=\ln(1+1/n)\to0$ et $\ln n\to+\infty$.

Pour $x\ne0$, le quotient des valeurs absolues des termes successifs tend donc vers $|x|$.

La série converge absolument si $|x|<1$ et diverge si $|x|>1$.

En $x=1$ et en $x=-1$, les termes ne tendent pas vers zéro. **Le rayon vaut $1$ et le domaine réel est $]-1,1[$.**

> [!JURY]
> Le critère de d’Alembert laisse les points du bord à examiner séparément. Le rapport relève des usages du quotient sans valeur absolue ou sans justification.

## VII.B — Étude de $f$ en $1$

La comparaison est relative. Elle consiste à calculer une fonction de référence et à comparer sa divergence à l’erreur.

### Question 39

> [!INDICATION]
> Minorez les coefficients à partir d’un rang fixé et comparez la somme à une série familière.

#### Solution

Pour $0\le x<1$, tous les termes sont positifs ou nuls. Pour $n\ge2$, $\ln n\ge\ln2$, ce qui donne

$$
f(x)\ge\frac{(\ln2)x^2}{1-x}.
$$

La borne inférieure tend vers $+\infty$. **$f(x)\to+\infty$ lorsque $x\to1^-$.**

> [!METHODE]
> La positivité sur la demi-droite positive permet de minorer la somme par celle d’une autre série pour chaque abscisse.

### Question 40

> [!INDICATION]
> Encadrez chaque somme harmonique par des expressions simples en son indice.

#### Solution

Si $H_n=\sum_{k=1}^n1/k$, alors $1\le H_n\le n$. Pour $|x|<1$, la série $\sum n|x|^n$ converge, donc $\sum H_nx^n$ converge absolument.

Pour $|x|\ge1$, le terme ne tend pas vers zéro. **Le rayon est $1$.**

> [!PIEGE]
> Le coefficient est toute la somme harmonique, pas son dernier terme. Un encadrement grossier suffit à déterminer le rayon.

### Question 41

> [!INDICATION]
> Pour le produit de Cauchy, regroupez les couples d’indices qui ont une somme fixée.

> [!INDICATION]
> Pour identifier la seconde somme, intégrez la série géométrique en prenant la primitive nulle à l’origine.

#### Solution

Pour $|x|<1$, les deux séries indiquées sont absolument convergentes.

Le produit de Cauchy de $\sum_{j\ge0}x^j$ et $\sum_{k\ge1}x^k/k$ a pour coefficient de $x^n$ le nombre $H_n$ pour les degrés strictement positifs, et zéro en degré zéro.

La série géométrique a pour somme $1/(1-x)$. La primitive de la série géométrique sur $]-1,1[$, prise nulle en zéro, donne $\sum_{k\ge1}x^k/k=-\ln(1-x)$. Ainsi

$$
\boxed{g(x)=\frac{\ln(1-x)}{x-1}\qquad(|x|<1).}
$$

> [!JURY]
> Le rapport relève des justifications insuffisantes dans le produit de Cauchy. Vérifiez la convergence absolue des deux facteurs et identifiez le coefficient avec ses bonnes bornes.

### Question 42

> [!INDICATION]
> Contrôlez la différence des coefficients grâce à la convergence établie au début.

#### Solution

Par la question 2, $(H_n-\ln n)_{n\ge1}$ est convergente, donc bornée en valeur absolue par un réel $M>0$. Pour $0\le x<1$, l’inégalité triangulaire appliquée aux séries convergentes donne

$$
|f(x)-g(x)|\le\frac{M}{1-x}.
$$

> [!METHODE]
> La différence est majorée par une constante indépendante de l’indice. Cela ramène la somme d’erreurs à une série géométrique.

### Question 43

> [!INDICATION]
> Divisez l’estimation de la différence par la fonction de référence avant de passer à la limite.

> [!INDICATION]
> Réutilisez la formule explicite issue du produit de Cauchy pour décider lequel des facteurs de l’estimation peut diverger.

#### Solution

Pour $0<x<1$, $g(x)=-\ln(1-x)/(1-x)>0$. D’après la question 42,

$$
\left|\frac{f(x)}{g(x)}-1\right|
\le \frac{M}{-\ln(1-x)}.
$$

Ce majorant tend vers zéro. Donc **$f(x)\sim g(x)$ lorsque $x\to1^-$**.

> [!JURY]
> Le jury relève que contrôler une différence ne suffit pas à justifier un équivalent. L’écart relatif doit tendre vers zéro.

## VII.C — Étude de $f$ en $-1$

La série auxiliaire atteint ses deux bords par convergence uniforme. Sa valeur au bord négatif transporte l’information vers la série proposée.

### Question 44

> [!INDICATION]
> Développez le logarithme au-delà de l’ordre qui se compense. Examinez alors les deux points de module un.

#### Solution

Par développement limité, $-\ln(1-1/n)=1/n+1/(2n^2)+o(n^{-2})$. Ainsi $c_n\sim 1/(2n^2)$. La série $\sum |c_n|$ converge par comparaison, d’où la convergence absolue de $\sum c_nx^n$ pour $|x|\le1$.

Si $|x|>1$, la valeur absolue de son terme général est équivalente à $|x|^n/(2n^2)$ et tend vers $+\infty$. **Le rayon est $1$ et le domaine réel de $h$ est $[-1,1]$.**

> [!METHODE]
> Le domaine réel se détermine en plus du rayon. Les coefficients ici permettent une convergence absolue même lorsque le module de la variable vaut un.

### Question 45

> [!INDICATION]
> Écrivez le logarithme en différence de deux logarithmes consécutifs et calculez une somme partielle.

#### Solution

Pour $n\ge2$, on peut écrire $c_n=\ln n-\ln(n-1)-1/n$. Avec $c_1=-1$, le télescopage donne $\sum_{k=1}^n c_k=\ln n-H_n$. Par la question 2, **la somme de la série vaut $-\gamma$**.

> [!PIEGE]
> Le premier coefficient est défini séparément. Intégrez-le à la somme partielle avant de comparer avec la suite de départ.

### Question 46

> [!INDICATION]
> Cherchez un majorant indépendant de l’abscisse qui reste valable au bord.

#### Solution

Sur $[-1,1]$, on a $\sup |c_n x^n|=|c_n|$. Ces majorants sont sommables d’après la question 44. La série converge donc normalement, donc uniformément.

Ses termes sont continus sur ce segment, d’où la continuité de $h$ sur $[-1,1]$. **En particulier, $h$ est continue en $1$ et $h(1)=-\gamma$.**

> [!METHODE]
> La convergence uniforme sur le segment fermé autorise le passage de la continuité des sommes partielles à celle de leur limite au bord.

### Question 47

> [!INDICATION]
> Séparez la partie harmonique et la partie logarithmique. Pour la seconde, traitez les indices pairs et impairs séparément.

> [!INDICATION]
> Le coefficient d’indice un apporte seulement une contribution à la somme harmonique alternée.

#### Solution

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

> [!METHODE]
> Après regroupement, traduisez les produits de facteurs pairs et impairs en factorielles. Pensez au produit vide pour le premier indice.

### Question 48

> [!INDICATION]
> Les différences successives de logarithmes suggèrent de multiplier une série par un polynôme de degré un. Pour le produit factoriel, comparez des intégrales de puissances trigonométriques d’indices voisins.

> [!INDICATION]
> Pour les intégrales de puissances, cherchez une relation par intégration par parties qui diminue l’exposant de deux. Encadrez ensuite le rapport d’indices voisins.

#### Solution

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

> [!METHODE]
> Il y a deux limites distinctes à justifier. La continuité de la somme auxiliaire donne le passage au bord, puis un encadrement des intégrales de puissances donne la limite du produit.

## Bilan

- Pour les suites, calculez les différences au bon ordre avant de chercher une comparaison. Pour une limite en probabilité, combinez une majoration quantitative de la fluctuation et une estimation distincte de l’écart déterministe.
- Avant une interversion, indiquez la nature de la convergence demandée. Une suite d’intégrales, une série à intégrer et une série à dériver appellent des hypothèses différentes. Sur un intervalle impropre, contrôlez chacune des bornes.
- Une série entière peut être étudiée par comparaison de coefficients, par produit de Cauchy ou par décalage d’indices. Aux extrémités, vérifiez le domaine de définition puis choisissez une série auxiliaire dont la convergence jusqu’au bord est justifiée.
- Une approximation avec erreur garantie repose sur une identité exacte, un contrôle du signe et des majorations séparées de tous les restes.
