# CCINP MPI — Informatique 2025 · Corrigé guidé

*Corrigé rédigé par IA, non officiel. Signalez toute erreur.*

## Présentation du sujet

L'épreuve dure quatre heures, sans calculatrice, et comporte trois parties indépendantes. La première étudie une grammaire non contextuelle, la deuxième analyse une heuristique de rangement et la troisième compare deux algorithmes de couplage. Le rangement est programmé en OCaml. Les couplages et les manipulations de graphes sont programmés en C.

| Partie | Questions | Travail principal |
|---|---|---|
| I | Q1–Q5 | Dériver un mot, lire des arbres et décomposer un langage en blocs de lettres. |
| II | Q6–Q16 | Justifier une appartenance à NP et une réduction, borner l'heuristique, puis programmer des opérations sur les listes de boîtes. |
| III | Q17–Q38 | Prouver la stabilité et l'optimalité du côté des proposants, puis manipuler les préférences et les listes d'adjacence en C. |

Les questions de code Q11–Q16 et Q32–Q38 sont accessibles après lecture des types et des conventions d'indices. Le cœur des preuves réside dans Q9–Q10 pour le volume des boîtes et dans Q23–Q25 pour les rejets. On peut réserver environ une demi-heure à la grammaire, une heure au rangement et deux heures quinze aux couplages, puis utiliser le dernier quart d'heure pour vérifier les signatures et les indices.

Le rapport relève une coquille dans les préférences de $u_2$ et précise que l'algorithme 4 retient uniquement les arcs de $V$ vers $U$. Le corrigé explicite ces deux lectures au moment de dérouler les algorithmes.

## Partie I — Grammaire non contextuelle

Pour cette grammaire, un non-terminal peut toujours revenir à une production vide par les règles de niveau inférieur. Cette possibilité est aussi importante pour les arbres que pour les blocs entre séparateurs.

### Question 1

> [!INDICATION]
> Pour introduire la première lettre du mot, cherchez la règle qui contient son terminal.

> [!INDICATION]
> À chaque étape, remplacez strictement le non-terminal le plus à gauche. Utilisez les règles de descente jusqu'à la production vide pour supprimer le préfixe.

#### Solution

On remplace à chaque étape le non-terminal le plus à gauche.

$$
\begin{aligned}
S&\Rightarrow SaS\Rightarrow AaS\Rightarrow BaS\Rightarrow aS\\
 &\Rightarrow aA\Rightarrow aAbA\Rightarrow aBbA\Rightarrow abA\\
 &\Rightarrow abB\Rightarrow abBcB\Rightarrow abcB\Rightarrow abc.
\end{aligned}
$$

Ainsi **$abc\in L(G)$**.

> [!JURY]
> Le rapport distingue la dérivation à gauche et l'arbre. Pour une dérivation, le contrôle se fait à chaque flèche, pas seulement sur le mot obtenu.

### Question 2

> [!INDICATION]
> Développez $S$ avec la règle qui crée un $a$. Il reste deux endroits possibles pour créer le deuxième.

> [!INDICATION]
> Complétez les trois branches issues de $S$ qui ne doivent plus produire de lettre jusqu'à la feuille vide.

#### Solution

Dans le premier arbre, le fils gauche de la racine développe le premier $a$. Dans le second, c'est le fils droit qui développe le deuxième $a$. Les fils de chaque nœud sont donnés dans l'ordre de lecture.

```text
S                         S
├── S                     ├── S
│   ├── S                 │   └── A
│   │   └── A             │       └── B
│   │       └── B         │           └── ε
│   │           └── ε     ├── a
│   ├── a                 └── S
│   └── S                     ├── S
│       └── A                 │   └── A
│           └── B             │       └── B
│               └── ε         │           └── ε
├── a                         ├── a
└── S                         └── S
    └── A                         └── A
        └── B                         └── B
            └── ε                         └── ε
```

Les feuilles lues de gauche à droite donnent $aa$ dans les deux arbres. **La grammaire est ambiguë.**

> [!JURY]
> Le rapport demande autant de fils que de symboles dans le membre droit de la règle. Les règles vers un seul non-terminal et les productions vides apparaissent aussi dans les arbres.

### Question 3

> [!INDICATION]
> Relevez, pour chaque règle, le premier symbole dans chacun de ses membres droits possibles.

#### Solution

Les règles $S\to SaS$, $A\to AbA$ et $B\to BcB$ commencent chacune par leur non-terminal de gauche. **Les trois variables sont récursives gauches directes.**

### Question 4

> [!INDICATION]
> Appliquez séparément la transformation de l'énoncé à chacun des trois non-terminaux.

> [!INDICATION]
> Pour $B$, traitez $\varepsilon$ comme un préfixe vide lors de la concaténation. Examinez ce que mémorise la nouvelle variable.

#### Solution

On applique le procédé donné aux trois non-terminaux. Dans le cas de $B$, le préfixe $\beta$ est vide. On obtient

$$
\boxed{\begin{aligned}
S&\to AS' & S'&\to aSS'\mid\varepsilon\\
A&\to BA' & A'&\to bAA'\mid\varepsilon\\
B&\to B'  & B'&\to cBB'\mid\varepsilon .
\end{aligned}}
$$

