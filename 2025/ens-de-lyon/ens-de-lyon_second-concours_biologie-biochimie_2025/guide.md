# ENS de Lyon — Second concours · Biologie-biochimie 2025 · Corrigé partiel guidé

*Corrigé rédigé par IA, non officiel.*

**Rédaction** · modèle exact non renseigné (famille GPT-6) · effort non renseigné · vitesse non renseignée

**Révision (tour 1)** · GPT-6.2 Astra Ultra · vitesse non renseignée

**Couverture de l’épreuve (32 questions).** Les Q7, 18, 23, 31 et 32 sont traitées intégralement. Les Q1, 3, 8, 9, 21, 26 et 30 abordent uniquement des principes généraux de biochimie et de lecture des mesures. Les 20 autres questions et l’interprétation des expériences sur la virulence de Listeria monocytogenes sont hors périmètre.

## Présentation du sujet

Le sujet officiel porte sur le contrôle de l’expression de facteurs de virulence chez Listeria monocytogenes. Cette sélection développe les questions autonomes sur les molécules et la lecture des méthodes de biochimie, ainsi que des exemples de régulation chez les eucaryotes.

## I — Messages, acides aminés et détection de complexes

Le premier cadre de lecture d’un message, la charge d’une chaîne latérale et la mobilité d’un complexe sont trois propriétés différentes.

### Question 1 — éléments de réponse

> [!INDICATION]
> Compter les cadres de lecture distincts sur la figure 1 et se demander comment le ribosome cytosolique eucaryote choisit son codon de départ.

> [!INDICATION]
> Le qualificatif bicistronique s’applique à l’ARNm portant deux cadres distincts.

#### Solution

Un ARNm qui contient deux cadres de lecture codants distincts est **bicistronique**. Dans le cytosol eucaryote, l’initiation canonique dépend de la coiffe $5^{\prime}$. La petite sous-unité et les facteurs associés parcourent le messager vers son extrémité $3^{\prime}$ jusqu’à un codon de départ en contexte favorable. À la fin de la traduction, le ribosome se dissocie généralement. La présence d’un second cadre ne suffit donc pas à assurer sa traduction efficace. Ce raisonnement porte sur un messager générique.

![Figure 1 — Organisation générique de deux cadres successifs sur un même ARNm. Dans le cytosol eucaryote, le balayage favorise normalement le premier AUG approprié.](figures/q01-lecture-arn-bicistronique.svg)

### Question 3 — éléments de réponse

> [!INDICATION]
> Distinguer la mesure du bruit de fond et la vérification du bon fonctionnement du détecteur.

#### Solution

Pour interpréter une perte de signal avec un colorant fluorescent, il faut une mesure de référence. Un échantillon sans colorant renseigne sur l’autofluorescence et un étalon fluorescent permet de vérifier que le dispositif de lecture répond. Un signal au niveau du blanc signifie que l’expérience ne distingue pas la fluorescence de l’échantillon du bruit de fond. Ce principe de lecture est traité ici indépendamment des souches du sujet.

### Question 7

> [!INDICATION]
> Vérifier la valence du carbone α et la protonation usuelle de l’amine et du carboxyle vers pH 7.

> [!INDICATION]
> Un carboxylate peut être écrit sous deux formes mésomères équivalentes.

#### Solution

La **glycine** fournit l’exemple le plus simple. Sa formule moléculaire est $\mathrm{C_2H_5NO_2}$ et sa formule usuelle en solution aqueuse proche de la neutralité est $\mathrm{{}^+H_3N{-}CH_2{-}COO^-}$. L’ammonium porte $+1$ et le carboxylate $-1$, d’où une charge nette nulle. Le carbone α porte le groupe ammonium, le carboxylate et deux H. Il forme quatre liaisons et n’est pas chiral. La glycine reste globalement neutre sous cette forme malgré ses deux groupes chargés. En milieu très acide, le carboxylate se protone et la charge nette devient $+1$. En milieu très basique, l’ammonium perd un proton et la charge nette devient $-1$. La chaîne latérale de la glycine est un hydrogène.

![Figure 2 — La glycine, sous sa forme zwitterionique vers pH 7, porte deux charges opposées et deux H sur le carbone α.](figures/q07-glycine-zwitterion.svg)

### Question 8 — éléments de réponse

