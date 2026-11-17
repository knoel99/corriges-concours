# Agrégation Chimie — Problème de chimie 2025 · Corrigé brut

*Corrigé rédigé par IA, non officiel. Signalez toute erreur.*

Épreuve de 6 heures (session 2025), sujet « Membranes à perméabilité sélective » : 74 questions en quatre parties — I. fabrication d'un matériau quasi bidimensionnel (Nylon 6-10 et polymérisation interfaciale, puis polymères à microporosité intrinsèque) ; II. résine échangeuse d'ions, potentiel de Donnan et permsélectivité (Nafion) ; III. conducteurs ioniques ; IV. électrodialyse industrielle. Les questions suivies d'une étoile (*) sont les questions fondamentales signalées par l'énoncé. Principales données de l'énoncé : masse volumique du Nylon $\rho = 1{,}08\ \mathrm{g\cdot cm^{-3}}$, teneur volumique en eau de la membrane fraîche $w = 90\ \%$, $\mathcal F = 96\,500\ \mathrm{C\cdot mol^{-1}}$, masse molaire du lactate de sodium $88\ \mathrm{g\cdot mol^{-1}}$, masse molaire de $\mathrm{NaCl}$ $58{,}5\ \mathrm{g\cdot mol^{-1}}$.

---

## Partie I — Fabrication d'un matériau quasi bidimensionnel

### Question 1*

