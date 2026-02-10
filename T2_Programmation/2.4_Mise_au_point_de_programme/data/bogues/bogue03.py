"""Code Python contenant un bogue

Contexte :
  => un enseignant souhaite modifier les notes d'un devoir

Ce qu'on attend du script :
  => qu'il modifie toutes les notes en dessous la moyenne, par une note = 10

Ce qui se produit vraiment :
  => les moyennes sont identiques avant et après modification
"""


def cloner(notes):
    """Clone un tableau de notes passé en paramètre"""
    nouvelles_notes = notes
    return nouvelles_notes


def modifier(notes):
    """Modifie les notes pour éviter les notes en dessous 10"""
    for i in range(len(notes)):
        if notes[i] < 10:
            notes[i] = 10
    return notes

def calculer_moyenne(notes):
    """Calcule la moyenne des notes du devoir"""
    somme = 0
    for note in notes:
        somme += note
    return somme / len(notes)


# Bannière du programme
print("************************")
print("*** Augmentator v0.1 ***")
print("************************")

# Le dévoir a eu lieu, voici les notes...
anciennces_notes = [10, 8, 13, 7, 6]

# Modification des notes en dessous la moyenne
nouvelles_notes = cloner(anciennces_notes)
nouvelles_notes = modifier(nouvelles_notes)

# Comparaison des moyennes avant et après modification
print("Moyenne anciennes notes =>", calculer_moyenne(anciennces_notes) )
print("Moyenne nouvelles notes =>", calculer_moyenne(nouvelles_notes) )

# Bizarre on obtient la même moyenne ...



