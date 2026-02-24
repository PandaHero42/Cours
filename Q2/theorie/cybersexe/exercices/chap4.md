### 4.2.1 - Quels protocoles de routage sont supportés par un FortiGate ?

- RIP
- OSPF

___

### 4.2.2 - Qu’est-ce que la « policy routing table » ? Que contient-elle ?

- Routing table en fonction d'une police, spéciale utilisée pour le PBR (Policy-Based Routing)
- Permet de router selon : critères avancés de routage (services, priorités, users, interface d'entrée, adresse source et destination)
- Contrairement au routage classique basé uniquement sur la destination.
- Elle contient : 
  - règles de routage spécifiques
  - interface de sortie
  - gateway
  - priorité
- La policy routing est évaluée avant la table de routage classique.

___

### 4.2.3 - Expliquez l’acronyme ECMP. Dans quelles conditions l’ECMP est-il utilisé ?

- **ECMP** : Equal-Cost Multi-Path
  - C'est un mécanisme permettant d'utiliser plusieurs routes ayant le même coût (métrique) vers une même destination.
  - *Utilisé lorsque :*
    - Plusieurs routes vers la même destination
    - Même distance administrative
    - Même métrique
    - Même priorité

___

### 4.2.4 - Citez et expliquez les différentes méthodes de balancement de charge ECMP

Fortigate propose plusieurs algorithmes ECMP :

- 1. **Source IP based**
  - Basé sur l'adresse IP source
  - Même IP source -> même lien
  - Permet cohérence des sessions
- 2. **Source-Destination IP based**
  - Basé sur combinaison source + destination
  - Plus précis, meilleure répartition
- 3. **Weighted load balancing**
  - Permet d'attribuer un poids différent à chaque lien
    - Exemple :
      - WAN1 = 70%
      - WAN2 = 30%
- 4. **Spillover**
  - Utilise un lien principal jusqu'à saturation
  - Puis bascule sur le second 
- 5. **Usage-based**
  - Basé sur la bande passante utilisée

___

### 4.2.5 - Quelle est l’utilité de la fonction RPF (Reverse Path Forwarding Check) ?

- **RPF** : Reverse Path Forwarding
  - Mécanisme de sécurité permettant de vérifier : 
    - "Si je reçois un paquet par cette interface, est-ce que j'aurais utilisé cette même interface pour répondre ?"
    - **Objectif** :
      - Éviter le spoofing IP
      - Bloquer le trafic avec IP source falsifiée
      - Sécuriser contre attaques DoS
    - Si la route retour n'existe pas -> paquet rejeté.
___

### 4.2.6 - Citez les modes de fonctionnement de RPF ? Pouvez-vous les expliquer ? 

**Il existe 2 modes principaux :**

- 1. **Strict RPF**
  - Le paquet est accepté uniquement si : 
    - La route de retour utilise exactement la même interface.
  - Sinon, rejet.
  - => Très sécurisé
  - => Peut poser problème en environnement multi-WAN asymétrique.
- 2. **Loose RPF**
  - Le paquet est accepté si :
    - Une route vers l'adresse source existe dans la table de routage
    - Peu importe l'interface
  - => Plus flexible
  - => Adapté multi-WAN / ECMP


