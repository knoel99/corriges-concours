# CCINP MPI — Informatique 2024 · Corrigé brut

*Corrigé rédigé par IA, non officiel. Signalez toute erreur.*

## Partie I — Algorithme Single Pass

### Question 1

On affecte chaque document au centre qui minimise sa distance $\delta$, puis on prend la moyenne coordonnée par coordonnée dans chaque classe. Dans l’ordre des documents, les couples de distances sont $(6,5)$, $(0,3)$, $(2,3)$, $(4,3)$, $(3,0)$ à la première itération.

À la deuxième, ils sont $(5,7/3)$, $(1,11/3)$, $(1,11/3)$, $(3,5/3)$, $(2,8/3)$.

À la troisième, ils sont $(5,1)$, $(5/3,5)$, $(5/3,5)$, $(3,1)$, $(4/3,4)$.

- Itération 1. Centres $c_1=(2,1,0)$ et $c_2=(1,0,1)$. Classes $A_1=\{d_2,d_3\}$ et $A_2=\{d_1,d_4,d_5\}$.
- Itération 2. Centres $c_1=(1,1,0)$ et $c_2=(1,2,5/3)$. Classes $A_1=\{d_2,d_3,d_5\}$ et $A_2=\{d_1,d_4\}$.
- Itération 3. Centres $c_1=(1,2/3,1/3)$ et $c_2=(1,3,2)$. Classes $A_1=\{d_2,d_3,d_5\}$ et $A_2=\{d_1,d_4\}$.

**Les classes sont stabilisées à la troisième itération.**

### Question 2

On initialise $A_1=\{d_1\}$ et $c_1=(1,3,3)$. Le minimum de l’étape (iii) porte sur les $j$ centres existants. La borne $k<i$ engloberait des centres inexistants dès que $j<i-1$.

- $d_2$. Distances avant affectation $6$. Toutes strictement supérieures à 5 ? Oui. Classe $A_2=\{d_2\}$ (création), nouveau centre $(2,1,0)$.
- $d_3$. Distances avant affectation $6,2$. Toutes strictement supérieures à 5 ? Non. Classe $A_2=\{d_2,d_3\}$, nouveau centre $(1,1,0)$.
- $d_4$. Distances avant affectation $2,3$. Toutes strictement supérieures à 5 ? Non. Classe $A_1=\{d_1,d_4\}$, nouveau centre $(1,3,2)$.
- $d_5$. Distances avant affectation $4,2$. Toutes strictement supérieures à 5 ? Non. Classe $A_2=\{d_2,d_3,d_5\}$, nouveau centre $(1,2/3,1/3)$.

**Chaque ligne modifie uniquement la classe indiquée et son centre.**

### Question 3

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

### Question 4

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

### Question 5

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

### Question 6

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

### Question 7

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

## Partie II — Langages réguliers

### Question 8

La formule imprimée autorise $ab\to ba$. À la lettre, elle relie $ab$ à $ba$ sans relier $ba$ à $ab$. Puisque $R$ est annoncée symétrique, on autorise aussi l’échange inverse.

On utilise la fermeture réflexive transitive annoncée, c’est-à-dire une chaîne de longueur finie quelconque de ces échanges adjacents. La condition $i<\min(|u|,|v|)$ de l’énoncé doit être retirée. Lue comme une borne supplémentaire sur chaque étape de la chaîne, elle bornerait le nombre de coups par la longueur du mot.

Ainsi, $aaabbb$ et $bbbaaa$ demandent neuf échanges, puisque chaque échange change d’une unité le nombre de couples formés d’un $b$ précédant un $a$. Une suite de neuf coups existe en faisant remonter les $b$ un par un. On peut donc la découper en deux chaînes de longueur au plus six, ce qui montre que la relation bornée ne serait pas transitive.

Pour $R^*$, une chaîne de longueur zéro donne la réflexivité. L’inversion d’une chaîne est possible puisque $R$ est symétrique. La concaténation de deux chaînes donne la transitivité. **$R^*$ est donc une relation d’équivalence.**

### Question 9

Une permutation adjacente conserve la longueur. La classe de $u$ est donc incluse dans l’ensemble fini $\Sigma^{|u|}$. Pour chacun de ses mots, la concaténation de ses lettres donne une expression régulière de ce singleton (avec $\varepsilon$ pour le mot vide). Leur union finie décrit exactement la classe. **Chaque classe est régulière.**

### Question 10

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

### Question 11

