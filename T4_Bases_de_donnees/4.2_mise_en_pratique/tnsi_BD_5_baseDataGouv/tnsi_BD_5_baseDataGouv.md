# Exploiter un vrai jeu de donnée

# Mise en pratique sur une vraie base

A partir de maintenant, vous avez les connaissances pour réaliser une application s'appuyant sur une base de données. Il  ne reste plus qu'à les appliquer dans le cadre d'un projet ou un mini projet. Un exemple de mini-projet possible dans le domaine du *BigData* consiste à récupérer des données officielles et à s'aider du langage SQL pour les exploiter.

## Exemple de jeu de données

Une source intéressante pour récupérer des données est **data.gouv.fr**. Voici un exemple de jeu de données : https://www.data.gouv.fr/fr/datasets/resultats-du-controle-sanitaire-de-leau-distribuee-commune-par-commune/#_

La description de chacun des fichiers se trouve ici : https://static.data.gouv.fr/resources/resultats-du-controle-sanitaire-de-leau-distribuee-commune-par-commune/20190710-030936/20190708-eau-distrib-documentation-v4.pdf

1. Téléchargez le fichier dis-* le plus récent. Décompressez le et analysez sa structure.
2. Créez une nouvelle base de données et 3 tables à l'intérieur :
    - Communes
    - Prelevements
    - Resultats
3. Créez dans chacune des tables une clé primaire nommée Id*NomTable* ainsi que des attributs correspondants aux intitulés de colonne
4. A l'aide de Python, lisez chacun des fichiers et peuplez les tables correspondantes.
5. Créez des requêtes SQL afin de vous renseigner sur la qualité de l'eau dans les communes proches de chez vous.

### Création des tables


```python
import sqlite3
bdd = sqlite3.connect("dis_db")
curseur = bdd.cursor()
```


```python
# Creation table Communes
requete = """
CREATE TABLE Communes
(
    IdCommune INTEGER  PRIMARY KEY,
    inseecommune TEXT,
    nomcommune TEXT,
    quartier TEXT,
    cdreseau TEXT,
    nomreseau TEXT,
    debutalim DATE
);"""
curseur.execute(requete)

# Creation des tables Prelevements et Resultats

# YOUR CODE HERE

bdd.commit()
```

### Alimentation de la base de données


```python
# Exemple d'import d'un fichier CSV dans une BDD

import csv

with open('DIS_COM_UDI_2020.txt', encoding='utf-8') as csvfile:
    nb_lignes = 0
    lignes = csv.reader(csvfile)
    entete = True
    for l in lignes:
        if entete:
            entete = False
        else:
            nb_lignes += 1
            requete = f"""
            INSERT INTO Communes
                (inseecommune,nomcommune,quartier,cdreseau,nomreseau,debutalim)
            VALUES
                (?, ?, ?, ?, ?, ?)
            """
            curseur.execute(requete, l)
    bdd.commit()
    print(f"{nb_lignes} enregistrements créés")
```

!!! example "A faire"
    Procédez de même pour le fichier prélèvement

    ```python
    curseur.execute("SELECT COUNT(*) FROM Prelevements;")
    assert curseur.fetchone()[0] == 126730
    ```

!!! example "A faire"
    Procédez de même pour le fichier Resultat

    ```python
    curseur.execute("SELECT COUNT(*) FROM Resultats;")
    assert curseur.fetchone()[0] == 3683342
    ```
### Interrogation de la base de données

Nous avons à présent une vraie base de données avec de vraies données, en nombre conséquent. Une petite requête sur la table Resultats suffit pour s'en convaincre : Plus de 3 millions et demi d'enregistrements !

### Quelques idées de fonctions à créer ! 

- une fonction **liste_communes** prenant en entrée un curseur et un numéro de département et renvoyant la liste des communes dans de département présentes dans la base.
    - La fonction ne renverra pas plusieurs fois la même commune
    - Attention, pour un numéro de département inférieur à 10, if faut penser à ajouter "0"...
    - Le champ *numeroinsee* commence par le numéro du département mais est différent du code postal.

- une fonction **anomalies()** prenant un curseur et un nom de commune et qui renvoie la date et la conclusion du prélévement (champ *conclusionprel* dans **Prelevements** dans la commune) et la référence du prélèvement (champ *referenceprel* dans **Prelevements**) en cas d'anomalie. Vous repèrerez dans la base la phrase type lorsque tout va bien !

- une fonction **resultat()** prenant en paramètres un curseur et une référence de prélèvement et qui renvoie les résultats détaillés de l'analyse avec les informations suivantes :
    - libellé associé à chaque code paramètre, composant la dénomination du paramètre sous forme de texte libre
    - Le résultat de l’analyse physico-chimique ou microbiologique du paramètre
    - L'unité de mesure du paramètre
    - La limite(s) de qualité du paramètre concerné en vigueur  au moment du prélèvement


```python
assert "CAEN" in liste_communes(curseur, 14)
```

```python
anomalies(curseur, "HEROUVILLE-SAINT-CLAIR")
```
```python
resultats(curseur, "01400207768")
```

### Amusez vous

Interrogez la base de données pour rechercher des anomalies dans votre commune ou les environs, et récupérez les résultats détaillés des analyses en cas de problème pour identifier la source de l'anomalie.

Au fil de votre parcours de la base, vous pouvez avoir envie de créer d'autres fonctions pour afficher d'autres informations. Ne vous privez pas !!!


```python
# Amusez vous !
liste_communes(curseur,14)
```

### Pour aller plus loin

Vous avez les outils à présent pout construire une application graphique (avec TKInter par exemple) ou bien un site web (avec PHP ou Flask par exemple) mettant à disposition ces résultats. Cela peut faire l'objet d'un projet.

## Fin du travail

On n'oublie pas de fermer l'accès à la base de données :smiley:

Vous aurez pu constater au cours de vos requêtes que les réponses de la base de données sont immédiates malgré les millions d'enregistrement que celle-ci contient !!

```python
bdd.close()
```
