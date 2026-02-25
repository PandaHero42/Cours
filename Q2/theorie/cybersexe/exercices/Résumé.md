# Réponse aux questions cybersécurité 

## 01 Introduction à l'UTM Fortigate
- Dessinez une architecture réseau simple telle que :
    - Sans DMZ et protégée par un pare-feu périmétrique et un proxy web transparent.
        ![alt text](image-1.png)

    - Avec DMZ et protégée par un pare-feu périmétrique, un proxy web explicite et un reverse proxy.
        ![alt text](image.png)

- Citez trois avantages liés à l’utilisation d’un proxy Web.
    - Capable d'analyser le trafic au niveau de la couche application
        - Offre un contrôle précis du trafic.
        - Permet de détecter des attaques plus sophistiquées comme un buffer overflow ou une injections SQL.
	    - Peut inclure une authentification des utilisateurs.
    - Améliore la protection des hôtes
	    - Masque les adresses des machines clientes
	    - C'est le proxy qui se connecte à des machines externes au réseau, il est donc plus difficile de mettre en place une attaque contre les hôtes internes du réseau.
    - Performances
	    - Amélioration possible des performances grâce à la mise en cache.
    - Journalisation très détaillée

- Citez trois limites/inconvénients liés à l’utilisation d’un proxy Web.
	- Consommation de ressources
		- Nécessite plus de ressources mémoire, processeur et disque qu'un filtrage sur les couches basses du modèle OSI.
	- Toutes les applications ne sont pas supportées 
		- Peut nécessiter un serveur proxy différent par application ou se limiter à un filtrage générique. 
	- Peut nécessiter l'installation d'un logiciel client sur les hôtes internes 
		- S'il n'y a pas besoin de configuration ou d'un logiciel sur le périphérique client, on parle de proxy transparent. 
	- Constitue potentiellement un point unique de défaillance (SPOF)

- Expliquez la notion de pare-feu avec état (statefull firewall).
	- Filtrage du trafic sur base des informations d'en-tête de couches 2 à 4. 
	- Capable de surveiller l'état des connexions.

- Citez les deux modes de fonctionnement (Modes of Operation) d’un FortiGate. Quel est le plus couramment utilisé ?
	- NAT/route
	- transparent 

-  Citez 5 fonctionnalités de sécurité supportée par un FortiGate/NGFW.
	- ==?== 

- Comparez les profils d’administrateur super_admin et prof_admin.
	-  super_admin 
		- Il a tous les droits, par défaut ce profil est utilisé par le compte admin. 
		- Ce profil ne peut pas être modifié ou supprimé.
	- prof_admin
		- Par défaut, il a tous les droits mais uniquement sur son VDOM. 
		- Pas d’accès aux paramètres globaux


## 02 Règles de pare-feu

- Que peut-on/doit-on utiliser dans le champ « source » d’une règle de pare-feu ?
	- Une adresse ou un ensemble d’adresses IP. 
	- Un réseau ou sous-réseau. 
	- Un FQDN. 
	- Une zone géographique. 
	- L’adresse d’un Fabric connector. 
	- Un objet de la base de données ”Internet service
	- utilisateur ou groupe
	- periphérique source

- Que peut-on utiliser dans le champ « Destination » d’une règle de pare-feu ?
	- Une adresse ou un ensemble d’adresses IP. 
	- Un réseau ou sous-réseau. 
	- Un FQDN. 
	- Une zone géographique. 
	- L’adresse d’un Fabric connector. 
	- Un objet de la base de données ”Internet service

- Que peut-on utiliser dans le champ « Service » d’une règle de pare-feu ? 
	- Base de données
		- Elle contient une liste d’adresse IP, de protocoles et de numéros de port utilisés par les servies Internet les plus courants
	- Protocole et N° de port
		- L'UTM vérifie le protocole (TCP, UDP, …) ainsi que les N° de port. 
		- De nombreux objets sont prédéfinis et peuvent être modifiés, d'autres peuvent être créés.

