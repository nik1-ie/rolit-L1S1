largeur_bouton = 300
hauteur_bouton = 40
fenetre_cree = False
musique_en_cours = True
mode_daltonien = False
largeur_fenetre, hauteur_fenetre = 600, 400
x_fenetre, y_fenetre = 100, 100
nb_joueurs = 2
taille = 8
manches = 3
volume= 0.5
nb_bots = 0
difficulte_bots = []

theme = "froid"
'''Thèmes possibles :
    chaud - Thème chaud
    froid - Thème froid
    verdure - Thème verdure'''

theme_possible= {"chaud": [["#ffc896", "#e1a082", "#c3786e", "#a5505a"],["#af7846", "#915032","#73281e", "#55000a"]],
                 "froid": [["#96d2ff","#82c9e1","#6ea2c3","#507da5"], ["#467caf","#323a91","#1e2e73","#001455"]],
                 "verdure": [["#a4ff96", "#abe182", "#82c36e", "#78a550"],["#5aad45", "#4d9132","#25731e", "#00550e"]]}
'''Themes possibles liste index
    [couleur de fond, dégradé 1, dégradé 2, dégradé 3][couleur bouton 1, couleur bouton 2, couleur bouton 3, couleur bouton 4]'''

current_theme=theme_possible[theme]
def changer_theme():
    global current_theme, theme, theme_possible
    if theme=="chaud":
        theme="froid"
        current_theme=theme_possible[theme]
    elif theme=="froid":
        theme="verdure"
        current_theme=theme_possible[theme]
    elif theme=="verdure":
        theme="chaud"
        current_theme=theme_possible[theme]
        
current_page="menu"
'''Pages possibles :
    menu - Menu principal
    choix - Page des choix de début de partie
    rules - Règles du jeu
    param - Paramètres du logiciel
    game pause - Paramètres du logiciel au milieu d'une partie
    bots - Choix du mode de jeu / Partie contre un bot
    dices - Lancé de dé
    game - Partie en cours
    save - Page affichant les sauvegardes
    endgame - Page concluant les parties'''