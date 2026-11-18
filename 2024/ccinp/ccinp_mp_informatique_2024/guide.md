# CCINP MP — Informatique 2024 · Corrigé guidé

*Corrigé rédigé par IA, non officiel. Signalez toute erreur.*

## Présentation du sujet

Les trois parties indépendantes traitent de la coloration de graphes en Python, de la satisfiabilité propositionnelle en OCaml, puis des périodes de mots et de la reconnaissance de motifs par automate en OCaml. Les deux figures figurent dans le sujet officiel.

Une inversion dans la définition imprimée de la conséquence logique est examinée en Q21 et Q22.

## Partie I — Coloration de graphes

### I.1 — Définitions et propriétés

### Question 1

> [!INDICATION]
> Cherchez un sommet adjacent à tous les autres et examinez les arêtes entre ses voisins.

#### Solution

Oui. Dans $G_1$, les seules arêtes relient le sommet 0 aux sommets 1, 2 et 3. Donner la couleur 0 au centre et la couleur 1 aux trois feuilles fournit une 2-coloration.

### Question 2

> [!INDICATION]
> Que contraint l’arête entre deux sommets quelconques ?

#### Solution

Dans $K_n$, deux sommets distincts sont toujours adjacents. Ils doivent donc recevoir deux couleurs distinctes, ce qui impose au moins $n$ couleurs. Attribuer une couleur propre à chaque sommet suffit. Ainsi $\chi(K_n)=n$.

### Question 3

> [!INDICATION]
> Appliquez une coloration du graphe à une clique, puis cherchez une coloration valable quel que soit le graphe.

#### Solution

Toute coloration de $G$ restreinte à une clique de taille $\omega(G)$ donne une coloration de cette clique. Ses sommets doivent recevoir des couleurs toutes distinctes, donc $\omega(G)\leq\chi(G)$. En donnant une couleur à chaque sommet du graphe, on obtient $\chi(G)\leq n$. Pour le graphe vide, les trois quantités valent zéro.

### I.2 — Programmation en Python

### Question 4

> [!INDICATION]
> Une arête non orientée se lit dans chacune des deux listes d’adjacence.

#### Solution

```python
d1 = {0: [1, 2, 3], 1: [0], 2: [0], 3: [0]}
```

### Question 5

> [!INDICATION]
> Avec un graphe simple, le degré se lit directement dans la liste des voisins.

#### Solution

```python
def degres_sommets(d):
    degres = []
    for i in d.keys():
        degres.append((len(d[i]), i))
    return degres
```

### Question 6

> [!INDICATION]
> Après le tri, quelle information faut-il conserver dans chaque couple ?

#### Solution

On utilise une convention de tri en place pour la fonction fournie `tri`. Si elle renvoie une nouvelle liste, il suffit d’affecter le résultat à `degres`.

```python
def tri_degres(d):
    degres = degres_sommets(d)
    tri(degres)
    sommets = []
    for degre, sommet in degres:
        sommets.append(sommet)
    return sommets
```

### Question 7

> [!INDICATION]
> Vérifiez séparément quelles valeurs sont admises et quelles couleurs peuvent se trouver aux deux bouts d’une arête.

#### Solution

Les clés de `c` sont les sommets par hypothèse. Chaque couleur doit appartenir à l’ensemble formé de 0 et de 1. Sur un graphe sans arête, une seule couleur utilisée peut suffire.

```python
def test(d, c):
    for s in d.keys():
        if c[s] != 0 and c[s] != 1:
            return False
        for voisin in d[s]:
            if c[s] == c[voisin]:
                return False
    return True
```

### Question 8

> [!INDICATION]
> Le sommet de degré maximal est unique. Déroulez le premier passage depuis ce sommet.

#### Solution

Le sommet 0 est seul dans la première classe de couleur 0, puisqu’il est voisin de tous les autres. Au passage suivant, les trois feuilles, sans arête entre elles, prennent la couleur 1. On peut écrire `colorie = {0: 0, 1: 1, 2: 1, 3: 1}`. L’ordre entre les feuilles ne change aucune couleur.

