def moyenne(éléments):
    if len(éléments) == 0:
        raise ValueError("Pas de moyenne pour le vide.")
    return sum(éléments) / len(éléments)