> [!INDICATION]
> Distinguer charge nette, polarité et capacité à former des liaisons hydrogène.

#### Solution

À pH voisin de 7, la chaîne latérale de la **lysine** se termine généralement par un ammonium positif. L’amide de la **glutamine** et l’alcool de la **sérine** sont polaires et globalement neutres. La **glycine**, dont la chaîne latérale est H, est peu encombrée et permet une grande liberté de conformation locale. La charge intervient dans les interactions électrostatiques, tandis qu’un groupe polaire neutre peut encore former des liaisons hydrogène. Ces propriétés seules ne prédisent pas l’effet mesuré d’une substitution sur une protéine. Cette réponse se limite à la comparaison chimique des quatre résidus.

### Question 9 — éléments de réponse

> [!INDICATION]
> Dessiner un puits de départ et placer sur son axe de migration une sonde libre puis une sonde dont la mobilité a diminué.

#### Solution

Dans un exemple générique de gel natif, deux objets peuvent porter le même marqueur tout en migrant différemment. La sonde libre donne une bande de référence. Une sonde retenue dans un complexe peut former une bande plus proche du puits. La détection ne révèle que les espèces qui portent le marqueur. Un décalage seul ne donne ni l’identité ni la masse de tous les constituants du complexe.

![Figure 3 — Gel natif schématique. Une sonde libre indique la position de référence et un complexe se déplace moins loin.](figures/q09-retard-migration.svg)

## II — Mesurer un ARN ou une protéine

Le choix de la molécule détectée détermine la méthode et le type de témoin pertinent.

### Question 18

> [!INDICATION]
> Distinguer la séparation préalable des protéines et la reconnaissance spécifique qui rend l’une d’elles visible.

> [!INDICATION]
> La présence d’une bande ne donne pas directement une activité enzymatique.

#### Solution

Le **Western blot** ou immunotransfert détecte une protéine dans un mélange. Une électrophorèse, usuellement en présence de SDS, sépare les protéines principalement selon leur masse apparente. Elles sont ensuite transférées sur une membrane. Après blocage des fixations non spécifiques, un anticorps primaire reconnaît la protéine recherchée et un système de révélation, souvent un anticorps secondaire marqué, visualise la bande. Le marqueur de masse renseigne sur la taille apparente. Un témoin de charge ou une coloration des protéines totales permet de normaliser les comparaisons entre pistes. L’intensité n’est proportionnelle à la quantité que dans la gamme de réponse non saturée.

### Question 21 — éléments de réponse

> [!INDICATION]
> Le nom du transfert indique quelle famille de molécules est détectée. Penser également à la distinction entre taille et abondance.

> [!INDICATION]
> Une bande renseigne sur un ARN si la sonde nucléique permet de le reconnaître.

#### Solution

Dans un **Northern blot**, on sépare les ARN selon leur longueur, on les transfère sur une membrane et on révèle ceux qui s’hybrident à une sonde complémentaire. Un marqueur de longueur sert de référence. Une bande plus intense ne traduit une abondance plus élevée que si le chargement, l’intégrité de l’ARN et la gamme de détection sont comparables. Une autre approche de mesure d’abondance est la RT-qPCR, qui associe transcription inverse des ARN et amplification quantitative. L’application aux transcrits du sujet reste hors périmètre.

![Figure 4 — Le Western blot reconnaît une protéine avec un anticorps ; le Northern blot reconnaît un ARN par complémentarité de séquence.](figures/q21-transferts-proteines-et-arn.svg)

### Question 23

> [!INDICATION]
> L’imidazole des histidines coordonne des ions métalliques. Il peut aussi être reconnu dans une étiquette par un anticorps.

#### Solution

Une étiquette polyhistidine sert à la **purification par affinité sur métal immobilisé**. Ses groupes imidazole coordonnent, par exemple, des ions nickel ou cobalt fixés à une matrice. La protéine étiquetée peut être séparée de nombreuses autres protéines par cette affinité. Un anticorps anti-His peut aussi détecter une protéine étiquetée indépendamment de sa fonction. L’étiquette est un outil analytique ; sa présence ne démontre pas qu’une protéine a conservé son activité.

### Question 26 — éléments de réponse

> [!INDICATION]
> Comparer la grandeur lue sur un gel natif à celle que fournit un gel dénaturant.

#### Solution

