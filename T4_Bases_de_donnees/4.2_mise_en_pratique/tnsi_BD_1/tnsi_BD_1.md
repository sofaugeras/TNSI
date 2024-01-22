# Découverte du langage SQL

!!! note "Téléchargement"
    Vous pouvez télécharger le notebook du cours [ici](./data/tnsi_BD_1.ipynb)

Dans ce TP jous allons découvrir le langage SQL (*Structured Query Language*) qui est le langage utilisé pour
effectuer des requêtes sur une base de données relationnelles. Nous apprendrons lors de ce TP à : <br />
- créer des tables avec les attributs que l'on souhaite<br />
- insérer des enregistrements<br />
- faire des requêtes sur la base pour extraire des informations

Contrairement aux apparences, nous n'utiliserons pas Python dans ce classeur, mais directement SQL grâce à l'extension **ipython-sql** qu'il faut activer en ouvrant une console Anaconda prompt et taper les commandes suivantes :

 ```Python Console Session
pip install jupyter-sql
pip install ipython-sql
```
puis relancer jupyter.

On charge le module SQL avec la commande suivante

```Python Console Session
%load_ext sql
```

## Créer la base de données

Nous allons commencer par créer une base vide dans laquelle nous allons travailler :

```python
%sql sqlite:///livres_db
```

La base s'appelle **livres_db** et est au format *sqlite* qui est un gestionnaire de base de données relationnelles léger et facile à prendre en main.<br />

Les données seront inscrites dans le fichier **livres_db** qui vient d'être créé à côté de ce classeur et que vous pourrez retrouver dans votre travail de travail quand vous aurez fini ce chapitre.<br />

L'objectif est de peupler une base de données avec la base **livres** dont voici le modèle relationnel. Cette base sera constituée de 4 tables :

