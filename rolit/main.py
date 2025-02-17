#################################################
#              Jeu ROLIT - 2024                 #
#       Anastasia Cordun & Niekita Joseph       #
#################################################


#-------Import-------
from fichiers.audio import jouer_musique, ajuster_volume
from fichiers.config import volume, musique_en_cours
from fichiers.menu import afficher_menu, gestion_clic
from fichiers import fltk

#-------Fonctions-------
def main():
    """ 
    Point d'entrée 0 du programme.

    - Lance la musique de fond.
    - Ajuste le volume à 50%.
    - Affiche le menu principal.
    - Gère les clics de l'utilisateur.+
     """
    global musique_en_cours
    jouer_musique()
    musique_en_cours=True
    ajuster_volume(volume)
    fltk.cree_fenetre(600, 400)

    afficher_menu()
    gestion_clic()

if __name__ == "__main__":
    main()
    fltk.ferme_fenetre()
