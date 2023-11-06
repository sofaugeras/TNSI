# Exploiter une base de données avec Python

Dans ce TP, nous allons reprendre notre base de données d'exemples sur les livres, mais nous allons utiliser Python pour exécuter et exploiter les requêtes SQL. 

Notre SGBD sera toujours SQLite : le module python que nous utiliserons se nomme **sqlite3**.

```python
import sqlite3
```

Le module étant importé, nous devons réaliser deux actions pour pouvoir commencer à utiliser notre base :
- ouvrir le fichier de base de données
- créer un curseur

Le *curseur* est un objet python offrant des méthodes pour exécuter des requêtes et récupérer le ou les résultats de ces requêtes.


```python
bdd = sqlite3.connect("livres_db")
curseur = bdd.cursor()
```

*livres_db* est le nom du fichier contenant la base de donnéees SQLite que nous allons exploiter. Si le fichier n'existe pas, une nouvelle base de données sera créée.

## Exécuter des requêtes de sélection

### Le principe

Reste ensuite à exécuter notre première requête. Pour cela, nous utiliserons la méthode **execute()** du curseur, la requête étant une chaîne de caractères passée en paramètre.


```python
requete = "SELECT * FROM Livres;"
curseur.execute(requete)
```

Pour visualiser le résultat de notre requête, nous utiliserons encore notre curseur. Deux méthodes permettent principalement de le faire :
- **fetchone()** pour récupérer un résultat puis avancer le curseur d'un cran
- **fetchall()** pour récupérer d'un coup tous les résultats. 

Regardez les exemples ci-dessous pour mieux comprendre comment fonctionne le curseur : il s'agit littéralement d'un curseur que l'on déplace de résultat en résultat. Vous vous en rendrez compte en exécutant plusieurs fois la cellule ci-dessous.


```python
curseur.fetchone()
```

Vous constatez que le résultat est un *tuple*  dont les éléments correspondent aux attributs sélectionnés : ici c'est \*. Il n'est pas facile de se rappeler de l'ordre des attributs. Pour cela vous pouvez faire appel à la propriété :


```python
curseur.description
```

et pour rendre la réponse plus lisible, une petite liste en compréhension ;). Et voilà les attributs de colonne en clair dans l'ordre ou ils apparaissent dans le résultat de la requête !


```python
[d[0] for d in curseur.description]
```

A présent, le fonctionnement de **fetchall()** ne devrait pas vous étonner : on récupère logiquement un tuple avec tous les résultats.


```python
curseur.fetchall()
```

Si vous avez suivi les instructions précédentes, vous devriez constater qu'il manque des enregistrements. Pourquoi ?
Un indice : si vous réexécutez une nouvelle fois la méthode **fetchall()** du curseur, celle-ci ne renverra rien !

Et oui, c'est la notion de curseur qui se déplace au fur à mesure qu'unb résultat est donné : les précédents appels de **fetchone()** ont fait avancer le curseur, et de même, **fetchall()** positionne le curseur à la toute fin.

Pour retrouver tous les résultats à nouveau, il faut réexécuter la requête. Evitez donc de mélanger **fetchone()** et **fetchall()** sous peine de ne plus trop savoir ou en est le curseur et ce que vous récupérez.

Voici donc le moyen le plus simple de récupérer tous les résultats d'une requête d'un coup.


```python
curseur.execute(requete)
resultats = curseur.fetchall()
resultats
```

### Construire des requêtes à partir de variables python

Nous allons dans l'exemple suivant écrire une fonction **prenom()** 
- qui prend en paramètre un curseur et un nom d'auteur
- qui renvoie son prénom

Si le nom de l'auteur ne figure pas dans la table *Auteurs*, la fonction renverra **None**.


```python
def prenom(c, nom):
    requete = "SELECT PrenomAuteur FROM Auteurs WHERE NomAuteur = ?"
    c.execute(requete, [nom])
    r = c.fetchall()
    if len(r) == 0:
        return None
    elif len(r) == 1:
        return r[0][0]
```


```python
prenom(curseur, "Verne")
```

### Explications

Dans cet exemple, nous construisons une requête à partir d'une variable Python. SQLite propose un mécanisme de substitution sécurisé permettant d'injecter une ou plusieurs variables à l'intérieur d'une requête. **C'est ce mécanisme que vous devez utiliser** : ne construisez pas vous même la chaîne de caractère contenant la requête complète, c'est une mauvaise pratique qui vous conduira inévitablement à des problèmes.

Pour utiliser ce mécanisme de substitution, vous devez
- mettre des **?** dans votre requête à l'emplacement de la variable à insérer
- passer en second paramètre la liste des valeurs à substituer dans la requête

C'est simple, fiable et sécurisé, en particulier contre les [injections SQL](https://xkcd.com/327/) !

### A vous de jouer

Ecrivez une fonction **romans()** 
- qui prend en paramètre un curseur et un nom d'auteur
- qui renvoie une liste de *Titres* de romans écrits par cet auteur

Si le nom de l'auteur ne figure pas dans la table *Auteurs*, la fonction renverra **None**.


```python
def romans(c, nom):
    # YOUR CODE HERE
```


```python
assert romans(curseur, "Asimov") == ['Fondation', 'Les Robots', 'La Fin de l’éternité']
assert romans(curseur, "Verne") == ['De la Terre à la Lune']
```

## Insérer de nouveaux enregistrements

Les requêtes de modification sur la base se font de la même manière que les requêtes de sélection, à une petite subtilité près : après exécution de la requête, il faudra faire appel à la méthode **commit()** de l'objet *bdd* (issu de la connexion) afin que les modifications soient prises en compte dans le fichier de base de données. 

**Attention** : Si vous oubliez l'appel à commit, vos modifications seront perdues lorsque vous quitterez votre programme car elles ne seront pas inscrites dans le fichier de la base de données.


```python
requete = """
INSERT INTO Auteurs 
  (NomAuteur, PrenomAuteur, IdLangue, AnneeNaissance)
VALUES
  ('Lecluse', 'Olivier', 2, 1870);
"""

curseur.execute(requete)
bdd.commit()
```

la propriété **lastrowid** peut être intéressante car elle donne accès à la clé primaire créée automatiquement pour notre nouvel enregistrement. En voici une utilisation :


```python
last_id = curseur.lastrowid
last_id 
```


```python
requete = "SELECT * FROM Auteurs WHERE IdAuteur = ?"
curseur.execute(requete, [last_id])
curseur.fetchone()
```

### A vous de jouer
Effacez de la table auteur ce dernier enregistrement que nous avons créé.


```python
# YOUR CODE HERE
```


```python
requete = "SELECT COUNT(*) from Auteurs"
curseur.execute(requete)
assert curseur.fetchone()[0] == 10
```


```python
curseur.execute("SELECT * FROM Auteurs")
curseur.fetchall()
```

## Pour Finir

Notre travail sur la BDD exemple est à présent terminé. Afin de fermer le fichier proprement et de s'assurer que les données saisies seront bien inscrites dans le fichier, il faut *impérativement* appeler la méthode **close()** sur l'objet *bdd* :


```python
bdd.close()
```


```python
curseur
```

A partir de ce moment là, plus acune opération n'est possible sur la base de données comme le montre la cellule suivante :


```python
requete = "SELECT COUNT(*) from Auteurs"
curseur.execute(requete)
```