Dans la nomenclature « Nylon $a$-$b$ » de Dupont-de-Nemours, $a$ est le nombre d'atomes de carbone de la **diamine** et $b$ celui du **diacide** (ou de son dichlorure). L'hexaméthylènediamine $\mathrm{H_2N-(CH_2)_6-NH_2}$ apporte 6 carbones, le chlorure de sébacoyle (dichlorure de l'acide décanedioïque) $\mathrm{ClOC-(CH_2)_8-COCl}$ en apporte 10 :

$$
\boxed{\text{Nylon 6-10 : 6 carbones de diamine, 10 carbones de diacide}}
$$

### Question 2*

Le groupe amide $-\mathrm{C(=O)-N}<$ possède une forme mésomère dans laquelle le doublet de l'azote se délocalise sur l'oxygène :

$$
\mathrm{-C(=O)-N< \;\longleftrightarrow\; -C(-O^{-})=N^{+}<}\;.
$$

La liaison C–N acquiert un **caractère partiel de double liaison** : l'azote est de type $sp^2$ et les six atomes (C, O, N et leurs trois substituants) sont **coplanaires**. La rotation autour de C–N est bloquée. Une description VSEPR isolée conduirait à tort à un azote pyramidal.

$$
\boxed{\text{Le groupe amide est plan (résultat expérimental avéré), la rotation C--N est bloquée}}
$$

### Question 3*

Un acide carboxylique et une amine réagissent à température ambiante par une **réaction acide-base de salification**, qui forme un carboxylate d'ammonium et **bloque toute autre transformation**. Le chlorure d'acyle, beaucoup plus électrophile ($\mathrm{Cl^-}$ est un bon groupe partant), subit l'attaque nucléophile de l'amine de façon rapide et irréversible dès la température ambiante : c'est lui qui permet la polycondensation interfaciale.

### Question 4*

Le **chlorure de thionyle** $\mathrm{SOCl_2}$ convient :

$$
\mathrm{R-COOH + SOCl_2 \rightarrow R-COCl + SO_2\!\uparrow + HCl\!\uparrow}\;.
$$

Les sous-produits $\mathrm{SO_2}$ et $\mathrm{HCl}$ étant gazeux, ils s'éliminent spontanément du milieu réactionnel, ce qui rend le traitement très simple.

### Question 5*

L'unité répétitive est le motif

$$
\mathrm{\big[-NH-(CH_2)_6-NH-CO-(CH_2)_8-CO-\big]}\;,
$$

de formule brute $\mathrm{C_{16}H_{30}N_2O_2}$ (deux fonctions amide par motif, donc deux HCl éliminés par motif lors de la polycondensation avec le dichlorure d’acyle). D'où

$$
M = 16(12{,}01) + 30(1{,}008) + 2(14{,}01) + 2(16{,}00) \approx \boxed{282\ \mathrm{g\cdot mol^{-1}}}\;.
$$

### Question 6*

Les motifs s'associent par **liaisons hydrogène** entre le $\mathrm{N-H}$ d'un groupe amide (donneur) et l'oxygène du carbonyle $\mathrm{C=O}$ d'un autre motif (accepteur), au sein d'une même chaîne ou entre chaînes voisines :

$$
\mathrm{N-H\cdots O=C}\;.
$$

### Question 7*

La laine et la soie sont des **protéines**, donc des **polyamides naturels** : leurs liaisons peptidiques $-\mathrm{CO-NH}-$ sont les mêmes fonctions amide que celles du Nylon, avec le même réseau de liaisons hydrogène inter-chaînes. Les propriétés mécaniques des fibres (résistance, souplesse) sont donc analogues, ce qui permet au Nylon de se substituer à ces fibres textiles.

### Question 8*

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

Cohérent avec l'ordre de grandeur annoncé (quelques dizaines de micromètres).

### Question 9

La masse de polymère contenue dans la membrane vaut $nM$ ; son volume $nM/\rho$ est la fraction $(1-w)$ du volume $Sx$ de la membrane fraîche :

$$
\frac{nM}{\rho} = (1-w)\,S\,x
$$

$$
\boxed{x = \frac{nM}{\rho(1-w)S}}
$$

### Question 10

Par dérivation par rapport au temps, $S$, $M$, $\rho$ et $w$ étant constants :

$$
\begin{aligned}
\frac{\mathrm{d}n}{\mathrm{d}t} &= \frac{\rho(1-w)S}{M}\,\frac{\mathrm{d}x}{\mathrm{d}t} \\
\frac{\mathrm{d}x}{\mathrm{d}t} &= \frac{M}{\rho(1-w)S}\,\frac{\mathrm{d}n}{\mathrm{d}t}
\end{aligned}
$$

$\mathrm{d}n/\mathrm{d}t$ est la vitesse de formation des motifs, c'est-à-dire la cinétique de la réaction de polymérisation.

### Question 11

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

Loi de Fick : $J = -D\,\mathrm{d}C/\mathrm{d}x$. Le gradient linéaire vaut, sur l'épaisseur $x$ de la membrane,

$$
\frac{\mathrm{d}C_A}{\mathrm{d}x} = \frac{C_A - 0}{x} = \frac{C_A}{x}\;,
$$

d'où

$$
\boxed{J = -D\,\frac{C_A}{x}}\;.
$$

### Question 13

Toute la diamine arrivant à l'interface est convertie en polymère : $\mathrm{d}n/\mathrm{d}t = |J|\,S = \dfrac{D\,C_A}{x}\,S$. En reportant dans la question 10 :

$$
\boxed{\frac{\mathrm{d}x}{\mathrm{d}t} = \frac{M\,D\,C_A}{\rho(1-w)\,x}}\;.
$$

### Question 14

En posant $a = \dfrac{M D C_A}{\rho(1-w)}$, l'équation $\mathrm{d}x/\mathrm{d}t = a/x$ s'intègre en $x\,\mathrm{d}x = a\,\mathrm{d}t$, soit

$$
\frac{x^2}{2} = a\,t
$$

$$
x = \sqrt{\frac{2\,M\,C_A\,D}{(1-w)\,\rho}\,t}
$$

Cette loi en $\sqrt{t}$ **croît indéfiniment** : la membrane ne cesserait jamais de s'épaissir. Or l'expérience montre une épaisseur qui **se stabilise** après quelques minutes : la solution proposée **n'est pas compatible** avec l'observation expérimentale.

### Question 15

Par unité de surface, le volume de membrane fraîche vaut $x$ ; l'eau en occupe la fraction volumique $w$, soit un volume $wx$. Avec la masse volumique de l'eau $\rho_{\text{eau}} \simeq 1\ \mathrm{g\cdot cm^{-3}}$ et $M_{\text{eau}} = 18\ \mathrm{g\cdot mol^{-1}}$ :

$$
\boxed{\Gamma_{\mathrm{H_2O}} = \frac{w\,\rho_{\text{eau}}\,x}{18}}\;.
$$

Dans la formule de l'énoncé, le symbole $\rho$ désigne la masse volumique de **l'eau** (et non celle du polymère) : $x$ en dm et $\rho_{\text{eau}}$ en $\mathrm{g\cdot dm^{-3}}$ donnent bien $\Gamma_{\mathrm{H_2O}}$ en $\mathrm{mol\cdot dm^{-2}}$.

### Question 16

L'hydrolyse du chlorure d'acyle par l'eau, d'ordres partiels égaux à 1, a pour vitesse surfacique

$$
v_{\text{hyd}} = k\,\Gamma_C\,\Gamma_{\mathrm{H_2O}}\;.
$$

$\Gamma_C$ étant constante et $\Gamma_{\mathrm{H_2O}} = \dfrac{w\rho_{\text{eau}}}{18}\,x$ (question 15) :

$$
\boxed{v_{\text{hyd}} = k\,\Gamma_C\,\frac{w\,\rho_{\text{eau}}}{18}\,x \;\propto\; x}\;.
$$

### Question 17

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

Avec le changement de variable $Y = x^2$ : $\dfrac{\mathrm{d}Y}{\mathrm{d}t} = 2x\,\dfrac{\mathrm{d}x}{\mathrm{d}t} = 2a - 2b\,Y$. L'équation linéaire $\mathrm{d}Y/\mathrm{d}t + 2bY = 2a$, avec $Y(0) = 0$, a pour solution $Y = \dfrac{a}{b}\big(1 - e^{-2bt}\big)$, soit

$$
\boxed{x(t) = \sqrt{\frac{a}{b}\big(1 - e^{-2bt}\big)}}\;.
$$

**Coquille de l'énoncé signalée** : la formule proposée $x(t) = \sqrt{a/b}\,(1-e^{-bt})$ est incorrecte (il manque le facteur 2 dans l'argument de l'exponentielle, et la racine doit porter sur tout le trinôme) ; on le vérifie en reportant la solution correcte dans $\mathrm{d}x/\mathrm{d}t = a/x - bx$.

### Question 19

À la limite $t \to \infty$, $e^{-2bt} \to 0$, donc l'épaisseur finale vaut

$$
x_m = \sqrt{\frac{a}{b}} = \sqrt{\frac{18\,D\,C_A}{k\,\Gamma_C\,w\,\rho_{\text{eau}}}}\;.
$$

$$
\boxed{x_m = \sqrt{\frac{a}{b}} = \sqrt{\frac{18\,D\,C_A}{k\,\Gamma_C\,w\,\rho_{\text{eau}}}}}\;.
$$

La croissance est désormais **auto-limitée** : $x \to x_m$ fini, ce qui corrige le défaut du modèle de la question 14.

### Question 20

Le modèle prévoit

$$
x' = \frac{x}{x_m} = \sqrt{1 - e^{-2bt}}\;,
$$

fonction croissante de $t$ tendant vers **1** : il apparaît un **plateau**, conforme à la figure 3. De plus, comme $b$ ne dépend pas de $C_A$, la courbe normalisée est **indépendante de $C_A$** : les jeux de points obtenus pour les différentes concentrations se superposent sur une courbe maîtresse unique, exactement ce que montre la figure 3. Les hypothèses du modèle (régime stationnaire, gradient linéaire, $\Gamma_C$ constante, réaction parasite) sont donc qualitativement validées.

### Question 21

La membrane est semi-perméable à l'eau et contient des solutés : le phénomène est l'**osmose**. Dans l'**eau distillée**, l'activité de l'eau extérieure est maximale : l'eau entre par osmose, la membrane **gonfle** (son diamètre augmente). Dans l'**eau salée** à $0{,}1\ \mathrm{mol\cdot dm^{-3}}$, l'activité de l'eau extérieure est abaissée : l'eau sort, la membrane se **contracte**. L'alternance des bains explique les variations réversibles de diamètre observées sur la figure 4.

### Question 22*

Dans un polymère, chaque type de proton occupe une **distribution d'environnements chimiques** légèrement différents (longueur de chaîne, configurations, bouts de chaîne), et la **mobilité réduite** des segments de chaîne limite le moyennage par relaxation. Il en résulte une distribution de déplacements chimiques, donc un **élargissement de tous les signaux**.

### Question 23

Attribution des signaux du spectre $^1\mathrm{H}$-RMN du motif répétitif (20 H au total) :

| $\delta$ (ppm) | Multiplicité | Intégration | Attribution |
|---|---|---|---|
| 7,28 | m | 4H | H aromatiques |
| 4,57 | s | 2H | pont $\mathrm{N-CH_2-N}$ de la base de Tröger |
| 4,05 | s | 4H | 2 × $\mathrm{Ar-CH_2-N}$ de la base de Tröger |
| 1,81 | m | 6H | 2 × $\mathrm{CH_3}$ en positions 9 et 10 |
| 1,65 | m | 4H | pont éthano $-\mathrm{CH_2-CH_2}-$ |

### Question 24*

Le motif réunit le motif 9,10-diméthyl-9,10-éthanoanthracène (14 C du squelette anthracène, 2 C des méthyles, 2 C du pont éthano) et les **3 carbones apportés par le méthanal** de la base de Tröger (question 32), avec 2 N et 20 H (cohérent avec les intégrations de la question 23) :

$$
\mathrm{C_{21}H_{20}N_2}\;.
$$

$$
M = 21(12{,}01) + 20(1{,}008) + 2(14{,}01) = \boxed{300\ \mathrm{g\cdot mol^{-1}}}\;.
$$

### Question 25

Degré de polymérisation moyen en nombre :

$$
DP = \frac{M_n}{M} = \frac{40\,700}{300} \approx \boxed{136}\;.
$$

La dispersité Đ vaut $\dfrac{M_w}{M_n} = \dfrac{155\,800}{40\,700} \approx 3{,}8$.

### Question 26

Au chauffage vers 260 °C, le pont éthano du motif 9,10-éthanoanthracène subit une **rétro-Diels-Alder** : le pont bicyclo[2.2.2] se fragmente en libérant de l'**éthylène** $\mathrm{CH_2=CH_2}$ et en restaurant l'aromaticité du noyau anthracène. La réaromatisation, très exergonique, est la force motrice de la réaction ; la température de l'analyse thermogravimétrique fournit l'énergie d'activation.

### Question 27

Chaque motif ($M = 300\ \mathrm{g\cdot mol^{-1}}$) perd une molécule d'éthylène ($M = 28\ \mathrm{g\cdot mol^{-1}}$) par rétro-Diels-Alder totale :

$$
\frac{\Delta m}{m} = \frac{28}{300} = 9{,}3\ \% \approx \boxed{10\ \%}\;,
$$

en accord avec l'analyse thermogravimétrique.

### Question 28

Le motif 9,10-éthanoanthracène est le dibenzobicyclo[2.2.2]octane : deux têtes de pont $sp^3$ (C9 et C10) portant chacune un $\mathrm{CH_3}$, réunies par deux ponts ortho-phénylène et un pont $-\mathrm{CH_2-CH_2}-$ ; les substituants R occupent les positions 2 et 6 (ou 2 et 7) des noyaux aromatiques. En perspective cavalière, les deux noyaux benzéniques sont quasi parallèles et le pont éthano ferme le bicyclo[2.2.2]octane (qui **ne peut pas exister en conformation chaise**). La molécule possède des plans de symétrie : elle est **achirale** et ne comporte **aucun centre stéréogène** (C9 et C10 portent deux substituants méthyle/phényle en relation de symétrie).

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

### Question 29*

Les deux atomes d'azote « têtes de pont » de la base de Tröger sont configurationnellement stables, mais leurs configurations sont **couplées** par la rigidité du pont : seules les combinaisons $(R,R)$ et $(S,S)$ sont géométriquement possibles (la forme « méso » $(R,S)$ est impossible). L'image dans un miroir n'est pas superposable à la molécule. Il existe donc

$$
\boxed{2\ \text{stéréo-isomères, énantiomères l'un de l'autre}}
$$

### Question 30*

La base de Tröger possède un **axe de symétrie $C_2$**, mais **ni plan de symétrie ni centre d'inversion** : elle est **chirale**. Les **centres stéréogènes sont les deux atomes d'azote**, chacun de configuration absolue fixée ; on les repère par les descripteurs CIP, qui donnent le couple $(R,R)$ et son énantiomère $(S,S)$ (par exemple $(5R,11R)$ et $(5S,11S)$).

### Question 31

Aucun contrôle stéréochimique n'étant exercé pendant la polymérisation, chaque jonction de Tröger se forme indifféremment en $(R,R)$ ou $(S,S)$ : la macromolécule est une **succession aléatoire de coudes de chiralités opposées**, irrégulière et contorsionnée, sans ordre à longue distance. Les chaînes ne peuvent pas s'empiler de façon compacte, ce qui crée le **volume libre** responsable de la microporosité intrinsèque.

### Question 32

Dans le motif Tröger, les atomes de carbone qui **ne proviennent pas de la diamine 1** sont les **trois méthylènes** : le pont central $\mathrm{N-CH_2-N}$ et les deux ponts $\mathrm{Ar-CH_2-N}$.

### Question 33

Ces trois méthylènes forment des **aminals** ($\mathrm{N-CH_2-N}$) et des liaisons de type Mannich ($\mathrm{Ar-CH_2-N}$). Leur disconnexion rétrosynthétique (hydrolyse rétro) régénère les deux fonctions amine aromatiques et **trois équivalents de méthanal** :

$$
\text{base de Tröger} \;\Longrightarrow\; 2\ \mathrm{Ar-NH_2} + 3\ \mathrm{H_2CO}\;.
$$

### Question 34

En milieu acide (acide trifluoroéthanoïque), le diméthoxyméthane $\mathrm{CH_2(OMe)_2}$ est protoné puis perd un méthanol pour engendrer l'**ion oxocarbénium** $\mathrm{[CH_2=O^{+}Me \leftrightarrow {}^{+}CH_2-OMe]}$, électrophile en carbone. Cet ion est strictement équivalent au cation méthylèneoxonium obtenu par protonation du méthanal $\mathrm{H_2C=O}$ : le diméthoxyméthane est donc un **équivalent synthétique du méthanal**, plus commode à manipuler (liquide, anhydre).

### Question 35*

L'addition de 2 équivalents de $\mathrm{PhMgBr}$ sur l'hexane-2,5-dione donne le **2,5-diphénylhexane-2,5-diol**, qui porte deux stéréocentres équivalents (C2 et C5). On dénombre

$$
\boxed{3\ \text{stéréo-isomères}}
$$

: la paire d'énantiomères $(R,R)$ / $(S,S)$ et le composé **méso** $(R,S)$, qui possède un plan de symétrie interne.

### Question 36

Mécanisme de la réaction (ii), en deux étapes identiques :

1. $\mathrm{AlCl_3}$ (acide de Lewis) complexe un groupe $\mathrm{OH}$ ; la liaison C–O se rompt en libérant $\mathrm{[AlCl_3OH]^-}$ et un **carbocation tertiaire benzylique**, stabilisé par mésomérie ;
2. **substitution électrophile aromatique intramoléculaire** (type Friedel-Crafts) : un noyau phényle attaque le carbocation, puis réaromatisation par perte de $\mathrm{H^+}$ — première cyclisation.

Le second $\mathrm{OH}$ subit la même séquence (carbocation puis SEAr intramoléculaire) : seconde cyclisation. Le bilan est une **double déshydratation** conduisant au 9,10-diméthyl-9,10-éthanoanthracène (composé 3).

### Question 37

Le sous-produit principal (éther cyclique) provient de l'attaque intramoléculaire de l'**oxygène du second hydroxyle** sur le carbocation tertiaire benzylique formé comme en question 36 : la fermeture du cycle donne le **2,5-diméthyl-2,5-diphényltétrahydrofurane** (cycle à 5 chaînons), après perte du proton.

### Question 38*

$\mathrm{KNO_3}$ réagit avec l'anhydride trifluoroacétique $(\mathrm{CF_3CO})_2\mathrm{O}$ pour engendrer le **nitrate de trifluoroacétyle** :

$\mathrm{CF_3CO-O-NO_2}$, qui se dissocie en ion trifluoroacétate et en **ion nitronium** $\mathrm{NO_2^{+}}$ :

$$
\boxed{\mathrm{CF_3COONO_2 \rightarrow CF_3COO^{-} + NO_2^{+}}}\;.
$$

$\mathrm{NO_2^+}$ est l'électrophile effectif de la nitration.

### Question 39*

L'acétonitrile est un solvant **polaire aprotique** : il solvate et stabilise les espèces ioniques ($\mathrm{NO_2^+}$ et l'état de transition chargé de la SEAr), ce qui favorise la génération et la réactivité du nitronium, tout en dissolvant les réactifs organiques.

