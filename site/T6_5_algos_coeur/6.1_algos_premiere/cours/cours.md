# algos de première 1️⃣

## Minimum

??? note "Minimun"
    Fonction qui renvoie le minimum d'une liste de nombres ou None si vide.

    ===  "solution itérative 1"
        Parcours élément par élément

        ```python
        def minimum(liste):
        if liste != []:
            minimum = liste[0]
            for element in liste:
                if element < minimum:
                    minimum = element
            return minimum
        ```

    ===  "solution itérative 2"
        Parcours à l'aide des indices

        ```python
            def minimum(liste):
                if liste != []:
                    indice_minimum = 0
                    for indice in range(len(liste):
                        if liste[indice] < liste[indice_minimum]:
                            indice_minimum = indice
                return liste[indice_minimum]

        ```
    ===  "solution récursive"
        Informatiom : "liste.pop()" supprime le dernier élément de la liste et le renvoie. La liste est, ici, supposée non vide.

            ```python
            def minimum(liste):
                """Renvoie le minimum de la liste d'entiers, supposée non vide

                Parameters
                ----------
                    liste : list(int)

                Returns
                -------
                    int
                    
                exemple
                -------
                >>> minimum([15,7,8,9])
                7
                >>> minimum([6])
                6
                
                """
                assert liste != [], "Une liste vide n'a pas de minimum"
                l = liste[:]
                if len(l) == 1:
                    return l[0]
                else:
                    min1 = l.pop()
                    min2 = minimum(l)
                    if min1 < min2:
                        return min1
                    else:
                        return min2
            ```

## Maximum

??? note "Maximum"
    Fonction qui renvoie le maximum d'une liste de nombres ou None si vide.

    ```python
    def maximum(liste):
        if liste != []:
            maximum = liste[0]
            for i in range(len(liste)):
                if liste[i] > maximum:
                    maximum = liste[i]
            return maximum
    ```

## Indice du minimum et du maximum

??? note "Indice du minimum et du maximum"
    Fonction qui renvoie un tuple (indice du minimum, indice du maximum) d'une liste de nombres ou None si la liste est vide.

    ```python
    def indice_mini_maxi(liste):
        if liste != []:
            indice_minimum, indice_maximum = 0, 0
            for indice in range(len(liste)):
                if liste[indice] < liste[indice_minimum]:
                    indice_minimum = indice
                elif liste[indice] > liste[indice_maximum]:
                    indice_maximum = indice
            return (indicice_minimum, indice_maximum)
    ```

## Chaîne à l'envers

??? note "A l'envers"
    Fonction qui renvoie une chaîne de caractère à l'envers.

    ```python
    def renverse(chaine):
        """Renvoie la chaîne de caractère renversée, le dernier caractère devient le premier, l'avant dernier
        le deuxième et ainsi de suite...

        param : 
            chaine : str
        return :
            str
        
        exemple :
        >>> renverse("Bonjour")
        'ruojnoB'

        >>> renverse("")
        ''
        """
        renverse = ""
        for caractere in chaine:
            renverse = caractere + renverse
        return renverse
    ```
## Nombre d'occurrence

??? note "Compter le nombre d'occurrences"
    Fonction qui compte le nombre d'occurrences d'un caractère dans une chaîne.

    ```python
    def nombre_occurrences(chaine, carac):
        '''Renvoie le nombre d'occurrences de carac dans chaine

        param : 
            chaine : str
            carac : str
        return :
            int
        
        exemple :
        >>> nombre_occurences("bonjour","o")
        2
        >>> nombre_occurences("bonjour","z")
        0
        '''
        compteur = 0
        for car in chaine:
            if car == carac:
                compteur = compteur +1
        return compteur
    ```

## Indice de la première occurrence

??? note "Indice de la première occurrence"
    Fonction qui renvoie l'indice de la première occurrence d'un caractère dans une chaîne. Retourne -1 si la valeur n'est pas dans la chaîne.
    === "solution 1"
        Avec une boucle  ```for```

            ```python
            def indice(car, string):
            """Renvoie l'indice de la première occurrence du caractère car dans la chaine string. 
            Renvoie -1 si car n'est pas dans string.

            param :
                string : str
                car : str
            return :
                int

            exemple : 
            >>> indice("o", "Bonjour")
            1
            >>> indice("a", "Bonjour")
            -1
            """
            
            for indice in range(len(string)):
                if string[indice] == car:
                    return indice
            return -1
            ```
    === "solution 2"
        Avec une boucle ```while```

            ```python
            def indice(car, string):
                """Renvoie l'indice de la première occurrence du caractère car dans la chaine string. Renvoie -1 si car n'est pas dans string.

                param :
                    string : str
                    car : str
                return :
                    int

                exemple : 
                >>> indice("o", "Bonjour")
                1
                >>> indice("a", "Bonjour")
                -1
                """
                
                indice = 0
                while indice < len(string):
                    if string[indice] == car:
                        return indice
                    indice = indice + 1
                return -1
            ```

