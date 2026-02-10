"""Code Python contenant un bogue

Contexte :
  => un programme qui informe un utilisateur de ses droits selon son âge

Ce qu'on attend du script :
  => qu'il affiche les bonnes informations à savoir
    si age >= 18, alors voter + parier
    si age < 18, alors attendre d'être adulte

Ce qui se produit vraiment :
  => un enfant de 8 ans peut parier /!\
"""

# Les variables utilisées
age = 0
pouvoir_voter = False
pouvoir_parier = False


# Bannière du programme
print("************************")
print("*** Verificator v0.1 ***")
print("************************")

# L'utilisateur entre son âge
age = int(input("Entrez votre âge : "))


# Application des vérifications selon son âge
if age < 18:
    pouvoir_voter = False
else:
    pouvoir_voter = True
pouvoir_parier = True


# Affichage des informations selon l'âge de la personne
print(f"Comme vous avez {age} ans, vous pouvez :")
if pouvoir_voter == True:
    print(" - voter")
if pouvoir_parier == True:
    print(" - parier")
if pouvoir_voter == False and pouvoir_parier == False:
    print(" - attendre")


