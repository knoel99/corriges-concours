# X-ENS MPI · Informatique C 2025 · Corrigé guidé

*Corrigé rédigé par IA, non officiel. Signalez toute erreur.*

**Rédaction** · GPT-6.2 Astra Ultra · vitesse non renseignée · 24 novembre 2026

## Repères

Un chemin augmentant part et arrive sur des sommets découverts. Dans la partie II, distinguer les coefficients de la matrice, les poids des chemins et la parité avant la dernière fermeture. Dans la partie III, un déterminant non nul est un certificat, tandis qu’un zéro peut dépendre du tirage.

## I · Algorithme d’Edmonds

### Question 1 · Différence de listes

**Indication.** Parcourir seulement la première liste par récursion.

#### Solution

Un élément de la première liste est conservé exactement lorsqu’il est absent de la seconde. L’ordre et les multiplicités des éléments conservés sont préservés.

```ocaml
let rec del xs ys =
  match xs with
  | [] -> []
  | x :: suite when List.mem x ys -> del suite ys
  | x :: suite -> x :: del suite ys
```

### Question 2 · Clés d’une liste d’association

**Indication.** La clé est le premier champ de chaque paire.

#### Solution

Projeter la première composante préserve l’ordre de représentation et demande un seul parcours.

```ocaml
let keys associations = List.map (fun (cle, _) -> cle) associations
```

### Question 3 · Reconnaître un couplage sur le dessin

**Indication.** Vérifier d’abord l’existence de chaque arête, puis l’unicité de chaque extrémité.

#### Solution

(1) échoue car $\{1,2\}$ n’est pas une arête du graphe. (2) est un couplage : $\{1,3\}$ et $\{0,5\}$ existent et sont disjointes. (3) échoue car $0$ appartient à deux arêtes. Le croisement des deux diagonales du dessin ne représente pas un sommet supplémentaire.

### Question 4 · Liste des sommets couverts

**Indication.** La précondition de couplage garantit déjà l’absence de doublons.

#### Solution

Chaque arête fournit ses deux extrémités. Le temps est linéaire dans le nombre d’arêtes et aucune déduplication n’est nécessaire.

```ocaml
let rec couverts = function
  | [] -> []
  | (a,b) :: reste -> a :: b :: couverts reste
```

### Question 5 · Autre couplage de cardinal maximum

**Indication.** Une borne absolue se lit sur le nombre de sommets.

#### Solution

Choisir $\{0,5\},\{1,2\},\{3,4\}$. Ces trois arêtes couvrent les six sommets. Un couplage à quatre arêtes demanderait huit sommets distincts. Le sujet emploie « maximal » au sens de **cardinal maximum** tout au long de l’épreuve.

### Question 6 · Augmenter le couplage du graphe (1)

**Indication.** Les deux extrémités à libérer sont 1 et 3.

#### Solution

Le chemin $(1,2,4,3)$ alterne une arête libre, l’arête couplée $\{2,4\}$ et une arête libre. Remplacer $\{2,4\}$ par $\{1,2\}$ et $\{3,4\}$, en conservant $\{0,5\}$. On retrouve le couplage parfait de Q5.

![Les arêtes appariées sont épaisses. La bascule sur le chemin 1, 2, 4, 3 remplace une paire par deux et couvre les six sommets.](figures/q06-augmentation.svg)

### Question 7 · Augmentation en un seul pas

**Indication.** Une arête entre deux sommets découverts est déjà un chemin augmentant.

#### Solution

Dans le dessin de droite, le couplage contient $\{0,2\},\{4,6\},\{5,7\}$. Les sommets 1 et 9 sont tous deux libres et sont adjacents. Le chemin $(1,9)$ donne le couplage $\{\{0,2\},\{1,9\},\{4,6\},\{5,7\}\}$.

### Question 8 · Effet de la différence symétrique

**Indication.** Compter séparément les incidences des deux extrémités et de chaque sommet intérieur.

#### Solution

