"""
Script qui cherche le 1001 ième nombre premier

Cette première version n'est semble-t-il pas très optimisée et l'analyse
des performances devrait révéler quelques pistes d'améliorations possibles
"""


def etre_premier(n):
    """Détermine si le nombre n est premier ou pas

    Parameters:
        n (int) : nombre à tester

    Returns:
        (boolean) : True si le nombre est premier, False sinon
    """
    # Tests des cas particuliers
    if n <= 1:
        return False
    else:
        # Boucle testant tous les facteurs possibles de 2 à n-1
        # Si on en trouve un, le nombre n'est pas premier...
        facteur = 2
        while facteur < n:
            if (n % facteur) == 0:
                return False
            facteur += 1

        # Si aucun facteur n'a été trouvé, il est premier
        return True


def rechercher_nieme_nombre_premier(rang):
    """Recherche le nième nombre premier

    Parameters:
        rang (int) : rang du nombre premier à trouver

    Returns:
         (int) : le nième nombre premier
    """
    # Initialisations des variables
    compteur_nombres_premiers = 0
    nombre = 1

    #  Boucle de recherche
    while compteur_nombres_premiers != rang:
        nombre += 1
        if etre_premier(nombre) == True:
            compteur_nombres_premiers += 1

    # On retourne le nième nombre premier
    return nombre


if __name__ == "__main__":
    #  Lancement de la fonction
    rang = 2000
    resultat = rechercher_nieme_nombre_premier(2000)
    print(f"Le {rang}ième nombre premier est {resultat}")
