# Méthodologie de projet
Agile regroupe : 
- Scrum
- XP
- Lean Software Dev
- DevOps


## Triangle de fer
- Délais : Deadline
- Livrable : Produit fini
- Ressources :
    - Ressources Humaines
    - Argent

Une équilibre des 3, sinon on switch vers qqch.

## Modèles 
### Waterfall
Modèle en casqcade, une équipe fais une partie du produit, puis autre équipe pour une autre partie, etc. Chaque équipe a sa spécialité. (CdC -> Produit fini) mais en gros partie par partie.

### Itératif ou incrémentiel
    - Incrémentiel : Par partie de produit fonctionnel.
    - Itératif : Répéter les choses, construire le produit petit à petit.


### Différences
#### Waterfall
Livrable qui reste le même (contrainte), mais si on augmente les délais alors les ressources aussi. Donc triangle de fer important.

#### Agile
Alors là ce sont les délais et les ressources qui sont les contraites, donc le livrable dépendera de cet élément. Délais définis, ressources définies, ne pouvant pas être incrémentée.

### Comment choisir ?
Pas vraiment de meilleurs méthode, juste il faut choisir selon le contexte, mais en informatique généralement on bosse en Agile, mais en réseau c'est un peu + en waterfall.


## Waterfall - Planning
Un retro-planning est utilisé, c'est partir de la date de fin, et faire un planning des tâches.
Cycle en V, en rajoutant des tests régulierement, pour éviter un cout de changement trop élévé.

## Agile
4 valeurs importantes, et 12 principes.
### Valeurs
- Priorité aux individus et aux intérraction
- Client au centre de la démarche, c'est lui qui dicte exactement ce qu'il veut.
- Des produits opérationnels obligatoire.
- Adapation aux changements.