- Qu’est-ce qu’un objet de pare-feu ? Quels avantages présentent ils?
	- un regroupement d'éléments de configuration

- Qu’est-ce qu’un objet ISDB ?  
	- table avec port/ip des services les plus utilisés sur le web

- Dans quel ordre sont traitées les règles de pare-feu ?
	- Ordre des numéros de séquences
	
- A quoi correspondent le numéro de règle et le numéro de séquence d’une règle de pare-feu ?
	- à donner l'ordre dans lequel les règles sont traités

- Citez quatre types de règles de pare-feu.
	- IPv4 policy
	- IPv6 policy
	- Multicast policy
	- Local in policy

- Comment peut-on appliquer un profil de sécurité à du trafic traversant le pare-feu ?
	- Un profil de sécurité est un groupe d'options et de filtres que l'on peut appliquer à une règle de pare-feu (appliqué en les cochant)

- Que signifie la notion de pare-feu à états (statefull firewall) ?
	- Une fois établie il laisse passer 

- Expliquez les deux règles de l’image ci-dessous.
	![[Pasted image 20240529110906.png]]


## 03 NAT 

- Citez trois avantages et trois inconvénients liés à l’utilisation de la traduction d’adresses réseau.
	- Assure la cohérence des schémas d'adressage du réseau interne. 
	- Permet d'économiser les adresses publiques. 
	- Améliore la sécurité en empêchant de connaître les adresses utilisées en interne
	
- Citez deux méthodes de configuration de la NAT sur un FortiGate. Dans quel cas est-il plus intéressant d’utiliser une méthode plutôt que l’autre ?
	- Firewall Policy NAT mode
		- Petits réseaux
	- Central NAT mode
		- Utile dans les réseaux plus complexes avec de nombreuses règles de pare-feu

- Citez les deux manières de configurer de la SNAT
	- SNAT en utilisant l'interface de sortie
	- SNAT en utilisant un pool IP

- Citez les différents types de pools IP utilisables pour faire de la SNAT
	- IP pool type : Overload
	- IP pool type : One-to-one
	- IP pool type : Fixed port range
	- IP pool type : Port block allocation

- A quoi sert un objet VIP (Virtual IP) ?
	- Permet de mapper une adresse IP externe à une adresse IP interne (trafic entrant, généralement vers un serveur interne).

- Expliquez la notion de « port forwarding ».
	- Avec le Port Forwarding, vous pouvez réutiliser la même adresse externe et la mapper à différentes adresses et ports internes (One-to-one mapping désactivé)

- Dans l’exemple suivant, à quelle(s) condition(s) l’objet destination « ALL » va-t-il matcher avec l’adresse définie dans une VIP ?
	- Attention : les VIP et les objets « adresse » de pare-feu sont des objets différents. 
	- Par défaut, l'objet adresse "ALL" d'une règle de pare-feu n'inclut pas les VIP.
	![[Pasted image 20240529111732.png]]

- Si le menu Central NAT n’est pas visible sur le bandeau de gauche de l’écran de configuration, que devez vous faire pour qu’il apparaisse ?  
	![[Pasted image 20240529112527.png]]
    
- Comment FortiOS choisit-il la règle Central NAT à appliquer ?
	-  ==?==


## 04 Routage 

- Quels protocoles de routage sont supportés par un FortiGate ?
	- RIP
	- OSPF
	- IS-IS
	- BGP

- Expliquez ce qu’est la base de données ”Internet service” (ISDB).
	- Base de données régulièrement mise à jour par les services FortiGuard
		- Internet services est une DB qui contient une liste d'adresses IP, de protocoles IP et de numéros de port utilisés par les services Internet les plus courants.
	- Routage du trafic
		- Permet de router les paquets (de sélectionner l’interface de sortie), en fonction du services Internet de destination.

- Comment le FortiGate gère-t-il le trafic qui matche avec une route statique utilisant un objet ISDB comme destination ?
	- Ces routes ne sont pas ajoutées à la table de routage mais à la policy routing table

