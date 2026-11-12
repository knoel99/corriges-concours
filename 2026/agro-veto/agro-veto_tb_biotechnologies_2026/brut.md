# Agro-Véto TB — Biotechnologies 2026 · Corrigé brut

*Corrigé rédigé par IA, non officiel. Signalez toute erreur.*

Durée 3 heures. Abaques, tables, calculatrice et tout instrument électronique **interdits**. Sujet de 13 pages, 10 documents, 29 questions (Q1 à Q29), la question Q12 étant rédactionnelle. Thème : **« Le système bactérien CBASS, à l'origine d'un mécanisme immunitaire anti-phagique »**.

---

## Partie 1. Préparation d'outils pour l'étude du système immunitaire via le système CBASS

### 1. Bactériophage Φ80α

### Q1. Caractéristiques structurales et mode de multiplication du phage Φ80α

Le document 1 présente une carte génétique linéaire de **73 gènes** organisés en **six modules fonctionnels contigus** : lysogénie, réplication, encapsidation (*packaging*), tête (*head*), queue (*tail*) et lyse. C'est cette organisation modulaire, et non le détail des gènes, qui doit être exploitée.

**a. Caractéristiques structurales.**

- **Génome d'ADN double brin.** Les gènes de réplication nommés *Initiator*, *DnaC* et *SSB* (protéine de liaison à l'ADN simple brin, qui n'a de sens que lors de l'ouverture d'un duplex) et la présence d'une intégrase imposent un génome d'**ADN bicaténaire**. La carte est linéaire et bornée, ce qui est cohérent avec un ADN linéaire dans le virion, encapsidé par translocation à travers un portail. Un génome de 73 gènes correspond, pour un phage caudé, à quelques dizaines de kilopaires de bases (donnée extérieure au document).
- **Virion à symétrie mixte, de type « têtard ».** Le module « tête » (protéine d'échafaudage *Scaf*, protéine majeure de capside, protéase de maturation) impose une **capside icosaédrique** ; le module « queue », très développé (une douzaine de gènes dont *TMP*, *Tape Measure Protein*, *STP*, *TFiber*, une hydrolase associée), impose une **queue** munie de **fibres**. La longueur du gène *TMP* fixant la longueur de la queue, celle-ci est **longue** ; l'**absence**, sur la carte, de tout gène de gaine contractile ou de plaque basale oriente vers une **queue non contractile** (morphotype siphovirus) — conclusion probable, non certaine.
- **Virion nu.** Aucun gène de glycoprotéine ni de protéine d'enveloppe n'apparaît, et l'architecture tête-queue est celle d'un virion **non enveloppé**. La stabilité du lysat à 4 °C et sa filtrabilité (document 2) sont cohérentes avec cette conclusion.
- **Encapsidation active.** Les terminases *TerS*/*TerL* et la protéine du *portal* signent une translocation de l'ADN dans une procapside préformée.

La **nucléocapside** est donc formée de l'ADN bicaténaire linéaire condensé dans une capside protéique icosaédrique, l'ensemble prolongé par la queue : c'est l'organisation canonique d'un phage caudé.

**b. Mode de multiplication.** Le **module de lysogénie** placé en tête de carte contient une **intégrase** (*Int*), une **excisionase** (*Xis*), un **répresseur CI** et son antagoniste **Cro**. Ce quatuor est la signature d'un **phage tempéré**, capable des deux cycles :

- **cycle lysogénique** : intégration site-spécifique du génome viral dans le chromosome de l'hôte par *Int*, état de **prophage**, répression des gènes lytiques par CI, immunité de superinfection, transmission verticale ;
- **cycle lytique** : bascule CI → Cro, réplication de l'ADN (module de réplication), expression tardive des gènes de morphogenèse, encapsidation, puis **lyse**. Le module terminal associe une **holine** (perméabilisation de la membrane plasmique) et une **endolysine** (hydrolyse du peptidoglycane) : la libération se fait par **lyse** de l'hôte, non par bourgeonnement.

$$\boxed{\text{Φ80α : virus nu, ADN double brin linéaire, capside icosaédrique + queue longue à fibres ; phage } \textbf{tempéré} \text{ ; libération par lyse holine/endolysine.}}$$

### Q2. Étapes de purification du phage à partir du lysat

Après lyse totale, le lysat contient les virions recherchés, des bactéries non lysées, des débris de paroi et de membrane, des macromolécules solubles et le milieu de culture. Trois opérations successives, chacune fondée sur une **propriété différentielle** entre le virion et ce dont on le sépare.

**1. Centrifugation 4 300 g, 10 min — séparation par coefficient de sédimentation.** Une bactérie entière (≈ 1 µm) et les gros débris sédimentent à cette accélération modérée ; un virion (≈ 50–200 nm) reste en suspension, son culottage exigerait une ultracentrifugation (≳ 25 000 g). **Le produit recherché est donc le surnageant**, enrichi en phages et débarrassé des cellules et des débris grossiers. L'accélération est volontairement faible : plus élevée, elle entraînerait des phages dans le culot.

**2. Filtration sur membrane 0,45 µm — séparation par taille.** Le seuil de 0,45 µm est très inférieur au diamètre d'un coque de *S. aureus* (0,8–1,0 µm) et très supérieur à celui d'un virion : les bactéries résiduelles sont retenues, les phages traversent. La filtration est **clarifiante et débactérisante** vis-à-vis de *S. aureus* — elle n'est pas stérilisante au sens strict, seuil qui serait 0,22 µm. Le choix de 0,45 µm se justifie doublement : moindre colmatage sur un lysat chargé, et surtout moindre rétention non spécifique des phages à longue queue.

**3. Conservation à 4 °C — stabilisation.** Ce n'est pas une étape de séparation, mais elle est indissociable des précédentes : le froid ralentit les protéases et les nucléases résiduelles et limite la dénaturation des protéines de capside, donc la perte de titre infectieux. On évite la congélation, dont les cycles gel/dégel décrochent les queues.

Cette purification est **fonctionnelle et non absolue** : elle élimine cellules et débris, non les macromolécules solubles. Une purification poussée exigerait une ultracentrifugation en gradient de densité de chlorure de césium.

$$\boxed{\text{centrifugation } 4\,300\,g \ (\text{cellules, débris}) \rightarrow \text{filtration } 0{,}45\ \mu\text{m} \ (\text{bactéries résiduelles}) \rightarrow 4\ ^\circ\text{C} \ (\text{stabilité du titre})}$$

### Q3. Préparation de la suspension phagique à utiliser (argumentation par le calcul)

**Fenêtre de comptage imposée par le support.** Chaque spot dépose $V = 5\ \mu\text{L} = 5\times10^{-3}$ mL. Si $C$ est la concentration en phages infectieux de la suspension déposée, le nombre de plages attendues est $N = C\,V$. La contrainte « au plus 50 PFU comptables » s'écrit

$$\begin{aligned}
N = C\,V &\le 50 \\
C &\le \frac{50}{5\times10^{-3}} \\
C &\le 1{,}0\times10^{4}\ \text{PFU}\cdot\text{mL}^{-1}
\end{aligned}$$

Un comptage n'est en outre fiable qu'au-dessus d'une dizaine d'unités, l'incertitude relative d'un comptage poissonien valant $1/\sqrt{N}$ : ± 45 % pour $N = 5$, ± 14 % pour $N = 50$. D'où la fenêtre utile

$$\boxed{2\times10^{3}\ \text{PFU}\cdot\text{mL}^{-1} \le C_{\text{spot}} \le 1{,}0\times10^{4}\ \text{PFU}\cdot\text{mL}^{-1}}$$

c'est-à-dire une fenêtre **étroite, inférieure à une unité logarithmique** : les dilutions étant décimales, **une seule** dilution de la gamme y tombera.

**Facteur de dilution requis.** La suspension à vérifier est la **suspension phagique initiale infectieuse**, celle qui sert à infecter à MOI = 0,1 une culture à ≈ 1 × 10⁸ UFC·mL⁻¹ : le document 2 lui attribue $T \approx 1\times10^{7}$ PFU·mL⁻¹. Avec une dilution $10^{-n}$, il faut

$$\begin{aligned}
T\times10^{-n} &\le 10^{4} \\
n &\ge \log_{10} T - 4 \\
n &\ge 7 - 4 \\
n &\ge 3
\end{aligned}$$

- dilution $10^{-3}$ : $C = 10^{4}$ PFU·mL⁻¹, soit $N = 50$ plages — borne haute de la fenêtre ;
- dilution $10^{-4}$ : $C = 10^{3}$ PFU·mL⁻¹, soit $N = 5$ plages — comptable mais statistiquement médiocre.

**Plan de dilution retenu pour les 12 spots.** Le titre annoncé étant justement ce que l'on veut vérifier, on encadre largement : gamme décimale de $10^{-1}$ à $10^{-5}$ **en duplicat** (10 spots), plus un spot de **témoin diluant** (stérilité) et un spot de suspension pure (lyse confluente attendue, témoin positif) : $10 + 1 + 1 = 12$ spots exactement. Le duplicat divise par $\sqrt{2}$ l'incertitude de comptage et révèle une erreur de pipetage. Si le titre réel s'écartait beaucoup de $10^{7}$, la lecture resterait possible sur l'une des bornes et l'on ajusterait la gamme au second essai.

**Préparation matérielle.** Chaque dilution décimale se prépare en portant 100 µL de la dilution précédente dans 900 µL de diluant (BHI + 5 mM CaCl₂) : facteur 10, volume final 1 mL par tube, très supérieur aux 5 µL prélevés.

La concentration déposée doit rester au plus égale à $1{,}0\times10^{4}$ PFU·mL⁻¹, d'où la dilution minimale à appliquer à la suspension initiale :

$$\boxed{\text{dilution} \ge 10^{-3}}$$

Gamme retenue : de $10^{-1}$ à $10^{-5}$, en duplicat, plus deux témoins.

### Q4. Réalisation pratique et choix réalisés

**1. Préparation du tapis bactérien.** Dans une boîte de Petri Ø = 90 mm contenant une gélose BHI, on coule une couche de **gélose molle** (0,5 à 0,7 % d'agar) BHI additionnée de **5 mM CaCl₂** et ensemencée avec *S. aureus* RN4220 en phase exponentielle (≈ 10⁸ UFC·mL⁻¹). Trois choix sont décisifs :

- **gélose molle** : sa faible teneur en agar autorise la diffusion latérale des virions libérés, sans laquelle aucune plage de lyse ne deviendrait visible ;
- **CaCl₂** : les ions Ca²⁺ sont indispensables à l'**adsorption** du phage sur son récepteur pariétal ; les omettre effondre le titre apparent ;
- **hôte en phase exponentielle** : seules des bactéries en croissance active sont pleinement permissives.

La boîte est **séchée** 15 à 20 min, couvercle entrouvert : sans cela, les gouttes de 5 µL s'étalent et les spots fusionnent.

**2. Repérage.** On trace au marqueur, **sous** la boîte, une grille de 12 secteurs identifiés (3 × 4). La surface utile vaut $S = \pi\times(45)^2 \approx 6{,}4\times10^{3}$ mm², soit ≈ 530 mm² par secteur, c'est-à-dire un disque de ≈ 25 mm de diamètre : largement suffisant pour une goutte de 5 µL, qui s'étale sur 4 à 6 mm.

**3. Réalisation de la gamme.** Douze tubes stériles contenant 900 µL de diluant (BHI + 5 mM CaCl₂) sont alignés et identifiés. On porte 100 µL de la suspension mère dans le premier, on **homogénéise au vortex** 5 s, puis on reporte 100 µL dans le suivant, et ainsi de suite. **On change de cône à chaque transfert** : conserver le même cône reporte des virions adsorbés sur sa paroi et fausse la gamme par le haut.

**4. Dépôt.** On dépose 5 µL au centre de chaque secteur, en **commençant par la suspension la plus diluée** et en terminant par la plus concentrée, de façon qu'un report accidentel reste sans conséquence. Le cône est tenu à quelques millimètres de la gélose sans la toucher (une piqûre créerait un puits et une plage aberrante). On laisse la boîte à plat, couvercle entrouvert, 10 à 15 min, jusqu'à absorption complète des gouttes.

**5. Incubation.** 18 h à 37 °C, **boîte non retournée** tant que les gouttes ne sont pas absorbées — exception à la règle de l'incubation en position inversée, destinée ici à éviter la coulure.

**6. Lecture et calcul du titre.** On repère le secteur présentant entre 10 et 50 plages individualisées. Si $N$ plages sont comptées à la dilution $10^{-n}$ :

$$\begin{aligned}
T &= \frac{N}{V\times10^{-n}} \\
&= \frac{N}{5\times10^{-3}\times10^{-n}} \\
&= N\times 2\times10^{2}\times10^{n}\ \text{PFU}\cdot\text{mL}^{-1}
\end{aligned}$$

Exemple, pour $N = 35$ plages à la dilution $10^{-4}$ :

$$T = 35\times2\times10^{2}\times10^{4} = 7{,}0\times10^{7}\ \text{PFU}\cdot\text{mL}^{-1}.$$

**Asepsie.** Travail sous poste de sécurité microbiologique ou à proximité du bec Bunsen, cônes à filtre stériles, élimination des déchets contaminés en sac d'autoclavage.

$$\boxed{T = \frac{N}{V\cdot10^{-n}}}$$

### 2. Bactériophage Φ80α-virGFP

### Q5. Rôle des éléments apportés par pDVB434 et organisation du génome recombinant

**Rôle des trois éléments.**

- **Les deux bras d'homologie de 500 nt**, correspondant aux séquences *gp18* et *gp19* du phage, sont les **adresses** de la construction. Lorsqu'une bactérie transformée par pDVB434 est infectée par Φ80α-vir (étape 2), le génome viral et le plasmide coexistent dans le cytoplasme : la machinerie de **recombinaison homologue** de l'hôte (voie RecA) apparie ces bras aux régions correspondantes du génome viral et réalise un **double crossing-over**. Une longueur de 500 nt est le compromis usuel : assez longue pour une recombinaison efficace, assez courte pour un plasmide maniable.
- **La séquence codante *gfp*** est le **cargo** : c'est elle qui est transférée entre *gp18* et *gp19* lors du double crossing-over. C'est le **gène rapporteur** dont l'expression signalera l'infection.
- **La séquence RBS** (*Ribosome Binding Site*, Shine-Dalgarno) est indispensable à la **traduction** : elle recrute la petite sous-unité du ribosome en amont du codon initiateur AUG. Sans elle, l'ARN messager porteur de *gfp* serait transcrit mais non traduit, et aucune fluorescence n'apparaîtrait.

**Conséquence importante : pDVB434 n'apporte pas de promoteur.** La cassette est donc insérée en **fusion transcriptionnelle** : *gfp* est transcrit sous le contrôle du promoteur phagique qui gouverne déjà la région *gp18*–*gp19*. La GFP n'est par conséquent produite **que dans une cellule effectivement infectée et engagée dans le cycle**, ce qui fait d'elle un rapporteur de l'infection et non un marqueur constitutif. La lecture de la carte du document 1 place *gp18* et *gp19* dans la région précoce, en amont des modules de morphogenèse ; si cette lecture est exacte, la fluorescence apparaît tôt après l'infection — mais la conclusion précédente n'en dépend pas.

![Figure 1 — Construction de Φ80α-virGFP : double crossing-over entre les bras de 500 nt de pDVB434 et les séquences gp18 et gp19, insertion de la cassette RBS-gfp dépourvue de promoteur, module de lysogénie inactivé par la mutation vir](figures/q5-genome-virgfp.svg)

La cassette **RBS-*gfp*** est insérée entre *gp18* et *gp19*, sans promoteur propre ; le module de lysogénie (*cI*, *int*) est rendu non fonctionnel par la mutation *vir*, d'où un phage **exclusivement lytique**, comme l'annonce l'énoncé.

$$\boxed{\text{pDVB434 = matrice de recombinaison : 2 bras de 500 nt (adressage) + RBS (traduction) + }\textit{gfp}\text{ (rapporteur), sans promoteur.}}$$

### Q6. Fonctionnement de CRISPR-Cas9 et élimination des phages non recombinants

**a. Fonctionnement du système.** Le système CRISPR-Cas de type II est, dans son contexte naturel, un **système immunitaire adaptatif bactérien** dirigé contre les acides nucléiques étrangers, phages compris. Il repose sur deux composants :

- une **endonucléase Cas9**, protéine bilobée à deux domaines catalytiques (RuvC et HNH), chacun coupant un brin ;
- un **ARN guide**, chimère du crRNA — dont une vingtaine de nucléotides sont complémentaires de la cible — et du tracrRNA, qui assure le repliement et l'ancrage sur Cas9.

Le complexe Cas9–ARN guide balaie l'ADN à la recherche d'un motif court adjacent à la cible, le **PAM** (*Protospacer Adjacent Motif*), dont la séquence est propre à chaque orthologue de Cas9 (5′-NGG-3′ pour celui de *Streptococcus pyogenes*, 5′-NNGRRT-3′ pour celui de ***S. aureus***, qui est le système porté par pDVB435). En présence d'un PAM, l'ADN est localement déroulé, le guide s'apparie au brin complémentaire et, si l'appariement est correct, les deux domaines catalytiques coupent : il en résulte une **cassure double brin à bouts francs**, trois paires de bases en amont du PAM.

**b. Élimination des phages non recombinants.** À l'issue de l'étape 2, la descendance phagique est une population **mixte** : une minorité de recombinants ayant intégré la cassette RBS-*gfp*, et une écrasante majorité de parentaux Φ80α-vir n'ayant pas recombiné, la recombinaison homologue étant un événement rare (de l'ordre de 10⁻⁴ à 10⁻⁶). Un criblage individuel par fluorescence serait hors de portée.

Le plasmide pDVB435 porte un système CRISPR-Cas9 ciblant « uniquement une séquence spécifique du bactériophage Φ80α », en l'occurrence la séquence du point d'insertion. Lorsque, à l'**étape 3**, ces phages infectent *S. aureus*-pDVB435 :

- chez un **phage non recombinant**, la séquence cible est intacte : Cas9 la reconnaît, coupe le génome viral en double brin, et le cycle avorte. Le phage ne se multiplie pas et ne forme pas de plage ;
- chez un **phage recombinant**, l'insertion de la cassette a détruit ou déplacé la séquence cible et son PAM : le guide ne trouve plus d'appariement, Cas9 ne coupe pas, le génome est répliqué et encapsidé normalement.

La coupure est **létale pour le phage** parce que, dans ce contexte, elle n'est pas réparée : *S. aureus* ne possède pas de voie de jonction d'extrémités non homologues, et le génome viral coupé ne dispose d'aucune matrice homologue utilisable. (La recombinaison homologue bactérienne, elle, existe bel et bien : c'est elle qui a réalisé l'insertion à l'étape 2.)

Le système réalise donc une **contre-sélection** : il n'avantage pas les recombinants, il élimine tout le reste. Le tri s'opère à l'étape 3, de sorte que les phages **récupérés et concentrés à l'étape 4 sont pratiquement tous des Φ80α-virGFP**, sans criblage individuel.

$$\boxed{\text{Cas9 coupe le génome des phages ayant conservé la cible ; seuls les recombinants, dont la cible est remplacée par RBS-}\textit{gfp}\text{, se multiplient.}}$$

### Q7. Obtenir des phages lytiques Φ80α-vir à partir de Φ80α

**Cible moléculaire.** Le caractère tempéré de Φ80α repose sur le module de lysogénie identifié en Q1 ; la bascule lyse/lysogénie est gouvernée par le **répresseur CI**, qui occupe les opérateurs et réprime les gènes lytiques précoces. Un mutant *vir* est un mutant **insensible à la répression**. Rendre le phage strictement lytique revient donc à **supprimer la fonction CI** et, pour être complet, à supprimer également l'**intégrase** *int*, ce qui interdit physiquement l'intégration au chromosome.

**Méthode proposée — remplacement allélique par recombinaison homologue, puis contre-sélection CRISPR** (transposition de la stratégie du document 3) :

1. **Construire un plasmide** portant deux bras d'homologie d'environ 500 nt correspondant aux régions flanquant *cI*–*int*, encadrant une délétion ou une courte séquence de substitution (codons stop dans les trois cadres).
2. **Transformer** *S. aureus* RN4220 par ce plasmide.
3. **Infecter** cette souche par Φ80α sauvage : pendant le cycle lytique, une fraction rare des génomes viraux subit un double crossing-over et perd *cI* (et *int*).
4. **Récupérer la descendance** et en **infecter une seconde souche** transformée par un plasmide CRISPR-Cas9 dont le guide cible la séquence *cI* sauvage : les phages ayant conservé *cI* sont coupés et éliminés, seuls les phages délétés se multiplient.
5. **Vérifier** le phénotype par trois critères indépendants : plages de lyse **claires** et non troubles, absence de formation de lysogènes sur boîte, et incapacité à être bloqué par une souche lysogène pour Φ80α.

**Variante par enzymes de restriction.** Le même objectif — supprimer les séquences codant la lysogénie — s'atteint par digestion du génome viral purifié au moyen d'enzymes de restriction encadrant le module *cI*–*int*, religature du génome délété, puis transfection de la souche hôte. La méthode est plus grossière (elle dépend de la présence de sites uniques bien placés) mais elle ne demande ni plasmide de recombinaison ni système CRISPR.

**Méthode alternative, sans génie génétique.** Historiquement, les mutants *vir* s'obtiennent par **sélection de mutants spontanés** : on étale une forte quantité de phages sauvages sur un tapis d'une souche **lysogène** pour Φ80α, immunisée par le CI qu'elle produit. Seuls les rares mutants insensibles à CI (mutations des opérateurs) forment des plages, que l'on repique. Rendement faible et mutation non contrôlée, mais aucun outil moléculaire requis ; une mutagenèse préalable (UV, agent alkylant) augmente la fréquence au prix de mutations secondaires.

$$\boxed{\text{Inactiver } \textit{cI} \text{ (et } \textit{int}\text{) par recombinaison homologue plasmidique, puis contre-sélectionner par CRISPR-Cas9 ciblant } \textit{cI}.}$$

### 3. *Staphylococcus aureus* RN4220

### Q8. Analyse fonctionnelle du milieu BHI Broth

Le bouillon BHI (*Brain Heart Infusion*) est un milieu **liquide, complexe (non synthétique), riche, tamponné et non sélectif**.

| Constituant (pour 1 L) | Nature / apport chimique | Rôle fonctionnel |
|---|---|---|
| Peptone — 10,0 g | Hydrolysat enzymatique de protéines : peptides courts, acides aminés libres | Source d'**azote** organique et de **carbone** directement assimilable ; fournit les acides aminés que *S. aureus*, auxotrophe pour plusieurs d'entre eux, ne sait pas synthétiser |
| Infusion de cervelle de veau — 12,5 g | Extrait tissulaire : peptides, acides aminés, lipides, vitamines du groupe B, bases azotées, oligo-éléments | Apport de **facteurs de croissance** non substituables ; permet la culture de bactéries exigeantes |
| Infusion de cœur de bœuf — 5,0 g | Extrait tissulaire complémentaire (nucléotides, minéraux, hème) | Même rôle ; la combinaison des deux infusions élargit le spectre des facteurs apportés |
| Chlorure de sodium — 5,0 g | Sels minéraux : Na⁺, Cl⁻ (≈ 86 mmol·L⁻¹) | Maintien de la **pression osmotique** et de l'**équilibre ionique** ; à 0,5 %, cette concentration n'a aucun effet sélectif |
| Hydrogénophosphate disodique anhydre — 2,5 g | Couple tampon HPO₄²⁻/H₂PO₄⁻ (p$K_{a2} \approx 7{,}2$), ≈ 18 mmol·L⁻¹ | **Double rôle** : pouvoir tampon limitant l'acidification due à la fermentation du glucose, et source de **phosphore** (acides nucléiques, ATP, phospholipides) |
| Glucose — 2,0 g | Ose simple, ≈ 11 mmol·L⁻¹ | **Source de carbone et d'énergie** rapidement métabolisable (glycolyse) ; soutient la croissance exponentielle rapide exigée par le protocole (phase exponentielle en ≈ 90 min) |
| Eau distillée — q.s.p. 1 000 mL | Solvant purifié, exempt d'ions parasites | **Solvant** de tous les constituants ; assure l'activité de l'eau et le transport des solutés |
| pH final 7,4 ± 0,2 à 25 °C | Paramètre physico-chimique | pH **neutre**, optimal pour *S. aureus* (neutrophile) et compatible avec la stabilité des virions |

**Conclusion.** Aucun constituant n'est inhibiteur ni indicateur : le BHI est un milieu **d'enrichissement non sélectif et non différentiel**, adapté à la production d'une forte biomasse en phase exponentielle, c'est-à-dire de cellules hôtes métaboliquement actives — exactement ce qu'exige la production de phages. Le complément de **5 mM CaCl₂** du document 2 n'appartient pas à la formule de base et n'a pas de rôle nutritionnel : il sert à l'**adsorption phagique**.

### Q9. Adaptation du milieu pour les souches OGM

Le document 4 indique que les deux souches modifiées, RN4220::*Ssc*-CBASS-cmᴿ et RN4220::*Ssc*-CdnE03-cmᴿ, portent toutes deux, intégrée au chromosome, une séquence **cmᴿ** codant la **résistance au chloramphénicol**. La souche sauvage en est dépourvue : le marqueur de sélection est donc fourni par l'énoncé.

**Adaptation proposée.** Ajouter au bouillon BHI du **chloramphénicol** à concentration sélective, soit environ **10 µg·mL⁻¹** pour *S. aureus* (usuellement 5 à 15 µg·mL⁻¹). L'antibiotique étant **thermolabile**, il ne doit pas être autoclavé : on prépare une solution mère concentrée dans l'éthanol, on la **stérilise par filtration à 0,22 µm** et on l'ajoute au milieu **après** autoclavage et refroidissement en dessous de 50 °C.

**Justification du couple mécanisme / sélection.** Le chloramphénicol est un inhibiteur de la **traduction** : il se fixe sur le centre peptidyl-transférase de la sous-unité **50S** du ribosome bactérien et bloque la formation de la liaison peptidique ; il est **bactériostatique**, à large spectre. Le gène cmᴿ code une **chloramphénicol acétyltransférase**, qui acétyle l'antibiotique et l'empêche de se fixer au ribosome.

- **Souches OGM** : elles produisent l'acétyltransférase, inactivent l'antibiotique et **croissent normalement**.
- **Souche sauvage** : dépourvue de cmᴿ, sa traduction est bloquée et sa **croissance est empêchée**, ce qu'exige l'énoncé.

**Deux réserves.** D'abord, le chloramphénicol étant **bactériostatique** et non bactéricide, il inhibe la souche sauvage sans la tuer : des cellules sauvages viables peuvent persister. Pour une élimination stricte, il faudrait augmenter la concentration, enchaîner des repiquages sélectifs ou choisir un marqueur bactéricide. Ensuite, ce milieu ne convient qu'à la **culture des souches** : le chloramphénicol bloquerait aussi la traduction des protéines virales et fausserait l'étude du CBASS. Il faut donc cultiver les OGM en BHI + chloramphénicol, puis **laver et transférer** les cellules en BHI sans antibiotique avant toute infection — c'est bien ce que fait le document 10, où seul du BHI + CaCl₂ est ajouté.

$$\boxed{\text{BHI Broth} + \text{chloramphénicol} \approx 10\ \mu\text{g}\cdot\text{mL}^{-1},\ \text{filtré à } 0{,}22\ \mu\text{m et ajouté après autoclavage.}}$$

### Q10. Allure des courbes de croissance dans les trois cas

Les trois cultures sont conduites en BHI Broth, à 37 °C, la densité optique à 600 nm étant portée en échelle logarithmique en fonction du temps. L'infection est réalisée à MOI = 0,1.

![Figure 2 — Allure des trois courbes de croissance : chute de la DO₆₀₀ vers 3–4 h dans les deux cultures infectées, reprise seulement avec le phage tempéré Φ80α](figures/q10-courbes-croissance.svg)

**Cas 1 — RN4220 sauvage seule (témoin).** Courbe de croissance canonique en milieu non renouvelé : **phase de latence** courte (milieu riche, inoculum issu d'une préculture, adaptation enzymatique minimale), **phase exponentielle** de pente maximale (temps de génération de *S. aureus* en BHI à 37 °C : ≈ 25–30 min), **ralentissement** puis **phase stationnaire** lorsque le glucose s'épuise et que les produits acides s'accumulent, enfin déclin lent.

**Cas 2 — RN4220 + Φ80α (phage tempéré).** Jusqu'à ≈ 2 h, la courbe est superposable au témoin : à MOI = 0,1, une bactérie sur dix seulement est initialement infectée et la croissance des non infectées masque la lyse. Après deux à trois cycles infectieux successifs (cycle de ≈ 30–45 min), la lyse devient synchrone à l'échelle de la population et la **densité optique s'effondre** — c'est la « perte totale de turbidité » observée à 3–4 h dans le document 2. **Mais la chute n'est pas définitive** : Φ80α étant **tempéré**, une fraction des cellules infectées est entrée en lysogénie. Ces lysogènes portent le prophage, expriment CI et bénéficient de l'**immunité de superinfection** : insensibles aux virions libres, ils repartent en croissance et la DO **remonte** après quelques heures. S'y ajoutent les mutants d'adsorption (récepteur pariétal altéré) sélectionnés par la pression phagique.

**Cas 3 — RN4220 + Φ80α-virGFP (phage strictement lytique).** Le début et la chute sont identiques (même hôte, même MOI, même cycle lytique). **La différence est en aval** : ce phage étant exclusivement lytique (module de lysogénie inactivé, Q5 et Q7), **aucun lysogène ne peut se former**. Aucune sous-population immunisée ne subsiste et la **DO reste basse durablement**. Seule une repousse tardive de mutants d'adsorption pourrait apparaître, plus lente et plus rare.

| | RN4220 seule | + Φ80α | + Φ80α-virGFP |
|---|---|---|---|
| Croissance initiale (0–2 h) | normale | normale | normale |
| Chute de DO | absente | marquée, vers 3–4 h | marquée, vers 3–4 h |
| Reprise ultérieure | — | **oui** (lysogènes immunisés) | **non** (sauf mutants rares, tardifs) |
| DO finale | maximale | intermédiaire | minimale |

**Précision indispensable.** La densité optique mesure une **turbidité**, donc la biomasse totale, cellules vivantes *et* cellules mortes non lysées : elle ne se confond pas avec un dénombrement de bactéries viables.

$$\boxed{\text{Témoin : croissance complète. Φ80α : lyse puis }\textbf{reprise}\text{ (lysogènes). Φ80α-virGFP : lyse }\textbf{sans reprise}\text{ (phage }\textit{vir}\text{).}}$$

### Q11. Intégration chromosomique plutôt que plasmide recombinant

Le document 4 porte la mention « *chromosomal integration* » : les séquences *Ssc*-CdnE03 ou *Ssc*-CBASS ont été insérées dans le chromosome bactérien.

**Avantages de l'intégration chromosomique.**

- **Stabilité génétique.** Le chromosome est répliqué et ségrégé fidèlement à chaque division, alors qu'un plasmide se perd par ségrégation aléatoire en l'absence de pression de sélection. C'est l'argument **décisif ici** : les expériences du document 10 durent 12 h, sans antibiotique dans le milieu (qui fausserait l'infection) ; seule l'intégration chromosomique garantit que toutes les bactéries observées portent encore le système.
- **Nombre de copies unique et défini.** Une copie par chromosome donne un niveau d'expression **physiologique**, comparable à celui du système natif. Un plasmide à 5, 20 ou 200 copies surexprimerait le système d'autant, au risque de créer artificiellement une immunité que la bactérie sauvage n'a pas : le phénotype observé ne serait plus qu'un artefact de dosage génique, inacceptable pour l'étude d'un mécanisme physiologique de défense.
- **Pas de charge métabolique ni de dissémination.** Pas de réplication plasmidique à financer, donc pas de biais de croissance ; et pas de transfert horizontal possible du système ou du marqueur de résistance.

**Inconvénients.**

- **Construction lourde et lente** : vecteur suicide ou recombinaison site-spécifique, sélection des intégrants, vérification du site par PCR et séquençage — là où une transformation plasmidique est affaire de quelques heures.
- **Faible niveau d'expression** : la copie unique peut rendre difficile la détection biochimique de la protéine ou sa purification, que facilite un plasmide multicopie.
- **Modification peu réversible et non transférable** : on ne « cure » pas une insertion chromosomique comme on perd un plasmide, et on ne la transfère pas telle quelle à une autre souche.
- **Effet de position** : l'insertion peut interrompre un gène ou perturber l'expression des gènes voisins ; il faut vérifier que le phénotype vient bien de la construction et non de la lésion créée.

$$\boxed{\text{Stabilité sans antibiotique + copie unique (expression physiologique) ; mais construction lourde, expression faible, effet de position.}}$$

### Q12 (rédactionnelle). Diversité structurale des virus, cycle viral, mise en évidence et quantification

**Introduction.** Un virus est une **entité biologique acellulaire**, **parasite intracellulaire obligatoire**, dépourvue de métabolisme propre et de machinerie de traduction. Il se réduit à un génome — un seul type d'acide nucléique, ADN **ou** ARN — protégé par une coque protéique, la capside, l'ensemble formant la **nucléocapside**, parfois entourée d'une enveloppe lipidique empruntée aux membranes de l'hôte. Le bactériophage Φ80α étudié ici en est un représentant, mais il n'illustre qu'une des morphologies possibles. Nous montrerons d'abord l'ampleur de la diversité structurale des virus, puis que cette diversité recouvre un schéma fonctionnel commun, le cycle viral, et nous proposerons enfin une méthode permettant de détecter et de quantifier spécifiquement un virus au cours d'une infection.

**I. Une diversité structurale considérable, organisée par quatre critères**

*1. Nature et topologie du génome.* C'est le critère fondateur de la classification de Baltimore. Le génome peut être de l'**ADN double brin** (Φ80α, Adénovirus, virus de l'herpès), de l'**ADN simple brin** (Parvovirus B19, phage M13), de l'**ARN double brin** (Rotavirus), de l'**ARN simple brin de polarité positive**, directement traduisible comme un ARN messager (Poliovirus, SARS-CoV-2), ou de l'**ARN simple brin de polarité négative**, qui impose au virus d'emporter sa propre ARN polymérase ARN-dépendante dans le virion (virus de la grippe, de la rage, Ebola). Les **rétrovirus** (VIH) ont un ARN positif rétrotranscrit en ADN par une transcriptase inverse. La topologie varie aussi : génome **linéaire** (Φ80α, Adénovirus) ou **circulaire** (phage φX174) ; **monopartite** ou **segmenté** — les huit segments du virus de la grippe A autorisent des réassortiments entre souches, à l'origine des pandémies.

*2. Symétrie de la capside.*

- **Symétrie icosaédrique** : polyèdre régulier à 20 faces triangulaires, construit par autoassemblage de capsomères identiques — l'architecture la plus économe en information génétique (Adénovirus, Poliovirus, Papillomavirus).
- **Symétrie hélicoïdale** : les protomères s'enroulent autour du génome en une hélice dont la longueur est fixée par celle de l'acide nucléique. Exemple canonique : le virus de la mosaïque du tabac, bâtonnet rigide de 300 nm ; les virus de la grippe et de la rage ont une nucléocapside hélicoïdale souple, repliée dans une enveloppe.
- **Symétrie complexe ou mixte** : les **phages caudés** comme Φ80α associent une tête icosaédrique et une queue hélicoïdale à fibres ; les Poxvirus (variole) sont des briques de 300 nm sans symétrie régulière.

*3. Présence ou absence d'enveloppe.* Les virus **nus** (Φ80α, Poliovirus, Adénovirus, Norovirus) n'ont pas de bicouche lipidique : ils résistent à la dessiccation, aux solvants organiques et aux détergents, d'où leur transmission féco-orale et leur persistance dans l'environnement — et, dans ce sujet, la possibilité de conserver le lysat à 4 °C après filtration. Les virus **enveloppés** (VIH, grippe, SARS-CoV-2, herpès) portent une membrane dérivée de l'hôte, hérissée de glycoprotéines : fragiles hors de l'organisme, mais capables d'entrer par fusion membranaire et partiellement camouflés vis-à-vis de l'immunité.

*4. Taille.* De ≈ 20 nm (Parvovirus) à ≈ 300 nm (Poxvirus) et jusqu'à ≈ 700 nm pour le Mimivirus, plus gros qu'une petite bactérie ; 30 nm pour un Poliovirus, 100 nm pour le VIH, 60–200 nm pour un phage caudé. Presque tous restent en deçà du pouvoir de résolution du microscope optique, d'où le recours à la microscopie électronique pour les observer.

```text
Quatre morphotypes
  (a) icosaédrique nu : capside polyédrique, pas d'enveloppe        (Adénovirus)
  (b) hélicoïdal nu   : bâtonnet rigide, protomères en hélice        (TMV)
  (c) enveloppé       : nucléocapside + bicouche + spicules          (SARS-CoV-2)
  (d) complexe caudé  : tête icosaédrique + queue + fibres           (Φ80α)
```

**II. Une unité fonctionnelle : les grandes étapes du cycle viral**

Quelle que soit sa structure, tout virus, incapable de produire son ATP et de traduire ses ARN, doit détourner une cellule. Le cycle se décompose universellement en six étapes.

1. **Attachement (adsorption).** Une protéine de surface du virion — fibres caudales chez Φ80α, protéine Spike chez le SARS-CoV-2, gp120 chez le VIH — reconnaît spécifiquement un **récepteur** de la cellule cible : acide teichoïque de la paroi staphylococcique, enzyme de conversion de l'angiotensine 2, molécule CD4. Cette reconnaissance détermine le **tropisme**. Chez les phages, l'adsorption exige souvent des cations divalents, d'où les 5 mM de CaCl₂ du document 2.
2. **Pénétration et décapsidation.** Un phage caudé **injecte** son seul ADN à travers la paroi et la membrane, la capside vide restant à l'extérieur ; un virus nu animal entre par **endocytose** ; un virus enveloppé entre par **fusion** de son enveloppe avec la membrane plasmique ou endosomale. Dans les deux derniers cas, une **décapsidation** libère ensuite le génome.
3. **Expression précoce et détournement de la cellule.** Sont produites les protéines non structurales : polymérases, protéines de réplication, protéines d'inhibition des défenses de l'hôte. Chez Φ80α, c'est le moment de la bascule CI/Cro qui décide de la lyse ou de la lysogénie, et c'est aussi celui où s'exprime la cassette *gfp* du phage rapporteur.
4. **Réplication du génome**, selon une stratégie propre à chaque classe de Baltimore : réplication semi-conservative pour les virus à ADN, ARN polymérase ARN-dépendante virale pour les virus à ARN, transcription inverse puis intégration pour les rétrovirus. Elle est massivement amplificatrice.
5. **Assemblage et maturation.** L'**expression tardive** fournit les protéines de structure ; les capsides s'autoassemblent, puis le génome est encapsidé — chez Φ80α, par translocation active à travers le portail sous l'action de la terminase TerS/TerL, avant fixation de la queue préassemblée. Des **clivages protéolytiques** de maturation rendent le virion infectieux.
6. **Libération.** Soit la **lyse**, brutale et létale — chez Φ80α, l'holine perméabilise la membrane et l'endolysine hydrolyse le peptidoglycane, libérant d'un coup une centaine de virions ; soit le **bourgeonnement**, progressif, qui laisse la cellule survivre un temps (VIH, grippe). Une voie particulière est le **cycle lysogénique** des phages tempérés, où le génome s'intègre au chromosome et se transmet verticalement jusqu'à une induction ultérieure.

**III. Détecter et quantifier spécifiquement un virus : la RT-qPCR**

Deux logiques coexistent. La **quantification du pouvoir infectieux** repose sur des méthodes biologiques : **dénombrement sur gélose avec plages de lyse** pour un phage (PFU·mL⁻¹, questions Q3–Q4), dose infectieuse 50 % en culture cellulaire pour un virus animal ; spécifiques d'une activité, mais lentes et inapplicables à un virus non cultivable. La **quantification des particules ou des génomes** repose sur des méthodes moléculaires ou immunologiques, plus rapides et plus sensibles : **qPCR** ou **RT-qPCR**, **hybridation par sonde moléculaire**, **ELISA** dirigé contre une protéine de capside, **microscopie** électronique ou à immunofluorescence pour un comptage direct de particules. C'est la seconde famille que nous détaillons, en retenant la méthode la plus spécifique et la plus quantitative.

*Principe.* La **RT-qPCR** (transcription inverse suivie d'une PCR quantitative en temps réel) détecte et dénombre les génomes viraux. Sa **spécificité** repose sur trois reconnaissances moléculaires : le couple d'**amorces**, choisi dans une région du génome propre au virus recherché et absente de l'hôte ; la **sonde d'hydrolyse** interne, marquée par un fluorochrome émetteur et un extincteur ; et la **température d'hybridation**, ajustée au $T_m$ des amorces.

*Déroulement.* Extraction des acides nucléiques de l'échantillon ; **transcription inverse** de l'ARN viral en ADN complémentaire (étape omise pour un virus à ADN, on parle alors de qPCR) ; **amplification** sur une quarantaine de cycles de dénaturation (95 °C), hybridation (≈ 60 °C) et élongation. À chaque élongation, l'activité exonucléasique 5′→3′ de la polymérase hydrolyse la sonde : l'émetteur, séparé de l'extincteur, **émet**. La fluorescence croît donc avec le nombre d'amplicons.

*Quantification.* On définit le **$C_t$**, numéro du cycle auquel la fluorescence franchit un seuil fixé au-dessus du bruit de fond. En régime exponentiel, $Q_n = Q_0 (1+E)^n$ avec $E$ l'efficacité, d'où une relation **affine** entre $C_t$ et $\log_{10} Q_0$ :

$$C_t = -\frac{1}{\log_{10}(1+E)}\ \log_{10}(Q_0) + \text{constante}.$$

La quantification est **absolue** si l'on établit une gamme d'étalonnage à partir de dilutions décimales d'un standard de concentration connue : la droite $C_t = f(\log_{10} Q_0)$ a une pente de $-3{,}32$ pour une efficacité de 100 % (car $\log_2 10 \approx 3{,}32$ cycles par décade), et l'on y reporte le $C_t$ de l'échantillon. Elle est **relative** si l'on compare l'échantillon à un calibrateur.

*Témoins obligatoires.* Témoin négatif d'extraction et témoin sans matrice (contamination), témoin positif, et **contrôle interne d'amplification** validant l'absence d'inhibiteurs de PCR.

*Limites et méthodes complémentaires.* La RT-qPCR quantifie des **génomes**, non des **virions infectieux** : elle reste positive alors qu'il ne subsiste que des débris génomiques. Pour conclure à une infection productive, on l'associe à une méthode fonctionnelle (culture, plages de lyse) ou à la détection de protéines virales par **ELISA**. La **sérologie**, elle, témoigne d'un contact avec le virus mais ne quantifie pas le virus lui-même.

**Conclusion.** La diversité structurale des virus — nature du génome, symétrie, enveloppe, taille — masque une remarquable unité de fonction : tous suivent la même séquence attachement – pénétration – expression – réplication – assemblage – libération, et tous imposent à l'hôte de fournir énergie et ribosomes. C'est cette unité qui rend les méthodes de détection transposables d'un virus à l'autre, et c'est elle aussi qui explique que les hôtes aient développé des défenses ciblant des étapes communes du cycle — le système CBASS étudié ici en est un exemple, qui interrompt le cycle entre la réplication et la libération.

---

## Partie 2. Étude du système immunitaire CBASS

### 1. Étude de la structure de la cyclase Ssc-CdnE03

### Q13. Nature et caractéristiques ioniques de K9, K13 et R83

Dans la nomenclature employée, la lettre est le code à une lettre de l'acide aminé et le nombre sa position dans la chaîne polypeptidique.

- **K9 et K13 : deux lysines** (Lys). Chaîne latérale $-(\mathrm{CH_2})_4-\mathrm{NH_3^+}$ : quatre carbones aliphatiques terminés par une **amine primaire** en position ε.
- **R83 : une arginine** (Arg). Chaîne latérale $-(\mathrm{CH_2})_3-\mathrm{NH}-\mathrm{C}(\mathrm{NH_2})_2^+$ : trois carbones terminés par un groupement **guanidinium**.

Ces trois résidus appartiennent à la famille des acides aminés **basiques**, à chaîne latérale chargée positivement.

| Résidu | Code 3 lettres | Groupement ionisable | p$K_R$ | Charge à pH 7,4 |
|---|---|---|---|---|
| Lysine (K9, K13) | Lys | ε-ammonium $-\mathrm{NH_3^+}$ | ≈ 10,5 | $+1$ |
| Arginine (R83) | Arg | guanidinium | ≈ 12,5 | $+1$ |

**Justification quantitative.** La relation de Henderson-Hasselbalch, $\mathrm{pH} = \mathrm{p}K_a + \log_{10}\big([\mathrm{A^-}]/[\mathrm{AH}]\big)$, donne pour la lysine à pH 7,4 :

$$\begin{aligned}
\log_{10}\frac{[\mathrm{NH_2}]}{[\mathrm{NH_3^+}]} &= 7{,}4 - 10{,}5 \\
&= -3{,}1 \\
\frac{[\mathrm{NH_3^+}]}{[\mathrm{NH_2}]} &\approx 1{,}3\times10^{3}
\end{aligned}$$

soit **plus de 99,9 % de forme protonée**. Pour l'arginine, l'écart de 5,1 unités porte ce rapport à ≈ 10⁵ : la protonation est totale. Le guanidinium est en outre exceptionnellement stable, sa charge positive étant **délocalisée par résonance** sur ses trois azotes — d'où son p$K_a$ très élevé et sa charge permanente dans toutes les conditions physiologiques.

$$\boxed{\text{K9 et K13 = lysines (ε-NH}_3^+\text{, p}K_R \approx 10{,}5\text{) ; R83 = arginine (guanidinium, p}K_R \approx 12{,}5\text{) ; charge } +1 \text{ chacun à pH 7,4.}}$$

### Q14. Argumentation de la liaison ARN – cyclase

**Propriétés physico-chimiques de l'ARN.** Un ARN est un polymère de ribonucléotides unis par des **liaisons phosphodiester** 3′–5′. Chaque phosphate intercalé entre deux riboses porte une fonction acide de p$K_{a} \approx 1$ : à pH physiologique, il est **totalement déprotoné** et porte une **charge négative**. Un ARN de $n$ nucléotides porte donc environ $n$ charges négatives régulièrement réparties : c'est un **polyanion linéaire de forte densité de charge**, et cette charge est **indépendante de la séquence**. Les bases azotées, aromatiques et globalement non chargées à ce pH, offrent en revanche des donneurs et accepteurs de liaison hydrogène et peuvent s'empiler. Le ribose porte un hydroxyle 2′, absent de l'ADN, qui impose la conformation A aux hélices et constitue un point de reconnaissance propre à l'ARN.

**Propriétés de la zone d'interaction (document 5).** La cartographie du potentiel électrostatique de surface montre une protéine globalement **acide** — les zones rouges, de potentiel négatif, dominent — à l'exception d'une **poche nettement bleue**, donc de potentiel **positif**, encadrée et désignée comme « zone d'interaction ARN-cyclase ». L'agrandissement attribue ce potentiel positif à la convergence spatiale des chaînes latérales de **K9, K13 et R83**, trois résidus éloignés dans la séquence primaire mais rapprochés par le repliement : le site est **discontinu**, créé par la structure tertiaire.

**Argumentation de la liaison.** Elle repose sur une **complémentarité électrostatique**.

- **Liaisons ioniques (ponts salins)** entre les ammoniums des lysines, le guanidinium de l'arginine et les oxygènes phosphate du squelette de l'ARN. Individuellement de l'ordre de quelques dizaines de kJ·mol⁻¹, leur multiplicité assure une forte affinité globale.
- **Liaisons hydrogène** : le guanidinium est un donneur **bidentate**, capable de former deux liaisons hydrogène simultanées avec les deux oxygènes non pontants d'un même phosphate — géométrie idéale, qui explique la fréquence des arginines dans les sites de liaison aux acides nucléiques.
- **Contribution entropique** : la formation de chaque pont salin libère des molécules d'eau et des contre-ions auparavant ordonnés autour des deux partenaires.

**Deux corollaires.** D'une part, ces interactions portent sur le **squelette** et sont donc *a priori* **non spécifiques de séquence** : la sélectivité observée plus loin (Q18) ne peut venir du seul contact électrostatique, mais de la **structure secondaire et tertiaire** de l'ARN ligand, qui doit s'ajuster géométriquement à la poche. D'autre part, la liaison est **sensible à la force ionique** : une forte concentration en sel écrante les charges et dissocie le complexe — propriété que l'on exploitera pour **éluer** l'ARN de la colonne d'affinité (Q15).

$$\boxed{\text{ARN polyanionique (phosphates déprotonés)} \longleftrightarrow \text{poche basique (K9, K13, R83) : ponts salins et liaisons hydrogène, non spécifiques de séquence.}}$$

### 2. Étude de l'affinité de la cyclase Ssc-CdnE03

### Q15. Étapes de la chromatographie d'affinité (schéma légendé et explicité)

La chromatographie d'affinité est une méthode séparative fondée sur une **interaction biospécifique et réversible** entre un **ligand** greffé sur la phase stationnaire et l'espèce à purifier. Ici, l'objet purifié n'est pas la protéine mais son **partenaire** : le ligand immobilisé est la **cyclase Ssc-CdnE03**, et l'on recherche les **ARN** capables de s'y fixer.

![Figure 3 — Les cinq étapes de la chromatographie d'affinité : la cyclase Ssc-CdnE03 est le ligand greffé, et l'élution par augmentation de la force ionique fournit les ARN qui lui sont liés](figures/q15-chromatographie-affinite.svg)

**1. Préparation et équilibration.** La cyclase, produite par voie recombinante (le plus souvent avec une étiquette polyhistidine), est immobilisée sur la matrice — couplage covalent sur résine activée, ou chélation par Ni²⁺-NTA. La colonne est rincée par le **tampon d'équilibration**, dont le pH et la force ionique rendent l'interaction possible : pH ≈ 7,5, où lysines et arginine sont protonées (Q13), et force ionique **faible** (50 à 150 mM NaCl), un excès de sel écrantant les charges et empêchant la fixation.

**2. Dépôt de l'échantillon.** On charge l'extrait d'**ARN totaux** de la condition testée (« – », « RN4220 » ou « Φ80α »), à débit lent pour laisser l'équilibre de liaison s'établir. Les ARN reconnus par la poche basique s'y fixent, les autres traversent.

**3. Lavage.** Plusieurs volumes de colonne de tampon d'équilibration **éliminent les ARN non retenus et les interactions faibles ou non spécifiques**. Cette étape conditionne la pureté du résultat : un lavage insuffisant laisse un bruit de fond sur le gel, un lavage trop agressif décroche le ligand recherché.

**4. Élution.** On rompt volontairement l'interaction. Trois voies : **augmentation de la force ionique** (NaCl 0,5 à 1 M), qui écrante les interactions électrostatiques — la voie la plus logique ici, compte tenu de la nature ionique de la liaison établie en Q14 ; **élution compétitive** par un excès de ligand libre ; ou **élution du complexe entier** par l'imidazole si le système repose sur une étiquette histidine, la protéine sortant alors avec son ARN. **C'est cette étape, et elle seule, qui fournit les ARN liés à la cyclase** demandés par l'énoncé.

**5. Récupération et analyse.** Les fractions d'élution sont collectées, éventuellement déprotéinisées et concentrées, puis déposées sur gel d'agarose : c'est le contenu du document 7.

$$\boxed{\text{équilibration} \rightarrow \text{dépôt} \rightarrow \text{lavage} \rightarrow \textbf{élution (force ionique)} \rightarrow \text{éluat = ARN liés à la cyclase}}$$

### Q16. Polarité et nom des électrodes E1 et E2

**Charge de l'échantillon.** Comme établi en Q14, un ARN est un **polyanion** : dans le tampon d'électrophorèse (pH ≈ 8), tous ses phosphates sont déprotonés. La charge est proportionnelle à la longueur, donc le rapport charge/masse est **constant** : la migration ne dépend que de l'effet tamis de l'agarose, et **les molécules courtes migrent plus loin** que les longues.

**Sens de migration.** Un ion migre vers l'électrode de signe opposé au sien : les ARN, négatifs, migrent vers l'**anode**, pôle **positif** (en électrophorèse, régime imposé, l'anode est le pôle +, siège de l'oxydation).

**Lecture du document 7.** L'échelle de tailles décroît du haut vers le bas (2 000, 1 000, 500, 400, 200, 100, 50 nt) : les molécules les plus courtes sont donc les plus basses, la migration s'est faite **du haut vers le bas**, les puits de dépôt sont en haut, du côté de E1, et le front de migration en bas, du côté de E2.

| Électrode | Position | Polarité | Nom |
|---|---|---|---|
| E1 | haut, côté des puits | $\ominus$ (négatif) | **cathode** |
| E2 | bas, côté du front | $\oplus$ (positif) | **anode** |

$$\boxed{\text{E1 = cathode, pôle négatif ; E2 = anode, pôle positif.}}$$

### Q17. Intérêt de l'échantillon d'ARN de cellules non infectées « RN4220 »

L'échantillon « RN4220 » contient l'ARN total de bactéries **non infectées** : ARN ribosomiques (80 à 85 % de l'ARN total), ARN de transfert, ARN messagers, petits ARN régulateurs. C'est un **témoin négatif biologique**, à distinguer du témoin « – », qui est un témoin *technique* sans aucun ARN.

Il permet de tester une hypothèse alternative précise : **la cyclase retient-elle n'importe quel ARN ?** La question est légitime, puisque l'interaction établie en Q14 est électrostatique et porte sur le squelette phosphate, commun à tous les ARN. Si la fixation n'était due qu'à la charge, les ARN bactériens abondants — ARN ribosomiques 16S (≈ 1 540 nt) et 23S (≈ 2 900 nt) en tête — seraient retenus et apparaîtraient sur le gel. Le témoin tranche donc entre deux interprétations :

- **si une bande apparaissait** dans cette piste, la fixation serait **non spécifique**, la colonne se comporterait comme un simple échangeur d'ions et la bande de la piste « Φ80α » n'aurait aucune signification biologique ;
- **si aucune bande n'apparaît**, la cyclase ne retient pas les ARN de l'hôte non infecté, et toute bande observée en piste « Φ80α » est nécessairement liée à l'**infection**.

Ce témoin remplit donc trois fonctions : il contrôle la **spécificité** du ligand, il valide la **qualité du lavage**, et il fournit la **ligne de base biologique** de la comparaison. Il documente accessoirement l'absence d'**auto-immunité** du système : une cyclase qui se fixerait aux ARN de sa propre bactérie déclencherait en permanence la mort de celle-ci.

$$\boxed{\text{Témoin négatif biologique : il vérifie que la cyclase ne fixe pas les ARN de l'hôte, donc que toute fixation observée est spécifique de l'infection.}}$$

### Q18. Analyse du gel et conclusion sur l'activation de la cyclase

**Analyse, piste par piste.**

- **Piste « – » (sans ARN)** : aucune bande. La colonne ne libère par elle-même aucun acide nucléique : ni contamination, ni ARN coélué avec la protéine recombinante. Le contrôle technique est validé.
- **Piste « RN4220 » (cellules non infectées)** : aucune bande visible. Bien que l'échantillon chargé contînt la totalité des ARN d'une bactérie, donc une immense majorité d'ARN ribosomiques, **aucun** n'a été retenu assez stablement pour se retrouver dans l'éluat.
- **Piste « Φ80α » (cellules infectées)** : une bande **unique, fine et bien définie**, située entre les repères 500 et 1 000 nt et plus proche de 1 000, soit une taille d'environ **700 nt** (l'échelle étant logarithmique et la lecture graphique, on retiendra l'ordre de grandeur 600–800 nt). Le caractère unique et net de la bande est aussi informatif que sa présence : il exclut un mélange hétérogène et désigne **une seule espèce d'ARN**.

**Interprétation.** Les pistes 2 et 3 ne diffèrent que par un paramètre, la présence ou l'absence d'infection : l'ARN retenu est donc **apparu avec l'infection**. Deux origines restent possibles — un **transcrit viral**, hypothèse la plus directe et celle des auteurs de l'étude, ou un ARN bactérien dont la transcription serait induite par l'infection. Le gel seul ne permet pas de trancher : il faudrait séquencer la bande. La conclusion mécanistique est la même dans les deux cas.

**Conclusion sur l'activation.** La cyclase Ssc-CdnE03 est une enzyme **dont l'activateur est un ARN spécifique produit lors de l'infection**. Elle fonctionne donc comme un **senseur moléculaire de l'infection** : en l'absence de phage, l'ARN activateur n'existe pas, la poche basique reste vide, l'enzyme est inactive et aucun nucléotide cyclique n'est produit ; dès l'infection, cet ARN s'accumule, se fixe dans la poche K9/K13/R83 et provoque le changement conformationnel **allostérique** qui organise le site catalytique. C'est le **premier maillon** de la cascade CBASS, celui de la **détection du non-soi**.

La sélectivité impose enfin une précision : le contact électrostatique de Q14 n'étant pas spécifique de séquence, elle provient nécessairement de la **structure secondaire et tertiaire** de cet ARN, que seul l'ARN viral adopte. La charge fournit l'énergie de liaison, la forme fournit la sélectivité.

$$\boxed{\text{Un seul ARN, d'environ 700 nt, présent uniquement lors de l'infection, se fixe à la cyclase : la cyclase est un senseur activé par un ARN viral spécifique.}}$$

### 3. Suivi de l'infection virale et de la réponse bactérienne par microscopie à fluorescence

### Q19. Structures secondaires de la GFP (document 8a)

Le modèle tridimensionnel en rubans, présenté sous deux angles, code chaque type de structure par une forme et une couleur. On en identifie **trois**, qu'il faut nommer avec leur couleur.

- **Des feuillets β (en jaune)**, figurés par de larges flèches plates : **très majoritaires**, ils constituent l'ossature de la protéine. Les flèches voisines pointent en sens opposés : les brins sont **antiparallèles**, et ils sont **enroulés en cylindre fermé** — les **11 brins β** du **tonneau β** de la GFP. Un feuillet β est stabilisé par des liaisons hydrogène *inter-brins* entre le C=O d'un résidu et le N–H d'un résidu du brin voisin, la chaîne étant en conformation étendue (≈ 0,34 nm par résidu).
- **Des hélices α (en violet)**, figurées par des rubans en spirale : peu nombreuses et courtes. **L'une d'elles traverse l'axe du tonneau et porte le chromophore**, visible au centre en représentation « boules et bâtonnets » ; les autres referment les extrémités du cylindre. Une hélice α est stabilisée par des liaisons hydrogène *intra-chaîne* entre le C=O du résidu $i$ et le N–H du résidu $i+4$, avec 3,6 résidus et 0,54 nm par tour.
- **Des coudes et boucles (en vert)**, non répétitifs, assurant les changements de direction entre brins consécutifs : ce ne sont pas des structures secondaires régulières.

**Précision de vocabulaire.** Le **tonneau β** n'est pas une structure secondaire mais un **motif de structure tertiaire**, résultant de l'agencement spatial de brins β. Les structures secondaires présentes sont donc les **feuillets β antiparallèles** et les **hélices α**.

**Signification fonctionnelle.** Le tonneau forme une **cage rigide** qui isole le chromophore du solvant, empêche sa désexcitation non radiative par collision avec les molécules d'eau, et confère à la GFP son rendement quantique élevé (≈ 0,8) comme sa grande stabilité.

$$\boxed{\text{Feuillets β antiparallèles en jaune (11 brins, motif en tonneau β), hélices α en violet (dont l'hélice axiale portant le chromophore), coudes et boucles en vert.}}$$

### Q20. Nature et nombre des composants du chromophore

Le document 8b montre l'état « pré-cyclisation » et identifie explicitement les trois résidus en cause : **Ser65**, **Tyr66** et **Gly67**.

**Nombre.** Le chromophore est formé de **trois acides aminés**, et de trois seulement : un **tripeptide contigu** de la chaîne polypeptidique, aux positions 65, 66 et 67. C'est le fait remarquable de la GFP : le chromophore n'est pas un cofacteur importé (contrairement à l'hème d'une hémoglobine ou au rétinal d'une rhodopsine), il est **intrinsèque à la séquence protéique**.

| Position | Résidu | Chaîne latérale | Rôle dans le chromophore |
|---|---|---|---|
| 65 | **Sérine** (Ser, S) | $-\mathrm{CH_2OH}$, polaire non chargée | Fournit le carbonyle du squelette attaqué lors de la cyclisation |
| 66 | **Tyrosine** (Tyr, Y) | $-\mathrm{CH_2}-\mathrm{C_6H_4}-\mathrm{OH}$, aromatique polaire | Apporte le **cycle phénolique**, cœur du système conjugué |
| 67 | **Glycine** (Gly, G) | $-\mathrm{H}$, la plus petite, achirale | Fournit l'azote nucléophile ; sa petitesse rend la cyclisation géométriquement possible |

**Nature chimique du chromophore mature.** Après maturation (Q21), ces trois résidus forment le **4-(p-hydroxybenzylidène)-5-imidazolinone** : un cycle **imidazolinone** à cinq sommets, issu de la cyclisation Ser65–Gly67, relié par un **pont méthylidène** $=\mathrm{CH}-$ au **cycle phénolique** de la tyrosine. L'ensemble constitue un système de **doubles liaisons conjuguées** étendu sur les deux cycles, responsable de l'absorption dans le visible.

$$\boxed{\text{Trois acides aminés contigus : Ser65 – Tyr66 – Gly67, formant après maturation le p-hydroxybenzylidène-imidazolinone.}}$$

### Q21. Modifications nécessaires à l'obtention du chromophore mature

Le tripeptide Ser65-Tyr66-Gly67 subit, une fois la protéine repliée en tonneau, une **maturation post-traductionnelle autocatalytique** en trois modifications successives.

```text
Ser65-Tyr66-Gly67            Intermédiaire cyclisé            Chromophore mature
(état pré-cyclisation)  -->  (hémiaminal)              -->    (système conjugué)
        1. cyclisation             2. déshydratation (- H2O)
        (N de Gly67 sur            3. oxydation (+ O2 -> H2O2)
         le C=O de Ser65)
```

**1. Cyclisation intramoléculaire.** L'**azote amide de Gly67**, nucléophile, attaque le **carbone du carbonyle de Ser65**, électrophile. Il se forme un **hétérocycle à cinq sommets** de type imidazolinone, à l'état d'**hémiaminal** — le document 8b montre bien un carbone portant simultanément $-$OH et $-$NH dans l'intermédiaire. Cette réaction n'est possible que parce que le repliement en tonneau a rapproché et contraint les trois résidus : c'est la structure tertiaire qui rend la chimie possible.

**2. Déshydratation.** L'élimination d'une molécule d'eau à partir de l'hémiaminal installe une double liaison C=N dans l'imidazolinone.

**3. Oxydation par le dioxygène.** C'est l'étape décisive, et la seule à exiger un réactif extérieur. Le **dioxygène** oxyde la liaison $\mathrm{C}_\alpha-\mathrm{C}_\beta$ de la **tyrosine 66** et crée la **double liaison exocyclique** entre le cycle imidazolinone et le cycle phénolique ; le document 8b indique la production concomitante de **peroxyde d'hydrogène** et d'eau. C'est cette double liaison qui **met les deux cycles en conjugaison** : le système $\pi$ délocalisé s'étend sur tout le chromophore, l'écart énergétique entre orbitales frontalières diminue, et l'absorption se déplace vers le proche UV et le visible. **Avant cette oxydation, la protéine n'est pas fluorescente ; après, elle l'est.**

**Conséquences pratiques.**

- La maturation est **autocatalytique** : ni enzyme accessoire ni cofacteur, ce qui explique que le seul gène *gfp* suffise à rendre fluorescent n'importe quel organisme.
- Elle **exige du dioxygène** : en anaérobiose stricte, la GFP est produite mais reste non fluorescente.
- Elle est **lente** : de quelques minutes à quelques dizaines de minutes, d'où un **délai** entre la traduction et l'apparition du signal, à prendre en compte dans l'interprétation cinétique du document 10.
- Le chromophore mature existe sous deux formes en équilibre acido-basique, **phénol** (neutre) et **phénolate** (anionique), toutes deux représentées sur le document 8b — ce qui expliquera les deux bandes d'excitation du document 8c.

$$\boxed{\text{(1) cyclisation} \rightarrow \text{(2) déshydratation} \rightarrow \text{(3) oxydation par O}_2 \text{ (avec production de H}_2\mathrm{O}_2\text{).}}$$

### Q22. Choix des longueurs d'onde et lien avec le mécanisme de fluorescence

**Lecture des spectres (document 8c).**

- Le **spectre d'excitation** présente un **maximum principal vers 395 nm** et un **épaulement secondaire vers 475 nm**, d'amplitude relative ≈ 0,25. Ces deux bandes correspondent aux deux formes du chromophore en équilibre (Q21) : la forme **phénol** neutre absorbe vers 395 nm, la forme **phénolate**, plus conjuguée donc plus basse en énergie, vers 475 nm.
- Le **spectre d'émission** présente un **maximum unique vers 508 nm**, avec une décroissance étalée vers 550–570 nm. Qu'une seule bande d'émission réponde à deux bandes d'excitation traduit une déprotonation à l'état excité : quelle que soit la forme excitée, l'émission part du même état.

**Choix retenus.**

- **Excitation** : $\lambda_{\mathrm{exc}} = 395$ nm donne le signal maximal. En pratique, sur un microscope à épifluorescence ou un cytomètre, on excite plutôt sur le pic secondaire, à **475–488 nm** : le rendement est moindre, mais l'excitation bleue est bien moins phototoxique et provoque moins d'autofluorescence cellulaire — argument décisif ici, où l'on observe des bactéries **vivantes** pendant 12 h.
- **Émission** : on collecte autour de $\lambda_{\mathrm{em}} = 508$ nm, au moyen d'un filtre passe-bande centré vers 510 nm et large d'une trentaine de nanomètres, qui recueille le maximum du signal en excluant la lumière d'excitation.

**Lien avec le mécanisme.** Le phénomène s'explique par le diagramme de Perrin-Jablonski, en trois temps : **absorption** (≈ 10⁻¹⁵ s) d'un photon d'énergie $E = hc/\lambda_{\mathrm{exc}}$, qui porte le chromophore de S₀ à un niveau vibrationnel excité de S₁ ; **relaxation vibrationnelle et conversion interne** (10⁻¹²–10⁻¹⁰ s), qui dissipent l'excédent d'énergie **sans émission de lumière** jusqu'au bas de S₁ ; **émission de fluorescence** (≈ 10⁻⁹ s), retour à S₀ avec émission d'un photon d'énergie $E' = hc/\lambda_{\mathrm{em}} < E$. Comme $E' < E$, nécessairement $\lambda_{\mathrm{em}} > \lambda_{\mathrm{exc}}$ : c'est le **déplacement de Stokes**.

$$\Delta\lambda_{\mathrm{Stokes}} = 508 - 395 = 113\ \text{nm}.$$

Vérification énergétique, avec $hc = 1240$ eV·nm :

$$\begin{aligned}
E &= \frac{1240}{395} \approx 3{,}14\ \text{eV} \\
E' &= \frac{1240}{508} \approx 2{,}44\ \text{eV} \\
E - E' &\approx 0{,}70\ \text{eV}
\end{aligned}$$

soit **environ 22 % de l'énergie de chaque photon absorbé perdue par relaxation vibrationnelle**. Cette perte d'énergie *par photon* ne doit pas être confondue avec le **rendement quantique de fluorescence**, qui est le *rapport du nombre de photons émis au nombre de photons absorbés* : il vaut ≈ 0,8 pour la GFP, et s'explique séparément par la protection du chromophore dans le tonneau β (Q19), qui ferme les voies de désexcitation non radiative.

Enfin, c'est le déplacement de Stokes qui rend la séparation optique possible — et qui permettra de distinguer dans une même cellule la GFP (verte, 508 nm) de l'iodure de propidium (rouge, 617 nm).

$$\boxed{\lambda_{\mathrm{exc}} \approx 395\ \text{nm (ou 488 nm en imagerie du vivant)},\qquad \lambda_{\mathrm{em}} \approx 508\ \text{nm},\qquad \Delta\lambda_{\mathrm{Stokes}} \approx 113\ \text{nm}}$$

### Q23. L'iodure de propidium, marqueur de l'intégrité membranaire

**Structure et propriétés.** Le document 9 montre un noyau **phénanthridinium** plan et aromatique, portant deux amines primaires et un substituant phényle, relié par une chaîne propylène à un **ammonium quaternaire triéthylé**. Les charges sont décisives :

- l'azote du cycle phénanthridinium porte une **charge positive permanente** ;
- l'ammonium quaternaire porte une **seconde charge positive permanente**, non titrable, indépendante du pH : un azote quaternaire n'a pas de doublet libre à protoner ou à déprotoner.

L'iodure de propidium est donc un **dication permanent**, associé à deux iodures ; molécule **très polaire, hydrosoluble**, de masse molaire élevée (≈ 668 g·mol⁻¹).

**Cellule à membrane intacte : exclusion.** Le cœur de la bicouche lipidique est un milieu **hydrophobe** de très faible constante diélectrique : le coefficient de partage d'une espèce doublement chargée y est extrêmement défavorable, la traversée coûterait une énergie de désolvatation considérable, et aucun transporteur bactérien ne prend cette molécule en charge. L'iodure de propidium reste donc **intégralement à l'extérieur** d'une cellule à membrane intacte. Or il est **très peu fluorescent à l'état libre** en solution : une cellule vivante **n'émet aucun signal rouge**.

**Cellule à membrane lésée : entrée et exaltation.** Si l'intégrité membranaire est compromise — pores, perte de la barrière de perméabilité, lyse —, le marqueur diffuse dans le cytoplasme et **s'intercale** entre les paires de bases empilées de l'ADN double brin (et des régions structurées de l'ARN), ce que permet la **planéité** du noyau phénanthridinium, tandis que ses charges positives sont attirées par les phosphates du squelette. Une fois intercalé, le fluorophore est **rigidifié et soustrait au solvant** : les voies de désexcitation non radiative sont bloquées et sa fluorescence est **exaltée d'un facteur 20 à 30**. La cellule devient **intensément rouge** ($\lambda_{\mathrm{exc}} = 535$ nm, $\lambda_{\mathrm{em}} = 617$ nm d'après le document 9).

| | Membrane intacte | Membrane lésée |
|---|---|---|
| Entrée du marqueur | non (dication exclu) | oui |
| Intercalation à l'ADN | — | oui |
| Fluorescence rouge (617 nm) | **nulle** | **intense** |
| Interprétation | cellule vivante | cellule morte ou perméabilisée |

**Exploitation.** L'iodure de propidium est un **marqueur d'exclusion** : la fluorescence rouge rapporte directement, en temps réel et à l'échelle de la cellule unique, la **perte d'intégrité de la membrane plasmique**. Son ajout **avant** l'infection (document 10 : 10 µM dès le début) permet de dater précisément le moment où chaque cellule perd son étanchéité, sans manipuler l'échantillon en cours d'expérience. Le critère rapporté est bien l'**intégrité membranaire** : une cellule métaboliquement morte mais à membrane étanche resterait non marquée.

$$\boxed{\text{Dication permanent, imperméant : il n'entre que si la membrane est lésée, s'intercale à l'ADN et devient alors fortement fluorescent (rouge, 617 nm).}}$$

### 4. Étude de l'immunité bactérienne

### Q24. Survie des deux souches en présence de Φ80α-virGFP (document 10a)

Les deux souches ne diffèrent que par un gène : « *Ssc*-CBASS » possède l'opéron complet (cyclase **et** effecteur CAP15), « *Ssc*-CdnE03 » ne possède que la cyclase. La comparaison est donc une expérience de **perte de fonction** ciblée sur l'effecteur : tout écart entre les deux courbes lui est imputable.

| Temps | *Ssc*-CdnE03 (cyclase seule) | *Ssc*-CBASS (cyclase + CAP15) | Écart |
|---|---|---|---|
| 0 h | 100 % | 100 % | 0 |
| 2 h | ≈ 97 % | 100 % | ≈ 3 points |
| 6 h | ≈ 50 % | ≈ 98 % | ≈ 48 points |
| 12 h | ≈ 5 % | ≈ 92 % | ≈ 87 points |

- **Souche *Ssc*-CdnE03** : survie proche de 100 % jusqu'à 2 h, puis chute régulière, approximativement linéaire entre 2 et 12 h (≈ 9 points de pourcentage par heure), avec un temps de demi-survie d'environ 6 h. La population est **presque intégralement détruite** en douze heures.
- **Souche *Ssc*-CBASS** : survie **quasi constante**, la perte totale restant inférieure à 10 points en douze heures. La population est **protégée**.

**Conclusion.** À 12 h, la souche complète survit **18 fois mieux** que la souche à cyclase seule. Il s'ensuit que :

1. la **cyclase seule ne confère aucune protection** : la souche *Ssc*-CdnE03 se comporte comme une souche sensible ;
2. l'**opéron CBASS complet confère une immunité quasi totale** à l'échelle de la population ;
3. par différence, l'**effecteur CAP15 est nécessaire** à cette immunité. La production de nucléotides cycliques n'est donc pas une fin en soi : c'est un **signal**, sans effet si aucun effecteur ne le lit et ne l'exécute. La cyclase détecte, l'effecteur agit.

**Précision indispensable.** La protection mesurée ici est **populationnelle** : le document 10a donne un pourcentage de survie *de la population*, et non le devenir d'une cellule infectée. Une survie de 92 % est parfaitement compatible avec la mort des quelques pour cent de cellules effectivement infectées.

$$\boxed{\text{Cyclase seule : } 100 \rightarrow 5\ \%\text{ en 12 h. Opéron complet : } \ge 92\ \%. \text{ CAP15 est indispensable à la protection.}}$$

### Q25. Analyse des résultats de fluorescence (document 10b) et évolution de l'iodure de propidium

**Grille de lecture.** Chaque image superpose le contraste de phase (cellules), le canal **vert** (GFP portée par le phage, donc **marqueur d'infection productive**) et le canal **rouge** (iodure de propidium, donc **marqueur de perte d'intégrité membranaire**). Une cellule orangée porte les deux signaux.

| Souche | 2 h | 6 h | 12 h |
|---|---|---|---|
| *Ssc*-CBASS (cyclase + CAP15) | Amas de cellules **vertes** intenses, aucun signal rouge | Cellules individualisées, vert en baisse, **rouge apparaissant** (teintes orangées) | Cellules **rouges**, vert quasi éteint ; **cellules toujours présentes et individualisées** |
| *Ssc*-CdnE03 (cyclase seule) | Cellules **vertes**, aucun signal rouge | Cellules **vertes**, signal maintenu, pas de rouge notable | **Plus de cellules** : champ vide, mention « lyse des bactéries » |

**Souche *Ssc*-CdnE03.** L'infection est productive : la GFP, exprimée à partir du génome viral, s'accumule et le signal vert persiste de 2 à 6 h ; l'iodure de propidium n'entre pas tant que la membrane est intacte. À 12 h, il n'y a plus de cellules : elles ont été **lysées** en fin de cycle lytique, libérant leur contenu — d'où la disparition simultanée des deux signaux. C'est le scénario d'une infection non contrariée, cohérent avec les 5 % de survie du document 10a.

**Souche *Ssc*-CBASS, et discussion de l'iodure de propidium.**

- **À 2 h** : vert intense, rouge **nul**. Le phage a donc bien infecté ces cellules et exprimé son génome : le CBASS ne bloque **ni** l'entrée du phage **ni** l'expression précoce. La membrane est encore parfaitement étanche : les cellules sont **vivantes et infectées**.
- **À 6 h** : l'iodure de propidium commence à pénétrer, les cellules virent à l'orangé, le signal vert plafonne puis décline. La membrane a donc **perdu son étanchéité** entre 2 et 6 h, et la production de nouvelles protéines virales s'interrompt : le cycle viral est **avorté**.
- **À 12 h** : toutes les cellules observées sont franchement rouges et la GFP a disparu. **Mais les cellules sont toujours là**, individualisées et morphologiquement reconnaissables : **il n'y a pas eu de lyse**.

**Ce que démontre l'évolution de l'iodure de propidium.** Dans la souche protégée, **la membrane plasmique des cellules infectées est activement perméabilisée**, et cette perméabilisation n'est pas la conséquence de la lyse virale, puisque précisément les cellules ne sont pas lysées et que la souche dépourvue de CAP15 ne devient jamais rouge avant de disparaître. La perméabilisation est donc l'œuvre de la bactérie elle-même, par l'effecteur **CAP15**, dont l'énoncé indique qu'il « perturbe l'intégrité de la membrane plasmique ».

**Cohérence avec le document 10a.** Il n'y a pas de contradiction entre « toutes les cellules observées deviennent rouges » et « 92 % de la population survit » : le document 10b montre **les cellules infectées**, celles qui ont capté un phage et exprimé la GFP, tandis que le document 10a mesure **l'ensemble de la population**, dont l'immense majorité n'a jamais été infectée. **Le CBASS sacrifie la cellule infectée et préserve la population.**

La disparition du signal vert à 12 h doit enfin être commentée prudemment : arrêt de la synthèse, photoblanchiment ou fuite de la protéine par une membrane devenue poreuse — ce seul document ne permet pas de trancher.

$$\boxed{\textit{Ssc}\text{-CBASS : GFP (2 h), entrée de l'iodure de propidium (6 h), mort sans lyse (12 h). } \textit{Ssc}\text{-CdnE03 : GFP croissante puis lyse.}}$$

### Q26. Hypothèse sur le mode d'action du système CBASS et de CAP15

**Hypothèse.** Le système CBASS est un système d'**infection avortée** (*abortive infection*) fonctionnant par **suicide altruiste** de la cellule infectée. Il s'organise en trois modules.

**1. Détection (senseur).** Le bactériophage infecte la cellule et exprime son génome (GFP visible dès 2 h, Q25). Parmi ces produits figure un **ARN viral spécifique** d'environ 700 nt (Q18), absent d'une bactérie non infectée (Q17). Cet ARN se fixe dans la **poche basique K9/K13/R83** de la cyclase (Q13, Q14), la reconnaissance combinant l'attraction électrostatique du squelette phosphate et la complémentarité de forme avec la structure repliée de l'ARN.

**2. Signalisation (amplification).** La fixation de l'ARN provoque un **changement de conformation allostérique** qui active le site catalytique. La cyclase, nucléotidyl transférase cyclique, polymérise alors des nucléotides en **oligonucléotides cycliques**, qui sont des **seconds messagers** : une seule molécule d'ARN activatrice permet la production catalytique de nombreuses molécules de signal. Cette **amplification** est ce qui permet à la réponse de devancer le cycle viral.

**3. Exécution (effecteur).** Les oligonucléotides cycliques se lient à **CAP15** et l'activent — vraisemblablement par **oligomérisation** et insertion dans la membrane, à la manière des effecteurs formeurs de pores ; cette dernière étape est une hypothèse, l'énoncé disant seulement que CAP15 perturbe l'intégrité membranaire. Il en résulte une **perte d'intégrité de la membrane plasmique**, attestée par l'entrée de l'iodure de propidium dès 6 h (Q25), et par conséquent :

- la **dissipation de la force proton-motrice** et l'effondrement du potentiel de membrane, donc l'arrêt de la synthèse d'ATP ;
- la fuite des métabolites et des ions, donc l'**arrêt du métabolisme** et de toute biosynthèse ;
- donc l'**arrêt de la réplication et de la morphogenèse virales** avant l'assemblage de virions matures.

**4. Conséquence populationnelle.** La cellule infectée meurt, mais **sans lyse** et **sans descendance virale** (Q25). Le phage est pris dans un cul-de-sac : il ne peut se propager aux cellules voisines. À l'échelle de la population, la perte de quelques cellules infectées préserve les ≈ 92 % restants (Q24). Le mécanisme est **altruiste**, sélectionné au niveau du clone et non de l'individu.

**Prédictions testables.**

- Un mutant catalytique de la cyclase doit se comporter comme la souche dépourvue de CAP15 : pas d'entrée d'iodure de propidium, lyse à 12 h.
- L'ajout exogène du nucléotide cyclique purifié à une souche exprimant CAP15 seule, **sans phage**, doit suffire à perméabiliser les cellules.
- Le titre en phages produit par la souche *Ssc*-CBASS doit être effondré par rapport à celui de la souche *Ssc*-CdnE03 — mesurable en PFU par la technique des spots (Q3–Q4).

$$\boxed{\text{ARN viral} \rightarrow \text{cyclase} \rightarrow \text{nucléotides cycliques} \rightarrow \text{CAP15} \rightarrow \text{perméabilisation membranaire} \rightarrow \text{mort de la cellule infectée sans libération virale.}}$$

### Q27. Composition d'un témoin expérimental et objectifs

**Témoin retenu : souche sauvage RN4220, dépourvue de tout système CBASS, infectée par Φ80α-virGFP dans les mêmes conditions.**

**Composition et conduite.** Chambre du même dispositif à faible volume ; bactéries *S. aureus* RN4220 **sauvages** piégées dans la chambre ; milieu BHI + 5 mM CaCl₂ + 10 µM d'iodure de propidium ; incubation 1 h ; ajout de Φ80α-virGFP à la même MOI ; incubation 60 min ; ajout de BHI stérile ; incubation 1 h ; acquisition aux mêmes temps (2, 6 et 12 h), avec les **mêmes réglages** d'excitation, d'exposition et de gain.

**Résultat attendu.** Infection productive : GFP intense dès 2 h, croissante à 6 h, puis lyse complète à 12 h, sans entrée notable d'iodure de propidium avant la lyse — comportement superposable à celui de la souche *Ssc*-CdnE03.

**Objectifs.**

1. Établir la **référence de sensibilité** : prouver que, dans ce dispositif et à cette MOI, le phage est bien infectieux et létal. Sans ce témoin, une absence de mortalité chez la souche CBASS pourrait tout aussi bien signifier que la préparation de phages était inactive.
2. Vérifier que le comportement de la souche *Ssc*-CdnE03 n'est **pas dû à l'insertion chromosomique elle-même** (effet de position, charge métabolique) mais bien à l'absence de l'effecteur.
3. Fournir la **cinétique de référence** d'une infection non contrariée, à laquelle comparer le décrochage observé chez *Ssc*-CBASS.

**Autres témoins nécessaires.**

| Témoin | Objectif |
|---|---|
| Chaque souche **sans phage**, avec iodure de propidium | Vérifier que le marqueur n'entre pas spontanément (viabilité, absence de toxicité) et mesurer l'autofluorescence de fond du canal vert |
| Souche *Ssc*-CBASS + phage **sans GFP** (Φ80α-vir) | Vérifier que le signal vert provient bien de la GFP virale et non d'une autofluorescence induite par l'infection |
| Cellules tuées à l'éthanol ou à la chaleur, avec iodure de propidium | **Témoin positif** du marquage : valider que le marqueur entre et fluoresce lorsque la membrane est détruite, donc qu'une absence de rouge est une information et non une panne |
| Souche exprimant la GFP de façon constitutive | Étalonner l'intensité du canal vert et mesurer le photoblanchiment au cours des 12 h |

*Remarque.* La souche *Ssc*-CdnE03 n'est pas un témoin : elle est l'une des deux conditions expérimentales comparées.

### 5. Conclusion

### Q28. Logigramme de la cascade d'évènements moléculaires

Les sept termes imposés — **bactériophage**, **infection**, **cyclase Ssc-CdnE03**, **nucléotides cycliques**, **CAP15**, **membrane plasmique**, **multiplication virale** — figurent tous dans le logigramme ci-dessous, en capitales.

![Figure 4 — Logigramme de la cascade CBASS : un ARN viral active la cyclase, les nucléotides cycliques activent CAP15, la membrane plasmique est perméabilisée et la multiplication virale s'arrête](figures/q28-logigramme-cbass.svg)

$$\boxed{\textbf{bactériophage} \rightarrow \textbf{infection} \rightarrow \text{ARN viral} \rightarrow \textbf{cyclase} \rightarrow \textbf{nucléotides cycliques} \rightarrow \textbf{CAP15} \rightarrow \textbf{membrane plasmique} \rightarrow \text{arrêt de la } \textbf{multiplication virale}}$$

### Q29. Lien avec la mort cellulaire par apoptose chez l'Homme

**1. Une même logique fonctionnelle.** L'apoptose est une **mort cellulaire programmée**, génétiquement encodée, déclenchée par la cellule elle-même lorsqu'elle détecte une anomalie irréparable — lésion de l'ADN, stress du réticulum, et notamment **infection virale**. Comme le CBASS, c'est un **sacrifice individuel au bénéfice de l'ensemble** : une cellule infectée qui s'autodétruit avant la fin du cycle viral n'engendre pas de descendance virale et protège l'organisme entier, exactement comme la bactérie *Ssc*-CBASS protège sa population. Dans les deux cas, le principe est celui de l'**infection avortée**.

**2. Une même architecture en trois modules.**

| Module | CBASS bactérien | Immunité innée et apoptose chez l'Homme |
|---|---|---|
| Détection du non-soi | Cyclase Ssc-CdnE03 liant un **ARN viral** | **cGAS** liant l'ADN cytosolique ; RIG-I et MDA5 liant l'ARN viral ; récepteurs de type Toll |
| Second messager | **Oligonucléotides cycliques** | **2′3′-cGAMP** produit par cGAS, reconnu par **STING** |
| Exécution | **CAP15**, qui perméabilise la membrane plasmique | **BAX/BAK**, qui perméabilisent la membrane mitochondriale externe (puis cytochrome *c* et caspases) ; **gasdermines**, qui perforent la membrane plasmique (pyroptose) |

**3. Une parenté évolutive, et pas seulement une analogie.** Les cyclases bactériennes de ce type appartiennent à la famille des **CD-NTases**, dont la cGAS humaine est un membre : même repliement, même chimie, même type de produit. Des domaines apparentés à **STING** et des **gasdermines** bactériennes ont été décrits dans des opérons de défense procaryotes. L'interprétation communément admise est que le système cGAS–STING des animaux **descend** de systèmes de défense antiphagiques procaryotes, ultérieurement complexifiés — ce que signale d'ailleurs le titre de l'article source cité dans la bibliographie du sujet, *Bacterial cGAS senses a viral RNA to initiate immunity*.

**4. Les limites du parallèle.**

- L'apoptose *stricto sensu* est une mort **non inflammatoire** qui **préserve l'intégrité de la membrane plasmique** jusqu'aux stades tardifs : la cellule apoptotique se fragmente en corps apoptotiques phagocytés et reste d'abord non marquée par l'iodure de propidium. Or, ici, l'entrée précoce du marqueur signale justement une perte d'étanchéité : le phénotype observé s'apparente davantage à la **pyroptose** ou à la **nécroptose** qu'à l'apoptose canonique.
- L'apoptose repose sur une cascade de **caspases**, dont aucun équivalent n'apparaît dans le CBASS étudié.
- Une bactérie est unicellulaire : le bénéficiaire du sacrifice n'est pas un organisme mais un **clone**, ce qui déplace la question évolutive vers la sélection de parentèle.
- Enfin, l'apoptose intervient aussi dans le **développement** (morphogenèse, sélection des lymphocytes), fonction sans équivalent bactérien.

On évitera donc d'écrire que les bactéries « font de l'apoptose » : elles réalisent une mort cellulaire programmée, ce qui n'est pas la même chose.

$$\boxed{\text{Même logique de suicide altruiste face à l'infection, même architecture senseur} \rightarrow \text{nucléotide cyclique} \rightarrow \text{effecteur perméabilisant ; le couple cGAS–STING humain en est l'héritier évolutif.}}$$