Deux ARN de même longueur peuvent avoir des mobilités différentes sur un **gel natif**, parce que leur conformation et leur compacité influencent leur passage dans les mailles du gel. Un déplacement par rapport à une échelle étalonnée en longueur donne alors une **taille apparente**. En conditions dénaturantes, les structures secondaires se défont et la migration devient surtout sensible à la longueur. Si la différence disparaît en conditions dénaturantes, un changement de conformation est une explication compatible. Cet argument général ne permet pas de déduire seul la structure tridimensionnelle.

## III — Expression des gènes chez les eucaryotes

La coiffe, la chromatine et la maturation nucléaire des messagers fournissent des niveaux de régulation complémentaires.

### Question 30 — éléments de réponse

> [!INDICATION]
> Comparer le recrutement du ribosome dans le cytosol humain et sur un messager bactérien canonique.

#### Solution

Chez l’humain, la reconnaissance canonique d’un ARNm cytosolique passe par la coiffe et les facteurs d’initiation, puis par le balayage jusqu’à un AUG en contexte favorable. Le dispositif bactérien d’appariement entre une séquence Shine–Dalgarno et l’ARNr de la petite sous-unité n’est pas celui des ribosomes cytosoliques humains. Cette différence empêche de transposer à l’identique une régulation qui dépend de cet appariement. Des structures secondaires peuvent néanmoins moduler la traduction humaine, par exemple en influençant le balayage ou en recrutant une protéine régulatrice.

### Question 31

> [!INDICATION]
> Choisir un exemple où la structure repliée de l’ARN est directement reconnue par un partenaire régulateur.

#### Solution

Dans les cellules animales, l’ARNm de la **ferritine** porte en $5'$ une tige-boucle appelée IRE, reconnue par des protéines régulatrices du fer, les IRP. Lorsque le fer disponible est faible, la liaison d’une IRP à l’IRE gêne l’initiation de traduction et limite la synthèse de cette protéine de stockage. Quand le fer est abondant, la fixation des IRP diminue et la synthèse de ferritine augmente. La même réponse au fer peut agir sur une autre étape : quand le fer manque, des IRP liées aux IRE en $3^{\prime}$ de l’ARNm du récepteur de la transferrine contribuent à stabiliser ce messager. La cellule peut alors accroître sa capacité à capter le fer, tout en réduisant son stockage dans la ferritine. La position d’un motif replié influe donc sur la nature de la réponse.

![Figure 5 — Exemple eucaryote indépendant. La fixation d’une IRP sur une structure IRE en 5′ de l’ARNm diminue la synthèse de ferritine.](figures/q31-regulation-ferritine.svg)

### Question 32

> [!INDICATION]
> Chercher des mécanismes associés à la chromatine nucléaire, à l’épissage et à la séparation du noyau et du cytoplasme.

> [!INDICATION]
> Donner au moins un effet concret de chaque mécanisme sur la quantité ou la nature du produit.

#### Solution

Chez les eucaryotes, plusieurs mécanismes découlent de l’organisation nucléaire du génome et de la maturation des pré-ARNm.

| Mécanisme | Effet possible sur l’expression |
|---|---|
| Remodelage des nucléosomes et modifications des histones | Changent l’accessibilité d’un promoteur ou d’un amplificateur dans la chromatine nucléaire |
| Épissage alternatif des pré-ARNm par le spliceosome | Produit des isoformes différentes à partir d’un même gène |
| Rétention, contrôle qualité et export des ARNm par les pores nucléaires | Conditionnent l’accès des messagers aux ribosomes cytosoliques |
| Inactivation du chromosome X chez les mammifères placentaires | Réduit à l’échelle d’un chromosome l’expression de nombreux gènes |

Par exemple, deux pré-ARNm transcrits du même gène peuvent être épissés différemment selon le tissu. Un exon codant facultatif peut alors être présent dans une protéine et absent d’une autre, bien que les deux cellules possèdent la même séquence génomique. La méthylation de l’ADN, prise isolément, serait un exemple moins discriminant, car les bactéries possèdent aussi des systèmes de méthylation.

## Bilan

Ces questions mobilisent plusieurs niveaux de preuve. Une mobilité sur gel natif dépend de la conformation, une sonde d’hybridation détecte une séquence et un anticorps reconnaît un antigène. Le repliement des ARN intervient aussi dans la régulation physiologique des cellules animales, comme l’illustre la ferritine.
