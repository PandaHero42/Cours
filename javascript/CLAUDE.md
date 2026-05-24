# Contexte – Cours Développement front-end (JavaScript)

## Informations générales
- **École** : HEH (Haute École en Hainaut), Bachelier en Informatique – orientation réseaux et télécommunications
- **Cours** : Développement front-end – Travaux pratiques
- **Profs** : Ivan Miller & Baptiste Dambrin
- **Année** : 2025-2026
- **Objectif actuel** : Révisions pour l'examen pratique JS (juin 2026)
- **Règle d'or** : Faire en vanilla JS pur autant que possible. jQuery seulement si nécessaire (animations, etc.). Pas d'AJAX sauf si demandé explicitement.

## Conditions d'examen réel
- Syllabus papier autorisé, notes manuscrites et livres autorisés
- Internet, GSM, clés USB **interdits**
- Fichiers distribués = HTML de base + jquery.min.js + instructions.txt

---

## Structure du dossier

```
javascript/
├── CLAUDE.md                      ← ce fichier
├── TR2-DevFrontEnd-syllabus2026.pdf  ← syllabus complet
├── Test events.html               ← démo interactive des évènements JS
├── exercices/
│   ├── tilapins/                  ← EXERCICE avec instructions (animaux + compteurs)
│   ├── bubulle/                   ← EXERCICE jQuery (bulle de navigation)
│   ├── Slider/                    ← EXERCICE jQuery (slider d'images)
│   ├── Menu burger/               ← EXERCICE jQuery (menu mobile hamburger)
│   ├── Mad Max/                   ← EXERCICE (images chat, pas de base HTML)
│   └── Exercice AJAX backgrounds/ ← IGNORÉ — AJAX pas à l'examen
└── examens/
    ├── Entrainement 2022/         ← Grille 81 cases + diviseurs + jauge
    ├── Entrainez-vous-juin2023/   ← Jeu du 44 (jetons + pioche)
    ├── Examen FrontEnd Chatons 2024/  ← Gestion de chats (+ démo solution fournie)
    ├── Examen Juin 2022 Q1/       ← Conteneurs à déchets
    ├── Examen juin 2022 Questionnaire 2/  ← Jeu des formes
    └── TQ2 DV2 Examen 1 Juin 2019/    ← Jetons/lettres + animation positionnement
```

---

## Plan de révisions (ordre de difficulté croissante)

### EXERCICES (échauffement)
| # | Dossier | Concept clé | Statut |
|---|---------|-------------|--------|
| E1 | `exercices/tilapins/` | Random au chargement, clic, compteur, classe CSS | Terminé |
| E2 | `exercices/Slider/` | Animation jQuery, position absolute, index courant | Terminé |
| E3 | `exercices/Menu burger/` | Toggle show/hide jQuery, clic burger | Terminé |
| E4 | `exercices/bubulle/` | Offset/position jQuery, survol nav | Terminé |

### EXAMENS (entraînement)
| # | Dossier | Concept clé | Statut |
|---|---------|-------------|--------|
| X1 | `examens/Examen FrontEnd Chatons 2024/` | append, val, attr disabled, each, recherche parmi éléments | À faire |
| X2 | `examens/Entrainement 2022/` | Boucle génération DOM, mouseover/mouseleave, modulo, animate() jauge | À faire |
| X3 | `examens/Entrainez-vous-juin2023/` | Jetons libres/bloqués, pioche, cartouches, fadeIn | À faire |
| X4 | `examens/Examen Juin 2022 Q1/` | Génération aléatoire, injection DOM, clic suppression, somme | À faire |
| X5 | `examens/Examen juin 2022 Questionnaire 2/` | Génération formes aléatoires, clic, vérification globale | À faire |
| X6 | `examens/TQ2 DV2 Examen 1 Juin 2019/` | Position aléatoire, fadeIn, animation vers cible, classe "noir" | À faire |

---

## Résumé des exercices et examens

### E1 – Tilapins (`exercices/tilapins/`)
**HTML de base** : `examen.html` + 12 images d'animaux dans `img/`
- Header avec 12 boutons `.bouton` (chacun a `<img>` + `<span>0</span>`)
- 2e header avec `#total > span`
- `<main id="main">` vide
**Ce qu'il faut coder** :
- Au chargement : chaque `<span>` reçoit valeur aléatoire 1-4 ; total = somme
- Au clic sur bouton : si compteur > 0 → ajouter image dans main, décrémenter compteur et total
- Si compteur → 0 : ajouter classe `vide` au bouton (opacité 0.5)
- Si total → 0 : ajouter classe `vide` au `#total` (fond vert)

