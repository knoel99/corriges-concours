# Agrégation Physique — Composition de physique 2026 · Corrigé guidé

*Corrigé rédigé par IA, non officiel. Signalez toute erreur.*

## Présentation du sujet

Session 2026, composition de physique (5 heures). Sujet « Étude d'écoulements tourbillonnaires en géophysique » en deux parties largement indépendantes : la partie I enchaîne les équations de base de la dynamique des fluides (Q1–Q5), les maëlstroms et l'analogie hydromagnétique (Q6–Q15), les allées de von Kármán avec l'optique des lames de savon (Q16–Q34) et les spirales d'Ekman en référentiel terrestre non galiléen (Q35–Q46) ; la partie II traite la structure interne de la Terre (statique lithostatique Q47–Q50, champ de gravitation par le théorème de Gauss Q51–Q56) puis un modèle de convection du noyau (Q57–Q69). 69 questions au total.

**Questions de cours.** Certaines questions, repérées par un numéro en contraste inversé dans le sujet (Q1, Q7, Q8, Q12, Q17, Q19–Q22, Q35–Q38, Q47, Q48, Q51–Q54, Q65), portent sur la présentation de lois ou la démonstration de résultats généraux ; elles représentent « environ 50% du barème » selon le rapport 2026.

**Barème et statistiques (rapport 2026, p. 10-14/59).** « 40% des points sont attribués à la restitution de connaissances », 5 % à la compétence S'APPROPRIER, 21 % ANALYSER, 22 % RÉALISER, 12 % VALIDER. Moyennes : 7,3/20 pour les candidats, 11,1/20 pour les admissibles. « En moyenne, les candidats ont abordé 53% des questions (64% pour les questions de restitution de connaissances). Le taux moyen de réussite aux questions abordées est de 61% » ; la meilleure copie a abordé 98 % des questions et répondu correctement à 89 % d'entre elles. Taux de réussite par sous-partie (figure CP-3) : I.A ≈ 60 %, I.B ≈ 44 %, I.C ≈ 22 %, I.D ≈ 33 %, II.A ≈ 37 %, II.B ≈ 18 % — les parties I.C (optique + von Kármán) et II.B (convection) sont les plus discriminantes.

**Exigences de rédaction du jury.**

> [!JURY]
> « Une démonstration de cours telle que celle-ci nécessite quelques phrases brèves, une définition du système et de la transformation étudiés, ainsi qu’un schéma permettant de spécifier les conventions d’orientation. Une suite de calculs sans explication, même parfaitement menée, ne permet pas d’obtenir la totalité des points. [...] Les flèches sur les vecteurs et les opérateurs qui en nécessitent sont un impératif de rigueur. »

> [!JURY]
> « Le correcteur doit comprendre immédiatement la démarche suivie par le candidat pour répondre à une question et vérifier que les hypothèses essentielles sont mentionnées. »

> [!JURY]
> « à utiliser un langage clair et précis, à veiller à la rigueur de la syntaxe et à la correction de l’orthographe ; à veiller à l’emploi irréprochable du vocabulaire scientifique (par exemple [...] à ne pas inverser cohérence spatiale et cohérence temporelle) ; à définir les acronymes [...] ; à accompagner les calculs de brèves phrases explicatives »

Les indications ci-dessous sont graduées et ne donnent jamais le résultat ; la solution complète figure sous chaque question.

## Partie I — Écoulements tourbillonnaires océaniques

### I.A — Résultats généraux

#### Q1

> [!INDICATION]
> Bilan de masse eulérien sur un volume **fixe** $\mathcal V$ délimité par $\mathcal S$ ; passage local par Green-Ostrogradski. Démonstration brève, soignée, avec flèches.

#### Solution

La masse contenue dans $\mathcal V$ fixe, $M=\iiint_{\mathcal V}\mu\,\mathrm d\mathcal V$, ne varie que par le flux de masse $\mu\vec v$ sortant de $\mathcal S$ :

$$
\frac{\mathrm dM}{\mathrm dt}=-\iint_{\mathcal S}\mu\vec v\cdot\vec n_{\text{ext}}\,\mathrm dS .
$$

$\mathcal V$ étant fixe, $\dfrac{\mathrm dM}{\mathrm dt}=\iiint_{\mathcal V}\dfrac{\partial\mu}{\partial t}\mathrm d\mathcal V$. Green-Ostrogradski donne $\iint_{\mathcal S}\mu\vec v\cdot\vec n_{\text{ext}}\mathrm dS=\iiint_{\mathcal V}\operatorname{div}(\mu\vec v)\,\mathrm d\mathcal V$. Pour tout $\mathcal V$ :

$$
\boxed{\dfrac{\partial\mu}{\partial t}+\operatorname{div}(\mu\vec v)=0.}
$$

#### Q2

> [!INDICATION]
> Définir « à flux conservatif » (divergence nulle), puis utiliser l'incompressibilité ($\mu$ uniforme et constante) dans la relation (1).

#### Solution

Un champ est **à flux conservatif** si son flux à travers toute surface fermée est nul, c'est-à-dire si sa **divergence est nulle** en tout point. Pour un fluide incompressible, $\mu$ est uniforme et constante ; (1) donne $\mu\operatorname{div}\vec v=0$, soit $\boxed{\operatorname{div}\vec v=0}$ : $\vec v$ est à flux conservatif. **Conséquence** : le flux de $\vec v$ (le débit volumique) se conserve le long d'un **tube de courant**, $v\,S=\text{cste}$ (le fluide accélère là où le tube se resserre).

#### Q3

> [!INDICATION]
> Dérivée totale (lagrangienne) en suivant la particule : $x=x(t)$ avec $\dot x=v$.

#### Solution

À 1D, la particule en $x$ a la vitesse $v(x,t)$ ; son accélération est la dérivée totale

$$
a(x,t)=\frac{\mathrm d}{\mathrm dt}v(x(t),t)=\frac{\partial v}{\partial t}+\dot x\,\frac{\partial v}{\partial x}=\frac{\partial v}{\partial t}+v\,\frac{\partial v}{\partial x}.
$$

Pour un écoulement quelconque, sans démonstration :

$$
\boxed{\vec a=\frac{\partial\vec v}{\partial t}+(\vec v\cdot\overrightarrow{\operatorname{grad}})\vec v=\frac{\mathrm D\vec v}{\mathrm Dt}}
$$

(dérivée particulaire du champ de vitesse).

#### Q4

> [!INDICATION]
> RFD sur une particule de volume $\mathrm d\tau$, de masse $\mu\,\mathrm d\tau$ ; additionner forces volumiques $\times\,\mathrm d\tau$ et diviser par $\mathrm d\tau$.

#### Solution

Sur la particule de masse $\mu\,\mathrm d\tau$ s'exercent : la force extérieure $\vec f_v\,\mathrm d\tau$, la force de pression $-\overrightarrow{\operatorname{grad}}P\,\mathrm d\tau$ et la force de viscosité $\eta\Delta\vec v\,\mathrm d\tau$. La RFD $\mu\,\mathrm d\tau\,\dfrac{\mathrm D\vec v}{\mathrm Dt}=\big(\vec f_v-\overrightarrow{\operatorname{grad}}P+\eta\Delta\vec v\big)\mathrm d\tau$ donne, après division par $\mathrm d\tau$ :

$$
\boxed{\mu\!\left[\frac{\partial\vec v}{\partial t}+(\vec v\cdot\overrightarrow{\operatorname{grad}})\vec v\right]=\vec f_v-\overrightarrow{\operatorname{grad}}P+\eta\Delta\vec v.}
$$

#### Q5

> [!INDICATION]
> Identifier les deux termes, comparer leurs **normes** par analyse d'ordres de grandeur.

#### Solution

Terme **convectif** $\mu(\vec v\cdot\overrightarrow{\operatorname{grad}})\vec v$ ; terme **diffusif** $\eta\Delta\vec v$. En ordres de grandeur, avec vitesse $V$ et longueur $L$ :

