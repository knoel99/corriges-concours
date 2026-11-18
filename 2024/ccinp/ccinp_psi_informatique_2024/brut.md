# CCINP PSI — Informatique 2024 · Corrigé brut

*Corrigé rédigé par IA, non officiel. Signalez toute erreur.*

## Partie I — Présentation et règles

### Question 1

Les seules cases non vides du camp d’Alice sont les cases **2, 4 et 5**. Le camp de Bob contient déjà des graines. Après chacun de ces coups, il lui reste au moins une graine, comme le montrent les plateaux de Q2. Les trois coups sont donc autorisés.

### Question 2

On donne les cases d’Alice dans l’ordre 0 à 5 et celles de Bob dans l’ordre 6 à 11. Le document-réponse dessine la rangée de Bob dans l’ordre inverse.

- Case 2. Alice (0, 0, 0, 1, 17, 5), Bob (2, 1, 0, 1, 0, 1). Gain 0.
- Case 4. Alice (1, 1, 3, 1, 0, 7), Bob (4, 0, 0, 0, 1, 2). Gain 8.
- Case 5. Alice (0, 0, 2, 0, 16, 0), Bob (3, 2, 1, 2, 1, 1). Gain 0.

Depuis 2, la dernière graine tombe en 4, dans le camp d’Alice. Depuis 4, la dernière tombe en 9. On récolte 3 graines en 9, 2 en 8 et 3 en 7, puis on s’arrête en 6 où il y en a 4. Depuis 5, la dernière graine tombe en 10, qui contient une seule graine.

### Question 3

Alice joue la case 5 et sème une graine dans chacune des cases 6 à 10. Sa propre rangée est vide dans les deux cas. Les cases 6 à 10 de Bob contiennent alors deux graines chacune.

- **À gauche**, la case 11 est vide. La récolte des cases 10 à 6 enlèverait toutes les graines de Bob. La règle de la partie I annule donc la récolte. Le camp de Bob, en indices croissants, vaut (2, 2, 2, 2, 2, 0) et le gain est nul.
- **À droite**, la case 11 contient une graine qui reste à Bob. La récolte des cases 10 à 6 est autorisée et rapporte 10 graines. Le camp de Bob vaut (0, 0, 0, 0, 0, 1).

## Partie II — Programmation de la structure de jeu

### II.1 — Représentation du jeu

### Question 4

Le joueur 1 joue aux tours de compteur pair. On teste le reste de la division par deux.

```python
def tour_joueur1(jeu):
    return jeu['n'] % 2 == 0
```

### Question 5

Les tranches gardent l’ordre des cases dans chaque camp.

```python
def tourner_plateau(jeu):
    plateau = jeu['plateau']
    jeu['plateau'] = plateau[6:12] + plateau[0:6]
```

### Question 6

Il y a 48 graines au total. Une case contient donc au maximum 48 graines pour le dimensionnement de la représentation. Le codage de 0 à 48 inclus demande 49 valeurs possibles. Cinq bits ne donnent que 32 valeurs et six bits en donnent 64. Il faut **6 bits**.

### Question 7

Les listes de scores et de cases doivent être copiées. Les noms sont des chaînes et le compteur un entier.

```python
def copie(jeu):
    return {
        'joueur1': jeu['joueur1'],
        'joueur2': jeu['joueur2'],
        'score': jeu['score'].copy(),
        'n': jeu['n'],
        'plateau': jeu['plateau'].copy()
    }
```

### II.2 — Programmation d’un tour de jeu

### Question 8

On vide la case choisie au départ. La variable derniere est mise à jour avant chaque dépôt.

```python
def deplacer_graines(plateau, case):
    graines = plateau[case]
    plateau[case] = 0
    derniere = case
    while graines > 0:
        derniere = (derniere + 1) % 12
        if derniere == case:
            derniere = (derniere + 1) % 12
        plateau[derniere] = plateau[derniere] + 1
        graines = graines - 1
    return derniere
```