- Expliquez l’acronyme ECMP. Dans quelles conditions l’ECMP est-il utilisé ?
	- Equal Cost Multi-path 
		-  Même réseau de destination 
		- Même distance (administrative) 
		- Même métrique 
		- Même priorité (si ce sont des routes statiques)

- Citez et expliquez le principe des différentes méthodes de balancement de charge ECMP
	- Source IP (default)
		- Les sessions d'une même adresse IP source utilisent la même route.
	- Source-destination IP
		- Les sessions avec la même paire IP source + IP destination utilisent la même route.
	- Weighted
		- Les sessions sont distribuées en fonction du poids des interfaces ou des routes. 
		- Route A de poids 5 (5/8 du trafic), route B de poids 3 (3/8 du trafic) (8 =5+3).
	- Usage (Spillover)
		- Méthode basée sur l'utilisation d'une route. 
		- La même route est utilisée jusqu' à ce que la bande passante de l'interface atteigne la limite de débordement configurée..

- Quelle est l’utilité de la fonction RPF (Reverse Path Forwarding Check) ?
	- Protection contre l'usurpation d'adresse IP
		- Permet au routeur de vérifier si une adresse source est réellement joignable
		- Si activé, le contrôle est exécuté sur le premier paquet de toute nouvelle session

- Quels sont les modes de fonctionnement de RPF ? Pouvez-vous les expliquez ?
	- Loose
		- Le paquet est accepté s’il y a une route active vers l'IP source via l'interface entrante
	- Strict
		- Le paquet est accepté s'il y a une route active vers l'IP source via l'interface entrante et si cette route est la meilleure route vers l'IP source

- Quelle est l’utilité du moniteur d'état de liaison (Link Health Monitor)?
	- Mécanisme permettant de détecter un routeur en panne le long d'une route. 
	- Utilisé, par exemple, lorsqu'il y a des routeurs redondants dans une infrastructure à doubles FAI et que l'ECMP n'est pas utilisé

- Quels protocoles peuvent être utilisés par le LHM ?
	- Ping
	- TCP/UDP
	- TWAMP
	- HTTP


## 05 Virtual Domains (VDOM)

- Expliquez ce qu'est un VDOM.  
	- Les VDOM sont une virtualisation au sein de FortiOS
		- Ils permettent de disposer de plusieurs pare-feux virtuels sur un équipement unique
	- Permet de subdiviser les stratégies de sécurité en plusieurs domaines
		- Chaque VDOM possède des politiques de sécurité et des tables de routage indépendantes
	- Permet d'attribuer des comptes administrateurs différents pour la gestion des différents domaines
    
- Citez les types de VDOM qu’il est possible de créer sur un FortiGate. 
	- Admin VDOM
	- Traffic VDOM
	
- Expliquez le rôle de chacun de ces types de VDOM.
	- Admin VDOM
		- Utilisé uniquement pour la gestion du pare-feu. 
		- Ne transfère aucun traffic d’une interface à une autre. 
		- Un seul admin VDOM possible.
	- Traffic VDOM
		- Utilisé pour traiter le traffic traversant le pare-feu.

- Citez 4 exemples de paramètres configurables par VDOM.
	- Mode de fonctionnement (transparent, NAT/route)
	- Mode d'inspection (flow/proxy)
	- Mode NGFW (profile/policy) 
	- Routes et interfaces réseau 
	- Règles de pare-feu 
	- Profils de sécurité

- Citez 4 exemples de paramètres globaux (ils sont communs aux différents VDOM).
	- Nom d'hôte 
	- Paramètres HA 
	- Paramètres FortiGuard 
	- Heure système 
	- Comptes administrateurs

- Quel est l’avantage d’utiliser des « Inter-VDOM links »?
	- Moins d'interfaces physiques et de câbles requis pour interconnecter des VDOM. 
	- Le trafic n'a pas besoin de quitter une interface physique puis d'entrer à nouveau dans le FortiGate

