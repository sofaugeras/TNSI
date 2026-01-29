!!! abstract "Exercice 5 du sujet La Réunion J1 2022"
    === "Énoncé"
        Exercice 5 du sujet [La Réunion J1 2022](./data/2022_LeReunion_J1.pdf){. target="_blank"}
    
        ??? tip "Correction Q1.a."
            Une adresse IPv4 se code à l'aide de 4 octets.

        ??? tip "Correction Q1.b."
            Le PC3 a pour adresse ```172.150.4.30 / 24```. Cela signfie que son masque, en notation CIDR, est 24. Ses 24 premiers bits sont donc à 1. Cela correspond au masque ```255.255.255.0``` en notation décimale.

        ??? tip "Correction Q2."
            ![image](data/ex5LR2022.png){: .center}

        ??? tip "Correction Q3.a."
            Pour être dans le réseau 1, il faut que le & logique entre l'IP de la machine et l'adresse du masque donne l'adresse réseau (```172.150.4.0``` ).

            Le réseau étant en ```/24``` (équivalent au masque ```255.255.255.0```), cela signifie que l'adresse IP de la machine soit de la forme ```172.150.4.???```.

            Attention, il faut en plus s'assurer que l'adresse ne soit pas déjà utilisée, et qu'elle ne soit pas l'adresse du réseau (```172.150.4.0```) ou de broadcast (```172.150.4.255```).

            Il reste alors les adresses 4) et 6). (```172.150.4.11``` et ```172.150.4.200```)

        ??? tip "Correction Q3.b."
            La commande permettant de connaître son adresse IP est ```ifconfig``` ou ```ip addr``` sous Linux / MacOS. Ou bien ```ipconfig``` sous Windows.  

        ??? tip "Correction Q4." 
            La solution de relier les switchs entre eux n'est pas satisfaisante. Les deux réseaux ne pourront pas communiquer entre eux, à moins d'élargir (beaucoup) leur masque de sous-réseau.

            La meilleure solution est d'installer un routeur entre les deux switchs, de lui attribuer une adresse IP dans chaque sous-réseau, et de renseigner cette adresse IP comme adresse de passerelle sur chacun des PCs des deux sous-réseaux. 

        ??? tip "Correction Q5."       
            ```python linenums='1'
            def adresse(IP, liste_IP):
                if IP in liste_IP:
                    print("trouvée")
                else:
                    liste_IP.append(IP)
                    print("pas trouvée, ajoutée")
            ```

!!! abstract "Exercice du sujet 0 de 2020"
    === "Énoncé"
        _2020, sujet 0_

        On considère un réseau composé de plusieurs routeurs reliés de la façon suivante :

        ![image](data/ex1.png){: .center width=40%}



        Le protocole RIP permet de construire les tables de routage des différents routeurs, en indiquant pour chaque routeur la distance, en nombre de sauts, qui le sépare d’un autre routeur. Pour le réseau ci-dessus, on dispose des tables de routage suivantes :

        ![image](data/ex2.png){: .center width=80%}

        **Question 1**

        1. Le routeur A doit transmettre un message au routeur G, en effectuant un nombre minimal de
        sauts. Déterminer le trajet parcouru.
        2. Déterminer une table de routage possible pour le routeur G obtenu à l’aide du protocole RIP.

        **Question 2**

        Le routeur C tombe en panne. Reconstruire la table de routage du routeur A en suivant le
        protocole RIP.


    === "Correction"
        **Q1.1.** Le trajet parcouru de A à G est A-C-F-G  
        **Q1.2.** 
        Table de routage de G :  

        | Destination | Routeur suivant | Distance |
        |:--:|:--:|:--:|
        |A|F|3|    
        |B|E|3|
        |C|E|2|
        |D|E|2|
        |E|E|1|
        |F|F|1|

        **Q2**  
        Nouvelle table de routage de A :  

        | Destination | Routeur suivant | Distance |
        |:--:|:--:|:--:|
        |B|B|1|
        |D|D|1|
        |E|D|2|
        |G|D|3|
        |F|D|4|