Les deux arêtes extrêmes du chemin (éventuellement la même) sont hors du couplage, car leurs extrémités sont libres. Sur un chemin alternant et élémentaire, chaque sommet intérieur touche une arête couplée et une arête libre du chemin. La bascule les échange ; aucune arête couplée extérieure ne touche ce sommet. Chacune des deux extrémités reçoit une unique arête, et les sommets hors du chemin gardent leurs incidences. C’est bien un couplage. Si le chemin a $2q+1$ arêtes, on en retire $q$ et on en ajoute $q+1$ : le cardinal augmente exactement de un. Le cas $q=0$ couvre Q7.

### Question 9 · Séparer les arêtes alternées

**Indication.** La première arête n’est pas couplée ; la suivante l’est.

#### Solution

Le premier résultat contient les arêtes du couplage et le second les arêtes libres du chemin. Avancer d’un **sommet** à chaque étape afin de conserver le point commun de deux arêtes consécutives. La fonction auxiliaire normalise les extrémités par ordre croissant.

```ocaml
let arete a b = if a < b then (a,b) else (b,a)

let separer chemin =
  let rec visiter dedans internes externes = function
    | a :: (b :: _ as suite) ->
        let e = arete a b in
        if dedans then visiter false (e :: internes) externes suite
        else visiter true internes (e :: externes) suite
    | _ -> (List.rev internes, List.rev externes)
  in visiter false [] [] chemin
```

### Question 10 · Calculer le couplage augmenté

**Indication.** La liste des arêtes retirées et celle des arêtes ajoutées ne jouent pas le même rôle.

#### Solution

Retirer les arêtes internes à l’ancien couplage, puis former l’union avec celles qui viennent d’entrer. Les lignes utilisent les fonctions ensemblistes du sujet.

```ocaml
let augmente cpl chemin =
  let (internes, externes) = separer chemin in
  join (del cpl internes) externes
```

### Question 11 · Contracter un ensemble de sommets

**Indication.** Construire aussi la liste d’adjacence du nouveau sommet.

#### Solution

Pour un sommet avalé, ajouter à la liste de $w$ ses voisins extérieurs et éliminer les répétitions avec la fonction fournie `join`. Pour un sommet extérieur, remplacer tous ses voisins avalés par $w$ une seule fois, avec `renomme`. Les arêtes intérieures ne créent aucune boucle en $w$. Si tout le graphe est contracté, il reste $w$ isolé.

```ocaml
let contracteG graphe bourgeon w =
  let rec construire voisins_w = function
    | [] -> [(w, voisins_w)]
    | (u, voisins) :: suite ->
        if List.mem u bourgeon then
          construire (join voisins_w (del voisins bourgeon)) suite
        else
          (u, renomme voisins bourgeon w) :: construire voisins_w suite
  in construire [] graphe
```

### Question 12 · Validité de la contraction du couplage

**Indication.** Combien de sommets du cycle peuvent encore être appariés à l’extérieur ?

#### Solution

Sur le bourgeon à $2m+1$ sommets, les $m$ arêtes couplées internes couvrent exactement $2m$ sommets distincts. Seule la base peut être incidente à une arête du couplage qui sort du bourgeon. Le nouveau sommet $w$ est donc incident à au plus une arête du couplage contracté. À chaque sommet extérieur, les incidences sont conservées avec éventuellement un voisin renommé ; chaque sommet reste incident à au plus une arête. Toutes les arêtes retenues existent dans le graphe contracté.

### Question 13 · Contracter les paires du couplage

**Indication.** Après renommage, une boucle correspond à une arête avalée.

#### Solution

Renommer par $w$ chaque extrémité intérieure, éliminer les paires égales puis remettre les extrémités en ordre. La preuve de Q12 assure l’absence de doublons entre deux arêtes traversantes.

