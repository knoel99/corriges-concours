# Banque PT PT — Physique C - Thermodynamique 2012 · Corrigé guidé

*Corrigé rédigé par IA, non officiel. Signalez toute erreur.*

**Rédaction** · modèle exact non renseigné (famille Claude) · effort non renseigné · vitesse non renseignée

## Présentation du sujet

**Thème.** Étude d'une turbine à gaz (turbine à combustion). L'épreuve dure 2 heures, **calculatrice autorisée**, et comporte 40 questions numérotées de 1 à 40, en quatre parties. Un document réponse (la figure 8) est à rendre avec la copie.

- *Partie I (questions 1 à 4)* : premier principe pour un fluide en écoulement permanent, cas du gaz parfait, capacités thermiques massiques de l'air.
- *Partie II (questions 5 à 25)* : cycle de Joule idéal (deux isentropiques, deux isobares). Tracés dans les diagrammes $(P, v)$ et $(T, s)$, transferts thermiques et travaux, rendement, signification des aires, optimisation du travail récupéré.
- *Partie III (questions 26 à 29)* : compression à deux étages avec refroidissement intermédiaire, étudiée graphiquement.
- *Partie IV (questions 30 à 40)* : installation complète à deux étages de compression et de détente avec régénérateur, tracé sur le document réponse, rendement, puis limite d'un nombre infini d'étages.

**Notions mobilisées.** Premier principe des systèmes ouverts en régime permanent ; gaz parfait, relation de Mayer, lois de Joule et loi de Laplace ; identité thermodynamique et entropie du gaz parfait ; second principe pour une évolution réversible ; diagrammes de Clapeyron et entropique ; rendement d'un moteur, rendement de Carnot.

**Documents à lire.** Aucune table ni courbe graduée. Les figures 4, 6 et 8 du sujet sont des schémas sans échelle : il ne s'agit pas d'y lire des valeurs, mais d'y reconnaître des courbes (isobares, isotherme, isentropique) par le raisonnement. Les seules données numériques sont $M$, $\gamma$, $R$, $T_1 = 300\ \mathrm{K}$ et $T_3 = 1000\ \mathrm{K}$.

**Difficulté.** Le sujet est long mais très guidé et proche du cours. La difficulté est dans la rigueur : définir le système de la question 1, justifier chaque travail nul et chaque transfert thermique nul (questions 8 à 10), justifier la signification des aires (questions 17 et 18). Les questions 14 et 32 demandent de l'initiative. Deux applications numériques seulement (questions 4 et 25).

**Gestion du temps.** Environ 15 minutes pour la partie I, 55 minutes pour la partie II, 20 minutes pour la partie III et 30 minutes pour la partie IV. Les quatre parties sont largement indépendantes : les questions 26 à 31 et 33 à 36 peuvent être traitées même si la partie II n'est pas terminée.

> [!JURY]
> Le rapport 2012 note que les quatre parties, largement indépendantes, ont été abordées par le plus grand nombre. Il regrette un manque de rigueur dans une majorité de copies : les réponses doivent être clairement justifiées et ne peuvent se réduire à une suite d'affirmations. Beaucoup trop de résultats numériques sont donnés sans unité ou avec une unité fausse, et les résultats doivent être homogènes. Pour un nombre important de candidats, les questions proches du cours sont ignorées ou très mal traitées, ce qui fait perdre beaucoup de points ; dès qu'une question n'est pas détaillée, peu de candidats l'abordent. Le rapport déplore aussi l'emploi d'une encre trop claire dans certaines copies et estime que certains candidats auraient obtenu de meilleurs résultats en gérant mieux leur temps. Il souligne la présence d'excellentes copies, aux raisonnements parfaitement argumentés, qui traitent une grande partie du sujet.

