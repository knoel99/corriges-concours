# Agrégation Physique — Composition de physique 2025 · Corrigé brut

*Corrigé rédigé par IA, non officiel. Signalez toute erreur.*

Concours externe de l'agrégation de physique-chimie, option physique, session 2025. Composition de physique, 5 heures, calculatrice autorisée. Sujet : « Physique du sang » — trois parties indépendantes et 55 questions (Q1 à Q55).

Données de l'énoncé :
- viscosité dynamique du sang : $\eta=4{,}8\times10^{-3}$ Pa·s ;
- masse volumique du sang : $\rho=1{,}07\times10^{3}$ kg·m$^{-3}$ ;
- débit cardiaque : $Q_{\text{cœur}}=5$ L·min$^{-1}$ ;
- vitesse du son dans le corps humain : $c_s=1{,}540\times10^{3}$ m·s$^{-1}$ ;
- $760$ mmHg $=1013$ hPa ;
- tension de surface d'un globule rouge : $\gamma_{GR}=5\times10^{-5}$ N·m$^{-1}$, rayon $R=3$ µm, indice $n_1=1{,}38$ ;
- vitesse de la lumière dans le vide : $c=3\times10^{8}$ m·s$^{-1}$.

## Partie 1 — Modèles d'écoulement du sang

### 1.1.1 Préliminaires

**Q1.**

La masse contenue dans $V$ fixe est $M=\iiint_V \rho\,\mathrm dV$. Sa variation provient uniquement du flux de masse sortant à travers $S$ :

$$
\frac{\mathrm dM}{\mathrm dt}=-\oiint_S \rho\vec v\cdot\mathrm d\vec S .
$$

Comme $V$ est fixe, $\dfrac{\mathrm dM}{\mathrm dt}=\iiint_V \dfrac{\partial\rho}{\partial t}\,\mathrm dV$. Le théorème de Green‑Ostrogradski donne $\oiint_S \rho\vec v\cdot\mathrm d\vec S=\iiint_V \operatorname{div}(\rho\vec v)\,\mathrm dV$. D'où, pour tout volume $V$ :

$$

\begin{aligned}
\iiint_V\!\left(\frac{\partial\rho}{\partial t}+\operatorname{div}(\rho\vec v)\right)\!\mathrm dV &= 0 \\
&\Longrightarrow\;\boxed{\frac{\partial\rho}{\partial t}+\operatorname{div}(\rho\vec v)=0.}
\end{aligned}

$$

**Q2.**

Avec $\operatorname{div}(\rho\vec v)=\rho\operatorname{div}\vec v+\vec v\cdot\overrightarrow{\operatorname{grad}}\rho$ :

$$
\frac{\partial\rho}{\partial t}+\vec v\cdot\overrightarrow{\operatorname{grad}}\rho+\rho\operatorname{div}\vec v=0 .
$$

On pose la **dérivée particulaire** (dérivée en suivant la particule de fluide) $\dfrac{\mathrm D\rho}{\mathrm Dt}=\dfrac{\partial\rho}{\partial t}+\vec v\cdot\overrightarrow{\operatorname{grad}}\rho$, d'où

$$
\boxed{\frac{\mathrm D\rho}{\mathrm Dt}+\rho\operatorname{div}\vec v=0.}
$$

Un écoulement **incompressible** signifie que la masse volumique d'une particule de fluide ne varie pas en la suivant : $\dfrac{\mathrm D\rho}{\mathrm Dt}=0$. L'équation (2) impose alors $\boxed{\operatorname{div}\vec v=0}$ : le champ de vitesses est à **flux conservatif** (son flux à travers toute surface fermée est nul).

**Q3.**

Avec $\vec v=v_z(r,\theta,z)\vec u_z$, l'incompressibilité en cylindriques s'écrit

$$

\begin{aligned}
\operatorname{div}\vec v &= \frac1r\frac{\partial(rv_r)}{\partial r}+\frac1r\frac{\partial v_\theta}{\partial\theta}+\frac{\partial v_z}{\partial z} \\
&= \frac{\partial v_z}{\partial z}=0,
\end{aligned}

$$

donc $v_z$ ne dépend pas de $z$ : l'écoulement est **établi**. Le dispositif est invariant par rotation autour de $Oz$ (symétrie de révolution), donc $v_z$ ne dépend pas de $\theta$. Finalement $\boxed{v_z=v_z(r)}$.

**Q4.**

Sur la surface externe $r+\mathrm dr$ (aire $2\pi(r+\mathrm dr)\mathrm dz$), le fluide plus éloigné de l'axe exerce $+\sigma(r+\mathrm dr)\,2\pi(r+\mathrm dr)\mathrm dz\,\vec u_z$ ; sur la surface interne $r$, le fluide plus proche de l'axe exerce $-\sigma(r)\,2\pi r\,\mathrm dz\,\vec u_z$. La résultante de cisaillement est

$$

\begin{aligned}
\vec F_{\text{cis}} &= 2\pi\,\mathrm dz\big[(r+\mathrm dr)\sigma(r+\mathrm dr)-r\sigma(r)\big]\vec u_z \\
&= 2\pi\,\mathrm dz\,\frac{\partial(r\sigma)}{\partial r}\mathrm dr\,\vec u_z \\
&= \frac1r\frac{\partial(r\sigma)}{\partial r}\,(2\pi r\,\mathrm dr\,\mathrm dz)\,\vec u_z .
\end{aligned}

$$

Le PFD sur la particule de volume $\mathrm d\tau=2\pi r\,\mathrm dr\,\mathrm dz$ et de masse $\rho\,\mathrm d\tau$ s'écrit $\rho\,\mathrm d\tau\,\dfrac{\mathrm D\vec v}{\mathrm Dt}=-\overrightarrow{\operatorname{grad}}P\,\mathrm d\tau+\vec F_{\text{cis}}$. En divisant par $\mathrm d\tau$ :

$$
\boxed{\rho\frac{\mathrm D\vec v}{\mathrm Dt}=-\overrightarrow{\operatorname{grad}}P+\frac1r\frac{\partial(\sigma r)}{\partial r}\vec u_z.}
$$

### 1.1.2 Écoulement de Poiseuille newtonien

**Q5.**

