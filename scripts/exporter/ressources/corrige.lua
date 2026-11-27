-- Filtre pandoc des corrigés publiés : Markdown KaTeX → LaTeX.
--
-- * alertes `> [!INDICATION|METHODE|PIEGE|JURY]` → encadrés tcolorbox titrés,
--   indications numérotées par question (remise à zéro à chaque titre `###` ou
--   au-dessus dans le Markdown) ;
-- * titres remontés d'un niveau (`##` → \section) par ce filtre, pas par
--   `--shift-heading-level-by` : selon la version de pandoc, ce décalage s'applique avant
--   ou après les filtres, et le compteur d'indications ne se remettait plus à zéro ;
-- * figures `figures/<slug>/<nom>.svg` → PDF vectoriel (converti en amont par
--   rsvg-convert), centrées, largeur ≤ \linewidth, légende = texte alt ;
-- * équations hors texte → \equationajustee{…} (réduite si elle déborde) ;
-- * rien n'est replié : le PDF s'imprime.

local TYPES = {
  INDICATION = "indication",
  METHODE = "methode",
  ["MÉTHODE"] = "methode",
  PIEGE = "piege",
  ["PIÈGE"] = "piege",
  JURY = "jury",
  NOTE = "encadrenote",
  REMARQUE = "encadrenote",
}

local indication = 0

local function latex(inlines)
  local doc = pandoc.Pandoc({ pandoc.Plain(inlines) })
  local texte = pandoc.write(doc, "latex")
  return (texte:gsub("%s+$", ""))
end

local function chemin_pdf(src)
  if src:match("^figures/.+%.svg$") then
    return (src:gsub("%.svg$", ".pdf"))
  end
  return src
end

-- Figure seule dans son paragraphe. `dans_encadre` : pas de flottant possible.
local function figure_latex(image, legende, dans_encadre)
  local src = chemin_pdf(image.src)
  local leg = latex(legende)
  local corps = "\\centering\n\\includegraphics{" .. src .. "}\n"
  if dans_encadre then
    local s = "\\par\\smallskip\n\\begin{minipage}{\\linewidth}\n" .. corps
    if leg ~= "" then
      s = s .. "\\captionof*{figure}{" .. leg .. "}\n"
    end
    return pandoc.RawBlock("latex", s .. "\\end{minipage}\\par\\smallskip")
  end
  local s = "\\begin{figure}[H]\n" .. corps
  if leg ~= "" then
    s = s .. "\\caption*{" .. leg .. "}\n"
  end
  return pandoc.RawBlock("latex", s .. "\\end{figure}")
end

local function image_de_figure(fig)
  if #fig.content ~= 1 then return nil end
  local bloc = fig.content[1]
  if (bloc.t == "Plain" or bloc.t == "Para") and #bloc.content == 1 and bloc.content[1].t == "Image" then
    return bloc.content[1]
  end
  return nil
end

local function traiter_figure(fig, dans_encadre)
  local img = image_de_figure(fig)
  if not img then return nil end
  return figure_latex(img, img.caption, dans_encadre)
end

local function Image(img)
  img.src = chemin_pdf(img.src)
  return img
end

