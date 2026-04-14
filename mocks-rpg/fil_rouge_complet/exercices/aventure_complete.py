# aventure_complete.py
# Système RPG complet du fil rouge — NE PAS MODIFIER.
#
# Architecture : le jeu complet repose sur 4 couches
#   1. ServicesExternes   — dés, BDD, notifications (toutes mockables)
#   2. Entités            — Heros, Monstre, Objet
#   3. MoteurJeu          — orchestre tout (la logique à tester)
#   4. JeuRPG             — point d'entrée (non testé directement)

from __future__ import annotations
import random
from dataclasses import dataclass, field
from typing import Protocol


# ══════════════════════════════════════════════════════════════════════════════
# COUCHE 1 — Protocoles (interfaces des services externes)
# ══════════════════════════════════════════════════════════════════════════════

class IDe(Protocol):
    def lancer(self, faces: int, nb: int = 1) -> list[int]: ...

class IBDD(Protocol):
    def charger(self, cle: str) -> dict | None: ...
    def sauvegarder(self, cle: str, data: dict) -> None: ...
    def existe(self, cle: str) -> bool: ...

class INotificateur(Protocol):
    def envoyer(self, message: str, niveau: str = "info") -> bool: ...

class IGenerateurNom(Protocol):
    """Génère des noms de monstres aléatoires (service externe ou API)."""
    def generer(self, race: str) -> str: ...


# ══════════════════════════════════════════════════════════════════════════════
# COUCHE 2 — Entités
# ══════════════════════════════════════════════════════════════════════════════

@dataclass
class Heros:
    nom: str
    pv: int
    pv_max: int
    attaque: int
    defense: int
    experience: int = 0
    niveau: int = 1
    inventaire: list[str] = field(default_factory=list)

    @property
    def est_vivant(self) -> bool:
        return self.pv > 0

    def soigner(self, montant: int) -> None:
        self.pv = min(self.pv + montant, self.pv_max)


@dataclass
class Monstre:
    nom: str
    race: str
    pv: int
    attaque: int
    defense: int
    butin_xp: int
    butin_or: int = 0

    @property
    def est_vivant(self) -> bool:
        return self.pv > 0

    def subir_degats(self, degats: int) -> None:
        self.pv = max(0, self.pv - degats)


@dataclass
class Objet:
    nom: str
    type: str          # "potion", "arme", "armure"
    valeur: int        # effet numérique (PV soignés, bonus attaque…)


# ══════════════════════════════════════════════════════════════════════════════
# COUCHE 3 — MoteurJeu (logique principale)
# ══════════════════════════════════════════════════════════════════════════════

