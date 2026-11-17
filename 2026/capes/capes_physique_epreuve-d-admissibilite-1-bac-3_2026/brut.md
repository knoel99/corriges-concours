# CAPES Physique — Épreuve d'admissibilité 1 (bac+3) 2026 · Corrigé brut

*Corrigé rédigé par IA, non officiel. Signalez toute erreur.*

Tronc traité : **majeure physique (14 points) + mineure chimie (6 points)**. Épreuve de 4 heures, calculatrice autorisée, sans document. La célérité de la lumière dans le vide est notée $c$, fixée à $299\,792\,458~\text{m}\cdot\text{s}^{-1}$.

## MAJEURE PHYSIQUE (14 points) — Une histoire de la mesure de la célérité de la lumière dans le vide

### Partie A — Mesure de $c$ par circuits électriques : Rosa & Dorsey (1907)

**A.1 — La théorie électromagnétique de Maxwell.**

#### Q1

Dans un espace vide de charge et de courant ($\rho=0$, $\vec\jmath=\vec 0$), les équations de Maxwell deviennent :

$$
\begin{aligned}
\operatorname{div}\vec E&=0, & \operatorname{div}\vec B&=0,\\
\overrightarrow{\operatorname{rot}}\,\vec E&=-\frac{\partial\vec B}{\partial t}, &
\overrightarrow{\operatorname{rot}}\,\vec B&=\mu_0\varepsilon_0\frac{\partial\vec E}{\partial t}.
\end{aligned}
$$

#### Q2

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

#### Q3

Posons $E(z,t)=E(t-z/c)$. À l'instant $t+\Delta t$ et à l'abscisse $z$, le champ vaut $E(t+\Delta t-z/c)$. Or :

$$
E\!\left(t+\Delta t-\frac{z}{c}\right)=E\!\left(t-\frac{z-c\Delta t}{c}\right),
$$

c'est-à-dire la valeur qu'avait le champ à l'instant $t$ à l'abscisse $z-\Delta z$ avec $\Delta z=c\,\Delta t>0$. Le profil se translate donc sans déformation vers les $z$ croissants, à la célérité $c$
 : il s'agit d'une **onde plane progressive** se propageant selon $+\vec e_z$ à la vitesse $c$. *Schéma attendu : le profil $E(z)$ tracé à $t$ et à $t+\Delta t$,
 identique et décalé de $\Delta z=c\Delta t$ vers la droite.* $\square$

#### Q4

La phase $\varphi=\omega(t-z/c)$ ne dépend spatialement que de $z$ : les surfaces équiphases sont les plans $z=\text{cte}$, l'onde est **plane**. La dépendance temporelle est sinusoïdale à la pulsation unique $\omega$ : l'onde est **harmonique** (monochromatique). Le champ $\vec E=E\,\vec e_x$
 est orthogonal à la direction de propagation $\vec e_z$ : l'onde est **transverse**. Enfin $\vec E$ garde une direction fixe $\vec e_x$ au cours du temps : la polarisation est **rectiligne**. $\square$

#### Q5

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

#### Q6

En négligeant les effets de bord, les plaques sont assimilées à des plans infinis uniformément chargés. Pour un point $M$ quelconque, les deux plans verticaux orthogonaux passant par $M$ sont des plans de symétrie de la distribution. Le champ électrique en $M$ appartient à ces deux plans ; leur intersection est la droite normale aux armatures passant par $M$. **Le champ est donc perpendiculaire aux plaques en tout point.**

Entre les armatures, il est dirigé de la plaque positive ($z=d$) vers la plaque négative ($z=0$), donc selon $-\vec e_z$.

#### Q7

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

#### Q8

Le plan supérieur ($\sigma=+Q/A_C$) crée $\vec E=+\frac{Q}{2\varepsilon_0 A_C}\vec e_z$ pour $z>d$ et $\vec E=-\frac{Q}{2\varepsilon_0 A_C}\vec e_z$ pour $z<d$. Par le **principe de superposition**, dans les trois zones :

- $z<0$ : $\vec E=\vec 0$ ;
- $0<z<d$ : $\boxed{\vec E=-\dfrac{Q}{\varepsilon_0 A_C}\vec e_z}$ ;
- $z>d$ : $\vec E=\vec 0$.

Le champ est nul à l'extérieur du condensateur et uniforme entre les armatures. *Schéma attendu : les vecteurs $\vec E$ dans les trois zones $z<0$, $0<z<d$, $z>d$.* $\square$

