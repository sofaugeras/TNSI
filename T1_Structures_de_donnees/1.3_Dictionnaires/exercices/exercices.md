
!!! abstract "Entrainement"
    Pour s'entraîner avec les dictionnaires, c'est [ici](https://e-nsi.gitlab.io/pratique/tags/#3-dictionnaire)

# Un peu de cyber

## A quoi sert un mot de passe ?

• **Accès** à des services en ligne grâce au contrôle d’accès.<br/>
• **Imputabilité**, preuve de qui a fait quoi.<br/>
• **Traçabilité** des actions, historique des actions.<br/>

Exemple, <br/>
^^télédéclaration de l’impôt :^^ imputabilité = lien entre la déclaration et la personne *ET* traçabilité = connaître l’heure et la date de la déclaration.

## un mot de passe, c'est 

• La connaissance :point_right: JE CONNAIS<br/>
• La possession :point_right: JE POSSEDE<br/>
• Les caractéristiques biométriques :point_right: JE SUIS<br/>

![source : https://www.apog.net/deploiement-solution-mfa-indispensable](./data/Facteurs.jpg){: .center width=90%}

## Les risques 

• **Divulgation :**<br/>

> - Par négligence : faiblesse d’une personne, support amovible, diffusion à un tiers.<br/>
> - Par un service non sécurisé : protocoles https, imaps, pop3s, etc… à privilégier.<br/>
> - Par l’utilisation d’un vecteur infecté.<br/>
> - Mot de passe enregistré sans protection.<br/>

• **Malveillance :**<br/>

> - Authentification sur un service illégitime.<br/>
> - Attaque par ingénierie sociale, piège.<br/>
> - Attaque par force brute ou divulgation d’une base de données mal sécurisée.<br/>

• Ces deux cas de figure peuvent entraîner :<br/>

> - La compromission des messages personnels.<br/>
> - La destruction de données.<br/>
> - La publication de messages ou photos préjudiciables sur les réseaux sociaux par exemple.<br/>
> - Des achats.<br/>
> - Des virements bancaires.<br/>

## Craquer un mot de passe

- Par **force brute**<br/>
- Par **dictionnaire**, en général avant l’attaque par force brute<br/>
- Par **permutation** en échangeant des caractères (exemple : E par 3 ou O par 0).<br/>

## Mais un souci de temps

une image plutôt qu'un long discours :

![temps de craquage par force brute d'un mdp](./data/etude-hive-systems-mots-de-passe.jpg){: .center width=90%}

## Comment construire un mot de passe fort ? 🔐

Le mot de passe doit apporter un niveau de sécurité suffisant, c’est-à-dire difficile à découvrir par un attaquant dans un temps raisonnable à  l’aide d’outils automatisés de recherche qui mettent en oeuvre les différentes techniques d’attaque. Il doit être composé au minimum de *10 caractères* et ceux-ci doivent être de tout type.

!!! info "Préconisations ANSI"
    Créez un mot de passe suffisamment long, complexe et inattendu : de 8 caractères minimum et contenant des minuscules, des majuscules, des chiffres et des caractères spéciaux. [source](https://cyber.gouv.fr/bonnes-pratiques-protegez-vous)

Quelques astuces : 
- Grâce à une [phrase de passe](https://www.cnil.fr/fr/generer-un-mot-de-passe-solide) avec des mots concaténés.
- Par phonétique.
- Les premières lettres des mots d’une phrase, citation, chanson, etc…
- Mixer les trois méthodes.

!!! note "Activité Phrase de passe"

    === "Manipulation de chaîne de caractère"

        🔽 Télécharger le notebook Activité correspondant [ici](./data/phrase_de_passe-v2.ipynb)<br />
    === "correction"

        🔽 Télécharger le notebook Activité corrigé [ici](./data/phrase_de_passe-v2-Corrige.ipynb)

!!! abstract "**Création d'une rainbow table** :rainbow:"
    === "Objectif"

        Créer une fonction ```inverse_md5()``` qui va chercher dans un dictionnaire (construit préalablement) le mot correspondant au hash donné en paramètre.

        Exemple : 
        ```
        >>> inverse_md5('0571749e2ac330a7455809c6b0e7af90')
        >>> 'sunshine'
        ```

        **Aide :**

        - liste de 1000 mots de passe fréquents : [ici](http://glassus1.free.fr/extraitrockyou.txt)
        - comment lire / convertir le contenu d'un fichier dans une liste de ```string``` :
        ```python
        lst = open("monfichier.txt").read().splitlines()
        ```
        - comment calculer du MD5 en Python : 
        ```python
        import hashlib
        result = hashlib.md5('azerty'.encode())
        print(result.hexdigest())
        ```
    === "Correction"

        ```python
        import hashlib

        def inverse_md5(h, dico) :
            """
            fonction qui va chercher dans un dictionnaire passé en paramètre
            le mot correspondant au hash donné en paramètre.
            >>> inverse_md5('0571749e2ac330a7455809c6b0e7af90')
            >>> 'sunshine'
            @param entree : h : chaine de caractère : hash du mdp à rechercher
                            dico : dictionnaire de correspondance hash/mdp
            @param sortie : chaine de caractère : un mot de passe
            """
            return  dico[h]
            
        def contruct_dico():
            dico = {}
            lst = open("extraitrockyou.txt").read().splitlines()
            for elt in lst:
                h = hashlib.md5(elt.encode())
                dico[h.hexdigest()] = elt
                
            return dico

        dico = contruct_dico()
        print(inverse_md5('48238b7f2aa5f76a1d1e119f8942ebe7', dico))
        ```

## Stockage d'un mot de passe

La règle de "base" en hygiène de codeur est de ne JAMAiS stocké un mot de passe en clair, que ce soit dans un fichier ou pire dans une base de données. Un site ne doit jamais être en capacité de vous communiquer votre mot de passe initial !

Le seul moment où un mot de passe est en clair est quand il est saisi dans le champ du formulaire. <br />
Imaginons ... Si tous les sites avaient tous la même méthode de chiffrement (MD5 ou SH256) et qu'un utilisateur utilisait le même mot de passe sur tous ces sites ...

Il existe des fuites de données recensant le couple identifiant/mot de passe d'un grand nombre de personne ! <br />
Vous pouvez tester votre adresse mail sur le site [';--have i been pwned?](https://haveibeenpwned.com/) pour savoir si celle ci appartient à une fuite de données connue.


^^Mise en exemple :^^ <br />
Alphonse (al@mail.com) utilise le mot de passe "secret" pour les sites monsite.fr et concurrent.fr<br />
Chacun des deux sites utilise la même méthode de chiffrement MD5.<br />
Donc chacun des deux sites possèdent dans sa base le couple `al@mail.com` et `5ebe2294ecd0e0f08eab7690d2a6ee69`.<br />
monsite.fr subit une attaque et une fuite de données massive.<br />
le pirate possède donc le moyen de se connecter à concurrent.fr avec le compte d'alphonse...

C'est la que l'on introduit la notion de **salage**.

^^Définition :^^ Le salage est un procédé utilisé en cryptographie pour renforcer la sécurité des mots de passe stockés. Il consiste à ajouter une valeur aléatoire unique (appelée "sel" ou "salt") à chaque mot de passe avant de le hacher. Cela rend plus difficile pour les attaquants d'utiliser des attaques par table arc-en-ciel ou par dictionnaire, car même si deux utilisateurs ont le même mot de passe, leurs hashs seront différents grâce aux sels uniques.

```python linenums='1'
import hashlib

# generate new salt, hash password
# h est le sel qui sera utilisé pour le hachage
h = b"monsite.fr"
# Hash du mot de passe classique sans salage
pwd_md5 = hashlib.md5(b"secret").hexdigest()
print(pwd_md5)
# Hash du mot de passe classique avec salage
pwd = hashlib.pbkdf2_hmac('md5', b"secret", h, 100000)
print(pwd)
```
```
5ebe2294ecd0e0f08eab7690d2a6ee69
b'\xc3;K\xc2\xfb\xb4z\xca`f\xc4T\xc9I\x1b.'
```