# ⭐ Fil Rouge Complet — Aventure RPG

## Objectif

Tester **MoteurJeu** — le cœur d'un mini-RPG complet —
en mobilisant toutes les compétences des 3 niveaux précédents.

## Architecture du projet

```
aventure_complete.py
│
├── IDe              ← service de dés          (à mocker)
├── IBDD             ← base de données         (à mocker)
├── INotificateur    ← notifications/logs      (à mocker)
├── IGenerateurNom   ← générateur de noms      (à mocker)
│
└── MoteurJeu        ← logique principale      (à TESTER)
    ├── creer_heros()
    ├── charger_heros() / sauvegarder_heros()
    ├── generer_monstre()
    ├── attaque_heros() / attaque_monstre()
    ├── resoudre_combat()
    └── utiliser_objet()
```

## Structure des exercices

| Partie | Guidage | Compétences |
|--------|---------|-------------|
| **A** — Tests guidés | Squelettes fournis avec TODO | Niveaux 1+2 |
| **B** — Semi-guidés | Contexte fourni, pas de squelette | Niveaux 2+3 |
| **C** — Libres | Docstring seule | Tout combiner |

## La fonction helper

```python
def creer_moteur_test():
    """Retourne (moteur, mock_de, mock_bdd, mock_notif, mock_gen)"""
```

**Utilise-la systématiquement** — elle garantit des mocks propres avec `autospec`.

## Lancer les tests

```bash
cd fil_rouge_complet/exercices
python -m pytest test_aventure.py -v --tb=short
```

## Récapitulatif de tous les outils utilisés

```python
from unittest.mock import Mock, MagicMock, patch, create_autospec, call, ANY

# ── Niveau 1 ──────────────────────────────────────────────────
faux = Mock()
faux.methode.return_value = 42          # dicter la réponse
faux.methode.assert_called_once()       # a-t-il été appelé ?
faux.methode.assert_called_once_with(x) # avec quels args ?
faux.methode.assert_not_called()        # ne doit PAS être appelé

# ── Niveau 2 ──────────────────────────────────────────────────
faux.methode.side_effect = [1, 2, 3]          # séquence de valeurs
faux.methode.side_effect = ValueError("boom") # simuler une panne
faux.methode.assert_has_calls([               # vérifier plusieurs appels
    call(a=1), call(a=2)
])

# ── Niveau 3 ──────────────────────────────────────────────────
faux = create_autospec(MonInterface, instance=True)  # mock typé
ANY   # joker pour assert_called_with quand le message exact importe peu
```

## Conseil de progression

1. Commence par la **Partie A** (les TODO sont guidés)
2. Passe en **Partie B** quand la Partie A est au vert
3. Attaque la **Partie C** quand tu te sens à l'aise
4. Le dernier test (`test_scenario_aventure_complet`) est volontairement
   le plus long — prends le temps de calculer la séquence de dés sur papier
   avant de coder
