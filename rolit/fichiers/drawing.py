#-------Import-------
import math
from .fltk import rectangle, ligne, texte

#-------Fonctions-------
def dessiner_secteur(x, y, rayon, angle_debut, angle_fin, couleur):
    """
    Dessine un secteur de cercle.

    - paramètre: (int) x = La coordonnée x du centre du cercle.
    - paramètre: (int) y = La coordonnée y du centre du cercle.
    - paramètre: (int) rayon = Le rayon du cercle.
    - paramètre: (int) angle_debut = L'angle de départ du secteur.
    - paramètre: (int) angle_fin = L'angle de fin du secteur.
    - paramètre: (str) couleur = La couleur des lignes du secteur.
    """
    points = []
    for angle in range(angle_debut, angle_fin):
        x_point = x + rayon * math.cos(math.radians(angle))
        y_point = y + rayon * math.sin(math.radians(angle))
        points.append((x_point, y_point))
    
    for i in range(len(points) - 1):
        ligne(x, y, points[i][0], points[i][1], couleur)
        ligne(x, y, points[i+1][0], points[i+1][1], couleur)