Dans (ii), la première différence peut se trouver à l’indice $1$. On lit donc $i\ge1$, avec un préfixe vide à cet indice. Sinon $a$ et $b$ seraient incomparables et la relation ne pourrait être totale.

Prolongeons chaque mot fini par une répétition d’un symbole de fin $\bot$, avec $\bot<a<b<c$. Deux mots distincts se comparent à leur premier indice de différence, soit un préfixe propre départagé par $\bot$, soit une différence de lettres. L’égalité entraîne la réflexivité.

Pour la transitivité, si $u\prec v$ et $v\prec w$ ont leurs premières différences en $i$ et $j$, alors les trois mots prolongés coïncident avant $\min(i,j)$.

Si $i<j$, à l’indice $i$, $u_i<v_i=w_i$. Si $j<i$, à l’indice $j$, $u_j=v_j<w_j$.

Si $i=j$, à cet indice, $u_i<v_i<w_i$.

Dans chaque cas $u\prec w$. Les cas d’égalité sont immédiats. Deux mots distincts sont comparables et le sens opposé est exclu par l’ordre sur les symboles. **$\preceq$ est donc un ordre total avec cette correction.**

Avec la borne littérale $i>1$, la réflexivité demeure. Deux mots non vides comparables doivent commencer par la même lettre, et sur chaque ensemble de mots de première lettre fixée, la relation est l’ordre lexicographique déjà étudié. Le mot vide est inférieur à tous les mots. La relation littérale est donc également transitive, mais elle ne compare pas les mots de premières lettres distinctes.

### Question 12

À l’intérieur de chaque bloc séparé par $c$, le mot minimal place tous les $a$ avant les $b$.

Les blocs $ba$ et $bab$ deviennent $ab$ et $abb$. Le représentant est **$abcabb$**.

### Question 13

Une classe est déterminée par les positions des $c$ et les effectifs de $a$ et $b$ dans chacun des blocs.

Tous les mots de la classe atteignent le même mot par échanges $ba\to ab$, jusqu’à disparition de toute inversion $b$ avant $a$ dans un bloc.

Chaque échange diminue le mot pour l’ordre lexicographique, ce qui donne son minimum. Les représentants sont donc exactement les blocs de la forme $a^*b^*$ séparés par des $c$, blocs vides compris.

$$
\boxed{L=a^*b^*(ca^*b^*)^*.}
$$

### Question 14

On part de $A$. Les états finaux sont $A$ et $B$.

L’état $A$ signifie que le bloc courant ne contient pas de $b$, $B$ qu’on a vu un $b$ dans ce bloc, et $P$ qu’une inversion a été rencontrée.

- $A$ (initial et final). Sur `a`, $A$. Sur `b`, $B$. Sur `c`, $A$.
- $B$ (final). Sur `a`, $P$. Sur `b`, $B$. Sur `c`, $A$.
- $P$. Sur `a`, $P$. Sur `b`, $P$. Sur `c`, $P$.

**L’automate est déterministe, complet et accepte exactement $L$.**

## Partie III — Correspondance de Burge

### III.1 — Partitions d’un entier

#### Question 15

Chaque arête a deux extrémités et contribue une unité au degré de chacune. Ainsi, pour tout graphe simple à $m$ arêtes,

$$
\sum_{i=1}^{l} d_i = 2m.
$$

**Une suite de somme impaire ne peut donc pas être graphique.**

#### Question 16

Partons d’un graphe simple sur les sommets $2,\ldots,l$ dont les degrés sont $d_2,\ldots,d_l$.

Ajoutons le sommet $1$ et relions-le à chacun des $d_1$ sommets de $2$ à $d_1+1$, ce qui est possible car $d_1\le l-1$. On ajoute uniquement des arêtes distinctes et sans boucle.

Le sommet $1$ a degré $d_1$, chacun de ses nouveaux voisins gagne une unité et les autres degrés restent inchangés. La suite obtenue est décroissante, notamment $d_1\ge d_2+1$. **Le graphe réalise la suite demandée.**

#### Question 17

Si $d_1=0$, la propriété est immédiate. Sinon, notons $D=\{2,\ldots,d_1+1\}$. Parmi les réalisations étiquetées de la suite, choisissons-en une où le nombre de voisins de $1$ dans $D$ est maximal.

Supposons qu’un sommet $u\in D$ ne soit pas voisin de $1$. Comme $1$ possède exactement $|D|$ voisins, il a un voisin $v\notin D$. Alors $d_u\ge d_v$.

