# Agrégation Chimie — Composition de physique 2026 · Corrigé brut

*Corrigé rédigé par IA, non officiel. Signalez toute erreur.*

Épreuve B (session 2026, concours externe, section physique-chimie, option chimie), sujet « Voir de plus en plus petit, “voir” les atomes » : **64 questions** en quatre parties — 1. l'œil humain et son pouvoir de résolution ; 2. microscopie photonique ; 3. microscope électronique à balayage (lentille magnétique) ; 4. microscopie à effet tunnel. Les 33 questions « socle » repérées par une étoile (*) dans l'énoncé sont indiquées ici par `Question N*`. Convention de l'énoncé : axe optique orienté dans le sens de propagation ; $\overline{OA}$, $\overline{OA'}$ algébriques. Principales données : $d_{pp} = 0{,}250$ m, $d = 17$ mm (rétine), $N_c = 160\times10^{3}$ cellules/mm² (fovéa), $D = 3{,}0$ mm (pupille), $\lambda_0 = 500$ nm, $d_0 = 160$ mm + $f'_1 + f'_2$ (microscope, indications ×40 et ×10), $w_0 = 0{,}65$, $|V_a| = 10$ kV puis $10^3$ kV, $B_T \sim 10^{-5}$ T, bobine $a = 40$ mm, $N = 600$ spires, $I = 4{,}0$ A, barrière $W_s = 4{,}5$ eV, $E = 3{,}5$ eV, $b = 0{,}5$–$0{,}6$ nm.

---

## Partie 1 — L'œil humain et son pouvoir de résolution

### Question 1*

Dans l'**approximation de l'optique géométrique**, la lumière est décrite par des **rayons lumineux**, courbes suivies par l'énergie lumineuse, mutuellement indépendants et rectilignes dans un milieu homogène. Cette description néglige le caractère ondulatoire (diffraction, interférences). Elle est valable lorsque la **longueur d'onde est très petite devant les dimensions caractéristiques** des diaphragmes et obstacles : $\lambda \ll d$.

### Question 2*

- *Décrite par l'optique géométrique :* l'ombre nette portée par un objet macroscopique éclairé (dimensions $\gg \lambda$), ou la formation d'image par une lentille de diamètre quelques centimètres en lumière visible.
- *Non décrite :* la figure de diffraction derrière une fente de largeur de l'ordre de $\lambda$, ou les franges d'interférences des trous d'Young — phénomènes d'optique ondulatoire.

### Question 3*

L'**approximation de Gauss** consiste à ne considérer que des **rayons paraxiaux** : peu inclinés sur l'axe optique **et** peu écartés de celui-ci. Les angles $\alpha$ sont alors faibles : $\sin\alpha \approx \tan\alpha \approx \alpha$ (en **radians**). Un système centré y est approximativement stigmatique et aplanétique.

### Question 4*

- **Stigmatisme rigoureux** pour $(A,A')$ : tout rayon issu de $A$ émerge en passant (réellement ou en prolongement) par un **unique** point $A'$. Schéma : faisceau issu de $A$ convergeant exactement en $A'$.
- **Stigmatisme approché** : les rayons émergents passent au **voisinage** d'un point $A'$ (tache image de petite dimension). Schéma : faisceau formant une petite tache autour de $A'$.
- **Aplanétisme** : l'image d'un objet plan **perpendiculaire** à l'axe optique est elle-même plane et perpendiculaire à l'axe.

### Question 5*

- **Foyer objet $F$** : point de l'axe dont l'image est rejetée à l'infini (rayons émergents parallèles à l'axe).
- **Foyer image $F'$** : image d'un point-objet à l'infini sur l'axe (rayons incidents parallèles à l'axe convergent en $F'$).

### Question 6*

