# ENS de Cachan · Épreuve à option — dominante gestion 2016 — corrigé guidé

*Corrigé rédigé par IA, non officiel. Signalez toute erreur.*

**Rédaction** · GPT-6.2 Astra Ultra · vitesse non renseignée · 26 novembre 2026

## Étude de cas

Le sujet distingue les comptes du club OML et ceux de son futur centre de Guérande. Les calculs des deux premiers dossiers sont en euros, ceux du troisième en milliers d’euros (k€). Les montants de l’annexe 5 sont convertis avant d’utiliser les tableaux arrondis des annexes 3 et 4.

### Dossier 1 : dresser deux chronologies

Pour le logiciel, tracez une ligne de quatre ans et, au-dessous, une ligne fiscale de douze mois commençant le premier jour du mois d’acquisition. À chaque inventaire, calculez séparément dotation économique et dérogatoire. Pour le brevet, écrivez trois colonnes : valeur sans dépréciation, valeur effectivement comptabilisée, valeur d’usage. Le plafond de reprise se lit dans la première colonne.

### Dossier 2 : passer d’un calendrier à un bilan

Un salaire mensuel coûte 140 000, dont 80 000 sortent le mois même et 60 000 le mois suivant. Les 100 000 du sponsor d’octobre arrivent en novembre. Marquez d’une couleur les engagements, d’une autre les paiements. Vous verrez apparaître au 31 décembre un droit à encaisser du sponsor et une dette sociale. Le découvert est une dette et les intérêts de décembre seront payés en janvier.

![Figure 1 — En 2016, aux tarifs de référence, la contribution annuelle d’un interne couvre une fraction des frais fixes. La capacité physique du centre fixe la borne supérieure.](figures/rentabilite-centre.svg)

### Dossier 3 : vérifier les unités puis boucler les flux

Une dette fournisseur passant de 78 014 à 36 014 k€ consomme 42 000 k€ de trésorerie, toutes choses égales. L’emprunt de l’annexe 5 n’apporte que 3 005,418 k€. Faites ce rapprochement avant d’interpréter la chute de trésorerie. Pour le choix de joueur, soustrayez A de B avant d’actualiser : comparer directement les taux de rentabilité des deux projets ne donnerait pas le seuil d’indifférence demandé.

## Résolution des dossiers

### Dossier 1 — Comptabilité

**1. Coût historique.** Un actif acheté entre à son coût d’acquisition, y compris les coûts directement nécessaires à sa mise en état d’utilisation, hors TVA récupérable. Un actif produit entre à son coût de production. La valeur nette ultérieure tient compte des amortissements et des pertes de valeur. La facture rend l’entrée vérifiable ; l’écart avec une valeur actuelle complique cependant la comparaison entre actifs de dates différentes et laisse certaines plus-values latentes hors du résultat.

**2. Définitions.** Un actif est une ressource identifiable que l’entité contrôle à la suite d’événements passés et dont elle attend des avantages économiques futurs. Une utilisation limitée dans le temps le rend amortissable. Une immobilisation incorporelle est un actif non monétaire sans substance physique, identifiable notamment parce qu’il est séparable ou résulte d’un droit contractuel ou légal. Le club peut par exemple acquérir des droits contractuels relatifs à un joueur ; la personne du joueur ne constitue pas la ressource comptable.

**3. Reconnaissance et mesure.** L’avantage doit être probable, le coût mesurable de façon fiable, et le club doit contrôler les droits acquis. Un brevet ou un logiciel acquis séparément est évalué au prix d’achat augmenté des dépenses directement attribuables. Pour une création interne, les frais de recherche passent en charges. Les dépenses de développement individualisables peuvent être immobilisées à compter de la satisfaction des critères de faisabilité technique, intention et capacité d’achèvement et d’utilisation ou de vente, ressources disponibles, avantages futurs et mesure fiable du coût. La notoriété ou un fichier clientèle générés en interne ne prennent pas pour coût la somme des dépenses de publicité. L’amortissement suit la durée d’utilisation, complété si nécessaire par une dépréciation.