<code>
LANGUE (<u>idLangue</u> int, langue str)<br />
AUTEUR (<u>idAuteur</u>> int, nom str, prenom str, anneeNaissance int, #idLangue int)<br />
THEME (<u>idTheme</u> int, theme str)<br />
LIVRE (<u>idLivre</u> int, titre str, #idAuteur int, #idTheme int)
</code>

## Créer une table

Il est temps de commencer à peupler notre base de données. Nous allons commencer par créer la table **Langues** en saisissant notre première requête :


```sql
%%sql 
CREATE TABLE Langues 
(
IdLangue INTEGER  PRIMARY KEY,
Langue   TEXT
);
```

### Quelques explications :

Pour commencer, dans jupyter lorsque nous voulons taper une commande **SQL** et non du langage python. Pour cela, nous inscrirons **en première ligne de cellule** la commande *magique* `%%sql`. N'oubliez jamais de commencer toutes vos cellules ainsi car sinon, la commande sera interprétée par *python* et non *SQL*.

La première requête **SQL** que nous allons apprendre est la requête `CREATE TABLE`<br />
- on indique le nom de la table à créer<br />
- entre parenthèse on liste les *attributs* à mettre ainsi que leur *type*.<br />
- une requête se termine **toujours** par ;

Nous avons deux types différents dans notre base de données :<br />
- le type TEXT pour tout ce qui est chaîne de caractères<br />
- le type INTEGER pour les entiers

L'attribut **IdLangue** est la :key: **clé primaire** de la table. C'est un entier qui commence à 1 et qui sera automatiquement incrémenté au fur à mesure que l'on insère des données dans la table. C'est en indiquant `PRIMARY KEY` après le type dans la déclaration de l'attribut **IdLangue** que *sqlite* se comporte ainsi.

## Insérer des enregistrements dans la table

Maintenant que nous avons une table vide, il nous faut la remplir avec les données sur les auteurs. Nous utiliserons pour cela la requête **INSERT**. Voici son utilisation :

```sql
%%sql
INSERT INTO Langues 
    (Langue)
VALUES
    ("Anglais"),
    ("Français");
```

### Quelques explications :

La requête **INSERT** s'utilise ainsi :

```sql
INSERT INTO ##TABLE##
    (## attributs dont on donne les valeurs##)
VALUES
    (## enregistrement 1 ##),
    ...
    (## enregistrement n ##);
```

On peut refaire une autre requête **INSERT** à la suite si on souhaite ajouter encore des données au bout de la table. 

Vous remarquez que l'on ne donne pas de valeur pour l'attribut **IdLangue**. C'est parce qu'on l'a déclaré en `PRIMARY KEY`. Il est donc automatiquement géré par sqlite. Nous verrons cela en lisant le contenu complet de la table.

On est pas obligé de préciser tous les attributs. **IdLangue** est un exemple particulier, mais il est possible d'omettre d'autres attributs. Ils seront alors affectés d'une valeur nulle.

A l'issue de la requête, sqlite nous informe que 2 lignes ont été créées.

## Lire le contenu d'une table

Nous allons à présent utiliser une requête **SELECT** afin de récupérer le contenu de la table. Ces requêtes peuvent être très sophistiquées comme on va le voir en fin de TP. Pour le moment, nous nous contenterons de la forme la plus simple :


```sql
%%sql

SELECT * FROM Langues;
```

```text
     * sqlite:///livres_db
    Done.
```   

<table>
    <tr>
        <th>IdLangue</th>
        <th>Langue</th>
    </tr>
    <tr>
        <td>1</td>
        <td>Anglais</td>
    </tr>
    <tr>
        <td>2</td>
        <td>Français</td>
    </tr>
</table>

Vous voyez donc appraître le contenu de la table. Vous constatez que la clé primaire **IdLangue** a bien été générée correctement.

Il est possible de stocker le résultat de cette requête dans une variable pour l'exploiter plus facilement dans jupyter. Voici comment procéder en modifiant légèrement la première ligne :


```python
resultat = %sql SELECT * FROM Langues;
```

Vous voyez au passage la syntaxe concise permettant de récupérer le résultat d'une requête dans une variable. Cette variable résultat est exploitable dans ce classeur, y compris par python !!

!!! example "A faire"
    Essayer de manipuler la variable `resultat` avec print, type. Essayer de sélectionner le premier élément

On a donc ici le meilleur des deux mondes : des requêtes **SQL** et une base de données pour stocker efficacement les données, le langage python pour traiter ces données grâce à des algorithmes faciles à écrire.

## Table Auteur

!!! example "A faire"
    Créez la table Auteurs afin que celle-ci reflète les informations suivantes :

|   Nom    |    Prenom    | annee naissance |  langue  |
|----------|--------------|-----------|----------|
|  Orwell  |    George    |    1903   | Anglais  |
| Herbert  |    Frank     |    1920   | Anglais  | 
|  Asimov  |    Isaac     |    1920   | Anglais  |
|  Huxley  |    Aldous    |    1894   | Anglais  |  
| Bradbury |     Ray      |    1920   | Anglais  | 
| K. Dick  |    Philip    |    1928   | Anglais  |  
| Barjavel |     René     |    1911   | Français | 
|  Boulle  |    Pierre    |    1912   | Français |  
| Van Vogt | Alfred Elton |    1912   | Anglais  | 
|  Verne   |    Jules     |    1828   | Français |  

Pour cela, vous utiliserez la commande suivante pour créer la table et vous adapterez les données à cette structure.

```sql
%%sql 
CREATE TABLE Auteurs (
    IdAuteur       INTEGER  PRIMARY KEY,
    NomAuteur      TEXT,
    PrenomAuteur   TEXT,
    IdLangue       INTEGER,
    AnneeNaissance INTEGER,
    FOREIGN KEY(IdLangue) REFERENCES Langues(IdLangue)
);
```

Une nouveauté apparaît ici dans la création de la table : La table **Auteurs** possède une *clé étangère* : *IdLangue*. Cette clé est un entier.

Remarquez la ligne `FOREIGN KEY(IdLangue) REFERENCES Langues(IdLangue)`. Celle-ci permet de déclarer une *contrainte* sur cette clé afin d'indiquer à SQLite que *IdLangue* est une clé étrangère. SQLite sera alors responsable de maintenir la cohérence entre les deux tables que l'on a ainsi reliée.

Cette déclaration est obligatoire pour garantir l'intégrité référentielle de la base de données.

!!! example "A faire"
    === "Requete"
        Ajoutez les occurrences d'auteur à la la table Auteurs afin que celle-ci reflète les informations ci dessus :

        ```sql
        %%sql 

        INSERT INTO Auteurs (idAuteur, NomAuteur, ...)
        VALUES
        (1, "Orwell", "Georges", ...)
        ```
    === "Correction"


## Table Theme et Table Livre

Notre base n'est pas encore complète : il nous reste à créer les tables **Livres** et **Themes** qui doivent refléter le contenu suivant :

|           Titre           |   NomAuteur    |    PrenomAuteur    | AnneeNaissance |  Langue  | AnneePubli | Themes |
|---------------------------|----------|--------------|-----------|----------|-----------|------|
|            1984           |  Orwell  |    George    |    1903   | Anglais  |    1949   |  Totalitarisme, science-fiction, anticipation, Dystopie  |
|            Dune           | Herbert  |    Frank     |    1920   | Anglais  |    1965   | science-fiction, anticipation   |
|         Fondation         |  Asimov  |    Isaac     |    1920   | Anglais  |    1951   |  science-fiction, Economie  |
|   Le meilleur des mondes  |  Huxley  |    Aldous    |    1894   | Anglais  |    1931   |  Totalitarisme, science fiction, dystopie   |
|       Fahrenheit 451      | Bradbury |     Ray      |    1920   | Anglais  |    1953   |   	science-fiction, Dystopie  |
|            Ubik           | K. Dick  |    Philip    |    1928   | Anglais  |    1969   |  	science-fiction, anticipation   |
|   Chroniques martiennes   | Bradbury |     Ray      |    1920   | Anglais  |    1950   |   	science-fiction, anticipation   |
|     La nuit des temps     | Barjavel |     René     |    1911   | Français |    1968   |   	science-fiction, tragédie   |
|        Blade Runner       | K. Dick  |    Philip    |    1928   | Anglais  |    1968   |   	Intelligence artificielle, science fiction  |
|         Les Robots        |  Asimov  |    Isaac     |    1920   | Anglais  |    1950   |  science fiction, Intelligence artificielle   |
|   La Planète des singes   |  Boulle  |    Pierre    |    1912   | Français |    1963   |   	science fiction, Dystopie   |
|           Ravage          | Barjavel |     René     |    1911   | Français |    1943   |  Science-Fiction, anticipation   |
| Le Maître du Haut Château | K. Dick  |    Philip    |    1928   | Anglais  |    1962   |   	Dystopie, Uchronie  |
|       Le monde des A      | Van Vogt | Alfred Elton |    1912   | Anglais  |    1945   |   	science fiction, IA   |
|    La Fin de l’éternité   |  Asimov  |    Isaac     |    1920   | Anglais  |    1955   |  science-fiction, voyage dans le temps  |
|   De la Terre à la Lune   |  Verne   |    Jules     |    1828   | Français |    1865   |   	Science-Fiction, aventure  |

### La table LIVRES

La table **LIVRES** devra avoir la structure décrite dans l'extrait suivant :

| IdLivre |           Titre           | IdAuteur | AnneePubli |
|----|---------------------------|-----------|-----------|
| ...  |            ...          |     ...     |    ...   |
| 8  |     La nuit des temps     |     7     |    1968   |
| ...  |            ...          |     ...     |    ...   |

- l'année de publication est de type **INTEGER**
- **IdLivre** désigne bien sûr la clé primaire
- **IdAuteur** est une *clé externe* faisant référence à l'auteur.
- dans l'extrait, la clé **IdAuteur** vaut 7. L'auteur de *La nuit des temps* est donc *Barjavel*
- on ne renseigne pas la langue ou l'année de naissance de l'auteur car ces informations sont déjà présentes dans la table **Auteurs**.
- On traitera la problématique des thèmes plus tard...


!!! exampe "A faire"
    === "Requete"
        saisissez la requête pour créer la table **Livres** puis insérer les données dans la table 

        Vérifiez votre travail en listant tous les enregistrements de la table **LIVRES** dans la variable `resultat`

        ```python
        assert (1, '1984', 1, 1949) in resultat
        ```
    === "Correction"


### La table Themes

Traitons à présent la problématique des Thèmes. La table Themes devra avoir la structure décrite dans l'extrait suivant :

| IdTheme | Intitule |
|----|----------|
| 1 |    Science-fiction     |
| ...  |   ...     |

- **IdTheme** désigne bien sûr la clé primaire
- **Intitule** est un champ texte contenant l'intitulé du thème tel qu'il apparaît dans le tableau global.

!!! example "A faire" 
    Dans la cellule ci-dessous, vous saisirez donc 2 requêtes :<br />
    - Une pour créer la table Themes<br />
    - Une pour insérer les données dans la table.

    Vérifiez votre travail en lisant tous les enregistrements de la table **Themes** dans la variable `resultat`

    ```python
    assert (1, "Science-fiction") in resultat
    ```

### Une table manquante !

La saisie de notre base de donnée est incomplète ! Nous avons en effet saisi tous les auteurs, tous les livres, toutes les langues, tous les thèmes et pourtant il manque une information. Laquelle ?

Quelle solution envisager pour saisir cette information ?

!!! example "A faire"
    Créer une table **RelationsLivreTheme** mettant en relation les livres et les thèmes associés. Saisir le contenu de cette table.


```python
resultat = %sql SELECT IdLivre, IdTheme FROM RelationsLivreTheme;
assert (1, 1) in resultat
```

## Cardinalité

En regardant notre base de données et les relations que nous avons créé entre les tables, on remarque que celles-ci ont des *cardinalités* différentes. La *cardinalité* d'une relation entre deux tables **A** et **B** exprime à combien d'enregistrements de **A** peut être relié chaque enregistrement de **B**.

Par exemple, à un livre est associé un auteur unique, mais pour un auteur donné, il peut y avoir plusieurs livres. On parle alors de **relation de 1 à n**

Lorsque plusieurs enregistrements de la table **A** peuvent être associés à plusieurs enregistrements de la table **B**, on parle alors d'une **relation de n à n**

!!! example "A vous de jouer"
    Citez dans la base de données<br />
    - une relation de 1 à n<br />
    - une relation de n à n

### Table de relation

Pour une **relation de n à n**, nous aurons en général recours à la création d'une nouvelle table de relation contenant les clés externes des tables à mettre en relation. C'est ce que nous avons mis en oeuvre pour la table **RelationsLivreTheme**.