### Question 40

Les deux noyaux aromatiques de la molécule 3 réagissent **indépendamment** l'un de l'autre. Sur chaque noyau, la régiosélectivité est imposée par les effets électroniques des substituants (méthyle donneur $+I$, pont éthano), mais la position **relative** des deux groupes $\mathrm{NO_2}$ sur l'ensemble de la molécule peut être différente : le composé dinitré 4 est un **mélange de deux régioisomères** (non séparés), selon que les deux nitrations sont du même côté (syn) ou opposé (anti) de la molécule.

### Question 41

L'hydrate d'hydrazine sur nickel de Raney peut être remplacé par :

- une **hydrogénation catalytique** $\mathrm{H_2}$ sur $\mathrm{Pd/C}$ (ou $\mathrm{PtO_2}$) ;
- une réduction en milieu acide : $\mathrm{SnCl_2/HCl}$ ou $\mathrm{Fe/HCl}$.

Dans tous les cas, la fonction visée est la réduction de $\mathrm{NO_2}$ en $\mathrm{NH_2}$.

---

## Partie II — Résine échangeuse d'ions, potentiel de Donnan, rejet d'une espèce ionique

### Question 42*

Les acides sulfoniques $\mathrm{SO_3H}$ sont des **acides forts** ($\mathrm pK_a \approx -1$ à $-2$) : sur toute la fenêtre $0 \le \mathrm{pH} \le 14$, les fonctions sont **totalement déprotonées** en sulfonate $\mathrm{SO_3^-}$. Le polymère est donc toujours ionisé (anionique) dans l'eau.

