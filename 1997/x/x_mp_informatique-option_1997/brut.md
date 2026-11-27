# École polytechnique MP — Informatique (option) 1997 · Corrigé brut

*Corrigé rédigé par IA, non officiel. Signalez toute erreur.*

**Rédaction** · GPT-6.2 Astra Ultra · vitesse non renseignée

**Révision** · GPT-6.2 Astra Ultra · vitesse non renseignée · 26 novembre 2026

**Simulation gravitationnelle et arbres quaternaires.** La partie commune étudie la profondeur des subdivisions. Les parties II et III proposent les deux variantes de programmation du sujet, en Caml et en Pascal. Les coordonnées sont celles du carré initial, centré en l’origine. Les masses des corps sont positives.

## I. Profondeur d’un arbre quaternaire adaptatif

### Question 1.a

La profondeur 3 permet au plus $4^3=64$ corps. On l’atteint avec une grille de $8\times8$ cellules dont chacune contient un corps. Pour le minimum, deux corps suffisent. Dans le carré unité, placer les points $(1/16,1/16)$ et $(3/16,1/16)$. Ils restent ensemble lors des deux premiers partages et se séparent lors du troisième. Avec zéro ou un corps, l’arbre est une feuille de profondeur 0.

![Figure 1 — Dans les deux univers le dernier partage atteint le niveau 3. À droite, seule la cellule contenant les deux points est subdivisée.](figures/profondeur-trois.svg)

### Question 1.b

Une grille uniforme de profondeur $p$ possède $4^p$ cases. Chaque feuille occupée d’un arbre de profondeur au plus $p$ contient au moins une de ces cases, et des feuilles distinctes ont des cases distinctes. Donc $N\le4^p$ et, pour $N\ge1$,
$$p\ge f(N)=\lceil\log_4 N\rceil.$$
Pour chaque $p_0$, remplir les $4^{p_0}$ cases à raison d’un corps par case donne une profondeur exactement $p_0$. Même pour un $N$ imposé, placer les corps dans $N$ cases distinctes de la grille de niveau $\lceil\log_4N\rceil$ réalise la borne, puisque aucune cellule de ce niveau ne peut être subdivisée. Pour $N=0$ la profondeur vaut 0.

### Question 1.c

Pour tout entier $h\ge1$, dans le carré unité, considérons
$$(x_1,y_1)=(2^{-h-1},2^{-h-1}),\qquad (x_2,y_2)=(3\cdot2^{-h-1},2^{-h-1}).$$
Ils sont dans le même carré inférieur gauche jusqu’au niveau $h-1$, puis dans deux cases distinctes au niveau $h$. La profondeur $h$ est arbitraire pour $N=2$. Une borne supérieure qui ne dépendrait que de $N$ est donc impossible.

### Question 1.d

Tous les points d’un carré de côté $D$ sont à distance au plus $D$ pour la norme $\|u\|_\infty=\max(|u_x|,|u_y|)$. Si l’arbre a profondeur $p\ge1$, le parent d’une feuille la plus profonde contient au moins deux corps. Son côté est $D_U2^{-(p-1)}$. La définition du minimum $\delta$ donne $\delta\le D_U2^{-(p-1)}$. Ainsi
$$p\le 1+\left\lfloor\log_2(D_U/\delta)\right\rfloor.$$
L’emploi de l’inégalité large convient aussi aux points situés sur des bords. Pour zéro ou un corps, la profondeur est déjà connue.

### Question 1.e

Dans le modèle de l’énoncé, le pas vaut $2^e$. Deux coordonnées différentes sont séparées d’au moins ce pas. Deux positions distinctes diffèrent sur au moins une coordonnée, d’où $\delta\ge2^e$. Le côté $D_U$, lui aussi homogène à une distance, vaut au plus $(2^m-1)2^e$. Donc $D_U/\delta\le2^m-1<2^m$. La réponse de 1.d donne **$p\le m$**. Ce résultat utilise l’échelle commune imposée aux nombres du problème.

## II. Construction de l’arbre

### Question 2.a

Pour la branche Caml, on emploie la syntaxe d’OCaml. Les types ci-dessous reprennent les champs du sujet.

```ocaml
type vecteur = { x : float; y : float }
type corps = {
  mass : float; mutable pos : vecteur;
  mutable vel : vecteur; mutable acc : vecteur
}
let vecteur_nul = { x = 0.; y = 0. }
let add u v = { x = u.x +. v.x; y = u.y +. v.y }
let sub u v = { x = u.x -. v.x; y = u.y -. v.y }
```

On obtient bien $u+v$ et $u-v$ composante par composante.

