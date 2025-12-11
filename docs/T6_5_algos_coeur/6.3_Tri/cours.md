# Algos de tris ♻️

## Comparaison des Tris
![image](data/comparaisons.gif){: .center}

## Tri par insertion

??? note "Tri par insertion"
    Fonction qui prend comme paramètre une liste et trie cette liste en place (c'est-à-dire que la liste initiale est modifiée) en utilisant l'algorithme de tri par insertion. Plusieurs versions proposées .
    === "Version1"
        Tri en place, itératif

        ```python
        def insere(donnees, indice):
            """insere la donnee d'indice indice à sa bonne place dans la liste formée des
            éléments d'indice inférieur ou égaux à indice.
            Le début de la liste est sensé être trié.
            LA MODIFICATION SE FAIT EN PLACE
             
            param :
                donnees : list
                indice : int
                    
            exemple :
            >>> a = [3, 9, 5, 6, 4, 1]
            >>> insere(a, 2)
            >>> a
            [3, 5, 9, 6, 4, 1]
                
            """
            while indice>0 and donnees[indice]<donnees[indice-1]:
                donnees[indice-1], donnees[indice] = donnees[indice], donnees[indice-1]
                indice = indice -1

        def tri_insertion(donnees):
            """tri la liste données en place, avec l'algorithme de tri par insertion
            LE TRI SE FAIT EN PLACE.
                
            param :
                donnees : list
                    
            exemple :
            >>> liste3 = [ "ruby", "python", "logo", "elan", "rust"]
            >>> tri_insertion(liste3)
            >>> liste3
            ['elan', 'logo', 'python', 'ruby', 'rust']
                
            """
            for ind in range(len(donnees)):
                insere(donnees,ind)
        ```

    === "Version 2"
        Tri itératif qui renvoie une nouvelle liste

        ```python
        def insere2(liste, valeur):
            """Insère la valeur dans la liste, supposée triée. la modification est en place

            param :
                liste : list : liste de nombres
                valeur : float/int
                return :
                    list : nouvelle liste avec la valeur insérée

            Exemple:
                >>> liste1 = [3,5.2,6]
                >>> insere2(liste1, 4)
                >>> liste1
                [3, 4, 5.2, 6]
                """
            liste.append(valeur)
            indice = len(liste)-1
            while indice>0 and liste[indice-1] > liste[indice]:
                liste[indice],liste[indice-1] = liste[indice-1],liste[indice]
                indice = indice - 1
                

        def tri_insertion2(liste):
            """renvoie une nouvelle liste qui est une version triée de liste

             param :
                    liste : list
            return :
                    liste

            Exemple :
                >>> tri_insertion2([8,2,6,5])
                [2, 5, 6, 8]
                """
            liste_triee = []
            for element in liste:
                insere2(liste_triee, element)
            return liste_triee
        ```

    === "Version 3"
        Tri récursif qui renvoie une nouvelle liste

        ```python
        def insere3(liste, valeur):
        """Insère la valeur dans la liste, supposée triée

            param :
                liste : list : liste de nombres
                   valeur : float/int
            return :
                 list : nouvelle liste avec la valeur insérée

            Exemple:
                >>> liste1 = [3,5.2,6]
                >>> liste2 = insere3(liste1, 4)
                >>> liste2
                [3, 4, 5.2, 6]
        """
            if liste == []:
                return [valeur]
            elif liste[-1]>valeur:
                return insere3(liste[:-1],valeur) + [liste[-1]]
            else:
                return liste + [valeur]

         def tri_recursif_insertion3(liste):
        """renvoie une nouvelle liste qui est une version triée de liste. Méthode récursive.

            param :
                liste : list
            return :
                liste

            Exemple :
            >>> tri_recursif_insertion3([8,2,6,5])
                [2, 5, 6, 8]
         """
            if liste == []:
                return []
            else:
                return insere3(tri_recursif_insertion3(liste[:-1]),liste[-1])

        ```

## Tri par sélection

??? note "Tri par sélection"
    Fonction qui renvoie la liste triée par ordre croissant.

    ```python
    def index_min(donnees, indice):
        """retourne l'indice du plus petit élément d'une liste, à partir d'un indice donné
        Exemple:  
        >>> index_min(["curl", "bash", "python", "cilk", "nesl"], 0)
        1
        >>> index_min(["curl", "bash", "python", "cilk", "nesl"], 2)
        3 
        """
        pos = indice
        for i in range(indice, len(donnees)):
            if donnees[i]<donnees[pos] :
                pos = i
        return pos

    def tri_selection(donnees):
        """tri la liste donnees en place, avec l'algorithme de tri par sélection
        >>> liste3 = [ "ruby", "python", "logo", "elan", "rust"]
        >>> tri_selection(liste3)
        >>> liste3
        ['elan', 'logo', 'python', 'ruby', 'rust'] 
        """
        for i in range(len(donnees)-1):
            j = index_min(donnees,i)
            donnees[i], donnees[j] = donnees[j], donnees[i]
    ```

## Tri fusion

??? note "Algorithme de tri fusion (*merge sort*) :heart: :heart: :heart:"

    ```python
    def interclassement(lst1, lst2):
        lst_totale = []
        n1, n2 = len(lst1), len(lst2)
        i1, i2 = 0, 0
        while i1 < n1 and i2 < n2:
            if lst1[i1] < lst2[i2]:
                lst_totale.append(lst1[i1])
                i1 += 1
            else:
                lst_totale.append(lst2[i2])
                i2 += 1
        return lst_totale + lst1[i1:] + lst2[i2:]

    def tri_fusion(lst):
        if len(lst) <= 1:
            return lst
        else:
            m = len(lst) // 2
            return interclassement(tri_fusion(lst[:m]), tri_fusion(lst[m:]))
    ```