### Question 9

Le camp adverse occupe les indices 6 à 11.

```python
def case_ramassable(plateau, case):
    return 6 <= case < 12 and (plateau[case] == 2 or plateau[case] == 3)
```

### Question 10

La récursion s’arrête à la première case non ramassable, au plus tard à l’entrée du camp actif.

```python
def ramasser_graines(plateau, case):
    if not case_ramassable(plateau, case):
        return 0
    graines = plateau[case]
    plateau[case] = 0
    return graines + ramasser_graines(plateau, case - 1)
```

### Question 11

La partie II impose de déclarer non acceptable un coup dont la simulation de récolte vide le camp adverse. À la Q3, on appliquait la consigne d’annulation de la récolte de la partie I. Pour respecter le canevas de Q12, le test examine la condition 3 seule, même si la case est vide. Sans graines à distribuer, le plateau simulé reste dans son état initial. On vérifie dans tous les cas si le camp adverse contient encore des graines.

```python
def test_famine(plateau, case):
    simulation = plateau.copy()
    if simulation[case] > 0:
        derniere = deplacer_graines(simulation, case)
        ramasser_graines(simulation, derniere)
    for indice in range(6, 12):
        if simulation[indice] > 0:
            return True
    return False
```

### Question 12

La condition de la ligne 6 est la conjonction de l’indice dans le camp actif, du contenu non nul et de condition3.

```python
def test_case(plateau, case):
    condition3 = test_famine(plateau, case)
    test = (0 <= case < 6) and (plateau[case] > 0) and condition3
    return test
```

### Question 13

Le seul ajout est effectué dans la liste résultat. Le test de Q11 simule le coup sur sa propre copie.

```python
def cases_possibles(jeu):
    possibles = []
    plateau = jeu['plateau']
    for case in range(6):
        if test_case(plateau, case):
            possibles.append(case)
    return possibles
```

### Question 14

On compte les graines encore sur le plateau par une boucle, sans utiliser d’agrégat Python absent de l’annexe.

```python
def tour_suivant(jeu):
    score = jeu['score']
    if score[0] >= 25 or score[1] >= 25 or jeu['n'] >= 100:
        return False
    restantes = 0
    for graines in jeu['plateau']:
        restantes = restantes + graines
        if restantes > 3:
            return len(cases_possibles(jeu)) > 0
    return False
```

### Question 15

- Instruction 1 · « derniere = deplacer_graines(plateau, case) ».
- Instruction 2 · « graines_gagnees = ramasser_graines(plateau, derniere) ».
- Condition 1 · « tour_joueur1(jeu) ».
- Instruction 3 · « jeu['n'] = jeu['n'] + 1 ».

Le canevas tourne ensuite le plateau. Si la case est refusée, ni le score ni le compteur ni le plateau ne changent.

```python
def tour_jeu(jeu, case):
    plateau = jeu['plateau']
    if test_case(plateau, case):
        derniere = deplacer_graines(plateau, case)
        graines_gagnees = ramasser_graines(plateau, derniere)
        if tour_joueur1(jeu):
            jeu['score'][0] = jeu['score'][0] + graines_gagnees
        else:
            jeu['score'][1] = jeu['score'][1] + graines_gagnees
        jeu['n'] = jeu['n'] + 1
        tourner_plateau(jeu)
        return tour_suivant(jeu)
    print("La case choisie n’est pas valable")
    return True
```

### Question 16

On détermine à qui correspond le camp d’indices 0 à 5, puis on affecte les graines restantes aux réserves. On vide les cases pour matérialiser le ramassage.

```python
def gagnant(jeu):
    if tour_joueur1(jeu):
        actif, adverse = 0, 1
    else:
        actif, adverse = 1, 0
    plateau = jeu['plateau']
    score = jeu['score']
    for i in range(6):
        score[actif] = score[actif] + plateau[i]
        score[adverse] = score[adverse] + plateau[i + 6]
        plateau[i] = 0
        plateau[i + 6] = 0
    if score[0] > score[1]:
        return jeu['joueur1']
    if score[1] > score[0]:
        return jeu['joueur2']
    return 'égalité'
```