#### Pascal · Types et résultats par référence

Dans le programme d’exemple, la constante de taille vaut huit. Elle peut être remplacée par la taille voulue à la compilation. L’alias `type_nature` distingue le nom du type de celui du champ discriminant pour le compilateur. Le type nommé `indice_corps` désigne l’intervalle `1..N` du sujet. Les deux entrées des opérations vectorielles sont passées par valeur et le résultat par référence. Le premier argument peut ainsi désigner la même variable que la sortie.

```pascal
const N = 8;
type
  vecteur = record x, y: real end;
  corps = record
    mass: real;
    pos, vel, acc: vecteur
  end;
  indice_corps = 1..N;
  type_nature = (Feuille, Noeud);
  arbre = ^cellule;
  cellule = record
    case nature: type_nature of
      Feuille: (corps: indice_corps);
      Noeud: (cm_mass: real; cm_pos: vecteur;
              filles: array[0..3] of arbre)
  end;
  nature = type_nature;
var
  univers: array[indice_corps] of corps;
  arbre_univers: arbre;
  vecteur_nul: vecteur;
  taille_univers, theta: real;

procedure add(u, v: vecteur; var r: vecteur);
begin
  r.x := u.x + v.x;
  r.y := u.y + v.y
end;

procedure sub(u, v: vecteur; var r: vecteur);
begin
  r.x := u.x - v.x;
  r.y := u.y - v.y
end;
```

### Question 2.b

La multiplication scalaire envoie $(x,y)$ sur $(mx,my)$.

```ocaml
let scal m u = { x = m *. u.x; y = m *. u.y }
```

#### Pascal · Produit par un scalaire

Le résultat est écrit dans les deux champs du dernier argument.

```pascal
procedure scal(m: real; u: vecteur; var r: vecteur);
begin
  r.x := m * u.x;
  r.y := m * u.y
end;
```

### Question 2.c

Le carré de la norme vaut $u_x^2+u_y^2$.

```ocaml
let carre u = u.x *. u.x +. u.y *. u.y
```

#### Pascal · Norme au carré

La multiplication évite de calculer une racine pour obtenir le carré de la norme.

```pascal
function carre(u: vecteur): real;
begin
  carre := u.x * u.x + u.y * u.y
end;
```

### Question 3.a

Numérotons les quadrants sud-ouest, sud-est, nord-ouest, nord-est par $0,1,2,3$. La médiane verticale est attribuée à l’est et l’horizontale au nord. Cette convention est utilisée par tous les appels.

```ocaml
type arbre = Noeud of cellule | Feuille of corps | Vide
and cellule = {
  mutable cm_mass : float; mutable cm_pos : vecteur;
  filles : arbre array
}

let indice_fille centre p =
  let est = if p.x >= centre.x then 1 else 0 in
  let nord = if p.y >= centre.y then 2 else 0 in
  est + nord
```

#### Pascal · Numérotation des quatre filles

Les quatre cases du tableau sont respectivement sud-ouest, sud-est, nord-ouest et nord-est. Une position sur une médiane est attribuée à l’est ou au nord.

```pascal
function indice_fille(p_c, p: vecteur): integer;
var i: integer;
begin
  i := 0;
  if p.x >= p_c.x then i := i + 1;
  if p.y >= p_c.y then i := i + 2;
  indice_fille := i
end;
```

### Question 3.b

La composante horizontale du déplacement du centre vaut $+D/4$ pour un indice impair et $-D/4$ pour un indice pair. La composante verticale vaut $+D/4$ pour les indices 2, 3 et $-D/4$ pour 0, 1.

```ocaml
let position_fille centre taille i =
  let quart = taille /. 4. in
  { x = centre.x +. (if i mod 2 = 1 then quart else -.quart);
    y = centre.y +. (if i >= 2 then quart else -.quart) }
```

#### Pascal · Centre d’une fille

Le bit horizontal donne le signe du déplacement en abscisse, le bit vertical son signe en ordonnée. Le déplacement vaut le quart du côté du parent.

```pascal
function position_fille(p: vecteur; taille: real; i: integer): vecteur;
var q: vecteur;
begin
  if odd(i) then q.x := p.x + taille / 4
            else q.x := p.x - taille / 4;
  if i >= 2 then q.y := p.y + taille / 4
            else q.y := p.y - taille / 4;
  position_fille := q
end;
```

### Question 4.a

Dans le cas d’une collision de feuille, plaçons d’abord l’ancien corps dans sa fille, puis insérons le nouveau. Un seul appel récursif par niveau reste ainsi à traiter.