### Question 9

> [!INDICATION]
> Parmi les voisins de `s`, certains n’ont peut-être pas encore de couleur.

#### Solution

```python
def adjacent(d, dc, s, c):
    for voisin in d[s]:
        if voisin in dc and dc[voisin] == c:
            return True
    return False
```

### Question 10

> [!INDICATION]
> Fixez une couleur pendant un passage entier. Faites évoluer le dictionnaire au fur et à mesure de ce passage.

#### Solution

```python
def welsh_powel(d):
    ordre = tri_degres(d)
    colorie = {}
    couleur = 0
    while len(colorie) < len(ordre):
        for sommet in ordre:
            if sommet not in colorie and not adjacent(d, colorie, sommet, couleur):
                colorie[sommet] = couleur
        couleur = couleur + 1
    return colorie
```

Chaque passage colorie au moins le premier sommet libre, car la couleur est nouvelle au début du passage. Lorsqu’on réemploie cette couleur, la fonction `adjacent` écarte tout conflit avec un sommet déjà colorié dans ce passage. Le dictionnaire final encode donc une coloration, sans garantie d’optimalité. Le jury accepte aussi une liste indexée par sommet.

### Question 11

> [!INDICATION]
> Les classes de couleur donnent des groupes indépendants. Vérifiez aussi la taille de chaque classe.

#### Solution

On prend les huit étudiants comme sommets. Les arêtes sont les paires d’amis $AB,AC,AG,BC,BE,BF,DE,DF,EF,FH,GH$. L’ordre décroissant par degré $B,F,A,E,C,D,G,H$ est admissible. Welsh-Powel donne alors les groupes suivants.

- Béatrice, David et Gary.
- Fanny et Alice.
- Eloïs, Carl et Hedge.

Aucune arête ne relie deux membres d’un même groupe. Les groupes sont disjoints, couvrent toute la promotion et contiennent respectivement trois, deux et trois étudiants.

## Partie II — Satisfiabilité propositionnelle

### Question 12

> [!INDICATION]
> Utilisez un constructeur pour chaque variable et chaque connecteur.

#### Solution

```ocaml
let c = Ou (Ou (Var 0, Var 1), Non (Var 2))
```

### Question 13

> [!INDICATION]
> La conjonction extérieure est représentée par la liste des clauses.

#### Solution

```ocaml
let f = [c; Ou (Non (Var 1), Var 2)]
```

### Question 14

> [!INDICATION]
> Distinguez les trois constructeurs du type et évaluez récursivement les sous-clauses.

#### Solution

```ocaml
let rec evalue_clause clause valuation =
  match clause with
  | Var i -> valuation.(i)
  | Non sous_clause -> not (evalue_clause sous_clause valuation)
  | Ou (gauche, droite) ->
      evalue_clause gauche valuation || evalue_clause droite valuation
```

Chaque appel descend vers une sous-clause stricte. Les branches reproduisent la sémantique de la variable, de la négation et de la disjonction.

### Question 15

> [!INDICATION]
> Quelle est la valeur de la conjonction sans opérande ?

#### Solution

```ocaml
let rec evalue_FNC formule valuation =
  match formule with
  | [] -> true
  | clause :: reste ->
      evalue_clause clause valuation && evalue_FNC reste valuation
```

La liste vide représente la conjonction vide, vraie. Pour une liste non vide, la formule est vraie exactement quand la première clause et la conjonction des clauses restantes sont vraies.

### Question 16

> [!INDICATION]
> Calculez la valeur de chaque clause avant de prendre leur conjonction.

#### Solution

La première clause vaut vrai grâce à $x_1$. La seconde vaut vrai grâce à $x_2$. La conjonction vaut donc `true`.

### Question 17

> [!INDICATION]
> Cherchez depuis la droite le premier bit qui peut absorber la retenue.

#### Solution