!!! abstract "Exercice 5 du sujet Métropole J1 2022"

    Exercice 5 du sujet [Métropole J1 2022](./data/22-NSIJ1ME1.pdf)

    ??? tip "Correction Q1.a."
        L'écriture décimale de cette adresse ipv4 est donc b. Le dernier octet a 256 valeurs possibles (de 0 à 255), le nombre d'adresses différentes possibles du réseau A est donc 256.

        note : Deux adresses sont réservées dans un réseau : une pour le réseau lui-même et l'autre pour la diffusion (broadcast). Donc parmi les 256 possibilités, 254 peuvent être attribuées à un hôte du réseau.

    ??? tip "Correction Q2.a."
        Le routeur A est directement relié à B, C et D (métrique 1)

    ??? tip "Correction Q2.b."
        ![schéma](./data/MEJ1_2b.png){: .center width=50%}

    ??? tip "Correction Q3"
        ![tab](./data/MEJ1_3.png){: .center width=50%}

    ??? tip "Correction Q4.a."
         Le chemin emprunté sera F - H - J - K - I pour un coût de 13. Les autres chemins ont un coût supérieur et dans le protocole ospf on minimise le coût (et pas le nombre de routeurs traversés comme dans le protocole rip)

    ??? tip "Correction Q4.b."
        ![tab](./data/MEJ1_4b.png){: .center width=50%}

    ??? tip "Correction Q4.c."
        Une panne du routeur H, en effet dans ce cas :

        - pour transmettre de I à F le chemin serait I - K - J - G - F (coût minimal de 19),
        - pour transmettre de K à F le chemin serait K - J - G - F (coût minimal de 14),
        - pour transmettre de J à F le chemin serait J - G - F (coût minimal de 12)
        - pour transmettre de L à F le chemin serait L - G - F (coût minimal de 20)

        Dans tous les cas, on transite bien par G.

