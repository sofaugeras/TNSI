"""Code Python contenant un bogue

Contexte :
  => on souhaite proposer un programme qui calcule y = 3 * 2 * x

Ce qu'on attend du script :
  => pour 2, on devrait obtenir : y = 3 * 2 * 2 = 12
  => pour 4, on devrait obtenir : y = 3 * 2 * 4 = 24
  => pour 5, on devrait obtenir : y = 3 * 2 * 5 = 30

Ce qui se produit vraiment :
  => pour 2, on obtient y = 66 au lieu de 12
  => pour 4, on obtient y = 132 au lieu de 24
  => pour 5, on obtient y = 165 au lieu de 30
"""

def doubler(x):
    """Double la valeur du paramètre"""
    resultat = x * 2
    return resultat

def tripler(y):
    """Triple la valeur du paramètre"""
    resultat = int(y) * 3
    return resultat


# Bannière du programme
print("****************************")
print("*** Tripladoublator v0.1 ***")
print("****************************")

# Saisie utilisateur et calcul
nombre = input("Saisir un nombre : ")
print( tripler(doubler(nombre)) )