**4. Logiciel.** Hypothèses : mise en service le 16 octobre, TVA normale de 20 %, linéaire en mois commerciaux. La dotation économique est 2 000 par an. Le dispositif fiscal applicable au millésime étale 8 000 sur douze mois dès le 1er octobre : 2 000 en N−2 et 6 000 en N−1. L’écart est porté en amortissement dérogatoire.

| Date | Débit | Crédit |
|---|---|---|
| 16/10/N−2, acquisition | 205 logiciel 8 000 ; 44562 TVA 1 600 | 404 fournisseur 9 600 |
| 31/12/N−2 | 68111 dotation 416,67 ; 68725 dérogatoire 1 583,33 | 2805 amortissement 416,67 ; 145 dérogatoire 1 583,33 |
| 31/12/N−1 | 68111 dotation 2 000 ; 68725 dérogatoire 4 000 | 2805 pour 2 000 ; 145 pour 4 000 |
| 01/04/N, amortir jusqu’à la vente | 68111 dotation 500 | 2805 amortissement 500 |
| Cession HT 5 600 | 462 créance 6 720 | 775 cession 5 600 ; 44571 TVA 1 120 |
| Sortie | 2805 amortissement 2 916,67 ; 675 VNC 5 083,33 | 205 logiciel 8 000 |
| Reprise du dérogatoire restant | 145 dérogatoire 5 583,33 | 78725 reprise 5 583,33 |

**5. Comparaison après comptabilisation.** IAS 38 permet le modèle du coût ou la réévaluation à la juste valeur déterminée par référence à un marché actif, rare pour une marque ou un droit très spécifique. Les réévaluations portent sur toute la catégorie lorsque le marché actif existe et sont renouvelées assez souvent pour maintenir une valeur significative. Une hausse alimente normalement l’écart de réévaluation dans les autres éléments du résultat global, sauf annulation d’une baisse antérieure passée en résultat. Une baisse frappe le résultat au-delà de l’écart disponible. Une hausse de valeur augmente actif et capitaux propres, puis les amortissements futurs si la durée est finie ; elle n’apporte pas d’argent. En comptes sociaux français au moment du cas, la réévaluation libre porte sur l’ensemble des immobilisations corporelles et financières, avec écart en capitaux propres. Ce dispositif ne permet pas de réévaluer isolément le brevet ou le logiciel.

**6. Brevet.** La prudence impose de reconnaître une perte de valeur quand la valeur actuelle devient inférieure à la valeur nette. Sans valeur vénale renseignée, on utilise ici la valeur d’usage. Acquisition le 16/11/N−3 : D 205 brevet 40 000, D 44562 TVA 8 000, C 404 fournisseur 48 000. Le plan initial est de 10 000 par an. À chaque arrêté, D 68111 / C 2805 du montant indiqué.

| Exercice | Dotation | VNC avant test | Test et écriture | VNC finale |
|---|---:|---:|---|---:|
| N−3, 1,5 mois | 1 250 | 38 750 | Aucun indice fourni | 38 750 |
| N−2 | 10 000 | 28 750 | Aucun indice fourni | 28 750 |
| N−1 | 10 000 | 18 750 | Usage 13 800 : D 6816 / C 2905, 4 950 | 13 800 |
| N | 7 360 | 6 440 | Usage 9 000 : D 2905 / C 7816, 2 310 | 8 750 |

À fin N−1, il reste 22,5 mois ; la dotation sur la nouvelle base vaut $13\,800\times12/22{,}5=7\,360$. Le plafond après reprise est la VNC théorique sans dépréciation, $18\,750-10\,000=8\,750$. Reprendre jusqu’à 9 000 dépasserait ce plafond.

### Dossier 2 — Centre de formation

**1. Budget de trésorerie, octobre à décembre 2015.** Il retrace les dates d’entrée et de sortie d’argent, permet de négocier un financement avant une échéance et de vérifier le plafond de découvert. On néglige la TVA comme demandé. Les avances sont supposées de 250 000 chacune. Le sponsor paie le mois suivant la présence ; familles et fédération rapportent ensemble $60(1\,000+200)=72\,000$ par mois. Taxes et commissions portent sur les recettes d’activité encaissées.

