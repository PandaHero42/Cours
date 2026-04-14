# rpg_boss.py
# Architecture complète du mini-RPG — NE PAS MODIFIER ce fichier.

from __future__ import annotations
from dataclasses import dataclass, field
from typing import Protocol


# ── Protocoles (interfaces) ──────────────────────────────────────────────────

class IDe(Protocol):
    """Interface d'un service de dés."""
    def lancer(self, faces: int, nb: int = 1) -> list[int]: ...


class IBaseDeDonnees(Protocol):
    """Interface d'une base de données de jeu."""
    def charger(self, cle: str) -> dict | None: ...
    def sauvegarder(self, cle: str, valeur: dict) -> None: ...


class INotificateur(Protocol):
    """
    Interface d'un service de notification (logs, alertes, emails...).
    En prod : envoie des messages à un serveur externe.
    """
    def envoyer(self, message: str, niveau: str = "info") -> bool: ...


# ── Entités ──────────────────────────────────────────────────────────────────

@dataclass
class StatsBoss:
    nom: str
    pv_max: int
    pv: int
    attaque: int
    defense: int
    phases: list[str] = field(default_factory=list)
    phase_actuelle: int = 0

    @property
    def est_vivant(self) -> bool:
        return self.pv > 0

    @property
    def phase_courante(self) -> str:
        if not self.phases:
            return "normale"
        return self.phases[min(self.phase_actuelle, len(self.phases) - 1)]

    def passer_phase_suivante(self) -> None:
        if self.phase_actuelle < len(self.phases) - 1:
            self.phase_actuelle += 1


@dataclass
class StatsHeros:
    nom: str
    pv: int
    attaque: int
    defense: int
    experience: int = 0
    niveau: int = 1


# ── Logique métier ───────────────────────────────────────────────────────────

class MoteurCombatBoss:
    """
    Moteur de combat contre un boss à plusieurs phases.

    Règles :
      - Le héros attaque en premier chaque tour.
      - Jet d'attaque héros : 1d20 + attaque héros vs defense boss
        → touche si jet_total > defense boss
      - Dégâts si touché : 1d8 + attaque héros
      - Changement de phase boss : quand les PV du boss passent sous 50 %
      - Le boss contre-attaque chaque tour où il est vivant :
        jet d20 + attaque boss vs defense héros → touche si jet > defense
        Dégâts boss : 1d6 (doublés en phase "enragé")
      - Fin : boss mort → héros gagne XP = pv_max boss
               héros mort → défaite
    """

    def __init__(
        self,
        de: IDe,
        bdd: IBaseDeDonnees,
        notificateur: INotificateur,
    ):
        self.de = de
        self.bdd = bdd
        self.notificateur = notificateur

    def jouer_tour(self, heros: StatsHeros, boss: StatsBoss) -> dict:
        """
        Joue un tour complet : attaque héros, puis contre-attaque boss.
        Retourne un résumé du tour.
        """
        resume = {
            "heros_attaque": False,
            "degats_heros": 0,
            "boss_attaque": False,
            "degats_boss": 0,
            "boss_change_phase": False,
            "boss_vivant": boss.est_vivant,
            "heros_vivant": heros.pv > 0,
        }

        if not boss.est_vivant or heros.pv <= 0:
            return resume

        # ── Attaque du héros ──────────────────────────────────────────────
        jet_attaque_h = self.de.lancer(faces=20, nb=1)[0] + heros.attaque
        if jet_attaque_h > boss.defense:
            degats = self.de.lancer(faces=8, nb=1)[0] + heros.attaque
            boss.pv -= degats
            resume["heros_attaque"] = True
            resume["degats_heros"] = degats
            self.notificateur.envoyer(
                f"{heros.nom} inflige {degats} dégâts à {boss.nom}."
            )

            # Changement de phase
            if boss.pv <= boss.pv_max // 2 and boss.phase_actuelle == 0:
                boss.passer_phase_suivante()
                resume["boss_change_phase"] = True
                self.notificateur.envoyer(
                    f"{boss.nom} passe en phase '{boss.phase_courante}' !",
                    niveau="warning",
                )

        # ── Contre-attaque du boss ────────────────────────────────────────
        if boss.est_vivant:
            jet_attaque_b = self.de.lancer(faces=20, nb=1)[0] + boss.attaque
            if jet_attaque_b > heros.defense:
                degats_b = self.de.lancer(faces=6, nb=1)[0]
                if boss.phase_courante == "enragé":
                    degats_b *= 2
                heros.pv -= degats_b
                resume["boss_attaque"] = True
                resume["degats_boss"] = degats_b
                self.notificateur.envoyer(
                    f"{boss.nom} inflige {degats_b} dégâts à {heros.nom}.",
                    niveau="warning",
                )

        resume["boss_vivant"] = boss.est_vivant
        resume["heros_vivant"] = heros.pv > 0
        return resume

    def terminer_combat(self, heros: StatsHeros, boss: StatsBoss) -> str:
        """
        Appelée quand le combat se termine.
        Sauvegarde le héros en BDD, envoie une notification.
        Retourne "victoire" ou "defaite".
        """
        if not boss.est_vivant:
            heros.experience += boss.pv_max
            self.bdd.sauvegarder(
                heros.nom,
                {"pv": heros.pv, "experience": heros.experience, "niveau": heros.niveau},
            )
            self.notificateur.envoyer(
                f"VICTOIRE ! {heros.nom} a vaincu {boss.nom} !",
                niveau="success",
            )
            return "victoire"
        else:
            self.bdd.sauvegarder(
                heros.nom,
                {"pv": 0, "experience": heros.experience, "niveau": heros.niveau},
            )
            self.notificateur.envoyer(
                f"DÉFAITE. {heros.nom} a été vaincu par {boss.nom}.",
                niveau="error",
            )
            return "defaite"


class SystemeProgression:
    """
    Gère la montée en niveau des héros.
    Charge les stats depuis la BDD, calcule la progression.
    """

    XP_PAR_NIVEAU = {1: 0, 2: 100, 3: 300, 4: 600, 5: 1000}

    def __init__(self, bdd: IBaseDeDonnees, notificateur: INotificateur):
        self.bdd = bdd
        self.notificateur = notificateur

    def verifier_progression(self, nom: str) -> dict:
        """
        Charge le héros depuis la BDD.
        Si l'XP dépasse le seuil du niveau suivant → monte de niveau.
        Retourne {"niveau_actuel": int, "monte_niveau": bool}.
        """
        data = self.bdd.charger(nom)
        if data is None:
            raise ValueError(f"Héros '{nom}' introuvable en BDD.")

        niveau_actuel = data.get("niveau", 1)
        xp = data.get("experience", 0)
        prochain_niveau = niveau_actuel + 1

        if prochain_niveau not in self.XP_PAR_NIVEAU:
            return {"niveau_actuel": niveau_actuel, "monte_niveau": False}

        if xp >= self.XP_PAR_NIVEAU[prochain_niveau]:
            data["niveau"] = prochain_niveau
            self.bdd.sauvegarder(nom, data)
            self.notificateur.envoyer(
                f"{nom} passe au niveau {prochain_niveau} !",
                niveau="success",
            )
            return {"niveau_actuel": prochain_niveau, "monte_niveau": True}

        return {"niveau_actuel": niveau_actuel, "monte_niveau": False}