!!! abstract "Exercice du sujet Métropole J1 2021"
    === "Énoncé"
        _2021, sujet Métropole 1_

        On représente ci-dessous un réseau dans lequel R1, R2, R3, R4, R5 et R6 sont des
        routeurs. Le réseau local L1 est relié au routeur R1 et le réseau local L2 au routeur R6.

        ![image](data/bac1.png){: .center width=70%}


        Dans cet exercice, les adresses IP sont composées de 4 octets, soit 32 bits. Elles sont notées X1.X2.X3.X4, où X1, X2, X3 et X4 sont les valeurs des 4 octets, convertis en notation décimale.
        La notation X1.X2.X3.X4/n signifie que les n premiers bits de poids forts de l’adresse IP représentent la partie « réseau », les bits suivants représentent la partie « hôte ».
        Toutes les adresses des hôtes connectés à un réseau local ont la même partie réseau et peuvent donc communiquer directement. L’adresse IP dont tous les bits de la partie « hôte » sont à 0 est appelée « adresse du réseau ».

        On donne également des extraits de la table de routage des routeurs R1 à R5 dans le
        tableau suivant :

        ![image](data/bac2.png){: .center width=70%}

        1/ Un paquet part du réseau local L1 à destination du réseau local L2.

        1.a. En utilisant l’extrait de la table de routage de R1, vers quel routeur R1 envoie-t-il ce paquet : R2 ou R3 ? Justifier.

        1.b. A l’aide des extraits de tables de routage ci-dessus, nommer les routeurs traversés par ce paquet, lorsqu’il va du réseau L1 au réseau L2.

        2/ La liaison entre R1 et R2 est rompue.

        2.a. Sachant que ce réseau utilise le protocole RIP (distance en nombre de sauts), donner l’un des deux chemins possibles que pourra suivre un paquet allant de L1 vers L2.

        2.b. Dans les extraits de tables de routage ci-dessus, pour le chemin de la question 2.a, quelle(s) ligne(s) sera (seront) modifiée(s) ?

        3/ On a rétabli la liaison entre R1 et R2.
        Par ailleurs, pour tenir compte du débit des liaisons, on décide d’utiliser le
        protocole OSPF (distance liée au coût minimal des liaisons) pour effectuer le
        routage. Le coût des liaisons entre les routeurs est donné par le tableau suivant :

        ![image](data/bac3.png){: .center width=90%}

        a. Le coût _C_ d’une liaison est donné ici par la formule
        $C = \frac{10^9}{BP}$

        où $BP$ est la bande passante de la connexion en bps (bits par seconde).
        Sachant que la bande passante de la liaison R2-R3 est de 10 Mbps, calculer le coût correspondant.


        b. Déterminer le chemin parcouru par un paquet partant du réseau L1 et arrivant au réseau L2, en utilisant le protocole OSPF.

        c. Indiquer pour quel(s) routeur(s) l’extrait de la table de routage sera modifié pour un paquet à destination de L2, avec la métrique OSPF.

    === "Correction"
        1.a. D'après la table, R1 doit passer par la passerelle 86.154.10.1 qui correspond au routeur R2.  
        1.b. Le paquet va traverser R1, R2, R6 avant d'arriver à L2.  
        2.a. RIP doit minimiser le nombre de sauts, donc les deux chemins minimaux possibles sont R1-R3-R4-R6 et R1-R3-R2-R6.  
        2.b. La ligne R1 sera modifiée, il faudra partir vers R3 (et son réseau 112.44.65.0/24). Les autres lignes n'ont pas à être modifiées puisque R3 amène en R4 qui amène en R6.  
        3.a $\dfrac{10^9}{10 \times 10^6}=100$ donc le coût R2-R3 est 100.  
        3.b. Avec OSPF, le chemin qui minimise le coût est le chemin R1-R2-R4-R5-R6 (coût 103) :
        ![image](data/bac1_corr.png){: .center width=50%}
        3.c. Dans la table de routage initiale, il faut modifier R2 pour qu'elle envoie sur R4 (et non sur R6), mais aussi R4 pour qu'elle envoie sur R5 (et non sur R6).
        


