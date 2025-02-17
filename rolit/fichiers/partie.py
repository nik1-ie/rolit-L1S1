#-------Import-------
from .moteur import Plateau
from .graphics import *
from .final import *
from .saving import *
from . import bots
from . import fltk
import random
from . import audio
from . import config
from . import utils

#-------Fonctions-------


def nouvelle_partie(nb_joueurs, taille, manches, nb_bots, difficulte_bots):
    """
    Lancement de la partie.
    Arguments:
              nb_joueurs (int) - Le nombre de joueurs.
              taille (int) - La taille du plateau de jeu.
              manches (int) - Nombre de manches.
              nb_bots (int) - Nombre de bots
              difficulte_bots (liste) - Difficulté des éventuels bots.
    """
    config.current_page="dices"

    game = Plateau(nb_joueurs, taille, manches, nb_bots)
    players = utils.attribution_couleurs(nb_joueurs, nb_bots, config.mode_daltonien)
    game.players=players
    
    draw_sidebar(game)
    fltk.rectangle(0, 0, 650, 650, remplissage=config.current_theme[0][0], couleur=config.current_theme[0][0] , tag="lancer_de")

    largeur_bouton, hauteur_bouton = 200, 80
    bouton_x = (600 - largeur_bouton) / 2
    bouton_y = (600 - hauteur_bouton) / 2
    utils.dessiner_bouton(bouton_x, bouton_y, largeur_bouton, hauteur_bouton, "Lancer le dé", "bouton", 1)
    fltk.texte(300, 150, "QUI VA JOUER EN PREMIER?", taille=27, couleur="black", ancrage="center", police='Fixedsys')
    
    fltk.mise_a_jour()
    
    
    x, y = fltk.attend_clic_gauche()

    if utils.est_bouton_clique(x, y, bouton_x, bouton_y, largeur_bouton, hauteur_bouton):
        audio.jouer_son_clic1()
        fltk.efface("bouton")
        
        rolls, gagnants,p = utils.roll_dice(game.players)
        
        if len(gagnants) > 1:
            utils.notification1("Egalité!")
            fltk.efface("dice")
            fltk.attente(1)
            while len(gagnants) > 1:
                rolls, gagnants,p = utils.roll_dice(gagnants)

        first_player = gagnants[0]
        game.ordre_init(p)
        fltk.efface("notif")
        utils.notification1(f"{first_player.nom} commence!")
        fltk.attente(1)

    fltk.efface_tout()
    game.creationtab()
    game.initialisationcolor()
    play(game)

def play(game):
    """
    Lancement de partie à partir d'un plateau de jeu.

    Arguments :
                game : objet de classe Plateau (models.py)
    """
    from .menu import afficher_menu, afficher_parametres
    config.current_page="game"
    hauteur_fenetre, largeur_fenetre = create_graphique(game.taille, game.tab, game)
    draw_sidebar(game)
    utils.dessiner_bouton(700, 580, 200, 50, "Quitter", "quit", 2, 2)
    utils.dessiner_bouton(700, 125, 200, 50, "Sauvegarde", "save", 0, 2)
    utils.dessiner_bouton(700, 500, 200, 50, "Paramètres", "settings", 0, 2)

    while game.partieEnCours:
        fltk.efface("tour_notif")
        draw_pions(game, config.mode_daltonien)

        fltk.mise_a_jour()
        current_player = game.joueurActuel    
        tour_de(game)
        
        if current_player.is_bot:
            fltk.attente(0.9)
            if current_player.difficulte == 1:
                bots.bot_move(game, current_player)
            elif current_player.difficulte == 2:
                bots.bot_coup_moyen(game, current_player)
            elif current_player.difficulte == 3:
                bots.bot_coup_difficile(game, current_player)
            else:
                bots.bot_coup_facile(game, current_player)
            game.joueurActuel = game.next_turn()
            continue
        
        if game.fin_de_manche() and not game.fin_de_partie():
                fltk.efface("scores_notif")
                notification("Fin de la manche!")
                fltk.attente(0.5)
                game.manche+=1
                fltk.efface("pion")
                game.new_manche()
        elif game.fin_de_partie():
                notification("Fin de la partie! Résulats dans un instant...")
                fltk.attente(0.5)
                scores=[]
                gagnant, id ="", 0
                for joueur in game.players:
                    scores.append([joueur.nom, joueur.score])
                    if id<= joueur.score:
                        gagnant=joueur.nom
                        id=joueur.score
                fltk.redimensionne_fenetre(600, 400)
                fltk.efface_tout()
                endgame(scores,gagnant)
                break

        ev = fltk.donne_ev()
        tev = fltk.type_ev(ev)
        
        if tev == 'ClicGauche':
            x_click, y_click = fltk.abscisse(ev), fltk.ordonnee(ev)
            audio.jouer_son_clic2()
            fltk.efface("notif")

            '''Gestion des clics sur les boutons'''
            if utils.est_bouton_clique(x_click, y_click, 700, 500, 200, 50):
                fltk.redimensionne_fenetre(600, 400)
                fltk.efface_tout()
                quick_save(game)
                afficher_parametres()
                break
            elif utils.est_bouton_clique(x_click, y_click, 700, 580, 200, 50):
                fltk.redimensionne_fenetre(600, 400)
                fltk.efface_tout()
                utils.quitting_frompartie()
                afficher_menu()
                break
            elif utils.est_bouton_clique(x_click, y_click, 700, 125, 200, 50):
                fltk.redimensionne_fenetre(600,400)
                fltk.efface_tout()
                affiche_sauvegarde(game)
                break
            y = x_click // (largeur_fenetre // config.taille)  
            x = y_click // (hauteur_fenetre // config.taille)

            
            '''Gestion des clics dans le plateau de jeu.'''
            if 0 <= x < config.taille and 0 <= y < config.taille and game.valid_pos(x, y):
                game.game_on(x, y)
                fltk.efface("scores_notif")
                fltk.efface("tour_notif")
                tour_de(game)
                game.joueurActuel = game.next_turn()
            else:
                notification("Clic invalide")
                fltk.attente(0.1)
    fltk.attend_ev() 