```ocaml
let contracteC cpl bourgeon w =
  let image u = if List.mem u bourgeon then w else u in
  let rec transformer = function
    | [] -> []
    | (a,b) :: suite ->
        let u, v = image a, image b in
        if u = v then transformer suite
        else arete u v :: transformer suite
  in transformer cpl
```

### Question 14 · Retrouver une étiquette dans une forêt

**Indication.** Après l’échec dans les enfants d’une racine, explorer les arbres frères.

#### Solution

La branche fructueuse ajoute l’étiquette de son parent en tête de la liste renvoyée. La racine et le sommet cherché sont inclus, même quand ils coïncident. Un parcours infructueux renvoie `None`. Chaque nœud est visité au plus une fois.

```ocaml
type arbre = N of int * foret
and foret = arbre list

let rec find foret v =
  match foret with
  | [] -> None
  | N (u, enfants) :: suivants ->
      if u = v then Some [u]
      else match find enfants v with
        | Some chemin -> Some (u :: chemin)
        | None -> find suivants v
```

### Question 15 · Ajouter un enfant aux occurrences de u

**Indication.** Recopier aussi les descendants des nœuds qui correspondent au test.

#### Solution

Chaque arbre garde sa racine et une copie de tous ses anciens enfants. Si son étiquette vaut $u$, il reçoit en plus une feuille d’étiquette $v$. Effectuer la récursion sur les seuls enfants d’origine traite correctement le cas $u=v$.

```ocaml
let rec extend foret u v =
  let modifier (N (a, enfants)) =
    let copies = extend enfants u v in
    if a = u then N (a, N (v, []) :: copies) else N (a, copies)
  in List.map modifier foret
```

### Question 16 · Pourquoi relier deux arbres donne un chemin augmentant

**Indication.** Établir l’invariant de la forêt depuis les racines découvertes.

#### Solution

Au départ les racines sont les sommets non couverts, toutes distinctes. Une extension accroche un voisin nouveau $v$ à un sommet pair $u$ par une arête libre, puis son partenaire $z$ par l’arête couplée. L’arête libre est bien hors du couplage : si $u$ est une racine il est libre ; sinon son partenaire est déjà son parent. De plus $z$ est nouveau : tout sommet couvert déjà dans la forêt y figure avec son partenaire, donc la présence antérieure de $z$ impliquerait celle de $v$. Ces propriétés garantissent l’unicité de chaque sommet dans la forêt et l’alternance de tout chemin issu d’une racine.

Deux arbres distincts ont donc des chemins racine–sommet disjoints. Leurs extrémités paires, si elles sont autres que les racines, sont atteintes par une arête couplée. L’arête $uv$ qui joint les deux arbres est nécessairement libre car tout partenaire d’un nœud couvert appartient au même arbre. Concaténer le premier chemin, $uv$ et le second chemin en sens inverse donne un chemin élémentaire alternant, de longueur positive, entre deux racines libres.

### Question 17 · Ligne 15 de la figure 1

**Indication.** La longueur de la liste des sommets est égale à la profondeur augmentée de un.

#### Solution

Une longueur de liste paire signale une profondeur impaire. Ce voisin n’apporte ni jonction entre deux sommets pairs ni nouveau sommet. Continuer avec les autres voisins.

```ocaml
aux_voisins u tl
```

### Question 18 · Lignes 17 et 18

**Indication.** Les chemins fournis par find sont tous deux dirigés depuis leur racine.

#### Solution

Les deux arbres sont distincts et l’arête $uv$ est implicite entre le dernier élément de $cu$ et le premier élément du renversé de $cv$. Construire le résultat optionnel ; l’opérateur OCaml de concaténation est `@`.

```ocaml
Some (cu @ List.rev cv)
```

### Question 19 · Extraire le bourgeon

**Indication.** La base est le dernier ancêtre commun des deux sommets.

#### Solution