### Principes
- Satisfaire le client, c'est pour lui qu'on travaille, c'est lui qui a eu l'idée
- Accueillir positivement les changements. Pas de faire le changement, juste accueillir, et lui faire savoir que à quel point c'est impactant, etc...
- Livrez fréquemment il faut mettre sur le marché le plus vite possible comme ça, il peux réinjecter dans le produit. 
- Les équipes doivent travailler ensemble.
- Réalisez des projets avec des personnes motivées. (Se tirer vers le haut)
- Parlez en face à face. (Car moins de place à l'interpretation disfonctionnel)
- Produit fonctionnel (Sinon il va pas pouvoir le mettre en production)
- Travaillez à rythme constant
- Excellence technique, et bon design
- Simplicité, jamais trop cherché, la simplicité prime. 
- Equipes auto-organisées.
- S'adapter régulierement


## Scrum
Méthode agile.

### Vue générale
- Sprint : C'est le moment ou on travaille sur le produit, on travaille sur une partie de produit (Incrément) doit être fonctionnel à la sortie du sprint.
- Sprint Planning : On définit ce qu'on va retoruver dans la partie de produit (incrément). Définit à partir du product backlog = CdC ségmenté en partie, en fonction de ce qui est important, etc... Discussion avec le client, on pose des questions, etc. On prend des sprint backlog (des fonctionnalités venant du product backlog). Bien comprendre les besoin.
- Sprint review : Présentation de la partie de produit (incrément)
- Sprint backlog : petit CdC d'un sprint
- Daily Scrum : Réunion journalière, pour voir si ça avance bien etc, si y'a besoin d'aide.
- Retrospective : Ce qui s'est bien/pas bien passé pendant le sprint, comment améliorer les choses.

### Scrum Team
- Product Owner : Client (faisant partie de l'équipe)
- Scrum Master : Gestionnaire de projet, il facilite, car il connait la méthode, plus grande communications que les autres, etc...Aussi développeur
- Les devs


### Scrum events
- Sprint : 
    - Durée : 4 Semaines
    - Qui ? Devs + Scrum Master
    - Quoi ? On bosse sur le sujet
- Sprint Planning : 
    - Durée : 8h
    - Qui ? Product Owner + Scrum Master + Dev
    - QUoi ? Définit ce qu'on va faire pendant un sprint
- Daily Scrum : 
    - Durée : 15min/jour
    - Qui ? Scrum Master + Dev
    - Quoi ? 
        - Qu'est-ce qui a été fait hier ?
        - Quel est le plan de la journée
        - Obstacles ?
- Sprint Review
    - Durée : 4h
    - Qui ? Product Owner + Scrum Master + Dev (+ parties prenantes)
    - Quoi ? Présentation de ce qui a été fait pendant le sprint (incrément).
- Sprint rétrospective : 
    - Durée : 3h
    - Qui ? SM + dev
    - Quoi ? On se remet en question du dernier Sprint


### Scrum Artefacts
- Product Backlog : = CdC, besoins globaux
- Sprint Backlog : Taches à faire pendant le sprint
- Incrément : Une partie du produit fini.

### Scrum Board
|TODO | IN PROGRESS | TEST | DONE |
|-|-|-|-|
|Tache à faire|Tache entrain d'etre bossée|Tache en test|Tache finie|

On met des story points via  planning poker.

DoD = Définition of Done, définit exactement quand une tache est finie. (Checklist)


### User Story
Pour écrire le product backlog, qui sont des fonctionnalités du produit client. Mais on veut que ça soit simple donc on utilise les mots du client. Aussi y mettre l'avantage de la fonctionnalité, pour y determiner la priorité.
C'est une base de discussion, discuter sur les taches, etc.

En tant que
Je veux que
pour que

### Planning Poker
Méthode des story points. Ce sont des points attribué à des taches/user story. Et on determine ça tous en semble.

Planning poker est une méthodo pour attribuer ces story point. 

Sprint Planning, le scrum master demande si y'a toute les informations sur une user story. On va eviter d'influencer les autres. Chacun choisit une carte. 

On demande aux plus bas, et aux plus haut pourquoi ils ont mis ça? Ensuite on refais, puis on fait la moyenne des cartes tirées.

vélocité = l'addition des storypoints de chaque tache en fin de journée. 


## Design Thinking
C'est complémentaire au SCRUM, mais chronologiquement avant d'appliquer du SCRUM.

Définit la viabilité du projet.

### Etapes
#### Empathie
Comprendre les users, les besoins, et émotions. Se mettre à la place du client/user final. 
#### Définition
Définir son besoin, reformuler le problème pour donner une direction claire
#### Idéation
Trouver des solution, générer des idées lié au problème. Donner toute les idées.Filtrer ces idées.
#### Prototypage
Transformer les idées en prototypes tangibles.
#### Test
Tester le prototype, et recueillir des feedback. Tester par rapport à la problèmatique.En fonction des feedbacks on fait l'itération ou pas.



# Serious Game

Groupe 1 : Composé de Matteo, Kelian, Cyril, Alexandre s'occupe de la zone 1 et 3

Groupe 2 : Nicola, Aaron, Kelyan, Nathan Zone 2 et 4. 

## Empathie
Questions à se poser : 
- Quels sont les besoins prioritaires pour chaque persona
- Quelles sont les frustrations majeures à éviter dans la conception de la ville.



Zone 2 Commerciale et affaire: 
- Besoin de parkins
- Besoin de transports
- Manque de modernité
- Manque d'espace vert


Zone 4 infra et TEC: Transports en commun. Segmenté en zone : 
- Transports en commun -> Ecologie
- Trajet plus court pour la maman
- Environnement pas safe
- Peu d'accessibilité


## Définition

## User Stories
Zone Infra (4) :

En tant que maire, je veux des transports publics écologique pour réduire la circulation automobile et la pollution

En tant que maman, je veux des transports sécurisé me permettant de me deplacer rapidemment.

En tant qu'entrepreuneur, je veux que ça circule bien dans chaque zone 

Zone commerrcial (2) :
En tant que entrepreneur, je veux une accessibilité/facilité à venir dans la zone commerciale.

En tant que maire, je veux des espaces verts pour ma zone commerciale

En tant que entrepreneur, je veux un endroit moderne et accueillant pour les clients. 