## Recherche dichotomique

??? note "Recherche dichotomique"
    Fonction qui renvoie la position d'un élément dans une liste, ou False si l'élément ne s'y trouve pas. Le principe de dichotomie est utilisé.

    ```python
    def recherche_dicho(val, table):
        '''
        recherche la position de la valeur  dans la table
        
        param :
            table : list : liste ordonnée de valeurs
            val : type identique aux éléments de la liste
        
        return : 
            int : position de la valeur dans table
            False : si valeur n'est pas dans table
        
        Exemple :
        >>> recherche_dicho(14, [10, 11, 11, 12, 13, 15, 18, 23, 41])
        >>> recherche_dicho(23, [10, 11, 11, 12, 13, 15, 18, 23, 41])
        7
        
        '''
        d = 0
        f = len(table)-1
        while d<=f:
            m = (d+f) // 2
            if table[m] == val :
                return m
            elif val > table[m]:
                d = m+1
            else:
                f = m -1
        return False
    ```

## Conversion décimal vers binaire

??? note "Conversion décimal vers binaire"
    Fonction qui à partir d'un entier sous la forme décimal renvoie sa version binaire

    === "version 1"

        ```python
        def conv_dec_bin(entier):
            """ cette fonction permet de convertir un nombre entier en binaire

            param
            -----
            entier : int
            
            return
            ------
            str : chaine de caractères composée de 0 et de 1 
            
            exemples:
            ---------
            >>> conv_dec_bin(13)
            '1101'
            
            >>> conv_dec_bin(192)
            '11000000'
            
            """
            reponse = ""
            if entier == 0:
                return "0"
            else:
                while entier !=0:
                    reste = entier%2
                    reponse = str(reste) + reponse 
                    entier = entier//2
            return reponse
        ```

    === "version 2"

        ```python
        def conv_dec_bin(entier):
            """ cette fonction permet de convertir un nombre entier en binaire

            param
            -----
            entier : int
            
            return
            ------
            str : chaine de caractères composée de 0 et de 1 
            
            exemples:
            ---------
            >>> conv_dec_bin(13)
            '1101'
            
            >>> conv_dec_bin(192)
            '11000000'
            
            """
            exposant = 0
            reponse = ""
            while 2**exposant < entier:
                exposant += 1
            while entier != 0:
                exposant = exposant -1
                if 2**exposant > entier:
                    reponse = reponse + "0"
                else:
                    reponse = reponse + "1"
                    entier = entier - 2**exposant
                
            reponse = reponse +"0"*exposant
            return reponse
        ```

## Conversion binaire vers décimal

??? note "Conversion binaire vers décimal"
    Fonction qui à partir d'un nombre écrit sous forme binaire renvoie sa forme décimal

    === "version 1"

        ```python
        def conv_bin_dec(binaire):
            """ cette fonction permet de convertir un nombre en binaire en décimal.

                param
                -----
                binaire : str
                
                return
                ------
                int 
                
                exemples:
                ---------
                >>> conv_bin_dec('1101')
                13
                >>> conv_bin_dec('11000000')
                192

                """
            assert binaire != "","La chaîne doit être non vide"
            resultat = 0
            for chiffre in binaire:
                resultat = 2 * resultat + int(chiffre)
            return resultat
        ```
    === "version 2"

        ```python
        def conv_bin_dec(binaire):
            """ cette fonction permet de convertir un nombre en binaire en décimal.

                param
                -----
                binaire : str
                
                return
                ------
                int 
                
                exemples:
                ---------
                >>> conv_bin_dec('1101')
                13
                >>> conv_bin_dec('11000000')
                192

                """
            assert binaire != "","La chaîne doit être non vide"
            longueur = len(binaire)
            resultat = 0
            for indice in range(longueur):
                resultat = resultat + int(binaire[indice])*2**(longueur - 1- indice)
            return resultat
        ```

## Moyenne d'une liste de nombres

??? note "Moyenne d'une liste de nombres"
    Fonction qui renvoie la moyenne d'une liste de nombres et None si la liste est vide
    
    ```python
    def moyenne(liste):
        """renvoie la valeur moyenne d'une liste de nombres et None en cas de liste vide.

        param:
            liste : list
        return :
            float

        exemple :

        >>> moyenne([1,2,4])
        3.5
        >>> moyenne([])

        """
        if liste != []:
            somme = 0
            for elt in liste:
                somme = somme +elt
            return somme/len(liste)
    ```