Retirer le préfixe commun tout en mémorisant son dernier sommet $b$. Les deux suffixes disjoints décrivent les branches de $b$ vers $u$ et vers $v$. Avec l’arête supplémentaire $uv$, leur union avec $b$ est le bourgeon ; la représentation demandée ne prescrit aucun ordre. Si un chemin est préfixe de l’autre, le suffixe vide ne supprime pas la base. L’ancêtre de divergence est pair : un nœud impair n’a qu’un enfant, son partenaire. La longueur du cycle est donc impaire.

```ocaml
let extrait cu cv =
  let rec descend base xs ys =
    match xs, ys with
    | a :: suite_a, b :: suite_b when a = b ->
        descend a suite_a suite_b
    | _ -> base :: (xs @ ys)
  in
  match cu, cv with
  | racine :: us, _ :: vs -> descend racine us vs
  | _ -> []  (* Appel exclu pour les chemins de la figure 1. *)
```

### Question 20 · Lignes 24 à 26

**Indication.** La recherche récursive travaille sur des noms contractés.

#### Solution

Si elle échoue, l’équivalence de contraction admise prouve qu’aucune augmentation n’est possible dans le graphe courant. En cas de succès, appliquer la fonction fournie `gonfle` au graphe et au bourgeon d’origine pour ramener le chemin dans ce graphe.

```ocaml
(match recherche ng nc with
 | None -> None
 | Some ch -> Some (gonfle graphe bourgeon ch nv))
```

### Question 21 · Itération d’Edmonds

**Indication.** Le lemme de Berge fournit la condition d’arrêt exacte.

#### Solution

Le couplage vide est valide. Chaque succès de la recherche ajoute exactement une arête par Q8. Il ne peut donc y avoir plus de $\lfloor |V|/2\rfloor$ augmentations. À l’arrêt, l’absence de chemin augmentant implique la cardinalité maximum par le lemme de Berge.

```ocaml
let edmonds graphe =
  let rec iterer cpl =
    match recherche graphe cpl with
    | None -> cpl
    | Some chemin -> iterer (augmente cpl chemin)
  in iterer []
```

## II · Déterminant de Mahajan–Vinay

### Question 22 · Index d’une matrice linéarisée

**Indication.** Chaque ligne occupe n cases contiguës et les indices commencent à zéro.

#### Solution

La première case de la ligne $i$ est à l’offset $in$. Ajouter $j$ donne l’adresse demandée. La seconde fonction modifie le tableau passé par pointeur.

```c
int read_sqmatrix(int n, int *A, int i, int j) {
    return A[i*n + j];
}
void write_sqmatrix(int n, int *A, int i, int j, int val) {
    A[i*n + j] = val;
}
```

### Question 23 · Graphe pondéré d’une matrice

**Indication.** La ligne indique l’origine de l’arc, la colonne sa destination.

#### Solution

Les sommets 0 et 1 portent des boucles de poids respectifs 2 et 1. L’arc $0\to1$ pèse 3 et l’arc $1\to0$ pèse $-2$. Aucun arc de la matrice n’est nul.

![Deux sommets et les quatre arcs pondérés de la matrice. Le signe de chaque poids est conservé.](figures/q23-adjacence.svg)

### Question 24 · Marche de tête 1 et de longueur 3

**Indication.** Partir du plus petit sommet qui sera visité et le retrouver seulement à la fin.

#### Solution

La marche $1\to3\to2\to1$ utilise trois arcs du dessin. Les sommets intermédiaires sont strictement supérieurs à 1. La tête n’est reprise qu’à la fin.

### Question 25 · Lister les marches puis les suites

**Indication.** Une boucle peut répéter un sommet intérieur, mais la tête d’une marche ne doit jamais être intérieure.

#### Solution

Les marches admissibles de longueur au plus 3 sont les suivantes.

| Longueur | Marche | Poids |
|---|---|---:|
| 1 | $2\to2$ | $5$ |
| 2 | $1\to2\to1$ | $1\cdot3=3$ |
| 3 | $0\to1\to2\to0$ | $2\cdot1\cdot2=4$ |
| 3 | $1\to2\to2\to1$ | $1\cdot5\cdot3=15$ |

