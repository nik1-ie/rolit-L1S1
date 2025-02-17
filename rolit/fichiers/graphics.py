#-------Import-------
from . import fltk
import math
from . import config
from .drawing import dessiner_secteur

#-------Fonctions-------

def create_graphique(taille, plateau, game):
    """
    Crée l'interface graphique pour afficher le plateau de jeu.

    - paramètre: (int) taille = La taille du plateau.
    - paramètre: (objet) plateau = L'objet représentant le plateau de jeu.
    - retourne: (tuple) hauteur_fenetre, largeur_fenetre = Dimensions de la fenêtre.
    """
    hauteur_fenetre = 650
    largeur_fenetre = 650
    taille = taille
    couleurs = {'R': "red", 'J': "yellow", 'B': "blue", 'V': "green"}
    case_size = hauteur_fenetre // taille
    rayon_cercle = case_size // 3  

    fltk.efface_tout()
    for i in range(1, taille):
        fltk.ligne(i * (hauteur_fenetre // taille), 0, i * (hauteur_fenetre // taille), hauteur_fenetre)
        fltk.ligne(0, i * (largeur_fenetre // taille), largeur_fenetre, i * (largeur_fenetre // taille))


    centre = taille // 2
    couleurs_initiales = ['R', 'J', 'B', 'V']
    positions = [(centre-1, centre-1), (centre-1, centre), (centre, centre-1), (centre, centre)]
    
    game.initialisationcolor()
    '''for (i, j), couleur in zip(positions, couleurs_initiales):
        x_centre = j * case_size + case_size // 2
        y_centre = i * case_size + case_size // 2
        if config.mode_daltonien:
            forme = game.players[couleurs_initiales.index(couleur)-2].symbole
            dessiner_figures(x_centre, y_centre, forme)
        else:
            couleur_cercle = couleurs[couleur]
            fltk.cercle(x_centre, y_centre, rayon_cercle, 
                        couleur=couleur_cercle, remplissage=couleur_cercle, epaisseur=1, tag="pion")'''
    return hauteur_fenetre, largeur_fenetre

def draw_pions(plateau, mode_daltonien=False):
    """
    Dessine les pions sur le plateau avec des cercles ou des formes pour les daltoniens.

    - Argument : (objet) plateau = L'objet représentant le plateau de jeu.
    - Argument : (bool) mode_daltonien = Si True, dessine des formes au lieu de cercles.
    """
    couleurs = {'R': "red", 'J': "yellow", 'B': "blue", 'V': "green"}
    hauteur_fenetre = 650
    largeur_fenetre = 650
    taille = plateau.taille
    case_size = hauteur_fenetre // taille
    rayon_cercle = case_size // 3  
    
    fltk.efface("pion")
    for i in range(taille):
        for j in range(taille):
            x_centre = j * case_size + case_size // 2
            y_centre = i * case_size + case_size // 2
            
            if not mode_daltonien:
                fltk.cercle(x_centre, y_centre, rayon_cercle, 
                            couleur="white", remplissage="white", epaisseur=0, tag="pion")
            
            couleur = plateau.tab[i][j]
            joueur = None
            
            for player in plateau.players:  
                if player.id == couleur:
                    joueur = player
                    break

            if joueur:
                if mode_daltonien:
                    forme = joueur.symbole  
                    dessiner_figures(x_centre, y_centre, forme)  
                else:
                    couleur_cercle = couleurs.get(couleur, "white")
                    fltk.cercle(x_centre, y_centre, rayon_cercle, 
                                couleur=couleur_cercle, remplissage=couleur_cercle, epaisseur=1, tag="pion")
    

    fltk.mise_a_jour
      
def dessiner_figures(x, y, forme):
    taille = 25  

    if forme == "cercle":
        fltk.cercle(x, y, taille, remplissage="red", couleur="red", tag="pion") 
    elif forme == "carre":
        fltk.rectangle(x - taille, y - taille, x + taille, y + taille, remplissage="green", couleur="green", tag="pion")
    elif forme == "triangle":
        fltk.polygone([(x, y - taille), (x - taille, y + taille), (x + taille, y + taille)], remplissage="blue", couleur="blue", tag="pion") 
    elif forme == "etoile":
        fltk.polygone([(x, y - taille), (x - taille // 2, y - taille // 2), (x - taille, y),
                       (x - taille // 2, y + taille // 2), (x, y + taille),
                       (x + taille // 2, y + taille // 2), (x + taille, y),
                       (x + taille // 2, y - taille // 2)], remplissage="yellow", couleur="yellow", tag="pion")



def draw_sidebar(game):
    """
    Dessine la barre latérale du jeu à côté du plateau.

    - paramètre: (objet) game = L'objet représentant le jeu.
    """
    hauteur_fenetre=650
    largeur_plateau=650
    largeur_fenetre=largeur_plateau+300

    for i in range(4):
        couleur = config.current_theme[0][i]
        fltk.rectangle(largeur_plateau, (i*100), largeur_fenetre, (hauteur_fenetre/4)*100, remplissage=couleur, epaisseur=0)

    fltk.texte(210+515, 70, "R", taille=40, couleur="darkblue", ancrage="center", police="Fixedsys")
    fltk.texte(255+515, 70, "o", taille=40, couleur="blue", ancrage="center", police="Fixedsys")
    fltk.texte(295+515, 70, "l", taille=40, couleur="darkblue", ancrage="center", police="Fixedsys")
    fltk.texte(335+515, 70, "i", taille=40, couleur="darkblue", ancrage="center", police="Fixedsys")
    fltk.texte(375+515, 70, "t", taille=40, couleur="darkblue", ancrage="center", police="Fixedsys")

    x_center, y_center = 255+515, 70
    radius = 23

    dessiner_secteur(x_center, y_center, radius, 0, 90, "red")
    dessiner_secteur(x_center, y_center, radius, 90, 180, "green")
    dessiner_secteur(x_center, y_center, radius, 180, 270, "blue")
    dessiner_secteur(x_center, y_center, radius, 270, 360, "yellow")

    if config.current_page == "game":
        fltk.texte(620+50,162.5+70, "Au tour de:", taille=15, police="Comic Sans MS")
        couleur_joueur = {'R': "red", 'J': "yellow", 'B': "blue", 'V': "green"}
        couleur_cercle = couleur_joueur.get(game.joueurActuel.id)
        x_cercle = 620 + 50 + 200 
        y_cercle = 162.5 + 70 + 10  
        
        rayon_cercle = 30
        fltk.cercle(x_cercle, y_cercle, rayon_cercle, couleur="black", remplissage="black", tag="tour_notif")
        fltk.cercle(x_cercle, y_cercle, rayon_cercle - 2, couleur=couleur_cercle, remplissage=couleur_cercle, tag="tour_notif")



def tour_de(game):
    couleur_joueur = {'R': "red", 'J': "yellow", 'B': "blue", 'V': "green"}
    couleur_cercle = couleur_joueur.get(game.joueurActuel.id)
    x_cercle = 620 + 50 + 200 
    y_cercle = 162.5 + 70 + 10  
    
    rayon_cercle = 30
    fltk.cercle(x_cercle, y_cercle, rayon_cercle, couleur="black", remplissage="black", tag="tour_notif")
    fltk.cercle(x_cercle, y_cercle, rayon_cercle - 2, couleur=couleur_cercle, remplissage=couleur_cercle, tag="tour_notif")

    for i in range(len(game.players)):
        couleur_j=couleur_joueur.get(game.players[i])
        fltk.texte(620+50, y_cercle + 60+(i*40), f"Le score de {game.players[i].nom}: {game.players[i].score}", taille=15, police="Fixedsys", couleur=couleur_j, tag="scores_notif")
    fltk.mise_a_jour

def notification(txt):
    fltk.texte(620+50, 162.5+95, txt, taille=15, police="Fixedsys", tag="notif")
    fltk.mise_a_jour()