- Quelles commandes permettent de vérifier le routage des paquets au sein d’un FortiGate ?
	- ``FGT# diagnose sniffer packet <’filter’>``
	-  `FGT# diagnose debug enable`
	  `FGT# diagnose debug flow filter addr` 
	  `FGT# diagnose debug flow trace start 100`

-  Par défaut, le trafic d'un VDOM ne peut pas aller vers un autre VDOM.
	- Faux

- L'interface sur laquelle un paquet arrive détermine quel VDOM traite le trafic.
	- Vrai 

- Chaque VDOM possède des politiques de sécurité et des tables de routage indépendantes.
	- Vrai

- Une interface physique peut être associée à plusieurs VDOM.
	- Faux

- Le VDOM de gestion est toujours le VDOM root.
	- Vrai

- Un VDOM pourrait monopoliser toutes les ressources du FortiGate.
	- Vrai

- Le Mode d'inspection (flow/proxy) doit être le même pour tous les VDOM.
	- Vrai

- Mode de fonctionnement (transparent, NAT/route) doit être le même pour tous les VDOM.
	- Faux

- Par défaut, un compte utilisateur avec un profil prof_admin a accès à tous les VDOM et aux paramètres globaux.
	- Vrai

- Un profil de sécurité se configure par VDOM. Si l’on veut utiliser le même profil de sécurité dans plusieurs VDOM, il faut le créer dans chaque VDOM.
	- Vrai

- Les liens inter-VDOM permettent de relier directement des VDOM sans devoir créer des routes et des règles de pare-feu.
	- Vrai


## 06 Contrôle d'application 

- Citer trois avantages liés à l’utilisation du contrôle d’application
	- Apporter une meilleure visibilité et un contrôle fin des applications
		- Quel que soit le port ou le protocole utilisé.
	- Réduire les risques liés au Bring-Your-Own-Device (BYOD).
		- Ne maitrisant pas les applications installées sur les équipements BYOD, les administrateurs doivent pouvoir réaliser un contrôle d'application afin de réguler ce qu'un utilisateur peut faire sur le réseau.
	- Limiter l'exposition notamment créée par les applications de médias sociaux
		- Certaines fonctionnalités peuvent être intéressante pour l’entreprise, tout bloquer pourrait causer une perte de productivité.
	- Réduire les surfaces d'attaque
		- En bloquant certaines applications ou fonctionnalités des applications, certaines attaques sont rendues impossibles
	- Récupérer la bande passante
		- En contrôlant la BP allouées aux applications de streaming ou encore de partage (P2P). 
		- En garantissant une bande passante suffisante pour les applications stratégiques.

- L’IPS peut-il détecter les applications même si elles utilisent des protocoles et des ports non standards ?
	- Vrai


- L’IPS peut-il identifier les applications même si l'utilisateur passe par un proxy externe ?
	- Vrai

- L’IPS peut-il identifier les applications si le trafic est chiffré avec SSL ?
	- Faux

- A l’instar d’un antivirus, l’IPS doit-il être mis à jour ?
	- Vrai

- Quels sont les trois filtres utilisés par le contrôle d’applications, dans quel ordre sont-ils utilisés ?
	- Application overrides 
	- Filter overrides 
	- Categories

- Quelles sont les actions possibles sur le trafic ?
	- Allow : le trafic est accepté et ne génère pas de log. 
	- Monitor : le trafic peut passer et il y a génération d'un log (utile pour découvrir le trafic d'un réseau). 
	- Block : abandonne le trafic et journalise. Un message de blocage est envoyé s’il s’agit d’une application HTTP. •
	- Quarantine : bloque le trafic de l'IP source jusqu'à l'expiration du temps de quarantaine et journalise.

- Expliquer les types de régulation de trafic (traffic shaping)
	- Shared shaper 
		- Fixe une limite à la bande passante en upload, tous les utilisateurs se partagent cette bande passante. 
	- Reverse shaper 
		- Idem shared shaper mais pour le téléchargement/streaming. 
	- Per-IP Shaper 
		- Applique la mise en forme du trafic à toutes les adresses IP source listée dans la politique de sécurité. Chaque IP se verra allouer la même bande passante maximale.


