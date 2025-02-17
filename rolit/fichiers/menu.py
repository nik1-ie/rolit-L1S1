#-------Import-------
from .fltk import *
from .drawing import dessiner_secteur
from . import config
from .partie import nouvelle_partie
from . import audio
import sys
from . import saving
import time

#-------Constantes-------
menu_or_game="Menu"

#-------Fonctions-------
def afficher_menu():
    """
    Affiche le menu principal du jeu.
    
    Ce menu présente des options pour commencer le jeu, consulter les règles, accéder aux paramètres, ou quitter le jeu.
    Il inclut également un arrière-plan avec un dégradé et un logo.
    """
    config.current_page="menu"
    efface_tout()
    
    for i in range(4): 
        couleur = config.current_theme[0][i]
        rectangle(0, i * 100, 600, (i + 1) * 100, remplissage=couleur, epaisseur=0)

    texte(210, 70, "R", taille=40, couleur="darkblue", ancrage="center", police="Fixedsys")
    texte(255, 70, "o", taille=40, couleur="blue", ancrage="center", police="Fixedsys")
    texte(295, 70, "l", taille=40, couleur="darkblue", ancrage="center", police="Fixedsys")
    texte(335, 70, "i", taille=40, couleur="darkblue", ancrage="center", police="Fixedsys")
    texte(375, 70, "t", taille=40, couleur="darkblue", ancrage="center", police="Fixedsys")

    x_center, y_center = 255, 70
    radius = 23


    dessiner_secteur(x_center, y_center, radius, 0, 90, "red")    
    dessiner_secteur(x_center, y_center, radius, 90, 180, "green") 
    dessiner_secteur(x_center, y_center, radius, 180, 270, "blue") 
    dessiner_secteur(x_center, y_center, radius, 270, 360, "yellow") 
    
    
    options = [
        (200, 250, "règles"),
        (260, 310, "paramètres"),
        (320, 370, "quitter"),
    ]

    rectangle(200, 140, 295, 190, remplissage=config.current_theme[1][0], epaisseur=2, couleur="black")
    texte(245, (140+190)//2, "jouer", taille=22,couleur="black", ancrage="center", police="Fixedsys")
    rectangle(305, 140, 400, 190, remplissage=config.current_theme[1][0], epaisseur=2, couleur="black")
    texte(355, (140+190)//2, "saves", taille=22,couleur="black", ancrage="center", police="Fixedsys")

    for index, (y1, y2, text) in enumerate(options):
        remplissage = config.current_theme[1][index]
        rectangle(200, y1, 400, y2, remplissage=remplissage, epaisseur=2, couleur="black")
        texte(300, (y1 + y2) // 2, text, taille=22, couleur="black", ancrage="center", police="Fixedsys")

    mise_a_jour()
    gestion_clic()

def afficher_parametres():
    """
    Affiche la fenêtre des paramètres du jeu.
    
    Dans cette fenêtre, l'utilisateur peut voir et modifier certaines configurations du jeu, telles que la
    musique et les options de son.
    Le fond de la fenêtre est décoré de bandes colorées et un bouton pour chaque option qui est affichée.
    """
    global menu_or_game
    menu_or_game = ""
    if config.current_page == "game":
        menu_or_game = "Retour"
        config.current_page = "game pause"
    elif config.current_page == "menu":
        menu_or_game = "Menu"
        config.current_page = "param"
    efface_tout()
    largeur_fenetre, hauteur_fenetre = 600, 400


    for i in range(4):  
        couleur = config.current_theme[0][i]
        rectangle(0, i * 100, largeur_fenetre, (i + 1) * 200, remplissage=couleur, epaisseur=0)

    texte(largeur_fenetre // 3.8, 50, "Paramètres", taille=30, couleur="black", ancrage="center", police="Fixedsys")

    if config.musique_en_cours == True:
        texte(300, 165, "ON", taille=22, couleur="black", ancrage="center", police="Fixedsys", tag="music_playing")
    elif config.musique_en_cours == False:
        texte(300, 165, "OFF", taille=22, couleur="black", ancrage="center", police="Fixedsys", tag="music_playing")

    if config.mode_daltonien==False:
        texte(300, 280, "OFF", taille=22, couleur="black", ancrage="center", police="Fixedsys", tag="daltonisme_or_no")
    elif config.mode_daltonien==True:
        texte(300, 280, "ON", taille=22, couleur="black", ancrage="center", police="Fixedsys", tag="daltonisme_or_no")
    
    rectangle(50, 140, 250, 190, remplissage=config.current_theme[1][0], epaisseur=2, couleur="black")
    texte(150, 165, "Musique", ancrage="center", police="Fixedsys", taille="22", couleur="black")
    rectangle(350, 260, 550, 310, remplissage=config.current_theme[1][2], epaisseur=2, couleur="black")
    texte(450, 285, "Daltonisme", ancrage="center", police="Fixedsys", taille="22", couleur="black")
    rectangle(350, 320, 550, 370, remplissage=config.current_theme[1][3], epaisseur=2, couleur="black")
    texte(450, 345, "Thèmes", ancrage="center", police="Fixedsys", taille="22", couleur="black")

    rectangle(50, 210, 145, 250, epaisseur=2, couleur="black", remplissage=config.current_theme[1][1])
    texte(97,230, "+", ancrage="center", couleur="black", taille=22)
    rectangle(155, 210,250,250, epaisseur=2, couleur="black", remplissage=config.current_theme[1][1])
    texte(203,230, "-", ancrage="center", couleur="black", taille=22)

    
    rectangle(500, 20, 550, 70, epaisseur=2, remplissage=config.current_theme[1][2])
    texte((500+550)//2, (20+70)//2, "❌", police="Fixedsys", taille=15, ancrage="center")
    mise_a_jour()



class Slider:
    """
    Représente un composant interactif de type "slider" qui permet à l'utilisateur de sélectionner une valeur dans un intervalle donné.
    
    Un slider est constitué d'un rail et d'un bouton déplaçable. L'utilisateur peut ajuster la valeur du slider en déplaçant le bouton sur le rail.
    
    Attributs:
    
    min_val (int): La valeur minimale du slider.
    max_val (int): La valeur maximale du slider.
    nb_choice (int)  Le nombres de choix possibles.
    val (int): La valeur actuelle du slider.
    x (int): La position horizontale du coin supérieur gauche du slider.
    y (int): La position verticale du coin supérieur gauche du slider.
    largeur (int): La largeur du rail du slider.
    
    Méthodes:
    
    valeur(): Retourne la valeur actuelle du slider.
    calculer_valeur(x_clic): Met à jour la valeur du slider en fonction de la position du clic de la souris.
    afficher(): Affiche visuellement le slider dans la fenêtre.
    """
    def __init__(self, min_val, max_val, val_init, x, y, largeur):
        self.min_val = min_val
        self.max_val = max_val
        self.nb_choice = self.max_val - self.min_val
        self.val = val_init
        self.x = x
        self.y = y
        self.largeur = largeur
      
    
    def valeur(self):
        """
        Retourne la valeur actuelle du curseur.
        """
        return self.val
    
    def calculer_valeur(self, x_clic):
        """
        Met à jour la valeur du curseur en fonction de la position du clic.
        """
        if self.x <= x_clic <= self.x + self.largeur:
            position = (x_clic - self.x) / self.largeur
            self.val = self.min_val + position * (self.max_val - self.min_val)
            self.val = round(self.val) 
        return self.val

    def afficher(self):
        """
        Affiche le curseur sur l'écran.
        """
        slider_range = self.max_val - self.min_val
        if slider_range == 0: 
           slider_range = 1
        slider_position = (self.val - self.min_val) / slider_range * self.largeur


        rectangle(self.x, self.y, self.x + self.largeur, self.y + 20, remplissage="#d3d3d3", epaisseur=2, couleur="#d3d3d3" ) #d3d3d3
        
        for i in range(1,self.nb_choice+2):
            position = self.x + ((i - 1) / slider_range * self.largeur)
            ligne(position, self.y, position, self.y + 20, couleur="black")

        rectangle(self.x + slider_position - 5, self.y - 5,
                  self.x + slider_position + 5, self.y + 25, remplissage="#823538", epaisseur=0)

# def mettre_a_jour_slider_bots():
#     """Mettons les sliders dépendants l'un de l'autre."""
#     slider_bots.valeur_max = 4 - config.nb_joueurs
#     slider_bots.calculer_valeur(slider_bots.valeur)
    
def afficher_choix():
    """
    Affiche la fenêtre permettant de choisir le nombre de joueurs et la taille du plateau de jeu.
    
    Cette fonction présente deux sliders interactifs pour sélectionner le nombre de joueurs (entre 1 et 4) et la taille du plateau de jeu (entre 8x8 et 20x20).
    Elle inclut également un bouton "start" pour démarrer le jeu une fois les choix effectués.
    
    Le nombre de joueurs et la taille du plateau sont mis à jour en fonction des interactions avec les sliders.
    """
    config.current_page = "choix"
    efface_tout()
    global slider_bots


    slider_joueurs = Slider(1, 4, 2, 200, 140 -5, 200)  
    slider_taille = Slider(8, 20, 8, 200, 190-5, 200) 
    slider_manche = Slider(1, 5, 3, 200, 240-5, 200)
    slider_bots = Slider(0, 3 , 0, 200, 290-5, 200) #4 - config.nb_joueurs
    slider_difficulte = Slider(1, 3, 1, 200, 340-5, 200) 

    largeur_fenetre, hauteur_fenetre = 600, 400

    def mise_a_jour_affichage():
        global slider_bots
        efface_tout()

        for i in range(4):  
            couleur = config.current_theme[0][i]
            rectangle(0, i * 100, largeur_fenetre, (i + 1) * 100, remplissage=couleur, epaisseur=0)
#         if config.nb_joueurs == 1:
#            slider_bots = Slider(0, 3, 0, 200, 300, 200)
#         elif config.nb_joueurs ==2:
#            slider_bots = Slider(0, 2, 0, 200, 300, 200)
#         elif config.nb_joueurs ==3:
#            slider_bots = Slider(0, 1, 0, 200, 300, 200)
#         elif config.nb_joueurs ==4:
#            slider_bots = Slider(0, 0, 0, 200, 300, 200)
        texte(300, 50, "Choisissez les paramètres:", taille=22, couleur="black", ancrage="center", police="Fixedsys")
        rectangle(200, 320, 400, 370, remplissage=config.current_theme[0][0], epaisseur=2, couleur=config.current_theme[0][0])
        texte(300, (320 + 370) // 2, "Start", taille=22, couleur="black", ancrage="center", police="Fixedsys")

        slider_joueurs.afficher()
        slider_taille.afficher()
        slider_manche.afficher()
        slider_bots.afficher()

        texte(300, 125 -15, f"{config.nb_joueurs} joueurs", taille=15, couleur="black", ancrage="center", police="Fixedsys")
        texte(300, 185 -15, f"Taille: {config.taille}x{config.taille}", taille=15, couleur="black", ancrage="center", police="Fixedsys")
        texte(300, 235 -15, f"{config.manches} manches", taille=15, couleur="black", ancrage="center", police="Fixedsys")
        texte(300, 285 -15, f"{config.nb_bots} bots", taille=15, couleur="black", ancrage="center", police="Fixedsys")

        mise_a_jour()
    

    mise_a_jour_affichage()
    
    while True:
        x, y = attend_clic_gauche()
        audio.jouer_son_clic1()

        if 200 <= x <= 400 and 150-15 <= y <= 170 -15:
            config.nb_joueurs = slider_joueurs.calculer_valeur(x)
        elif 200 <= x <= 400 and 200-15 <= y <= 220-15:
            config.taille = slider_taille.calculer_valeur(x)
        elif 200 <= x <= 400 and 250-15 <= y <= 280-15:
            config.manches= slider_manche.calculer_valeur(x)
        elif 200 <= x <= 400 and 300-15 <= y <= 320-15: 
            config.nb_bots = slider_bots.calculer_valeur(x)

        elif 200 <= x <= 400 and 320 <= y <= 370:
            afficher_choix_bots(config.nb_joueurs, config.nb_bots)
            break

        mise_a_jour_affichage()
        
def afficher_choix_bots(nb_joueurs, nb_bots):
    """
    Affiche la fenêtre pour choisir la difficulté des bots.
    
    Cette fonction affiche des icônes pour les joueurs et les bots, et propose des boutons
    pour sélectionner la difficulté des bots (facile, moyen, difficile).
    """
    config.current_page = "choix_bots"
    efface_tout()
    largeur_fenetre, hauteur_fenetre = 600, 400
    
    
    espace_horizontal = 20 
    largeur_rectangle = (largeur_fenetre - (nb_joueurs + nb_bots + 1) * espace_horizontal) // (nb_joueurs + nb_bots)
    hauteur_rectangle = 225
    y_centre = hauteur_fenetre // 2
    choisibot1 = "White"
    choisibot2 = "White"
    choisibot3 = "White"

    def mise_a_jour_affichage():
        global slider_bots
        efface_tout()

        for i in range(4):  
            couleur = config.current_theme[0][i]
            rectangle(0, i * 100, largeur_fenetre, (i + 1) * 100, remplissage=couleur, epaisseur=0)
            
    def texteaffichage():
        
            texte((facile[0] + facile[2]) // 2, (facile[1] + facile[3]) // 2, "Difficile", 
                  taille=12, couleur=choisibot1, ancrage="center", police="Fixedsys")
            
            texte((moyen[0] + moyen[2]) // 2, (moyen[1] + moyen[3]) // 2, "Moyen", 
                  taille=12, couleur=choisibot2, ancrage="center", police="Fixedsys")
            
            texte((difficile[0] + difficile[2]) // 2, (difficile[1] + difficile[3]) // 2, "Facile", 
                  taille=12, couleur=choisibot3, ancrage="center", police="Fixedsys")
            
    mise_a_jour_affichage()

    texte(largeur_fenetre // 2, 50, "Choisissez la difficulté des bots", taille=22, couleur="black",
          ancrage="center", police="Fixedsys")


    def calculer_taille_texte(nb_joueurs, nb_bots):
        total_personnes = nb_joueurs + nb_bots
        if total_personnes <= 4:
            return 18 
        elif total_personnes <= 3:
            return 22  
        else:
            return 25  

    taille_texte = calculer_taille_texte(nb_joueurs, nb_bots)
    boutons = []
    for i in range(nb_joueurs + nb_bots):
        x_gauche = (i + 1) * espace_horizontal + i * largeur_rectangle
        x_droite = x_gauche + largeur_rectangle


        if i < nb_joueurs:
            couleur_rect = remplissage=config.current_theme[1][2]
            rectangle(x_gauche, y_centre - hauteur_rectangle // 2, x_droite, y_centre + hauteur_rectangle // 2, 
                  couleur=couleur_rect, remplissage=couleur_rect)
            texte(x_gauche + 5, y_centre + hauteur_rectangle // 2 - 20, f"Player {i + 1}", 
                  taille=taille_texte, couleur="black", ancrage="w", police="Fixedsys")
        else:
            bot_index = i - nb_joueurs
            
            
            
            couleur_rect = "red"
            rectangle(x_gauche, y_centre - hauteur_rectangle // 2, x_droite, y_centre + hauteur_rectangle // 2, 
                  couleur=couleur_rect, remplissage=couleur_rect)
            texte(x_gauche + 5, y_centre + hauteur_rectangle // 2 - 20, f"Bot {bot_index + 1}", 
                  taille=taille_texte, couleur="black", ancrage="w", police="Fixedsys")


            facile = (x_gauche + 10, y_centre - 30 -20 -20, x_gauche + largeur_rectangle - 10 , y_centre + 10-20- 20)
            moyen = (x_gauche + 10, y_centre + 10-20 +10 -10 -5, x_gauche + largeur_rectangle - 10, y_centre + 50-20+10 -10 -5)
            difficile = (x_gauche + 10, y_centre + 50-20+10, x_gauche + largeur_rectangle - 10, y_centre + 90-20+10)
            boutons.append((facile, moyen, difficile))

            rectangle(*facile, couleur="black", remplissage="black")
            texte((facile[0] + facile[2]) // 2, (facile[1] + facile[3]) // 2, "Difficile", 
                  taille=12, couleur="white", ancrage="center", police="Fixedsys")
            rectangle(*moyen, couleur="black", remplissage="black")
            texte((moyen[0] + moyen[2]) // 2, (moyen[1] + moyen[3]) // 2, "Moyen", 
                  taille=12, couleur="white", ancrage="center", police="Fixedsys")
            rectangle(*difficile, couleur="black", remplissage="black")
            texte((difficile[0] + difficile[2]) // 2, (difficile[1] + difficile[3]) // 2, "Facile", 
                  taille=12, couleur="white", ancrage="center", police="Fixedsys")
        
            
            mise_a_jour()


    bouton_start = (largeur_fenetre // 2 - 100, hauteur_fenetre - 80, largeur_fenetre // 2 + 100, hauteur_fenetre - 40)
    rectangle(*bouton_start, couleur=config.current_theme[0][0], remplissage=config.current_theme[0][0], epaisseur=2)
    texte((bouton_start[0] + bouton_start[2]) // 2, (bouton_start[1] + bouton_start[3]) // 2, "Commencer",
          taille=22, couleur="black", ancrage="center", police="Fixedsys")

    mise_a_jour()

    difficulte_bots = [1] * nb_bots  

    while True:
        x, y = attend_clic_gauche()
        audio.jouer_son_clic1()

        for i, (facile, moyen, difficile) in enumerate(boutons):
            if facile[0] <= x <= facile[2] and facile[1] <= y <= facile[3]:
                choisibot1 = "Red"
                choisibot2 = "White"
                choisibot3 = "White"
                difficulte_bots[i] = 1
                texteaffichage()
            elif moyen[0] <= x <= moyen[2] and moyen[1] <= y <= moyen[3]:
                choisibot1 = "White"
                choisibot2 = "Red"
                choisibot3 = "White"
                difficulte_bots[i] = 2
                texteaffichage()
            elif difficile[0] <= x <= difficile[2] and difficile[1] <= y <= difficile[3]:
                choisibot1 = "White"
                choisibot2 = "White"
                choisibot3 = "Red"
                difficulte_bots[i] = 3
                texteaffichage()
                
        if bouton_start[0] <= x <= bouton_start[2] and bouton_start[1] <= y <= bouton_start[3]:
            redimensionne_fenetre(950, 650)
            nouvelle_partie(config.nb_joueurs, config.taille, config.manches, config.nb_bots, config.difficulte_bots)
            break
        


def afficher_texte_progressif(message, x, y, taille=12, couleur='black', delai=0.05):
    x_line = x
    mots = message.split()
    for i, mot in enumerate(mots):
        if i > 0:
            mot = ' ' + mot
        texte(x, y, mot, taille=taille, couleur=couleur, ancrage='nw', police='Fixedsys', tag="reglesaffich")
        mot_width = taille_texte(mot,'Fixedsys', taille=taille)[0]
        x = x_line + mot_width
        x_line += mot_width
        mise_a_jour()
        time.sleep(delai)
    
def afficher_rules():
    config.current_page="rules"
    efface_tout()
    redimensionne_fenetre(600, 600)

    for i in range(4):  
            couleur = config.current_theme[0][i]
            rectangle(0, i * 150, 600, (i + 1) * 150, remplissage=couleur, epaisseur=0)

    texte(30, 50, "RRRWWW du   Règles du jeu", taille=34, couleur="black", ancrage="center", police='Fixedsys')
    rectangle(530, 25, 580, 75, epaisseur=2, remplissage=config.current_theme[1][2])
    texte((530+580)//2, (25+75)//2, "❌", police="Fixedsys", taille=15, ancrage="center")
    
    chibik_image = "images/chibi_regles.png"
    image(270, 470, chibik_image, ancrage='center', largeur=450, hauteur=300)
    rectangle(0, 320, 45, 620, couleur='black', remplissage="black")  # gauche
    rectangle(495, 320, 600, 620, couleur='black', remplissage="black")

    
    rectangle(20, 180, 580, 260, remplissage="black", couleur="black", epaisseur=2)
    
    regles = [
        "Bienvenue à toi joueur!\n",
        "Tu es prêt à apprendre\n",
        "comment jouer à ROLIT?\n",
        "Je vais t'expliquer ça,\n",
        "Et tu vas vite comprendre !\n",
        "Alors, écoute bien:\n",
        "Voici les règles du jeu!!\n\n",

        "C'EST QUOI TON OBJECTIF?!\n",
        "Voilà la mission:\n",
        "Manger un maximum de boules!\n",
        "Celles de TA couleur!\n",
        "À la fin, y'a qu'un gagnant.\n",
        "Et ce gagnant, c'est toi!\n\n",

        "COMMENT ÇA SE MET EN PLACE?\n",
        "Alors, voilà comment:\n",
        "C'est un jeu pour 2 à 4!\n",
        "Chaque joueur a SA couleur.\n",
        "C'est simple: pas de choix.\n",
        " À 2, c'est: A=rouge.\n",
        " Et B=vert, évidemment.\n",
        " À 3 ? A=rouge, B=jaune.\n",
        "Et enfin, C=vert, logique!\n",
        "À 4 ? Toutes les couleurs.\n",
        "A=rouge, B=jaune, C=vert.\n",
        "Et D=bleu, complet!\n\n",

        "COMMENT JOUER ?!\n",
        "Prépare-toi, \n",
        "C'est le plus intéressant! \n",
        "Pose une boule,\n",
        "Tranquillement.\n",
        "Coince celles des autres.\n",
        "Et prends-les pour toi!\n",
        "Si t'alignes deux boules :\n",
        "BOUM, tu les captures!\n",
        "À l'horizontale, verticale,\n",
        "Ou même en diagonale...\n"
        "Facile, hein?\n\n",

        "FIN DE LA PARTIE:\n",
        "Une manche se termine quand\n",
        "Toutes les boules sont là!\n",
        "Plus de place? C'est fini.\n",
        "Sinon, une nouvelle manche..\n",
        "Si tu veux une revanche! \n",
        "Et le boss ultime?\n",
        "Celui avec le PLUS de pions!\n",
        "Celles de sa couleur..\n\n",

        "Allez, c'est parti!\n",
        "Pose ta première boule.\n",
        "Et prouve que t'es le king!\n",
        "LET'S GOOOOO!\n",
        ". . . \n",
        ". . . . . . .\n",
        ". . . . . . . . . .\n",
        ". . . . . . . . . . . . . .\n",
        "(Tu peux sortir...)"
    ]



    for regle in regles:
        afficher_texte_progressif(regle, 25, 190, taille=27, couleur="white", delai=0.15)
        time.sleep(1)
        efface("reglesaffich")

        ev=donne_ev()
        if type_ev(ev) == "ClicGauche":
            audio.jouer_son_clic1()
            x=abscisse_souris()
            y=ordonnee_souris()
            if 530 <= x <= 580 and 25 <= y <= 75:
                redimensionne_fenetre(600, 400)
                afficher_menu()
                break
    gestion_clic
    

    


def gestion_clic():
    global mtxt
    """
    Gère les événements de clics dans le menu principal et dans les fenêtres du logiciel (hors-jeu).
    
    Cette fonction prends en compte les clics de souris et effectue les actions appropriées, comme afficher la fenêtre de choix des paramètres ou quitter le jeu.
    Les clics sur les différentes options du menu ou sur les boutons du jeu déclenchent l'affichage de la fenêtre correspondante ou l'exécution des actions.
    """
    while True:
        x, y = attend_clic_gauche()
        audio.jouer_son_clic1()
        if config.current_page=="menu":
            if 200 <= x <= 400:
                if 200 <= x <= 295 and 140 <= y <= 190:
                    afficher_choix()
                elif 305 <= x <= 400 and 140 <= y <= 190:
                    saving.affiche_sauvegarde()
                elif 200 <= y <= 250:
                    afficher_rules()
                elif 260 <= y <= 310:
                    afficher_parametres()
                elif 320 <= y <= 370:
                    ferme_fenetre()
                    sys.exit()
        elif config.current_page=="param" or config.current_page=="game pause":
            if 50 <= x <= 250 and 140 <= y <= 190:
                efface("music_playing")
                if config.musique_en_cours==True:
                    config.musique_en_cours=False
                    texte(300, 165, "OFF", taille=22, couleur="black", ancrage="center", police="Fixedsys", tag="music_playing")
                    audio.arreter_musique()
                elif config.musique_en_cours==False:
                    config.musique_en_cours=True
                    texte(300, 165, "ON", taille=22, couleur="black", ancrage="center", police="Fixedsys", tag="music_playing")
                    audio.jouer_musique()
            elif 50 <= x <= 145 and 210 <= y <= 250:
                config.volume = min(1.0, config.volume + 0.1)
                audio.ajuster_volume(config.volume)
            elif 155 <= x <= 250 and 210 <= y <= 250:
                config.volume = max(0.0, config.volume - 0.1)
                audio.ajuster_volume(config.volume)
            elif 350 <= x <= 550 and 260 <= y <= 310:
                efface("daltonisme_or_no")
                if config.mode_daltonien==False:
                    config.mode_daltonien=True
                    texte(300, 280, "ON", taille=22, couleur="black", ancrage="center", police="Fixedsys", tag="daltonisme_or_no")
                elif config.mode_daltonien==True:
                    config.mode_daltonien=False
                    texte(300, 280, "OFF", taille=22, couleur="black", ancrage="center", police="Fixedsys", tag="daltonisme_or_no")
            elif 350 <= x <= 550 and 320 <= y <= 370:
                config.changer_theme()
                efface_tout()
                afficher_parametres()
            elif 490 <= x <= 590 and 20 <= y <= 60:
                if config.current_page=="param":
                    afficher_menu()
                elif config.current_page=="game pause":
                    saving.reprendre_partie()
        elif config.current_page=="rules":
            if 530 <= x <= 580 and 25 <= y <= 75:
                redimensionne_fenetre(600, 400)
                afficher_menu()