```ocaml
let suivant valuation =
  let n = Array.length valuation in
  let rec cherche i =
    if i < 0 then false
    else if valuation.(i) then cherche (i - 1)
    else begin
      valuation.(i) <- true;
      for j = i + 1 to n - 1 do
        valuation.(j) <- false
      done;
      true
    end
  in
  cherche (n - 1)
```

On change en un le zéro le plus à droite et on remet à zéro tous les bits situés après lui, qui valaient un. Lorsqu’aucun zéro n’existe, il n’y a pas de successeur et le tableau reste intact. Cela couvre aussi le tableau vide.

### Question 18

> [!INDICATION]
> Évaluez la valuation courante avant de chercher sa suivante.

#### Solution

```ocaml
let satisfiable formule n =
  let valuation = Array.make n false in
  let rec examine () =
    if evalue_FNC formule valuation then true
    else if suivant valuation then examine ()
    else false
  in
  examine ()
```

Les valuations sont visitées dans l’ordre croissant de leur valeur binaire, de la valuation toute fausse à la valuation toute vraie si nécessaire. Le résultat est vrai dès qu’un modèle est rencontré. Le tableau vide permet de tester l’unique valuation sur zéro variable.

### Question 19

> [!INDICATION]
> Comptez les valuations, puis la taille des objets visités lors de l’évaluation d’une valuation.

#### Solution

Soit $L$ le nombre total de nœuds dans les clauses et $n$ le nombre de variables. Une évaluation coûte au plus $O(1+L)$ et un appel à `suivant` coûte au plus $O(1+n)$. On obtient ainsi la majoration $O(2^n(1+L+n))$.

On peut l’affiner pour ce code. Sur une énumération entière, chaque position contribue au parcours de la retenue avec une fréquence qui décroît géométriquement à mesure qu’on s’éloigne du bit de droite. Le coût total des incréments réussis est $O(2^n)$, et le dernier appel infructueux coûte $O(1+n)$. Avec l’initialisation, on obtient $O(2^n(1+L)+n)$. Le coût est exponentiel en $n$ dans le pire cas, par exemple avec la contradiction $x_0\land\neg x_0$ pour $n\geq1$, si les autres variables sont ajoutées sous forme de clauses tautologiques pour apparaître dans la formule.

### Question 20

> [!INDICATION]
> Avec une valuation partielle, à quelle condition une clause peut-elle déjà condamner toute la branche ?

#### Solution

Choisir une variable non fixée et essayer successivement les valeurs faux et vrai. Après chaque choix, supprimer les clauses qui contiennent un littéral devenu vrai et ôter des autres clauses les littéraux devenus faux. Si une clause n’a plus de littéral, revenir au choix précédent. Si toutes les clauses sont supprimées, la valuation partielle se complète arbitrairement en un modèle. Sinon, continuer avec une autre variable.

Chaque simplification préserve les possibilités d’extension de la valuation courante. Les deux branches couvrent toutes les extensions possibles du choix suivant. L’arrêt est assuré puisque la profondeur est au plus le nombre de variables.

### Question 21

> [!INDICATION]
> Une implication est invalidée exactement par un modèle de son antécédent qui réfute son conséquent.

#### Solution

Avec le sens usuel de $\Gamma\models F$, on cherche une valuation qui satisfait toutes les hypothèses et rend $F$ fausse.

```text
H ← conjonction de F1, …, Fn
C ← forme normale conjonctive équivalente à H et non F
N ← nombre de variables, après une renumérotation commune
renvoyer la négation de satisfiable(C, N)
```

La définition imprimée inverse les rôles en demandant que tout modèle de $F$ soit un modèle de $\Gamma$. Si on suit cette phrase littéralement, le programme teste à la place l’insatisfiabilité de $F\land\neg H$. La convention usuelle est celle employée pour la correction de la déduction naturelle en Q22.

### Question 22

> [!INDICATION]
> Lisez d’abord la dernière formule du séquent. Est-elle déjà une hypothèse ?

