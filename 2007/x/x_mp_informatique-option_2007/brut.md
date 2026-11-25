# X · MP · Informatique (option) 2007 — corrigé brut

*Corrigé rédigé par IA, non officiel. Signalez toute erreur.*

**Rédaction** · GPT-6.2 Astra Ultra · vitesse non renseignée · 25 novembre 2026

Langage choisi : OCaml. Le premier p et l’inversion inv sont les données globales du sujet. Une liste donne les coefficients dans l’ordre des degrés croissants. Les complexités comptent les opérations dans le corps fini.

## I. Encodage direct

### Question 1 · Horner

Une tête $a$ et une queue $T$ représentent $a+XT$. Appliquer cette identité en $x$, en réduisant à chaque étage.

```ocaml
type poly = int list
let plus a b = (a + b) mod p
let moins a b = (a - b + p) mod p
let fois a b = (a * b) mod p
let rec valeur u x = match u with
  | [] -> 0
  | a :: t -> plus a (fois x (valeur t x))
```

Le choix $p<2^{15}$ borne les produits de deux représentants.

### Question 2 · Message codé

Évaluer le même message à chaque point en conservant l’ordre de la liste.

```ocaml
let codage alpha a = List.map (valeur a) alpha
```

### Question 3 · Coûts

Il y a exactement $k$ additions et $k$ multiplications dans notre évaluation, puis $n$ évaluations. Les bornes sont $O(k)$ et $O(nk)$.

## II. Opérations usuelles

### Question 4 · Somme

Additionner les coefficients de même indice et partager la queue de l’opérande le plus long. Coût $O(\min(\ell_U,\ell_V))$ dans le corps.

```ocaml
let rec addition u v = match u, v with
  | [], w | w, [] -> w
  | a :: s, b :: t -> plus a b :: addition s t
```

### Question 5 · Différence

Lorsque $U$ s’épuise, opposer toute la queue de $V$. Coût $O(\ell_V)$ dans le corps, en particulier $O(\max(\ell_U,\ell_V))$.

```ocaml
let rec soustraction u v = match u, v with
  | w, [] -> w
  | [], w -> List.map (moins 0) w
  | a :: s, b :: t -> moins a b :: soustraction s t
```

### Question 6 · Multiplication par un scalaire

Multiplier indépendamment chaque coefficient. Il y a $\ell_U$ multiplications.

```ocaml
let produitParScalaire u s = List.map (fois s) u
```

### Question 7 · Produit ordinaire

Développer $(a+XT)V=aV+X(TV)$. Chaque étape effectue $O(\ell_V)$ opérations, soit $O(\ell_U\ell_V)$.

```ocaml
let rec produit u v = match u, v with
  | [], _ | _, [] -> []
  | [a], _ -> produitParScalaire v a
  | a :: t, _ -> addition (produitParScalaire v a) (0 :: produit t v)
```

### Question 8 · Quotient par élimination

Éliminer les colonnes en partant du degré maximal. Le coefficient $q_i$ est le coefficient courant de degré $i+d_V$ multiplié par l’inverse du coefficient dominant de $V$. Retrancher alors $q_iX^iV$.

```ocaml
let divreste u v =
  let a = Array.of_list u and b = Array.of_list v in
  let n = Array.length a and m = Array.length b in
  if m = 0 || b.(m - 1) = 0 then invalid_arg "diviseur non canonique";
  let q = Array.make (max 0 (n - m + 1)) 0 in
  let inverse = inv b.(m - 1) in
  for i = Array.length q - 1 downto 0 do
    let t = fois a.(i + m - 1) inverse in
    q.(i) <- t;
    for j = 0 to m - 1 do
      a.(i+j) <- moins a.(i+j) (fois t b.(j))
    done
  done;
  (Array.to_list q, Array.to_list (Array.sub a 0 (min n (m-1))))
let division u v = fst (divreste u v)
```

L’identité entre dividende, quotient partiel fois diviseur et tampon courant est conservée à chaque soustraction. Les colonnes éliminées restent nulles. Le coût dans le corps est $O(1+\ell_V\max(0,\ell_U-\ell_V+1))$, en plus des parcours linéaires de conversion.