$\mathcal R_E=\dfrac{2R\rho U}{\eta}$ compare l'ordre de grandeur des forces d'inertie $\rho U^2/(2R)$ aux forces visqueuses $\eta U/(2R)^2$. Dans une conduite cylindrique, l'écoulement est **laminaire** tant que $\mathcal R_E\lesssim 2000$ et devient **turbulent** au‑delà de la transition (quelques milliers).

**Q6.**

Stationnaire : $\partial/\partial t=0$. Établi et incompressible (Q3) : $\vec v\cdot\overrightarrow{\operatorname{grad}}\vec v=v_z\dfrac{\partial v_z}{\partial z}\vec u_z=\vec 0$. Donc $\dfrac{\mathrm D\vec v}{\mathrm Dt}=\vec 0$, et newtonien $\sigma=\eta\,\mathrm dv_z/\mathrm dr$. L'équation (3) projetée donne $\partial_rP=0,\ \partial_\theta P=0$ et

$$
\frac{\partial P}{\partial z}=\frac1r\frac{\mathrm d}{\mathrm dr}\!\left(\eta r\frac{\mathrm dv_z}{\mathrm dr}\right).
$$

Le membre de gauche ne dépend que de $z$, celui de droite que de $r$ : ils valent une constante. Comme $P(0)=P_1$, $P(L)=P_2$ : $\dfrac{\partial P}{\partial z}=\dfrac{P_2-P_1}{L}=-\dfrac{\Delta P}{L}$, soit $\boxed{P(z)=P_1-\dfrac{\Delta P}{L}z}$ (affine). Alors

$$

\begin{aligned}
\frac{\mathrm d}{\mathrm dr}\!\left(r\frac{\mathrm dv_z}{\mathrm dr}\right) &= -\frac{\Delta P}{\eta L}r \\
\Rightarrow\ r\frac{\mathrm dv_z}{\mathrm dr} &= -\frac{\Delta P}{2\eta L}r^2+C_1 .
\end{aligned}

$$

La vitesse étant finie en $r=0$, $C_1=0$. Puis $v_z=-\dfrac{\Delta P}{4\eta L}r^2+C_2$ ; le non‑glissement $v_z(R)=0$ donne $C_2=\dfrac{\Delta P}{4\eta L}R^2$ :

$$
\boxed{v_z(r)=-\frac{\Delta P}{4\eta L}\,(r^2-R^2).}
$$

**Q7.**

$v_z$ est maximale sur l'axe, $v_z(0)=\dfrac{\Delta P\,R^2}{4\eta L}>0$, et s'annule à la paroi $r=R$.
*Schéma : parabole $v_z(r)$ pour $r\in[0,R]$, sommet sur l'axe, nulle en $\pm R$, flèche $\vec u_z$.*

**Q8.**

$$

\begin{aligned}
Q_v &= \iint_{\text{section}}\vec v\cdot\mathrm d\vec S \\
&= \int_0^R v_z(r)\,2\pi r\,\mathrm dr \\
&= -\frac{\pi\Delta P}{2\eta L}\int_0^R(r^3-R^2r)\,\mathrm dr \\
&= -\frac{\pi\Delta P}{2\eta L}\!\left(\frac{R^4}{4}-\frac{R^4}{2}\right).
\end{aligned}

$$

$$
\boxed{Q_v=\frac{\pi R^4\,\Delta P}{8\eta L}.}
$$

**Q9.**

$R_h=\dfrac{\Delta P}{Q_v}=\boxed{\dfrac{8\eta L}{\pi R^4}}$, en $\mathrm{Pa\cdot s\cdot m^{-3}}=\mathrm{kg\cdot m^{-4}\cdot s^{-1}}$. En électricité, $R_{\text{élec}}=\rho_e L/(\pi R^2)\propto R^{-2}$, alors qu'ici $R_h\propto R^{-4}$ : la perte de charge est **beaucoup plus sensible** au rayon (diviser $R$ par 2 multiplie $R_h$ par 16). Une faible variation du calibre d'un vaisseau modifie fortement le débit.

### 1.1.3 Vérification expérimentale

**Q10.**

Les tuyaux de raccordement ($d\ge12$ mm, soit $R\ge6$ mm) ont un rayon $\sim12$ fois supérieur à celui du capillaire ($R=0{,}5$ mm) ; comme $R_h\propto R^{-4}$, leur résistance est réduite d'un facteur $\sim10^{4}$ et devient négligeable. Les pertes incontrôlées proviennent des **pertes de charge singulières** (coudes de l'enroulement, raccords) ; un grand rayon de courbure limite les écoulements secondaires et décollements.
La différence de pression motrice est donnée par la **loi de l'hydrostatique** (réservoir de hauteur $H$ au‑dessus de la sortie) : $\boxed{\Delta P=\rho_{\text{eau}}\,g\,H}$. D'où

$$
\boxed{Q_v=\frac{\pi R^4\rho_{\text{eau}}\,g\,H}{8\eta L}.}
$$

**Q11.**

Les lignes 20–25 n'utilisent aucune série de mesures répétées : il s'agit d'évaluations de **type B** (non statistiques, fondées sur la connaissance de l'appareil).
- $u(R)$ : $R$ connu à $\pm0{,}005$ mm, loi rectangulaire de demi‑largeur $a$, $u=a/\sqrt3$.
- $u(H)$ : lecture au cm, loi rectangulaire de largeur $1$ cm, $u=\text{(largeur)}/\sqrt{12}$.
- $u(Q_v)$ : propagation quadratique $\dfrac{u(Q_v)}{Q_v}=\sqrt{\big(u(V_0)/V_0\big)^2+\big(u(t_0)/t_0\big)^2}$, puisque $Q_v=V_0/t_0$.

**Q12.**