Le symbole initial reste $S$ et aucune règle ne commence par le non-terminal qu'elle développe. Pour chaque transformation, une chaîne de règles récursives gauches suivie de la règle $\beta$ produit une suite ordonnée de suffixes $\alpha$ après $\beta$. La nouvelle variable engendre précisément toutes ces suites finies, avec les mêmes sous-arbres attachés. Le remplacement et son inverse préservent le mot produit, ce qui donne $L(G')=L(G)$.

### Question 5

> [!INDICATION]
> Commencez par ce que peut engendrer $B$. Cherchez ensuite le rôle des lettres $b$ dans les productions de $A$.

> [!INDICATION]
> Décomposez le mot en blocs séparés par $a$, puis chaque bloc en morceaux séparés par $b$. Autorisez les blocs vides.

#### Solution

Le langage de $B$ est $c^*$ puisque $B$ produit $\varepsilon$ et peut produire un $c$ de plus par $B\Rightarrow BcB\Rightarrow cB$.

Tout mot de $\{b,c\}^*$ se décompose aux occurrences de $b$ en blocs de $c$, éventuellement vides.

Avec une règle $A\to AbA$ pour chaque séparateur et $A\to B$ pour chaque bloc, il est produit par $A$.

Enfin on décompose tout mot de $\{a,b,c\}^*$ aux occurrences de $a$ en blocs de $\{b,c\}^*$.

On emploie $S\to SaS$ et $S\to A$ de la même façon.

Les seules lettres terminales émises étant $a,b,c$, **$L(G')=L(G)=\{a,b,c\}^*$.**

> [!METHODE]
> Une lettre qui ne peut apparaître qu'à un niveau de la grammaire sert souvent de séparateur pour décomposer un mot et reconstruire une dérivation.

## Partie II — Problème de bin-packing

Les preuves de complexité portent sur les tailles rationnelles exactes. Dans la partie programmation, les types imposés utilisent des flottants. L'ordre d'ouverture des boîtes constitue la donnée centrale de l'heuristique.

### Question 6

> [!INDICATION]
> Choisissez un certificat dont on peut borner la longueur en bits.

> [!INDICATION]
> Il suffit de parcourir les boîtes qui reçoivent au moins un objet. Justifiez que l'addition exacte des rationnels n'introduit pas des entiers d'une longueur exponentielle.

#### Solution

Un certificat est le tableau des $n$ valeurs $R(i)$, chacune décrite avec $O(\log(k+1))$ bits.

Sa longueur est polynomiale en celle de l'entrée.

On vérifie que chaque valeur est comprise entre $1$ et $k$, puis on regroupe les objets par étiquette de boîte, par exemple en triant les étiquettes.

Il suffit de contrôler les boîtes non vides, au nombre d'au plus $n$.

Pour chaque boîte, on additionne exactement ses rationnels et on vérifie que la somme est au plus $1$.

Les produits de dénominateurs ont une longueur binaire bornée par la somme des longueurs des dénominateurs de l'entrée.

Les additions et comparaisons restent donc polynomiales en coût binaire.

**BIN-PACKING appartient à NP.**

> [!JURY]
> Le rapport relève fréquemment l'oubli de la taille du certificat. Ici le nombre de boîtes est écrit en binaire, ce qui rend également utile de distinguer boîtes présentes et boîtes vides.

### Question 7

> [!INDICATION]
> Imaginez deux boîtes remplies exactement, une pour chaque groupe de PARTITION.

> [!INDICATION]
> Normalisez les entiers par la moitié de leur somme. Traitez à part les cas où le dénominateur s'annule ou une taille dépasserait la capacité.

#### Solution

PARTITION revient à choisir des signes $\epsilon_i\in\{-1,1\}$ tels que $\sum_i\epsilon_i c_i=0$.

Remplacer les $c_i$ par leurs valeurs absolues préserve l'existence de tels signes et les zéros peuvent être enlevés.

Notons $T$ la somme des entiers positifs restants.

Si $T=0$, on renvoie une instance positive fixe, deux objets de taille $1$ pour deux boîtes.

Si l'un des entiers dépasse $T/2$, aucune partition ne peut équilibrer les deux groupes.

On renvoie alors une instance négative fixe, trois objets de taille $1$ pour deux boîtes.

Dans les autres cas, on pose $k=2$ et $a_i=2|c_i|/T$ pour les indices retenus.

Ces tailles sont dans $]0,1]$ et leur somme vaut $2$.

Une partition équilibrée fournit un rangement de charge $1$ par boîte.

Réciproquement, un rangement valide a nécessairement une charge $1$ dans chaque boîte.

En multipliant les deux charges par $T/2$, on obtient une partition des valeurs absolues, donc une solution de l'instance de départ.

Les additions et l'écriture des fractions prennent un temps polynomial en longueur binaire. Cette réduction polynomiale depuis PARTITION et Q6 montrent que **BIN-PACKING est NP-complet**.

> [!METHODE]
> Dans une réduction, traiter les données pour lesquelles l'instance construite sortirait du domaine. On peut renvoyer une instance fixe de réponse déjà connue lorsque le cas de départ est décidable directement.

### Question 8

> [!INDICATION]
> Regardez l'objet qui a ouvert la boîte considérée.

