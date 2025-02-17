#-------Import-------
import pygame
from . import config
pygame.mixer.init()

#-------Fonctions-------
def jouer_musique(chemin=r"audio\background.mp3"):
    """
    Joue la musique de fond en boucle.

    - paramètre: (str) = Le chemin vers le fichier audio.
    """
    config.musique_en_cours=True
    pygame.mixer.music.load(chemin)
    pygame.mixer.music.play(-1, 0.0)

def arreter_musique():
    """
    Arrête la musique.
    """
    pygame.mixer.music.stop()

def ajuster_volume(vol):
    """
    Définit le volume de la musique.

    - paramètre: (float) = Le volume, une valeur entre 0.0 et 1.0.
    """
    pygame.mixer.music.set_volume(vol)

def jouer_son_clic1():
    """
    Joue le son de clic 1 (dans le menu).
    """
    son_clic = pygame.mixer.Sound(r"audio\click1.wav")
    son_clic.play()

def jouer_son_clic2():
    """
    Joue le son de clic 2 (dans le jeu).
    """
    son_clic = pygame.mixer.Sound(r"audio\click2.wav")
    son_clic.play()