$$
\|\mu(\vec v\cdot\overrightarrow{\operatorname{grad}})\vec v\|\sim\frac{\mu V^2}{L},\qquad\|\eta\Delta\vec v\|\sim\frac{\eta V}{L^2}.
$$

Le rapport vaut $\dfrac{\mu V^2/L}{\eta V/L^2}=\boxed{\dfrac{\mu V L}{\eta}=\mathcal R e}$.

### I.B — Maëlstroms de Saltstraumen

#### Q6

> [!INDICATION]
> AN avec $V=40\,\mathrm{km\cdot h^{-1}}$, $L\sim10$ m ; conclure sur le terme visqueux.

#### Solution

$V=\dfrac{40\times10^3}{3600}=11{,}1\ \mathrm{m\,s^{-1}}$, $L\sim10$ m :

$$
\mathcal R e=\frac{\mu_{\text{eau}}VL}{\eta_{\text{eau}}}=\frac{998{,}3\times11{,}1\times10}{1{,}003\times10^{-3}}\approx\boxed{1{,}1\times10^{8}.}
$$

$\mathcal R e\gg1$ : le terme diffusif $\eta\Delta\vec v$ est négligeable devant le terme convectif ; on néglige la viscosité.

> [!JURY]
> « et non 6 ou 7 »

#### Q7

> [!INDICATION]
> Écrire les deux équations locales du champ magnétostatique, puis les deux équations locales de l'écoulement, et identifier l'analogie.

#### Solution

Magnétostatique : $\operatorname{div}\vec B=0$ et $\overrightarrow{\operatorname{rot}}\vec B=\mu_0\vec\jmath$. Écoulement incompressible : $\operatorname{div}\vec v=0$ (Q2) et $\overrightarrow{\operatorname{rot}}\vec v=\vec\Omega$ (définition de la vorticité). Les systèmes sont **formellement identiques** :

| Magnétostatique | Écoulement |
|---|---|
| $\operatorname{div}\vec B=0$ | $\operatorname{div}\vec v=0$ |
| $\overrightarrow{\operatorname{rot}}\vec B=\mu_0\vec\jmath$ | $\overrightarrow{\operatorname{rot}}\vec v=\vec\Omega$ |

$$
\boxed{\vec B\ \leftrightarrow\ \vec v,\qquad \mu_0\vec\jmath\ \leftrightarrow\ \vec\Omega.}
$$

#### Q8

> [!INDICATION]
> Déduire le théorème d'Ampère de $\overrightarrow{\operatorname{rot}}\vec B=\mu_0\vec\jmath$ par Stokes-Ampère, en définissant l'intensité enlacée.

#### Solution

Schéma : contour fermé orienté $\Gamma$, surface $\mathcal S$ s'appuyant dessus, normale $\vec n$ orientée par la règle de la main droite..
Pour tout contour fermé orienté $\Gamma$ s'appuyant sur une surface $\mathcal S$ :

$$
\oint_\Gamma\vec B\cdot\mathrm d\vec\ell\overset{\text{Stokes}}{=}\iint_{\mathcal S}\overrightarrow{\operatorname{rot}}\vec B\cdot\vec n\,\mathrm dS=\mu_0\iint_{\mathcal S}\vec\jmath\cdot\vec n\,\mathrm dS=\mu_0\,I_{\text{enlacé}},
$$

où $I_{\text{enlacé}}$ est l'intensité **algébrique** traversant $\mathcal S$ (comptée positivement dans le sens de $\vec n$). $\boxed{\oint_\Gamma\vec B\cdot\mathrm d\vec\ell=\mu_0 I_{\text{enlacé}}}$.

#### Q9

> [!INDICATION]
> Symétries/invariances **de la distribution de courants**.

#### Solution

$\vec\jmath=j\,\vec u_z$ (pour $r\le a$) est invariant par rotation autour de $(Oz)$ et par translation selon $z$ : $\vec B$ ne dépend que de $r$. Pour un point $M$ repéré par $r$, le plan $(M,\vec u_r,\vec u_z)$ **contient le courant** : c'est un plan de symétrie de la distribution. $\vec B$ (pseudovecteur) lui est orthogonal, donc $\boxed{\vec B=B(r)\,\vec u_\theta}$.

#### Q10

> [!INDICATION]
> Théorème d'Ampère sur un cercle d'axe $(Oz)$, rayon $r$, orienté selon $\vec u_\theta$.

#### Solution

Schéma : cercle d'Ampère de rayon $r$, orienté selon $+\vec u_\theta$.. $\oint\vec B\cdot\mathrm d\vec\ell=B(r)\,2\pi r$.
- $r\le a$ : $I_{\text{enlacé}}=j\,\pi r^2$, d'où $\boxed{\vec B=\dfrac{\mu_0 j\,r}{2}\vec u_\theta}$ ;
- $r>a$ : $I_{\text{enlacé}}=j\,\pi a^2$, d'où $\boxed{\vec B=\dfrac{\mu_0 j\,a^2}{2r}\vec u_\theta}$.

#### Q11

> [!INDICATION]
> Appliquer $\vec v\leftrightarrow\vec B$, $\vec\Omega\leftrightarrow\mu_0\vec\jmath$ (Q7) aux résultats de Q10.

#### Solution

$\mu_0 j\to\Omega$ :

$$
\boxed{\vec v(r)=\begin{cases}\dfrac{\Omega\,r}{2}\,\vec u_\theta & r\le a\\[2mm]\dfrac{\Omega\,a^2}{2r}\,\vec u_\theta & r>a\end{cases}}
$$

Schéma : $v(r)$ croît linéairement de $0$ (en $r=0$) à $v_{\max}=\Omega a/2$ (en $r=a$), puis décroît en $1/r$ ; axes légendés $v$ et $r$..
« L'œil du cyclone » : au centre $r=0$, $v=0$ — la zone centrale est **calme**, bien que l'écoulement tourbillonne vigoureusement autour.

#### Q12

> [!INDICATION]
> Démontrer Bernoulli pour écoulement **irrotationnel** à partir d'Euler, via l'identité $(\vec v\cdot\overrightarrow{\operatorname{grad}})\vec v=\overrightarrow{\operatorname{grad}}(v^2/2)+(\overrightarrow{\operatorname{rot}}\vec v)\wedge\vec v$.

#### Solution

**Hypothèses** : fluide parfait ($\eta\to0$), écoulement **stationnaire, incompressible et homogène**, **irrotationnel**, forces volumiques de pesanteur $\mu\vec g=-\mu g\,\vec u_z=-\overrightarrow{\operatorname{grad}}(\mu gz)$. Euler stationnaire :

$$
\mu(\vec v\cdot\overrightarrow{\operatorname{grad}})\vec v=-\overrightarrow{\operatorname{grad}}P+\mu\vec g.
$$

Avec l'identité et $\overrightarrow{\operatorname{rot}}\vec v=\vec0$ : $\mu\,\overrightarrow{\operatorname{grad}}\!\big(\tfrac{v^2}{2}\big)=-\overrightarrow{\operatorname{grad}}P-\overrightarrow{\operatorname{grad}}(\mu gz)$, soit

$$
\overrightarrow{\operatorname{grad}}\!\left(P+\tfrac12\mu v^2+\mu gz\right)=\vec0\ \Rightarrow\ \boxed{P+\tfrac12\mu v^2+\mu gz=\text{cste (uniforme dans tout le fluide).}}
$$

> [!JURY]
> « fluide incompressible et homogène »

#### Q13

> [!INDICATION]
> $r>a$ est irrotationnel : appliquer Bernoulli entre un point de la surface très loin ($r\to\infty$, $v=0$, $z=0$, $P=P_0$) et un point $(r,z)$.

#### Solution

Les conditions de Q12 sont réunies pour $r>a$. La constante, évaluée très loin en surface, vaut $P_0$. Donc $P(r,z)+\tfrac12\mu v(r)^2+\mu gz=P_0$, avec $v(r)=\dfrac{\Omega a^2}{2r}$ :