### Question 43

Une mole de fonctions $\mathrm{SO_3H}$ correspond à $1100\ \mathrm{g}$ de résine sèche de masse volumique $1{,}98\ \mathrm{g\cdot cm^{-3}}$ :

$$
[\mathrm{SO_3^-}]_{\text{sec}} = \frac{1\ \mathrm{mol}}{1100\ \mathrm{g}} \times 1{,}98\ \mathrm{g\cdot cm^{-3}} = 1{,}8\times10^{-3}\ \mathrm{mol\cdot cm^{-3}} \approx \boxed{1{,}8\ \mathrm{mol\cdot L^{-1}}}\;.
$$

### Question 44

Pour 1 mol de $\mathrm{SO_3H}$ (1100 g de résine sèche), l'eau absorbée vaut $0{,}165 \times 1100 = 181{,}5\ \mathrm{g}$, soit $0{,}1815\ \mathrm{dm^3}$. La concentration en sulfonate rapportée à l'eau contenue dans la membrane gonflée est donc

$$
C_\Sigma = \frac{1\ \mathrm{mol}}{0{,}1815\ \mathrm{dm^3}} \approx \boxed{5{,}5\ \mathrm{mol\cdot dm^{-3}}}\;.
$$

### Question 45

**Non.** Le potentiel de Galvani (potentiel interne) d'une phase isolée n'est pas mesurable : seules sont accessibles des différences de potentiel entre deux phases de **même composition chimique** reliées par un conducteur. La différence $\Delta\psi = \psi_m - \psi_{\text{sol}}$ entre la membrane et la solution, de compositions différentes, n'est pas mesurable directement.