## Partie III — Intelligence artificielle et bibliothèque d’ouverture

### III.1 — Arbre des configurations

### Question 17

La case est valide par hypothèse. Le joueur qui récolte est identifié avant la mise à jour du tour.

```python
def gain(jeu, case):
    nouveau_jeu = copie(jeu)
    plateau = nouveau_jeu['plateau']
    derniere = deplacer_graines(plateau, case)
    graines = ramasser_graines(plateau, derniere)
    if tour_joueur1(nouveau_jeu):
        joueur = 0
    else:
        joueur = 1
    nouveau_jeu['score'][joueur] = nouveau_jeu['score'][joueur] + graines
    nouveau_jeu['n'] = nouveau_jeu['n'] + 1
    tourner_plateau(nouveau_jeu)
    return graines, nouveau_jeu
```

### III.2 — Algorithme MinMax

### Question 18

On conserve le plateau non inversé du document-réponse. Les rangées ci-dessous sont dans l’ordre croissant des indices. Les branches appariées au dessin sont, de gauche à droite après rotation de la page, les coups d’Alice 1, 5 et 2.

- Case 1. Alice (0, 0, 7, 1, 1, 3), Bob (1, 0, 0, 0, 0, 5). Gain d’Alice 4, valeur du nœud de Bob 4.
- Case 5. Alice (0, 7, 6, 0, 0, 0), Bob (1, 0, 1, 0, 0, 5). Gain d’Alice 2, valeur du nœud de Bob 0.
- Case 2. Alice (0, 7, 0, 1, 1, 3), Bob (1, 0, 0, 0, 0, 5). Gain d’Alice 4, valeur du nœud de Bob 4.

La liste donne les feuilles à inscrire. Les deux premières lignes restituent la branche déjà remplie. La valeur remontée de chaque feuille est 0 avec la profondeur imposée.

- Alice joue 1, Bob joue 11. Alice (1, 1, 8, 0, 0, 3), Bob (1, 0, 0, 0, 0, 0). Gain de Bob 4.
- Alice joue 1, Bob joue 6. Alice (0, 0, 7, 1, 1, 3), Bob (0, 1, 0, 0, 0, 5). Gain de Bob 0.
- Alice joue 5, Bob joue 11. Alice (1, 8, 7, 1, 1, 0), Bob (1, 0, 1, 0, 0, 0). Gain de Bob 0.
- Alice joue 5, Bob joue 8. Alice (0, 7, 6, 0, 0, 0), Bob (1, 0, 0, 1, 0, 5). Gain de Bob 0.
- Alice joue 5, Bob joue 6. Alice (0, 7, 6, 0, 0, 0), Bob (0, 1, 1, 0, 0, 5). Gain de Bob 0.
- Alice joue 2, Bob joue 11. Alice (1, 8, 1, 0, 0, 3), Bob (1, 0, 0, 0, 0, 0). Gain de Bob 4.
- Alice joue 2, Bob joue 6. Alice (0, 7, 0, 1, 1, 3), Bob (0, 1, 0, 0, 0, 5). Gain de Bob 0.

Pour le coup 5, Alice prend deux graines en case 7 et s’arrête à la case 6, qui n’en contient qu’une. Bob ne récolte sur aucun des trois coups suivants. Pour le coup 2, Bob peut jouer en 11 pour récolter deux graines en 4 et deux en 3. Ainsi les valeurs vues par Alice valent respectivement $4-4=0$, $2-0=2$ et $4-4=0$. **Alice doit jouer la case 5.**

### Question 19