Pour une suite, la longueur totale doit être exactement 3 et les têtes doivent croître strictement. Il y a les deux marches de longueur 3 prises seules (poids 4 et 15), puis la marche $1\to2\to1$ suivie de $2\to2$ (poids 15). Trois fois la boucle serait interdite à cause de sa tête répétée. La somme signée vaut $4+15-15=4$.

### Question 26 · Cinq arcs à ajouter sur la figure

**Indication.** Vérifier tour à tour les arcs d’initialisation, d’extension, de changement de tête et de sortie.

#### Solution

En notant $[p,h,u,i]$ les quadruplets de la planche, il manque exactement :

| Origine | Destination | Poids |
|---|---|---:|
| $s$ | $[0,0,0,0]$ | $1$ |
| $[0,0,0,0]$ | $[0,0,1,1]$ | $3$ |
| $[0,0,0,0]$ | $[1,1,1,1]$ | $2$ |
| $[0,0,1,1]$ | $t_1$ | $-2$ |
| $[1,1,1,1]$ | $t_0$ | $1$ |

En particulier, le troisième arc ferme la boucle en 0 puis commence à la tête 1. Les chemins de poids $2$ vers $t_0$ et $-6$ vers $t_1$ donnent bien $2-(-6)=8$, le déterminant de la matrice de Q23.

![Les cinq arcs à ajouter sont en rouge. Les autres figurent déjà sur la planche. Certaines sources de la dernière couche figurent sans chemin depuis s.](figures/q26-couches.svg)

### Question 27 · D’une suite positive à un chemin vers t₀

**Indication.** Distinguer la continuation d’une marche et sa fermeture sur sa tête.

#### Solution

Dans $C=h,u_1,\dots,u_m,h$, chaque $u_j$ est strictement supérieur à $h$, et chaque arc utilisé a un coefficient non nul. Les transitions de type (2) relient donc successivement $[p,h,h,i]$ à $[p,h,u_1,i+1]$, puis jusqu’à $[p,h,u_m,i+m]$, sans modifier $p$. Les indices de couche satisfont les bornes de l’énoncé. Pour une boucle ($m=0$), ce segment ne comporte aucun arc.

Pour une suite à $k$ marches, partir de $s$ par l’arc de type (1) vers sa première tête, avec $p=n\bmod2$. Entre marches successives, l’arc final $u_m\to h$ existe et la tête suivante est strictement supérieure : la transition (3) ferme la marche, change de tête et inverse la parité. Après $n-1$ arcs consommés, il reste exactement la fermeture de la dernière marche par (4), qui inverse une dernière fois la parité. L’indice de la sortie est $(n+k)\bmod2$, donc 0 pour une suite positive. Le produit des poids est conservé, l’unique arc supplémentaire depuis $s$ ayant poids 1.

### Question 28 · Sommes de chemins par couche

**Indication.** L’arrivée sur une tête et l’arrivée strictement au-dessus de cette tête correspondent à deux types d’arcs disjoints.

#### Solution

Écrire $F_i(p,h,v)=F_A([p,h,v,i])$. Pour $i\geq1$ et $v>h$,

$$
F_i(p,h,v)=\sum_{w=h}^{n-1}F_{i-1}(p,h,w)A_{wv}.
$$

Pour $v=h$, le prédécesseur doit fermer sa marche de tête $h'<h$ avant de repartir sur la nouvelle tête :

$$
F_i(p,h,h)=\sum_{h'=0}^{h-1}\sum_{w=h'}^{n-1}F_{i-1}(1-p,h',w)A_{wh'}.
$$

Le cas $w=h'$ est indispensable pour fermer une boucle de longueur 1. Les coefficients nuls peuvent rester dans les sommes. On additionne des produits, car chaque chemin s’obtient de façon unique en ajoutant son dernier arc à un chemin de la couche précédente.

### Question 29 · Initialiser la couche zéro