### Question 46

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

### Question 47

En égalant les deux expressions de $\Delta\psi$ :

$$
\frac{[\mathrm{Na^+}]_{\text{sol}}}{[\mathrm{Na^+}]_m} = \frac{[\mathrm{Cl^-}]_m}{[\mathrm{Cl^-}]_{\text{sol}}}
$$

$$
\boxed{[\mathrm{Na^+}]_{\text{sol}}\,[\mathrm{Cl^-}]_{\text{sol}} = [\mathrm{Na^+}]_m\,[\mathrm{Cl^-}]_m}
$$

### Question 48*

Électroneutralité dans la **solution** (pH 7, $\mathrm{H_3O^+}$ et $\mathrm{OH^-}$ négligeables) :

$$
[\mathrm{Na^+}]_{\text{sol}} = [\mathrm{Cl^-}]_{\text{sol}}\;.
$$

Électroneutralité dans la **membrane**, où les sulfonates fixes $C_\Sigma$ s'ajoutent aux charges négatives mobiles :

$$
[\mathrm{Na^+}]_m = [\mathrm{Cl^-}]_m + C_\Sigma\;.
$$

### Question 49

En combinant la question 47, $[\mathrm{Na^+}]_{\text{sol}} = [\mathrm{Cl^-}]_{\text{sol}}$ et $[\mathrm{Na^+}]_m = [\mathrm{Cl^-}]_m + C_\Sigma$, il vient l'équation du second degré