La régression linéaire est obtenue par **`np.polyfit(H_simule, Qv_simule, 1)`** (ligne 35), qui renvoie la pente et l'ordonnée à l'origine. La loi de Poiseuille prévoit $Q_v=A\,H$ avec $A=\pi R^4\rho_{\text{eau}}g/(8\eta L)$ : la **linéarité $Q_v(H)$** et le **faible écart des points de mesure à la droite** (dispersion très réduite, fig. 3) valident le modèle. On lit $\boxed{A=1{,}55\times10^{-7}\ \mathrm{m^2\,s^{-1}},\quad u(A)=0{,}08\times10^{-7}\ \mathrm{m^2\,s^{-1}}}$ (deux CS cohérents avec l'incertitude).

**Q13.**

**Principe.** La méthode de Monte‑Carlo propage les incertitudes en tirant, pour chaque grandeur d'entrée ($L$, $R$, $A$), un grand nombre de valeurs aléatoires distribuées selon leur loi (ici normales, lignes 49–51), en calculant pour chaque tirage la valeur de la grandeur de sortie, puis en formant la **moyenne** (estimateur) et l'**écart‑type** (incertitude‑type) de l'échantillon obtenu.
**Ligne 51 à compléter :** `A1=np.random.normal(A,u_A,n_simulation)`.
**Calcul (ligne 53) :** de $A=\pi R^4\rho_{\text{eau}}g/(8\eta L)$ on tire $\eta=\dfrac{\pi R^4\rho_{\text{eau}}g}{8LA}$, codé `eta_eau=3.14*R1**4*rho_eau*g/(8*L1*A1)`. Puis `eta_eauexp=np.mean(eta_eau)` et `u_etaeauexp=np.std(eta_eau)` (lignes 80–81) :

$$

\begin{aligned}
\boxed{\eta_{\text{eau,exp}}=8{,}6\times10^{-4}\ \mathrm{Pa\,s}} \\
u(\eta_{\text{eau,exp}})=0{,}5\times10^{-4}\ \mathrm{Pa\,s}.
\end{aligned}

$$

On aurait pu les déduire de l'histogramme (fig. 3) : abscisse du centre de la distribution (moyenne) et largeur (écart‑type).
**Conclusion.** Écart normalisé avec la référence $\eta_{\text{réf}}=8{,}91\times10^{-4}\pm0{,}20\times10^{-4}\ \mathrm{Pa\,s}$ :

$$
z=\frac{|\eta_{\text{exp}}-\eta_{\text{réf}}|}{\sqrt{u_{\text{exp}}^2+u_{\text{réf}}^2}}=\frac{0{,}31\times10^{-4}}{\sqrt{(0{,}5)^2+(0{,}20)^2}\times10^{-4}}\approx0{,}6<2 .
$$

Les valeurs sont **compatibles** : l'expérience constitue une mesure expérimentale valable de $\eta_{\text{eau}}$.

### 1.2 Écoulement newtonien du sang

**Q14.**

*Schéma : artère (nœud $P_{ar}$) → $N_c$ résistances $R_{hc}$ identiques en parallèle → veine (nœud $P_v$), source imposant $Q_{ar}$.*
Résistance d'un capillaire : $R_{hc}=\dfrac{8\eta\ell_c}{\pi R_c^4}=\dfrac{8\cdot4{,}8\times10^{-3}\cdot10^{-2}}{\pi(5\times10^{-6})^4}\approx\boxed{2{,}0\times10^{17}\ \mathrm{Pa\,s\,m^{-3}}}$.
$N_c$ en parallèle : $R_h=\dfrac{R_{hc}}{N_c}$. Or $R_h=\dfrac{P_{ar}-P_v}{Q_{ar}}$ avec $Q_{ar}=0{,}05\,Q_{\text{cœur}}=0{,}05\cdot\dfrac{5\times10^{-3}}{60}=4{,}2\times10^{-6}\ \mathrm{m^3\,s^{-1}}$ :

$$

\begin{aligned}
R_h=\frac{12000-1330}{4{,}2\times10^{-6}} &\approx 2{,}6\times10^{9}\ \mathrm{Pa\,s\,m^{-3}}, \\
N_c=\frac{R_{hc}}{R_h} &\approx \boxed{8\times10^{7}}.
\end{aligned}

$$

Débit par capillaire : $\boxed{Q_c=\dfrac{Q_{ar}}{N_c}\approx5\times10^{-14}\ \mathrm{m^3\,s^{-1}}}$. Commentaire : le très grand nombre de capillaires ($\sim10^8$) assure un débit unitaire minuscule et une grande surface d'échange.

**Q15.**

- Artère : $U_{ar}=\dfrac{Q_{ar}}{\pi R_{ar}^2}=\dfrac{4{,}2\times10^{-6}}{\pi(2{,}5\times10^{-3})^2}\approx0{,}21\ \mathrm{m\,s^{-1}}$.
- Capillaire : $U_c=\dfrac{Q_c}{\pi R_c^2}=\dfrac{5\times10^{-14}}{\pi(5\times10^{-6})^2}\approx0{,}7\ \mathrm{mm\,s^{-1}}$.
- Sortie du cœur (aorte) : $U_{ao}=\dfrac{Q_{\text{cœur}}}{\pi R_{ao}^2}=\dfrac{8{,}3\times10^{-5}}{\pi(8\times10^{-3})^2}\approx0{,}41\ \mathrm{m\,s^{-1}}$.
Nombres de Reynolds $\mathcal R_E=2R\rho U/\eta$ ($\rho=1{,}07\times10^3$, $\eta=4{,}8\times10^{-3}$) :

$$
\mathcal R_{E,ar}\approx2{,}4\times10^{2},\qquad \mathcal R_{E,c}\approx1{,}6\times10^{-3},\qquad \mathcal R_{E,ao}\approx1{,}5\times10^{3}.
$$

Tous inférieurs à $2000$ : l'écoulement est **laminaire** partout ; l'aorte est la plus proche de la transition, les capillaires sont en régime visqueux dominant.

**Q16.**

$\boxed{R_{h\text{circ}}=\dfrac{P_{ao}-P_{vc}}{Q_{\text{cœur}}}=\dfrac{12900-800}{8{,}3\times10^{-5}}\approx1{,}5\times10^{8}\ \mathrm{Pa\,s\,m^{-3}}}$, cohérent avec la valeur annoncée.

### 1.3 Effet Windkessel

**Q17.**

Le débit moyen sur une période vaut $Q_{\text{cœur}}=\dfrac1T\int_0^T Q\,\mathrm dt=\dfrac{Q_{\text{sys}}\,t_0}{T}$. D'où $\boxed{Q_{\text{sys}}=Q_{\text{cœur}}\dfrac{T}{t_0}}$ (avec $t_0=T/3$, $Q_{\text{sys}}=3Q_{\text{cœur}}$).

**Q18.**

La chambre élastique **stocke un volume** sous l'effet de la pression, comme un **condensateur stocke une charge** : la compliance $C=\mathrm dV/\mathrm dP$ est analogue à la capacité $C_{\text{élec}}=\mathrm dq/\mathrm dU$ (avec $V\leftrightarrow q$, $P\leftrightarrow U$). 
Le **débit cardiaque** $Q_{\text{sys}}$ est analogue à une **source de courant**, $R_{h\text{circ}}$ à une résistance, le clapet à une diode/interrupteur et $P_v$ à un potentiel de référence. L'énergie élastique stockée pendant la systole est restituée pendant la diastole, lissant le débit.

**Q19.**

Clapet ouvert : $Q_{\text{sys}}=Q_{\text{circ}}+Q_{\text{stocké}}$ avec $Q_{\text{stocké}}=\dfrac{\mathrm dV}{\mathrm dt}=C\dfrac{\mathrm dP_a}{\mathrm dt}$ et $Q_{\text{circ}}=\dfrac{P_a-P_v}{R_{h\text{circ}}}=\dfrac{\Delta P}{R_{h\text{circ}}}$. Comme $P_v$ est constante, $\dfrac{\mathrm dP_a}{\mathrm dt}=R_{h\text{circ}}\dfrac{\mathrm dQ_{\text{circ}}}{\mathrm dt}$, d'où

$$

\begin{aligned}
\boxed{\tau\frac{\mathrm dQ_{\text{circ}}}{\mathrm dt}+Q_{\text{circ}}=Q_{\text{sys}}} \\
\boxed{\tau=R_{h\text{circ}}\,C}\ \ (\text{en }\mathrm{Pa\,s\,m^{-3}\times m^3\,\mathrm{Pa}^{-1}=\mathrm{s}}).
\end{aligned}

$$

Solution avec $Q_{\text{circ}}(0)=Q_{\text{circ}1}$ : $Q_{\text{circ}}(t)=Q_{\text{sys}}+(Q_{\text{circ}1}-Q_{\text{sys}})e^{-t/\tau}$, soit en $t=t_0$ l'équation (7).

**Q20.**

$T=60/70=0{,}86\ \mathrm s$, $t_0=T/3=0{,}29\ \mathrm s$, $t_1=2T/3=0{,}57\ \mathrm s$, $\tau=R_{h\text{circ}}C=1{,}5\times10^8\times6\times10^{-9}=0{,}9\ \mathrm s$.
$Q_{\text{sys}}=3Q_{\text{cœur}}=2{,}5\times10^{-4}\ \mathrm{m^3\,s^{-1}}$.

$$
Q_{\text{circ}0}=Q_{\text{sys}}\frac{1-e^{-t_0/\tau}}{1-e^{-T/\tau}}=2{,}5\times10^{-4}\frac{1-e^{-0{,}32}}{1-e^{-0{,}95}}\approx1{,}1\times10^{-4}\ \mathrm{m^3\,s^{-1}},
$$

$$
Q_{\text{circ}1}=Q_{\text{circ}0}\,e^{-t_1/\tau}\approx1{,}1\times10^{-4}\,e^{-0{,}63}\approx5{,}9\times10^{-5}\ \mathrm{m^3\,s^{-1}}.
$$

$Q_{\text{circ}}$ oscille entre $\approx5{,}9\times10^{-5}$ et $\approx1{,}1\times10^{-4}\ \mathrm{m^3\,s^{-1}}$ autour de $Q_{\text{cœur}}$.
*Schéma : $Q_{\text{circ}}(t)$ : charge exponentielle sur $[0,t_0]$ vers $Q_{\text{sys}}$, décharge sur $[t_0,T]$, régime périodique à faible ondulation.*
**Conclusion.** La compliance **lisse** le débit discontinu du cœur en un débit artériolo‑capillaire quasi continu.

**Q21.**

$P_{a0}=P_v+R_{h\text{circ}}Q_{\text{circ}0}=800+1{,}5\times10^8\times1{,}1\times10^{-4}\approx1{,}7\times10^4\ \mathrm{Pa}$ ; $P_{a1}=800+1{,}5\times10^8\times5{,}9\times10^{-5}\approx9{,}6\times10^3\ \mathrm{Pa}$. Conversion ($760\ \mathrm{mmHg}=1013\ \mathrm{hPa}$) : $P_{a0}\approx\boxed{131\ \mathrm{mmHg}}$ (systolique), $P_{a1}\approx\boxed{72\ \mathrm{mmHg}}$ (diastolique). À comparer aux valeurs médicales $130/80$ : accord très satisfaisant, surtout en diastole.

## Partie 2 — Mesure d'écoulement sanguin par effet Doppler

### 2.1 Propagation des ondes acoustiques

**Q22.**

Champs : $\rho_1=\rho+\mu$, $p_1=P_0+p$, $\vec v$ du premier ordre.
Conservation de la masse (2) : $\dfrac{\partial\mu}{\partial t}+\rho\operatorname{div}\vec v=0$ (on néglige $\vec v\cdot\overrightarrow{\operatorname{grad}}\mu$ et $\mu\operatorname{div}\vec v$, du second ordre).
Euler ($\eta=0$) : $\rho\dfrac{\partial\vec v}{\partial t}=-\overrightarrow{\operatorname{grad}}p$ (on néglige $\vec v\cdot\overrightarrow{\operatorname{grad}}\vec v$, $\mu\,\partial_t\vec v$ ; $\overrightarrow{\operatorname{grad}}P_0=\vec0$).
Compressibilité isentropique : $\chi_S=\dfrac1{\mu_1}\!\left(\dfrac{\partial\mu_1}{\partial p_1}\right)_S\simeq\dfrac1\rho\dfrac{\partial\mu}{\partial p}$, donc $\mu=\rho\chi_S\,p$.
Combinaison : $\rho\chi_S\partial_t p+\rho\operatorname{div}\vec v=0$ ; en dérivant par $t$ et en reportant $\operatorname{div}\partial_t\vec v=-\Delta p/\rho$ :

$$

\begin{aligned}
\boxed{\Delta p-\rho\chi_S\frac{\partial^2 p}{\partial t^2}=0}\quad\text{(d'Alembert)} \\
\boxed{c_s=\frac1{\sqrt{\rho\chi_S}}}.
\end{aligned}

$$

Dimension : $[\chi_S]=\mathrm{Pa^{-1}}$, $[\rho]=\mathrm{M\,L^{-3}}$, $[\rho\chi_S]=\mathrm{T^2L^{-2}}$ donc $[c_s]=\mathrm{L\,T^{-1}}$. ✓

**Q23.**

Avec $\underline p=p_m e^{j(\omega t-kx)}$ dans d'Alembert : $-k^2+\rho\chi_S\omega^2=0$, soit $\boxed{k=\dfrac\omega{c_s}}$. Euler projetée : $j\omega\rho\,\underline v=-\partial_x\underline p=jk\,\underline p$, d'où $\boxed{\underline v=\dfrac{\underline p}{\rho c_s}}$. Impédance :

$$

\begin{aligned}
\underline Z=\frac{\underline p}{\underline v} &= \rho c_s=\sqrt{\frac{\rho}{\chi_S}}, \\
Z=|\underline Z| &= \rho c_s=\sqrt{\frac{\rho}{\chi_S}}.
\end{aligned}

$$

$\underline Z$ est **réelle** : $p$ et $v$ sont en phase.

**Q24.**

$\vec\Pi=p\vec v$ est le **vecteur densité de courant énergétique acoustique** (analogue au vecteur de Poynting), en $\mathrm{W\,m^{-2}}$ ($=\mathrm{Pa\cdot m\,s^{-1}}$). Avec $v=p/(\rho c_s)$ et $p=p_m\cos(\omega t-kx)$, $\langle\cos^2\rangle=\tfrac12$ :

$$

\begin{aligned}
I=\langle\|\vec\Pi\|\rangle &= \frac{\langle p^2\rangle}{\rho c_s} \\
&= \boxed{\frac{p_m^2}{2\rho c_s}.}
\end{aligned}

$$

**Q25.**

$I_{\max}=1\ \mathrm{W\,cm^{-2}}=10^4\ \mathrm{W\,m^{-2}}$. De $I=p_m^2/(2\rho c_s)$ :

$$
p_{\max}=\sqrt{2\rho c_s I}=\sqrt{2\cdot10^3\cdot1540\cdot10^4}\approx\boxed{1{,}75\times10^{5}\ \mathrm{Pa}.}
$$

**Q26.**

$\delta=\dfrac\alpha{f_0}=\dfrac{2\ \mathrm{cm\cdot MHz}}{3\ \mathrm{MHz}}=0{,}67\ \mathrm{cm}$. Après $x=10$ cm : $\dfrac x\delta=15$. L'atténuation est

$$

\begin{aligned}
L=10\log\frac{I_0}{I} &= 10\,\frac{x}{\delta}\,\log e \\
&= 10\times15\times0{,}434 \\
&\approx \boxed{+65\ \mathrm{dB}.}
\end{aligned}

$$

Atténuation très forte : le signal réfléchi doit être **amplifié** avant traitement.

**Q27.**

La résolution spatiale est limitée par la **diffraction**. L'ordre de grandeur est la longueur d'onde : $\ell\sim\lambda=\dfrac{c_s}{f_0}=\dfrac{1540}{3\times10^6}\approx\boxed{0{,}5\ \mathrm{mm}}$.

**Q28.**

Le choix de $f_0$ résulte d'un compromis : (i) **intensité diffusée** $I\propto f_0^4$ → haute fréquence favorise le signal ; (ii) **résolution** $\ell\sim c_s/f_0$ → meilleure à haute fréquence ; (iii) **pénétration** $\delta=\alpha/f_0$ → l'atténuation croît avec $f_0$, limitant la profondeur. Pour une artère **profonde**, on abaisse $f_0$ (pénétration) ; pour une bonne résolution superficielle, on l'augmente. La diffusion par les globules rouges est précisément le phénomène qui rend l'échographie Doppler possible.

### 2.2 Principe de l'échographie Doppler

**Q29.**

*Schéma : sonde, artère, vecteur $\vec v$ du GR faisant l'angle $\theta$ avec la direction de propagation.* Le GR, mobile, reçoit une fréquence décalée puis la réémet : les deux décalages s'ajoutent. Pour $v\ll c_s$,

$$
f_D=f_0'-f_0=\boxed{\frac{2f_0\,v\cos\theta}{c_s}}.
$$

$f_D<0$ lorsque $\cos\theta<0$, c'est‑à‑dire quand le GR **s'éloigne** de la sonde. 
AN ($v=0{,}30\ \mathrm{m\,s^{-1}}$, $\cos\theta\simeq1$, $f_0=3$ MHz) : $f_D=\dfrac{2\cdot3\times10^6\cdot0{,}30}{1540}\approx1{,}2\ \mathrm{kHz}$, qui appartient au **domaine audible** ($20\ \mathrm{Hz}$–$20\ \mathrm{kHz}$).

**Q30.**

$v=\dfrac{f_D c_s}{2f_0\cos\theta}$ donne $\dfrac{\mathrm dv}{v}=-\dfrac{\mathrm d(\cos\theta)}{\cos\theta}=\tan\theta\,\mathrm d\theta$, d'où $\boxed{\dfrac{u(v)}{v}=|\tan\theta|\,u(\theta)}$. 
Pour $\dfrac{u(v)}{v}=0{,}15$ et $u(\theta)=10^\circ=0{,}175\ \mathrm{rad}$ : $|\tan\theta|=\dfrac{0{,}15}{0{,}175}=0{,}86$, soit $\boxed{\theta_{\max}\approx41^\circ}$. Il faut donc opérer sous $\sim40^\circ$, difficile en pratique car le praticien ne connaît pas l'orientation du vaisseau (d'où l'inclinaison variable de la sonde).

**Q31.**

L'écho d'une impulsion doit revenir avant l'émission suivante : la durée d'aller‑retour $2d/c_s$ doit être inférieure à $1/\mathrm{PRF}$. La profondeur maximale est atteinte quand $\dfrac{2d_{\max}}{c_s}=\dfrac1{\mathrm{PRF}}$, soit $\boxed{\mathrm{PRF}=\dfrac{c_s}{2d_{\max}}}$ (facteur 2 = aller‑retour). La position de la fenêtre d'écoute (délai $2d/c_s$) sélectionne la profondeur ; une fenêtre **courte** assure une bonne résolution en profondeur.

**Q32.**

La multiplication du signal reçu (fréquences $f_0+f_D$, $f_0+\mathrm{PRF}+f_D$, $f_0-\mathrm{PRF}+f_D$) par la porteuse $\cos(2\pi f_0 t)$ 
produit des fréquences **somme** (voisines de $2f_0$) et **différence** : $f_D$, $\mathrm{PRF}+f_D$, $-\mathrm{PRF}+f_D$. 
Avec $f_D<\mathrm{PRF}$, seul $f_D$ est à basse fréquence. 
Un **filtre passe‑bas** de coupure $f_c$ telle que $\boxed{f_D<f_c<\mathrm{PRF}-f_D}$ récupère le signal Doppler utile.

**Q33.**

Les vitesses étant distribuées, le signal Doppler a un **spectre continu** de $0$ à $f_{D,\max}$. L'échantillonnage à la cadence $\mathrm{PRF}$ impose, pour éviter le **repliement** (aliasing), le **critère de Nyquist‑Shannon** : $\boxed{\mathrm{PRF}>2f_{D,\max}}$. Après filtrage passe‑bas, le spectre occupe la bande $[0,f_{D,\max}]$.
*Schéma : spectre continu triangulaire de $0$ à $f_{D,\max}$ après filtrage.*

### 2.3 Analyse d'un Doppler sanguin

**Q34.**

$d_{\max}=\dfrac{c_s}{2\,\mathrm{PRF}}=\dfrac{1540}{2\times3731}\approx\boxed{20{,}6\ \mathrm{cm}}$. L'artère est à $11{,}1$ cm $<20{,}6$ cm : la profondeur est bien **accessible** (cohérent).

**Q35.**

Échelle $\pm60\ \mathrm{cm\,s^{-1}}$, $\theta=0$, $f_0=2{,}5$ MHz. Lecture : $v_{\text{sys}}\simeq0{,}55\ \mathrm{m\,s^{-1}}$, $v_{\text{dia}}\simeq0{,}18\ \mathrm{m\,s^{-1}}$.

$$
f_{D,\text{sys}}=\frac{2f_0v_{\text{sys}}}{c_s}\approx1{,}8\ \mathrm{kHz},\qquad f_{D,\text{dia}}\approx0{,}6\ \mathrm{kHz}.
$$

Non‑repliement : $f_{D,\max}<\mathrm{PRF}/2=1865\ \mathrm{Hz}$. Le pic systolique $\approx1{,}8\ \mathrm{kHz}$ est **juste** sous cette limite : l'échelle de vitesse a été calée sur $\mathrm{PRF}/2$, le repliement est évité.

**Q36.**

**Systole** : profil « bouchon » (quasi plat), presque tous les GR à la même vitesse élevée → spectre **très piqué** au voisinage de $f_{D,\text{sys}}$. **Diastole** : profil de Poiseuille parabolique, vitesses réparties uniformément → spectre **large et plat** de $0$ à $f_{D,\text{dia}}$.
*Schéma : deux spectres $I(f)$ : raie étroite piquée (systole) ; plateau étalé (diastole), fréquences cohérentes avec Q35.*

**Q37.**

Pour une sténose de grade I (réduction $<40\%$), la conservation du débit $Q_v=S\,U$ impose une **augmentation de la vitesse** dans la section réduite → fréquences Doppler plus élevées et **élargissement spectral** (turbulence naissante). Le médecin relie l'élévation de la vitesse systolique maximale à la réduction de section. À l'oreille : sifflement plus aigu.

**Q38.**

Pour un grade IV ($60$–$90\%$) : forte hausse de vitesse, **élargissement spectral majeur** et apparition de **fréquences négatives**. Ces dernières traduisent des **globules repartant en sens inverse** (recirculations/tourbillons en aval de la sténose serrée). À l'oreille : son rauque et rugueux.

## Partie 3 — Mécanique des globules rouges

### 3.1 Modèle simplifié

**Q39.**

**Expérience** : étirement d'un film de savon sur un cadre dont un côté coulisse ; pour maintenir le côté mobile (longueur $\ell$, deux faces) il faut exercer $F=2\gamma\ell$ — on mesure ainsi $\gamma$. **Définition** : $\gamma$ est l'énergie à fournir par unité d'aire créée (J·m⁻²), de façon équivalente la force par unité de longueur (N·m⁻¹) s'opposant à l'extension. **Origine** : les molécules de surface ont moins de voisines que celles du volume ; les interactions attractives (**forces de van der Waals**) y sont déséquilibrées, ce qui rend énergétiquement coûteuse toute augmentation de surface.

**Q40.**

$[\gamma]=\mathrm{N\,m^{-1}}=\mathrm{J\,m^{-2}}$, dimension $\mathrm{M\,T^{-2}}$. Pour la sphère de rayon $R$ : $\boxed{E_{\text{surf}}=\gamma\,S=\gamma\,4\pi R^2}$.

**Q41.**

Pour une dilatation $\mathrm dR$ ($\mathrm dV=4\pi R^2\,\mathrm dR$) :
- travail des forces de pression : $\delta W_P=(P_1-P_2)\,\mathrm dV=(P_1-P_2)4\pi R^2\,\mathrm dR$ ;
- travail de la tension de surface : $\delta W_\gamma=-\gamma\,\mathrm dS=-\gamma\,8\pi R\,\mathrm dR$.
À l'équilibre, $\delta W_P+\delta W_\gamma=0$ pour tout $\mathrm dR$ :

$$

\begin{aligned}
(P_1-P_2)\,4\pi R^2 &= 8\pi\gamma R \\
\Rightarrow\ \Delta P=P_1-P_2 &= \boxed{\frac{2\gamma_{GR}}{R}}\quad\text{(loi de Laplace)}.
\end{aligned}

$$

AN : $\Delta P=\dfrac{2\cdot5\times10^{-5}}{3\times10^{-6}}\approx\boxed{33\ \mathrm{Pa}}$.

**Q42.**

Incompressibilité : $V=\tfrac43\pi m^2M=\text{cste}$. Donc $\mathrm dV=\tfrac43\pi(2mM\,\mathrm dm+m^2\,\mathrm dM)=0$, soit $2M\,\mathrm dm+m\,\mathrm dM=0$, d'où $\dfrac{\mathrm dm}{\mathrm dM}=-\dfrac{m}{2M}$. Au voisinage de la sphère ($m=M=R$) : $\boxed{\mathrm dm=-\tfrac12\,\mathrm dM}$.

**Q43.**

Conservation du volume : $m^2M=R^3$ avec $M=R(1+\varepsilon)$, $m=R(1-\varepsilon')$ : $(1-\varepsilon')^2(1+\varepsilon)=1$. 
Au premier ordre $(1-2\varepsilon')(1+\varepsilon)\approx1$ donne $\boxed{\varepsilon'=\varepsilon/2}$, d'où $m=R\!\left(1-\dfrac\varepsilon2\right)$.
La force admise $\|\vec F_\gamma\|\approx3\pi\gamma_{GR}R\,\varepsilon$ est **linéaire** en $\varepsilon$ : c'est une loi de Hooke $F=k\,x$ avec une **élongation** $x\sim R\varepsilon$ et une **constante de raideur** $k\sim3\pi\gamma_{GR}$. Le globule se comporte donc comme un ressort élastique pour de petites déformations. 
AN pour $\varepsilon=0{,}10$ : $\|\vec F_\gamma\|=3\pi\cdot5\times10^{-5}\cdot3\times10^{-6}\cdot0{,}10\approx\boxed{1{,}4\times10^{-10}\ \mathrm N}$ (≈ 0,14 nN).

### 3.2 Pression de radiation : approche corpusculaire

**Q44.**

$\vec p=\hbar\vec k$, de norme $p=\hbar k=\hbar\dfrac{n\omega}{c}=\dfrac{nE}{c}$ (car $E=\hbar\omega$ et $k=n\omega/c$). 
L'énergie $E=\hbar\omega$ dépend de la **fréquence**, conservée à la traversée de l'interface : $E$ ne dépend **pas** du milieu (seuls $k$ et $\lambda$ changent).

**Q45.**

$N$ photons par unité de temps et de surface frappent $\mathrm dS$. 
Chaque photon incident porte $+\dfrac{n_1E}{c}\vec u_z$ ; la fraction $R$ est réfléchie ($-\dfrac{n_1E}{c}\vec u_z$) et la fraction $T$ transmise ($+\dfrac{n_2E}{c}\vec u_z$). La variation de quantité de mouvement des photons par unité de temps est

$$
\overrightarrow{\mathrm dp}=N\,\mathrm dS\,\frac Ec\big[-Rn_1+Tn_2-n_1\big]\vec u_z .
$$

Par réaction, la force sur l'interface vaut

$$
\boxed{\overrightarrow{\mathrm dF}=-\overrightarrow{\mathrm dp}=\frac{NE}{c}\big[n_1(1+R)-n_2T\big]\,\mathrm dS\,\vec u_z.}
$$

**Q46.**

En incidence oblique $\theta_i$, tous les rayons sont coplanaires. 
La composante tangentielle ($x$) de la quantité de mouvement entrante est $n_1\dfrac Ec\sin\theta_i$ ; la sortante vaut $R\,n_1\dfrac Ec\sin\theta_r+T\,n_2\dfrac Ec\sin\theta_t$. 
Or $\theta_r=\theta_i$ (réflexion) et $n_2\sin\theta_t=n_1\sin\theta_i$ (Snell‑Descartes), d'où la sortante $=(R+T)n_1\dfrac Ec\sin\theta_i=n_1\dfrac Ec\sin\theta_i$ (car $R+T=1$ en énergie). 
La variation tangentielle est **nulle** : la force totale de pression de radiation est **selon la normale** $\vec u_z$.

**Q47.**

En $\theta_i=0$, (10) donne $P_{\text{rad}}(0)=\dfrac{n_1I}{c}\big[1+R-\tfrac{n_2}{n_1}T\big]$. Or $I=NE$ (puissance par unité de surface), donc $\dfrac{\mathrm dF}{\mathrm dS}=\dfrac Ic\big[n_1(1+R)-n_2T\big]=\dfrac{n_1I}{c}\big[1+R-\tfrac{n_2}{n_1}T\big]$ : **compatible** avec Q45.
Pour $n_1>n_2$ (ex. $1{,}38>1{,}35$) : $R\approx1{,}2\times10^{-4}$, $T\approx1{,}00$, $\big[1+R-\tfrac{n_2}{n_1}T\big]\approx+0{,}022>0$. 
La force est selon $+\vec u_z$, dans le sens de propagation (du milieu $1$ vers le milieu $2$) : l'interface est poussée **vers le milieu de plus faible indice** ($n_2$).

**Q48.**

Photons du milieu $2$ ($n_2$) vers le milieu $1$ ($n_1$). 
*Schéma : rayon incident et réfléchi dans $2$, transmis dans $1$, $\theta_i$ dans $2$, $\theta_t$ dans $1$.* 
Le même bilan donne, en incidence normale, $P_{\text{rad}}(0)=\dfrac{n_2I}{c}\big[1+R-\tfrac{n_1}{n_2}T\big]$. 
Avec $n_1>n_2$ : $\tfrac{n_1}{n_2}T>1$, le crochet $\approx-0{,}022<0$ : la force est selon $-\vec u_z$, **à nouveau orientée vers le milieu de plus faible indice** $n_2$. 
Conclusion (contre‑intuitive) : quel que soit le sens de propagation, la pression de radiation déforme l'interface **vers le milieu d'indice le plus faible**.

**Q49.**

Faisceau cylindrique uniforme de puissance $\mathcal P$ et demi‑largeur $w_0$ : $I=\dfrac{\mathcal P}{\pi w_0^2}$. D'où, pour une incidence quelconque $\theta_i$ (milieu $1\to2$),

$$
\boxed{P_{\text{rad}}(\theta_i)=\frac{n_1}{c}\frac{\mathcal P}{\pi w_0^2}\cos^2\theta_i\!\left[1+R(\theta_i,\theta_t)-\frac{n_2\cos\theta_t}{n_1\cos\theta_i}T(\theta_i,\theta_t)\right].}
$$

**Q50.**

Pour $n_1>n_2$ (propagation $1\to2$), il existe un **angle de réflexion totale** $\boxed{\theta^*=\arcsin(n_2/n_1)}$. 
Pour $\theta_i\ge\theta^*$ : $R=1$, $T=0$, d'où $P_{\text{rad}}=2\dfrac{n_1I}{c}\cos^2\theta_i$. 
La pression croît en approchant $\theta^*$ (contribution transmise qui s'éteint, réflexion qui monte vers $1$) d'où le **maximum en $\theta^*$** ; au‑delà, $P_{\text{rad}}$ **décroît** en $\cos^2\theta_i$.

**Q51.**


En incidence normale,
$$P_{\mathrm{rad}}(0)=\frac{I}{c}[n_1(1+R)-n_2T],\qquad I=\frac{\mathcal P}{\pi w_0^2}.$$
Les coefficients de Fresnel deviennent
$$R=\left(\frac{n_1-n_2}{n_1+n_2}\right)^2,\qquad T=\frac{4n_1n_2}{(n_1+n_2)^2}.$$
Avec $\mathcal P=0,5$ W, $w_0=10\ \mu$m, $n_1=1,38$ et $n_2=1,35$, on trouve $I\simeq1,59\times10^9$ W/m², $R\simeq1,21\times10^{-4}$ et
$$\boxed{P_{\mathrm{rad}}(0)\simeq0,16\ \mathrm{Pa}.}$$
Cette pression est environ deux cents fois plus petite que la surpression de Laplace $2\gamma/R\simeq33$ Pa. Les deux pressions ne sont pas du même ordre de grandeur ; la déformation se calcule par le bilan de forces des questions suivantes.

### 3.3 Déformation et rhéologie

**Q52.**

Le globule ($n_{GR}=n_1>n_{\text{ext}}=n_2$) est traversé par le laser selon $+z$. **Face avant** (extérieur $\to$ intérieur, $n_2\to n_1$) : d'après Q48 la force vise le milieu de plus faible indice (extérieur, côté $-z$) → l'interface avant est tirée vers $-z$. 
**Face arrière** (intérieur $\to$ extérieur, $n_1\to n_2$) : la force vise encore le faible indice (extérieur, côté $+z$) → tirée vers $+z$. Les deux faces sont donc **tirées vers l'extérieur le long de l'axe** : le globule **s'allonge selon la direction du laser** (ellipsoïde prolate), conformément à la figure 19b.
*Schéma : sphère, flèches de force sortantes aux pôles avant ($-z$) et arrière ($+z$), ellipsoïde allongé selon $z$.*

**Q53.**

En incidence quasi normale, la **force sur la face avant** ($2\to1$, Q48) vaut, en module,

$$
F_{\text{av}}=\frac{n_2\mathcal P}{c}\left[\frac{n_1}{n_2}T-1-R\right]\quad(\text{orientée vers }-z,\ \text{vers l'extérieur}).
$$

La puissance **transmise** dans le globule est $T\mathcal P$ ; la **force sur la face arrière** ($1\to2$, Q47) s'en déduit :

$$
F_{\text{ar}}=\frac{n_1\,(T\mathcal P)}{c}\left[1+R-\frac{n_2}{n_1}T\right]\quad(\text{orientée vers }+z,\ \text{vers l'extérieur}).
$$

Les deux forces étirent le globule selon $z$.

**Q54.**


Posons les modules des forces Q53
$$F_a=\frac{\mathcal P}{c}[n_1T-n_2(1+R)],$$
$$F_r=\frac{\mathcal PT}{c}[n_1(1+R)-n_2T].$$
Les deux forces pointent vers l'extérieur. Leur composante symétrique d'étirement vaut $F_{\mathrm{étir}}=(F_a+F_r)/2$ ; leur différence produit une translation et sera discutée en Q55. Dans le modèle de faible déformation de Q43,
$$3\pi\gamma_{GR}R\varepsilon=F_{\mathrm{étir}}.$$
En utilisant $\mathcal P=\pi w_0^2I$,
$$\boxed{\gamma_{GR}\varepsilon=\frac{w_0^2I}{6Rc}\left[n_1T(2+R)-n_2(1+R+T^2)\right].}$$
Le contraste d'indice étant faible, $R\ll1$, $T\simeq1$ et les deux forces ont des modules voisins de $\mathcal P(n_1-n_2)/c$. Au premier ordre en ce contraste,
$$\boxed{\gamma_{GR}\varepsilon\simeq\frac{(n_1-n_2)w_0^2}{3Rc}I.}$$
La pente de la déformation en fonction de l'intensité donne donc la tension superficielle pour une géométrie et des indices connus.

**Q55.**


Avec $+z$ dans le sens du faisceau, la face avant subit $-F_a\vec u_z$ et la face arrière $+F_r\vec u_z$. En sommant les expressions Q53,
$$\vec F_{\mathrm{tot}}=\frac{\mathcal P}{c}\left[n_2(1+R-T^2)+n_1TR\right]\vec u_z.$$
Comme $T=1-R$,
$$\boxed{\vec F_{\mathrm{tot}}=\frac{\mathcal P R}{c}[n_2(3-R)+n_1(1-R)]\vec u_z.}$$
Le coefficient est positif : le globule est poussé dans le sens de propagation, même si les forces principales étirent ses deux faces en sens opposés. Dans l'approximation négligeant les réflexions internes multiples retenue en Q53, la formule ci-dessus est la résultante correspondante.

Pour les deux faisceaux identiques et contrapropageants, les résultantes de translation sont opposées et se compensent ; les contributions d'étirement s'ajoutent. Représentation : deux lasers alignés sur $Oz$, l'un vers $+z$, l'autre vers $-z$, avec le globule centré sur leur axe commun. Cette compensation évite une dérive axiale ; à elle seule, dans des faisceaux parfaitement uniformes, elle ne prouve pas un rappel stable après tout déplacement.

