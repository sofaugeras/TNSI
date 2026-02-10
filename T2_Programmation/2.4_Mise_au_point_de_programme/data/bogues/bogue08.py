"""Code Python contenant un bogue

Contexte :
  => simulateur de fusée

Ce qu'on attend du script :
  => des messages d'avertissement selon l'accélération de la fusée. En effet le pilote
  n'a pas forcément de notion du danger selon la valeur brute de l'accélération

Ce qui se produit vraiment :
  => aucun message d'alerte à 3G, le pilote ne freine pas, la fusée explose
"""

# Variables du programme
acceleration_fusee = 0.0
etat_fusee = True


def verifier_et_conseiller(acceleration):
    if acceleration == 1.0:
        print("\033[30;32mOK, accélération de 1G\033[00m")
    if acceleration == 2.0:
        print("\033[30;33mAttention, accélération de 2G \033[00m")
    if acceleration == 3.0:
        print("\033[30;31mUrgence, accélération de 3G, veuillez freiner\033[00m")


# Bannière du programme
print("************************")
print("*** Accelerator v0.1 ***")
print("************************")


# On simule le pilotage de la fusée
while etat_fusee == True:
    choix = input("Que voulez-vous faire (a=accélérer et f=freiner) : ")
    if choix == "a":
        acceleration_fusee += 0.2
        print(f"J'accélère : acceleration_fusee = {acceleration_fusee:.2f}")
    if choix == "f":
        acceleration_fusee -= 0.2
        print(f"Je freine  : acceleration_fusee = {acceleration_fusee:.2f}")

    verifier_et_conseiller(acceleration_fusee)
    if acceleration_fusee > 3.1:
        print("!!! Explosion !!!")
        etat_fusee = False