```ocaml
let rec insere_corps c a centre taille =
  let descendre filles =
    let i = indice_fille centre c.pos in
    let q = position_fille centre taille i in
    filles.(i) <-
      insere_corps c filles.(i) q (taille /. 2.)
  in
  match a with
  | Vide -> Feuille c
  | Noeud cell ->
      descendre cell.filles;
      a
  | Feuille ancien ->
      let filles = Array.make 4 Vide in
      filles.(indice_fille centre ancien.pos) <- Feuille ancien;
      descendre filles;
      Noeud { cm_mass = 0.; cm_pos = vecteur_nul; filles }

let construire_arbre univers taille_univers =
  Array.fold_left
    (fun a c -> insere_corps c a vecteur_nul taille_univers)
    Vide univers
```

Le tableau et le côté, globaux dans la boucle imprimée, sont ici passés à cette boucle en arguments. Une ancienne feuille est subdivisée exactement lorsqu’elle contient dorénavant deux corps. Le cas `Noeud` conserve les trois sœurs et tous les corps précédents. Les champs de barycentre seront remplis en 5.

#### Pascal · Insertion par modification du pointeur

Les constructeurs ci-dessous implémentent les primitives indiquées dans le sujet. La feuille contient l’indice d’un corps dans `univers`. Un pointeur nul représente une cellule vide. Quand une feuille doit être partagée, on la conserve et on la rattache sous le nouveau nœud avant de descendre avec le nouvel indice. Cette réutilisation conserve le corps et évite de perdre la feuille allouée.

```pascal
function cree_feuille(c: indice_corps): arbre;
var f: arbre;
begin
  new(f);
  f^.nature := Feuille;
  f^.corps := c;
  cree_feuille := f
end;

function cree_noeud(m: real; pos: vecteur;
                     f0, f1, f2, f3: arbre): arbre;
var a: arbre;
begin
  new(a);
  a^.nature := Noeud;
  a^.cm_mass := m;
  a^.cm_pos := pos;
  a^.filles[0] := f0; a^.filles[1] := f1;
  a^.filles[2] := f2; a^.filles[3] := f3;
  cree_noeud := a
end;

procedure insere_corps(c: indice_corps; var a: arbre;
                       p: vecteur; taille: real);
var ancien: arbre; i: integer; q: vecteur;
begin
  if a = nil then
    a := cree_feuille(c)
  else begin
    if a^.nature = Feuille then begin
      ancien := a;
      i := indice_fille(p, univers[ancien^.corps].pos);
      a := cree_noeud(0, vecteur_nul, nil, nil, nil, nil);
      a^.filles[i] := ancien
    end;
    i := indice_fille(p, univers[c].pos);
    q := position_fille(p, taille, i);
    insere_corps(c, a^.filles[i], q, taille / 2)
  end
end;

procedure construire_arbre;
var i: indice_corps;
begin
  vecteur_nul.x := 0; vecteur_nul.y := 0;
  arbre_univers := nil;
  for i := 1 to N do
    insere_corps(i, arbre_univers, vecteur_nul, taille_univers)
end;
```

![Figure 2 — Insertion Pascal de deux corps dans des quadrants distincts. Une ancienne feuille est rattachée au nouveau nœud et les filles vides valent nil.](figures/insertion-pascal.svg)

### Question 4.b

Le carré initial contient toutes les positions. Au cours d’une insertion, les seuls appels récursifs suivent les quadrants de la nouvelle position. Chaque appel divise le côté par deux. Si l’arbre était vide au départ, l’insertion est immédiate. Sinon, la distance $\delta_c$ pour la norme du maximum entre le nouveau corps et le plus proche des anciens est strictement positive, car les positions sont distinctes et en nombre fini. Après un nombre fini de divisions, le côté devient inférieur à $\delta_c$. La cellule ne peut alors contenir aucun ancien corps et l’appel termine dans le cas vide. Le même argument justifie la séparation éventuelle des deux corps d’une ancienne feuille.

**Variante Pascal.** En Pascal, recycler l’ancienne feuille conserve un seul appel récursif vers la fille du nouveau corps. À chaque appel, le côté de la cellule est divisé par deux. Le même argument de séparation établit la terminaison.

### Question 4.c

Pour une profondeur finale $p$, chaque insertion visite au plus $p+1$ niveaux. Les opérations locales, y compris la création d’un tableau de quatre filles, coûtent $O(1)$. La construction coûte donc $O(N(1+p))$. Sous 1.e, $p\le m$ avec $m$ fixé, d’où $O(N)$. La boucle traite chacun des $N$ corps, ce qui donne aussi la minoration $\Omega(N)$ et finalement **$\Theta(N)$**.