**Indication.** Une seule parité peut être atteinte depuis la source.

#### Solution

La fonction `create` fournit une table nulle. Les seuls arcs de la source ont poids 1 et conduisent aux sommets $[n\bmod2,h,h,0]$. La création en $O(n^3)$ domine les $n$ écritures.

```c
Fourtable *initialise(int n) {
    Fourtable *t = create(n);
    for (int h = 0; h < n; ++h)
        write(t, 1, n % 2, h, h, 0);
    return t;
}
```

### Question 30 · Remplir la table sans construire le graphe

**Indication.** Au début d’une tête h, un accumulateur contient déjà la somme des fermetures depuis les têtes inférieures.

#### Solution

Traiter les couches croissantes. Pour $v>h$, effectuer directement la première somme de Q28. Pour $v=h$, la seconde somme se met à jour d’une tête à la suivante en ajoutant les fermetures de la tête qui vient d’être traitée. Le calcul de tous les $v>h$ demande $O(n^3)$ par couche et par parité. Les mises à jour des fermetures y ajoutent $O(n^2)$. Les deux parités et les $n$ couches donnent $O(n^4)$, avec la table $O(n^3)$ du sujet.

```c
Fourtable *remplit(int n, int *A) {
    Fourtable *t = initialise(n);
    for (int i = 1; i < n; ++i) {
        for (int p = 0; p < 2; ++p) {
            int fermetures = 0;
            for (int h = 0; h < n; ++h) {
                write(t, fermetures, p, h, h, i);
                for (int v = h + 1; v < n; ++v) {
                    int somme = 0;
                    for (int w = h; w < n; ++w)
                        somme += read(t,p,h,w,i-1)
                               * read_sqmatrix(n,A,w,v);
                    write(t,somme,p,h,v,i);
                }
                /* Les têtes suivantes pourront venir de h. */
                for (int w = h; w < n; ++w)
                    fermetures += read(t,1-p,h,w,i-1)
                                * read_sqmatrix(n,A,w,h);
            }
        }
    }
    return t;
}
```

### Question 31 · Fermer la dernière marche et calculer le déterminant

**Indication.** La parité de la couche terminale est celle d’avant l’ultime fermeture.

#### Solution

Le poids vers $t_0$ provient de $p=1$, et celui vers $t_1$ de $p=0$. Multiplier par $A_{vh}$ pour fermer la marche, puis soustraire les contributions vers $t_1$. Les $O(n^2)$ termes terminaux et la libération de la table s’ajoutent au coût $O(n^4)$ du remplissage. Pour $n=1$, on retrouve $A_{00}$. Les calculs numériques de la partie C supposent que coefficients et intermédiaires sont représentables, comme dans le modèle arithmétique de l’épreuve.

```c
int determinant(int n, int *A) {
    Fourtable *t = remplit(n, A);
    int resultat = 0;
    for (int h = 0; h < n; ++h)
        for (int v = h; v < n; ++v) {
            int difference = read(t,1,h,v,n-1) - read(t,0,h,v,n-1);
            resultat += difference * read_sqmatrix(n,A,v,h);
        }
    free(t);
    return resultat;
}
```

## III · Test probabiliste des couplages parfaits

### Question 32 · Évaluer la matrice de Tutte

**Indication.** Une variable symbolique appartient à une paire non ordonnée, donc ne doit être tirée qu’une fois.

#### Solution

Pour $i<j$, effectuer un tirage uniforme sur $\{0,\ldots,n^2\}$ lorsque l’arête existe, mettre son opposé dans la case symétrique et mettre zéro partout ailleurs. Les tirages pour les arêtes distinctes sont indépendants. Le tableau local préserve la matrice d’adjacence reçue. La construction en $O(n^2)$ précède le calcul du déterminant en $O(n^4)$.