> [!INDICATION]
> Par l'ordre décroissant, que peut-on dire des objets qui ont ouvert les boîtes précédentes ?

#### Solution

Le premier objet placé dans $B_{k_1}$ est au moins aussi grand que tout autre objet de cette boîte. S'il y en a un de taille supérieure à $1/2$, son premier objet dépasse donc $1/2$. Les $k_1-1$ boîtes précédentes ont chacune été ouvertes par un objet traité plus tôt, de taille au moins aussi grande par décroissance. Ces $k_1$ objets sont deux à deux incompatibles dans une boîte, d'où

$$
\boxed{k^*\ge k_1\ge\frac23 k.}
$$

### Question 9

> [!INDICATION]
> Une boîte qui n'a finalement qu'un objet avait aussi seulement cet objet à l'ouverture de la suivante.

> [!INDICATION]
> Distinguez les boîtes ordinaires de la dernière. Pour la seconde affirmation, suivez la charge d'une boîte avant et après un refus de placement.

#### Solution

Dans le second cas, tous les objets des boîtes $B_{k_1},\ldots,B_k$ sont de taille au plus $1/2$. C'est vrai pour $B_{k_1}$ par hypothèse et pour les suivantes par l'ordre de traitement. Si une de ces boîtes autre que la dernière ne contenait finalement qu'un objet, le premier objet de la boîte suivante aurait pu y entrer lors de son traitement. Cela contredit le choix du premier casier disponible. La dernière boîte contient au moins un objet et chaque autre boîte du suffixe en contient au moins deux, soit **au moins $2(k-k_1)+1$ objets**.

Chaque objet du suffixe a été traité alors que toutes les boîtes avant $B_{k_1}$ étaient ouvertes. Il n'a pu entrer dans aucune d'elles à ce moment, et leur charge n'a ensuite fait qu'augmenter. Il n'entre donc dans aucune d'elles à la fin.

> [!JURY]
> Le rapport souligne l'importance du « plus un », fourni par la dernière boîte. L'ouverture d'une boîte suivante est précisément ce qui permet d'écarter une boîte singleton parmi les précédentes.

### Question 10

> [!INDICATION]
> Dans le cas de Q9, prenez un objet de taille minimale parmi ceux des dernières boîtes.

> [!INDICATION]
> Majorez la capacité restante des premières boîtes à l'aide de cet objet, puis comparez la borne obtenue à une combinaison convexe des deux décomptes.

#### Solution

Dans le cas de Q9, notons $s>0$ la taille minimale des objets du suffixe, $r=k_1-1$ le nombre de boîtes précédentes et $m=2(k-k_1)+1$. Chaque boîte précédente a une charge strictement supérieure à $1-s$, et le suffixe porte une charge au moins égale à $ms$. Si $r>0$,

$$
\begin{aligned}
\sum_i a_i&>r(1-s)+ms\\
          &\ge\min(r,m).
\end{aligned}
$$

Si $r=0$, la somme est strictement positive et la même borne stricte vaut.

Cette inégalité de masse concerne le cas de Q9. Lue sans cette restriction, elle est fausse. Par exemple, neuf objets de taille $51/100$ occupent neuf boîtes distinctes. La somme des tailles vaut $459/100$, inférieure à $\min(5,7)=5$.

Par l'inégalité admise, $3k_1\le 2k+2$, d'où $m\ge r$. Dans la branche de Q9, on a donc $k^*\ge\sum_i a_i> k_1-1$, car une boîte peut porter au plus une unité. Puisque $k^*$ est entier, **$k^*\ge k_1=\lceil 2k/3\rceil \ge 2k/3$**, dans les deux cas. Pour le rangement vide, la borne d'approximation est immédiate et les questions utilisant $B_{k_1}$ concernent les entrées non vides.

> [!PIEGE]
> La borne sur la masse s'applique au second cas. Le premier cas donne une borne par incompatibilité de grands objets. Les deux raisonnements se rejoignent seulement sur la borne pour $k^*$.

### Question 11

> [!INDICATION]
> Identifiez la valeur initiale des deux champs, en respectant leur type.

#### Solution

On reprend les types de l'énoncé.

```ocaml
type objet = { id : int; taille : float }
type boite = { charge : float; objets : objet list }

let boite_vide : boite = { charge = 0.0; objets = [] }
```

### Question 12

> [!INDICATION]
> Construisez un nouvel enregistrement. Une insertion en tête de la liste d'objets suffit.

#### Solution

La nouvelle boîte contient l'objet de plus et sa charge est mise à jour. La fonction suppose l'insertion permise, comme lorsque Q15 l'appelle.

```ocaml
let ajoute_boite (o : objet) (b : boite) : boite =
  { charge = b.charge +. o.taille; objets = o :: b.objets }
```

### Question 13

> [!INDICATION]
> Distinguez la liste vide, la tête compatible et la tête incompatible.

> [!INDICATION]
> Un indice calculé sur la queue doit être décalé d'une unité. Vérifiez aussi le sens de ce décalage en cas d'échec.

#### Solution

La liste vide renvoie sa longueur, zéro. Une tête compatible a l'indice zéro. Sinon, on ajoute un à l'indice renvoyé sur la queue, y compris quand celui-ci vaut la longueur de la queue.

