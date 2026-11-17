# CAPES Physique — Épreuve d'admissibilité 1 (bac+3) 2026 · Corrigé guidé

*Corrigé rédigé par IA, non officiel. Signalez toute erreur.*

Tronc traité : **majeure physique (14 points) + mineure chimie (6 points)**.

## Présentation du sujet

**Format.** Première épreuve d'admissibilité du CAPES/CAFEP bac+3, section physique-chimie : 4 heures, calculatrice autorisée (circulaire du 17 juin 2021), sans aucun document. Le sujet propose deux troncs exclusifs ; celui traité ici est **majeure physique (14 points) + mineure chimie (6 points)**, soit **52 questions**. La copie doit reprendre le titre de chaque partie traitée, et la note zéro à l'une des deux parties est éliminatoire. Session 2026 : moyenne de la majeure physique **7,74/14** (écart-type 2,75), barre d'admissibilité **9,13/20**.

**Thème.** Trois mesures historiques de la célérité $c$ de la lumière dans le vide : une mesure **électrocinétique** par circuit $LC$ (Rosa & Dorsey, 1907), qui relie $c$ aux constantes $\varepsilon_0$ et $\mu_0$ sans mesurer ni distance ni temps ($c=1/\sqrt{\mu_0\varepsilon_0}$) ; une mesure par **cavité résonante cylindrique** (Essen & Gordon-Smith, 1948), où la séparation des variables fait émerger les fonctions de Bessel ; une mesure par **battements des modes longitudinaux** d'un laser He-Ne (D'Orazio *et al.*, 2010). La mineure chimie porte sur l'électrochimie du nettoyage de l'argenterie (pile Al/Ag₂S) puis sur deux dosages de l'urée (colorimétrique par la triazine, pH-métrique en retour).

