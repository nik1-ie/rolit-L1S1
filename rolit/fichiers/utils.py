# ------- Import -------
import random
from .moteur import Joueurs, Plateau
from . import config
from . import fltk
import time

# ------- Fonctions -------


def attribution_couleurs(nb_joueurs, nb_bots, mode_daltonien):
    """
    Attribue des couleurs et des formes aux joueurs et aux bots en fonction du nombre de joueurs.
    - nb_joueurs: (int) Le nombre de joueurs humains.
    - nb_bots: (int) Le nombre de bots.
    - mode_daltonien: (bool) Activer le mode daltonien ou non.
    - return: Deux listes contenant les objets Joueurs (joueurs humains et bots).
    """
    formes = ['cercle', 'carre', 'triangle', 'etoile']
    joueurs = []
    difficultes = [3, 2, 1]
    if nb_joueurs == 1:
        if nb_bots == 1:
            joueurs.append(Joueurs('rouge', 'R', formes[0] if not mode_daltonien else formes[0], is_bot=False))
            joueurs.append(Joueurs('vert', 'V', formes[0] if not mode_daltonien else formes[1], is_bot=True, difficulte=difficultes[0]))
        elif nb_bots == 2:
            joueurs.append(Joueurs('rouge', 'R', formes[0] if not mode_daltonien else formes[0], is_bot=False))
            joueurs.append(Joueurs('jaune', 'J', formes[0] if not mode_daltonien else formes[1], is_bot=True, difficulte=difficultes[0]))
            joueurs.append(Joueurs('vert', 'V', formes[0] if not mode_daltonien else formes[2], is_bot=True, difficulte=difficultes[1]))
        elif nb_bots == 3:
            joueurs.append(Joueurs('rouge', 'R', formes[0] if not mode_daltonien else formes[0], is_bot=False))
            joueurs.append(Joueurs('jaune', 'J', formes[0] if not mode_daltonien else formes[1], is_bot=True, difficulte=difficultes[0]))
            joueurs.append(Joueurs('vert', 'V', formes[0] if not mode_daltonien else formes[2], is_bot=True, difficulte=difficultes[1]))
            joueurs.append(Joueurs('bleu', 'B', formes[0] if not mode_daltonien else formes[3], is_bot=True, difficulte=difficultes[2]))

    elif nb_joueurs == 2:
        joueurs.append(Joueurs('rouge', 'R', formes[0] if not mode_daltonien else formes[0], is_bot=False))
        joueurs.append(Joueurs('vert', 'V', formes[0] if not mode_daltonien else formes[1], is_bot=nb_bots > 0, difficulte=difficultes[0] if nb_bots > 0 else 0))
    elif nb_joueurs == 3:
        joueurs.append(Joueurs('rouge', 'R', formes[0] if not mode_daltonien else formes[0], is_bot=False))
        joueurs.append(Joueurs('jaune', 'J', formes[0] if not mode_daltonien else formes[1], is_bot=nb_bots > 0, difficulte=difficultes[0] if nb_bots > 0 else 0))
        joueurs.append(Joueurs('vert', 'V', formes[0] if not mode_daltonien else formes[2], is_bot=nb_bots > 1, difficulte=difficultes[1] if nb_bots > 1 else 0))
    elif nb_joueurs == 4:
        joueurs.append(Joueurs('rouge', 'R', formes[0] if not mode_daltonien else formes[0], is_bot=False))
        joueurs.append(Joueurs('jaune', 'J', formes[0] if not mode_daltonien else formes[1], is_bot=nb_bots > 0, difficulte=difficultes[0] if nb_bots > 0 else 0))
        joueurs.append(Joueurs('vert', 'V', formes[0] if not mode_daltonien else formes[2], is_bot=nb_bots > 1, difficulte=difficultes[1] if nb_bots > 1 else 0))
        joueurs.append(Joueurs('bleu', 'B', formes[0] if not mode_daltonien else formes[3], is_bot=nb_bots > 2, difficulte=difficultes[2] if nb_bots > 2 else 0))

    return joueurs


