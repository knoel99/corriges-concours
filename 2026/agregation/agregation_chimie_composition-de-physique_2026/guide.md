# Agrégation Chimie — Composition de physique 2026 · Corrigé guidé

*Corrigé rédigé par IA, non officiel. Signalez toute erreur.*

## Présentation du sujet

Le sujet « Voir de plus en plus petit, « voir » les atomes » enchaîne quatre instruments d'observation de la matière, du plus familier au plus sophistiqué, et fait parcourir à la fois l'optique géométrique, l'optique ondulatoire, l'électromagnétisme, la mécanique du point et les éléments de mécanique quantique :

| Partie | Thème | Questions |
|---|---|---|
| 1 | L'œil humain et son pouvoir de résolution | Q1* – Q9 |
| 2 | Microscope optique (photonique) | Q10 – Q20 |
| 3 | Microscope électronique à balayage (MEB) | Q21* – Q48 |
| 4 | Microscope à effet tunnel | Q49* – Q64 |

Sur 64 questions, **33 « relevant d'un socle fondamental de connaissances et de compétences »** sont repérées par une étoile (*) : Q1–Q7, Q13, Q17, Q21, Q22, Q23, Q27–Q37, Q39, Q49–Q57.

Quelques statistiques du rapport de jury de cette épreuve : moyenne des candidats admissibles 10,85 (écart-type 3,30), moyenne des admis 11,52 (écart-type 3,47), notes extrêmes 3,99 et 20 chez les admissibles, 5,89 et 20 chez les admis.

Le rapport insiste sur la forme attendue :

> [!JURY]
> « Il est particulièrement important que les réponses fournies soient des phrases rédigées en français, reprenant les termes de la question et non pas un simple mot « oui » ou « non », même accompagné d’une phrase de justification. »

> [!JURY]
> « le jury [...] recommande de relier les différentes étapes par des commentaires explicites. Le traitement rigoureux des questions passe également par le respect des notations proposées dans l’énoncé »

> [!JURY]
> « Une distance focale de microscope a peu de chance d’être de l’ordre du mètre (ou plus…), celle du cristallin est probablement de l’ordre du centimètre et l’ordre de grandeur du champ magnétique terrestre a fait l’objet de réponses hasardeuses, dignes parfois d’un champ d’étoile à neutrons. »

> [!JURY]
> « Ces questions, au nombre de 33 (sur un total de 64) sur cette épreuve, étaient repérées à l’aide d’une étoile (*). »

> [!JURY]
> « Les questions annoncées comme étant moins guidées (questions 18, 63 et 64) ont été assez peu abordées par les candidats et rares sont les copies où tous les points prévus par le barème ont été attribués. Pourtant, le jury tient à rappeler que toute piste de réponse sensée est valorisée, même lorsque celle-ci n’est pas menée à son terme. »

Conseils de lecture de ce guidé : les indications (`[!INDICATION]`) sont graduées et ne donnent jamais le résultat ; la solution complète figure sous chaque question (`#### Solution`) ; les blocs `[!JURY]` citent mot pour mot le rapport de cette épreuve.

---

## Partie 1 — L'œil humain et son pouvoir de résolution

### Question 1*

> [!INDICATION]
> Comparer la longueur d’onde aux dimensions des obstacles et ouvertures.

#### Solution

Dans l'**approximation de l'optique géométrique**, la lumière est décrite par des **rayons lumineux**, courbes suivies par l'énergie lumineuse, mutuellement indépendants et rectilignes dans un milieu homogène. Cette description néglige le caractère ondulatoire (diffraction, interférences). Elle est valable lorsque la **longueur d'onde est très petite devant les dimensions caractéristiques** des diaphragmes et obstacles : $\lambda \ll d$.

### Question 2*

> [!INDICATION]
> Choisir une observation de formation d’image et une manifestation du caractère ondulatoire.

#### Solution

- *Décrite par l'optique géométrique :* l'ombre nette portée par un objet macroscopique éclairé (dimensions $\gg \lambda$), ou la formation d'image par une lentille de diamètre quelques centimètres en lumière visible.
- *Non décrite :* la figure de diffraction derrière une fente de largeur de l'ordre de $\lambda$, ou les franges d'interférences des trous d'Young — phénomènes d'optique ondulatoire.

### Question 3*

> [!INDICATION]
> Préciser les deux conditions sur les rayons paraxiaux.

#### Solution

L'**approximation de Gauss** consiste à ne considérer que des **rayons paraxiaux** : peu inclinés sur l'axe optique **et** peu écartés de celui-ci. Les angles $\alpha$ sont alors faibles : $\sin\alpha \approx \tan\alpha \approx \alpha$ (en **radians**). Un système centré y est approximativement stigmatique et aplanétique.

### Question 4*

> [!INDICATION]
> Distinguer convergence exacte, tache image et conjugaison des plans transverses.

#### Solution

- **Stigmatisme rigoureux** pour $(A,A')$ : tout rayon issu de $A$ émerge en passant (réellement ou en prolongement) par un **unique** point $A'$. Schéma : faisceau issu de $A$ convergeant exactement en $A'$.
- **Stigmatisme approché** : les rayons émergents passent au **voisinage** d'un point $A'$ (tache image de petite dimension). Schéma : faisceau formant une petite tache autour de $A'$.
- **Aplanétisme** : l'image d'un objet plan **perpendiculaire** à l'axe optique est elle-même plane et perpendiculaire à l'axe.

### Question 5*

> [!INDICATION]
> Décrire les faisceaux incidents ou émergents associés aux deux foyers.

#### Solution

- **Foyer objet $F$** : point de l'axe dont l'image est rejetée à l'infini (rayons émergents parallèles à l'axe).
- **Foyer image $F'$** : image d'un point-objet à l'infini sur l'axe (rayons incidents parallèles à l'axe convergent en $F'$).

### Question 6*

> [!INDICATION]
> Placer l’objet au PP et son image sur la rétine avant la relation de conjugaison.

#### Solution