Œil accommodant au Punctum Proximum : objet en $\overline{OA} = -d_{pp}$, image nette sur la rétine en $\overline{OA'} = +d$. La relation de conjugaison donne

$$
-\frac{1}{\overline{OA}} + \frac{1}{\overline{OA'}} = \frac{1}{f'_p}\ \Longrightarrow\ \frac{1}{d_{pp}} + \frac{1}{d} = \frac{1}{f'_p},
$$

$$
\boxed{f'_p = \frac{d_{pp}\,d}{d_{pp}+d}} = \frac{0{,}250\times17\times10^{-3}}{0{,}250+17\times10^{-3}} \approx 15{,}9\ \text{mm} \approx 1{,}6\ \text{cm}.
$$

Ordre de grandeur attendu pour le cristallin (de l'ordre du centimètre).

### Question 7*

Œil non accommodant (Punctum Remotum à l'infini) : $f'_r = d$. Deux objets à l'infini séparés de $\alpha$ ont leurs images séparées sur la fovéa de $y = f'_r\tan\alpha \approx f'_r\,\alpha$. La densité surfacique de cellules étant $N_c$, l'espacement moyen entre deux cellules vaut $\delta \approx 1/\sqrt{N_c}$. On distingue les deux points si $y \geq \delta$, d'où

$$
\boxed{\alpha_1 = \frac{1}{f'_r\sqrt{N_c}}.}
$$

Avec $\sqrt{N_c} = \sqrt{160\times10^{3}\times10^{6}} = 4{,}0\times10^{5}\ \text{m}^{-1}$ :

$$
\alpha_1 = \frac{1}{17\times10^{-3}\times4{,}0\times10^{5}} = 1{,}5\times10^{-4}\ \text{rad} \approx 0{,}5'.
$$

### Question 8

Critère de Rayleigh : les centres des taches d'Airy sont distants d'au moins un rayon $\epsilon_d$. Avec $y = f'_r\,\alpha$ et $\epsilon_d = \dfrac{1{,}22\,\lambda_0 f'_r}{D}$ :

$$
\boxed{\alpha_2 = \frac{1{,}22\,\lambda_0}{D}} = \frac{1{,}22\times500\times10^{-9}}{3{,}0\times10^{-3}} = 2{,}0\times10^{-4}\ \text{rad} \approx 0{,}70'.
$$

On a $\alpha_2 \approx 0{,}70' > \alpha_1 \approx 0{,}5'$ : c'est la **diffraction** qui limite le pouvoir de résolution de l'œil ; l'échantillonnage rétinien est juste assez fin pour l'exploiter.

### Question 9

Le plus petit objet est vu au Punctum Proximum sous l'angle limite $\alpha_2$ :

$$
a_{\min} = d_{pp}\,\alpha_2 = 0{,}25\times2{,}0\times10^{-4} = 5{,}1\times10^{-5}\ \text{m} \approx 50\ \mu\text{m}.
$$

Exemple d'objet de cette taille : le diamètre d'un cheveu humain ($\sim 50$–$100\ \mu$m).

---

## Partie 2 — Microscopie photonique

### Question 10

$\overline{O_1O_2} = \overline{O_1F'_1} + \overline{F'_1F_2} + \overline{F_2O_2} = f'_1 + \Delta + f'_2$, d'où

$$
\boxed{\Delta = d_0 - f'_1 - f'_2.}
$$

### Question 11

Observation sans accommodation ⇒ image finale à l'infini ⇒ image intermédiaire $A_1B_1$ dans le plan focal objet de l'oculaire, soit en $F_2$ : $\overline{F'_1A_1} = \Delta$. La relation de Newton $\overline{F_1A}\cdot\overline{F'_1A_1} = -f'^2_1$ donne $\overline{F_1A} = -f'^2_1/\Delta$, puis $\overline{O_1A} = -f'_1 - f'^2_1/\Delta$, d'où

$$
\boxed{h = |\overline{O_1A}| = f'_1 + \frac{f'^2_1}{\Delta} = \frac{f'_1(f'_1+\Delta)}{\Delta}.}
$$

Comme $\Delta \gg f'_1$, $h \approx f'_1$ : l'objet est quasi dans le plan focal objet de l'objectif.

### Question 12

Par Newton, $\gamma_1 = -\dfrac{\overline{F'_1A_1}}{f'_1} = -\dfrac{\Delta}{f'_1}$. L'indication ×40 donne $|\gamma_1| = \Delta/f'_1 = 40$, d'où

$$
f'_1 = \frac{\Delta}{40} = \frac{160}{40} = \boxed{4{,}0\ \text{mm}}.
$$

### Question 13*

Schéma à rendre : depuis $B$, (i) un rayon parallèle à l'axe émerge de $L_1$ en passant par $F'_1$ ; (ii) un rayon passant par $O_1$ n'est pas dévié ; leur intersection définit $B_1$, et l'on vérifie que $A_1B_1$ se situe dans le **plan focal objet $F_2$ de l'oculaire**. De $B_1$ situé en $F_2$, les rayons émergent de $L_2$ **parallèles entre eux**, inclinés de l'angle $\alpha'$ sur l'axe : l'image finale est à l'infini.

### Question 14

L'objet $A_1B_1$ étant dans le plan focal objet de $L_2$, l'image à l'infini est vue sous $\tan\alpha' = \dfrac{A_1B_1}{f'_2}$. À l'œil nu, à la distance $d_{pp}$, le même objet est vu sous $\tan\alpha_0' = \dfrac{A_1B_1}{d_{pp}}$. En approximation de Gauss,

$$
\boxed{G_2 = \frac{\alpha'}{\alpha_0'} = \frac{d_{pp}}{f'_2}} \ \Longrightarrow\ f'_2 = \frac{d_{pp}}{G_2} = \frac{250}{10} = \boxed{25\ \text{mm}}.
$$

### Question 15

$\tan\alpha' = \dfrac{A_1B_1}{f'_2} = \dfrac{|\gamma_1|\,AB}{f'_2}$ et $\tan\alpha_0 = \dfrac{AB}{d_{pp}}$. En Gauss,

$$
\boxed{G = \frac{\alpha'}{\alpha_0} = \frac{|\gamma_1|\,d_{pp}}{f'_2} = \frac{\Delta\,d_{pp}}{f'_1 f'_2} = |\gamma_1|\,G_2.}
$$

Numériquement $G = 40\times10 = 400$ (vérification : $\dfrac{160\times250}{4\times25} = 400$).

### Question 16

Objet usuel : une cellule, $AB \sim 10\ \mu$m. Alors $\alpha_0 = \dfrac{AB}{d_{pp}} = \dfrac{10\times10^{-6}}{0{,}25} \approx 4\times10^{-5}$ rad et $\alpha' = G\,\alpha_0 \approx 400\times4\times10^{-5} = 1{,}6\times10^{-2}$ rad ($\approx 0{,}9^\circ$). Ces deux angles sont très petits devant 1 rad : l'approximation de Gauss est pleinement justifiée.

### Question 17*

$\mathcal P = |\alpha'|/AB$ s'exprime en rad·m⁻¹ = m⁻¹ = **dioptrie** ($\delta$). Avec $|\alpha'| = |\gamma_1|\,AB/f'_2$ et $1/f'_2 = G_2/d_{pp}$ :

$$
\boxed{\mathcal P = \frac{|\gamma_1|}{f'_2} = \frac{|\gamma_1|\,G_2}{d_{pp}}} = \frac{40\times10}{0{,}25} = \boxed{1{,}6\times10^{3}\ \delta}.
$$

### Question 18

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

$$
a'_{\min} = \frac{0{,}61\,\lambda_0}{w_0} = \frac{0{,}61\times500\times10^{-9}}{0{,}65} \approx 4{,}7\times10^{-7}\ \text{m} = \boxed{0{,}47\ \mu\text{m}}.
$$

Un globule rouge ($\sim 7\ \mu$m) est résolu ; les **détails plus fins que $\sim 0{,}5\ \mu$m** ne le sont pas.

### Question 20

Puisque $a'_{\min} = \dfrac{0{,}61\,\lambda_0}{w_0}$, on améliore le pouvoir de résolution en **diminuant $\lambda_0$** (éclairage bleu/UV) ou en **augmentant l'ouverture numérique $w_0 = n\sin\alpha$** (objectif à immersion, $n > 1$).

---

## Partie 3 — Microscope électronique à balayage

### Question 21*

Relation de de Broglie :

$$
\boxed{\lambda_{dB} = \frac{h}{p}.}
$$

### Question 22*

Force de Lorentz :

$$
\boxed{\vec F_L = q(\vec E + \vec v \wedge \vec B).}
$$

### Question 23*

Le champ électrostatique dérive du **potentiel scalaire** $V$ : $\vec E = -\overrightarrow{\operatorname{grad}}\,V$. L'énergie potentielle d'une charge $q$ est $E_{pe} = qV$ (à une constante près). Pour l'électron ($q = -e$) partant de la cathode ($V=0$, vitesse quasi nulle) vers l'anode ($V = V_a$), le théorème de l'énergie cinétique donne $\tfrac12 m_e v_f^2 = eV_a$. Pour que la vitesse augmente, il faut

$$
\boxed{V_a > 0}
$$

(l'anode positive attire et accélère les électrons négatifs). Schéma : $\vec E$ dirigé anode→cathode, force $-e\vec E$ dirigée cathode→anode.

### Question 24

Non relativiste : $\tfrac12 m_e v_f^2 = eV_a$, d'où

$$
\boxed{v_f = \sqrt{\frac{2eV_a}{m_e}}.}
$$

### Question 25

- $|V_a| = 10$ kV : $v_f = \sqrt{\dfrac{2\times1{,}6\times10^{-19}\times10^{4}}{9{,}11\times10^{-31}}} = 5{,}9\times10^{7}\ \text{m}\cdot\text{s}^{-1}$, soit $v_f/c \approx 0{,}20$ : à la **limite** de validité du cadre non relativiste.
- $|V_a| = 10^{3}$ kV : la formule donnerait $v_f = 5{,}9\times10^{8}\ \text{m}\cdot\text{s}^{-1} > c$, **impossible** : l'hypothèse non relativiste est invalide, il faut un traitement relativiste.

### Question 26

$|V_a| = 10$ kV : $\lambda_{dB} = \dfrac{h}{m_e v_f} = \dfrac{6{,}62\times10^{-34}}{9{,}11\times10^{-31}\times5{,}9\times10^{7}} \approx 1{,}2\times10^{-11}$ m $= 12$ pm. Avec $w_0 = 0{,}65$ : $a'_{\min} = \dfrac{0{,}61\,\lambda_{dB}}{w_0} \approx 1{,}2\times10^{-11}$ m $\approx 0{,}01$ nm, très inférieur à la taille atomique ($\sim 0{,}1$ nm) : dans cette hypothèse, **l'étude de la matière à l'échelle atomique serait possible** (en pratique le pouvoir de résolution n'est pas donné par cette relation, comme le signale l'énoncé).

### Question 27*

Champ magnétique terrestre : ordre de grandeur $B_T \sim 10^{-5}$ T (quelques dizaines de µT, $\approx 47\ \mu$T). Origine : **effet dynamo** — les mouvements de convection du métal liquide (fer-nickel) du **noyau externe** engendrent des courants électriques, source du champ.

### Question 28*

La force magnétique $\vec F = -e\,\vec v\wedge\vec B$ est orthogonale à $\vec v$, donc sa puissance est nulle :

$$
\frac{\mathrm d}{\mathrm dt}\!\left(\tfrac12 m_e v^2\right) = \vec F\cdot\vec v = 0.
$$

L'énergie cinétique est constante : $\|\vec v\|$ reste constante.

### Question 29*

$\vec v\wedge\vec B = (v_x,v_y,v_z)\wedge(0,0,B) = (v_yB, -v_xB, 0)$. Le PFD $m_e\,\dfrac{\mathrm d\vec v}{\mathrm dt} = -e\,\vec v\wedge\vec B$ donne, avec $\omega_c = eB/m_e$,

$$
\boxed{\frac{\mathrm dv_x}{\mathrm dt} = -\omega_c v_y,\qquad \frac{\mathrm dv_y}{\mathrm dt} = \omega_c v_x,\qquad \frac{\mathrm dv_z}{\mathrm dt} = 0.}
$$

La trajectoire est **rectiligne** si $\vec v\wedge\vec B = \vec 0$, c'est-à-dire $\vec v_0 \parallel \vec B$ : condition $\boxed{\beta = 0}$.

### Question 30*

De la force de Lorentz $F = qvB$ on tire $[eB] = \dfrac{[F]}{[v]} = \dfrac{\text{kg}\cdot\text{m}\cdot\text{s}^{-2}}{\text{m}\cdot\text{s}^{-1}} = \text{kg}\cdot\text{s}^{-1}$, donc

$$
[\omega_c] = \frac{[eB]}{[m_e]} = \text{s}^{-1} :
$$

$\omega_c$ est homogène à une **pulsation** : c'est la **pulsation cyclotron**.

### Question 31*

$\dfrac{\mathrm dv_z}{\mathrm dt} = 0 \Rightarrow v_z = v_0\cos\beta$ ($\vec v_0$ dans $(yOz)$ à l'angle $\beta$ de $\vec u_z$). En intégrant depuis $O$ :

$$
\boxed{z(t) = v_0\cos\beta\;t.}
$$

### Question 32*

$\dfrac{\mathrm dZ}{\mathrm dt} = \dfrac{\mathrm dv_x}{\mathrm dt} + i\dfrac{\mathrm dv_y}{\mathrm dt} = -\omega_c v_y + i\omega_c v_x = i\omega_c Z$, donc $Z(t) = Z(0)e^{i\omega_c t}$ avec $Z(0) = i\,v_0\sin\beta$ :

$$
\boxed{v_x = -v_0\sin\beta\,\sin\omega_c t,\qquad v_y = v_0\sin\beta\,\cos\omega_c t.}
$$

### Question 33*

En intégrant avec $x(0)=y(0)=0$ :

$$
\boxed{x(t) = \frac{v_0\sin\beta}{\omega_c}\big(\cos\omega_c t - 1\big),\qquad y(t) = \frac{v_0\sin\beta}{\omega_c}\sin\omega_c t,\qquad z(t) = v_0\cos\beta\,t.}
$$

### Question 34*

Pour $\beta = \pi/2$ : $z = 0$, mouvement plan, et

$$
\left(x + \frac{v_0}{\omega_c}\right)^2 + y^2 = \left(\frac{v_0}{\omega_c}\right)^2.
$$

C'est un **cercle** de centre $(-v_0/\omega_c, 0)$ et de rayon

$$
\boxed{r_C = \frac{v_0}{\omega_c} = \frac{m_e v_0}{eB}.}
$$

Schéma : $\vec B = B\vec u_z$ sortant, $\vec v_0 = v_0\vec u_y$ à $t=0$ ; la force initiale courbe la trajectoire vers $-x$ ; parcours circulaire dans le sens trigonométrique vu de $+z$.

### Question 35*

La source (spire circulaire d'axe $Oz$) est **invariante par toute rotation autour de $Oz$**. Les grandeurs physiques qui en découlent ne dépendent pas de $\theta$ (coordonnées cylindriques) : $B(M) = B(r,z)$.

### Question 36*

Le plan méridien $\Pi$ contenant $M$ et l'axe $Oz$ est un **plan d'antisymétrie des courants** : par réflexion dans $\Pi$, la spire est conservée mais le courant azimutal change de sens. Le champ magnétique étant un **pseudo-vecteur**, pour $M \in \Pi$ il est **contenu** dans ce plan ; sa composante orthoradiale est nulle :

$$
\boxed{\vec B(M) = B_r(r,z)\,\vec u_r + B_z(r,z)\,\vec u_z.}
$$

### Question 37*

Un point $P$ de l'axe appartient à **tous** les plans méridiens (plans d'antisymétrie des courants). $\vec B(P)$, contenu dans chacun, est porté par leur intersection commune, l'axe $Oz$ :

$$
\boxed{\vec B(P) = B_a(z)\,\vec u_z.}
$$

### Question 38

Sur l'axe, $\vec B = B_a(z)\vec u_z$ est colinéaire à $\vec v_0 \parallel Oz$ : la force $-e\,\vec v\wedge\vec B$ reste nulle, la trajectoire demeure **rectiligne le long de $Oz$** (électron non dévié).

### Question 39*

En optique géométrique, « faible étendue radiale » ($r \ll a$) et « angle $\beta$ faible » correspondent exactement aux **conditions de l'approximation de Gauss** (rayons paraxiaux).

### Question 40

$B_a(z) = \dfrac{B_0}{(1+z^2/a^2)^{3/2}}$ : courbe en cloche, paire, maximale ($B_0$) en $z=0$, tendant vers 0 à l'infini. Schéma : axes $z$ et $B_a$ nommés, maximum $B_0$ repéré en $z=0$, valeur $B_0/2$ repérée. $B_a = B_0/2$ pour $(1+z^2/a^2)^{3/2} = 2$, soit

$$
\boxed{\ell = a\sqrt{2^{2/3}-1} \approx 0{,}77\,a.}
$$

### Question 41

$$
B_0 = \frac{\mu_0 N I}{2a} = \frac{4\pi\times10^{-7}\times600\times4{,}0}{2\times0{,}040} \approx \boxed{3{,}8\times10^{-2}\ \text{T} = 38\ \text{mT}}.
$$

Comparé au champ terrestre ($\sim 5\times10^{-5}$ T) : $B_0/B_T \approx 7\times10^{2}$ — négliger le champ terrestre est justifié.

### Question 42

Force magnétique $\sim e v_0 B_0 \approx 1{,}6\times10^{-19}\times6\times10^{7}\times3{,}8\times10^{-2} \approx 3{,}6\times10^{-13}$ N ; poids $m_e g \approx 8{,}9\times10^{-30}$ N. Le rapport $\dfrac{m_e g}{e v_0 B_0} \approx 2\times10^{-17} \ll 1$ : le poids est totalement négligeable.

### Question 43

Ligne 19 : `B0 = mu0*N*I/(2*a)`.
L'équation (4) s'écrit $\dfrac{\mathrm d^2r}{\mathrm dz^2} = -\dfrac{e^2}{4m_e^2v_0^2}B_a^2(z)\,r$ avec $B_a^2 = \dfrac{B_0^2}{(1+z^2/a^2)^3}$ ; le code posant $A = \left(\dfrac{B_0 e}{2m v_0}\right)^2 a$, on a $\dfrac{e^2B_0^2}{4m_e^2v_0^2} = \dfrac{A}{a}$, donc

$$
\frac{\mathrm d^2r}{\mathrm dz^2} = -\frac{A}{a}\,\frac{r}{(1+z^2/a^2)^3}.
$$

Ligne 35 : `return([rprime, -A*r/(a*(1+(z/a)**2)**3)])`.

### Question 44

Dans la boucle, l'angle d'initialisation est `tan(beta/(i+1))` ; la plus grande valeur ($i=0$) vaut $\beta$. Pour $5^\circ$ : ligne 25, `beta = 5*np.pi/180`.

### Question 45

$\beta_{\max} = 5^\circ = 8{,}7\times10^{-2}$ rad $\ll 1$ : hypothèse (H2) vérifiée. Sur la figure 12, $\max(r/a) \approx 0{,}048 \ll 1$ : hypothèse (H4) ($r \ll a$) vérifiée.

### Question 46

En considérant $r \approx r_0$ constant dans la zone d'épaisseur $2\ell$ (approximation « lentille mince »), l'intégration de (4) entre $-\ell$ et $\ell$ donne

$$
\left.\frac{\mathrm dr}{\mathrm dz}\right|_{\ell} - \left.\frac{\mathrm dr}{\mathrm dz}\right|_{-\ell} = -\frac{e^2}{4m_e^2v_0^2}\,r_0\int_{-\ell}^{\ell}B_a^2\,\mathrm dz = -\frac{e^2}{4m_e^2v_0^2}\,r_0\,\Gamma.
$$

Avec $\left.\dfrac{\mathrm dr}{\mathrm dz}\right|_{-\ell} = -\dfrac{r_0}{\overline{OA}}$ et $\left.\dfrac{\mathrm dr}{\mathrm dz}\right|_{\ell} = -\dfrac{r_0}{\overline{OA'}}$, on divise par $r_0$ :

$$
\frac{1}{\overline{OA'}} - \frac{1}{\overline{OA}} = \frac{e^2\Gamma}{4m_e^2v_0^2},
$$

relation de conjugaison de lentille mince avec

$$
\boxed{f' = \frac{4m_e^2v_0^2}{e^2\,\Gamma}}\quad (f' > 0,\ \text{lentille convergente}).
$$

### Question 47

À tension $U$ (donc $v_0$) fixée, $f' = \dfrac{4m_e^2v_0^2}{e^2\Gamma}$ : rapprocher $A'$ de $A$ revient à **diminuer $f'$**, donc **augmenter $\Gamma = \int B_a^2\,\mathrm dz$**, c'est-à-dire augmenter le champ, donc le **produit $NI$** (nombre de spires ou intensité).

### Question 48

$f' = \dfrac{32}{3\pi a}\left(\dfrac{m_e v_0}{eB_0}\right)^2$. Avec $a = 0{,}040$ m, $B_0 = 0{,}040$ T, $v_0 = 6{,}0\times10^{7}$ m/s : $\dfrac{m_e v_0}{eB_0} \approx 8{,}5\times10^{-3}$ m, d'où

$$
f' = \frac{32}{3\pi\times0{,}040}\times(8{,}5\times10^{-3})^2 \approx \boxed{6\ \text{mm}}.
$$

Une focale aussi courte est **inaccessible à une lentille de verre** en optique photonique : les lentilles magnétiques permettent des focales très faibles, d'où un fort grandissement.

---

## Partie 4 — Microscope à effet tunnel

### Question 49*

Interprétation de Born : $|\Psi(x,t)|^2\,\mathrm dx$ est la **probabilité de présence** de la particule dans $[x, x+\mathrm dx]$ à l'instant $t$ ; $\rho = |\Psi|^2$ est la **densité linéique de probabilité de présence**.

### Question 50*

Énergie mécanique $E = \tfrac{p^2}{2m} + W = \tfrac{\hbar^2 k^2}{2m} + W$, exprimée en joules :

$$
\boxed{E = \frac{\hbar^2 k^2}{2m} + W \;\text{[J]}.}
$$

Un état stationnaire est de la forme $\Psi(x,t) = \varphi(x)e^{-iEt/\hbar}$, donc $|\Psi(x,t)|^2 = |\varphi(x)|^2$ **indépendant du temps**.

### Question 51*

En injectant $\Psi = \varphi(x)e^{-iEt/\hbar}$ dans l'équation de Schrödinger $\hat H\Psi = i\hbar\,\partial\Psi/\partial t$ avec $\hat H = -\dfrac{\hbar^2}{2m}\dfrac{\mathrm d^2}{\mathrm dx^2} + W(x)$, il vient l'équation de Schrödinger **stationnaire** :

$$
\boxed{-\frac{\hbar^2}{2m}\,\varphi''(x) + W(x)\varphi(x) = E\varphi(x),}\qquad\text{soit}\qquad \boxed{\varphi''(x) + \frac{2m}{\hbar^2}\big(E - W(x)\big)\varphi(x) = 0.}
$$

### Question 52

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

$\varphi$ et $\varphi' = \mathrm d\varphi/\mathrm dz$ (les coefficients de l'équation étant finis par morceaux) sont **continus** aux raccords en $z = 0$ et $z = b$ : quatre équations linéaires reliant $A, B, C, D, F$.

### Question 54

Dans la barrière, la partie spatiale est une combinaison d'exponentielles réelles en $z$ : les solutions sont **évanescentes**, et non des ondes planes oscillantes. La longueur de décroissance d'une exponentielle est $1/q$.

Sur une barrière d'épaisseur finie, il faut garder les deux exponentielles avec des coefficients complexes. Le courant total n'est pas nécessairement nul :
$$J_z=\frac{\hbar}{m_e}\operatorname{Im}(\varphi_2^*\varphi_2')=\frac{2\hbar q}{m_e}\operatorname{Im}(D^*C).$$
Une exponentielle isolée a un courant nul ; leur combinaison raccordée aux deux régions de propagation permet un courant transmis non nul. Il ne s'agit pas d'une onde progressive absorbée par un milieu dissipatif.

### Question 55

Un exemple est la **réflexion totale interne en optique** : lorsqu'une onde passe d'un milieu d'indice élevé vers un milieu d'indice plus faible au-delà de l'angle critique, le champ transmis est évanescent suivant la normale à l'interface. Il peut exister dans le second milieu même si aucune onde propagative ne transporte l'énergie loin de l'interface dans cette direction.

Comme $q$ intervient dans $e^{-qz}$, il est homogène à l'inverse d'une longueur. Ainsi
$$\boxed{\delta=\frac1q=\frac{\hbar}{\sqrt{2m_e(W_s-E)}}}$$
est une **longueur de pénétration** : après une distance $\delta$, l'amplitude de l'exponentielle décroissante est divisée par $e$ (la densité de probabilité par $e^2$).

### Question 56

Le vecteur $\vec J$ est une **densité de courant de probabilité**. Le flux $\vec J\cdot\vec n\,dS\,dt$ représente la probabilité transportée à travers la surface orientée $dS$ pendant $dt$ ; dans le modèle unidimensionnel, $J_zdt$ est la probabilité traversant un point durant cet intervalle. L'équation de continuité est
$$\partial_t\rho+\operatorname{div}\vec J=0.$$
L'analogie est celle du transport de masse, avec $\vec j_m=\rho_m\vec v$, ou du transport de charge avec $\vec j_e=\rho_e\vec v$. Ici, pour l'onde plane donnée,
$$\vec J=|\Psi|^2\frac{\hbar k}{m_e}\vec u_z,$$
et $\hbar k/m_e$ joue le rôle de la vitesse de transport de la probabilité.

### Question 57

$T = \dfrac{J_{\text{transmise}}}{J_{\text{incidente}}}$ est la **probabilité de transmission** (de traversée) de la barrière. Classiquement, pour $E < W_s$ la particule rebrousse chemin : la barrière est **infranchissable** ; en mécanique quantique, $T > 0$ : c'est l'**effet tunnel**.

### Question 58

Une **barrière épaisse** vérifie $qb\gg1$ : sa largeur est grande devant la longueur de pénétration $1/q$. Alors
$$\sinh(qb)=\frac{e^{qb}-e^{-qb}}2\simeq\frac{e^{qb}}2,$$
et donc $\gamma\sinh^2(qb)\gg1$. La formule exacte fournie devient
$$T\simeq\frac{4}{\gamma}e^{-2qb}.$$
En remplaçant $\gamma=W_s^2/[4E(W_s-E)]$ :
$$\boxed{T\simeq16\frac{E}{W_s}\left(1-\frac{E}{W_s}\right)e^{-2qb}.}$$
Il n'est pas nécessaire de supposer $E\ll W_s$ : on conserve tout le préfacteur.

### Question 59

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

Le modèle fourni impose
$$\boxed{\Delta x_{\min}\simeq\sqrt{\frac{2z'}{k_0}}.}$$
$z'$ mesure la distance de la surface au **centre** de l'atome terminal de la pointe. La séparation géométrique est de l'ordre de $0,1$ nm ; en ajoutant une longueur atomique de l'ordre de $0,1$ nm, on estime $z'\sim0,2$ nm. Ainsi
$$\Delta x_{\min}\sim\sqrt{\frac{2\times2\times10^{-10}}{1,09\times10^{10}}}\simeq1,9\times10^{-10}\ \mathrm m.$$
L'ordre de grandeur est donc **$0,1$ à $0,2$ nm**. Si l'on assimile au premier ordre $z'$ à $0,1$ nm, on obtient $0,14$ nm ; ce choix géométrique doit être explicité. La résolution latérale est d'ordre atomique et moins fine que la résolution verticale.

### Question 62

La résolution verticale obtenue est de l'ordre de $0,6$ pm, très inférieure aux dimensions atomiques. La résolution latérale, de l'ordre de $0,1$ à $0,2$ nm, est comparable aux distances entre atomes : des sites atomiques voisins peuvent être distingués.

**Le microscope accède donc à une image de résolution atomique.** Cette image est une cartographie du courant tunnel ou de la hauteur nécessaire pour le maintenir constant ; son contraste dépend aussi de la densité électronique locale. « Voir les atomes » ne signifie pas obtenir une photographie optique de sphères matérielles.

### Question 63

Sur le graphite, l'image fait apparaître un **sous-réseau** de paramètre $d_{\exp} \approx 0{,}25$ nm : seuls certains atomes (un sur deux du réseau hexagonal, ceux qui contribuent à la densité d'états au niveau de Fermi) apparaissent. La distance C–C du graphite vaut $0{,}142$ nm : $d_{\exp}/d_{CC} \approx 1{,}73 \approx \sqrt{3}$, caractéristique du sous-réseau imagé. Schéma : maille hexagonale annotée, $d_{CC} = 0{,}142$ nm et $d_{\exp} = \sqrt{3}\,d_{CC} \approx 0{,}25$ nm repérés.

### Question 64

Les vaguelettes sont des **interférences d'ondes électroniques de surface**, réfléchies et diffusées par les atomes de fer qui délimitent l'enclos. Le courant tunnel révèle les variations de densité locale d'états associées aux modes confinés ; les crêtes ne sont pas des rangées d'atomes supplémentaires.

Pour une estimation à une puissance de dix près, choisissons explicitement une énergie cinétique de l'ordre de $1$ eV pour un électron de surface : cette valeur est une hypothèse d'ordre de grandeur, non une donnée de l'énoncé. Avec la masse de l'électron libre,
$$\lambda_{dB}=\frac{h}{\sqrt{2m_eE_c}}\simeq\frac{6,62\times10^{-34}}{\sqrt{2\times9,11\times10^{-31}\times1,60\times10^{-19}}}\simeq1,2\times10^{-9}\ \mathrm m.$$
La longueur d'onde est **nanométrique**, de sorte que plusieurs oscillations peuvent tenir dans l'enclos de rayon $7,13$ nm. La figure montre bien quelques anneaux sur cette longueur. Pour une superposition locale d'ondes opposées, le contraste de densité est proportionnel à un carré d'amplitude et sa période spatiale est de l'ordre de $\lambda/2$.

Un ajustement quantitatif de la période nécessite la dispersion et la masse effective des états de surface du cuivre : l'énergie de Fermi du métal massif ne doit pas être substituée sans justification. À titre de contrôle d'un calcul souvent proposé, prendre $E_c=7$ eV avec la masse libre donnerait $0,46$ nm, et non $2$ nm.

