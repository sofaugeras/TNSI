"""Code Python contenant un bogue

Contexte :
  => le programme affiche les nombres pairs jusqu'à une certaine limite saisie par l'utilisateur

Ce qu'on attend du script :
  => si limite=10 alors 0 2 4 6 8
  => si limite=13 alors 0 2 4 6 8 10 12

Ce qui se produit vraiment :
  => tout fonctionne bien pour 10, mais pas pour 13 (serait-ce parce qu'il porte malheur ?)
"""

# Variables du programme
limite = 0
nombre = 0


# Bannière du programme
print("****************************")
print("*** Affichapairator v0.1 ***")
print("****************************")

# Saisie de la limite par l'utilisateur
limite = int(input("Saisir la valeur limite : "))

# Affichage des nombres pairs
while nombre != limite:
    print(f"{nombre} ", end="")
    nombre += 2