**Variante Pascal.** La boucle Pascal traite les indices de 1 à N. Le changement de pointeur et le rattachement de l’ancienne feuille prennent un temps constant par niveau. La même borne s’applique.

## III. Barycentres et calcul approché des forces

### Question 5

Associons à une cellule le couple $(M,Q)$ avec $M=\sum m_j$ et $Q=\sum m_jp_j$. La somme de ces couples sur ses quatre filles donne celui de la mère. Pour une cellule interne, non vide et de masse positive, son centre de masse est $Q/M$. On mémorise la masse et le centre après la visite des filles.

```ocaml
let barycentres a =
  let rec bilan = function
    | Vide -> (0., vecteur_nul)
    | Feuille c -> (c.mass, scal c.mass c.pos)
    | Noeud cell ->
        let ajouter (m, q) fille =
          let mi, qi = bilan fille in
          (m +. mi, add q qi)
        in
        let m, q =
          Array.fold_left ajouter (0., vecteur_nul) cell.filles
        in
        cell.cm_mass <- m;
        cell.cm_pos <- scal (1. /. m) q;
        (m, q)
  in
  ignore (bilan a)
```

Pour une feuille, le couple renvoyé est bien celui de son seul corps ou de l’ensemble vide. L’additivité établit la correction de l’appel interne par récurrence sur la hauteur. Chaque cellule est visitée une fois.

#### Pascal · Bilan ascendant des masses

Un appel local renvoie par référence la masse et le moment de sa cellule. Le pointeur nul contribue zéro. Une feuille lit la masse et la position dans le tableau des corps. Seuls les nœuds internes reçoivent une masse et une position en mémoire. Leurs masses sont positives.

```pascal
procedure barycentres(a: arbre);
  procedure bilan(s: arbre; var masse: real; var moment: vecteur);
  var i: integer; m: real; q: vecteur;
  begin
    masse := 0;
    moment := vecteur_nul;
    if s <> nil then
      case s^.nature of
        Feuille: begin
          masse := univers[s^.corps].mass;
          scal(masse, univers[s^.corps].pos, moment)
        end;
        Noeud: begin
          for i := 0 to 3 do begin
            bilan(s^.filles[i], m, q);
            masse := masse + m;
            add(moment, q, moment)
          end;
          s^.cm_mass := masse;
          scal(1 / masse, moment, s^.cm_pos)
        end
      end
  end;
var masse: real; moment: vecteur;
begin
  bilan(a, masse, moment)
end;
```

### Question 6.a

Pour une source de masse $M$ et de position $q$, posons $d=q-p$. Sa contribution vaut $M d/(\|d\|^2\sqrt{\|d\|^2})$. La feuille du corps cible contribue zéro. Pour éviter d’inclure sa propre masse dans une approximation, on ouvre également toute cellule qui le contient. Avec $0<\theta\le1/\sqrt2$, cette dernière précaution découle déjà du critère imprimé, car $r\le\sqrt2D$ dans cette cellule. Elle permet de garder la somme sur les **autres** corps pour tout seuil positif. Le test équivalent $D<\theta r$ évite une division par $r$ à distance nulle.

```ocaml
let contribution d r2 m =
  scal (m /. (r2 *. sqrt r2)) d

let grav_approx pos arbre taille =
  let rec visite a centre cote contient =
    match a with
    | Vide -> vecteur_nul
    | Feuille c ->
        let d = sub c.pos pos in
        let r2 = carre d in
        if r2 = 0. then vecteur_nul
        else contribution d r2 c.mass
    | Noeud cell ->
        let d = sub cell.cm_pos pos in
        let r2 = carre d in
        if not contient && cote < theta *. sqrt r2 then
          contribution d r2 cell.cm_mass
        else
          let i = indice_fille centre pos in
          let somme = ref vecteur_nul in
          for j = 0 to 3 do
            let q = position_fille centre cote j in
            let v = visite cell.filles.(j) q (cote /. 2.)
                           (contient && i = j) in
            somme := add !somme v
          done;
          !somme
  in
  visite arbre vecteur_nul taille true
```

Comme dans l’appel imprimé, `arbre` désigne ici l’univers centré en l’origine, après calcul de ses barycentres, et `theta` désigne le seuil global. L’indicateur de présence suit exactement une fille sur le chemin du corps cible. Les cellules acceptées et les feuilles traitées couvrent une seule fois les masses sources. L’appel sur chaque fille utilise la moitié du côté. L’égalité au seuil entraîne une subdivision.

#### Pascal · Parcours gravitationnel