class MoteurJeu:
    """
    Orchestre toutes les mécaniques du jeu.
    Toutes les dépendances sont injectées → 100 % testable avec mocks.
    """

    XP_PAR_NIVEAU = {1: 0, 2: 100, 3: 250, 4: 500, 5: 900}

    def __init__(
        self,
        de: IDe,
        bdd: IBDD,
        notificateur: INotificateur,
        generateur_nom: IGenerateurNom,
    ):
        self.de = de
        self.bdd = bdd
        self.notificateur = notificateur
        self.generateur_nom = generateur_nom

    # ── Gestion du héros ─────────────────────────────────────────────────────

    def creer_heros(self, nom: str, classe: str) -> Heros:
        """
        Crée un héros selon sa classe et le sauvegarde en BDD.
        Lève ValueError si le héros existe déjà.
        Classes disponibles : "guerrier", "mage", "rôdeur"
        """
        if self.bdd.existe(nom):
            raise ValueError(f"Un héros nommé '{nom}' existe déjà.")

        stats_par_classe = {
            "guerrier": {"pv": 40, "attaque": 8, "defense": 12},
            "mage":     {"pv": 20, "attaque": 14, "defense": 5},
            "rôdeur":   {"pv": 30, "attaque": 10, "defense": 8},
        }
        if classe not in stats_par_classe:
            raise ValueError(f"Classe inconnue : '{classe}'")

        stats = stats_par_classe[classe]
        heros = Heros(
            nom=nom, pv=stats["pv"], pv_max=stats["pv"],
            attaque=stats["attaque"], defense=stats["defense"],
        )
        self.bdd.sauvegarder(nom, self._heros_vers_dict(heros))
        self.notificateur.envoyer(f"Bienvenue, {nom} le {classe} !", niveau="success")
        return heros

    def charger_heros(self, nom: str) -> Heros:
        """Charge un héros depuis la BDD. Lève KeyError si introuvable."""
        data = self.bdd.charger(nom)
        if data is None:
            raise KeyError(f"Héros '{nom}' introuvable.")
        return Heros(**data)

    def sauvegarder_heros(self, heros: Heros) -> None:
        self.bdd.sauvegarder(heros.nom, self._heros_vers_dict(heros))

    def _heros_vers_dict(self, heros: Heros) -> dict:
        return {
            "nom": heros.nom, "pv": heros.pv, "pv_max": heros.pv_max,
            "attaque": heros.attaque, "defense": heros.defense,
            "experience": heros.experience, "niveau": heros.niveau,
            "inventaire": heros.inventaire,
        }

    # ── Combat ───────────────────────────────────────────────────────────────

    def generer_monstre(self, race: str, niveau_donjon: int) -> Monstre:
        """
        Génère un monstre dont les stats sont adaptées au niveau du donjon.
        Utilise IGenerateurNom pour obtenir un nom unique.
        """
        nom = self.generateur_nom.generer(race)
        pv = 10 + niveau_donjon * 5
        attaque = 3 + niveau_donjon * 2
        defense = 2 + niveau_donjon
        xp = 20 * niveau_donjon
        or_ = self.de.lancer(faces=6, nb=1)[0] * niveau_donjon
        return Monstre(nom=nom, race=race, pv=pv, attaque=attaque,
                       defense=defense, butin_xp=xp, butin_or=or_)

    def attaque_heros(self, heros: Heros, monstre: Monstre) -> dict:
        """
        Attaque d'un héros sur un monstre.
        Jet d'attaque : 1d20 + attaque héros.
        Touche si jet_total > defense monstre.
        Dégâts si touché : 1d8 + attaque héros.
        Retourne {"touche": bool, "degats": int}.
        """
        jet = self.de.lancer(faces=20, nb=1)[0] + heros.attaque
        if jet <= monstre.defense:
            return {"touche": False, "degats": 0}
        degats = self.de.lancer(faces=8, nb=1)[0] + heros.attaque
        monstre.subir_degats(degats)
        return {"touche": True, "degats": degats}

    def attaque_monstre(self, monstre: Monstre, heros: Heros) -> dict:
        """
        Attaque d'un monstre sur le héros.
        Jet : 1d20 + attaque monstre vs defense héros.
        Dégâts : 1d6 + attaque monstre.
        """
        jet = self.de.lancer(faces=20, nb=1)[0] + monstre.attaque
        if jet <= heros.defense:
            return {"touche": False, "degats": 0}
        degats = self.de.lancer(faces=6, nb=1)[0] + monstre.attaque
        heros.pv -= degats
        return {"touche": True, "degats": degats}

    def resoudre_combat(self, heros: Heros, monstre: Monstre) -> str:
        """
        Boucle de combat jusqu'à mort d'un des deux combattants.
        Retourne "victoire" ou "defaite".
        """
        tour = 0
        while heros.est_vivant and monstre.est_vivant:
            tour += 1
            att_h = self.attaque_heros(heros, monstre)
            if att_h["touche"]:
                self.notificateur.envoyer(
                    f"Tour {tour} — {heros.nom} inflige {att_h['degats']} dégâts."
                )
            if not monstre.est_vivant:
                break
            att_m = self.attaque_monstre(monstre, heros)
            if att_m["touche"]:
                self.notificateur.envoyer(
                    f"Tour {tour} — {monstre.nom} inflige {att_m['degats']} dégâts.",
                    niveau="warning",
                )

        if heros.est_vivant:
            heros.experience += monstre.butin_xp
            self._verifier_montee_niveau(heros)
            self.sauvegarder_heros(heros)
            self.notificateur.envoyer(
                f"Victoire ! {heros.nom} gagne {monstre.butin_xp} XP.",
                niveau="success",
            )
            return "victoire"

        self.sauvegarder_heros(heros)
        self.notificateur.envoyer(
            f"{heros.nom} a été vaincu par {monstre.nom}.",
            niveau="error",
        )
        return "defaite"

    # ── Inventaire & objets ───────────────────────────────────────────────────

    def utiliser_objet(self, heros: Heros, objet: Objet) -> str:
        """
        Utilise un objet de l'inventaire du héros.
        - "potion" → soigne valeur PV
        - "arme"   → augmente attaque de valeur (permanent)
        - Objet inconnu → lève ValueError
        Sauvegarde le héros après usage.
        Retourne une description de l'effet.
        """
        if objet.type == "potion":
            avant = heros.pv
            heros.soigner(objet.valeur)
            soigne = heros.pv - avant
            self.sauvegarder_heros(heros)
            self.notificateur.envoyer(f"{heros.nom} récupère {soigne} PV.")
            return f"+{soigne} PV"
        elif objet.type == "arme":
            heros.attaque += objet.valeur
            self.sauvegarder_heros(heros)
            self.notificateur.envoyer(
                f"{heros.nom} équipe {objet.nom} (+{objet.valeur} ATT)."
            )
            return f"+{objet.valeur} ATT"
        else:
            raise ValueError(f"Type d'objet inconnu : '{objet.type}'")

    # ── Progression ───────────────────────────────────────────────────────────

    def _verifier_montee_niveau(self, heros: Heros) -> bool:
        """Vérifie et applique la montée de niveau si XP suffisant."""
        prochain = heros.niveau + 1
        if prochain not in self.XP_PAR_NIVEAU:
            return False
        if heros.experience >= self.XP_PAR_NIVEAU[prochain]:
            heros.niveau = prochain
            heros.pv_max += 10
            heros.soigner(10)
            self.notificateur.envoyer(
                f"{heros.nom} passe au niveau {prochain} !",
                niveau="success",
            )
            return True
        return False


# ══════════════════════════════════════════════════════════════════════════════
# COUCHE 4 — JeuRPG (point d'entrée — pas testé directement)
# ══════════════════════════════════════════════════════════════════════════════

class DeReelle:
    def lancer(self, faces: int, nb: int = 1) -> list[int]:
        return [random.randint(1, faces) for _ in range(nb)]

class BDDMemoire:
    def __init__(self): self._data = {}
    def charger(self, cle): return self._data.get(cle)
    def sauvegarder(self, cle, data): self._data[cle] = data
    def existe(self, cle): return cle in self._data

class NotificateurConsole:
    def envoyer(self, message, niveau="info"):
        print(f"[{niveau.upper()}] {message}")
        return True

class GenerateurNomAleatoire:
    NOMS = {"gobelin": ["Grix", "Skab", "Nox"], "troll": ["Grug", "Boro"]}
    def generer(self, race):
        noms = self.NOMS.get(race, ["Inconnu"])
        return random.choice(noms)
