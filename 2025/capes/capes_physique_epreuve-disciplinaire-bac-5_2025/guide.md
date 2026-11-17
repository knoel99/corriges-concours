# CAPES Physique — Épreuve disciplinaire (bac+5) 2025 · Corrigé guidé

*Corrigé rédigé par IA, non officiel. Signalez toute erreur.*

## Présentation du sujet

L'épreuve disciplinaire du CAPES de physique-chimie dure **5 heures** (coefficient 2, coefficient 4 pour les troisièmes concours) et comporte **deux copies séparées** : une composition de physique (Partie A) et une composition de chimie (Partie B). Ce corrigé porte sur la **Partie A, « Physique dans l'automobile »** : **40 questions** réparties en cinq sous-parties indépendantes et progressives — le moteur Diesel (Q1-Q8), le freinage par courants de Foucault (Q9-Q19), le capteur de choc et l'airbag (Q20-Q29), le détecteur de pluie (Q30-Q35), l'allumage automatique des feux (Q36-Q40).

Notions du programme mobilisées : thermodynamique du gaz parfait (lois de Laplace, premier principe, inégalité de Clausius), électromagnétisme (induction, loi de Lenz-Faraday, force de Laplace), mécanique newtonienne (référentiels galiléen et non galiléen, oscillateur amorti), optique géométrique (loi de Snell-Descartes, réflexion totale), électrocinétique (loi des mailles, loi d'Ohm, photodiode) et un peu de programmation Python.

Session 2025 (rapport du jury de la même épreuve) : moyenne 8,95/20, écart-type 3,08, notes de 1,54 à 17,36, barre d'admissibilité 7,35/20. Le rapport insiste : « Les expressions littérales sont à privilégier » et « les lois de la physique doivent être énoncées lorsqu'elles sont utilisées » (p. 8) ; il recommande une bonne lisibilité, les numéros de questions ressortis et des réponses clairement explicitées.

**Questions à ne pas manquer** : les sous-parties étant indépendantes, on peut les traiter dans l'ordre de son choix. D'après le rapport, les questions les moins bien réussies (donc discriminantes) sont Q7 (inégalité de Clausius), Q19, Q24, Q28-Q29, Q34, Q39-Q40 (« très rarement traitée ») ; les questions sûres sont Q1, Q9, Q12, Q15-Q18, Q23, Q26, Q31-Q33, Q35-Q36.

**Gestion du temps** : comptez environ 50 min pour la partie I (calculs guidés), 1 h 10 pour la partie II (les deux sous-parties), 1 h 10 pour la partie III, et gardez 20-30 min de relecture (conversions d'unités, kelvin, chiffres significatifs, sens des vecteurs).

## I. Le moteur Diesel

Thermodynamique du gaz parfait : on décrit le cycle Diesel modélisé, puis on borne son rendement par le rendement de Carnot via l'inégalité de Clausius. Les questions sont progressives et l'énoncé donne plusieurs résultats intermédiaires.

### Q1

> [!INDICATION]
> Exploiter le caractère isochore de D→A et le caractère isobare de B→C.

> [!INDICATION]
> Écrire la loi d'état du gaz parfait en B et en C, sachant que P_B = P_C et la quantité de matière est la même.

#### Solution

D→A est isochore :

$$
\boxed{V_A=V_D}.
$$

B→C est isobare :

$$
\boxed{P_B=P_C}.
$$

Loi d'état du gaz parfait $PV=nRT$ écrite en B et en C (même quantité de matière, $P_B=P_C$) :

$$
\frac{P_BV_B}{T_B}=\frac{P_CV_C}{T_C},
$$

d'où

$$
\boxed{\frac{V_B}{T_B}=\frac{V_C}{T_C}}.
$$

### Q2

> [!INDICATION]
> Deux définitions distinctes : réversibilité (succession d'états d'équilibre, pas d'entropie créée) et adiabaticité (aucun transfert thermique).

> [!INDICATION]
> Un système non isolé peut-il être le siège d'une transformation adiabatique ?

#### Solution

Une transformation **réversible** est une succession continue d'états d'équilibre internes ; le système peut repasser par les mêmes états en sens inverse en inversant infinitésimalement les contraintes extérieures ; aucune entropie n'est créée ($S_{\text{créée}}=0$).

Une transformation **adiabatique** est une transformation au cours de laquelle le système n'échange aucune chaleur avec l'extérieur ($Q=0$ à chaque instant). Un système **non isolé** peut subir une transformation adiabatique (parois calorifugées) : adiabatique ne signifie pas isolé, et ne s'oppose pas à isotherme.

### Q3

> [!INDICATION]
> C→D est adiabatique réversible : penser à la loi de Laplace reliant T et V.

> [!INDICATION]
> Écrire explicitement les hypothèses (gaz parfait, transformation isentropique), puis utiliser V_D = V_A et V_C = V_A/b.

#### Solution

Hypothèses : gaz parfait, $\gamma$ constant, transformation **isentropique** (adiabatique et réversible). La loi de Laplace s'écrit $T\,V^{\gamma-1}=\text{cte}$, donc entre C et D :

$$
T_C\,V_C^{\gamma-1}=T_D\,V_D^{\gamma-1}.
$$

Or $V_D=V_A$ (Q1) et $V_C=V_A/b$, donc

$$
T_D=T_C\left(\frac{V_C}{V_A}\right)^{\gamma-1}=\boxed{T_C\left(\frac{1}{b}\right)^{\gamma-1}}.
$$

Par analogie (A→B isentropique), on admet $T_A=T_C\,b\left(\dfrac{1}{a}\right)^{\gamma}$.

> [!JURY]
> Le rapport 2025 rappelle les hypothèses : « un gaz parfait subissant une transformation isentropique, c’est-à-dire adiabatique et réversible » (p. 9).

### Q4

> [!INDICATION]
> Placer A (volume maximal, pression minimale), puis B, C et D en utilisant le caractère des quatre transformations.

> [!INDICATION]
> Le travail reçu sur un cycle vaut W = −∮P dV : relier son signe au sens de parcours et à l'aire du cycle.

#### Solution

Positions sur le diagramme de Clapeyron $(P,V)$ :

```text
P ↑   B━━━━━━━C
  │  ╱         ╲
  │ ╱           ╲
  │╱             D
  │              │
  └──────────────┴──→ V
                 A
```

- A : volume maximal $V_A$, pression minimale $P_A$ (en bas à droite) ;
- B : volume minimal $V_B$, pression maximale $P_B$ (en haut à gauche), atteint par la compression adiabatique A→B ;
- C : sur l'isobare de B, à droite de B ($V_C$, $P_C=P_B$) ;
- D : sur la verticale de A, au-dessus de A ($V_D=V_A$, $P_D>P_A$).

Le cycle est parcouru dans le **sens horaire**. Le travail reçu par le gaz sur un cycle vaut $W=-\oint P\,\mathrm{d}V$, égal à **moins l'aire** du cycle (parcouru horaire) :

$$
W=-\mathcal{A}<0.
$$

Le gaz fournit du travail au milieu extérieur : le cycle est **moteur**.

> [!JURY]
> « Le sens horaire du parcours du cycle n’est pas toujours bien mis en relation avec le caractère moteur du cycle » (rapport 2025, p. 9) ; penser aussi à « rappeler la définition du travail afin de faire le lien avec l’aire du cycle ».

### Q5

> [!INDICATION]
> Premier principe pour un système fermé entre deux états d'équilibre : une relation entre ΔU, Q et W ; définir chaque terme (pas de « variation de chaleur »).

#### Solution

Premier principe de la thermodynamique pour un système fermé, entre deux états d'équilibre :

$$
\boxed{\Delta U=Q+W},
$$

où $\Delta U$ est la variation d'énergie interne (fonction d'état), $Q$ le transfert thermique reçu et $W$ le travail reçu (ici le travail des forces de pression, l'énergie cinétique macroscopique étant nulle). $Q$ et $W$ sont des quantités échangées : on ne parle pas de « variation de chaleur » ni de « variation de travail ».

### Q6

> [!INDICATION]
> Identifier les deux thermostats : la combustion dans le cylindre (document 1) et l'air ambiant (refroidissement D→A).

#### Solution

La **source chaude** est modélisée par les **gaz issus de la combustion** du mélange air-carburant dans le cylindre : le document 1 donne une température caractéristique de $800\ °\text{C}$ dans le cylindre d'un moteur Diesel, d'où $T_c=800\ °\text{C}$. La **source froide** est l'**air ambiant extérieur**, au contact duquel s'effectue le refroidissement isochore D→A, d'où $T_f=20\ °\text{C}$.

### Q7

> [!INDICATION]
> Sur un cycle, ΔU = 0 : exprimer le rendement η à l'aide de Q_c et Q_f.

> [!INDICATION]
> Majorer η par l'inégalité de Clausius écrite pour les deux sources (l'égalité correspond au cycle réversible).

#### Solution

Sur un cycle, $\Delta U=0$, donc $W+Q_c+Q_f=0$ : le travail fourni au milieu extérieur vaut $-W=Q_c+Q_f$. Le rendement est

$$
\eta=\frac{-W}{Q_c}=\frac{Q_c+Q_f}{Q_c},
$$

soit

$$
\eta=1+\frac{Q_f}{Q_c}.
$$

Le second principe, sous forme de l'**inégalité de Clausius** pour un cycle entre deux sources à $T_c$ et $T_f$ :

$$
\frac{Q_c}{T_c}+\frac{Q_f}{T_f}\le 0,
$$

d'où $Q_f\le -Q_c\,\dfrac{T_f}{T_c}$ (avec $Q_c>0$), et finalement

$$
\eta=1+\frac{Q_f}{Q_c}\le 1-\frac{T_f}{T_c}.
$$

$$
\boxed{\eta\le\eta_C=1-\frac{T_f}{T_c}}
$$

(avec $T_f<T_c$), l'égalité étant atteinte seulement pour un cycle réversible (rendement de Carnot).

> [!JURY]
> « L’argument de l’inégalité de Clausius en lien avec l’irréversibilité n’est pas toujours bien maîtrisé, pourtant nécessaire dans la démonstration pour prouver que η ≤ ηC » (rapport 2025, p. 9).

### Q8

> [!INDICATION]
> Convertir T_c et T_f en kelvin avant tout calcul numérique.

> [!INDICATION]
> Calculer η_C et η (expression admise par l'énoncé), les comparer au rendement réel de 45 %, et discuter le rôle de la réversibilité.

#### Solution

Conversion en kelvin : $T_f=20+273=293\ \text{K}$ et $T_c=800+273=1073\ \text{K}$. Rendement de Carnot :

$$
\eta_C=1-\frac{293}{1073}\approx\boxed{0{,}73\ \text{soit}\ 73\,\%}.
$$

Rendement du cycle modélisé (expression admise par l'énoncé) :

$$
\eta=1+
\frac{1}{\gamma}\times\frac{\left(\frac1a\right)^{\gamma}-\left(\frac1b\right)^{\gamma}}{\frac1b-\frac1a}.
$$

Avec $\left(\frac1{22}\right)^{1{,}4}\approx1{,}3\times10^{-2}$, $\left(\frac13\right)^{1{,}4}\approx0{,}215$ et $\frac1b-\frac1a\approx0{,}288$ :

$$
\eta\approx1+\frac{1}{1{,}4}\times\frac{1{,}3\times10^{-2}-0{,}215}{0{,}288}\approx\boxed{0{,}50\ \text{soit}\ 50\,\%}.
$$

Le rendement réel d'un moteur Diesel vaut environ $45\ \%$. On a donc

$$
\boxed{\eta_{\text{réel}}\ (45\,\%)<\eta\ (50\,\%)<\eta_C\ (73\,\%)}.
$$

Discussion : $\eta_C$ est un **majorant théorique**, atteint uniquement si le cycle est réversible entre les deux sources. Le cycle modélisé, déjà idéalisé (transformations quasi statiques, sans pertes mécaniques), lui est inférieur ; le moteur réel, soumis à des frottements, des transferts thermiques parasites et une combustion imparfaite, a un rendement encore plus faible.

> [!JURY]
> « Un nombre important et donc non négligeable de candidats oublient de convertir en kelvin les températures Tc et Tf pour calculer le rendement maximal ηC de Carnot » ; « La référence à la réversibilité pour le cycle de Carnot est peu abordée » (rapport 2025, p. 9).

## II. Freinage et collision

Deux sous-parties indépendantes : d'abord l'électromagnétisme (induction et freinage par courants de Foucault), ensuite la mécanique du capteur de choc dans un référentiel non galiléen.

### 1. Freinage par courants de Foucault

Induction électromagnétique : variation de flux → courant induit → force de Laplace freinante, puis équation différentielle du mouvement du cadre.

### Q9

> [!INDICATION]
> Un champ de 1 T : penser aux bobines parcourues par un courant (électroaimant) ou aux aimants permanents puissants (néodyme-fer-bore).

> [!INDICATION]
> Quel est l'ordre de grandeur du champ magnétique terrestre ?

#### Solution

Un champ de $1\ \text{T}$ est obtenu avec un **électroaimant** (bobine parcourue par un courant électrique suffisant) ou un **aimant permanent** au néodyme-fer-bore. Le champ magnétique terrestre vaut environ

$$
\boxed{B_{\text{Terre}}\approx10^{-5}\ \text{T}}
$$

(quelques dizaines de microteslas), soit cinq ordres de grandeur de moins.

### Q10

> [!INDICATION]
> Enchaînement attendu : variation temporelle du flux → f.é.m. induite → courant induit → force de Laplace (loi de modération de Lenz).

> [!INDICATION]
> Cas du cadre entièrement plongé dans la zone : que devient le flux ? que vaut alors la force ?

#### Solution

Lorsque le cadre **pénètre** dans la zone de champ, la surface qu'il offre au champ augmente : le flux magnétique $\Phi$ qui le traverse **varie dans le temps**. Par la loi de **Lenz-Faraday**, une force électromotrice apparaît, qui fait circuler un **courant induit** dans le cadre conducteur. D'après la loi de **modération de Lenz**, les effets de ce courant s'opposent à la cause qui lui donne naissance : la **force de Laplace** résultante s'oppose au déplacement, le cadre est **freiné**.

Lorsque le cadre est **entièrement** dans la zone, le champ étant uniforme, la surface plongée ne varie plus : $\Phi=\text{cte}$, donc $\mathrm{d}\Phi/\mathrm{d}t=0$ : plus de courant induit, plus de force de Laplace ; en l'absence de frottements, le mouvement est **uniforme**.

> [!PIEGE]
> Ne pas confondre la force de Lorentz sur les porteurs de charge (origine microscopique du courant) et la force de Laplace sur le cadre (Q14), ni la vitesse des porteurs et celle du cadre.

### Q11

> [!INDICATION]
> Choisir le sens trigonométrique pour i : le vecteur surface est alors colinéaire et de même sens que B.

> [!INDICATION]
> Tant que le cadre n'est que partiellement dans la zone, la surface plongée vaut ℓ·x(t) : écrire Φ = B⃗·S⃗.

#### Solution

On oriente le courant $i(t)$ dans le **sens trigonométrique** ; par la règle de la main droite, le vecteur surface $\vec S=S\,\vec u_z$ est alors colinéaire et de même sens que $\vec B=B\,\vec u_z$. Tant que le cadre n'est que partiellement dans la zone, la longueur plongée vaut $x(t)$ et la surface concernée vaut $\ell\,x(t)$ :

$$
\Phi(x)=\vec B\cdot\vec S=B\,\ell\,x(t).
$$

$$
\boxed{\Phi(x)=B\,\ell\,x(t)}
$$

### Q12

> [!INDICATION]
> Appliquer la loi de Lenz-Faraday e = −dΦ/dt au flux trouvé en Q11, avec v = dx/dt.

#### Solution

Loi de **Lenz-Faraday** : $e=-\dfrac{\mathrm{d}\Phi}{\mathrm{d}t}$. Avec $\Phi=B\,\ell\,x$ et $v=\dot x$ :

$$
e(t)=-B\,\ell\,\frac{\mathrm{d}x}{\mathrm{d}t},
$$

$$
\boxed{e(t)=-B\,\ell\,v(t)}.
$$

### Q13

> [!INDICATION]
> R_c modélise la résistivité du matériau conducteur (dissipation par effet Joule).

> [!INDICATION]
> Circuit équivalent : f.é.m. e en série avec R_c (inductance propre négligée) ; loi des mailles, avec les conventions d'orientation.

#### Solution

La résistance $R_c$ est la **résistance électrique totale du cadre** : elle modélise la **résistivité du matériau conducteur** et la dissipation d'énergie par **effet Joule** lors de la circulation du courant induit.

Circuit équivalent (inductance propre négligée) : la force électromotrice $e$ en série avec $R_c$ :

```text
      i(t) →
   ┌──────────┐
   +          │
  (e)       [R_c]
   −          │
   └──────────┘
```

Loi des mailles : $e=R_c\,i$, d'où

$$
i(t)=\frac{e(t)}{R_c},
$$

$$
\boxed{i(t)=-\frac{B\,\ell\,v(t)}{R_c}}.
$$

> [!JURY]
> Le rapport 2025 attendait « soit une référence à la résistivité du matériau soit à l’effet Joule » (p. 10).

### Q14

> [!INDICATION]
> Seul le côté du cadre situé dans le champ contribue : écrire la force de Laplace F⃗_L = i ℓ⃗ ∧ B⃗.

> [!INDICATION]
> Attention à la rigueur des signes, en lien avec le sens de i choisi en Q11.

#### Solution

Seul le côté du cadre situé dans le champ contribue à la force de Laplace : le côté AB, de longueur $\ell$, orienté selon $\vec u_y$ par le sens trigonométrique choisi en Q11. La résultante des forces de Laplace vaut $\vec F_L=i\,\vec\ell\wedge\vec B$ :

$$
\vec F_L=i(t)\,\ell\,\vec u_y\wedge B\,\vec u_z=i(t)\,\ell\,B\,\vec u_x.
$$

En reportant l'expression de $i(t)$ (Q13) :

$$
\boxed{\vec F_L=-\frac{B^2\ell^2}{R_c}\,v(t)\,\vec u_x}.
$$

Cette force est **opposée à la vitesse** : elle freine le cadre, conformément à la loi de Lenz.

> [!METHODE]
> Avec le sens trigonométrique, le côté AB est orienté selon +u_y et u_y ∧ u_z = u_x : le produit vectoriel se fait pas à pas.

### Q15

> [!INDICATION]
> Deuxième loi de Newton dans le référentiel terrestre (galiléen), projetée sur u_x : seule la force de Laplace est horizontale.

> [!INDICATION]
> Mettre le résultat sous la forme dv/dt + (1/τ)v = 0 et identifier τ.

#### Solution

Deuxième loi de Newton dans le référentiel terrestre galiléen, projetée sur $\vec u_x$ (les forces orthogonales au mouvement, poids et réaction du support, sont écartées) :

$$
m\frac{\mathrm{d}v}{\mathrm{d}t}=-\frac{B^2\ell^2}{R_c}\,v.
$$

$$
\frac{\mathrm{d}v}{\mathrm{d}t}+\frac{1}{\tau}\,v=0
$$

avec

$$
\boxed{\tau=\frac{m\,R_c}{B^2\ell^2}}.
$$

### Q16

> [!INDICATION]
> Application numérique de τ en unités SI (ℓ en mètres).

> [!INDICATION]
> Comparer τ à la durée de l'expérience et conclure sur la faisabilité en classe (distance de freinage ~ v_0τ).

#### Solution

$$
\tau=\frac{2{,}0\times1{,}0\times10^{-3}}{(1{,}0)^2\times(0{,}10)^2}=\boxed{0{,}2\ \text{s}}.
$$

La vitesse décroît sur quelques $\tau$, soit une fraction de seconde ; la distance de freinage (Q18) est de l'ordre de $v_0\tau\approx0{,}2\ \text{m}$ pour $v_0\sim1\ \text{m·s}^{-1}$. L'expérience est **réalisable en classe** (rail à coussin d'air, enregistrement rapide par caméra par exemple).

### Q17

> [!INDICATION]
> Résoudre l'équation du premier ordre avec la condition initiale v(0) = v_0.

> [!INDICATION]
> Allure de v(t) ; pourquoi la vitesse tend-elle vers 0 sans jamais l'atteindre ?

#### Solution

Équation $\dot v+v/\tau=0$, $v(0)=v_0$ :

$$
\boxed{v(t)=v_0\,e^{-t/\tau}}.
$$

Allure : exponentielle décroissante de $v_0$ (en $t=0$) vers $0$, d'asymptote horizontale $v=0$, dont la tangente à l'origine coupe l'axe des temps en $t=\tau$. La vitesse tend vers $0$ **sans jamais l'atteindre** : ce freinage, d'effet proportionnel à la vitesse, ne peut immobiliser le véhicule ; il doit rester un **complément** d'un freinage classique par frottements.

### Q18

> [!INDICATION]
> x(t) s'obtient en intégrant v(t) : ne pas oublier la condition initiale x(0) = 0.

> [!INDICATION]
> Limite de x(t) quand t ≫ τ : ordre de grandeur de la zone de freinage.

#### Solution

Avec $x(0)=0$ :

$$
x(t)=\int_0^t v_0\,e^{-t'/\tau}\,\mathrm{d}t',
$$

$$
\boxed{x(t)=v_0\tau\left(1-e^{-t/\tau}\right)}.
$$

Lorsque $t\gg\tau$, $x(t)\to v_0\tau$ : l'ordre de grandeur de la **zone de freinage** est

$$
\boxed{x_{\infty}\approx v_0\,\tau}.
$$

> [!PIEGE]
> La constante d'intégration est souvent oubliée ou prise nulle à tort ; certains confondent primitive et dérivée.

### Q19

> [!INDICATION]
> Pour la roue, chaque secteur du disque entre puis sort de la zone de champ : le flux varie.

> [!INDICATION]
> Si tout le disque était dans un champ uniforme, le flux serait constant : que se passerait-il ? Citer avantages et inconvénients.

#### Solution

Pour une roue, le disque conducteur solidaire tourne devant un champ $\vec B$ **localisé sur une partie du disque** : chaque secteur du disque entre puis sort continûment de la zone de champ, donc le flux qui le traverse **varie dans le temps** ; il y naît des **courants de Foucault** et une force de Laplace freinante (couple de freinage). Si tout le disque était plongé dans un champ uniforme, le flux serait constant au cours de la rotation : aucun courant induit, aucun freinage. Il est donc indispensable de ne plonger qu'une partie de la roue dans la zone magnétique.

Avantages : freinage **sans contact** (pas d'usure de garniture), moins sensible à l'échauffement que les freins classiques. Inconvénients : pas d'**arrêt complet** possible (effet proportionnel à la vitesse), énergie dissipée par effet Joule ; à n'utiliser qu'en complément de freins classiques.

> [!JURY]
> « La nécessaire variation temporelle du flux magnétique pour engendrer des courants de Foucault, et donc un freinage, explique la nécessité de ne plonger qu’une seule partie de la roue dans la zone magnétique » (rapport 2025, p. 10).

### 2. Éléments de sécurité lors d'un impact

Choc frontal : référentiel non galiléen du véhicule, force d'inertie d'entraînement, oscillateur amorti et seuil de déclenchement de l'airbag.

### Q20

> [!INDICATION]
> Définir un référentiel galiléen via le principe d'inertie ; distinguer soigneusement repère et référentiel.

> [!INDICATION]
> Hypothèse temporelle : comparer la durée de l'expérience à la période de rotation propre de la Terre (24 h).

#### Solution

Un **référentiel** est un solide de référence muni d'une horloge ; un **repère** n'en est que la description mathématique (origine et base). Un référentiel est **galiléen** si le **principe d'inertie** y est vérifié : tout point matériel isolé (ou pseudo-isolé) y est animé d'un mouvement rectiligne uniforme.

Hypothèse temporelle pour le référentiel terrestre : la durée de l'expérience doit être **très inférieure à 24 h**, période de **rotation propre** de la Terre autour de l'axe des pôles, pour que les effets de cette rotation (forces d'inertie) soient négligeables.

> [!JURY]
> « Il est notamment incontournable de savoir distinguer repère et référentiel » (rapport 2025, p. 10).

### Q21

> [!INDICATION]
> Dans R galiléen, au moment de l'arrêt brutal du véhicule : appliquer la première loi de Newton à M.

> [!INDICATION]
> En déduire le mouvement de M dans le référentiel R_V du véhicule.

#### Solution

À l'instant où le véhicule s'arrête brutalement, dans le référentiel terrestre $R$ galiléen, la masse $M$ n'est soumise à aucune force horizontale (le ressort est à sa longueur à vide, le poids est compensé par le support). Par la **première loi de Newton** (principe d'inertie), elle **conserve son mouvement rectiligne uniforme** à la vitesse $v_0$ selon $+\vec u_x$.

Dans le référentiel du véhicule $R_V$, qui décélère, la masse $M$ se déplace donc **vers l'avant** (selon $+\vec u_{x_1}$) et comprime le ressort.

### Q22

> [!INDICATION]
> Pendant la décélération, R_V est non galiléen : ajouter la force d'inertie d'entraînement (translation → pas de force de Coriolis).

> [!INDICATION]
> Lister les autres forces selon u_x1 : rappel du ressort (−k x_1, l'élongation vaut x_1) et frottement fluide (−α ẋ_1).

#### Solution

Pendant la phase de décélération, le véhicule n'est pas en translation rectiligne uniforme par rapport à $R$ : le référentiel $R_V$ est **non galiléen**, et la **force d'inertie d'entraînement** $\vec F_{ie}=-m\,\vec a_e$ doit être prise en compte dans la relation fondamentale de la dynamique appliquée dans $R_V$. (Le mouvement de $R_V$ par rapport à $R$ étant une translation, la force d'inertie de Coriolis est nulle.)

Les autres forces s'exerçant sur $M$ selon $\vec u_{x_1}$ sont :

- la **force de rappel du ressort** : $-k\,x_1\,\vec u_{x_1}$, l'élongation étant directement égale à $x_1$ (car $x_1=\ell_0-\ell$ dans la configuration du schéma, $\ell_0$ n'intervient donc pas) ;
- la **force de frottement fluide** : $-\alpha\,\dot x_1\,\vec u_{x_1}$.

> [!JURY]
> Le rapport 2025 précise que « l’élongation [est] directement égale à x1 car x1 = ℓ0 – ℓ », la longueur à vide ℓ0 n’intervenant pas (p. 11).

### Q23

> [!INDICATION]
> Allure de v_v(t) : segment de droite de (0, v_0) à (t_f, 0), puis nul.

> [!INDICATION]
> Écrire v_v(t) affine par morceaux sur [0, t_f].

#### Solution

$v_v(t)$ décroît **affinement** de $v_0$ (en $t=0$) à $0$ (en $t=t_f$), puis reste nulle :

$$
\boxed{v_v(t)=v_0\left(1-\frac{t}{t_f}\right)}
$$

pour $0\le t\le t_f$ (et $v_v=0$ après $t_f$).

### Q24

> [!INDICATION]
> L'accélération d'entraînement est a_e = dv_v/dt ; la force d'inertie d'entraînement vaut F_ie = −m a_e.

#### Solution

L'accélération d'entraînement est celle du véhicule :

$$
\vec a_e=\frac{\mathrm{d}\vec v_v}{\mathrm{d}t}=-\frac{v_0}{t_f}\,\vec u_x.
$$

La force d'inertie d'entraînement vaut $\vec F_{ie}=-m\,\vec a_e$ :

$$
\vec F_{ie}=-m\left(-\frac{v_0}{t_f}\,\vec u_x\right),
$$

$$
\boxed{\vec F_{ie}=m\,\frac{v_0}{t_f}\,\vec u_{x_1}}.
$$

### Q25

> [!INDICATION]
> Assembler Q22-Q24 : RFD dans R_V projetée sur u_x1, avec la force d'inertie.

> [!INDICATION]
> Diviser par m et identifier terme à terme avec la forme canonique (ω_0, Q, x_e).

#### Solution

Relation fondamentale de la dynamique dans $R_V$ (non galiléen), projetée sur $\vec u_{x_1}$ :

$$
m\,\ddot x_1=-k\,x_1-\alpha\,\dot x_1+m\frac{v_0}{t_f}.
$$

En divisant par $m$ :

$$
\ddot x_1+\frac{\alpha}{m}\,\dot x_1+\frac{k}{m}\,x_1=\frac{v_0}{t_f}.
$$

Par identification avec $\ddot x_1+\dfrac{\omega_0}{Q}\,\dot x_1+\omega_0^2\,x_1=\omega_0^2\,x_e$ :

$$
\boxed{\omega_0=\sqrt{\frac{k}{m}}},
$$

$$
\boxed{Q=\frac{m\,\omega_0}{\alpha}=\frac{\sqrt{k\,m}}{\alpha}},
$$

$$
\boxed{x_e=\frac{v_0}{t_f\,\omega_0^2}=\frac{m\,v_0}{k\,t_f}}.
$$

### Q26

> [!INDICATION]
> Lire la figure 6 : quelles oscillations observe-t-on ?

> [!INDICATION]
> Nommer les trois régimes transitoires possibles pour un oscillateur du second ordre.

#### Solution

La figure 6 présente des **oscillations amorties** qui s'atténuent : c'est le régime **pseudo-périodique**. Les deux autres régimes transitoires possibles pour cette équation du second ordre sont le régime **apériodique** (amortissement fort, retour à l'équilibre sans oscillation) et le régime **critique** (cas limite, retour le plus rapide sans oscillation).

### Q27

> [!INDICATION]
> Donner le sens physique de Q (énergie emmagasinée / énergie dissipée par pseudo-période) et sa valeur limite.

> [!INDICATION]
> Conclure pour Q = 1 à partir de la figure 6.

#### Solution

Le **facteur de qualité** $Q$ caractérise l'amortissement : $Q=2\pi\times\dfrac{\text{énergie emmagasinée}}{\text{énergie dissipée par pseudo-période}}$. La **valeur limite** qui distingue les régimes est

$$
\boxed{Q=\frac12}.
$$

Elle vaut $Q>\tfrac12$ en régime pseudo-périodique, $Q<\tfrac12$ en régime apériodique, et $Q=\tfrac12$ au régime critique.
Un facteur $Q=1>\tfrac12$ donne bien un régime **pseudo-périodique**, en accord avec le tracé de la figure 6.

### Q28

> [!INDICATION]
> Condition de déclenchement : d_max ≥ ℓ_0/2 ; le seuil a_0,min s'obtient au cas limite d_max = ℓ_0/2.

> [!INDICATION]
> Isoler a_0,min dans l'expression admise d_max = (m a_0/k)(1 + e^{−t_a/τ}).

#### Solution

Le contact électrique (déclenchement de l'airbag) a lieu lorsque $d_{\max}\ge\dfrac{\ell_0}{2}$. La décélération minimale $a_{0,\min}$ correspond au cas limite $d_{\max}=\dfrac{\ell_0}{2}$, avec $d_{\max}=\dfrac{m\,a_0}{k}\left(1+e^{-t_a/\tau}\right)$ :

$$
\frac{m\,a_{0,\min}}{k}\left(1+e^{-t_a/\tau}\right)=\frac{\ell_0}{2},
$$

$$
\boxed{a_{0,\min}=\frac{k\,\ell_0}{2\,m\left(1+e^{-t_a/\tau}\right)}}.
$$

### Q29

> [!INDICATION]
> Lire t_a sur la figure 6 : première annulation de la vitesse (pas le minimum).

> [!INDICATION]
> Calculer τ = 2Q/ω_0 pour Q = 1, puis a_0,min ; comparer à 5g.

#### Solution

Sur la figure 6, la vitesse de la masse mobile s'annule **pour la première fois** en $t_a\approx0{,}05\ \text{s}$ (première annulation, à ne pas confondre avec le minimum, atteint plus tard). Pour $Q=1$ :

$$
\omega_0=\sqrt{\frac{k}{m}}=\sqrt{\frac{55}{0{,}010}}\approx74\ \text{rad·s}^{-1},
$$

$$
\tau=\frac{2Q}{\omega_0}\approx\boxed{2{,}7\times10^{-2}\ \text{s}}.
$$

Avec $t_a/\tau\approx1{,}9$, donc $e^{-t_a/\tau}\approx0{,}16$ :

$$
a_{0,\min}=\frac{55\times0{,}020}{2\times0{,}010\times(1+0{,}16)}\approx\boxed{47\ \text{m·s}^{-2}}.
$$

Or $5\,g=5\times9{,}81\approx49\ \text{m·s}^{-2}>a_{0,\min}$ : une décélération de $5\,g$ dépasse le seuil minimal, le capteur **est capable de la détecter** et de déclencher l'airbag.

> [!JURY]
> « Certains candidats ont confondus annulation de la fonction avec minimum » (rapport 2025, p. 11).

## III. Éléments facilitant la conduite

Deux sous-parties indépendantes : l'optique géométrique (réflexion totale, détecteur de pluie), puis l'électrocinétique et le capteur de luminosité (photodiode, programme Python, microcontrôleur).

### 1. Détecteur de pluie de voiture

Le détecteur joue sur le changement d'interface verre→air (réflexion totale) / verre→eau (réfraction) au dioptre supérieur du pare-brise.

### Q30

> [!INDICATION]
> Rappeler la loi de Snell-Descartes n_1 sin i_1 = n_2 sin i_2 et considérer le cas limite i_2 = 90°.

#### Solution

Loi de **Snell-Descartes** pour la réfraction : $n_1\sin i_1=n_2\sin i_2$. Pour $n_2<n_1$, l'angle réfracté croît avec $i_1$ et vaut au maximum $i_2=90°$ à l'incidence limite $i_{1\ell}$ ; au-delà, il y a réflexion totale. Au cas limite :

$$
n_1\sin i_{1\ell}=n_2\sin90°=n_2,
$$

$$
\boxed{i_{1\ell}=\arcsin\!\left(\frac{n_2}{n_1}\right)}.
$$

### Q31

> [!INDICATION]
> Trois applications numériques de l'angle limite, avec 3 chiffres significatifs.

#### Solution

Trois applications numériques (3 chiffres significatifs) :

- verre → air : $i_{1\ell}=\arcsin\!\left(\dfrac{1{,}00}{1{,}50}\right)\approx\boxed{41{,}8°}$ ;
- verre → eau : $i_{1\ell}=\arcsin\!\left(\dfrac{1{,}33}{1{,}50}\right)\approx\boxed{62{,}5°}$ ;
- eau → air : $i_{1\ell}=\arcsin\!\left(\dfrac{1{,}00}{1{,}33}\right)\approx\boxed{48{,}8°}$.

### Q32

> [!INDICATION]
> Géométrie dans la lame : déplacement horizontal y_A = e tan α pour traverser l'épaisseur e.

> [!INDICATION]
> Angle d'incidence en A (angle alterne interne de l'angle d'entrée), comparé à l'angle limite verre→air.

#### Solution

Dans la lame, le rayon fait l'angle $\alpha=45°$ avec la normale $(Oz)$ ; le déplacement horizontal pour traverser l'épaisseur $e$ vaut $e\tan\alpha$ :

$$
y_A=e\tan\alpha,
$$

$$
y_A=1\ \text{cm}\times\tan45°=\boxed{1\ \text{cm}}.
$$

À l'interface supérieure verre→air (normale verticale), l'**angle d'incidence en A** vaut $45°$ (angle alterne interne de l'angle d'entrée). Comme

$$
45°>i_{1\ell}(\text{verre}\to\text{air})=41{,}8°,
$$

le rayon subit une **réflexion totale** en A : il est totalement réfléchi.

> [!JURY]
> « L’explicitation de la valeur de l’angle d’incidence en A […] a été trop rare » (rapport 2025, p. 11).

### Q33

> [!INDICATION]
> Avec une goutte en A, l'interface devient verre→eau : comparer 45° au nouvel angle limite.

> [!INDICATION]
> Pourquoi le constructeur choisit-il 45° ? Le situer entre les deux angles limites.

#### Solution

Si une goutte d'eau est déposée en A, l'interface devient **verre→eau**, d'angle limite $i_{1\ell}=62{,}5°$. Comme $45°<62{,}5°$, la réflexion totale ** cesse** : le rayon est partiellement réfracté et sort du pare-brise (il n'atteint plus le récepteur).

Le constructeur choisit $\alpha=45°$ parce que cet angle est **compris entre les deux angles limites** :

$$
i_{1\ell}(\text{verre}\to\text{air})=41{,}8°<45°<i_{1\ell}(\text{verre}\to\text{eau})=62{,}5°.
$$

Ainsi, sans goutte (verre→air), il y a réflexion totale et le signal reste guidé vers le récepteur ; avec une goutte (verre→eau), le signal fuit vers l'extérieur. Le dispositif discrimine donc la présence d'eau sur le pare-brise.

### Q34

> [!INDICATION]
> Un déplacement horizontal de e tan 45° = 1 cm par traversée de la lame : enchaîner les réflexions totales.

> [!INDICATION]
> Jusqu'où monte le rayon avant de rencontrer la goutte en B (y_B = 3 cm) ? Quelle réfraction y a-t-il alors ?

#### Solution

Goutte au point B ($y_B=3\ \text{cm}$, face supérieure $z=e$). Le rayon pénètre en O sous $\alpha=45°$ ; à chaque traversée de la lame ($e=1\ \text{cm}$), il se décale horizontalement de $e\tan45°=1\ \text{cm}$. Marche du rayon :

- O ($y=0$) → A ($y=1\ \text{cm}$, face supérieure, verre→air) : **réflexion totale** ;
- A → $y=2\ \text{cm}$ (face inférieure, verre→air) : **réflexion totale** ;
- $y=2\ \text{cm}$ → B ($y=3\ \text{cm}$, face supérieure, interface verre→eau à cause de la goutte) : **réfraction**, le rayon sort du pare-brise.

**Deux réflexions totales, puis une réfraction au point B.**

> [!JURY]
> « Le jury attendait in fine dans la construction deux réflexions totales, puis une réfraction au point B » (rapport 2025, p. 12).

### Q35

> [!INDICATION]
> Chaque goutte crée une interface verre→eau où le rayon fuit partiellement au lieu d'être totalement réfléchi.

> [!INDICATION]
> Relier le nombre de gouttes à l'intensité reçue, puis énoncer le principe du détecteur.

#### Solution

Chaque goutte déposée sur le pare-brise crée une interface verre→eau : à sa rencontre, le rayon, au lieu d'être totalement réfléchi, est **partiellement réfracté** et perd une partie de son énergie vers l'extérieur. Plus il y a de gouttes, plus le rayon « fuit » à chaque rencontre, et **moins l'intensité lumineuse** parvenant au récepteur est importante.

Principe du détecteur : la photodiode mesure l'intensité reçue ; une **baisse** de cette intensité traduit la présence de gouttes de pluie, et commande le déclenchement des essuie-glaces à une fréquence d'autant plus élevée que la pluie est dense.

### 2. Allumage automatique des feux de croisement

Photodiode polarisée en inverse : lois des circuits, programme Python de tracé, caractéristique, puis capteur de luminosité piloté par microcontrôleur.

### Q36

> [!INDICATION]
> Loi des mailles sur la maille (E, photodiode, R) — les tensions sont des scalaires — puis loi d'Ohm aux bornes de R.

#### Solution

**Loi des mailles** (relation entre tensions, grandeurs scalaires) :

$$
\boxed{E=u_d+u_R}.
$$

**Loi d'Ohm** aux bornes de $R$ (convention récepteur) : $u_R=R\,i_d$, d'où

$$
\boxed{i_d=\frac{u_R}{R}}.
$$

> [!JURY]
> « Les tensions ne sont pas des vecteurs et ne doivent pas apparaître comme tel lors de l’écriture de la loi des mailles » (rapport 2025, p. 12).

### Q37

> [!INDICATION]
> Sur la figure 9, u_d se déduit de la loi des mailles ; i_d = u_R/R est en ampères.

> [!INDICATION]
> Convertir le courant en µA dans la ligne 15 : quel facteur multiplicatif ?

#### Solution

Lignes 14 et 15 du programme, à partir de la figure 9 ($u_d=E-u_R$ d'après la loi des mailles ; $u_R/R$ est en A, d'où le facteur $10^6$ pour obtenir des µA) :

```python
u_d = E - u_R            # en V
i_d = u_R / R * 1e6      # en µA
```

> [!PIEGE]
> Le facteur de conversion A → µA (×10^6, écrit 1e6) est frequently oublié à la ligne 15 ; 10^{-6} est une erreur. Le rapport 2025 le signale explicitement (p. 12).

### Q38

> [!INDICATION]
> Générateur de courant continu = plateau de la caractéristique (i_d constant) avec u_d et i_d de signes opposés.

> [!INDICATION]
> Lire l'intervalle de u_d correspondant sur la figure 10.

#### Solution

La photodiode polarisée en inverse se comporte comme un **générateur de courant continu** lorsque le courant $i_d$ est **constant** (plateau de la caractéristique, figure 10) et que $u_d$ et $i_d$ sont de **signes opposés** (fonctionnement générateur). Sur la figure 10, cela correspond à :

$$
\boxed{u_d\in[-0{,}25\ \text{V}\,;\,0\ \text{V}]}.
$$

> [!JURY]
> « L’intervalle demandé de la tension ud était [– 0,25 V ; 0 V] pour que l’intensité id soit constante » (rapport 2025, p. 12).

### Q39

> [!INDICATION]
> Sur papier log-log, une droite traduit une loi puissance : log I_ra = a log E_A + b, soit I_ra = 10^b (E_A)^a.

> [!INDICATION]
> Deux points de la droite de la figure 11 donnent la pente a, puis 10^b.

#### Solution

Sur la figure 11 (papier **log-log**), la caractéristique est une droite : elle traduit une loi puissance $\log I_{ra}=a\log E_A+b$, soit $I_{ra}=10^{b}(E_A)^{a}$. Deux points de la droite : $(E_A=10\ \text{lux}\,;\,I_{ra}\approx0{,}6\ \mu\text{A})$ et $(E_A=10^{4}\ \text{lux}\,;\,I_{ra}\approx600\ \mu\text{A})$. Pente :

$$
a=\frac{\log(600)-\log(0{,}6)}{\log(10^{4})-\log(10)},
$$

$$
a=\frac{3}{3}=1.
$$

Ordonnée à l'origine : $10^{b}=\dfrac{I_{ra}}{E_A}=\dfrac{0{,}6}{10}=0{,}06$. D'où la relation numérique (loi **linéaire**) :

$$
\boxed{I_{ra}\approx0{,}06\times E_A}\qquad(I_{ra}\ \text{en}\ \mu\text{A},\ E_A\ \text{en}\ \text{lux}).
$$

> [!JURY]
> « L’exploitation de la représentation graphique de la figure 11 tracée sur papier logarithmique a été très rare » (rapport 2025, p. 12).

### Q40

> [!INDICATION]
> Intérêt de I_ra = f(E_A) : mesurer un courant revient à mesurer un éclairement (capteur).

> [!INDICATION]
> Mise en œuvre : chaîne de mesure u_R → i_d → E_A, seuil programmé, commande des feux par le microcontrôleur.

#### Solution

L'intérêt d'une telle relation est d'établir une correspondance **biunivoque et proportionnelle** entre l'éclairement $E_A$ et une grandeur électrique directement mesurable : mesurer le courant $i_d$ (via $u_R=R\,i_d$) revient à mesurer la luminosité. C'est le principe d'un **capteur de luminosité**.

Mise en œuvre avec le microcontrôleur : la photodiode polarisée en inverse, associée à $R$, débite un courant $i_d=I_{ra}$ proportionnel à $E_A$ ;
le microcontrôleur mesure $u_R$ sur l'entrée analogique A1, en déduit $i_d=u_R/R$ puis $E_A=i_d/0{,}06$.
Un **seuil d'éclairement** est programmé : lorsque $E_A$ passe en dessous (tombée du jour, entrée d'un tunnel), le microcontrôleur commande l'**allumage automatique des feux de croisement** (et leur extinction lorsque la luminosité remonte au-dessus du seuil).

> [!JURY]
> « Cette question a été très rarement traitée » (rapport 2025, p. 12) : elle valorise fortement une copie qui va jusqu’au capteur piloté.

## Bilan

- **Partie I (moteur Diesel).** Repérer le caractère de chaque transformation (isochore, isobare, adiabatique réversible) avant toute loi ; loi de Laplace avec ses hypothèses (gaz parfait, isentropique) ; sur un cycle ΔU = 0 ; le rendement est borné par Carnot via l'inégalité de Clausius, avec égalité seulement pour un cycle réversible. Piège classique : oublier la conversion en kelvin (Q8).
- **Partie II (freinage et collision).** Freinage par induction : flux → f.é.m. (Lenz-Faraday) → courant → force de Laplace opposée au mouvement, d'où dv/dt + v/τ = 0 et v(t) = v_0 e^{−t/τ} (jamais d'arrêt complet). Capteur de choc : référentiel non galiléen → force d'inertie d'entraînement F_ie = −m a_e ; oscillateur amorti caractérisé par ω_0, Q (valeur limite 1/2) ; seuil de déclenchement d_max ≥ ℓ_0/2.
- **Partie III (conduite assistée).** Réflexion totale : angle limite i_{1ℓ} = arcsin(n_2/n_1), atteint quand i_2 = 90° ; le détecteur de pluie exploite le passage verre→air / verre→eau autour de 45°. Photodiode en inverse : loi des mailles scalaire E = u_d + u_R, loi d'Ohm, conversion A→µA (×10^6) dans le programme, lecture d'une caractéristique (plateau générateur pour u_d ∈ [−0,25 V ; 0 V]) et d'un graphe log-log (loi puissance, ici linéaire).
- **Prérequis à revoir** : lois de Laplace et inégalité de Clausius, induction (Lenz-Faraday, Laplace), référentiels non galilens et forces d'inertie, oscillateur amorti (pseudo-périodique/apériodique/critique), Snell-Descartes et réflexion totale, lois des circuits en régime continu, proportionnalité capteur.
- **Transposable** : la chaîne « variation de flux → courant induit → force de Laplace » se retrouve dans tout freinage par induction (trains, poids lourds) ; la lecture log-log d'une loi puissance sert dès qu'un graphe est tracé sur papier logarithmique ; le seuil « d_max ≥ ℓ_0/2 » est un raisonnement de cas limite classique.
- **Conseils de rédaction du jury (rapport 2025)** : lisibilité, numéros de questions ressortis, expressions littérales privilégiées (vérification de l'homogénéité), lois énoncées à chaque utilisation, notations vectorielles rigoureuses, conversions d'unités soignées.
