# test_aventure.py — FIL ROUGE COMPLET ⭐
# Projet : Aventure Complète
#
# Contexte
# --------
# Tu testes MoteurJeu — le cœur du RPG.
# Il dépend de quatre services injectés :
#   IDe · IBDD · INotificateur · IGenerateurNom
#
# Consulte aventure_complete.py pour comprendre chaque méthode.
# La fonction creer_moteur_test() ci-dessous te donne un moteur
# prêt à l'emploi avec quatre autospec propres.
#
# Progression
# -----------
#   Partie A : tests guidés par un contexte précis
#   Partie B : contexte fourni, structure libre
#   Partie C : docstring seule — tu décides de tout
#
# Lance avec : python -m unittest test_aventure -v

import unittest
from unittest.mock import create_autospec, ANY

from aventure_complete import (
    MoteurJeu, Heros, Monstre, Objet,
    IDe, IBDD, INotificateur, IGenerateurNom,
)


def creer_moteur_test():
    """Retourne (moteur, mock_de, mock_bdd, mock_notif, mock_gen)."""
    mock_de   = create_autospec(IDe,             instance=True)
    mock_bdd  = create_autospec(IBDD,            instance=True)
    mock_notif= create_autospec(INotificateur,   instance=True)
    mock_notif.envoyer.return_value = True
    mock_gen  = create_autospec(IGenerateurNom,  instance=True)
    moteur = MoteurJeu(
        de=mock_de, bdd=mock_bdd,
        notificateur=mock_notif, generateur_nom=mock_gen,
    )
    return moteur, mock_de, mock_bdd, mock_notif, mock_gen


# ─────────────────────────────────────────────────────────────────────────────
# PARTIE A — Tests guidés
# ─────────────────────────────────────────────────────────────────────────────

class TestA_CreerHeros(unittest.TestCase):

    def test_creer_guerrier_sauvegarde_en_bdd(self):
        # Crée un guerrier "Aldric" (héros inexistant en BDD).
        # Vérifie que bdd.sauvegarder est appelée et que les stats retournées
        # sont celles d'un guerrier (pv=40, attaque=8, defense=12).
        pass

    def test_creer_heros_existant_leve_erreur(self):
        # bdd.existe retourne True → ValueError attendue.
        pass

    def test_creer_heros_envoie_notification_success(self):
        # La création réussie doit déclencher une notification niveau="success".
        pass

    def test_creer_classe_inconnue_leve_erreur(self):
        # La classe "paladin" n'existe pas → ValueError attendue.
        pass


class TestA_AttaqueEtObjets(unittest.TestCase):

    def test_attaque_heros_touche(self):
        # Aldric (attaque=8) frappe Gobelin (defense=5, pv=15).
        # Jet=10 → touche, dégâts jet=4 → 12 pts.
        # Vérifie le résultat et les PV restants du gobelin.
        pass

    def test_attaque_heros_rate(self):
        # Jet=2 → rate le boss (defense=15).
        # Vérifie : pas touché, lancer() appelé une seule fois.
        pass

    def test_utiliser_potion_soigne_heros(self):
        # Héros blessé (pv=10, pv_max=40) utilise une Potion de Soin (valeur=15).
        # Vérifie les PV après soin et que la BDD est mise à jour.
        pass


# ─────────────────────────────────────────────────────────────────────────────
# PARTIE B — Tests semi-guidés
# ─────────────────────────────────────────────────────────────────────────────

class TestB_ResoudreCombat(unittest.TestCase):

    def test_combat_victoire_un_tour(self):
        # Héros très fort (attaque=20) tue un gobelin (pv=5, defense=2) en un coup.
        # Vérifie : résultat "victoire", héros gagne l'XP du gobelin,
        # BDD sauvegardée, notification "success".
        pass

    def test_combat_defaite(self):
        # Héros fragile (pv=5, defense=2) ne touche jamais le boss (defense=20)
        # et se fait tuer dès le premier contre.
        # Vérifie : résultat "defaite", BDD sauvegardée, notification "error".
        pass

    def test_montee_niveau_apres_victoire(self):
        # Héros niveau 1 à 90 XP bat un gobelin qui donne 20 XP → total 110.
        # Seuil niveau 2 = 100 → monte de niveau.
        # Vérifie niveau=2, pv_max augmenté, notification "success" pour la montée.
        pass


# ─────────────────────────────────────────────────────────────────────────────
# PARTIE C — Tests libres (docstring = seule spécification)
# ─────────────────────────────────────────────────────────────────────────────

class TestC_Libre(unittest.TestCase):

    def test_generer_monstre_utilise_generateur_nom(self):
        """
        generer_monstre("gobelin", niveau_donjon=3) doit appeler
        generateur_nom.generer("gobelin") et retourner un Monstre
        avec les stats adaptées au niveau 3 (pv=25, attaque=9, defense=5, butin_xp=60).
        """
        pass

    def test_charger_heros_inexistant_leve_keyerror(self):
        """charger_heros() avec bdd.charger retournant None → KeyError."""
        pass

    def test_utiliser_arme_augmente_attaque(self):
        """
        Héros (attaque=8) équipe une "Épée Elfique" (type="arme", valeur=4).
        Son attaque passe à 12. BDD mise à jour. Notification envoyée.
        """
        pass

    def test_utiliser_objet_type_inconnu_leve_erreur(self):
        """Type d'objet "parchemin" non supporté → ValueError."""
        pass

    def test_potion_ne_depasse_pas_pv_max(self):
        """
        Héros pv=38, pv_max=40. Potion de 10 PV.
        PV capés à 40. L'effet retourné indique +2 PV (pas +10).
        """
        pass

    def test_scenario_aventure_complet(self):
        """
        Ragnar (guerrier, pv=40, attaque=8, defense=12, xp=50)
        affronte Grug le Troll (pv=20, defense=6, attaque=5, butin_xp=40).

        Tour 1 : att_h jet=8  → touche (16>6), dégâts jet=5 → 13 pts (troll : 7 PV)
                 att_m jet=3  → rate (8≤12)
        Tour 2 : att_h jet=6  → touche (14>6), dégâts jet=7 → 15 pts (troll : mort)

        Après : Ragnar gagne 40 XP → total 90 (pas encore niveau 2).
        Vérifie les PV du troll à chaque tour, les PV de Ragnar (inchangés),
        l'XP final, la BDD sauvegardée et au moins 1 notification "success".
        """
        pass


if __name__ == "__main__":
    unittest.main(verbosity=2)
