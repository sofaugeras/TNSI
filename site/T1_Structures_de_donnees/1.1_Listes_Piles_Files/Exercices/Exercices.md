

!!! example "Exercice 1 - Pile"
    === "Énoncé"
        Exercice 5 du sujet [Centres Étrangers 1 - 2021](../../T6_Annales/data/2021/21_Centres_Etrangers_1.pdf){. target="blank"}

    === "Corr. Q1"
        ![image](data/ex1Q1.png){: .center width=50%}

    === "Corr. Q2"
        ![image](data/ex1Q2.png){: .center width=50%}

    === "Corr. Q3"
        ```python linenums='1'
        def maximum(P):
            if est_vide(P):
                return None
            m = depile(P)
            while not est_vide(P):
                val = depile(P)
                if val > m:
                    m = val
            return m
        ```

        Avec le code ci-dessus, la pile ```p``` est vide à la fin de l'exécution. Pour éviter cela, on peut par exemple créer une pile ```q``` temporaire qui recevra les éléments de ```p```, avant de retransférer à la fin du programme les éléments de ```q```  dans ```p```.

        ```python linenums='1'
        def maximum(P):
            Q = creer_pile()
            if est_vide(P):
                return None
            m = depile(P)
            empile(Q, m)
            while not est_vide(P):
                val = depile(P)
                empile(Q, val)
                if val > m:
                    m = val
            while not est_vide(Q):
                empile(P, depile(Q))
            return m
        ``` 

    === "Corr. Q4"
        **Q4a.** On va vider la pile ```p``` dans une pile ```q``` tout en comptant le nombre d'éléments dépilés dans une variable ```t```. 
        On redonne ensuite à ```p``` son état initial en vidant ```q``` dans ```p```.

        **Q4b**

        ```python linenums='1'
        def taille(P):
            if est_vide(P):
                return 0
            Q = creer_pile()
            t = 0
            while not est_vide(P):
                empile(Q, depile(P))
                t += 1
            while not est_vide(Q):
                empile(P, depile(Q))
            return t
        ```

!!! example "Exercice 2 - Pile"
    === "Énoncé"
        Exercice 1 du sujet [La Réunion J2 - 2022](../../T6_Annales/data/2022/2022_LaReunion_J2.pdf){. target="blank"}

    === "Corr. Q1"
        ![image](data/ex2Q1.png){: .center width=70%}

    === "Corr. Q2a"
        La variable ```temp``` contient la valeur 25.

    === "Corr. Q2b"
        ```p1``` est identique, elle contient toujours les valeurs 25, 3 et 7. 

    === "Corr. Q3"
        ```python linenums='1'
        def addition(p):
            nb1 = depiler(p)
            nb2 = depiler(p)
            empiler(p, nb1 + nb2)
        ``` 
    === "Corr. Q4"
        ```python linenums='1'
        p = pile_vide()
        empiler(p, 3)
        empiler(p, 5)
        addition(p)
        empiler(p, 7)
        multiplication(p)
        ```