## 07 Filtrage Web 

- Contre quels types de menaces le filtrage Web permet-il de se protéger?
	- Préserver les ressources 
		- Éviter une mauvaise utilisation de la bande passante. 
		- Préserver la productivité des employés. 
	- Réduire l'exposition aux menaces Web. 
		- Empêcher l'accès aux sites connus pour être infectés. 
		- Empêcher la perte ou l'exposition d'informations confidentielles. 
		- Empêcher la violation du droit d'auteur. 
	- Protéger contre certains contenus 
		- Empêcher (les enfants) de regarder des contenus inappropriés (Écoles)

- Citez les caractéristiques principales du mode d’inspection Flow-based avec le mode NGFW en Profile-based. Dans ce mode, quelles sont les actions possibles sur le trafic ?
	- Mode d’inspection par défaut. 
	- Moins de latence (scan plus rapide). 
	- Consomme moins de ressources. 
	- Moins d'options de filtrage. 
	- NGFW mode disponible

- Citez les caractéristiques principales du mode d’inspection Flow-based avec le mode NGFW en policy-based. Dans ce mode, quelles sont les actions possibles sur le trafic ?
	- Appliquer le filtrage par catégorie directement dans une règle de pare-feu 
	- Profil d'inspection SSL/SSH est requis

- Citez les caractéristiques principales du mode d’inspection proxy-based. Dans ce mode, quelles sont les actions possibles sur le trafic ?
	- Intercepte le traffic (proxy transparent, deux connexions TCP). 
	- Plus de latence. 
	- Consomme plus de ressources. • Plus d'options de filtrage, meilleure sécurité.

- Expliquez la manière dont se déroule le filtrage web par catégories sur un FortiGate.
	1.  **Analyse des URL** : Le FortiGate examine les URL demandées.
	2. **Catégorisation** : Les sites sont classés dans des catégories comme "Social Media", "Malware", etc
	3. **Application des politiques** : Les politiques définies par l'administrateur bloquent ou autorisent l'accès en fonction des catégories
	4. **Notification des utilisateurs** : Les utilisateurs sont informés si un site est bloqué.
	5. **Journalisation** : Toutes les activités sont enregistrées pour l'analyse ultérieure

- Que permet la fonctionnalité « Threat Feeds » ? 
	- La fonctionnalité "Threat Feeds" permet aux dispositifs Fortigate d'intégrer des flux de renseignements sur les menaces externes pour renforcer la détection et la prévention des attaques.

- Que permet la fonctionnalité Web Rating Override ?
	- De modifier la catégorie d'un site sans passer par FortiGuard

- Que permet la fonctionnalité Web Profile Overrides ?
	- Changer le profil de filtrage Web
		- Permet d'adapter les règles d'inspection du trafic
			- Selon les utilisateurs, les groupes d'utilisateurs ou les adresses IP. 
			- Uniquement disponible pour l'inspection en mode proxy
		- Pour l'utiliser, une authentification est nécessaire 
			- Une fois activée, la page de blocage de FortiGuard affiche un lien que les utilisateurs peuvent sélectionner pour activer le remplacement.

- Citez les caractéristiques principales du filtrage DNS. Quelles sont les actions possibles sur le trafic ?
	- Impacte tous les protocoles qui dépendent du DNS, pas seulement le trafic HTTP. 
		- Ne permet pas de filtrer aussi précisément que le filtrage HTTP.  Prend en charge le filtrage d'URL et les catégories FortiGuard uniquement. 
	- Possible de filtrer les requêtes DNS chiffrées (> FortiOS 7) 
		- DNS over TLS (DoT). 
		- DNS over HTTPS (DoH). 
	- Le filtrage DNS s’effectue sur les réponses.

- Comment savoir à quelle catégorie est associé un site Web ?
	- ==?==

## 08 VPN IPsec

- Citez 4 avantages liés à l’utilisation d’un VPN.
	- Sécurité
	-  Productivité - flexibilité
	- Réduction des coûts
	- Évolutivité