```c
void remplir_tutte(int n, int *A, int *T) {
    for (int i = 0; i < n; ++i) {
        T[i*n+i] = 0;
        for (int j = i + 1; j < n; ++j) {
            int x = A[i*n+j] ? rand_range(n*n) : 0;
            T[i*n+j] = x;
            T[j*n+i] = -x;
        }
    }
}

int tirage_tutte(int n, int *A) {
    int T[n*n];
    remplir_tutte(n, A, T);
    return determinant(n, T);
}
```

### Question 33 · Borner strictement l’erreur du test

**Indication.** Le lemme de Schwartz–Zippel utilise le degré total et le cardinal de l’ensemble de tirage, pas le nombre de variables.

#### Solution

Si le graphe n’a aucun couplage parfait, le polynôme de Tutte est identiquement nul et chaque essai renvoie zéro. Sinon, c’est un polynôme non nul de degré total au plus $n$ par la formule des permutations. Pour $n\geq2$, la probabilité d’un zéro accidentel est au plus $n/(n^2+1)<1/n$. Avec $r$ essais indépendants, la probabilité d’une réponse fausse est donc strictement inférieure à $n^{-r}$. Un seul essai non nul certifie la réponse positive. Pour $n$ impair, répondre immédiatement faux.

Pour $p\geq1$, prendre $b=\lfloor\log_2 n\rfloor$ et $r=\lceil p/b\rceil$ donne $n^{-r}\leq2^{-p}$. La solution usuelle répète simplement Q32, en temps $O(n^4\lceil p/b\rceil)$. Le plafond compte si $p$ peut rester petit et $n$ croître : pour obtenir uniformément la borne demandée $O(pn^4/\log_2 n)$ avec les deux paramètres, le code emploie un seul déterminant cubique lorsque $p<b$. Dans cette branche un seul tirage suffit et $n^3=O(pn^4/\log_2 n)$. Pour $p\geq b$, $r\leq2p/b$ et Q32 convient. L’option $p=0$ effectue encore un essai et satisfait la borne probabiliste stricte.

Le test cubique utilise l’élimination entière de Bareiss : à chaque pivot non nul, l’identité des mineurs donne le nouveau coefficient $(a_{kk}a_{ij}-a_{ik}a_{kj})/d$, où $d$ est le pivot précédent, initialement 1. La division est exacte. Un échange de lignes permet de choisir un pivot ; son effet sur le signe est indifférent au test de non-nullité. Une colonne sans pivot prouve la singularité. En C à entiers bornés, l’arithmétique exacte de l’exercice demanderait des entiers de précision adaptée pour de grandes matrices.

```c
/* Test de non-nullité par élimination entière de Bareiss.
   Les opérations sont exactes dans le modèle de l'énoncé. */
bool tirage_rapide(int n, int *A) {
    int t[n*n];
    remplir_tutte(n, A, t);
    int precedent = 1;
    for (int k = 0; k < n-1; ++k) {
        int r = k;
        while (r < n && t[r*n+k] == 0) ++r;
        if (r == n) return false;
        if (r != k)
            for (int j = k; j < n; ++j) {
                int temporaire = t[k*n+j];
                t[k*n+j] = t[r*n+j];
                t[r*n+j] = temporaire;
            }
        int pivot = t[k*n+k];
        for (int i = k+1; i < n; ++i)
            for (int j = k+1; j < n; ++j)
                t[i*n+j] = (pivot*t[i*n+j] - t[i*n+k]*t[k*n+j])
                            / precedent;
        precedent = pivot;
    }
    return t[(n-1)*n+n-1] != 0;
}

bool parfait(int n, int *A, int p) {
    if (n % 2 != 0) return false;
    int bits = 0;
    for (int v = n; v > 1; v /= 2) ++bits;
    /* n est non nul par hypothèse, donc ici n >= 2. */
    if (p < bits) return tirage_rapide(n, A);
    int repetitions = p/bits + (p%bits != 0);
    if (repetitions == 0) repetitions = 1;
    for (int r = 0; r < repetitions; ++r)
        if (tirage_tutte(n,A) != 0) return true;
    return false;
}
```
