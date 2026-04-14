# 🟢 Niveau 1 — La Taverne (Débutant)

## Objectifs pédagogiques

À la fin de ce niveau, tu sais :

- Créer un `Mock()` manuellement
- Configurer `.return_value` pour contrôler la réponse
- Vérifier un appel avec `.assert_called_once()` et `.assert_called_once_with()`
- Injecter un mock dans une vraie classe via le constructeur

## Contexte narratif

Tu arrives dans la ville de **Froidelame**. La taverne locale propose des quêtes
aux aventuriers, mais la difficulté est déterminée par un lancer de dé aléatoire.

Pour tester la logique du héros et de la taverne **sans jamais lancer un vrai dé**,
tu vas utiliser des Mocks.

## Fichiers

| Fichier | Rôle |
|---------|------|
| `exercices/rpg_taverne.py` | Classes fournies — **ne pas modifier** |
| `exercices/test_taverne.py` | **Ton fichier à compléter** |
| `solutions/test_taverne_SOLUTION.py` | Correction — ouvre après avoir essayé |

## Lancer les tests

```bash
cd niveau1_debutant/exercices
python -m pytest test_taverne.py -v
```

## Progression attendue

```
EXERCICE 1 — Créer et configurer un Mock basique        (2 tests)
EXERCICE 2 — Injecter un mock dans Taverne              (3 tests)
EXERCICE 3 — Mocker la Taverne entière pour tester Heros (3 tests)
EXERCICE 4 — Écrire un test complet de zéro             (1 test)
```

## Indice si tu bloques

Un mock se crée ainsi :
```python
from unittest.mock import Mock
faux_objet = Mock()
faux_objet.ma_methode.return_value = 42
```

Pour vérifier qu'une méthode a été appelée :
```python
faux_objet.ma_methode.assert_called_once()
faux_objet.ma_methode.assert_called_once_with(42)
```