[Sujet officiel (archive réunissant les deux parties de Physique C)](https://www.banquept.fr/documents/2012/phys_c_pt_2012.zip) · [Rapport du jury](https://www.banquept.fr/documents/ecrit/rapport/2012/rapport_phys_c_ecrit_2012.pdf)

*Mode d'emploi* : chercher chaque question seul, lire la première indication en cas de blocage, réessayer, puis la seconde, et seulement ensuite la solution. Convention : $w$ et $q$ désignent des grandeurs massiques reçues par l'air, comptées algébriquement. Les valeurs retenues pour tracer les figures, quand l'énoncé ne les donne pas, sont signalées comme un choix du corrigé.

## Partie I — Préliminaires

### Question 1 — Premier principe pour un écoulement permanent

> [!INDICATION]
> Le premier principe ne s'écrit que pour un système fermé. Construire un système fermé qui « accompagne » le fluide pendant une durée $\mathrm{d}t$ : le fluide contenu dans la machine, plus la petite masse qui va y entrer.

> [!INDICATION]
> Faire la liste des travaux reçus par ce système fermé : le travail indiqué, mais aussi le travail des forces de pression exercées par le fluide en amont (qui pousse) et en aval (qui est repoussé). C'est ce travail de transvasement qui transforme $u$ en $h = u + Pv$.

#### Solution

**Système.** La machine délimite un volume de contrôle (système ouvert). On lui associe un système fermé $\Sigma^*$, suivi entre les instants $t$ et $t + \mathrm{d}t$ :

- à l'instant $t$ : le fluide contenu dans la machine, plus la masse $\mathrm{d}m_e$ qui va y entrer pendant $\mathrm{d}t$ ;
- à l'instant $t + \mathrm{d}t$ : le fluide contenu dans la machine, plus la masse $\mathrm{d}m_s$ qui en est sortie pendant $\mathrm{d}t$.

**Régime permanent.** La masse et l'énergie du fluide contenu dans la machine ne dépendent pas du temps. La conservation de la masse de $\Sigma^*$ donne donc

$$\mathrm{d}m_e = \mathrm{d}m_s = \mathrm{d}m = D\,\mathrm{d}t$$

**Variation d'énergie de $\Sigma^*$.** L'énergie totale est la somme de l'énergie interne, de l'énergie cinétique macroscopique et de l'énergie potentielle de pesanteur. L'énergie du contenu de la machine étant la même à $t$ et à $t + \mathrm{d}t$, il ne reste que la différence entre la tranche sortie et la tranche entrée :

$$\mathrm{d}E = \mathrm{d}m\left[\left(u_s + \tfrac{1}{2}c_s^2 + g z_s\right) - \left(u_e + \tfrac{1}{2}c_e^2 + g z_e\right)\right]$$

**Énergie reçue par $\Sigma^*$ pendant $\mathrm{d}t$.**

- Travail des forces de pression en amont : le fluide situé en amont pousse la tranche entrante, de volume $v_e\,\mathrm{d}m$, sous la pression $P_e$. Travail reçu : $+P_e v_e\,\mathrm{d}m$.
- Travail des forces de pression en aval : la tranche sortante, de volume $v_s\,\mathrm{d}m$, repousse le fluide aval sous la pression $P_s$. Travail reçu : $-P_s v_s\,\mathrm{d}m$.
- Travail indiqué fourni par les parties mobiles de la machine : $w\,\mathrm{d}m$.
- Transfert thermique, reçu seulement dans la machine puisque les canalisations sont calorifugées : $q\,\mathrm{d}m$.

Le poids est déjà pris en compte par l'énergie potentielle : on ne le compte pas une seconde fois comme un travail.

**Premier principe appliqué à $\Sigma^*$.**

$$\mathrm{d}E = \left(P_e v_e - P_s v_s\right)\mathrm{d}m + w\,\mathrm{d}m + q\,\mathrm{d}m$$

En divisant par $\mathrm{d}m$ et en regroupant $u + Pv = h$ :

$$\boxed{(h_s - h_e) + \tfrac{1}{2}\left(c_s^2 - c_e^2\right) + g\,(z_s - z_e) = q + w}$$

Chaque terme est une énergie massique, en $\mathrm{J\cdot kg^{-1}}$.

> [!JURY]
> Le rapport qualifie cette question de question de cours et regrette qu'elle ne soit pas traitée avec plus de sérieux. Quelques copies donnent une démonstration clairement argumentée, mais la majorité propose un raisonnement bâclé, avec des notations imprécises. Le système fermé auquel on applique le premier principe est mal défini, les étapes sont peu ou pas justifiées (confusion entre régime permanent et système fermé), et beaucoup de candidats « démontrent » la relation en partant du résultat.

> [!METHODE]
> Quatre étapes à faire apparaître dans cet ordre : définition du système fermé aux deux instants ; usage du régime permanent (même masse entrante et sortante, énergie du contenu inchangée) ; bilan des travaux, dont ceux des forces de pression amont et aval ; regroupement en enthalpie.

### Question 2 — Cas d'un gaz parfait non pesant

> [!INDICATION]
> Trois hypothèses, trois simplifications : repérer le terme de la relation de la question 1 que chacune fait disparaître ou transforme.

> [!INDICATION]
> Pour un gaz parfait, l'enthalpie massique ne dépend que de la température : $\mathrm{d}h = c_{pm}\,\mathrm{d}T$.

#### Solution

On reprend la relation de la question 1.

- Air non pesant : le terme $g\,(z_s - z_e)$ est négligé.
- Variation d'énergie cinétique négligeable : le terme $\tfrac{1}{2}(c_s^2 - c_e^2)$ est négligé.
- Gaz parfait : l'enthalpie ne dépend que de la température (seconde loi de Joule), $\mathrm{d}h = c_{pm}\,\mathrm{d}T$. Comme $c_{pm}$ est indépendante de la température, $h_s - h_e = c_{pm}\,(T_s - T_e)$.

$$\boxed{c_{pm}\,(T_s - T_e) = q + w}$$

> [!PIEGE]
> Dans une machine traversée par un fluide, c'est l'enthalpie qui intervient, pas l'énergie interne : écrire $c_{vm}\,(T_s - T_e) = q + w$ revient à oublier le travail de transvasement.

### Question 3 — Capacités thermiques massiques

> [!INDICATION]
> Il faut deux relations entre $c_{pm}$ et $c_{vm}$ : la définition de $\gamma$ et la relation de Mayer, écrite pour un kilogramme de gaz.

> [!INDICATION]
> Pour une mole, $C_p - C_v = R$. Une mole a pour masse $M$ : diviser par $M$.

#### Solution

Relation de Mayer pour un gaz parfait, ramenée à l'unité de masse (une mole a pour masse $M$) :

$$c_{pm} - c_{vm} = \frac{R}{M}$$

Avec $c_{pm} = \gamma\,c_{vm}$, on obtient $c_{vm}\,(\gamma - 1) = R/M$, d'où

$$\boxed{c_{vm} = \frac{R}{M\,(\gamma - 1)}}$$

$$\boxed{c_{pm} = \frac{\gamma R}{M\,(\gamma - 1)}}$$

### Question 4 — Application numérique

> [!INDICATION]
> Convertir la masse molaire en $\mathrm{kg\cdot mol^{-1}}$ avant tout calcul.

> [!INDICATION]
> Contrôle : la capacité thermique massique à pression constante de l'air vaut environ $1\ \mathrm{kJ\cdot K^{-1}\cdot kg^{-1}}$.

#### Solution

Avec $M = 29\times 10^{-3}\ \mathrm{kg\cdot mol^{-1}}$, $\gamma = 1{,}4$ et $R = 8{,}31\ \mathrm{J\cdot K^{-1}\cdot mol^{-1}}$ :

$$c_{vm} = \frac{8{,}31}{29\times 10^{-3}\times 0{,}4} = 716\ \mathrm{J\cdot K^{-1}\cdot kg^{-1}}$$

$$c_{pm} = \gamma\,c_{vm} = \frac{1{,}4\times 8{,}31}{29\times 10^{-3}\times 0{,}4} = 1{,}00\times 10^{3}\ \mathrm{J\cdot K^{-1}\cdot kg^{-1}}$$

$$\boxed{c_{pm} \approx 1{,}00\times 10^{3}\ \mathrm{J\cdot K^{-1}\cdot kg^{-1}} \qquad c_{vm} \approx 7{,}2\times 10^{2}\ \mathrm{J\cdot K^{-1}\cdot kg^{-1}}}$$

Le calcul donne $c_{pm} = 1003\ \mathrm{J\cdot K^{-1}\cdot kg^{-1}}$ ; c'est cette valeur qui sert dans la suite.

> [!JURY]
> Le rapport déplore que beaucoup trop de candidats donnent leurs résultats numériques sans unité ou avec une unité fausse.

> [!PIEGE]
> Laisser $M$ en grammes par mole donne des capacités mille fois trop petites. L'ordre de grandeur connu pour l'air permet de s'en apercevoir.

## Partie II — Modélisation idéale du cycle : cycle de Joule

### Question 5 — Cycle dans le diagramme de Clapeyron

> [!INDICATION]
> Placer d'abord les deux isobares, horizontales : $P_1$ en bas (points 1 et 4), $P_2$ en haut (points 2 et 3).

> [!INDICATION]
> Une isentropique de gaz parfait vérifie $P v^{\gamma} = \text{cste}$ : courbe décroissante. Pour ordonner les points sur une même isobare, comparer les températures : à pression fixée, $v$ est proportionnel à $T$.

#### Solution

Dans le plan $(P, v)$ :

- $1 \to 2$, compression isentropique : arc de courbe $P v^{\gamma} = \text{cste}$ (loi de Laplace, gaz parfait en évolution isentropique), parcouru vers les pressions croissantes et les volumes massiques décroissants ;
- $2 \to 3$, chauffage isobare : segment horizontal à $P_2$, parcouru vers la droite car $v = RT/(MP)$ augmente avec $T$ ;
- $3 \to 4$, détente isentropique : second arc $P v^{\gamma} = \text{cste}$, situé à droite du premier, parcouru vers les pressions décroissantes ;
- $4 \to 1$, refroidissement isobare : segment horizontal à $P_1$, parcouru vers la gauche.

Comme $T_3 > T_2$ et $T_4 > T_1$, on a $v_3 > v_2$ et $v_4 > v_1$. **Le cycle est parcouru dans le sens horaire** : c'est un cycle moteur.

![Figure 1 — Cycle de Joule dans le diagramme de Clapeyron (P, v), parcouru dans le sens horaire](figures/q05-cycle-joule-clapeyron.svg)

La figure est tracée à l'échelle pour les valeurs de la question 25 ($P_2/P_1 \approx 8{,}2$).

> [!PIEGE]
> Le sens de parcours n'est pas un détail : il est demandé par l'énoncé et il conditionne le signe du travail aux questions 17 à 19.

### Question 6 — Entropie massique du gaz parfait

> [!INDICATION]
> Partir de l'identité thermodynamique écrite avec l'enthalpie : $\mathrm{d}h = T\,\mathrm{d}s + v\,\mathrm{d}P$.

> [!INDICATION]
> Remplacer $\mathrm{d}h$ par $c_{pm}\,\mathrm{d}T$ et $v$ par $RT/(MP)$, diviser par $T$, puis intégrer entre l'état $(T_0, P_0)$ et l'état $(T, P)$.

#### Solution

Identité thermodynamique pour un kilogramme d'air :

$$\mathrm{d}h = T\,\mathrm{d}s + v\,\mathrm{d}P$$

Pour le gaz parfait, $\mathrm{d}h = c_{pm}\,\mathrm{d}T$ et $v = \dfrac{RT}{MP}$, donc

$$\mathrm{d}s = c_{pm}\,\frac{\mathrm{d}T}{T} - \frac{R}{M}\,\frac{\mathrm{d}P}{P}$$

L'entropie est une fonction d'état et $c_{pm}$ est constante : on intègre de $(T_0, P_0)$ à $(T, P)$.

$$\boxed{s(T, P) = s_0 + c_{pm}\ln\frac{T}{T_0} - \frac{R}{M}\ln\frac{P}{P_0}}$$

Comme $\dfrac{R}{M} = c_{pm}\,\dfrac{\gamma - 1}{\gamma}$, on peut aussi écrire $s = s_0 + c_{pm}\ln\left[\dfrac{T}{T_0}\left(\dfrac{P_0}{P}\right)^{(\gamma-1)/\gamma}\right]$.

Contrôle : à entropie constante on retrouve la loi de Laplace $T^{\gamma}P^{1-\gamma} = \text{cste}$.

> [!METHODE]
> Les arguments des logarithmes sont des rapports sans dimension : $T/T_0$ et $P/P_0$. Écrire $\ln T$ ou $\ln P$ seuls n'a pas de sens.

### Question 7 — Allure d'une isobare dans le diagramme (T, s)

> [!INDICATION]
> Fixer $P$ dans l'expression de la question 6 et l'inverser pour obtenir $T$ en fonction de $s$.

> [!INDICATION]
> Pour comparer deux isobares, regarder à entropie donnée laquelle correspond à la température la plus élevée.

#### Solution

Sur une isobare de pression $P$, la relation de la question 6 s'inverse en

$$\boxed{T = T_0\left(\frac{P}{P_0}\right)^{(\gamma-1)/\gamma}\exp\left(\frac{s - s_0}{c_{pm}}\right)}$$

À pression fixée, $T$ est une **fonction exponentielle croissante de $s$**. Sa pente, $\left(\dfrac{\partial T}{\partial s}\right)_P = \dfrac{T}{c_{pm}}$, est positive et augmente avec la température : la courbe est convexe.

C'est bien l'allure des arcs $2 \to 3$ et $4 \to 1$ de la figure 4 du sujet. De plus :

- à entropie donnée, la température est multipliée par $(P_2/P_1)^{(\gamma-1)/\gamma} > 1$ quand on passe de l'isobare $P_1$ à l'isobare $P_2$ : l'isobare $P_2$ (arc $2 \to 3$) est au-dessus de l'isobare $P_1$ (arc $4 \to 1$) ; les deux courbes se déduisent l'une de l'autre par une translation parallèle à l'axe des entropies ;
- les deux isentropiques $1 \to 2$ et $3 \to 4$ sont des segments verticaux.

> [!JURY]
> Le rapport précise une fois de plus que les résultats présentés doivent être homogènes et rappelle, à ce propos, qu'une exponentielle n'a pas d'unité.

> [!METHODE]
> Contrôle d'homogénéité : l'argument de l'exponentielle, $(s - s_0)/c_{pm}$, est le rapport de deux grandeurs en $\mathrm{J\cdot K^{-1}\cdot kg^{-1}}$ ; le facteur $(P/P_0)^{(\gamma-1)/\gamma}$ est sans dimension ; le résultat est bien une température.

### Question 8 — Transferts thermiques dans les échangeurs

> [!INDICATION]
> Appliquer la relation de la question 2 à chacun des deux échangeurs. Que vaut le travail indiqué dans un échangeur, et pourquoi ?

> [!INDICATION]
> Un échangeur ne contient aucune pièce mobile : c'est cela, et non le caractère isobare, qui annule le travail indiqué.

#### Solution

Un échangeur de chaleur est un organe à parois fixes, sans aucune pièce mobile : le travail indiqué y est nul, $w = 0$. La relation de la question 2 (écoulement permanent, gaz parfait, énergies cinétique et potentielle négligées) se réduit à $c_{pm}\,(T_s - T_e) = q$.

$$\boxed{q_{23} = c_{pm}\,(T_3 - T_2)}$$

$$\boxed{q_{41} = c_{pm}\,(T_1 - T_4)}$$

Signes : $q_{23} > 0$ (l'air est chauffé, $T_3 > T_2$) et $q_{41} < 0$ (l'air cède de la chaleur à l'atmosphère, $T_1 < T_4$).

> [!JURY]
> Le rapport relève une confusion fréquente entre le premier principe pour un système fermé au repos macroscopique et le premier principe pour un fluide en écoulement. De nombreux candidats justifient l'égalité entre la variation d'enthalpie massique et le transfert thermique dans un échangeur en disant qu'une évolution isobare s'accompagne d'un travail nul, ce que le rapport refuse.

> [!PIEGE]
> Le travail des forces de pression n'est pas nul sur une isobare ($v$ varie). Il est déjà compté dans l'enthalpie. Ce qui est nul ici, c'est le travail indiqué, faute de pièce mobile.

### Question 9 — Travail massique reçu dans le compresseur

> [!INDICATION]
> Même relation qu'à la question 8, mais c'est maintenant le transfert thermique qu'il faut annuler. Avec quel argument ?

> [!INDICATION]
> L'évolution est donnée réversible et isentropique : pour une évolution réversible, $\delta q = T\,\mathrm{d}s$.

#### Solution

**La compression est adiabatique.** L'énoncé la donne à la fois réversible et isentropique. Pour une évolution réversible, le transfert thermique massique élémentaire est $\delta q = T\,\mathrm{d}s$ ; comme $\mathrm{d}s = 0$, on a $q_{12} = 0$. Physiquement, le compresseur n'est pas conçu pour échanger de la chaleur et l'air le traverse trop vite pour que cet échange compte.

La relation de la question 2 donne alors

$$\boxed{w_{12} = c_{pm}\,(T_2 - T_1)}$$

$w_{12} > 0$ : l'air reçoit du travail, sa température augmente ($T_2 > T_1$).

> [!JURY]
> D'après le rapport, le caractère adiabatique des évolutions dans le compresseur et dans la turbine est soit non justifié, soit mal justifié (par exemple en affirmant qu'une isentropique est nécessairement adiabatique et réversible), et peu de candidats se soucient de cette justification. Le rapport signale aussi des copies où le travail indiqué d'une évolution adiabatique est égalé à la variation d'énergie interne massique.

> [!PIEGE]
> « Isentropique » seul n'entraîne pas « adiabatique » : une évolution irréversible peut garder son entropie si elle cède de la chaleur. L'implication tient ici parce que l'énoncé précise que les quatre évolutions sont réversibles.

### Question 10 — Travail massique reçu dans la turbine

> [!INDICATION]
> Le raisonnement est celui de la question 9, entre les points 3 et 4.

> [!INDICATION]
> Vérifier le signe : la turbine fournit du travail à l'arbre, donc l'air en reçoit un travail négatif.

#### Solution

La détente dans la turbine est réversible et isentropique, donc adiabatique ($\delta q = T\,\mathrm{d}s = 0$). La relation de la question 2 donne

$$\boxed{w_{34} = c_{pm}\,(T_4 - T_3)}$$

$w_{34} < 0$ puisque $T_4 < T_3$ : l'air cède du travail aux aubes de la turbine, donc à l'arbre.

### Question 11 — Travail net en fonction des travaux

> [!INDICATION]
> $w_{net}$ est un travail récupéré par l'extérieur, alors que $w_{12}$ et $w_{34}$ sont des travaux reçus par l'air : attention à la convention.

> [!INDICATION]
> L'arbre reçoit $-w_{34}$ de la turbine et doit fournir $w_{12}$ au compresseur.

#### Solution

$w_{12}$ et $w_{34}$ sont des travaux massiques **reçus par l'air**. Le travail net est celui que l'arbre met à la disposition de l'extérieur : la turbine fournit $-w_{34} > 0$ à l'arbre, qui en cède $w_{12}$ au compresseur monté sur le même arbre.

$$\boxed{w_{net} = -\,(w_{12} + w_{34}) = |w_{34}| - w_{12}}$$

Ce travail est rapporté à un kilogramme d'air admis. Comme l'énoncé le définit pour un kilogramme d'air par seconde, la puissance récupérée pour un débit $D$ est $D\,w_{net}$.

> [!PIEGE]
> Écrire $w_{net} = w_{12} + w_{34}$ donne une grandeur négative : c'est le travail total reçu par l'air sur un cycle, l'opposé du travail récupéré.

### Question 12 — Travail net en fonction des températures

> [!INDICATION]
> Reporter les résultats des questions 9 et 10 dans celui de la question 11.

#### Solution

Avec $w_{12} = c_{pm}\,(T_2 - T_1)$ et $w_{34} = c_{pm}\,(T_4 - T_3)$ :

$$\boxed{w_{net} = c_{pm}\left[(T_3 - T_4) - (T_2 - T_1)\right]}$$

Le premier terme est le travail fourni par la turbine, le second le travail absorbé par le compresseur.

### Question 13 — Définition du rendement

> [!INDICATION]
> Un rendement est le rapport de ce qui est utile à ce qui est coûteux. Qu'est-ce qui coûte, dans une turbine à combustion ?

> [!INDICATION]
> La chaleur $q_{41}$ est rejetée à l'atmosphère : elle ne coûte rien et ne figure pas au dénominateur.

#### Solution

Le rendement est le rapport de la grandeur utile, le travail net récupéré sur l'arbre, à la grandeur coûteuse, la chaleur fournie par la source chaude (la combustion, modélisée par l'échangeur $2 \to 3$) :