!!! abstract "Exercice du sujet Métropole J2 2021"
    === "Énoncé"
        _2021, sujet Métropole 2_ (sujet modifié, correction d'erreurs sur les adresses passerelles)

        | ![](data/ex3_1.png) | 
        |:--:| 
        | *Figure 1* |

        La figure 1 ci-dessus représente le schéma d’un réseau d’entreprise. Il y figure deux réseaux locaux L1 et L2. Ces deux réseaux locaux sont interconnectés par les routeurs R2, R3, R4 et R5. Le réseau local L1 est constitué des PC portables P1 et P2 connectés à la passerelle R1 par le switch Sw1. Les serveurs S1 et S2 sont connectés à la passerelle R6 par le switch Sw2.

        Le tableau 1 suivant indique les adresses IPv4 des machines constituants le réseau de l’entreprise.

 
        | ![](data/ex3_2corr.png)  | 
        |:--:| 
        | *Tableau 1 : adresses IPv4 des machines* |

        **Rappels et notations**

        Rappelons qu’une adresse IP est composée de 4 octets, soit 32 bits. Elle est notée
        X1.X2.X3.X4, où X1, X2, X3 et X4 sont les valeurs des 4 octets. Dans le tableau 1, les valeurs des 4 octets ont été converties en notation décimale.

        La notation X1.X2.X3.X4/n signifie que les n premiers bits de poids forts de l’adresse IP représentent la partie « réseau », les bits suivants de poids faibles représentent la partie « machine ».

        Toutes les adresses des machines connectées à un réseau local ont la même partie réseau.
        L’adresse IP dont tous les bits de la partie « machine » sont à 0 est appelée « adresse du réseau ».
        L’adresse IP dont tous les bits de la partie « machine » sont à 1 est appelée « adresse de diffusion ».

        1/ 
        1.a. Quelles sont les adresses des réseaux locaux L1 et L2 ?

        1.b. Donner la plus petite et la plus grande adresse IP valides pouvant être attribuées à un ordinateur portable ou un serveur sur chacun des réseaux L1 et L2 sachant que l’adresse du réseau et l’adresse de diffusion ne peuvent pas être attribuées à une machine.

        1.c. Combien de machines peut-on connecter au maximum à chacun des réseaux locaux L1
        et L2 ? 

        2/ 
        2.a. Expliquer l’utilité d’avoir plusieurs chemins possibles reliant les réseaux L1 et L2.

        2.b. Quel est le chemin le plus court en nombre de sauts pour relier R1 et R6 ? Donner le nombre de sauts de ce chemin et préciser les routeurs utilisés.

        2.c. La bande passante d’une liaison Ether (quantité d’information qui peut être transmise en bits/s) est de $10^7$ bits/s et celle d’une liaison FastEther est de $10^8$ bits/s. Le coût d’une liaison est défini par $\frac{10^8}{d}$ , où $d$ est sa bande passante en bits/s.

        | ![](data/ex3_3.png)  | 
        |:--:| 
        | *Tableau 2 : type des liaisons entre les routeurs* |

        Quel est le chemin reliant R1 et R6 qui a le plus petit coût ? Donner le coût de ce chemin et préciser les routeurs utilisés.

        3/ Dans l’annexe A figurent les tables de routages des routeurs R1, R2, R5 et R6 au
        démarrage du réseau. Indiquer sur votre copie ce qui doit figurer dans les lignes laissées vides des tables de routage des routeurs R5 et R6 pour que les échanges entre les ordinateurs des réseaux L1 et L2 se fassent en empruntant le chemin le plus court en nombre de sauts.

        ![](data/ex3_4_corrige.png)

    === "Correction"
        1.a L'adresse du réseau L1 est 192.168.1.0/24. L'adresse de L2 est 175.6.0.0/16.   
        1.b Pour le réseau L1 (192.168.1.0/24), l'adresse min est 192.168.1.1/24, l'adresse max est 192.168.1.254/24.  
        Pour le réseau L2 (175.6.0.0/16), l'adresse min est 175.6.0.1/16 et l'adresse max est 175.6.255.254/16  
        1.c. Pour le réseau L1, il y a donc 254 adresses (256 moins les deux interdites)  
        Pour le réseau L2, il y en a $256^2-2$, soit 65534.

        2.a Il est utile d'avoir plusieurs chemins en cas de panne d'un routeur.  
        2.b En nombres de sauts (protocole RIP), le chemin le plus court est R1-R2-R5-R6, qui contient 3 sauts.  
        2.c Les liaisons Ether ont un coût de 10, les liaisons FastEther ont un coût de 1. Ce qui donne :
        ![image](data/ex3_1_corr.png){: .center width=50%}
        Le chemin le plus court est donc R1-R2-R3-R4-R5-R6, avec un coût total de 23.

        3. On veut que le chemin soit le plus court en nombre de sauts, donc il faut que le chemin soit R1-R2-R5-R6.
        ![image](data/ex3_1_corr3.png){: .center width=70%}
        Dans la table R5, il manque les lignes

        | IP destination | Passerelle | Interface|
        |:--:|:--:|:--:|
        |192.168.1.0/24|10.1.3.1|Interface 1|
        |172.16.0.0/16|10.1.7.2|Interface 4|  
        

        Dans la table R6, on peut compléter comme ceci (il faudrait des lignes supplémentaires pour y inscrire tous les réseaux)

        | IP destination | Passerelle | Interface|
        |:--:|:--:|:--:|
        |10.1.7.0/24| |Interface 2|
        |192.168.1.0/24|10.1.7.1|Interface 2|
    

!!! abstract "Exercice du sujet Amérique du Nord 2021"
    === "Énoncé"
        _2021, sujet Amérique du Nord_

        Un constructeur automobile possède six sites de production qui échangent des documents entre eux. Les sites de production sont reliés entre eux par six routeurs A, B, C, D, E et F.  
        On donne ci-dessous les tables de routage des routeurs A à F obtenues avec le protocole RIP.

        ![image](data/tabAN.png){: .center}

        1. Déterminer à l'aide de ces tables le chemin emprunté par un paquet de données envoyé du routeur A vers le routeur F.
        2. On veut représenter schématiquement le réseau de routeur à partir des tables de routage. 
        Recopier sur la copie le schéma ci-dessous : 

        ![image](data/graphAN.png){: .center}

        En s'appuyant sur les tables de routage, tracer les liaisons entre les routeurs.

    === "Correction"
        1. A-B-E-F  

        2.
        ![image](data/graphAN_corr.png){: .center}
    

!!! abstract "Exercice 3 du sujet Métropole J1 2025 (8 points)"

    Exercice 3 du sujet [Métropole J1 2025](../../T6_Annales/data/2025/25_NSIJ1ME1.pdf){. target="_blank"}

    *Cet exercice porte sur l'architecture matérielle (réseau), les arbres binaires de recherche et la programmation Python*

    L'entreprise CaféNet possède plusieurs cafés répartis dans différentes villes. Le réseau de la chaîne de cafés est représenté en Figure 1.

    <img src="https://i.ibb.co/Wv0nm12R/ex3-1.png">
    <p style="text-align:center">Figure 1. Schéma d'une partie du réseau</p>
    </figure>

    Sur le schéma sont représentés 4 routeurs, le réseau du siège social, le réseau du café 1, le rése.au du café 2. Dans les réseaux du café 1 et du café 2, des bornes de commandes sont connectées à des switchs (ce sont des boitiers de connexion qui n'ont pas eux-mêmes d'adresse IP). Les 4 routeurs représentés sont composés d'au moins 3 interfaces réseau capables de relier des réseaux ensemble. Chaque interface possède donc une adresse IPv4 sur le réseau auquel elle est reliée.

    Les masques des sous-réseaux sont tous 255.255.255.0. Avec ce masque, les trois premiers octets des adresses IP codent l'adresse réseau. Le dernier octet, c'est-à-dire les 8 derniers bits, code l'adresse des machines à l'intérieur de chaque sous-réseau.

    **Partie A**

    Le gérant veut faire installer une troisième borne de commande dans le café 1.

    1_ Indiquer les deux seules adresses IP valides pour cette nouvelle borne, parmi les quatre adresses IP proposées.
    a. 192.168.20.2
    b. 192.168.20.157
    c. 192.168.20.261
    d. 192.168.24.10
    ??? tip "Correction"
        Ce sont les IP a. et b.

    L'adresse de diffusion, appelée aussi adresse de *broadcast*, est la dernière adresse disponible à l'intérieur d'un réseau local.

    2_ Déterminer l'adresse de diffusion du réseau du café 1.
    ??? tip "Correction"
        Il s'agit de l'IP 192.168.20.255.

    3_ Déterminer compbien de machines informatiques il est encore possible de connecter au réseau du café 1 après l'installation de la troisième borne de commande.

    ??? tip "Correction"

        Sur un octet, il est possible d’obtenir 256 valeurs. Il existe donc 256 adresses machines au sein 
        du réseau du café 1. En décomptant les deux adresses IP réservées (réseau et diffusion), les trois 
        bornes de commandes et l’interface du routeur, il reste 250 adresses IP disponibles.


    Le réseau local du café 1 n'a pas besoin de plus de 8 adresses IP différentes. Ce décompte d'adresses IP inclut les adresses IP réservées (à savoir l'adresse de diffusion et l'adresse du réseau). Il est rappelé que la longueur du masque de sous-réseau est actuellement de 24 bits (c'est-à-dire 3 octets).

    4_ Expliquer quelle est la longueur maximale du masque de sous-réseau que l'on pourrait choisir pour le réseau local du café 1.
    ??? tip "Correction"

        Il faut exactement 3 bits pour coder 8 adresses différentes. Le masque pourrait donc aller jusqu’à compter 29 bits (32 bits - 3 bits).

    **Partie B**

    **RIP** (Routing Information Protocol) est un protocole de routage utilisé dans les réseaux IP. Il est conçu pour réduire le nombre de sauts entre deux réseaux. Un « saut » correspond au transfert des données d'un routeur à un autre. Le protocole RIP utilise le nombre de sauts comme critère principal pour évaluer le coût d'un chemin. Autrement dir, il considère que le chemin le plus optimal est celui qui traverse le moins de routeurs.

    La table de routage du routeur 2 de la Figure 1 est représentée ci-dessous

    | Réseau de destination | Interface de sortie | Prochain routeur | Nombre de sauts |
    | --------------------- | ------------------- | ---------------- | --------------- |
    | 192.168.20.0          | 192.168.20.1        | aucun            | 0               |
    | 172.16.3.0            | 172.16.3.1          | aucun            | 0               |
    | 172.16.4.0            | 172.16.4.1          | aucun            | 0               |
    | 192.168.10.0          | 172.16.3.1          | 172.16.3.2       | 2               |
    | 172.16.0.0            | 172.16.4.1          | 172.16.4.2       | 1               |
    | 172.16.2.0            | 172.16.4.1          | 172.12.4.2       | 1               |
    | 192.168.20.0          | ...                 | ...              | ...             |
    | 172.16.1.0            | ...                 | ...              | ...             |

    5_ Recopier et compléter les deux dernières lignes de la table de routage du routeur 2.
    ??? tip "Correction"

        | Réseau de destination | Interface de sortie | Prochain routeur | Nombre de sauts |
        | --------------------- | ------------------- | ---------------- | --------------- |
        | 192.168.30.0          | 172.16.4.1                 | 172.16.4.2              | 1             |
        | 172.16.1.0            | 172.16.3.1                | 172.16.3.2              | 1            |


    La table de routage du routeur 2 contient un réseau de destination pour lequel deux routes différentes sont possibles. La ligne conrrespondante dans la table de routage aurait donc pu être remplie différemment tout en respectant le protocole RIP.

    6_ Identifier, dans la table de routage du routeur 2, le réseau de destination que l'on peut atteindre d'une autre façon et indiquer comment cette ligne de la table de routage pourrait être modifiée.
    ??? tip "Correction"

        On peut choisir, pour le réseau 192.168.10.0, la route qui sort par l’interface 172.16.4.1 vers le prochain routeur 172.16.4.2. On obtient encore une route à 2 sauts.

    Une adresse IP qui n’est pas référencée dans la table de routage doit être routée par défaut vers Internet.

    7_ Recopier et compléter la ligne à ajouter à la table de routage du routeur 2.
    
    | Réseau destination | Interface de sortie | Prochain routeur |
    | ------------------ | ------------------- | ---------------- |
    | autre              | ...                 | ...              |

    ??? tip "Correction"

        | Réseau destination | Interface de sortie | Prochain routeur |
        | ------------------ | ------------------- | ---------------- | 
        | autre              | 172.16.3.1          | 172.16.3.2       |


    **Partie C**

    **OSPF** est également un protocole d’échanges de données entre les routeurs qui prend en compte le coût des routes. Le coût est lié au débit des liaisons entre les routeurs par la formule suivante :
    $cout=\dfrac{10^9}{debit}$ avec le débit en $bit.s^{-1}$.

    8_ Recopier et compléter la dernière colonne du tableau ci-dessous :

    | Type de connexion | Débit en $bit.s^{-1}$.          | coût |
    | ----------------- | ------------------------------- | ---- |
    | Ethernet          | 10 $Mbit.s^{-1}=10^7\ bit.s-1$  | 100  |
    | Fast Ethernet     | 100 $Mbit.s^{-1}=10^8\ bit.s-1$ | ...  |
    | Fibre optique     | 1 $Gbit.s^{-1}=10^9\ bit.s-1$   | ...  |

    ??? tip "Correction"

        Le coût de la liaison Fast Ethernet est 10 et celui de la fibre optique est 1.

    Le schéma ci-dessous met en évidence les types de connexion qui relient les routeurs.

    <img src="https://i.ibb.co/Q1q95rL/ex3-2.png">
    <p style="text-align:center">Figure 2. Schéma des types de connexion</p>

    9_ Déterminer la route dont le coût est minimal pour aller du routeur 1 jusqu’au routeur 4 et calculer son coût au sens du protocole OSPF.

    ??? tip "Correction"

        1→2→3→4 est la route à choisir pour respecter le protocole OSPF. Son coût est de 21.


    **Partie D** 

    *les arbres binaires de recherche et la programmation Python*
    
    Le but de cette partie est de classer les adresses IP des différents réseaux afin de faciliter leur recherche.
    La fonction `ip_bin` prend en argument une chaîne de caractères décrivant une adresse IP en notation décimale, et renvoie une chaîne de caractères, de longueur 35 (32 bits et les 3 points), décrivant l’adresse IP en notation binaire.

    Exemple :
    ```python
    >>> ip_bin('192.168.10.1')
    '11000000.10101000.00001010.00000001'
    ```
    10_ Donner la chaîne de caractères renvoyée par ip_bin('192.168.20.12').
    ??? tip "Correction"

        Les conversions en binaire des nombres 192 et 168 sont donnés dans l’exemple. Il reste à convertir 20 et 12 en binaire.<br />
        `11000000.10101000.00010100.00001100`

    La fonction `precede` prend en paramètres deux adresses IP en notation binaire, sous forme de chaînes de caractères identiques à celles renvoyées par la fonction `ip_bin`. La fonction `precede` renvoie un booléen qui vaut `True` si la première adresse IP en paramètre précède la seconde adresse IP.

    Exemple :
    ```python
    >>> a = '11000000.10101000.00001010.00000001' 
    >>> b = '11000000.10101000.00001111.00000001' 
    >>> precede(a, b) 
    True
    ```

    L’algorithme compare bit à bit les deux chaînes binaires, en lisant les chaînes de caractères dans le sens usuel (de gauche à droite). Dans l’exemple ci-dessus, tous les caractères sont identiques jusqu’au sixième caractère du troisième octet. Comme le bit de l’adresse `a` est inférieur à celui de l’adresse `b`, on en déduit que l’adresse IP `a` précède l’adresse IP `b`.

    Si la première adresse IP ne précède pas la seconde, la fonction doit renvoyer `False`.
    L’algorithme de comparaison est traduit dans le langage Python sous la forme suivante :

    ```python
    def precede(ip_1, ip_2):
        for i in range(35):
            if ip_1[i] < ip_2[i]:
                return ...
            elif ip_1[i] > ip_2[i]:
                return ...
        return ...
    ```

    11_ Expliquer dans quel cas la fonction `precede` exécutera la dernière instruction `return` de la ligne 7.

    ??? tip "Correction"

        Il faut que tous les caractères soient identiques, c’est-à-dire que les adresses IP passées en paramètre soient les mêmes.

    12_ Recopier et compléter les lignes 4, 6 et 7 du code de la fonction `precede`.

    ??? tip "Correction"

        ```python
        4 return True
        6 return False
        7 return False
        ```

    Les tables de routage de chaque routeur sont implémentées sous la forme d’arbre binaire de recherche avec la classe Abr.

    ```python
    class Abr:
        def __init__(self, adresse_ip, 
                    interface, passerelle,
                    cout):
            self.adresse_ip = adresse_ip
            self.interface = interface
            self.passerelle = passerelle
            self.cout = cout  
            if adresse_ip != '': 
                self.gauche = Abr('', '', '', 0) 
                self.droite = Abr('', '', '', 0) 
                
    def est_vide(self):
        return ...
    ```
    Dans cette représentation :
    - `adresse_ip` désigne l’adresse IP de la destination ;
    - `interface` désigne l’interface réseau ;
    - `passerelle` désigne l’adresse IP du prochain routeur ;
    - `cout` désigne le nombre de sauts pour atteindre la destination.
    - par convention, l’arbre binaire vide est une instance de `Abr` pour laquelle `adresse_ip` est une chaîne de caractères vide ;
    - un arbre binaire de recherche non vide possède nécessairement un sous-arbre gauche et un sous-arbre droit, éventuellement vides, qui sont tous les deux des arbres binaires de recherche. Ces sous-arbres sont désignés par gauche et droite dans la classe `Abr` ;
    - si elle n’est pas vide, l’adresse IP du sous-arbre gauche précède l’adresse IP de l’instance parent ;
    - si le sous-arbre droit n’est pas vide, alors l’adresse IP de l’instance parent précède l’adresse IP du sous-arbre droit.


    13_ Citer un attribut et citer une méthode de la classe `Abr`.

    ??? tip "Correction"

        `adresse_ip` est un attribut. `est_vide` est une méthode.

    14_ Recopier et compléter la ligne 14 du code de la classe `Abr`.

    ??? tip "Correction"

        ```python
        14    return self.adresse_ip == ''
        ```

    15_ Justifier, en mobilisant des connaissances de cours, l’intérêt qu’il peut y avoir à représenter la table de routage par un arbre binaire de recherche.
    
    ??? tip "Correction"

        Le coût de l’algorithme de recherche peut être logarithmique, alors que le coût de la recherche dans un tableau est linéaire.

    16_ La section de code qui définit `modifie` est incluse dans la classe `Abr`.

    ```python
    def modifie(self, adresse_ip,
                interface, passerelle,
                cout):
        if self.est_vide():
            self.adresse_ip = adresse_ip 
            self.interface = interface 
            self.passerelle = passerelle 
            self.cout = cout 
            self.gauche = Abr('', '', '', 0) 
            self.droite = Abr('', '', '', 0) 
        else: 
            self.adresse_ip = adresse_ip 
            self.interface = interface 
            self.passerelle = passerelle 
            self.cout = cout
    ```
    Les lignes 20 à 23 sont exactement les mêmes que les lignes 27 à 30.

    16_ Réécrire le code de la fonction modifie en évitant cette répétition.

    ??? tip "Correction"

        ```python
        def modifie(self, adresse_ip, 
                    interface, passerelle, 
                    cout):
            if self.est_vide():
                self.gauche = Abr('','','',0) 
                self.droite = Abr('','','',0) 
            self.adresse_ip = adresse_ip 
            self.interface = interface 
            self.passerelle = passerelle 
            self.cout = cout
        ```
    
    La classe `Abr` est complétée afin de permettre l’ajout de nouvelles lignes à la table de routage, tout en conservant les propriétés que doit posséder un arbre binaire de recherche.
    
    ```python
    def rechercher(self, adresse_ip): 
        if self.est_vide() or adresse_ip==self.adresse_ip: 
            return self 
        elif precede(...): 
            return self.gauche.rechercher(adresse_ip) 
        else: 
            return self.droite.rechercher(adresse_ip) 
        
    def inserer(self, adresse_ip, 
                interface, passerelle, 
                cout): 
        destination = self.rechercher(adresse_ip)
        destination.modifie(adresse_ip, 
                            interface, passerelle, 
                            cout)
    ```
    On rappelle que la fonction `precede` prend en arguments des adresses IP écrites sous forme binaire.

    17_
     Recopier et compléter la ligne 35 du code de la fonction `rechercher`.

    ??? tip "Correction"

        ```python
        precede(ip_bin(adresse_ip),ip_bin(self.adresse_ip))
        ```       
