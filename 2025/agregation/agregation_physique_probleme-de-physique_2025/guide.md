# Agrégation Physique — Problème de physique 2025 · Corrigé guidé

*Corrigé rédigé par IA, non officiel. Signalez toute erreur.*

## Présentation du sujet

**Thème.** « Manipulation de macromolécules uniques » : le sujet modélise les **pinces magnétiques**, qui manipulent une molécule d'ADN unique accrochée entre une lame de verre et une microbille superparamagnétique. Trois registres du programme de l'agrégation de physique sont mobilisés : **électromagnétisme** (dipôle magnétique, matériaux magnétiques), **mécanique** (pendule, oscillateur harmonique, milieux continus élastiques) et **thermodynamique / physique statistique** (marche aléatoire, statistique de Boltzmann, équipartition), plus **optique** (diffraction de Fraunhofer) et un peu d'**informatique** (moindres carrés en Python). Épreuve de 6 heures, calculatrice autorisée, 66 questions en trois parties.

**Découpage.**

| Partie | Questions | Contenu | Notions du programme |
|---|---|---|---|
| A | Q1–Q33 | Fonctionnement du dispositif : champ de deux aimants (A.1), mesure de force par fluctuations browniennes puis analyse de Fourier (A.2), mesure de position par diffraction (A.3) | dipôle magnétique, superparamagnétisme, loi d'Arrhenius, oscillateur harmonique, équipartition, bruit blanc et TF, diffraction de Fraunhofer, Babinet |
| B | Q34–Q49 | Élasticité entropique de l'ADN : chaîne librement jointe 1D puis 3D, approche thermodynamique | marche aléatoire, système à deux niveaux, fonction de Langevin, entropie statistique |
| C | Q50–Q66 | ADN comme longue tige flexible : traction, flexion, longueur de persistance, retour sur le « modèle du ver » | loi de Hooke, module de Young, énergie de courbure, équipartition, fonction de corrélation |

**Difficulté et longueur.** Sujet long (66 questions) mais très balisé. Le rapport du jury 2025 relève : moyenne **6,14/20** sur 456 copies (59 % sous la moyenne, quartiles 3,32 / 5,43 / 7,85), « taux moyen de réussite […] aux questions abordées […] autour de 27 % », barème total 188 points (A : 100, B : 48, C : 40). Partie A la plus rentable (taux 37 %) mais A.1 « anormalement » faible (magnétisme) ; B.2 (élasticité entropique), C.3 (milieux continus) et C.4 (vision globale) les plus difficiles (taux 21–26 %). Questions 22–24 (Fourier) particulièrement bien réussies (85 %).

**Barème et taux de réussite du rapport 2025** (188 points au total) :