$$
[\mathrm{Cl^-}]_m^2 + C_\Sigma\,[\mathrm{Cl^-}]_m - ([\mathrm{Cl^-}]_{\text{sol}})^2 = 0\;.
$$

Seule la racine positive est physiquement acceptable :

$$
\boxed{[\mathrm{Cl^-}]_m = \frac{-C_\Sigma + \sqrt{C_\Sigma^2 + 4\,([\mathrm{Cl^-}]_{\text{sol}})^2}}{2}}\;.
$$

### Question 50

Si $C_\Sigma \gg [\mathrm{Cl^-}]_{\text{sol}}$, le développement limité $\sqrt{1+\varepsilon} \approx 1 + \varepsilon/2$ donne

$$
\sqrt{C_\Sigma^2 + 4[\mathrm{Cl^-}]_{\text{sol}}^2} \approx C_\Sigma + \frac{2[\mathrm{Cl^-}]_{\text{sol}}^2}{C_\Sigma}\;,
$$

d'où

$$
\boxed{[\mathrm{Cl^-}]_m \approx \frac{([\mathrm{Cl^-}]_{\text{sol}})^2}{C_\Sigma}}\;.
$$

### Question 51

Eau de mer à $35\ \mathrm{g\cdot dm^{-3}}$ de $\mathrm{NaCl}$ :

$$
[\mathrm{Cl^-}]_{\text{sol}} = \frac{35}{58{,}5} \approx 0{,}60\ \mathrm{mol\cdot dm^{-3}}\;.
$$

Avec $C_\Sigma \approx 5{,}5\ \mathrm{mol\cdot dm^{-3}}$, le rapport vaut $C_\Sigma/[\mathrm{Cl^-}]_{\text{sol}} \approx 9$ : la condition $C_\Sigma \gg [\mathrm{Cl^-}]_{\text{sol}}$ est **raisonnablement vérifiée** (un ordre de grandeur), l'approximation de la question 50 reste acceptable, quoique moins bonne qu'en solution diluée.

### Question 52

Avec les valeurs numériques, $[\mathrm{Cl^-}]_m \approx \dfrac{0{,}60^2}{5{,}5} \approx 0{,}065\ \mathrm{mol\cdot dm^{-3}}$, très inférieur à $[\mathrm{Cl^-}]_{\text{sol}} = 0{,}60\ \mathrm{mol\cdot dm^{-3}}$ : les **anions (co-ions) sont quasiment exclus** de la membrane par la forte densité de charges fixes négatives (exclusion de Donnan). Seuls les cations (contre-ions $\mathrm{Na^+}$) y pénètrent et la traversent : la membrane est une **membrane échangeuse de cations (MEC) permsélective**, ce qui justifie le schéma de la figure 11 ($\mathrm{Cl^-}$ rejeté, $\mathrm{Na^+}$ transmis).

