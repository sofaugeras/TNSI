# tests & bugs

!!! note "Source"

    Date : 15/10/2020 - Ensemble Scolaire Niort<br />
    - Antoine MAROT <br />
    - David SALLÉ <br />
    - Julien SIMONNEAU 

    Ce document est mis à disposition selon les termes de la licence ``Creative Commons BY-NC-SA 4.0``
 
??? question "Table des matières"

    Table des matières
    ```text
    1 - Introduction	3
        1.1 - Plan	3
        1.2 - Un peu d’histoire	4
        1.3 - Vue d’ensemble	5
        1.4 - Conseils	5
        1.5 - Erreur avec l’interpréteur Python	6
    2 - Les exceptions	7
        2.1 - Utiliser try/except	8
        2.2 - Différenciation	8
        2.3 - Et quoi qu’il arrive...	9
        2.4 - Lever soi même une Exception	9
    3 - Bogues et débogueur	10
        3.1 - Causes des bogues	10
        3.2 - Outil de débogage	10
        3.3 - Source d’information	11
    4 - Tests unitaires	12
        4.1 - Introduction 	12
            4.1.1 - Avantages/inconvénients	12
            4.1.2 - Outils	12
        4.2 - Mise en œuvre	13
            4.2.1 - Fonctionnement 	13
            4.2.2 - Module calculs.py 	13
            4.2.3 - Tests unitaires avec les assertions	14
            4.2.4 - Tests unitaires avec la librairie unittest	15
    5 - Optimisation des performances	18
        5.1 - Principe	18
        5.2 - Chronométrage simple	18
        5.3 - Profilage	18
    ```

## 1 - Introduction

En préambule de ce sujet, quelques éléments de réflexion avec les vidéos suivantes.