### E2 – Slider (`exercices/Slider/`)
**HTML de base** : `slider.html` + 5 images `landscape1-5.jpg`
- `#lucarne` (800×600, overflow:hidden) > `#plateau` (position:absolute) > 5 `<img>` empilées
- `#num` affiche le numéro courant
**Ce qu'il faut coder** :
- Clic droit/gauche ou auto → déplacer `#plateau` en left = -index*800px (animate)
- Mise à jour du `#num`

### E3 – Menu burger (`exercices/Menu burger/`)
**HTML de base** : `menu.html`
- `#burger` = bouton hamburger
- `.volet > #navTop` = menu vertical masquable
**Ce qu'il faut coder** :
- Au clic sur `#burger` : toggle show/hide du `.volet` (ou slideToggle)

### E4 – Bubulle (`exercices/bubulle/`)
**HTML de base** : `bubulle.html`
- `#nav > #menu` avec 5 liens `<a>`, et `#bubulle` en position absolute
**Ce qu'il faut coder** :
- Au survol d'un lien : déplacer `#bubulle` pour se superposer au lien (offset/position jQuery, animate)

---

### X1 – Chatons 2024 (`examens/Examen FrontEnd Chatons 2024/`)
**HTML** : `examen à compléter.html` | **Démo solution** : `demo2026.html` (avec le JS du prof)
- `#nom` (input), `#couleur` (select), `#ajouter` (button disabled), `#vider` (button disabled), `#nombre` (span), `#chats` (div)
- Structure d'un chat : `<figure class="chat"><img src="[couleur].jpg" alt=""><figcaption>[nom]</figcaption></figure>`
- Classe `hola` sur figure → zoom (CSS déjà présent)
**Ce qu'il faut coder** :
- Clic `#ajouter` : append figure, vider champ nom, activer vider, màj nombre
- Clic `#vider` : vider `#chats`, nombre = 0, désactiver vider
- Event `input` sur `#nom` : si vide → désactiver ajouter ; sinon → activer ajouter + chercher chat et appliquer classe `hola`

### X2 – Entrainement 2022 (`examens/Entrainement 2022/`)
**HTML** : `index à compléter.html`
- 4 voyants `#div2 #div3 #div5 #div7` (classe `vert` = allumé)
- `#nb` (span dans h2), `#metre` (jauge orange, width en %), `#grille` (vide)
- Classe `moiaussi` sur `.case` = fond beige
**Ce qu'il faut coder** :
- Au chargement : générer 81 `.case` avec valeur = rand(1-7) × rand(1-7) dans `#grille`
- Survol `.case` : cette case + toutes les cases mêmes valeur → classe `moiaussi`, allumer voyants diviseurs (% 2/3/5/7 === 0), afficher nb diviseurs, animer jauge
- Fin survol `#grille` : tout reset (enlever classes, nb=0, jauge animate 0)

### X3 – Jeu du 44 (`examens/Entrainez-vous-juin2023/`)
**HTML** : `examen.html`
- `#pioche` (bouton), 5 `.cartouche` (verte → rouge = `vide`), 6 `.jeton.libre`
- `#total` (span), `#victoire` et `#perdu` (cachés par défaut, display:none)
**Ce qu'il faut coder** :
- Au chargement : chaque jeton libre reçoit valeur random 1-9 ; màj total
- Clic sur jeton : toggle classe `libre` (libre=gris, pas libre=noir)
- Clic sur `#pioche` : les jetons **libres** reçoivent nouvelle valeur random 1-9 ; màj total ; vider une cartouche (rouge)
- Si total ≥ 44 : `#victoire` fadeIn
- Si dernière cartouche vidée et total < 44 : `#perdu` fadeIn

### X4 – Conteneurs (`examens/Examen Juin 2022 Q1/`)
**HTML** : `index à compléter.html`
- 4 `#conteneur1-4` (div.conteneur) + 4 `#conteneur1-4-etiquette` avec `.contenance` et `.contenu`
**Ce qu'il faut coder** :
- `var contenances = [8,10,12,15,20]` ; `var dechets = ['planches','bricaillons','briques','carrelages','poutres','sable','contreplaqués',...]`
- Au chargement : pour chaque conteneur → contenance aléatoire, générer x (1-5) déchets `.dechet` avec intitulé + volume aléatoire (1-7)
- Évaluation : sommer volumes, afficher dans `.contenu`, si > contenance → classe `trop` (rouge)
- Clic sur `.dechet` : supprimer, réévaluer