### Question 53

Le Nafion est un polymère **perfluoré**, de la famille des **PFAS** (« polluants éternels ») : persistants dans l'environnement, bioaccumulables et problématiques pour la santé, désormais soumis à des **restrictions réglementaires** croissantes. Leur coût et la difficulté de leur recyclage renforcent la tendance socio-économique à les éliminer des piles à combustible au profit de membranes non fluorées.

---

## Partie III — Conducteurs ioniques

### Question 54*

Un **conducteur ionique** est un milieu dans lequel le courant électrique est transporté par le **déplacement d'ions** — porteurs de charge **dissociés et mobiles**. La seule présence d'ions ne suffit pas : ils doivent être dissociés et jouir d'une certaine mobilité.

### Question 55

En régime stationnaire, la force motrice et la force de friction visqueuse se compensent : $\vec F_i + \vec f_i = \vec 0$, soit

$$
-\frac{1}{\mathcal N_A}\frac{\partial\tilde\mu_i}{\partial x} = 6\pi\eta r_i\,v_i\;.
$$

Avec la relation de Stokes-Einstein $D_i = \dfrac{k_B T}{6\pi\eta r_i}$ et $\mathcal N_A k_B = R$, la vitesse vaut $v_i = -\dfrac{D_i}{RT}\dfrac{\partial\tilde\mu_i}{\partial x}$, et avec $J_i = C_i v_i$ :

$$
\boxed{J_i = -\frac{C_i\,D_i}{RT}\,\frac{\partial\tilde\mu_i}{\partial x}}\;.
$$

### Question 56

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

### Question 57

La densité de courant électrique portée par les ions $i$ est $j_i=z_i\mathcal FJ_i$. En utilisant le terme de migration et $E=-\partial_x\psi$,
$$j_i^{\mathrm{mig}}=\frac{z_i^2\mathcal F^2C_iD_i}{RT}E.$$
Le sujet définit une mobilité électrique **signée**,
$$u_i=\frac{z_i\mathcal F D_i}{RT}.$$
En conservant cette convention,
$$\boxed{j_i^{\mathrm{mig}}=z_i\mathcal F u_iC_iE=\frac{z_i^2\mathcal F^2C_iD_i}{RT}E.}$$
Les anions se déplacent en sens inverse du champ, mais leur charge est négative : leur contribution au courant conventionnel est, comme celle des cations, dans le sens du champ.

### Question 58

Le nombre de transport de l'espèce $i$ est la fraction du courant total qu'elle porte par migration :

$$
\boxed{t_i = \frac{j_i}{j}}
$$

avec $\sum_i t_i = 1$.

### Question 59

Dans une membrane échangeuse de cations **parfaite**, les anions $\mathrm{Cl^-}$ étant exclus (question 52), seul $\mathrm{Na^+}$ est mobile dans la membrane : tout le courant y est porté par $\mathrm{Na^+}$, d'où

$$
\boxed{t_m^{+} = 1}
$$

$$
\boxed{t_m^{-} = 0}
$$

---

## Partie IV — Électrodialyse industrielle

### Question 60

Sous l'effet du champ électrique, les cations $\mathrm{M^+}$ migrent vers la cathode et les anions $\mathrm{X^-}$ vers l'anode. Dans un compartiment de **type 1** (cathode/MEC/effluent 1/MEA/anode), les cations sortent par la MEC (côté cathode) et les anions par la MEA (côté anode) : le compartiment s'appauvrit en sel. Dans un compartiment de **type 2**, les ions entrent des compartiments voisins et y sont piégés : il s'enrichit.

```text
cathode │ MEC │ effluent 1 │ MEA │ anode      type 1 : appauvri  → diluat
cathode │ MEA │ effluent 2 │ MEC │ anode      type 2 : enrichi    → concentrat
```

$$
\boxed{C_1 < C_0 < C_2}
$$

Effluent 1 = diluat, effluent 2 = concentrat.

### Question 61

Sur la représentation de Cowan-Brown $U/j = f(1/j)$, à **très faible intensité** imposée, $1/j$ est très grand : le **point de départ est situé tout à droite** du graphe. Quand l'intensité augmente, $1/j$ diminue : le point de fonctionnement se déplace **vers la gauche** le long de la **branche ohmique** (portion de droite décroissante), jusqu'au voisinage de $1/j_{\text{lim}}$.

### Question 62

Dans le régime ohmique, la cellule se comporte comme un **électrolyseur** de caractéristique $U = E_{\text{seuil}} + R\,j$, d'où

$$
\frac{U}{j} = E_{\text{seuil}}\cdot\frac{1}{j} + R\;.
$$