#### Solution

Dans le sens usuel de conséquence logique, la correction de la déduction naturelle assure que tout séquent prouvé est valide sémantiquement. Avec la définition imprimée, cette justification générale échouerait. Ici, par exemple, $P$ vrai et $Q$ faux satisfont la conclusion $P$ mais réfutent une hypothèse. L’axiome d’hypothèse, qui permet de dériver une formule présente dans le contexte, suffit ici.

$$
\frac{P\in\{P\to Q,\ Q\to R,\ P\}}
{P\to Q,\ Q\to R,\ P\vdash P}\quad\text{(Hypothèse)}
$$

La condition au-dessus du trait est la condition d’application de l’axiome. L’arbre de déduction n’a qu’un nœud et les implications restent disponibles dans le contexte.

## Partie III — Automates et reconnaissance de motifs

### III.1 — Recherche naïve et périodes

### Question 23

> [!INDICATION]
> Quel ensemble d’indices doit être vérifié lorsque le décalage égale la longueur du mot ?

#### Solution

Si $x$ est non vide, sa longueur $m$ est positive. Pour $p=m$, l’ensemble des indices $0\leq i<m-p$ est vide. La propriété requise est donc vraie et $m$ est une période.

### Question 24

> [!INDICATION]
> Énumérez uniquement les positions qui laissent assez de place pour tout le motif.

#### Solution

```ocaml
let occurrence x y =
  let m = String.length x and n = String.length y in
  let rec coincide depart j =
    j = m || (x.[j] = y.[depart + j] && coincide depart (j + 1))
  in
  let rec cherche depart =
    depart <= n - m && (coincide depart 0 || cherche (depart + 1))
  in
  cherche 0
```

Le mot vide est trouvé en position zéro. Un motif trop long est rejeté avant tout accès aux caractères. À tout départ admissible, l’auxiliaire compare les lettres jusqu’à la fin du motif ou au premier désaccord.

### Question 25

> [!INDICATION]
> Multipliez le nombre de départs admissibles par le coût maximal d’une comparaison.

#### Solution

Si $1\leq m\leq n$, le pire cas est $\Theta((n-m+1)m)$. Par exemple, sur un alphabet qui contient deux lettres, prenez un texte formé seulement de `a` et le motif formé de $m-1$ lettres `a` puis de `b`. Chaque départ admissible échoue à la dernière comparaison. Si $m=0$ ou $m>n$, ce code répond en temps constant.

### Question 26

> [!INDICATION]
> Éliminez les deux plus petits décalages, puis vérifiez toutes les comparaisons pour le suivant.

#### Solution

Le décalage 1 échoue aux indices 1 et 2, et le décalage 2 échoue aux indices 0 et 2. Pour le décalage 3, les cinq comparaisons sont vraies, puisque le préfixe et le suffixe de longueur 5 sont tous deux `aabaa`. La période minimale est donc 3.

### Question 27

> [!INDICATION]
> Testez les décalages dans l’ordre croissant. La longueur entière est un décalage garanti.

#### Solution

```ocaml
let periode x =
  let n = String.length x in
  let rec verifie p i =
    i = n - p || (x.[i] = x.[i + p] && verifie p (i + 1))
  in
  let rec cherche p =
    if verifie p 0 then p else cherche (p + 1)
  in
  if n = 0 then failwith "periode : mot vide" else cherche 1
```

Le test porte exactement sur les indices prescrits. Comme la longueur est une période, le parcours termine et s’arrête à la première période. Le mot vide est hors du domaine défini dans l’énoncé.

### Question 28

> [!INDICATION]
> Regardez les deux facteurs de longueur commune obtenus en supprimant $p$ lettres à une extrémité du mot.

#### Solution

Si $p$ est une période, le préfixe et le suffixe de longueur $|x|-p$ coïncident, car leurs lettres d’indice $i$ sont respectivement $x_i$ et $x_{i+p}$. Soit $w$ ce mot commun.