-- Code en ligne : \texttt (listings refuse l'Unicode dans \lstinline : « → », « … »).
-- Un long code sans espace (SMILES, chemin) peut se couper après la ponctuation.
local function Code(c)
  local brut = pandoc.write(pandoc.Pandoc({ pandoc.Plain({ pandoc.Code(c.text) }) }), "latex")
  brut = brut:gsub("%s+$", "")
  if #c.text > 16 then
    brut = brut:gsub("([=,;:/%(%)])", "%1\\allowbreak{}")
    brut = brut:gsub("({%]})", "%1\\allowbreak{}")
  end
  return pandoc.RawInline("latex", brut)
end

-- Long mot sans espace coupé de tirets (chaîne carbonée « CH₃–CO–CH(OTBS)–CH₂–… ») :
-- coupure permise après chaque tiret.
local TIRETS = { [0x2D] = true, [0x2013] = true, [0x2014] = true }

local function Str(el)
  local n = utf8.len(el.text)
  if n == nil or n < 24 then return nil end
  local res, courant, coupe = pandoc.List(), {}, false
  for _, code in utf8.codes(el.text) do
    courant[#courant + 1] = utf8.char(code)
    if TIRETS[code] then
      res:insert(pandoc.Str(table.concat(courant)))
      res:insert(pandoc.RawInline("latex", "\\allowbreak{}"))
      courant, coupe = {}, true
    end
  end
  if not coupe then return nil end
  if #courant > 0 then res:insert(pandoc.Str(table.concat(courant))) end
  return res
end

-- Tableaux : pandoc garde des colonnes `l` (sans retour à la ligne) quand le Markdown
-- est étroit, et règle les largeurs sur les tirets de la ligne d'en-tête sinon. Si le
-- contenu dépasse la ligne, on donne des largeurs relatives tirées du contenu.
local LARGEUR_LIGNE = 92 -- caractères environ, corps 11 pt sur 16,6 cm

local function longueur_cellule(cellule)
  local texte = pandoc.utils.stringify(cellule.contents)
  return utf8.len(texte) or #texte
end

local function Table(t)
  local n = #t.colspecs
  if n == 0 then return nil end
  local maxi = {}
  for i = 1, n do maxi[i] = 3 end
  local function mesurer(lignes)
    for _, ligne in ipairs(lignes) do
      for i, cellule in ipairs(ligne.cells) do
        if i <= n then maxi[i] = math.max(maxi[i], longueur_cellule(cellule)) end
      end
    end
  end
  mesurer(t.head.rows)
  for _, corps in ipairs(t.bodies) do mesurer(corps.body) end
  local total = 0
  for i = 1, n do total = total + maxi[i] end
  if total + 3 * n <= LARGEUR_LIGNE then return nil end
  -- Largeur ∝ racine de la longueur : une colonne courte reste lisible.
  local poids, somme = {}, 0
  for i = 1, n do
    poids[i] = math.sqrt(maxi[i])
    somme = somme + poids[i]
  end
  for i = 1, n do
    t.colspecs[i] = { t.colspecs[i][1], 0.97 * poids[i] / somme }
  end
  return t
end

local function Math(m)
  if m.mathtype == "DisplayMath" then
    -- \tag n'est pas permis dans une boîte : on garde alors \[ … \] tel quel.
    if m.text:find("\\tag") then
      return pandoc.RawInline("latex", "\\[" .. m.text .. "\\]")
    end
    return pandoc.RawInline("latex", "\\equationajustee{" .. m.text .. "}")
  end
  return nil
end

-- Repère `[!TYPE]` en tête du premier paragraphe d'une citation.
local function type_alerte(bq)
  local premier = bq.content[1]
  if not premier or (premier.t ~= "Para" and premier.t ~= "Plain") then return nil end
  local tete = premier.content[1]
  if not tete or tete.t ~= "Str" then return nil end
  local nom = tete.text:match("^%[!([^%]]+)%]$")
  if not nom then return nil end
  return TYPES[nom:upper()] or "encadrenote", premier
end

local function retirer_marqueur(premier)
  local contenu = premier.content
  contenu:remove(1)
  while #contenu > 0 and (contenu[1].t == "SoftBreak" or contenu[1].t == "LineBreak" or contenu[1].t == "Space") do
    contenu:remove(1)
  end
end

local function dans_encadre(blocs)
  return blocs:walk({
    Figure = function(f) return traiter_figure(f, true) end,
  })
end

local function BlockQuote(bq)
  local env, premier = type_alerte(bq)
  local blocs = bq.content
  if not env then
    blocs = dans_encadre(blocs)
    local res = pandoc.List({ pandoc.RawBlock("latex", "\\begin{quote}") })
    res:extend(blocs)
    res:insert(pandoc.RawBlock("latex", "\\end{quote}"))
    return res
  end
  retirer_marqueur(premier)
  if #premier.content == 0 then blocs:remove(1) end
  blocs = dans_encadre(blocs)
  local ouverture
  if env == "indication" then
    indication = indication + 1
    ouverture = "\\begin{indication}{" .. indication .. "}"
  else
    ouverture = "\\begin{" .. env .. "}"
  end
  local res = pandoc.List({ pandoc.RawBlock("latex", ouverture) })
  res:extend(blocs)
  res:insert(pandoc.RawBlock("latex", "\\end{" .. env .. "}"))
  return res
end

local function Header(h)
  if h.level <= 3 then indication = 0 end
  h.level = math.max(1, h.level - 1)
  return h
end

-- Dans une copie bilingue, la première lettre détermine le sens du paragraphe.
-- Babel garde la ponctuation, les chiffres et les passages latins dans leur sens.
local function paragraphe_droite_gauche(p)
  for _, code in utf8.codes(pandoc.utils.stringify(p.content)) do
    local langue
    if (code >= 0x621 and code <= 0x64A) or (code >= 0x671 and code <= 0x6D3) then
      langue = "arabic"
    elseif code >= 0x5D0 and code <= 0x5EA then
      langue = "hebrew"
    end
    if langue then
      return {
        pandoc.RawBlock("latex", "\\begin{otherlanguage}{" .. langue .. "}"),
        p,
        pandoc.RawBlock("latex", "\\end{otherlanguage}"),
      }
    end
    if (code >= 65 and code <= 90) or (code >= 97 and code <= 122)
        or (code >= 0xC0 and code <= 0x2AF) then return nil end
  end
end

-- Parcours dans l'ordre du document (le compteur d'indications en dépend).
function Pandoc(doc)
  -- Pandoc émet lui-même otherlanguage ou foreignlanguage pour lang=ru.
  local russe_balise = false
  local function relever_langue(element)
    if element.attributes.lang == "ru" then russe_balise = true end
  end
  doc = doc:walk({ Math = Math, Image = Image, Code = Code, Table = Table, Str = Str,
                   Div = relever_langue, Span = relever_langue })
  if russe_balise then doc.meta.russe_balise = true end
  local blocs = pandoc.List()
  for _, b in ipairs(doc.blocks) do
    if b.t == "Header" then
      Header(b)
      blocs:insert(b)
    elseif b.t == "BlockQuote" then
      blocs:extend(BlockQuote(b))
    elseif b.t == "Figure" then
      blocs:insert(traiter_figure(b, false) or b)
    else
      blocs:insert(b)
    end
  end
  doc.blocks = blocs
  if doc.meta.arabe or doc.meta.hebreu then
    doc = doc:walk({ Para = paragraphe_droite_gauche })
  end
  return doc
end