def afficher_face_cube(numero, x, y, couleur, largeur=100, hauteur=100):
    '''Cette fonction va afficher les faces d'un cube lors du lancer de dé.
    Arguments : numero (int) - chiffre/face de dé à afficher.
                x, y (int) - coordonnées x et y de l'image.
                couleur (str) - couleur du fond de l'image afin de l'associer à un joueur.
                largeur, hauteur (int) : taille de l'image du dé.'''
    chemin_image = f"images/dice_{numero}.png"
    fltk.rectangle(x - (largeur + 30) // 2, y - (hauteur + 30) // 2, x + (largeur + 30) // 2, y + (hauteur + 30) // 2, 
                   remplissage=couleur, couleur=couleur, epaisseur=2, tag="dice")

    fltk.image(x, y, chemin_image, largeur=largeur+70, hauteur=hauteur+70, ancrage="center")
    
    
def lancer_animation_cube(x, y, couleur):
    '''Fonction parmettant d'animer le dé.
    Arguments : numero (int) - chiffre/face de dé à afficher.
                x, y (int) - coordonnées x et y de l'image.'''
    dernier_resultat = 0
    for _ in range(10):  
        numero_aleatoire = random.randint(1, 6) 
        afficher_face_cube(numero_aleatoire, x, y, couleur)
        fltk.mise_a_jour()
        time.sleep(0.2)
        dernier_resultat = numero_aleatoire  
    return dernier_resultat


def roll_dice(players):
    '''Fonction gérant le lancé de dé.
    Arguments : players (liste) - liste des joueurs.
    Return : roll
             gagnant - gagnant du tirage au sort.'''
    fltk.efface("dice")
    rolls = {}
    max_roll = 0
    gagnants = []
    nb_total = len(players)
    
    x_offset = 100 
    y_position = 300
    
    if nb_total == 2:
        x_offset += 150
    elif nb_total == 3:
        x_offset += 75
        
    couleurs = ['red', 'green', 'yellow', 'blue'] 
    p=None
    for i, player in enumerate(players):
        couleur = couleurs[i % len(couleurs)]  
        roll = lancer_animation_cube(x_offset, y_position, couleur)  
        rolls[player] = roll  
        x_offset += 150  
        
        if roll > max_roll:
            max_roll = roll
            gagnants = [player]
            p=player
        elif roll == max_roll:
            gagnants.append(player)
    return rolls, gagnants, p



def notification1(message):
    fltk.texte(300, 450, message, ancrage='center', taille=25, tag="notif", police = "Fixedsys")
    fltk.mise_a_jour()
    
def dessiner_bouton(x, y, largeur, hauteur, texte, tag, id=3, epaisseur=0):
    fltk.rectangle(x, y, x + largeur, y + hauteur, remplissage=config.current_theme[1][id], couleur="black", epaisseur=epaisseur, tag=tag)
    fltk.texte(x + largeur/2, y + hauteur/2, texte, ancrage='center', taille=20, tag=tag, police='Fixedsys')
    return x, y, x+largeur, y+hauteur

def est_bouton_clique(x, y, bouton_x, bouton_y, largeur_bouton, hauteur_bouton):
    '''Fonctions déterminant si un bouton est cliqué
    Argument : x_click (int)- coordonnée x du clic
               y_click (int - coordonnée y du clic
               bouton_x (int) - coordonnée x du bouton
               bouton_y (int) - coordonnée y du bouton
               largeur_bouton, hauteur_bouton (int)- largeur et hauteur du bouton
    Return :  Booleen'''
    return bouton_x <= x <= bouton_x + largeur_bouton and bouton_y <= y <= bouton_y + hauteur_bouton

def quitting_frompartie():
    '''Fonction appelée pour réinitialiser les paramètres du jeu.'''
    config.nb_joueurs = 2
    config.taille = 8
    config.manches = 3
    config.volume= 0.5
    config.nb_bots = 0
    config.difficulte_bots = []
    config.manches=3
    config.mode_daltonien=False
