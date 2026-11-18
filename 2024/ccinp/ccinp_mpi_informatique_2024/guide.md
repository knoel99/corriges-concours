# CCINP MPI — Informatique 2024 · Corrigé guidé

*Corrigé rédigé par IA, non officiel. Signalez toute erreur.*

## Présentation du sujet

L’épreuve écrite d’informatique dure quatre heures, sans calculatrice. Le sujet comporte 35 questions en trois parties indépendantes et des exercices de programmation dans deux langages.

- **I · Classification (Q1–Q7).** Exécuter deux algorithmes de classification à la main, puis implémenter le second en C à l’aide de structures et de listes chaînées.
- **II · Langages réguliers (Q8–Q14).** Caractériser les classes d’une relation de permutation et reconnaître leurs représentants par automate.
- **III · Correspondance de Burge (Q15–Q35).** Réaliser des suites de degrés, puis effectuer des insertions dans des tableaux de Young, avec du code OCaml fonctionnel.

Les outils du programme MP2I/MPI mobilisés sont notamment les k-moyennes, les structures et pointeurs du C, les automates finis et les expressions régulières, les graphes simples, la récursion sur listes, le filtrage et le tri. Les définitions propres aux diagrammes de Young sont fournies dans le sujet. Prenez les points abordables de calcul et de code court, notamment Q2 à Q6, Q19, Q20, Q24 et Q25. Prévoyez du temps dans la troisième partie pour les preuves par échange d’arêtes et les traces d’insertion. Les trois parties indépendantes permettent de reprendre ailleurs si un raisonnement bloque.

