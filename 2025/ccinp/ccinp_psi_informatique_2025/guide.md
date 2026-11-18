# CCINP PSI — Informatique 2025 · Corrigé guidé

*Corrigé rédigé par IA, non officiel. Signalez toute erreur.*

## Présentation du sujet

L’épreuve comporte des requêtes SQL, des fonctions Python et une preuve de correction. Les réponses aux tableaux reprennent les colonnes et les rangs du document réponse.

## Partie I — Gestion des randonnées dans une base de données

On identifie les clés puis on construit les requêtes de sélection, de jointure et de dénombrement.

### Question 1

> [!INDICATION]
> Deux randonnées distinctes peuvent-elles recevoir le même intitulé ? Cherchez un attribut prévu pour l’identification.

#### Solution

Deux itinéraires différents peuvent porter le même titre, par exemple « Tour du lac ». Une clé primaire doit identifier une seule ligne. **L’attribut `Id` de `Randonnee`** est prévu à cet effet.

### Question 2

> [!INDICATION]
> Quel attribut désigne un objet stocké dans une autre table ?

#### Solution

**`Randonnee.IdAuteur`** est une clé étrangère qui référence `Auteur.Id`.

### Question 3

> [!INDICATION]
> Distinguez les attributs à afficher et celui qui permet de filtrer.

#### Solution

On filtre le type d’activité et on projette les trois attributs demandés.

```sql
SELECT Titre, Lieu, Distance
FROM Randonnee
WHERE Type = 'Pied';
```

### Question 4

> [!INDICATION]
> Sélectionnez d’abord les activités utiles, puis formez un groupe par auteur.

> [!INDICATION]
> Triez le résultat de l’agrégation sur l’effectif calculé.

#### Solution

Le filtrage se fait avant le regroupement par auteur. Le nombre de lignes de chaque groupe compte les activités retenues.

```sql
SELECT IdAuteur, COUNT(*) AS NbActivites
FROM Randonnee
WHERE Type = 'Pied' AND Niveau = 3
GROUP BY IdAuteur
ORDER BY NbActivites DESC;
```

> [!JURY]
> Le jury relève l’oubli du regroupement. Le filtre sur le type et le niveau sélectionne les lignes avant l’agrégation.

### Question 5

> [!INDICATION]
> Reliez la clé étrangère de la randonnée à la clé primaire de son auteur.

#### Solution

La jointure relie chaque ligne de randonnée à son auteur par la clé étrangère.

```sql
SELECT A.Pseudo, R.Titre
FROM Auteur AS A
JOIN Randonnee AS R ON R.IdAuteur = A.Id;
```

> [!PIEGE]
> Les deux tables ont chacune un attribut Id. La qualification par l’alias de table évite de confondre les identifiants.

### Question 6

> [!INDICATION]
> Filtrez d’abord les activités du bon type puis classez les effectifs par auteur.

> [!INDICATION]
> Regroupez sur l’identifiant, même si deux auteurs ont le même nom.

#### Solution

On regroupe les randonnées à cheval par identifiant d’auteur et on garde un groupe d’effectif maximal. Le tri par identifiant départage les éventuels ex æquo.

```sql
SELECT A.Nom, A.Prenom
FROM Auteur AS A
JOIN Randonnee AS R ON R.IdAuteur = A.Id
WHERE R.Type = 'Cheval'
GROUP BY A.Id, A.Nom, A.Prenom
ORDER BY COUNT(*) DESC, A.Id
LIMIT 1;
```

## Partie II — Quelques calculs de dénivelés

Les itinéraires sont des listes de triplets. On distingue altitude maximale, écart au départ et cumul des montées, puis on applique deux méthodes de correction.

### Question 7

> [!INDICATION]
> Utilisez le mot-clé Python qui rend accessible tout un module.

#### Solution

```python
import gpxpy
```

### Question 8

> [!INDICATION]
> Repérez la composante ajoutée et lisez le dénominateur de la division finale.

#### Solution

La somme des altitudes est $100+102+110+108=420$. La fonction retourne donc **$105{,}0$ mètres**, la moyenne arithmétique des altitudes des quatre points mesurés.

### Question 9

> [!INDICATION]
> Comparez le coût d’un passage dans la boucle et le nombre de passages.

#### Solution