```ocaml
let rec trouve_boite (bl : boite list) (o : objet) : int =
  match bl with
  | [] -> 0
  | b :: suite ->
      if b.charge +. o.taille <= 1.0 then 0
      else 1 + trouve_boite suite o
```

> [!JURY]
> Le rapport attend une fonction récursive. Le même appel récursif traite les échecs partiels et l'absence de boîte compatible.

### Question 14

> [!INDICATION]
> Descendez jusqu'au bon indice en reconstruisant les têtes non modifiées.

> [!INDICATION]
> Si la liste est épuisée, la seule valeur à reconstruire est l'image de la valeur par défaut.

#### Solution

L'indice est supposé non négatif. Lorsqu'on atteint la liste vide, l'insertion de la valeur par défaut vaut aussi pour un indice égal à la longueur, ce qui permettra d'ouvrir une boîte en Q15.

```ocaml
let rec transforme d f i l =
  match l with
  | [] -> [f d]
  | x :: suite ->
      if i = 0 then f x :: suite
      else x :: transforme d f (i - 1) suite
```

### Question 15

> [!INDICATION]
> Conservez les boîtes dans l'ordre de leur ouverture.

> [!INDICATION]
> Utilisez le même appel à la transformation lorsque la recherche trouve une boîte ou atteint la longueur de la liste.

#### Solution

L'accumulateur conserve l'ordre d'ouverture des boîtes. Après recherche de l'indice, la transformation remplace la boîte choisie ou en crée une en fin de liste.

```ocaml
let premier_casier (objets : objet list) : boite list =
  let rec ranger boites restants =
    match restants with
    | [] -> boites
    | o :: suite ->
        let indice = trouve_boite boites o in
        let mises_a_jour =
          transforme boite_vide (ajoute_boite o) indice boites
        in
        ranger mises_a_jour suite
  in
  ranger [] objets
```

### Question 16

> [!INDICATION]
> Appliquez l'algorithme précédent après avoir trié sur le champ pertinent.

> [!INDICATION]
> Pour produire un ordre décroissant avec un tri croissant, échangez les deux tailles dans la comparaison.

#### Solution

On compare les tailles dans l'ordre inverse, puis on applique Premier Casier. Chaque objet conserve son identifiant. Si l'on reconstruisait la fonction $R$ à partir d'une permutation $\sigma$ qui envoie un rang trié sur le rang d'origine, il faudrait écrire $R(\sigma(i))=R_1(i)$. Ici le retour direct des boîtes rend cette étape inutile.

```ocaml
let premier_casier_decroissant (objets : objet list) : boite list =
  let tries =
    List.sort (fun o1 o2 -> compare o2.taille o1.taille) objets
  in
  premier_casier tries
```

Les fonctions Q11–Q16 utilisent les flottants demandés. Le test de capacité s'effectue donc dans cette arithmétique, tandis que les preuves de Q6–Q10 portent sur les tailles rationnelles exactes.

> [!JURY]
> Le rapport note les imprécisions des descriptions de la comparaison et du tri. En écrivant explicitement les deux tailles dans l'ordre inverse, on trie selon le bon champ, quel que soit l'identifiant.

## Partie III — Algorithmes de couplage

Les deux algorithmes utilisent les mêmes listes de préférences mais des règles différentes. Pour le premier, suivre l'historique des propositions et rejets. Pour le second, suivre les premiers choix sur l'ensemble courant.

**III.1 — Recherche de couplages stables**

### Question 17

> [!INDICATION]
> Notez pour chaque proposant les personnes à qui il a déjà proposé.

> [!INDICATION]
> Après toute substitution, réexaminez l'ensemble des personnes libres et prenez la plus petite, même si son indice est inférieur à celui choisi au tour précédent.

#### Solution

Dans $D$, on lit la préférence de $u_2$ comme $v_2>_{u_2} v_1>_{u_2}v_3$. Les propositions et les couplages provisoires sont les suivants.

| Tour | Proposition | Décision | Couples après le tour |
|---|---|---|---|
| 1 | $(v_1,u_2)$ | Acceptée | $(v_1,u_2)$ |
| 2 | $(v_2,u_1)$ | Acceptée | $(v_1,u_2),(v_2,u_1)$ |
| 3 | $(v_3,u_1)$ | Remplace $v_2$ | $(v_1,u_2),(v_3,u_1)$ |
| 4 | $(v_2,u_2)$ | Remplace $v_1$ | $(v_2,u_2),(v_3,u_1)$ |
| 5 | $(v_1,u_1)$ | Remplace $v_3$ | $(v_1,u_1),(v_2,u_2)$ |
| 6 | $(v_3,u_2)$ | Refusée | $(v_1,u_1),(v_2,u_2)$ |
| 7 | $(v_3,u_3)$ | Acceptée | $(v_1,u_1),(v_2,u_2),(v_3,u_3)$ |

**Le résultat est le couplage diagonal.**

### Question 18

> [!INDICATION]
> Comptez les paires n'ayant jamais donné lieu à une proposition.

> [!INDICATION]
> Avant d'utiliser ce variant, prouvez qu'une personne encore libre n'a pas épuisé ses choix. Que devient une personne de $U$ après sa première proposition reçue ?