| Euros | Octobre | Novembre | Décembre |
|---|---:|---:|---:|
| Solde initial | 0 | −28 600 | −40 038,33 |
| Capital, puis avances | 200 000 | 250 000 | 250 000 |
| Subvention, sponsors, familles et fédération | 132 000 | 172 000 | 172 000 |
| Salaires nets | 80 000 | 80 000 | 80 000 |
| Cotisations de M−1 | 0 | 60 000 | 60 000 |
| Loyers, entretien, véhicules et honoraires | 103 300 | 103 300 | 103 300 |
| Commission de M−1 | 0 | 6 600 | 8 600 |
| Taxes de M | 19 800 | 25 800 | 25 800 |
| Investissement, un quart de 630 000 | 157 500 | 157 500 | 157 500 |
| Agios de M−1 | 0 | 238,33 | 333,65 |
| Total décaissé | 360 600 | 433 438,33 | 435 533,65 |
| **Solde final** | **−28 600** | **−40 038,33** | **−53 571,98** |

Les quatre charges regroupées valent $15\,000+0{,}02(140\,000)+60(1\,300)+7\,500=103\,300$. Les agios de décembre, $53\,571{,}98\times10\%/12=446{,}43$, sont dus en janvier.

**2. Résultat du trimestre.** Produits : subvention 60 000, sponsors acquis 300 000, familles 180 000, fédération 36 000, total **576 000**. Charges : personnel 420 000, loyers 45 000, entretien 8 400, véhicules et assurances 234 000, honoraires 22 500, commissions $5\%\times476\,000=23\,800$, taxes 71 400, amortissements $360\,000/10/4+30\,000/5/4=10\,500$. Le terrain n’est pas amorti. S’y ajoutent les intérêts de la première avance pendant décembre, $250\,000\times3{,}6\%/12=750$, et les agios de 1 018,41. Charges **837 368,41** ; perte **261 368,41**.

**3. Bilan et appréciation.**

| Actif au 31 décembre | Euros | Passif au 31 décembre | Euros |
|---|---:|---|---:|
| Terrain | 240 000 | Capital | 200 000 |
| Aménagements nets | 351 000 | Résultat | −261 368,41 |
| Agencements nets | 28 500 | Avances de la société mère | 500 000 |
| Sponsors à recevoir | 100 000 | Intérêts sur avances et agios dus | 1 196,43 |
| | | Dette d’investissement | 157 500 |
| | | Cotisations et commission de décembre | 68 600 |
| | | Découvert | 53 571,98 |
| **Total** | **719 500** | **Total** | **719 500** |

Le compte courant procure des liquidités selon un calendrier souple, sans modifier les parts de capital, et rémunère la mère. En contrepartie, 500 000 seront remboursables dès mai 2016. Le découvert reste inférieur aux 300 000 autorisés mais les capitaux propres sont déjà négatifs de 61 368,41. Il faut projeter les échéances de janvier et de mai avant de conclure sur la solvabilité.

**4. Coût annuel.** Pour retrouver l’équation imposée, la subvention « déterminée en fonction du nombre de joueurs » est ramenée au tarif annuel de référence $240\,000/60=4\,000$ par joueur. On reconduit le tarif unitaire, et on exclut les charges de financement du calcul d’exploitation. Pour un interne, revenus $35\,000+12\,000+2\,400+4\,000=53\,400$, coût variable $12\times1\,300+20\%\times53\,400=26\,280$. Les charges fixes valent personnel 1 680 000, loyer 180 000, entretien 33 600, honoraires 90 000, amortissements 42 000, soit **2 025 600**. Au tarif sponsor de référence, $C=26\,280J+2\,025\,600$. Une subvention forfaitaire constamment égale à 240 000, quel que soit l’effectif, ne donnerait pas l’équation indiquée.