Pour une liste de longueur $n$, l’initialisation, les accès indexés et la division finale se font en temps constant. Chacune des $n$ itérations fait un nombre constant d’opérations. **Le temps est linéaire, en $\Theta(n)$.**

### Question 10

> [!INDICATION]
> Choisissez une initialisation valable même au-dessous du niveau de la mer.

#### Solution

On initialise le maximum avec l’altitude d’un point réel du parcours. Cela couvre aussi les parcours dont toutes les altitudes sont négatives.

```python
def altitude_maximale(iti):
    plus_haute = iti[0][2]
    for i in range(1, len(iti)):
        altitude = iti[i][2]
        if altitude > plus_haute:
            plus_haute = altitude
    return plus_haute
```

> [!JURY]
> L’initialisation avec une altitude du parcours couvre les valeurs négatives sans utiliser de fonction de maximum.

### Question 11

> [!INDICATION]
> Identifiez quels points donnent les deux altitudes à soustraire.

#### Solution

Le parcours doit contenir son point de départ. Son altitude est celle du premier triplet.

```python
def denivele_global(iti):
    return altitude_maximale(iti) - iti[0][2]
```

### II.1 — Premier calcul de dénivelé positif

### Question 12

> [!INDICATION]
> Comparez deux points successifs et vérifiez la première valeur de l’indice.

> [!INDICATION]
> Ne cumulez que les accroissements qui correspondent à une montée.

#### Solution

Pour chaque paire successive, on calcule l’altitude d’arrivée moins celle de départ. On ajoute uniquement les différences strictement positives. Une liste de moins de deux points donne zéro.

```python
def denivele_positif_cumule(iti):
    total = 0.0
    for i in range(1, len(iti)):
        difference = iti[i][2] - iti[i - 1][2]
        if difference > 0:
            total = total + difference
    return total
```

### II.2 — Lissage des altitudes

### Question 13

> [!INDICATION]
> Déterminez la première position hors de la fenêtre.

> [!INDICATION]
> Divisez par le nombre de positions réellement parcourues, surtout en fin de liste.

#### Solution

Le pas $p$ est positif. À l’indice $i$, la fenêtre va de $i$ à $\min(i+p,n)-1$. On divise par le nombre de valeurs réellement présentes, ce qui traite les dernières fenêtres raccourcies.

```python
def alt_glissante(liste_alt, p):
    n = len(liste_alt)
    resultat = []
    for i in range(n):
        fin = min(i + p, n)
        total = 0.0
        for j in range(i, fin):
            total = total + liste_alt[j]
        resultat.append(total / (fin - i))
    return resultat
```

> [!PIEGE]
> Au dernier indice, la fenêtre contient un seul point. Les bornes du parcours et le dénominateur doivent le refléter ensemble.

### Question 14

> [!INDICATION]
> Comptez les additions pour un indice de départ fixé puis additionnez ces coûts.

#### Solution

À l’indice $i$, la boucle intérieure effectue $\min(p,n-i)$ additions.

Le nombre total d’additions vaut $\sum_{k=1}^n\min(p,k)$. Si $p\le n$, cette somme vaut $p(p-1)/2+p(n-p+1)$. Sinon, elle vaut $n(n+1)/2$.

Ainsi, pour $n\ge1$, **le temps est en $\Theta(n\min(p,n))$**, donc en $O(np)$, et la liste résultat occupe un espace linéaire.

### II.3 — Utilisation d’altitudes de référence

### Question 15

> [!INDICATION]
> Regardez ce que contient une clé de dictionnaire et ce que la boucle prélève dans cette clé.

#### Solution

Les deux variables sont des **listes de flottants** dans le modèle. La boucle ajoute respectivement la latitude et la longitude de chaque clé de `dem`. Les coordonnées peuvent donc se répéter avec les différents points de la grille. Ces listes suivent l’ordre de parcours du dictionnaire à ce stade.

### Question 16

> [!INDICATION]
> Inspectez les opérations appliquées à chaque argument et la valeur effectivement renvoyée.

#### Solution

Dans le contexte des coordonnées, les signatures sont **`auxiliaire(x: list, y: list) -> list`** et **`principal(x: list) -> list`**, avec des listes de flottants. Les accès par indice, les tranches et les méthodes `pop` et `append` portent sur des listes. Chaque fonction retourne l’une de ces listes ou le résultat d’un autre appel qui retourne une liste.

