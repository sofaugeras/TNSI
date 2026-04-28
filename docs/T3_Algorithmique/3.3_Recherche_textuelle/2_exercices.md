# Exercices

## Exercice 1 - EP25_sujet 31
!!! example "Exercice 1 - EP25_sujet 31"
    === "Enoncé"
        Écrire une fonction recherche_motif qui prend en paramètre une chaîne de caractères motif non vide et une chaîne de caractères texte et qui renvoie la liste des positions de motif dans texte. Si motif n’apparaît pas, la fonction renvoie une liste vide.
        Exemples:

        ```bash
        >>> recherche_motif("ab", "")
        []
        >>> recherche_motif("ab", "cdcdcdcd")
        []
        >>> recherche_motif("ab", "abracadabra")
        [0, 7]
        >>> recherche_motif("ab", "abracadabraab")
        [0, 7, 11]
        ```

    === "Correction"

        ```python linenums='1'
        def recherche_motif(motif, texte):
            sol = []
            i = 0
            while i <= len(texte) - len(motif):
                j = 0
                while j < len(motif) and motif[j] == texte[j+i]:
                    j += 1
                if j == len(motif):
                    sol.append(i)
                i += 1
            return sol
        ```
        
## Exercice 2

!!! example "exercice 2"
    === "Enoncé"
        Questions 14 et 15 de l'exercice 3 du [Sujet Métropole Septembre 2025](./data/25-NSIJ1ME3.pdf){. target="_blank"}

        ```python linenums='1'
        def recherche_seq(seq, chaine):
            """Renvoie l'indice du premier caractère de
            chaine où commence `seq` si la séquence `seq`
            se trouve dans la chaine de caractères chaine,
            -1 sinon
            Paramètres:
            seq : séquence à rechercher
            chaine : chaine d'ADN
            Renvoie:
            indice du premier caractère de seq dans
            la chaine, -1 sinon.
            """
            for i in range(len(chaine)-len(seq) + 1):
                j = 0
                while j < len(seq) and ...:
                    j += 1
                if ...:
                    return i
            return -1
        ```

    === "Correction Q14"

        ```python linenums='1'
        def recherche_seq(seq, chaine):
            '''Renvoie l'indice du premier caractère de
            chaine où commence `seq` si la séquence `seq`
            se trouve dans la chaine de caractères chaine,
            -1 sinon
            Paramètres:
            seq : séquence à rechercher
            chaine : chaine d'ADN
            Renvoie:
            indice du premier caractère de seq dans
            la chaine, -1 sinon.
            '''
            for i in range(len(chaine)-len(seq) + 1):
                j = 0
                while j < len(seq) and chaine[i+j] == seq[j]:
                    j += 1
                if j == len(seq):
                    return i
            return -1
        ```
    === "Correction Q15"

        Cet algorithme permet de faire des décalages intelligents si la lettre sur laquelle on est positionné fait partie ```seq```. Cela accélère considérablement la recherche par rapport à l'algorithme ```recherche_seq```. 

## Exercice 3 Dictionnaire d'occurrence

Lien vers [Codex](https://codex.forge.apps.education.fr/exercices/dico_occurrences/){ target="_blank" }
