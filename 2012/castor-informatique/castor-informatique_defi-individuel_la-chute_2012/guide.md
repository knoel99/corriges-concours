# Castor informatique — Défi individuel — La chute 2012 · Corrigé guidé

*Corrigé rédigé par IA, non officiel. Signalez toute erreur.*

## Présentation du sujet

Exercice autonome 2012-FR-10 de l’archive française de France-ioi. On doit prévoir la sortie d’un robot dans le deuxième labyrinthe, en appliquant exactement sa règle de déplacement. La direction horizontale fait partie des informations à mémoriser.

### Question unique

> [!INDICATION]
> Note une flèche pour chaque nouvelle plate-forme. Une chute peut traverser un espace vide avant que le robot rencontre la suivante.

#### Solution

Le robot va vers la droite sur la longue plate-forme supérieure. À sa première réception, il repart à gauche sur la plate-forme de droite. Il franchit son bord gauche, tombe sur la petite plate-forme centrale et repart à droite. Au bord droit de celle-ci, il descend sur la longue plate-forme juste au-dessous et repart à gauche. Il atteint ensuite la petite plate-forme centrale du dernier étage, qu’il quitte par la droite. La verticale issue de ce dernier bord aboutit dans **la case D**.

## Bilan

Pour simuler une trajectoire, noter ensemble la position et la direction. Le changement de direction se produit après la réception, une fois par chute.
