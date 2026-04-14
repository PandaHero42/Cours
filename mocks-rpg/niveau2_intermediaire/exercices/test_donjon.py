# test_donjon.py — NIVEAU 2 : Intermédiaire 🟡
# Fil rouge : Le Donjon
#
# Contexte
# --------
# Le donjon a deux dépendances critiques :
#   - ServeurDes    : service réseau — lent et aléatoire
#   - BaseDeDonnees : persistance — on ne veut PAS écrire de vraies données
#
# Compétences visées
# ------------------
#   @patch  ·  side_effect (liste + exception)  ·  assert_called_with  ·  call
#
# Comment travailler
# ------------------
# Consulte rpg_donjon.py pour comprendre ce que fait chaque méthode.
# Lance avec : python -m unittest test_donjon -v

import unittest
from unittest.mock import Mock, patch, call

from rpg_donjon import ServeurDes, BaseDeDonnees, Monstre, SystemeCombat, GestionnaireDonjon


# ─────────────────────────────────────────────────────────────────────────────
# EXERCICE 1 — @patch : remplacer ServeurDes via le décorateur
# ─────────────────────────────────────────────────────────────────────────────
class TestExercice1_PatchDecorator(unittest.TestCase):

    def test_attaque_touche(self):
        # Utilise @patch sur 'rpg_donjon.ServeurDes'.
        # Scénario : jet d20 = 15 (touche), jet d6 = 4, dégâts_base = 3.
        # Vérifie : touché, 7 dégâts (4+3), monstre toujours vivant (pv=10).
        pass

    def test_attaque_rate(self):
        # Scénario : jet d20 = 5 (raté).
        # Vérifie : pas touché, 0 dégâts, lancer() appelé UNE seule fois
        # (pas de deuxième lancer pour les dégâts).
        pass


# ─────────────────────────────────────────────────────────────────────────────
# EXERCICE 2 — side_effect : exceptions et séquences
# ─────────────────────────────────────────────────────────────────────────────
class TestExercice2_SideEffect(unittest.TestCase):

    def test_panne_serveur_pendant_fuite(self):
        # Le ServeurDes lève une ConnectionError lors de la fuite.
        # Vérifie que fuir() propage bien l'exception.
        pass

    def test_sequence_fuite_reussie_puis_ratee(self):
        # Première tentative de fuite : dé = 5 → réussie.
        # Deuxième tentative : dé = 2 → ratée.
        # Vérifie les deux résultats.
        pass


# ─────────────────────────────────────────────────────────────────────────────
# EXERCICE 3 — Vérifier les arguments précis des appels
# ─────────────────────────────────────────────────────────────────────────────
class TestExercice3_Arguments(unittest.TestCase):

    def test_sauvegarder_appele_avec_bons_arguments(self):
        # Après une attaque réussie (jet=18, dégâts=6, base=2),
        # vérifie que bdd.sauvegarder_personnage est appelée avec
        # le nom du héros ET le bon dictionnaire de données.
        pass

    def test_lancer_appele_avec_bonnes_faces(self):
        # Le jet d'attaque doit utiliser faces=20, le jet de dégâts faces=6.
        # Vérifie les deux appels dans l'ordre avec assert_has_calls.
        pass


# ─────────────────────────────────────────────────────────────────────────────
# EXERCICE 4 — patch() comme context manager
# ─────────────────────────────────────────────────────────────────────────────
class TestExercice4_ContextManager(unittest.TestCase):

    def test_explorer_salle_piege(self):
        # Dé = 3 → piège. Héros démarre avec 20 PV.
        # Vérifie le résultat "Piège !" et que la BDD est sauvegardée
        # avec les PV réduits à 15.
        # Utilise 'with patch(...) as mock:' pour patcher ServeurDes.
        pass

    def test_explorer_salle_heros_introuvable(self):
        # La BDD retourne None pour le héros demandé.
        # Vérifie le résultat "Héros introuvable" et que le ServeurDes
        # n'a jamais été sollicité.
        pass


# ─────────────────────────────────────────────────────────────────────────────
# EXERCICE 5 — Scénario libre
# Objectif : écrire un scénario de combat complet de A à Z.
#
# Scénario :
#   Zara affronte un Gobelin (10 PV, attaque=2, defense=2).
#   Tour 1 : jet d20=8  → raté, pas de dégâts.
#   Tour 2 : jet d20=14 → touché, jet d6=5, dégâts=5+4=9 → Gobelin vivant (1 PV).
#   La BDD doit être appelée deux fois (une par attaque).
# ─────────────────────────────────────────────────────────────────────────────
class TestExercice5_Libre(unittest.TestCase):

    def test_scenario_combat_deux_tours(self):
        pass


if __name__ == "__main__":
    unittest.main(verbosity=2)
