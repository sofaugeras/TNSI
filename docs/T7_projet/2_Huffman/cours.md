# Projet Les marmottes 🐹

!!! info "Crédits"
    Cette activité est adaptée du jeu ["Les marmottes ont le sommeil léger"](https://members.loria.fr/MDuflot/files/med/marmottes.html) de Marie Duflot Kremer, maître de conférences chez Université de Lorraine, LORIA & Inria Nancy Grand Est et d’une activité de l’IREM de Grenoble 

    Crédit de mise en forme : [Rodrigo SCHWENCKE](https://eskool.gitlab.io/tnsi/donnees/arbres/binaires/td/huffman/marmottes/)

## 1. Les marmottes ont le sommeil léger 🐹

![les marmottes](./data/marmottes.png){: .center width=50%}

### Principe du Jeu

Un groupe de **marmottes au sommeil léger** (càd qui se réveillent lorsque d'autres marmottes leur passent à côté, durant leur hibernation), moyennement satisfaites de leur terrier actuel, décide de concevoir un nouveau terrier, et de le creuser avant l’hiver.

* Chaque marmotte doit dormir dans **une Salle (de sommeil)** de son terrier
* Chaque marmotte **se réveille un certain nombre précis de fois** (connu à l'avance) durant son hibernation en hiver
* Le but de jeu étant de gêner/réveiller le moins possible les autres marmottes durant leur hibernation, car elles ont chacune le Sommeil Léger.

### Règles de Construction du Terrier

Plus précisément, on déduit des règles du jeu précédentes, que la contruction du terrier doit suivre les $3$ règles suivantes :

1. **Règle de Stabilité du Terrier** : A partir de l'entrée, ou à partir de l'extrêmité d'un couloir (appelé un embranchement/<red>noeud</red>), on peut **au maximum creuser deux couloirs**, sinon la structure risque de s'effondrer.
2. **Règle Individuelle de Sommeil Léger 1 : Pas de marmottes aux embranchements/noeuds**.  
Autrement dit, **les Salles de Sommeil des marmottes sont forcément situées au fin fond d'une galerie**.  
En effet, si la salle de sommeil était sur un noeud (ou encore pire, au milieu d'un couloir) alors elle se ferait marcher dessus par d'autres marmottes habitant plus loin dans le terrier, et cela la réveillerait : elle a le **sommeil léger**. Les marmottes dorment donc uniquement au fond d'une galerie qui ne donne sur rien d'autre que sa salle.
3. **Règle Globale de Sommeil Léger 2 : Minimisation du bruit total des déplacements**  
Même le simple déplacement des marmottes qui se réveillent, à cause du bruit lointain de leurs petites pattes, génère des vibrations qui dérangent le groupe pendant leur sommeil : elles ont vraiment le sommeil léger !! Du coup, comme on sait combien de fois chacune va se réveiller et sortir (et revenir) du terrier pendant l'hiver, l'objectif sera que **la somme des déplacements de toutes les marmottes soit la plus petite possible.**. Par souci de simplicité (et parce que cela change pas le résultat), on pourra ne compter que les sorties du terrier, inutile de compter les retours dans le terrier.

!!! exp "En Pratique : Comment compter les déplacements des marmottes ?"
    Voici deux exemples de comptage des déplacements des marmottes : 

    * Une marmotte dormant à $4$ couloirs de l’entrée, et se réveillant $5$ fois dans l’hiver va parcourir $4\times 5=20$ couloirs **aller** (il faudrait aussi compter les $20$ **retours**, mais pour simplifier on ne va compter que les allers).
    * une marmotte qui se réveille $6$ fois, et située à $3$ couloirs de la sortie, devra parcourir $6 \times 3 = 18$ couloirs **aller** (il faudrait aussi compter les $18$ **retours**, mais pour avoir des chiffres moins gros on ne va compter que les allers). Si on la mettait à $1$ couloir de la sortie, elle ne parcourrait plus que $6 \times 1 = 6$ couloirs.

!!! info "A vous de jouer 🐹"
   A l'aide du matériel distribué en classe, déterminer quel est le meilleur terrier pour ces marmottes. 

??? question "Le meilleur terrier"
    Pour trouver le meilleur terrier, il y a une méthode infaillible, qui ne demande pas trop de calculs :

    - on choisit les deux (ou deux parmi les) marmottes qui se lèvent le moins souvent, et on les relie par un morceau de terrier. Sur le coude on note le nombre de fois que ce morceau est emprunté (donc la somme des valeurs des deux marmottes, par exemple 2 + 3 = 5)
    - on recommence exactement la même chose, mais les deux marmottes reliées à l’étape précédente comptent maintenant pour une seule marmotte qui se réveillerait 5 fois
    - on continue, jusqu’à ce que toutes les marmottes soient reliées en un seul terrier.
    - et comme on a noté des chiffres sur les coudes de terriers au fur et à mesure on a juste à faire la somme de ces chiffres pour compter le nombre de déplacements

## 2. Algorithme de compression de Huffman

Et quel est le lien avec l'informatique ? 

L'algorithmme que nous venons d'appliquer pour trouver les meilleurs terriers, est utilisé dans le domaine de la **compression de texte**.

Le but de la compression de texte est ... de réduire le poids du texte. Les textes sont codés en binaire la plupart du temps.

??? info "Le code ASCII"
    Le but de la compression est de trouver un codage du texte, en binaire parce que dans un ordinateur tout est stocké en binaire, qui soit le plus court possible, et qui soit facile à coder et décoder. En général pour représenter un texte non compressé, on utilise le code ASCII ou l’une de ses extensions. Mais même rien qu’en ASCII on a 8 chiffres binaires (8 bits) pour stocker un caractère. Si ce n’est pas grave que le code du "w" ou du "k" soient longs en français, par contre le "e" qui apparaît plus souvent on aimerait bien que son code soit plus court, et c’est précisément ce que fait le codage de Huffman : donner à chaque lettre un code binaire tel que si on met bout à bout le code de toutes les lettre du texte, on a une version codée la plus courte possible

↩️ Retourner les terriers ! <br />

La structure que l’on obtient est celle d’un **arbre**, avec la **racine** en haut, les couloirs qui se nomment des **branches**, et les extrémités des branches appelées **feuilles**. Et dans cet arbre une marmotte correspond à une lettre, et son nombre de réveils au nombre de fois que la lettre apparaît dans un texte.

😕 Essayons d'y voir plus clair

Les textes à envoyer via un canal de communication sont (la plupart du temps) codés en binaire. 

Essayons avec ``BARBARA RASE BASILE LE BARBIER``

On obtient la fréquence d'apparition de chaque lettre : 

|Lettre|Fréquence|
|:--:|:--:|
|A|6|
|B|5|
|R|5|
|espace|4|
|E|4|
|S|2|
|I|2|
|L|2|

1. Ecrire sur chaque feuille une lettre en commençant par assembler les lettres avec la fréquence d'apparition la plus faible. On additionne sur la racine la somme des fréquences.
2. On poursuit la construction de l'arbre en appliquer les contraintes vues avec les marmottes.
3. Ajouter sur chaque branche de gauche un $0$ et sur chaque branche de droite un $1$

Sur notre structure de terrier on peut facilement lire le code de chaque lettre : on part de la racine
du terrier et on lit le bit écrit sur chaque couloir que l’on emprunte. Par exemple si pour aller de l’entrée à la lettre ``A`` on prend à gauche puis à droite puis à droite, le code de ``A`` est ``011``
 
<div style="position:relative;p;height:0;overflow:hidden;"><iframe width="560" height="315" src="https://player.vimeo.com/video/173747112" title="Viméo codage" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe></div>

??? info "Codage Préfixe"
    Texte de Marie Duflot Kremer

    Imaginez que je donne le code 0 à la lettre E, 01 à la lettre S et 10 à la lettre T. 
    
    Pour coder ce n’est pas difficile : ETES donne 0 puis 10 puis 0 puis 01 soit 010001. 

    Par contre pour décoder c’est franchement plus difficile. Si je lis 10010001 je sais que ça commence par un T, et puis il me reste 010001 que je peux décoder en ETES ou SEES. Sur cet exemple je sais que TETES est un mot et TSEES pas, mais sur un long texte je vais au mieux perdre énormément de temps, au pire avoir plusieurs possibilités et ne pas savoir comment décoder.

    Le problème est que 0 est à la fois le code de E et le début du code de S, donc si je vois un 0 je ne sais pas si je peux décoder E tout de suite ou prendre le prochain bit et les décoder ensemble. Si au contraire on impose un codage préfixe, on interdit que le code d’une lettre soit le début du code d’une autre. Du coup on va commencer à la racine, suivre les branches en fonction des 0 et 1 dans le texte compressé, et dès qu’on arrive sur une lettre on la note (comme on ne peut pas continuer plus loin car la branche s’arrête là, on est sûr d’avoir lu le code de cette lettre) et on repart de la racine en continuant à lire les chiffres binaires. Le décodage/décompression se fait donc très rapidement et sans hésitation.

    Et les codes qui ne sont pas préfixes, on peut les jeter ? Non, pas tous. Si on regarde le code Morse par exemple, on a le E (un point) qui est préfixe du I (deux points). La différence c’est qu’en Morse on fait une légère pause entre deux lettres qui permet de savoir quand une lettre s’arrête et ainsi différencier un double e d’un i. En informatique tous les 0 et les 1 sont rangés les uns à la suite des autres, sans pause, et c’est pour cela qu’on a besoin d’un codage préfixe.

!!! Warning "🔥 Challenge 🔥"

    1. Mettez vous par binôme.
    2. Choisissez un mot ou une phrase de 15 caractères max
    3. Compresser votre phrase

    4. Fournissez à votre binôme le code binaire obtenu, ainsi que l'arbre de compression.

    🔥 Qui est le plus rapide à décompresser ?

!!! info "Résumé Le codage de Huffman"
    Il a été prouvé que l’algorithme vu avec les marmottes est l’algorithme optimal pour le codage de symboles uniques, c’est-à-dire qu’on ne peut pas faire plus court que ce codage. Cet algorithme a été inventé par l’informaticien américain David Albert Huffman, et publié en 1952.

    Étant optimal il est utilisé dans de très nombreuses application de compression de données, comme le célèbre format zip
    (ou rar). En fait il constitue souvent la dernière étape de la compression (on effectue d’abord une première compression qui dépend de la nature des données (son, image, texte, vidéo…) puis on stocke les données compressées avec l’algorithme d’Huffman).

    Le but de cette deuxième partie est d’écrire un programme capable d’effectuer la compression et la décompression d’un
    texte avec l’algorithme de Huffman et d’estimer son efficacité.

    La compression d’un texte avec l’algorithme de Huffman se fait en quatre étapes :

    1. Analyse du texte et détermination des fréquences des différents symboles constituant le texte
    2. Création de l’arbre binaire de codage en suivant l’algorithme vu avec les marmottes
    3. Création d’un dictionnaire de codage associant à chaque symbole son code binaire dans l’arbre
    4. Encodage du texte, caractère par caractère en utilisant le dictionnaire de codage