**5. Équation du résultat.** Pour un parrainage unitaire annuel $s$, les recettes sont $(18\,400+s)J$. Après taxes et commissions, $R=[0{,}8(18\,400+s)-15\,600]J-2\,025\,600=(0{,}8s-880)J-2\,025\,600$. Avec $S=sJ$ pour le total des sponsors, $R=0{,}8S-880J-2\,025\,600$. À 60 joueurs et 35 000 par joueur, **−398 400**.

**6. Seuil.** Chaque joueur apporte $53\,400-26\,280=27\,120$. Le seuil est $2\,025\,600/27\,120=74{,}69$, soit **75 joueurs**. Il faut 15 internes de plus, et la capacité est de 85. À 75, l’excédent est seulement 8 400. Une chute des financements par joueur ferait remonter le seuil.

**7. Sponsors pour 70 joueurs.** De $R=0$, on tire $S=(2\,025\,600+880\times70)/0{,}8=2\,609\,000$, soit **37 271,43 par joueur**, 2 271,43 de plus que la prévision.

**8. Ajustement pour 60 internes.** Il faut combler 398 400. H1 : trois mutations à 150 000 nets procurent 450 000 ; cinq procurent 750 000. Le recrutement n’est pas signé et ne constitue pas un revenu récurrent. H2 : la contribution par usager est $900(1-0{,}10)=810$, d’où **492 usagers**. Ce chiffre suppose les 10 % annoncés comme coût variable total de ces locations ; si les 20 % de taxes et commissions sont aussi dus en sus, la contribution tombe à 630 et il faut 633 usagers. Vérifier les créneaux de terrain et la demande. H3 : un externe apporte $25\,000(1-0{,}20)-2\,000=18\,000$, soit **23 externes**. Ce calcul suppose des places d’enseignement disponibles même si les externes n’occupent aucun lit. Une combinaison des trois recettes peut réduire la dépendance envers les transferts.

### Dossier 3 — Diagnostic du club et choix d’investissement

**1. Soldes intermédiaires, en k€.** Marge commerciale $0-14=-14$ ; production de services 358 022 ; valeur ajoutée $358\,022-14-1\,200-50\,003=306\,805$ ; EBE $306\,805-20\,000-180\,002-50\,001=56\,802$. Après 60 017 d’amortissements, résultat d’exploitation **−3 215**. Résultat financier $66-2\,854=-2\,788$, soit −6 003 par les lignes arrondies ; l’état imprime **−6 004** de résultat courant. Résultat exceptionnel $10\,640-8\,720=1\,920$, dont 570 de plus-value de cession. Le poste IS est créditeur (−1 811 en charges), d’où le résultat net imprimé $-6\,004+1\,920+1\,811=-2\,273$.

**2. Bilan fonctionnel, en k€.** Les immobilisations sont prises en brut et leurs amortissements en ressources stables. Annexe 5 : concours 2,012 et intérêts courus 35,266. Emprunts stables $4\,507+40-2{,}012-35{,}266=4\,509{,}722$. Ressources stables $2\,386+108\,555+4\,509{,}722=115\,450{,}722$. **FRNG = −35 983,278** face aux 151 434 d’emplois stables. Le bilan ne chiffre pas la part d’IS dans les dettes fiscales ; on les classe dans l’exploitation en l’absence de ventilation. **BFRE** $=1+150\,001+12-36\,014-73\,000=41\,000$. **BFRHE** $=-96\,760-35{,}266=-96\,795{,}266$ ; **BFR = −55 795,266**. La trésorerie nette est donc **19 811,988**, égale à $19\,814-2{,}012$. Si $x$ de dettes fiscales correspondait à de l’IS, le BFRE augmenterait de $x$, le BFRHE diminuerait d’autant.

Les ressources stables couvrent 76,2 % de l’actif immobilisé brut. Les fonds propres représentent $2\,386/212\,707=1{,}12\%$ du bilan net. Le BFRE absorbe environ 42 jours de CA sur 365. Le crédit des fournisseurs d’immobilisations finance le besoin d’exploitation et une partie des actifs longs ; son renouvellement constitue un enjeu.

