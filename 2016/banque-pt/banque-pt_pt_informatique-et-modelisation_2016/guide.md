# Banque PT PT — Informatique et modélisation 2016 · Corrigé guidé

*Corrigé rédigé par IA, non officiel. Signalez toute erreur.*

**Rédaction** · modèle exact non renseigné (famille Claude) · effort non renseigné · vitesse non renseignée

## Présentation du sujet

Épreuve de quatre heures, sans calculatrice, consacrée à un tensiomètre électronique : un capteur à membrane et jauges de déformation convertit la pression du brassard en tension, puis une carte numérise, filtre et exploite le signal. Le sujet compte 37 questions, numérotées de 1 à 37 ; sa partie I est une présentation sans question.

- **Partie II, modélisation (questions 1 à 17, 1 h 30 conseillée).** Résistance des matériaux sur une poutre encastrée (questions 1 à 5), facteur de jauge par différentielle logarithmique (questions 6 à 11), pont de Wheatstone et sensibilité du capteur (questions 12 à 17).
- **Partie III, informatique (questions 18 à 28).** Choix du convertisseur et du type de stockage (18 et 19), filtre du second ordre intégré par le schéma de Newmark (20 à 26), recherche des pressions systolique et diastolique dans le signal filtré (27 et 28).
- **Partie IV, informatique (questions 29 à 37, 2 h 30 conseillées pour les parties III et IV).** Clé primaire, requêtes SQL, tracé d'un graphique, minimum, maximum, moyenne, médiane par tri et complexités.

Les questions 6 à 10, 12, 18, 19, 21, 23, 29 à 31 et 33 sont proches du cours et rapportent vite des points. Les plus sélectives sont les questions 1 à 3 (hyperstatisme, isolements, conditions aux limites), 13 à 16 (pont linéarisé) et 27 et 28 (extrema locaux). Les applications numériques sont attendues avec un seul chiffre significatif.

Un point de l'énoncé demande de l'attention : le modèle simplifié de la figure 3(b) garde la force $F$ entière sur la demi-membrane, alors que la symétrie n'en attribue que la moitié à chaque côté. Ce corrigé suit le modèle de l'énoncé et le signale à la question 1.

> [!JURY]
> Le rapport 2016 précise que le poids de chaque partie dans la note est proportionnel à sa durée conseillée. La plupart des candidats ont avancé de façon linéaire et la fin de la partie modélisation est rarement traitée ; en informatique, ils ont profité de l'indépendance des sous-parties, et les questions sur les bases de données ont été mieux traitées cette année. Le jury apprécie les programmes dont l'indentation est marquée par des barres verticales et juge illisibles les traits horizontaux ou les flèches. Il demande de soigner explications et commentaires : quand la question laisse de la liberté, une phrase avant le programme ou quelques commentaires bien placés sont préférables.