### Question 9 · Reste

Le tampon final de la question 8 contient le reste dans ses $d_V$ premières cases au plus. Sa partie haute est nulle. Même coût que pour la division.

```ocaml
let modulo u v = snd (divreste u v)
```

## III. Multiplication et division rapides

### Question 10 · Trois produits

Poser $W_b=U_bV_b$, $W_h=U_hV_h$ et $W_m=(U_b+U_h)(V_b+V_h)-W_b-W_h$. Alors $UV=W_b+X^eW_m+X^{2e}W_h$.

### Question 11 · Karatsuba

Compléter les deux listes avec des zéros de poids fort jusqu’à une même longueur puissance de deux. L’appel interne travaille sur des opérandes de même longueur exacte. Les décalages se font côté constant et les trois blocs sont additionnés sur leurs zones de recouvrement.

```ocaml
let rec ajuste n u =
  if n = 0 then [] else match u with
  | [] -> 0 :: ajuste (n-1) []
  | x :: t -> x :: ajuste (n-1) t
let rec coupe k u =
  if k = 0 then ([], u) else match u with
  | [] -> invalid_arg "coupure"
  | x :: t -> let a,b = coupe (k-1) t in (x :: a, b)
let decale k u = List.init k (fun _ -> 0) @ u
let produitRapide u v =
  let nu = List.length u and nv = List.length v in
  let rec taille n = if n >= max nu nv then n else taille (2*n) in
  let rec mult n u v =
    if n = 1 then [fois (List.hd u) (List.hd v)] else
    let e = n/2 in
    let ub,uh = coupe e u and vb,vh = coupe e v in
    let a = mult e ub vb and b = mult e uh vh in
    let s = mult e (addition ub uh) (addition vb vh) in
    let m = soustraction (soustraction s a) b in
    addition a (addition (decale e m) (decale (2*e) b))
  in
  if nu = 0 || nv = 0 then [] else
  let n = taille 1 in ajuste (nu+nv-1) (mult n (ajuste n u) (ajuste n v))
```

Avec $a=\log_2 3$, la récurrence $M(n)=3M(n/2)+O(n)$ donne $O(n^a)$, par somme des $3^j$ tâches de taille $n/2^j$. Le remplissage initial coûte au plus un facteur deux sur la taille maximale.

### Question 12 · Division récursive

Écrire $d=\ell-1$, $e=\lfloor\ell/2\rfloor$, $t=d-e$. La division du haut porte sur $2t+1$ et $t+1$ coefficients. Après obtention de $Q_h$, calculer $R_h=U_h-Q_hV_h$ par multiplication rapide et garder ses $t$ coefficients possibles.

```ocaml
let rec divisionRapide u v =
  let l = List.length v in
  if l = 1 then [fois (List.hd u) (inv (List.hd v))] else
  let e = l/2 in
  let t = l-1-e in
  let ub,uh = coupe (2*e) u and vb,vh = coupe e v in
  let qh = divisionRapide uh vh in
  let rh = ajuste t (soustraction uh (produitRapide qh vh)) in
  let terme = decale (e-1) [List.nth ub (2*e-1)] in
  let s = soustraction (addition (decale e rh) terme) (produitRapide qh vb) in
  let qb = divisionRapide (ajuste (2*t+1) s) vh in
  ajuste e qb @ qh
```

La formule de $S$ utilise le coefficient $u_{2e-1}$ du bas. Les autres termes du haut de $U_b/X^e$ ont degré au plus $e-2<t$ et ne changent pas son quotient par $V_h$. Les $e$ coefficients de $Q_b$ précèdent ceux de $Q_h$. Pour $\ell$ puissance de deux, $D(\ell)=2D(\ell/2)+O(\ell^a)=O(\ell^a)$ puisque $2/2^a=2/3$. Pour une taille quelconque, les sous-appels ont taille $\lceil\ell/2\rceil$, ce qui donne la même borne par majoration par la puissance de deux suivante.

### Question 13 · Reste rapide