- [Les bugs en informatique | Gérard Berry](https://www.youtube.com/watch?v=qE0QFxNiQLI)
- [Comment rendre l'informatique plus sûre](https://www.youtube.com/watch?v=PZLvXESq82c)

### 1.1 - Plan

Ce document présente quelques notions autours de la mise au point des programmes :

·	gestion des erreurs/exceptions
·	gestion des bugs
·	tests unitaires
·	analyse des performances

Débutons par un slogan en informatique !

![feature](./data/itsnotabug.jpg){: width=20% .center}

### 1.2 - Un peu d’histoire

L’histoire de l’informatique est truffée d’inventions et de grandes réalisations, mais aussi parfois de désastres industriels. Les conséquences peuvent aller de simples erreurs au plantage complet du système en passant par les failles de sécurité.

Quelques exemples de bugs ou bogues tristement connus :

|Quand	|Quoi	|Conséquence|
|:--:|:--:|:--:|
|1947	|Un insecte (bug in english) est venu créer un faux contact entre 2 relais électromécaniques de l’ordinateur Harvard Mark II. ![](./data/1947.jpg){: width=20% .center}|Une simple erreur|
|1991|	Une erreur d’arrondi pour passer d’un entier à un réel sur 24 bits a engendré une erreur de 600m dans les calculs de trajectoire du système anti-missile Patriot.![](./data/1991.png){: width=20% .center}|	Mort de 28 soldats américains|
|1996|	Un dépassement d’entier dans le programme d’Ariane5 qui avait été en partie copié/collé d’Ariane4. Mais les variables utilisées ne convenaient plus en taille pour la puissance d’Ariane 5	![](./data/1996.jpg){: width=20% .center}|Explosion de la fusée|
|1997	|Quelques jours après son arrivée sur Mars, le robot Sojourner de la mission Pathfinder se bloque à cause d’une inversion de priorité dans ses tâches. Le problème sera corrigé à distance depuis la Terre![](./data/1997.jpg){: width=20% .center}|Retard dans la mission|
|2014	|Le célèbre clip Gangnam Style provoque un débordement d’entier dans le compteur de vue de la plateforme Youtube![](./data/2014.png){: width=30% .center} |	Rien de particulier|
|2038	|Un dépassement d’entier dans la gestion de la date. Y2038 en écho à Y2000 (bug de l’an 2000) appaîtra peut-être dans les systèmes 32 bits qui compte les secondes à partir du 1er janvier 1970 pour gérer la date du système. ![](./data/2038.png){: width=30% .center}  |	L’année deviendra 1901 au lieu de 2038|

D’autres exemples ici : [Wikipedia List_of_software_bugs](https://en.wikipedia.org/wiki/List_of_software_bugs)

### 1.3 - Vue d’ensemble

Lorsqu’on programme en Python (et dans les autres langages également), on est rapidement confronté à 3 types d’erreurs.

|Type d’erreur|	Description|	Difficulté à résoudre|
|:--:|:--:|:--:|
|Syntaxe liée au langage	|Le code source comporte des erreurs et l’interpréteur n’arrive pas à l’exécuter. Il vous indique en général l'emplacement de l'erreur. <br /> <font color='green'>*Solution : se référer au message de l’interpréteur Python et vérifier la syntaxe*</font>	|Facile|
|Valeur ou action inappropriée|	Le programme se lance bien, mais dans certaines conditions “plante”.<br /> <font color='green'>*Solution : se référer au message d’erreur de l’interpréteur Python et vérifier les valeurs notamment à l’aide d’un débogueur*</font>|	Difficile|
|Conception de l’algorithme|	Le programme se lance bien, ne plante pas, mais ne produit pas le résultat escompté <br /><font color='green'> *Solution : revoir l’algorithme utilisé et les étapes de l’exécution du programme avec un débogueur*	</font>|Très difficile|


### 1.4 - Conseils

Conseils lorsqu’on créé un script Python :

-	corriger les erreurs de syntaxe
-	anticiper les erreurs de saisie de l’utilisateur, imaginer le pire
-	tester unitairement (entrées => sorties, cas limite avec 0, “”, tous les cas de figure if/else)
-	vérifier les boucles while et leurs conditions de sortie (invariant)
-	contrôler les erreurs avec try/except
-	se méfier des calculs et comparaisons avec les nombres flottants

### 1.5 - Erreur avec l’interpréteur Python


Anatomie d’un message d’erreur de l’interpréteur Python :

![interpréeteur](./data/interpréteur.png){: width=80% .center}

A noter que quand on utilise des fonctions qui appellent d’autres fonctions, le message d’erreur retrace tout le parcours et il faut commencer à lire par la fin.

Quelques erreurs courantes liées au langage Python :

|Type|	Description|exemple|
|:--:|:--|:--|
|**SyntaxError**|Erreur de syntaxe | -	confusion entre ``=`` et ``==``<br/> -	oubli d’une parenthèse ``(`` ou ``)``<br/>-	oubli d’un délimiteur de string ``“`` ou ``‘`` ou ``“””``<br/>-	oubli du ``:`` annonçant un bloc|
|**NameError**|Erreur sur le nom d’une variable ou fonction|- mauvais nom<br/>- déclaration au mauvais endroit<br/>- oubli d’import d’un module|
|**IndentationError**|Erreur d’indentation|- mauvais alignement<br/>- mélange d’espaces et tabulations (Python3)|
|**TypeError**|	Erreur sur les types|- addition impossible entre ``int`` et ``string``<br/>- arrondi d’un ``string``|
|**AssertionError**	|Erreur issue d’un test unitaire||
|**ZeroDivisionError**	|Erreur de division par 0||
|**KeyError**	|Erreur sur un dictionnaire||
|**IOError**|	Erreur lors d’un entrée/sortie (fichier...)||

## 2 - Les exceptions

Toutes les erreurs du tableau précédent sont en fait des exceptions qui héritent de la même classe mère ``Exception``.

![arbre des exceptions](./data/pileException.jpg){: width=80% .center}
 
Lorsque Python lève une exception telle que celles présentes dans le tableau, le programme est stoppé immédiatement et un message d’erreur est affiché pour prévenir l’utilisateur de la cause du problème.

Prenons l’exemple de ce programme qui saisit un nombre et calcule son inverse :
```python
#version normale
x = int(input("Saisir x : "))
print("1/x =", 1/x)
```
Selon ce que va saisir l’utilisateur, le résultat sera très différent. En cas de mauvaise saisie, le programme stoppe.

|Saisie d’un entier<br />``x=4``	|Saisie d’un string<br />``x=”2”``|Saisie d’un entier<br />``x = 0``|
||||
|Saisir x : 4<br />1/x = 0.25|Traceback (...):  File "test.py", line 1...<br />ValueError: invalid literal for int() with base 10: '"2"'|Traceback (...):  File "/test.py", line 2...<br />ZeroDivisionError: division by zero|

### 2.1 - Utiliser try/except

Cependant parfois, il est plus intéressant de **capturer**/**trapper**  cette exception de manière à informer l’utilisateur du problème et lui proposer une alternative, plutôt que de stopper brutalement le programme.

Pour cela on utilisera les mot-clefs ``try`` et ``except`` :

-	``try`` va débuter un bloc d’instructions à risque, susceptible de générer une erreur
-	``except`` va intercepter l’erreur pour éviter l’arrêt brutal du programme et proposer un traitement du problème, souvent un affichage

Le modèle est celui-ci :

```python
try:
    # Code à risque
except Exception as erreur:
    # Traitement de l'erreur (affichage...)
```
Pour le programme qui calcule l’inverse cela donnerait :
```python
# Version avec capture simple et affichage de l'erreur
try:
    x = int(input("Saisir x : "))
    print("1/x =", 1 / x)
except Exception as erreur:
    print("Erreur :", erreur)
```
### 2.2 - Différenciation

Si l’on souhaite différencier le traitement des erreurs, il faudra ajouter plusieurs blocs except, typiquement un par type d’erreur
```python
# Version avec capture et traitement différenciés
try:
    x = int(input("Saisir x : "))
    print("1/x =", 1 / x)
except ValueError as erreur:
    print("Erreur de saisie :", erreur)
except ZeroDivisionError as erreur:
    print("Impossible de diviser par zéro :", erreur)
```
### 2.3 - Et quoi qu’il arrive...

On peut également ajouter un bloc d’instructions qui sera exécuté quoiqu’il arrive : erreur ou comportement normal. Pour cela on ajoutera à la fin le mot clef ``finally`` :
```python
# Version avec capture et traitement différenciés et
# quoiqu'il arrive un message de fin
try:
    x = int(input("Saisir x : "))
    print("1/x =", 1 / x)
except ValueError as erreur:
    print("Erreur de saisie :", erreur)
except ZeroDivisionError as erreur:
    print("Impossible de diviser par zéro :", erreur)
finally:
    print("Merci d'avoir utiliser ce calculateur")
```

### 2.4 - Lever soi même une Exception

Quand on écrit son propre module Python avec ses fonctions, ses classes, ses méthodes, on a souvent besoin de lever nous même des exceptions sans attendre l’interpréteur Python.

A l’aide du mot-clef ``raise``, on peut lever une exception à tout moment.
```python
# Levée d'exception
x = int(input("Saisir x : "))
if x == 13:
    raise ValueError("Désolé, je suis superstitieux")
print("1/x =", 1/x)
```
Celle-ci sera interceptée par un bloc ``try/except ``ou pas. Il est également possible de définir ses propres exceptions personnalisées en la rattachant à la classe ``Exception`` via l’héritage.

```python
# Définition d'une Exception personnalisée
class SuperstitionError(Exception):
    """Classe représentation l'erreur liée au nombre 13"""
    pass

# Levée d'une exception personnalisée
x = int(input("Saisir x : "))
if x == 13:
    raise SuperstitionError("Désolé, je suis superstitieux")
print("1/x =", 1/x)
```

## 3 - Bogues et débogueur

### 3.1 - Causes des bogues

Dans la suite de ce chapitre, on tentera de présenter sommairement les causes les plus courantes des bogues dans les programmes.

-	Problème de typage
-	Effet de bord non désiré
-	Débordement dans un tableau
-	Instruction conditionnelle non exhaustive
-	Mauvais choix d’inégalité
-	Calcul/comparaison de nombres flottants
-	Débordement d’entier
-	Mauvaise indentation

### 3.2 - Outil de débogage

Le **débogueur** est un outil intégré dans la majorité des IDE (++control+arrow-up+y++ dans VSCode). Il permet de fixer des points d’arrêt (breakpoints) et de consulter l’état des variables (watches). On peut ensuite avancer pas à pas en mode :

- ++f9++ : Ajouter/Supprimer un point d'arrêt (breakpoint)
- ++f5++ : Démarrer/Continuer le débogage
- ++f11++ : Entrer dans une fonction (Step Into)
- ++arrow-up+f11++ : Sortir d'une fonction (Step Out)
- ++f10++ : Passer à la ligne suivante (Step Over)
- ++arrow-up+f5++ : Arrêter le débogage
- ++control+arrow-up+f5++ : Redémarrer le débogage

#### Exemple d’utilisation dans VSCode

**Etape 1 :** on fixe un point d’arrêt dans le programme dans la zone à déboguer (Affichage > Console de débogage ou icone à gauche)
![etape 1](./data/E1.png){: width=50% .center}
**Etape 2 :** on lance l’exécution du programme en mode debug (++f5++) et on visualise l’état des variables
 Soit dans la zone “watches”, Soit directement dans le code (survol des variables avec la souris)
![Etape 2](./data/E2.png){: width=50% .center}
**Etape 3 :** on avance pas à pas avec la touche ++f10++
![Etape 3](./data/E3.png){: width=50% .center}
**Etape 4 :** on reboucle à l’étape 4 jusqu’à trouver l’origine du bogue

### 3.3 - Source d’information

Où trouver de l’aide quand on a un bogue :

-	[https://stackoverflow.com/](https://stackoverflow.com/)
-	[https://github.com/](https://github.com/)

Les types de vulnérabilités les plus courantes liées à des bogues :

-	[https://www.cvedetails.com/vulnerabilities-by-types.php](https://www.cvedetails.com/vulnerabilities-by-types.php)
-	[https://owasp.org/www-project-top-ten/](https://owasp.org/www-project-top-ten/)


##  4 - Tests unitaires

### 4.1 - Introduction

Les tests unitaires consistent à vérifier le bon fonctionnement d’une portion de code informatique, typiquement une fonction.
Ils s’inscrivent dans une démarche plus générale de tests qui consiste à valider qu’un produit répond bien au besoin exprimé en amont. Pyramide des tests :
![pyramide des tests](./data/test.png){: width=50% .center}

Certaines méthodes de développement comme **TDD** (Test Driven Development) propose même d’écrire les tests avant le code source.

![TDD](./data/TDD.png){: width=50% .center}

#### 4.1.1 - Avantages/inconvénients

**:white_check_mark: Avantages :**  

-	s’assurer du bon fonctionnement
-	trouver des bugs le plus tôt possible
-	garantir la non régression du code après la correction d’un bug
-	servir de documentation et d’exemple en complément de l’API

**:x: Inconvénients :**	cela peut être long et fastidieux à réaliser

#### 4.1.2 - Outils

Plusieurs outils sont disponibles dont certains seront présentés en détails dans la suite du document :

-	``assert`` : mot clef Python
-	``unittest`` : librairie standard de tests unitaires
-	``doctest`` : librairie standard utilisant les tests unitaires dans les docstring
-	``pytest``  : libraire de tests unitaires

### 4.2 - Mise en œuvre

#### 4.2.1 - Fonctionnement

Imaginons que vous avez écrit un module Python nommé ``calculs.py`` contenant différentes fonctions.<br />
Pour réaliser des tests unitaires sur votre module, vous allez devoir créer un nouveau fichier ``test_calculs.py`` dont le rôle sera de valider le bon fonctionnement de votre module ``rectangle.py``.

Cela se fera en 3 étapes :

1.	**initialisation** (setUp) : préparation d’un environnement pour exécuter le test (fixture)
2.	**vérification** (test_xxx) : comparaison du résultat obtenu avec le résultat escompté
3.	**désactivation** (tearDown) : désinstallation de l’environnement de test afin de le pas polluer les tests suivants

Les tests doivent être indépendants et reproductibles, c’est ce qui explique les étapes 1 et 3.

#### 4.2.2 - Module calculs.py

Soit le module ``calculs.py ``ci-dessous à tester.
```python
def additionner(a, b):
    """Calcule et retourne la somme de a et b"""
    return a * b

def etre_pair(n):
    """Test la parité d'un nombre"""
    if n % 2 == 0:
        return True
    else:
        return False
```

Vous aurez noter que le développeur a fait une faute de frappe dans la fonction ``additionner()`` en remplaçant le signe ``+`` par ``*``.
Tout l’intérêt des tests unitaires va être de repérer cette erreur suffisamment tôt, idéalement avant l’intégration du module ``calcul.py`` dans un autre projet. Car une fois intégré, l’erreur peut s’avérer beaucoup plus longue et complexe à trouver et corriger.


#### 4.2.3 - Tests unitaires avec les assertions

Afin de tester ce module ``calculs.py``, il va falloir créer un fichier test_calculs.py contenant nos tests unitaires.
Ce fichier va utiliser le mot clef Python ``assert`` pour vérifier que le résultat produit par une fonction et bien conforme aux attentes. Si ce n’est pas le cas une erreur ``AssertionError`` stoppe le programme.

```python
# Assertion vraie, ne produisant pas d'erreur
assert 1 == 1, "1 doit être égal à 1"

# Assertion fausse, produisant une AssertionError
assert 1 == 0, "1 = 0 devrait lever une erreur"

Traceback (most recent call last):
  File "tests_assert.py", line 4, in <module>
    assert 1 == 0, "1 = 0 devrait lever une erreur"
AssertionError
```

Pour les tests unitaires du module ``calculs.py``, on pourrait écrire les assertions suivantes :

```python
# Importation du module à tester et ses fonctions
from calculs import additionner, etre_pair

# Tests unitaires de la fonction additionner()
assert additionner(2, 2) == 4, "2 + 2 = 4"
assert additionner(0, 0) == 0, "0 + 0 = 0"
assert additionner(11, 5) == 16, "11 + 5 = 16"

# Tests unitaires de la fonction etre_pair()
assert etre_pair(5) == False, "5 n’est pas pair"
assert etre_pair(4) == True, "4 est pair"
assert etre_pair(0) == True, "0 est pair"
```

Le lancement de test_calculs.py produira alors l’erreur suivante :
```python
Traceback (most recent call last):
  File "tests_calculs.py", line 7, in <module>
    assert additionner(11, 5) == 16, "11 + 5 = 16"
AssertionError
```

Notre script de tests unitaires a bien repéré une erreur sur la fonction ``additionner()`` qu’il devrait être aisé de corriger.<br/>
A noter que les 2 premiers tests sont passés malgré l’erreur de codage, d’où l’importance d’être le plus exhaustif possible dans l’écriture des tests.

Cependant on pourra remarquer quelques faiblesses avec cette méthode ``assert`` :

-	le script s’est arrêté à la première erreur, donc on ne sait pas si la fonction ``etre_pair()`` est correcte
-	quand tous les tests passeront avec succès, le script ne produira rien
-	certains tests sont plus difficiles à réaliser avec ``assert`` (chaînes de caractères, sortie affichage, plusieurs fonctions...)
-	si chaque test demandait une initialisation avant de s’exécuter (ouverture fichier, base de données, réseaux...) il faudrait le faire avant chaque assert => très lourd car de nombreux copier/coller

Nous allons voir une librairie dédiée aux tests unitaires, plus puissante mais aussi plus lourde d’utilisation.

#### 4.2.4 - Tests unitaires avec la librairie unittest

Avec la librairie ``unittest`` les mêmes tests qu’avec assert pourraient ressembler à :

```python
# Librairies utilisées
import unittest
from calculs import additionner, etre_pair

class TestCalculs(unittest.TestCase):
    """Classe gérant les tests unitaires du module calculs"""

    def test_additionner(self):
        """Tests unitaires de la fonction additionner()"""
        self.assertEqual(additionner(2, 2), 4, "2 + 2 => 4")
        self.assertEqual(additionner(0, 0), 0, "0 + 0 => 0")
        self.assertEqual(additionner(11, 5), 16, "11 + 5 => 16")

    def test_etre_pair(self):
        """Tests unitaires de la fonction etre_pair()"""
        self.assertEqual(etre_pair(5), False, "5 est impair")
        self.assertEqual(etre_pair(4), True, "4 est pair")
        self.assertEqual(etre_pair(0), True, "0 est pair")

# Lancement des tests
if __name__ == '__main__':
    unittest.main()

```
On retrouve dans ce code :<br />

|Code python|	Description|
|:--|:--|
|``import unittest``|	Importation de la librairie unittest qui fait partie de la librairie standard Python, donc pas d’installation|
|``class TestCalculs(unittest.TestCase):``|	Création d’un classe regroupant les tests unitaires et héritant de TestCase|
|``def test_additionner(self):``	|Fonction débutant par test_xxx signifiant qu’elle embarque des tests unitaires|
|``self.assertEqual(additionner(2, 2), 4, "2 + 2 => 4")``|	Assertion vérifiant le résultat retourné par une fonction accompagnée d’un message|
|``if __name__ == '__main__': unittest.main()``|Lancement des tests, la librairie va rechercher seul les tests à effectuer (méthodes débutant par test_xxx et les exécuter)|

Le lancement de ce script de test produira le résultat suivant :
```python
$ python3 -m unittest
======================================================================
FAIL: test_additionner (test_calculs_unittest.TestCalculs)
Tests unitaires de la fonction additionner()
----------------------------------------------------------------------
Traceback (most recent call last):
  File "test_calculs.py", line 21, in test_additionner
    self.assertEqual(additionner(11, 5), 16, "11 + 5 => 16")
AssertionError: 55 != 16 : 11 + 5 => 16

----------------------------------------------------------------------
Ran 5 tests in 0.001s

FAILED (failures=1, errors=1)
```

Par rapport à la méthode ``assert``, on peut remarquer que :

-	tous les tests ont été lancés, le script ne s’est pas arrêté à la première erreur
-	d’autres méthodes de tests que assertEqual() existent :
    -	assertTrue() : teste si égal à True
    -	assertIsNone() : teste si vaut None
    -	assertAlmostEqual() : teste si égal avec une marge d’erreur
    -	assertRaises() : teste si une exception est levée
    -	assertRegex() : teste une chaîne de caractères
    -	assertLogs() : teste si un log a bien été produit

La librairie ``unittest`` permet également d’initialiser (``setUp``) l’environnement (``fixture``) avant l’exécution de chaque test et aussi de le désactiver (``tearDown``) pour le prochain. Dans cet exemple on ouvre et ferme un fichier de données :
```python
class TestCalculs(unittest.TestCase):
    """Classe gérant les tests unitaires du module calculs"""

    def setUp(self):
        """Initialisation des tests"""
        # Ouverture du fichier contenant le jeu de test
        self.fichier = open("data.json", "r")

    def tearDown(self):
        """Désactivation des tests"""
        # Fermeture du fichier contenant le jeu de test
        self.fichier.close()

    # ...suite de la classe tronquée
```

## 5 - Optimisation des performances

Les gains d’optimisation sont souvent liés :

-	à l’algorithme utilisé
-	au langage lui même et sa machinerie interne

### 5.1 - Chronométrage simple

Le chronométrage d’une portion de code ou d’une fonction peut s’effectuer avec la fonction ``perf_counter() ``du module **time** comme ci-dessous :
```python
# Importation des outils pour mesurer le temps
import time

# Fonction qu'on souhaite chronométrer
def additionner(limite):
    somme = 0
    for i in range(0, limite+1):
        somme += i
    return somme

#  Lancement et chronométrage de la fonction
debut = time.perf_counter()
resultat = additionner(1000000)
fin = time.perf_counter()

# Affichage du résultat et de la durée d'exécution
print(f"La somme jusqu’à 1000000 est {resultat}")
delai = fin - debut
print(f"Durée d'exécution = {delai} s")
```

### 5.2 - Profilage

Le profilage d’un code donne des résultats beaucoup plus complet avec pour chaque fonction :

-	le temps total d’exécution
-	le nombre d’appels
-	la durée moyenne d’un appel
-	...


Le module ``cProfile`` présent dans la distribution standard de Python permet de réaliser facilement ce profilage. Il suffit de lancer l’exécution d’un script depuis un terminal comme ci-dessous :

```prompt
C:\Users\corte>python -m cProfile D:\NSI\Premiere\eratosthene.py
```
![profilage](./data/profilage.png){: width=80% .center}

On peut noter par exemple que la fonction ``eratosthene() ``a été appelée 1000000 de fois pour un temps total d’exécution de 0 s. Pas de problèmes d'optimisation pour cette fonction.