**Notions mobilisées (programmes bac+3).** Équations de Maxwell et ondes électromagnétiques dans le vide ; électrostatique (théorème de Gauss, condensateur plan) ; magnétostatique (théorème d'Ampère, inductance propre) ; électrocinétique (oscillateur $LC$) ; mesures et incertitudes (propagation, écart normalisé) ; cavité électromagnétique, séparation des variables, équation de Bessel ; ondes et battements ; chimie : atomistique, structure de Lewis, quotient de réaction, oxydoréduction et piles, spectrophotométrie UV-visible (loi de Beer-Lambert), dosage acido-basique en retour.

**Difficulté et gestion du temps.** Taux de réussite observés (rapport 2026) : majeure physique — A.1 (Q1-5) 59 %, A.2 (Q6-20) 33 à 39 %, B (Q21-30) 31 %, C (Q31-35) 21 % ; mineure chimie — A (Q1-9) 61 %, B (Q10-17) 49 %. Ordre conseillé : sécuriser d'abord A.1 puis A.2 (Gauss, Ampère, circuit $LC$), puis la mineure chimie, très rentable, avant d'attaquer la cavité (B) et le laser (C). Questions décisives : Q19-Q20 (exploitation de la régression et incertitude), **Q26 (coquille de l'énoncé à signaler)**, Q30 et Q35 (où $c$ est obtenu avec la plus grande précision), et en chimie Q14-Q17 (titrage en retour). Le jury attend de la rigueur transversale : « il faut être capable de vérifier l'homogénéité d'une formule, de choisir de façon cohérente le nombre de chiffres significatifs pour une application numérique, de manipuler les objets mathématiques (fonctions, vecteurs, etc.) avec rigueur ». Comptez environ 2 h 45 pour la majeure physique et 1 h 15 pour la mineure chimie.

# CAPES Physique — Épreuve d'admissibilité 1 (bac+3) 2026 · Corrigé brut

*Corrigé rédigé par IA, non officiel. Signalez toute erreur.*

Tronc traité : **majeure physique (14 points) + mineure chimie (6 points)**. Épreuve de 4 heures, calculatrice autorisée, sans document. La célérité de la lumière dans le vide est notée $c$, fixée à $299\,792\,458~\text{m}\cdot\text{s}^{-1}$.

## MAJEURE PHYSIQUE (14 points) — Une histoire de la mesure de la célérité de la lumière dans le vide

### Partie A — Mesure de $c$ par circuits électriques : Rosa & Dorsey (1907)

**A.1 — La théorie électromagnétique de Maxwell.**

### Q1

> [!INDICATION]
> Quelles sont les sources ($\rho$, $\vec\jmath$) dans un espace vide ? Attention à ne pas annuler les dérivées temporelles.

#### Solution

Dans un espace vide de charge et de courant ($\rho=0$, $\vec\jmath=\vec 0$), les équations de Maxwell deviennent :

$$
\begin{aligned}
\operatorname{div}\vec E&=0, & \operatorname{div}\vec B&=0,\\
\overrightarrow{\operatorname{rot}}\,\vec E&=-\frac{\partial\vec B}{\partial t}, &
\overrightarrow{\operatorname{rot}}\,\vec B&=\mu_0\varepsilon_0\frac{\partial\vec E}{\partial t}.
\end{aligned}
$$

### Q2

> [!INDICATION]
> Prendre le rotationnel de l'équation de Maxwell-Faraday, utiliser l'identité fournie avec $\operatorname{div}\vec E=0$.

> [!INDICATION]
> Traiter explicitement le cas de $\vec B$ : pas de « de même ».

#### Solution


Dans le vide sans charge ni courant, les équations de Maxwell donnent $\operatorname{div}\vec E=\operatorname{div}\vec B=0$, $\operatorname{rot}\vec E=-\partial_t\vec B$ et $\operatorname{rot}\vec B=\mu_0\varepsilon_0\partial_t\vec E$.

En utilisant l'identité $\operatorname{rot}(\operatorname{rot}\vec A)=\operatorname{grad}(\operatorname{div}\vec A)-\Delta\vec A$,

$$
\begin{aligned}
-\Delta\vec E
&=\operatorname{rot}(\operatorname{rot}\vec E)\\
&=-\partial_t(\operatorname{rot}\vec B)\\
&=-\mu_0\varepsilon_0\partial_t^2\vec E,
\end{aligned}
$$

d'où $\boxed{\Delta\vec E-\mu_0\varepsilon_0\partial_t^2\vec E=\vec0}$.

Pour le champ magnétique, le calcul explicite est

$$
\begin{aligned}
-\Delta\vec B
&=\operatorname{rot}(\operatorname{rot}\vec B)\\
&=\mu_0\varepsilon_0\partial_t(\operatorname{rot}\vec E)\\
&=-\mu_0\varepsilon_0\partial_t^2\vec B.
\end{aligned}
$$

Ainsi $\boxed{\Delta\vec B-\mu_0\varepsilon_0\partial_t^2\vec B=\vec0}$.

> [!JURY]
> « le jury sanctionne les copies avec des égalités entre grandeurs vectorielle d’un côté et scalaire de l’autre côté » ; « une mention du type “de même pour le champ magnétique” (ou analogue) n’est pas suffisante ».

### Q3

> [!INDICATION]
> Évaluer le champ en $z$ à l'instant $t+\Delta t$, et le comparer à sa valeur à l'instant $t$ en $z-\Delta z$, avec $\Delta z=c\Delta t$.

#### Solution

Posons $E(z,t)=E(t-z/c)$. À l'instant $t+\Delta t$ et à l'abscisse $z$, le champ vaut $E(t+\Delta t-z/c)$. Or :

$$
E\!\left(t+\Delta t-\frac{z}{c}\right)=E\!\left(t-\frac{z-c\Delta t}{c}\right),
$$

c'est-à-dire la valeur qu'avait le champ à l'instant $t$ à l'abscisse $z-\Delta z$ avec $\Delta z=c\,\Delta t>0$. Le profil se translate donc sans déformation vers les $z$ croissants, à la célérité $c$
 : il s'agit d'une **onde plane progressive** se propageant selon $+\vec e_z$ à la vitesse $c$. *Schéma attendu : le profil $E(z)$ tracé à $t$ et à $t+\Delta t$,
 identique et décalé de $\Delta z=c\Delta t$ vers la droite.* $\square$

### Q4

> [!INDICATION]
> Lire chaque propriété sur la phase $\omega(t-z/c)$ et sur la direction fixe de $\vec E$ (attention : direction de propagation et direction de polarisation sont distinctes).

#### Solution

La phase $\varphi=\omega(t-z/c)$ ne dépend spatialement que de $z$ : les surfaces équiphases sont les plans $z=\text{cte}$, l'onde est **plane**. La dépendance temporelle est sinusoïdale à la pulsation unique $\omega$ : l'onde est **harmonique** (monochromatique). Le champ $\vec E=E\,\vec e_x$
 est orthogonal à la direction de propagation $\vec e_z$ : l'onde est **transverse**. Enfin $\vec E$ garde une direction fixe $\vec e_x$ au cours du temps : la polarisation est **rectiligne**. $\square$

### Q5

> [!INDICATION]
> Injecter la solution proposée dans l'équation d'onde et identifier le coefficient de $\vec E$.

#### Solution

Soit $\vec E=E_0\cos(\omega(t-z/c))\,\vec e_x$. Seule la composante $E_x$ dépend de $z$ et de $t$ :

$$
\begin{aligned}
\frac{\partial^2 E_x}{\partial z^2}&=-\frac{\omega^2}{c^2}E_x,\\
\frac{\partial^2\vec E}{\partial t^2}&=-\omega^2\vec E.
\end{aligned}
$$

L'équation d'onde $\Delta\vec E-\mu_0\varepsilon_0\frac{\partial^2\vec E}{\partial t^2}=\vec 0$ donne :

$$
\begin{aligned}
-\frac{\omega^2}{c^2}\vec E-\mu_0\varepsilon_0(-\omega^2)\vec E&=\vec 0\\
\omega^2\!\left(\mu_0\varepsilon_0-\frac{1}{c^2}\right)\vec E&=\vec 0.
\end{aligned}
$$

Cette égalité vaut pour tout $(z,t)$ avec $\omega\neq0$ et $\vec E\neq\vec 0$, donc $\mu_0\varepsilon_0=\frac{1}{c^2}$, soit :

$$
\boxed{c=\frac{1}{\sqrt{\mu_0\varepsilon_0}}.}
$$
$\square$

**A.2 — Le principe de la mesure électrocinétique.**

**A.2.a — Le condensateur.**

> [!JURY]
> « Certaines copies présentent une double erreur de signe qui, par compensation, conduit au résultat attendu ; ces erreurs sont pénalisées. »

### Q6

> [!INDICATION]
> Quels plans sont plans de symétrie de la distribution de charges ? En déduire la direction de $\vec E$, puis son sens (la plaque supérieure, en $z=d$, porte $+Q$).

#### Solution


En négligeant les effets de bord, les plaques sont assimilées à des plans infinis uniformément chargés. Pour un point $M$ quelconque, les deux plans verticaux orthogonaux passant par $M$ sont des plans de symétrie de la distribution. Le champ électrique en $M$ appartient à ces deux plans ; leur intersection est la droite normale aux armatures passant par $M$. **Le champ est donc perpendiculaire aux plaques en tout point.**

Entre les armatures, il est dirigé de la plaque positive ($z=d$) vers la plaque négative ($z=0$), donc selon $-\vec e_z$.

> [!JURY]
> « en électrostatique, il est exact de dire que le champ est “porté par” l’axe Oz ; en revanche, parler de “propagation selon Oz” est incorrect, d’autant que le régime est stationnaire et écarte toute notion de propagation. »

### Q7

> [!INDICATION]
> Modéliser la plaque inférieure comme un plan infini chargé $\sigma=-Q/A_C$ ; choisir une surface de Gauss cylindrique symétrique par rapport au plan.

> [!INDICATION]
> La charge enlacée est $\sigma S$, pas $-Q$ ; distinguer la valeur du champ selon le demi-espace.

#### Solution

Modélisons la plaque inférieure comme un plan infini uniformément chargé, de densité surfacique $\sigma=-Q/A_C$. Par symétrie, son champ s'écrit $\vec E=E(z)\vec e_z$ avec $E(-z)=-E(z)$. Choisissons une **surface de Gauss cylindrique** d'axe $Oz$, de section $S$,
 symétrique par rapport au plan $z=0$ et débouchant en $\pm z$ : seules les deux bases contribuent au flux (le champ est tangent à la surface latérale). Le théorème de Gauss donne :

$$
\begin{aligned}
\Phi=2E(z)S&=\frac{Q_{\text{int}}}{\varepsilon_0}\\
&=\frac{\sigma S}{\varepsilon_0}=\frac{-Q\,S}{\varepsilon_0 A_C},
\end{aligned}
$$

d'où, pour $z>0$ :

$$
\boxed{E(z>0)=-\frac{Q}{2\varepsilon_0 A_C}.}
$$

Pour le plan inférieur seul : $\vec E=-\frac{Q}{2\varepsilon_0 A_C}\vec e_z$ pour $z>0$ et $\vec E=+\frac{Q}{2\varepsilon_0 A_C}\vec e_z$ pour $z<0$ (le champ pointe vers le plan, cohérent avec une charge négative). $\square$

> [!JURY]
> « la définition de la surface fermée adaptée à la distribution de charges est trop souvent imprécise » ; « un tel raccourci conduit inévitablement à un résultat erroné » (charge intérieure prise égale à $-Q$).

### Q8

> [!INDICATION]
> Superposer les champs créés par chaque plan dans les trois zones $z<0$, $0<z<d$, $z>d$.

#### Solution

Le plan supérieur ($\sigma=+Q/A_C$) crée $\vec E=+\frac{Q}{2\varepsilon_0 A_C}\vec e_z$ pour $z>d$ et $\vec E=-\frac{Q}{2\varepsilon_0 A_C}\vec e_z$ pour $z<d$. Par le **principe de superposition**, dans les trois zones :

- $z<0$ : $\vec E=\vec 0$ ;
- $0<z<d$ : $\boxed{\vec E=-\dfrac{Q}{\varepsilon_0 A_C}\vec e_z}$ ;
- $z>d$ : $\vec E=\vec 0$.

Le champ est nul à l'extérieur du condensateur et uniforme entre les armatures. *Schéma attendu : les vecteurs $\vec E$ dans les trois zones $z<0$, $0<z<d$, $z>d$.* $\square$

### Q9

> [!INDICATION]
> Écrire $\vec E=-\overrightarrow{\operatorname{grad}}V$, intégrer $\mathrm dV/\mathrm dz$ entre les armatures, et vérifier le signe de $U$.

#### Solution

Par définition, $Q=C_u\,U$ avec $U=V(z=d)-V(z=0)$. Le champ s'écrit $\vec E=-\overrightarrow{\operatorname{grad}}V$, donc $E_z=-\mathrm dV/\mathrm dz=-\frac{Q}{\varepsilon_0 A_C}$, d'où $\mathrm dV/\mathrm dz=\frac{Q}{\varepsilon_0 A_C}>0$ (potentiel croissant du bas vers le haut, cohérent avec $+Q$ sur la plaque supérieure). Ainsi :

$$
\begin{aligned}
U=V(d)-V(0)&=\int_0^d\frac{Q}{\varepsilon_0 A_C}\,\mathrm dz\\
&=\frac{Qd}{\varepsilon_0 A_C},
\end{aligned}
$$

et :

$$
\boxed{C_u=\frac{\varepsilon_0 A_C}{d}.}
$$
$\square$

> [!JURY]
> « le jury bonifie les candidats vigilants sur l’orientation du champ électrique en lien avec le signe des charges et de la différence de potentiel. »

### Q10

> [!INDICATION]
> En parallèle : mêmes tensions, charges additives.

#### Solution

Les $n$ condensateurs unitaires sont en parallèle : soumis à la même tension $U$, ils portent chacun la charge $Q=C_uU$. La charge totale vaut $Q_{\text{tot}}=nQ=nC_uU$, donc $C_n=Q_{\text{tot}}/U=nC_u$, soit :

$$
\boxed{C_n=\frac{n\,\varepsilon_0 A_C}{d}.}
$$
$\square$

**A.2.b — La bobine.**

### Q11

> [!INDICATION]
> Invariances par rotation autour de $Oz$ et translation selon $Oz$ ; tout plan perpendiculaire à $Oz$ est plan de symétrie des courants.

> [!INDICATION]
> Règle de la main droite pour le sens de $\vec B$.

#### Solution

La distribution de courants est invariante par rotation autour de $Oz$ et par translation selon $Oz$ (solénoïde infini). Tout plan perpendiculaire à $Oz$ est plan de symétrie des courants : $\vec B$, pseudo-vecteur, lui est perpendiculaire, donc $\vec B\parallel\vec e_z$.
 Pour $i>0$, la règle de la main droite donne $\vec B$ selon $+\vec e_z$ à l'intérieur :

$$
\boxed{\vec B\parallel+\vec e_z\ \text{à l'intérieur du solénoïde.}}
$$
$\square$

### Q12

> [!INDICATION]
> Énoncer le théorème d'Ampère en précisant « courants enlacés par le contour ».

#### Solution

**Théorème d'Ampère** (magnétostatique) : la circulation de $\vec B$ le long d'un contour fermé orienté $\mathcal C$ vaut $\mu_0$ fois l'intensité totale des **courants enlacés par le contour** :

$$
\boxed{\oint_{\mathcal C}\vec B\cdot\mathrm d\vec\ell=\mu_0\,I_{\text{enlacé}}.}
$$
$\square$

> [!JURY]
> « il est nécessaire de préciser que les courants pris en compte sont les courants enlacés par le contour d’Ampère, une précision trop fréquemment omise. »

### Q13

> [!INDICATION]
> Quatre étapes : symétries, choix d'un contour rectangulaire, calcul de la circulation, courants enlacés ($Ni$).

#### Solution


Dans le modèle du solénoïde infini, les symétries donnent $\vec B=B_z(r)\vec e_z$, et les invariances imposent l'indépendance en $z$ et en l'angle azimutal. Elles ne suffisent pas, à elles seules, à établir l'indépendance en $r$.

Choisissons d'abord un rectangle d'Ampère dont deux côtés de longueur $\ell'$ sont parallèles à $Oz$, à deux rayons tous deux intérieurs au solénoïde. Aucun courant n'est enlacé entre ces côtés. Les côtés radiaux ne contribuent pas à la circulation ; le théorème d'Ampère donne

$$
\bigl(B_z(r_1)-B_z(r_2)\bigr)\ell'=0.
$$

Le champ est donc uniforme à l'intérieur. Il l'est aussi à l'extérieur, par le même raisonnement. Dans le modèle idéal sans champ extérieur imposé, le champ extérieur est nul.

Prenons maintenant un rectangle avec un côté intérieur de longueur $\ell'$ et l'autre extérieur. Le nombre de spires enlacées est $(N/\ell)\ell'$, de sorte que

$$
B\ell'=\mu_0\frac{N}{\ell}\ell' i.
$$

Le sens est celui obtenu par la règle de la main droite à Q11. Ainsi

$$
\boxed{\vec B=\frac{\mu_0Ni}{\ell}\vec e_z.}
$$

### Q14

> [!INDICATION]
> Le flux propre à travers les $N$ spires est proportionnel à $i$ : c'est la définition de $L$.

#### Solution

Le flux propre du champ magnétique à travers les $N$ spires est proportionnel à l'intensité qui le crée :

$$
\boxed{\Phi=L\,i,}
$$

relation qui **définit** le coefficient d'auto-induction $L$ (inductance propre, en henrys). $\square$

### Q15

> [!INDICATION]
> Flux à travers une spire = $B A_L$ ; à travers les $N$ spires = $N B A_L$ ; identifier à $L i$.

#### Solution

Le flux à travers une spire vaut $B\,A_L=\frac{\mu_0 N i}{\ell}A_L$ ; à travers les $N$ spires, $\Phi=N B A_L=\frac{\mu_0 N^2 A_L}{\ell}i$. Par identification à $\Phi=Li$ :

$$
\boxed{L=\frac{\mu_0 N^2 A_L}{\ell}.}
$$
$\square$

**A.2.c — Le circuit $LC$.**

### Q16

> [!INDICATION]
> Sur $[T_g/2,\,T_g]$ le générateur est nul : maille fermée $L$–$C$.

> [!INDICATION]
> Poser les conventions sur un schéma, écrire la loi des mailles, éliminer $i$ pour obtenir une équation sur $u$.

#### Solution

Sur l'intervalle $[T_g/2,\,T_g]$, la tension du générateur est nulle : le circuit est une maille fermée $L$–$C$. Soit $u$ la tension aux bornes du condensateur (mesurée par l'oscilloscope) et $i$
 l'intensité dans la bobine, avec la convention récepteur pour le condensateur ($i=C\,\mathrm du/\mathrm dt$) et la loi des mailles $L\frac{\mathrm di}{\mathrm dt}+u=0$. En substituant :

$$
\boxed{\frac{\mathrm d^2u}{\mathrm dt^2}+\frac{1}{LC}\,u=0\qquad(t\in[T_g/2,\,T_g]).}
$$
$\square$

> [!JURY]
> « seulement 52 % des copies abordant la question aboutissent à l’équation différentielle demandée. »

> [!METHODE]
> Toujours poser les conventions (schéma fléché) avant d'écrire une loi des mailles ; l'équation doit porter sur la tension $u$ mesurée, pas sur $i$.

### Q17

> [!INDICATION]
> Reconnaître l'oscillateur harmonique de pulsation propre $\omega_0=1/\sqrt{LC}$ ; en déduire la période $T$.

#### Solution

L'équation de Q16 est celle d'un oscillateur harmonique de pulsation propre $\omega_0=\frac{1}{\sqrt{LC}}$ ; sa solution est sinusoïdale, de période :

$$
\boxed{T=\frac{2\pi}{\omega_0}=2\pi\sqrt{LC}.}
$$
$\square$

### Q18

> [!INDICATION]
> Assembler $L$ (Q15) et $C=C_n+C_{osc}$ (Q10) dans $T^2=4\pi^2LC$ ; la structure affine en $n$ apparaît.

#### Solution

Avec $T^2=4\pi^2LC$, $L=\frac{\mu_0 N^2 A_L}{\ell}$ (Q15) et $C=C_n+C_{osc}=\frac{\varepsilon_0 A_C}{d}n+C_{osc}$ (Q10) :

$$
\boxed{T^2=\frac{4\pi^2 N^2 A_L\mu_0}{\ell}\left(\frac{\varepsilon_0 A_C}{d}\,n+C_{osc}\right).}
$$
$\square$

### Q19

> [!INDICATION]
> Identifier la pente $a$ de $T^2=a\,n+b$ à son expression littérale, où $\mu_0\varepsilon_0=1/c^2$ apparaît ; isoler $c$.

> [!INDICATION]
> Application numérique : tenir compte de l'unité de la pente ($\mu\text{s}^2$) et des chiffres significatifs.

#### Solution

La pente de la droite $T^2=a\,n+b$ s'identifie à :

$$
a=\frac{4\pi^2 N^2 A_L\mu_0\varepsilon_0 A_C}{\ell d}=\frac{4\pi^2 N^2 A_L A_C}{\ell d\,c^2},
$$

d'où $c=\sqrt{\frac{4\pi^2 N^2 A_L A_C}{\ell d\,a}}$. Application numérique : $a=34{,}1~\mu\text{s}^2=34{,}1\times10^{-12}~\text{s}^2$, $A_L=\pi R_L^2=\pi(0{,}025)^2=1{,}96\times10^{-3}~\text{m}^2$, $A_C=0{,}067~\text{m}^2$, $\ell=0{,}19~\text{m}$,
 $d=3\times10^{-3}~\text{m}$, $N=700$, donc :

$$
c=\sqrt{\frac{4\pi^2(700)^2(1{,}96\times10^{-3})(0{,}067)}{(0{,}19)(3\times10^{-3})(34{,}1\times10^{-12})}}\approx\boxed{3{,}6\times10^{8}~\text{m}\cdot\text{s}^{-1}.}
$$
$\square$

> [!JURY]
> « Il faut également tenir compte de l’unité du coefficient directeur de la droite utilisé pour faire le calcul de c. »

### Partie B — Cavité cylindrique : Essen & Gordon-Smith (1948)

### Q20

> [!INDICATION]
> De Q19, $c\propto d^{-1/2}$ : propager l'incertitude avec le facteur $\tfrac12$.

> [!INDICATION]
> Calculer l'écart normalisé $z=|c-c_{\text{réf}}|/u(c)$, pas l'écart relatif.

#### Solution

De Q19, $c\propto d^{-1/2}$, donc la propagation des incertitudes donne $\frac{u(c)}{c}=\frac12\frac{u(d)}{d}$. Avec $u(d)=1~\text{mm}$ et $d=3~\text{mm}$ :

$$
\frac{u(c)}{c}=\frac12\times\frac13\approx0{,}17,
$$

soit $u(c)\approx0{,}17\times3{,}6\times10^8\approx0{,}6\times10^8~\text{m}\cdot\text{s}^{-1}$. On écrit $c=(3{,}6\pm0{,}6)\times10^8~\text{m}\cdot\text{s}^{-1}$. L'écart normalisé (z-score) à la valeur de référence $c_{\text{réf}}=2{,}998\times10^8~\text{m}\cdot\text{s}^{-1}$ vaut :

$$
\begin{aligned}
z&=\frac{|c-c_{\text{réf}}|}{u(c)}\\
&=\frac{|3{,}6-3{,}0|\times10^8}{0{,}6\times10^8}\approx1{,}0.
\end{aligned}
$$

$z<2$ : la mesure est **compatible** avec la valeur admise. $\square$

> [!JURY]
> « Le 2 est souvent oublié dans la formule de propagation des incertitudes. L’écart normalisé (ou z-score) est parfois confondu avec l’écart relatif. »

> [!PIEGE]
> Oublier le facteur $\tfrac12$ dans la propagation de $u(d)$ sur $c\propto d^{-1/2}$, ou confondre z-score et écart relatif.

### Q21

> [!INDICATION]
> La composante tangentielle de $\vec E$ s'annule sur une paroi métallique : traduire sur $E_0(a)$, $g(0)$, $g(h)$.

#### Solution

Le champ $\vec E=E_0(r)g(z)e^{i\omega t}\vec e_\theta$ est tangentiel aux trois parois métalliques, où sa composante tangentielle s'annule. Sur la paroi latérale $r=a$, $\vec e_\theta$ est tangent, d'où $E_0(a)=0$. Sur les bases $z=0$
 et $z=h$, $\vec e_\theta$ est aussi tangent, d'où $g(0)=0$ et $g(h)=0$. $\square$

### Q22

> [!INDICATION]
> Partir de l'équation d'onde du vide (Q2) avec le laplacien cylindrique fourni ; substituer la forme $E_0(r)g(z)e^{i\omega t}$.

#### Solution

Le champ vérifie l'équation d'onde du vide (Q2, avec $\mu_0\varepsilon_0=1/c^2$) : $\Delta\vec E-\frac{1}{c^2}\frac{\partial^2\vec E}{\partial t^2}=\vec 0$. Avec le laplacien cylindrique fourni et $\frac{\partial^2\vec E}{\partial t^2}=-\omega^2\vec E$, l'EDP vérifiée par $\underline E(r,z,t)=E_0(r)g(z)e^{i\omega t}$ est :

$$
\frac{\partial^2\underline E}{\partial r^2}+\frac{\partial^2\underline E}{\partial z^2}+\frac1r\frac{\partial\underline E}{\partial r}-\frac{\underline E}{r^2}+\frac{\omega^2}{c^2}\underline E=0.
$$

En substituant $\underline E=E_0(r)g(z)e^{i\omega t}$ et en divisant par $e^{i\omega t}$ :

$$
g\,E_0''+E_0\,g''+\frac{g}{r}E_0'-\frac{E_0 g}{r^2}+\frac{\omega^2}{c^2}E_0 g=0.
$$
$\square$

### Q23

> [!INDICATION]
> Diviser par $E_0 g$ : chaque membre ne dépend que d'une variable, donc est une constante $\beta$.

> [!INDICATION]
> Signe de $\beta$ : utiliser les conditions aux limites de Q21, pas une simple affirmation.

#### Solution

En divisant par $E_0 g$ :

$$
\underbrace{\frac{E_0''}{E_0}+\frac1r\frac{E_0'}{E_0}-\frac{1}{r^2}+\frac{\omega^2}{c^2}}_{\text{fonction de }r\text{ seul}}=\underbrace{-\frac{g''}{g}}_{\text{fonction de }z\text{ seul}}.
$$

Une fonction de $r$ seul égale à une fonction de $z$ seul est nécessairement **constante**. En posant $\frac{g''}{g}=\beta$ :

$$
\boxed{\frac{\mathrm d^2g}{\mathrm dz^2}=\beta\,g.}
$$

Si $\beta\geq0$, les solutions (exponentielles ou affine) ne peuvent s'annuler en $z=0$ **et** en $z=h$ qu'en étant identiquement nulles, ce qui est exclu ($g\not\equiv0$). Les conditions aux limites de Q21 imposent donc :

$$
\boxed{\beta<0.}
$$
$\square$

> [!JURY]
> « Dans de nombreuses copies, β est identifié à une expression dépendant de r sans avoir montré que β est bien constante. »

### Q24

> [!INDICATION]
> Poser $\beta=-k^2$ ; résoudre $g''=-k^2g$ avec $g(0)=g(h)=0$ : la quantification $k=p\pi/h$ vient des conditions aux limites (comme la corde de Melde).

#### Solution

Posons $\beta=-k^2$ avec $k>0$ : $g(z)=A\sin(kz)+B\cos(kz)$. La condition $g(0)=0$ donne $B=0$
 ; la condition $g(h)=0$ donne $\sin(kh)=0$, soit $kh=p\pi$ avec $p\in\mathbb N^*$. Les modes autorisés sont :

$$
\boxed{g_p(z)=A_p\sin\!\left(\frac{p\pi z}{h}\right),\quad p\in\mathbb N^*.}
$$
$\square$

### Q25

> [!INDICATION]
> Reprendre la séparation de Q23 : le membre radial vaut $-\omega^2/c^2+k^2$.

#### Solution

D'après la séparation de Q23, le membre radial vaut $-\frac{\omega^2}{c^2}-\beta=-\frac{\omega^2}{c^2}+k^2=-\frac{\omega^2}{c^2}+\frac{p^2\pi^2}{h^2}$. L'équation vérifiée par $E_0$ est donc :

$$
\boxed{\frac{\mathrm d^2E_0}{\mathrm dr^2}+\frac1r\frac{\mathrm dE_0}{\mathrm dr}-\frac{E_0(r)}{r^2}=E_0(r)\left(\frac{p^2\pi^2}{h^2}-\frac{\omega^2}{c^2}\right).}
$$
$\square$

### Q26

> [!INDICATION]
> Signaler la coquille de l'énoncé et poursuivre.

> [!INDICATION]
> Adimensionner par $x=\kappa r$ avec $\kappa^2=\omega^2/c^2-p^2\pi^2/h^2$ pour obtenir l'équation de Bessel d'ordre 1.

#### Solution


**Coquille de l'énoncé.** Dans la forme imprimée, le terme de dérivée première est $x^{-1}\tilde E_0'$. Lorsque le coefficient de $\tilde E_0''$ est $x^2$, le coefficient correct de $\tilde E_0'$ est **$x$**. La forme divisée par $x^2$ comporterait, elle, $x^{-1}\tilde E_0'$.

Posons

$$
\kappa=\sqrt{\frac{\omega^2}{c^2}-\frac{p^2\pi^2}{h^2}},
\qquad x=\kappa r,
\qquad \tilde E_0(x)=E_0(r).
$$

Les dérivées se transforment selon $E_0'(r)=\kappa\tilde E_0'(x)$ et $E_0''(r)=\kappa^2\tilde E_0''(x)$. L'équation Q25 devient

$$
\kappa^2\tilde E_0''+\frac{\kappa}{r}\tilde E_0'-\frac{\tilde E_0}{r^2}=-\kappa^2\tilde E_0.
$$

En multipliant par $r^2$ et en utilisant $x=\kappa r$, on obtient bien l'équation de Bessel d'ordre 1 :

$$
\boxed{x^2\tilde E_0''+x\tilde E_0'+(x^2-1)\tilde E_0=0.}
$$

> [!JURY]
> « Le jury a accordé des points à toute tentative de raisonnement, même incomplète, dès lors que le candidat manifeste une gêne ou une interrogation face à cette erreur » (la coquille porte sur le deuxième terme : « le x est au numérateur et non au dénominateur »).

### Q27

> [!INDICATION]
> La solution régulière en $r=0$ est $J_1(x)$.

> [!INDICATION]
> La condition $E_0(a)=0$ impose $J_1(\kappa a)=0$ : $\kappa a$ est un zéro $x_n$ de $J_1$, lu sur la figure 6.

#### Solution

La solution régulière en $r=0$ est $\tilde E_0(x)=J_1(x)$. La condition $E_0(a)=0$ (Q21) impose $J_1(\kappa a)=0$ : $\kappa a$
 doit être un **zéro de $J_1$**. En notant $x_n$ le $n$-ième zéro de $J_1$ ($x_1=3{,}832$,
 $x_2=7{,}016$, …), on a $\kappa a=x_n$, $n\in\mathbb N^*$ : seuls les modes $E_{0,n}$ existent. $\square$

### Q28

> [!INDICATION]
> Assembler Q24 et Q27 : produit de $J_1(x_n r/a)$, $\sin(p\pi z/h)$ et $e^{i\omega t}$, dirigé selon $\vec e_\theta$.

#### Solution

Pour le mode $(n,p)$, $\kappa=x_n/a$ donne $E_0(r)=J_1(\frac{x_n r}{a})$ et $g(z)=\sin(\frac{p\pi z}{h})$. À une constante multiplicative $K$ près :

$$
\boxed{\underline E_{n,p}(r,z,t)=K\,J_1\!\left(\frac{x_n r}{a}\right)\sin\!\left(\frac{p\pi z}{h}\right)e^{i\omega t}\,\vec e_\theta.}
$$
$\square$

### Q29

> [!INDICATION]
> De $\kappa=x_n/a$ et $\kappa^2=\omega^2/c^2-p^2\pi^2/h^2$, tirer $\omega$ puis $f$.

#### Solution

De $\kappa=x_n/a$ et $\kappa^2=\frac{\omega^2}{c^2}-\frac{p^2\pi^2}{h^2}$ :

$$
\frac{\omega^2}{c^2}=\frac{x_n^2}{a^2}+\frac{p^2\pi^2}{h^2}.
$$

Avec $\omega=2\pi f$, la fréquence du mode $(n,p)$ s'écrit :

$$
\boxed{f_{n,p}=c\sqrt{\frac{x_n^2}{4\pi^2 a^2}+\frac{p^2}{4h^2}}.}
$$
$\square$

### Partie C — Battements des modes longitudinaux d'un laser He-Ne : D'Orazio *et al.* (2010)

### Q30

> [!INDICATION]
> Inverser la relation donnant $f_{1,1}$ pour obtenir $c$ ; les données ont 4 chiffres significatifs.

#### Solution

Pour le mode $(1,1)$ : $x_1=3{,}832$, $a=\frac{7{,}398}{2}=3{,}699~\text{cm}=0{,}03699~\text{m}$, $h=8{,}558~\text{cm}=0{,}08558~\text{m}$, $f_{1,1}=5{,}244~\text{GHz}$. Alors :

$$
\begin{aligned}
c&=\frac{f_{1,1}}{\sqrt{\frac{x_1^2}{4\pi^2 a^2}+\frac{1}{4h^2}}}\\
&=\frac{5{,}244\times10^9}{\sqrt{271{,}8+34{,}13}}\\
&=\frac{5{,}244\times10^9}{17{,}49}\\ 
&\approx\boxed{2{,}998\times10^8~\text{m}\cdot\text{s}^{-1}.}
\end{aligned}
$$
$\square$

> [!JURY]
> « Il faut ici être extrêmement vigilant sur le nombre de chiffres significatifs à donner dans la réponse. Le nombre de chiffres significatifs dans les données de l’énoncé ne laissent aucune place au doute. »

### Q31

> [!INDICATION]
> Condition de résonance sur le déphasage d'un aller-retour (chemin optique $2n_{air}L_c$) ; ne pas oublier l'indice de l'air.

#### Solution

Une onde faisant un aller-retour dans la cavité parcourt le chemin optique $2n_{air}L_c$ ; la résonance impose un déphasage multiple de $2\pi$, soit $2n_{air}L_c=m\lambda$, $m\in\mathbb N$. D'où :

$$
\boxed{\lambda=\frac{2n_{air}L_c}{m}.}
$$

$$
\boxed{f_m=\frac{c}{\lambda}=\frac{m\,c}{2n_{air}L_c}.}
$$
$\square$

> [!JURY]
> « L’indice de l’air est très souvent oublié dans l’expression de f_m ; or, c’est bien la prise en compte précise de l’indice de l’air qui permettra, in fine, de gagner quelques chiffres significatifs. »

### Q32

> [!INDICATION]
> Développer $s^2$ en linéarisant aussi les $\cos^2$ ; lister toutes les fréquences du spectre.

#### Solution

$s(t)^2=E_q^2\cos^2(2\pi f_q t)+E_{q+1}^2\cos^2(2\pi f_{q+1}t)+2E_qE_{q+1}\cos(2\pi f_q t)\cos(2\pi f_{q+1}t)$. En linéarisant aussi les $\cos^2$ ($\cos^2 a=\frac12(1+\cos2a)$) et le produit de cosinus :

$$
s(t)^2=\frac{E_q^2+E_{q+1}^2}{2}+\frac{E_q^2}{2}\cos(4\pi f_q t)+\frac{E_{q+1}^2}{2}\cos(4\pi f_{q+1}t)+E_qE_{q+1}\big[\cos(2\pi(f_q{+}f_{q+1})t)+\cos(2\pi(f_{q+1}{-}f_q)t)\big].
$$

Spectre de $s(t)^2$ : $\{0,\ 2f_q,\ 2f_{q+1},\ f_q+f_{q+1},\ f_{q+1}-f_q\}$. $\square$

### Q33

> [!INDICATION]
> La moyenne sur $\tau_d$ filtre les hautes fréquences ; relier chaque inégalité sur $\tau_d$ à la fréquence conservée ou éliminée.

#### Solution

$I(t)=\langle s^2\rangle_{\tau_d}$. Comme $\tau_d\gg\frac{1}{f_q},\frac{1}{f_{q+1}},\frac{1}{f_q+f_{q+1}}$, les termes à $2f_q$, $2f_{q+1}$ et $f_q+f_{q+1}$
 oscillent de nombreuses fois sur $\tau_d$ : leur moyenne est nulle. En revanche $\tau_d\ll\frac{1}{f_{q+1}-f_q}$ : le terme de battement est quasi constant sur $\tau_d$ et subsiste. D'où :

$$
I(t)=\frac{E_q^2+E_{q+1}^2}{2}+E_qE_{q+1}\cos\!\big(2\pi(f_{q+1}-f_q)t\big).
$$

Seule fréquence non nulle du spectre de $I$ :

$$
\boxed{f_b=f_{q+1}-f_q.}
$$
$\square$

### Q34

> [!INDICATION]
> $f_b=f_{q+1}-f_q$ avec $f_m=mc/(2n_{air}L_c)$ : le $m$ se simplifie.

#### Solution

D'après Q31, $f_{q+1}-f_q=\frac{(q+1)c}{2n_{air}L_c}-\frac{qc}{2n_{air}L_c}$, d'où :

$$
\boxed{f_b=\frac{c}{2n_{air}L_c}.}
$$
$\square$

### Q35

> [!INDICATION]
> L'énoncé fournit $\Delta L_c$ et non $L_c$ : poser $L_c=L_{c0}+\Delta L_c$ et tracer $1/f_b$ en fonction de $\Delta L_c$ ; la pente vaut $2n_{air}/c$.

#### Solution

L'énoncé fournit $\Delta L_c$ et non $L_c$ : posons $L_c=L_{c0}+\Delta L_c$. De Q34 :

$$
\frac{1}{f_b}=\frac{2n_{air}}{c}L_c=\frac{2n_{air}}{c}(L_{c0}+\Delta L_c),
$$

soit $\frac{1}{f_b}=\frac{2n_{air}}{c}\Delta L_c+\frac{2n_{air}L_{c0}}{c}$ : on trace $\frac{1}{f_b}$ (en s) en fonction de $\Delta L_c$ (en m) ; la pente vaut $s=\frac{2n_{air}}{c}$, indépendante de $L_{c0}$ inconnu.

| $\Delta L_c$ (mm) | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|---|---|---|---|---|---|---|---|
| $1/f_b$ (ns) | 2,6858 | 2,6924 | 2,6991 | 2,7058 | 2,7125 | 2,7191 | 2,7258 |

La régression linéaire donne $s=6{,}673\times10^{-9}~\text{s}\cdot\text{m}^{-1}$, d'où :

$$
\begin{aligned}
c=\frac{2n_{air}}{s}&=\frac{2\times1{,}00024}{6{,}673\times10^{-9}}\\
&\approx\boxed{2{,}9978\times10^8~\text{m}\cdot\text{s}^{-1}.}
\end{aligned}
$$

C'est la mesure la plus précise des trois (cinq chiffres significatifs), en excellent accord avec $c=2{,}99792458\times10^8~\text{m}\cdot\text{s}^{-1}$. *Schéma attendu : nuage $(\Delta L_c, 1/f_b)$ aligné, de pente $2n_{air}/c$.* $\square$

> [!JURY]
> « C’est à cette question que le résultat de la mesure de c est obtenu avec la plus grande précision (cinq chiffres significatifs sont attendus et, là encore, pas les neuf donnés par la calculatrice). »

## MINEURE CHIMIE (6 points)

### Partie A — Étude du nettoyage de l'argenterie

### Q1

> [!INDICATION]
> $A$ = nombre de nucléons (nombre de masse) ; $Z$ = numéro atomique (nombre de protons).

#### Solution

$A=108$ est le **nombre de masse** de l'atome d'argent (nombre de nucléons) ; $Z=47$ est le **numéro atomique** (nombre de charge, c'est-à-dire le nombre de protons, égal au nombre d'électrons de l'atome neutre). $\square$

### Q2

> [!INDICATION]
> Le soufre a 6 électrons de valence : 2 liaisons et 2 doublets non liants ; VSEPR $AX_2E_2$.

> [!INDICATION]
> Justifier la forme coudée par la répulsion électronique entre doublets.

#### Solution


Le soufre possède six électrons de valence. Il forme deux liaisons simples S–H et conserve **deux doublets non liants** :

```text
    ..
H — S — H
    ..
```

La répartition est de type $AX_2E_2$ : quatre domaines électroniques autour du soufre, dont deux doublets non liants. La molécule est donc **coudée**, et non linéaire.

### Q3

> [!INDICATION]
> Équilibrer élément par élément (Ag, H, S, O).

#### Solution

Équation [1] : $4\,\text{Ag}+2\,\text{H}_2\text{S}+\text{O}_2=a\,\text{Ag}_2\text{S}+b\,\text{H}_2\text{O}$. Ag : $4=2a$ donc $a=2$ ; H : $4=2b$ donc $b=2$
 ; on vérifie S ($2=a$) et O ($2=b$). D'où :

$$
\boxed{a=2,\ b=2.}
$$
$\square$

### Q4

> [!INDICATION]
> $2~\text{ppm}=2\times10^{-6}$ en fraction molaire ; calculer $Q_r$ et comparer à $K°$.

#### Solution

Fractions molaires : $x(\text{H}_2\text{O})=0{,}010$, $x(\text{O}_2)=0{,}209$, $x(\text{H}_2\text{S})=2~\text{ppm}=2\times10^{-6}$. Le quotient de réaction vaut :

$$
\begin{aligned}
Q_r&=\frac{x(\text{H}_2\text{O})^2}{x(\text{H}_2\text{S})^2\,x(\text{O}_2)}\\
&=\frac{(0{,}010)^2}{(2\times10^{-6})^2\times0{,}209}\\
&=\frac{10^{-4}}{8{,}36\times10^{-13}}\\
&\approx1{,}2\times10^{8}.
\end{aligned}
$$

$Q_r\approx10^8\ll K°=10^{140}$ : le système évolue dans le **sens direct** (formation de Ag₂S) ; l'argent se ternit spontanément. $\square$

> [!JURY]
> « Le terme de “ppm” (ou partie par million) est parfois incompris. »

### Q5

> [!INDICATION]
> Couples $\text{Ag}_2\text{S}/\text{Ag}$ et $\text{Al(OH)}_3/\text{Al}$ ; demi-équations en milieu acide, dans l'ordre oxydant/réducteur.

#### Solution

Couples mis en jeu : $\text{Ag}_2\text{S}(\text{s})/\text{Ag}(\text{s})$ et $\text{Al(OH)}_3(\text{s})/\text{Al}(\text{s})$. Demi-équations en milieu acide, dans l'ordre oxydant/réducteur :

$$
\begin{aligned}
\text{Ag}_2\text{S}(\text{s})+2\,\text{H}^+(\text{aq})+2\,e^-&=2\,\text{Ag}(\text{s})+\text{H}_2\text{S}(\text{aq})\\
\text{Al}(\text{s})+3\,\text{H}_2\text{O}(\ell)&=\text{Al(OH)}_3(\text{s})+3\,\text{H}^+(\text{aq})+3\,e^-.
\end{aligned}
$$
$\square$

### Q6

> [!INDICATION]
> Al : $Z=13$, configuration $1s^2 2s^2 2p^6 3s^2 3p^1$ ; ion le plus stable $\text{Al}^{3+}$.

#### Solution

Aluminium ($Z=13$) : $1s^2\,2s^2\,2p^6\,3s^2\,3p^1$ ; électrons de valence $3s^2\,3p^1$. L'ion le plus stable est $\text{Al}^{3+}$ (perte des trois électrons de valence), de configuration $1s^2\,2s^2\,2p^6$ (celle du néon). $\square$

### Q7

> [!INDICATION]
> Contact direct des deux solides = pile en court-circuit : Al s'oxyde (anode, pôle $-$), Ag₂S se réduit (cathode, pôle $+$).

#### Solution

C'est une pile en court-circuit (contact direct des deux solides, sans fils). L'aluminium, réducteur le plus fort, s'oxyde : c'est l'**anode** (pôle $-$). Le sulfure d'argent se réduit à la surface de l'objet en argent : c'est la **cathode** (pôle $+$). Les électrons circulent dans le métal de l'anode (Al) vers la cathode (objet en Ag) ; le courant circule en sens inverse. *Schéma attendu : feuille d'Al et objet en Ag en contact dans la solution de NaCl, flèche $e^-$ de Al vers Ag.* $\square$

> [!JURY]
> « il n’y a, par exemple, pas de fils électriques reliant les deux électrodes (qui sont en contact direct). »

### Q8

> [!INDICATION]
> Le sel est l'électrolyte : conduction ionique dans la solution, sans être consommé.

#### Solution

Le sel $(\text{Na}^+,\text{Cl}^-)$ joue le rôle d'**électrolyte** : il assure la conduction ionique dans la solution (fermeture du circuit), sans être consommé par la réaction [2]. La dénomination « bain de sel » est donc partiellement trompeuse : le nettoyage résulte d'une réaction électrochimique, le sel n'étant qu'un porteur de charges en solution. $\square$

> [!JURY]
> « De nombreuses copies passent à côté du fait que le sel sert d’électrolyte et n’est pas consommé par la réaction. »

### Partie B — Dosage de l'urée

### Q9

> [!INDICATION]
> L'eau chaude agit comme facteur cinétique (loi d'Arrhenius), pas comme un effet de solubilité.

#### Solution

L'eau chaude agit essentiellement comme **facteur cinétique** : l'élévation de température accroît la vitesse de la réaction (loi d'Arrhenius) et accélère le nettoyage ; elle augmente aussi la mobilité des ions, donc la conductivité de l'électrolyte. $\square$

### Q10

> [!INDICATION]
> Règle systématique : un doublet non liant par atome de N, deux par atome de O.

#### Solution

Sur la figure 1 complétée : chaque atome d'azote porte **un** doublet non liant ; chaque atome d'oxygène porte **deux** doublets non liants (C=O du diacétylmonoxime, N–O**H** de l'oxime, deux C=O de l'urée et de la triazine, hydroxylamine $\text{H}_2\text{N}$–O**H** formée). $\square$

### Q11

> [!INDICATION]
> Loi de Beer-Lambert $A=\varepsilon\ell c$ : nommer chaque facteur et donner son unité.

#### Solution

**Loi de Beer-Lambert** : $A=\varepsilon\,\ell\,c$, où $A$ est l'absorbance (sans unité), $\varepsilon$ le coefficient d'absorption molaire ($\text{L}\cdot\text{mol}^{-1}\cdot\text{cm}^{-1}$), $\ell$
 la longueur de la cuve ($\text{cm}$) et $c$ la concentration en triazine ($\text{mol}\cdot\text{L}^{-1}$). Valable en solution diluée, à $\lambda$ fixée. $\square$

> [!JURY]
> « La version A = kC vue en classe de première ne suffit pas. »

### Q12

> [!INDICATION]
> Dosage par étalonnage : faire le blanc, régler $\lambda$, préparer une gamme de solutions colorées (triazine), tracer $A=f(c)$.

#### Solution

Dosage par étalonnage à $\lambda=520~\text{nm}$ :

1. Préparer une **gamme étalon de triazine** : solutions d'urée de concentrations connues, traitées par le diacétylmonoxime en excès en milieu acide et chauffées (l'urée seule, incolore, ne peut être dosée directement) ;
2. régler le spectrophotomètre sur $\lambda=520~\text{nm}$ et faire le **blanc** (réactifs sans urée) ;
3. mesurer $A$ pour chaque étalon et tracer la droite d'étalonnage $A=f(c)$ ;
4. traiter l'échantillon dans les mêmes conditions, mesurer son $A$ et lire $c$ sur la droite. $\square$

> [!JURY]
> « il est essentiel de ne pas omettre de faire le blanc et de régler la longueur d’onde utilisée pour la mesure d’absorbance. »

### Q13

> [!INDICATION]
> Un catalyseur abaisse l'énergie d'activation, n'est pas consommé, et ne change ni $K°$ ni le rendement.

#### Solution

Un catalyseur accélère la réaction en abaissant l'énergie d'activation, sans figurer dans le bilan et sans être consommé ; il ne modifie **pas** la thermodynamique (ni la constante d'équilibre, ni le rendement). L'uréase est ici un catalyseur enzymatique, spécifique. $\square$

> [!PIEGE]
> Écrire qu'un catalyseur « augmente le rendement » : il ne change que la cinétique, pas la thermodynamique.

### Q14

> [!INDICATION]
> $\text{NH}_4^+$ est un acide : c'est l'ion carbonate $\text{CO}_3^{2-}$ (dibase) qui réagit avec $\text{H}^+$ en excès.

> [!INDICATION]
> Justifier la quantitativité par $K°=1/(K_{a1}K_{a2})\gg1$.

#### Solution

$\text{NH}_4^+$ est un **acide** (couple $\text{NH}_4^+/\text{NH}_3$) : il ne réagit pas avec l'acide fort. C'est l'ion carbonate $\text{CO}_3^{2-}$ (dibase) qui réagit ; l'acide étant en excès, la réaction va jusqu'à $\text{CO}_2$ :

$$
\text{CO}_3^{2-}(\text{aq})+2\,\text{H}^+(\text{aq})=\text{CO}_2(\text{aq})+\text{H}_2\text{O}(\ell).
$$

Avec $K_{a1}(\text{CO}_2/\text{HCO}_3^-)=10^{-6{,}4}$ et $K_{a2}(\text{HCO}_3^-/\text{CO}_3^{2-})=10^{-10{,}3}$, la constante de cette réaction vaut :

$$
\begin{aligned}
K°&=\frac{1}{K_{a1}K_{a2}}\\
&=10^{6{,}4+10{,}3}=10^{16{,}7}\\
&\approx5\times10^{16}\gg1.
\end{aligned}
$$

La réaction est donc quantitative. $\square$

> [!JURY]
> « NH₄⁺ est un acide (et non une base) : ce n’est donc pas lui qui réagit avec l’acide fort. » ; « il est attendu des candidats qu’ils calculent la valeur de la constante d’équilibre K° associée à la réaction acide-base de l’ion carbonate avec l’acide fort en excès […] puis de constater que K° ≫ 1 pour conclure. »

### Q15

> [!INDICATION]
> Un monoacide fort qui ne réagit pas avec les ions présents : l'acide chlorhydrique $(\text{H}^+, \text{Cl}^-)$.

#### Solution

L'acide **chlorhydrique** $(\text{H}^+,\text{Cl}^-)$ convient : monoacide fort, ne réagissant pas avec les ions en jeu (l'acide nitrique conviendrait aussi). $\square$

### Q16

> [!INDICATION]
> Hydrolyse : 1 urée $\to 2\,\text{NH}_4^+ + \text{CO}_3^{2-}$ ; puis tableau d'avancement de $\text{CO}_3^{2-}+2\text{H}^+\to\text{CO}_2+\text{H}_2\text{O}$.

#### Solution

Soit $n_0=C_0V_0$ la quantité initiale d'urée. L'hydrolyse (catalysée par l'uréase) donne $1$ urée $\to 2\,\text{NH}_4^+ + \text{CO}_3^{2-}$, donc $n(\text{NH}_4^+)=2C_0V_0$ et $n(\text{CO}_3^{2-})=C_0V_0$.
 On ajoute $n(\text{H}^+)=CV_a$ (en excès). Tableau d'avancement de $\text{CO}_3^{2-}+2\,\text{H}^+\to\text{CO}_2+\text{H}_2\text{O}$ (carbonate limitant) :

| | $\text{CO}_3^{2-}$ | $\text{H}^+$ | $\text{CO}_2$ | $\text{NH}_4^+$ |
|---|---|---|---|---|
| état initial | $C_0V_0$ | $CV_a$ | $0$ | $2C_0V_0$ |
| état final | $0$ | $CV_a-2C_0V_0$ | $C_0V_0$ | $2C_0V_0$ |

Avant dosage, la solution contient $CV_a-2C_0V_0$ mol de $\text{H}^+$ en excès, $C_0V_0$ mol de $\text{CO}_2$ et $2C_0V_0$
 mol de $\text{NH}_4^+$. $\square$

### Q17

> [!INDICATION]
> Dosage en retour : la soude titre l'excès d'acide fort, pas l'urée.

> [!INDICATION]
> À l'équivalence : $C_bV_{eq}=CV_a-2C_0V_0$ ; conclure sur le caractère normal ou non de la teneur.

#### Solution

Dosage **en retour** : la soude titre l'excès d'acide fort (et non l'urée). Le rouge de méthyle (virage $4{,}4$–$6{,}2$) repère l'équivalence acide fort/base forte, avant toute réaction de $\text{NH}_4^+$ ($\text{p}K_a=9{,}2$). À l'équivalence, $C_bV_{eq}=CV_a-2C_0V_0$, donc :

$$
\begin{aligned}
2C_0V_0&=CV_a-C_bV_{eq}\\
&=(0{,}010\times30)-(0{,}010\times10{,}2)\\
&=0{,}300-0{,}102=0{,}198~\text{mmol},\\
C_0V_0&=0{,}099~\text{mmol},\\
C_0&=\frac{0{,}099}{25}\\ 
&\approx\boxed{3{,}96\times10^{-3}~\text{mol}\cdot\text{L}^{-1}=3{,}96~\text{mmol}\cdot\text{L}^{-1}.}
\end{aligned}
$$

**Conclusion.** $C_0\approx4{,}0~\text{mmol}\cdot\text{L}^{-1}$ est inférieur au seuil pathologique de l'adulte ($8{,}3~\text{mmol}\cdot\text{L}^{-1}$, et au seuil nourrisson $4{,}2~\text{mmol}\cdot\text{L}^{-1}$) : pour un adulte, la teneur en urée est **normale**. $\square$

> [!JURY]
> « Le principe indirect du dosage ici réalisé est très peu compris. Toute prise d’initiative quant à la détermination des concentrations est valorisée. »

> [!METHODE]
> Sécuriser le calcul par un schéma des trois quantités d'acide : total versé $CV_a$, consommé par le carbonate $2C_0V_0$, dosé en retour $C_bV_{eq}$.

## Bilan

**Méthodes à retenir.**

- **Ondes électromagnétiques dans le vide** : à partir de Maxwell, obtenir les équations d'onde pour $\vec E$ et $\vec B$ (les rédiger toutes les deux), puis identifier $c=1/\sqrt{\mu_0\varepsilon_0}$ sur une solution harmonique plane.
- **Électrostatique / magnétostatique** : symétries → surface ou contour adapté → théorème de Gauss ou d'Ampère (préciser « courants enlacés ») → champ ; superposition pour le condensateur ; $B=\mu_0 Ni/\ell$ et $L=\mu_0 N^2 A_L/\ell$ pour le solénoïde.
- **Circuit $LC$** : poser les conventions, obtenir $\ddot u+u/(LC)=0$, $T=2\pi\sqrt{LC}$, puis exploiter la droite $T^2=a\,n+b$ pour remonter à $c$ — en tenant compte de l'unité de la pente.
- **Incertitudes** : propagation d'une incertitude relative avec le bon facteur ($c\propto d^{-1/2}$ donne $\tfrac12$), puis écart normalisé $z=|c-c_{\text{réf}}|/u(c)$ ; 1-2 chiffres significatifs pour $u(c)$, cohérence des chiffres du résultat.
- **Cavité cylindrique** : séparation des variables $\vec E=E_0(r)g(z)e^{i\omega t}\vec e_\theta$, conditions aux limites métalliques, $\beta=-k^2<0$, quantification axiale $k=p\pi/h$ et radiale $\kappa a=x_n$ (zéros de $J_1$), d'où $f_{n,p}$.
- **Battements** : linéariser complètement $s^2$ (y compris les $\cos^2$), filtrer par la moyenne sur $\tau_d$, $f_b=c/(2n_{air}L_c)$ ; exploiter $1/f_b$
 linéaire en $\Delta L_c$ pour obtenir $c$ avec cinq chiffres significatifs.
- **Chimie** : pile en court-circuit (anode Al, cathode Ag₂S, sel = électrolyte non consommé) ; quotient de réaction et sens d'évolution ; dosage colorimétrique (Beer-Lambert, gamme de triazine, blanc) ; dosage pH-métrique en retour ($C_bV_{eq}=CV_a-2C_0V_0$).

**Pièges signalés par le rapport de la session 2026.** Égalités entre grandeurs vectorielles et scalaires ; « de même pour $\vec B$ » non rédigé ; double erreur de signe compensée ; « propagation selon $Oz$ » en électrostatique ; charge enlacée de Gauss prise égale à $-Q$ ; courant enlacé d'Ampère non précisé ; équation du circuit $LC$ écrite sur $i$
 au lieu de $u$ ; facteur 2 oublié dans la propagation des incertitudes ; z-score confondu avec l'écart relatif ; $\beta$ non montré constant dans la séparation des variables ; coquille de la Q26 non signalée ; indice de l'air oublié ; chiffres significatifs non maîtrisés ; en chimie : ppm incompris, sel confondu avec un réactif, catalyseur confondu avec un gain de rendement, $\text{NH}_4^+$ pris pour une base, principe du dosage en retour non compris.

**Pré-requis à revoir.** Équations de Maxwell et identité du double rotationnel ; théorèmes de Gauss et d'Ampère ; oscillateur harmonique ; séparation des variables et équation de Bessel ; propagation des incertitudes et écart normalisé ; loi de Beer-Lambert ; tableaux d'avancement et dosage en retour.
