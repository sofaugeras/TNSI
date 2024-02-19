
!!! abstract "Exercice 1 : Tri Fusion : application"

    === "Enoncé"
        Détaillez les étapes du **tri fusion** sur le tableau [23, 17, 28, 11, 20, 22, 19, 16].<br />
        Déterminez le nombre de comparaisons effectuées durant les étapes de fusion.<br />
        Combien faudrait-il faire de comparaisons avec l'algorithme de tri par sélection ?

    === "Correction"

        ![etapes du tri fusion](data/ex1Correction.png)

        **Déterminez le nombre de comparaisons effectuées durant les étapes de fusion.**<br />
        Pour fusionner les tableaux de taille 1, il en faut 4×1 = 4.<br />
        Pour fusionner les tableaux de taille 2, il en faut 3 + 2 = 5.<br />
        Pour fusionner les tableaux de taille 4, il en faut 6.<br />
        Ce qui donne un total de 4 + 5 + 6 = 15 comparaisons.<br />

        **Combien faudrait-il faire de comparaisons avec l'algorithme de tri par sélection ?**<br />
        Il en faut 7 + 6 + 5 + 4 + 3 + 2 + 1 = 28.<br />

!!! abstract "Exercice 2 : Tri Fusion : application"

    === "Enoncé"
        Détaillez les étapes du **tri fusion** sur le tableau [68, 46, 27, 54, 32].<br />
        Déterminez le nombre de comparaisons effectuées durant les étapes de fusion.<br />
        Combien faudrait-il faire de comparaisons avec l'algorithme de tri par sélection ?

    === "Correction"
        
        ![etapes du tri fusion](data/ex2Correction.png)

        **Déterminez le nombre de comparaisons effectuées durant les étapes de fusion.**<br />
        Pour fusionner [68] avec [46] et [54] avec [32], il en faut 2×1 = 2.<br />
        Pour fusionner [27] avec [32, 54], il en faut 1 seule.<br />
        Pour fusionner [46, 68] avec [27, 32, 54], il en faut 4.<br />
        Ce qui donne un total de 2 + 1 + 4 = 7 comparaisons.<br />

        ** Combien faudrait-il faire de comparaisons avec l'algorithme de tri par sélection ?**<br />
        Il en faut 4 + 3 + 2 + 1 = 10.<br />

!!! abstract "Exercice 3 "
    === "Enoncé"
        On considère la fonction `rechercher(x,T,debut,fin)` de recherche, entre debut et fin inclus, de l'indice d'un élément `x` dans un tableau `T` trié suivant l'ordre croissant.
        
        ```python
        def rechercher(x, T, debut, fin):
        """ Renvoie l'indice de x, entre debut et fin, dans le tableau trié dans l'ordre croissant T, et -1 sinon. """
            while debut <= fin:
                milieu = (debut + fin) // 2
                if x == T[milieu]:
                    return milieu
                elif x < T[milieu]:
                    fin = milieu - 1
                else:
                    debut = milieu + 1
            return -1

        def indice(x, L):
            return rechercher(x, L, 0, len(L)-1)

        premiers = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59]
        print(indice(19, premiers))
        >> 7 
        print(indice(51, premiers))
        >> 1
        ```
        De quel algorithme s'agit-il ? <br />
        En quoi cet algorithme relève-t-il du paradigme diviser-pour-régner ?<br />
        Réécrire la fonction `rechercher(x,T,debut,fin)` sous la forme récursive.
        
    === "Correction"
        **De quel algorithme s'agit-il ?** 
        Il s'agit d'une implémentation itérative de la recherche dichotomique.<br />
        **En quoi cet algorithme relève-t-il du paradigme diviser-pour-régner ?**<br />
        L'algorithme de recherche dichotomique divise l'intervalle de recherche en deux sous-intervalles disjoints `([debut;milieu-1] et [milieu+1;fin])` et détermine, au moyen d'une comparaison, le sous-intervalle sur lequel il convient de poursuivre cette recherche pour trouver la réponse (l'indice de
        l'élément recherché).<br />
        L'algorithme procède donc par division en sous problèmes indépendants, qu'il résout en combinant les réponses (en poursuivant la recherche sur le seul sous-intervalle pertinent, capable de fournir la réponse si elle existe)<br />

        ```python
        def rechercher(x, T, debut, fin):
            if debut > fin:
                return -1
            else:
                milieu = (debut + fin) // 2
                if x == T[milieu]:
                    return milieu
                elif x < T[milieu]:
                    return rechercher(x, T, debut, milieu - 1)
                else:
                    return rechercher(x, T, milieu + 1, fin)
        ```