En prenant $u$ comme préfixe de longueur $p$ et $v$ comme suffixe de même longueur, on a $x=uw=wv$.

Réciproquement, dans ces deux décompositions, $w$ occupe les positions qui commencent respectivement à l’indice $p$ et à l’indice zéro. On a donc $x_i=x_{i+p}$ pour chaque indice prescrit. Cela inclut $p=|x|$ et $w$ vide.

### Question 29

> [!INDICATION]
> Montrez que tout bord strictement plus court que le plus long bord en est à la fois un préfixe et un suffixe.

#### Solution

Raisonnons par récurrence sur la longueur positive de $x$. À la longueur 1, seul le mot vide est un bord. Plus généralement, si le plus long bord est vide, le résultat sur les bords est immédiat.

Sinon, notons $b$ le plus long bord de $x$. Un autre bord $z$ est plus court que $b$, puisque les deux sont des préfixes de $x$.

Comme $b$ est à la fois préfixe et suffixe de $x$, le mot $z$ est préfixe et suffixe de $b$.

Réciproquement, tout bord de $b$ est un bord de $x$ par transitivité de ces deux relations. Les bords de $x$ sont donc $b$, puis les bords de $b$, dans l’ordre donné par l’hypothèse de récurrence.

D’après Q28, à un bord de longueur $k$ correspond exactement la période $|x|-k$. Cette correspondance inverse l’ordre des longueurs, donc la suite proposée énumère les périodes dans l’ordre croissant.

### Question 30

> [!INDICATION]
> Après un échec, le préfixe déjà lu contient les lettres nécessaires pour choisir un décalage sans repartir de zéro.

#### Solution

Soit $j$ le nombre de lettres déjà reconnues au début du motif. Lors d’un désaccord, un alignement commençant à l’intérieur du bloc reconnu doit réutiliser un suffixe de ce bloc qui soit aussi un préfixe du motif. On remplace donc $j$ par la longueur du plus long bord propre du préfixe reconnu, et on compare de nouveau la même lettre du texte. En cas de nouvel échec, on suit les bords successifs. Si aucun caractère n’est reconnu, le texte peut avancer après l’échec.

On peut prétraiter les longueurs de bord en appliquant le même mécanisme aux préfixes successifs du motif. Chaque lettre augmente d’au plus un la longueur courante, et chaque repli la diminue d’au moins un. Le coût de tous les replis est donc linéaire en plus du balayage. On obtient l’algorithme de Knuth–Morris–Pratt, en $O(m+n)$ avec le prétraitement du motif de longueur $m$ et le balayage du texte de longueur $n$.

### III.2 — Localisation par automate

### Question 31

> [!INDICATION]
> Relevez séparément l’état initial, les états terminaux et les trois destinations depuis chaque état.

#### Solution

```ocaml
let automate =
  let transition e lettre =
    match e, lettre with
    | 0, 'a' -> 1
    | 0, ('b' | 'c') -> 0
    | 1, 'a' -> 2
    | 1, 'b' -> 3
    | 1, 'c' -> 0
    | 2, 'a' -> 2
    | 2, 'b' -> 3
    | 2, 'c' -> 0
    | 3, 'a' -> 4
    | 3, ('b' | 'c') -> 0
    | 4, 'a' -> 2
    | 4, 'b' -> 3
    | 4, 'c' -> 0
    | _ -> failwith "couple hors de l'automate"
  in
  { etats = [0; 1; 2; 3; 4]; alphabet = ['a'; 'b'; 'c'];
    initial = 0; transition = transition; final = [2; 4] }
```

Le dernier cas est hors de l’ensemble des couples état-lettre de l’automate.

### Question 32

> [!INDICATION]
> Pour chaque état, établissez un chemin depuis l’initial et un chemin vers un terminal.

#### Solution

Depuis 0, les mots vide, `a`, `aa`, `ab` et `aba` atteignent respectivement les états 0, 1, 2, 3 et 4. Les états 2 et 4 sont terminaux. Les états 0, 1 et 3 mènent à un terminal en lisant respectivement `aa`, `a` et `a`. Tous les états sont accessibles et coaccessibles, donc l’automate est émondé.