### Question 17

> [!INDICATION]
> La fonction s’appelle-t-elle elle-même ? Comment la taille du problème change-t-elle ?

#### Solution

Cocher **Récursif** et **Diviser pour régner**. La fonction s’appelle sur deux moitiés du problème, puis combine leurs résultats.

### Question 18

> [!INDICATION]
> Cherchez une quantité entière qui diminue à chaque appel pour chacune des deux fonctions.

#### Solution

Pour une liste d’au moins deux éléments, les deux tranches de `principal` sont de longueur strictement inférieure. La récursion atteint donc le cas d’une liste de longueur zéro ou un.

Pour `auxiliaire`, le variant est $\texttt{len(x)}+\texttt{len(y)}$. Tant que les deux listes sont non vides, l’appel récursif retire exactement un élément. Une liste finit ainsi par être vide et déclenche le retour.

> [!JURY]
> Citer le cas d’arrêt ne suffit pas à expliquer qu’on y arrive. Le rapport attend aussi un variant pour auxiliaire.

### Question 19

> [!INDICATION]
> Reconnaissez d’abord la façon dont le problème est découpé, puis le rôle de la combinaison finale.

#### Solution

C’est un **tri fusion**. La fonction `principal` trie récursivement les deux moitiés. La fonction `auxiliaire` retire le plus grand dernier élément des deux listes triées, fusionne récursivement le reste puis ajoute cet élément à la fin.

### Question 20

> [!INDICATION]
> Conservez une borne stricte à gauche et large à droite.

> [!INDICATION]
> Prenez un milieu entier et comparez les écarts lorsque les indices sont adjacents.

#### Solution

L’encadrement strict à gauche et large à droite est conservé en remplaçant l’une des deux bornes par l’indice milieu. Dans le dernier test, une égalité des écarts sélectionne la borne gauche.

```python
def ref(valeur, liste_ref):
    ind_deb = 0                                      # Ligne 5
    ind_fin = len(liste_ref) - 1                     # Ligne 6
    while ind_deb < ind_fin - 1:
        k = (ind_deb + ind_fin) // 2                 # Ligne 8
        if valeur <= liste_ref[k]:
            ind_fin = k                              # Ligne 10
        else:
            ind_deb = k                              # Ligne 12
    if liste_ref[ind_fin] - valeur < valeur - liste_ref[ind_deb]:
        return liste_ref[ind_fin]                    # Ligne 15
    else:
        return liste_ref[ind_deb]                    # Ligne 17
```

### Question 21

> [!INDICATION]
> Trouvez la clé de référence en traitant les coordonnées séparément.

> [!INDICATION]
> Un nouveau triplet doit contenir les coordonnées mesurées et une altitude issue de la grille.

#### Solution

Les nouvelles coordonnées servent de clé du dictionnaire. Dans le nouvel itinéraire, on conserve les latitude et longitude mesurées. Le cas d’une coordonnée égale à une borne est traité directement, puisque `ref` suppose un encadrement strict.

```python
def standardise(liste_parcours):
    def plus_proche(valeur, grille):
        if valeur == grille[0] or valeur == grille[len(grille) - 1]:
            return valeur
        return ref(valeur, grille)

    resultat = []
    for latitude, longitude, altitude in liste_parcours:
        lat = plus_proche(latitude, lat_ref)
        lon = plus_proche(longitude, long_ref)
        resultat.append((latitude, longitude, dem[(lat, lon)]))
    return resultat
```

> [!JURY]
> Le document demande un nouvel itinéraire. Construisez-le sans modifier la liste reçue et ajoutez chaque tuple comme un seul élément.

## Partie III — Organisation d’un trek

On compare un choix local avec les recherches de plus court chemin. Les étiquettes provisoires et définitives ont des rôles distincts.

### III.1 — Première idée : algorithme intuitif

### Question 22

> [!INDICATION]
> Repérez le critère de sélection d’un voisin parmi les sommets encore admissibles.

#### Solution

La boucle choisit, parmi les voisins du sommet actuel qui n’ont pas été visités, celui relié par l’arête de plus faible difficulté. C’est une étape **gloutonne**, qui minimise le coût immédiat du prochain déplacement.

### Question 23

