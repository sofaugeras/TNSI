!!! example "Crédits"

    Crédits des corrections : 
    - Julien SALVA - Lycée Déodat de Séverac
    - Mydatalogger

!!! example "2024 Asie Jour 1 24-NSIJ1G11"
    Exercice 2 du [2024 Asie Jour 1](./data/Sujet 24-asie-j1-ex2.pdf)

    ??? success "Q1"
        C’est un graphe orienté.

    ??? success "Q2"
        - réaliser la tâche (f) puis la tâche (g) : Possible
        - réaliser la tâche (g) puis la tâche (f) : Impossible
        - réaliser la tâche (i) puis la tâche (j) : Possible
        - réaliser la tâche (j) puis la tâche (i) : Possible

    ??? success "Q3"
        Pour réaliser la tâche (k), il faut avoir réaliser les tâches (a), (h), (i), (c) et (j).

    ??? success "Q4"
        Il n’y a pas de cycle.

    ??? success "Q5"
        Il est possible de réaliser les tâche dans l’ordre : 2, 0 puis 1 et 3 puis 5 puis 4.

    ??? success "Q6"
        [image](./data/24-NSIJ1G11_Q6.png)

    ??? success "Q7"
         Il est impossible de trouver un ordre car le graphe possède un cycle $1-2-3$.
    
    ??? success "Q8"
        la matrics M est
        $\\pmatrix{
        0 & 1 & 0 & 0 & 0  \\\\
        0 & 0 & 1 & 0 & 0  \\\\ 
        0 & 0 & 0 & 1 & 0  \\\\
        0 & 1 & 0 & 0 & 1  \\\\ 
        0 & 0 & 0 & 0 & 0  \\\\
        }$  

        [image](./data/24-NSIJ1G11_Q7.png)

        La variable ok vaut ``False`` car le dernier appel de mystere du tableau renvoie ``False`` et chaque appel de la pile d’appel récursif renvoie ``False``.
    
    ??? success "Q9"
        La fonction mystere renvoie ``False`` à chaque fois qu’un cycle est détecté dans le graphe.

    ??? success "Q10"
        Après l’exécution des instructions la variable ``elt`` est associée à la valeur $2$.

    ??? success "Q11"
        La fonction mystere réalise un parcours en **profondeur** du graphe. Dès qu’il arrive sur une étape finale (bout d’une branche), il la marque comme terminée et remonte dans la branche.<br />
        Il faut ainsi empiler cette étape afin qu’elle soit réalisée en dernier : ``resultat.empiler(s)``