!!! abstract "Exercice 4 : couple (minimum, maximum)"
    === "Algorithme"
        **Recherche du couple (minimum, maximum) dans un tableau avec une méthode « diviser pour régner »** <br />
        On scindera le tableau en deux parties et on effectuera la recherche récursivement.<br />
        Si le tableau a une taille de 2, alors le couple `(minimum, maximum)` s’obtient directement par comparaison 
        des deux valeurs.<br />
        Si le tableau a une taille de 1, alors le couple `(minimum, maximum)` est composé de deux fois l’unique 
        valeur du tableau.<br />
        Lors de la phase de combinaison, on comparera les résultats « remontant » de la récursivité pour obtenir le 
        résultat.<br />
        
        :arrow_right: Implémenter cet algorithme <br />
        :arrow_right: Donner la complexité de l’algorithme.<br />
        _Remarque :_ ceux qui sont à l’aise essaieront autant que possible de ne pas utiliser de slices, mais plutôt des indices de début et de fin. Ceci pour des raisons d’efficacité lors de l’implémentation.
    
    === "Correction"

        ```python
        from random import randint

        liste = []
        for i in range(0, 30):
            liste.append(randint(1,100))

        print(liste)

        def min_et_max(T):
            if len(T) == 1:
                return (T[0], T[0])
            elif len(T) == 2:
                if T[0] < T[1]:
                    return (T[0], T[1])
                else:
                    return (T[1], T[0])
            else:
                m = len(T) // 2
                min1, max1 = min_et_max(T[:m])
                min2, max2 = min_et_max(T[m:])
                return min(min1, min2), max(max1, max2)
            
        print(min_et_max(liste))
        ```

!!! abstract "Exercice 5 : Quick sort (facultatif)"
    === "Algorithme (pas au programme de terminale, mais un des tris les plus efficace"

        Le **tri rapide** (quicksort en anglais) est un algorithme de tri généralement très rapide qui met en oeuvre le paradigme diviser-pour-régner suivant l'algorithme : <br />
        • Lorsqu'un tableau est vide ou ne contient qu'un élément, il est déjà trié.<br />
        • Sinon :<br />
            o Prendre l'élément (appelé pivot) situé au milieu du tableau T à trier.<br />
            o Créer le tableau Tinf des éléments de T strictement inférieurs au pivot.<br />
            o Créer le tableau Tpivot des éléments de T égaux au pivot.<br />
            o Créer le tableau Tsup des éléments strictement supérieurs au pivot.<br />
            o Le tableau trié est obtenu par la concaténation des trois tableaux :
            Tinf trié, Tpivot non trié et Tsup trié suivant le même algorithme.<br />
        
        :arrow_right: Implémentez le tri rapide sous la forme d'une fonction récursive tri_rapide()

        ![quick sort](data/quicksort.gif)

        @Credits: [fullyunderstood.com](https://fullyunderstood.com/pseudocodes/quick-sort/) et [codescope.com](https://www.codesdope.com/course/algorithms-quicksort/)

    === "Correction"

        ```python
        from random import randint

        liste = []
        for i in range(0, 30):
            liste.append(randint(1,100))

        print(liste)

        def triRapide(liste):
            """
            fonction qui initialise la fonction récursive de tri rapide d'une liste.
            """
            trier(liste, 0, len(liste+1))

        def trier(liste, indiceDebut, indiceFin):
            """
            fonction récursive qui trie une liste en utilisant la méthode trie rapide.
            """
            if (indiceFin <= indiceDebut):
                return 
            indicePivot = randint(indiceDebut, indiceFin)
            pivot = liste[indicePivot]
            indicePivot = partitionner(liste, pivot, indiceDebut, indicePivot, indiceFin)
            trier(liste, indiceDebut, indicePivot-1)
            trier(liste, indicePivot+1, indiceFin)

        def partitionner(liste, pivot, indiceDebut, indicePivot, indiceFin):
            """
            fonction qui partitionne une liste en fonction d'un pivot en mettant à gauche
            du pivot les éléments plus petits que le pivot et à droite les éléments plus
            grand. L'indice du pivot est susceptible d'être modifié au cours du traitement ;
            il est donc renvoyé par cette fonction.
            """
            termine = False
            indiceCourant = indiceDebut
            while indiceCourant <= indiceFin:
                if liste[indiceCourant] > pivot and indiceCourant < indicePivot:
                    liste[indicePivot] = liste[indiceCourant]
                    liste[indiceCourant] = liste[indicePivot-1]
                    liste[indicePivot-1] = pivot
                    indicePivot = indicePivot - 1
                elif liste[indiceCourant] < pivot and indiceCourant > indicePivot:
                    liste[indicePivot] = liste[indiceCourant]
                    liste[indiceCourant] = liste[indicePivot+1]
                    liste[indicePivot+1] = pivot
                    indicePivot = indicePivot + 1
                else:
                    indiceCourant = indiceCourant + 1
            return indicePivot

        triRapide(liste)
        print(liste)
        ```