> [!INDICATION]
> Appliquez le choix local à chaque étape et additionnez les seuls poids réellement parcourus.

#### Solution

Le programme choisit successivement $c,d,e,f$. Le résultat est **`(["a", "c", "d", "e", "f"], 8)`**. Le coût vaut $2+4+1+1=8$.

### Question 24

> [!INDICATION]
> Comparez la route obtenue à une route qui utilise dès le départ une autre arête.

#### Solution

Le chemin $a,d,e,f$ coûte $4+1+1=6$, alors que le programme retourne un chemin de coût 8. **Le choix glouton ne garantit donc pas la difficulté cumulée minimale.**

> [!METHODE]
> Un chemin réalisable strictement moins coûteux suffit à réfuter l’optimalité du résultat glouton.

### III.2 — Deuxième idée : l’algorithme de Dijkstra

### Question 25

> [!INDICATION]
> Aux étapes 4 et 5, partez du sommet de la frontière dont l’étiquette est minimale.

> [!INDICATION]
> Ne changez une étiquette que si le nouveau coût est strictement inférieur.

#### Solution

Voici les deux lignes à compléter dans le document réponse. Chaque couple indique une distance et le prédécesseur correspondant.

$$
\begin{array}{c|cccccccc}
\text{Étape} & \text{sTraite} & a & b & c & d & e & f & aVisiter\\ \hline
4 & d & (0,\ a) & (3,\ a) & (2,\ a) & (4,\ a) & (5,\ d) & (8,\ d) & \texttt{["e",\ "f"]} \\
5 & e & (0,\ a) & (3,\ a) & (2,\ a) & (4,\ a) & (5,\ d) & (6,\ e) & \texttt{["f"]}
\end{array}
$$

Depuis $d$, la distance de $e$ passe à 5 et $f$ est découvert au coût 8. Le traitement de $e$ ramène le coût de $f$ à 6. Le programme traite ensuite $f$ avant de sortir de la boucle. Cette dernière itération ne change aucune étiquette du tableau.

### Question 26

> [!INDICATION]
> Suivez la seconde composante des couples en remontant, puis lisez la première composante en fin de chemin.

#### Solution

Le chemin est reconstruit à rebours en suivant les prédécesseurs jusqu’au sommet initial. L’inversion finale, déjà donnée, remet les sommets dans l’ordre du départ vers l’arrivée.

```python
while s != sInit:          # Ligne 8
    s = distance[s][1]     # Ligne 9
    chemin.append(s)       # Ligne 10
```

À la ligne 15, le dernier argument de `print` est **`distance[sFin][0]`**. Ici le chemin est `["a", "d", "e", "f"]` et son coût est 6.

### Question 27

> [!INDICATION]
> Les tests demandent surtout de connaître l’état d’un sommet. Quelle structure permet de l’obtenir directement ?

#### Solution

Le test sur `aVisiter` sert à éviter des doublons. Une table de statuts par sommet peut distinguer « inconnu », « à visiter » et « traité ». Un seul accès à un dictionnaire permet de décider s’il faut ajouter le voisin, mettre à jour son étiquette ou passer au suivant. On peut conserver `aVisiter` pour la recherche du minimum et éviter d’y faire des recherches linéaires d’appartenance.

### Question 28

> [!INDICATION]
> Suivez les couches d’égale distance et l’ordre d’insertion des voisins.

> [!INDICATION]
> Arrêtez-vous au traitement du sommet d’arrivée.

#### Solution

Les arêtes ont toutes un poids de 1. Les sommets d’une même couche sont traités dans l’ordre d’insertion, car `cherche_min` ne remplace son choix qu’en présence d’une distance strictement plus petite.

- Depuis `a1` vers `j1` : **`a1, b1, c1, d1, e1, f1, g1, h1, i1, j1`**.
- Depuis `j1` vers `a1` : **`j1, g1, c1, a1`**.

### III.3 — Troisième idée : l’algorithme de Dijkstra bidirectionnel

### Question 29

> [!INDICATION]
> Quand les deux minima sont égaux, comparez d’abord les tailles des frontières.

> [!INDICATION]
> Actualisez les étiquettes de la direction traitée et comparez ensuite tous les raccords.

#### Solution

À l’étape 3, les deux minima valent 2. La liste backward comporte deux sommets, contre trois en forward. On traite donc $d$ en backward.