La condition 1 de la fonction fournie est « not tour_suivant(jeu) » et la condition 2 est « profondeur >= profondeur_max ». L’instruction 1 est « g, nouveau_jeu = gain(jeu, case) ». L’instruction 2 est « p = NegaAwale(nouveau_jeu, profondeur_max, profondeur + 1) ». On ajoute ensuite la différence g − p.

La fonction gagnant de Q16 transfère les graines. Dans une version complète, un seul appel à cette fonction sur une copie suffit pour évaluer une feuille sans modifier l’état d’entrée. La règle utilisée est bien celle de la formule de remontée à la fin de la page 12. Plus haut sur cette page, l’identité entre minimum et maximum des opposés a omis le signe moins devant le maximum.

```python
def NegaAwale(jeu, profondeur_max, profondeur):
    if not tour_suivant(jeu):
        vainqueur = gagnant(copie(jeu))
        if tour_joueur1(jeu):
            actif = jeu['joueur1']
            adverse = jeu['joueur2']
        else:
            actif = jeu['joueur2']
            adverse = jeu['joueur1']
        if vainqueur == 'égalité':
            return 0
        if vainqueur == actif:
            return 500
        if vainqueur == adverse:
            return -500
    elif profondeur >= profondeur_max:
        return 0
    else:
        vals_jeu = []
        for case in cases_possibles(jeu):
            g, nouveau_jeu = gain(jeu, case)
            p = NegaAwale(nouveau_jeu, profondeur_max, profondeur + 1)
            vals_jeu.append([case, g - p])
        return max_vals(vals_jeu, profondeur)
```

Les noms sont compris comme les désignations distinctes des joueurs et « égalité » comme la valeur réservée de match nul, conformément au canevas.

### Question 20

Le code ne rencontre une liste vide qu’en dehors du cas d’appel de Q19. Une position sans coup a déjà été traitée comme terminale. La comparaison stricte garde le premier maximum.

```python
def max_vals(vals_jeu, profondeur):
    meilleure_case, meilleure_valeur = vals_jeu[0]
    for i in range(1, len(vals_jeu)):
        case, valeur = vals_jeu[i]
        if valeur > meilleure_valeur:
            meilleure_case, meilleure_valeur = case, valeur
    if profondeur == 0:
        return meilleure_case
    return meilleure_valeur
```

### Question 21

On remplace **uniquement la ligne 6**. L’appel de profondeur initiale zéro renvoie l’indice choisi. Les deux joueurs utilisent cette même ligne, puisque le plateau est réorienté après chaque coup.

```python
case_choisie = NegaAwale(jeu, 6, 0)
```

### III.3 — Bibliothèque d’ouverture

### Question 22

La borne est stricte.

```sql
SELECT id_Joueur
FROM Joueur
WHERE niveau > 1900;
```

### Question 23

Le code 1 désigne une victoire du premier joueur et la lettre a est l’indice 0. Le pourcentage est défini s’il existe au moins une partie commençant ainsi.

```sql
SELECT 100.0 * (
    SELECT COUNT(*)
    FROM Partie
    WHERE jeu LIKE 'a%' AND resultat = 1
) / COUNT(*) AS pourcentage
FROM Partie
WHERE jeu LIKE 'a%'
HAVING COUNT(*) > 0;
```

### Question 24

Le second critère permet de choisir exactement trois lignes même en cas d’égalité de niveau.

```sql
SELECT nom, prenom
FROM Joueur
ORDER BY niveau DESC, id_Joueur
LIMIT 3;
```

### Question 25

On regroupe par identifiant pour distinguer les homonymes. La condition sur chaque partie est dans WHERE, le seuil sur le total dans HAVING.

```sql
SELECT j.nom, j.prenom, COUNT(*) AS victoires
FROM Joueur AS j
JOIN Partie AS p ON p.id_joueur1 = j.id_Joueur
WHERE p.resultat = 1
GROUP BY j.id_Joueur, j.nom, j.prenom
HAVING COUNT(*) > 100
ORDER BY victoires DESC;
```
