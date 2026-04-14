# 🔴 Niveau 3 — Le Boss Final (Avancé)

## Objectifs pédagogiques

À la fin de ce niveau, tu sais :

- Utiliser `create_autospec()` pour contraindre un mock à une vraie interface
- Vérifier l'**ordre** des appels avec `assert_has_calls`
- Tester des comportements conditionnels complexes (phases de boss)
- Gérer plusieurs dépendances mockées simultanément (dés + BDD + notificateur)
- Vérifier des effets de bord multiples dans un seul test

## Contexte narratif

Le boss final **Dragon Limon** a plusieurs phases — il devient *enragé* quand
ses PV tombent sous 50 %. Trois services externes entrent en jeu simultanément :
le serveur de dés, la base de données, et le notificateur d'alertes.

Pour tester tout ça sans rien déclencher en vrai, tu vas découvrir deux
nouveaux outils.

---

## 🔍 Fiche découverte — `create_autospec`

### Le problème que ça résout

Un `Mock()` classique accepte **n'importe quel appel**, même les fautes de frappe :

```python
mock_de = Mock()
mock_de.lancer(foo="bar")   # ← pas d'erreur ! pourtant ça n'existe pas
mock_de.lancerr(faces=20)   # ← faute de frappe → toujours pas d'erreur
```

Résultat : ton test peut passer alors que ton code appelle une méthode
qui n'existe pas. C'est un **faux positif silencieux**.

### La solution : `create_autospec`

```python
from unittest.mock import create_autospec

# On crée un mock qui respecte EXACTEMENT la signature de IDe
mock_de = create_autospec(IDe, instance=True)

mock_de.lancer(faces=20, nb=1)   # ✅ signature correcte → OK
mock_de.lancer(foo="bar")        # ❌ TypeError immédiat → bug détecté !
mock_de.lancerr(faces=20)        # ❌ AttributeError → faute de frappe détectée !
```

### Quand l'utiliser

- Dès que tu patches **une classe entière** (pas juste une méthode)
- Quand tu veux être sûr que ton code appelle les bonnes méthodes
  avec les bons arguments
- En niveau 3+, utilise `create_autospec` par défaut à la place de `Mock()`

### Résumé en une ligne

> `create_autospec(MaClasse, instance=True)` = un `Mock()` qui connaît
> la vraie forme de `MaClasse` et refuse tout le reste.

---

## 🔍 Fiche découverte — `assert_has_calls`

### Le problème que ça résout

`assert_called_once_with()` ne vérifie que le **dernier appel**, ou qu'il y
en a eu exactement un. Mais parfois on veut vérifier **plusieurs appels dans l'ordre** :

```python
# On veut vérifier que ces deux appels ont eu lieu dans cet ordre :
# 1. lancer(faces=20, nb=1)   ← jet d'attaque
# 2. lancer(faces=8, nb=1)    ← jet de dégâts

mock_de.assert_called_once_with(...)  # ← ne peut vérifier qu'un seul appel
```

### La solution : `assert_has_calls`

```python
from unittest.mock import call

mock_de.assert_has_calls([
    call(faces=20, nb=1),   # 1er appel attendu
    call(faces=8, nb=1),    # 2ème appel attendu
])
```

Par défaut, vérifie que ces appels ont eu lieu **dans cet ordre**,
mais accepte qu'il y ait d'autres appels entre les deux.

Pour exiger que ce soient les **seuls** appels et dans le bon ordre :

```python
mock_de.assert_has_calls([
    call(faces=20, nb=1),
    call(faces=8, nb=1),
], any_order=False)   # False = ordre strict (c'est le défaut)
```

### `call` — à quoi ça sert ?

`call(...)` est juste un objet qui représente un appel attendu.
C'est ce qu'on met dans la liste passée à `assert_has_calls`.

```python
from unittest.mock import call

# Ces deux écritures sont équivalentes :
mock.assert_called_once_with("Aldric", niveau="success")

mock.assert_has_calls([
    call("Aldric", niveau="success")
])
```

### Quand l'utiliser

- Quand une méthode est appelée **plusieurs fois** avec des arguments différents
- Quand l'**ordre** des appels a de l'importance (ex : d'abord le jet d'attaque,
  ensuite le jet de dégâts — pas l'inverse)
- Pour vérifier une séquence de notifications dans le bon ordre

### Résumé en une ligne

> `assert_has_calls([call(...), call(...)])` = "ces appels ont-ils eu lieu,
> dans cet ordre ?"

---

## Fichiers

| Fichier | Rôle |
|---------|------|
| `exercices/rpg_boss.py` | Classes fournies — **ne pas modifier** |
| `exercices/test_boss.py` | **Ton fichier à compléter** |
| `solutions/test_boss_SOLUTION.py` | Correction — ouvre après avoir essayé |

## Lancer les tests

```bash
cd niveau3_avance/exercices
python -m unittest test_boss -v
```

## Progression attendue

```
EXERCICE 1 — Découvrir create_autospec                  (2 tests)
EXERCICE 2 — Tester un tour de combat complet           (3 tests)
EXERCICE 3 — Vérifier l'ordre des notifications         (2 tests)
EXERCICE 4 — Tester SystemeProgression (BDD + logique)  (3 tests)
EXERCICE 5 — Scénario complet de zéro                   (1 test)
```

## Rappel des outils vus aux niveaux précédents

```python
from unittest.mock import Mock, MagicMock, patch, create_autospec, call

# Niveau 1
mock = Mock()
mock.methode.return_value = 42
mock.methode.assert_called_once()
mock.methode.assert_called_once_with(42)

# Niveau 2
mock.methode.side_effect = [1, 2, 3]          # séquence
mock.methode.side_effect = ValueError("boom") # exception

# Niveau 3 (nouveau)
mock = create_autospec(MonInterface, instance=True)  # mock typé
mock.methode.assert_has_calls([call(1), call(2)])    # ordre des appels
```