$$
\boxed{P(r,z)=P_0-\mu gz-\frac{\mu\,\Omega^2 a^4}{8r^2}\qquad(r>a).}
$$

#### Q14

> [!INDICATION]
> Pour $r\le a$ l'écoulement est **rotationnel** : Bernoulli inapplicable entre deux lignes de courant. Utiliser Euler projeté (accélération centripète).

#### Solution

Bernoulli ne s'applique pas ici (écoulement rotationnel). Avec $\vec v=\tfrac{\Omega r}{2}\vec u_\theta$, l'accélération convective est purement centripète : $(\vec v\cdot\overrightarrow{\operatorname{grad}})\vec v=-\dfrac{v_\theta^2}{r}\vec u_r=-\dfrac{\Omega^2 r}{4}\vec u_r$. Euler $\mu(\vec v\cdot\overrightarrow{\operatorname{grad}})\vec v=-\overrightarrow{\operatorname{grad}}P+\mu\vec g$ se projette :

$$
\frac{\partial P}{\partial r}=\frac{\mu\Omega^2 r}{4},\qquad\frac{\partial P}{\partial z}=-\mu g.
$$

Intégration : $P(r,z)=\dfrac{\mu\Omega^2 r^2}{8}-\mu gz+C$. Continuité en $r=a$ avec Q13 : $\dfrac{\mu\Omega^2 a^2}{8}+C=P_0-\dfrac{\mu\Omega^2 a^2}{8}$, d'où $C=P_0-\dfrac{\mu\Omega^2 a^2}{4}$ :

$$
\boxed{P(r,z)=P_0-\mu gz+\mu\Omega^2\!\left(\frac{r^2}{8}-\frac{a^2}{4}\right).}
$$

#### Q15

> [!INDICATION]
> La surface libre est l'isobare $P=P_0$ ; en déduire $z(r)$ à l'intérieur et à l'extérieur, puis la profondeur du creux.

#### Solution

**Surface libre** : $P(r,z_s)=P_0$.
- $r\le a$ : $z_s(r)=\dfrac{\Omega^2}{g}\!\left(\dfrac{r^2}{8}-\dfrac{a^2}{4}\right)$, minimale au centre : $z_s(0)=-\dfrac{\Omega^2 a^2}{4g}$ ;
- $r>a$ : $z_s(r)=-\dfrac{\Omega^2 a^4}{8gr^2}\to0$ quand $r\to\infty$ (raccord en $r=a$ : $z_s=-\Omega^2a^2/8g$).

Schéma : surface plane loin ($z=0$), s'affaissant en un creux centré, point le plus bas au centre..
Profondeur du creux (par rapport à la surface lointaine) : $H=|z_s(0)|=\dfrac{\Omega^2 a^2}{4g}$. Avec $a=5$ m, $H=5$ m :

$$
\Omega=\sqrt{\frac{4gH}{a^2}}=\sqrt{\frac{4\times9{,}81\times5}{25}}=\boxed{2{,}8\ \mathrm{rad\,s^{-1}}.}
$$

En $r=a$, $v=\Omega a/2$, vitesse angulaire $\omega=v/a=\Omega/2$ ; période $T=\dfrac{2\pi}{\omega}=\dfrac{4\pi}{\Omega}\approx\boxed{4{,}5\ \mathrm s}$. Un tour toutes les $\sim4{,}5$ s : écoulement très rapide, cohérent avec le maëlstrom le plus puissant du monde.

### I.C — Allées de von Kármán

#### Q16

> [!INDICATION]
> Comparer les amplitudes des rayons réfléchis successifs via $r,t$ fournis (air $n=1$, savon $n=1{,}4$).

#### Solution

À chaque dioptre, $|r|=\dfrac{|n_1-n_2|}{n_1+n_2}=\dfrac{0{,}4}{2{,}4}=0{,}17$, donc $R=r^2\approx2{,}8\%$ et $T=1-R\approx0{,}97$. Amplitudes (par rapport à l'incidente) :
- rayon 1 (réfléchi avant) : $|r|\approx0{,}17$ ;
- rayon 2 ($t\,r\,t'$) : $\approx T\,|r|\approx0{,}16$ — **comparable** au rayon 1 ;
- rayon 3 : rayon 2 $\times R\approx0{,}16\times0{,}028\approx4{,}5\times10^{-3}$ — **négligeable**.

Les deux premiers rayons ayant des amplitudes voisines et les suivants étant $100$ fois plus faibles, le modèle à **deux ondes** est justifié.

#### Q17

> [!INDICATION]
> Incidence **normale** (demandée), différence de marche géométrique = double traversée de la lame.

#### Solution

En incidence normale, le rayon 2 parcourt $2e$ de plus dans le milieu d'indice $n$ : la différence de marche **géométrique** est $\delta_{\text{géo}}=2ne$. Déphasage associé :

$$
\boxed{\Delta\varphi_{\text{géo}}=\frac{2\pi}{\lambda_0}\,2ne=\frac{4\pi n e}{\lambda_0}.}
$$

#### Q18

> [!INDICATION]
> Terme de réflexion supplémentaire quand $e\to0$.

#### Solution

Le rayon 1 se réfléchit sur un milieu **plus réfringent** (air→savon) : déphasage supplémentaire de $\pi$ ; le rayon 2 se réfléchit à l'arrière sur un milieu **moins réfringent** (savon→air) : pas de déphasage. Quand $e\to0$, $\Delta\varphi_{\text{géo}}\to0$ mais il reste $\Delta\varphi\to\pi$ : interférences **destructives** en réflexion. La lame ne réfléchit plus : elle paraît **noire** juste avant d'éclater.

> [!JURY]
> « très peu traitée »

#### Q19

> [!INDICATION]
> Cohérence **spatiale** et notion de localisation.

#### Solution

Une source étendue est **spatialement incohérente** : chaque point source produit son propre système de franges, décalé des autres. Ces systèmes se superposent de façon constructive (franges visibles) **uniquement** au lieu où la différence de marche est **stationnaire** vis-à-vis de la position du point source : les franges y sont **localisées**. Pour un dispositif à division d'amplitude, les deux rayons issus d'un même rayon incident interfèrent toujours ; les franges restent donc observables avec une source étendue, mais localisées.

#### Q20

> [!INDICATION]
> Lame à faces parallèles → franges d'égale inclinaison à l'infini.

#### Solution

Pour une lame d'épaisseur **constante**, les franges (d'égale inclinaison) sont localisées **à l'infini**. Schéma : lame éclairée par faisceau convergent/étendu, lentille convergente en aval, observation dans son **plan focal image** (ou œil accommodant à l'infini)..

#### Q21

> [!INDICATION]
> Lame coin, incidence quasi-normale ; déphasage géométrique $2ne(z_A)$ + terme $\pi$.

#### Solution

En incidence quasi-normale, la différence de marche géométrique au point $A$ vaut $2n\,e(z_A)$. Le rayon 1 se réfléchissant sur un milieu plus réfringent ajoute un déphasage $\pi$, soit une marche $\lambda_0/2$ :

$$
\boxed{\Delta\varphi(M)=\frac{2\pi}{\lambda_0}\!\left[2n\,e(z_A)+\frac{\lambda_0}{2}\right].}
$$

Schéma : coin de savon, rayons incident/réfléchis en $A$ et $B$, épaisseur $e(z_A)$ indiquée..

#### Q22

> [!INDICATION]
> Lame d'épaisseur variable → franges d'égale épaisseur (Fizeau) localisées sur la lame.

#### Solution