!!! example "Exercice 3 - Pile"
    === "Énoncé"
        Exercice 2 du sujet [Métropole Candidats Libres J1 - 2021](../../T6_Annales/data/2021/21_Metropole_Candidats_libres_1.pdf){. target="blank"}

    === "Corr. Q1a"
        ```python linenums='1'
        pile1 = Pile()
        pile1.empiler(7)
        pile1.empiler(5)
        pile1.empiler(2)
        ```

    === "Corr. Q1b"
        L'affichage produit est ```7, 5, 5, 2```.

    === "Corr. Q2a"
        - Cas n°1 : ```3, 2``` 
        - Cas n°2 : ```3, 2, 5, 7```
        - Cas n°3 : ```3```
        - Cas n°4 : ```«pile vide»```

    === "Corr. Q2b"
        La fonction ```mystere``` permet d'obtenir la pile retournée jusqu'à un élément particulier (s'il existe).

    === "Corr. Q3"
        ```python linenums='1'
        def etendre(pile1, pile2):
            while not pile2.est_vide():
                val = pile2.depiler()
                pile1.empiler(val)
        ```
    === "Corr. Q4"
        ```python linenums='1'
        def supprime_toutes_occurences(pile, element):
            p_temp = Pile()
            while not pile.est_vide():
                val = pile.depiler()
                if val != element:
                    p_temp.empiler(val)
            while not p_temp.est_vide():
                val = p_temp.depiler()
                pile.empiler(val)
        ```

!!! example "Exercice 4 - Pile"
    === "Énoncé"
         Exercice 5 du sujet [Amérique du Nord J1 - 2021](../../T6_Annales/data/2021/21_Amérique_du_Nord.pdf){. target="blank"}

    === "Corr. Q1a"
        Le contenu de la pile P sera 

        ```python
        | "rouge" |
        | "vert"  |
        | "jaune" |
        | "rouge" |
        | "jaune" |
         _________
        ```

    === "Corr. Q1b"   
        ```python linenums='1'
        def taille_file(F):
            """File -> Int"""
            F_temp = creer_file_vide()
            n = 0
            while not est_vide(F):
                enfiler(F_temp, defiler(F))
                n += 1
            while not est_vide(F_temp):
                enfiler(F, defiler(F_temp))
            return n
        ```

    === "Corr. Q2"   
        ```python linenums='1'
        def former_pile(F):
            """File -> Pile"""
            P_temp = creer_pile_vide()
            P = creer_pile_vide()
            while not est_vide(F):
                empiler(P_temp, defiler(F))
            while not est_vide(P_temp):
                empiler(P, depiler(P_temp))
            return P
        ```

    === "Corr. Q3"   
        ```python linenums='1'
        def nb_elements(F, elt):
            """File, Int -> Int"""
            F_temp = creer_file_vide()
            n = 0
            while not est_vide(F):
                val = defiler(F)
                if val == elt:
                    n += 1
                enfiler(F_temp, val)
            while not est_vide(F_temp):
                enfiler(F, deFiler(F_temp))
            return n
        ```
    === "Corr. Q4"   
        ```python linenums='1'
        def verifier_contenu(F, nb_rouge, nb_vert, nb_jaune):
            """File, Int, Int, Int -> Bool"""
            return nb_elements(F, "rouge") <= nb_rouge and \
                   nb_elements(F, "vert") <= nb_vert and \
                   nb_elements(F, "jaune") <= nb_jaune
        ```

!!! example "Exercice 5 - File"
    === "Énoncé"
         Exercice 5 du sujet [Métropole Septembre- 2022](./data/22-metropole-septembre-ex5.pdf){. target="blank"}
    
    === "Corr. Q1"
        C'est la situation 2 qui est associé à une structure de file puisque le premier travail envoyé sera aussi le premier a être imprimé.

    === "Corr. Q2a"
        ``Val`` contiendra Prioritaire, V contiendra Client3, Clien2, Client1 et F contiendra Client4.

    === "Corr. Q2b"

        ```python
        def longueur_file(F):
            V = creer_file()
            n = 0
            while not est_vide(F):
                n = n + 1
                val = defiler(F)
                enfiler(V,val)
            while not est_vide(F):
                val = defiler(V)
                enfiler(F,val)
            return n
        ```
    === "Corr. Q2c"    
        On reprend la fonction précédente en ajoutant une condition de façon à ne compter que les personnes prioritaires

        ```python
        def longueur_file(F):
            V = creer_file()
            prio = 0
            while not est_vide(F):
                val = defiler(F)
                if val == "Prioritaire":
                    prio = prio + 1
                enfiler(V,val)
            while not est_vide(F):
                val = defiler(V)
                enfiler(F,val)
            return prio
        ```

!!! example "Exercice 6 - File"
    === "Énoncé"
         Exercice 5 du sujet [Amérique du Nord J1- 2022](./data/22-amerique-nord-j1-ex5.pdf){. target="blank"}
        Relévé de Températures

    === "Corr. Q1a"   
        Proposition 2

    === "Corr. Q1b"

        ```python
        f = creer_file_vide() 
        enfiler(f, 15) 
        enfiler(f, 17) 
        enfiler(f, 14)
        ```

    === "Corr. Q2"

        ```python
        def longueur_file(F): 
            G = creer_file_vide() 
            n = 0 
            while not(est_vide(F)): 
                v = defiler(F) 
                n = n + 1 
                enfiler(G, v) 
            while not(est_vide(G)): 
                v = defiler(G) 
                enfiler(F, v) 
            return n
        ```
    === "Corr. Q3"

        ```python
        def variations(F): 
            taille = longueur_file(F) 
            if taille == 1 : 
                return [] 
            else: 
                tab = [0 for k in range(taille - 1)]
                element1 = defiler(F) 
                for i in range(taille - 1): 
                    element2 = defiler(F) 
                    tab[i]=element2 - element1 
                    element1 = element2 
            return tab
        ```
    === "Corr. Q4"

        ```python
        def nombre_baisses(tab): 
            mini = tab[0] 
            nbr = 0 
            for v in tab: 
                if v < 0: 
                    nbr = nbr + 1 
                if v < mini: 
                    mini = v 
            if nbr == 0: 
                return (0,0) 
            else: 
                return (nbr, mini)
        ```