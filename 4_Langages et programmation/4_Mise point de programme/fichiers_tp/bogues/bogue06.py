"""Code Python contenant un bogue

Contexte :
  => le programme sert à suivre le poids d'une personne

Ce qu'on attend du script :
  => qu'il mémorise bien les changements d'informations, ici le poids devrait être de 82kg

Ce qui se produit vraiment :
  => Après une session de raclette dantesque, le poids reste le même 80kg, au lieu de 82kg
"""


# Variable du programme
poids = 80


# Définitions des fonctions
def afficher_poids():
    print("Mon poids est de %d kg" % (poids))

def modifier_poids(nouveau_poids):
    poids = nouveau_poids
    print("Mon nouveau poids est de %d kg" % (poids))


# Bannière du programme
print("************************")
print("*** Raclettator v0.1 ***")
print("************************")

print("Avant la raclette")
afficher_poids()
modifier_poids(82)
print("Après la raclette")
afficher_poids()