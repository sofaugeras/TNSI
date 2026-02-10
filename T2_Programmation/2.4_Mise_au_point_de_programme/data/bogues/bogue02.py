"""Code Python contenant un bogue

Contexte :
  => pas important

Ce qu'on attend du script :
  => qu'il supprime les voyelles d'un mot

Ce qui se produit vraiment :
  => ne semble fonctionner que pour la voyelle o ???
"""


def supprimer_les_voyelles(mot):
    """Supprime les voyelles d'un mot

    Parameters:
        mot (string) : mot dont on souhaite supprimer les voyelles

    Returns:
        (string) : le mot modifié ne contenant plus de voyelle(s)
    """
    nouveau_mot = ""
    les_voyelles = ('a', 'e', 'i', 'o', 'u')
    for lettre in mot.lower():
      if lettre in les_voyelles:
          nouveau_mot = mot.replace(lettre, "")
          print(nouveau_mot)
    return nouveau_mot


# Bannière du programme
print("***********************")
print("*** Voyellator v0.1 ***")
print("***********************")

# Quelques tests
print(supprimer_les_voyelles("hello"))
print(supprimer_les_voyelles("world"))
print(supprimer_les_voyelles("allo"))