$$\boxed{\eta = \frac{w_{net}}{q_{23}}}$$

C'est un nombre sans dimension compris entre 0 et 1.

### Question 14 — Rendement en fonction de T₁ et T₂

> [!INDICATION]
> Exprimer $w_{net}$ et $q_{23}$ avec les quatre températures (ou écrire le premier principe sur le cycle : $w_{net} = q_{23} + q_{41}$). Il reste à relier $T_4$ aux autres températures.

> [!INDICATION]
> Les deux isentropiques relient les deux mêmes pressions : la loi de Laplace donne $T_2/T_1 = T_3/T_4$.

#### Solution

**Expression avec les quatre températures.** Sur un cycle, la variation d'enthalpie massique est nulle. La somme des relations de la question 2 écrites pour les quatre organes donne $w_{12} + w_{34} + q_{23} + q_{41} = 0$, soit $w_{net} = q_{23} + q_{41}$. Donc

$$\eta = 1 + \frac{q_{41}}{q_{23}} = 1 - \frac{T_4 - T_1}{T_3 - T_2}$$

**Lien entre les températures.** Pour un gaz parfait en évolution isentropique, la loi de Laplace s'écrit $T^{\gamma}P^{1-\gamma} = \text{cste}$ (elle se lit aussi sur le résultat de la question 6 à $s$ constante). Les évolutions $1 \to 2$ et $3 \to 4$ relient les deux mêmes pressions $P_1$ et $P_2$ :

$$\frac{T_2}{T_1} = \left(\frac{P_2}{P_1}\right)^{(\gamma-1)/\gamma} = \frac{T_3}{T_4}$$

On en tire $\dfrac{T_4}{T_1} = \dfrac{T_3}{T_2}$, donc

$$T_4 - T_1 = T_1\left(\frac{T_3}{T_2} - 1\right) = \frac{T_1}{T_2}\,(T_3 - T_2)$$

**Conclusion.**

$$\boxed{\eta = 1 - \frac{T_1}{T_2}}$$

Ce n'est pas le rendement de Carnot : celui-ci ferait intervenir les températures extrêmes du cycle et vaudrait $1 - T_1/T_3$, valeur plus grande puisque $T_2 < T_3$.

> [!JURY]
> Le rapport note que très peu de copies ont traité cette question et que beaucoup de candidats confondent ce rendement avec celui de Carnot. Il la cite comme exemple de question non détaillée, que peu de candidats abordent.

> [!METHODE]
> Dans un cycle à deux isobares et deux isentropiques, le réflexe est de relier les quatre températures par la loi de Laplace : le rapport $T_2/T_1 = T_3/T_4$ simplifie presque tous les résultats de la partie II.

### Question 15 — Rendement en fonction du taux de compression

> [!INDICATION]
> Il suffit d'exprimer $T_2/T_1$ avec $\tau$ : la relation a déjà été écrite à la question 14.

#### Solution

D'après la loi de Laplace utilisée à la question 14 :

$$\frac{T_2}{T_1} = \left(\frac{P_2}{P_1}\right)^{(\gamma-1)/\gamma} = \tau^{(\gamma-1)/\gamma}$$

Donc $\eta = 1 - \dfrac{T_1}{T_2} = 1 - \dfrac{1}{z}$ avec

$$\boxed{z = \tau^{(\gamma-1)/\gamma} = \frac{T_2}{T_1} = \frac{T_3}{T_4}}$$

Pour l'air, $(\gamma - 1)/\gamma = 0{,}4/1{,}4 \approx 0{,}286$.

