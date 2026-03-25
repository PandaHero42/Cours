___
6.6.1 - Quels éléments de sécurité un VPN IPsec apporte-t-il ?

- **Confidentialité des données :** Chiffrement des données (AES, 3DES,...). Le trafic est transmis dans un tunnel IPsec peut être chiffré.
- **Intégrité des données :** vérification que les données n'ont pas été altérées (HMAC-SHA...). IPsec utilise des algorithmes de hachage permettant de vérifier l'intégrité des données.
- **L'authentification des machines aux extrémités :** vérification de l'identité des pairs (PSK, certificats). Les utilisateurs, eux, ne sont pas authentifiés par IPsec.
- **Anti-rejeu :** numérotation des paquets pour éviter la réutilisation de paquets capturés.
  - Le rejeu consiste à capturer un ou plusieurs paquets dans le but de les envoyer à nouveau.
  - Le rejeu peut permettre à l'attaquant de bénéficier des mêmes avantages que l'envoyeur initial.
  - Il n'est pas nécessaire à l'attaquant d'avoir déchiffré les paquets pour les réenvoyer.
___

6.6.2 - Pourquoi l’utilisation du protocole IPsec ESP n’est pas compatible avec l’utilisation de traduction de port (PAT)?

- ESP chiffre et encapsule tout le payload, y compris les en-têtes TCP/UDP. Le PAT (Port Address Translation) a besoin de lire/modifier les numéros de port source pour maintenir sa table de translation — ce qui est impossible si ces ports sont chiffrés et intégrés dans le payload ESP.
- Avec AH, les champs adresse source et adresse destination ne peuvent pas être modifiées (KHMAC).
- Une encapsulation NAT-T permet cependant de traverser un équipement qui fait de la NAPT.
___

6.6.3 - Expliquez la notion de NAT-T (NAT-Traversal).

- Solution qui encapsule les paquets ESP dans des datagrammes UDP (port 4500). Cela permet au trafic IPsec de traverser un équipement NAT/PAT, car UDP est translatable normalement par le NAT. Les deux pairs détectent la présence d'un NAT via IKE et activent automatiquement NAT-T.
___

6.6.4 - Expliquez la fonction de l’Algorithme Diffie-Hellman.

- Protocole d'échange de clé qui permet à deux parties de se mettre d'accord sur un secret partagé via un canal non sécurisé, sans jamais s'envoyer la clé elle-même. Basé sur des opérations mathématiques à sens unique (exponentiation modulaire ou courbes elliptiques). Ce secret sert ensuite à dériver les clés de chiffrement.

___

6.6.5 - Expliquez la notion de groupe Diffie-Hellman.

Définit la taille et le type des paramètres mathématiques utilisés dans l'échange DH, donc le niveau de sécurité :

| Groupe | Type | Taille |
|--------|------|--------|
| 1 | Modulaire | 768 bits (obsolète) |
| 2 | Modulaire | 1024 bits (déprécié) |
| 14 | Modulaire | 2048 bits |
| 19/20 | Courbes elliptiques | 256/384 bits |

Plus le groupe est élevé, plus l'échange est sécurisé (et coûteux en calcul).

___

6.6.6 - Expliquez la fonction du protocole IKE.

- IKE est le protocole de négociation et gestion des clés pour IPsec. Il automatise :

L'authentification des deux pairs
La négociation des algorithmes (chiffrement, intégrité, DH)
L'échange de clés Diffie-Hellman
L'établissement des Security Associations (SA)

___

6.6.7 - Quel est le rôle de chacune des phases IKE ? Quel N° de port est utilisé par IKE?

- Port : UDP 500 (UDP 4500 si NAT-T actif)

| Phase | Rôle |
|-------|------|
| Phase 1 | Établit un canal sécurisé et authentifié entre les pairs (IKE SA / ISAKMP SA). Mode *Main* (6 messages) ou *Aggressive* (3 messages). |
| Phase 2 | Négocie les SA IPsec (ESP/AH) qui protégeront le trafic réel. Mode *Quick Mode*. |

___

6.6.8 - Expliquez ce qu’est une SA (Security Association).

- Une SA est un ensemble de paramètres convenus entre deux pairs pour protéger une communication :

Algorithme de chiffrement et clé associée
Algorithme d'intégrité
Durée de vie
Chaque SA est unidirectionnelle → un tunnel bidirectionnel nécessite 2 SA. Les SA sont identifiées par un triplet : ``(SPI, adresse destination, protocole).``
___
6.6.9 - Expliquez la notion de Perfect Forward Secrecy.

- Propriété garantissant que la compromission d'une clé à long terme ne compromet pas les clés de session passées. En pratique, PFS impose un nouvel échange Diffie-Hellman à chaque renouvellement de SA (phase 2), de sorte que chaque clé de session est indépendante. Si une clé est découverte, seule la session correspondante est compromise, pas les sessions précédentes ou futures.
___