Le premier appel porte sur la racine centrée en l’origine et la position d’un corps du tableau. Le booléen local signale l’unique chemin qui contient ce corps. Cette précaution garde l’auto-interaction nulle pour tout seuil positif. La division par la distance n’intervient qu’après le test strict, ou sur une autre feuille de position distincte.

```pascal
function grav_approx(p: vecteur; a: arbre; taille: real): vecteur;
  function visite(s: arbre; centre: vecteur; cote: real;
                  contient: boolean): vecteur;
  var
    d, q, terme, somme: vecteur;
    masse, r2: real;
    i, j: integer;
  begin
    somme := vecteur_nul;
    if s <> nil then begin
      if s^.nature = Feuille then begin
        masse := univers[s^.corps].mass;
        sub(univers[s^.corps].pos, p, d);
        r2 := carre(d);
        if r2 > 0 then scal(masse / (r2 * sqrt(r2)), d, somme)
      end else begin
        sub(s^.cm_pos, p, d);
        r2 := carre(d);
        if (not contient) and (cote < theta * sqrt(r2)) then
          scal(s^.cm_mass / (r2 * sqrt(r2)), d, somme)
        else begin
          i := indice_fille(centre, p);
          for j := 0 to 3 do begin
            q := position_fille(centre, cote, j);
            terme := visite(s^.filles[j], q, cote / 2,
                            contient and (i = j));
            add(somme, terme, somme)
          end
        end
      end
    end;
    visite := somme
  end;
begin
  grav_approx := visite(a, vecteur_nul, taille, true)
end;

procedure ajuste_acc_approx;
var i: indice_corps;
begin
  for i := 1 to N do
    univers[i].acc :=
      grav_approx(univers[i].pos, arbre_univers, taille_univers)
end;
```

### Question 6.b

Fixons la cible $c$ et une taille $D$. Si le test géométrique exige l’ouverture, $r=\|G-c\|\le D/\theta$, où $G$ est le barycentre. Les masses étant positives, $G$ appartient au carré. Tout point du carré se trouve à distance au plus $\sqrt2D$ de $G$, donc à distance au plus $(1/\theta+\sqrt2)D$ de $c$. Si $k$ carrés de cette taille satisfont la condition, leurs intérieurs sont disjoints et
$$ k D^2\le \pi(1/\theta+\sqrt2)^2D^2.$$
On peut ainsi prendre $K_0(\theta)=\lfloor\pi(1/\theta+\sqrt2)^2\rfloor$ pour le seul critère imprimé. Pour le programme de 6.a, on peut prendre $K(\theta)=K_0(\theta)+1$, car il y a au plus **une** cellule supplémentaire de cette taille sur le chemin de la cible. Ce majorant est indépendant de la répartition des corps et de $N$.

![Figure 3 — Le barycentre G d’une cellule ouverte par le critère est dans le disque en pointillés. Le carré entier tient dans le grand disque.](figures/cellules-ouvertes-a-un-niveau.svg)

**Variante Pascal.** Dans le parcours Pascal, la seule ouverture éventuelle s’ajoutant au test de distance est celle de la cellule portant le marqueur de présence. Il y en a au plus une par profondeur.

### Question 6.c

À un niveau donné, au plus $K(\theta)$ cellules sont ouvertes. Au niveau suivant, au plus $4K(\theta)$ cellules sont donc visitées. Avec la racine, le nombre d’appels est au plus $1+4pK(\theta)$. Un appel effectue un nombre borné d’opérations locales. Sous les hypothèses demandées, $p\le m$ et $\theta>0$ sont fixés. Pour une cible, `grav_approx` coûte donc **$O(1)$ en $N$**. Pour mettre à jour les $N$ accélérations, `ajuste_acc_approx` coûte **$\Theta(N)$**, chaque corps étant visité au moins une fois. La dépendance en $p$ et en $\theta$ explique la portée précise de cette estimation.

**Variante Pascal.** Les quatre filles Pascal comprennent les pointeurs nuls, dont le traitement coûte un temps constant. Les bornes par niveau et pour la boucle de mise à jour restent valables.

## Vérification des programmes

Les blocs publiés ont été extraits séparément des éditions brute et guidée. Les quatre vérifications de cette épreuve ont utilisé Free Pascal 3.2.2 ou OCaml 5.3.0. Pour chaque édition et chaque langage, cinq configurations de huit corps ont été soumises à six seuils. Les 240 accélérations obtenues ont été comparées au parcours indépendant d’une partition construite directement à partir des positions. Au seuil nul du test, la comparaison porte aussi sur la somme exacte des contributions des autres corps. Les essais Pascal vérifient les quatre quadrants, les indices conservés, les profondeurs et les barycentres des cellules internes.