### Question 16 — Comment augmenter le rendement

> [!INDICATION]
> Étudier le sens de variation de $z$ avec $\tau$, puis celui de $\eta$ avec $z$.

> [!INDICATION]
> Un rendement élevé ne suffit pas : que devient le travail récupéré par kilogramme d'air quand $T_2$ s'approche de $T_3$ ? Penser aussi à ce que coûte un compresseur.

#### Solution

Comme $\gamma > 1$, $z = \tau^{(\gamma-1)/\gamma}$ est une fonction croissante de $\tau$, et $\eta = 1 - 1/z$ est une fonction croissante de $z$. **Pour augmenter le rendement, il faut augmenter le taux de compression $\tau = P_2/P_1$.**

Mais le rendement n'est pas le seul critère de conception :

- la température de fin de compression $T_2 = z\,T_1$ ne peut pas dépasser $T_3$, elle-même limitée par la tenue des matériaux des aubes ;
- quand $T_2$ s'approche de $T_3$, la chaleur reçue $q_{23}$ et le travail net par kilogramme d'air tendent vers zéro : pour une puissance donnée, il faudrait un débit d'air, donc une machine, de plus en plus grands ;
- un compresseur à fort taux de compression est coûteux à construire et à entretenir.

L'étude technico-commerciale doit donc prendre en compte **le travail récupéré par kilogramme d'air** (la puissance de l'installation pour un débit donné) et le **coût** de l'installation, en particulier celui du compresseur. C'est l'objet des questions 17 à 25.

### Question 17 — Aire du cycle dans le diagramme de Clapeyron

> [!INDICATION]
> L'aire d'un cycle dans le plan $(P, v)$ est, au signe près, $\oint P\,\mathrm{d}v$. Il faut relier cette intégrale au travail indiqué d'un fluide en écoulement, qui n'est pas $-\int P\,\mathrm{d}v$.

> [!INDICATION]
> Pour une évolution réversible, comparer $\mathrm{d}h = \delta q + \delta w$ et $\mathrm{d}h = T\,\mathrm{d}s + v\,\mathrm{d}P$ avec $\delta q = T\,\mathrm{d}s$. Puis utiliser $\oint \mathrm{d}(Pv) = 0$.

#### Solution

**Travail indiqué élémentaire.** Pour un kilogramme d'air traversant un organe, la relation de la question 2 s'écrit, sur une étape élémentaire, $\mathrm{d}h = \delta q + \delta w$. Les évolutions sont réversibles, donc $\delta q = T\,\mathrm{d}s$. En comparant avec l'identité thermodynamique $\mathrm{d}h = T\,\mathrm{d}s + v\,\mathrm{d}P$ :

$$\delta w = v\,\mathrm{d}P$$

Ce résultat est cohérent avec la question 8 : dans un échangeur isobare, $\mathrm{d}P = 0$ et le travail indiqué est nul.

**Sur le cycle.** Le travail total reçu par l'air est

$$w_{12} + w_{34} = \oint v\,\mathrm{d}P$$

Or $\oint \mathrm{d}(Pv) = 0$ sur un cycle ($Pv$ est une fonction d'état), donc $\oint v\,\mathrm{d}P = -\oint P\,\mathrm{d}v$.

**Lien avec l'aire.** Dans le plan $(P, v)$, $\oint P\,\mathrm{d}v$ est l'aire $\mathcal{A}$ délimitée par le cycle, comptée positivement lorsque le cycle est parcouru dans le sens horaire : la branche haute $2 \to 3 \to 4$ est parcourue vers les $v$ croissants, la branche basse $4 \to 1 \to 2$ vers les $v$ décroissants. C'est le cas ici (question 5). Donc

$$\boxed{\mathcal{A}_{(P,v)} = \oint P\,\mathrm{d}v = -\,(w_{12} + w_{34}) = w_{net}}$$

**L'aire du cycle dans le diagramme de Clapeyron représente le travail net massique récupéré sur l'arbre.**

> [!JURY]
> Le rapport juge les réponses aux questions 17 et 18 peu rigoureuses : beaucoup de candidats se contentent d'écrire que l'aire est le résultat du produit d'un volume et d'une pression.

> [!PIEGE]
> Pour un système fermé, le travail reçu est celui des forces de pression, $-\int P\,\mathrm{d}v$. Ici le fluide s'écoule et le travail utile est le travail indiqué, $\int v\,\mathrm{d}P$. Les deux intégrales ne coïncident que sur un cycle complet : il faut le dire.

### Question 18 — Aire du cycle dans le diagramme (T, s)

> [!INDICATION]
> Même démarche : que vaut $T\,\mathrm{d}s$ pour une évolution réversible ?

> [!INDICATION]
> Vérifier le sens de parcours du cycle dans le plan $(T, s)$ à l'aide de la figure 4 du sujet.

#### Solution

Dans le plan $(T, s)$, l'aire délimitée par le cycle est $\oint T\,\mathrm{d}s$, comptée positivement si le cycle est parcouru dans le sens horaire. C'est le cas sur la figure 4 du sujet : la branche haute $2 \to 3$ est parcourue vers les entropies croissantes, la branche basse $4 \to 1$ vers les entropies décroissantes.

Toutes les évolutions sont réversibles : d'après le second principe, l'entropie créée est nulle et le transfert thermique massique élémentaire reçu par l'air est $\delta q = T\,\mathrm{d}s$. Donc

$$\boxed{\mathcal{A}_{(T,s)} = \oint T\,\mathrm{d}s = q_{23} + q_{41}}$$

**L'aire du cycle dans le diagramme $(T, s)$ représente le transfert thermique massique total reçu par l'air au cours d'un cycle.**

Détail : l'aire sous l'arc $2 \to 3$ (jusqu'à l'axe des entropies) vaut $q_{23} > 0$, l'aire sous l'arc $4 \to 1$ vaut $|q_{41}|$, et les deux isentropiques verticales ne contribuent pas.

### Question 19 — Lecture du travail net sur le diagramme (T, s)

> [!INDICATION]
> Écrire le premier principe pour un kilogramme d'air qui a parcouru tout le cycle.

#### Solution

L'enthalpie est une fonction d'état : sur un cycle, $\Delta h = 0$. En sommant la relation de la question 2 sur les quatre organes :

$$0 = (w_{12} + w_{34}) + (q_{23} + q_{41})$$

$$\boxed{w_{net} = -\,(w_{12} + w_{34}) = q_{23} + q_{41} = \mathcal{A}_{(T,s)}}$$

Le travail net récupéré sur l'arbre est donc égal à l'aire du cycle dans le diagramme $(T, s)$ : il se lit directement sur ce diagramme. Les deux aires, dans $(P, v)$ et dans $(T, s)$, représentent la même grandeur.

### Question 20 — Cycles de Joule pour deux rapports de compression

> [!INDICATION]
> Ce qui est fixé : le point 1, l'isobare $P_1$ (qui passe par 1 et porte le point 4), et l'isotherme $T_3$ (qui porte le point 3). Ce qui change : la hauteur du point 2 sur la verticale issue de 1.

> [!INDICATION]
> Calculer $T_4$ dans chaque cas avec $T_4 = T_1 T_3 / T_2$ (question 14).

#### Solution

Éléments fixes du tracé : le point 1 (température $T_1$, pression $P_1$), l'isobare $P_1$ issue de 1, qui porte le point 4, et l'horizontale $T = T_3$, qui porte le point 3. Le point 2 est sur la verticale issue de 1 (isentropique), d'autant plus haut que le rapport de compression est grand. Le point 3 est à l'intersection de l'isobare $P_2$ issue de 2 et de l'horizontale $T_3$ ; le point 4 est à la verticale de 3, sur l'isobare $P_1$. D'après la question 14, $T_4 = T_1 T_3 / T_2$.

**a. $T_2$ proche de $T_3$ (grand rapport de compression).** L'isentropique $1 \to 2$ monte presque jusqu'à $T_3$, l'isobare $2 \to 3$ est très courte, et $T_4 = T_1 T_3/T_2$ est proche de $T_1$. Le cycle est une bande verticale très étroite, collée à la verticale issue de 1.

**b. $T_2$ proche de $T_1$ (petit rapport de compression).** L'isentropique $1 \to 2$ est très courte, l'isobare $P_2$ est presque confondue avec l'isobare $P_1$, et $T_4$ est proche de $T_3$. Le cycle est une bande très mince, couchée le long de l'isobare $P_1$.

![Figure 2 — Cycles de Joule dans le diagramme (T, s) à T₁, T₃ et P₁ fixés : cas a, cas b et cas d'aire maximale](figures/q20-cycles-joule-entropique.svg)

La figure est tracée à l'échelle pour $T_1 = 300\ \mathrm{K}$ et $T_3 = 1000\ \mathrm{K}$, avec $T_2 = 900\ \mathrm{K}$ (cas a), $T_2 = 330\ \mathrm{K}$ (cas b) et $T_2 = 548\ \mathrm{K}$ (cas de la question 25). Ces valeurs de $T_2$ pour les cas a et b sont un choix du corrigé, l'énoncé ne les chiffrant pas.

> [!PIEGE]
> Changer le rapport de compression ne déplace ni le point 1 ni l'isobare $P_1$. En revanche le point 3 se déplace le long de l'horizontale $T_3$ : son entropie n'est pas fixée.

### Question 21 — Existence d'un maximum du travail net

> [!INDICATION]
> Utiliser la question 19 : le travail net est l'aire du cycle. Que vaut cette aire dans les deux cas extrêmes de la question 20 ?

#### Solution

D'après la question 19, $w_{net}$ est l'aire du cycle dans le diagramme $(T, s)$.

- Quand $T_2 \to T_1$ (cas b poussé à la limite), les deux isobares se confondent : l'aire tend vers zéro.
- Quand $T_2 \to T_3$ (cas a poussé à la limite), l'isobare $2 \to 3$ se réduit à un point : l'aire tend vers zéro.
- Entre les deux, l'aire est strictement positive et varie continûment avec le rapport de compression.

Une fonction continue, positive, nulle aux deux bornes de l'intervalle, admet un maximum à l'intérieur : **$w_{net}$ passe par un maximum pour une valeur de $T_2$ comprise entre $T_1$ et $T_3$**, c'est-à-dire pour un rapport de compression intermédiaire.

### Question 22 — Travail net en fonction de z

> [!INDICATION]
> Exprimer $T_2$ et $T_4$ en fonction de $z$, $T_1$ et $T_3$ avec la question 15, puis reporter dans la question 12.

#### Solution

D'après la question 15, $T_2 = z\,T_1$ et $T_4 = \dfrac{T_3}{z}$. En reportant dans le résultat de la question 12 :

$$\boxed{w_{net} = c_{pm}\left[T_3\left(1 - \frac{1}{z}\right) - T_1\,(z - 1)\right]}$$

Contrôle : $w_{net} = 0$ pour $z = 1$ ($T_2 = T_1$) et pour $z = T_3/T_1$ ($T_2 = T_3$), comme attendu à la question 21.

### Question 23 — Valeur de z donnant le travail net maximal

> [!INDICATION]
> Dériver $w_{net}$ par rapport à $z$, à $T_1$ et $T_3$ fixés.

> [!INDICATION]
> Vérifier qu'il s'agit d'un maximum (signe de la dérivée seconde, ou argument de la question 21).

#### Solution

À $T_1$ et $T_3$ fixés :

$$\frac{\mathrm{d}w_{net}}{\mathrm{d}z} = c_{pm}\left(\frac{T_3}{z^2} - T_1\right)$$

Cette dérivée s'annule pour $z^2 = T_3/T_1$. Elle est positive avant et négative après ; la dérivée seconde, $-2\,c_{pm}T_3/z^3$, est négative. Il s'agit bien d'un maximum :

$$\boxed{z_{max} = \sqrt{\frac{T_3}{T_1}}}$$

On a alors $T_2 = z\,T_1 = \sqrt{T_1 T_3}$ et $T_4 = T_3/z = \sqrt{T_1 T_3}$ : **le travail net est maximal quand $T_2 = T_4$**. Cette valeur est bien comprise entre $1$ et $T_3/T_1$.

### Question 24 — Travail net maximal

> [!INDICATION]
> Remplacer $z$ par $\sqrt{T_3/T_1}$ dans l'expression de la question 22 et reconnaître un carré.

#### Solution

Avec $z = \sqrt{T_3/T_1}$, on a $T_3/z = z\,T_1 = \sqrt{T_1 T_3}$, donc

$$w_{net,max} = c_{pm}\left(T_3 - \sqrt{T_1 T_3} - \sqrt{T_1 T_3} + T_1\right)$$

$$\boxed{w_{net,max} = c_{pm}\left(T_1 + T_3 - 2\sqrt{T_1 T_3}\right) = c_{pm}\left(\sqrt{T_3} - \sqrt{T_1}\right)^2}$$

### Question 25 — Application numérique

> [!INDICATION]
> Calculer d'abord $z$, puis $T_2 = z\,T_1$ et $T_4 = T_3/z$, le rendement $1 - 1/z$ et enfin le travail.

> [!INDICATION]
> On peut en déduire le taux de compression correspondant, $\tau = z^{\gamma/(\gamma-1)}$, pour juger du réalisme du résultat.

#### Solution

Données : $T_1 = 300\ \mathrm{K}$, $T_3 = 1000\ \mathrm{K}$, $c_{pm} = 1003\ \mathrm{J\cdot K^{-1}\cdot kg^{-1}}$ (question 4).

$$z = \sqrt{\frac{1000}{300}} = 1{,}826$$

$$T_2 = T_4 = \sqrt{T_1 T_3} = \sqrt{300\times 1000} = 548\ \mathrm{K}$$

$$w_{net} = c_{pm}\left(T_1 + T_3 - 2\sqrt{T_1 T_3}\right) = 1003\times(1300 - 2\times 547{,}7) = 2{,}05\times 10^{5}\ \mathrm{J\cdot kg^{-1}}$$

$$\eta = 1 - \frac{1}{z} = 1 - \frac{300}{547{,}7} = 0{,}45$$

$$\boxed{w_{net} \approx 205\ \mathrm{kJ\cdot kg^{-1}} \qquad T_2 = T_4 \approx 548\ \mathrm{K} \qquad \eta \approx 0{,}45}$$

Compléments : le taux de compression correspondant est $\tau = z^{\gamma/(\gamma-1)} = 1{,}826^{3{,}5} \approx 8{,}2$. Pour un kilogramme d'air par seconde, la puissance récupérée est d'environ $205\ \mathrm{kW}$. Le rendement de Carnot entre $300\ \mathrm{K}$ et $1000\ \mathrm{K}$ vaudrait $0{,}70$.

Contrôle : $q_{23} = c_{pm}\,(T_3 - T_2) = 1003\times 452{,}3 = 4{,}54\times 10^{5}\ \mathrm{J\cdot kg^{-1}}$, et $w_{net}/q_{23} = 0{,}45$.

> [!METHODE]
> Deux contrôles rapides : $T_2$ et $T_4$ doivent tomber entre $T_1$ et $T_3$, et le rendement doit rester inférieur au rendement de Carnot entre les températures extrêmes, ici $0{,}70$.

## Partie III — Mise en place d'une compression étagée

### Question 26 — Isotherme et isentropique issues du point 1

> [!INDICATION]
> Écrire l'équation de chacune des deux courbes dans le plan $(P, v)$ pour un gaz parfait, puis calculer sa pente $\mathrm{d}P/\mathrm{d}v$ en un même point.

> [!INDICATION]
> Les deux courbes partent du point 1, à la pression $P_1$ (pointillé du bas), et montent vers les hautes pressions. La plus raide s'écarte le moins vers la gauche.

#### Solution

**Pentes au même point du plan $(P, v)$.**

- Isotherme d'un gaz parfait : $Pv = \dfrac{RT}{M} = \text{cste}$. En différentiant, $v\,\mathrm{d}P + P\,\mathrm{d}v = 0$ :

$$\left(\frac{\partial P}{\partial v}\right)_T = -\frac{P}{v}$$

- Isentropique d'un gaz parfait (loi de Laplace) : $Pv^{\gamma} = \text{cste}$. En différentiant, $v^{\gamma}\,\mathrm{d}P + \gamma P v^{\gamma-1}\,\mathrm{d}v = 0$ :

$$\left(\frac{\partial P}{\partial v}\right)_s = -\gamma\,\frac{P}{v}$$

D'où la relation demandée :

$$\boxed{\left(\frac{\partial P}{\partial v}\right)_s = \gamma\left(\frac{\partial P}{\partial v}\right)_T}$$

Les deux pentes sont négatives et, comme $\gamma = 1{,}4 > 1$, **l'isentropique est plus raide que l'isotherme** en tout point.

**Identification sur la figure 6 du sujet.** L'axe vertical porte $P$, l'axe horizontal $v$ ; les trois pointillés horizontaux sont les isobares $P_1$ (en bas), $P_x$ et $P_2$ (en haut). Les deux courbes partent du point 1, situé sur le pointillé du bas, et montent vers la gauche. La plus raide atteint une pression donnée avec le volume massique le plus grand : **la courbe de droite est l'isentropique, la courbe de gauche est l'isotherme $T_1$**.

Vérification physique : au cours d'une compression isentropique, la température augmente ; à pression donnée, le volume massique $v = RT/(MP)$ est donc plus grand que sur l'isotherme.

> [!JURY]
> Le rapport constate que le tracé des évolutions classiques dans les diagrammes $(P, v)$ et $(T, s)$ n'est pas maîtrisé, avec une confusion fréquente entre compression et détente.

> [!PIEGE]
> « Plus raide » ne dit pas de quel côté se trouve la courbe : cela dépend du sens de parcours. Partant du même point, l'isentropique est à droite de l'isotherme pour une compression, et à gauche (en dessous) pour une détente.

### Question 27 — Compressions à un et à deux étages dans le diagramme de Clapeyron

> [!INDICATION]
> Placer d'abord le point 1b : il est à la pression $P_x$ et à la température $T_1$, donc sur l'isotherme issue de 1.

> [!INDICATION]
> La seconde compression, de 1b à 2a, est une nouvelle isentropique : elle part de l'isotherme et s'en écarte vers la droite, puisqu'elle est plus raide.

#### Solution

On reprend la figure 6 avec l'isentropique et l'isotherme identifiées à la question 26.

- **Un étage, $1 \to 2$** : on suit l'isentropique issue de 1 (courbe de droite) de la pression $P_1$ jusqu'à la pression $P_2$.
- **Deux étages** :
  - $1 \to 1a$ : même isentropique, mais seulement de $P_1$ à $P_x$ ; le point 1a est à l'intersection de cette courbe et de l'horizontale $P_x$ ;
  - $1a \to 1b$ : refroidissement isobare, segment horizontal à $P_x$ parcouru vers la gauche (le volume massique diminue avec la température) jusqu'à la température $T_1$, c'est-à-dire jusqu'à l'isotherme issue de 1 ; le point 1b est à l'intersection de l'horizontale $P_x$ et de l'isotherme ;
  - $1b \to 2a$ : isentropique issue de 1b, de $P_x$ à $P_2$. Plus raide que l'isotherme, elle passe à droite de celle-ci, mais à gauche de la première isentropique : le point 2a est sur l'horizontale $P_2$, à gauche du point 2.

![Figure 3 — Compression à un étage et à deux étages dans le diagramme de Clapeyron ; l'aire verte est le travail économisé](figures/q27-compression-etagee-clapeyron.svg)

La figure est tracée à l'échelle pour $P_x/P_1 = P_2/P_x = 3$ et $\gamma = 1{,}4$ ; ces rapports de pression sont un choix du corrigé pour le dessin.

### Question 28 — Intérêt de la compression à deux étages

> [!INDICATION]
> Le travail indiqué d'une compression réversible est $\int v\,\mathrm{d}P$ (question 17). À quelle aire du diagramme de Clapeyron correspond-il ?

> [!INDICATION]
> C'est l'aire comprise entre la courbe et l'axe des pressions (axe vertical), et non l'aire sous la courbe.

#### Solution

Pour une compression réversible d'un fluide en écoulement, le travail indiqué massique est $w = \displaystyle\int v\,\mathrm{d}P$ (question 17). Dans le diagramme de Clapeyron, c'est **l'aire comprise entre la courbe suivie et l'axe des pressions**, entre les horizontales $P_1$ et $P_2$. Le palier $1a \to 1b$ est isobare et ne contribue pas.

- Un étage : aire à gauche de la courbe $1 \to 2$.
- Deux étages : aire à gauche de la ligne $1 \to 1a \to 1b \to 2a$.

Entre $P_1$ et $P_x$ les deux lignes coïncident. Entre $P_x$ et $P_2$, la courbe $1b \to 2a$ est à gauche de la courbe $1a \to 2$ : les volumes massiques y sont plus petits à chaque pression. La différence des deux travaux est l'aire du quadrilatère curviligne $1a$–$2$–$2a$–$1b$ (en vert sur la figure 3).

**La compression à deux étages avec refroidissement intermédiaire demande donc moins de travail que la compression à un étage**, pour les mêmes pressions extrêmes : on comprime un gaz refroidi, donc moins volumineux. De plus l'air sort moins chaud ($T_{2a} < T_2$).

Vérification par le calcul, avec la question 9. En posant $a = (P_x/P_1)^{(\gamma-1)/\gamma}$ et $b = (P_2/P_x)^{(\gamma-1)/\gamma}$ :

$$w_{\text{un étage}} = c_{pm}T_1\,(ab - 1)$$

$$w_{\text{deux étages}} = c_{pm}T_1\,(a - 1) + c_{pm}T_1\,(b - 1)$$

$$w_{\text{un étage}} - w_{\text{deux étages}} = c_{pm}T_1\,(a - 1)(b - 1) > 0$$

À la limite d'un très grand nombre d'étages, la ligne suivie se rapproche de l'isotherme, qui correspond au travail de compression le plus faible.

> [!JURY]
> Selon le rapport, l'intérêt d'une compression à deux étages a rarement été mis en évidence.

> [!PIEGE]
> L'aire sous la courbe (jusqu'à l'axe des volumes) est $\int P\,\mathrm{d}v$ : c'est le travail des forces de pression d'un système fermé, pas le travail indiqué d'un compresseur traversé par un fluide.

### Question 29 — Compression à deux étages dans le diagramme (T, s)

> [!INDICATION]
> D'après la question 7, les isobares sont des exponentielles croissantes décalées horizontalement. Laquelle est la plus à gauche ?

> [!INDICATION]
> Une compression isentropique est un segment vertical montant ; un refroidissement isobare descend le long d'une isobare, vers les entropies décroissantes.

#### Solution

**Isobares.** D'après la question 7, ce sont trois exponentielles croissantes qui se déduisent l'une de l'autre par translation horizontale. À température donnée, l'entropie diminue quand la pression augmente (question 6) : de la droite vers la gauche, on trouve $P_1$, $P_x$, $P_2$. Autrement dit, à entropie donnée, l'isobare $P_2$ est la plus haute.

**Isotherme $T_1$.** Droite horizontale. Le point 1 est à son intersection avec l'isobare $P_1$.

**Évolutions.**

- $1 \to 1a$ : compression isentropique, segment vertical montant du point 1 jusqu'à l'isobare $P_x$.
- $1a \to 1b$ : refroidissement isobare, on redescend le long de l'isobare $P_x$ (entropie décroissante) jusqu'à l'isotherme $T_1$.
- $1b \to 2a$ : compression isentropique, segment vertical montant du point 1b jusqu'à l'isobare $P_2$.

![Figure 4 — Compression à deux étages dans le diagramme (T, s), avec les isobares P₁, Pₓ, P₂ et l'isotherme T₁](figures/q29-compression-etagee-entropique.svg)

La compression à un étage serait le segment vertical issu de 1 prolongé jusqu'à l'isobare $P_2$ (point 2, en pointillés). La figure est tracée pour des rapports de pression égaux, $P_x/P_1 = P_2/P_x$, comme le propose l'énoncé à la fin de la partie III : dans ce cas $T_{1a} = T_{2a}$.

## Partie IV — Turbine à gaz avec compresseur et turbine à deux étages et régénérateur

### Question 30 — Cycle complet sur la figure 8 du document réponse

> [!INDICATION]
> Identifier d'abord les courbes. Les quatre droites horizontales sont les isothermes, de bas en haut $T_1$, $T_2$, $T_5$, $T_6$. Les trois courbes croissantes sont les isobares : laquelle est $P_2$ ?

> [!INDICATION]
> Chaque point est l'intersection d'une isotherme et d'une isobare. Dresser le tableau (température, pression) des dix points à l'aide des égalités de température données par l'énoncé, puis relier les points : verticales pour les isentropiques, arcs d'isobare pour les échanges thermiques.

#### Solution

**Identification des courbes de la figure 8.**

- Les quatre droites horizontales (traits mixtes) sont les isothermes. De bas en haut : $T_1$, $T_2$, $T_5$, $T_6$. En effet la compression donne $T_2 > T_1$, la détente donne $T_6 > T_7 = T_5$, et le préchauffage dans le régénérateur donne $T_5 > T_4 = T_2$.
- Les trois courbes croissantes (pointillés) sont les isobares. D'après la question 29, de la gauche vers la droite : $P_2$, $P_x$, $P_1$.

**Position des dix points.** L'énoncé donne $T_1 = T_3$, $T_4 = T_2 = T_{10}$, $T_5 = T_7 = T_9$ et $T_6 = T_8$.

| Point | Température | Pression | Position sur la figure 8 |
|---|---|---|---|
| 1 | $T_1$ | $P_1$ | isotherme du bas, isobare de droite |
| 2 | $T_2$ | $P_x$ | deuxième isotherme, isobare du milieu, à la verticale de 1 |
| 3 | $T_1$ | $P_x$ | isotherme du bas, isobare du milieu |
| 4 | $T_2$ | $P_2$ | deuxième isotherme, isobare de gauche, à la verticale de 3 |
| 5 | $T_5$ | $P_2$ | troisième isotherme, isobare de gauche |
| 6 | $T_6$ | $P_2$ | isotherme du haut, isobare de gauche |
| 7 | $T_5$ | $P_x$ | troisième isotherme, isobare du milieu, à la verticale de 6 |
| 8 | $T_6$ | $P_x$ | isotherme du haut, isobare du milieu |
| 9 | $T_5$ | $P_1$ | troisième isotherme, isobare de droite, à la verticale de 8 |
| 10 | $T_2$ | $P_1$ | deuxième isotherme, isobare de droite |

**Tracé.**

- $1 \to 2$ et $3 \to 4$ : segments verticaux montants (compressions isentropiques).
- $2 \to 3$ : arc de l'isobare $P_x$ parcouru en descendant (refroidissement).
- $4 \to 5$ puis $5 \to 6$ : arc de l'isobare $P_2$ parcouru en montant (régénérateur, puis chambre de combustion).
- $6 \to 7$ et $8 \to 9$ : segments verticaux descendants (détentes isentropiques).
- $7 \to 8$ : arc de l'isobare $P_x$ parcouru en montant (réchauffement).
- $9 \to 10$ puis $10 \to 1$ : arc de l'isobare $P_1$ parcouru en descendant (régénérateur, puis refroidissement).

Le cycle est parcouru dans le sens horaire (cycle moteur).

![Figure 5 — Cycle de la turbine à deux étages avec régénérateur, tracé sur les isobares et les isothermes de la figure 8](figures/q30-cycle-regenerateur-entropique.svg)

Sur la figure 8 du sujet, les courbes sont bien disposées pour que les points 1 et 2, 3 et 4, 6 et 7, 8 et 9 soient à la verticale l'un de l'autre. La figure 5 ci-dessus reproduit cette disposition avec des valeurs choisies par le corrigé pour le dessin ($T_1 = 300\ \mathrm{K}$, $T_5 = 700\ \mathrm{K}$, rapport de pression 3 par étage) ; la figure 8 du sujet ne porte aucune graduation.

> [!JURY]
> Le rapport indique que, dans cette quatrième partie, le fonctionnement du régénérateur, du réchauffement lors des détentes et du refroidissement lors des compressions n'a pas été compris.

> [!METHODE]
> Avant de tracer, écrire le couple (température, pression) de chaque point. Le tracé se réduit alors à dix intersections et le contrôle est immédiat : toute isentropique doit être verticale.

### Question 31 — Lecture graphique des transferts thermiques

> [!INDICATION]
> Les quatre transferts ont lieu sur des isobares, dans des échangeurs sans pièce mobile : la relation de la question 2 les exprime simplement.

> [!INDICATION]
> Chaque transfert est $c_{pm}$ fois une différence de températures : il se lit sur l'axe des ordonnées, comme l'écart entre deux isothermes.

#### Solution

Les quatre transferts ont lieu dans des échangeurs (ou dans la chambre de combustion), sans pièce mobile : $w = 0$ et la relation de la question 2 donne $q = c_{pm}\,(T_s - T_e)$.

Chaque transfert thermique se lit donc **sur l'axe des ordonnées, comme la différence des températures des deux isothermes qui encadrent l'arc d'isobare parcouru**, au coefficient $c_{pm}$ près :

$$\boxed{\begin{aligned}
q_{45} &= c_{pm}\,(T_5 - T_2) > 0 \\
q_{56} &= c_{pm}\,(T_6 - T_5) > 0 \\
q_{9\,10} &= c_{pm}\,(T_2 - T_5) < 0 \\
q_{10\,1} &= c_{pm}\,(T_1 - T_2) < 0
\end{aligned}}$$

Sur le diagramme de la question 30 (figure 5), ils sont portés le long des arcs correspondants : $q_{45}$ et $q_{56}$ sur l'isobare $P_2$, entre les isothermes $T_2$ et $T_5$ puis $T_5$ et $T_6$ ; $q_{9\,10}$ et $q_{10\,1}$ sur l'isobare $P_1$, entre les isothermes $T_5$ et $T_2$ puis $T_2$ et $T_1$.

On vérifie que $q_{9\,10} = -q_{45}$ : dans le régénérateur idéal, toute la chaleur cédée par l'air détendu est reçue par l'air comprimé. C'est ce qui impose $T_{10} = T_4$ et $T_5 = T_9$.

Remarque : chaque transfert est aussi l'aire sous l'arc d'isobare correspondant, puisque $\delta q = T\,\mathrm{d}s$ ; mais la lecture par simple différence, demandée ici, est celle des températures.

### Question 32 — Rendement de l'installation

> [!INDICATION]
> Recenser toutes les chaleurs reçues de l'extérieur : il y en a deux (chambre de combustion et réchauffement entre les deux turbines). La chaleur échangée dans le régénérateur est interne à l'installation.

> [!INDICATION]
> Les deux étages ont le même rapport de pression : $w_{12} = w_{34}$, $w_{67} = w_{89}$ et $q_{56} = q_{78}$.

#### Solution

**Définition.** Grandeur utile : le travail net récupéré sur l'arbre, $w_{net} = -\,(w_{12} + w_{34} + w_{67} + w_{89})$. Grandeur coûteuse : la chaleur fournie par l'extérieur à haute température, c'est-à-dire dans la chambre de combustion ($q_{56}$) et lors du réchauffement entre les deux turbines ($q_{78}$). Les transferts $q_{45}$ et $q_{9\,10}$ sont échangés à l'intérieur de l'installation, dans le régénérateur, et ne coûtent rien ; $q_{23}$ et $q_{10\,1}$ sont cédés à l'extérieur.

$$\boxed{\eta = \frac{-\,(w_{12} + w_{34} + w_{67} + w_{89})}{q_{56} + q_{78}}}$$

Le premier principe sur le cycle, avec $q_{45} + q_{9\,10} = 0$, donne $w_{net} = q_{56} + q_{78} + q_{23} + q_{10\,1}$, d'où la forme équivalente

$$\eta = 1 + \frac{q_{23} + q_{10\,1}}{q_{56} + q_{78}}$$

**Expression avec les températures.** Avec la relation de la question 2 et les égalités de températures de l'énoncé :

$$\begin{aligned}
w_{12} &= c_{pm}\,(T_2 - T_1) \\
w_{34} &= c_{pm}\,(T_4 - T_3) = c_{pm}\,(T_2 - T_1) \\
w_{67} &= c_{pm}\,(T_7 - T_6) = -\,c_{pm}\,(T_6 - T_5) \\
w_{89} &= c_{pm}\,(T_9 - T_8) = -\,c_{pm}\,(T_6 - T_5) \\
q_{56} &= c_{pm}\,(T_6 - T_5) \\
q_{78} &= c_{pm}\,(T_8 - T_7) = c_{pm}\,(T_6 - T_5)
\end{aligned}$$

$$\eta = \frac{2\,c_{pm}\left[(T_6 - T_5) - (T_2 - T_1)\right]}{2\,c_{pm}\,(T_6 - T_5)}$$

$$\boxed{\eta = 1 - \frac{T_2 - T_1}{T_6 - T_5}}$$

**Simplification.** Les étages ont tous le même rapport de pression, donc, par la loi de Laplace, $\dfrac{T_2}{T_1} = \dfrac{T_6}{T_7} = \dfrac{T_6}{T_5}$. Alors $\dfrac{T_2 - T_1}{T_6 - T_5} = \dfrac{T_1}{T_5}$ et

$$\eta = 1 - \frac{T_1}{T_5} = 1 - \frac{T_2}{T_6}$$

> [!JURY]
> Le rapport signale que l'expression du rendement donnée à cette question s'est souvent avérée fausse, faute d'avoir compris le rôle du régénérateur, du réchauffement lors des détentes et du refroidissement lors des compressions.

> [!PIEGE]
> Deux erreurs à éviter au dénominateur : y faire figurer $q_{45}$ (chaleur gratuite, récupérée sur les gaz détendus) ou oublier $q_{78}$ (le réchauffement entre les deux turbines est bien une chaleur apportée par l'extérieur).

### Question 33 — Taux de compression d'un étage

> [!INDICATION]
> Les rapports de pression des étages successifs se multiplient.

#### Solution

Soit $r$ le taux de compression commun aux $n$ étages. Les refroidissements intermédiaires sont isobares, donc la pression de sortie d'un étage est la pression d'entrée du suivant. Les taux se multiplient :

$$r^{\,n} = \frac{P_2}{P_1}$$

$$\boxed{r = \left(\frac{P_2}{P_1}\right)^{1/n}}$$

Pour $n = 2$, on retrouve $P_x = \sqrt{P_1 P_2}$.

### Question 34 — Limite d'un nombre infini d'étages

> [!INDICATION]
> Écrire $r = \exp\left[\dfrac{1}{n}\ln\dfrac{P_2}{P_1}\right]$ et faire tendre $n$ vers l'infini.

> [!INDICATION]
> En déduire ce que devient l'échauffement de l'air dans un étage.

#### Solution

$$r = \exp\left[\frac{1}{n}\ln\frac{P_2}{P_1}\right] \xrightarrow[n \to +\infty]{} 1$$

$$\boxed{\lim_{n \to +\infty} r = 1}$$

Chaque étage ne réalise plus qu'une compression élémentaire. La température en sortie d'un étage, $T_1\,r^{(\gamma-1)/\gamma}$, tend vers $T_1$ : l'air, ramené à $T_1$ après chaque étage, ne s'en écarte plus. **La compression étagée devient une compression isotherme à la température $T_1$.** De même, une détente à nombre infini d'étages avec réchauffements devient une détente isotherme à la température la plus haute.

### Question 35 — Cycle limite dans le diagramme (T, s)

> [!INDICATION]
> Deux isothermes : deux horizontales. Deux isobares : deux exponentielles croissantes, $P_2$ à gauche de $P_1$.

> [!INDICATION]
> Le cycle est moteur : il doit être parcouru dans le sens horaire. La compression (vers $P_2$) se fait à la température basse.

#### Solution

Le cycle est délimité par deux horizontales (isothermes $T_a$ en bas, $T_b$ en haut) et par deux arcs d'exponentielle (isobare $P_2$ à gauche, isobare $P_1$ à droite, d'après les questions 7 et 29). En nommant A, B, C, D ses sommets (notation du corrigé) :

- $A \to B$ : compression isotherme à $T_a$, de $P_1$ à $P_2$ ; segment horizontal parcouru vers la gauche (l'entropie diminue quand la pression augmente à température fixée) ;
- $B \to C$ : chauffage isobare à $P_2$, de $T_a$ à $T_b$ ; arc montant ;
- $C \to D$ : détente isotherme à $T_b$, de $P_2$ à $P_1$ ; segment horizontal parcouru vers la droite ;
- $D \to A$ : refroidissement isobare à $P_1$, de $T_b$ à $T_a$ ; arc descendant.

Le cycle est parcouru dans le sens horaire.

![Figure 6 — Cycle limite formé de deux isothermes et de deux isobares dans le diagramme (T, s)](figures/q35-cycle-isothermes-isobares.svg)

Les deux arcs d'isobare se déduisent l'un de l'autre par translation horizontale : les segments AB et CD ont la même longueur. La figure est tracée pour $T_a = 300\ \mathrm{K}$, $T_b = 1000\ \mathrm{K}$ et $P_2/P_1 = 9$, valeurs choisies par le corrigé pour le dessin.

### Question 36 — Identification des évolutions

> [!INDICATION]
> Reprendre le cycle de la question 30 et regarder ce que deviennent ses différentes portions quand le nombre d'étages augmente.

#### Solution

Sur le cycle de la question 35 (sommets A, B, C, D de la figure 6) :

- **Régénérateur** : les deux isobares. Sur $B \to C$ (isobare $P_2$), l'air comprimé est préchauffé de $T_a$ à $T_b$ ; la chaleur nécessaire, $c_{pm}\,(T_b - T_a)$, lui est cédée par l'air détendu qui se refroidit de $T_b$ à $T_a$ sur $D \to A$ (isobare $P_1$). Ces deux transferts sont opposés et internes à l'installation.
- **Réchauffement lors des détentes** : l'isotherme haute $C \to D$, à la température $T_b$. C'est la limite de la ligne en dents de scie $6 \to 7 \to 8 \to 9$ de la question 30 ; l'air y reçoit de la chaleur de la source chaude.
- **Refroidissement lors des compressions** : l'isotherme basse $A \to B$, à la température $T_a$. C'est la limite de la ligne $1 \to 2 \to 3 \to 4$ ; l'air y cède de la chaleur à l'extérieur.

### Question 37 — Transfert thermique du réchauffement

> [!INDICATION]
> L'évolution est isotherme et réversible : le second principe donne $q = T\,\Delta s$.

> [!INDICATION]
> Calculer $\Delta s$ avec l'expression de la question 6, à température constante.

#### Solution

L'évolution $C \to D$ est réversible et isotherme à la température $T_b$. Le second principe s'écrit, pour un kilogramme d'air, $\Delta s = s_{\text{échangée}} + s_{\text{créée}}$ avec $s_{\text{créée}} = 0$ (réversibilité) et $s_{\text{échangée}} = q_{ch}/T_b$ :

$$q_{ch} = T_b\,(s_D - s_C)$$

D'après la question 6, à température constante, entre les pressions $P_2$ (point C) et $P_1$ (point D) :

$$s_D - s_C = -\frac{R}{M}\ln\frac{P_1}{P_2} = \frac{R}{M}\ln\frac{P_2}{P_1}$$

$$\boxed{q_{ch} = \frac{R\,T_b}{M}\ln\frac{P_2}{P_1}}$$

$q_{ch} > 0$ : l'air reçoit de la chaleur pendant qu'il se détend.

> [!PIEGE]
> Sur une isotherme, la relation $q = c_{pm}\,\Delta T$ donnerait zéro : elle ne vaut que dans un organe sans travail indiqué. Ici, détente et réchauffement sont simultanés, et la chaleur reçue compense exactement le travail cédé ($\Delta h = 0$).

### Question 38 — Transfert thermique du refroidissement

> [!INDICATION]
> Même raisonnement sur l'isotherme basse, parcourue de $P_1$ vers $P_2$.

#### Solution

L'évolution $A \to B$ est réversible et isotherme à la température $T_a$, de la pression $P_1$ à la pression $P_2$. De la même façon :

$$q_{fr} = T_a\,(s_B - s_A) = -\,T_a\,\frac{R}{M}\ln\frac{P_2}{P_1}$$

$$\boxed{q_{fr} = -\frac{R\,T_a}{M}\ln\frac{P_2}{P_1}}$$

$q_{fr} < 0$ : l'air cède de la chaleur à l'extérieur pendant qu'il est comprimé.

### Question 39 — Rendement du cycle limite

> [!INDICATION]
> Quelle est la seule chaleur fournie par la source chaude ? Ne pas compter celle du régénérateur.

> [!INDICATION]
> Le premier principe sur le cycle donne le travail net comme somme de tous les transferts thermiques ; ceux des deux isobares se compensent.

#### Solution

Les transferts thermiques sur les deux isobares se compensent, $c_{pm}\,(T_b - T_a)$ et $-\,c_{pm}\,(T_b - T_a)$, et restent internes à l'installation (régénérateur idéal). La seule chaleur fournie par l'extérieur à haute température est $q_{ch}$.

Premier principe sur le cycle ($\Delta h = 0$) :

$$w_{net} = q_{ch} + q_{fr} = \frac{R}{M}\,(T_b - T_a)\ln\frac{P_2}{P_1}$$

$$\eta = \frac{w_{net}}{q_{ch}} = 1 + \frac{q_{fr}}{q_{ch}}$$

$$\boxed{\eta = 1 - \frac{T_a}{T_b}}$$

Ce rendement ne dépend plus des pressions. Avec $T_a = 300\ \mathrm{K}$ et $T_b = 1000\ \mathrm{K}$ (températures $T_1$ et $T_3$ de la partie II), il vaudrait $0{,}70$, contre $0{,}45$ pour le cycle de Joule simple de la question 25.

### Question 40 — Remarque et choix pratique de trois étages

> [!INDICATION]
> Reconnaître l'expression obtenue à la question 39.

> [!INDICATION]
> Pour la seconde partie de la question, mettre en balance le gain apporté par un étage supplémentaire et ce qu'il coûte.

#### Solution

**Remarque.** On reconnaît le **rendement de Carnot** d'un moteur fonctionnant entre deux sources de températures $T_a$ et $T_b$ : c'est le rendement maximal permis par le second principe entre ces deux températures. Le résultat était prévisible : le cycle limite est réversible et n'échange de la chaleur avec l'extérieur qu'à ces deux températures, la chaleur des isobares étant recyclée à l'intérieur par le régénérateur idéal. Le rendement ne dépend alors ni du gaz ni du rapport des pressions. L'étagement des compressions et des détentes, associé à la régénération, fait donc passer du rendement $1 - T_1/T_2$ du cycle de Joule (question 14) au rendement de Carnot.

**Pourquoi trois étages en pratique.** Cette limite suppose un nombre infini d'étages et des échangeurs parfaits. Or :

- le gain apporté par chaque étage supplémentaire décroît vite : l'essentiel du rapprochement vers l'isotherme est obtenu avec les deux ou trois premiers étages ;
- chaque étage ajoute un compresseur ou une turbine et un échangeur, donc du coût, de l'encombrement, de la masse et de la maintenance ;
- chaque échangeur réel introduit des pertes de charge et des écarts de température, c'est-à-dire des irréversibilités qui finissent par annuler le gain théorique.

Trois étages constituent un compromis entre le rendement et le coût de l'installation.

## Bilan

**Résultats à retenir.**

| Grandeur | Résultat |
|---|---|
| Premier principe en écoulement permanent (question 1) | $\Delta h + \Delta\left(\tfrac{1}{2}c^2\right) + g\,\Delta z = q + w$ |
| Capacités thermiques de l'air (question 4) | $c_{pm} \approx 1{,}00\times 10^{3}$ et $c_{vm} \approx 7{,}2\times 10^{2}\ \mathrm{J\cdot K^{-1}\cdot kg^{-1}}$ |
| Entropie du gaz parfait (question 6) | $s = s_0 + c_{pm}\ln(T/T_0) - (R/M)\ln(P/P_0)$ |
| Rendement du cycle de Joule (questions 14 et 15) | $\eta = 1 - T_1/T_2 = 1 - \tau^{-(\gamma-1)/\gamma}$ |
| Travail net maximal (questions 23 et 24) | $z = \sqrt{T_3/T_1}$, $w_{net} = c_{pm}\left(\sqrt{T_3} - \sqrt{T_1}\right)^2$ |
| Valeurs numériques (question 25) | $w_{net} \approx 205\ \mathrm{kJ\cdot kg^{-1}}$, $T_2 = T_4 \approx 548\ \mathrm{K}$, $\eta \approx 0{,}45$ |
| Pentes dans le diagramme de Clapeyron (question 26) | pente de l'isentropique $= \gamma\ \times$ pente de l'isotherme |
| Rendement avec deux étages et régénérateur (question 32) | $\eta = 1 - (T_2 - T_1)/(T_6 - T_5)$ |
| Rendement du cycle limite (question 39) | $\eta = 1 - T_a/T_b$ (rendement de Carnot) |

**Méthodes à retenir.**

- Fluide en écoulement permanent : passer par un système fermé défini à deux instants, puis utiliser $\Delta h = q + w$ organe par organe en annulant $w$ (pas de pièce mobile) ou $q$ (évolution adiabatique) avec un argument explicite.
- Cycle à deux isobares et deux isentropiques : relier les températures par la loi de Laplace, $T_2/T_1 = T_3/T_4$.
- Aires de cycle : $\oint P\,\mathrm{d}v$ dans le diagramme de Clapeyron, $\oint T\,\mathrm{d}s$ dans le diagramme entropique ; pour un cycle réversible, elles sont égales et valent le travail net.
- Diagramme $(T, s)$ d'un gaz parfait : isentropiques verticales, isothermes horizontales, isobares exponentielles décalées horizontalement, la plus haute pression à gauche.
- Travail d'un compresseur réversible : $\int v\,\mathrm{d}P$, aire entre la courbe et l'axe des pressions.

**Points de vigilance.**

- $w_{net}$ est un travail récupéré : il est l'opposé de la somme des travaux reçus par l'air.
- Le rendement du cycle de Joule fait intervenir $T_2$, pas $T_3$ : ce n'est pas le rendement de Carnot.
- Rendement maximal et travail maximal ne sont pas obtenus pour le même taux de compression.
- Dans le rendement de l'installation à régénérateur, la chaleur échangée dans le régénérateur ne compte pas, mais celle du réchauffement entre les turbines compte.
- Masse molaire en $\mathrm{kg\cdot mol^{-1}}$, unités à chaque résultat numérique.
