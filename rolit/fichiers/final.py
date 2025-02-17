#-------Import-------
from . import fltk
from . import config
from . import menu
import sys
from . import saving
#-------Fonctions-------
def endgame(score, winner):
    config.current_page="endgame"
    fltk.efface_tout()

    for i in range(4): 
        couleur = config.current_theme[0][i]
        fltk.rectangle(0, i * 100, 600, (i + 1) * 100, remplissage=couleur, epaisseur=0)
    
    fltk.texte(300, 50, "Fin de jeu", taille=30, couleur="black", ancrage="center", police="Comic Sans MS")
    fltk.texte(150, 150, f"Le gagnant est {winner}!", taille=20, couleur="black", ancrage="center", police="Comic Sans MS")

    for i in range(len(score)):
        fltk.texte(30,210+(i*35),f"Score de {score[i][0]}: {score[i][1]}", taille=17, police="Comic Sans MS", couleur="black")

    boutons = [
        (105, 150,"Menu"),
        (170 ,220,"Sauvegarde"),
        (245, 295,"Quitter")
    ]
    positions=[(400, 105),(400,170),(400,245)]
    
    for index, (y1, y2, text) in enumerate(boutons):
        x1, y1 = positions[index] 
        x2 = x1 + 150
        remplissage = config.current_theme[1][index]  
        fltk.rectangle(x1, y1, x2, y2, remplissage=remplissage, epaisseur=2, couleur="black")
        fltk.texte((x1 + x2) // 2, (y1 + y2) // 2, text, taille=20, couleur="black", ancrage="center", police="Comic Sans MS")

    while True:
        x, y= fltk.attend_clic_gauche()
        if 400 <= x <= 550:
            if 105 <= y <= 150:
                fltk.efface_tout()
                menu.afficher_menu()
                break
            elif 170 <= y <= 220:
                fltk.efface_tout()
                saving.affiche_sauvegarde()
                break
            elif 245 <= y <= 295:
                fltk.ferme_fenetre()
                sys.exit()