#### Q9

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

#### Q10

Les $n$ condensateurs unitaires sont en parallèle : soumis à la même tension $U$, ils portent chacun la charge $Q=C_uU$. La charge totale vaut $Q_{\text{tot}}=nQ=nC_uU$, donc $C_n=Q_{\text{tot}}/U=nC_u$, soit :

$$
\boxed{C_n=\frac{n\,\varepsilon_0 A_C}{d}.}
$$
$\square$

**A.2.b — La bobine.**

#### Q11

La distribution de courants est invariante par rotation autour de $Oz$ et par translation selon $Oz$ (solénoïde infini). Tout plan perpendiculaire à $Oz$ est plan de symétrie des courants : $\vec B$, pseudo-vecteur, lui est perpendiculaire, donc $\vec B\parallel\vec e_z$.
 Pour $i>0$, la règle de la main droite donne $\vec B$ selon $+\vec e_z$ à l'intérieur :

$$
\boxed{\vec B\parallel+\vec e_z\ \text{à l'intérieur du solénoïde.}}
$$
$\square$

#### Q12

**Théorème d'Ampère** (magnétostatique) : la circulation de $\vec B$ le long d'un contour fermé orienté $\mathcal C$ vaut $\mu_0$ fois l'intensité totale des **courants enlacés par le contour** :

$$
\boxed{\oint_{\mathcal C}\vec B\cdot\mathrm d\vec\ell=\mu_0\,I_{\text{enlacé}}.}
$$
$\square$

#### Q13

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

#### Q14

Le flux propre du champ magnétique à travers les $N$ spires est proportionnel à l'intensité qui le crée :

$$
\boxed{\Phi=L\,i,}
$$

relation qui **définit** le coefficient d'auto-induction $L$ (inductance propre, en henrys). $\square$

#### Q15

Le flux à travers une spire vaut $B\,A_L=\frac{\mu_0 N i}{\ell}A_L$ ; à travers les $N$ spires, $\Phi=N B A_L=\frac{\mu_0 N^2 A_L}{\ell}i$. Par identification à $\Phi=Li$ :

$$
\boxed{L=\frac{\mu_0 N^2 A_L}{\ell}.}
$$
$\square$

**A.2.c — Le circuit $LC$.**

#### Q16

Sur l'intervalle $[T_g/2,\,T_g]$, la tension du générateur est nulle : le circuit est une maille fermée $L$–$C$. Soit $u$ la tension aux bornes du condensateur (mesurée par l'oscilloscope) et $i$
 l'intensité dans la bobine, avec la convention récepteur pour le condensateur ($i=C\,\mathrm du/\mathrm dt$) et la loi des mailles $L\frac{\mathrm di}{\mathrm dt}+u=0$. En substituant :

$$
\boxed{\frac{\mathrm d^2u}{\mathrm dt^2}+\frac{1}{LC}\,u=0\qquad(t\in[T_g/2,\,T_g]).}
$$
$\square$

#### Q17

L'équation de Q16 est celle d'un oscillateur harmonique de pulsation propre $\omega_0=\frac{1}{\sqrt{LC}}$ ; sa solution est sinusoïdale, de période :

$$
\boxed{T=\frac{2\pi}{\omega_0}=2\pi\sqrt{LC}.}
$$
$\square$

#### Q18

Avec $T^2=4\pi^2LC$, $L=\frac{\mu_0 N^2 A_L}{\ell}$ (Q15) et $C=C_n+C_{osc}=\frac{\varepsilon_0 A_C}{d}n+C_{osc}$ (Q10) :

$$
\boxed{T^2=\frac{4\pi^2 N^2 A_L\mu_0}{\ell}\left(\frac{\varepsilon_0 A_C}{d}\,n+C_{osc}\right).}
$$
$\square$

#### Q19

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

#### Q20

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

### Partie B — Cavité cylindrique : Essen & Gordon-Smith (1948)

#### Q21

Le champ $\vec E=E_0(r)g(z)e^{i\omega t}\vec e_\theta$ est tangentiel aux trois parois métalliques, où sa composante tangentielle s'annule. Sur la paroi latérale $r=a$, $\vec e_\theta$ est tangent, d'où $E_0(a)=0$. Sur les bases $z=0$
 et $z=h$, $\vec e_\theta$ est aussi tangent, d'où $g(0)=0$ et $g(h)=0$. $\square$

#### Q22

Le champ vérifie l'équation d'onde du vide (Q2, avec $\mu_0\varepsilon_0=1/c^2$) : $\Delta\vec E-\frac{1}{c^2}\frac{\partial^2\vec E}{\partial t^2}=\vec 0$. Avec le laplacien cylindrique fourni et $\frac{\partial^2\vec E}{\partial t^2}=-\omega^2\vec E$, l'EDP vérifiée par $\underline E(r,z,t)=E_0(r)g(z)e^{i\omega t}$ est :

$$
\frac{\partial^2\underline E}{\partial r^2}+\frac{\partial^2\underline E}{\partial z^2}+\frac1r\frac{\partial\underline E}{\partial r}-\frac{\underline E}{r^2}+\frac{\omega^2}{c^2}\underline E=0.
$$

En substituant $\underline E=E_0(r)g(z)e^{i\omega t}$ et en divisant par $e^{i\omega t}$ :

$$
g\,E_0''+E_0\,g''+\frac{g}{r}E_0'-\frac{E_0 g}{r^2}+\frac{\omega^2}{c^2}E_0 g=0.
$$
$\square$

#### Q23

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

#### Q24

Posons $\beta=-k^2$ avec $k>0$ : $g(z)=A\sin(kz)+B\cos(kz)$. La condition $g(0)=0$ donne $B=0$
 ; la condition $g(h)=0$ donne $\sin(kh)=0$, soit $kh=p\pi$ avec $p\in\mathbb N^*$. Les modes autorisés sont :

$$
\boxed{g_p(z)=A_p\sin\!\left(\frac{p\pi z}{h}\right),\quad p\in\mathbb N^*.}
$$
$\square$

#### Q25

D'après la séparation de Q23, le membre radial vaut $-\frac{\omega^2}{c^2}-\beta=-\frac{\omega^2}{c^2}+k^2=-\frac{\omega^2}{c^2}+\frac{p^2\pi^2}{h^2}$. L'équation vérifiée par $E_0$ est donc :

$$
\boxed{\frac{\mathrm d^2E_0}{\mathrm dr^2}+\frac1r\frac{\mathrm dE_0}{\mathrm dr}-\frac{E_0(r)}{r^2}=E_0(r)\left(\frac{p^2\pi^2}{h^2}-\frac{\omega^2}{c^2}\right).}
$$
$\square$

#### Q26

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

#### Q27

La solution régulière en $r=0$ est $\tilde E_0(x)=J_1(x)$. La condition $E_0(a)=0$ (Q21) impose $J_1(\kappa a)=0$ : $\kappa a$
 doit être un **zéro de $J_1$**. En notant $x_n$ le $n$-ième zéro de $J_1$ ($x_1=3{,}832$,
 $x_2=7{,}016$, …), on a $\kappa a=x_n$, $n\in\mathbb N^*$ : seuls les modes $E_{0,n}$ existent. $\square$

#### Q28

Pour le mode $(n,p)$, $\kappa=x_n/a$ donne $E_0(r)=J_1(\frac{x_n r}{a})$ et $g(z)=\sin(\frac{p\pi z}{h})$. À une constante multiplicative $K$ près :

$$
\boxed{\underline E_{n,p}(r,z,t)=K\,J_1\!\left(\frac{x_n r}{a}\right)\sin\!\left(\frac{p\pi z}{h}\right)e^{i\omega t}\,\vec e_\theta.}
$$
$\square$

#### Q29

De $\kappa=x_n/a$ et $\kappa^2=\frac{\omega^2}{c^2}-\frac{p^2\pi^2}{h^2}$ :

$$
\frac{\omega^2}{c^2}=\frac{x_n^2}{a^2}+\frac{p^2\pi^2}{h^2}.
$$

Avec $\omega=2\pi f$, la fréquence du mode $(n,p)$ s'écrit :

$$
\boxed{f_{n,p}=c\sqrt{\frac{x_n^2}{4\pi^2 a^2}+\frac{p^2}{4h^2}}.}
$$
$\square$

#### Q30

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

### Partie C — Battements des modes longitudinaux d'un laser He-Ne : D'Orazio *et al.* (2010)

#### Q31

Une onde faisant un aller-retour dans la cavité parcourt le chemin optique $2n_{air}L_c$ ; la résonance impose un déphasage multiple de $2\pi$, soit $2n_{air}L_c=m\lambda$, $m\in\mathbb N$. D'où :

$$
\boxed{\lambda=\frac{2n_{air}L_c}{m}.}
$$

$$
\boxed{f_m=\frac{c}{\lambda}=\frac{m\,c}{2n_{air}L_c}.}
$$
$\square$

#### Q32

$s(t)^2=E_q^2\cos^2(2\pi f_q t)+E_{q+1}^2\cos^2(2\pi f_{q+1}t)+2E_qE_{q+1}\cos(2\pi f_q t)\cos(2\pi f_{q+1}t)$. En linéarisant aussi les $\cos^2$ ($\cos^2 a=\frac12(1+\cos2a)$) et le produit de cosinus :

$$
s(t)^2=\frac{E_q^2+E_{q+1}^2}{2}+\frac{E_q^2}{2}\cos(4\pi f_q t)+\frac{E_{q+1}^2}{2}\cos(4\pi f_{q+1}t)+E_qE_{q+1}\big[\cos(2\pi(f_q{+}f_{q+1})t)+\cos(2\pi(f_{q+1}{-}f_q)t)\big].
$$

Spectre de $s(t)^2$ : $\{0,\ 2f_q,\ 2f_{q+1},\ f_q+f_{q+1},\ f_{q+1}-f_q\}$. $\square$

#### Q33

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

#### Q34

D'après Q31, $f_{q+1}-f_q=\frac{(q+1)c}{2n_{air}L_c}-\frac{qc}{2n_{air}L_c}$, d'où :

$$
\boxed{f_b=\frac{c}{2n_{air}L_c}.}
$$
$\square$

#### Q35

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

## MINEURE CHIMIE (6 points)

### Partie A — Étude du nettoyage de l'argenterie

#### Q1

$A=108$ est le **nombre de masse** de l'atome d'argent (nombre de nucléons) ; $Z=47$ est le **numéro atomique** (nombre de charge, c'est-à-dire le nombre de protons, égal au nombre d'électrons de l'atome neutre). $\square$

#### Q2

Le soufre possède six électrons de valence. Il forme deux liaisons simples S–H et conserve **deux doublets non liants** :

```text
    ..
H — S — H
    ..
```

La répartition est de type $AX_2E_2$ : quatre domaines électroniques autour du soufre, dont deux doublets non liants. La molécule est donc **coudée**, et non linéaire.

#### Q3

Équation [1] : $4\,\text{Ag}+2\,\text{H}_2\text{S}+\text{O}_2=a\,\text{Ag}_2\text{S}+b\,\text{H}_2\text{O}$. Ag : $4=2a$ donc $a=2$ ; H : $4=2b$ donc $b=2$
 ; on vérifie S ($2=a$) et O ($2=b$). D'où :

$$
\boxed{a=2,\ b=2.}
$$
$\square$

#### Q4

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

#### Q5

Couples mis en jeu : $\text{Ag}_2\text{S}(\text{s})/\text{Ag}(\text{s})$ et $\text{Al(OH)}_3(\text{s})/\text{Al}(\text{s})$. Demi-équations en milieu acide, dans l'ordre oxydant/réducteur :

$$
\begin{aligned}
\text{Ag}_2\text{S}(\text{s})+2\,\text{H}^+(\text{aq})+2\,e^-&=2\,\text{Ag}(\text{s})+\text{H}_2\text{S}(\text{aq})\\
\text{Al}(\text{s})+3\,\text{H}_2\text{O}(\ell)&=\text{Al(OH)}_3(\text{s})+3\,\text{H}^+(\text{aq})+3\,e^-.
\end{aligned}
$$
$\square$

#### Q6

Aluminium ($Z=13$) : $1s^2\,2s^2\,2p^6\,3s^2\,3p^1$ ; électrons de valence $3s^2\,3p^1$. L'ion le plus stable est $\text{Al}^{3+}$ (perte des trois électrons de valence), de configuration $1s^2\,2s^2\,2p^6$ (celle du néon). $\square$

#### Q7

C'est une pile en court-circuit (contact direct des deux solides, sans fils). L'aluminium, réducteur le plus fort, s'oxyde : c'est l'**anode** (pôle $-$). Le sulfure d'argent se réduit à la surface de l'objet en argent : c'est la **cathode** (pôle $+$). Les électrons circulent dans le métal de l'anode (Al) vers la cathode (objet en Ag) ; le courant circule en sens inverse. *Schéma attendu : feuille d'Al et objet en Ag en contact dans la solution de NaCl, flèche $e^-$ de Al vers Ag.* $\square$

#### Q8

Le sel $(\text{Na}^+,\text{Cl}^-)$ joue le rôle d'**électrolyte** : il assure la conduction ionique dans la solution (fermeture du circuit), sans être consommé par la réaction [2]. La dénomination « bain de sel » est donc partiellement trompeuse : le nettoyage résulte d'une réaction électrochimique, le sel n'étant qu'un porteur de charges en solution. $\square$

#### Q9

L'eau chaude agit essentiellement comme **facteur cinétique** : l'élévation de température accroît la vitesse de la réaction (loi d'Arrhenius) et accélère le nettoyage ; elle augmente aussi la mobilité des ions, donc la conductivité de l'électrolyte. $\square$

### Partie B — Dosage de l'urée

#### Q10

Sur la figure 1 complétée : chaque atome d'azote porte **un** doublet non liant ; chaque atome d'oxygène porte **deux** doublets non liants (C=O du diacétylmonoxime, N–O**H** de l'oxime, deux C=O de l'urée et de la triazine, hydroxylamine $\text{H}_2\text{N}$–O**H** formée). $\square$

#### Q11

**Loi de Beer-Lambert** : $A=\varepsilon\,\ell\,c$, où $A$ est l'absorbance (sans unité), $\varepsilon$ le coefficient d'absorption molaire ($\text{L}\cdot\text{mol}^{-1}\cdot\text{cm}^{-1}$), $\ell$
 la longueur de la cuve ($\text{cm}$) et $c$ la concentration en triazine ($\text{mol}\cdot\text{L}^{-1}$). Valable en solution diluée, à $\lambda$ fixée. $\square$

#### Q12

Dosage par étalonnage à $\lambda=520~\text{nm}$ :

1. Préparer une **gamme étalon de triazine** : solutions d'urée de concentrations connues, traitées par le diacétylmonoxime en excès en milieu acide et chauffées (l'urée seule, incolore, ne peut être dosée directement) ;
2. régler le spectrophotomètre sur $\lambda=520~\text{nm}$ et faire le **blanc** (réactifs sans urée) ;
3. mesurer $A$ pour chaque étalon et tracer la droite d'étalonnage $A=f(c)$ ;
4. traiter l'échantillon dans les mêmes conditions, mesurer son $A$ et lire $c$ sur la droite. $\square$

#### Q13

Un catalyseur accélère la réaction en abaissant l'énergie d'activation, sans figurer dans le bilan et sans être consommé ; il ne modifie **pas** la thermodynamique (ni la constante d'équilibre, ni le rendement). L'uréase est ici un catalyseur enzymatique, spécifique. $\square$

#### Q14

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

#### Q15

L'acide **chlorhydrique** $(\text{H}^+,\text{Cl}^-)$ convient : monoacide fort, ne réagissant pas avec les ions en jeu (l'acide nitrique conviendrait aussi). $\square$

#### Q16

Soit $n_0=C_0V_0$ la quantité initiale d'urée. L'hydrolyse (catalysée par l'uréase) donne $1$ urée $\to 2\,\text{NH}_4^+ + \text{CO}_3^{2-}$, donc $n(\text{NH}_4^+)=2C_0V_0$ et $n(\text{CO}_3^{2-})=C_0V_0$.
 On ajoute $n(\text{H}^+)=CV_a$ (en excès). Tableau d'avancement de $\text{CO}_3^{2-}+2\,\text{H}^+\to\text{CO}_2+\text{H}_2\text{O}$ (carbonate limitant) :

| | $\text{CO}_3^{2-}$ | $\text{H}^+$ | $\text{CO}_2$ | $\text{NH}_4^+$ |
|---|---|---|---|---|
| état initial | $C_0V_0$ | $CV_a$ | $0$ | $2C_0V_0$ |
| état final | $0$ | $CV_a-2C_0V_0$ | $C_0V_0$ | $2C_0V_0$ |

Avant dosage, la solution contient $CV_a-2C_0V_0$ mol de $\text{H}^+$ en excès, $C_0V_0$ mol de $\text{CO}_2$ et $2C_0V_0$
 mol de $\text{NH}_4^+$. $\square$

#### Q17

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