- Citez trois inconvénients liés à l’utilisation d’un VPN.
	- Les niveaux de services ne sont généralement pas garantis
	- Source potentielle de lenteur
	- Confidentialité?

- Expliquez la notion de clé de chiffrement.
	1. **Symétrique** :
	    - **Même clé** pour chiffrer et déchiffrer.
	    - **Exemple** : AES.
	2. **Asymétrique** :
	    - **Deux clés** : publique pour chiffrer, privée pour déchiffrer.
	    - **Exemple** : RSA.
	3. Utilisation
		- **Chiffrement** : Rend les données illisibles.
		- **Déchiffrement** : Récupère les données originales.
	4. Applications
		- **SSL/TLS** : Sécurise Internet.
		- **Chiffrement de Disque** : Protège les données.

- De quoi dépend le degré de sécurité d’un système de chiffrement ?
	- Le degré de sécurité d'un système de chiffrement dépend de la complexité de l'algorithme et de la longueur de la clé utilisée.

- Expliquez le principe du chiffrement symétrique.
	- Le chiffrement symétrique utilise une seule clé pour chiffrer et déchiffrer les données.

- Quels sont les avantages et inconvénients du chiffrement symétrique ?
	- Avantages : Rapidité, efficacité pour le traitement de données massives. 
	- Inconvénients : Gestion des clés plus complexe, nécessité d'une transmission sécurisée des clés.

- Expliquez le principe du chiffrement asymétrique.
	- Le chiffrement asymétrique utilise une paire de clés : une clé publique pour chiffrer et une clé privée pour déchiffrer. Les données chiffrées avec la clé publique ne peuvent être déchiffrées qu'avec la clé privée correspondante, assurant ainsi une sécurité renforcée.

- Quels sont les avantages et inconvénients du chiffrement asymétrique ?
	- Avantages : Sécurité renforcée, pas besoin de partager des clés secrètes. 
	- Inconvénients : Plus lent et nécessite plus de ressources que le chiffrement symétrique.

- Quel est l’avantage du chiffrement symétrique par rapport au chiffrement asymétrique ?
	- L'avantage principal du chiffrement symétrique par rapport au chiffrement asymétrique est sa rapidité et son efficacité pour le traitement de grandes quantités de données.

- Expliquez le principe d’une fonction de hachage.
	- Une fonction de hachage prend en entrée des données de taille variable et les transforme en une empreinte numérique de taille fixe, appelée hash. Cette empreinte est unique pour chaque entrée et permet de vérifier l'intégrité des données sans avoir besoin de stocker les données originales.

- Expliquez la notion de collision de hachage cryptographique. Pourquoi une collision est-elle dangereuse?
	- Une collision de hachage cryptographique se produit lorsque deux ensembles de données différents produisent le même résultat de hachage. C'est dangereux car cela peut être exploité pour falsifier des données sans être détecté.
    
- Quelle est l’utilité d’une fonction de hachage dans le cadre d’un VPN ?
	- Une fonction de hachage dans un VPN assure que les données ne sont pas altérées pendant la transmission, garantissant ainsi leur intégrité et la sécurité des communications.

- Citez trois algorithmes de hachage.
	- SHA-256
	- MD5 
	- SHA-1

- Expliquez ce que signifie l’acronyme KHMAC.
	- HMAC signifie "Keyed-Hash Message Authentication Code". C'est une méthode de sécurité utilisée pour vérifier l'intégrité des données en utilisant une fonction de hachage et une clé secrète partagée.

- Expliquez le principe de la signature numérique (avec et sans certificat).
	- La signature numérique assure l'authenticité et l'intégrité des données en utilisant une clé privée pour signer et une clé publique pour vérifier la signature.
		- Sans certificat : L'entité signe directement avec sa clé privée.
		- Avec certificat : Une autorité de certification fournit un certificat contenant la clé publique de l'entité pour la vérification.