Les franges (d'égale épaisseur) sont localisées **sur la surface de la lame** (ou son voisinage immédiat). Schéma : lentille imageant la surface du film sur un écran/capteur..

#### Q23

> [!INDICATION]
> Comparer les amplitudes des ondes interférant en transmission vs réflexion → contraste.

#### Solution

Le contraste $V=\dfrac{2a_1a_2}{a_1^2+a_2^2}$ est maximal pour des amplitudes égales. En **réflexion** (Q16), les deux ondes ont des amplitudes voisines ($\approx0{,}17$ et $0{,}16$) : $V\approx1$. En **transmission**, l'onde directe a une amplitude $\approx T\approx0{,}97$ (forte) tandis que l'onde deux fois réfléchie a une amplitude $\approx T\,R\approx0{,}027$ (faible) : amplitudes **très inégales**, donc $V\approx\dfrac{2\times0{,}97\times0{,}027}{0{,}97^2}\approx0{,}06$. Figure de transmission beaucoup moins contrastée.

> [!JURY]
> « intensités »

#### Q24

> [!INDICATION]
> Condition de frange brillante (constructive) : $\Delta\varphi=2p\pi$, $p$ entier.

#### Solution

Frange brillante : $\Delta\varphi=2p\pi$ avec $p\in\mathbb N^*$. Donc $2ne+\dfrac{\lambda_0}{2}=p\lambda_0$, soit $2ne=\Big(p-\tfrac12\Big)\lambda_0$ :

$$
\boxed{e(z)=\frac{2p-1}{4n}\,\lambda_0.}
$$

#### Q25

> [!INDICATION]
> Interpréter le profil $e(z)$ décroissant par le drainage gravitaire ; écarts rouge/bleu par l'incertitude d'attribution d'ordre.

#### Solution

$e$ décroît du bas vers le haut de la lame : cohérent avec le **drainage par gravité**, qui amincit le film en haut et l'épaissit en bas (film en coin). Les épaisseurs tirées du rouge et du bleu devraient coïncider ; les petits écarts proviennent de l'**incertitude sur la position des franges** et sur l'**attribution de l'ordre entier** $p$ (la relation de Q24 dépend de $\lambda_0$ et d'un entier).

#### Q26

> [!INDICATION]
> Variation d'épaisseur entre deux franges consécutives ($\Delta p=1$).

#### Solution

Entre deux franges brillantes voisines, $\Delta p=1$ donne $\Delta e=\dfrac{\lambda_0}{2n}$ : c'est l'ordre de grandeur de la plus petite variation d'épaisseur résolue.

$$
\Delta e_{\text{rouge}}=\frac{600}{2\times1{,}4}\approx214\ \mathrm{nm},\qquad\Delta e_{\text{bleu}}=\frac{440}{2\times1{,}4}\approx157\ \mathrm{nm}.
$$

$\Delta e$ plus petit dans le bleu : la **sensibilité est meilleure en lumière bleue**.

#### Q27

> [!INDICATION]
> Lumière blanche → cohérence temporelle, condition de non-brouillage sur l'ordre.

#### Solution

En lumière blanche, chaque $\lambda$ donne ses franges à des épaisseurs différentes : pour $e$ faible, teintes irisées ; pour $e$ grand, les ordres de toutes les longueurs d'onde se recouvrent et les franges se **brouillent** (cohérence temporelle limitée). Les franges restent visibles tant que l'ordre varie de moins de $1$ sur le spectre visible :

$$
\Delta p=2ne\!\left(\frac{1}{\lambda_{\min}}-\frac{1}{\lambda_{\max}}\right)\lesssim1.
$$

Avec $\lambda_{\min}\approx400$ nm, $\lambda_{\max}\approx800$ nm : $2\times1{,}4\times e\times(1{,}25\times10^{-3}\ \mathrm{nm^{-1}})\lesssim1\Rightarrow e\lesssim\boxed{3\times10^{2}\ \mathrm{nm}}$ (quelques centaines de nm).

#### Q28

> [!INDICATION]
> Interpréter $St=fd/v_t$, pas seulement dimensionner.

#### Solution

Avec $T=1/f$ période d'émission : $St=\dfrac{fd}{v_t}=\dfrac{d}{v_t T}$. Or $v_t T$ est la distance parcourue par un tourbillon pendant une période, c'est-à-dire l'espacement entre tourbillons de même sens. Donc :

$$
\boxed{St=\frac{d}{v_tT}=\frac{\text{taille de l'obstacle}}{\text{espacement des tourbillons}}}
$$

(rapport de deux **longueurs**), ou de façon équivalente $St=\dfrac{d/v_t}{T}$, rapport du **temps d'advection** sur une distance $d$ à la **période d'émission** $T$.

#### Q29

> [!INDICATION]
> $St\approx0{,}2$, $v_t\approx V_\infty/2$ ; estimer $f$ puis $\mathcal R e$.

#### Solution

$f=\dfrac{St\,v_t}{d}=\dfrac{0{,}2\times(V_\infty/2)}{d}$. Avec $V_\infty=2\ \mathrm{cm\,s^{-1}}$, $d=2$ mm, $v_t=1\ \mathrm{cm\,s^{-1}}$ :

$$
f=\frac{0{,}2\times10^{-2}}{2\times10^{-3}}=\boxed{1\ \mathrm{Hz}.}
$$

$$
\mathcal R e=\frac{\mu_{\text{eau}}V_\infty d}{\eta_{\text{eau}}}=\frac{998{,}3\times0{,}02\times2\times10^{-3}}{1{,}003\times10^{-3}}\approx\boxed{40.}
$$

$\mathcal R e\approx40$, proche du seuil critique $\mathcal R e=48$ : on est au voisinage de l'apparition de l'allée de von Kármán, cohérent.

#### Q30

> [!INDICATION]
> Rappel de cours.

#### Solution

$\boxed{\vec B(r)=\dfrac{\mu_0 I}{2\pi r}\,\vec u_\theta}$ (fil infini, courant $I$ selon $+\vec u_z$).

#### Q31

> [!INDICATION]
> Deux tourbillons successifs contrarotatifs → courants de signes alternés entre les deux rangées.

#### Solution

Dans l'analogie $\vec v\leftrightarrow\vec B$, un tourbillon de vorticité $\pm\Omega\vec u_z$ correspond à un courant $\pm I$. Les tourbillons des deux rangées tournant en sens opposés (fig. 9a), les fils de la **rangée supérieure** (1, 3, 5) portent un courant d'un signe et ceux de la **rangée inférieure** (2, 4) le signe opposé. Le signe est choisi pour que l'écoulement induit entre les deux rangées soit dirigé vers l'aval ($+\vec u_x$), conformément aux lignes de courant.

#### Q32

> [!INDICATION]
> Superposition : champ uniforme ($\leftrightarrow V_\infty$) + 4 plus proches fils. Les deux voisins de même rangée se compensent ; les deux de l'autre rangée imposent la vitesse induite.

#### Solution

La vitesse induite par un fil, analogue de $B=\mu_0 I/2\pi r$ avec la correspondance $\mu_0 I\leftrightarrow\pi V_\infty D$, vaut $v_{\text{ind}}=\dfrac{\pi V_\infty D}{2\pi r}=\dfrac{V_\infty D}{2r}$, perpendiculaire à la ligne de jonction.

Pour le $3^{\text e}$ tourbillon (rangée du haut) :
- les deux voisins de **même rangée** (à $\pm a$ selon $x$, même signe) induisent des vitesses **verticales opposées** qui se **compensent** ;
- les deux fils de la **rangée inférieure** (à $(\pm a/2,-b)$, signe opposé, distance $r=\sqrt{a^2/4+b^2}$) induisent des vitesses dont les composantes verticales se compensent et les composantes **horizontales s'ajoutent** : chacune contribue $\dfrac{V_\infty D}{2r}\cdot\dfrac{b}{r}$, soit au total $\dfrac{V_\infty D\,b}{r^2}=\dfrac{V_\infty D\,b}{a^2/4+b^2}$, dirigée vers $-\vec u_x$.

Avec l'advection $V_\infty\vec u_x$ par le champ uniforme :

$$
\boxed{\vec v_3=V_\infty\!\left(1-\frac{Db}{\dfrac{a^2}{4}+b^2}\right)\vec u_x.}
$$

#### Q33

> [!INDICATION]
> Lecture de la figure 8 (échelle 20 km), rapport de stabilité $b/a\approx0{,}28$.

#### Solution

De l'échelle (20 km), on estime l'espacement longitudinal $\boxed{a\approx40\ \mathrm{km}}$ et l'écart entre rangées $\boxed{b\approx12\ \mathrm{km}}$ (cohérent avec le rapport de stabilité $b/a\approx0{,}28$ d'une allée de von Kármán).

#### Q34

> [!INDICATION]
> Employer la définition du nombre de Strouhal donnée avant Q28, en identifiant la vitesse d’advection.

#### Solution

Avec $D=7$ km, $a\simeq40$ km et $b\simeq12$ km,
$$\frac{v_3}{V_\infty}=1-\frac{Db}{a^2/4+b^2}\simeq1-\frac{84}{544}\simeq0,85.$$
Pour $V_\infty=18$ km/h $=5$ m/s, $v_3\simeq4,2$ m/s. L'espacement longitudinal $a$ entre tourbillons de même rangée donne
$$f=\frac{v_3}{a}\simeq1,1\times10^{-4}\ \mathrm{Hz},$$
soit une période proche de $2,6$ heures. La définition du sujet utilise la vitesse d'advection $v_t=v_3$, non $V_\infty$ :
$$\boxed{St=\frac{fD}{v_3}=\frac Da\simeq0,175.}$$
Cette valeur est cohérente avec un nombre de Strouhal de l'ordre de $0,2$, compte tenu des lectures graphiques.

### I.D — Spirales d'Ekman

#### Q35

> [!INDICATION]
> Définition par le principe d'inertie.

#### Solution

Un **référentiel galiléen** est un référentiel dans lequel le **principe d'inertie** est vérifié : tout point matériel isolé (ou pseudo-isolé) y est au repos ou en mouvement rectiligne uniforme. (Les lois de Newton y sont valables.)

#### Q36

> [!INDICATION]
> Repère d'espace + repère de temps ; condition de galiléité.

#### Solution

Le **référentiel géocentrique** a pour origine le centre de masse de la Terre et trois axes pointant vers des **étoiles lointaines** (directions fixes) ; il est muni d'une horloge. Il est **galiléen** si l'on néglige l'accélération de son centre dans son mouvement orbital autour du Soleil, c'est-à-dire pour des durées courtes devant l'année.

#### Q37

> [!INDICATION]
> Idem, lié à la Terre.

#### Solution

Le **référentiel terrestre** est lié à la surface de la Terre (origine en un point de la surface, axes fixes par rapport au sol), muni d'une horloge. Il est **galiléen** si l'on néglige la **rotation propre** de la Terre (effets de Coriolis et d'entraînement), ce qui n'est **pas** le cas pour les courants océaniques étudiés.

#### Q38

> [!INDICATION]
> Rappel des deux accélérations d'inertie pour une rotation uniforme $\vec\omega$ fixe.

#### Solution

Pour un référentiel en rotation uniforme $\vec\omega$ (constant) autour d'un axe fixe, en notant $\vec v_{\text{rel}}$ la vitesse de la particule **dans le référentiel tournant** et $H$ le projeté de $M$ sur l'axe :
- accélération de **Coriolis** (complémentaire) : $\boxed{\vec a_C=2\,\vec\omega\wedge\vec v_{\text{rel}}}$ ;
- accélération **d'entraînement** : $\boxed{\vec a_e=\vec\omega\wedge(\vec\omega\wedge\overrightarrow{OM})=-\omega^2\,\overrightarrow{HM}}$ (centripète).

#### Q39

> [!INDICATION]
> Forces volumiques dans le référentiel terrestre non galiléen ; l'entraînement est dans le poids.

#### Solution

Sur une particule de fluide s'exercent (par unité de volume) : le **poids** $\mu\,\vec g$ (où $\vec g$ **inclut déjà** l'inertie d'entraînement centrifuge), la force de **pression** $-\overrightarrow{\operatorname{grad}}P$, la force de **viscosité** $\eta\Delta\vec v$ et la force d'inertie de **Coriolis** $-2\mu\,\vec\omega\wedge\vec v$.

#### Q40

> [!INDICATION]
> $\vec v=v_x(z)\vec u_x+v_y(z)\vec u_y$ ne dépend que de $z$ et $v_z=0$.

#### Solution

$(\vec v\cdot\overrightarrow{\operatorname{grad}})\vec v=\Big(v_x\dfrac{\partial}{\partial x}+v_y\dfrac{\partial}{\partial y}+v_z\dfrac{\partial}{\partial z}\Big)\vec v$. Or $\vec v$ est indépendant de $x$ et $y$, et $v_z=0$ ; les trois termes sont donc nuls : $\boxed{(\vec v\cdot\overrightarrow{\operatorname{grad}})\vec v=\vec0}$.

#### Q41

> [!INDICATION]
> Navier-Stokes stationnaire avec convectif nul, Coriolis au pôle Nord ($\vec\omega=\omega\vec u_z$, $\omega=2\pi/T_{\text{jour}}$).

#### Solution

Avec $-2\mu\vec\omega\wedge\vec v=-2\mu\omega(v_x\vec u_y-v_y\vec u_x)=2\mu\omega(v_y\vec u_x-v_x\vec u_y)$ et $2\omega=\dfrac{4\pi}{T_{\text{jour}}}$ :

$$
\mu_{\text{eau}}\vec g-\overrightarrow{\operatorname{grad}}P+\frac{4\pi}{T_{\text{jour}}}\mu_{\text{eau}}(v_y\vec u_x-v_x\vec u_y)+\eta_{\text{eau}}\Delta\vec v=\vec0,
$$

soit

$$
\boxed{\overrightarrow{\operatorname{grad}}P=\mu_{\text{eau}}\vec g+\frac{4\pi}{T_{\text{jour}}}\mu_{\text{eau}}(v_y\vec u_x-v_x\vec u_y)+\eta_{\text{eau}}\Delta\vec v.}
$$

#### Q42

> [!INDICATION]
> Pas de gradient horizontal de pression (écoulement purement entraîné) ; composante verticale hydrostatique.

#### Solution

$\vec v$ est horizontale, donc $(\Delta\vec v)_z=0$ ; la projection sur $\vec u_z$ donne $\dfrac{\partial P}{\partial z}=-\mu_{\text{eau}}g$. En l'absence de gradient horizontal de pression (écoulement engendré par le seul vent), $P$ ne dépend que de $z$ :

$$
\boxed{P(z)=P_0-\mu_{\text{eau}}\,g\,z}
$$

($P_0$ pression atmosphérique en surface $z=0$ ; $P$ croît avec la profondeur, $z<0$).

#### Q43

> [!INDICATION]
> Projeter Q41 sur $x$ et $y$ avec $\overrightarrow{\operatorname{grad}}P$ horizontal nul ; $\Delta\vec v=\dfrac{\mathrm d^2\vec v}{\mathrm dz^2}$.

#### Solution

$$
0=\frac{4\pi}{T_{\text{jour}}}\mu_{\text{eau}}v_y+\eta_{\text{eau}}\frac{\mathrm d^2v_x}{\mathrm dz^2},\qquad 0=-\frac{4\pi}{T_{\text{jour}}}\mu_{\text{eau}}v_x+\eta_{\text{eau}}\frac{\mathrm d^2v_y}{\mathrm dz^2}.
$$

En posant $\dfrac{1}{\delta^2}=\dfrac{4\pi\mu_{\text{eau}}}{T_{\text{jour}}\,\eta_{\text{eau}}}$ :

$$
\boxed{\frac{\mathrm d^2v_x}{\mathrm dz^2}+\frac{1}{\delta^2}v_y=0,\qquad\frac{\mathrm d^2v_y}{\mathrm dz^2}-\frac{1}{\delta^2}v_x=0.}
$$

$\boxed{\delta=\sqrt{\dfrac{T_{\text{jour}}\,\eta_{\text{eau}}}{4\pi\mu_{\text{eau}}}}}$. Dimension : $[\delta^2]=[T\,\eta/\mu]=[\text{s}]\cdot[\text{m}^2\,\text{s}^{-1}]=\text{m}^2$, donc $\delta$ est une **longueur**. AN :

$$
\delta=\sqrt{\frac{8{,}62\times10^4\times1{,}003\times10^{-3}}{4\pi\times998{,}3}}\approx\boxed{8{,}3\times10^{-2}\ \mathrm m}.
$$

(Valeur faible car on a pris la viscosité **moléculaire** ; une viscosité turbulente donnerait des dizaines de mètres.)

#### Q44

> [!INDICATION]
> Combiner les deux ODE via $\underline V=v_x+iv_y$.

#### Solution

$\dfrac{\mathrm d^2\underline V}{\mathrm dz^2}=\dfrac{\mathrm d^2v_x}{\mathrm dz^2}+i\dfrac{\mathrm d^2v_y}{\mathrm dz^2}=-\dfrac{1}{\delta^2}v_y+i\dfrac{1}{\delta^2}v_x=\dfrac{i}{\delta^2}(v_x+iv_y)$ :

$$
\boxed{\frac{\mathrm d^2\underline V}{\mathrm dz^2}=\frac{i}{\delta^2}\,\underline V.}
$$

#### Q45

> [!INDICATION]
> Résoudre, garder la solution bornée en $z\to-\infty$, condition de surface $\underline V(0)=v_0$.

#### Solution

Équation caractéristique $k^2=\dfrac{i}{\delta^2}$, $\sqrt i=e^{i\pi/4}=\dfrac{1+i}{\sqrt2}$, donc $k=\pm\dfrac{1+i}{\sqrt2\,\delta}$. Pour un océan infiniment profond ($z\to-\infty$), on ne garde que la racine $\mathrm{Re}(k)>0$ (sinon $\underline V$ diverge) : $\underline V=v_0\,e^{(1+i)z/(\sqrt2\,\delta)}$ (avec $\underline V(0)=v_0$, $\vec v_0=v_0\vec u_x$). En posant $\delta_E=\sqrt2\,\delta$ :

$$
\boxed{v_x(z)=v_0\,e^{z/\delta_E}\cos\!\Big(\frac{z}{\delta_E}\Big),\qquad v_y(z)=v_0\,e^{z/\delta_E}\sin\!\Big(\frac{z}{\delta_E}\Big)}\quad(z\le0).
$$

En surface $\vec v=v_0\vec u_x$ ; en profondeur, la vitesse décroît exponentiellement et **tourne vers la droite** ($v_y<0$ dès $z<0$) : c'est la spirale d'Ekman.

#### Q46

> [!INDICATION]
> Débits massiques intégrés sur toute la profondeur ; intégrer $\underline V$.

#### Solution

Par définition, $D_x=\mu_{\text{eau}}\displaystyle\int_{-\infty}^0 v_x\,\mathrm dz$ et $D_y=\mu_{\text{eau}}\displaystyle\int_{-\infty}^0 v_y\,\mathrm dz$. Or

$$
\int_{-\infty}^0\underline V\,\mathrm dz=\Big[\frac{\underline V}{k}\Big]_{-\infty}^0=\frac{v_0}{k}=\frac{v_0\,\sqrt2\,\delta}{1+i}=\frac{v_0\,\delta}{\sqrt2}(1-i).
$$

D'où $\displaystyle\int v_x\mathrm dz=\frac{v_0\delta}{\sqrt2}$, $\displaystyle\int v_y\mathrm dz=-\frac{v_0\delta}{\sqrt2}$ :

$$
\boxed{D_x=\frac{\mu_{\text{eau}}v_0\delta}{\sqrt2},\qquad D_y=-\frac{\mu_{\text{eau}}v_0\delta}{\sqrt2}.}
$$

Le transport $(D_x,D_y)\propto(1,-1)$ est dirigé à **45° à droite du courant de surface** (lui-même $\sim45°$ à droite du vent) : l'eau est globalement transportée **perpendiculairement, à droite du vent**. Ceci prolonge l'observation de l'introduction (icebergs et navires dérivant à droite de la direction du vent).

## Partie II — Écoulements au sein de la Terre

### II.A — Structure interne

#### Q47

> [!INDICATION]
> Forme **locale** (différentielle) de la statique.

#### Solution

Dans un fluide au repos, le gradient de pression équilibre les forces volumiques de pesanteur :

$$
\boxed{\overrightarrow{\operatorname{grad}}P=\mu\,\vec g.}
$$

#### Q48

> [!INDICATION]
> $\vec g$ radial (symétrie sphérique) → $\overrightarrow{\operatorname{grad}}P$ radial → $P=P(r)$.

#### Solution

$\overrightarrow{\operatorname{grad}}P=\mu\vec g$ avec $\vec g=g(r)\vec u_r$ (symétrie sphérique). Les composantes $\theta$ et $\varphi$ de $\overrightarrow{\operatorname{grad}}P$ sont donc nulles : $P$ ne dépend que de $r$. À une profondeur donnée ($r$ fixé), la pression lithostatique est **la même partout**.

#### Q49

> [!INDICATION]
> Lecture directe de la figure 12.

#### Solution

La courbe $\mu(r)$ dans le manteau varie de $\sim3{,}3\times10^3$ (surface) à $\sim5{,}5\times10^3\ \mathrm{kg\,m^{-3}}$ (base). On retient la valeur moyenne $\boxed{\mu_{\text{manteau}}\approx4{,}5\times10^3\ \mathrm{kg\,m^{-3}}}$.

#### Q50

> [!INDICATION]
> Statique avec $\mu_{\text{manteau}}$ uniforme et $g$ constant ; intégrer de la surface vers la base.

#### Solution

$\dfrac{\mathrm dP}{\mathrm dr}=-\mu_{\text{manteau}}\,g$ (la pression croît quand $r$ décroît). En négligeant $P$ au sommet du manteau ($r=R_T$) :

$$
P(r)=\mu_{\text{manteau}}\,g\,(R_T-r).
$$

À la base, $r=R_M=3490$ km :

$$
P_M=4{,}5\times10^3\times9{,}81\times(6371-3490)\times10^3\approx\boxed{1{,}3\times10^{11}\ \mathrm{Pa}=1{,}3\times10^{2}\ \mathrm{GPa}.}
$$

À comparer à $140$ GPa (fig. 11) : accord en ordre de grandeur, la légère sous-estimation venant de l'approximation de densité uniforme.

#### Q51

> [!INDICATION]
> Énoncer Gauss (flux **sortant**).

#### Solution

Le flux du champ électrostatique $\vec E$ à travers une surface **fermée**, orienté vers l'**extérieur**, est égal à la charge intérieure divisée par $\varepsilon_0$ :

$$
\boxed{\iint_{\mathcal S}\vec E\cdot\vec n_{\text{ext}}\,\mathrm dS=\frac{Q_{\text{int}}}{\varepsilon_0}.}
$$

#### Q52

> [!INDICATION]
> Correspondance Coulomb ↔ gravitation.

#### Solution

Les forces sont formellement analogues : $\vec F_{\text{Coulomb}}=\dfrac{1}{4\pi\varepsilon_0}\dfrac{q_1q_2}{r^2}\vec u$ et $\vec F_{\text{grav}}=-G\dfrac{m_1m_2}{r^2}\vec u$. La correspondance est $q\to m$, $\dfrac{1}{4\pi\varepsilon_0}\to-G$, soit $\dfrac{1}{\varepsilon_0}\to-4\pi G$. Le théorème de Gauss gravitationnel s'écrit donc :

$$
\boxed{\iint_{\mathcal S}\vec g\cdot\vec n_{\text{ext}}\,\mathrm dS=-4\pi G\,M_{\text{int}}.}
$$

> [!JURY]
> « rarement »

#### Q53

> [!INDICATION]
> Symétrie sphérique de la distribution de masses.

#### Solution

La distribution de masse étant à symétrie sphérique, tout plan contenant le centre $O$ et le point $M$ est plan de symétrie : $\vec g$ est **radial** et ne dépend que de $r$, $\vec g=g(r)\vec u_r$.

#### Q54

> [!INDICATION]
> Gauss gravitationnel sur une sphère de rayon $r$, $\mu$ uniforme.

#### Solution

Schéma : sphère de Gauss de rayon $r$ centrée sur $O$.. $\iint\vec g\cdot\vec n_{\text{ext}}\,\mathrm dS=g(r)\,4\pi r^2=-4\pi G\,M_{\text{int}}$, avec $M_{\text{int}}=\mu\dfrac{4}{3}\pi r^3$ :

$$
g(r)\,4\pi r^2=-4\pi G\,\mu\frac{4}{3}\pi r^3\ \Rightarrow\ \boxed{\vec g(r)=-\frac{4\pi G\mu}{3}\,r\,\vec u_r.}
$$

#### Q55

> [!INDICATION]
> Statique dans le noyau liquide avec $g(r)$ de Q54.

#### Solution

$\dfrac{\mathrm dP}{\mathrm dr}=\mu\,g_r=-\dfrac{4\pi G\mu^2}{3}r$. Intégration :

$$
P(r)=-\frac{2\pi G\mu^2}{3}r^2+C.
$$

Condition $P(R_M)=P_M$ : $C=P_M+\dfrac{2\pi G\mu^2}{3}R_M^2$, d'où

$$
\boxed{P(r)=P_M+\frac{2\pi\mu^2 G}{3}\big(R_M^2-r^2\big).}
$$

#### Q56

> [!INDICATION]
> La graine commence où $P$ atteint la pression de solidification du fer à 5000 K.

#### Solution

La graine (fer solide) apparaît en $r=R_G$ où $P(R_G)=P_{\text{sol}}(5000\,\mathrm K)=320$ GPa :

$$
P_{\text{sol}}-P_M=\frac{2\pi\mu^2 G}{3}\big(R_M^2-R_G^2\big).
$$

Coefficient : $\dfrac{2\pi G\mu^2}{3}=\dfrac{2\pi\times6{,}67\times10^{-11}\times(11\times10^3)^2}{3}\approx1{,}69\times10^{-2}\ \mathrm{Pa\,m^{-2}}$. Avec $R_M=3486$ km :

$$
R_M^2-R_G^2=\frac{(320-140)\times10^9}{1{,}69\times10^{-2}}\approx1{,}07\times10^{13}\ \mathrm m^2,
$$

$$
R_G^2=(3{,}486\times10^6)^2-1{,}07\times10^{13}\approx1{,}5\times10^{12}\ \mathrm m^2\ \Rightarrow\ \boxed{R_G\approx1{,}2\times10^{3}\ \mathrm{km}.}
$$

Excellent accord avec la figure 11 ($R_G=1216$ km).

### II.B — Convection thermique du noyau

#### Q57

> [!INDICATION]
> $T\nearrow$ avec la profondeur, $\mu$ décroît avec $T$ (dilatation), pression négligée.

#### Solution

La température augmente vers le centre, donc $T$ **décroît** quand $r$ croît. En négligeant l'effet de la pression, $\mu$ décroît avec $T$ ; donc $\mu$ **croît** avec $r$ : $\boxed{\mu\ \text{fonction croissante de }r}$. Le fluide le plus dense est au-dessus du plus léger : configuration **instable**.

#### Q58

> [!INDICATION]
> Comparer densité de la sphère ($T_0$) et du fluide environnant (plus chaud) → sens de la résultante.

#### Solution

La sphère part du haut à $T_0$, de masse volumique $\mu(T_0)$. En descendant, le fluide environnant est plus chaud ($T>T_0$), donc **moins dense** : $\mu_{\text{sphère}}=\mu(T_0)>\mu_{\text{fluide}}$. La résultante poids + poussée d'Archimède, $(\mu_{\text{sphère}}-\mu_{\text{fluide}})V\vec g$, est dirigée **vers le bas** : la sphère descend jusqu'à la limite inférieure.

#### Q59

> [!INDICATION]
> RFD avec poids, Archimède (constant, fluide à $T_0+\Delta T/2$) et Stokes.

#### Solution

Masse $m=\mu(T_0)V$, $V=\frac{4}{3}\pi a^3$. Avec $\vec v$ compté vers le bas :

$$
m\frac{\mathrm dv}{\mathrm dt}=\big[\mu(T_0)-\mu(T_0+\tfrac{\Delta T}{2})\big]V g-6\pi\eta_0 a\,v,
$$

soit $\boxed{\dfrac{4}{3}\pi a^3\mu(T_0)\dfrac{\mathrm dv}{\mathrm dt}=\big[\mu(T_0)-\mu(T_0+\tfrac{\Delta T}{2})\big]\dfrac{4}{3}\pi a^3 g-6\pi\eta_0 a\,v}$.

#### Q60

> [!INDICATION]
> $\mathrm dv/\mathrm dt=0$ et linéariser $\mu(T_0+\Delta T/2)-\mu(T_0)\approx\frac{\Delta T}{2}\mu'(T_0)$.

#### Solution

$v_{\text{lim}}=\dfrac{[\mu(T_0)-\mu(T_0+\Delta T/2)]Vg}{6\pi\eta_0 a}$. Avec $\mu(T_0)-\mu(T_0+\tfrac{\Delta T}2)\approx-\tfrac{\Delta T}{2}\mu'(T_0)$ et $V=\frac43\pi a^3$ :

$$
\boxed{v_{\text{lim}}=-\frac{\mu'(T_0)\,\Delta T\,g\,a^2}{9\,\eta_0}>0\ \ (\text{car }\mu'<0).}
$$

#### Q61

> [!INDICATION]
> Temps caractéristique de l'équation linéaire du premier ordre.

#### Solution

$\tau=\dfrac{m}{6\pi\eta_0 a}=\dfrac{\mu(T_0)\frac43\pi a^3}{6\pi\eta_0 a}=\boxed{\dfrac{2\,\mu(T_0)\,a^2}{9\,\eta_0}}$.

#### Q62

> [!INDICATION]
> $\Delta t_1=h/v_{\text{lim}}$ ; comportement en bas.

#### Solution

$\boxed{\Delta t_1=\dfrac{h}{v_{\text{lim}}}=-\dfrac{9\,\eta_0\,h}{\mu'(T_0)\,\Delta T\,g\,a^2}>0}$. En atteignant le bas, la sphère (toujours à $T_0$) est plus dense que le fluide environnant (à $T_0+\Delta T$) : elle **s'y arrête et s'accumule** au fond.

#### Q63

> [!INDICATION]
> Symétrie montante.

#### Solution

Une sphère partie du bas à $T_0+\Delta T$ (chaude, peu dense) est **moins** dense que le fluide au-dessus (plus froid) : la résultante poids + Archimède est dirigée **vers le haut**. Elle **monte** à la vitesse limite jusqu'à la face supérieure.

#### Q64

> [!INDICATION]
> Égalité des températures → flottabilité neutre.

#### Solution

Quand $T_{\text{sphère}}=T_{\text{fluide}}$, les masses volumiques sont égales : la résultante poids + Archimède s'annule, il n'y a plus de force motrice. La sphère cesse d'être accélérée et, freinée par Stokes, **s'immobilise** (flottabilité neutre).

#### Q65

> [!INDICATION]
> Bilan d'énergie 1D + loi de Fourier, généralisé à 3D.

#### Solution

Loi de Fourier $\vec\jmath_Q=-\lambda\,\overrightarrow{\operatorname{grad}}T$. Bilan d'énergie interne sur un volume fixe, sans source interne : la variation d'énergie interne égale l'opposé du flux de chaleur divergent,

$$
\mu c\,\frac{\partial T}{\partial t}=-\operatorname{div}\vec\jmath_Q=\lambda\,\Delta T,
$$

soit

$$
\boxed{\frac{\partial T}{\partial t}=\frac{\lambda}{\mu c}\,\Delta T=D_{\text{th}}\,\Delta T.}
$$

(Démonstration 1D : $\mu c\,\partial_t T\,\mathrm d\tau=[\jmath_Q(x)-\jmath_Q(x+\mathrm dx)]\,S=-\partial_x\jmath_Q\,\mathrm d\tau$, généralisée à 3D.)

#### Q66

> [!INDICATION]
> Analyse dimensionnelle avec $D_{\text{th}}$ et la taille $a$.

#### Solution

$[D_{\text{th}}]=\mathrm{m^2\,s^{-1}}$ : le temps de thermalisation sur la taille $a$ est

$$
\boxed{\Delta t_2\sim\frac{a^2}{D_{\text{th}}}=\frac{a^2\mu c}{\lambda}.}
$$

#### Q67

> [!INDICATION]
> Identifier d’abord le signe de l’anomalie de densité de la sphère froide.

#### Solution

La sphère initialement froide doit conserver son **excès de masse volumique** pendant la descente ; sa thermalisation doit donc être plus lente que le transport : $\Delta t_1<\Delta t_2$. En utilisant les expressions Q62 et Q66,
$$-\frac{9\eta_0h}{\mu'(T_0)\Delta Tga^2}<\frac{a^2}{D_{\mathrm{th}}}.$$
Comme $\mu'(T_0)<0$, les deux temps sont positifs et cette condition équivaut à
$$\boxed{\Pi=\frac{-\mu'(T_0)\Delta Tga^4}{\eta_0D_{\mathrm{th}}h}>9.}$$
Le numérateur et le dénominateur ont la même dimension : $\Pi$ est sans dimension.

#### Q68

> [!INDICATION]
> Cycle descente–thermalisation–montée–thermalisation.

#### Solution

Si $\Pi>9$, le cycle s'auto-entretient : la sphère descend en $\Delta t_1$, se réchauffe au fond en $\Delta t_2$ (devient flottante), remonte en $\Delta t_1$, se refroidit en haut en $\Delta t_2$, et recommence. Le mouvement est **périodique**, de période en ordre de grandeur

$$
\boxed{T_{\text{cycle}}\sim2(\Delta t_1+\Delta t_2).}
$$

#### Q69

> [!INDICATION]
> Comparer $\Pi$ au nombre de Rayleigh ; discuter forme et seuil.

#### Solution

Le critère exact est $\mathcal R a=\dfrac{-g\,\mu'(T_0)\,\Delta T}{\eta_0\,D_{\text{th}}}h^3\ge\dfrac{27}{4}\pi^4\approx658$. Notre nombre $\Pi=\dfrac{-g\mu'(T_0)\Delta T\,a^4}{\eta_0 D_{\text{th}}h}$ : en prenant une bulle de taille comparable à l'épaisseur de la couche ($a\sim h$), $\Pi\to\dfrac{-g\mu'(T_0)\Delta T\,h^3}{\eta_0 D_{\text{th}}}=\mathcal R a$. Le modèle simple retrouve donc **exactement le bon paramètre de contrôle** (le nombre de Rayleigh) et prédit l'**existence d'un seuil**, mais le seuil obtenu ($\Pi\sim9$) est $\sim70$ fois trop faible : l'analyse complète tient compte de la géométrie de l'écoulement, des conditions aux limites et de la déstabilisation collective de toute la couche, que notre « sphère isolée » ignore. Compatibilité **qualitative** (même nombre sans dimension, même nature de seuil), désaccord **quantitatif** sur la valeur critique.

---

## Bilan

- **Partie I.A (Q1–Q5)** : équation de continuité
$$
\partial_t\mu+\operatorname{div}(\mu\vec v)=0
$$
, champ à flux conservatif et
$$
\operatorname{div}\vec v=0
$$
(incompressible), dérivée particulaire, équation d'Euler-Navier-Stokes, nombre de Reynolds
$$
\mathcal Re=\mu V L/\eta
$$
(maëlstrom :
$$
\mathcal Re\approx1{,}1\times10^{8}
$$
, viscosité négligeable).
- **Partie I.B (Q6–Q15)** : analogie hydromagnétique
$$
\vec v\leftrightarrow\vec B
$$
,
$$
\vec\Omega\leftrightarrow\mu_0\vec\jmath
$$
; maëlstrom :
$$
v=\Omega r/2
$$
(
$$
r\le a
$$
),
$$
v=\Omega a^2/(2r)
$$
(
$$
r>a
$$
) ; Bernoulli irrotationnel (
$$
r>a
$$
) :
$$
P=P_0-\mu gz-\mu\Omega^2a^4/(8r^2)
$$
; rotationnel (
$$
r\le a
$$
) :
$$
P=P_0-\mu gz+\mu\Omega^2(r^2/8-a^2/4)
$$
; surface libre
$$
P=P_0
$$
, creux
$$
H=\Omega^2a^2/(4g)
$$
,
$$
\Omega\approx2{,}8\ \mathrm{rad\,s^{-1}}
$$
, période
$$
\approx4{,}5\ \mathrm s
$$
.
- **Partie I.C (Q16–Q34)** : interférences à deux ondes en lame de savon (
$$
|r|\approx0{,}17
$$
, deux premiers rayons réfléchis) ; déphasage
$$
4\pi n e/\lambda_0
$$
+
$$
\pi
$$
(réflexion sur milieu plus réfringent) ; franges d'égale épaisseur localisées sur la lame ;
$$
\Delta e=\lambda_0/(2n)
$$
entre franges ; cohérence spatiale vs temporelle ; nombre de Strouhal
$$
St=d/(v_tT)\approx0{,}2
$$
; allée de von Kármán modélisée par des fils de courant (superposition) :
$$
a\approx40
$$
km,
$$
b\approx12
$$
km,
$$
v_3/V_\infty\approx0{,}85
$$
,
$$
f\approx1\times10^{-4}\ \mathrm{Hz}
$$
,
$$
St\approx0{,}175
$$
.
- **Partie I.D (Q35–Q46)** : référentiels galiléen/géocentrique/terrestre ; accélérations de Coriolis
$$
2\vec\omega\wedge\vec v_{\text{rel}}
$$
et d'entraînement ; spirale d'Ekman :
$$
v_x+iv_y=v_0 e^{(1+i)z/(\sqrt2\,\delta)}
$$
, échelle
$$
\delta\approx8{,}3\times10^{-2}\ \mathrm m
$$
(viscosité moléculaire), transport à 45° à droite du vent (débits
$$
D_x=-D_y=\mu v_0\delta/\sqrt2
$$
).
- **Partie II (Q47–Q69)** : statique
$$
\overrightarrow{\operatorname{grad}}P=\mu\vec g
$$
; pression à la base du manteau
$$
P_M\approx1{,}3\times10^{11}\ \mathrm{Pa}
$$
; Gauss gravitationnel
$$
\iint\vec g\cdot\vec n_{\text{ext}}\,\mathrm dS=-4\pi G M_{\text{int}}
$$
,
$$
\vec g=-(4\pi G\mu/3)\,r\,\vec u_r
$$
; pression dans le noyau
$$
P(r)=P_M+\frac{2\pi\mu^2G}{3}(R_M^2-r^2)
$$
, rayon de la graine
$$
R_G\approx1{,}2\times10^{3}\ \mathrm{km}
$$
; convection : vitesse limite
$$
v_{\text{lim}}=-\mu'(T_0)\Delta T\,g\,a^2/(9\eta_0)
$$
, temps
$$
\tau=2\mu a^2/(9\eta_0)
$$
, diffusion
$$
\Delta t_2\sim a^2/D_{\text{th}}
$$
, critère
$$
\Pi>9
$$
, mouvement périodique, lien avec le nombre de Rayleigh
$$
\mathcal Ra\ge27\pi^4/4\approx658
$$
.
- **Transversal** : deux chiffres significatifs pour les nombres sans dimension qualitatifs ; flèches et schémas exigés pour les démonstrations de cours ; distinguer cohérence spatiale et temporelle, force et force volumique ; ne pas appliquer une même constante de Bernoulli à des lignes de courant différentes dans un écoulement rotationnel ; dans les conditions usuelles, Bernoulli reste applicable le long d’une ligne de courant.
