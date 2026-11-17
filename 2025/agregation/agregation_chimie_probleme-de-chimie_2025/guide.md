# Agrégation Chimie — Problème de chimie 2025 · Corrigé guidé

*Corrigé rédigé par IA, non officiel. Signalez toute erreur.*

## Présentation du sujet

**Thème.** « Membranes à perméabilité sélective » : le sujet parcourt la physico-chimie des membranes sélectives, de la fabrication des matériaux (Nylon 6-10 par polymérisation interfaciale, polymères à microporosité intrinsèque à base de Tröger) à une application industrielle (l'électrodialyse), en passant par la thermodynamique des ionomères (potentiel de Donnan) et le transport ionique sous champ. Trois registres sont mobilisés : chimie organique et macromoléculaire, physico-chimie des solutions ioniques, génie des procédés. Épreuve de 6 heures, calculatrice autorisée, 74 questions en quatre parties.

**Découpage.**

| Partie | Questions | Contenu | Notions du programme mobilisées |
|---|---|---|---|
| I | Q1–Q41 | Nylon 6-10, cinétique de polymérisation interfaciale (Q1–Q21) ; polymère à microporosité intrinsèque : RMN, GPC, ATG, stéréochimie de la base de Tröger, synthèse de la diamine (Q22–Q41) | polycondensation, mésomérie, loi de Fick, équation différentielle linéaire, osmose, RMN $^1$H, Diels-Alder, stéréochimie (CIP, énantiomérie), mécanismes (SEAr, organomagnésiens, nitration) |
| II | Q42–Q53 | Nafion : ionisation, potentiel de Donnan, permsélectivité | acide fort, potentiel électrochimique, équilibre de Donnan, électroneutralité |
| III | Q54–Q59 | Conducteurs ioniques : flux de diffusion, osmotique, de migration, nombres de transport | loi de Nernst-Einstein, mobilité, Stokes-Einstein |
| IV | Q60–Q74 | Électrodialyse : diluat/concentrat, polarisation, courant limite, dimensionnement | électrolyse, bilan de matière de réacteurs ouverts, rendement faradique |

**Difficulté et longueur.** Sujet long (74 questions) mais très balisé : les 20 questions fondamentales (marquées *) sont des restitutions directes à sécuriser en priorité. Les blocs calculatoires les plus denses sont la cinétique de croissance Q8–Q20 (équation différentielle, coquille de l'énoncé en Q18), le bloc Donnan Q46–Q52 et le dimensionnement Q71–Q74. Le rapport du jury 2025 relève les questions les plus discriminantes : Q8, Q14–Q19, Q36–Q37, Q46–Q50, Q61–Q70.

**Ce qu'en dit le rapport 2025.** 275 candidats, moyenne des admissibles 8,85/20 et des admis 10,55/20. « 20 questions fondamentales sur les 74 du sujet » représentaient « 25 % du total des points », avec un taux moyen de réussite d'environ 40 % sur ces questions contre 25 % pour l'ensemble. « 5 % du total des points de la copie ont été attribués à la présentation, à la qualité de la rédaction » : soigner notations, schémas et commentaires critiques. Deux coquilles de l'énoncé (Q15 : la masse volumique de l'eau figurait implicitement dans la formule ; Q18 : facteur 2 manquant dans l'exponentielle) ont été neutralisées : le barème a été ajusté « de manière à valoriser en priorité la qualité du raisonnement des candidats », et « Le Jury accueille avec bienveillance toute forme de regard critique émanant des candidats à l'égard du contenu de l'énoncé de l'épreuve. »

**Gestion du temps.** Les quatre parties sont indépendantes. Une répartition raisonnable est d'environ 2 h pour la partie I (dont le bloc cinétique Q8–Q20 enchaîné), 1 h 15 pour la partie II, 45 min pour la partie III, 1 h 30 pour la partie IV. Dans la partie I, les questions Q9 → Q10 → Q13 → Q17 → Q18 → Q19 s'enchaînent : retenir les résultats intermédiaires pour pouvoir repartir en cas de blocage.

---

## Partie I — Fabrication d'un matériau quasi bidimensionnel

La partie I construit d'abord un modèle cinétique de la polymérisation interfaciale du Nylon 6-10 (Q1–Q21 : nomenclature, liaisons faibles, bilan volumique, loi de Fick, équation différentielle de croissance et sa correction par une réaction parasite), puis étudie un polymère à microporosité intrinsèque (Q22–Q41 : spectre RMN, masses molaires, stéréochimie de la base de Tröger, rétrosynthèse et synthèse de la diamine). Les outils principaux sont la mésomérie, la loi de Fick et les bilans de matière.

### Question 1*

> [!INDICATION]
> Décoder la convention « Nylon $a$-$b$ » à partir des deux monomères nommés dans l'énoncé.

> [!INDICATION]
> Compter les atomes de carbone de chaque monomère : lequel est la diamine, lequel est le diacide (ou son dichlorure) ?

#### Solution

Dans la nomenclature « Nylon $a$-$b$ » de Dupont-de-Nemours, $a$ est le nombre d'atomes de carbone de la **diamine** et $b$ celui du **diacide** (ou de son dichlorure). L'hexaméthylènediamine $\mathrm{H_2N-(CH_2)_6-NH_2}$ apporte 6 carbones, le chlorure de sébacoyle (dichlorure de l'acide décanedioïque) $\mathrm{ClOC-(CH_2)_8-COCl}$ en apporte 10 :

$$
\boxed{\text{Nylon 6-10 : 6 carbones de diamine, 10 carbones de diacide}}
$$

> [!PIEGE]
> Ne pas inverser les deux nombres, et ne pas oublier de compter les deux carbonyles dans les 10 carbones du diacide.

### Question 2*

> [!INDICATION]
> Ne pas appliquer VSEPR mécaniquement à l'azote : chercher une forme mésomère du groupe amide.

> [!INDICATION]
> Quelle conséquence une double liaison partielle C–N a-t-elle sur la géométrie et sur la rotation autour de C–N ?

#### Solution

Le groupe amide $-\mathrm{C(=O)-N}<$ possède une forme mésomère dans laquelle le doublet de l'azote se délocalise sur l'oxygène :

$$
\mathrm{-C(=O)-N< \;\longleftrightarrow\; -C(-O^{-})=N^{+}<}\;.
$$

La liaison C–N acquiert un **caractère partiel de double liaison** : l'azote est de type $sp^2$ et les six atomes (C, O, N et leurs trois substituants) sont **coplanaires**. La rotation autour de C–N est bloquée. Une description VSEPR isolée conduirait à tort à un azote pyramidal.

$$
\boxed{\text{Le groupe amide est plan, la rotation C--N est bloquée}}
$$

> [!JURY]
> Le rapport 2025 rappelle que « le groupe amide est plan, ce qui est un résultat expérimental avéré », et déplore l'« approche de type VSEPR » qui « aboutissait à une structure incorrecte, où l'azote était représenté comme pyramidal ».

### Question 3*

> [!INDICATION]
> Comparer la réactivité d'un acide carboxylique et d'un chlorure d'acyle vis-à-vis d'une amine à température ambiante.

> [!INDICATION]
> Quelle réaction acide-base parasite se produit entre un acide et une amine, et quel groupe partant rend le chlorure d'acyle réactif ?

#### Solution

Un acide carboxylique et une amine réagissent à température ambiante par une **réaction acide-base de salification**, qui forme un carboxylate d'ammonium et **bloque toute autre transformation**. Le chlorure d'acyle, beaucoup plus électrophile ($\mathrm{Cl^-}$ est un bon groupe partant), subit l'attaque nucléophile de l'amine de façon rapide et irréversible dès la température ambiante : c'est lui qui permet la polycondensation interfaciale.

> [!JURY]
> « La réaction de salification entre un acide et une amine, qui à température ambiante bloque toute autre transformation, est largement méconnue. »

### Question 4*

> [!INDICATION]
> L'énoncé oriente le choix sur la facilité de traitement des sous-produits : chercher un réactif de chloration dont les sous-produits sont gazeux.

#### Solution

Le **chlorure de thionyle** $\mathrm{SOCl_2}$ convient :

$$
\mathrm{R-COOH + SOCl_2 \rightarrow R-COCl + SO_2\!\uparrow + HCl\!\uparrow}\;.
$$

Les sous-produits $\mathrm{SO_2}$ et $\mathrm{HCl}$ étant gazeux, ils s'éliminent spontanément du milieu réactionnel, ce qui rend le traitement très simple.

### Question 5*

> [!INDICATION]
> Écrire l'unité répétitive à partir des deux monomères, en retirant ce qui est éliminé à chaque liaison amide.

> [!INDICATION]
> Combien de fonctions amide comporte le motif, et donc combien de molécules d'eau (ou HCl) sont éliminées au total ?

#### Solution

L'unité répétitive est le motif

$$
\mathrm{\big[-NH-(CH_2)_6-NH-CO-(CH_2)_8-CO-\big]}\;,
$$

de formule brute $\mathrm{C_{16}H_{30}N_2O_2}$ (deux fonctions amide par motif, donc deux HCl éliminés par motif lors de la polycondensation avec le dichlorure d’acyle). D'où

$$
M = 16(12{,}01) + 30(1{,}008) + 2(14{,}01) + 2(16{,}00) \approx \boxed{282\ \mathrm{g\cdot mol^{-1}}}\;.
$$

### Question 6*

> [!INDICATION]
> Quel groupe polaire du motif peut interagir avec un autre motif de façon inter- ou intramoléculaire ?

#### Solution

Les motifs s'associent par **liaisons hydrogène** entre le $\mathrm{N-H}$ d'un groupe amide (donneur) et l'oxygène du carbonyle $\mathrm{C=O}$ d'un autre motif (accepteur) :

$$
\mathrm{N-H\cdots O=C}\;.
$$

### Question 7*

> [!INDICATION]
> De quelle famille de macromolécules naturelles la laine et la soie sont-elles des exemples ?

#### Solution

La laine et la soie sont des **protéines**, donc des **polyamides naturels** : leurs liaisons peptidiques $-\mathrm{CO-NH}-$ sont les mêmes fonctions amide que celles du Nylon, avec le même réseau de liaisons hydrogène inter-chaînes. Les propriétés mécaniques des fibres (résistance, souplesse) sont donc analogues, ce qui permet au Nylon de se substituer à ces fibres textiles.

> [!JURY]
> « Une majorité de candidats ignore que la laine et la soie sont des protéines, et qu'à ce titre, elles présentent une structure proche de celle des polyamides. »

### Question 8*

> [!INDICATION]
> Procéder par volumes : masse sèche → volume de polymère → volume de membrane fraîche → épaisseur.

> [!INDICATION]
> La membrane fraîche ne contient que 10 % de polymère en volume : quel facteur relie le volume de polymère au volume total de la membrane humide ?

#### Solution

Après dessiccation, la membrane sèche a une masse $m = 40\ \mathrm{mg} = 0{,}040\ \mathrm{g}$, d'où un volume de polymère

$$
\begin{aligned}
V_{\text{pol}} &= \frac{m}{\rho} \\
&= \frac{0{,}040}{1{,}08} \\
&= 3{,}70\times10^{-2}\ \mathrm{cm^3}
\end{aligned}
$$

Le polymère ne représente que $(1-w) = 10\ \%$ du volume de la membrane fraîche, donc

$$
\begin{aligned}
V_{\text{memb}} &= \frac{V_{\text{pol}}}{1-w} \\
&= \frac{3{,}70\times10^{-2}}{0{,}10} \\
&= 0{,}370\ \mathrm{cm^3}
\end{aligned}
$$

La surface du disque de diamètre $10\ \mathrm{cm}$ vaut $S = \pi (5)^2 = 78{,}5\ \mathrm{cm^2}$, d'où l'épaisseur de la membrane fraîche :

$$
\begin{aligned}
x &= \frac{V_{\text{memb}}}{S} = \frac{0{,}370}{78{,}5} \\
&= 4{,}7\times10^{-3}\ \mathrm{cm} \approx \boxed{47\ \mu\mathrm{m}}
\end{aligned}
$$

> [!PIEGE]
> L'erreur classique est d'oublier le facteur $1/(1-w)$ : on ne divise pas le volume de polymère par $w$, on le rapporte à la fraction de polymère $(1-w) = 10\ \%$.

> [!JURY]
> « Le jury a été particulièrement surpris par la difficulté rencontrée par les candidats à résoudre une question pourtant classique de physico-chimie : le calcul de l'épaisseur d'une membrane humide à partir de sa surface, en sachant qu'elle est constituée à 10% en volume de matière sèche. »

### Question 9

> [!INDICATION]
> Relier la quantité de matière de motifs $n$ au volume de polymère, puis à la fraction $(1-w)$ du volume de membrane.

#### Solution

La masse de polymère contenue dans la membrane vaut $nM$ ; son volume $nM/\rho$ est la fraction $(1-w)$ du volume $Sx$ de la membrane fraîche :

$$
\frac{nM}{\rho} = (1-w)\,S\,x
$$

$$
\boxed{x = \frac{nM}{\rho(1-w)S}}
$$

### Question 10

> [!INDICATION]
> Dériver la relation de la question 9 par rapport au temps : quelles grandeurs sont constantes ?

#### Solution

Par dérivation par rapport au temps, $S$, $M$, $\rho$ et $w$ étant constants :

$$
\begin{aligned}
\frac{\mathrm{d}n}{\mathrm{d}t} &= \frac{\rho(1-w)S}{M}\,\frac{\mathrm{d}x}{\mathrm{d}t} \\
\frac{\mathrm{d}x}{\mathrm{d}t} &= \frac{M}{\rho(1-w)S}\,\frac{\mathrm{d}n}{\mathrm{d}t}
\end{aligned}
$$

$\mathrm{d}n/\mathrm{d}t$ est la vitesse de formation des motifs, c'est-à-dire la cinétique de la réaction de polymérisation.

### Question 11

> [!INDICATION]
> La réaction est totale et limitée par la diffusion : que vaut la concentration de diamine au point où elle est consommée instantanément ?

> [!INDICATION]
> Quelles sont les concentrations du chlorure d'acyle dans chaque phase (l'énoncé les suppose homogènes hors membrane) ?

#### Solution

La réaction étant totale et limitée par la diffusion, toute diamine atteignant l'interface réactive y est instantanément consommée : **$C_A = 0$ à l'interface**. Le profil de diamine est linéaire dans la membrane, de $C_A$ (côté aqueux) à $0$ (interface réactive). Le chlorure d'acyle reste à sa concentration $C_C$ homogène dans la phase organique et ne pénètre pas dans la membrane ($C_C = 0$ dans la membrane et dans la phase aqueuse).

```text
C
↑
C_A ┤╲
    │  ╲  diamine A (linéaire, nulle à l'interface réactive)
  0 ┼───╲──────────→ x
    0   x  interface réactive (phase organique, C_C constant au-delà)
```

### Question 12

> [!INDICATION]
> Appliquer la loi de Fick au profil linéaire établi en question 11.

#### Solution

Loi de Fick : $J = -D\,\mathrm{d}C/\mathrm{d}x$. Le gradient linéaire vaut, sur l'épaisseur $x$ de la membrane,

$$
\frac{\mathrm{d}C_A}{\mathrm{d}x} = \frac{C_A - 0}{x} = \frac{C_A}{x}\;,
$$

d'où

$$
\boxed{J = -D\,\frac{C_A}{x}}\;.
$$

### Question 13

> [!INDICATION]
> Écrire que toute la diamine arrivant à l'interface est convertie en motifs, puis mobiliser la question 10.

#### Solution

Toute la diamine arrivant à l'interface est convertie en polymère : $\mathrm{d}n/\mathrm{d}t = |J|\,S = \dfrac{D\,C_A}{x}\,S$. En reportant dans la question 10 :

$$
\boxed{\frac{\mathrm{d}x}{\mathrm{d}t} = \frac{M\,D\,C_A}{\rho(1-w)\,x}}\;.
$$

### Question 14

> [!INDICATION]
> Intégrer l'équation différentielle de la question 13 (séparer les variables).

> [!INDICATION]
> Confronter la loi de croissance obtenue à l'observation expérimentale : l'épaisseur se stabilise-t-elle ?

#### Solution

En posant $a = \dfrac{M D C_A}{\rho(1-w)}$, l'équation $\mathrm{d}x/\mathrm{d}t = a/x$ s'intègre en $x\,\mathrm{d}x = a\,\mathrm{d}t$, soit

$$
\frac{x^2}{2} = a\,t
$$

$$
x = \sqrt{\frac{2\,M\,C_A\,D}{(1-w)\,\rho}\,t}
$$

Cette loi en $\sqrt{t}$ **croît indéfiniment** : la membrane ne cesserait jamais de s'épaissir. Or l'expérience montre une épaisseur qui **se stabilise** après quelques minutes : la solution proposée **n'est pas compatible** avec l'observation expérimentale.

> [!METHODE]
> Face à une équation différentielle autonome en $x$, penser d'abord à la séparation des variables ($x\,\mathrm{d}x = a\,\mathrm{d}t$), et toujours confronter la loi trouvée à l'observation expérimentale.

### Question 15

> [!INDICATION]
> Exprimer le volume d'eau par unité de surface dans une tranche d'épaisseur $x$, puis convertir en moles.

> [!INDICATION]
> Quelle masse volumique intervient dans la conversion en moles : celle du polymère ou celle de l'eau ?

#### Solution

Par unité de surface, le volume de membrane fraîche vaut $x$ ; l'eau en occupe la fraction volumique $w$, soit un volume $wx$. Avec la masse volumique de l'eau $\rho_{\text{eau}} \simeq 1\ \mathrm{g\cdot cm^{-3}}$ et $M_{\text{eau}} = 18\ \mathrm{g\cdot mol^{-1}}$ :

$$
\boxed{\Gamma_{\mathrm{H_2O}} = \frac{w\,\rho_{\text{eau}}\,x}{18}}\;.
$$

Dans la formule de l'énoncé, le symbole $\rho$ désigne la masse volumique de **l'eau** (et non celle du polymère) : $x$ en dm et $\rho_{\text{eau}}$ en $\mathrm{g\cdot dm^{-3}}$ donnent bien $\Gamma_{\mathrm{H_2O}}$ en $\mathrm{mol\cdot dm^{-2}}$.

> [!JURY]
> « Quelques candidats ont correctement identifié que la masse volumique de l'eau figurait implicitement dans la formule donnée à la question 15 » : signaler cette lecture critique de l'énoncé rapporte des points.

### Question 16

> [!INDICATION]
> Écrire la loi de vitesse de l'hydrolyse avec des ordres partiels égaux à 1, en notant $k$ la constante apparente.

> [!INDICATION]
> $\Gamma_C$ est constante : exprimer la vitesse en fonction de $x$ grâce à la question 15.

#### Solution

L'hydrolyse du chlorure d'acyle par l'eau, d'ordres partiels égaux à 1, a pour vitesse surfacique

$$
v_{\text{hyd}} = k\,\Gamma_C\,\Gamma_{\mathrm{H_2O}}\;.
$$

$\Gamma_C$ étant constante et $\Gamma_{\mathrm{H_2O}} = \dfrac{w\rho_{\text{eau}}}{18}\,x$ (question 15) :

$$
\boxed{v_{\text{hyd}} = k\,\Gamma_C\,\frac{w\,\rho_{\text{eau}}}{18}\,x \;\propto\; x}\;.
$$

### Question 17

> [!INDICATION]
> Faire le bilan de matière sur la diamine, par unité de surface : le flux qui arrive se partage entre la croissance de la membrane et la réaction parasite.

> [!INDICATION]
> Identifier les deux termes du bilan grâce aux questions 10 et 16, puis mettre sous la forme $\mathrm{d}x/\mathrm{d}t = a/x - bx$.

#### Solution

Bilan de matière sur la diamine, par unité de surface : le flux arrivant $|J| = D C_A/x$ alimente la croissance de la membrane et est consommé par la réaction parasite (l'HCl produit neutralise la diamine) :

$$
\frac{D\,C_A}{x} = \frac{\rho(1-w)}{M}\,\frac{\mathrm{d}x}{\mathrm{d}t} + k\,\Gamma_C\,\frac{w\,\rho_{\text{eau}}}{18}\,x\;.
$$

D'où

$$
\boxed{\frac{\mathrm{d}x}{\mathrm{d}t} = \frac{a}{x} - b\,x}\;,
$$

avec

$$
\boxed{a = \frac{M\,D\,C_A}{\rho(1-w)}}
$$

$$
\boxed{b = \frac{M\,k\,\Gamma_C\,w\,\rho_{\text{eau}}}{18\,\rho(1-w)}}
$$

### Question 18

> [!INDICATION]
> Le changement de variable $Y = x^2$ linéarise l'équation : poser $Y = x^2$ et exprimer $\mathrm{d}Y/\mathrm{d}t$ en fonction de $Y$.

> [!INDICATION]
> Résoudre l'équation linéaire obtenue, puis vérifier la cohérence avec la solution proposée par l'énoncé (facteur 2 dans l'exponentielle ?).

#### Solution

Avec le changement de variable $Y = x^2$ : $\dfrac{\mathrm{d}Y}{\mathrm{d}t} = 2x\,\dfrac{\mathrm{d}x}{\mathrm{d}t} = 2a - 2b\,Y$. L'équation linéaire $\mathrm{d}Y/\mathrm{d}t + 2bY = 2a$, avec $Y(0) = 0$, a pour solution $Y = \dfrac{a}{b}\big(1 - e^{-2bt}\big)$, soit

$$
\boxed{x(t) = \sqrt{\frac{a}{b}\big(1 - e^{-2bt}\big)}}\;.
$$

**Coquille de l'énoncé signalée** : la formule proposée $x(t) = \sqrt{a/b}\,(1-e^{-bt})$ est incorrecte (il manque le facteur 2 dans l'argument de l'exponentielle, et la racine doit porter sur tout le trinôme) ; on le vérifie en reportant la solution correcte dans $\mathrm{d}x/\mathrm{d}t = a/x - bx$.

> [!JURY]
> « L'erreur portait sur l'absence d'un facteur 2 dans l'argument de l'exponentielle » ; « Le jury a particulièrement apprécié les candidats ayant signalé leurs doutes sur l'énoncé ».

### Question 19

> [!INDICATION]
> Passer à la limite $t \to \infty$ dans la solution de la question 18.

> [!INDICATION]
> Simplifier $a/b$ littéralement : quels facteurs se compensent entre $a$ et $b$ ?

#### Solution

À la limite $t \to \infty$, $e^{-2bt} \to 0$, donc l'épaisseur finale vaut

$$
\boxed{x_m = \sqrt{\frac{a}{b}} = \sqrt{\frac{18\,D\,C_A}{k\,\Gamma_C\,w\,\rho_{\text{eau}}}}}\;.
$$

En effet $a/b = \dfrac{M D C_A}{\rho(1-w)} \cdot \dfrac{18\rho(1-w)}{M k \Gamma_C w \rho_{\text{eau}}} = \dfrac{18 D C_A}{k \Gamma_C w \rho_{\text{eau}}}$ : la masse molaire $M$ et la masse volumique du polymère $\rho$ se simplifient. La croissance est désormais **auto-limitée** : $x \to x_m$ fini, ce qui corrige le défaut du modèle de la question 14.

> [!PIEGE]
> Dans le rapport $a/b$, les facteurs $M$, $\rho$ et $(1-w)$ se compensent : ne pas garder de $\rho$ parasite au dénominateur.

### Question 20

> [!INDICATION]
> Exprimer $x' = x/x_m$ avec la solution de la question 18 : quelle allure de courbe obtient-on ?

> [!INDICATION]
> Cette courbe normalisée dépend-elle de $C_A$ ? Comparer à la superposition des points expérimentaux de la figure 3.

#### Solution

Le modèle prévoit

$$
x' = \frac{x}{x_m} = \sqrt{1 - e^{-2bt}}\;,
$$

fonction croissante de $t$ tendant vers **1** : il apparaît un **plateau**, conforme à la figure 3. De plus, comme $b$ ne dépend pas de $C_A$, la courbe normalisée est **indépendante de $C_A$** : les jeux de points obtenus pour les différentes concentrations se superposent sur une courbe maîtresse unique, exactement ce que montre la figure 3. Les hypothèses du modèle (régime stationnaire, gradient linéaire, $\Gamma_C$ constante, réaction parasite) sont donc qualitativement validées.

### Question 21

> [!INDICATION]
> La membrane est semi-perméable à l'eau et contient des solutés : quel phénomène de transport d'eau explique le gonflement dans l'eau distillée et la contraction dans l'eau salée ?

#### Solution

Le phénomène est l'**osmose**. Dans l'**eau distillée**, l'activité de l'eau extérieure est maximale : l'eau entre par osmose, la membrane **gonfle** (son diamètre augmente). Dans l'**eau salée** à $0{,}1\ \mathrm{mol\cdot dm^{-3}}$, l'activité de l'eau extérieure est abaissée : l'eau sort, la membrane se **contracte**. L'alternance des bains explique les variations réversibles de diamètre observées sur la figure 4.

> [!JURY]
> Le jury a regretté que « le phénomène d'osmose (qui explique les variations de dimensions de la membrane en fonction de la salinité, question 21) n'ait pratiquement jamais été identifié » : nommer explicitement l'osmose.

### Question 22*

> [!INDICATION]
> Dans un polymère, un même type de proton existe-t-il dans un environnement unique ?

> [!INDICATION]
> La mobilité des segments de chaîne est-elle élevée en dessous de la température de transition vitreuse ?

#### Solution

Dans un polymère, chaque type de proton occupe une **distribution d'environnements chimiques** légèrement différents (longueur de chaîne, configurations, bouts de chaîne), et la **mobilité réduite** des segments de chaîne limite le moyennage par relaxation. Il en résulte une distribution de déplacements chimiques, donc un **élargissement de tous les signaux**.

> [!JURY]
> Le rapport déplore une « interprétation fantaisiste de l'élargissement des signaux pour un spectre de polymère (mis en cause : le solvant CDCl3, le grand nombre d'hydrogènes de la macromolécule, la mésomérie/délocalisation électronique, la qualité du spectromètre utilisé, …) » : l'argument correct est la distribution d'environnements et la mobilité réduite des chaînes.

### Question 23

> [!INDICATION]
> Combiner intégrations et déplacements chimiques usuels : aromatiques, $\mathrm{CH_2}$ liés à N, $\mathrm{CH_3}$, pont éthano.

> [!INDICATION]
> Vérifier la cohérence : la somme des intégrations doit correspondre au nombre total de H du motif.

#### Solution

Attribution des signaux du spectre $^1\mathrm{H}$-RMN du motif répétitif (20 H au total) :

| $\delta$ (ppm) | Multiplicité | Intégration | Attribution |
|---|---|---|---|
| 7,28 | m | 4H | H aromatiques |
| 4,57 | s | 2H | pont $\mathrm{N-CH_2-N}$ de la base de Tröger |
| 4,05 | s | 4H | 2 × $\mathrm{Ar-CH_2-N}$ de la base de Tröger |
| 1,81 | m | 6H | 2 × $\mathrm{CH_3}$ en positions 9 et 10 |
| 1,65 | m | 4H | pont éthano $-\mathrm{CH_2-CH_2}-$ |

> [!JURY]
> Le rapport relève une attribution « parfois chaotique » : « méthylène non recopié, hydrogènes surnuméraires, non reconnaissance des hydrogènes équivalents, méconnaissance des déplacements chimiques usuels (aromatiques vs aliphatique) ». Les deux singulets des méthylènes azotés (4,57 et 4,05 ppm) sont discriminants.

### Question 24*

> [!INDICATION]
> Déduire la formule brute du motif à partir de l'attribution RMN (nombre de H) et de la structure (nombre de C et N).

> [!INDICATION]
> Quels carbones du motif proviennent du méthanal (question 32) ?

#### Solution

Le motif réunit le motif 9,10-diméthyl-9,10-éthanoanthracène (14 C du squelette anthracène, 2 C des méthyles, 2 C du pont éthano) et les **3 carbones apportés par le méthanal** de la base de Tröger (question 32), avec 2 N et 20 H (cohérent avec les intégrations de la question 23) :

$$
\mathrm{C_{21}H_{20}N_2}\;.
$$

$$
M = 21(12{,}01) + 20(1{,}008) + 2(14{,}01) = \boxed{300\ \mathrm{g\cdot mol^{-1}}}\;.
$$

### Question 25

> [!INDICATION]
> Le degré de polymérisation moyen en nombre se calcule avec quelle masse molaire moyenne, $M_n$ ou $M_w$ ?

#### Solution

Degré de polymérisation moyen en nombre :

$$
DP = \frac{M_n}{M} = \frac{40\,700}{300} \approx \boxed{136}\;.
$$

La dispersité Đ vaut $\dfrac{M_w}{M_n} = \dfrac{155\,800}{40\,700} \approx 3{,}8$.

> [!PIEGE]
> Ne pas utiliser $M_w$ pour le $DP$ en nombre : c'est $M_n$ qui compte.

### Question 26

> [!INDICATION]
> Le chauffage du motif 9,10-éthanoanthracène casse quelle réaction péricyclique à l'envers ?

> [!INDICATION]
> Quelle petite molécule est libérée, et quelle force motrice (aromatisation) conduit la réaction vers 260 °C ?

#### Solution

Au chauffage vers 260 °C, le pont éthano du motif 9,10-éthanoanthracène subit une **rétro-Diels-Alder** : le pont bicyclo[2.2.2] se fragmente en libérant de l'**éthylène** $\mathrm{CH_2=CH_2}$ et en restaurant l'aromaticité du noyau anthracène. La réaromatisation, très exergonique, est la force motrice de la réaction ; la température de l'analyse thermogravimétrique fournit l'énergie d'activation.

> [!JURY]
> La réaction de thermolyse « a très rarement été identifiée comme une rétro-Diels-Alder (avec départ d'éthylène) » : hors du contexte classique de la Diels-Alder entre l'anthracène et un diénophile, le motif 9,10-éthanoanthracène est mal connu.

### Question 27

> [!INDICATION]
> Relier la perte de masse à l'élimination d'une molécule d'éthylène par motif.

#### Solution

Chaque motif ($M = 300\ \mathrm{g\cdot mol^{-1}}$) perd une molécule d'éthylène ($M = 28\ \mathrm{g\cdot mol^{-1}}$) par rétro-Diels-Alder totale :

$$
\frac{\Delta m}{m} = \frac{28}{300} = 9{,}3\ \% \approx \boxed{10\ \%}\;,
$$

en accord avec l'analyse thermogravimétrique.

### Question 28

> [!INDICATION]
> Représenter le dibenzobicyclo[2.2.2]octane en perspective cavalière : quelles têtes de pont portent les méthyles, et quels ponts sont aromatiques ?

> [!INDICATION]
> Chercher les éléments de symétrie de la molécule pour conclure sur la chiralité et les centres stéréogènes.

#### Solution

Le motif 9,10-éthanoanthracène est le dibenzobicyclo[2.2.2]octane : deux têtes de pont $sp^3$ (C9 et C10) portant chacune un $\mathrm{CH_3}$, réunies par deux ponts ortho-phénylène et un pont $-\mathrm{CH_2-CH_2}-$ ; les substituants R occupent les positions 2 et 6 (ou 2 et 7) des noyaux aromatiques. En perspective cavalière, les deux noyaux benzéniques sont quasi parallèles et le pont éthano ferme le bicyclo[2.2.2]octane (qui **ne peut pas exister en conformation chaise**). La molécule possède des plans de symétrie : elle est **achirale** et ne comporte **aucun centre stéréogène**.

```text
        CH3
         |
    ┌────C9────┐      C9, C10 : têtes de pont sp3
   /│    ││    │\     pont éthano : C9–CH2–CH2–C10
  │ └──┬─┘──┬─┘ │    deux ponts = noyaux benzéniques (R en 2,6 / 2,7)
  │    C10  │  │
  └────┼────┘  │
       CH3    │
```

> [!JURY]
> Le rapport invite à soigner ces représentations : « Un noyau benzénique n'est pas un cyclohexane ; […] le bicyclo[2,2,2]octane ne peut pas exister en conformation chaise ».

### Question 29*

> [!INDICATION]
> Représenter la base de Tröger et son image dans un miroir : sont-elles superposables ?

> [!INDICATION]
> Les deux atomes d'azote têtes de pont sont configurationnellement stables : quelles combinaisons de configurations la rigidité du pont autorise-t-elle ?

#### Solution

Les deux atomes d'azote « têtes de pont » de la base de Tröger sont configurationnellement stables, mais leurs configurations sont **couplées** par la rigidité du pont : seules les combinaisons $(R,R)$ et $(S,S)$ sont géométriquement possibles (la forme « méso » $(R,S)$ est impossible). L'image dans un miroir n'est pas superposable à la molécule. Il existe donc

$$
\boxed{2\ \text{stéréo-isomères, énantiomères l'un de l'autre}}
$$

> [!JURY]
> « Le jury recommande FORTEMENT aux candidats de manipuler des modèles moléculaires et d'en réaliser des “dessins d'après nature”. »

### Question 30*

> [!INDICATION]
> Recenser les rotations propres et les éventuels éléments de symétrie impropres (plan miroir, centre d’inversion, rotation-réflexion) de la base de Tröger.

> [!INDICATION]
> Quels atomes portent une configuration absolue stable ? Proposer les descripteurs CIP des deux configurations possibles.

#### Solution

La base de Tröger possède un **axe de symétrie $C_2$**, mais **ni plan de symétrie ni centre d'inversion** : elle est **chirale**. Les **centres stéréogènes sont les deux atomes d'azote**, chacun de configuration absolue fixée ; on les repère par les descripteurs CIP, qui donnent le couple $(R,R)$ et son énantiomère $(S,S)$ (par exemple $(5R,11R)$ et $(5S,11S)$).

### Question 31

> [!INDICATION]
> Sans contrôle stéréochimique, chaque jonction de Tröger adopte quelle configuration, au hasard ?

> [!INDICATION]
> Quelle conséquence ce désordre configurationnel a-t-il sur l'empilement des chaînes et sur la porosité ?

#### Solution

Aucun contrôle stéréochimique n'étant exercé pendant la polymérisation, chaque jonction de Tröger se forme indifféremment en $(R,R)$ ou $(S,S)$ : la macromolécule est une **succession aléatoire de coudes de chiralités opposées**, irrégulière et contorsionnée, sans ordre à longue distance. Les chaînes ne peuvent pas s'empiler de façon compacte, ce qui crée le **volume libre** responsable de la microporosité intrinsèque.

### Question 32

> [!INDICATION]
> Sur la structure de la base de Tröger, entourer les carbones qui n'appartiennent pas au squelette de la diamine 1.

#### Solution

Dans le motif Tröger, les atomes de carbone qui **ne proviennent pas de la diamine 1** sont les **trois méthylènes** : le pont central $\mathrm{N-CH_2-N}$ et les deux ponts $\mathrm{Ar-CH_2-N}$.

### Question 33

> [!INDICATION]
> Quelles fonctions organiques relient ces trois méthylènes aux azotes (aminal, liaison de type Mannich) ?

> [!INDICATION]
> Par quelles disconnections rétrosynthétiques (hydrolyse rétro) faire apparaître le méthanal ?

#### Solution

Ces trois méthylènes forment des **aminals** ($\mathrm{N-CH_2-N}$) et des liaisons de type Mannich ($\mathrm{Ar-CH_2-N}$). Leur disconnexion rétrosynthétique (hydrolyse rétro) régénère les deux fonctions amine aromatiques et **trois équivalents de méthanal** :

$$
\text{base de Tröger} \;\Longrightarrow\; 2\ \mathrm{Ar-NH_2} + 3\ \mathrm{H_2CO}\;.
$$

> [!JURY]
> Le rapport note que « les candidats ne justifient pas assez leurs choix mécanistiques (y compris lors de la rétro-synthèse de la base de Tröger), et les noms des mécanismes (SN1, SN2, SEAr, etc.) sont rarement mentionnés ».

### Question 34

> [!INDICATION]
> En milieu acide, que devient le diméthoxyméthane après protonation et perte d'un méthanol ?

> [!INDICATION]
> Comparer l'ion obtenu à celui formé par protonation du méthanal.

#### Solution

En milieu acide (acide trifluoroéthanoïque), le diméthoxyméthane $\mathrm{CH_2(OMe)_2}$ est protoné puis perd un méthanol pour engendrer l'**ion oxocarbénium** $\mathrm{[CH_2=O^{+}Me \leftrightarrow {}^{+}CH_2-OMe]}$, électrophile en carbone. Cet ion est strictement équivalent au cation méthylèneoxonium obtenu par protonation du méthanal $\mathrm{H_2C=O}$ : le diméthoxyméthane est donc un **équivalent synthétique du méthanal**, plus commode à manipuler (liquide, anhydre).

### Question 35*

> [!INDICATION]
> Quel diol obtient-on par addition de 2 PhMgBr sur l'hexane-2,5-dione, et combien de stéréocentres comporte-t-il ?

> [!INDICATION]
> Les deux stéréocentres sont équivalents : penser au cas méso en plus de la paire d'énantiomères.

#### Solution

L'addition de 2 équivalents de $\mathrm{PhMgBr}$ sur l'hexane-2,5-dione donne le **2,5-diphénylhexane-2,5-diol**, qui porte deux stéréocentres équivalents (C2 et C5). On dénombre

$$
\boxed{3\ \text{stéréo-isomères}}
$$

: la paire d'énantiomères $(R,R)$ / $(S,S)$ et le composé **méso** $(R,S)$, qui possède un plan de symétrie interne.

> [!PIEGE]
> Ne pas conclure $2^2 = 4$ stéréo-isomères : avec deux centres équivalents, la forme $(R,S)$ est le composé méso, identique à $(S,R)$.

> [!JURY]
> Le rapport relève « un diol précurseur qui ne comportait que 3 stéréoisomères et non pas 2 ou $2^2$ ».

### Question 36

> [!INDICATION]
> Quel intermédiaire cationique un acide de Lewis (AlCl3) fait-il apparaître à partir d'un alcool ?

> [!INDICATION]
> Ce carbocation peut être attaqué par quoi, de façon intramoléculaire, et quelle réaction de cyclisation s'ensuit (deux fois) ?

#### Solution

Mécanisme de la réaction (ii), en deux étapes identiques :

1. $\mathrm{AlCl_3}$ (acide de Lewis) complexe un groupe $\mathrm{OH}$ ; la liaison C–O se rompt en libérant $\mathrm{[AlCl_3OH]^-}$ et un **carbocation tertiaire benzylique**, stabilisé par mésomérie ;
2. **substitution électrophile aromatique intramoléculaire** (type Friedel-Crafts) : un noyau phényle attaque le carbocation, puis réaromatisation par perte de $\mathrm{H^+}$ — première cyclisation.

Le second $\mathrm{OH}$ subit la même séquence (carbocation puis SEAr intramoléculaire) : seconde cyclisation. Le bilan est une **double déshydratation** conduisant au 9,10-diméthyl-9,10-éthanoanthracène (composé 3).

> [!JURY]
> « La possibilité d'aboutir à un carbocation tertiaire et benzylique transitoire est très/trop rarement envisagée, les candidats privilégiant des mécanismes sans intermédiaires réactionnels », et « Les mécanismes “tout en un”, trop succincts, sont à proscrire ».

### Question 37

> [!INDICATION]
> Après formation du carbocation, quel autre nucléophile intramoléculaire peut l'attaquer (autre que le noyau aromatique) ?

> [!INDICATION]
> Quel cycle se forme alors ?

#### Solution

Le sous-produit principal (éther cyclique) provient de l'attaque intramoléculaire de l'**oxygène du second hydroxyle** sur le carbocation tertiaire benzylique formé comme en question 36 : la fermeture du cycle donne le **2,5-diméthyl-2,5-diphényltétrahydrofurane** (cycle à 5 chaînons), après perte du proton.

### Question 38*

> [!INDICATION]
> Quelle espèce électrophile la réaction entre un nitrate et un anhydride d'acide génère-t-elle classiquement ?

#### Solution

$\mathrm{KNO_3}$ réagit avec l'anhydride trifluoroacétique $(\mathrm{CF_3CO})_2\mathrm{O}$ pour engendrer le **nitrate de trifluoroacétyle** :

$\mathrm{CF_3CO-O-NO_2}$, qui se dissocie en ion trifluoroacétate et en **ion nitronium** $\mathrm{NO_2^{+}}$ :

$$
\boxed{\mathrm{CF_3COONO_2 \rightarrow CF_3COO^{-} + NO_2^{+}}}\;.
$$

$\mathrm{NO_2^+}$ est l'électrophile effectif de la nitration.

### Question 39*

> [!INDICATION]
> La nitration passe par des espèces chargées ($\mathrm{NO_2^+}$, état de transition) : quel type de solvant les stabilise ?

#### Solution

L'acétonitrile est un solvant **polaire aprotique** : il solvate et stabilise les espèces ioniques ($\mathrm{NO_2^+}$ et l'état de transition chargé de la SEAr), ce qui favorise la génération et la réactivité du nitronium, tout en dissolvant les réactifs organiques.

### Question 40

> [!INDICATION]
> Les deux noyaux aromatiques réagissent indépendamment : combien de positions relatives des deux NO2 obtient-on au total ?

#### Solution

Les deux noyaux aromatiques de la molécule 3 réagissent **indépendamment** l'un de l'autre. Sur chaque noyau, la régiosélectivité est imposée par les effets électroniques des substituants (méthyle donneur $+I$, pont éthano), mais la position **relative** des deux groupes $\mathrm{NO_2}$ sur l'ensemble de la molécule peut être différente : le composé dinitré 4 est un **mélange de deux régioisomères** (non séparés), selon que les deux nitrations sont du même côté (syn) ou opposé (anti) de la molécule.

> [!JURY]
> Le rapport indique que les effets électroniques (+M ou −M, +I ou −I) ont été « sanctionnés lors de la discussion de la régiosélectivité lors de la nitration (question 40) » : justifier l'orientation par les effets électroniques, pas seulement par l'encombrement.

### Question 41

> [!INDICATION]
> La réduction d'un groupe nitro en amine se fait classiquement par hydrogénation catalytique ou en milieu acide réducteur : citer un équivalent de N2H4/Ni de Raney.

#### Solution

L'hydrate d'hydrazine sur nickel de Raney peut être remplacé par :

- une **hydrogénation catalytique** $\mathrm{H_2}$ sur $\mathrm{Pd/C}$ (ou $\mathrm{PtO_2}$) ;
- une réduction en milieu acide : $\mathrm{SnCl_2/HCl}$ ou $\mathrm{Fe/HCl}$.

Dans tous les cas, la fonction visée est la réduction de $\mathrm{NO_2}$ en $\mathrm{NH_2}$.

---

## Partie II — Résine échangeuse d'ions, potentiel de Donnan, rejet d'une espèce ionique

La partie II établit le potentiel de Donnan à l'interface entre une membrane ionomère (Nafion) et une solution saline, puis en déduit l'exclusion des co-ions (permsélectivité). Les outils sont le potentiel électrochimique, l'égalité des potentiels électrochimiques à l'équilibre et l'électroneutralité dans chaque phase ; le bloc Q46–Q50 est le cœur calculatoire, à mener avec rigueur.

### Question 42*

> [!INDICATION]
> Quelle est la force d'un acide sulfonique $\mathrm{SO_3H}$ (penser au pKa des acides sulfoniques usuels) ?

#### Solution

Les acides sulfoniques $\mathrm{SO_3H}$ sont des **acides forts** ($\mathrm pK_a \approx -1$ à $-2$) : sur toute la fenêtre $0 \le \mathrm{pH} \le 14$, les fonctions sont **totalement déprotonées** en sulfonate $\mathrm{SO_3^-}$. Le polymère est donc toujours ionisé (anionique) dans l'eau.

> [!JURY]
> « Très peu de candidats savaient que les acides sulfoniques sont des acides forts. »

### Question 43

> [!INDICATION]
> Une mole de SO3H pèse 1100 g de résine sèche ; convertir la masse volumique en concentration molaire.

> [!INDICATION]
> Soigner la conversion $\mathrm{cm^{-3}} \to \mathrm{L^{-1}}$.

#### Solution

Une mole de fonctions $\mathrm{SO_3H}$ correspond à $1100\ \mathrm{g}$ de résine sèche de masse volumique $1{,}98\ \mathrm{g\cdot cm^{-3}}$ :

$$
[\mathrm{SO_3^-}]_{\text{sec}} = \frac{1\ \mathrm{mol}}{1100\ \mathrm{g}} \times 1{,}98\ \mathrm{g\cdot cm^{-3}} = 1{,}8\times10^{-3}\ \mathrm{mol\cdot cm^{-3}} \approx \boxed{1{,}8\ \mathrm{mol\cdot L^{-1}}}\;.
$$

### Question 44

> [!INDICATION]
> La concentration cherchée est rapportée à l'eau absorbée par la membrane (16,5 % de la masse initiale), pas à la résine sèche.

> [!INDICATION]
> Pour 1100 g de résine sèche, quelle masse (puis quel volume) d'eau est absorbée ?

#### Solution

Pour 1 mol de $\mathrm{SO_3H}$ (1100 g de résine sèche), l'eau absorbée vaut $0{,}165 \times 1100 = 181{,}5\ \mathrm{g}$, soit $0{,}1815\ \mathrm{dm^3}$. La concentration en sulfonate rapportée à l'eau contenue dans la membrane gonflée est donc

$$
C_\Sigma = \frac{1\ \mathrm{mol}}{0{,}1815\ \mathrm{dm^3}} \approx \boxed{5{,}5\ \mathrm{mol\cdot dm^{-3}}}\;.
$$

> [!JURY]
> « Le calcul de la concentration apparente en “groupes sulfonate” dans le Nafion réhydraté, très élevée, a aussi été délicat pour certains. » Cette valeur (~5,5 M) est décisive pour les questions 50–52.

### Question 45

> [!INDICATION]
> Quelles différences de potentiel sont mesurables expérimentalement ?

#### Solution

**Non.** Le potentiel de Galvani (potentiel interne) d'une phase isolée n'est pas mesurable : seules sont accessibles des différences de potentiel entre deux phases de **même composition chimique** reliées par un conducteur. La différence $\Delta\psi = \psi_m - \psi_{\text{sol}}$ entre la membrane et la solution, de compositions différentes, n'est pas mesurable directement.

### Question 46

> [!INDICATION]
> Écrire l'égalité des potentiels électrochimiques de Na+ dans les deux phases (pressions égales, activités = concentrations).

> [!INDICATION]
> Faire de même pour Cl− (attention au signe de $z$), puis exprimer $\Delta\psi$ dans les deux cas.

#### Solution

À l'équilibre, le potentiel électrochimique de chaque ion est le même dans les deux phases (les pressions étant égales et les activités confondues avec les concentrations). Pour $\mathrm{Na^+}$ ($z = +1$) :

$$
\mu^\circ + RT\ln[\mathrm{Na^+}]_{\text{sol}} + \mathcal F\psi_{\text{sol}} = \mu^\circ + RT\ln[\mathrm{Na^+}]_m + \mathcal F\psi_m\;,
$$

d'où

$$
\boxed{\Delta\psi = \psi_m - \psi_{\text{sol}} = \frac{RT}{\mathcal F}\ln\frac{[\mathrm{Na^+}]_{\text{sol}}}{[\mathrm{Na^+}]_m}}\;.
$$

Pour $\mathrm{Cl^-}$ ($z = -1$), on obtient de même

$$
\Delta\psi = \frac{RT}{\mathcal F}\ln\frac{[\mathrm{Cl^-}]_m}{[\mathrm{Cl^-}]_{\text{sol}}}\;.
$$

> [!JURY]
> Le rapport souligne que l'établissement du potentiel de Donnan « nécessitait de manipuler avec rigueur les potentiels chimiques et électrochimique (condition d'équilibre) en particulier d'exploiter la phrase “les pressions dans la membrane et dans la solution sont égales” ».

### Question 47

> [!INDICATION]
> Égaler les deux expressions de $\Delta\psi$ obtenues en question 46.

#### Solution

En égalant les deux expressions de $\Delta\psi$ :

$$
\frac{[\mathrm{Na^+}]_{\text{sol}}}{[\mathrm{Na^+}]_m} = \frac{[\mathrm{Cl^-}]_m}{[\mathrm{Cl^-}]_{\text{sol}}}
$$

$$
\boxed{[\mathrm{Na^+}]_{\text{sol}}\,[\mathrm{Cl^-}]_{\text{sol}} = [\mathrm{Na^+}]_m\,[\mathrm{Cl^-}]_m}
$$

> [!METHODE]
> C'est la relation de Donnan : le produit des concentrations ioniques est conservé à l'interface.

### Question 48*

> [!INDICATION]
> Écrire l'électroneutralité dans la solution (pH 7 : H3O+ et OH− négligeables).

> [!INDICATION]
> Dans la membrane, quelles charges fixes s'ajoutent aux ions mobiles ?

#### Solution

Électroneutralité dans la **solution** (pH 7, $\mathrm{H_3O^+}$ et $\mathrm{OH^-}$ négligeables) :

$$
[\mathrm{Na^+}]_{\text{sol}} = [\mathrm{Cl^-}]_{\text{sol}}\;.
$$

Électroneutralité dans la **membrane**, où les sulfonates fixes $C_\Sigma$ s'ajoutent aux charges négatives mobiles :

$$
[\mathrm{Na^+}]_m = [\mathrm{Cl^-}]_m + C_\Sigma\;.
$$

> [!JURY]
> « Les relations clés ici étaient celles de l'électroneutralité, en solution et au sein de la membrane », relations « souvent apparues comme mal maîtrisées ».

### Question 49

> [!INDICATION]
> Combiner la relation de Donnan (Q47) avec les deux électroneutralités (Q48) pour obtenir une équation du second degré en $[\mathrm{Cl^-}]_m$.

> [!INDICATION]
> Ne garder que la racine physiquement positive.

#### Solution

En combinant la question 47, $[\mathrm{Na^+}]_{\text{sol}} = [\mathrm{Cl^-}]_{\text{sol}}$ et $[\mathrm{Na^+}]_m = [\mathrm{Cl^-}]_m + C_\Sigma$, il vient l'équation du second degré

$$
[\mathrm{Cl^-}]_m^2 + C_\Sigma\,[\mathrm{Cl^-}]_m - ([\mathrm{Cl^-}]_{\text{sol}})^2 = 0\;.
$$

Seule la racine positive est physiquement acceptable :

$$
\boxed{[\mathrm{Cl^-}]_m = \frac{-C_\Sigma + \sqrt{C_\Sigma^2 + 4\,([\mathrm{Cl^-}]_{\text{sol}})^2}}{2}}\;.
$$

### Question 50

> [!INDICATION]
> Partir du développement limité suggéré $\sqrt{1+\varepsilon} \approx 1 + \varepsilon/2$ avec $\varepsilon = 4[\mathrm{Cl^-}]_{\text{sol}}^2/C_\Sigma^2 \ll 1$.

#### Solution

Si $C_\Sigma \gg [\mathrm{Cl^-}]_{\text{sol}}$, le développement limité $\sqrt{1+\varepsilon} \approx 1 + \varepsilon/2$ donne

$$
\sqrt{C_\Sigma^2 + 4[\mathrm{Cl^-}]_{\text{sol}}^2} \approx C_\Sigma + \frac{2[\mathrm{Cl^-}]_{\text{sol}}^2}{C_\Sigma}\;,
$$

d'où

$$
\boxed{[\mathrm{Cl^-}]_m \approx \frac{([\mathrm{Cl^-}]_{\text{sol}})^2}{C_\Sigma}}\;.
$$

### Question 51

> [!INDICATION]
> Convertir 35 g/L de NaCl en concentration molaire (M(NaCl) = 58,5 g/mol).

> [!INDICATION]
> Comparer cette valeur à $C_\Sigma \approx 5{,}5$ mol/L : la condition $C_\Sigma \gg [\mathrm{Cl^-}]_{\text{sol}}$ est-elle vérifiée ?

#### Solution

Eau de mer à $35\ \mathrm{g\cdot dm^{-3}}$ de $\mathrm{NaCl}$ :

$$
[\mathrm{Cl^-}]_{\text{sol}} = \frac{35}{58{,}5} \approx 0{,}60\ \mathrm{mol\cdot dm^{-3}}\;.
$$

Avec $C_\Sigma \approx 5{,}5\ \mathrm{mol\cdot dm^{-3}}$, le rapport vaut $C_\Sigma/[\mathrm{Cl^-}]_{\text{sol}} \approx 9$ : la condition $C_\Sigma \gg [\mathrm{Cl^-}]_{\text{sol}}$ est **raisonnablement vérifiée** (un ordre de grandeur), l'approximation de la question 50 reste acceptable, quoique moins bonne qu'en solution diluée.

> [!PIEGE]
> Ne pas écrire que 35 g/L de NaCl correspondent à 1 mol/L d'ions chlorure.

> [!JURY]
> « Certains candidats ont écrit que l'eau de mer à 35 g.L-1 de sel contenait 1 mol.L-1 d'ions chlorures ! »

### Question 52

> [!INDICATION]
> Évaluer numériquement $[\mathrm{Cl^-}]_m$ avec la question 50 et comparer à $[\mathrm{Cl^-}]_{\text{sol}}$.

> [!INDICATION]
> Quelle espèce ionique traverse alors la membrane, et comment qualifie-t-on ce comportement ?

#### Solution

Avec les valeurs numériques, $[\mathrm{Cl^-}]_m \approx \dfrac{0{,}60^2}{5{,}5} \approx 0{,}065\ \mathrm{mol\cdot dm^{-3}}$, très inférieur à $[\mathrm{Cl^-}]_{\text{sol}} = 0{,}60\ \mathrm{mol\cdot dm^{-3}}$ : les **anions (co-ions) sont quasiment exclus** de la membrane par la forte densité de charges fixes négatives (exclusion de Donnan). Seuls les cations (contre-ions $\mathrm{Na^+}$) y pénètrent et la traversent : la membrane est une **membrane échangeuse de cations (MEC) permsélective**, ce qui justifie le schéma de la figure 11 ($\mathrm{Cl^-}$ rejeté, $\mathrm{Na^+}$ transmis).

### Question 53

> [!INDICATION]
> Le Nafion est un polymère perfluoré : à quelle famille de composés persistants appartient-il, et quelle évolution réglementaire connaît-elle ?

#### Solution

Le Nafion est un polymère **perfluoré**, de la famille des **PFAS** (« polluants éternels ») : persistants dans l'environnement, bioaccumulables et problématiques pour la santé, désormais soumis à des **restrictions réglementaires** croissantes. Leur coût et la difficulté de leur recyclage renforcent la tendance socio-économique à les éliminer des piles à combustible au profit de membranes non fluorées.

---

## Partie III — Conducteurs ioniques

La partie III établit la relation fondamentale entre flux molaire et gradient de potentiel électrochimique (bilan des forces en régime stationnaire, Stokes-Einstein), puis la décompose en termes de diffusion, osmotique et de migration, et définit les nombres de transport. C'est un enchaînement de cours à mener proprement, qui prépare la partie IV.

### Question 54*

> [!INDICATION]
> Par quoi le courant est-il transporté dans un conducteur ionique, et à quelles conditions sur les ions ?

#### Solution

Un **conducteur ionique** est un milieu dans lequel le courant électrique est transporté par le **déplacement d'ions** — porteurs de charge **dissociés et mobiles**. La seule présence d'ions ne suffit pas : ils doivent être dissociés et jouir d'une certaine mobilité.

> [!JURY]
> « La présence d'ions ne suffit pas (sont-ils dissociés ?) […] un conducteur ionique n'est pas simplement qu'un milieu contenant des ions. »

### Question 55

> [!INDICATION]
> En régime stationnaire, quelles deux forces s'exercent sur l'ion et se compensent ?

> [!INDICATION]
> Relier le coefficient de diffusion à la viscosité par Stokes-Einstein, et $\mathcal N_A k_B$ à $R$.

#### Solution

En régime stationnaire, la force motrice et la force de friction visqueuse se compensent : $\vec F_i + \vec f_i = \vec 0$, soit

$$
-\frac{1}{\mathcal N_A}\frac{\partial\tilde\mu_i}{\partial x} = 6\pi\eta r_i\,v_i\;.
$$

Avec la relation de Stokes-Einstein $D_i = \dfrac{k_B T}{6\pi\eta r_i}$ et $\mathcal N_A k_B = R$, la vitesse vaut $v_i = -\dfrac{D_i}{RT}\dfrac{\partial\tilde\mu_i}{\partial x}$, et avec $J_i = C_i v_i$ :

$$
\boxed{J_i = -\frac{C_i\,D_i}{RT}\,\frac{\partial\tilde\mu_i}{\partial x}}\;.
$$

> [!JURY]
> « L'établissement de la relation entre le flux molaire Ji et le gradient de potentiel électrochimique n'a posé que peu de difficulté. »

### Question 56

> [!INDICATION]
> Quelles sont les trois dépendances de $\tilde\mu_i(C_i, P, \psi)$ (activité, pression, potentiel) ?

> [!INDICATION]
> Dériver terme à terme et identifier les trois contributions du flux (diffusion, osmotique, migration).

#### Solution

Le potentiel électrochimique s'écrit $\tilde\mu_i = \mu_i^\circ + RT\ln a_i + \bar V_i P + z_i\mathcal F\psi$, avec $a_i \approx C_i$. En dérivant et en reportant dans la question 55 :

$$
J_i = -\frac{C_iD_i}{RT}\left(\frac{RT}{C_i}\frac{\partial C_i}{\partial x} + \bar V_i\frac{\partial P}{\partial x} + z_i\mathcal F\frac{\partial\psi}{\partial x}\right)\;,
$$

soit la somme de trois termes :

$$
\boxed{\begin{aligned}
J_i^{diff} &= -D_i\,\frac{\partial C_i}{\partial x} \\[2pt]
J_i^{osm} &= -\frac{C_i\,D_i\,\bar V_i}{RT}\,\frac{\partial P}{\partial x} \\[2pt]
J_i^{mig} &= -\frac{z_i\,\mathcal F\,C_i\,D_i}{RT}\,\frac{\partial\psi}{\partial x}
\end{aligned}}\qquad J_i = J_i^{diff} + J_i^{osm} + J_i^{mig}\;.
$$

> [!JURY]
> « Tout au plus fallait-il savoir la dépendance du potentiel chimique avec la pression » : c'est ce terme qui donne le flux osmotique.

### Question 57

> [!INDICATION]
> Distinguer le signe de la vitesse des ions de celui du courant électrique qu’ils portent.

#### Solution

La densité de courant électrique portée par les ions $i$ est $j_i=z_i\mathcal FJ_i$. En utilisant le terme de migration et $E=-\partial_x\psi$,
$$j_i^{\mathrm{mig}}=\frac{z_i^2\mathcal F^2C_iD_i}{RT}E.$$
Le sujet définit une mobilité électrique **signée**,
$$u_i=\frac{z_i\mathcal F D_i}{RT}.$$
En conservant cette convention,
$$\boxed{j_i^{\mathrm{mig}}=z_i\mathcal F u_iC_iE=\frac{z_i^2\mathcal F^2C_iD_i}{RT}E.}$$
Les anions se déplacent en sens inverse du champ, mais leur charge est négative : leur contribution au courant conventionnel est, comme celle des cations, dans le sens du champ.

### Question 58

> [!INDICATION]
> Le nombre de transport est la fraction du courant total portée par l'espèce $i$.

#### Solution

Le nombre de transport de l'espèce $i$ est la fraction du courant total qu'elle porte par migration :

$$
\boxed{t_i = \frac{j_i}{j}}
$$

avec $\sum_i t_i = 1$.

### Question 59

> [!INDICATION]
> Dans une MEC parfaite, quels ions sont mobiles dans la membrane (question 52) ?

#### Solution

Dans une membrane échangeuse de cations **parfaite**, les anions $\mathrm{Cl^-}$ étant exclus (question 52), seul $\mathrm{Na^+}$ est mobile dans la membrane : tout le courant y est porté par $\mathrm{Na^+}$, d'où

$$
\boxed{t_m^{+} = 1}
$$

$$
\boxed{t_m^{-} = 0}
$$

---

## Partie IV — Électrodialyse industrielle

La partie IV applique les résultats précédents à une cellule d'électrodialyse : identifier diluat et concentrat, lire la caractéristique courant-tension (représentation de Cowan-Brown), comprendre la polarisation de concentration et le courant limite, puis dimensionner une installation de concentration de lactate par bilans de matière de réacteurs ouverts.

### Question 60

> [!INDICATION]
> Suivre la migration des cations (vers la cathode) et des anions (vers l'anode) dans chaque type de compartiment.

> [!INDICATION]
> Un compartiment qui perd des ions par les deux membranes s'appauvrit : lequel est le diluat ?

#### Solution

Sous l'effet du champ électrique, les cations $\mathrm{M^+}$ migrent vers la cathode et les anions $\mathrm{X^-}$ vers l'anode. Dans un compartiment de **type 1** (cathode/MEC/effluent 1/MEA/anode), les cations sortent par la MEC (côté cathode) et les anions par la MEA (côté anode) : le compartiment s'appauvrit en sel. Dans un compartiment de **type 2**, les ions entrent des compartiments voisins et y sont piégés : il s'enrichit.

```text
cathode │ MEC │ effluent 1 │ MEA │ anode      type 1 : appauvri  → diluat
cathode │ MEA │ effluent 2 │ MEC │ anode      type 2 : enrichi    → concentrat
```

$$
\boxed{C_1 < C_0 < C_2}
$$

Effluent 1 = diluat, effluent 2 = concentrat.

> [!JURY]
> « Les candidats ont facilement identifié de la figure 13 les “diluats” et “concentrats” parmi les effluents » : question accessible, à ne pas manquer.

### Question 61

> [!INDICATION]
> À très faible intensité, $1/j$ est très grand : où se situe le point de départ sur la figure 14B ?

> [!INDICATION]
> Quand l'intensité augmente, $1/j$ diminue : dans quel sens se déplace le point de fonctionnement ?

#### Solution

Sur la représentation de Cowan-Brown $U/j = f(1/j)$, à **très faible intensité** imposée, $1/j$ est très grand : le **point de départ est situé tout à droite** du graphe. Quand l'intensité augmente, $1/j$ diminue : le point de fonctionnement se déplace **vers la gauche** le long de la **branche ohmique** (portion de droite décroissante), jusqu'au voisinage de $1/j_{\text{lim}}$.

### Question 62

> [!INDICATION]
> Dans le régime ohmique, la cellule a la caractéristique d'un électrolyseur : $U = E_{\text{seuil}} + R j$.

> [!INDICATION]
> En déduire $U/j$ en fonction de $1/j$ : pente, ordonnée à l'origine, passage par l'origine ?

#### Solution

Dans le régime ohmique, la cellule se comporte comme un **électrolyseur** de caractéristique $U = E_{\text{seuil}} + R\,j$, d'où

$$
\frac{U}{j} = E_{\text{seuil}}\cdot\frac{1}{j} + R\;.
$$

La branche ohmique est donc une **droite affine en $1/j$**, de pente $E_{\text{seuil}}$ et d'ordonnée à l'origine $R$ : elle **ne passe pas par l'origine** (présence d'un seuil, apparenté à la tension de seuil d'un électrolyseur).

> [!JURY]
> « Pour ce régime, la représentation U/j = f(1/j) est une portion de droite ne passant pas par l'origine (présence d'un seuil apparenté à la tension de seuil d'un électrolyseur) et donc se situant vers les courants faibles (1/j grand). »

### Question 63

> [!INDICATION]
> Au-delà de $j_{\text{lim}}$, la concentration en cations à la surface de la membrane tend vers 0 : quel transport ne peut plus assurer le courant ?

> [!INDICATION]
> Quelle réaction de l'eau s'amorce alors, et quels ions très mobiles provoquent l'acidification du diluat ?

#### Solution

Au-delà de $j_{\text{lim}}$ (soit $1/j \le 1/j_{\text{lim}}$), la concentration en cations à la surface de la membrane tend vers zéro : le transport par les cations ne suffit plus à porter le courant, et une nouvelle réaction s'amorce, l'**autoprotolyse de l'eau** :

$$
\mathrm{2\,H_2O \rightarrow H_3O^+ + OH^-}\;.
$$

Les ions $\mathrm{H_3O^+}$, très mobiles, s'accumulent dans le diluat : d'où l'**acidification** observée (chute de pH).

> [!JURY]
> « Peu ont identifié l'autoprotolyse de l'eau comme étant la réaction à éviter. »

### Question 64

> [!INDICATION]
> Au-delà de $j_{\text{lim}}$, quelle fraction du courant est portée par les ions issus de l'eau plutôt que par les ions du sel ?

#### Solution

Au-delà de $j_{\text{lim}}$, le courant est de plus en plus porté par les ions $\mathrm{H_3O^+}$ et $\mathrm{OH^-}$ issus de la dissociation de l'eau, et non par les ions du sel à transférer : le **rendement faradique chute** et la consommation énergétique augmente. On cherchera donc à faire travailler la cellule avec un courant **proche mais inférieur à $j_{\text{lim}}$**, dans le régime ohmique, pour maximiser le transfert utile tout en évitant la réaction parasite.

### Question 65

> [!INDICATION]
> Lire le profil de la figure 15 : la concentration de surface est-elle inférieure ou supérieure à celle du cœur ?

> [!INDICATION]
> Un compartiment appauvri au voisinage de la membrane est un diluat : compléter le profil du compartiment voisin par symétrie.

#### Solution

Le profil de la figure 15 montre une concentration de surface $C^+_{\text{sol},0} < C^+_{\text{sol},\infty}$ : le compartiment **B est appauvri** au voisinage de la membrane, c'est le **diluat (effluent 1)**. Les cations quittent B par la face anodique de la MEC et passent dans le compartiment voisin **A**, le **concentrat (effluent 2)** : dans A, le profil est symétrique mais inversé, avec une concentration de surface **supérieure** à celle du cœur (accumulation côté membrane).

> [!JURY]
> « La forme du profil (figure 15) indiquait que les cations allaient de B (face anodique) vers A (donc du diluat vers le concentrat) ».

### Question 66*

> [!INDICATION]
> À la densité de courant limite, la déplétion en cations à la surface de la membrane est maximale : quelle valeur limite atteint $C^+_{\text{sol},0}$ ?

#### Solution

À la densité de courant limite, la déplétion en cations à la surface de la membrane est maximale :

$$
\boxed{C^+_{\text{sol},0} \to 0}\;.
$$

### Question 67

> [!INDICATION]
> Relier le plateau de la caractéristique I–U à la saturation du flux de diffusion lorsque $C^+_{\text{sol},0} \to 0$.

#### Solution

Lorsque $C^+_{\text{sol},0} \to 0$ (question 66), le flux de diffusion des cations vers la membrane, $\propto (C^+_{\text{sol},\infty} - C^+_{\text{sol},0})/\delta$, atteint sa valeur maximale et ne peut plus croître : le courant **sature à $j_{\text{lim}}$**, indépendamment de la tension appliquée. D'où le **plateau** de la caractéristique intensité-tension (régime limité par le transport de matière), conformément à la question 64.

### Question 68

> [!INDICATION]
> Dans la membrane, la concentration en contre-ions est-elle hétérogène (fort gradient) ou quasi uniforme ?

> [!INDICATION]
> Comparer alors les termes de diffusion et de migration dans l'expression de la question 56.

#### Solution

La membrane contient une très forte concentration de charges fixes ($C_\Sigma \approx 5{,}5\ \mathrm{mol\cdot L^{-1}}$, question 44), qui impose une concentration en contre-ions quasi uniforme : les gradients de concentration y sont faibles et les co-ions exclus. Le terme de **diffusion** ($\propto \partial C/\partial x$) y est donc négligeable devant le terme de **migration**, gouverné par le champ électrique.

### Question 69

> [!INDICATION]
> L'épaisseur $\delta$ de la couche de diffusion est-elle fixée par la diffusion moléculaire ou par l'écoulement du fluide dans le compartiment ?

#### Solution

L'épaisseur $\delta$ de la couche de diffusion est fixée par l'**hydrodynamique de l'écoulement longitudinal** dans le compartiment (convection forcée, régime établi et stationnaire) : elle ne dépend pas du courant et reste **constante**.

> [!JURY]
> « Il était important de remarquer que l'épaisseur de la couche est contrôlée par l'hydrodynamique de l'écoulement longitudinal. »

### Question 70

> [!INDICATION]
> Repartir de l'expression de l'annexe $j = \mathcal F D^+_{\text{sol}}(C^+_{\text{sol},\infty} - C^+_{\text{sol},0})/(\delta(t_{+,m} - t_{+,sol}))$.

> [!INDICATION]
> Passer à la limite $C^+_{\text{sol},0} \to 0$ et utiliser $t_{+,m} = 1$ (question 59).

#### Solution

L'annexe donne

$$
j = \frac{\mathcal F\,D^+_{\text{sol}}\,(C^+_{\text{sol},\infty} - C^+_{\text{sol},0})}{\delta\,(t_{+,m} - t_{+,sol})}\;.
$$

À la limite $C^+_{\text{sol},0} \to 0$ (question 66) et avec $t_{+,m} = 1$ (MEC parfaite, question 59) :

$$
\boxed{j_{\text{lim}} = \frac{\mathcal F\,D^+_{\text{sol}}\,C^+_{\text{sol},\infty}}{\delta\,(1 - t_{+,sol})}}\;.
$$

### Question 71*

> [!INDICATION]
> Le facteur de concentration 1,96 s'applique à quelle concentration, celle du concentrat ou celle du diluat ?

> [!INDICATION]
> Pour l'autre compartiment, écrire le bilan global de matière sur le lactate (deux alimentations au même débit $\mathcal D$, à $C_0$).

#### Solution

Le facteur de concentration vaut 1,96, donc le compartiment **concentrat** sort à

$$
C_c = 1{,}96 \times 50 = \boxed{98\ \mathrm{g\cdot L^{-1}}}\;.
$$

Les deux compartiments (diluat et concentrat) sont alimentés au même débit $\mathcal D$ et à la même concentration $C_0 = 50\ \mathrm{g\cdot L^{-1}}$ ; le bilan global de matière sur le lactate (réacteur ouvert en écoulement, régime permanent) s'écrit $2\,\mathcal D\,C_0 = \mathcal D\,C_c + \mathcal D\,C_d$, d'où

$$
C_d = 2C_0 - C_c = 100 - 98
$$

$$
\boxed{C_d = 2\ \mathrm{g\cdot L^{-1}}}
$$

### Question 72

> [!INDICATION]
> Le flux à transférer vaut le débit fois l'écart de concentration entre l'alimentation et le diluat.

> [!INDICATION]
> Convertir le résultat en mol/s avec la masse molaire du lactate (88 g/mol).

#### Solution

Le flux de lactate à transférer vaut, par unité de temps,

$$
\begin{aligned}
F_{\text{trans}} &= \mathcal D\,(C_0 - C_d) \\
&= 1\ \mathrm{m^3\cdot h^{-1}} \times (50 - 2)\ \mathrm{g\cdot L^{-1}} \\
&= 48\ \mathrm{kg\cdot h^{-1}}
\end{aligned}
$$

En moles par seconde, avec $M_{\text{lactate}} = 88\ \mathrm{g\cdot mol^{-1}}$ :

$$
F_{\text{trans}} = \frac{48\,000\ \mathrm{g\cdot h^{-1}}}{88\ \mathrm{g\cdot mol^{-1}} \times 3600\ \mathrm{s\cdot h^{-1}}} \approx \boxed{0{,}152\ \mathrm{mol\cdot s^{-1}}}\;.
$$

### Question 73

> [!INDICATION]
> Calculer d'abord la densité de courant de travail $j = 0{,}8\,j_{\text{lim}}$.

> [!INDICATION]
> Relier la densité de flux de lactate (monovalent) au rendement faradique et à $j$ via $\mathcal F$.

#### Solution

On travaille à $j = 0{,}8\,j_{\text{lim}} = 0{,}8 \times 444 = 355{,}2\ \mathrm{A\cdot m^{-2}}$. Le lactate étant monovalent, la densité de flux de lactate liée au rendement faradique $R = 0{,}8$ est

$$
J_{\text{lactate}} = \frac{R\,j}{\mathcal F} = \frac{0{,}8 \times 355{,}2}{96\,500} \approx \boxed{2{,}94\times10^{-3}\ \mathrm{mol\cdot m^{-2}\cdot s^{-1}}}\;.
$$

### Question 74

> [!INDICATION]
> La surface cherchée est le rapport du flux total à transférer (Q72) à la densité de flux de lactate (Q73).

#### Solution

La surface nécessaire est le rapport du flux à transférer à la densité de flux de lactate :

$$
S = \frac{F_{\text{trans}}}{J_{\text{lactate}}} = \frac{0{,}152}{2{,}94\times10^{-3}} \approx \boxed{52\ \mathrm{m^2}}\;.
$$

C'est l'ordre de grandeur de la surface totale de membrane nécessaire à l'opération.

> [!JURY]
> « Les dernières questions faisaient appel à l'analyse de bilan de matière de réacteurs ouverts en écoulement. Le rapport entre le flux de lactate à transférer et la densité de flux de lactate résultant de la densité de courant électrique appliquée permettait d'aboutir à la surface des membranes recherchée. En règle générale cette dernière section a été peu abordée » : les intentions pertinentes ont été remarquées par le jury.

---

## Bilan

**Méthodes à retenir.**

- **Cinétique de croissance interfaciale (Q9–Q20)** : relier une grandeur extensive à une épaisseur par un bilan volumique ($nM/\rho = (1-w)Sx$), passer au flux par la loi de Fick, intégrer par séparation des variables, et linéariser par $Y = x^2$ quand l'équation est du type $\mathrm{d}x/\mathrm{d}t = a/x - bx$. Toujours confronter la loi trouvée à l'observation (croissance bornée ou non) et signaler les coquilles de l'énoncé (Q15, Q18).
- **Équilibre de Donnan (Q46–Q52)** : égalité des potentiels électrochimiques à l'interface (en exploitant « pressions égales »), relation de Donnan (produit des concentrations conservé), électroneutralité dans chaque phase avec les charges fixes $C_\Sigma$, puis développement limité quand $C_\Sigma \gg$ concentration du sel. Le résultat clé est l'exclusion des co-ions, $[\mathrm{Cl^-}]_m \approx [\mathrm{Cl^-}]_{\text{sol}}^2/C_\Sigma$.
- **Transport ionique (Q55–Q59)** : bilan des forces en régime stationnaire + Stokes-Einstein → $J_i = -(C_iD_i/RT)\,\partial\tilde\mu_i/\partial x$, à décomposer en diffusion, osmotique (terme de pression) et migration ; $j_i = z_i\mathcal F J_i$ et $t_i = j_i/j$.
- **Électrodialyse (Q60–Q74)** : sens de migration des ions et identification diluat/concentrat ; représentation de Cowan-Brown $U/j = f(1/j)$ (branche ohmique = droite à seuil) ; courant limite par déplétion ($C^+_{\text{sol},0} \to 0$) et formule de l'annexe ; dimensionnement par bilans de réacteurs ouverts ($2C_0 = C_c + C_d$, $S = F_{\text{trans}}/J$).

**Prérequis à revoir.** groupe amide plan (mésomérie, et non VSEPR) ; salification acide-amine ; acides sulfoniques forts ; loi de Fick et profils de concentration en régime stationnaire ; potentiel électrochimique et mobilité ; osmose ; stéréochimie de la base de Tröger (2 énantiomères, pas de forme méso) ; rétro-Diels-Alder ; mécanismes avec intermédiaires réactionnels nommés (SEAr, carbocation tertiaire benzylique).

**Questions classiques transposables.** le modèle de croissance auto-limitée (Q17–Q19) est transposable à tout phénomène de croissance contrôlée par un réactif consommé par une réaction parasite ; le bloc Donnan (Q46–Q52) est transposable à toute membrane ionomère (diaphragmes, échangeurs) ; la polarisation de concentration et le courant limite (Q61–Q70) se retrouvent dans toute cellule à membrane (électrolyse, piles) ; le dimensionnement Q71–Q74 est un bilan de réacteur ouvert classique.

**Ce que le rapport 2025 retient de l'épreuve.** outre les statistiques rappelées en présentation (20 questions fondamentales sur 74, 25 % des points, 5 % pour la présentation), le jury insiste sur la rigueur de rédaction, les schémas légendés et le commentaire critique des résultats : « Le jury accueille avec bienveillance toute forme de regard critique émanant des candidats à l'égard du contenu de l'énoncé de l'épreuve. »
