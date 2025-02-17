#        Jeu ROLIT - Guide d'utilisateur        
#       Anastasia Cordun & Niekita Joseph       


## ---- Comment lancer le logiciel? ----
Python 3 doit être installé sur la machine <br/>
Décompresser le dossier 'rolit' <br/>
Ouvrir un terminal depuis le dossier 'rolit' <br/>
Taper la commande : python3 main.py <br/>

## ---- Comment utiliser le logiciel? ----
En lançant le programme, la page de Menu s'ouvre. <br/>
Ici, il vous suffit de cliquer sur ce que vous souhaitez voir: <br/>
- Les règles du Jeu ROLIT <br/>
- Les paramètres du logiciel <br/>
- Lancer une partie <br/>
- Charger une partie <br/>
- Quitter le logiciel <br/>

### Règles du Jeu
Les règles s'affichent progressivement sans aucune action nécessaire.<br/>
Vous pouvez quitter à tout moment grâce au bouton en haut à droit.<br/>

### Paramètres du logiciel
Une fois entrés dans la page des paramètres du logiciel, vous avez plusieurs choix. <br/>
- Retourner au menu <br/>
- Couper/Lancer la musique de fond <br/>
- Baisser/Augmenter le volume de la musique <br/>
- Activer le mode daltonisme (permettant d'avoir des pions de différentes formes) <br/>
- Changer de thème <br/>

### Charger une partie
Si une partie a été sauvegardée précédemment, la date, l'heure, le nombres de joueurs et de manches sera affiché. <br/>
Il vous suffit de cliquer sur le bouton "Load" qui s'affichera uniquement si une partie a été sauvegarder. <br/>
Le bouton "Save" ne fera rien si vous venez de lancer le logiciel. <br/>


### Lancer une partie
Une fois le bouton cliqué, vous aurez accès à un certain nombre de paramètres que vous pouvez ajuster avec les sliders:
- Le nombre de joueurs (1 à 4) <br/>
- La taille de plateau (8x8 à 20x20) <br/>
- Le nombre de manches (1 à 5) <br/>
- Le nombre de bots (0 à 4) <br/>
Une fois choisi, vous n'avez plus qu'à cliquer sur Start ! <br/>

### Jouer une partie
Avant de commencer véritablement à jouer, il ne vous reste plus qu'a lancer le dé. Le bouton "Lancer le dé" lancera une petite animation. <br/>
Une fois le premier joueur choisi, vous n'avez plus qu'à jouer! <br/>
Les boutons disponibles: <br/>
- Sauvegarde : ce bouton vous permet d'accéder à la page de sauvegarde, afin de sauvegarder une partie pour plus tard ou d'en charger une. <br/>
- Paramètres : vous pouvez accéder à la page des paramètres en pleine partie si nécessaire (afin de changer le thème, ou le volume de la musique) <br/>
Vous pourrez retourner tranquillement à votre partie en cours en cliquant sur la croix.
- Quitter le jeu sans enregister. <br/>

### Fin de partie
Une fois votre partie finie, votre plateau de jeu laissera place à la page finale, affichant le gagnant, ainsi que les scores finaux. <br/>
Vous pourrez: <br/>
- Accéder au menu principal pour rejouer <br/>
- Accéder à la page de sauvegarde <br/>
Notez que si vous enregistrer une partie finie, cela ne fera que prendre un emplacement de sauvegarde. <br/>
Vous ne pouvez pas jouer à une partie finie plus tard. <br/>
- Quitter le logiciel <br/>

## Contexte du Jeu
Le jeu Rolit est un jeu de plateau stratégique pouvant être joué par 2 à 4 joueurs. <br/>
Chaque joueur dispose de boules colorées, et le but est de capturer un maximum de pions adverses en retournant leur couleur.

### Commanditaire :
Le projet a été commandé par Game Fan-Attic, une association passionnée de jeux de société, désireuse de moderniser Rolit pour le rendre plus accessible et attractif à une génération habituée aux jeux numériques. <br/>
Objectifs :
- Développer une application intuitive pour jouer à Rolit en mode local.
- Garantir une interface conviviale et esthétiquement plaisante.
Intégrer des fonctionnalités supplémentaires telles que :
- Mode "bot" pour jouer seul.
- Sauvegarde des parties.
- Menu interactif permettant une navigation fluide.


## Licence 
Le code source sera **réutilisable et partageable**, sous réserve qu'aucune modification ne soit effectuée par des tiers sans autorisation. Cette licence vise à permettre une future évolution du jeu tout en respectant les droits des développeurs.

## Equipe de développement - TP 11 Groupe 3
Anastasia CORDUN <br/>
Niekita JOSEPH

## Liste des fichiers
main.py - Fichier principal à partir duquel le logiciel se lance. <br/>
dossier audio (contenant les bande sons nécessaires au jeu) <br/>
dossier images (contenant les images utilisées dans le logiciel) <br/>
dossier save (contenant les fichiers dans lesquels les parties sont sauvegardées) <br/>

dans le dossier Fichiers (contenant les fichiers de programmation) <br/>
config.py - Fichier contenant les constantes du logiciel. <br/>
menu.py - Fichier gérant le menu principal, et son interface. <br/>
moteur.py - Fichier contenant le jeu ainsi que ses règles. <br/>
partie.py - Fichier gérant une partie de jeu. <br/>
graphics.py - Fichier contenant l'interface du plateau de jeu. <br/>
drawing.py - Fichier contenant l'affichage d'une partie du logo ROLIT. <br/>
saving.py - Ficheir gérant la sauvegarde des parties. <br/>
audio.py - Fichier contenant la gestion du son et de la musique du logiciel. <br/>
utils.py - Fichier contenant certaines fonctions nécessaire à la partie, sans surcharger le fichier partie.py <br/>
final.py - Fichier contenant l'interface à la fin d'une partie. <br/>
