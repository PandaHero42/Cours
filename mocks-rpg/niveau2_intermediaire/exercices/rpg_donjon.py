# rpg_donjon.py
# Classes RPG — NE PAS MODIFIER ce fichier.

class ServeurDes:
    """
    Service distant qui génère des lancers de dés.
    En production, ce serait un appel réseau vers une API.
    """

    def lancer(self, faces: int, nb: int = 1) -> list[int]:
        """Lance `nb` dés à `faces` faces. Retourne une liste de résultats."""
        import random
        return [random.randint(1, faces) for _ in range(nb)]


class BaseDeDonnees:
    """Simule une base de données de personnages persistante."""

    def __init__(self):
        self._data: dict = {}

    def charger_personnage(self, nom: str) -> dict | None:
        return self._data.get(nom)

    def sauvegarder_personnage(self, nom: str, data: dict) -> bool:
        self._data[nom] = data
        return True


class Monstre:
    """Un monstre dans le donjon avec ses propres stats."""

    def __init__(self, nom: str, pv: int, attaque: int):
        self.nom = nom
        self.pv = pv
        self.attaque = attaque
        self.est_vivant = True

    def subir_degats(self, degats: int) -> None:
        self.pv -= degats
        if self.pv <= 0:
            self.est_vivant = False


class SystemeCombat:
    """
    Gère les combats tour par tour entre un héros et un monstre.
    Dépend d'un ServeurDes pour les jets d'attaque.
    """

    def __init__(self, serveur_des: ServeurDes, bdd: BaseDeDonnees):
        self.serveur_des = serveur_des
        self.bdd = bdd

    def attaquer(self, attaquant_nom: str, degats_base: int, monstre: Monstre) -> dict:
        """
        Le héros attaque. Lance 1d20 pour toucher (>=10 = succès),
        puis 1d6 + degats_base pour les dégâts si touché.
        Sauvegarde l'état du héros après l'attaque.
        Retourne {"touche": bool, "degats": int, "monstre_vivant": bool}.
        """
        jet_attaque = self.serveur_des.lancer(faces=20, nb=1)[0]

        if jet_attaque < 10:
            self.bdd.sauvegarder_personnage(attaquant_nom, {"derniere_action": "raté"})
            return {"touche": False, "degats": 0, "monstre_vivant": monstre.est_vivant}

        jet_degats = self.serveur_des.lancer(faces=6, nb=1)[0]
        degats_totaux = jet_degats + degats_base
        monstre.subir_degats(degats_totaux)

        self.bdd.sauvegarder_personnage(attaquant_nom, {
            "derniere_action": "attaque",
            "degats_infliges": degats_totaux,
        })

        return {
            "touche": True,
            "degats": degats_totaux,
            "monstre_vivant": monstre.est_vivant,
        }

    def fuir(self, heros_nom: str) -> bool:
        """
        Le héros tente de fuir. Lance 1d6 : >=4 = succès.
        Retourne True si fuite réussie.
        """
        jet = self.serveur_des.lancer(faces=6, nb=1)[0]
        succes = jet >= 4
        self.bdd.sauvegarder_personnage(heros_nom, {
            "derniere_action": "fuite",
            "fuite_reussie": succes,
        })
        return succes


class GestionnaireDonjon:
    """
    Gère l'exploration du donjon.
    Charge le héros depuis la BDD, décide de l'issue des rencontres.
    """

    def __init__(self, bdd: BaseDeDonnees, serveur_des: ServeurDes):
        self.bdd = bdd
        self.serveur_des = serveur_des

    def explorer_salle(self, heros_nom: str) -> str:
        """
        Explore une salle. Charge le héros, lance 1d6 pour déterminer
        ce qu'il y a dans la salle :
          1-2 : "Salle vide"
          3-4 : "Piège !" (le héros perd 5 PV — mis à jour en BDD)
          5-6 : "Monstre !"
        Retourne une description de la salle.
        """
        heros = self.bdd.charger_personnage(heros_nom)
        if heros is None:
            return "Héros introuvable"

        jet = self.serveur_des.lancer(faces=6, nb=1)[0]

        if jet <= 2:
            return "Salle vide"
        elif jet <= 4:
            heros["pv"] = heros.get("pv", 20) - 5
            self.bdd.sauvegarder_personnage(heros_nom, heros)
            return "Piège !"
        else:
            return "Monstre !"