#### Solution

Pendant l'algorithme, $A$ reste un couplage, car un proposant est libre et une substitution libère l'ancien partenaire. Tout $u$ ayant reçu une proposition est désormais apparié, puisque sa première proposition est acceptée et que tout remplacement est immédiat. Si un $v$ libre avait déjà proposé à tout $U$, tous les éléments de $U$ seraient appariés et, par égalité des effectifs, tous ceux de $V$ également. C'est impossible. Chaque tour peut donc effectuer une nouvelle proposition. Le nombre de paires encore jamais proposées est entier, positif ou nul, et décroît strictement d'une unité par tour. **La boucle termine.**

> [!JURY]
> Le rapport relève des variants qui ne décroissent pas strictement. Le nombre de personnes libres peut rester constant lors d'un refus ou d'un remplacement.

### Question 19

> [!INDICATION]
> Cherchez une propriété du nombre de couples auxquels chaque personne peut appartenir, puis utilisez le test de sortie.

#### Solution

**Invariant.** À l'entrée de chaque tour, $A$ est un couplage partiel, c'est-à-dire qu'aucun sommet n'appartient à deux paires de $A$. À l'arrêt, la condition de boucle est fausse, donc tous les éléments de $V$ sont appariés. Les deux groupes ayant le même effectif, tous les éléments de $U$ le sont aussi.

### Question 20

> [!INDICATION]
> Supposez qu'un proposant préfère à son partenaire final une autre personne.

> [!INDICATION]
> Justifiez qu'il lui a effectivement proposé et comparez les préférences de cette personne au moment du rejet puis à l'arrêt.

#### Solution

Notons $A$ le couplage parfait final.

Supposons que $v$ préfère un autre $u$ à $m_A(v)$.

Les propositions de $v$ suivent son ordre de préférence, donc il a proposé à $u$ avant son partenaire final.

Puisqu'il n'est pas avec $u$ à l'arrêt, il a été rejeté soit immédiatement, soit à l'occasion d'un remplacement.

Au moment du rejet, $u$ détenait un partenaire qu'il préférait à $v$.

Le partenaire de $u$ ne peut ensuite que s'améliorer dans son ordre de préférence.

Ainsi $u$ préfère $m_A(u)$ à $v$.

**Aucune paire ne bloque $A$, qui est stable.**

### Question 21

> [!INDICATION]
> Étudiez l'instant où le dernier sommet de $U$ reçoit sa toute première proposition.

> [!INDICATION]
> Toutes les autres personnes de $U$ ont déjà un partenaire à cet instant. Que reste-t-il à faire après cette acceptation ?

#### Solution

Pour $n\ge1$, soit $u_\mathrm{f}$ le dernier élément de $U$ à recevoir sa première proposition.

Juste avant celle-ci, les $n-1$ autres éléments de $U$ sont appariés par la propriété de Q18.

La proposition à $u_\mathrm{f}$ crée la dernière paire et arrête la boucle.

Elle est donc la seule proposition à $u_\mathrm{f}$.

Les autres éléments de $U$ reçoivent au plus $n$ propositions chacun.

On trouve **au plus $n(n-1)+1$ tours**, strictement moins que $n^2$ si $n\ge2$.

Pour $n=1$, il y a exactement un tour.

Pour $n=0$, il n'y en a aucun.

Dans ces deux cas la borne stricte écrite ne vaut pas.

> [!PIEGE]
> Compter toutes les paires donne une borne large. Pour la rendre stricte, repérez au moins une paire qui ne donnera lieu à aucune proposition.

### Question 22

> [!INDICATION]
> Exploitez la stabilité du couplage que $v$ apprécie le moins.

> [!INDICATION]
> Imaginez que son partenaire dans l'autre couplage préfère aussi retrouver $v$. La paire serait-elle compatible avec cette stabilité ?

#### Solution

Soit $u=m_A(v)$ et supposons que $v$ préfère $A$ à $A'$.

Alors $v$ préfère $u$ à $m_{A'}(v)$.

Comme $A'$ est stable, $u$ doit préférer $m_{A'}(u)$ à $v$, sinon la paire $(v,u)$ bloquerait $A'$.

L'égalité entre ces partenaires est exclue, puisque $v$ change de partenaire entre $A$ et $A'$.

**$u$ préfère $A'$.**

### Question 23

> [!INDICATION]
> Supposez l'existence d'un rejet d'une paire réalisable et choisissez un tel rejet de façon à contrôler le passé.

> [!INDICATION]
> Dans un couplage stable contenant la paire rejetée, cherchez le partenaire du proposant retenu. Comparez son ordre à l'ordre des propositions qu'il a déjà effectuées.

#### Solution

Supposons qu'une paire réalisable soit rejetée pendant l'exécution, et considérons le premier tel rejet. Notons-le $(v,u)$ et choisissons un couplage parfait stable $A'$ contenant cette paire. Lors de ce rejet, $u$ accepte ou conserve un proposant $w$ qu'il préfère à $v$. Cela couvre le refus immédiat de $v$ et la rupture d'une acceptation provisoire.

Soit $u'=m_{A'}(w)$.

On a $u'\ne u$.