Documents officiels : [sujet](https://www.banquept.fr/documents/2016/info_mod_2016_pt.pdf) et [rapport du jury](https://www.banquept.fr/documents/ecrit/rapport/2016/rapport_info_model_ecrit_2016.pdf).

## Partie II — Étude du capteur de pression

**II.1 Modélisation de la déformation de la membrane (questions 1 à 5).**

Le problème est plan. Les torseurs sont écrits dans la base $(\vec x, \vec y, \vec z)$ ; le torseur de cohésion en $G$, de composantes $T_X$, $T_Y$, $M_Z$, est l'action de la partie droite sur la partie gauche.

### Question 1 — Équivalence des deux modèles et hyperstatisme

> [!INDICATION]
> Cherchez ce que la géométrie, les liaisons et le chargement du modèle complet ont en commun, puis ce que cela impose à la section située en $B$.

> [!INDICATION]
> Problème plan : 3 équations de statique par solide isolé. Comptez les inconnues de chaque liaison : 3 pour un encastrement, 2 pour la liaison en $B$ qui laisse libre la translation suivant $\vec y$.

#### Solution

**Équivalence.** Dans le modèle complet, la géométrie, les liaisons (deux encastrements en $A$ et $C$) et le chargement (force portée par $\vec y$ au milieu $B$) sont symétriques par rapport au plan $(B, \vec y, \vec z)$. La déformée l'est donc aussi : $u_y(2L - x) = u_y(x)$. On en tire, pour la section médiane :

- la pente est nulle, $\theta(L) = 0$ : la rotation autour de $(B, \vec z)$ est bloquée ;
- le point $B$ ne se déplace pas suivant $\vec x$ ;
- le déplacement suivant $\vec y$ reste libre (c'est la flèche).

Ce sont exactement les mobilités de la liaison placée en $B$ sur la figure 3(b) : une glissière de direction $\vec y$. Il suffit donc d'étudier la moitié $[AB]$ de la poutre munie de cette liaison ; l'autre moitié s'en déduit par symétrie.

**Degré d'hyperstatisme.** Le modèle étant plan, l'isolement de la poutre fournit 3 équations de statique et la poutre n'a aucune mobilité.

- Modèle (a) : deux encastrements, soit $3 + 3 = 6$ inconnues de liaison, d'où $h_a = 6 - 3 = 3$.
- Modèle (b) : un encastrement (3 inconnues $X_A$, $Y_A$, $M_A$) et une glissière (2 inconnues $X_B$, $M_B$), d'où $h_b = 5 - 3 = 2$.

$$\boxed{h_a = 3 \qquad h_b = 2}$$

**Intérêt.** Le modèle simplifié a une inconnue hyperstatique de moins et un seul tronçon à étudier : le moment fléchissant y a une seule expression sur $[0, L]$, sans raccordement au point d'application de la force. La symétrie remplace les équations supplémentaires par la condition $\theta(L) = 0$.

**Remarque sur la charge.** Par symétrie, chaque moitié de la membrane ne reprend que $F/2$. La figure 3(b) conserve pourtant la force $\vec F = -F\,\vec y$ en $B$ et la question 2 demande l'effort tranchant en fonction de $F$ : on suit le modèle de l'énoncé, chargé par $F$. Avec la charge $F/2$, tous les déplacements, déformations et tensions qui suivent seraient divisés par deux.

> [!JURY]
> Le rapport 2016 signale que cette question a été très mal traitée : très peu de copies évoquent la symétrie du problème et les calculs de degré d'hyperstatisme sont très souvent faux.

> [!PIEGE]
> Compter 6 équations de statique comme en trois dimensions fausse le résultat : dans un modèle plan, il n'y en a que 3 par solide.

### Question 2 — Moment fléchissant et effort tranchant

> [!INDICATION]
> Faites le bilan des actions extérieures au tronçon $[0, x]$ : la liaison en $A$ et la partie droite. Écrivez que leur somme est nulle, en résultante suivant $\vec y$ et en moment au point $G$.

> [!INDICATION]
> Pour l'effort tranchant, isolez le tronçon $[x, L]$ : la liaison en $B$ ne transmet rien suivant $\vec y$.

#### Solution

**Premier isolement : tronçon $[0, x]$.** Il est soumis à deux actions mécaniques :

- la liaison en $A$, de résultante $X_A\,\vec x + Y_A\,\vec y$ et de moment $M_A\,\vec z$ en $A$ ;
- la partie droite, par le torseur de cohésion : résultante $T_X\,\vec x + T_Y\,\vec y$ et moment $M_Z\,\vec z$ en $G$.

Le principe fondamental de la statique s'écrit comme la nullité de la somme de ces actions. En projection sur $\vec y$ :

$$Y_A + T_Y = 0 .$$

Pour l'équation de moment en $G$ suivant $\vec z$, on transporte l'action de $A$ : $\overrightarrow{GA} \wedge (X_A\,\vec x + Y_A\,\vec y) = -x\,\vec x \wedge Y_A\,\vec y = -x\,Y_A\,\vec z$. D'où

$$M_A - x\,Y_A + M_Z = 0 .$$

En éliminant $Y_A = -T_Y$ :

$$\boxed{M_Z = -M_A - x\,T_Y}$$

**Second isolement : tronçon $[x, L]$.** Il est soumis à l'action de la partie gauche (opposée du torseur de cohésion), à la force $-F\,\vec y$ en $B$ et à la liaison en $B$, qui ne transmet aucun effort suivant $\vec y$ (seulement $X_B$ et $M_B$). La résultante en projection sur $\vec y$ donne

$$-T_Y - F = 0 ,$$

$$\boxed{T_Y = -F}$$

On retrouve $Y_A = F$ : l'encastrement en $A$ reprend toute la charge du modèle simplifié.

**Conclusion.**

$$\boxed{M_Z(x) = F\,x - M_A}$$

Le moment d'encastrement $M_A$ reste inconnu à ce stade : c'est l'inconnue hyperstatique utile, la statique seule ne la donne pas. Vérification : $\dfrac{\mathrm{d}M_Z}{\mathrm{d}x} = F = -T_Y$, relation attendue entre moment fléchissant et effort tranchant avec cette convention.

> [!JURY]
> D'après le rapport 2016, les candidats se trompent souvent dans l'expression des actions mécaniques et dans leur bilan, et l'application du principe fondamental de la statique les amène souvent à écrire l'égalité de deux actions au lieu de la nullité de leur somme.

> [!METHODE]
> Pour chaque isolement : frontière, liste des actions extérieures, torseurs réduits au même point, puis somme nulle. Le transport du moment se fait avec $\vec M_G = \vec M_A + \overrightarrow{GA} \wedge \vec R$.

### Question 3 — Déformée de la membrane

> [!INDICATION]
> Intégrez deux fois $EI\,u_y'' = M_Z$. Deux constantes apparaissent : quelles conditions l'encastrement en $A$ impose-t-il au déplacement et à la rotation ?

> [!INDICATION]
> L'inconnue $M_A$ s'élimine avec la condition que la liaison en $B$ impose à la rotation de la section.

#### Solution

La relation de comportement donne

$$EI\,\frac{\mathrm{d}^2 u_y}{\mathrm{d}x^2} = F\,x - M_A .$$

Première intégration :

$$EI\,\frac{\mathrm{d} u_y}{\mathrm{d}x} = \frac{F\,x^2}{2} - M_A\,x + C_1 .$$

L'encastrement en $A$ bloque la rotation : $\theta(0) = 0$, donc $C_1 = 0$. Seconde intégration :

$$EI\,u_y = \frac{F\,x^3}{6} - \frac{M_A\,x^2}{2} + C_2 .$$

L'encastrement en $A$ bloque aussi le déplacement : $u_y(0) = 0$, donc $C_2 = 0$. Les deux constantes sont nulles à cause des conditions aux limites en $A$, et pour cette seule raison.

Il reste à déterminer $M_A$ par la condition en $B$, où la liaison bloque la rotation : $\theta(L) = 0$, soit

$$\frac{F\,L^2}{2} - M_A\,L = 0 ,$$

$$M_A = \frac{F\,L}{2} .$$

On obtient bien $u_y(x) = A_1\,x^3 + A_2\,x^2$ avec

$$\boxed{A_1 = \frac{F}{6\,EI} \qquad A_2 = -\frac{F\,L}{4\,EI}}$$

soit $u_y(x) = \dfrac{F\,x^2\,(2x - 3L)}{12\,EI}$. Vérifications : $u_y \le 0$ sur $[0, L]$ (la membrane descend sous la force), la flèche en $B$ vaut $u_y(L) = -\dfrac{F\,L^3}{12\,EI}$, et $F L^3/(EI)$ est bien une longueur.

> [!JURY]
> Le rapport 2016 note que peu de candidats justifient la nullité des constantes d'intégration, et qu'ils semblent les annuler par habitude, comme pour une équation différentielle temporelle.

> [!PIEGE]
> La condition en $B$ porte sur la pente, pas sur le déplacement : $u_y(L)$ est libre, c'est la flèche cherchée.

### Question 4 — Déformation de la peau supérieure

> [!INDICATION]
> Dérivez deux fois $u_y(x) = A_1 x^3 + A_2 x^2$ et reportez dans la relation donnée avec $y = e/2$.

#### Solution

En $y = e/2$ :

$$\varepsilon(x) = -\frac{e}{2}\,\frac{\mathrm{d}^2 u_y}{\mathrm{d}x^2} = -\frac{e}{2}\,(6A_1\,x + 2A_2) = -\frac{e}{2\,EI}\left(F\,x - \frac{F\,L}{2}\right).$$

Donc $\varepsilon = A_3 + A_4\,x$ avec

$$\boxed{A_3 = \frac{e\,F\,L}{4\,EI} \qquad A_4 = -\frac{e\,F}{2\,EI}}$$

soit $\varepsilon(x) = \dfrac{e\,F}{2\,EI}\left(\dfrac{L}{2} - x\right)$. La peau supérieure est tendue près de l'encastrement ($\varepsilon > 0$ pour $x < L/2$) et comprimée près de la force ($\varepsilon < 0$ pour $x > L/2$) ; la déformation est sans dimension, comme il se doit ($e F L/(EI)$ : $\mathrm{m \cdot N \cdot m / (Pa \cdot m^4)}$).

> [!JURY]
> Selon le rapport 2016, les questions 4 et 5 n'ont pas posé de difficulté aux très rares candidats qui avaient réussi les précédentes.

### Question 5 — Position des jauges

> [!INDICATION]
> Où une fonction affine atteint-elle ses valeurs extrêmes sur un segment ? Demandez-vous aussi où la déformation s'annule.

> [!INDICATION]
> Pour les jauges 3 et 4, situées sur l'autre moitié, utilisez la symétrie de la question 1 plutôt qu'un nouveau calcul.

#### Solution

**Position idéale.** La jauge doit être placée là où $|\varepsilon|$ est le plus grand. Comme $\varepsilon$ est affine en $x$, ses extrêmes sont aux bornes : $\varepsilon(0) = +\dfrac{eFL}{4EI}$ à l'encastrement et $\varepsilon(L) = -\dfrac{eFL}{4EI}$ sous la force, et par symétrie en $x = 2L$. Les positions idéales sont donc les encastrements et le milieu de la membrane. À l'inverse, $x = L/2$ est la pire position : la déformation y est nulle. En pratique une jauge a une longueur non nulle et ne peut être collée ni dans l'encastrement ni sous la tige du piston, d'où les positions retenues.

**Positions réelles.** Sur la moitié gauche :

$$\varepsilon\!\left(\frac{L}{4}\right) = \frac{e\,F}{2\,EI}\cdot\frac{L}{4} = \frac{e\,F\,L}{8\,EI} \qquad\qquad \varepsilon\!\left(\frac{3L}{4}\right) = -\frac{e\,F\,L}{8\,EI} .$$

Ce sont les jauges 1 et 2. Par symétrie par rapport au milieu, la jauge 3 (en $2L - 3L/4$) subit la même déformation que la jauge 2 et la jauge 4 (en $2L - L/4$) la même que la jauge 1 :

$$\boxed{\varepsilon_1 = -\varepsilon_2 = -\varepsilon_3 = \varepsilon_4 = k\,F \quad\text{avec}\quad k = \frac{e\,L}{8\,EI}}$$

Chaque jauge mesure la moitié de la déformation maximale. Deux jauges sont tendues et deux comprimées, avec la même valeur absolue : c'est ce qui rendra le pont de la partie II.3 quatre fois plus sensible qu'avec une seule jauge.

![Figure 1 — Déformation de la peau supérieure le long de la membrane et position des quatre jauges](figures/q5-deformation-jauges.svg)

> [!PIEGE]
> La formule $\varepsilon = A_3 + A_4 x$ n'est valable que pour $x \in [0, L]$ : l'appliquer en $x = 5L/4$ ou $7L/4$ donne des valeurs fausses.

**II.2 Choix des jauges de déformation (questions 6 à 11).**

### Question 6 — Variation relative de résistance

> [!INDICATION]
> La résistance est un produit de puissances : différentiez son logarithme.

#### Solution

On prend le logarithme de $R = \rho\,\ell / s$ :

$$\ln R = \ln \rho + \ln \ell - \ln s .$$

En différentiant, pour de petites variations :

$$\boxed{\frac{\delta R}{R} = \frac{\delta \rho}{\rho} + \frac{\delta \ell}{\ell} - \frac{\delta s}{s}}$$

> [!JURY]
> Le rapport 2016 indique que cette sous-partie a été très mal traitée faute de comprendre ce qui était attendu, à savoir une différentielle logarithmique (ou des incertitudes-types, conformément au programme de physique) ; les candidats qui l'ont compris l'ont très bien réussie.

> [!METHODE]
> Différentielle logarithmique : si $R = \rho\,\ell^{1}\,s^{-1}$, alors $\delta R / R$ est la somme des variations relatives, chacune multipliée par son exposant. Les signes sont conservés : ce n'est pas un calcul d'incertitude.

### Question 7 — Rôle du coefficient de Poisson

> [!INDICATION]
> Exprimez $\delta s / s$ à partir de $s = a\,b$, toujours par différentielle logarithmique.

#### Solution

La section vaut $s = a\,b$, donc

$$\frac{\delta s}{s} = \frac{\delta a}{a} + \frac{\delta b}{b} = -2\nu\,\frac{\delta \ell}{\ell} .$$

En reportant :

$$\boxed{\frac{\delta R}{R} = (1 + 2\nu)\,\frac{\delta \ell}{\ell} + \frac{\delta \rho}{\rho}}$$

Le terme $(1 + 2\nu)\,\delta\ell/\ell$ est purement géométrique : la jauge s'allonge et sa section diminue.

### Question 8 — Facteur de jauge d'un métal

> [!INDICATION]
> Le volume est $V = \ell\,s$ : sa variation relative s'exprime avec $\delta\ell/\ell$ seul grâce à la question 7.

#### Solution

Le volume vaut $V = \ell\,s$, donc

$$\frac{\delta V}{V} = \frac{\delta \ell}{\ell} + \frac{\delta s}{s} = (1 - 2\nu)\,\frac{\delta \ell}{\ell} .$$

La loi de Bridgman donne alors $\dfrac{\delta\rho}{\rho} = c\,(1 - 2\nu)\,\dfrac{\delta\ell}{\ell}$, et

$$\frac{\delta R}{R} = \bigl[\,1 + 2\nu + c\,(1 - 2\nu)\,\bigr]\,\frac{\delta \ell}{\ell} .$$

C'est la forme demandée, avec

$$\boxed{K = 1 + 2\nu + c\,(1 - 2\nu)}$$

### Question 9 — Facteur de jauge d'un semi-conducteur

> [!INDICATION]
> Éliminez la contrainte $\sigma$ entre les deux lois données pour écrire $\delta\rho/\rho$ en fonction de $\delta\ell/\ell$.

#### Solution

Ici $\dfrac{\delta\rho}{\rho} = \Pi\,\sigma$ et $\sigma = E\,\dfrac{\delta\ell}{\ell}$, donc $\dfrac{\delta\rho}{\rho} = \Pi\,E\,\dfrac{\delta\ell}{\ell}$. En reportant dans le résultat de la question 7 :

$$\boxed{K = 1 + 2\nu + \Pi\,E}$$

Le produit $\Pi E$ est sans dimension ($\mathrm{Pa^{-1} \cdot Pa}$).

### Question 10 — Valeurs numériques et commentaire

> [!INDICATION]
> Calculez séparément la part géométrique $1 + 2\nu$ et la part due à la résistivité, puis comparez-les dans chaque matériau.

#### Solution

Pour le cuivre :

$$K_{\mathrm{Cu}} = 1 + 2 \times 0{,}3 + 1 \times (1 - 2 \times 0{,}3) = 1 + 0{,}6 + 0{,}4 = \mathbf{2} .$$

Pour le silicium, $\Pi E = 10^{-9} \times 10^{11} = 100$ :

$$K_{\mathrm{Si}} = 1 + 2 \times 0{,}4 + 100 = 101{,}8 \approx \mathbf{1 \times 10^{2}} .$$

**Commentaire.** Le facteur de jauge du silicium est environ cinquante fois plus grand que celui du cuivre : à déformation égale, la variation de résistance, donc le signal, est cinquante fois plus forte. Dans le métal, l'effet est surtout géométrique (allongement et striction, $1 + 2\nu = 1{,}6$ sur 2). Dans le semi-conducteur, il est dominé par la piézorésistivité ($\Pi E = 100$ contre $1{,}8$ pour la géométrie). C'est ce qui justifie des jauges en silicium pour mesurer les très petites déformations de la membrane.

### Question 11 — Source d'erreur

> [!INDICATION]
> Quelle grandeur physique, autre que la déformation, fait varier la résistivité d'un matériau ?

#### Solution

**La température.** La résistivité dépend de la température, très fortement pour un semi-conducteur, et la jauge comme son support se dilatent : une variation de température change $R$ sans qu'aucun effort ne soit appliqué, ce que la mesure interprète comme une contrainte. L'échauffement de la jauge par effet Joule, dû au courant de mesure, agit dans le même sens.

Le montage en pont de la partie suivante limite ce défaut : une variation de température commune aux quatre jauges modifie les quatre résistances de la même quantité et laisse $V_p$ inchangée au premier ordre.

**II.3 Circuit de conditionnement : pont de Wheatstone (questions 12 à 17).**

Lecture de la figure 6 : la branche supérieure relie $C$ à $D$ par $R_a$ puis $R_b$, avec le point $A$ entre les deux ; la branche inférieure relie $C$ à $D$ par $R_c$ puis $R_d$, avec le point $B$ entre les deux. La flèche de $V_p$ va de $B$ vers $A$, donc $V_p = V_A - V_B$ ; la source impose $V_C - V_D = V_{alim}$ et $D$ est à la masse.

### Question 12 — Tension de déséquilibre du pont

> [!INDICATION]
> Aucun courant ne sort par $A$ ni par $B$ : chaque branche du pont est un diviseur de tension alimenté par $V_{alim}$.

> [!INDICATION]
> Écrivez les potentiels de $A$ et de $B$ par rapport à $D$, puis faites la différence dans le sens de la flèche de $V_p$.

#### Solution

L'amplificateur branché entre $A$ et $B$ a une résistance d'entrée très grande : il ne prélève aucun courant. $R_a$ et $R_b$ sont donc en série, de même que $R_c$ et $R_d$, et les deux branches sont soumises à $V_{alim}$. Deux diviseurs de tension, avec $V_D = 0$ :

$$V_A = \frac{R_b}{R_a + R_b}\,V_{alim} \qquad\qquad V_B = \frac{R_d}{R_c + R_d}\,V_{alim} .$$

D'où

$$\boxed{V_p = V_A - V_B = \left(\frac{R_b}{R_a + R_b} - \frac{R_d}{R_c + R_d}\right) V_{alim} = \frac{R_b\,R_c - R_a\,R_d}{(R_a + R_b)(R_c + R_d)}\,V_{alim}}$$

Le pont est équilibré ($V_p = 0$) quand $R_b\,R_c = R_a\,R_d$.

> [!JURY]
> Le rapport 2016 relève que cette dernière sous-partie a été assez peu traitée, hormis la question 12, et qu'assez peu de candidats parviennent à appliquer les lois de l'électrocinétique pour obtenir $V_p$.

### Question 13 — Linéarisation autour de l'équilibre

> [!INDICATION]
> Remplacez chaque $R_i$ par $R_0 + \Delta R_i$ et développez chaque rapport au premier ordre en $\Delta R_i / R_0$.

#### Solution

On pose $R_i = R_0 + \Delta R_i$ avec $|\Delta R_i| \ll R_0$. Au premier ordre :

$$\frac{R_b}{R_a + R_b} = \frac{R_0 + \Delta R_b}{2R_0 + \Delta R_a + \Delta R_b} \approx \frac{1}{2}\left(1 + \frac{\Delta R_b}{R_0}\right)\left(1 - \frac{\Delta R_a + \Delta R_b}{2R_0}\right) \approx \frac{1}{2} + \frac{\Delta R_b - \Delta R_a}{4R_0} .$$

De même $\dfrac{R_d}{R_c + R_d} \approx \dfrac{1}{2} + \dfrac{\Delta R_d - \Delta R_c}{4R_0}$. Par différence :

$$\boxed{\Delta V_p = \frac{V_{alim}}{4\,R_0}\,\bigl(\Delta R_b + \Delta R_c - \Delta R_a - \Delta R_d\bigr)}$$

Les résistances de deux bras opposés ($R_b$ et $R_c$) agissent dans le même sens, celles de deux bras adjacents en sens contraires.

> [!PIEGE]
> Une variation identique des quatre résistances donne $\Delta V_p = 0$ : ne pas en conclure que le pont est insensible, mais que les jauges doivent être placées pour que les quatre termes s'ajoutent.

### Question 14 — Place des jauges dans le pont

> [!INDICATION]
> Dans le résultat de la question 13, repérez les termes précédés d'un signe plus et ceux précédés d'un signe moins, puis le signe de la déformation de chaque jauge.

#### Solution

D'après la question 8 ou 9, $\dfrac{\Delta R}{R_0} = K\,\varepsilon$ : les jauges 1 et 4 ($\varepsilon = +kF$) voient leur résistance augmenter de $K\varepsilon_1 R_0$, les jauges 2 et 3 ($\varepsilon = -kF$) la voient diminuer d'autant.

Pour que les quatre contributions s'ajoutent dans $\Delta V_p$, il faut que $\Delta R_b$ et $\Delta R_c$ aient le même signe, opposé à celui de $\Delta R_a$ et $\Delta R_d$. La jauge 1 étant $R_b$ :

$$\boxed{R_c = \text{jauge 4} \qquad R_a \text{ et } R_d = \text{jauges 2 et 3 (dans un ordre indifférent)}}$$

Les deux jauges tendues occupent deux bras opposés du pont, les deux jauges comprimées les deux autres.

![Figure 2 — Pont de Wheatstone : place des quatre jauges et sens des tensions](figures/q14-pont-wheatstone.svg)

### Question 15 — Tension en fonction de la déformation

> [!INDICATION]
> Reportez $\Delta R_i = \pm K \varepsilon_1 R_0$ dans la relation de la question 13.

#### Solution

Avec ce câblage, $\Delta R_b = \Delta R_c = K\,\varepsilon_1\,R_0$ et $\Delta R_a = \Delta R_d = -K\,\varepsilon_1\,R_0$, donc

$$V_p = \frac{V_{alim}}{4\,R_0} \times 4\,K\,\varepsilon_1\,R_0 ,$$

$$\boxed{V_p = K\,\varepsilon_1\,V_{alim}}$$

Le pont complet est quatre fois plus sensible qu'un pont à une seule jauge active.

### Question 16 — Sensibilité du capteur

> [!INDICATION]
> Enchaînez les trois relations : $V_p = K \varepsilon_1 V_{alim}$, $\varepsilon_1 = kF$ et $F = P S_m$.

> [!INDICATION]
> Pour l'application numérique, convertissez tout en unités SI, en particulier $I$ : $1\ \mathrm{mm^4} = 10^{-12}\ \mathrm{m^4}$.

#### Solution

On a $\varepsilon_1 = k\,F$ avec $k = \dfrac{e\,L}{8\,EI}$ (question 5) et $F = P\,S_m$. Donc

$$\boxed{V_p = \frac{K\,V_{alim}\,e\,L\,S_m}{8\,EI}\;P}$$

La sensibilité du capteur est le rapport de la grandeur de sortie à la grandeur d'entrée, ici constant puisque la loi est linéaire :

$$\boxed{s = \frac{V_p}{P} = \frac{K\,V_{alim}\,e\,L\,S_m}{8\,EI}}$$

Application numérique, en unités SI, avec $K \approx 100$, $e = 10^{-4}\ \mathrm{m}$, $L = 2 \times 10^{-3}\ \mathrm{m}$, $S_m = 4 \times 10^{-6}\ \mathrm{m^2}$ et $I = 2 \times 10^{-4}\ \mathrm{mm^4} = 2 \times 10^{-16}\ \mathrm{m^4}$ :

$$s = \frac{100 \times 16 \times 10^{-4} \times 2 \times 10^{-3} \times 4 \times 10^{-6}}{8 \times 10^{11} \times 2 \times 10^{-16}} = \frac{1{,}28 \times 10^{-9}}{1{,}6 \times 10^{-4}} = 8 \times 10^{-6}\ \mathrm{V \cdot Pa^{-1}} .$$

Soit $8\ \mathrm{\mu V}$ par pascal, ou environ $1\ \mathrm{mV}$ par millimètre de mercure ($1\ \mathrm{mmHg} \approx 133\ \mathrm{Pa}$). Un écart d'un millimètre de mercure donne donc une tension de l'ordre du millivolt, facile à mesurer après amplification : l'objectif de précision annoncé est accessible.

> [!PIEGE]
> Le moment quadratique est donné en $\mathrm{mm^4}$ : oublier le facteur $10^{-12}$ fausse la sensibilité de douze ordres de grandeur.

### Question 17 — Tension pour 50 kPa

> [!INDICATION]
> Multipliez la sensibilité par la pression exprimée en pascals, puis vérifiez que la déformation correspondante reste petite.

#### Solution

$$V_p = s\,P = 8 \times 10^{-6} \times 5 \times 10^{4} ,$$

$$\boxed{V_p = 0{,}4\ \mathrm{V}}$$

Contrôle : la déformation des jauges vaut alors $\varepsilon_1 = V_p / (K\,V_{alim}) = 2{,}5 \times 10^{-4}$, valeur très inférieure à 1, compatible avec l'hypothèse des petites déformations ; et $V_p \ll V_{alim} = 16\ \mathrm{V}$, ce qui valide la linéarisation de la question 13. Avec la charge $F/2$ évoquée à la question 1, on trouverait $0{,}2\ \mathrm{V}$.

## Partie III — Traitement numérique des informations

Les programmes sont écrits en Python. Tout le code de cette partie et de la suivante a été exécuté et testé.

**III.1 Numérisation du signal (questions 18 et 19).**

### Question 18 — Résolution du convertisseur

> [!INDICATION]
> Convertissez l'étendue de mesure en millimètres de mercure, puis comptez combien d'intervalles de $0{,}02\ \mathrm{mmHg}$ elle contient.

> [!INDICATION]
> Comparez ce nombre à $2^{10}$, $2^{12}$ et $2^{16}$.

#### Solution

Étendue de mesure en millimètres de mercure :

$$1350\ \mathrm{hPa} \times \frac{750\ \mathrm{mmHg}}{1013\ \mathrm{hPa}} \approx 1000\ \mathrm{mmHg} .$$

Un convertisseur de $n$ bits découpe cette étendue (la plage $[0, 5\ \mathrm{V}]$) en $2^n$ niveaux ; son pas vaut $1000 / 2^n\ \mathrm{mmHg}$. Pour un pas d'au plus $0{,}02\ \mathrm{mmHg}$, il faut

$$2^n \ge \frac{1000}{0{,}02} = 50\,000 .$$

Or $2^{10} = 1024$, $2^{12} = 4096$ et $2^{16} = 65\,536$. Les pas correspondants sont environ $1\ \mathrm{mmHg}$, $0{,}24\ \mathrm{mmHg}$ et $0{,}015\ \mathrm{mmHg}$.

**Seul le convertisseur de 16 bits respecte le critère** ; celui de 12 bits suffirait pour l'affichage au millimètre de mercure, pas pour le traitement.

> [!JURY]
> Le rapport 2016 indique que cette question a été globalement bien traitée.

### Question 19 — Type de stockage et mémoire

> [!INDICATION]
> Quelle est la nature de la grandeur délivrée par un convertisseur analogique-numérique de $n$ bits, et dans quel intervalle se trouve-t-elle ?

#### Solution

Un convertisseur analogique-numérique de 16 bits délivre un **entier** compris entre $0$ et $2^{16} - 1 = 65\,535$. Le type adapté est donc l'**entier non signé codé sur 16 bits**, qui couvre exactement cet intervalle. Un entier relatif sur 16 bits s'arrête à $32\,767$ et ne convient pas ; les types de 32 ou 64 bits, entiers ou réels, conviendraient mais doubleraient ou quadrupleraient la mémoire sans rien apporter.

Nombre de valeurs : $60\ \mathrm{s} \times 1000\ \mathrm{Hz} = 60\,000$ échantillons, de 2 octets chacun :

$$\boxed{60\,000 \times 2 = 120\,000\ \text{octets} \approx 120\ \text{ko}}$$

> [!JURY]
> D'après le rapport 2016, peu de candidats savent qu'un convertisseur analogique-numérique fournit une valeur entière, ce qui les empêche de conclure correctement.

**III.2 Filtrage numérique du signal (questions 20 à 26).**

### Question 20 — Choix des paramètres du filtre

> [!INDICATION]
> Convertissez 190 pulsations par minute en hertz, puis en radians par seconde, et comparez à $\omega$.

> [!INDICATION]
> Pour $z$, pensez à la résonance d'un filtre du second ordre et à la rapidité de sa réponse indicielle.

#### Solution

L'équation est celle d'un filtre passe-bas du second ordre, de gain statique 1, de pulsation propre $\omega$ et de coefficient d'amortissement $z$.

- **Pulsation.** La fréquence cardiaque maximale est $190 / 60 \approx 3{,}2\ \mathrm{Hz}$, soit une pulsation $2\pi \times 3{,}2 \approx 20\ \mathrm{rad \cdot s^{-1}}$. En prenant $\omega = 20\ \mathrm{rad \cdot s^{-1}}$, on place la coupure juste au-dessus de la bande utile : les oscillations dues aux battements du cœur sont conservées et le bruit de mesure, de fréquence plus élevée, est atténué de 40 dB par décade.
- **Amortissement.** Avec $z = 0{,}7 \approx 1/\sqrt{2}$, la réponse en fréquence n'a pas de résonance (pas d'amplification artificielle autour de $\omega$, bande passante la plus plate possible) et la réponse temporelle est la plus rapide, avec un dépassement d'environ 5 % seulement.

> [!JURY]
> Le rapport 2016 note que la justification des paramètres du filtre est souvent restée partielle, bien que la majorité des candidats aient calculé la pulsation cardiaque en radians par seconde.

### Question 21 — Relation de récurrence

> [!INDICATION]
> Écrivez l'équation différentielle à l'instant $(i+1)T_e$, puis remplacez-y $\dot U_{f,i+1}$ et $U_{f,i+1}$ par les relations de Newmark.

> [!INDICATION]
> Regroupez à gauche tous les termes en $\ddot U_{f,i+1}$ : leur coefficient doit être $1/B_1$.

#### Solution

L'équation différentielle au pas $(i+1)\,T_e$ s'écrit

$$\frac{1}{\omega^2}\,\ddot U_{f,i+1} + \frac{2z}{\omega}\,\dot U_{f,i+1} + U_{f,i+1} = U_{e,i+1} .$$

On y remplace $\dot U_{f,i+1}$ et $U_{f,i+1}$ par les deux relations de Newmark, puis on regroupe les termes en $\ddot U_{f,i+1}$ dans le membre de gauche :

$$\left(\frac{1}{\omega^2} + \frac{2z\gamma}{\omega}\,T_e + \beta\,T_e^2\right)\ddot U_{f,i+1} = U_{e,i+1} - \left[\frac{2z}{\omega}(1-\gamma)\,T_e + T_e^2\left(\tfrac12 - \beta\right)\right]\ddot U_{f,i} - \left(\frac{2z}{\omega} + T_e\right)\dot U_{f,i} - U_{f,i} .$$

Le facteur de gauche est $1/B_1$. On obtient bien $\ddot U_{f,i+1} = B_1\,\bigl(U_{e,i+1} + B_2\,\ddot U_{f,i} + B_3\,\dot U_{f,i} + B_4\,U_{f,i}\bigr)$ avec

$$\boxed{B_2 = -\frac{2z}{\omega}(1-\gamma)\,T_e - T_e^2\left(\frac12 - \beta\right) \qquad B_3 = -\frac{2z}{\omega} - T_e \qquad B_4 = -1}$$

Les constantes dépendent aussi du pas $T_e$. Homogénéité : $B_2$ en $\mathrm{s^2}$ comme $1/\omega^2$, $B_3$ en $\mathrm{s}$, $B_4$ sans dimension, et $B_1$ en $\mathrm{s^{-2}}$ : le produit est bien une dérivée seconde.

> [!JURY]
> Le rapport 2016 indique que cette question n'a pas posé de problème, aux erreurs de calcul près.

### Question 22 — Stabilité du schéma

> [!INDICATION]
> Pour chaque courbe de la figure 7, regardez si l'écart à la valeur finale 1 croît, se maintient ou décroît au cours du temps.

#### Solution

Lecture de la figure 7 (réponse à un échelon unité) :

- pour $T_e = 0{,}2\ \mathrm{s}$, la sortie oscille avec une amplitude croissante (environ $2{,}1$ à $t = 1{,}2\ \mathrm{s}$, puis une valeur négative) : le schéma diverge ;
- pour $T_e = 0{,}175\ \mathrm{s}$, les oscillations gardent une amplitude à peu près constante (entre $0{,}55$ et $1{,}45$ environ) : c'est la limite de stabilité ;
- pour $T_e = 0{,}13\ \mathrm{s}$, les oscillations s'amortissent et la sortie tend vers 1 ;
- pour $T_e \le 0{,}05\ \mathrm{s}$, la sortie tend vers 1 sans oscillation parasite.

**Le schéma est conditionnellement stable : il est stable tant que le pas de temps reste inférieur à une valeur critique voisine de $0{,}175\ \mathrm{s}$** (soit $\omega\,T_e$ de l'ordre de $3{,}5$), et instable au-delà.

> [!JURY]
> D'après le rapport 2016, le jury attendait ici une analyse de la dépendance de la stabilité à la période d'échantillonnage.

### Question 23 — Ordre de convergence

> [!INDICATION]
> Par combien l'erreur est-elle divisée quand le pas de temps est divisé par 10 ?

#### Solution

Le tableau donne $\eta = 0{,}05$, $0{,}005$ et $0{,}0005$ pour $T_e = 0{,}01$, $0{,}001$ et $0{,}0001$ : chaque fois que le pas est divisé par 10, l'erreur est divisée par 10. L'erreur est proportionnelle au pas,

$$\eta \approx 5\,T_e ,$$

**le schéma converge donc à l'ordre 1 dans cette configuration** (une méthode d'ordre $p$ donnerait une erreur divisée par $10^p$).

Contrôle par simulation de la réponse indicielle du filtre avec la fonction de la question 25 : on retrouve des erreurs de $0{,}047$, $0{,}0046$ et $0{,}00046$ pour ces trois pas.

> [!JURY]
> Le rapport 2016 précise que le jury attendait une analyse de l'évolution de l'erreur en fonction de la période ; l'ordre de convergence n'étant pas explicitement au programme, une réponse décrivant une évolution linéaire était acceptée.

### Question 24 — Qualité du signal filtré

> [!INDICATION]
> Calculez le pas de temps imposé par la fréquence d'échantillonnage, puis comparez-le au pas critique (question 22) et lisez l'erreur correspondante (question 23).

#### Solution

Le pas d'intégration est imposé par l'acquisition : $T_e = 1/f_e = 10^{-3}\ \mathrm{s}$.

- **Stabilité.** Ce pas est environ 175 fois plus petit que le pas critique de la question 22 : le calcul est stable, avec une marge très large.
- **Précision.** D'après le tableau, l'erreur vaut $\eta = 0{,}005$ pour un échelon unité, soit $0{,}5\ \%$ de l'amplitude du signal ; sur la figure 7, la courbe $T_e = 0{,}001\ \mathrm{s}$ est lisse et se confond avec celle de $T_e = 0{,}01\ \mathrm{s}$.

**Le signal filtré est donc calculé de façon stable et précise** : l'intégration numérique ne dégrade pas la mesure, et il est inutile de chercher un schéma plus fin.

### Question 25 — Fonction newmark

> [!INDICATION]
> Trois suites sont nécessaires : le signal filtré, sa dérivée première et sa dérivée seconde. Dans quel ordre les valeurs au pas $i+1$ doivent-elles être calculées ?

> [!INDICATION]
> Commencez par $\ddot U_{f,i+1}$ (question 21), qui sert ensuite aux deux relations de Newmark.

#### Solution

On calcule, à chaque pas, la dérivée seconde par la relation de la question 21, puis la dérivée première et le signal par les deux relations de Newmark. Les trois grandeurs sont nulles au premier indice (conditions initiales nulles). Les constantes $B_1$ à $B_4$ sont des variables globales.

```python
def newmark(gamma, beta, omega, z, e, Te):
    """Renvoie la liste Uf du signal e filtré (conditions initiales nulles)."""
    N = len(e)
    Uf = [0.0] * N        # signal filtré
    Vf = [0.0] * N        # dérivée première
    Af = [0.0] * N        # dérivée seconde
    for i in range(N - 1):
        # accélération au pas i+1 (relation de la question 21)
        Af[i + 1] = B1 * (e[i + 1] + B2 * Af[i] + B3 * Vf[i] + B4 * Uf[i])
        # vitesse puis position au pas i+1 (schéma de Newmark)
        Vf[i + 1] = Vf[i] + (1 - gamma) * Te * Af[i] + gamma * Te * Af[i + 1]
        Uf[i + 1] = (Uf[i] + Te * Vf[i] + Te**2 * (0.5 - beta) * Af[i]
                     + Te**2 * beta * Af[i + 1])
    return Uf
```

La fonction effectue $N - 1$ passages dans la boucle : sa complexité est linéaire en la taille du signal. Test : pour un échelon unité, $\omega = 20\ \mathrm{rad \cdot s^{-1}}$, $z = 0{,}7$ et $T_e = 10^{-3}\ \mathrm{s}$, la sortie tend vers 1 et s'écarte de la solution exacte d'au plus $0{,}0046$.

> [!JURY]
> Le rapport 2016 s'étonne que les questions 25 et 26 n'aient été traitées que par environ 60 % des candidats, contre 80 % pour les questions voisines ; ceux qui les ont abordées ont en général plutôt bien réussi.

> [!PIEGE]
> La boucle s'arrête à l'indice $N - 2$ : elle écrit la case $i + 1$, et aller jusqu'à $N - 1$ ferait sortir de la liste.

### Question 26 — Version économe en mémoire

> [!INDICATION]
> Parmi les trois listes de la question 25, lesquelles sont réellement relues plus d'un pas après avoir été écrites ?

#### Solution

La fonction précédente crée trois listes de taille $N$ alors que seule `Uf` est demandée : les dérivées première et seconde ne servent qu'au pas suivant. On les remplace par deux scalaires, mis à jour à chaque pas ; la mémoire auxiliaire passe de $2N$ flottants à trois.

```python
def newmark2(gamma, beta, omega, z, e, Te):
    """Même calcul avec trois scalaires au lieu de deux listes auxiliaires."""
    N = len(e)
    Uf = [0.0] * N
    u, v, a = 0.0, 0.0, 0.0           # valeurs au pas courant i
    for i in range(N - 1):
        a_suiv = B1 * (e[i + 1] + B2 * a + B3 * v + B4 * u)
        # u d'abord : il utilise encore l'ancienne vitesse v
        u = u + Te * v + Te**2 * (0.5 - beta) * a + Te**2 * beta * a_suiv
        v = v + (1 - gamma) * Te * a + gamma * Te * a_suiv
        a = a_suiv
        Uf[i + 1] = u
    return Uf
```

L'ordre des mises à jour compte : le signal `u` est calculé avant `v`, car il utilise la vitesse du pas $i$. Test : cette fonction renvoie la même liste que celle de la question 25 pour tous les pas de temps essayés.

> [!PIEGE]
> En remplaçant les listes par des scalaires, mettre à jour la vitesse avant le signal fausse le calcul : la relation donnant $U_{f,i+1}$ utilise $\dot U_{f,i}$, pas $\dot U_{f,i+1}$.

**III.3 Détermination des pressions systolique et diastolique (questions 27 et 28).**

Convention retenue pour le critère : chaque maximum local (bosse) est comparé au minimum local (creux) qui le suit immédiatement dans le temps.

### Question 27 — Pression systolique

> [!INDICATION]
> Un maximum local se trouve en avançant tant que la valeur suivante est plus grande ; un minimum local en avançant tant qu'elle est plus petite.

> [!INDICATION]
> Structure possible : une boucle `while` sur le critère, contenant deux boucles `while` successives, l'une pour atteindre la bosse, l'autre pour atteindre le creux.

#### Solution

Le brassard se dégonfle : la pression décroît, d'abord sans oscillation, puis avec des bosses et des creux. On saute la descente initiale jusqu'au premier creux, puis on répète : monter jusqu'à la bosse, descendre jusqu'au creux suivant, évaluer le critère. On s'arrête à la première bosse qui le vérifie.

```python
def pression_systolique(data):
    n = len(data)
    i = 0
    # descente initiale : on rejoint le premier creux
    while i < n - 1 and data[i + 1] <= data[i]:
        i = i + 1
    critere = False
    while not critere:
        # montée jusqu'au maximum local
        while i < n - 1 and data[i + 1] >= data[i]:
            i = i + 1
        maxi = data[i]
        # descente jusqu'au minimum local suivant
        while i < n - 1 and data[i + 1] <= data[i]:
            i = i + 1
        mini = data[i]
        critere = (maxi - mini) / mini > 4e-5
    return maxi
```

Les tests `i < n - 1` empêchent de sortir du tableau. Les inégalités larges font franchir les éventuels paliers. Complexité linéaire : l'indice `i` ne recule jamais.

![Figure 3 — Bosses et creux de la pression filtrée, sens de parcours des questions 27 et 28](figures/q27-bosses-creux.svg)

Test : sur un signal synthétique (rampe décroissante de $175$ à $65\ \mathrm{mmHg}$ à laquelle s'ajoutent des oscillations d'amplitude variable), la fonction renvoie la même valeur qu'une recherche exhaustive de tous les couples bosse-creux, pour 41 signaux différents.

> [!JURY]
> Le rapport 2016 indique que 80 % des candidats ont abordé cette sous-partie mais que peu ont compris comment déterminer les extrema locaux. La solution la plus simple, selon lui, consiste en des boucles `while` imbriquées : une boucle sur le critère d'arrêt, contenant une boucle qui trouve un maximum local puis, au même niveau, une boucle qui trouve un minimum local.

> [!PIEGE]
> Le premier point du tableau n'est pas une bosse : sans le saut de la descente initiale, il serait comparé au premier creux et le critère serait vérifié à tort dès le départ.

### Question 28 — Pression diastolique

> [!INDICATION]
> « Pour la dernière fois en parcourant par temps croissant » équivaut à « pour la première fois en parcourant par temps décroissant ».

> [!INDICATION]
> Reprenez la structure de la question 27 en faisant décroître l'indice, et ajoutez la condition sur les $40\ \mathrm{mmHg}$ dans le critère.

#### Solution

On cherche cette fois la **dernière** bosse qui vérifie le critère (seuil $4 \times 10^{-3}$) et qui dépasse $40\ \mathrm{mmHg}$. Le plus simple est de parcourir le tableau à rebours, depuis la fin, et de s'arrêter à la première bosse rencontrée qui convient. En remontant le temps, on écarte d'abord la dernière bosse, dont le creux suivant n'est pas dans le tableau, puis on répète : mémoriser le creux, remonter jusqu'à la bosse qui le précède, tester, remonter jusqu'au creux précédent.

```python
def pression_diastolique(data):
    i = len(data) - 1
    # on remonte le temps : dernière bosse (son creux suivant est inconnu) ...
    while i > 0 and data[i - 1] >= data[i]:
        i = i - 1
    # ... puis creux qui la précède
    while i > 0 and data[i - 1] <= data[i]:
        i = i - 1
    critere = False
    while not critere:
        mini = data[i]                  # creux qui suit la bosse cherchée
        while i > 0 and data[i - 1] >= data[i]:
            i = i - 1
        maxi = data[i]                  # bosse
        critere = (maxi - mini) / mini > 4e-3 and maxi > 40
        while i > 0 and data[i - 1] <= data[i]:
            i = i - 1                   # creux précédent
    return maxi
```

La valeur `maxi` retenue est celle qui a rendu le critère vrai : la dernière boucle interne ne la modifie pas. Test : même contrôle qu'à la question 27, sur les mêmes 41 signaux, par comparaison avec la recherche exhaustive de la dernière bosse satisfaisant les deux conditions.

> [!JURY]
> Le rapport 2016 constate que peu de candidats parcourent la courbe de pression dans l'ordre décroissant, ce qui rend la réponse fausse.

## Partie IV — Stockage et analyse des résultats

Les requêtes ont été exécutées sur une base d'essai (SQLite) reproduisant les deux tables.

### Question 29 — Clé primaire

> [!INDICATION]
> Quelle propriété une clé primaire doit-elle garantir pour toutes les lignes de la table ? Passez en revue les attributs et demandez-vous lesquels la possèdent.

#### Solution

Une clé primaire est un attribut (ou un groupe d'attributs) dont la valeur **identifie de façon unique** chaque enregistrement d'une table : deux lignes distinctes n'ont jamais la même clé, et la clé est toujours renseignée.

- Dans `patients`, `id` désigne un patient sans ambiguïté, même en cas d'homonymes. C'est lui que la table `mesures` recopie dans `pid` pour rattacher chaque mesure à son patient : la clé primaire rend les jointures possibles.
- Dans `mesures`, `id` distingue deux mesures, même prises sur le même patient et de même type.

**Autre clé possible.** Dans `patients`, le numéro de sécurité sociale `numero_secu` est propre à chaque personne et pourrait servir de clé primaire, sous réserve que tout patient en ait un (ce n'est pas garanti pour un nouveau-né ou un patient étranger, d'où l'intérêt d'un identifiant interne). Les autres attributs ne conviennent pas : nom, prénom, date de naissance, adresse ou téléphone peuvent être communs à plusieurs patients. Dans `mesures`, aucun attribut seul ne convient (`pid`, `type` et `datetime` se répètent) ; seule une association comme (`pid`, `type`, `datetime`) pourrait jouer ce rôle.

> [!JURY]
> Le rapport 2016 note que cette question a donné lieu à quelques définitions étonnantes et que le concept reste assez mal maîtrisé.

### Question 30 — Mesures entre deux dates

> [!INDICATION]
> Une seule table est concernée. La condition porte sur l'attribut `datetime`, encadré par les deux dates.

#### Solution

```sql
SELECT datetime, pdias, psyst, pouls
FROM mesures
WHERE datetime >= time1 AND datetime <= time2;
```

La condition peut aussi s'écrire `datetime BETWEEN time1 AND time2`. Dans le format année-mois-jour heure:minute:seconde, l'ordre des chaînes de caractères coïncide avec l'ordre chronologique, la comparaison est donc correcte.

`time1` et `time2` sont des variables du programme : en Python, la requête envoyée au serveur est la chaîne

```python
requete = ("SELECT datetime, pdias, psyst, pouls FROM mesures WHERE datetime >= '"
           + time1 + "' AND datetime <= '" + time2 + "'")
```

> [!JURY]
> Le rapport 2016 relève une nette amélioration des réponses sur les bases de données ; les requêtes ont été plutôt bien traitées.

### Question 31 — Mesures de tension d'un patient

> [!INDICATION]
> Dans la table `mesures`, quel attribut contient l'identifiant du patient ? Attention, ce n'est pas `id`.

#### Solution

On ajoute deux conditions, sur le patient et sur le type de mesure. Les champs sont rangés dans l'ordre du tableau décrit ensuite par l'énoncé (date, systolique, diastolique, pouls).

```sql
SELECT datetime, psyst, pdias, pouls
FROM mesures
WHERE datetime >= time1 AND datetime <= time2
  AND pid = id_patient
  AND type = 'tension';
```

Aucune jointure n'est nécessaire : l'identifiant du patient figure dans `mesures` sous le nom `pid` (l'attribut `id` de cette table est l'identifiant de la mesure).

> [!PIEGE]
> Écrire `id = id_patient` sélectionne la mesure dont le numéro est celui du patient, pas les mesures du patient. `'tension'` est une chaîne de caractères : les apostrophes sont obligatoires.

### Question 32 — Tracé des trois courbes

> [!INDICATION]
> Séparez d'abord les colonnes : dans `resultat_requete`, l'ordre est date, systolique, diastolique, pouls.

> [!INDICATION]
> Un appel à `plot` par courbe avec une chaîne de format de l'annexe (couleur et type de trait), puis `xlabel`, `ylabel`, `title` et `legend`.

#### Solution

On extrait les quatre colonnes du tableau, puis on trace les trois courbes sur le même graphique, chacune avec son style, avant d'ajouter les titres et la légende (fonctions de l'annexe, supposées importées).

```python
n = len(resultat_requete)
temps = [resultat_requete[k][0] for k in range(n)]   # colonne datetime
psyst = [resultat_requete[k][1] for k in range(n)]   # pression systolique
pdias = [resultat_requete[k][2] for k in range(n)]   # pression diastolique
pouls = [resultat_requete[k][3] for k in range(n)]   # pouls
plot(temps, psyst, 'r-')     # systolique : trait continu rouge
plot(temps, pdias, 'b--')    # diastolique : tirets bleus
plot(temps, pouls, 'k:')     # pouls : pointillés noirs
xlabel('Date et heure de la mesure')
ylabel('Pression (mmHg) et pouls (pulsations par minute)')
title('Evolution de la tension et du pouls du patient')
legend(['Pression systolique', 'Pression diastolique', 'Pouls'])
```

La légende est donnée dans l'ordre des tracés. Pression et pouls partagent l'axe vertical : leurs valeurs sont du même ordre (quelques dizaines à deux centaines), ce qui garde le graphique lisible. Ces instructions ont été exécutées avec matplotlib sur un tableau d'essai.

> [!JURY]
> Le rapport 2016 regrette des réponses approximatives malgré la documentation fournie en annexe, et rappelle que le jury tient à ce que les candidats sachent tracer un graphique correctement légendé.

### Question 33 — Minimum, maximum et moyenne

> [!INDICATION]
> Initialisez minimum, maximum et somme avec le premier élément, puis parcourez le reste de la liste une seule fois.

#### Solution

Un seul parcours de la liste suffit : on tient à jour le plus petit élément, le plus grand et la somme. La liste est supposée non vide.

```python
def analyse(valeurs):
    mini = valeurs[0]
    maxi = valeurs[0]
    somme = valeurs[0]
    for k in range(1, len(valeurs)):
        v = valeurs[k]
        somme = somme + v
        if v < mini:
            mini = v
        elif v > maxi:
            maxi = v
    return mini, maxi, somme / len(valeurs)
```

Le `elif` évite une comparaison inutile : un élément plus petit que le minimum courant ne peut pas dépasser le maximum. Test : résultats identiques à ceux de `min`, `max` et `sum` sur 2000 listes aléatoires de 1 à 30 éléments.

> [!JURY]
> Le rapport 2016 indique que cette question est bien traitée dans la majorité des cas et que les algorithmes de base semblent bien maîtrisés.

### Question 34 — Complexité de la fonction analyse

> [!INDICATION]
> Comptez les opérations d'un passage dans la boucle, en distinguant le cas où le premier test est vrai de celui où il est faux.

#### Solution

La boucle est exécutée $n - 1$ fois. À chaque passage : 1 addition, puis 1 ou 2 comparaisons entre valeurs. Après la boucle : 1 division.

- **Meilleur cas** (liste strictement décroissante : chaque élément est un nouveau minimum, le second test n'est jamais fait) : $n - 1$ comparaisons, $n - 1$ additions, 1 division, soit $2n - 1$ opérations.
- **Pire cas** (aucun élément n'est plus petit que le minimum courant, par exemple une liste croissante : les deux tests sont toujours faits) : $2(n - 1)$ comparaisons, $n - 1$ additions, 1 division, soit $3n - 2$ opérations.

$$\boxed{\text{Complexité linéaire, en } O(n), \text{ dans le meilleur comme dans le pire des cas}}$$

Il n'y a ni soustraction ni multiplication. On ne peut pas faire mieux qu'un coût linéaire : chaque valeur doit être lue au moins une fois.

> [!JURY]
> Le rapport 2016 juge approximative la complexité calculatoire associée à ces algorithmes de base.

### Question 35 — Médiane par tri fusion

> [!INDICATION]
> Une fois la liste triée, où se trouve la médiane ? Distinguez les longueurs paires et impaires.

> [!INDICATION]
> Choisissez un tri du cours et décrivez-le en une phrase avant de l'écrire : par exemple le tri fusion, avec une fonction auxiliaire qui fusionne deux listes triées.

#### Solution

La médiane est la valeur centrale de la liste triée (la moyenne des deux valeurs centrales si le nombre d'éléments est pair). On trie donc une copie de la liste, ici par **tri fusion** : on coupe la liste en deux moitiés, on trie chacune récursivement, puis on fusionne les deux moitiés triées en prenant à chaque étape le plus petit des deux éléments de tête.

```python
def fusion(a, b):
    """Fusionne deux listes triées en une liste triée."""
    c = []
    i, j = 0, 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            c.append(a[i])
            i = i + 1
        else:
            c.append(b[j])
            j = j + 1
    # l'une des deux listes est épuisée : on recopie le reste de l'autre
    return c + a[i:] + b[j:]


def tri_fusion(t):
    if len(t) <= 1:
        return t[:]
    m = len(t) // 2
    return fusion(tri_fusion(t[:m]), tri_fusion(t[m:]))


def mediane(valeurs):
    t = tri_fusion(valeurs)
    n = len(t)
    if n % 2 == 1:
        return t[n // 2]
    return (t[n // 2 - 1] + t[n // 2]) / 2
```

La liste reçue n'est pas modifiée. Test : `mediane` renvoie la même valeur que la fonction `median` du module `statistics` sur 2000 listes aléatoires, de longueur paire ou impaire.

> [!JURY]
> Le rapport 2016 rappelle que la question demandait de faire appel à un algorithme de tri du cours et que les candidats pourraient mieux expliquer ce qu'ils vont faire avant de le faire ; la grande majorité utilise le tri rapide ou le tri fusion.

### Question 36 — Complexité et efficacité

> [!INDICATION]
> Combien de comparaisons faut-il, au moins et au plus, pour fusionner deux listes triées de $n/2$ éléments ?

> [!INDICATION]
> Écrivez la relation de récurrence sur le nombre de comparaisons pour $n = 2^p$ et sommez niveau par niveau : il y a $\log_2 n$ niveaux.

#### Solution

Seul le tri effectue des comparaisons entre valeurs ; le choix de la valeur centrale n'en demande aucune. Notons $C(n)$ le nombre de comparaisons du tri fusion, pour $n = 2^p$.

La fusion de deux listes triées de $n/2$ éléments demande entre $n/2$ comparaisons (une liste est épuisée avant que l'autre soit entamée) et $n - 1$ comparaisons (les éléments s'intercalent jusqu'au bout).

- **Meilleur cas** (par exemple une liste déjà triée) : $C(n) = 2\,C(n/2) + n/2$ avec $C(1) = 0$, d'où

$$C(n) = \frac{n}{2}\,\log_2 n .$$

- **Pire cas** : $C(n) = 2\,C(n/2) + n - 1$, d'où

$$C(n) = n\,\log_2 n - n + 1 .$$

$$\boxed{\text{Complexité en } O(n \log n) \text{ dans le meilleur comme dans le pire des cas}}$$

Contrôle par comptage sur machine pour $n = 8$ : 12 comparaisons pour une liste triée et 17 au maximum sur toutes les permutations, conformément aux deux formules.

**Efficacité.** Pour un tri, oui : $O(n \log n)$ est le meilleur ordre de grandeur possible pour un tri par comparaisons, bien meilleur que le $O(n^2)$ du tri par insertion ou par sélection dans le pire cas, et le tri fusion n'a pas de cas défavorable (contrairement au tri rapide). Pour la médiane seule, on fait cependant plus que nécessaire : trier toute la liste n'est pas indispensable, un algorithme de sélection trouve la valeur centrale en temps linéaire en moyenne. Le tri fusion consomme en outre une mémoire auxiliaire proportionnelle à $n$.

> [!JURY]
> Le rapport 2016 constate que la complexité calculatoire associée au tri choisi est, là encore, méconnue.

### Question 37 — Patients à surveiller

> [!INDICATION]
> Les informations demandées sont réparties dans deux tables : quel attribut de `mesures` correspond à la clé primaire de `patients` ?

> [!INDICATION]
> Les inégalités sont strictes. Un même patient peut avoir plusieurs mesures qui conviennent : comment éviter les doublons ?

#### Solution

Les noms sont dans `patients`, les constantes dans `mesures` : il faut une jointure, sur l'égalité entre la clé primaire `patients.id` et l'attribut `mesures.pid`. On retient les patients dont au moins une mesure vérifie les trois conditions à la fois.

```sql
SELECT DISTINCT patients.nom, patients.prenom, patients.telephone
FROM patients JOIN mesures ON patients.id = mesures.pid
WHERE mesures.psyst > 160 AND mesures.pdias > 110
  AND mesures.pouls > 100 AND mesures.pouls < 150;
```

Les deux tables ont un attribut `id` : il faut le préfixer par le nom de la table. `DISTINCT` évite qu'un patient apparaisse autant de fois qu'il a de mesures concernées. Test : sur la base d'essai, un patient ayant deux mesures conformes n'apparaît qu'une fois, et les patients dont une constante est exactement à la borne (pouls de 150, diastolique de 110) sont écartés.

> [!PIEGE]
> Les deux tables possèdent un attribut `id` : écrire `id = pid` sans préfixe est ambigu, et joindre sur `patients.id = mesures.id` associerait un patient à la mesure de même numéro.

## Bilan

**Méthodes à retenir.**

- Poutre hyperstatique : exploiter la symétrie pour réduire le modèle, isoler un tronçon pour écrire le torseur de cohésion, intégrer $EI\,u_y'' = M_Z$ et justifier chaque constante par une condition aux limites ; l'inconnue hyperstatique se détermine par la condition géométrique restante.
- Différentielle logarithmique d'un produit de puissances, avec ses signes, pour relier de petites variations relatives.
- Pont de Wheatstone : deux diviseurs de tension, linéarisation autour de l'équilibre, jauges de même signe sur des bras opposés. Le pont complet donne $V_p = K\,\varepsilon\,V_{alim}$.
- Numérisation : un convertisseur de $n$ bits délivre un entier parmi $2^n$ ; son pas est l'étendue de mesure divisée par $2^n$.
- Schéma d'intégration : écrire l'équation au pas $i+1$, isoler l'inconnue, puis juger le schéma par sa stabilité (pas critique) et son ordre (évolution de l'erreur avec le pas).
- Recherche d'extrema locaux par boucles `while` successives, avec garde sur les bornes du tableau ; « la dernière fois » se traite en parcourant à rebours.
- SQL : sélection avec conditions combinées par `AND`, jointure sur l'égalité clé primaire = clé étrangère, attributs préfixés quand deux tables partagent un nom, `DISTINCT` contre les doublons.
- Complexité : compter les opérations d'un passage de boucle dans le meilleur et le pire cas ; pour le tri fusion, poser la récurrence et la sommer.

**À revoir si la question a résisté.** Le décompte des inconnues de liaison dans un modèle plan (question 1), l'écriture du principe fondamental de la statique comme une somme nulle (question 2), les conversions d'unités de l'application numérique (question 16), la mise à jour ordonnée des variables dans un schéma numérique (questions 25 et 26).

**Questions transposables.** La chaîne capteur, jauges, pont de Wheatstone se retrouve dans de nombreux sujets de modélisation ; l'intégration numérique d'une équation différentielle du second ordre, la recherche d'extrema dans un signal échantillonné et le triplet minimum, maximum, moyenne, suivi d'un tri avec sa complexité, sont des exercices classiques de cette épreuve.