Dans $S\setminus\{1,u,v\}$, le sommet $u$ a $d_u-\mathbf{1}_{\{u,v\}\in A}$ voisins, tandis que $v$ en a $d_v-1-\mathbf{1}_{\{u,v\}\in A}$. Le premier nombre est strictement plus grand.

Il existe donc un sommet $x$ de cet ensemble adjacent à $u$ et non adjacent à $v$.

Supprimons $\{1,v\}$ et $\{u,x\}$ et ajoutons $\{1,u\}$ et $\{v,x\}$. Les quatre sommets sont distincts et les deux nouvelles arêtes étaient absentes. Chacun des quatre degrés reste inchangé. Le sommet $1$ gagne un voisin dans $D$, contre la maximalité. **Le graphe choisi contient donc toutes les arêtes demandées.**

#### Question 18

Dans la réalisation obtenue à la question 17, supprimons le sommet $1$. Les sommets $2$ à $d_1+1$ perdent une unité de degré et les autres conservent leur degré. À l’intérieur de chaque bloc la décroissance est préservée. À la jonction, $d_{d_1+1}>d_{d_1+2}$ entraîne $d_{d_1+1}-1\ge d_{d_1+2}$, puisque les degrés sont entiers. Chaque degré modifié est positif ou nul, les sommets concernés ayant eu le voisin $1$. **La suite réduite est donc graphique.** Si le second bloc est vide, il n’y a aucune jonction à vérifier.

#### Question 19

À chaque réduction, on enlève le premier degré, on décrémente autant de degrés suivants et on trie la suite restante. Le sens direct de Havel-Hakimi est donné dans l’énoncé. Dans l’autre sens, on peut étiqueter les sommets de manière à retrouver l’ordre avant le tri, puis ajouter un sommet relié aux sommets décrémentés. La réduction préserve donc le caractère graphique tant qu’elle peut être effectuée.

- $(4,3,3,3,3)\to(2,2,2,2)\to(2,1,1)\to(0,0)$. La dernière suite est réalisée par deux sommets isolés. **La première suite est graphique.**
- $(6,4,4,2,2,1,1)\to(3,3,1,1,0,0)\to(2,0,0,0,0)$. Un sommet de degré $2$ doit avoir deux voisins de degré positif. **La seconde suite est impossible.**

#### Question 20

```ocaml
let compare_entiers (m : int) n =
  if m < n then 1
  else if m > n then -1
  else 0
```

#### Question 21

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

#### Question 22

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

#### Question 23

Sur $[5]$, considérons les ensembles d’arêtes suivants, en notant $ij$ l’arête $\{i,j\}$.

- $G_1$ a pour arêtes $12,13,15,24,34$.
- $G_2$ a pour arêtes $12,13,14,23,45$.

Dans chaque graphe, les sommets $1$ à $5$ ont respectivement les degrés **$(3,2,2,2,1)$**. Le premier graphe ne contient aucun triangle, le second contient le triangle $1,2,3$. Ils sont donc même non isomorphes.

### III.2 — Diagramme et tableau de Young

#### Question 24

La première colonne rencontre les six lignes. Les colonnes $2$, $3$ et $4$ rencontrent les deux premières lignes, et la colonne $5$ ne rencontre que la première.

$$
\boxed{\lambda^*=(6,2,2,2,1).}
$$

#### Question 25

La diagonale a deux cases puisque $\lambda_2\ge2$ et $\lambda_3<3$. Les deux premières colonnes ont $5$ et $4$ cases.

On obtient $\alpha_1=4-1=3$, $\alpha_2=3-2=1$, $\beta_1=5-1=4$ et $\beta_2=4-2=2$.

$$
\boxed{\begin{pmatrix}3&1\\4&2\end{pmatrix}.}
$$

### III.3 — Insertion de Schensted

#### Question 26

Les deux insertions se font séparément dans $T_0$. On ajoute la valeur en bout de ligne si aucun élément de la ligne ne lui est strictement supérieur, y compris en cas d’égalité avec le dernier élément. Cette convention est imposée par la recherche du premier élément strictement supérieur et par la croissance au sens large des lignes.

Pour $5$, la première ligne est allongée. Pour $1$, le premier $2$ de la première ligne descend dans la deuxième, où il déplace le premier $3$. Ce $3$ prolonge alors la troisième ligne.

```text
Insertion de 5      Insertion de 1
1 1 2 2 4 5        1 1 1 2 4
2 3 3              2 2 3
3                  3 3
4                  4
```

#### Question 27