!!! exercice "2024 Amérique Nord Jour 1"

    Exercice 2 du [2024 Amérique Nord Jour 1](./data/24-amerique-nord-j1-ex2.pdf)
    Cet exercice porte sur les graphes.

    **Partie A : Matrice d’adjacence**

    ??? success "Q1"
        [image graphe](./data/24-NSIJ1AN1_Q1.png)
    
    ??? success "Q2"
        ```
        # sommets : G, J, Y, E, N, M, A, L
        ```
        $\\pmatrix{
        0 & 1 & 1 & 0 & 1 & 1 & 0 & 0 \\\\
        1 & 0 & 1 & 1 & 0 & 0 & 0 & 1 \\\\
        1 & 1 & 0 & 1 & 1 & 1 & 1 & 0 \\\\
        0 & 1 & 1 & 0 & 1 & 0 & 0 & 0 \\\\
        1 & 0 & 1 & 1 & 0 & 0 & 0 & 0 \\\\
        1 & 0 & 1 & 0 & 0 & 0 & 1 & 0 \\\\
        0 & 0 & 1 & 0 & 0 & 1 & 0 & 0 \\\\
        0 & 1 & 0 & 0 & 0 & 0 & 0 & 0 \\\\
        }$  

    ??? success "Q3"
        Avec ``sommets = ['G', 'J', 'Y', 'E', 'N', 'M', 'A', 'L'] :``
        ``position(sommets, 'G')`` renvoie $0$
        ``position(sommets, 'Z')`` renvoie ``None``

    ??? success "Q4"

        ```python
        def nb_amis(L, m, s):
            pos_s = position(L, s)
            if pos_s == None:
                return None
            amis = 0
            for i in range(len(m)):
                amis += m[i][pos_s]
            return amis
        ```

    ??? success "Q5"
        ``nb_amis(sommets, matrice_adj, 'G')`` renvoie 4.
    
    **Partie B : Dictionnaire de listes d’adjacence**

    ??? success "Q6"
        Dans un dictionnaire, c représente une clé et v la valeur qui lui est associée.

    ??? success "Q7"

        ```python
        graphe = {'G' : ['J', 'Y', 'N', 'M'],
        'J' : ['G', 'Y', 'E', 'L'],
        'Y' : ['G', 'J', 'E', 'N', 'M', 'A'],
        'E' : ['J', 'Y', 'N'],
        'N' : ['G', 'Y', 'E'],
        'M' : ['G', 'Y', 'A'],
        'A' : ['Y', 'M'],
        'L' : ['J']
        }`
        ```
    ??? success "Q8"

        ```python
        def nb_amis(d, s):
            return len(d[s])
        ```
    
    ??? success "Q9"
        Le cercle d’amis de Lou est Jade, Gabriel, Nino, Yanis et Emma.

    ??? success "Q10"

        ```python
        def parcours_en_profondeur(d, s, visites = []):
            visites += [s]
            for v in d[s]:
                if v not in visites:
                    parcours_en_profondeur(d, v)
            return visites
        ```

!!! exercice "2024 Polynésie Jour 1"

    Exercice 1 du [2024 Polynésie Jour 1](./data/24-polynesie-j1-ex1.pdf)<br />
    Cet exercice porte sur les graphes et les protocoles réseau

    **Partie A**

    ??? success "Q1"
        $2⁸ – 2 = 254$
    ??? success "Q2"
        $1101 1001$
    ??? success "Q3"
        £0011 00102 = 32 + 16 + 2 = 50$
    ??? success "Q4"
        ``110.217.52.0/24`` admet une plage @ de ``110.217.52.0`` à ``110.217.52.255``
    ??? success "Q5"
    
        |Destination |Passerelle| Interface|
        |:--:|:--:|:--:|
        |110.217.50.0 |on-link |110.217.50.254|
        |110.217.52.0 |110.217.54.253 |110.217.54.254|
        |110.217.54.0 |on-link| 110.217.54.254|
        |110.217.56.0 ||110.217.54.253 |110.217.54.254|

        [image](./data/24-polynesie-j1-ex1_Q5.png)
    
    ??? success "Q6"
        |Destination |Passerelle| Interface|
        |:--:|:--:|:--:|
        |110.217.50.0| on-link |110.217.50.254|
        |110.217.52.0 |110.217.50.253 |110.217.50.254|
        |110.217.54.0| on-link| 110.217.54.254|
        |110.217.56.0| 110.217.54.253| 110.217.54.254|
    
    ??? success "Q7"
        non, le nombre de sauts reste inchangé pour R2

    **Partie B**

    ??? success "Q8"    
        La fonction effectue une recherche en profondeur mais ne garde pas trace des sommets déjà visités. Cela peut entraîner des boucles infinies si le graphe contient des cycles.

    ??? success "Q9"

        ```python
        def recherche_v2(R1, R2, visités=None):
            if visités == None:
                visités = [] # évite les effets de bord !
            if R1 == R2:
                return True
            if R1 not in visités:
                visités.append(R1)
            for S in adjacents(R1,G):
                if S not in visités:
                    if recherche_v2(S, R2, visités):
                        return True
            return False
        ```

!!! exercice "2024 Polynésie Jour 2"
    Exercice 1 du [2024 Polynésie Jour 2](./data/24-polynesie-j2-ex1.pdf)<br />
    Cet exercice porte sur les structures de données FILE et PILE, les graphes et les algorithmes de parcours.

    Partie A

    ??? success "Q2"

        - Mp → Ar → Mr → Nc
        - 332km

    ??? success "Q2"

        - Mp → Ar → Mr → Nc
        - Mp → Ar → Ax → Nc

        [image](./data/24-polynesie-j2-ex1_Q2.png)

    ??? success "Q3"

        ```python
        G = {
        'Av': ['Mr', 'Ni', 'Ax'],
        'Ni': ['Av', 'Ar', 'Mp'],
        'Mp': ['Ni', 'Ar'],
        'Ar': ['Mr', 'Ni', 'Mp', 'Ax'],
        'Mr': ['Av', 'Ar', 'Ax', 'To', 'Nc'],
        'Ax': ['Av', 'Ar', 'Mr', 'To', 'Nc', 'Di'],
        'To': ['Mr', 'Ax', 'Nc'],
        'Nc': ['Mr', 'To', 'Ax', 'Di'],
        'Di': ['Nc', 'Ax']
        }
        ```
    ??? success "Q4"

        - LIFO : Last In First Out
        - FIFO : First In First Out

    ??? success "Q5"
        FIFO
    ??? success "Q6"
        ``['Av', 'Mr', 'Ni', 'Ax', 'Ar', 'To', 'Nc', 'Mp', 'Di']``
    ??? success "Q7"
    	proposition A : parcours en largeur

    ??? success "Q8"

        ```python
        def distance(graphe : dict, sommet : str) -> dict:
        """
        @param graphe -- dictionnaire représentant un graphe sous la forme de listes d’adjacence
        @param sommet -- un sommet du graphe
        @return un dictionnaire dont les clés sont les sommets du graphe
        et la valeur associée, la distance entre ce sommet clé et le sommet d’origine sommet
        """
            f = creerFile()
            enfiler(f, sommet)
            distances = {sommet: 0}
            visite = [sommet]
            while not estVide(f):
                s = defiler(f)
                for v in graphe[s]:
                    if v not in visite:
                        visite.append(v)
                        distances[v] = distances[s] + 1
                        enfiler(f, v)
            return distances
        ```

    ??? success "Q9"
        ``{'Av': 0, 'Mr': 1, 'Ni': 1, 'Ax': 1, 'Ar': 2, 'To': 2, 'Nc': 2, 'Mp': 2, 'Di': 2}``

    ??? success "Q10"

        ```python
        def parcours2(G : dict, sommet : str) -> list:
        """
        @param G -- un dictionnaire représentant un graphe sous la forme de listes d’adjacence
        @param s -- un sommet du graphe
        @return parcours en profondeur depuis s
        """
            p = creerPile()
            empiler(p, sommet)
            visite = [] # visite doit être initialisé à vide
            while not estVide(p):
                s = depiler(p)
                if not (s in visite): # sinon on ne rentre pas dans ce bloc => fin
                    visite.append(s)
                    for v in G[s]:
                        empiler(p, v)
            return visite
        ```
    ??? success "Q11"
        ``['Av', 'Ax', 'Di', 'Nc', 'To', 'Mr', 'Ar', 'Mp', 'Ni']``

!!! exercice "2024 Polynésie Jour 1"
    
    Exercice 1 du [2024 Polynésie Jour 1](./data/24-metropole-j1-ex1.pdf)
    Cet exercice porte sur la programmation objet en Python et les graphes.

    ??? success "Q1"
        Aucun autre site ne fait référence à Site2

    ??? success "Q2"
        ``s4.predecesseurs = [(s1,1), (s2,2)]
        s5.predecesseurs = [(s1,1), (s3,3), (s4,6)]``

    ??? success "Q3"
        donne le nombre de citations vers le 2ème site : 5

    ??? success "Q4"
        $4 + 2 = 6$

    ??? success "Q5"

        ```python
        def calculPopularite(self) -> int:
            popularite = 0
            for _, liens in self.predecesseurs:
                popularite += liens
            return popularite
        ```
    ??? success "Q6"
        une file

    ??? success "Q7"
        parcours en largeur

    ??? success "Q8 "
        La liste des sites qui ont été référencés par s1 (incluant s1) : ``[s1, s3, s4, s5]``

    ??? success "Q9"    
    
        ```python
        def lePlusPopulaire(listeSites : list) -> Site:
            maxPopularite = 0
            siteLePlusPopulaire = listeSites[0]
            for site in listeSites:
                if site.popularite > maxPopularite:
                    maxPopularite = site.popularite
                siteLePlusPopulaire = site
            return siteLePlusPopulaire
        ```
    ??? success "Q10"
        le nom du site le plus populaire : site1

    ??? success "Q11"
        Les listes en Python ne sont pas implémentées comme des listes chaînées mais comme des tableaux dynamiques : la suppression d'un élément au début de la liste avec pop(0) implique un décalage de tous les éléments suivants, ce qui a une complexité O(n). On est donc en complexité quadratique sans compter du parcours des successeurs.

        Il faudrait utiliser une « vraie » implémentation de liste (deque) et un dictionnaire pour stocker les infos sur les nœuds.


!!! exercice "2024 Métropole Jour 2"
    Exercice 3 du [2024 Métropole Jour 2](./data/24-metropole-j2-ex3.pdf)
    Cet exercice porte sur la programmation orientée objet, les graphes et utilise la structure de données dictionnaire.

    **Partie A : Analyse des classes Piste et Domaine**

    ??? success "Q1"
        Les attributs de la classe ``Piste`` et leur type sont les suivants :

        1. **nom** (type : str) : Le nom de la piste.
        2.**denivele**(type : int) : Le dénivelé de la piste en mètres.
        3.**longueur**(type : float) : La longueur de la piste en kilomètres.
        4.**couleur**(type : str) : La couleur de la piste (par exemple : verte, bleue, rouge, noire). Cet  attribut est initialisé avec une chaîne vide.
        5.**ouverte**(type : bool) : Un indicateur qui précise si la piste est ouverte ou fermée. Cet attribut est initialisé avec la valeur True.

    ??? success "Q2"

        ```python
        def set_couleur(self): 
            if self.denivele >= 100: 
                self.couleur = 'noire' 
            elif self.denivele >= 70: 
                self.couleur = 'rouge' 
            elif self.denivele >= 40: 
                self.couleur = 'bleue' 
            else:
                self.couleur = 'verte'
        ```
    ??? success "Q3"
        Proposition D : une liste d’objets de type Piste. 

    ??? success "Q4"

        ```python
        for piste in lievre_blanc.get_pistes(): 
        if piste.get_couleur() == 'verte': 
        piste.ouverte = False 
        ```

    ??? success "Q5"

        ```python
        def pistes_de_couleur(lst, couleur): 
            return [piste.get_nom() for piste in lst if piste.get_couleur() == couleur] 
        ```

    ??? success "Q6"

        ```python
        def semi_marathon(L): 
            distance = 0 
            liste_pistes = lievre_blanc.get_pistes() 
            for nom in L:
                for piste in liste_pistes: 
                    if piste.get_nom() == nom: 
                        distance += piste.get_longueur() 
            return distance > 21.1 
        ```
    
    **Partie B : Recherche par force brute**

    ??? success "Q7"
        ``print(domaine['E']['F'])``

    ??? success "Q8"

        ```python
        def voisins(G, s): 
            if s in G: 
                return list(G[s].keys()) 
            else: 
                return [] 
        ```

    ??? success "Q9"

        ```python
        def longueur_chemin(G, chemin):
            precedent = chemin[0]
            longueur = 0
            for i in range(1, len(chemin)):
                longueur = longueur + G[precedent][
                chemin[i]]
                precedent =  chemin[i]
            return longueur
        ```
    ??? success "Q10"
        La fonction ``parcours`` est une fonction récursive car elle s'appelle elle-même à partir de la ligne 7, c'est à dire qu'elle fait référence à elle même dans son propre corps,

    ??? success "Q11"

        ```python
        def parcours_dep_arr(G, depart, arrivee):
            liste_chemins = parcours(G, depart)
            chemins_dep_arr = []
            for chemin in liste_chemins:
                if chemin[-1] == arrivee:
                    if chemin not in chemins_dep_arr:
                        chemins_dep_arr.append(chemin)
            return chemins_dep_arr
        ```

    ??? success "Q12"

        ```python
        def plus_court(G, depart, arrivee):
            liste_chemins = parcours_dep_arr(G, depart, arrivee)
            if not liste_chemins:
                return None

            chemin_plus_court = liste_chemins[0]
            minimum = longueur_chemin(G, chemin_plus_court)
            for chemin in liste_chemins[1:]:
                longueur = longueur_chemin(G, chemin)
                if longueur < minimum:
                    minimum = longueur
                    chemin_plus_court = chemin  
            return chemin_plus_court
        ```

    ??? success "Q13"
        La distance minimale ne prend pas en compte d'autres facteurs importants tels que la difficulté du terrain, les conditions météorologiques, la disponibilité des équipements nécessaires, etc. Une approche plus intégrée, prenant en considération plusieurs critères comme le temps de parcours estimé et la difficulté des pistes, permettrait au secouriste d'arriver efficacement et en toute sécurité sur le lieu de l'incident. 