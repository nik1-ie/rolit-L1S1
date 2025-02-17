#-------Import-------
from . import fltk
import pickle
from datetime import date, datetime
import sys
import os
from . import partie
from . import moteur
from . import config
from . import audio
from . import utils
#-------Constantes-------
slots=[
        [10, 150, "fichiers\save\save1", False],
        [155, 295, "fichiers\save\save2", False],
        [300, 440, "fichiers\save\save3", False],
        [445, 590, "fichiers\save\save4", False]
    ]
past_page=None
#-------Fonction-------
def quick_save(g):
    '''Enregistre la partie en cours afin d'y revenir par la suite.
    Argument :  g objet de classe Plateau (fichier models.py)'''
    save=open("fichiers\save\quick_save", "wb")
    pickle.dump(g,save)
    save.close()
    return

def reprendre_partie():
    '''Reprend la partie en cours.'''
    saved=open("fichiers\save\quick_save", "rb")
    saved_game=pickle.load(saved)
    saved.close()
    fltk.redimensionne_fenetre(950,650)
    partie.play(saved_game)
    return

def check_files():
    '''Fonction vérifiant si le fichier de sauvegarde est occupé ou non.'''
    global slots
    for file in range(len(slots)):
        path=slots[file][2]
        size=os.path.getsize(path)
        if size==0:
            slots[file][3]=False
        elif size!=0:
            slots[file][3]=True
    return

def affiche_sauvegarde(g=None):
    '''Fonction affichant la page de sauvegarde.
    Permet d'enregistrer la partie en cours, ou d'accèder à une partie enregistrée.
    Argument:
              g (class Plateau) - Plateau de jeu éventuel à enregistrer.
    Fonctions :
                save - fonction permettant d'enregistrer la partie en cours.
                load - fonction permettant de charger une partie.'''
    #global slots, past_page
    from .menu import afficher_menu
    if config.current_page=="game" or config.current_page=="menu":
        past_page=config.current_page
    if g!=None:
        quick_save(g)

    config.current_page="save"
    fltk.efface_tout()

    for i in range(4): 
        couleur = config.current_theme[0][i]
        fltk.rectangle(0, i * 100, 600, (i + 1) * 100, remplissage=couleur, epaisseur=0)
    
    fltk.texte(300, 50, "Sauvegardes", taille=30, couleur="black", ancrage="center", police="Fixedsys")

    fltk.rectangle(530, 25, 580, 75, epaisseur=2, remplissage=config.current_theme[1][2])
    fltk.texte((530+580)//2, (25+75)//2, "❌", police="Fixedsys", taille=15, ancrage="center")

    check_files()
    for index, (x1, x2, file, used) in enumerate(slots):
        saved=open(file, "rb")
        middle=(x1+x2)//2
        fltk.rectangle(x1, 100, x2, 300, remplissage=config.current_theme[1][0], epaisseur=1, couleur="black")
        fltk.texte(middle, 130, f" {index+1}", taille=15, police="Fixedsys", ancrage="center", couleur="black")

        fltk.rectangle(x1+5, 260, middle-5, 295, remplissage=config.current_theme[0][1], epaisseur=1, couleur="black", tag="save")
        fltk.texte((x1 + middle)//2, (260+295)//2, "save", taille=15, police="Fixedsys", ancrage="center")

        if used==True:
            fltk.rectangle(middle+5, 260, x2-5, 295, remplissage=config.current_theme[0][1], epaisseur=1, couleur="black", tag="load")
            fltk.texte((middle + x2)//2, (260+295)//2, "load", taille=15, police="Fixedsys", ancrage="center")
            saved=pickle.load(saved)
            day=saved.day
            time=saved.time
            manche, manche_max= saved.manche, saved.manchemax
            players= saved.n
            fltk.texte(middle,160, day, taille=12, police="Fixedsys", ancrage="center")
            fltk.texte(middle,180, time, taille=12, police="Fixedsys", ancrage="center")
            fltk.texte(middle, 200, f"{players} joueurs", taille=12, police="Fixedsys", ancrage="center")
            fltk.texte(middle, 220, f"Manche {manche}/{manche_max}", taille=12, police="Fixedsys", ancrage="center")


    def save(n, game):
        '''Enregistre une partie.
        Arguments : n (int) - emplacement choisi
                    game (class Plateau) - partie à enregistrer'''
        if game==None:
            return
        slot=open(slots[n][2], "wb")
        pickle.dump(game,slot)
        slot.close()
        return

    def load(n):
        '''Charge une partie à partir de sa position dans la sauvegarde
        Argument: n (int) - emplacement de sauvegarde'''
        slot=open(slots[n][2], "rb")
        saved_game=pickle.load(slot)

        dayy= date.today()
        dayy=dayy.strftime("%B %d, %Y")
        timee=str(datetime.now())
        timee=timee[11:]
        timee=timee[:5]
        saved_game.day=dayy
        saved_game.time=timee

        config.taille=saved_game.taille
        config.manches=saved_game.manchemax
        config.nb_joueurs=saved_game.n
        config.nb_bots=saved_game.nb_bots


        slot.close()
        fltk.redimensionne_fenetre(950,650)
        partie.play(saved_game)
        return
    
    while True:
        x, y = fltk.attend_clic_gauche()
        audio.jouer_son_clic1()
        if 530 <= x <= 580 and 25 <= y <= 75:
            if past_page=="menu":
                fltk.efface_tout()
                afficher_menu()
            elif past_page=="game":
                reprendre_partie()
        elif 15 <= x <= 75 and 260 <= y <= 295:
            save(0,g)
            fltk.efface_tout()
            affiche_sauvegarde()
        elif (85 <= x <= 145 and 260 <= y <= 295) and slots[0][3]==True:
            load(0)
        elif 160 <= x <= 220 and 260 <= y <= 295:
            save(1,g)
            fltk.efface_tout()
            affiche_sauvegarde()
        elif (225 <= x <= 290 and 260 <= y <= 295) and slots[1][3]==True:
            load(1)
        elif 305 <= x <= 365 and 260 <= y <= 295:
            save(2,g)
            fltk.efface_tout()
            affiche_sauvegarde()
        elif (375 <= x <= 435 and 260 <= y <= 295) and slots[2][3]==True:
            load(2)
        elif 450 <= x <= 512 and 260 <= y <= 295:
            save(3,g)
            fltk.efface_tout()
            affiche_sauvegarde()
        elif (522 <= x <= 585 and 260 <= y <= 295) and slots[3][3]==True:
            load(3)
        else:
            fltk.attend_clic_gauche()