### Question 33

> [!INDICATION]
> Ajoutez des états initial et final propres. Pour chaque paire de voisins de 0, suivez une entrée, les boucles en 0, puis une sortie.

#### Solution

On introduit un nouvel état initial $I$ avec une transition $\varepsilon$ vers 0, et un nouvel état final $F$ atteint depuis 2 et 4 par des transitions $\varepsilon$. L’état $I$ n’a pas d’entrée et $F$ n’a pas de sortie. On groupe les lettres des transitions parallèles par union.

Pour éliminer 0, le seul successeur distinct de 0 est l’état 1, atteint par $a$. La boucle porte $b\cup c$. Posons $u=(b\cup c)^*a$. On insère les transitions suivantes, données par leur origine et leur étiquette, toutes vers 1.

- De $I$ à 1, l’étiquette est $u$.
- Des états 1, 2 et 4 vers 1, l’étiquette est $cu$.
- De 3 à 1, l’étiquette est $(b\cup c)u$.

On conserve les autres transitions, y compris celles vers $F$, puis on supprime 0 et ses arêtes incidentes. Chaque nouvelle transition remplace exactement un passage par 0, avec un nombre arbitraire de tours sur sa boucle.

### Question 34

> [!INDICATION]
> Appliquez une transition par lettre et relevez les indices d’arrivée dans les deux états terminaux.

#### Solution

Les indices sont les positions finales, numérotées à partir de zéro, des occurrences reconnues. L’automate ne précise pas à lui seul le début de chaque occurrence. Pour `cabaac`, les états après les six lettres sont successivement $0,1,3,4,2,0$. Les seuls états terminaux visités donnent la liste `[3; 4]`.

### Question 35

> [!INDICATION]
> Parcourez le texte une seule fois. Si vous ajoutez les indices en tête, rétablissez leur ordre au retour.

#### Solution

```ocaml
let cherche m t =
  let n = String.length t in
  let rec terminal etat liste =
    match liste with
    | [] -> false
    | premier :: reste -> etat = premier || terminal etat reste
  in
  let rec inverse indices acc =
    match indices with
    | [] -> acc
    | premier :: reste -> inverse reste (premier :: acc)
  in
  let rec parcourt i etat indices =
    if i = n then inverse indices []
    else
      let suivant = m.transition etat t.[i] in
      let nouveaux =
        if terminal suivant m.final then i :: indices else indices
      in
      parcourt (i + 1) suivant nouveaux
  in
  parcourt 0 m.initial []
```

### Question 36

> [!INDICATION]
> Après avoir lu un préfixe de longueur $i$, formulez ce que représentent l’état courant et la liste accumulée.

#### Solution

Au début de l’appel d’indice $i$, `etat` est l’état atteint après lecture des $i$ premières lettres. La liste `indices` contient, dans l’ordre décroissant, les positions inférieures à $i$ auxquelles le préfixe correspondant se termine par un mot de $X$. Au départ, l’état initial et la liste vide établissent cet invariant. Le motif ne contient pas le mot vide.

À l’itération suivante, `transition` calcule l’état après la lecture de la lettre d’indice $i$. Cet état est terminal exactement quand le nouveau préfixe appartient à $A^*X$, donc quand un mot de $X$ se termine en $i$. L’indice est alors ajouté en tête, ce qui conserve l’ordre décroissant. L’indice d’appel augmente jusqu’à la longueur du texte. L’invariant final et le renversement de la liste donnent exactement les positions demandées en ordre croissant.

## Bilan

- En coloration, une classe de couleur doit rester un ensemble de sommets deux à deux non adjacents.
- Pour décider une conséquence logique, cherchez une valuation qui satisfait les hypothèses et réfute la conclusion.
- Pour une recherche de motifs par automate, les états finaux signalent les positions où une occurrence se termine.