La branche ohmique est donc une **droite affine en $1/j$**, de pente $E_{\text{seuil}}$ et d'ordonnée à l'origine $R$ : elle **ne passe pas par l'origine** (présence d'un seuil, apparenté à la tension de seuil d'un électrolyseur).

### Question 63

Au-delà de $j_{\text{lim}}$ (soit $1/j \le 1/j_{\text{lim}}$), la concentration en cations à la surface de la membrane tend vers zéro : le transport par les cations ne suffit plus à porter le courant, et une nouvelle réaction s'amorce, l'**autoprotolyse de l'eau** :

$$
\mathrm{2\,H_2O \rightarrow H_3O^+ + OH^-}\;.
$$

Les ions $\mathrm{H_3O^+}$, très mobiles, s'accumulent dans le diluat : d'où l'**acidification** observée (chute de pH).

### Question 64

Au-delà de $j_{\text{lim}}$, le courant est de plus en plus porté par les ions $\mathrm{H_3O^+}$ et $\mathrm{OH^-}$ issus de la dissociation de l'eau, et non par les ions du sel à transférer : le **rendement faradique chute** et la consommation énergétique augmente. On cherchera donc à faire travailler la cellule avec un courant **proche mais inférieur à $j_{\text{lim}}$**, dans le régime ohmique, pour maximiser le transfert utile tout en évitant la réaction parasite.

### Question 65

Le profil de la figure 15 montre une concentration de surface $C^+_{\text{sol},0} < C^+_{\text{sol},\infty}$ : le compartiment **B est appauvri** au voisinage de la membrane, c'est le **diluat (effluent 1)**. Les cations quittent B par la face anodique de la MEC et passent dans le compartiment voisin **A**, le **concentrat (effluent 2)** : dans A, le profil est symétrique mais inversé, avec une concentration de surface **supérieure** à celle du cœur (accumulation côté membrane).

### Question 66*

À la densité de courant limite, la déplétion en cations à la surface de la membrane est maximale :

$$
\boxed{C^+_{\text{sol},0} \to 0}\;.
$$

### Question 67

Lorsque $C^+_{\text{sol},0} \to 0$ (question 66), le flux de diffusion des cations vers la membrane, $\propto (C^+_{\text{sol},\infty} - C^+_{\text{sol},0})/\delta$, atteint sa valeur maximale et ne peut plus croître : le courant **sature à $j_{\text{lim}}$**, indépendamment de la tension appliquée. D'où le **plateau** de la caractéristique intensité-tension (régime limité par le transport de matière), conformément à la question 64.

### Question 68

La membrane contient une très forte concentration de charges fixes ($C_\Sigma \approx 5{,}5\ \mathrm{mol\cdot L^{-1}}$, question 44), qui impose une concentration en contre-ions quasi uniforme : les gradients de concentration y sont faibles et les co-ions exclus. Le terme de **diffusion** ($\propto \partial C/\partial x$) y est donc négligeable devant le terme de **migration**, gouverné par le champ électrique.

### Question 69

L'épaisseur $\delta$ de la couche de diffusion est fixée par l'**hydrodynamique de l'écoulement longitudinal** dans le compartiment (convection forcée, régime établi et stationnaire) : elle ne dépend pas du courant et reste **constante**.

### Question 70

L'annexe donne

$$
j = \frac{\mathcal F\,D^+_{\text{sol}}\,(C^+_{\text{sol},\infty} - C^+_{\text{sol},0})}{\delta\,(t_{+,m} - t_{+,sol})}\;.
$$

À la limite $C^+_{\text{sol},0} \to 0$ (question 66) et avec $t_{+,m} = 1$ (MEC parfaite, question 59) :

$$
\boxed{j_{\text{lim}} = \frac{\mathcal F\,D^+_{\text{sol}}\,C^+_{\text{sol},\infty}}{\delta\,(1 - t_{+,sol})}}\;.
$$

### Question 71*

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

On travaille à $j = 0{,}8\,j_{\text{lim}} = 0{,}8 \times 444 = 355{,}2\ \mathrm{A\cdot m^{-2}}$. Le lactate étant monovalent, la densité de flux de lactate liée au rendement faradique $R = 0{,}8$ est

$$
J_{\text{lactate}} = \frac{R\,j}{\mathcal F} = \frac{0{,}8 \times 355{,}2}{96\,500} \approx \boxed{2{,}94\times10^{-3}\ \mathrm{mol\cdot m^{-2}\cdot s^{-1}}}\;.
$$

### Question 74

La surface nécessaire est le rapport du flux à transférer à la densité de flux de lactate :

$$
S = \frac{F_{\text{trans}}}{J_{\text{lactate}}} = \frac{0{,}152}{2{,}94\times10^{-3}} \approx \boxed{52\ \mathrm{m^2}}\;.
$$

C'est l'ordre de grandeur de la surface totale de membrane nécessaire à l'opération.
