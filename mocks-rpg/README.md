# 🎮 Mocks en Python — Série RPG

Bienvenue dans la série d'exercices sur les **mocks Python** avec le fil rouge
**Donjon & Dragons du Code** — un mini-RPG textuel qu'on construit et teste
au fil des trois niveaux.

---

## 🗺️ Carte du dépôt

```
mocks-rpg/
├── niveau1_debutant/        # 🟢 Premiers mocks — objets simples
├── niveau2_intermediaire/   # 🟡 @patch, side_effect, séquences
├── niveau3_avance/          # 🔴 autospec, architecture, intégration
└── fil_rouge_complet/       # ⭐ Projet final — tout en un
```

Chaque dossier contient :
- `exercices/`  → fichiers **à compléter** par l'étudiant
- `solutions/`  → **NE PAS OUVRIR** avant d'avoir essayé 😄

---

## 🧰 Prérequis

```bash
python --version   # 3.9+
python -m pytest --version
```

Pas d'installation supplémentaire — `unittest.mock` est dans la stdlib.

---

## ▶️ Lancer les tests

```bash
# Depuis un dossier niveau
python -m pytest exercices/ -v

# Ou en unittest classique
python -m unittest discover exercices/
```

---

## 📖 Les niveaux

| Niveau | Thème | Compétences |
|--------|-------|-------------|
| 🟢 Débutant | La Taverne | `Mock()`, `return_value`, `assert_called` |
| 🟡 Intermédiaire | Le Donjon | `@patch`, `side_effect`, séquences de valeurs |
| 🔴 Avancé | Le Boss Final | `autospec`, injection de dépendances, architecture |
| ⭐ Fil rouge | Aventure complète | Tout combiner dans un vrai mini-jeu |

---

> *"Un bon test de RPG ne fait pas exploser le serveur de dés — il le mocke."*
