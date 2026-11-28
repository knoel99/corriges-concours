# Banque PT PT — Physique B - Chimie 2021 · Corrigé guidé

*Corrigé rédigé par IA, non officiel. Signalez toute erreur.*

**Rédaction** · modèle exact non renseigné (famille Claude) · effort non renseigné · vitesse non renseignée

## Présentation du sujet

**Thème.** Le zinc et son sulfure, en phase solide et en solution aqueuse. L'épreuve dure 2 heures, **sans calculatrice**, et comporte 39 questions réparties en quatre parties largement indépendantes, sans document à rendre : les diagrammes demandés se tracent sur la copie.

- *Partie A (questions 1 à 5)* : maille de la blende, coordinences, condition de tangence, rapport des rayons ioniques, masse volumique.
- *Partie B (questions 6 à 20)* : diagramme E-pH du zinc dans l'eau (attribution, frontières verticales, stabilité du métal), puis diagramme du couple sulfure de zinc/zinc en présence de soufre dissous (pentes, potentiel de palier, oxydation par le dioxygène).
- *Partie C (questions 21 à 28)* : dissolution du sulfure de zinc en milieu carbonate : grandeurs standard de réaction, constante d'équilibre, influence de la température, basicité de l'ion carbonate, combinaison de réactions.
- *Partie D (questions 29 à 39)* : précipitation homogène par décomposition de la thioacétamide (TAA) : loi de vitesse, intégration, exploitation d'une courbe, critère de précipitation, durée de l'opération.

**Notions mobilisées.** Cristaux ioniques, produit de solubilité, complexation, diagrammes potentiel-pH, relation de Nernst, couples acide-base et diagrammes de prédominance, loi de Hess, relation entre enthalpie libre standard et constante d'équilibre, loi de Van't Hoff, cinétique d'ordre 1 et dégénérescence de l'ordre.

**Difficulté.** Le sujet reste proche du cours des deux années, mais il est long : 39 questions en 120 minutes. Les questions les plus discriminantes d'après le rapport sont l'inégalité sur les rayons (question 3), l'application numérique de la masse volumique (question 5), le passage en milieu basique (questions 8 à 10), l'interprétation du second diagramme (question 20) et les bilans acido-basiques du carbonate (questions 27 et 28). Les données de l'énoncé comportent quelques coquilles (seconde constante d'acidité notée $\mathrm{p}K_{a1}$, « bicarbonate » pour carbonate) et deux incohérences numériques, signalées aux questions 28 et 35.

**Gestion du temps.** Environ 20 minutes pour la partie A, 40 pour la partie B, 30 pour la partie C et 30 pour la partie D. La partie D, souvent abandonnée faute de temps, contient pourtant plusieurs questions rapides (29 à 34, 37 et 38) : ne pas s'enliser dans la partie B.

> [!JURY]
> Le rapport 2021 rappelle que seule une réponse justifiée et argumentée reçoit tous les points, et qu'une valeur numérique sans unité n'est pas créditée. La présentation a été jugée soignée dans l'ensemble, mais l'orthographe et la syntaxe des réponses rédigées laissent à désirer. Le jury demande une attention particulière aux calculs d'ordre de grandeur, menés ici sans calculatrice.