**3. Intérêt des flux.** Le tableau explique la variation de liquidités par les activités courantes, les investissements et les financements. Il montre notamment si un apport d’actionnaires masque une consommation de trésorerie d’exploitation. Les dotations ne sont pas des règlements, tandis que le recouvrement des créances et le paiement d’anciennes dettes le sont.

**4. Reconstitution du tableau OEC, en k€.** En méthode indirecte, partir du résultat et neutraliser les dotations et la plus-value de cession. La charge fiscale rattachable à la cession est assumée payée et classée en investissement, soit $570/3=190$. Les intérêts sont classés en activité. Vérification du besoin d’exploitation N−1 : $2+162\,001+12-78\,014-106\,553=-22\,552$ ; sa hausse atteint 63 552. Les intérêts courus diminuent de 0,008.

| Poste | Flux N en k€ |
|---|---:|
| Résultat net + dotations − plus-value | −2 273 + 60 017 − 570 = 57 174 |
| Neutralisation de l’IS sur cession | +190 |
| Hausse du BFRE et baisse des intérêts à payer | −63 552 − 0,008 |
| **Flux d’activité** | **−6 188,008** |
| Acquisitions, ajustées des dettes sur immobilisations | −6 348,250 + (96 760 − 96 560) |
| Cessions et IS correspondant | +3 140 − 190 |
| **Flux d’investissement** | **−3 198,250** |
| Capital, emprunts nouveaux, remboursement | +3 143 + 3 005,418 − 0,940 |
| **Flux de financement** | **+6 147,478** |
| **Variation calculée** | **−3 238,780** |
| Trésorerie initiale, puis finale observée | 23 050,973 ; 19 811,988 |
| **Variation observée** | **−3 238,985** |

L’écart entre les variations est 0,205 k€, soit 205 €, compatible avec les arrondis imposés aux comptes de bilan et de résultat. Laisser l’IS de cession en activité donnerait −6 378,008 pour l’activité et −3 008,250 pour l’investissement, avec le même total.

**5. Diagnostic.** Une trésorerie finale positive et un apport en numéraire apportent un répit, mais la diminution des dettes fournisseurs et fiscales absorbe plus que les encaissements provenant des clients en diminution. Les investissements et l’activité consomment du numéraire. Sans nouveaux financements, la baisse aurait été sensiblement supérieure. M. Dupont doit suivre les échéances des 96 760 k€ dus sur immobilisations, les recettes sur joueurs et les salaires récurrents avant d’accélérer le programme.

**6. CAF.** La capacité d’autofinancement est la ressource potentielle générée par le résultat après exclusion des charges et produits calculés et des opérations de cession d’actifs. Ici $-2\,273+60\,017+2\,570-3\,140=57\,174$ k€. Le passage de cette ressource à la trésorerie exige de retrancher les décalages de règlement puis de tenir compte des investissements et financements. La CAF positive est compatible avec un flux d’activité négatif.

**7. Choix des joueurs.** Pour les projets exclusifs, la VAN de B moins celle de A vaut $-5\,000+2\,400/(1+r)+3\,200/(1+r)^2$ en k€. Posons $x=1+r>0$ ; l’indifférence vérifie $5\,000x^2-2\,400x-3\,200=0$, soit $x=1{,}0752245$. **Au-delà de 7,52 %, A a la VAN la plus élevée** ; au seuil les VAN sont égales, au-dessous B l’emporte. Une VAN plus élevée peut rester négative : si renoncer est admis, comparer aussi le meilleur projet à zéro.

## Sources

Banque ENS Cachan–ENSAI D2, fascicule C1693, cas OML Football. Le PDF institutionnel contient cinq annexes et s’achève sur les informations complémentaires. Le tableau de flux demandé est reconstitué ci-dessous avec les postes de l’OEC.

[Sujet de la dominante, p. 3](https://ens-paris-saclay.fr/sites/default/files/CONCOURS/ANNALES_1C/1C_D2_1/2016_Sujet_1A_D2-1_Options.pdf#page=3) · [Annales institutionnelles](https://ens-paris-saclay.fr/admission/concours/concours-pre-master/annales-concours-pre-master?field_orientation_1c_target_id%5B%5D=289&field_year_target_id%5B%5D=281)