| Partie | Points | Taux de réussite | % de candidats ayant traité |
|---|---|---|---|
| A (dispositif) | 100 | 37 % | 100 % |
| — A.1 (aimants, bille) | 40 | 42 % | 100 % |
| — A.2 (mesure de force) | 42 | 40 % | 96 % |
| — A.3 (mesure de position) | 19 | 32 % | 98 % |
| B (élasticité de l'ADN) | 48 | 23 % | 79 % |
| — B.1 | 4 | 48 % | 82 % |
| — B.2 (élasticité entropique) | 34 | 26 % | 72 % |
| — B.3 (thermodynamique) | 10 | 37 % | 70 % |
| C (tige flexible) | 40 | 21 % | 43 % |
| — C.1 | 6 | 53 % | 71 % |
| — C.2 | 9 | 44 % | 56 % |
| — C.3 (flexion) | 13 | 26 % | 63 % |
| — C.4 (vision globale) | 12 | 25 % | 34 % |

**Questions pièges signalées par le jury.** Q12–15 (signes en mécanique : équilibre *stable*, signe + dans l'équation de l'oscillateur), Q18–19 (moyenne vs variance vs écart-type), Q35 (extension ≠ longueur bout-à-bout, 9 % de réussite), Q54 (facteur ½ de l'intégration du travail), et rigueur exigée sur les questions de cours (magnétisme, optique, élasticité).

**Préambule du sujet.** L'énoncé fournit les formules utiles (champ dipolaire, loi d'Arrhenius, loi de Stokes, intégrales usuelles dont $\int_{-1}^{1}x^2\sqrt{1-x^2}\,dx = \pi/8$, DL de la fonction de Langevin) et les données numériques (géométrie des aimants, $K$, $m_{\text{sat}}$, $\Delta B/\Delta z$, rayon de la bille, $\eta$, $a$, $\lambda$, taille des pixels, $L$, diamètre de l'ADN, 0,34 nm/pb, ajustement $k$ de la Figure 7) : les mobiliser explicitement, avec unités, fait partie de la rigueur attendue.

**Gestion du temps.** Commencer par la partie A en entier (soigner A.1, discriminant) ; enchaîner Q22–24 (Fourier, « réservoir de points ») ; aborder B.1 puis le début guidé de B.2 (Q36–43) ; finir par C.1 (estimation) puis C.3/C.4 en fin d'épreuve. Environ 2 h 30 pour A, 2 h pour B, 1 h 30 pour C.

**Ordre de traitement conseillé.** Le rapport relève que 156/456 candidats ont abordé plus de 40/66 questions et que 22 ont dépassé 60 questions : la gestion du temps est décisive. Commencer par A en entier (partie la plus rentable, 37 % de réussite, 100 % de candidats l'ayant traitée), en soignant A.1 (magnétisme, point faible collectif donc discriminant). Enchaîner immédiatement le bloc Fourier Q22–24 (85 % de réussite sur les copies les ayant abordées) et le début guidé de B.2 (Q36–43, système à deux niveaux). Garder C.1 (estimation, 53 %) pour le milieu de copie, et réserver C.3/C.4 (milieux continus, vision globale ; 17 % de candidats seulement ont abordé C.4) pour la fin, même au prix d'une conclusion rapide.

---

## Partie A — Fonctionnement du dispositif

La partie A décrit le dispositif expérimental : création du champ magnétique par deux aimants permanents, comportement superparamagnétique de la microbille, mesure de la force de traction (par les fluctuations thermiques de la bille, puis par analyse de Fourier de ces fluctuations), et mesure de position par diffraction de la lumière. Les outils sont le calcul dipolaire, la mécanique du point (équilibre, PFD, énergie) et l'analyse spectrale d'un oscillateur brownien.

**A.1. Piégeage de la bille magnétique**

> [!JURY]
> « On peut remarquer un taux de réussite "anormalement" faible pour la partie A.1, portant sur le magnétisme et impliquant non seulement quelques calculs qui peuvent avoir déstabilisé certains candidats en début de problème, mais aussi des réflexions plus fines sur les caractéristiques d'un matériau super-paramagnétique. » Et : « des lacunes sur des domaines de physique assez fondamentaux ont aussi été remarquées dans certains cas (magnétisme, optique, élasticité) ». (rapport 2025, p. 30-31/66)

### Question 1

> [!INDICATION]
> Écrire l'énergie potentielle d'interaction d'un dipôle avec le champ, puis en déduire couple et force par dérivation (à moment fixé).

> [!INDICATION]
> Vérifier le signe de $E_p$ (dipôle stable aligné sur $\vec B$) et la condition de non-uniformité du champ pour une force non nulle.

#### Solution

$$
E_p = -\vec M\cdot\vec B,\qquad \vec\Gamma = \vec M\times\vec B,\qquad \boxed{\vec F = \vec\nabla(\vec M\cdot\vec B).}
$$

Force non nulle seulement si $\vec B$ non uniforme (un champ uniforme ne produit qu'un couple).

### Question 2

> [!INDICATION]
> Appliquer la formule du champ dipolaire à chaque aimant au point O, en orientant correctement le vecteur r (de la source vers le point). Les deux contributions selon x s'ajoutent.

> [!INDICATION]
> Schéma lisible avec les deux dipôles et le vecteur $\vec r$ orienté de la source vers le point $O$ ; sommer les deux contributions selon $\vec e_x$.

#### Solution

$$
\boxed{\vec B(O) = \frac{\mu_0}{4\pi}\,\frac{32M}{d^3}\,\vec e_x = \frac{8\mu_0 M}{\pi d^3}\,\vec e_x.}
$$

### Question 3

> [!INDICATION]
> En un point P = (0, z) à égale distance des deux aimants, invoquer la symétrie : quelles composantes se compensent ?

> [!INDICATION]
> Poser $\rho = \sqrt{(d/2)^2+z^2}$ ; les composantes verticales se compensent par symétrie ; vérifier la cohérence avec la Q2 en $z=0$.

#### Solution

$$
\boxed{\vec B(P) = \frac{\mu_0 M}{2\pi}\,\frac{d^2/2 - z^2}{\big((d/2)^2+z^2\big)^{5/2}}\,\vec e_x,\qquad \text{annulation en } z = \pm\frac{d}{\sqrt2}.}
$$

### Question 4

> [!INDICATION]
> Donner les trois définitions (linéaire, homogène, isotrope) et la relation constitutive générale, avec les unités de chaque champ.

> [!INDICATION]
> Ne pas confondre dimension et unité : $\vec H$ et $\vec M$ en A·m⁻¹, $\vec B$ en T.

#### Solution

$$
\boxed{\vec B = \mu_0(\vec H + \vec M)}
$$

($\vec B$ en T ; $\vec H$ et $\vec M$ en A·m⁻¹).

### Question 5

> [!INDICATION]
> Linéariser M(H) au premier ordre (M = χm H) et réinjecter dans la relation de la Q4.

> [!INDICATION]
> $\chi_m$ est sans dimension ; $1+\chi_m$ est la perméabilité relative $\mu_r$.

#### Solution

$$
\boxed{\mu = \mu_0(1+\chi_m).}
$$

### Question 6

> [!INDICATION]
> Associer chaque courbe à sa signature physique : signe de la pente, saturation, hystérésis.

> [!INDICATION]
> Justifier par le comportement physique (alignement des moments, domaines de Weiss), pas seulement par l'allure des courbes.

#### Solution

(A) pente négative : **diamagnétique** ; (B) pente positive : **paramagnétique** ; (C) saturation + hystérésis : **ferromagnétique**.

### Question 7

> [!INDICATION]
> Comparer le temps de mesure au temps de retournement τ : que vaut la moyenne temporelle de l'aimantation si τmes ≫ τ ? Y a-t-il rémanence ?

> [!INDICATION]
> Argument temporel : $\tau_{\text{mes}} \gg \tau$ ⇒ basculements nombreux pendant la mesure ; équiprobabilité des deux orientations en champ nul.

#### Solution

Moyenne temporelle nulle en champ nul (deux orientations équiprobables) : **superparamagnétisme** = paramagnétisme d'un moment géant de mono-domaine, **sans rémanence**.

### Question 8

> [!INDICATION]
> Inverser la loi d'Arrhenius τ = τ0 exp(Kv/kBT) à la condition de blocage τmes = τ.

> [!INDICATION]
> Attention au sens de l'inégalité : $T < T_B \Leftrightarrow \tau > \tau_{\text{mes}}$ (particule bloquée).

#### Solution

$$
\boxed{T_B = \frac{Kv}{k_B\ln(\tau_{\text{mes}}/\tau_0)}},
$$

bloquée si $T < T_B$ (retournement trop lent).

### Question 9

> [!INDICATION]
> Imposer TB ≥ 300 K pour en déduire le volume minimal, puis convertir en diamètre de sphère.

> [!INDICATION]
> Conserver les unités dans l'A.N. ; conclure sur un ordre de grandeur réaliste (quelques nm).

#### Solution

$v \geq 2{,}4\times10^{-25}\ \text{m}^3$, d'où $\boxed{D \approx 7{,}6\ \text{nm}}$ (quelques nm).

### Question 10

> [!INDICATION]
> Tracer m(B) : quelle allure à faible champ, à fort champ, et y a-t-il hystérésis ?

> [!INDICATION]
> Légender le tracé (axes, pente à l'origine, $\pm m_{\text{sat}}$) ; absence d'hystérésis = absence de rémanence.

#### Solution

Courbe impaire, linéaire à l'origine puis saturation à $\pm m_{\text{sat}}$, **sans hystérésis** : paramagnétique saturable (signature du superparamagnétisme).

### Question 11

> [!INDICATION]
> Dériver l'énergie magnétique à saturation pour obtenir la force ; estimer ∇B par ΔB/Δz.

> [!INDICATION]
> Le facteur $\tfrac12$ vient de la construction progressive de l'aimantation ; estimer $\vec\nabla B$ par $\Delta B/\Delta z$.

#### Solution

$$
\vec F = \frac12 m_{\text{sat}}\vec\nabla B,\qquad \|\vec\nabla B\| \sim \frac{0{,}5}{5\times10^{-3}} = 100\ \text{T/m},\qquad \boxed{F \approx 5\times10^{-11}\ \text{N} \approx 50\ \text{pN}.}
$$

## A.2. Mesures de force

### A.2.1. Modèle de pendule inversé

### Question 12

> [!INDICATION]
> Bilan des forces (le poids est négligé ; un fil ne peut que tirer). Quelle position d'équilibre est compatible avec la direction de la tension ?

> [!INDICATION]
> Vérifier la stabilité par le signe de la dérivée seconde de l'énergie potentielle.

#### Solution

$\vec F + \vec F_t = \vec 0$ avec $\vec F_t$ dirigée vers l'ancrage impose $\boxed{\beta = 0}$ ; $E_p = -FL\cos\beta$ est minimale en $\beta = 0$ : équilibre **stable**.

> [!JURY]
> Sur les questions 12 à 15 : « un nombre trop important de candidats […] a proposé une expression de l'énergie potentielle où la position d'équilibre était instable. Plus grave encore, cela a pu conduire à écrire une équation différentielle avec un signe opposé, mais qui a néanmoins été présentée comme l'équation de l'oscillateur harmonique ! » (rapport 2025, p. 31/66)

### Question 13

> [!INDICATION]
> Projeter le PFD sur la base cylindrique (er, eθ) en décomposant ez. Quelle équation sur β (signe !), quelle expression de la tension ?

> [!INDICATION]
> Projeter $\vec e_z = \cos\beta\,\vec e_r - \sin\beta\,\vec e_\theta$ ; le terme en $F\sin\beta$ doit être un rappel (signe +).

#### Solution

$$
\boxed{mL\ddot\beta + F\sin\beta = 0}\qquad\text{(rappel vers }\beta=0\text{),}\qquad \boxed{F_t = F\cos\beta + mL\dot\beta^2.}
$$

### Question 14

> [!INDICATION]
> Approche énergétique : écrire Ep, Ec, Em ; justifier que la tension ne travaille pas ; dériver Em(t) = cte.

> [!INDICATION]
> Justifier que la tension ne travaille pas (perpendiculaire à la vitesse) avant de dériver $E_m$.

#### Solution

$$
E_m = \frac12 mL^2\dot\beta^2 - FL\cos\beta,\quad \vec F_t\cdot\vec v = 0,\quad \frac{dE_m}{dt}=0 \Rightarrow mL\ddot\beta + F\sin\beta = 0
$$

(identique à Q13).

### Question 15

> [!INDICATION]
> Linéariser sin β à l'ordre 1 et reconnaître l'oscillateur harmonique.

> [!INDICATION]
> $\sin\beta \approx \beta$ à l'ordre 1 ; vérifier la cohérence du signe avec la Q13.

#### Solution

$$
\ddot\beta + \frac{F}{mL}\beta = 0,\qquad \boxed{\omega_0 = \sqrt{F/(mL)}.}
$$

### Question 16

> [!INDICATION]
> Nommer le moteur des oscillations observées en présence de solvant : qui excite, qui amortit ?

> [!INDICATION]
> Deux effets du solvant : excitation aléatoire (mouvement brownien) et amortissement (viscosité).

#### Solution

**Agitation thermique (brownienne)** qui excite, **viscosité** qui amortit : oscillateur harmonique amorti forcé par un bruit thermique (Langevin).

### A.2.2. Fluctuations thermiques

### Question 17

> [!INDICATION]
> DL de Ep(β) à l'ordre 2, puis passer à x = L sin β ≈ Lβ. Quelle raideur apparente ?

> [!INDICATION]
> DL de $\cos\beta$ à l'ordre 2 ; passer à $x = L\sin\beta \approx L\beta$.

#### Solution

$$
\boxed{E_p(x) \approx -FL + \frac12\frac FL x^2,}\qquad k = F/L.
$$

### Question 18

> [!INDICATION]
> Appliquer l'équipartition au degré de liberté x. Attention : que lit-on sur l'histogramme, la variance ou l'écart-type ?

> [!INDICATION]
> $\langle x\rangle = 0$ donc variance $= \langle x^2\rangle = (\text{écart-type})^2$ : ne pas confondre.

#### Solution

$$
\frac12\frac FL\langle x^2\rangle = \frac12 k_BT\ \Rightarrow\ \boxed{F = \frac{Lk_BT}{\langle x^2\rangle}},\qquad \langle x^2\rangle = \text{variance} = (\text{écart-type})^2.
$$

> [!JURY]
> « Les questions 18 et 19 […] n'ont également pas souvent été bien traitées (notamment à cause de confusions entre moyenne, variance et écart type). » (rapport 2025, p. 31/66)

### Question 19

> [!INDICATION]
> Lire l'écart-type sur la Figure 5, l'élever au carré, et appliquer la Q18 avec les données numériques.

> [!INDICATION]
> Lire l'écart-type sur la Figure 5, l'élever au carré, puis A.N. avec $L$ et $k_BT$.

#### Solution

$\sqrt{\langle x^2\rangle} \approx 0{,}15\ \mu$m, d'où $\boxed{F \approx 3\ \text{pN}}$ (ordre du pN acceptable).

### Question 20

> [!INDICATION]
> Écrire la statistique de Boltzmann ; conclure sur la forme de P(x) puisque Ep est quadratique.

> [!INDICATION]
> Potentiel quadratique ⇒ gaussienne (Boltzmann) ; variance $= Lk_BT/F$.

#### Solution

$$
\mathcal P(x) \propto e^{-Fx^2/(2Lk_BT)} :\ \text{gaussienne de variance } Lk_BT/F.
$$

### A.2.3. Analyse de Fourier

### Question 21

> [!INDICATION]
> Nommer chaque terme de l'équation de Langevin : inertie, frottement, rappel, bruit.

> [!INDICATION]
> Quatre termes : inertie, frottement visqueux, rappel élastique, force aléatoire de Langevin.

#### Solution

$m\ddot x$ : inertie ; $-\gamma\dot x$ : frottement visqueux (Stokes) ; $-\tfrac FL x$ : rappel élastique ($k=F/L$) ; $\xi(t)$ : force aléatoire (bruit thermique).

### Question 22

> [!INDICATION]
> Négliger l'inertie, passer en Fourier (TF de la dérivée = iω), résoudre pour X(ω).

> [!INDICATION]
> Négliger $m\ddot x$ (régime basse fréquence) ; $\mathrm{TF}[\dot x] = i\omega X$.

#### Solution

$$
\boxed{X(\omega) = \frac{\Xi(\omega)}{F/L + i\gamma\omega}.}
$$

### Question 23

> [!INDICATION]
> Prendre le module carré et factoriser par (F/L)² pour retrouver la forme (3). Quels A et ωc ?

> [!INDICATION]
> Factoriser le dénominateur par $(F/L)^2$ pour lire $A$ et $\omega_c$.

#### Solution

$$
\boxed{A = \frac{L^2}{F^2},\qquad \omega_c = \frac{F}{\gamma L}.}
$$

> [!JURY]
> « Les questions 22 à 24 qui portaient sur l'analyse de Fourier ont été particulièrement bien réussies (85 %) par les candidats les ayant abordées. » (rapport 2025, p. 31/66)

### Question 24

> [!INDICATION]
> Injecter le bruit blanc Sξξ = 2γkBT ; reconnaître la forme.

> [!INDICATION]
> Bruit blanc de fluctuation-dissipation : $S_{\xi\xi} = 2\gamma k_BT$ ; forme lorentzienne.

#### Solution

$$
\boxed{S_{xx}(\omega) = \frac{2\gamma k_BT L^2/F^2}{1+(\omega/\omega_c)^2}}
$$

: lorentzienne de fréquence de coupure $\omega_c = F/(\gamma L)$.

> [!METHODE]
> Chaîne d'analyse spectrale d'un oscillateur brownien : négliger l'inertie aux basses fréquences → TF de l'équation de Langevin → module carré → bruit blanc de fluctuation-dissipation (Sξξ = 2γkBT) → lorentzienne dont la coupure donne la raideur, donc la force.

### Question 25

> [!INDICATION]
> Loi de Stokes γ = 6πηr : attention, r est le rayon (moitié du diamètre de 1 µm).

> [!INDICATION]
> Rayon $r = 0{,}5\ \mu$m (et non le diamètre de 1 µm).

#### Solution

$$
\boxed{\gamma = 6\pi\eta r \approx 9{,}4\times10^{-9}\ \text{N}\cdot\text{s}\cdot\text{m}^{-1}.}
$$

### Question 26

> [!INDICATION]
> Lire fc sur la Figure 6, puis F = γLωc = γL·2πfc ; comparer à la Q19.

> [!INDICATION]
> $f_c \approx 1$ Hz sur le spectre ; $F = \gamma L\cdot 2\pi f_c$ ; cohérence avec la Q19.

#### Solution

$f_c \approx 1$ Hz, d'où $\boxed{F \approx 1\ \text{pN}}$, cohérent avec la méthode directe (Q19).

## A.3. Mesures de position

### A.3.1. Position horizontale

### Question 27

> [!INDICATION]
> Quelles conditions définissent la diffraction de Fraunhofer (champ lointain) ? Quelle figure pour une pupille circulaire ?

> [!INDICATION]
> Condition de champ lointain $z \gg a^2/\lambda$ ; amplitude = TF de la pupille ; premier anneau sombre en $1{,}22\lambda/a$.

#### Solution

Fraunhofer : source et écran à l'infini (plans focaux), condition $z \gg a^2/\lambda$ ; amplitude = TF spatiale de la pupille. Pupille circulaire → **tache d'Airy** : disque central + anneaux concentriques, premier anneau sombre en $\theta_1 \simeq 1{,}22\lambda/a$.

### Question 28

> [!INDICATION]
> La bille opaque est l'écran complémentaire d'une ouverture circulaire : quel théorème compare leurs figures ? Que diffère au centre ?

> [!INDICATION]
> Babinet : écrans complémentaires ⇒ mêmes figures hors axe ; tache d'Arago-Poisson au centre.

#### Solution

**Théorème de Babinet** : mêmes anneaux d'Airy hors axe ; au centre, faisceau transmis + point brillant (tache d'Arago-Poisson), contrastes inversés.

### Question 29

> [!INDICATION]
> Dans le plan focal image d'une lentille de focale f', la direction θ se projette en r = f' tan θ ≈ f'θ. Quel diamètre pour le premier anneau sombre ?

> [!INDICATION]
> Plan focal image : $r = f'\tan\theta \approx f'\theta$ ; diamètre du premier anneau sombre $= 2r_1$.

#### Solution

$$
\boxed{d_1 = 2f'\theta_1 = \frac{2{,}44\lambda f'}{a}.}
$$

### Question 30

> [!INDICATION]
> Critère d'échantillonnage : la tache d'Airy doit couvrir au moins 2 pixels. En déduire la focale minimale.

> [!INDICATION]
> Critère de Nyquist : $d_1 \gtrsim 2p$ ; en déduire la focale minimale.

#### Solution

$d_1 \gtrsim 2p = 20\ \mu$m, d'où $f' \gtrsim \dfrac{d_1 a}{2{,}44\lambda} \approx \boxed{1{,}3\times10^{-4}\ \text{m}}$ (≈ 0,1 mm ; en pratique plus grande).

### A.3.2. Position verticale

### Question 31

> [!INDICATION]
> Méthode des moindres carrés : quelle fonction S minimise-t-on, par rapport à quelles variables ?

> [!INDICATION]
> Minimiser $S$ sur les paramètres $\vec p$ du modèle, pas sur les variables de mesure $x_i$.

#### Solution

$$
\boxed{S(\vec p) = \sum_i [y_i - f(x_i,\vec p)]^2},
$$

minimisée sur les **paramètres** $\vec p$ du modèle (les $x_i$ sont les variables de mesure).

### Question 32

> [!INDICATION]
> Dans l'expérience, quel paramètre physique fait varier le profil de référence ?

> [!INDICATION]
> C'est la position verticale $z$ de la bille qui fait varier le profil de référence.

#### Solution

La **position verticale z de la bille** (distance au plan focal) : on cherche le z qui minimise S.

### Question 33

> [!INDICATION]
> Compléter le script (somme des carrés des résidus), puis discuter l'effet du pas step sur la convergence.

> [!INDICATION]
> Somme des carrés des résidus ; un pas trop grand saute le minimum, un pas trop petit converge lentement.

#### Solution

```python
quantite_prec = sum((ydata - func(xdata, A))**2)
quantite_actu = sum((ydata - func(xdata, A))**2)
```
Pas trop grand (on saute le minimum) ni trop petit (convergence lente, arrêt prématuré sur un plateau).

---

## Partie B — Élasticité de l'ADN

La partie B justifie le régime élastique de l'ADN à faible force par l'**élasticité entropique** : l'ADN y est modélisé comme une chaîne librement jointe de N monomères de longueur ℓ, d'abord en 1D (modèle à deux niveaux sous champ de force), puis en 3D (fonction de Langevin), enfin par une approche thermodynamique (énergie libre). Outils : marche aléatoire, statistique de Boltzmann, équipartition.

**B.1. Un comportement élastique**

### Question 34

> [!INDICATION]
> Lire la Figure 7 : à quelles forces le régime est-il linéaire, et quelle est l'ordre de grandeur de la pente ?

> [!INDICATION]
> Lire la pente sur l'agrandissement de la Figure 7 ; donner l'ordre de grandeur en S.I.

#### Solution

Régime linéaire pour $f \lesssim 0{,}2$ pN ($z$ jusqu'à ≈ 8–10 µm) ; pente $k \sim \dfrac{0{,}1\times10^{-12}}{5\times10^{-6}} \approx \boxed{2\times10^{-8}\ \text{N}\cdot\text{m}^{-1}}$.

### Question 35

> [!INDICATION]
> Comparer l'extension du régime linéaire à la longueur étirée L = 16,5 µm : que vaut le rapport ? Quelle en est la conséquence physique ?

> [!INDICATION]
> Comparer $z$ (extension) à $L$ (longueur bout-à-bout) : le rapport vaut environ 1/2.

#### Solution

$z \approx 8$–$10\ \mu$m ≈ **la moitié de L** : l'élasticité apparaît **avant** l'étirement complet, donc elle ne vient pas des liaisons chimiques mais du dépliement d'une conformation enroulée → modèle entropique nécessaire.

> [!JURY]
> « On peut également remarquer un taux de réussite particulièrement faible (9 %) pour la question 35, où les candidats ont confondu la longueur bout à bout de l'ADN avec son allongement à partir de la longueur étirée, et n'ont donc pas compris que la spécificité de ce système était d'avoir un comportement élastique avant que la molécule ne soit complètement étirée. » (rapport 2025, p. 31/66)

**B.2. Élasticité entropique**

### Question 36

> [!INDICATION]
> z = somme des z_i = ±ℓ. Calculer ⟨z⟩ (équiprobabilité) puis ⟨z²⟩ en justifiant l'annulation des termes croisés (indépendance).

> [!INDICATION]
> Indépendance des orientations ⇒ termes croisés nuls ; $\langle z^2\rangle = N\ell^2$.

#### Solution

$$
\boxed{\langle z\rangle = 0,\qquad \langle z^2\rangle = N\ell^2 = \ell L.}
$$

### Question 37

> [!INDICATION]
> Mettre en correspondance terme à terme avec ⟨x²⟩ = 2Dt de la marche aléatoire 1D.

> [!INDICATION]
> Même forme $N\times(\text{pas})^2$ : $\langle x^2\rangle = 2Dt = N\delta x^2$.

#### Solution

$$
\boxed{\langle z^2\rangle \leftrightarrow \langle x^2\rangle,\quad N \leftrightarrow N,\quad \ell \leftrightarrow \delta x.}
$$

### Question 38

> [!INDICATION]
> Travail d'une force constante f de 0 à z, puis énergie potentielle associée (f = −∂U/∂z).

> [!INDICATION]
> $W = \int_0^z f\,dz' = fz$ ; $U = -fz$ car $f = -\partial U/\partial z$.

#### Solution

$W = fz$, d'où $\boxed{U = -fz}$ (par monomère : $u_i = \mp f\ell$).

### Question 39

> [!INDICATION]
> Système à deux niveaux : probabilités de Boltzmann p±, puis ⟨z_i⟩ = ℓ(p+ − p−). Mettre sous forme de tanh.

> [!INDICATION]
> Boltzmann à deux niveaux ; réduire $(e^u-e^{-u})/(e^u+e^{-u})$ à $\tanh u$.

#### Solution

$$
\boxed{\langle z_i\rangle = \ell\tanh\!\Big(\frac{f\ell}{k_BT}\Big).}
$$

### Question 40

> [!INDICATION]
> Sommer sur les N monomères indépendants ; tracer ⟨z⟩/L en fonction de fℓ/kBT (allure, pente à l'origine, asymptote).

> [!INDICATION]
> Somme sur les $N$ monomères indépendants ; tracer $\tanh$ (pente 1 à l'origine, asymptote +1).

#### Solution

$$
\boxed{\langle z\rangle = L\tanh\!\Big(\frac{f\ell}{k_BT}\Big)}
$$

(courbe impaire, pente 1 à l'origine, asymptote +1).

### Question 41

> [!INDICATION]
> Étudier les deux limites de tanh ; discuter le réalisme du modèle à très forte force.

> [!INDICATION]
> $\tanh u \to 1$ (saturation à $L$) et $\tanh u \approx u$ (linéaire) ; le modèle ne décrit pas le sur-étirement au-delà de $L$.

#### Solution

- $f\ell/k_BT \gg 1$ : $\langle z\rangle \to L$ (saturation ; le modèle ne décrit pas le sur-étirement au-delà de L) ;
- $f\ell/k_BT \ll 1$ : $\langle z\rangle \approx N\ell^2 f/k_BT$ (réponse linéaire).

### Question 42

> [!INDICATION]
> Force exercée par l'ADN = opposée de la force extérieure, dans le régime linéaire de la Q41. Pourquoi « entropique » ?

> [!INDICATION]
> Force opposée à la traction ; $\propto T$ et $U=0$ ⇒ origine entropique.

#### Solution

$$
\boxed{\vec f_{\text{ADN}} = -\frac{k_BT}{N\ell^2}\langle z\rangle\,\vec e_z,}
$$

proportionnelle à T, sans variation d'énergie interne ($U=0$) : tendance vers l'état le plus désordonné → élasticité **entropique**.

### Question 43

> [!INDICATION]
> Identifier la raideur dans f = k⟨z⟩ et vérifier l'homogénéité.

> [!INDICATION]
> $k = k_BT/(N\ell^2)$ ; vérifier $[k] = \text{N}\cdot\text{m}^{-1}$.

#### Solution

$$
\boxed{k^{1D}_{\text{ADN}} = \frac{k_BT}{N\ell^2} = \frac{k_BT}{L\ell}}\quad ([k] = \text{N}\cdot\text{m}^{-1}).
$$

### Modèle 3D

### Question 44

> [!INDICATION]
> Justifier l'intégrale (5) : choix des coordonnées sphériques, axe polaire selon la force, poids de Boltzmann, élément d'angle solide.

> [!INDICATION]
> Coordonnées sphériques, axe polaire selon $\vec f$ ; poids de Boltzmann ; élément d'angle solide $\sin\theta\,d\theta\,d\phi$.

#### Solution

$u_i = -f\ell\cos\theta_i$ ; intégration sur toutes les orientations avec $\sin\theta_i\,d\theta_i\,d\phi_i$, normalisée par Z → équation (5).

### Question 45

> [!INDICATION]
> Factoriser Z : exponentielle d'une somme = produit, variables indépendantes.

> [!INDICATION]
> $e^{\text{somme}} = \prod e^{\ldots}$ et variables indépendantes ⇒ $Z = (\text{intégrale angulaire})^N$.

#### Solution

$$
\boxed{Z = \Big(\int_0^{2\pi}\!d\phi\int_0^\pi\!\sin\theta\,d\theta\,e^{\frac{f\ell\cos\theta}{k_BT}}\Big)^{\!N}.}
$$

### Question 46

> [!INDICATION]
> Calculer l'intégrale angulaire (poser c = cos θ), puis ⟨z⟩ = kBT ∂f ln Z. Quelle fonction reconnaît-on ?

> [!INDICATION]
> Poser $c=\cos\theta$ : $\int_{-1}^1 e^{uc}dc = 2\sinh u/u$ ; puis $\langle z\rangle = k_BT\,\partial\ln Z/\partial f$ ; fonction de Langevin.

#### Solution

$$
\boxed{\langle z\rangle = N\ell\Big[\coth\!\Big(\frac{f\ell}{k_BT}\Big) - \frac{k_BT}{f\ell}\Big]}\quad\text{(fonction de Langevin } \mathcal L(u) = \coth u - 1/u).
$$

### Question 47

> [!INDICATION]
> Limites de la fonction de Langevin (DL fourni) ; en déduire la raideur 3D à faible force et comparer à la 1D.

> [!INDICATION]
> $\coth u - 1/u \approx u/3$ à petit $u$ ; $k^{3D} = 3k_BT/(L\ell) = 3\,k^{1D}$.

#### Solution

- $u \gg 1$ : $\langle z\rangle \to L$ (saturation) ;
- $u \ll 1$ : $\langle z\rangle \approx N\ell^2 f/(3k_BT)$, d'où $\boxed{k^{3D} = \dfrac{3k_BT}{L\ell}}$ — **3 fois** la raideur 1D (seule 1/3 des orientations contribue à z).

**B.3. Élasticité entropique : thermodynamique**

### Question 48

> [!INDICATION]
> Dénombrer les configurations (2^N à force nulle, 1 à force élevée), appliquer S = kB ln Ω, puis l'A.N. pour N = 100.

> [!INDICATION]
> $\Omega = 2^N$ à force nulle puis 1 ; $S = k_B\ln\Omega$ ; A.N. avec unité.

#### Solution

$$
\boxed{S_{f=0} = Nk_B\ln2 \approx 9{,}6\times10^{-22}\ \text{J}\cdot\text{K}^{-1},\qquad S_{f\gg f_0} = 0.}
$$

### Question 49

> [!INDICATION]
> Justifier U = 0 (articulations libres), poser F = −TS, en déduire f = (∂F/∂z)T, et comparer à la Q47.

> [!INDICATION]
> $U=0$ (articulations libres) ⇒ $\mathcal F = -TS$ ; $f = (\partial\mathcal F/\partial z)_T$ ; cohérence avec la Q47.

#### Solution

$f = \dfrac{3k_BT}{N\ell^2}z$, soit $\boxed{k = \dfrac{3k_BT}{L\ell} = k^{3D}}$ : **identique** à la Q47, les deux approches sont cohérentes (origine entropique).

---

## Partie C — Modélisation de l'ADN comme une longue tige flexible

La partie C justifie le modèle de chaîne par une approche mécanique : l'ADN est une tige élastique de module de Young Y (traction, C.2), douée d'une rigidité de flexion B (C.3), ce qui définit une longueur de persistance LP par équipartition ; le retour sur le « modèle du ver » (C.4) boucle sur l'équivalence des deux modèles (ℓ = 2LP).

**C.1. Ajustement avec le « modèle du ver »**

### Question 50

> [!INDICATION]
> Faire le DL à l'ordre 1 de la loi (11) en z/L : que devient le crochet ?

> [!INDICATION]
> Identifier la raideur obtenue et la comparer à celle de la Q47.

#### Solution

$(1-z/L)^{-2} \approx 1 + 2z/L$, le crochet vaut $\tfrac{3z}{2L}$, d'où

$$
f \approx \frac{2k_BT}{\ell}\cdot\frac{3z}{2L} = \frac{3k_BT}{L\ell}z,
$$

soit $k = \dfrac{3k_BT}{L\ell} = k^{3D}_{\text{ADN}}$ : le « modèle du ver » redonne l'élasticité entropique à faible force.

### Question 51

> [!INDICATION]
> Inverser k = 3kBT/(Lℓ) pour obtenir ℓ ; propager l'incertitude relative (Δℓ/ℓ = Δk/k).

> [!INDICATION]
> Convertir ℓ en nombre de paires de bases grâce à la Figure 1 (montée de 0,34 nm/pb).

#### Solution

$$
\ell = \frac{3\times4{,}1}{1{,}65\times10^4\times7{,}70\times10^{-6}} \approx \boxed{98\ \text{nm}},\quad \Delta\ell/\ell = 0{,}40/7{,}70 \approx 5\,\%,\quad \ell = (98\pm5)\ \text{nm},
$$

et $n_\ell = 98/0{,}34 \approx \boxed{290\ \text{paires de bases}}$ (~300).

**C.2. L'ADN comme une tige élastique : traction**

### Question 52

> [!INDICATION]
> À partir de σ = Yε, trouver l'unité de Y et son interprétation énergétique (énergie par unité de volume).

> [!INDICATION]
> Pa = J·m⁻³ ; $Y$ = énergie de liaison × densité de liaisons (énergie de cohésion par unité de volume).

#### Solution

$Y$ en **Pa** = J·m⁻³ : énergie de cohésion (énergie de liaison × densité de liaisons) stockée par unité de volume lors de la déformation.

### Question 53

> [!INDICATION]
> Estimer Y par énergie de liaison (~1 eV) divisée par le volume par liaison (~1 Å³), puis comparer au Tableau 1.

> [!INDICATION]
> 1 eV / 1 Å³ ≈ 160 GPa ; comparer au Tableau 1 (acier 200, cuivre 117, diamant ~1000 GPa).

#### Solution

$$
Y \sim \frac{1{,}6\times10^{-19}}{10^{-30}} = \boxed{1{,}6\times10^{11}\ \text{Pa} \approx 160\ \text{GPa}},
$$

cohérent avec acier (200 GPa), cuivre (117 GPa), diamant (~1000 GPa).

### Question 54

> [!INDICATION]
> L'énergie d'étirement est le travail de la force de rappel f = (YA/L)x, qui croît avec x : intégrer de 0 à ΔL (ne pas écrire f·ΔL).

> [!INDICATION]
> En déduire la densité d'énergie par unité de volume et le coefficient α.

#### Solution

$$
E_{\text{étirem}} = \int_0^{\Delta L}\frac{YA}{L}x\,dx = \boxed{\frac{\pi r^2 Y}{2L}\Delta L^2},\qquad e = \frac Y2\Big(\frac{\Delta L}{L}\Big)^2,\qquad \boxed{\alpha = \frac Y2.}
$$

> [!JURY]
> « A la question 54, une erreur assez répandue a été de ne pas intégrer correctement le terme de travail infinitésimal pour obtenir le travail et donc l'énergie potentielle, causant la perte d'un facteur 1/2. » (rapport 2025, p. 31/66)

**C.3. Flexion et longueur de persistance**

> [!JURY]
> « Les parties qui ont globalement posé le plus de difficultés sont la partie B.2, qui concernait le calcul de l'élasticité entropique de la chaîne librement jointe, et les parties finales C.3, qui portait sur la mécanique des milieux continus, et C.4, qui demandait en effet une vision globale du problème. » (rapport 2025, p. 30/66)

### C.3.1. Énergie de courbure

### Question 55

> [!INDICATION]
> À la hauteur z de la section circulaire, la largeur est la corde du cercle : laquelle ?

> [!INDICATION]
> En déduire le volume élémentaire dv(z) de la tranche de longueur L.

#### Solution

$$
\boxed{w(z) = 2\sqrt{r^2-z^2},\qquad dv(z) = 2L\sqrt{r^2-z^2}\,dz.}
$$

### Question 56

> [!INDICATION]
> La fibre à la hauteur z a un rayon de courbure R+z : exprimer son allongement relatif en fonction de z/R.

> [!INDICATION]
> Rayon de courbure $R+z$ ⇒ $\Delta L(z)/L = z/R$ (déformation linéaire en $z$).

#### Solution

$$
\boxed{\Delta L(z) = L\,\frac zR,\qquad \varepsilon(z) = \frac{\Delta L(z)}{L} = \frac zR.}
$$

### Question 57

> [!INDICATION]
> Intégrer la densité d'énergie locale e(z) = (Y/2)(z/R)² sur le volume, avec l'intégrale du préambule ∫x²√(1−x²)dx = π/8.

> [!INDICATION]
> Mettre sous la forme (12) E = (B/2)(L/R²) et identifier B et κ.

#### Solution

$$
E_{\text{flexion}} = \frac{YL}{R^2}\cdot\frac{\pi r^4}{8} = \frac12\,\frac{\pi r^4 Y}{4}\frac{L}{R^2},\qquad \boxed{B = \kappa Y,\ \kappa = \frac{\pi r^4}{4}.}
$$

### Question 58

> [!INDICATION]
> La Figure 1 donne un diamètre de 2,0 nm : quel rayon utiliser dans κ = πr⁴/4 ?

> [!INDICATION]
> Rayon $r = 1$ nm (pas le diamètre) ; $\kappa = \pi r^4/4$.

#### Solution

$r = 1{,}0$ nm, d'où $\kappa = \pi\times10^{-36}/4 \approx \boxed{0{,}78\times10^{-36}\ \text{S.I.}}$ (prendre le rayon, pas le diamètre).

### Question 59

> [!INDICATION]
> B varie comme quelle puissance de r ? Que se passe-t-il si le diamètre double ?

> [!INDICATION]
> $B \propto r^4$ ; diamètre doublé ⇒ $B \times 16$.

#### Solution

$B \propto r^4$ : si le diamètre double, $B$ est multiplié par $2^4 = \boxed{16}$.

### Question 60

> [!INDICATION]
> Diviser E_flexion par L, puis exprimer 1/R en fonction de θ/L.

> [!INDICATION]
> $e = E/L = B/(2R^2)$ ; avec $\theta = L/R$, $e = (B/2)\theta^2/L^2$.

#### Solution

$$
\boxed{e_{\text{flexion}} = \frac{B}{2R^2} = \frac B2\,\frac{\theta^2}{L^2}.}
$$

### C.3.2. Fluctuations thermiques

### Question 61

> [!INDICATION]
> L'énergie de courbure est quadratique en θ : appliquer l'équipartition. À quelle longueur L les fluctuations atteignent-elles 1 rad² ?

> [!INDICATION]
> Énergie quadratique en $\theta$ ⇒ équipartition $\tfrac12 k_BT$ ; $L_P = B/k_BT$.

#### Solution

$$
\frac{B}{2L}\langle\theta^2\rangle = \frac12 k_BT\ \Rightarrow\ \boxed{\langle\theta^2\rangle = \frac{k_BT L}{B}},\qquad \boxed{L_P = \frac{B}{k_BT}.}
$$

**C.4. Retour sur le « modèle du ver » et comparaison avec le modèle articulé**

### Question 62

> [!INDICATION]
> Tracer ⟨t⃗(s)·t⃗(s')⟩ = exp(−|s−s'|/LP) : allure, valeur en 0, valeur en LP. Que mesure LP ?

> [!INDICATION]
> Corrélation $= e^{-|s-s'|/L_P}$ ; tracer ; valeur $1/e$ en $|s-s'| = L_P$.

#### Solution

Exponentielle décroissante de 1 (en 0) à 1/e (en |s−s'| = LP) : LP = distance curviligne de « perte de mémoire » de l'orientation.

### Question 63

> [!INDICATION]
> Le vecteur tangent est la dérivée de la position par abscisse curviligne : intégrer entre s et s+L.

> [!INDICATION]
> $\vec t = d\vec r/du$ ⇒ $\vec R(L) = \int_s^{s+L}\vec t(u)\,du$.

#### Solution

$$
\boxed{\vec R(L) = \int_s^{s+L}\vec t(u)\,du.}
$$

### Question 64

> [!INDICATION]
> Partir de ⟨R²⟩ = ∬ e^{−a|s−s'|} ds ds', utiliser la symétrie s↔s' pour réduire à un triangle, puis l'intégrale du préambule.

> [!INDICATION]
> Symétrie $s\leftrightarrow s'$ : double intégrale = 2×(triangle) ; intégrale interne $(1-e^{-as})/a$.

#### Solution

$$
\boxed{\langle R^2(L)\rangle = 2LL_P\Big[1 - \frac{L_P}{L}\big(1-e^{-L/L_P}\big)\Big].}
$$

### Question 65

> [!INDICATION]
> Double limite : L ≪ LP par DL de l'exponentielle ; L ≫ LP directement. Interpréter chaque régime.

> [!INDICATION]
> $L\ll L_P$ : DL ⇒ $\langle R^2\rangle \approx L^2$ (tige rigide) ; $L\gg L_P$ : $\langle R^2\rangle \approx 2LL_P$ (pelote).

#### Solution

- $L \ll L_P$ : $\langle R^2\rangle \approx L^2$ → **tige rigide** ($\sqrt{\langle R^2\rangle} \approx L$) ;
- $L \gg L_P$ : $\boxed{\langle R^2\rangle \approx 2LL_P}$ → **pelote statistique** ($\propto L$, marche aléatoire).

### Question 66

> [!INDICATION]
> À grand L, égaler les ⟨R²⟩ du modèle du ver (2LLP) et de la chaîne jointe (ℓL) : que vaut ℓ ?

> [!INDICATION]
> Interpréter (longueur de Kuhn = 2 LP), puis calculer B = LP kBT et Y = B/κ, et comparer au Tableau 1.

#### Solution

$$
\boxed{\ell = 2L_P.}
$$

Avec $\ell \simeq 100$ nm : $L_P = 50$ nm, $B = L_P k_BT \approx \boxed{2{,}1\times10^{-28}\ \text{J}\cdot\text{m}}$, $Y = B/\kappa \approx \boxed{2{,}7\times10^8\ \text{Pa} \approx 0{,}3\ \text{GPa}}$ : rigidité de l'ADN au niveau des **plastiques** (0,2–5 GPa), très en dessous des solides durs.

## Bilan

**Méthodes à retenir.**

- **Dipôle magnétique** : $E_p = -\vec M\cdot\vec B$, $\vec\Gamma = \vec M\times\vec B$, $\vec F = \vec\nabla(\vec M\cdot\vec B)$ (force nulle en champ uniforme) ; champ dipolaire avec $\vec r$ orienté de la source vers le point.
- **Oscillateur brownien** : à l'équilibre, potentiel harmonique → équipartition (½k⟨x²⟩ = ½kBT, avec ⟨x²⟩ = **variance**) ; hors équilibre, TF de l'équation de Langevin sans inertie → lorentzienne de coupure ωc = k/γ, et bruit blanc de fluctuation-dissipation $S_{\xi\xi} = 2\gamma k_BT$. Deux méthodes de mesure de F (variance spatiale, fréquence de coupure) à confronter.
- **Chaîne librement jointe** : marche aléatoire (⟨z²⟩ = Nℓ²), système à deux niveaux sous force (tanh en 1D, fonction de Langevin en 3D), raideurs $k^{1D} = k_BT/(L\ell)$ et $k^{3D} = 3k_BT/(L\ell)$ ; origine entropique ($U=0$, $\mathcal F = -TS$, force ∝ T).
- **Tige élastique** : traction (loi de Hooke, $e = (Y/2)\varepsilon^2$, **intégrer** le travail) ; flexion ($B = \kappa Y$, $\kappa = \pi r^4/4$, énergie quadratique en θ) ; équipartition → $L_P = B/k_BT$ ; équivalence des modèles : $\ell = 2L_P$.
- **Optique** : Fraunhofer (champ lointain, TF de la pupille), tache d'Airy (1,22 λ/a), Babinet, échantillonnage de Nyquist.

**Pièges signalés par le jury.** Signes en mécanique (équilibre stable, signe + de l'oscillateur, Q12–15) ; moyenne/variance/écart-type (Q18–19) ; extension vs longueur bout-à-bout (Q35) ; facteur ½ du travail intégré (Q54) ; rayon vs diamètre (Q25, Q58) ; rigueur sur les questions de cours (magnétisme, optique, élasticité).

> [!JURY]
> « Les candidats doivent justifier explicitement toutes les étapes de calculs, s'efforcer de présenter des schémas lisibles et complets, expliciter les raisonnements. Le non-respect de ces règles s'est traduit par des minorations de point ; au contraire, le soin mis à les respecter a été valorisé par des majorations de points. » (rapport 2025, p. 32/66)

**Questions de cours (RCO).** Le rapport note des taux un peu inférieurs aux autres catégories pour les questions de restitution de connaissances, « supposées plus abordables », ce qui est « probablement lié en partie à une certaine exigence de la part des correcteurs sur ces questions de restitution de connaissances, qui sont parfois traitées sans la rigueur nécessaire et qui manquent de soin, voire d'explications » (rapport 2025, p. 31/66). Les questions RCO étaient valorisées en moyenne 3,2 points/question : ce sont des points sûrs à condition d'être rédigées avec rigueur (définitions complètes, unités, schémas légendés).

**Prérequis à revoir.** Électromagnétisme des milieux magnétiques (dipôle, susceptibilité, superparamagnétisme, loi d'Arrhenius) ; mécanique du point et oscillateur harmonique (PFD en coordonnées cylindriques, énergie, signes) ; physique statistique (marche aléatoire, Boltzmann, équipartition, bruit blanc) ; élasticité des milieux continus (traction, flexion, module de Young) ; optique ondulatoire (diffraction de Fraunhofer, tache d'Airy, Babinet).

**Questions classiques transposables.** Mesure d'une force par analyse des fluctuations (pinces optiques, AFM) ; élasticité entropique d'un polymère (caoutchouc) ; longueur de persistance et fonction de corrélation d'une chaîne semi-flexible ; filtrage de Kalman/mesure de position par caméra (moindres carrés).