Former $R=U-QV$ avec le quotient rapide et le produit rapide, puis garder au plus $d$ coefficients. Compléter le dividende à $2d+1$ si nécessaire.

```ocaml
let moduloRapide u v =
  let d = List.length v - 1 in
  if List.length u <= d then u else
  let u = ajuste (2*d+1) u in
  let q = divisionRapide u v in
  ajuste d (soustraction u (produitRapide q v))
```

Le coût est $O((d+1)^a)$. Les diviseurs ont un coefficient dominant non nul et les listes du dividende ne contiennent aucune composante non nulle au-delà de la borne annoncée.

## IV. Évaluation multipoints

### Question 14 · Arbre de sous-produits

Fractionner chaque bloc en $\lceil s/2\rceil$ et $\lfloor s/2\rfloor$ points. Les produits se calculent en remontant. Un tableau des points rend constant l’accès à la feuille.

```ocaml
type arbre = Vide | Noeud of poly * arbre * arbre
let etiquette = function Noeud (m,_,_) -> m | Vide -> invalid_arg "vide"
let arbreAvec multiplier alpha =
  let a = Array.of_list alpha in
  let rec batir i s =
    if s = 0 then Vide
    else if s = 1 then Noeud ([moins 0 a.(i); 1], Vide, Vide)
    else
      let k = (s+1)/2 in
      let g = batir i k and d = batir (i+k) (s-k) in
      Noeud (multiplier (etiquette g) (etiquette d), g, d)
  in batir 0 (Array.length a)
let arbreSousProduits = arbreAvec produitRapide
```

Pour $n=2^h$ et un produit de coût $O(s^b)$, le niveau de blocs de taille $s$ coûte $O((n/s)s^b)$. La somme sur les puissances de deux est $O(n^b)$ dès que $b>1$. D’où $O(n^2)$ avec le produit ordinaire et $O(n^a)$ avec Karatsuba.

### Question 15 · Restes descendants

Le diviseur de chaque fils divise celui du parent. Réduire le reste du parent donne donc le reste de $A$ au fils. À la racine le degré de $A$ est strictement inférieur à $k\le n$, son reste y est déjà $A$.

```ocaml
let restesAvec reduire t a =
  let rec descend t u = match t with
    | Vide -> Vide
    | Noeud (m,g,d) ->
        let r = reduire u m in Noeud (r, descend g r, descend d r)
  in descend t a
let arbreRestes = restesAvec moduloRapide
```

![Figure 1 — Évaluation de 1 + X² en quatre points de F₇. Chaque enfant reçoit le reste de son parent modulo son propre produit.](figures/evaluation-des-restes.svg)

Dans la figure, $(X-2)(X-3)=X^2-5X+6$. La réduction de $1+X^2$ donne donc $2+5X$ modulo 7. À chaque niveau, la somme des coûts suit la même série géométrique qu’en question 14. Les tailles diffèrent d’au plus un à profondeur fixée. Les bornes sont $O(n^a)$ avec la partie III et $O(n^2)$ avec le reste ordinaire.

### Question 16 · Lire le codage

Collecter les constantes des feuilles dans l’ordre initial. Une liste vide représente le reste nul. La traversée coûte $O(n)$ et le codage complet $O(n^a)$ avec les deux opérations rapides, $O(n^2)$ avec les ordinaires.

```ocaml
let codageArbre alpha a =
  let rec lire t acc = match t with
    | Vide -> acc
    | Noeud (r,Vide,Vide) -> (match r with [] -> 0 | x :: _ -> x) :: acc
    | Noeud (_,g,d) -> lire g (lire d acc)
  in lire (arbreRestes (arbreSousProduits alpha) a) []
```

[Sujet](https://www.wikiprepa.fr/concours/data/x_option-info_mp_2007.pdf) · [Rapport](https://www.doc-solus.fr/prepa/sci/adc/pdf/rapports.pdf/2007/MP_INFO_X_1_2007.rapport.pdf) · [Autre exemplaire](https://www.doc-solus.fr/prepa/sci/adc/pdf/enonces.pdf/2007/MP_INFO_X_1_2007.enonce.pdf)
