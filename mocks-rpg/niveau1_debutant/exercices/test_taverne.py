# test_taverne.py — NIVEAU 1 : Débutant 🟢
# Fil rouge : La Taverne
#
# Contexte
# --------
# Le héros Aldric veut tenter des quêtes dans la taverne.
# La taverne utilise un dé RÉEL — résultats imprévisibles à chaque test.
# Ta mission : remplacer le dé et la taverne par des Mocks pour
# contrôler les scénarios.
#
# Compétences visées
# ------------------
#   Mock()  ·  return_value  ·  assert_called  ·  injection manuelle
#
# Comment travailler
# ------------------
# Lis le contexte de chaque test, puis écris le code.
# Lance avec : python -m unittest test_taverne -v

import unittest
from unittest.mock import Mock

from rpg_taverne import De, Taverne, Heros


# ─────────────────────────────────────────────────────────────────────────────
# EXERCICE 1 — Ton premier Mock
# Objectif : créer un Mock, lui configurer une réponse, vérifier qu'il répond.
# ─────────────────────────────────────────────────────────────────────────────
class TestExercice1_PremierMock(unittest.TestCase):

    def test_mock_de_retourne_valeur_configuree(self):
        de = Mock()
        de.lancer.return_value = 4
        resultat = de.lancer()
        self.assertEqual(resultat, 4)

    def test_mock_memorise_les_appels(self):
        de = Mock()
        de.lancer()
        de.lancer()
        de.lancer()
        self.assertEqual(de.lancer.call_count, 3)
        


# ─────────────────────────────────────────────────────────────────────────────
# EXERCICE 2 — Injecter un Mock dans Taverne
# Objectif : remplacer le vrai dé par un Mock pour contrôler quelle quête
#            est proposée.
# ─────────────────────────────────────────────────────────────────────────────
class TestExercice2_TaverneAvecMock(unittest.TestCase):

    def test_taverne_propose_quete_facile(self):
        # Dé fixé à 1 → quête attendue : "Chercher des champignons", difficulté 1.
        de = Mock()
        de.lancer.return_value = 1
        taverne = Taverne(de)
        quete = taverne.proposer_quete()
        self.assertEqual(quete["difficulte"], 1)
        self.assertEqual(quete["nom"], "Chercher des champignons")

    def test_taverne_propose_quete_difficile(self):
        # Dé fixé à 6 → quête attendue : "Tuer le dragon de la montagne", difficulté 6.
        de = Mock()
        de.lancer.return_value = 6
        taverne = Taverne(de)
        quete = taverne.proposer_quete()
        self.assertEqual(quete["difficulte"], 6)
        self.assertEqual(quete["nom"], "Tuer le dragon de la montagne")
        

    def test_taverne_appelle_le_de_une_fois(self):
        # Pour une seule quête proposée, lancer() doit être appelé exactement une fois.
        de = Mock()
        de.lancer.return_value = 3
        taverne = Taverne(de)
        quete = taverne.proposer_quete()
        de.lancer.assert_called_once()


# ─────────────────────────────────────────────────────────────────────────────
# EXERCICE 3 — Tester Heros sans la vraie Taverne
# Objectif : mocker la Taverne entière pour tester uniquement la logique
#            de Heros.tenter_quete().
# ─────────────────────────────────────────────────────────────────────────────
class TestExercice3_Heros(unittest.TestCase):

    def test_heros_reussit_quete_facile(self):
        # Aldric (force=5) face à une quête de difficulté 2.
        # Résultat attendu : "Victoire !", quetes_reussies == 1.
        taverne = Mock()
        taverne.proposer_quete.return_value = {"nom": "Livrer un colis au village voisin", "difficulte": 2}
        heros = Heros(nom="Aldric", force=5, taverne=taverne)
        resultat = heros.tenter_quete()
        self.assertEqual(resultat, "Victoire !")
        self.assertEqual(heros.quetes_reussies, 1)

    def test_heros_echoue_quete_trop_difficile(self):
        # Aldric (force=2) face à une quête de difficulté 5.
        # Résultat attendu : "Échec...", quetes_reussies == 0.
        taverne = Mock()
        taverne.proposer_quete.return_value = {"nom": "Retrouver un enfant perdu", "difficulte": 5}
        heros = Heros(nom="Aldric", force=2, taverne=taverne)
        resultat = heros.tenter_quete()
        self.assertEqual(resultat, "Échec...")
        self.assertEqual(heros.quetes_reussies, 0)

    def test_heros_consulte_toujours_la_taverne(self):
        # Peu importe le résultat, proposer_quete() doit être appelée.
        taverne = Mock()
        taverne.proposer_quete.return_value = {"nom": "Escorter un marchand", "difficulte": 3}
        heros = Heros(nom="Aldric", force=1, taverne=taverne)
        resultat = heros.tenter_quete()
        taverne.proposer_quete.assert_called()


# ─────────────────────────────────────────────────────────────────────────────
# EXERCICE 4 — Écriture libre
# Objectif : écrire un test complet de A à Z, sans squelette.
#
# Scénario : Aldric (force=3) tente 3 quêtes de difficulté 3.
#            Il doit les réussir toutes → quetes_reussies == 3.
# ─────────────────────────────────────────────────────────────────────────────
class TestExercice4_Libre(unittest.TestCase):

    def test_trois_victoires_consecutives(self):
        taverne = Mock()
        taverne.proposer_quete.return_value = {"nom": "Escorter un marchand", "difficulte": 3}
        heros = Heros(nom="Aldric", force=3, taverne=taverne)
        for _ in range(3):
            resultat = heros.tenter_quete()
            self.assertEqual(resultat, "Victoire !")
        self.assertEqual(heros.quetes_reussies, 3)


if __name__ == "__main__":
    unittest.main(verbosity=2)
