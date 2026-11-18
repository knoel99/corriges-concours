# CCINP MP — Informatique 2025 · Corrigé guidé

*Corrigé rédigé par IA, non officiel. Signalez toute erreur.*

## Présentation du sujet

L’épreuve dure quatre heures, sans calculatrice. Elle étudie le partage d’un réseau entre deux opérateurs. Les parties I et V relèvent du tronc commun informatique MP, les parties II à IV de l’option informatique. Le sujet autorise l’emploi des résultats et des fonctions des questions précédentes, même si vous les avez admis.

- **Q1–Q3.** Interroger le réseau en SQL. Cette partie est indépendante.
- **Q4–Q25.** Établir les propriétés de l’arbre couvrant de poids maximal, puis mettre en œuvre Borůvka en OCaml.
- **Q26–Q28.** Relier l’arbre couvrant maximal à la bande passante d’un chemin et du réseau.
- **Q29–Q38.** Analyser le jeu de partage, coder ses transitions et en calculer les scores en Python. La partie V fournit les primitives qui permettent d’avancer même en ayant admis des résultats précédents.

[Sujet officiel](https://www.concours-commun-inp.fr/_resource/annales%20%C3%A9crits/2025/MP/Informatique_2025.pdf) · [Rapport du jury](https://www.concours-commun-inp.fr/_resource/annales%20%C3%A9crits/2025/MP/MP_ECRIT_Informatique%202025_10.pdf) · [BO du tronc commun](https://www.education.gouv.fr/bo/21/Special1/ESRS2035774A.htm) · [BO de l’option](https://www.education.gouv.fr/bo/21/Special1/ESRS2035775A.htm)

## Partie I — Base de données du réseau

Distinguez les identifiants des noms de ville et les résultats demandés en lignes des conditions utilisées pour les produire.

### Question 1

> [!INDICATION]
> Pour chaque table, cherchez ce qui distingue deux lignes. Dans quelle table retrouve-t-on les deux identifiants d’une liaison ?

#### Solution

La clé primaire de `villes` est `id`, identifiant unique d’une ville. La clé primaire de `liaisons` est le couple `(id1, id2)`. Chaque paire de villes est reliée par au plus une liaison et l’ordre `id1 < id2` fixe son écriture. Les attributs `id1` et `id2` sont séparément des clés étrangères qui référencent `villes(id)`.

> [!JURY]
> Le jury rappelle que l’unicité des bandes passantes intervient plus tard. La clé de liaisons combine les deux identifiants.

### Question 2

> [!INDICATION]
> Pour (a), traduisez strictement le seuil. Pour (b), distinguez les deux positions possibles de l’identifiant. Pour (c), séparez le calcul du maximum et la récupération des noms.

#### Solution

**(a)** Le seuil de cinq millions est strict.

```sql
SELECT nom
FROM villes
WHERE pop > 5;
```

**(b)** L’identifiant peut se trouver dans l’une ou l’autre colonne de la liaison.

```sql
SELECT AVG(bp)
FROM liaisons
WHERE id1 = 2 OR id2 = 2;
```

**(c)** On joint deux fois la table des villes, une fois par extrémité. Les bandes passantes étant distinctes, il y a au plus une liaison source.

```sql
SELECT v1.nom, v2.nom
FROM liaisons AS l
JOIN villes AS v1 ON v1.id = l.id1
JOIN villes AS v2 ON v2.id = l.id2
WHERE l.bp = (SELECT MAX(bp) FROM liaisons);
```

### Question 3

> [!INDICATION]
> Quel couple produit chacune des deux branches de l’union pour une même liaison ?

> [!INDICATION]
> Après la jointure, comptez les occurrences de chaque identifiant sur les données de la figure 3.

#### Solution

Les deux branches du `UNION` produisent les deux orientations de chaque arête. Le groupement par `id` compte donc le degré de chaque ville présente dans la jointure. Après filtrage des degrés au moins égaux à quatre et tri par identifiant, le résultat est

```text
nom            d
Lurenberg      4
Veroja         4
Aschlöss       6
Gossard        4
Sainte Marie   4
Gasparländ     4
```

> [!JURY]
> Le jury attend les lignes du résultat et leur ordre exact. Une description de la requête ne suffit pas.

## Partie II — Arbre couvrant de poids maximal

Les preuves utilisent les deux inégalités de la proposition 1 à des moments différents. Le nombre d’arêtes et les cycles guideront les échanges.

### II.1 — Acyclicité, connexité et arbres

### Question 4

> [!INDICATION]
> Considérez un chemin entre deux sommets quelconques. Que permet la partie du cycle qui subsiste après la suppression ?

#### Solution

Soient $s,t$ deux sommets quelconques. Fixons un chemin entre eux dans $G$. La suppression de $a=\{x,y\}$ laisse un chemin de $x$ à $y$ le long du reste du cycle.

Dans le chemin initial, remplaçons chaque traversée de $a$ par ce détour, orienté dans le sens de la traversée. On obtient un chemin de $s$ à $t$ dans $G-a$. Ce graphe est donc connexe.

> [!JURY]
> Le rapport demande de raisonner sur des sommets quelconques et de remplacer toutes les traversées d’une arête supprimée.

### Question 5

> [!INDICATION]
> Supposez qu’un cycle existe et combinez Q4 avec la borne pour les graphes connexes.

#### Solution

Si $G$ avait un cycle, la suppression d’une de ses arêtes laisserait, par Q4, un graphe connexe sur $|S|$ sommets ayant $|S|-2$ arêtes. Cela contredit la proposition 1(a). Ainsi $G$ est connexe et acyclique, donc c’est un arbre.

### II.2 — Sous-graphe et arbre couvrant

### Question 6

> [!INDICATION]
> Dans le sens direct, considérez les sous-graphes connexes sur S. Quelle grandeur entière pouvez-vous minimiser ?

#### Solution

Si $G$ est connexe, parmi ses sous-graphes connexes sur $S$, il en existe un de cardinal d’arêtes minimal, puisque l’ensemble est fini et contient $G$. Ce sous-graphe est acyclique. Dans le cas contraire, Q4 permettrait d’y retirer une arête en conservant la connexité. C’est donc un arbre couvrant. Réciproquement, les chemins de tout arbre couvrant de $G$ sont des chemins de $G$ et relient tous les sommets.

> [!JURY]
> Le rapport attend un argument de finitude pour la suppression des cycles. Choisir un sous-graphe connexe minimal est une manière directe de le fournir.

### Question 7

> [!INDICATION]
> Dans (a), comptez les arêtes avant et après l’ajout. Dans (b), raisonnez sur la connexité et le nombre d’arêtes après le retrait.

#### Solution

**(a)** Par les deux inégalités de la proposition 1, $T$ a $|S|-1$ arêtes. Comme $a$ est absente de $T$, le graphe $T+a$ en a $|S|$. Il ne peut donc pas être acyclique.

**(b)** $T+a$ est connexe, et enlever $a'$ d’un de ses cycles conserve la connexité par Q4. Le résultat est un sous-graphe de $G$ sur $S$ à $|S|-1$ arêtes. Par Q5, c’est un arbre couvrant.

### II.3 — Graphes pondérés et arbre couvrant de poids maximal

### Question 8

> [!INDICATION]
> Quelles sont les deux propriétés de l’ensemble des arbres couvrants qui garantissent l’existence d’un maximum ?

#### Solution

Par Q6, l’ensemble des arbres couvrants est non vide. Il est fini car leurs ensembles d’arêtes sont des parties de $A$. Leurs poids forment donc une partie finie non vide de $\mathbb R$, qui admet un maximum, atteint par au moins un arbre couvrant.

> [!JURY]
> Le jury distingue la preuve d’existence du futur algorithme de construction. La finitude des arbres couvrants suffit.

### Question 9

> [!INDICATION]
> Dans le cycle créé par l’ajout, que se passerait-il si toutes les arêtes appartenaient au second arbre ?

> [!INDICATION]
> Appliquez Q7 à l’échange. Comparez ensuite les poids grâce au choix dans la différence symétrique.

#### Solution

**(a)** Par Q7(a), $T^1+a_2$ a un cycle. Il contient $a_2$, car $T^1$ est acyclique.

Si toutes ses autres arêtes appartenaient à $A_2$, elles formeraient avec $a_2$ un cycle de $T^2$. Il existe donc sur ce cycle une arête $a_1\in A_1\setminus A_2$.

**(b)** Q7(b) garantit que $T^1+a_2-a_1$ est couvrant. Par le choix de $a_2$ dans la différence symétrique et l’injectivité, $p(a_2)>p(a_1)$. L’échange augmente strictement le poids de $T^1$, contradiction. L’arbre couvrant maximal est unique.

## Partie III — Recherche d’un arbre couvrant de poids maximal

Les structures sont les tableaux et listes d’adjacence de l’énoncé. La sûreté d’une arête se juge pour une composante de la forêt en cours.

### III.1 — Rappels et fonctions élémentaires en OCaml

### Question 10

> [!INDICATION]
> Choisissez une valeur initiale qui convient aussi pour un tableau dont toutes les valeurs sont négatives.

#### Solution

```ocaml
let max_tab (a : int array) : int =
  let meilleur = ref a.(0) in
  for i = 1 to Array.length a - 1 do
    meilleur := max !meilleur a.(i)
  done;
  !meilleur
```

Après l’indice $i$, la référence contient le maximum des cases $0$ à $i$. Les $n-1$ itérations ont chacune un coût constant, donc le temps est $\Theta(n)$.

### III.2 — Représentation des graphes en OCaml

### Question 11

> [!INDICATION]
> Dans la figure 3, relevez toutes les lignes où 7 apparaît dans l’une des deux colonnes d’identifiants.

#### Solution

Une valeur possible est `[(0, 18.0); (8, 19.0)]`.

### Question 12

> [!INDICATION]
> Combien de listes faut-il modifier ? Préférez une opération dont le temps est indépendant de leur taille.

#### Solution

```ocaml
let ajoute_arete (g : graphe) ((w, i, j) : float * int * int) : unit =
  g.(i) <- (j, w) :: g.(i);
  g.(j) <- (i, w) :: g.(j)
```

Les deux insertions en tête maintiennent la symétrie, en temps constant.

> [!JURY]
> Le rapport insiste sur la symétrie des listes d’adjacence et le temps constant. Une concaténation en fin de liste peut parcourir toute la liste.

### Question 13

> [!INDICATION]
> Parcourez chaque case. Parmi les deux orientations d’une liaison, imposez celle fixée par la représentation en triplet.

> [!INDICATION]
> Une référence vers la liste résultat permet l’ajout en tête pendant le parcours.

#### Solution

```ocaml
let toutes_les_aretes (g : graphe) : (float * int * int) list =
  let resultat = ref [] in
  for i = 0 to Array.length g - 1 do
    List.iter
      (fun (j, w) ->
        if i < j then resultat := (w, i, j) :: !resultat)
      g.(i)
  done;
  !resultat
```

La condition $i<j$ conserve une seule orientation. On examine les $|S|$ cases et les $2|A|$ entrées d’adjacence, avec un coût constant par entrée. Le temps est $\Theta(|S|+|A|)$.

> [!JURY]
> Le jury signale l’oubli fréquent de la condition d’ordre sur les extrémités. Comptez les deux entrées lues par arête et l’unique triplet produit.

### Question 14

> [!INDICATION]
> Commencez par le motif d’une liste à un élément. Pour une liste plus longue, comparez la tête et le minimum de la queue.

#### Solution

```ocaml
let rec min_arete (aretes : (float * int * int) list) :
    float * int * int =
  match aretes with
  | [] -> failwith "min_arete : liste vide"
  | [a] -> a
  | a :: reste -> min a (min_arete reste)
```

Le minimum est comparé par poids en premier, grâce à l’ordre des triplets du sujet. Pour une liste de longueur $r\geq1$, la récursion dépile $r-1$ cons et chaque comparaison coûte un temps constant, d’où $\Theta(r)$.

### III.3 — Recherche des composantes connexes

### Question 15

> [!INDICATION]
> Repérez le test avant la visite et le moment où l’indice k est inscrit. Quels effets un sommet déjà marqué peut-il avoir sur la propagation ?

#### Solution

Si `c.(s) >= 0`, l’appel ne fait rien. Sinon, il marque `s` avec l’indice `k` puis se propage à travers les listes d’adjacence, en marquant chaque sommet avant d’explorer ses voisins. Il affecte donc `k` exactement aux sommets atteignables depuis `s` par un chemin entièrement composé de sommets initialement non visités. Les cases déjà non négatives sont préservées. Dans la recherche des composantes, les visites précédentes ont marqué des composantes entières. Un nouveau départ non visité repère donc toute sa composante.

### Question 16

> [!INDICATION]
> Parcourez les sommets. Incrémentez un compteur de composante seulement lorsque vous trouvez un sommet encore non marqué.

#### Solution

```ocaml
let composantes_connexes (g : graphe) : int array =
  let c = Array.make (Array.length g) (-1) in
  let k = ref 0 in
  for s = 0 to Array.length g - 1 do
    if c.(s) < 0 then begin
      explorer g c !k s;
      k := !k + 1
    end
  done;
  c
```

L’identifiant ne progresse qu’après la découverte d’une composante, d’où les indices successifs $0,\ldots,p-1$. Chaque sommet déclenche au plus un parcours de sa liste d’adjacence, ce qui donne $O(|S|+|A|)$.

> [!JURY]
> Le rapport demande que la numérotation des composantes soit consécutive.

### Question 17

> [!INDICATION]
> Quelle valeur maximale peut avoir le tableau des indices lorsque le graphe est connexe ?

#### Solution

```ocaml
let est_connexe (g : graphe) : bool =
  max_tab (composantes_connexes g) = 0
```

Le graphe a au moins un sommet. Les composantes sont numérotées de $0$ à $p-1$, donc le maximum vaut zéro exactement quand $p=1$.

### III.4 — Algorithme de Borůvka

### Question 18

> [!INDICATION]
> Écartez d’abord les arêtes dont les deux extrémités sont dans la composante.

#### Solution

Pour $\{3\}$, l’arête sûre est $\{1,3\}$, de poids $17$, devant les arêtes de poids $9$ et $11$.

Pour $\{7,8\}$, c’est $\{0,7\}$, de poids $18$, devant les arêtes sortantes de poids $16,11,6$. L’arête de poids $19$ est interne à cette composante.

> [!PIEGE]
> Une liaison plus rapide entièrement interne à la composante ne peut pas être une arête sûre de cette composante.

### Question 19

> [!INDICATION]
> Ajoutez au maximum couvrant une arête sûre qui lui manquerait. Quelles arêtes du cycle sont susceptibles de franchir la même coupe ?

> [!INDICATION]
> Trouvez un échange qui préserve le caractère couvrant et comparez les deux poids.

#### Solution

Soit $a$ l’arête sûre de la composante $C$ de $H$. Si $a\notin A^*$, le graphe $T^*+a$ possède un cycle qui contient $a$.

En ôtant $a$ du cycle, on obtient un chemin dont une extrémité est dans $C$ et l’autre en dehors. Une autre arête $b\in A^*$ franchit donc la coupe. Comme $a$ est sûre et les poids sont distincts, $p(b)<p(a)$.

Par Q7, $T^*+a-b$ est couvrant et de poids strictement supérieur à $T^*$. Cela contredit sa maximalité.

### Question 20

> [!INDICATION]
> Pour chaque tour, figez le partitionnement avant de choisir les arêtes. Mettez-le à jour après tous les choix.

#### Solution

Les poids étant distincts, le poids indique l’arête sans ambiguïté. À chaque tour, les composantes sont celles du graphe au début du tour.

**Tour 1.** Pour les singletons de $\{0\}$ à $\{8\}$, les poids sûrs sont respectivement $24,17,24,17,23,23,22,19,19$. On ajoute les arêtes de poids $24,17,23,22,19$.

Les composantes deviennent $\{0,2,6\}$, $\{1,3\}$, $\{4,5\}$ et $\{7,8\}$.

**Tour 2.** Dans cet ordre, les poids sûrs sont $18,13,13,18$. On ajoute les arêtes de poids $18$ et $13$. Il reste $\{0,2,6,7,8\}$ et $\{1,3,4,5\}$.

**Tour 3.** L’arête sûre est celle de poids $11$ pour chacune des deux composantes. On l’ajoute et $H$ devient connexe.

> [!JURY]
> Le rapport attend les trois tours distincts, avec une arête identifiée pour chaque composante avant de dédupliquer les ajouts.

### Question 21

> [!INDICATION]
> Réfléchissez à l’effet d’au moins une arête sûre sur le nombre de composantes.

#### Solution

Le nombre de composantes connexes de $H$, diminué de $1$, est un variant entier positif ou nul. Quand $H$ est non connexe, la connexité de $G$ assure qu’au moins une arête sûre relie deux composantes de $H$. Elle les fusionne, et les autres ajouts ne peuvent pas augmenter le nombre de composantes. Le variant décroît donc strictement à chaque tour.

### Question 22

> [!INDICATION]
> Quel invariant portant sur l’ensemble d’arêtes de H découle de Q19 ? Combinez-le avec le test d’arrêt.

#### Solution

L’invariant est $B\subseteq A^*$. Il est initialement vrai car $B$ est vide. S’il est vrai avant un tour, $H$ est acyclique et Q19 assure que toutes les arêtes ajoutées appartiennent à $A^*$.

À la fin, $H$ est connexe, donc possède au moins $|S|-1$ arêtes par la proposition 1(a). Comme elles appartiennent à $A^*$, qui en possède exactement $|S|-1$, on a $B=A^*$.

> [!JURY]
> Le rapport distingue la preuve de terminaison et la preuve de correction. Pour la correction, formulez l’invariant utilisé dès le départ.

### Question 23

> [!INDICATION]
> Quels indices désignent les cases du résultat ? Pour chaque case, quelles arêtes entrent effectivement en comparaison ?

> [!INDICATION]
> Additionnez les coûts de chaque parcours, en tenant compte des arêtes de H et du lien entre la taille des sommets et celle des arêtes.

#### Solution

Le type est `graphe -> graphe -> (float * int * int) array`. Le résultat est un tableau de longueur $p$, nombre de composantes de $H$. Sa case $k$ contient l’arête sûre de la composante d’indice $k$. Le même triplet peut apparaître dans deux cases.

Pour une composante, la case est initialisée à la plus petite arête de $G$. Le parcours compare ensuite cette case seulement aux arêtes qui franchissent la coupe. Il en existe au moins une par connexité de $G$ et la valeur initiale est inférieure ou égale à chacune. À la fin, la case contient donc exactement le maximum des arêtes sortantes.

L’étiquetage des composantes coûte $O(|S|+|B|)$, la recherche du nombre de composantes et l’initialisation coûtent $O(|S|)$, et l’énumération des arêtes de $G$ coûte $\Theta(|S|+|A|)$. Le minimum initial et le parcours des arêtes coûtent chacun $\Theta(|A|)$.

Comme $|B|\leq|A|$ et $|S|\leq|A|+1$, l’ensemble coûte $\Theta(|A|)$ dans cette sous-question, où $H$ non connexe implique $|A|\geq1$.

> [!METHODE]
> Pour prouver ce que contient une case, suivez-la pendant le parcours. Elle emmagasine dès la première arête sortante le maximum des candidates vues.

### Question 24

> [!INDICATION]
> Reprenez le pseudocode. Quel tableau doit représenter le sous-graphe au départ et lequel faut-il tester dans la boucle ?

#### Solution

```ocaml
let borukva (g : graphe) : graphe =
  let h = Array.make (Array.length g) [] in
  while not (est_connexe h) do
    let sures = aretes_sures g h in
    ajoute_aretes_sures h sures
  done;
  h
```

Le tableau `h` est distinct de `g`. La fonction fournie élimine les doubles ajouts éventuels.

### Question 25

> [!INDICATION]
> Combien d’anciennes composantes faut-il au minimum pour former chaque nouvelle composante ?

> [!INDICATION]
> Multipliez le coût d’un passage par le nombre de divisions possibles. Pour le meilleur cas, cherchez un graphe dont les arêtes sont presque toutes imposées par des sommets de degré un.

#### Solution

**(a)** Au début d’un tour, supposons qu’il y ait $p>1$ composantes. Chacune est incidente à l’arête sûre qu’elle choisit et est donc fusionnée avec au moins une autre. Chaque nouvelle composante regroupe au moins deux anciennes composantes. Il en reste au plus $\lfloor p/2\rfloor$.

**(b)** Il y a au plus $\lfloor\log_2|S|\rfloor$ tours. Un tour, test de connexité compris, coûte $O(|A|)$ d’après Q23 et les coûts de `est_connexe` et d’`ajoute_aretes_sures`. L’initialisation et le dernier test coûtent également $O(|A|)$ pour $|S|\geq2$. La borne au pire cas est $O(|A|\log |S|)$.

Cette borne peut être atteinte. Sur un chemin de $2^r$ sommets consécutifs, numérotons l’arête séparant les sommets $i-1$ et $i$ par $i$.

Attribuons des poids distincts, ceux des indices divisibles par $2^j$ mais pas par $2^{j+1}$ étant tous supérieurs à ceux des indices divisibles par $2^{j+1}$.

À partir de blocs contigus de taille $2^j$, chaque bloc choisit la frontière qui le sépare de son voisin dans la même paire de blocs. Son indice est divisible par $2^j$ mais pas par $2^{j+1}$. Ainsi chaque tour double la taille des blocs et il y a $r$ tours, chacun parcourant toutes les arêtes de $G$.

**(c)** Dans une étoile, chaque feuille choisit son unique arête, ce qui achève l’algorithme en un tour. Pour $|S|\geq2$, au moins un tour est nécessaire et parcourt toutes les arêtes. Le meilleur cas est donc $\Theta(|A|)$. Pour un singleton, le temps est constant et la boucle est vide.

> [!JURY]
> Le rapport attend une justification de la réduction du nombre de composantes puis une combinaison des coûts des fonctions appelées.

## Partie IV — Chemin de bande passante maximale

Le poids d’un arbre est une somme, tandis que la bande passante d’un chemin est fixée par l’arête la plus faible.

### Question 26

> [!INDICATION]
> Après avoir trouvé un bon chemin, essayez de montrer que supprimer toutes les arêtes de poids au plus égal à sa bande passante déconnecte les extrémités.

#### Solution

Le chemin $0,7,8,3,1$ emprunte les arêtes de poids $18,19,11,17$, donc sa bande passante vaut **$11\,\mathrm{Tb\,s^{-1}}$**.

La coupe qui sépare $\{0,2,6,7,8\}$ de $\{1,3,4,5\}$ doit être franchie par tout chemin de $0$ à $1$. Les arêtes de cette coupe ont pour poids $4,7,8,9,11,5$. Aucune ne dépasse $11$.

### Question 27

> [!INDICATION]
> Isolez le cas du chemin vide. Dans l’autre cas, retirez du chemin de l’arbre une arête qui réalise sa bande passante.

> [!INDICATION]
> Un chemin strictement meilleur traverse la coupe créée. Examinez l’effet d’un échange sur le poids de l’arbre.

#### Solution

Si $x=y$, le chemin vide a une bande passante $+\infty$, donc il est optimal. Si $x\ne y$, soit $a$ une arête de poids minimal sur le chemin élémentaire entre ces sommets dans $T^*$.

Retirer $a$ sépare $T^*$ en deux composantes, l’une contenant $x$, l’autre $y$. Les extrémités de l’arête ne peuvent rester reliées sans former un cycle avec elle. Tout sommet reste relié à l’une des deux extrémités.

Si un chemin dans $G$ avait une bande passante strictement supérieure à $p(a)$, il franchirait la coupe par une arête $b$ de poids $p(b)>p(a)$.

Le graphe $T^*-a+b$ serait connexe sur $S$ à $|S|-1$ arêtes, donc couvrant par Q5. Son poids serait strictement supérieur à celui de $T^*$. Contradiction.

> [!METHODE]
> Dans un problème de bande passante, une coupe fournit une borne supérieure sur la capacité de tout chemin qui la traverse.

### Question 28

> [!INDICATION]
> Cherchez d’abord une borne valable pour tous les couples. Quel couple force l’égalité lorsque l’arbre possède au moins une arête ?

#### Solution

Si $G$ n’est pas connexe, deux sommets de composantes différentes ont $b_{\max}(x,y)=-\infty$, donc $b_{\lim}(G)=-\infty$.

Si $G$ est connexe et possède au moins deux sommets, posons $w_*=\min_{a\in A^*}p(a)$. Par Q27, chaque couple est relié avec une bande passante maximale au moins égale à $w_*$.

Si $a_*$ est une arête de $T^*$ de poids $w_*$, le chemin de $T^*$ entre ses deux extrémités se réduit à cette arête. Q27 donne alors l’égalité, et $b_{\lim}(G)=w_*$.

Pour un singleton, l’unique couple utilise le chemin vide. Alors $b_{\lim}(G)=+\infty$. La formule donnée s’étend à ce cas avec la convention $\min\varnothing=+\infty$ dans les réels étendus.

> [!JURY]
> Pour obtenir un minimum exact, il faut en particulier exhiber un couple qui atteint la valeur annoncée.

## Partie V — Jeu sur un graphe

Les sommets sont communs aux deux sous-graphes. Une configuration ajoute aux choix d’arêtes l’identité du prochain joueur.

### V.1 — Procédure de partage vue comme un jeu

### Question 29

> [!INDICATION]
> Comptez ce qu’il reste à attribuer avant et après chaque choix.

#### Solution

Le nombre d’arêtes non attribuées est un entier positif ou nul. Un coup le diminue exactement de $1$, et quand il est strictement positif, un coup reste possible. Toute partie compte donc exactement $|A|$ coups.

### Question 30

> [!INDICATION]
> Séparez les cas suivant le nombre de sous-graphes connexes. Lorsque les deux sont connexes, de quelles arêtes proviennent les deux valeurs ?

> [!INDICATION]
> Vérifiez aussi le cas limite où l’arbre couvrant n’a aucune arête.

#### Solution

Pour $|S|\geq2$, si un joueur seul a un sous-graphe connexe, sa bande passante limite est finie et celle de l’autre vaut $-\infty$. Si les deux sous-graphes sont connexes, leurs bandes passantes limites sont, par Q28, des poids d’arêtes appartenant à des ensembles disjoints. Comme les poids sont injectifs, ces valeurs sont différentes. Il y a donc égalité exactement quand les deux sous-graphes sont non connexes.

Si l’on inclut le graphe à un seul sommet permis par la définition générale, le jeu est immédiatement nul avec deux sous-graphes connexes et une bande passante $+\infty$ de chaque côté. La conclusion demandée suppose donc au moins deux villes.

### Question 31

> [!INDICATION]
> Réutilisez la figure 5. Comment le second joueur peut-il inciter le glouton à laisser un sommet isolé ?

#### Solution

Sur le graphe complet pondéré de la figure 5, considérons la suite de poids choisis $8,2,7,5,6,3$, avec MaxDébit en premier. Ses choix $8,7,6$ sont à chaque fois maximaux parmi les arêtes restantes. Ils forment le triangle $\{1,3\},\{0,3\},\{0,1\}$, qui isole le sommet 2.

MinLatence obtient les poids $2,5,3$, c’est-à-dire l’étoile de centre $2$. Sa bande passante limite vaut $2$ et celle de MaxDébit vaut $-\infty$. La stratégie gloutonne peut donc perdre.

> [!JURY]
> Les deux sous-graphes contiennent tous les sommets du graphe initial. Le rapport demande de compter aussi les sommets isolés.

### V.2 — Implémentation en Python

### Question 32

> [!INDICATION]
> Quelle valeur caractérise une arête libre dans la liste d’état ?

#### Solution

```python
def finale(c):
    _, etat = c
    for valeur in etat:
        if valeur == 0:
            return False
    return True
```

### Question 33

> [!INDICATION]
> Créez une nouvelle liste pour chaque arête libre, puis basculez le signe du joueur courant.

#### Solution

```python
def configurations_suivantes(c):
    t, etat = c
    resultat = []
    for k in range(len(etat)):
        if etat[k] == 0:
            suivant = etat.copy()
            suivant[k] = t
            resultat.append((-t, suivant))
    return resultat
```

Chaque copie correspond à une arête libre, attribuée au joueur courant. Le tour change de signe et la liste initiale reste intacte.

> [!JURY]
> Le jury relève les mutations de la liste initiale. Une copie différente est nécessaire pour chaque successeur.

### V.3 — Calcul des attracteurs

### Question 34

> [!INDICATION]
> Interprétez chaque valeur du point de vue de ce qu’un joueur peut garantir face aux réponses adverses.

#### Solution

- **Score $1$.** La configuration appartient à l’attracteur des finales gagnantes de MaxDébit. Il peut forcer la victoire quelles que soient les réponses de MinLatence.
- **Score $-1$.** Symétriquement, MinLatence peut forcer la victoire. La configuration appartient à son attracteur.
- **Score $0$.** Chaque joueur dispose d’une stratégie qui lui garantit au moins le nul et aucun ne peut forcer la victoire. Si les deux jouent de manière optimale, la partie est nulle. Une erreur peut permettre une victoire.

Cela se lit par récurrence sur le nombre d’arêtes libres. MaxDébit choisit un maximum des scores des successeurs et MinLatence choisit un minimum.

> [!JURY]
> Le jury attend le vocabulaire des attracteurs. Un score nul est compatible avec une victoire si l’adversaire commet une erreur.

### Question 35

> [!INDICATION]
> Interprétez la règle du maximum au tour de MaxDébit et celle du minimum au tour adverse, à score fixé.

#### Solution

À chaque configuration atteinte de score $1$ contrôlée par MaxDébit, il choisit un successeur de score $1$, dont l’existence découle de la règle du maximum. À une configuration de score $1$ contrôlée par MinLatence, tous les successeurs ont score $1$, car leur minimum vaut $1$. Il suffit donc de prélever un tel choix pour chacune des positions pertinentes de MaxDébit.

### V.4 — Mémoïsation

### Question 36

> [!INDICATION]
> Fabriquez la clé avec la fonction du sujet. Cherchez quels appels doivent eux-mêmes utiliser le cache.

> [!INDICATION]
> Faites suivre les cas terminal et non terminal par une mise en cache commune.

#### Solution

On utilise `finale` de Q32, qui est la fonction appelée `est_finale` dans l’extrait de la fonction `score` du sujet. Le cache est associé à un graphe fixé et se vide avant de traiter un autre graphe.

```python
cache = {}

def score_memo(g, c):
    cle = fige(c)
    if cle not in cache:
        if finale(c):
            resultat = gagnant(g, c)
        else:
            t, _ = c
            scores = [score_memo(g, suivant)
                      for suivant in configurations_suivantes(c)]
            if t == 1:
                resultat = max(scores)
            else:
                resultat = min(scores)
        cache[cle] = resultat
    return cache[cle]
```

> [!JURY]
> Les appels récursifs doivent également employer la version mémoïsée. Le rapport signale aussi les caches qui ne contiennent que les finales.

### V.5 — MinMax avec heuristique et profondeur limitée

### Question 37

> [!INDICATION]
> Il y a deux raisons de s’arrêter. La valeur exacte d’une finale est-elle disponible si le budget de profondeur est épuisé ?

#### Solution

```python
def score_minmax(g, c, p):
    if finale(c):
        return gagnant(g, c)
    if p == 0:
        return heuristique(g, c)
    t, _ = c
    scores = [score_minmax(g, suivant, p - 1)
              for suivant in configurations_suivantes(c)]
    if t == 1:
        return max(scores)
    return min(scores)
```

Une configuration finale est évaluée exactement même si elle se trouve au niveau de coupure. La profondeur restante décroît d’une unité à chaque coup.

### V.6 — Vol de stratégie

### Question 38

> [!INDICATION]
> Après un premier coup arbitraire, imaginez que MaxDébit réponde comme le second joueur d’une partie simulée.

> [!INDICATION]
> Suivez une arête de réserve qui existe seulement dans la partie réelle. Que faire si la stratégie simulée demande précisément cette arête ? Puis comparez les deux paires de sous-graphes finaux.

#### Solution

Pour un graphe sans arête, la partie est nulle. Sinon, supposons par l’absurde qu’une stratégie $\sigma$ assure la victoire au second joueur. MaxDébit joue d’abord une arête quelconque, puis simule une partie dans laquelle il est le second joueur, sous les mêmes règles et avec les rôles permutés. Les deux objectifs sont symétriques à permutation des joueurs. Le gain du joueur simulé se compare donc par les mêmes bandes passantes.

Avant chaque coup de son adversaire, tant que la partie réelle continue, MaxDébit maintient l’invariant suivant. Les arêtes de MinLatence coïncident avec celles du premier joueur simulé et les arêtes réelles de MaxDébit sont celles du second joueur simulé augmentées d’une arête réservée. Le coup réel de MinLatence est disponible dans la simulation, donc on le reproduit. Si $\sigma$ prescrit une arête autre que la réservée, MaxDébit la joue dans les deux parties. Si $\sigma$ prescrit la réservée, il la joue dans la simulation et, s’il reste un coup réel, choisit une autre arête réelle comme nouvelle réserve. L’invariant est alors rétabli.

Lorsque le dernier coup réel est celui de MinLatence, la seule réponse simulée de $\sigma$ est l’arête réservée. MaxDébit l’a déjà et n’a plus de coup à jouer. Lorsque le dernier coup réel est celui de MaxDébit, il reste une seule arête libre dans la simulation, la réserve, et le premier joueur simulé la prend. Ainsi la partie simulée respecte $\sigma$ jusqu’au bout, les arêtes du second joueur simulé sont incluses dans celles de MaxDébit et celles de MinLatence sont incluses dans celles du premier joueur simulé.

Ajouter des arêtes ne peut que faire augmenter, au sens large, chaque meilleure bande passante et donc la bande passante limite. Une victoire stricte du second joueur simulé entraîne alors une victoire stricte de MaxDébit dans la partie réelle. Cela contredit l’existence de $\sigma$ comme stratégie gagnante pour MinLatence.

> [!METHODE]
> Pour comparer deux parties entières, formulez les inclusions entre ensembles d’arêtes qui rendent le vol de stratégie favorable, puis vérifiez ces inclusions après le dernier coup.

## Bilan

- En SQL, distinguez les identifiants qui relient les tables des colonnes que la requête restitue.
- Pour les arbres couvrants, gardez le nombre de sommets fixé pendant un échange. Un argument de coupe permet de comparer des poids entre l’intérieur et l’extérieur d’une composante.
- Pour analyser Borůvka, distinguez le coût d’un tour, la décroissance du nombre de composantes et l’invariant reliant la forêt à l’arbre optimal.
- Pour les jeux, distinguez la valeur exacte d’une position, ce que chaque joueur peut garantir et l’estimation heuristique lorsque le calcul s’arrête avant les feuilles.