Le rapport du jury relève les difficultés rencontrées dans la lecture des traces à la main, les démonstrations de Q17–Q18 et le tri répété de Q22. Écrivez les états intermédiaires, vérifiez les hypothèses des arguments et gardez des noms de variables lisibles. [Sujet officiel](https://www.concours-commun-inp.fr/_resource/annales%20%C3%A9crits/2024/MPI/2024_MPI5IN.pdf?download=true) · [Rapport 2024](https://www.concours-commun-inp.fr/_resource/annales%20%C3%A9crits/2024/MPI/MPI_ECRIT_Informatique_2024_v2.pdf?download=true) · [Programme au Bulletin officiel](https://www.education.gouv.fr/bo/21/Special1/ESRS2035777A.htm)

## Partie I — Algorithme Single Pass

Les k-moyennes réaffectent tous les documents à chaque itération. Single Pass traite les documents dans l’ordre et ne met à jour que la classe concernée.

### Question 1

> [!INDICATION]
> Séparez la phase d’affectation de la phase de recalcul.

> [!INDICATION]
> Calculez les deux distances de chaque document avec les centres de début d’itération. Faites ensuite deux moyennes de vecteurs.

#### Solution

On affecte chaque document au centre qui minimise sa distance $\delta$, puis on prend la moyenne coordonnée par coordonnée dans chaque classe. Dans l’ordre des documents, les couples de distances sont $(6,5)$, $(0,3)$, $(2,3)$, $(4,3)$, $(3,0)$ à la première itération.

À la deuxième, ils sont $(5,7/3)$, $(1,11/3)$, $(1,11/3)$, $(3,5/3)$, $(2,8/3)$.

À la troisième, ils sont $(5,1)$, $(5/3,5)$, $(5/3,5)$, $(3,1)$, $(4/3,4)$.

- Itération 1. Centres $c_1=(2,1,0)$ et $c_2=(1,0,1)$. Classes $A_1=\{d_2,d_3\}$ et $A_2=\{d_1,d_4,d_5\}$.
- Itération 2. Centres $c_1=(1,1,0)$ et $c_2=(1,2,5/3)$. Classes $A_1=\{d_2,d_3,d_5\}$ et $A_2=\{d_1,d_4\}$.
- Itération 3. Centres $c_1=(1,2/3,1/3)$ et $c_2=(1,3,2)$. Classes $A_1=\{d_2,d_3,d_5\}$ et $A_2=\{d_1,d_4\}$.

**Les classes sont stabilisées à la troisième itération.**

> [!PIEGE]
> La distance demandée est la somme des écarts absolus. L’itération des k-moyennes utilise ici les moyennes prescrites et le critère de distance du sujet.

### Question 2

> [!INDICATION]
> Tenez à jour sur une même ligne les centres disponibles et la décision concernant le document courant.

> [!INDICATION]
> Comparez le minimum au seuil. Si une classe existante reçoit un document, recalculer sa moyenne exige les documents affectés à cette classe.

#### Solution

On initialise $A_1=\{d_1\}$ et $c_1=(1,3,3)$. Le minimum de l’étape (iii) porte sur les $j$ centres existants. La borne $k<i$ engloberait des centres inexistants dès que $j<i-1$.

- $d_2$. Distances avant affectation $6$. Toutes strictement supérieures à 5 ? Oui. Classe $A_2=\{d_2\}$ (création), nouveau centre $(2,1,0)$.
- $d_3$. Distances avant affectation $6,2$. Toutes strictement supérieures à 5 ? Non. Classe $A_2=\{d_2,d_3\}$, nouveau centre $(1,1,0)$.
- $d_4$. Distances avant affectation $2,3$. Toutes strictement supérieures à 5 ? Non. Classe $A_1=\{d_1,d_4\}$, nouveau centre $(1,3,2)$.
- $d_5$. Distances avant affectation $4,2$. Toutes strictement supérieures à 5 ? Non. Classe $A_2=\{d_2,d_3,d_5\}$, nouveau centre $(1,2/3,1/3)$.

**Chaque ligne modifie uniquement la classe indiquée et son centre.**

> [!JURY]
> Le rapport 2024 relève des difficultés à exécuter le pseudo-code. Faites apparaître les distances et les centres obtenus après chaque décision.

### Question 3

> [!INDICATION]
> Repérez l’adresse à laquelle doit être stocké le nouveau pointeur de tête.

#### Solution

Les vérifications d’allocation utilisent `assert`, avec les assertions actives.

```c
#include <assert.h>
#include <stdlib.h>

void ajoutVecteur(vecteur *vec, noeud **tete)
{
    noeud *nouveau = malloc(sizeof(noeud));
    assert(nouveau != NULL);
    nouveau->c = vec;
    nouveau->suivant = *tete;
    *tete = nouveau;
}
```

> [!METHODE]
> Allouez le maillon et vérifiez l’allocation avant tout accès à ses champs. Chaînez-le à l’ancienne tête avant de changer le pointeur chez l’appelant.

### Question 4

> [!INDICATION]
> Calculez un écart entre deux coordonnées. Son signe vous indique comment obtenir sa valeur absolue.

#### Solution

```c
double delta(vecteur *di, vecteur *c)
{
    double distance = 0.0;
    for (int q = 0; q < di->taille; q = q + 1) {
        double ecart = di->v[q] - c->v[q];
        if (ecart < 0.0) {
            ecart = -ecart;
        }
        distance = distance + ecart;
    }
    return distance;
}
```

> [!PIEGE]
> Une valeur absolue d’entier risquerait de tronquer un écart lors du recalcul d’un centre à coordonnées fractionnaires.

### Question 5

> [!INDICATION]
> Pour invalider une condition qui doit être vraie pour toutes les distances, cherchez un seul contre-exemple.

#### Solution

```c
#include <stdbool.h>

bool distmax(double dists[], int j, double theta)
{
    for (int k = 0; k < j; k = k + 1) {
        if (!(dists[k] > theta)) {
            return false;
        }
    }
    return true;
}
```

> [!PIEGE]
> Une égalité au seuil rend le test universel faux.

### Question 6

> [!INDICATION]
> Gardez pendant le parcours l’indice où se trouve le meilleur candidat lu jusque-là.

#### Solution

Le tableau est non vide. En cas d’égalité, on retient le plus petit numéro de classe.

```c
int distmin(double dists[], int j)
{
    int indice = 0;
    for (int k = 1; k < j; k = k + 1) {
        if (dists[k] < dists[indice]) {
            indice = k;
        }
    }
    return indice + 1;
}
```

> [!METHODE]
> Vérifiez à part la convention d’indexation de la valeur renvoyée. Le numéro d’une classe et l’indice de sa distance diffèrent ici d’une unité.

### Question 7

> [!INDICATION]
> Donnez un rôle distinct au numéro de classe, à l’indice dans le tableau de distances et à la position du centre dans la liste.

> [!INDICATION]
> Quand une classe reçoit un document, son numéro doit être écrit dans le document avant l’appel de recalcul.

#### Solution

Le prototype imposé et celui de `recalculCentre` utilisent un tableau contigu de structures `vecteur`. On adopte cette représentation pour les deux fonctions. Elle diffère du tableau de pointeurs annoncé en amont. Les centres disposent de leurs propres coordonnées, car leur mise à jour doit préserver les coordonnées des documents. Le contrat de `recalculCentre` est de maintenir le numéro de classe du centre modifié et de calculer sa moyenne à partir des documents affectés à $\ell$. Si elle parcourt le tableau des documents, la longueur doit lui être connue par le contexte, puisque son prototype fourni ne la transmet pas.

```c
void recalculCentre(vecteur *documents, noeud **tete, int l);

vecteur *copieCentre(vecteur *document)
{
    vecteur *centre = malloc(sizeof(vecteur));
    assert(centre != NULL);
    centre->taille = document->taille;
    centre->num_classe = document->num_classe;
    centre->v = NULL;
    if (centre->taille > 0) {
        centre->v = malloc(centre->taille * sizeof(double));
        assert(centre->v != NULL);
        for (int q = 0; q < centre->taille; q = q + 1) {
            centre->v[q] = document->v[q];
        }
    }
    return centre;
}

noeud *algorithme1(vecteur *documents, int nb_documents, double theta)
{
    noeud *tete = NULL;
    if (nb_documents <= 0) {
        return tete;
    }

    double *dists = malloc(nb_documents * sizeof(double));
    assert(dists != NULL);
    for (int i = 0; i < nb_documents; i = i + 1) {
        documents[i].num_classe = 0;
    }

    int j = 1;
    documents[0].num_classe = j;
    ajoutVecteur(copieCentre(&documents[0]), &tete);
    for (int i = 1; i < nb_documents; i = i + 1) {
        for (noeud *courant = tete; courant != NULL; courant = courant->suivant) {
            int indice = courant->c->num_classe - 1;
            dists[indice] = delta(&documents[i], courant->c);
        }
        if (distmax(dists, j, theta)) {
            j = j + 1;
            documents[i].num_classe = j;
            ajoutVecteur(copieCentre(&documents[i]), &tete);
        } else {
            int l = distmin(dists, j);
            documents[i].num_classe = l;
            recalculCentre(documents, &tete, l);
        }
    }
    free(dists);
    return tete;
}
```

Avant chaque itération, les centres représentent les moyennes des classes des documents déjà affectés. Le rangement par numéro de classe dans `dists` permet de parcourir les nœuds dans leur ordre de chaînage. L’affectation ou la création préserve cet invariant.

Pour $n$ documents à $p\ge1$ coordonnées, l’itération $i$ coûte $O(pj_i)$ hors appel à `recalculCentre`, où $j_i\le i-1$ est le nombre de centres présents.

Le calcul des distances et la gestion des classes coûtent donc **$O(n^2p)$ dans le pire cas**, atteint quand chaque document crée une classe.

Avec un recalcul par balayage du tableau et moyenne des documents de la classe, chaque appel coûte au plus $O(np)$, d’où **$\Theta(n^2p)$ au pire** pour cette implémentation du recalcul. Le coût précis d’un appel dépend de l’implémentation fournie. Le stockage auxiliaire est $O(n)$ pour les distances, et $O(jp)$ pour les $j$ centres et leurs nœuds.

> [!PIEGE]
> Un ajout en tête change l’ordre de parcours de la liste. Utilisez le numéro mémorisé dans le centre pour écrire au bon indice. Conservez des coordonnées distinctes pour le centre et le document d’origine.

## Partie II — Langages réguliers

Les permutations autorisées laissent des séparateurs fixes. En étudiant les mots entre ces séparateurs, on peut passer des classes d’équivalence à un automate qui lit un mot lettre par lettre.

### Question 8

> [!INDICATION]
> Interprétez la fermeture réflexive transitive comme l’existence d’un chemin fini.

> [!INDICATION]
> Expliquez comment traiter un chemin vide, parcourir un chemin en sens inverse et joindre deux chemins.

#### Solution

La formule imprimée autorise $ab\to ba$. À la lettre, elle relie $ab$ à $ba$ sans relier $ba$ à $ab$. Puisque $R$ est annoncée symétrique, on autorise aussi l’échange inverse.

On utilise la fermeture réflexive transitive annoncée, c’est-à-dire une chaîne de longueur finie quelconque de ces échanges adjacents. La condition $i<\min(|u|,|v|)$ de l’énoncé doit être retirée. Lue comme une borne supplémentaire sur chaque étape de la chaîne, elle bornerait le nombre de coups par la longueur du mot.

Ainsi, $aaabbb$ et $bbbaaa$ demandent neuf échanges, puisque chaque échange change d’une unité le nombre de couples formés d’un $b$ précédant un $a$. Une suite de neuf coups existe en faisant remonter les $b$ un par un. On peut donc la découper en deux chaînes de longueur au plus six, ce qui montre que la relation bornée ne serait pas transitive.

Pour $R^*$, une chaîne de longueur zéro donne la réflexivité. L’inversion d’une chaîne est possible puisque $R$ est symétrique. La concaténation de deux chaînes donne la transitivité. **$R^*$ est donc une relation d’équivalence.**

> [!METHODE]
> Une description littérale contredit ici le nom de la relation. Isoler cette contradiction permet de démontrer la propriété pour la définition cohérente et de justifier la correction retenue.

### Question 9

> [!INDICATION]
> Cherchez une propriété de longueur que chaque échange conserve.

#### Solution

Une permutation adjacente conserve la longueur. La classe de $u$ est donc incluse dans l’ensemble fini $\Sigma^{|u|}$. Pour chacun de ses mots, la concaténation de ses lettres donne une expression régulière de ce singleton (avec $\varepsilon$ pour le mot vide). Leur union finie décrit exactement la classe. **Chaque classe est régulière.**

> [!METHODE]
> Pour prouver qu’un langage fini est régulier, construisez une expression en prenant l’union des expressions de ses singletons.

### Question 10

> [!INDICATION]
> Séparez les cas suivant le nombre et la position des lettres qui ne participent jamais aux échanges.

> [!INDICATION]
> Dans chaque bloc de deux ou trois lettres, regroupez les mots ayant les mêmes effectifs.

#### Solution

Les positions de $c$ sont fixes. Dans chaque bloc séparé par les $c$, y compris aux deux extrémités du mot, les effectifs de $a$ et $b$ sont invariants. Comme à la question 13, des échanges adjacents permettent de trier chaque bloc et l’on peut renverser chaque échange. Les mots ayant ces mêmes invariants forment donc une classe.

Les classes à plusieurs mots sont

$$
\boxed{\{aab,aba,baa\},\quad\{abb,bab,bba\},\quad\{abc,bac\},\quad\{cab,cba\}.}
$$

Les autres classes sont les singletons des mots suivants.

- Nombre de lettres $c$ égal à $0$ · $aaa,bbb$.
- Nombre de lettres $c$ égal à $1$ · $aac,bbc,caa,cbb,aca,acb,bca,bcb$.
- Nombre de lettres $c$ égal à $2$ · $acc,bcc,cac,cbc,cca,ccb$.
- Nombre de lettres $c$ égal à $3$ · $ccc$.

On compte ainsi **21 classes et 27 mots**.

> [!JURY]
> Le rapport 2024 relève des listes de classes incomplètes. En fin d’inventaire, additionnez les cardinaux et retrouvez les 27 mots.

### Question 11

> [!INDICATION]
> Comparez d’abord les préfixes égaux, puis le premier caractère différent.

> [!INDICATION]
> Pour trois mots, distinguez les cas selon les deux indices de première différence. Un symbole de fin permet de traiter aussi les préfixes propres.

#### Solution

Dans (ii), la première différence peut se trouver à l’indice $1$. On lit donc $i\ge1$, avec un préfixe vide à cet indice. Sinon $a$ et $b$ seraient incomparables et la relation ne pourrait être totale.

Prolongeons chaque mot fini par une répétition d’un symbole de fin $\bot$, avec $\bot<a<b<c$. Deux mots distincts se comparent à leur premier indice de différence, soit un préfixe propre départagé par $\bot$, soit une différence de lettres. L’égalité entraîne la réflexivité.

Pour la transitivité, si $u\prec v$ et $v\prec w$ ont leurs premières différences en $i$ et $j$, alors les trois mots prolongés coïncident avant $\min(i,j)$.

Si $i<j$, à l’indice $i$, $u_i<v_i=w_i$. Si $j<i$, à l’indice $j$, $u_j=v_j<w_j$.

Si $i=j$, à cet indice, $u_i<v_i<w_i$.

Dans chaque cas $u\prec w$. Les cas d’égalité sont immédiats. Deux mots distincts sont comparables et le sens opposé est exclu par l’ordre sur les symboles. **$\preceq$ est donc un ordre total avec cette correction.**

Avec la borne littérale $i>1$, la réflexivité demeure. Deux mots non vides comparables doivent commencer par la même lettre, et sur chaque ensemble de mots de première lettre fixée, la relation est l’ordre lexicographique déjà étudié. Le mot vide est inférieur à tous les mots. La relation littérale est donc également transitive, mais elle ne compare pas les mots de premières lettres distinctes.

> [!PIEGE]
> La définition d’un ordre total exige aussi l’antisymétrie et la comparabilité. Une comparaison doit pouvoir se décider dès la première lettre.

### Question 12

> [!INDICATION]
> Découpez le mot aux positions de la lettre immobile, puis cherchez à minimiser chaque bloc.

#### Solution

À l’intérieur de chaque bloc séparé par $c$, le mot minimal place tous les $a$ avant les $b$.

Les blocs $ba$ et $bab$ deviennent $ab$ et $abb$. Le représentant est **$abcabb$**.

### Question 13

> [!INDICATION]
> Déterminez ce qui rend un mot améliorable par un échange local.

> [!INDICATION]
> Décrivez d’abord la forme d’un bloc minimal sans lettre séparatrice. Ajoutez ensuite la possibilité d’enchaîner plusieurs blocs.

#### Solution

Une classe est déterminée par les positions des $c$ et les effectifs de $a$ et $b$ dans chacun des blocs.

Tous les mots de la classe atteignent le même mot par échanges $ba\to ab$, jusqu’à disparition de toute inversion $b$ avant $a$ dans un bloc.

Chaque échange diminue le mot pour l’ordre lexicographique, ce qui donne son minimum. Les représentants sont donc exactement les blocs de la forme $a^*b^*$ séparés par des $c$, blocs vides compris.

$$
\boxed{L=a^*b^*(ca^*b^*)^*.}
$$

> [!JURY]
> Le rapport 2024 relie les erreurs d’automate à une mauvaise caractérisation préalable des représentants. Vérifiez le mot vide, un mot fait uniquement de séparateurs et un mot dont l’inversion est interne à un bloc.

### Question 14

> [!INDICATION]
> Déterminez ce qu’il faut retenir depuis le dernier séparateur.

> [!INDICATION]
> Décidez ce qui se passe après une inversion et après le début d’un nouveau bloc.

#### Solution

On part de $A$. Les états finaux sont $A$ et $B$.

L’état $A$ signifie que le bloc courant ne contient pas de $b$, $B$ qu’on a vu un $b$ dans ce bloc, et $P$ qu’une inversion a été rencontrée.

- $A$ (initial et final). Sur `a`, $A$. Sur `b`, $B$. Sur `c`, $A$.
- $B$ (final). Sur `a`, $P$. Sur `b`, $B$. Sur `c`, $A$.
- $P$. Sur `a`, $P$. Sur `b`, $P$. Sur `c`, $P$.

**L’automate est déterministe, complet et accepte exactement $L$.**

> [!METHODE]
> Un état d’échec peut mémoriser la présence d’une inversion pour tout le reste de la lecture. Toute paire état–lettre doit avoir une transition dans un automate complet.

## Partie III — Correspondance de Burge

On commence par les suites de degrés, puis on utilise les diagrammes de Young pour donner une représentation qui conserve davantage d’information sur le graphe.

## III.1 — Partitions d’un entier

Pour analyser une suite de degrés, on cherche à réduire le problème d’un sommet. Une preuve d’échange prépare la réduction, puis les listes OCaml permettent de l’appliquer.

### Question 15

> [!INDICATION]
> Comptez les incidences sommet–arête de deux manières.

#### Solution

Chaque arête a deux extrémités et contribue une unité au degré de chacune. Ainsi, pour tout graphe simple à $m$ arêtes,

$$
\sum_{i=1}^{l} d_i = 2m.
$$

**Une suite de somme impaire ne peut donc pas être graphique.**

> [!JURY]
> Le rapport 2024 mentionne le lemme des poignées de main. Une phrase sur les deux extrémités de chaque arête suffit à établir le résultat.

### Question 16

> [!INDICATION]
> Gardez le graphe qui réalise la suite connue et ajoutez un sommet.

> [!INDICATION]
> Les sommets dont le degré augmente doivent être précisément les voisins du nouveau sommet.

#### Solution

Partons d’un graphe simple sur les sommets $2,\ldots,l$ dont les degrés sont $d_2,\ldots,d_l$.

Ajoutons le sommet $1$ et relions-le à chacun des $d_1$ sommets de $2$ à $d_1+1$, ce qui est possible car $d_1\le l-1$. On ajoute uniquement des arêtes distinctes et sans boucle.

Le sommet $1$ a degré $d_1$, chacun de ses nouveaux voisins gagne une unité et les autres degrés restent inchangés. La suite obtenue est décroissante, notamment $d_1\ge d_2+1$. **Le graphe réalise la suite demandée.**

> [!JURY]
> Le rapport 2024 attendait cette construction directe. Elle justifie à la fois la simplicité du graphe et les degrés finaux.

### Question 17

> [!INDICATION]
> Fixez une réalisation maximisant le nombre de voisins de $1$ dans l’ensemble visé.

> [!INDICATION]
> Comparez les voisinages d’un sommet voulu et d’un voisin hors de l’ensemble. Écartez des deux voisinages les sommets déjà engagés dans l’échange.

#### Solution

Si $d_1=0$, la propriété est immédiate. Sinon, notons $D=\{2,\ldots,d_1+1\}$. Parmi les réalisations étiquetées de la suite, choisissons-en une où le nombre de voisins de $1$ dans $D$ est maximal.

Supposons qu’un sommet $u\in D$ ne soit pas voisin de $1$. Comme $1$ possède exactement $|D|$ voisins, il a un voisin $v\notin D$. Alors $d_u\ge d_v$.

Dans $S\setminus\{1,u,v\}$, le sommet $u$ a $d_u-\mathbf{1}_{\{u,v\}\in A}$ voisins, tandis que $v$ en a $d_v-1-\mathbf{1}_{\{u,v\}\in A}$. Le premier nombre est strictement plus grand.

Il existe donc un sommet $x$ de cet ensemble adjacent à $u$ et non adjacent à $v$.

Supprimons $\{1,v\}$ et $\{u,x\}$ et ajoutons $\{1,u\}$ et $\{v,x\}$. Les quatre sommets sont distincts et les deux nouvelles arêtes étaient absentes. Chacun des quatre degrés reste inchangé. Le sommet $1$ gagne un voisin dans $D$, contre la maximalité. **Le graphe choisi contient donc toutes les arêtes demandées.**

> [!JURY]
> Le rapport 2024 signale que cette preuve a été mal traitée et souligne les difficultés de rédaction des justifications. Pour détailler l’échange, établissez l’existence du quatrième sommet, l’absence des deux futures arêtes et la conservation de chacun des quatre degrés.

### Question 18

> [!INDICATION]
> Supprimez le sommet distingué après avoir arrangé ses voisins.

> [!INDICATION]
> Les deux blocs restent ordonnés séparément. Examinez leur frontière.

#### Solution

Dans la réalisation obtenue à la question 17, supprimons le sommet $1$. Les sommets $2$ à $d_1+1$ perdent une unité de degré et les autres conservent leur degré. À l’intérieur de chaque bloc la décroissance est préservée. À la jonction, $d_{d_1+1}>d_{d_1+2}$ entraîne $d_{d_1+1}-1\ge d_{d_1+2}$, puisque les degrés sont entiers. Chaque degré modifié est positif ou nul, les sommets concernés ayant eu le voisin $1$. **La suite réduite est donc graphique.** Si le second bloc est vide, il n’y a aucune jonction à vérifier.

> [!PIEGE]
> Les degrés retirés et les degrés décrémentés sont différents. À la jonction, exploitez le caractère entier des degrés pour transformer l’inégalité stricte en l’inégalité large utile.

### Question 19

> [!INDICATION]
> Appliquez la réduction une ligne à la fois en retriant la liste à chaque fois.

#### Solution

À chaque réduction, on enlève le premier degré, on décrémente autant de degrés suivants et on trie la suite restante. Le sens direct de Havel-Hakimi est donné dans l’énoncé. Dans l’autre sens, on peut étiqueter les sommets de manière à retrouver l’ordre avant le tri, puis ajouter un sommet relié aux sommets décrémentés. La réduction préserve donc le caractère graphique tant qu’elle peut être effectuée.

- $(4,3,3,3,3)\to(2,2,2,2)\to(2,1,1)\to(0,0)$. La dernière suite est réalisée par deux sommets isolés. **La première suite est graphique.**
- $(6,4,4,2,2,1,1)\to(3,3,1,1,0,0)\to(2,0,0,0,0)$. Un sommet de degré $2$ doit avoir deux voisins de degré positif. **La seconde suite est impossible.**

> [!METHODE]
> Arrêtez-vous soit à une suite nulle, soit quand il manque des voisins de degré positif. La somme paire fournit seulement une condition nécessaire.

### Question 20

> [!INDICATION]
> Traduisez les trois cas de la comparaison dans l’ordre souhaité pour le tri.

#### Solution

```ocaml
let compare_entiers (m : int) n =
  if m < n then 1
  else if m > n then -1
  else 0
```

> [!PIEGE]
> Le signe attendu correspond à un tri décroissant. Comparer directement les deux valeurs évite aussi le débordement d’une soustraction d’entiers.

### Question 21

> [!INDICATION]
> Utilisez la valeur de $n$ pour décider si la tête doit changer.

> [!INDICATION]
> Si la modification du suffixe échoue, propagez cet échec avec le type option.

#### Solution

Le type du premier argument est `int`. Pour respecter le seuil strict de cette question, on impose ici que les valeurs à décrémenter soient au moins égales à $2$.

```ocaml
let rec decr_prefixe minimum n l =
  if n = 0 then Some l
  else
    match l with
    | [] -> None
    | x :: suite ->
        if x < minimum then None
        else
          match decr_prefixe minimum (n - 1) suite with
          | Some suite_decr -> Some ((x - 1) :: suite_decr)
          | None -> None

let decr_n n l =
  decr_prefixe 2 n l
```

Après $n$ succès, le suffixe est rendu tel quel. Une liste trop courte ou un élément trop petit dans le préfixe donne **`None`**.

> [!PIEGE]
> L’énoncé de Q21 exige le seuil strict. La question suivante nécessite un seuil distinct, car certains degrés doivent pouvoir passer de $1$ à $0$.

### Question 22

> [!INDICATION]
> Traitez d’abord les suites où l’on peut répondre sans appliquer de réduction.

> [!INDICATION]
> Une réduction réussie produit une liste plus courte. Rétablissez la précondition du prochain appel avant de l’utiliser.

#### Solution

Dans Havel-Hakimi, un degré égal à $1$ peut être décrémenté en $0$. On emploie donc `decr_prefixe 1`, version adaptée du test de la question 21.

```ocaml
let rec tous_nuls l =
  match l with
  | [] -> true
  | x :: suite -> x = 0 && tous_nuls suite

let rec havel_hakimi l =
  match l with
  | [] -> true
  | d :: suite ->
      if d < 0 then false
      else if d = 0 then tous_nuls suite
      else
        match decr_prefixe 1 d suite with
        | None -> false
        | Some reduite ->
            havel_hakimi (List.sort compare_entiers reduite)
```

Le test des suites nulles doit précéder l’application du théorème 1. Dans ce cas, la condition $d_{d_1+1}>0$ annoncée dans le théorème est sans objet. Pour $d>0$, un échec de décrément signifie qu’il n’y a pas $d$ autres sommets de degré positif dans la suite décroissante. Pour un succès, l’équivalence justifiée à la question 19 s’applique et la longueur diminue d’une unité. Les cas terminaux sont la suite vide et les suites entièrement nulles. **La fonction termine et décide si la suite décroissante est graphique.**

> [!JURY]
> Le rapport 2024 signale que le réordonnancement a souvent été oublié ou mal appliqué. Le tri décroissant est requis à chaque appel qui suit une réduction.

### Question 23

> [!INDICATION]
> Fixez d’abord les trois voisins du sommet de degré maximal et complétez les degrés restants.

#### Solution

Sur $[5]$, considérons les ensembles d’arêtes suivants, en notant $ij$ l’arête $\{i,j\}$.

- $G_1$ a pour arêtes $12,13,15,24,34$.
- $G_2$ a pour arêtes $12,13,14,23,45$.

Dans chaque graphe, les sommets $1$ à $5$ ont respectivement les degrés **$(3,2,2,2,1)$**. Le premier graphe ne contient aucun triangle, le second contient le triangle $1,2,3$. Ils sont donc même non isomorphes.

> [!METHODE]
> Pour obtenir deux exemples vraiment différents, imposez un triangle au premier essai et excluez les triangles au second. Vérifiez ensuite le degré de chaque sommet.

## III.2 — Diagramme et tableau de Young

Un même diagramme se lit en parcourant ses lignes, ses colonnes ou les crochets issus de sa diagonale.

### Question 24

> [!INDICATION]
> La hauteur de la colonne $j$ est le nombre de lignes qui atteignent la colonne $j$.

#### Solution

La première colonne rencontre les six lignes. Les colonnes $2$, $3$ et $4$ rencontrent les deux premières lignes, et la colonne $5$ ne rencontre que la première.

$$
\boxed{\lambda^*=(6,2,2,2,1).}
$$

### Question 25

> [!INDICATION]
> Comptez les cases diagonales avant de mesurer les prolongements de chaque crochet.

#### Solution

La diagonale a deux cases puisque $\lambda_2\ge2$ et $\lambda_3<3$. Les deux premières colonnes ont $5$ et $4$ cases.

On obtient $\alpha_1=4-1=3$, $\alpha_2=3-2=1$, $\beta_1=5-1=4$ et $\beta_2=4-2=2$.

$$
\boxed{\begin{pmatrix}3&1\\4&2\end{pmatrix}.}
$$

> [!PIEGE]
> Les longueurs des bras excluent la case diagonale. La longueur de la première ligne et la hauteur de la première colonne ne sont donc pas directement les deux premières coordonnées.

## III.3 — Insertion de Schensted

L’insertion propage au plus une valeur par ligne. Le test de déplacement doit respecter les inégalités différentes dans les lignes et dans les colonnes.

### Question 26

> [!INDICATION]
> Repartez de $T_0$ avant chaque insertion.

> [!INDICATION]
> À chaque déplacement, la valeur déplacée devient celle à insérer dans la ligne suivante.

#### Solution

Les deux insertions se font séparément dans $T_0$. On ajoute la valeur en bout de ligne si aucun élément de la ligne ne lui est strictement supérieur, y compris en cas d’égalité avec le dernier élément. Cette convention est imposée par la recherche du premier élément strictement supérieur et par la croissance au sens large des lignes.

Pour $5$, la première ligne est allongée. Pour $1$, le premier $2$ de la première ligne descend dans la deuxième, où il déplace le premier $3$. Ce $3$ prolonge alors la troisième ligne.

```text
Insertion de 5      Insertion de 1
1 1 2 2 4 5        1 1 1 2 4
2 3 3              2 2 3
3                  3 3
4                  4
```

> [!JURY]
> Le rapport 2024 relève des difficultés dans cette trace. Notez les valeurs déplacées et appliquez à chaque ligne le même test strict de déplacement.

### Question 27

> [!INDICATION]
> Pour la première ligne, examinez la seule inégalité de colonne à vérifier vers le bas.

> [!INDICATION]
> Pour une ligne ultérieure, comparez la colonne du déplacement précédent à la colonne retenue dans cette ligne.

#### Solution

Pour l’appel initial, **$T$ est semi-standard, $i=1$ et $k$ est une valeur positive admissible**. Si $T$ contient $n$ cases et que l’on applique littéralement la borne de la définition 8, on impose $1\le k\le n+1$. Pour la seule propriété d’ordre, aucune borne supérieure n’est utile.

La ligne $i$ est soit existante, soit la première ligne vide. Dans un appel récursif, l’entier à insérer est celui déplacé de la ligne précédente.

En effet, si le déplacement a lieu à la colonne $j$, la ligne du dessous, lorsqu’elle possède une case en $j$, y contient une valeur strictement supérieure à l’entier déplacé. Sa première case à remplacer est donc en colonne $j'\le j$. Si elle est plus courte que $j$, la colonne choisie, éventuellement une nouvelle case, vérifie aussi $j'\le j$.

Dans la ligne supérieure, toutes les valeurs jusqu’à la colonne $j$ sont désormais plus petites que l’entier déplacé, car celui-ci a été remplacé par une valeur strictement plus petite et la ligne reste croissante. La stricte croissance au-dessus de la case traitée est ainsi préservée. Sous une case remplacée, elle est préservée parce que la valeur de la case diminue. Une case ajoutée termine une ligne et conserve la forme de partition, puisqu’elle a une case au-dessus si elle n’est pas en première ligne et qu’elle n’a pas de case en dessous. L’algorithme finit au plus tard à la première ligne vide. Il conserve toutes les entrées de $T$ et ajoute exactement l’entrée $k$.

> [!PIEGE]
> L’hypothèse que le tableau est semi-standard ne suffit pas si on commence dans une ligne quelconque. Par exemple, une insertion arbitraire dans la deuxième ligne pourrait mettre une petite valeur sous une plus grande.

### Question 28

> [!INDICATION]
> Une ligne se parcourt récursivement jusqu’au premier élément qui doit être déplacé.

> [!INDICATION]
> Lors du retour, reconstruisez le préfixe avec les valeurs conservées.

#### Solution

On traite les entrées positives de sorte que la sentinelle $0$ soit distincte de toute valeur déplacée.

```ocaml
let rec insereligne k ligne =
  match ligne with
  | [] -> (0, [k])
  | x :: suite ->
      if x > k then (x, k :: suite)
      else
        let (deplace, suite_modifiee) = insereligne k suite in
        (deplace, x :: suite_modifiee)
```

Le préfixe des valeurs inférieures ou égales à $k$ est conservé. **La première valeur strictement supérieure est déplacée, ou $k$ est ajouté en bout de ligne.**

> [!METHODE]
> Le couple rend à la fois la ligne reconstruite et l’information utile à l’étage suivant. La sentinelle a un sens grâce à la positivité des entrées.

### Question 29

> [!INDICATION]
> Traitez la première ligne à l’aide du couple calculé dans la question précédente.

#### Solution

```ocaml
type tableau = int list list

let rec insertion (k : int) (t : tableau) : tableau =
  match t with
  | [] -> [[k]]
  | ligne :: lignes ->
      let (deplace, ligne_modifiee) = insereligne k ligne in
      if deplace = 0 then ligne_modifiee :: lignes
      else ligne_modifiee :: insertion deplace lignes
```

La fonction ne descend dans les lignes suivantes que lorsqu’une valeur a été déplacée. Elle implémente l’insertion de la question 27.

> [!PIEGE]
> Une liste de lignes vide lors d’un déplacement signifie que l’on crée une ligne. Un prolongement dans la ligne courante termine l’insertion.

### Question 30

> [!INDICATION]
> Maintenez le tableau courant dans un accumulateur que le prochain élément met à jour.

#### Solution

```ocaml
let construit_tableau (l : int list) : tableau =
  let rec ajouter t valeurs =
    match valeurs with
    | [] -> t
    | k :: suite -> ajouter (insertion k t) suite
  in
  ajouter [] l
```

Après le traitement d’un préfixe, l’accumulateur contient le tableau obtenu en insérant dans l’ordre les entrées de ce préfixe. À chaque ajout, les inégalités de semi-standardité sont préservées par la question 27. On considère ici une suite d’entrées positives, comme dans le sujet. Pour une suite de longueur $n$, les entrées dans $[n]$ garantissent aussi la borne de la définition 8 pour le tableau final. Les tableaux intermédiaires peuvent avoir des entrées supérieures à leur nombre courant de cases, ce qui ne gêne pas l’insertion.

> [!PIEGE]
> Une récursion qui traite entièrement la queue avant d’insérer la tête inverse l’ordre des insertions, ce qui peut modifier le tableau obtenu.

## III.4 — Correspondance de Burge

Chaque arête fournit deux étiquettes. L’algorithme les ajoute au tableau dans deux cases associées par la forme du diagramme.

### Question 31

> [!INDICATION]
> Pour chaque arête, commencez par fixer sa plus grande extrémité.

> [!INDICATION]
> En cas d’égalité sur la ligne du haut, relisez le sens du tri sur la ligne du bas.

#### Solution

Dans chaque colonne, on place le plus grand sommet de l’arête sur la première ligne. On trie ces sommets par ordre croissant et, pour une première ligne égale, on trie ceux de la seconde ligne par ordre décroissant.

$$
\boxed{\mathcal B_G=\begin{pmatrix}2&4&5&5&6&6\\1&1&3&2&5&3\end{pmatrix}.}
$$

> [!PIEGE]
> Un croisement de traits dans la figure ne crée pas un sommet. Relevez les deux extrémités de chacun des traits.

### Question 32

> [!INDICATION]
> Exprimez la longueur de la ligne et la hauteur de la colonne à partir de leur portion après la diagonale.

#### Solution

Pour $i\in[r]$, les définitions donnent $\lambda_i=i+\alpha_i$ et $\lambda_i^*=i+\beta_i$. Or ici $\beta_i=\alpha_i+1$. D’où **$\lambda_i^*=\lambda_i+1$**.

### Question 33

> [!INDICATION]
> Distinguez le côté de la diagonale où se trouve la case.

> [!INDICATION]
> Dans chaque crochet, repérez les cases par leur distance à la diagonale et observez le décalage entre les deux bras.

#### Solution

Si $s\le t$, la case $(s,t)$ est sur le bras horizontal du crochet diagonal $s$, à distance $t-s$ de la diagonale. Sa partenaire est sous la diagonale, dans la colonne $s$, à distance $t-s+1$.

Si $s>t$, la case se trouve à distance $s-t$ sous la diagonale dans le crochet $t$. Sa partenaire est dans la ligne $t$, à distance $s-t-1$ à droite de la diagonale.

$$
\boxed{(s,t)\longmapsto
\begin{cases}
(t+1,s)&\text{si }s\le t,\\
(t,s-1)&\text{si }s>t.
\end{cases}}
$$

Ces deux règles sont inverses l’une de l’autre et la différence d’une unité entre les longueurs des bras de chaque crochet garantit que les cases désignées existent.

> [!JURY]
> Le rapport 2024 relève l’oubli du cas sous la diagonale. Vérifiez que la correspondance appliquée deux fois redonne la case de départ, y compris sur la diagonale.

### Question 34

> [!INDICATION]
> Faites une ligne de trace pour chaque colonne de la représentation de Burge.

> [!INDICATION]
> Pendant une insertion, suivez la valeur déplacée jusqu’à l’endroit où la nouvelle case apparaît. C’est à partir de cette case que vous calculez sa partenaire.

#### Solution

Pour chaque colonne de $\mathcal B_G$, on insère $v_i$ et on utilise les coordonnées de la case effectivement créée en bout de course, puis on place $u_i$ dans la case opposée. Pour chaque étape ci-dessous, les listes entre crochets représentent les lignes du tableau de Young.

- Étape 1, couple $(2,1)$. Valeurs déplacées dans l’ordre · aucune. Case créée $(1,1)$, case opposée $(2,1)$. Lignes du tableau après les deux ajouts · `[1] [2]`.
- Étape 2, couple $(4,1)$. Valeurs déplacées dans l’ordre · aucune. Case créée $(1,2)$, case opposée $(3,1)$. Lignes du tableau après les deux ajouts · `[1,1] [2] [4]`.
- Étape 3, couple $(5,3)$. Valeurs déplacées dans l’ordre · aucune. Case créée $(1,3)$, case opposée $(4,1)$. Lignes du tableau après les deux ajouts · `[1,1,3] [2] [4] [5]`.
- Étape 4, couple $(5,2)$. Valeurs déplacées dans l’ordre · $3$. Case créée $(2,2)$, case opposée $(3,2)$. Lignes du tableau après les deux ajouts · `[1,1,2] [2,3] [4,5] [5]`.
- Étape 5, couple $(6,5)$. Valeurs déplacées dans l’ordre · aucune. Case créée $(1,4)$, case opposée $(5,1)$. Lignes du tableau après les deux ajouts · `[1,1,2,5] [2,3] [4,5] [5] [6]`.
- Étape 6, couple $(6,3)$. Valeurs déplacées dans l’ordre · $5$. Case créée $(2,3)$, case opposée $(4,2)$. Lignes du tableau après les deux ajouts · `[1,1,2,3] [2,3,5] [4,5] [5,6] [6]`.

**Le dernier tableau coïncide avec celui de l’énoncé.**

> [!JURY]
> Le rapport 2024 relève des difficultés d’application du pseudo-code et indique que cette question a été globalement mal traitée. Notez à chaque étape les deux coordonnées et le tableau après les deux opérations.

### Question 35

> [!INDICATION]
> Suivez le multiensemble des entrées, indépendamment de leurs positions.

#### Solution

L’insertion de Schensted ajoute exactement une occurrence de $v_i$ et déplace éventuellement d’autres entrées sans modifier leurs multiplicités. Le placement en case opposée ajoute une occurrence de $u_i$. Chaque arête contribue ainsi une occurrence de chacune de ses extrémités. **Le nombre d’occurrences de l’entier $x$ est le degré du sommet $x$, éventuellement nul s’il est isolé.**

> [!METHODE]
> Un déplacement conserve le nombre total d’occurrences de chaque valeur. En ne comptant que les ajouts, on peut lire les degrés sans reconstituer le graphe.

## Bilan

- Pour la classification, séparez les distances calculées sur l’état courant de la modification de cet état. En C, précisez quelle structure possède les coordonnées et quelle structure ne fait que pointer vers elles.
- Pour un langage obtenu par transformations locales, isolez les invariants, construisez une forme minimale puis traduisez la caractérisation en mémoire finie. Testez votre expression et votre automate sur un mot vide et quelques mots où la décision change.
- Pour une preuve d’échange dans un graphe, choisissez d’abord ce qui doit être maximisé. Vérifiez ensuite que les nouvelles arêtes sont permises et que les degrés sont conservés. Pour la réduction de Havel-Hakimi, le cas d’échec repose sur les degrés positifs et le tri restaure l’hypothèse de récurrence.
- Pour une insertion dans un tableau, suivez la case où le déplacement s’arrête. Les deux inégalités du tableau, large en ligne et stricte en colonne, s’appuient sur le choix du premier élément strictement supérieur. Elles expliquent le sens du test bien mieux qu’une trace isolée.