En partant de l’étiquette 2 de $d$, les distances arrière de $a,b,c$ deviennent respectivement 6, 4 et 6.

$$
\begin{array}{c|ccccccc}
\text{Étape} & \text{Traité} & a & b & c & d & e & f\\ \hline
4 & \text{d, B} & (0,\ a)\,/\,(6,\ d) & (3,\ a)\,/\,(4,\ d) & (2,\ a)\,/\,(6,\ d) & (4,\ a)\,/\,(2,\ e) & (\infty,\ a)\,/\,(1,\ f) & (\infty,\ a)\,/\,(0,\ f)
\end{array}
$$

Dans chaque case, le couple forward précède le couple backward.

$$
\begin{array}{c|ccccc}
\text{Étape} & \text{Fmin} & \text{Bmin} & \text{BFmin} & aVisiterF & aVisiterB\\ \hline
4 & 2 & 4 & 6 & \texttt{["b",\ "c",\ "d"]} & \texttt{["b",\ "a",\ "c"]}
\end{array}
$$

> [!METHODE]
> Une étiquette finie signifie que le sommet est atteint. L’étiquette devient définitive lorsqu’il est traité.

### Question 30

> [!INDICATION]
> Relisez le premier raccord fini du document réponse et comparez-le au dernier coût connu.

#### Solution

**Non.** Au premier sommet atteint dans les deux sens, à l’étape 2, le raccord en $d$ donne un coût 8.

Le chemin $a,d,e,f$ de coût 6 existe pourtant. Un premier raccord ne fournit qu’une borne supérieure sur la distance optimale.

> [!JURY]
> Le tableau précédent donne un contre-exemple direct à l’arrêt au premier raccord.

### Question 31

> [!INDICATION]
> Initialisez la recherche arrière à la destination et utilisez le critère d’arrêt de l’énoncé.

> [!INDICATION]
> Pour les trois minima, identifiez quelles étiquettes et quelles listes interviennent.

#### Solution

Dans le document-réponse, les lignes 4 et 5 s’initialisent avec `aVisiterB = [Sf]` et `dejaVisitesB = []`. À la ligne 13, le test est `BFmin > Fmin + Bmin`. Aux lignes 21 et 22, on prend le minimum des distances des sommets de la frontière correspondante. La ligne 23 calcule les coûts de raccordement aux sommets présents dans les deux dictionnaires.

```python
Fmin = min([distanceF[v][0] for v in aVisiterF if v in distanceF])  # 21
Bmin = min([distanceB[v][0] for v in aVisiterB if v in distanceB])  # 22
L = [distanceF[v][0] + distanceB[v][0] for v in distanceB
     if v in distanceF]                                         # 23
```

Voici la fonction complète. Elle ajoute le cas immédiat `Sd == Sf` et les gardes pour les frontières vides.

```python
def dijkstra_bidirectionnel(graph, Sd, Sf):
    infini = float("inf")
    aVisiterF = [Sd]
    dejaVisitesF = []
    aVisiterB = [Sf]                                  # Ligne 4
    dejaVisitesB = []                                 # Ligne 5
    distanceF = {s: (infini, Sd) for s in graph}
    distanceB = {s: (infini, Sf) for s in graph}
    distanceF[Sd] = (0, Sd)
    distanceB[Sf] = (0, Sf)
    Fmin, Bmin = 0, 0
    BFmin = infini
    if Sd == Sf:
        BFmin = 0

    while BFmin > Fmin + Bmin:                        # Ligne 13
        if Fmin < Bmin or (
            Fmin == Bmin and len(aVisiterF) <= len(aVisiterB)
        ):
            sTraite = cherche_min(distanceF, aVisiterF)
            unpas(graph, sTraite, distanceF, dejaVisitesF, aVisiterF)
        else:
            sTraite = cherche_min(distanceB, aVisiterB)
            unpas(graph, sTraite, distanceB, dejaVisitesB, aVisiterB)

        Fmin = infini
        if len(aVisiterF) > 0:
            Fmin = min([distanceF[v][0] for v in aVisiterF])
        Bmin = infini
        if len(aVisiterB) > 0:
            Bmin = min([distanceB[v][0] for v in aVisiterB])
        L = [distanceF[v][0] + distanceB[v][0] for v in distanceB
             if v in distanceF]                      # Ligne 23
        BFmin = min(L)
    return BFmin
```

