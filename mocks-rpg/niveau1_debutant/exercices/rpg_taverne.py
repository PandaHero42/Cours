# rpg_taverne.py
# Classes RPG fournies — NE PAS MODIFIER ce fichier.

class De:
    """Un dé à N faces. Lance un nombre aléatoire entre 1 et N."""

    def __init__(self, faces: int = 6):
        self.faces = faces

    def lancer(self) -> int:
        import random
        return random.randint(1, self.faces)


class Taverne:
    """
    La taverne propose des quêtes aux héros.
    Elle utilise un dé pour générer la difficulté de chaque quête.
    """

    def __init__(self, de: De):
        self.de = de

    def proposer_quete(self) -> dict:
        """
        Propose une quête dont la difficulté est tirée au dé (1d6).
        Retourne un dictionnaire  {"nom": str, "difficulte": int}.
        """
        difficulte = self.de.lancer()
        noms = {
            1: "Chercher des champignons",
            2: "Livrer un colis au village voisin",
            3: "Escorter un marchand",
            4: "Nettoyer les rats de la cave",
            5: "Retrouver un enfant perdu",
            6: "Tuer le dragon de la montagne",
        }
        return {"nom": noms[difficulte], "difficulte": difficulte}


class Heros:
    """
    Un héros qui peut accepter des quêtes depuis la taverne.
    Il réussit une quête si sa force est >= à la difficulté.
    """

    def __init__(self, nom: str, force: int, taverne: Taverne):
        self.nom = nom
        self.force = force
        self.taverne = taverne
        self.quetes_reussies = 0

    def tenter_quete(self) -> str:
        """
        Récupère une quête de la taverne et tente de la réussir.
        Retourne "Victoire !" ou "Échec..." selon la force du héros.
        """
        quete = self.taverne.proposer_quete()
        if self.force >= quete["difficulte"]:
            self.quetes_reussies += 1
            return "Victoire !"
        return "Échec..."
