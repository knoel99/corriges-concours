# CCINP PC — Informatique 2025 · Corrigé brut

*Corrigé rédigé par IA, non officiel. Signalez toute erreur.*

## Partie I — Gestion des randonnées dans une base de données

### Question 1

Deux itinéraires différents peuvent porter le même titre, par exemple « Tour du lac ». Une clé primaire doit identifier une seule ligne. **L’attribut `Id` de `Randonnee`** est prévu à cet effet.

### Question 2

**`Randonnee.IdAuteur`** est une clé étrangère qui référence `Auteur.Id`.

### Question 3

On filtre le type d’activité et on projette les trois attributs demandés.

```sql
SELECT Titre, Lieu, Distance
FROM Randonnee
WHERE Type = 'Pied';
```

### Question 4

Le filtrage se fait avant le regroupement par auteur. Le nombre de lignes de chaque groupe compte les activités retenues.

```sql
SELECT IdAuteur, COUNT(*) AS NbActivites
FROM Randonnee
WHERE Type = 'Pied' AND Niveau = 3
GROUP BY IdAuteur
ORDER BY NbActivites DESC;
```

### Question 5

La jointure relie chaque ligne de randonnée à son auteur par la clé étrangère.

```sql
SELECT A.Pseudo, R.Titre
FROM Auteur AS A
JOIN Randonnee AS R ON R.IdAuteur = A.Id;
```

### Question 6

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

### Question 7

```python
import gpxpy
```

### Question 8

La somme des altitudes est $100+102+110+108=420$. La fonction retourne donc **$105{,}0$ mètres**, la moyenne arithmétique des altitudes des quatre points mesurés.

### Question 9

Pour une liste de longueur $n$, l’initialisation, les accès indexés et la division finale se font en temps constant. Chacune des $n$ itérations fait un nombre constant d’opérations. **Le temps est linéaire, en $\Theta(n)$.**

### Question 10

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

### Question 11

Le parcours doit contenir son point de départ. Son altitude est celle du premier triplet.

```python
def denivele_global(iti):
    return altitude_maximale(iti) - iti[0][2]
```

### II.1 — Premier calcul de dénivelé positif

### Question 12

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

Le pas $p$ est positif. À l’indice $i$, la fenêtre va de $i$ à $\min(i+p,n)-1$. On divise par le nombre de valeurs réellement présentes, ce qui traite les dernières fenêtres raccourcies.

```python
def alt_glissante(liste_alt, p):
    n = len(liste_alt)
    resultat = []
    for i in range(n):
        fin = i + p
        if fin > n:
            fin = n
        total = 0.0
        for j in range(i, fin):
            total = total + liste_alt[j]
        resultat.append(total / (fin - i))
    return resultat
```

### Question 14

À l’indice $i$, la boucle intérieure effectue $\min(p,n-i)$ additions.

Le nombre total d’additions vaut $\sum_{k=1}^n\min(p,k)$. Si $p\le n$, cette somme vaut $p(p-1)/2+p(n-p+1)$. Sinon, elle vaut $n(n+1)/2$.

Ainsi, pour $n\ge1$, **le temps est en $\Theta(n\min(p,n))$**, donc en $O(np)$, et la liste résultat occupe un espace linéaire.

### II.3 — Utilisation d’altitudes de référence

### Question 15

Les deux variables sont des **listes de flottants** dans le modèle. La boucle ajoute respectivement la latitude et la longitude de chaque clé de `dem`. Les coordonnées peuvent donc se répéter avec les différents points de la grille. Ces listes suivent l’ordre de parcours du dictionnaire à ce stade.

### Question 16

Dans le contexte des coordonnées, les signatures sont **`auxiliaire(x: list, y: list) -> list`** et **`principal(x: list) -> list`**, avec des listes de flottants. Les accès par indice, les tranches et les méthodes `pop` et `append` portent sur des listes. Chaque fonction retourne l’une de ces listes ou le résultat d’un autre appel qui retourne une liste.

### Question 17

Cocher **Récursif** et **Diviser pour régner**. La fonction s’appelle sur deux moitiés du problème, puis combine leurs résultats.

### Question 18

Pour une liste d’au moins deux éléments, les deux tranches de `principal` sont de longueur strictement inférieure. La récursion atteint donc le cas d’une liste de longueur zéro ou un.

Pour `auxiliaire`, le variant est $\texttt{len(x)}+\texttt{len(y)}$. Tant que les deux listes sont non vides, l’appel récursif retire exactement un élément. Une liste finit ainsi par être vide et déclenche le retour.