Œil accommodant au Punctum Proximum : objet en $\overline{OA} = -d_{pp}$, image nette sur la rétine en $\overline{OA'} = +d$. La relation de conjugaison donne

$$
-\frac{1}{\overline{OA}} + \frac{1}{\overline{OA'}} = \frac{1}{f'_p}\ \Longrightarrow\ \frac{1}{d_{pp}} + \frac{1}{d} = \frac{1}{f'_p},
$$

$$
\boxed{f'_p = \frac{d_{pp}\,d}{d_{pp}+d}} = \frac{0{,}250\times17\times10^{-3}}{0{,}250+17\times10^{-3}} \approx 15{,}9\ \text{mm} \approx 1{,}6\ \text{cm}.
$$

Ordre de grandeur attendu pour le cristallin (de l'ordre du centimètre).

### Question 7*

> [!INDICATION]
> Déduire l’espacement des cellules de leur densité surfacique, puis le relier à l’angle.

#### Solution

Œil non accommodant (Punctum Remotum à l'infini) : $f'_r = d$. Deux objets à l'infini séparés de $\alpha$ ont leurs images séparées sur la fovéa de $y = f'_r\tan\alpha \approx f'_r\,\alpha$. La densité surfacique de cellules étant $N_c$, l'espacement moyen entre deux cellules vaut $\delta \approx 1/\sqrt{N_c}$. On distingue les deux points si $y \geq \delta$, d'où

$$
\boxed{\alpha_1 = \frac{1}{f'_r\sqrt{N_c}}.}
$$

Avec $\sqrt{N_c} = \sqrt{160\times10^{3}\times10^{6}} = 4{,}0\times10^{5}\ \text{m}^{-1}$ :

$$
\alpha_1 = \frac{1}{17\times10^{-3}\times4{,}0\times10^{5}} = 1{,}5\times10^{-4}\ \text{rad} \approx 0{,}5'.
$$

### Question 8

> [!INDICATION]
> Relier la séparation des images au rayon d’Airy et comparer les deux limites.

#### Solution

Critère de Rayleigh : les centres des taches d'Airy sont distants d'au moins un rayon $\epsilon_d$. Avec $y = f'_r\,\alpha$ et $\epsilon_d = \dfrac{1{,}22\,\lambda_0 f'_r}{D}$ :

$$
\boxed{\alpha_2 = \frac{1{,}22\,\lambda_0}{D}} = \frac{1{,}22\times500\times10^{-9}}{3{,}0\times10^{-3}} = 2{,}0\times10^{-4}\ \text{rad} \approx 0{,}70'.
$$

On a $\alpha_2 \approx 0{,}70' > \alpha_1 \approx 0{,}5'$ : c'est la **diffraction** qui limite le pouvoir de résolution de l'œil ; l'échantillonnage rétinien est juste assez fin pour l'exploiter.

### Question 9

> [!INDICATION]
> Relier la taille de l’objet au PP à l’angle minimal distinguable.

#### Solution

Le plus petit objet est vu au Punctum Proximum sous l'angle limite $\alpha_2$ :

$$
a_{\min} = d_{pp}\,\alpha_2 = 0{,}25\times2{,}0\times10^{-4} = 5{,}1\times10^{-5}\ \text{m} \approx 50\ \mu\text{m}.
$$

Exemple d'objet de cette taille : le diamètre d'un cheveu humain ($\sim 50$–$100\ \mu$m).

---

## Partie 2 — Microscope optique (photonique)

### Question 10

> [!INDICATION]
> Décomposer la distance entre les centres optiques selon les foyers intermédiaires.

#### Solution

$\overline{O_1O_2} = \overline{O_1F'_1} + \overline{F'_1F_2} + \overline{F_2O_2} = f'_1 + \Delta + f'_2$, d'où

$$
\boxed{\Delta = d_0 - f'_1 - f'_2.}
$$

### Question 11

> [!INDICATION]
> Placer l’image intermédiaire dans le plan focal objet de l’oculaire puis appliquer Newton.

#### Solution

Observation sans accommodation ⇒ image finale à l'infini ⇒ image intermédiaire $A_1B_1$ dans le plan focal objet de l'oculaire, soit en $F_2$ : $\overline{F'_1A_1} = \Delta$. La relation de Newton $\overline{F_1A}\cdot\overline{F'_1A_1} = -f'^2_1$ donne $\overline{F_1A} = -f'^2_1/\Delta$, puis $\overline{O_1A} = -f'_1 - f'^2_1/\Delta$, d'où

$$
\boxed{h = |\overline{O_1A}| = f'_1 + \frac{f'^2_1}{\Delta} = \frac{f'_1(f'_1+\Delta)}{\Delta}.}
$$

Comme $\Delta \gg f'_1$, $h \approx f'_1$ : l'objet est quasi dans le plan focal objet de l'objectif.

### Question 12

> [!INDICATION]
> Exprimer le grandissement de l’objectif à partir de l’intervalle optique.

#### Solution

Par Newton, $\gamma_1 = -\dfrac{\overline{F'_1A_1}}{f'_1} = -\dfrac{\Delta}{f'_1}$. L'indication ×40 donne $|\gamma_1| = \Delta/f'_1 = 40$, d'où

$$
f'_1 = \frac{\Delta}{40} = \frac{160}{40} = \boxed{4{,}0\ \text{mm}}.
$$

### Question 13*

> [!INDICATION]
> Construire d’abord l’image intermédiaire puis les rayons émergents de l’oculaire.

#### Solution

Schéma à rendre : depuis $B$, (i) un rayon parallèle à l'axe émerge de $L_1$ en passant par $F'_1$ ; (ii) un rayon passant par $O_1$ n'est pas dévié ; leur intersection définit $B_1$, et l'on vérifie que $A_1B_1$ se situe dans le **plan focal objet $F_2$ de l'oculaire**. De $B_1$ situé en $F_2$, les rayons émergent de $L_2$ **parallèles entre eux**, inclinés de l'angle $\alpha'$ sur l'axe : l'image finale est à l'infini.

### Question 14

> [!INDICATION]
> Comparer les angles de vision du même objet intermédiaire, avec et sans oculaire.

#### Solution

L'objet $A_1B_1$ étant dans le plan focal objet de $L_2$, l'image à l'infini est vue sous $\tan\alpha' = \dfrac{A_1B_1}{f'_2}$. À l'œil nu, à la distance $d_{pp}$, le même objet est vu sous $\tan\alpha_0' = \dfrac{A_1B_1}{d_{pp}}$. En approximation de Gauss,

$$
\boxed{G_2 = \frac{\alpha'}{\alpha_0'} = \frac{d_{pp}}{f'_2}} \ \Longrightarrow\ f'_2 = \frac{d_{pp}}{G_2} = \frac{250}{10} = \boxed{25\ \text{mm}}.
$$

### Question 15

> [!INDICATION]
> Combiner le grandissement transversal de l’objectif avec le grossissement de l’oculaire.

#### Solution

$\tan\alpha' = \dfrac{A_1B_1}{f'_2} = \dfrac{|\gamma_1|\,AB}{f'_2}$ et $\tan\alpha_0 = \dfrac{AB}{d_{pp}}$. En Gauss,

$$
\boxed{G = \frac{\alpha'}{\alpha_0} = \frac{|\gamma_1|\,d_{pp}}{f'_2} = \frac{\Delta\,d_{pp}}{f'_1 f'_2} = |\gamma_1|\,G_2.}
$$

Numériquement $G = 40\times10 = 400$ (vérification : $\dfrac{160\times250}{4\times25} = 400$).

### Question 16

> [!INDICATION]
> Choisir une taille d’objet usuelle et estimer les deux angles de vision en radians.

#### Solution

Objet usuel : une cellule, $AB \sim 10\ \mu$m. Alors $\alpha_0 = \dfrac{AB}{d_{pp}} = \dfrac{10\times10^{-6}}{0{,}25} \approx 4\times10^{-5}$ rad et $\alpha' = G\,\alpha_0 \approx 400\times4\times10^{-5} = 1{,}6\times10^{-2}$ rad ($\approx 0{,}9^\circ$). Ces deux angles sont très petits devant 1 rad : l'approximation de Gauss est pleinement justifiée.

### Question 17*

> [!INDICATION]
> Partir de la définition de la puissance et identifier ses dimensions.

#### Solution

$\mathcal P = |\alpha'|/AB$ s'exprime en rad·m⁻¹ = m⁻¹ = **dioptrie** ($\delta$). Avec $|\alpha'| = |\gamma_1|\,AB/f'_2$ et $1/f'_2 = G_2/d_{pp}$ :

$$
\boxed{\mathcal P = \frac{|\gamma_1|}{f'_2} = \frac{|\gamma_1|\,G_2}{d_{pp}}} = \frac{40\times10}{0{,}25} = \boxed{1{,}6\times10^{3}\ \delta}.
$$

### Question 18

> [!INDICATION]
> Comparer les graduations angulaires de la lunette et les divisions du micromètre, puis propager les incertitudes.

#### Solution

*Principe.* L'image par le microscope d'une longueur-objet $\ell$ est vue à travers la lunette afocale sous un angle $\alpha'$. En comptant, sur la figure 7(b), le nombre $n$ de graduations élémentaires de la lunette (chacune d'ouverture angulaire $\theta_e$) recouvrant $p$ divisions du micromètre-objet (chacune de longueur $a = 10\ \mu$m), on a $\alpha' = n\theta_e$ pour $\ell = p\,a$, donc

$$
\mathcal P = \frac{\alpha'}{\ell} = \frac{n\,\theta_e}{p\,a}.
$$

*Lecture (figure 7b).* Une division du micromètre ($p=1$, $a = 10\ \mu$m) se superpose à $n \approx 19$ graduations élémentaires. Avec $\theta_e = 0{,}0482^\circ = 8{,}4\times10^{-4}$ rad :

$$
\mathcal P = \frac{19\times8{,}4\times10^{-4}}{10\times10^{-6}} \approx 1{,}6\times10^{3}\ \delta.
$$

*Incertitude.* Sources indépendantes : $\theta_e$ (type B, $u(\theta_e)/\theta_e = 0{,}0005/0{,}0482 \approx 1{,}0\ \%$) et le comptage $n$ ($u(n) \approx 1$ sur 19, soit 5 %) :

$$
\frac{u(\mathcal P)}{\mathcal P} = \sqrt{\left(\frac{u(\theta_e)}{\theta_e}\right)^2 + \left(\frac{u(n)}{n}\right)^2} \approx 5\ \%,
$$

soit $\mathcal P = (1{,}6 \pm 0{,}1)\times10^{3}\ \delta$. L'écart normalisé à la valeur de la Q17 est voisin de 0 : **mesure et modèle sont compatibles**.

### Question 19

> [!INDICATION]
> Employer la relation de résolution fournie avec la longueur d’onde de l’énoncé.

#### Solution

$$
a'_{\min} = \frac{0{,}61\,\lambda_0}{w_0} = \frac{0{,}61\times500\times10^{-9}}{0{,}65} \approx 4{,}7\times10^{-7}\ \text{m} = \boxed{0{,}47\ \mu\text{m}}.
$$

Un globule rouge ($\sim 7\ \mu$m) est résolu ; les **détails plus fins que $\sim 0{,}5\ \mu$m** ne le sont pas.

### Question 20

> [!INDICATION]
> Identifier les paramètres qui diminuent la taille minimale résolue.

#### Solution

Puisque $a'_{\min} = \dfrac{0{,}61\,\lambda_0}{w_0}$, on améliore le pouvoir de résolution en **diminuant $\lambda_0$** (éclairage bleu/UV) ou en **augmentant l'ouverture numérique $w_0 = n\sin\alpha$** (objectif à immersion, $n > 1$).

---

## Partie 3 — Microscope électronique à balayage

### Question 21*

> [!INDICATION]
> Relier la longueur d’onde à la quantité de mouvement.

#### Solution

Relation de de Broglie :

$$
\boxed{\lambda_{dB} = \frac{h}{p}.}
$$

### Question 22*

> [!INDICATION]
> Écrire la force générale puis remplacer la charge par celle de l’électron.

#### Solution

Force de Lorentz :

$$
\boxed{\vec F_L = q(\vec E + \vec v \wedge \vec B).}
$$

### Question 23*

> [!INDICATION]
> Exprimer le travail électrique à partir de la variation de potentiel et contrôler son signe.

#### Solution

Le champ électrostatique dérive du **potentiel scalaire** $V$ : $\vec E = -\overrightarrow{\operatorname{grad}}\,V$. L'énergie potentielle d'une charge $q$ est $E_{pe} = qV$ (à une constante près). Pour l'électron ($q = -e$) partant de la cathode ($V=0$, vitesse quasi nulle) vers l'anode ($V = V_a$), le théorème de l'énergie cinétique donne $\tfrac12 m_e v_f^2 = eV_a$. Pour que la vitesse augmente, il faut

$$
\boxed{V_a > 0}
$$

(l'anode positive attire et accélère les électrons négatifs). Schéma : $\vec E$ dirigé anode→cathode, force $-e\vec E$ dirigée cathode→anode.

### Question 24

> [!INDICATION]
> Relier l’énergie cinétique finale au travail électrique.

#### Solution

Non relativiste : $\tfrac12 m_e v_f^2 = eV_a$, d'où

$$
\boxed{v_f = \sqrt{\frac{2eV_a}{m_e}}.}
$$

### Question 25

> [!INDICATION]
> Comparer chaque vitesse calculée à la célérité de la lumière.

#### Solution

- $|V_a| = 10$ kV : $v_f = \sqrt{\dfrac{2\times1{,}6\times10^{-19}\times10^{4}}{9{,}11\times10^{-31}}} = 5{,}9\times10^{7}\ \text{m}\cdot\text{s}^{-1}$, soit $v_f/c \approx 0{,}20$ : à la **limite** de validité du cadre non relativiste.
- $|V_a| = 10^{3}$ kV : la formule donnerait $v_f = 5{,}9\times10^{8}\ \text{m}\cdot\text{s}^{-1} > c$, **impossible** : l'hypothèse non relativiste est invalide, il faut un traitement relativiste.

### Question 26

> [!INDICATION]
> Combiner énergie cinétique, quantité de mouvement et longueur d’onde.

#### Solution

$|V_a| = 10$ kV : $\lambda_{dB} = \dfrac{h}{m_e v_f} = \dfrac{6{,}62\times10^{-34}}{9{,}11\times10^{-31}\times5{,}9\times10^{7}} \approx 1{,}2\times10^{-11}$ m $= 12$ pm. Avec $w_0 = 0{,}65$ : $a'_{\min} = \dfrac{0{,}61\,\lambda_{dB}}{w_0} \approx 1{,}2\times10^{-11}$ m $\approx 0{,}01$ nm, très inférieur à la taille atomique ($\sim 0{,}1$ nm) : dans cette hypothèse, **l'étude de la matière à l'échelle atomique serait possible** (en pratique le pouvoir de résolution n'est pas donné par cette relation, comme le signale l'énoncé).

### Question 27*

> [!INDICATION] Ordre de grandeur du champ magnétique terrestre en surface : quelques dizaines de microteslas.
> [!INDICATION] Origine : quel phénomène dans quelle couche de la Terre ?

#### Solution

$B_T \sim 10^{-5}$ T ($\approx 47\ \mu$T). Origine : **effet dynamo** dans le **noyau externe** (mouvements de convection du fer-nickel liquide conducteur).

> [!JURY]
> « un certain nombre de candidats confondent manteau (et roches en fusion) et noyau terrestre et si certains ordres de grandeurs cités sont aberrants. »

### Question 28*

> [!INDICATION] La force magnétique est orthogonale à la vitesse : que vaut sa puissance ?
> [!INDICATION] En déduire la conséquence sur l'énergie cinétique via le théorème de la puissance cinétique.

#### Solution

$\mathcal P = \vec F\cdot\vec v = 0$ car $\vec v \wedge \vec B \perp \vec v$ ; donc $\dfrac{\mathrm dE_c}{\mathrm dt} = 0$ : la norme $\|\vec v\|$ est **constante**.

### Question 29*

> [!INDICATION] Projeter le PFD sur les trois axes avec $\vec B = B\vec u_z$ ; poser $\omega_c = eB/m_e$.
> [!INDICATION] Ne pas supposer $Oz$ vertical : la seule force est magnétique ici.

#### Solution

$$
\frac{\mathrm dv_x}{\mathrm dt} = -\omega_c v_y,\quad \frac{\mathrm dv_y}{\mathrm dt} = \omega_c v_x,\quad \frac{\mathrm dv_z}{\mathrm dt} = 0.
$$
Trajectoire rectiligne ssi $\vec v_0 \parallel \vec B$, soit $\beta = 0$.

> [!JURY]
> « On rappelle que Oz n’est pas forcément l’axe vertical… le jury souligne que l’application de la 2e loi de Newton ne se fait pas uniquement dans le cadre de la chute libre ; plusieurs candidats ont cherché à retrouver le mouvement parabolique d’un projectile soumis uniquement à son poids, ce qui n’avait aucun lien avec la situation proposée ici. »

### Question 30*

> [!INDICATION] Partir de $[F] = [qvB]$ et isoler $[\omega_c] = [eB/m_e]$.
> [!INDICATION] Conclure sur la nature de $\omega_c$.

#### Solution

$[eB] = \text{kg}\cdot\text{s}^{-1}$ donc $[\omega_c] = \text{s}^{-1}$ : $\omega_c$ est une **pulsation** (pulsation cyclotron).

> [!JURY]
> « il est indispensable de fournir la ou les relations physiques qui amènent à la dimension cherchée. »

### Question 31*

> [!INDICATION] Intégrer $\mathrm dv_z/\mathrm dt = 0$ avec $v_z(0) = v_0\cos\beta$.
> [!INDICATION] Intégrer encore pour obtenir $z(t)$.

#### Solution

$$
\boxed{z(t) = v_0\cos\beta\;t.}
$$

### Question 32*

> [!INDICATION] Poser la variable complexe $Z = v_x + i\,v_y$ pour coupler les deux équations.
> [!INDICATION] Résoudre l'équation différentielle du premier ordre en $Z$ avec la condition initiale.

#### Solution

$\mathrm dZ/\mathrm dt = i\omega_c Z$ d'où $Z = Z(0)e^{i\omega_c t}$, soit

$$
v_x = -v_0\sin\beta\,\sin\omega_c t,\quad v_y = v_0\sin\beta\,\cos\omega_c t.
$$

### Question 33*

> [!INDICATION] Intégrer $v_x$ et $v_y$ avec $x(0) = y(0) = 0$.
> [!INDICATION] Faire apparaître le rayon $v_0\sin\beta/\omega_c$.

#### Solution

$$
x(t) = \frac{v_0\sin\beta}{\omega_c}(\cos\omega_c t - 1),\quad y(t) = \frac{v_0\sin\beta}{\omega_c}\sin\omega_c t,\quad z(t) = v_0\cos\beta\,t.
$$

### Question 34*

> [!INDICATION] Pour $\beta = \pi/2$, éliminer le temps entre $x(t)$ et $y(t)$.
> [!INDICATION] Reconnaître l'équation d'un cercle ; donner centre, rayon et sens de parcours.

#### Solution

$$
\left(x + \frac{v_0}{\omega_c}\right)^2 + y^2 = \left(\frac{v_0}{\omega_c}\right)^2
$$
: cercle de rayon
$$
\boxed{r_C = \frac{m_e v_0}{eB}}
$$
(rayon de Larmor), parcouru à la pulsation $\omega_c$.

### Question 35*

> [!INDICATION] Quelle transformation laisse invariante la spire circulaire d'axe $Oz$ ?
> [!INDICATION] En coordonnées cylindriques $(r,\theta,z)$, quelles coordonnées ne peuvent pas intervenir dans $B(M)$ ?

#### Solution

Invariance par rotation autour de $Oz$ : $B$ ne dépend pas de $\theta$ → $B(M) = B(r,z)$.

> [!JURY]
> « ne pas seulement évoquer une « invariance » ou une « symétrie » mais l’invariance de la source (de la distribution de courants par exemple) »

### Question 36*

> [!INDICATION] Le plan méridien contenant $M$ et $Oz$ est un plan d'antisymétrie des courants : quel est le comportement du pseudo-vecteur $\vec B$ par réflexion ?
> [!INDICATION] En déduire la direction de $\vec B$ en $M$ situé dans ce plan.

#### Solution

Réflexion dans le plan méridien : la spire est invariante mais le courant azimutal change de sens ; $\vec B$ pseudo-vecteur est **contenu** dans le plan en $M$ :
$$
\vec B(M) = B_r(r,z)\vec u_r + B_z(r,z)\vec u_z.
$$

> [!JURY]
> « la mention claire et explicite de tel ou tel plan de symétrie ou antisymétrie des sources, la mention du point M d’observation ainsi que de la direction du champ par rapport à ces plans. »

### Question 37*

> [!INDICATION] Un point de l'axe appartient à tous les plans méridiens : quelle est l'intersection de ces plans ?
> [!INDICATION] En déduire la direction de $\vec B$ sur l'axe.

#### Solution

Sur l'axe $Oz$, $\vec B$ appartient à tous les plans méridiens, donc à leur intersection :
$$
\vec B(P) = B_a(z)\,\vec u_z.
$$

### Question 38

> [!INDICATION] Sur l'axe, comparer la direction de $\vec v_0$ et celle de $\vec B$.
> [!INDICATION] Que vaut alors la force de Lorentz ?

#### Solution

$\vec v_0 \parallel \vec B$ sur l'axe → $\vec v \wedge \vec B = \vec 0$ : force nulle, trajectoire **rectiligne selon $Oz$**.

### Question 39*

> [!INDICATION] « Faible étendue radiale » et « angle $\beta$ faible » sont deux façons de nommer quelles conditions ?
> [!INDICATION] Faire le lien avec le stigmatisme approché de l'optique géométrique.

#### Solution

Ce sont exactement les **conditions de l'approximation de Gauss** (rayons paraxiaux), déjà rencontrées en partie 1.

> [!JURY]
> « Dans la question 39, le lien avec les conditions de Gauss a bien été fait, à la satisfaction du jury. »

### Question 40

> [!INDICATION] Allure de $B_a(z) = B_0/(1+z^2/a^2)^{3/2}$ : parité, maximum, limites.
> [!INDICATION] Résoudre $B_a(\ell) = B_0/2$. Tracer en annotant axes, noms des grandeurs et valeurs remarquables.

#### Solution

Courbe en cloche paire, max $B_0$ en $z=0$ ;
$$
\ell = a\sqrt{2^{2/3}-1} \approx 0{,}77\,a.
$$

> [!JURY]
> « le tracé d’un graphe doit faire apparaître clairement les noms ou symboles des grandeurs représentées en abscisses et en ordonnées, ainsi que les valeurs remarquables en abscisse et/ou en ordonnée. »

### Question 41

> [!INDICATION] Champ sur l'axe d'une spire de $N$ tours parcourus par $I$ : $B_0 = \mu_0 N I/(2a)$.
> [!INDICATION] Application numérique ; comparer au champ terrestre.

#### Solution

$$
B_0 = \frac{4\pi\times10^{-7}\times600\times4{,}0}{2\times0{,}040} \approx \boxed{38\ \text{mT}}
$$
; $B_0/B_T \sim 10^{3}$ : le champ terrestre est négligeable.

### Question 42

> [!INDICATION] Comparer la norme de la force magnétique $e v_0 B_0$ au poids $m_e g$.
> [!INDICATION] Conclure.

#### Solution

$\dfrac{m_e g}{e v_0 B_0} \approx 2\times10^{-17} \ll 1$ : le poids est **négligeable** devant la force magnétique.

### Question 43

> [!INDICATION] Identifier dans l'équation (4) le rôle de $B_a(z)$ et réécrire le second membre avec $A = (B_0 e/(2 m v_0))^2 a$.
> [!INDICATION] Quelles lignes du code définissent $B_0$ et le second membre de l'équation différentielle ?

#### Solution

Ligne 19 : `B0 = mu0*N*I/(2*a)` ; avec $B_a^2 = B_0^2/(1+z^2/a^2)^3$, l'équation (4) devient $\mathrm d^2r/\mathrm dz^2 = -(A/a)\,r/(1+z^2/a^2)^3$ ; ligne 35 : `return([rprime, -A*r/(a*(1+(z/a)**2)**3)])`.

### Question 44

> [!INDICATION] Lire la boucle d'initialisation : quelle suite d'angles est utilisée ?
> [!INDICATION] Quelle ligne fixe $\beta = 5^\circ$ en radians ?

#### Solution

Angles initiaux $\beta/(i+1)$ (le plus grand vaut $\beta$) ; ligne 25 : `beta = 5*np.pi/180`.

### Question 45

> [!INDICATION] Vérifier $\beta_{\max} \ll 1$ rad (hypothèse H2).
> [!INDICATION] Lire sur la figure 12 le maximum de $r/a$ et vérifier $r \ll a$ (hypothèse H4).

#### Solution

$\beta_{\max} = 5^\circ = 8{,}7\times10^{-2}$ rad $\ll 1$ ; $\max(r/a) \approx 0{,}048 \ll 1$ : H2 et H4 vérifiées.

### Question 46

> [!INDICATION] Intégrer l'équation (4) entre $-\ell$ et $\ell$ en considérant $r \approx r_0$ constant (lentille mince).
> [!INDICATION] Identifier $\Gamma = \int_{-\ell}^{\ell} B_a^2\,\mathrm dz$ et la relation de conjugaison.

#### Solution

$$
\frac{1}{\overline{OA'}} - \frac{1}{\overline{OA}} = \frac{e^2\Gamma}{4m_e^2v_0^2},\quad \boxed{f' = \frac{4m_e^2v_0^2}{e^2\,\Gamma} > 0}\ \text{(convergente)}.
$$

> [!JURY]
> « une distance focale si petite ne pourrait être réalisée en optique photonique. »

### Question 47

> [!INDICATION] À $v_0$ fixée, que faut-il augmenter pour diminuer $f'$ ?
> [!INDICATION] Quel paramètre expérimental contrôle $\Gamma$ ?

#### Solution

$f' \propto 1/\Gamma$ : il faut **augmenter $\Gamma = \int B_a^2\,\mathrm dz$**, donc $B_0$, donc le produit $NI$ (nombre de spires ou intensité du courant).

### Question 48

> [!INDICATION] Employer directement la formule de focale fournie et contrôler les unités avant le calcul.
> [!INDICATION] Application numérique ; comparer à une focale de lentille de verre.

#### Solution

$$
f' \approx \boxed{6\ \text{mm}}
$$
: une focale aussi courte est inaccessible en optique photonique, d'où l'intérêt des lentilles magnétiques du MEB.

---

## Partie 4 — Microscope à effet tunnel

### Question 49*

> [!INDICATION] Interprétation de Born : $|\Psi|^2\,\mathrm dx$ est une probabilité. Comment nomme-t-on $|\Psi|^2$ exactement ?
> [!INDICATION] Pourquoi parle-t-on de « densité » de probabilité ?

#### Solution

$\rho = |\Psi(x,t)|^2$ est la **densité linéique de probabilité de présence** de la particule.

> [!JURY]
> « le vocabulaire précis désignant le module au carré de la fonction d’onde comme étant la densité de probabilité de présence a été très peu souvent vu dans les réponses. »

### Question 50*

> [!INDICATION] Énergie mécanique $E = p^2/(2m) + W$ avec $p = \hbar k$ : exprimer $E$ en joules.
> [!INDICATION] Quelle propriété de $|\Psi|^2$ caractérise un état stationnaire ?

#### Solution

$$
E = \frac{\hbar^2 k^2}{2m} + W\ \text{[J]};
$$
état stationnaire : $|\Psi(x,t)|^2 = |\varphi(x)|^2$ **indépendant du temps**.

> [!JURY]
> « un état dont la densité de probabilité de présence ne dépend pas du temps. »

### Question 51*

> [!INDICATION] Injecter $\Psi = \varphi(x)e^{-iEt/\hbar}$ dans l'équation de Schrödinger dépendante du temps.
> [!INDICATION] Faire apparaître l'hamiltonien $\hat H = -\frac{\hbar^2}{2m}\frac{\mathrm d^2}{\mathrm dx^2} + W(x)$.

#### Solution

$$
\boxed{\varphi''(x) + \frac{2m}{\hbar^2}\big(E - W(x)\big)\varphi(x) = 0.}
$$

### Question 52

> [!INDICATION]
> Lire les trois niveaux du potentiel sur la figure 14, puis comparer chaque niveau à l’énergie E.

#### Solution

Le potentiel vaut $0$ dans les régions (I) et (III), et $W_s$ dans la région (II). Avec les paramètres imposés par l'énoncé,
$$k=\frac{\sqrt{2m_eE}}{\hbar},$$
$$q=\frac{\sqrt{2m_e(W_s-E)}}{\hbar},$$
les équations et leurs solutions générales sont :
$$\begin{aligned}
\varphi_1''+k^2\varphi_1&=0,&\varphi_1(z)&=A e^{ikz}+B e^{-ikz},\\
\varphi_2''-q^2\varphi_2&=0,&\varphi_2(z)&=C e^{qz}+D e^{-qz},\\
\varphi_3''+k^2\varphi_3&=0,&\varphi_3(z)&=F e^{ikz}+G e^{-ikz}.
\end{aligned}$$
Les coefficients sont complexes en général. Pour une expérience de diffusion avec onde incidente venant seulement du substrat, aucune onde n'arrive de $+\infty$ : on impose ensuite $G=0$.

### Question 53

> [!INDICATION] Quelles sont les conditions de raccordement en $z = 0$ et $z = b$ pour $\varphi$ et sa dérivée ?
> [!INDICATION] Combien d'équations obtient-on pour combien d'inconnues ?

#### Solution

$\varphi$ et $\varphi'$ **continus** en $z=0$ et $z=b$ : 4 équations linéaires pour les 5 amplitudes ($A, B, C, D, F$). Une amplitude incidente fixée permet de déterminer les autres par ces raccords ; le coefficient de transmission se calcule ensuite à partir des courants (Q57–58).

### Question 54

> [!INDICATION]
> Distinguer la forme spatiale exponentielle de la présence ou de l’absence d’un courant total.

#### Solution

Dans la barrière, la partie spatiale est une combinaison d'exponentielles réelles en $z$ : les solutions sont **évanescentes**, et non des ondes planes oscillantes. La longueur de décroissance d'une exponentielle est $1/q$.

Sur une barrière d'épaisseur finie, il faut garder les deux exponentielles avec des coefficients complexes. Le courant total n'est pas nécessairement nul :
$$J_z=\frac{\hbar}{m_e}\operatorname{Im}(\varphi_2^*\varphi_2')=\frac{2\hbar q}{m_e}\operatorname{Im}(D^*C).$$
Une exponentielle isolée a un courant nul ; leur combinaison raccordée aux deux régions de propagation permet un courant transmis non nul. Il ne s'agit pas d'une onde progressive absorbée par un milieu dissipatif.

### Question 55

> [!INDICATION]
> Chercher une situation optique où un champ existe de l’autre côté d’une interface sans onde propagative normale.

#### Solution

Un exemple est la **réflexion totale interne en optique** : lorsqu'une onde passe d'un milieu d'indice élevé vers un milieu d'indice plus faible au-delà de l'angle critique, le champ transmis est évanescent suivant la normale à l'interface. Il peut exister dans le second milieu même si aucune onde propagative ne transporte l'énergie loin de l'interface dans cette direction.

Comme $q$ intervient dans $e^{-qz}$, il est homogène à l'inverse d'une longueur. Ainsi
$$\boxed{\delta=\frac1q=\frac{\hbar}{\sqrt{2m_e(W_s-E)}}}$$
est une **longueur de pénétration** : après une distance $\delta$, l'amplitude de l'exponentielle décroissante est divisée par $e$ (la densité de probabilité par $e^2$).

### Question 56

> [!INDICATION]
> Interpréter un flux à travers une surface, puis comparer à un flux de masse ou de charge.

#### Solution

Le vecteur $\vec J$ est une **densité de courant de probabilité**. Le flux $\vec J\cdot\vec n\,dS\,dt$ représente la probabilité transportée à travers la surface orientée $dS$ pendant $dt$ ; dans le modèle unidimensionnel, $J_zdt$ est la probabilité traversant un point durant cet intervalle. L'équation de continuité est
$$\partial_t\rho+\operatorname{div}\vec J=0.$$
L'analogie est celle du transport de masse, avec $\vec j_m=\rho_m\vec v$, ou du transport de charge avec $\vec j_e=\rho_e\vec v$. Ici, pour l'onde plane donnée,
$$\vec J=|\Psi|^2\frac{\hbar k}{m_e}\vec u_z,$$
et $\hbar k/m_e$ joue le rôle de la vitesse de transport de la probabilité.

### Question 57

> [!INDICATION] Définir $T = J_{\text{transmise}}/J_{\text{incidente}}$.
> [!INDICATION] Que devient classiquement une particule d'énergie $E < W_s$ arrivant sur la barrière ?

#### Solution

$T$ = **probabilité de traversée** de la barrière ; classiquement la barrière est **infranchissable** ($E < W_s$) : $T > 0$ en quantique = **effet tunnel**.

> [!JURY]
> « barrière infranchissable pour une particule classique »

### Question 58

> [!INDICATION]
> Développer le sinus hyperbolique à grand argument et identifier le terme dominant du dénominateur.

#### Solution

Une **barrière épaisse** vérifie $qb\gg1$ : sa largeur est grande devant la longueur de pénétration $1/q$. Alors
$$\sinh(qb)=\frac{e^{qb}-e^{-qb}}2\simeq\frac{e^{qb}}2,$$
et donc $\gamma\sinh^2(qb)\gg1$. La formule exacte fournie devient
$$T\simeq\frac{4}{\gamma}e^{-2qb}.$$
En remplaçant $\gamma=W_s^2/[4E(W_s-E)]$ :
$$\boxed{T\simeq16\frac{E}{W_s}\left(1-\frac{E}{W_s}\right)e^{-2qb}.}$$
Il n'est pas nécessaire de supposer $E\ll W_s$ : on conserve tout le préfacteur.

### Question 59

> [!INDICATION]
> Déduire E des deux valeurs imposées avant de calculer la longueur de pénétration et le préfacteur.

#### Solution

L'énoncé fixe $W_s=4,5$ eV et $W_s-E=1$ eV, donc $E=3,5$ eV. Après conversion de l'électronvolt en joule,
$$q=\frac{\sqrt{2\times9,11\times10^{-31}\times1,60\times10^{-19}}}{1,055\times10^{-34}}\simeq5,12\times10^9\ \mathrm{m^{-1}}.$$
Le préfacteur est
$$16\frac{3,5}{4,5}\left(1-\frac{3,5}{4,5}\right)\simeq2,77.$$
Pour les deux largeurs :
$$\begin{aligned}
2qb_1&\simeq5,12,&T_1&\simeq2,77e^{-5,12}\simeq1,66\times10^{-2},\\
2qb_2&\simeq6,14,&T_2&\simeq2,77e^{-6,14}\simeq5,95\times10^{-3}.
\end{aligned}$$
Les valeurs exactes diffèrent de moins d'un pour cent de cette estimation de barrière épaisse. Une augmentation de largeur de seulement $0,1$ nm divise la transmission par environ $2,8$ : cette sensibilité à la distance rend le microscope utilisable.

### Question 60

> [!INDICATION]
> Utiliser la variation relative du courant donnée par sa dérivée logarithmique, en conservant le facteur 1/z.

#### Solution

Le document donne
$$I(z)=C U_t\frac{k_0}{z}e^{-2k_0z},\qquad k_0=\frac{\sqrt{2m_eW_s}}{\hbar}.$$
Avec $W_s=4,5$ eV,
$$\boxed{k_0\simeq1,09\times10^{10}\ \mathrm{m^{-1}}.}$$
À tension et densité électronique locale constantes, la dérivée logarithmique est
$$\frac{d\ln I}{dz}=-\frac1z-2k_0.$$
Pour une petite variation de hauteur,
$$\frac{|\Delta I|}{I}\simeq\left(\frac1z+2k_0\right)|\Delta z|.$$
À $z=0,1$ nm et pour un seuil relatif de détection de $2\%$,
$$\boxed{\Delta z_{\min}\simeq\frac{0,02}{10^{10}+2,17\times10^{10}}\simeq6,3\times10^{-13}\ \mathrm m=0,63\ \mathrm{pm}.}$$
C'est la résolution verticale déduite du modèle du document, non la profondeur de pénétration de la fonction d'onde.

### Question 61

> [!INDICATION]
> Employer la relation fournie et distinguer la séparation des surfaces de la distance au centre de l’atome terminal.

#### Solution

Le modèle fourni impose
$$\boxed{\Delta x_{\min}\simeq\sqrt{\frac{2z'}{k_0}}.}$$
$z'$ mesure la distance de la surface au **centre** de l'atome terminal de la pointe. La séparation géométrique est de l'ordre de $0,1$ nm ; en ajoutant une longueur atomique de l'ordre de $0,1$ nm, on estime $z'\sim0,2$ nm. Ainsi
$$\Delta x_{\min}\sim\sqrt{\frac{2\times2\times10^{-10}}{1,09\times10^{10}}}\simeq1,9\times10^{-10}\ \mathrm m.$$
L'ordre de grandeur est donc **$0,1$ à $0,2$ nm**. Si l'on assimile au premier ordre $z'$ à $0,1$ nm, on obtient $0,14$ nm ; ce choix géométrique doit être explicité. La résolution latérale est d'ordre atomique et moins fine que la résolution verticale.

### Question 62

> [!INDICATION]
> Comparer séparément chaque résolution à la longueur atomique et préciser la grandeur mesurée.

#### Solution

La résolution verticale obtenue est de l'ordre de $0,6$ pm, très inférieure aux dimensions atomiques. La résolution latérale, de l'ordre de $0,1$ à $0,2$ nm, est comparable aux distances entre atomes : des sites atomiques voisins peuvent être distingués.

**Le microscope accède donc à une image de résolution atomique.** Cette image est une cartographie du courant tunnel ou de la hauteur nécessaire pour le maintenir constant ; son contraste dépend aussi de la densité électronique locale. « Voir les atomes » ne signifie pas obtenir une photographie optique de sphères matérielles.

### Question 63

> [!INDICATION] Sur l'image STM du graphite, quel sous-réseau apparaît ? Mesurer son paramètre $d_{\exp}$.
> [!INDICATION] Le relier à la distance C–C ($0{,}142$ nm) et expliquer l'origine physique (densité d'états au niveau de Fermi).

#### Solution

$d_{\exp} \approx \boxed{0{,}25\ \text{nm}} \approx \sqrt{3}\times0{,}142$ nm : sous-réseau hexagonal imagé, dû aux atomes contribuant à la densité d'états au niveau de Fermi.

> [!JURY]
> « Les questions 63 et 64, non guidées, ont été abordées par un nombre non négligeable de candidats, donnant des valeurs numériques correctes. Les conclusions et interprétations ont été plus souvent erronées, cependant. »

### Question 64

> [!INDICATION]
> Relier les ondulations à une densité d’états et distinguer estimation nanométrique et ajustement quantitatif du métal.

#### Solution

Les vaguelettes sont des **interférences d'ondes électroniques de surface**, réfléchies et diffusées par les atomes de fer qui délimitent l'enclos. Le courant tunnel révèle les variations de densité locale d'états associées aux modes confinés ; les crêtes ne sont pas des rangées d'atomes supplémentaires.

Pour une estimation à une puissance de dix près, choisissons explicitement une énergie cinétique de l'ordre de $1$ eV pour un électron de surface : cette valeur est une hypothèse d'ordre de grandeur, non une donnée de l'énoncé. Avec la masse de l'électron libre,
$$\lambda_{dB}=\frac{h}{\sqrt{2m_eE_c}}\simeq\frac{6,62\times10^{-34}}{\sqrt{2\times9,11\times10^{-31}\times1,60\times10^{-19}}}\simeq1,2\times10^{-9}\ \mathrm m.$$
La longueur d'onde est **nanométrique**, de sorte que plusieurs oscillations peuvent tenir dans l'enclos de rayon $7,13$ nm. La figure montre bien quelques anneaux sur cette longueur. Pour une superposition locale d'ondes opposées, le contraste de densité est proportionnel à un carré d'amplitude et sa période spatiale est de l'ordre de $\lambda/2$.

Un ajustement quantitatif de la période nécessite la dispersion et la masse effective des états de surface du cuivre : l'énergie de Fermi du métal massif ne doit pas être substituée sans justification. À titre de contrôle d'un calcul souvent proposé, prendre $E_c=7$ eV avec la masse libre donnerait $0,46$ nm, et non $2$ nm.

## Bilan

Le sujet compare l’œil, le microscope optique, le MEB et le STM. Avec les données de l’énoncé : $\alpha_1\simeq0,5'$ et $\alpha_2\simeq0,70'$ ; la diffraction impose $a_{\min}\simeq50\ \mu\mathrm m$ au PP. Le microscope a $G=400$, une puissance instrumentale $\mathcal P\simeq1,6\times10^3\ \mathrm{m^{-1}}$ et une limite de résolution $a'_{\min}\simeq0,47\ \mu\mathrm m$ : ces deux grandeurs ont des définitions distinctes. Pour les électrons à 10 kV, $\lambda_{dB}\simeq12$ pm ; la bobine donne $B_0\simeq38$ mT et la focale magnétique est de l’ordre de 6 mm. Dans la barrière, $q\simeq5,12\times10^9\ \mathrm{m^{-1}}$ ; $T(0,5\ \mathrm{nm})\simeq0,0166$ et $T(0,6\ \mathrm{nm})\simeq0,00595$. La sensibilité verticale STM est d’environ $0,63$ pm ; la résolution latérale estimée est de l’ordre de $0,1$ à $0,2$ nm selon la géométrie terminale retenue. Les ondulations du corral quantique s’interprètent comme des interférences d’états électroniques de surface de longueur d’onde nanométrique ; une valeur précise exige leur dispersion, absente de l’énoncé.

Formellement, le rapport de jury insiste sur des réponses rédigées en phrases françaises, reliées par des commentaires explicites, respectant les notations de l'énoncé, illustrées de schémas annotés, et assorties d'ordres de grandeur permettant de juger de la pertinence des valeurs numériques obtenues.