- Expliquer la notion de non répudiation d'un message.
	- La non-répudiation d'un message signifie qu'une fois qu'une entité a signé numériquement un message, elle ne peut pas le nier plus tard. Cela renforce la confiance dans l'authenticité des communications numériques.

- La signature numérique garantit-elle la non répudiation ?
	- Oui, la signature numérique garantit la non-répudiation d'un message. Une fois qu'une entité a signé numériquement un message avec sa clé privée, elle ne peut pas nier l'avoir envoyé.

- Expliquer le fonctionnement d’une PKI.
	![[Pasted image 20240531115125.png]]

- Citez les avantages et inconvénients des certificats autosignés ?
	- Avantages 
		- Ils sont gratuits. 
		- Permettent de garantir la confidentialité des échanges au sein d'une organisation. 
			- Car ils permettent de s'assurer que les clés de chiffrement sont valables. 
		- Permettent d'authentifier les utilisateurs.
	- Inconvénients
		- A usage interne uniquement. 
		- Ils sont considérés comme non fiables
			→ Ils déclenchent des alertes (navigateurs). 
			→ L'administrateur sait qu’ils sont fiables et incite les utilisateurs à ignorer ces alertes. 
			→ Les utilisateurs pourraient avoir un mauvais comportement face à une vraie alerte.

- Quels éléments de sécurité un VPN apporte-t-il ?
	- un VPN renforce la sécurité en cryptant les données, en protégeant la vie privée, en contournant les restrictions géographiques, en sécurisant les connexions Wi-Fi publiques et en offrant un certain degré d'anonymat en ligne.

- Expliquez la notion de NAT-T.
	- Méthode permettant aux datagrammes IPsec de traverser un réseau utilisant du NAT. 
	- NAT-T détecte si les deux extrémités supportent NAT-T. 
	- NAT-T détecte les équipements qui font de la NAT sur le chemin des données (NAT-Discovery).

- Expliquez la fonction de l’Algorithme Diffie-Hellman.
	- flemme

- Expliquez la fonction du protocole IKE. Quel est le rôle de chacune des phases IKE ? Quel N° de port est utilisé par IKE?  
	- IKE facilite l'établissement de connexions sécurisées en négociant les paramètres de sécurité et en échangeant les clés de chiffrement. Ses deux phases permettent d'assurer une connexion VPN sécurisée et fiable.
    
- Expliquez ce qu’est une SA (Security Association).
	- une Security Association définit les paramètres de sécurité partagés entre deux entités pour sécuriser leur communication dans un VPN ou tout autre système de sécurité réseau

## 09 Configuration VPN IPsec

- Expliquez la notion de « confidentialité persistante parfaite » (Perfect Forward Secrecy).
	- La confidentialité persistante parfaite (PFS) garantit que même si une clé de chiffrement est compromise à l'avenir, les sessions passées restent sécurisées car elles utilisent des clés de session uniques et éphémères. Cela empêche la rétro-ingénierie des communications passées même si une clé est compromise ultérieurement.

- Quelle est l’utilité de l’option Dead Peer Detection (DPD)?
	- Négociation des SA IPsec terminée
	- DPD détecte les tunnels défaillants (ou mort) via l’envoi de sondes


- Expliquez ce qu’est l’authentification XAuth. Dans quel cas est-elle utilisée ?
	- Demande un couple username/password en plus de la PreShared Key. 
	- Intéressant pour les utilisateurs mobiles

- Quelles sont les méthodes d’authentification supportées durant la phase 1 de IKE ?
	- **Pre-Shared Key (PSK)**
	- **Certificats X.509**

- Quelle est le rôle des « Quick mode selectors » ?
	- Filtrage du trafic IPsec
	- Meilleure sécurité
	- Pour ne pas utiliser le filtrage du quick mode selector

- Quelle est l’utilité de l’option Auto-negotiate de la phase 2 de IKE ?
	- permet aux appareils FortiGate de négocier automatiquement les paramètres de sécurité avec leur homologue distant, simplifiant ainsi la configuration des tunnels VPN et assurant une adaptation dynamique des paramètres de sécurité

