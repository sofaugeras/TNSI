
!!! abstract "Entrainement"
    Pour s'entraîner avec les dictionnaires, c'est [ici](https://e-nsi.gitlab.io/pratique/tags/#3-dictionnaire)


!!! abstract "**Création d'une rainbow table** :rainbow:"
    === "Objectif"

        Créer une fonction ```inverse_md5()``` qui va chercher dans un dictionnaire (construit préalablement) le mot correspondant au hash donné en paramètre.

        Exemple : 
        ```
        >>> inverse_md5('0571749e2ac330a7455809c6b0e7af90')
        >>> 'sunshine'
        ```

        **Aide :**

        - liste de 1000 mots de passe fréquents : [ici](http://glassus1.free.fr/extraitrockyou.txt)
        - comment lire / convertir le contenu d'un fichier dans une liste de ```string``` :
        ```python
        lst = open("monfichier.txt").read().splitlines()
        ```
        - comment calculer du MD5 en Python : 
        ```python
        import hashlib
        result = hashlib.md5('azerty'.encode())
        print(result.hexdigest())
        ```
    === "Correction"

        ```python
        import hashlib

        def inverse_md5(h, dico) :
            """
            fonction qui va chercher dans un dictionnaire passé en paramètre
            le mot correspondant au hash donné en paramètre.
            >>> inverse_md5('0571749e2ac330a7455809c6b0e7af90')
            >>> 'sunshine'
            @param entree : h : chaine de caractère : hash du mdp à rechercher
                            dico : dictionnaire de correspondance hash/mdp
            @param sortie : chaine de caractère : un mot de passe
            """
            return  dico[h]
            
        def contruct_dico():
            dico = {}
            lst = open("extraitrockyou.txt").read().splitlines()
            for elt in lst:
                h = hashlib.md5(elt.encode())
                dico[h.hexdigest()] = elt
                
            return dico

        dico = contruct_dico()
        print(inverse_md5('48238b7f2aa5f76a1d1e119f8942ebe7', dico))
        ```