Pour l’appel initial, **$T$ est semi-standard, $i=1$ et $k$ est une valeur positive admissible**. Si $T$ contient $n$ cases et que l’on applique littéralement la borne de la définition 8, on impose $1\le k\le n+1$. Pour la seule propriété d’ordre, aucune borne supérieure n’est utile.

La ligne $i$ est soit existante, soit la première ligne vide. Dans un appel récursif, l’entier à insérer est celui déplacé de la ligne précédente.

En effet, si le déplacement a lieu à la colonne $j$, la ligne du dessous, lorsqu’elle possède une case en $j$, y contient une valeur strictement supérieure à l’entier déplacé. Sa première case à remplacer est donc en colonne $j'\le j$. Si elle est plus courte que $j$, la colonne choisie, éventuellement une nouvelle case, vérifie aussi $j'\le j$.

Dans la ligne supérieure, toutes les valeurs jusqu’à la colonne $j$ sont désormais plus petites que l’entier déplacé, car celui-ci a été remplacé par une valeur strictement plus petite et la ligne reste croissante. La stricte croissance au-dessus de la case traitée est ainsi préservée. Sous une case remplacée, elle est préservée parce que la valeur de la case diminue. Une case ajoutée termine une ligne et conserve la forme de partition, puisqu’elle a une case au-dessus si elle n’est pas en première ligne et qu’elle n’a pas de case en dessous. L’algorithme finit au plus tard à la première ligne vide. Il conserve toutes les entrées de $T$ et ajoute exactement l’entrée $k$.

#### Question 28

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

#### Question 29

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

#### Question 30

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

### III.4 — Correspondance de Burge

#### Question 31

Dans chaque colonne, on place le plus grand sommet de l’arête sur la première ligne. On trie ces sommets par ordre croissant et, pour une première ligne égale, on trie ceux de la seconde ligne par ordre décroissant.

$$
\boxed{\mathcal B_G=\begin{pmatrix}2&4&5&5&6&6\\1&1&3&2&5&3\end{pmatrix}.}
$$

#### Question 32

Pour $i\in[r]$, les définitions donnent $\lambda_i=i+\alpha_i$ et $\lambda_i^*=i+\beta_i$. Or ici $\beta_i=\alpha_i+1$. D’où **$\lambda_i^*=\lambda_i+1$**.

#### Question 33

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

#### Question 34

Pour chaque colonne de $\mathcal B_G$, on insère $v_i$ et on utilise les coordonnées de la case effectivement créée en bout de course, puis on place $u_i$ dans la case opposée. Pour chaque étape ci-dessous, les listes entre crochets représentent les lignes du tableau de Young.

- Étape 1, couple $(2,1)$. Valeurs déplacées dans l’ordre · aucune. Case créée $(1,1)$, case opposée $(2,1)$. Lignes du tableau après les deux ajouts · `[1] [2]`.
- Étape 2, couple $(4,1)$. Valeurs déplacées dans l’ordre · aucune. Case créée $(1,2)$, case opposée $(3,1)$. Lignes du tableau après les deux ajouts · `[1,1] [2] [4]`.
- Étape 3, couple $(5,3)$. Valeurs déplacées dans l’ordre · aucune. Case créée $(1,3)$, case opposée $(4,1)$. Lignes du tableau après les deux ajouts · `[1,1,3] [2] [4] [5]`.
- Étape 4, couple $(5,2)$. Valeurs déplacées dans l’ordre · $3$. Case créée $(2,2)$, case opposée $(3,2)$. Lignes du tableau après les deux ajouts · `[1,1,2] [2,3] [4,5] [5]`.
- Étape 5, couple $(6,5)$. Valeurs déplacées dans l’ordre · aucune. Case créée $(1,4)$, case opposée $(5,1)$. Lignes du tableau après les deux ajouts · `[1,1,2,5] [2,3] [4,5] [5] [6]`.
- Étape 6, couple $(6,3)$. Valeurs déplacées dans l’ordre · $5$. Case créée $(2,3)$, case opposée $(4,2)$. Lignes du tableau après les deux ajouts · `[1,1,2,3] [2,3,5] [4,5] [5,6] [6]`.

**Le dernier tableau coïncide avec celui de l’énoncé.**

#### Question 35

L’insertion de Schensted ajoute exactement une occurrence de $v_i$ et déplace éventuellement d’autres entrées sans modifier leurs multiplicités. Le placement en case opposée ajoute une occurrence de $u_i$. Chaque arête contribue ainsi une occurrence de chacune de ses extrémités. **Le nombre d’occurrences de l’entier $x$ est le degré du sommet $x$, éventuellement nul s’il est isolé.**

FIN