Le minimum d’une frontière vide vaut l’infini. À la ligne 23, `L` contient au moins le coût de raccord en `Sd`, puisque les deux dictionnaires ont été initialisés sur tous les sommets. Le code emploie les fonctions `cherche_min` et `unpas` données en III.2.

### Question 32

> [!INDICATION]
> Si un sommet n’a été traité dans aucun sens, minorez chacune de ses vraies distances par le minimum de la frontière correspondante.

#### Solution

Notons $D$ le coût du chemin supposé strictement meilleur que `BFmin`. Pour un sommet $s_i$ de ce chemin, la somme de ses vraies distances aux deux extrémités est au plus $D$, en comparant au préfixe et au suffixe du chemin.

Dans chaque direction, un sommet non traité est à une distance réelle au moins égale au minimum de la frontière. En effet, sur un plus court chemin, le premier sommet non traité a reçu l’étiquette exacte lors de la relaxation depuis son prédécesseur déjà traité. Si aucun sommet de ce chemin n’a encore été traité, ce premier sommet est la source, d’étiquette zéro. La non-négativité des poids transmet la minoration aux suivants.

Si $s_i$ n’était traité dans aucun sens, on aurait donc
$$
\begin{aligned}
D&\ge d(s,s_i)+d(s_i,t),\\
d(s,s_i)+d(s_i,t)&\ge \texttt{Fmin}+\texttt{Bmin}\ge\texttt{BFmin},
\end{aligned}
$$
la dernière inégalité étant le critère d’arrêt. C’est contradictoire. **Chaque $s_i$ est traité dans au moins une direction.**

### Question 33

> [!INDICATION]
> Pourquoi les extrémités ne peuvent-elles être traitées depuis la direction opposée ?

> [!INDICATION]
> Sur le chemin, prenez le premier sommet qui quitte l’ensemble traité en forward.

#### Solution

Le sommet $s$ ne peut avoir été traité en backward. Son étiquette arrière serait alors la distance exacte entre $s$ et $t$, au plus $D$.

Avec son étiquette forward nulle, le raccord en $s$ donnerait $\texttt{BFmin}\le D$, contradiction. De même, $t$ ne peut avoir été traité en forward.

Par Q32, $s$ est donc traité en forward, tandis que $t$ est traité en backward. Prenons le premier sommet du chemin qui n’a pas été traité en forward. Son prédécesseur $s_{i_0}$ a été traité en forward et, par Q32, ce sommet $s_{i_0+1}$ a été traité en backward.

### Question 34

> [!INDICATION]
> Quel coût provisoire obtient l’extrémité backward de l’arête de passage après relaxation ?

> [!INDICATION]
> Ajoutez à cette étiquette le coût arrière déjà définitif.

#### Solution

Posons $u=s_{i_0}$ et $v=s_{i_0+1}$. L’étiquette forward de $u$ est exacte et ne dépasse pas le coût du préfixe jusqu’à $u$.

Le traitement de $u$ a relaxé l’arête $uv$, sauf si $v$ avait déjà une étiquette forward définitive. Dans les deux cas, l’étiquette forward finale de $v$ ne dépasse pas le coût du préfixe jusqu’à $v$.

L’étiquette backward de $v$ est exacte et ne dépasse pas le coût du suffixe à partir de $v$. Ainsi le raccord en $v$ donne une somme au plus $D$, ce qui contredit $\texttt{BFmin}>D$. Tout raccord fini représenté par `BFmin` est un trajet réalisable dans le graphe non orienté. **À l’arrêt, la valeur renvoyée est donc optimale.**

> [!METHODE]
> La correction partielle établit la propriété du résultat si l’algorithme s’arrête. Le raisonnement se place à un état où le test d’arrêt est satisfait.

## Bilan

- Distinguez en SQL la sélection des lignes, le regroupement et l’ordre du résultat.
- Pour un parcours de liste, vérifiez les bornes ainsi que l’effet des cas d’une liste vide, d’un point unique ou d’une fenêtre tronquée.
- Dans Dijkstra, suivez la frontière, les prédécesseurs et les étiquettes définitives. Pour l’arrêt bidirectionnel, comparez le meilleur chemin connu aux deux minima de frontière.
