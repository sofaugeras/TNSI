"""Code Python contenant un bogue

Contexte :
  => pas important

Ce qu'on attend du script :
  => qu'il transforme "bateau" en "_b_a_t_e_a_u_"

Ce qui se produit vraiment :
  => on obtient bizarrement "u_" au lieu de "_b_a_t_e_a_u_"
"""


def ajouter_underscores(mot):
    """Ajoute des underscores entre les lettres d'un mot

    Examples:
        velo => _v_e_l_o_
        train => _t_r_a_in_
        voiture => _v_o_i_t_u_r_e_

    Parameters:
        mot (string) : mot à transformer

    Returns:
        (string) : mot transformé avec des underscores intercalés
    """
    nouveau_mot = "_"
    for i in range(len(mot)):
        nouveau_mot = mot[i] + "_"
    return nouveau_mot


# Bannière du programme
print("**************************")
print("*** Underscorator v0.1 ***")
print("**************************")

# Saisie utilisateur et affichage du résultat
mot_de_test = input("Saisir un mot : ")
resultat = ajouter_underscores(mot_de_test)
print(resultat)