[Sujet officiel](https://www.banquept.fr/documents/2021/ph_b_ch_2021_pt.pdf) · [Rapport du jury](https://www.banquept.fr/documents/ecrit/rapport/2021/rapport_phys_b_ecrit_2021.pdf)

*Mode d'emploi* : chercher chaque question seul, lire la première indication en cas de blocage, réessayer, puis la seconde, et seulement ensuite la solution.

## Partie A — Propriétés atomistiques et cristallographiques du zinc

### Question 1

> [!INDICATION]
> Commencer par le réseau des anions : un cube, un ion à chaque sommet et au centre de chaque face.

> [!INDICATION]
> Découper le cube en huit petits cubes d'arête $a/2$ : le centre de chacun est un site tétraédrique. N'en occuper qu'un sur deux, en alternance.

#### Solution

Les ions $\mathrm{S^{2-}}$ forment un réseau cubique à faces centrées : un ion à chacun des huit sommets du cube d'arête $a$ et un ion au centre de chacune des six faces.

Les sites tétraédriques sont les centres des huit petits cubes d'arête $a/2$. Les ions $\mathrm{Zn^{2+}}$ en occupent quatre, de façon alternée (deux sites voisins ne sont jamais occupés tous les deux), par exemple en $(\tfrac14,\tfrac14,\tfrac14)$, $(\tfrac34,\tfrac34,\tfrac14)$, $(\tfrac34,\tfrac14,\tfrac34)$ et $(\tfrac14,\tfrac34,\tfrac34)$.

![Figure 1 — Maille conventionnelle de la blende : ions sulfure aux sommets et aux centres des faces, ions zinc dans un site tétraédrique sur deux](figures/maille-blende.svg)

Population de la maille :

$$N(\mathrm{S^{2-}}) = 8\times\frac18 + 6\times\frac12 = 4$$

$$N(\mathrm{Zn^{2+}}) = 4\times 1 = 4$$

La maille contient **quatre motifs** $\mathrm{ZnS}$, ce qui respecte l'électroneutralité.

> [!JURY]
> Le rapport note que la maille cubique à faces centrées est connue, mais que les sites tétraédriques sont souvent mal placés. Les situer explicitement (centres des petits cubes d'arête $a/2$) et préciser lesquels sont occupés.

### Question 2

> [!INDICATION]
> Un site tétraédrique est, par définition, entouré de quatre atomes du réseau hôte.

> [!INDICATION]
> Pour l'anion, utiliser la stœchiométrie : il y a autant de cations que d'anions, donc les deux coordinences sont égales. On peut aussi compter : un anion touche huit sites tétraédriques, dont la moitié est occupée.

#### Solution

*Cation.* Un ion $\mathrm{Zn^{2+}}$ occupe le centre d'un petit cube d'arête $a/2$ dont quatre sommets (un sommet de la maille et trois centres de faces) portent un ion $\mathrm{S^{2-}}$. Il possède donc 4 plus proches voisins $\mathrm{S^{2-}}$, placés aux sommets d'un tétraèdre régulier.

*Anion.* Un ion $\mathrm{S^{2-}}$ est commun à huit petits cubes d'arête $a/2$, donc entouré de huit sites tétraédriques, dont un sur deux est occupé. Il possède donc 4 plus proches voisins $\mathrm{Zn^{2+}}$, eux aussi disposés en tétraèdre.

$$\boxed{\text{coordinence } 4 \text{ pour } \mathrm{Zn^{2+}} \text{ et } 4 \text{ pour } \mathrm{S^{2-}}}$$

Ce résultat est cohérent avec la stœchiométrie 1 : 1 du cristal, qui impose des coordinences égales.

> [!PIEGE]
> Les « plus proches voisins » d'un ion dans un cristal ionique sont les ions de signe opposé. Répondre 12 pour l'anion (ses voisins anions dans le réseau cubique à faces centrées) n'est pas ce qui est demandé.

### Question 3

> [!INDICATION]
> Le cation est au centre d'un petit cube d'arête $a/2$ et l'anion à l'un de ses sommets : la distance qui les sépare est une demi-diagonale de ce petit cube.

> [!INDICATION]
> Pour l'inégalité : les anions les plus proches sont sur la diagonale d'une face. Ils ne doivent pas s'interpénétrer. Éliminer $a$ entre cette condition et la condition de tangence.

#### Solution

**Tangence et distance cation-anion.** Dans le modèle des sphères dures, le cation et l'anion sont en contact. Le cation est au centre d'un petit cube d'arête $a/2$, l'anion à un sommet : leur distance est la demi-diagonale de ce petit cube, soit le quart de la grande diagonale de la maille.

$$d(\mathrm{Zn^{2+}}\text{–}\,\mathrm{S^{2-}}) = \frac12\times\frac{a}{2}\sqrt3$$

$$\boxed{R(\mathrm{Zn^{2+}}) + R(\mathrm{S^{2-}}) = d = \frac{a\sqrt3}{4}}$$

**Inégalité.** Les anions les plus proches sont alignés sur la diagonale d'une face (sommet, centre de la face), à la distance $a\sqrt2/2$. Ils ne peuvent pas s'interpénétrer (au mieux, ils se touchent) :

$$2\,R(\mathrm{S^{2-}}) \leqslant \frac{a\sqrt2}{2}$$

soit

$$a \geqslant 2\sqrt2\,R(\mathrm{S^{2-}})$$

En reportant dans la condition de tangence :

$$R(\mathrm{Zn^{2+}}) + R(\mathrm{S^{2-}}) = \frac{a\sqrt3}{4} \geqslant \frac{\sqrt3}{4}\times 2\sqrt2\,R(\mathrm{S^{2-}}) = \sqrt{\frac32}\,R(\mathrm{S^{2-}})$$

$$\boxed{\frac{R(\mathrm{Zn^{2+}})}{R(\mathrm{S^{2-}})} \geqslant \sqrt{\frac32} - 1 \approx 0{,}22}$$

> [!METHODE]
> Dans un cristal ionique : contact entre ions de signes opposés (égalité), non-recouvrement entre ions de même signe (inégalité). L'élimination du paramètre de maille entre les deux donne la borne inférieure du rapport des rayons pour le type de site considéré.

> [!JURY]
> D'après le rapport, beaucoup de candidats n'ont pas su déduire l'inégalité sur les rayons. La valeur $\sqrt{3/2} \approx 1{,}22$ donnée à la question suivante indique la forme attendue du résultat.

### Question 4

> [!INDICATION]
> Simplifier la fraction avant de calculer : $74/184 = 37/92$.

> [!INDICATION]
> Comparer à la borne de la question 3. On peut aussi comparer $R_+ + R_-$ à la distance $a\sqrt3/4$ calculée avec $a = 541$ pm.

#### Solution

$$\frac{R(\mathrm{Zn^{2+}})}{R(\mathrm{S^{2-}})} = \frac{74{,}0}{184} = \frac{37}{92} \approx 0{,}40$$

$$\boxed{\frac{R(\mathrm{Zn^{2+}})}{R(\mathrm{S^{2-}})} \approx 0{,}40 \geqslant \sqrt{\frac32} - 1 \approx 0{,}22}$$

**Commentaire.** L'inégalité de la question 3 est vérifiée : le cation est assez gros pour écarter les anions, qui ne sont donc pas en contact, et l'occupation des sites tétraédriques est géométriquement possible. La valeur 0,40 reste inférieure à $\sqrt2 - 1 \approx 0{,}41$, seuil à partir duquel un cation tient dans un site octaédrique en touchant ses six voisins : la coordinence 4 est bien celle que l'on attend.

Le modèle des sphères dures n'est cependant qu'approché. Avec $\sqrt3/2 = \sqrt{3/2}/\sqrt2 \approx 0{,}87$, la tangence donnerait

$$\frac{a\sqrt3}{4} \approx \frac{541\times 0{,}87}{2} \approx 234\ \mathrm{pm}$$

alors que la somme des rayons ioniques vaut $184 + 74 = 258\ \mathrm{pm}$. L'écart, de l'ordre de 10 %, traduit le caractère partiellement covalent de la liaison zinc-soufre.

### Question 5

> [!INDICATION]
> Une maille contient quatre motifs $\mathrm{ZnS}$ : exprimer sa masse à l'aide de la constante d'Avogadro, puis diviser par le volume $a^3$.

> [!INDICATION]
> Convertir avant de calculer : $a = 5{,}41\cdot 10^{-10}$ m et $M = 97{,}5\cdot 10^{-3}\ \mathrm{kg\cdot mol^{-1}}$. Arrondir $5{,}41^3$ à environ 158.

#### Solution

La maille, de volume $a^3$, contient 4 motifs $\mathrm{ZnS}$ de masse molaire $M(\mathrm{ZnS}) = M(\mathrm{Zn}) + M(\mathrm S) = 97{,}5\ \mathrm{g\cdot mol^{-1}}$ :

$$\boxed{\rho = \frac{4\,\bigl[M(\mathrm{Zn}) + M(\mathrm S)\bigr]}{\mathcal N_A\,a^3}}$$

Application numérique, en unités SI ($a = 5{,}41\cdot 10^{-10}\ \mathrm m$) :

$$a^3 \approx 5{,}4^3\cdot 10^{-30} \approx 1{,}6\cdot 10^{-28}\ \mathrm{m^3}$$

$$\mathcal N_A\,a^3 \approx 6{,}02\cdot 10^{23}\times 1{,}6\cdot 10^{-28} \approx 9{,}5\cdot 10^{-5}\ \mathrm{m^3\cdot mol^{-1}}$$

$$\rho \approx \frac{4\times 97{,}5\cdot 10^{-3}}{9{,}5\cdot 10^{-5}} = \frac{0{,}39}{9{,}5\cdot 10^{-5}}$$

$$\boxed{\rho \approx 4{,}1\cdot 10^{3}\ \mathrm{kg\cdot m^{-3}} = 4{,}1\ \mathrm{g\cdot cm^{-3}}}$$

L'ordre de grandeur est celui d'un solide minéral (quelques fois la masse volumique de l'eau).

> [!PIEGE]
> Les conversions font perdre le résultat : $1\ \mathrm{pm} = 10^{-12}\ \mathrm m$, donc $a^3$ est en $10^{-30}\ \mathrm{m^3}$ si $a$ est écrit en centaines de picomètres ($5{,}41\cdot 10^{-10}$ m). Ne pas oublier de passer la masse molaire en kilogrammes par mole.

> [!JURY]
> Le rapport signale des confusions entre compacité et masse volumique, des erreurs de conversion et des ordres de grandeur aberrants. Un contrôle rapide s'impose : un solide a une masse volumique de $10^3$ à $2\cdot 10^4\ \mathrm{kg\cdot m^{-3}}$. Il rappelle aussi qu'une valeur sans unité n'est pas créditée.

## Partie B — Diagrammes du zinc en solution aqueuse et en solution de sulfure

### Question 6

> [!INDICATION]
> L'hydroxyde de zinc est amphotère : il se dissout en cation $\mathrm{Zn^{2+}}$ du côté acide et en complexe $\mathrm{Zn(OH)_4^{2-}}$ du côté basique.

> [!INDICATION]
> Classer les espèces par nombre d'oxydation (vertical) puis, pour le zinc(II), par nombre de ligands hydroxyde croissant de gauche à droite.

#### Solution

Dissolution du précipité en ions $\mathrm{Zn^{2+}}$ :

$$\mathrm{Zn(OH)_2(s)} = \mathrm{Zn^{2+}(aq)} + 2\,\mathrm{HO^-(aq)} \qquad K_{s1} = 10^{-17}$$

(en milieu acide, le bilan s'écrit $\mathrm{Zn(OH)_2(s)} + 2\,\mathrm{H_3O^+} = \mathrm{Zn^{2+}} + 4\,\mathrm{H_2O}$).

Dissolution du précipité en ions $\mathrm{Zn(OH)_4^{2-}}$, en milieu basique :

$$\mathrm{Zn(OH)_2(s)} + 2\,\mathrm{HO^-(aq)} = \mathrm{Zn(OH)_4^{2-}(aq)}$$

**Attribution des domaines.** Le zinc est au nombre d'oxydation 0 dans $\mathrm{Zn(s)}$ et $+\mathrm{II}$ dans les trois autres espèces. Le métal occupe donc la partie basse du diagramme (potentiels les plus faibles). Les trois espèces du zinc(II) se succèdent de gauche à droite dans l'ordre des pH croissants, c'est-à-dire du nombre croissant d'ions hydroxyde fixés, séparées par les deux frontières verticales (aucun échange d'électron entre elles) :

| Zone | Espèce | Nature du domaine |
|---|---|---|
| en haut à gauche (pH inférieur à 6,5 environ) | $\mathrm{Zn^{2+}(aq)}$ | prédominance |
| en haut au centre | $\mathrm{Zn(OH)_2(s)}$ | existence |
| en haut à droite (pH supérieur à 13,5 environ) | $\mathrm{Zn(OH)_4^{2-}(aq)}$ | prédominance |
| en bas, sur toute la largeur | $\mathrm{Zn(s)}$ | existence |

![Figure 2 — Diagramme E-pH du zinc avec les espèces attribuées et, en tirets, les deux frontières des couples de l'eau](figures/diagramme-e-ph-zinc.svg)

La frontière du couple $\mathrm{Zn^{2+}/Zn}$ est horizontale, à $E = -0{,}76 + 0{,}03\log(10^{-2}) = -0{,}82\ \mathrm V$, ce qui correspond bien au palier lu sur la figure 1 du sujet.

> [!METHODE]
> Deux règles suffisent pour attribuer un diagramme E-pH : le nombre d'oxydation croît de bas en haut ; à nombre d'oxydation égal, les espèces les plus basiques (les plus riches en $\mathrm{HO^-}$) sont à droite. Une espèce dissoute a un domaine de prédominance, un solide un domaine d'existence.

### Question 7

> [!INDICATION]
> À l'apparition du premier grain de solide, le produit de solubilité est tout juste vérifié avec $[\mathrm{Zn^{2+}}] = 10^{-2}\ \mathrm{mol\cdot L^{-1}}$.

> [!INDICATION]
> En déduire $[\mathrm{HO^-}]$, puis le pH par $\mathrm{pH} = 14 - \mathrm{pOH}$.

#### Solution

Au début de la précipitation, le solide existe à l'état de trace et la concentration en ions $\mathrm{Zn^{2+}}$ vaut encore $c = 10^{-2}\ \mathrm{mol\cdot L^{-1}}$. L'équilibre de dissolution est établi (concentrations rapportées à $c^\circ = 1\ \mathrm{mol\cdot L^{-1}}$) :

$$K_{s1} = [\mathrm{Zn^{2+}}]\,[\mathrm{HO^-}]^2$$

$$[\mathrm{HO^-}] = \sqrt{\frac{K_{s1}}{c}} = \sqrt{\frac{10^{-17}}{10^{-2}}} = 10^{-7{,}5}\ \mathrm{mol\cdot L^{-1}}$$

$$\mathrm{pH} = \mathrm{p}K_e - \mathrm{pOH} = 14 - 7{,}5$$

$$\boxed{\mathrm{pH} = 6{,}5}$$

Cette valeur est celle de la première frontière verticale de la figure 1 du sujet, située entre les graduations 6 et 7.

> [!PIEGE]
> Le produit de solubilité fait intervenir $[\mathrm{HO^-}]$ et non $[\mathrm{H_3O^+}]$ : on obtient d'abord pOH = 7,5. Le produit ionique de l'eau, $K_e = 10^{-14}$ à 298 K, n'est pas rappelé par l'énoncé mais doit être connu.

### Question 8

> [!INDICATION]
> On est en milieu basique : le réactif qui redissout le solide est l'ion hydroxyde, pas l'eau ni l'ion oxonium.

#### Solution

En milieu basique, l'hydroxyde solide fixe deux ions hydroxyde supplémentaires :

$$\boxed{\mathrm{Zn(OH)_2(s)} + 2\,\mathrm{HO^-(aq)} = \mathrm{Zn(OH)_4^{2-}(aq)}}$$

> [!JURY]
> Le rapport indique que cette équation, qui traduit le passage en milieu basique, a été très souvent mal écrite. Vérifier la conservation des éléments et des charges, et n'employer que des espèces compatibles avec le pH du milieu.

### Question 9

> [!INDICATION]
> Écrire le quotient de réaction à l'équilibre : le solide n'y figure pas.

> [!INDICATION]
> La réaction est la somme de la dissolution de l'hydroxyde ($K_{s1}$) et de la formation du complexe ($K_c$) : les constantes se multiplient.

#### Solution

Le solide a une activité égale à 1 :

$$K = \frac{[\mathrm{Zn(OH)_4^{2-}}]}{[\mathrm{HO^-}]^2}$$

La réaction de la question 8 est la somme de deux réactions de constantes connues :

$$\mathrm{Zn(OH)_2(s)} = \mathrm{Zn^{2+}} + 2\,\mathrm{HO^-} \qquad K_{s1} = 10^{-17}$$

$$\mathrm{Zn^{2+}} + 4\,\mathrm{HO^-} = \mathrm{Zn(OH)_4^{2-}} \qquad K_c = 10^{16}$$

En multipliant numérateur et dénominateur de $K$ par $[\mathrm{Zn^{2+}}]\,[\mathrm{HO^-}]^2$, on fait apparaître ces deux constantes :

$$K = K_{s1}\,K_c = 10^{-17}\times 10^{16}$$

$$\boxed{K = \frac{[\mathrm{Zn(OH)_4^{2-}}]}{[\mathrm{HO^-}]^2} = K_{s1}\,K_c = 10^{-1}}$$

### Question 10

> [!INDICATION]
> Sur cette frontière, le solide est sur le point de disparaître : l'équilibre de la question 8 est établi avec $[\mathrm{Zn(OH)_4^{2-}}] = 10^{-2}\ \mathrm{mol\cdot L^{-1}}$.

#### Solution

Sur la frontière entre $\mathrm{Zn(OH)_2(s)}$ et $\mathrm{Zn(OH)_4^{2-}}$, l'équilibre de la question 8 est établi et la concentration du complexe vaut la concentration de tracé $c = 10^{-2}\ \mathrm{mol\cdot L^{-1}}$ :

$$[\mathrm{HO^-}]^2 = \frac{c}{K} = \frac{10^{-2}}{10^{-1}} = 10^{-1}$$

$$[\mathrm{HO^-}] = 10^{-0{,}5}\ \mathrm{mol\cdot L^{-1}}$$

$$\mathrm{pH} = 14 - 0{,}5$$

$$\boxed{\mathrm{pH} = 13{,}5}$$

La figure 1 du sujet place bien cette frontière entre les graduations 13 et 14.

> [!METHODE]
> Toute frontière verticale d'un diagramme E-pH se calcule ainsi : équilibre acido-basique ou de précipitation établi, espèce dissoute à la concentration de tracé. Contrôler chaque valeur sur la figure du sujet.

### Question 11

> [!INDICATION]
> L'eau intervient dans deux couples : comme réducteur avec le dioxygène, comme oxydant avec le dihydrogène.

> [!INDICATION]
> Écrire la relation de Nernst de chaque couple avec des pressions de 1 bar : les deux droites ont la même pente, $-0{,}06$ V par unité de pH.

#### Solution

L'allure demandée est celle de la figure 2 ci-dessus : deux droites parallèles en tirets, de pente $-0{,}06\ \mathrm V$ par unité de pH, qui délimitent trois domaines.

*Couple* $\mathrm{O_2(g)/H_2O}$ (droite supérieure) :

$$\mathrm{O_2(g)} + 4\,\mathrm{H^+} + 4\,e^- = 2\,\mathrm{H_2O}$$

$$E = 1{,}23 - 0{,}06\,\mathrm{pH} \quad (\text{en V, pour } P_{\mathrm{O_2}} = 1\ \mathrm{bar})$$

*Couple* $\mathrm{H^+/H_2(g)}$, c'est-à-dire $\mathrm{H_2O/H_2}$ (droite inférieure) :

$$2\,\mathrm{H^+} + 2\,e^- = \mathrm{H_2(g)}$$

$$E = -0{,}06\,\mathrm{pH} \quad (\text{en V, pour } P_{\mathrm{H_2}} = 1\ \mathrm{bar})$$

Attribution : **le dioxygène** au-dessus de la droite supérieure (l'eau y est oxydée), **l'eau** entre les deux droites (domaine de stabilité thermodynamique de l'eau), **le dihydrogène** au-dessous de la droite inférieure (l'eau y est réduite). Contrôle sur la figure 1 du sujet : les droites en pointillé partent de 1,23 V et de 0 V à pH = 0 et arrivent vers 0,39 V et $-0{,}84$ V à pH = 14.

### Question 12

> [!INDICATION]
> Comparer, à chaque pH, la position du domaine de $\mathrm{Zn(s)}$ et celle du domaine de l'eau : ont-ils une partie commune ?

> [!INDICATION]
> Préciser le produit d'oxydation selon le pH (trois zones) et écrire les bilans avec des espèces compatibles avec le milieu.

#### Solution

Quel que soit le pH, la frontière supérieure du domaine de $\mathrm{Zn(s)}$ est située sous la droite du couple $\mathrm{H_2O/H_2}$ : l'écart vaut 0,82 V à pH = 0, il se réduit à environ 0,43 V à pH = 6,5, reste constant jusqu'à pH = 13,5 (pentes égales), puis augmente à nouveau. Les domaines du zinc et de l'eau sont **disjoints à tout pH**.

$$\boxed{\text{Le zinc métallique est thermodynamiquement instable dans l'eau à tout pH}}$$

Il est oxydé par l'eau avec dégagement de dihydrogène, en un produit qui dépend du pH :

- pH inférieur à 6,5 : $\mathrm{Zn(s)} + 2\,\mathrm{H_3O^+} = \mathrm{Zn^{2+}} + \mathrm{H_2(g)} + 2\,\mathrm{H_2O}$ ;
- pH compris entre 6,5 et 13,5 : $\mathrm{Zn(s)} + 2\,\mathrm{H_2O} = \mathrm{Zn(OH)_2(s)} + \mathrm{H_2(g)}$ ;
- pH supérieur à 13,5 : $\mathrm{Zn(s)} + 2\,\mathrm{HO^-} + 2\,\mathrm{H_2O} = \mathrm{Zn(OH)_4^{2-}} + \mathrm{H_2(g)}$.

Le milieu acide est donc un domaine de corrosion (comme le milieu très basique), tandis qu'entre pH 6,5 et 13,5 la couche d'hydroxyde solide peut protéger le métal (passivation). Le diagramme ne renseigne que sur la thermodynamique : en pratique, la réduction de l'eau sur le zinc est lente, ce qui explique que l'attaque soit peu visible dans l'eau neutre.

> [!JURY]
> Le rapport reproche aux candidats d'introduire des ions oxonium ou hydroxyde dans les bilans sans se soucier du pH du milieu. Écrire $\mathrm{H_3O^+}$ en milieu acide, $\mathrm{H_2O}$ en milieu neutre, $\mathrm{HO^-}$ en milieu basique.

### Question 13

> [!INDICATION]
> Le cristal est ionique : revenir aux ions décrits dans la partie A.

#### Solution

Le sulfure de zinc est constitué d'ions $\mathrm{Zn^{2+}}$ et $\mathrm{S^{2-}}$ (le soufre, plus électronégatif, est au nombre d'oxydation $-\mathrm{II}$) :

$$\boxed{\text{n.o.}(\mathrm{Zn}) = +\mathrm{II} \text{ dans } \mathrm{ZnS(s)}}$$

Le précipité se forme à partir de l'ion $\mathrm{Zn^{2+}(aq)}$ et de l'ion sulfure $\mathrm{S^{2-}(aq)}$ :

$$\mathrm{Zn^{2+}(aq)} + \mathrm{S^{2-}(aq)} = \mathrm{ZnS(s)} \qquad K = \frac{1}{K_{s2}} = 10^{20}$$

Selon le pH, le soufre dissous qui apporte l'ion sulfure est majoritairement sous forme $\mathrm{H_2S}$, $\mathrm{HS^-}$ ou $\mathrm{S^{2-}}$ (question 14).

### Question 14

> [!INDICATION]
> $\mathrm{H_2S}$ est un diacide : deux frontières, placées aux deux $\mathrm{p}K_a$. L'espèce la plus acide prédomine aux pH les plus faibles.

#### Solution

$\mathrm{H_2S}$ est un diacide de constantes $\mathrm{p}K_{a1} = 7$ et $\mathrm{p}K_{a2} = 13$ (la seconde valeur, notée par erreur $\mathrm{p}K_{a1}$ dans les données, est celle du couple $\mathrm{HS^-/S^{2-}}$). Une forme acide prédomine sur sa base conjuguée lorsque $\mathrm{pH} < \mathrm{p}K_a$ :

```text
        H2S prédomine     |     HS- prédomine     |   S2- prédomine
  ------------------------+-----------------------+-----------------> pH
  0                       7                      13              14
                        pKa1                    pKa2
```

### Question 15

> [!INDICATION]
> Écrire les deux constantes d'acidité, puis leur produit : on relie directement $[\mathrm{S^{2-}}]$ à $[\mathrm{H_2S}]$ et à $[\mathrm{H_3O^+}]$.

> [!INDICATION]
> Le diagramme est tracé en donnant la valeur $c = 10^{-6}\ \mathrm{mol\cdot L^{-1}}$ à l'espèce du soufre qui prédomine : distinguer les trois domaines de la question 14.

#### Solution

On note $h = [\mathrm{H_3O^+}] = 10^{-\mathrm{pH}}$ et $c = 10^{-6}\ \mathrm{mol\cdot L^{-1}}$ la concentration en soufre dissous. Les constantes d'acidité s'écrivent

$$K_{a1} = \frac{[\mathrm{HS^-}]\,h}{[\mathrm{H_2S}]}$$

$$K_{a2} = \frac{[\mathrm{S^{2-}}]\,h}{[\mathrm{HS^-}]}$$

La conservation du soufre dissous donne

$$c = [\mathrm{H_2S}] + [\mathrm{HS^-}] + [\mathrm{S^{2-}}] = [\mathrm{S^{2-}}]\left(1 + \frac{h}{K_{a2}} + \frac{h^2}{K_{a1}K_{a2}}\right)$$

$$\boxed{[\mathrm{S^{2-}}] = \frac{c}{1 + \dfrac{h}{K_{a2}} + \dfrac{h^2}{K_{a1}K_{a2}}}}$$

Dans chaque domaine de prédominance, un seul terme du dénominateur domine (c'est la convention de tracé de l'énoncé, qui attribue la concentration $c$ à l'espèce prédominante) :

| Domaine | Espèce à la concentration $c$ | $[\mathrm{S^{2-}}]$ | $\log[\mathrm{S^{2-}}]$ |
|---|---|---|---|
| pH < 7 | $\mathrm{H_2S}$ | $K_{a1}K_{a2}\,c/h^2$ | $2\,\mathrm{pH} - 26$ |
| 7 < pH < 13 | $\mathrm{HS^-}$ | $K_{a2}\,c/h$ | $\mathrm{pH} - 19$ |
| pH > 13 | $\mathrm{S^{2-}}$ | $c$ | $-6$ |

> [!METHODE]
> Raisonner domaine par domaine : l'espèce prédominante porte la concentration de tracé, les autres s'en déduisent par les constantes d'acidité. C'est cette forme simplifiée, linéaire en pH, qui sert aux questions 17 à 19.

### Question 16

> [!INDICATION]
> En présence du précipité, le zinc(II) est sous forme $\mathrm{ZnS(s)}$ : c'est lui l'oxydant du couple.

#### Solution

En présence du précipité, le zinc(II) est engagé dans $\mathrm{ZnS(s)}$ :

$$\boxed{\mathrm{ZnS(s)} + 2\,e^- = \mathrm{Zn(s)} + \mathrm{S^{2-}(aq)}}$$

Selon l'espèce du soufre qui prédomine, la même demi-équation s'écrit aussi

$$\mathrm{ZnS(s)} + \mathrm{H^+} + 2\,e^- = \mathrm{Zn(s)} + \mathrm{HS^-} \qquad (7 < \mathrm{pH} < 13)$$

$$\mathrm{ZnS(s)} + 2\,\mathrm{H^+} + 2\,e^- = \mathrm{Zn(s)} + \mathrm{H_2S} \qquad (\mathrm{pH} < 7)$$

### Question 17

> [!INDICATION]
> À quels pH la pente change-t-elle sur la figure 2 du sujet ? Rapprocher ces valeurs des données.

> [!INDICATION]
> La pente d'une frontière vaut $-0{,}06\,m/n$ pour $m$ protons et $n$ électrons échangés : compter les protons dans chacune des trois écritures de la question 16.

#### Solution

Sur la figure 2 du sujet, la pente change à pH = 7 et à pH = 13, c'est-à-dire aux deux $\mathrm{p}K_a$ du diacide $\mathrm{H_2S}$. À chacun de ces pH, l'espèce prédominante du soufre dissous change, donc la demi-équation à considérer aussi, et avec elle le nombre de protons échangés pour deux électrons :

- pH < 7 : le soufre libéré est sous forme $\mathrm{H_2S}$, deux protons sont consommés, le potentiel décroît fortement avec le pH ;
- 7 < pH < 13 : il est sous forme $\mathrm{HS^-}$, un seul proton intervient, la pente est deux fois plus faible ;
- pH > 13 : il est sous forme $\mathrm{S^{2-}}$, aucun proton n'intervient, la frontière est horizontale.

De façon équivalente, le potentiel dépend de $\log[\mathrm{S^{2-}}]$, dont la loi en fonction du pH change à chaque $\mathrm{p}K_a$ (question 15). La frontière est continue, seule sa pente est rompue.

![Figure 3 — Frontière entre le sulfure de zinc et le zinc : trois segments dont la pente change aux deux pKa du sulfure de dihydrogène](figures/diagramme-e-ph-zinc-sulfure.svg)

### Question 18

> [!INDICATION]
> Écrire la relation de Nernst du couple $\mathrm{Zn^{2+}/Zn}$, puis remplacer $[\mathrm{Zn^{2+}}]$ par $K_{s2}/[\mathrm{S^{2-}}]$ puisque le précipité est présent.

> [!INDICATION]
> Pour pH > 13, $[\mathrm{S^{2-}}] = 10^{-6}\ \mathrm{mol\cdot L^{-1}}$.

#### Solution

En présence de $\mathrm{ZnS(s)}$, l'équilibre de précipitation impose $[\mathrm{Zn^{2+}}] = K_{s2}/[\mathrm{S^{2-}}]$. Le potentiel du couple $\mathrm{Zn^{2+}/Zn}$, égal à celui du couple $\mathrm{ZnS/Zn}$, s'écrit

$$E = E^\circ(\mathrm{Zn^{2+}/Zn}) + \frac{0{,}06}{2}\,\log[\mathrm{Zn^{2+}}]$$

$$E = E^\circ(\mathrm{Zn^{2+}/Zn}) + 0{,}03\,\log K_{s2} - 0{,}03\,\log[\mathrm{S^{2-}}]$$

Le potentiel standard du couple $\mathrm{ZnS/Zn}$ vaut donc

$$E^\circ(\mathrm{ZnS/Zn}) = -0{,}76 - 0{,}03\times 20 = -1{,}36\ \mathrm V$$

Pour pH > 13, l'ion sulfure prédomine et $[\mathrm{S^{2-}}] = 10^{-6}\ \mathrm{mol\cdot L^{-1}}$ :

$$E = -1{,}36 - 0{,}03\times(-6) = -1{,}36 + 0{,}18$$

$$\boxed{E = -1{,}18\ \mathrm V \quad (\mathrm{pH} > 13)}$$

C'est la valeur du palier lu sur la figure 2 du sujet, juste au-dessus de la graduation $-1{,}2$ V.

> [!PIEGE]
> Le signe : $\log K_{s2} = -20$ abaisse le potentiel standard (le précipité stabilise le zinc(II)), tandis que $-0{,}03\log[\mathrm{S^{2-}}]$ est positif car la concentration est inférieure à $1\ \mathrm{mol\cdot L^{-1}}$.

### Question 19

> [!INDICATION]
> Reprendre l'expression du potentiel de la question 18 et y reporter $\log[\mathrm{S^{2-}}] = \mathrm{pH} - 19$.

#### Solution

Entre pH 7 et pH 13, l'espèce $\mathrm{HS^-}$ prédomine et, d'après la question 15, $\log[\mathrm{S^{2-}}] = \mathrm{pH} - 19$. L'expression de la question 18 devient

$$E = -1{,}36 - 0{,}03\,(\mathrm{pH} - 19)$$

$$E = -0{,}79 - 0{,}03\,\mathrm{pH} \quad (\text{en V})$$

$$\boxed{\text{pente} = -0{,}03\ \mathrm{V\ par\ unité\ de\ pH}}$$

On retrouve ce résultat avec la demi-équation $\mathrm{ZnS(s)} + \mathrm{H^+} + 2\,e^- = \mathrm{Zn(s)} + \mathrm{HS^-}$ : un proton pour deux électrons, soit une pente de $-0{,}06\times\tfrac12$.

Contrôle sur la figure 2 du sujet : la frontière passe de $-1{,}00$ V à pH = 7 à $-1{,}18$ V à pH = 13, soit $-0{,}18$ V pour 6 unités de pH. Le même calcul pour pH < 7 donne $E = -0{,}58 - 0{,}06\,\mathrm{pH}$, en accord avec l'ordonnée à l'origine lue ($-0{,}58$ V).

### Question 20

> [!INDICATION]
> Placer à pH = 8 le potentiel du couple $\mathrm{O_2/H_2O}$ et celui de la frontière $\mathrm{ZnS/Zn}$ : les domaines du dioxygène et du zinc ont-ils une partie commune ?

> [!INDICATION]
> À pH = 8, le soufre dissous est sous forme $\mathrm{HS^-}$ et le milieu est légèrement basique : équilibrer le bilan avec $\mathrm{HO^-}$ plutôt qu'avec $\mathrm{H_3O^+}$.

#### Solution

À pH = 8, la frontière du couple $\mathrm{O_2/H_2O}$ est à

$$E = 1{,}23 - 0{,}06\times 8 = 0{,}75\ \mathrm V$$

et celle du couple $\mathrm{ZnS/Zn}$, lue sur la figure 2 du sujet ou calculée par la question 19, à

$$E = -0{,}79 - 0{,}03\times 8 = -1{,}03\ \mathrm V$$

Le domaine du dioxygène (au-dessus de 0,75 V) et celui du zinc (au-dessous de $-1{,}03$ V) sont disjoints, avec un écart de près de 1,8 V : en présence de soufre dissous, le dioxygène de l'air oxyde quantitativement le zinc en sulfure de zinc, espèce stable du zinc dans tout le domaine situé au-dessus de la frontière.

À pH = 8, le soufre dissous est sous forme $\mathrm{HS^-}$ (question 14). Les demi-équations sont

$$\mathrm{Zn(s)} + \mathrm{HS^-} = \mathrm{ZnS(s)} + \mathrm{H^+} + 2\,e^-$$

$$\mathrm{O_2(g)} + 4\,\mathrm{H^+} + 4\,e^- = 2\,\mathrm{H_2O}$$

La combinaison de deux fois la première et de la seconde donne $2\,\mathrm{Zn} + 2\,\mathrm{HS^-} + \mathrm{O_2} + 2\,\mathrm{H^+} = 2\,\mathrm{ZnS} + 2\,\mathrm{H_2O}$. Le milieu étant légèrement basique, on ajoute $2\,\mathrm{HO^-}$ de chaque côté pour ne pas faire figurer d'ions $\mathrm{H^+}$ :

$$\boxed{2\,\mathrm{Zn(s)} + \mathrm{O_2(g)} + 2\,\mathrm{HS^-(aq)} = 2\,\mathrm{ZnS(s)} + 2\,\mathrm{HO^-(aq)}}$$

(Conservation vérifiée : 2 Zn, 2 S, 2 O, 2 H et une charge $-2$ de chaque côté.)

> [!JURY]
> Le rapport constate que le second diagramme a été mal exploité pour interpréter cette oxydation, et que les bilans comportaient des ions sans rapport avec le pH du milieu. Deux réflexes : comparer les domaines à pH = 8, puis choisir l'espèce du soufre qui prédomine à ce pH.

## Partie C — Thermodynamique de la dissolution du sulfure de zinc en solution aqueuse

### Question 21

> [!INDICATION]
> L'ion carbonate figure dans un couple acide-base des données : y joue-t-il le rôle de l'acide ou de la base ? L'ion sodium est indifférent.

#### Solution

Le carbonate de sodium se dissocie totalement en ions $\mathrm{Na^+}$, indifférents du point de vue acido-basique, et en ions carbonate $\mathrm{CO_3^{2-}}$. L'ion carbonate est la base du couple $\mathrm{HCO_3^-/CO_3^{2-}}$ ($\mathrm{p}K_{a4} = 10{,}3$) : selon Brönsted, il capte un proton de l'eau.

$$\mathrm{CO_3^{2-}(aq)} + \mathrm{H_2O} = \mathrm{HCO_3^-(aq)} + \mathrm{HO^-(aq)}$$

Cette réaction produit des ions hydroxyde, donc $[\mathrm{HO^-}] > [\mathrm{H_3O^+}]$ :

$$\boxed{\text{la solution est basique } (\mathrm{pH} > 7)}$$

C'est ce qui rend possible la réaction (1), qui consomme des ions hydroxyde.

> [!JURY]
> Le rapport regrette que trop de candidats ignorent la définition d'un acide ou d'une base selon Brönsted et ne sachent pas identifier les espèces acido-basiques présentes. Nommer le couple, citer son $\mathrm{p}K_a$, écrire la réaction avec l'eau.

### Question 22

> [!INDICATION]
> Distinguer l'état standard d'un constituant (pression $P^\circ$, comportement idéal) et l'état standard de référence d'un élément (corps simple le plus stable à la température considérée).

> [!INDICATION]
> Une réaction de formation fabrique une mole du composé à partir des corps simples pris dans leur état standard de référence.

#### Solution

**État standard.** L'état standard d'un constituant physico-chimique, à une température $T$, est un état conventionnel défini à la pression standard $P^\circ = 1\ \mathrm{bar}$ :

- pour un gaz, le gaz parfait pur sous $P^\circ$ ;
- pour un solide ou un liquide, le corps pur dans le même état physique sous $P^\circ$ ;
- pour un soluté, le soluté à la concentration $c^\circ = 1\ \mathrm{mol\cdot L^{-1}}$ sous $P^\circ$, se comportant comme en solution infiniment diluée.

**État standard de référence.** L'état standard de référence d'un élément chimique, à la température $T$, est l'état standard du corps simple le plus stable de cet élément, dans son état physique le plus stable à cette température. À 298 K : $\mathrm{Zn(s)}$ pour le zinc, $\mathrm{S(s)}$ pour le soufre. L'enthalpie standard de formation d'un tel corps simple est nulle, ce qui explique les deux cases vides du tableau de données.

**Réaction de formation.** L'enthalpie standard de formation de $\mathrm{ZnS(s)}$ est l'enthalpie standard de la réaction qui forme une mole de $\mathrm{ZnS(s)}$ à partir de ses éléments pris dans leur état standard de référence :

$$\boxed{\mathrm{Zn(s)} + \mathrm{S(s)} = \mathrm{ZnS(s)} \qquad \Delta_f H^\circ(\mathrm{ZnS}) = -203\ \mathrm{kJ\cdot mol^{-1}}}$$

### Question 23

> [!INDICATION]
> Loi de Hess : somme des grandeurs de formation pondérées par les nombres stœchiométriques algébriques (positifs pour les produits, négatifs pour les réactifs). Même combinaison pour les entropies molaires standard.

> [!INDICATION]
> Attention au coefficient 3 de l'ion hydroxyde et aux signes : $-3\times(-230) = +690$.

#### Solution

Pour la réaction (1), $\mathrm{ZnS(s)} + 3\,\mathrm{HO^-} + \mathrm{H_2O} = \mathrm{Zn(OH)_4^{2-}} + \mathrm{HS^-}$, la loi de Hess donne

$$\Delta_r H^\circ = \Delta_f H^\circ(\mathrm{Zn(OH)_4^{2-}}) + \Delta_f H^\circ(\mathrm{HS^-}) - \Delta_f H^\circ(\mathrm{ZnS}) - 3\,\Delta_f H^\circ(\mathrm{HO^-}) - \Delta_f H^\circ(\mathrm{H_2O})$$

$$\Delta_r H^\circ = -1500 - 18 + 203 + 3\times 230 + 285$$

$$\boxed{\Delta_r H^\circ = -340\ \mathrm{kJ\cdot mol^{-1}}}$$

De même, avec les entropies molaires standard :

$$\Delta_r S^\circ = S_m^\circ(\mathrm{Zn(OH)_4^{2-}}) + S_m^\circ(\mathrm{HS^-}) - S_m^\circ(\mathrm{ZnS}) - 3\,S_m^\circ(\mathrm{HO^-}) - S_m^\circ(\mathrm{H_2O})$$

$$\Delta_r S^\circ = -30 + 63 - 58 + 3\times 11 - 70$$

$$\boxed{\Delta_r S^\circ = -62\ \mathrm{J\cdot K^{-1}\cdot mol^{-1}}}$$

**Signe.** $\Delta_r H^\circ < 0$ : la réaction est **exothermique**. À température et pression constantes, elle cède de l'énergie thermique au milieu extérieur lorsqu'elle avance dans le sens direct.

L'entropie standard de réaction est négative : la réaction consomme quatre espèces mobiles en solution (trois ions hydroxyde et une molécule d'eau) pour n'en former que deux.

> [!PIEGE]
> Les entropies molaires standard des corps simples ne sont pas nulles (contrairement à leurs enthalpies de formation), et celles des ions en solution peuvent être négatives. Garder les kilojoules pour $\Delta_r H^\circ$ et les joules pour $\Delta_r S^\circ$ jusqu'à la question suivante.

### Question 24

> [!INDICATION]
> Relation entre les trois grandeurs standard de réaction, à la température $T$. Convertir l'entropie en $\mathrm{kJ\cdot K^{-1}\cdot mol^{-1}}$.

#### Solution

Par définition, à la température $T$ :

$$\boxed{\Delta_r G^\circ(T) = \Delta_r H^\circ(T) - T\,\Delta_r S^\circ(T)}$$

À 298 K, avec $\Delta_r S^\circ = -62\cdot 10^{-3}\ \mathrm{kJ\cdot K^{-1}\cdot mol^{-1}}$ :

$$T\,\Delta_r S^\circ = 298\times(-0{,}062) \approx -18{,}5\ \mathrm{kJ\cdot mol^{-1}}$$

$$\Delta_r G^\circ = -340 + 18{,}5$$

$$\boxed{\Delta_r G^\circ(298\ \mathrm K) = -321{,}5\ \mathrm{kJ\cdot mol^{-1}}}$$

On retrouve la valeur indiquée par l'énoncé, ce qui valide les deux résultats de la question 23.

### Question 25

> [!INDICATION]
> Relation de cours entre $\Delta_r G^\circ$ et $K^\circ$ ; l'inverser.

#### Solution

La constante d'équilibre est définie par $\Delta_r G^\circ(T) + RT\ln K^\circ(T) = 0$ :

$$\boxed{K_1^\circ(T) = \exp\left(-\frac{\Delta_r G^\circ(T)}{RT}\right)}$$

avec $R$ la constante des gaz parfaits et $T$ la température en kelvins. Seule l'expression est demandée (la valeur de $R$ n'est pas fournie et la calculatrice est interdite). À titre indicatif, avec $R = 8{,}31\ \mathrm{J\cdot K^{-1}\cdot mol^{-1}}$, on obtient $\ln K_1^\circ \approx 130$ à 298 K, soit $K_1^\circ \approx 10^{56}$ : d'après ces données, la réaction (1) serait quantitative (voir la remarque de la question 28).

> [!PIEGE]
> Dans l'exponentielle, $\Delta_r G^\circ$ doit être exprimée en $\mathrm{J\cdot mol^{-1}}$ si $R$ est en $\mathrm{J\cdot K^{-1}\cdot mol^{-1}}$. Ne pas oublier le signe moins : une enthalpie libre standard négative donne une constante supérieure à 1.

### Question 26

> [!INDICATION]
> Loi de Van't Hoff : le sens de variation de la constante d'équilibre avec la température est fixé par le signe de l'enthalpie standard de réaction.

#### Solution

La loi de Van't Hoff relie la variation de la constante d'équilibre à l'enthalpie standard de réaction :

$$\frac{\mathrm d\ln K_1^\circ}{\mathrm dT} = \frac{\Delta_r H^\circ}{RT^2}$$

Ici $\Delta_r H^\circ = -340\ \mathrm{kJ\cdot mol^{-1}} < 0$ : $K_1^\circ$ est une fonction décroissante de la température.

$$\boxed{\text{Une élévation de température défavorise la réaction (1) du point de vue thermodynamique}}$$

À partir d'un état d'équilibre, une élévation de température à pression constante déplace l'équilibre dans le sens endothermique, c'est-à-dire dans le sens indirect. (Une température plus élevée accélère en revanche la réaction : l'argument cinétique va en sens opposé.)

### Question 27

> [!INDICATION]
> La constante de la réaction d'une base avec l'eau vaut $K_e/K_a$. Dresser un tableau d'avancement volumique.

> [!INDICATION]
> La constante est petite : supposer la base peu transformée ($[\mathrm{CO_3^{2-}}] \approx c$), calculer, puis vérifier l'hypothèse. Pour finir, $10^{-2{,}35} = 10^{0{,}65}\cdot 10^{-3}$.

#### Solution

L'énoncé parle de « bicarbonate », mais la formule $\mathrm{Na_2CO_3}$ et l'ion $\mathrm{CO_3^{2-}}$ désignent le **carbonate** de sodium : c'est donc l'ion carbonate que l'on considère, à la concentration apportée $c = 10^{-1}\ \mathrm{mol\cdot L^{-1}}$.

**Réaction (2)** (première basicité seule) :

$$\boxed{\mathrm{CO_3^{2-}(aq)} + \mathrm{H_2O} = \mathrm{HCO_3^-(aq)} + \mathrm{HO^-(aq)} \qquad (2)}$$

Sa constante se déduit de $K_{a4}$ et du produit ionique de l'eau :

$$K_2 = \frac{[\mathrm{HCO_3^-}]\,[\mathrm{HO^-}]}{[\mathrm{CO_3^{2-}}]} = \frac{K_e}{K_{a4}} = 10^{-14+10{,}3} = 10^{-3{,}7}$$

**Concentration en ions hydroxyde.** On note $x = [\mathrm{HO^-}]$. En négligeant l'autoprotolyse de l'eau, la réaction (2) forme autant d'ions hydrogénocarbonate que d'ions hydroxyde :

| | $\mathrm{CO_3^{2-}}$ | $\mathrm{HCO_3^-}$ | $\mathrm{HO^-}$ |
|---|---|---|---|
| état initial | $c$ | 0 | 0 |
| équilibre | $c - x$ | $x$ | $x$ |

$$K_2 = \frac{x^2}{c - x}$$

La constante étant petite, on suppose la base peu transformée, $x \ll c$ :

$$x \approx \sqrt{K_2\,c} = \sqrt{10^{-3{,}7}\times 10^{-1}} = 10^{-2{,}35}\ \mathrm{mol\cdot L^{-1}}$$

$$\boxed{[\mathrm{HO^-}] \approx 10^{-2{,}35} \approx 4{,}5\cdot 10^{-3}\ \mathrm{mol\cdot L^{-1}}}$$

Vérifications : $x/c \approx 4{,}5\ \%$, l'hypothèse $x \ll c$ est acceptable ; $x \gg 10^{-7}\ \mathrm{mol\cdot L^{-1}}$, l'autoprotolyse est négligeable. Le pH vaut $14 - 2{,}35 \approx 11{,}6$ : la solution est nettement basique, conformément à la question 21, et l'ion hydrogénocarbonate ($\mathrm{p}K_{a3} = 6{,}3$) ne réagit pratiquement pas à son tour, ce qui justifie de ne retenir que la première basicité.

> [!JURY]
> Le rapport cite précisément les questions sur les propriétés acido-basiques des ions carbonate comme source de bilans erronés. L'ion carbonate est une base : il capte un proton de l'eau et libère un ion hydroxyde.

### Question 28

> [!INDICATION]
> Éliminer les ions hydroxyde : la réaction (1) en consomme trois, la réaction (2) en produit un. Quelle combinaison former ?

> [!INDICATION]
> Les constantes se multiplient : $K_3 = K_1\,K_2^3$. Pour $K_1$, décomposer la réaction (1) en étapes de constantes connues ($K_{s2}$, $K_c$, puis la réaction de $\mathrm{S^{2-}}$ avec l'eau).

#### Solution

**Équation (3).** La réaction (1) consomme trois ions hydroxyde, la réaction (2) en fournit un : la combinaison $(3) = (1) + 3\times(2)$ les élimine.

$$\boxed{\mathrm{ZnS(s)} + 3\,\mathrm{CO_3^{2-}} + 4\,\mathrm{H_2O} = \mathrm{Zn(OH)_4^{2-}} + \mathrm{HS^-} + 3\,\mathrm{HCO_3^-} \qquad (3)}$$

**Constante d'équilibre.** Les constantes se multiplient :

$$K_3 = K_1\,K_2^{\,3}$$

La réaction (1) est elle-même la somme de trois réactions dont les constantes figurent dans les données :

$$\mathrm{ZnS(s)} = \mathrm{Zn^{2+}} + \mathrm{S^{2-}} \qquad K_{s2} = 10^{-20}$$

$$\mathrm{Zn^{2+}} + 4\,\mathrm{HO^-} = \mathrm{Zn(OH)_4^{2-}} \qquad K_c = 10^{16}$$

$$\mathrm{S^{2-}} + \mathrm{H_2O} = \mathrm{HS^-} + \mathrm{HO^-} \qquad \frac{K_e}{K_{a2}} = 10^{-14+13} = 10^{-1}$$

$$K_1 = K_{s2}\,K_c\,\frac{K_e}{K_{a2}} = 10^{-20+16-1} = 10^{-5}$$

D'où, avec $K_2 = 10^{-3{,}7}$ :

$$K_3 = 10^{-5}\times\bigl(10^{-3{,}7}\bigr)^3 = 10^{-5-11{,}1}$$

$$\boxed{K_3 = 10^{-16{,}1} \approx 8\cdot 10^{-17}}$$

**Conclusion.** $K_3 \ll 1$ : la réaction (3) est très peu avancée, la solution de carbonate de sodium ne dissout pratiquement pas le sulfure de zinc. Ordre de grandeur de la solubilité $s$ : la réaction (1) forme autant de complexe que d'ions $\mathrm{HS^-}$, dans un milieu où $[\mathrm{HO^-}] \approx 4{,}5\cdot 10^{-3}\ \mathrm{mol\cdot L^{-1}}$ reste fixée par le carbonate, donc

$$s^2 = K_1\,[\mathrm{HO^-}]^3 \approx 10^{-5}\times 9\cdot 10^{-8} \approx 9\cdot 10^{-13}$$

$$s \approx 1\cdot 10^{-6}\ \mathrm{mol\cdot L^{-1}}$$

Dans les 100 mL de solution, seule une quantité de l'ordre de $10^{-7}$ mol de sulfure de zinc (environ $10\ \mathrm{\mu g}$) passe en solution : presque toute la masse introduite reste solide. Un milieu beaucoup plus basique serait nécessaire.

**Remarque sur les données.** Les deux jeux de données de l'énoncé ne sont pas cohérents. La valeur $\Delta_r G^\circ = -321{,}5\ \mathrm{kJ\cdot mol^{-1}}$ des questions 24 et 25 conduirait à $K_1 \approx 10^{56}$, puis à $K_3 \approx 10^{45}$, et donc à la conclusion inverse (dissolution totale). On retient ici les constantes d'équilibre en solution ($K_{s2}$, $K_c$, $K_{a2}$), qui sont les seules exploitables sans calculatrice ni valeur de $R$, et dont le résultat est conforme au caractère très peu soluble du sulfure de zinc.

> [!METHODE]
> Combinaison de réactions : si $(3) = (1) + 3\times(2)$, alors $\Delta_r G_3^\circ = \Delta_r G_1^\circ + 3\,\Delta_r G_2^\circ$ et $K_3 = K_1\,K_2^3$. Les enthalpies libres s'ajoutent, les constantes se multiplient, avec les coefficients en exposants.

> [!PIEGE]
> Sur une copie, signaler l'incohérence entre les deux valeurs possibles de $K_1$ et indiquer clairement celle que l'on retient et pourquoi : l'énoncé invite lui-même le candidat à expliciter les initiatives qu'il prend.

## Partie D — Cinétique de la synthèse du sulfure de zinc

### Question 29

> [!INDICATION]
> Quelle concentration figure dans la loi de vitesse, en plus de celle du réactif TAA ? Que devient la loi si elle reste constante ?

#### Solution

Une solution tampon maintient le pH, donc $[\mathrm{H_3O^+}]$, pratiquement constant au cours de la réaction. Deux conséquences :

- la loi de vitesse, d'ordre 1 par rapport à chacune des deux espèces, se réduit à une loi d'ordre apparent 1 par rapport au seul TAA (**dégénérescence de l'ordre**), de constante apparente $k_{\mathrm{app}} = k\,[\mathrm{H_3O^+}]$, ce qui simplifie l'intégration et l'exploitation des mesures ;
- les équilibres acido-basiques de $\mathrm{H_2S}$ sont figés : la concentration en ions sulfure reste proportionnelle à celle de $\mathrm{H_2S}$ (question 33), avec un facteur constant.

### Question 30

> [!INDICATION]
> Ordre 1 par rapport à chaque réactif cité : la vitesse est proportionnelle au produit des deux concentrations.

#### Solution

La vitesse volumique de la réaction (4) est d'ordre partiel 1 par rapport au TAA et par rapport à l'ion oxonium :

$$\boxed{v = -\frac{\mathrm d[\mathrm{TAA}]}{\mathrm dt} = k\,[\mathrm{TAA}]\,[\mathrm{H_3O^+}]}$$

L'ordre global est 2, et $k$ s'exprime en $\mathrm{L\cdot mol^{-1}\cdot s^{-1}}$ (ou $\mathrm{L\cdot mol^{-1}\cdot min^{-1}}$). L'ion oxonium, qui n'apparaît pas dans le bilan (4), joue le rôle de catalyseur.

### Question 31

> [!INDICATION]
> Avec $[\mathrm{H_3O^+}]$ constante, l'équation est différentielle linéaire du premier ordre à coefficient constant.

> [!INDICATION]
> Séparer les variables ou reconnaître la solution exponentielle, puis utiliser la condition initiale $[\mathrm{TAA}](0) = [\mathrm{TAA}]_0$.

#### Solution

La concentration $[\mathrm{H_3O^+}]$ étant constante (tampon), la loi de vitesse est une équation différentielle linéaire du premier ordre à coefficient constant :

$$\frac{\mathrm d[\mathrm{TAA}]}{\mathrm dt} + k\,[\mathrm{H_3O^+}]\,[\mathrm{TAA}] = 0$$

Par séparation des variables, entre l'instant 0 et l'instant $t$ :

$$\ln\frac{[\mathrm{TAA}]}{[\mathrm{TAA}]_0} = -k\,[\mathrm{H_3O^+}]\,t$$

$$\boxed{[\mathrm{TAA}](t) = [\mathrm{TAA}]_0\,\exp\bigl(-k\,[\mathrm{H_3O^+}]\,t\bigr)}$$

La concentration décroît exponentiellement, avec le temps caractéristique $\tau = 1/(k\,[\mathrm{H_3O^+}])$.

> [!JURY]
> Le rapport regrette que l'outil mathématique manque à certains candidats pour résoudre ce type d'équation différentielle. La solution de $y' + a\,y = 0$ est $y = y(0)\,e^{-at}$ : à savoir écrire sans hésiter.

### Question 32

> [!INDICATION]
> Bilan de matière de la réaction (4) : une mole de $\mathrm{H_2S}$ formée par mole de TAA consommée, à volume constant.

#### Solution

D'après le bilan (4), une mole de $\mathrm{H_2S}$ apparaît pour chaque mole de TAA consommée. À volume constant, en l'absence initiale de $\mathrm{H_2S}$ et tant que celui-ci reste en solution sous cette forme (à pH = 1, très inférieur à $\mathrm{p}K_{a1}$, sa dissociation est négligeable) :

$$[\mathrm{H_2S}](t) = [\mathrm{TAA}]_0 - [\mathrm{TAA}](t)$$

$$\boxed{[\mathrm{H_2S}](t) = [\mathrm{TAA}]_0\,\Bigl(1 - \exp\bigl(-k\,[\mathrm{H_3O^+}]\,t\bigr)\Bigr)}$$

Cette concentration croît de 0 vers la valeur limite $[\mathrm{TAA}]_0$.

### Question 33

> [!INDICATION]
> Multiplier les deux constantes d'acidité : la concentration de l'espèce intermédiaire $\mathrm{HS^-}$ s'élimine.

#### Solution

Les deux équilibres acido-basiques, rapides devant la décomposition du TAA, sont établis à chaque instant :

$$K_{a1} = \frac{[\mathrm{HS^-}]\,[\mathrm{H_3O^+}]}{[\mathrm{H_2S}]}$$

$$K_{a2} = \frac{[\mathrm{S^{2-}}]\,[\mathrm{H_3O^+}]}{[\mathrm{HS^-}]}$$

Le produit des deux relations élimine $[\mathrm{HS^-}]$ :

$$K_{a1}\,K_{a2} = \frac{[\mathrm{S^{2-}}]\,[\mathrm{H_3O^+}]^2}{[\mathrm{H_2S}]}$$

$$\boxed{[\mathrm{S^{2-}}] = \frac{K_{a1}\,K_{a2}\,[\mathrm{H_2S}]}{[\mathrm{H_3O^+}]^2}}$$

### Question 34

> [!INDICATION]
> Reporter le résultat de la question 32 dans celui de la question 33.

#### Solution

En reportant l'expression de $[\mathrm{H_2S}](t)$ (question 32) dans la relation de la question 33 :

$$\boxed{[\mathrm{S^{2-}}](t) = K_{a1}\,K_{a2}\,\frac{[\mathrm{TAA}]_0}{[\mathrm{H_3O^+}]^2}\,\Bigl(1 - \exp\bigl(-k\,[\mathrm{H_3O^+}]\,t\bigr)\Bigr)}$$

C'est l'expression donnée par l'énoncé. La concentration croît de 0 vers la limite

$$[\mathrm{S^{2-}}]_\infty = K_{a1}\,K_{a2}\,\frac{[\mathrm{TAA}]_0}{[\mathrm{H_3O^+}]^2}$$

ce qui correspond à l'allure de la courbe de la figure 3 du sujet (croissance à concavité tournée vers le bas, tendant vers une asymptote).

### Question 35

> [!INDICATION]
> Former le rapport $[\mathrm{S^{2-}}](t_1)/[\mathrm{S^{2-}}]_\infty$ : le préfacteur disparaît et il ne reste que l'exponentielle.

> [!INDICATION]
> On obtient $\exp(-k\,[\mathrm{H_3O^+}]\,t_1) = 0{,}6$. Prendre le logarithme, avec $[\mathrm{H_3O^+}] = 10^{-1}\ \mathrm{mol\cdot L^{-1}}$ (pH = 1).

#### Solution

D'après la question 34 :

$$\frac{[\mathrm{S^{2-}}](t_1)}{[\mathrm{S^{2-}}]_\infty} = 1 - \exp\bigl(-k\,[\mathrm{H_3O^+}]\,t_1\bigr)$$

Avec le point de la courbe indiqué par l'énoncé (figure 3 du sujet : ordonnée 6 à l'abscisse 11 min, l'axe étant gradué en $10^{-18}\ \mathrm{mol\cdot L^{-1}}$) :

$$\frac{6\cdot 10^{-18}}{1{,}5\cdot 10^{-17}} = 0{,}4$$

$$\exp\bigl(-k\,[\mathrm{H_3O^+}]\,t_1\bigr) = 1 - 0{,}4 = 0{,}6$$

$$k = -\frac{\ln(0{,}6)}{[\mathrm{H_3O^+}]\,t_1}$$

Application numérique avec $[\mathrm{H_3O^+}] = 10^{-1}\ \mathrm{mol\cdot L^{-1}}$ (pH = 1), $t_1 = 11\ \mathrm{min}$ et $\ln(0{,}6) \approx -0{,}5$ :

$$k \approx \frac{0{,}5}{0{,}1\times 11}$$

$$\boxed{k \approx 0{,}45\ \mathrm{L\cdot mol^{-1}\cdot min^{-1}} \approx 7{,}6\cdot 10^{-3}\ \mathrm{L\cdot mol^{-1}\cdot s^{-1}}}$$

La constante apparente vaut $k\,[\mathrm{H_3O^+}] \approx 4{,}5\cdot 10^{-2}\ \mathrm{min^{-1}}$, soit un temps caractéristique de 22 min. Contrôle sur la figure 3 du sujet : à $t = 30$ min, le modèle donne $15\,(1 - e^{-1{,}36}) \approx 11$, ce qui est bien l'ordonnée lue à l'extrémité de la courbe.

**Remarque sur les données.** Avec $\mathrm{p}K_{a1} + \mathrm{p}K_{a2} = 20$, $[\mathrm{TAA}]_0 = 0{,}2\ \mathrm{mol\cdot L^{-1}}$ et pH = 1, l'expression de la question 34 donnerait une limite de $2\cdot 10^{-19}\ \mathrm{mol\cdot L^{-1}}$, et non la valeur $1{,}5\cdot 10^{-17}\ \mathrm{mol\cdot L^{-1}}$ indiquée. Cet écart est sans effet sur $k$, qui ne dépend que du rapport des deux ordonnées ; on utilise dans la suite les valeurs de la courbe, comme le demande l'énoncé.

> [!PIEGE]
> L'unité de $k$ : la loi est d'ordre global 2, donc $k$ est en $\mathrm{L\cdot mol^{-1}\cdot min^{-1}}$, et non en $\mathrm{min^{-1}}$ (unité de la constante apparente $k\,[\mathrm{H_3O^+}]$). Le rapport du jury rappelle qu'une valeur sans unité n'est pas créditée.

### Question 36

> [!INDICATION]
> Lire sur la figure 3 du sujet (ou calculer avec le modèle) la concentration en ions sulfure à $t_2 = 3$ min, puis former le produit $[\mathrm{Zn^{2+}}]\,[\mathrm{S^{2-}}]$.

> [!INDICATION]
> Comparer à $K_{s2} = 10^{-20}$ : si le produit dépasse $K_{s2}$ alors qu'aucun solide n'est encore apparu, comment qualifier la solution ?

#### Solution

On considère l'équilibre $\mathrm{ZnS(s)} = \mathrm{Zn^{2+}} + \mathrm{S^{2-}}$, de constante $K_{s2} = 10^{-20}$, et le quotient de réaction associé $Q = [\mathrm{Zn^{2+}}]\,[\mathrm{S^{2-}}]$.

Juste avant l'apparition du précipité, $[\mathrm{Zn^{2+}}] = 10^{-1}\ \mathrm{mol\cdot L^{-1}}$ (le nitrate de zinc est totalement dissocié). À $t_2 = 3$ min, la figure 3 du sujet donne une ordonnée voisine de 2 (la courbe passe par 1,3 environ à 2 min et 2,5 environ à 4 min). Le modèle le confirme, avec $1 - e^{-x} \approx x$ pour $x = k\,[\mathrm{H_3O^+}]\,t_2 \approx 0{,}14$ :

$$[\mathrm{S^{2-}}](t_2) \approx 1{,}5\cdot 10^{-17}\times 0{,}13 \approx 2\cdot 10^{-18}\ \mathrm{mol\cdot L^{-1}}$$

$$Q = [\mathrm{Zn^{2+}}]\,[\mathrm{S^{2-}}] \approx 10^{-1}\times 2\cdot 10^{-18}$$

$$\boxed{Q \approx 2\cdot 10^{-19} > K_{s2} = 10^{-20}}$$

Le quotient de réaction dépasse le produit de solubilité d'un facteur 20 environ : la solution n'est pas simplement saturée, elle est **sursaturée**. La condition thermodynamique de précipitation, $Q = K_{s2}$, soit $[\mathrm{S^{2-}}] = 10^{-19}\ \mathrm{mol\cdot L^{-1}}$, est atteinte dès les premières secondes (vers $t \approx 0{,}15$ min d'après le modèle). Le solide n'apparaît qu'ensuite, car la formation des premiers germes cristallins est lente : la solution reste dans un état métastable jusqu'à $t_2$.

> [!METHODE]
> Critère de précipitation : comparer $Q = [\mathrm{Zn^{2+}}]\,[\mathrm{S^{2-}}]$, calculé avec les concentrations réelles, à $K_s$. Si $Q < K_s$, pas de solide ; si $Q = K_s$, solution saturée ; si $Q > K_s$ sans solide, solution sursaturée, hors équilibre.

### Question 37

> [!INDICATION]
> $\mathrm{H_2S}$ est un diacide : il peut céder deux protons à deux molécules d'eau.

#### Solution

Le diacide $\mathrm{H_2S}$ cède deux protons à l'eau (somme des deux réactions d'acidité) :

$$\boxed{\mathrm{H_2S(aq)} + 2\,\mathrm{H_2O} = \mathrm{S^{2-}(aq)} + 2\,\mathrm{H_3O^+(aq)} \qquad (5)}$$

Sa constante vaut $K_5 = K_{a1}\,K_{a2} = 10^{-20}$ : la réaction est très peu avancée, surtout à pH = 1, mais elle fournit la très faible concentration en ions sulfure (de l'ordre de $10^{-18}\ \mathrm{mol\cdot L^{-1}}$) qui suffit à atteindre le produit de solubilité de $\mathrm{ZnS}$.

### Question 38

> [!INDICATION]
> Additionner la réaction (5) et la précipitation $\mathrm{Zn^{2+}} + \mathrm{S^{2-}} = \mathrm{ZnS(s)}$ : l'ion sulfure s'élimine.

#### Solution

En milieu acide, l'espèce du soufre présente en quantité notable est $\mathrm{H_2S}$. La somme de la réaction (5) et de la précipitation $\mathrm{Zn^{2+}} + \mathrm{S^{2-}} = \mathrm{ZnS(s)}$ donne

$$\boxed{\mathrm{Zn^{2+}(aq)} + \mathrm{H_2S(aq)} + 2\,\mathrm{H_2O} = \mathrm{ZnS(s)} + 2\,\mathrm{H_3O^+(aq)}}$$

Sa constante d'équilibre vaut

$$K = \frac{K_{a1}\,K_{a2}}{K_{s2}} = \frac{10^{-20}}{10^{-20}} = 1$$

La réaction libère des ions oxonium : c'est le tampon qui maintient le pH constant pendant la précipitation.

### Question 39

> [!INDICATION]
> D'après la question 38, il faut une mole de $\mathrm{H_2S}$ par mole de zinc : quelle fraction du TAA initial doit s'être décomposée ?

> [!INDICATION]
> La moitié : on cherche donc le temps de demi-réaction d'une cinétique d'ordre apparent 1, $t = \ln 2/(k\,[\mathrm{H_3O^+}])$.

#### Solution

D'après la question 38, la précipitation consomme une mole de $\mathrm{H_2S}$ par mole de $\mathrm{Zn^{2+}}$. En supposant cette précipitation rapide et totale, c'est la décomposition du TAA, étape lente, qui fixe la durée : il faut que la quantité de $\mathrm{H_2S}$ produite par litre atteigne la concentration initiale en zinc, $[\mathrm{Zn^{2+}}]_0 = 10^{-1}\ \mathrm{mol\cdot L^{-1}}$.

La production de $\mathrm{H_2S}$ suit la loi de la question 32 (la cinétique de décomposition du TAA ne dépend pas de ce que devient $\mathrm{H_2S}$) :

$$[\mathrm{TAA}]_0\,\Bigl(1 - \exp\bigl(-k\,[\mathrm{H_3O^+}]\,t\bigr)\Bigr) = [\mathrm{Zn^{2+}}]_0$$

$$\exp\bigl(-k\,[\mathrm{H_3O^+}]\,t\bigr) = 1 - \frac{0{,}1}{0{,}2} = \frac12$$

Le TAA étant en quantité double de celle du zinc, la durée cherchée est le temps de demi-réaction du TAA :

$$t = \frac{\ln 2}{k\,[\mathrm{H_3O^+}]}$$

Application numérique avec $\ln 2 \approx 0{,}69$ et $k\,[\mathrm{H_3O^+}] \approx 4{,}5\cdot 10^{-2}\ \mathrm{min^{-1}}$ :

$$\boxed{t \approx 15\ \mathrm{min}}$$

Il s'agit d'une estimation : elle suppose la précipitation quantitative et instantanée dès que $\mathrm{H_2S}$ est formé. La constante de la réaction de la question 38 valant 1, une faible fraction du zinc reste en réalité en solution à pH = 1, et la durée réelle est un peu supérieure.

> [!METHODE]
> Pour une cinétique d'ordre 1 de constante apparente $k_{\mathrm{app}}$, le temps de demi-réaction $t_{1/2} = \ln 2/k_{\mathrm{app}}$ ne dépend pas de la concentration initiale. Repérer qu'il faut consommer exactement la moitié du réactif évite tout calcul.

> [!JURY]
> D'après le rapport, cette dernière partie a été plutôt bien traitée par ceux qui l'ont abordée, mais beaucoup ne l'ont pas atteinte faute de temps. Les questions 29 à 34 et 37 sont proches du cours : elles méritent d'être traitées même si la partie B est restée inachevée.

## Bilan

**Ce qu'il faut retenir.**

- *Cristallographie* : dans la blende, les anions forment un réseau cubique à faces centrées et les cations occupent un site tétraédrique sur deux ; la coordinence est 4 pour les deux ions ; le contact cation-anion se fait sur le quart de la grande diagonale, $a\sqrt3/4 = R_+ + R_-$ ; le non-recouvrement des anions donne $R_+/R_- \geqslant \sqrt{3/2} - 1$.
- *Diagramme E-pH* : attribution par nombre d'oxydation (vertical) et par basicité (horizontal) ; une frontière verticale se calcule avec la constante de l'équilibre et la concentration de tracé ; la pente d'une frontière rédox vaut $-0{,}06\,m/n$ pour $m$ protons et $n$ électrons, et elle change chaque fois que l'espèce prédominante change ; un précipité abaisse le potentiel standard apparent, $E^\circ(\mathrm{ZnS/Zn}) = E^\circ(\mathrm{Zn^{2+}/Zn}) + 0{,}03\log K_s$.
- *Thermodynamique* : loi de Hess, puis $\Delta_r G^\circ = \Delta_r H^\circ - T\Delta_r S^\circ = -RT\ln K^\circ$ ; Van't Hoff pour l'effet de la température ; les constantes se multiplient quand les réactions s'ajoutent.
- *Acides et bases* : une base réagit avec l'eau avec la constante $K_e/K_a$ ; pour une base faible peu transformée, $[\mathrm{HO^-}] \approx \sqrt{K_e\,c/K_a}$, hypothèse à vérifier.
- *Cinétique* : un tampon rend constante la concentration en ions oxonium et ramène la loi à un ordre apparent 1 ; $y' + a\,y = 0$ donne $y = y(0)\,e^{-at}$ ; le rapport à la valeur limite élimine le préfacteur ; $t_{1/2} = \ln 2/k_{\mathrm{app}}$.
- *Précipitation* : comparer le quotient de réaction au produit de solubilité ; un quotient supérieur sans solide signale une sursaturation.

**Résultats numériques.** Rapport des rayons 0,40 (borne 0,22) ; $\rho \approx 4{,}1\cdot 10^{3}\ \mathrm{kg\cdot m^{-3}}$ ; frontières verticales à pH = 6,5 et pH = 13,5 ; $K = 10^{-1}$ pour la redissolution de l'hydroxyde ; palier du couple $\mathrm{ZnS/Zn}$ à $-1{,}18$ V et pente $-0{,}03$ V par unité de pH entre pH 7 et 13 ; $\Delta_r H^\circ = -340\ \mathrm{kJ\cdot mol^{-1}}$ ; $\Delta_r S^\circ = -62\ \mathrm{J\cdot K^{-1}\cdot mol^{-1}}$ ; $\Delta_r G^\circ = -321{,}5\ \mathrm{kJ\cdot mol^{-1}}$ ; $[\mathrm{HO^-}] \approx 4{,}5\cdot 10^{-3}\ \mathrm{mol\cdot L^{-1}}$ ; $K_3 = 10^{-16{,}1}$ ; $k \approx 0{,}45\ \mathrm{L\cdot mol^{-1}\cdot min^{-1}}$ ; $Q \approx 2\cdot 10^{-19}$ à 3 min ; durée de précipitation d'environ 15 min.

**Erreurs les plus coûteuses d'après le jury.** Mal placer les sites tétraédriques ; ne pas savoir établir l'inégalité sur les rayons ; confondre compacité et masse volumique ou se tromper dans les conversions ; écrire de façon fantaisiste la redissolution de l'hydroxyde en milieu basique ; introduire des ions oxonium ou hydroxyde sans rapport avec le pH du milieu ; ne pas reconnaître l'ion carbonate comme une base ; ne pas savoir résoudre l'équation différentielle d'ordre 1 ; donner une valeur sans unité.

**Pour s'entraîner.** Refaire sans aide les questions 3, 5, 9 et 10, puis l'enchaînement 15 à 20, et enfin les questions 27, 28, 35 et 39, en terminant chaque application numérique à la main.