### Question 19

C’est un **tri fusion**. La fonction `principal` trie récursivement les deux moitiés. La fonction `auxiliaire` retire le plus grand dernier élément des deux listes triées, fusionne récursivement le reste puis ajoute cet élément à la fin.

### Question 20

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

## Partie III — Organisation d’un trek

### III.1 — Première idée : algorithme intuitif

### Question 22

La boucle choisit, parmi les voisins du sommet actuel qui n’ont pas été visités, celui relié par l’arête de plus faible difficulté. C’est une étape **gloutonne**, qui minimise le coût immédiat du prochain déplacement.

### Question 23

Le programme choisit successivement $c,d,e,f$. Le résultat est **`(["a", "c", "d", "e", "f"], 8)`**. Le coût vaut $2+4+1+1=8$.

### Question 24

Le chemin $a,d,e,f$ coûte $4+1+1=6$, alors que le programme retourne un chemin de coût 8. **Le choix glouton ne garantit donc pas la difficulté cumulée minimale.**

### III.2 — Deuxième idée : l’algorithme de Dijkstra

### Question 25

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

Le chemin est reconstruit à rebours en suivant les prédécesseurs jusqu’au sommet initial. L’inversion finale, déjà donnée, remet les sommets dans l’ordre du départ vers l’arrivée.

```python
while s != sInit:          # Ligne 8
    s = distance[s][1]     # Ligne 9
    chemin.append(s)       # Ligne 10
```

À la ligne 15, le dernier argument de `print` est **`distance[sFin][0]`**. Ici le chemin est `["a", "d", "e", "f"]` et son coût est 6.

### Question 27

Le test sur `aVisiter` sert à éviter des doublons. Une table de statuts par sommet peut distinguer « inconnu », « à visiter » et « traité ». Un seul accès à un dictionnaire permet de décider s’il faut ajouter le voisin, mettre à jour son étiquette ou passer au suivant. On peut conserver `aVisiter` pour la recherche du minimum et éviter d’y faire des recherches linéaires d’appartenance.

### Question 28

Les arêtes ont toutes un poids de 1. Les sommets d’une même couche sont traités dans l’ordre d’insertion, car `cherche_min` ne remplace son choix qu’en présence d’une distance strictement plus petite.

- Depuis `a1` vers `j1` : **`a1, b1, c1, d1, e1, f1, g1, h1, i1, j1`**.
- Depuis `j1` vers `a1` : **`j1, g1, c1, a1`**.

### III.3 — Troisième idée : l’algorithme de Dijkstra bidirectionnel

### Question 29

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

### Question 30

**Non.** Au premier sommet atteint dans les deux sens, à l’étape 2, le raccord en $d$ donne un coût 8.

Le chemin $a,d,e,f$ de coût 6 existe pourtant. Un premier raccord ne fournit qu’une borne supérieure sur la distance optimale.

### Question 31

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

Le sommet $s$ ne peut avoir été traité en backward. Son étiquette arrière serait alors la distance exacte entre $s$ et $t$, au plus $D$.

Avec son étiquette forward nulle, le raccord en $s$ donnerait $\texttt{BFmin}\le D$, contradiction. De même, $t$ ne peut avoir été traité en forward.

Par Q32, $s$ est donc traité en forward, tandis que $t$ est traité en backward. Prenons le premier sommet du chemin qui n’a pas été traité en forward. Son prédécesseur $s_{i_0}$ a été traité en forward et, par Q32, ce sommet $s_{i_0+1}$ a été traité en backward.

### Question 34

Posons $u=s_{i_0}$ et $v=s_{i_0+1}$. L’étiquette forward de $u$ est exacte et ne dépasse pas le coût du préfixe jusqu’à $u$.

Le traitement de $u$ a relaxé l’arête $uv$, sauf si $v$ avait déjà une étiquette forward définitive. Dans les deux cas, l’étiquette forward finale de $v$ ne dépasse pas le coût du préfixe jusqu’à $v$.

L’étiquette backward de $v$ est exacte et ne dépasse pas le coût du suffixe à partir de $v$. Ainsi le raccord en $v$ donne une somme au plus $D$, ce qui contredit $\texttt{BFmin}>D$. Tout raccord fini représenté par `BFmin` est un trajet réalisable dans le graphe non orienté. **À l’arrêt, la valeur renvoyée est donc optimale.**