Si $w$ préférait $u'$ à $u$, il aurait proposé à $u'$ avant de proposer à $u$, donc aurait déjà été rejeté par $u'$.

Or $(w,u')$ est réalisable par définition de $A'$, ce qui contredit le choix du premier rejet d'une paire réalisable.

Ainsi $w$ préfère $u$ à $u'$, et $u$ préfère $w$ à $v$.

La paire $(w,u)$ bloque alors $A'$, contradiction.

**Aucune paire réalisable n'est rejetée.**

> [!JURY]
> Le rapport souligne qu'une acceptation n'est que provisoire. Considérer le premier rejet d'une paire réalisable traite à la fois le refus et la rupture ultérieure.

### Question 24

> [!INDICATION]
> Dans les deux cas, partez de l'ordre dans lequel $v$ doit parcourir sa liste.

> [!INDICATION]
> Distinguez le rejet d'une ancienne proposition lorsque $v$ est apparié et le rejet de toutes ses propositions passées lorsqu'il est libre.

#### Solution

1. Si $v$ est apparié à un élément moins bien classé que $M(v)$, il a d'abord proposé à $M(v)$. Comme il a poursuivi ses propositions au-delà, cette paire réalisable a été rejetée, contrairement à Q23.
2. Si $v$ est libre, toutes ses propositions antérieures ont été rejetées. Il n'a donc jamais proposé à $M(v)$. Comme il propose par ordre décroissant de préférence, toutes ses propositions étaient à des éléments strictement mieux classés que $M(v)$.

### Question 25

> [!INDICATION]
> Combinez le fait que le partenaire final appartient à un couplage parfait stable avec la borne de préférence de Q24.

#### Solution

À l'arrêt, le couplage est parfait par Q19 et stable par Q20. Le partenaire final de chaque $v$ est donc réalisable et ne peut être strictement meilleur que $M(v)$. Il est au moins aussi bien classé par Q24. Les préférences étant strictement ordonnées, ce partenaire est $M(v)$. **Le résultat est $A^*$ pour tout ordre de choix des proposants libres.**

### Question 26

**III.2 — Couplages Pareto-optimaux**

> [!INDICATION]
> Suivez les premiers choix à partir d'un sommet quelconque.

> [!INDICATION]
> La suite ne peut parcourir indéfiniment des sommets tous distincts. Isolez le segment entre deux occurrences du premier sommet répété.

#### Solution

Si les ensembles courants sont non vides, chaque sommet possède exactement un successeur, son premier choix dans l'autre ensemble. À partir d'un sommet, on suit ces successeurs. Comme le graphe est fini, un sommet finit par être répété. Le segment compris entre deux occurrences successives de la première répétition constitue un circuit. **Il existe au moins un circuit à chaque étape non vide.**

### Question 27

> [!INDICATION]
> Imaginez deux circuits passant par un même sommet et parcourez-les en partant de ce sommet.

> [!INDICATION]
> Où leurs parcours pourraient-ils diverger s'ils disposent d'un unique successeur à chaque étape ?

#### Solution

On considère des circuits simples à rotation du point de départ près, comme dans l'algorithme 4. Supposons que deux circuits distincts contiennent $x$. Partis de $x$, leurs trajets doivent suivre le même successeur à chaque étape, puisque chaque sommet n'en possède qu'un. Le premier retour à $x$ a donc lieu après la même suite de sommets pour les deux circuits. Ils sont identiques, contradiction. **Un sommet appartient à au plus un circuit simple.** Si l'on compte des tours répétés du même circuit comme des chemins fermés différents, ils correspondent au même circuit utilisé par l'algorithme.

> [!METHODE]
> L'unicité du successeur détermine intégralement une trajectoire, donc aussi le premier retour à son point de départ. Cette propriété est propre au graphe des premiers choix.

### Question 28

> [!INDICATION]
> Construisez le graphe des premiers choix avant de retirer quoi que ce soit.

> [!INDICATION]
> Dans un circuit, retenez les paires dans le sens $V$ vers $U$, puis recalculez les premiers choix à partir des seules personnes restantes.

#### Solution

Selon la définition d'un couplage, on ajoute uniquement les arcs du circuit qui vont de $V$ vers $U$. On reprend l'ordre corrigé de $u_2$ indiqué en Q17.

| Étape | Arcs issus de $V$ | Arcs issus de $U$ | Circuit |
|---|---|---|---|
| 1 | $v_1\to u_2,\ v_2\to u_1,\ v_3\to u_1$ | $u_1\to v_1,\ u_2\to v_2,\ u_3\to v_2$ | $v_1\to u_2\to v_2\to u_1\to v_1$ |
| 2 | $v_3\to u_3$ | $u_3\to v_3$ | $v_3\to u_3\to v_3$ |

Après la première étape, on a $A=\{(v_1,u_2),(v_2,u_1)\}$. Ces quatre sommets ayant été retirés, seuls $v_3,u_3$ restent. La seconde étape donne

$$
\boxed{A=\{(v_1,u_2),(v_2,u_1),(v_3,u_3)\}.}
$$

> [!JURY]
> Le rapport précise le sens des arcs à retenir. Les arcs opposés servent à trouver les circuits, puis les paires sont toujours écrites dans l'ordre proposant, partenaire.

### Question 29

> [!INDICATION]
> Cherchez une paire bloquante parmi les personnes qui n'ont pas obtenu leur premier choix.

> [!INDICATION]
> Inspectez les préférences du proposant qui n'appartient pas au premier circuit.

#### Solution

Dans le couplage de Q28, $v_3$ est apparié à $u_3$ mais préfère $u_1$.

D'autre part, $u_1$ est apparié à $v_2$ mais préfère $v_3$.

**La paire $(v_3,u_1)$ bloque ce couplage**, qui n'est donc pas stable.

### Question 30

> [!INDICATION]
> Choisissez deux personnes qui voudraient échanger leurs partenaires finaux.

> [!INDICATION]
> Comparez l'étape à laquelle chacun reçoit son partenaire. Pour la première personne appariée, repérez quels choix étaient encore disponibles, y compris en cas d'égalité d'étape.

#### Solution

À chaque étape, les circuits simples sont disjoints et alternent les deux groupes. Sur chaque circuit, les arcs de $V$ vers $U$ donnent un couplage parfait de ses sommets. On retire donc le même nombre de sommets des deux côtés, et au moins un de chaque côté par Q26. Ainsi l'algorithme termine par un couplage parfait.

Supposons que deux éléments $v,w$ de $V$ préfèrent chacun le partenaire final de l'autre.

Supposons, quitte à échanger leurs noms, que $v$ soit apparié avant $w$ ou à la même étape.

Le partenaire final de $w$ est alors encore présent au début de cette étape, même si les deux couples sont formés simultanément.

Mais $v$ reçoit, par l'arc de son circuit, son premier choix parmi les éléments encore présents.

Il ne peut donc préférer le partenaire de $w$.

**Le couplage est P-stable.**

> [!PIEGE]
> Si les deux personnes sont traitées au même tour, les deux partenaires étaient présents lors de la construction du graphe. Le raisonnement couvre aussi cette simultanéité.

### Question 31

> [!INDICATION]
> Reprenez le couplage obtenu en Q17 sur les données $D$.

> [!INDICATION]
> Cherchez deux proposants dont les partenaires seraient mieux classés si on les échangeait.

#### Solution

Pour les données $D$, le couplage de Q17 donne $u_1$ à $v_1$ et $u_2$ à $v_2$.

Or $v_1$ préfère $u_2$ à $u_1$ et $v_2$ préfère $u_1$ à $u_2$.

Ces deux éléments de $V$ souhaitent échanger leurs partenaires.

**Le couplage produit par l'algorithme 3 n'est pas P-stable sur $D$.**

### Question 32

**III.3 — Implémentation**

**III.3.1 — Algorithme de Gale-Shapley**

> [!INDICATION]
> Le rang est la position dans la liste, tandis que l'indice de colonne de la table résultat est l'identifiant de la personne classée.

#### Solution

Pour chaque $u$, si le candidat $v$ occupe la position $j$ dans la ligne de $u$, alors son rang est $j$.

```c
void calcule_rang(int Lu[n][n], int Rang[n][n])
{
    for (int u = 0; u < n; ++u) {
        for (int j = 0; j < n; ++j) {
            Rang[u][Lu[u][j]] = j;
        }
    }
}
```

### Question 33

> [!INDICATION]
> Choisissez une valeur qui ne peut être un identifiant valide. Pour la prochaine proposition, cherchez le premier rang dans une liste indexée à partir de zéro.

#### Solution

**Pour tout indice $i$, initialiser `CoupleV[i]` et `CoupleU[i]` à `-1`, puis `USuiv[i]` à `0`.** La valeur `-1` signale une personne libre, et le rang zéro désigne le premier choix.

### Question 34

> [!INDICATION]
> Au début du tour, cherchez le plus petit proposant libre en relisant le tableau des partenaires.

> [!INDICATION]
> Consommez son prochain rang même en cas de refus. Lors d'une substitution, maintenez les deux tableaux de partenaires cohérents.

#### Solution

À chaque tour, on choisit le premier $v$ libre, puis on incrémente le rang de sa prochaine proposition avant de traiter celle-ci. Lors d'une substitution, l'ancien partenaire de $u$ redevient libre. L'argument de Q18 garantit que le rang lu pour un $v$ libre est strictement inférieur à $n$.

```c
void gale_shapley(int Lv[n][n], int Lu[n][n],
                  int CoupleU[n], int CoupleV[n])
{
    int Rang[n][n];
    int USuiv[n];
    calcule_rang(Lu, Rang);

    for (int i = 0; i < n; ++i) {
        CoupleU[i] = -1;
        CoupleV[i] = -1;
        USuiv[i] = 0;
    }

    while (1) {
        int v = 0;
        while (v < n && CoupleV[v] != -1) {
            ++v;
        }
        if (v == n) {
            return;
        }

        int u = Lv[v][USuiv[v]];
        ++USuiv[v];
        int ancien = CoupleU[u];

        if (ancien == -1 || Rang[u][v] < Rang[u][ancien]) {
            if (ancien != -1) {
                CoupleV[ancien] = -1;
            }
            CoupleU[u] = v;
            CoupleV[v] = u;
        }
    }
}
```

> [!JURY]
> Le rapport relève l'oubli fréquent des initialisations dans le corps de la fonction. Les tableaux passés en argument ne contiennent pas encore les valeurs de Q33.

**III.3.2 — Algorithme de couplage par graphe orienté**

### Question 35

> [!INDICATION]
> Pour ajouter en tête, allouez le nouveau nœud, raccordez-le à l'ancienne tête, puis modifiez le champ dans le graphe.

#### Solution

Les fonctions suivantes reprennent la constante `n` et les types de l'énoncé. On garde une seule occurrence de chaque arc et on effectue toute nouvelle insertion en tête. Une assertion vérifie chaque allocation.

```c
#include <assert.h>
#include <stdlib.h>

void ajoute_arc(graphe *g, int i, int j)
{
    for (liste courant = g->liste_adjacence[i]; courant != NULL;
         courant = courant->suivant) {
        if (courant->individu == j) {
            return;
        }
    }
    liste nouveau = malloc(sizeof(struct noeud));
    assert(nouveau != NULL);
    nouveau->individu = j;
    nouveau->suivant = g->liste_adjacence[i];
    g->liste_adjacence[i] = nouveau;
}
```

### Question 36

> [!INDICATION]
> Cherchez l'arc en parcourant la liste et pensez à la suppression en tête.

> [!INDICATION]
> Une façon d'unifier les deux cas est de conserver l'adresse du lien qui pointe vers le nœud courant.

#### Solution

Le pointeur `lien` désigne le champ à modifier si l'on trouve la destination. Ce champ est soit la tête de liste, soit le champ `suivant` du nœud précédent.

```c
void supprime_arc(graphe *g, int i, int j)
{
    liste *lien = &g->liste_adjacence[i];
    while (*lien != NULL && (*lien)->individu != j) {
        lien = &(*lien)->suivant;
    }
    if (*lien != NULL) {
        liste retire = *lien;
        *lien = retire->suivant;
        free(retire);
    }
}
```

> [!JURY]
> Le rapport signale deux oublis courants. Il faut tester le pointeur avant de le déréférencer, puis libérer le nœud effectivement retiré.

### Question 37

> [!INDICATION]
> Distinguez les listes contenant les arcs qui partent de $s$ de celles qui peuvent contenir un arc vers $s$.

> [!INDICATION]
> Ne modifiez pas la numérotation des sommets. Réutilisez la fonction de suppression d'un arc pour les listes des autres sommets.

#### Solution

On libère la liste des arcs sortants, puis on supprime chaque éventuel arc entrant des listes restantes. Le nombre de sommets et leurs indices restent inchangés.

```c
void supprime_sommet(graphe *g, int s)
{
    liste courant = g->liste_adjacence[s];
    while (courant != NULL) {
        liste suivant = courant->suivant;
        free(courant);
        courant = suivant;
    }
    g->liste_adjacence[s] = NULL;

    for (int i = 0; i < g->nb_sommets; ++i) {
        if (i != s) {
            supprime_arc(g, i, s);
        }
    }
}
```

### Question 38

> [!INDICATION]
> Allouez le graphe et ses têtes de listes avant d'ajouter un arc.

> [!INDICATION]
> Les matrices emploient des numéros locaux. Appliquez le décalage seulement à une origine ou une destination qui représente une personne de $U$.

#### Solution

On initialise les $2n$ listes à vide.

Pour chaque indice local $i$, le premier choix de $i\in V$ est le sommet $n+\mathrm{Lv}[i][0]$.

Le premier choix du sommet $n+i$ est $\mathrm{Lu}[i][0]$, déjà numéroté dans $V$.

```c
graphe *construit_graphe(int Lv[n][n], int Lu[n][n])
{
    graphe *g = malloc(sizeof(graphe));
    assert(g != NULL);
    g->nb_sommets = 2 * n;
    g->liste_adjacence = malloc((2 * n) * sizeof(liste));
    assert(g->liste_adjacence != NULL);
    for (int i = 0; i < 2 * n; ++i) {
        g->liste_adjacence[i] = NULL;
    }
    for (int i = 0; i < n; ++i) {
        ajoute_arc(g, i, n + Lv[i][0]);
        ajoute_arc(g, n + i, Lu[i][0]);
    }
    return g;
}
```

> [!METHODE]
> Écrire les intervalles des deux groupes avant d'indexer les tableaux. On lit chaque préférence avec un indice local puis on transforme seulement l'extrémité qui appartient à $U$.

## Bilan

- Pour les grammaires, distinguer une suite de dérivation et un arbre, puis exploiter la structure des séparateurs pour établir une inclusion de langages.
- Pour une réduction polynomiale, préciser ce que l'on calcule, ce qui rend l'instance valide et pourquoi les deux réponses coïncident.
- Pour une boucle de propositions, séparer l'invariant de couplage, la possibilité de faire le tour suivant et le variant strictement décroissant.
- Dans les listes chaînées, tracer les références modifiées avant de libérer la cellule. Dans les graphes à deux groupes, distinguer le numéro local et le numéro global.
- Refaire Q9–Q10 pour la disjonction de cas, Q23–Q25 pour le premier événement interdit, et Q34–Q38 pour le suivi des indices et des pointeurs.