### X5 – Formes (`examens/Examen juin 2022 Questionnaire 2/`)
**HTML** : `index à compléter.html`
- `#header > h1 > #laforme` (span), `#main` (vide)
- Classes de formes déjà en CSS : `.triangle .cercle .carré .pentagone .trapèze .parallélogramme .losange .octogone`
- `var formes = ["triangle","cercle","carré","pentagone","trapèze","parallélogramme","losange","octogone"]`
**Ce qu'il faut coder** :
- Au chargement : piocher **laForme** (aléatoire), l'afficher dans `#laforme`, générer une `div.ligne` avec 8 `.forme.[nomforme]` (au moins 1 = laForme)
- Clic forme : si mauvaise → classe `badjob` (grise) ; si bonne → classe `goodjob` (verte), vérifier si toutes les laForme sont vertes → nouvelle ligne au-dessus

### X6 – Jetons/Lettres 2019 (`examens/TQ2 DV2 Examen 1 Juin 2019/`)
**HTML** : pas de base HTML fournie (à créer ou improviser)
- 10 cases en haut, 10 jetons avec lettres : a,a,i,s,c,j,v,t,r,p
- Jetons : `position:absolute`, apparition par opacité (fadeIn)
**Ce qu'il faut coder** :
- Générer 10 cases + 10 jetons en JS
- Positionner jetons aléatoirement (≥ 100px des bords), invisibles → fadeIn
- Survol jeton : change couleur ; clic : devient noir (classe `noir`, enlever sur les autres)
- Clic sur case : le jeton `noir` s'anime (800ms) vers la position de la case

---

## Patterns JS à maîtriser (récap rapide)

```javascript
// Nombre aléatoire entier entre 1 et N
Math.floor(Math.random() * N) + 1

// Cibler un élément (vanilla JS)
document.getElementById("id")
document.querySelectorAll(".classe")

// Modifier texte
element.textContent = "valeur";
element.innerHTML = "<span>html</span>";

// Ajouter/retirer une classe
element.classList.add("maclasse");
element.classList.remove("maclasse");
element.classList.toggle("maclasse");
element.classList.contains("maclasse"); // true/false

// Créer et injecter un élément
let div = document.createElement("div");
div.className = "case";
div.textContent = 42;
document.getElementById("grille").appendChild(div);

// innerHTML pour injection rapide (examen)
document.getElementById("grille").innerHTML += '<div class="case">42</div>';

// Event listener
element.addEventListener("click", function() { ... });
element.addEventListener("mouseover", function() { ... });
element.addEventListener("mouseleave", function() { ... });

// Au chargement du DOM (vanilla)
document.addEventListener("DOMContentLoaded", function() { ... });

// Récupérer valeur d'un input
document.getElementById("nom").value

// Attribut disabled
document.getElementById("btn").disabled = true;
document.getElementById("btn").disabled = false;

// Boucle sur NodeList
document.querySelectorAll(".case").forEach(function(el) { ... });

// Modulo (teste la divisibilité)
if (valeur % 2 === 0) { /* divisible par 2 */ }
```

## jQuery – patterns courants (si besoin)
```javascript
// Attendre le DOM
$(function() { ... });

// Sélecteurs
$('#id')  $('.classe')  $('div')

// Texte / HTML
$('#id').text("valeur")
$('#id').html("<span>...</span>")

// Classes
$('#id').addClass("maclasse")
$('#id').removeClass("maclasse")
$('#id').toggleClass("maclasse")
$('#id').hasClass("maclasse")  // true/false

// Valeur d'input
$('#nom').val()

// Attribut
$('#btn').attr('disabled', true)
$('#btn').attr('disabled', false)

// Créer/injecter
$('#grille').append('<div class="case">42</div>')
$('#grille').empty()

// Chaque élément
$('.case').each(function() {
    let val = $(this).text();
});

// Événements
$('#btn').on('click', function() { ... })
$('#nom').on('input', function() { ... })
$('.case').on('mouseover', function() { ... })
$('#grille').on('mouseleave', function() { ... })

// Animations
$('#el').fadeIn()
$('#el').fadeOut()
$('#el').animate({ width: '50%' }, 400)
$('#el').slideToggle()

// CSS
$('#el').css('left', '200px')

// Position / Offset (pour bubulle, jetons)
let pos = $('#el').offset();  // { top, left } relatif au document
let pos2 = $('#el').position(); // { top, left } relatif au parent positionné
```

---

## Approche pédagogique
- On avance **morceau par morceau**, une étape à la fois
- Je te dis **quoi écrire** et **où exactement** l'écrire
- On fait d'abord les **exercices** (E1→E4), puis les **examens** (X1→X6)
- Objectif : tout faire en **vanilla JS** sauf animations complexes (jQuery si vraiment nécessaire)
- Chaque solution sera dans le fichier HTML correspondant, dans une balise `<script>` avant `</body>`
