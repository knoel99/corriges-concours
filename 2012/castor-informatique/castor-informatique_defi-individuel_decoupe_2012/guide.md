# Castor informatique — Défi individuel — Découpe 2012 · Corrigé guidé

*Corrigé rédigé par IA, non officiel. Signalez toute erreur.*

## Présentation du sujet

Exercice autonome 2012-FR-09 de l’archive française de France-ioi. Un tracé en escalier est produit par quatre étapes de découpe. Pour distinguer les dessins proposés, on peut noter une hauteur par bande au lieu de redessiner toute la figure.

### Question unique

> [!INDICATION]
> Imagine deux fils pour une bande à la hauteur $h$. Quelle hauteur recevront-ils, dans l’ordre de gauche à droite ?

#### Solution

Chaque bande de hauteur $h$ donne, de gauche à droite, une bande de hauteur $h$ et une de hauteur $h+1$, les hauteurs étant mesurées en centimètres à partir de la position initiale. Après deux coupes on a $0,1,1,2$. Après la troisième, les huit hauteurs sont $0,1,1,2,1,2,2,3$. En remplaçant encore chaque valeur par le couple correspondant, on obtient

$$
0,1,1,2,1,2,2,3,1,2,2,3,2,3,3,4.
$$

**C’est le quatrième dessin (D).** En particulier, le dernier morceau est quatre centimètres plus haut que le premier, et le neuvième retombe à un centimètre.

## Bilan

Une transformation récursive se suit en gardant la même règle locale à toutes les étapes. Le nombre de morceaux double à chaque étape ; les différences de hauteur n’augmentent pas toutes ensemble.
