#-------Import-------
import random
from datetime import date, datetime
from .config import mode_daltonien
import copy
#-------Fonctions-------
class Joueurs:
    '''Représente chaque joueur dans le jeu.
    
    Attributs:  nom (str) - Nom du joueur
                id (str) - Identifiant du joueur sur le plateau
                score (int) - Score du joueur actualisé au fil de la partie'''
    def __init__(self, nom, i, symbole, is_bot=False, difficulte=0):
        self.nom = nom
        self.id = i
        self.score = 1
        self.symbole = symbole
        self.is_bot = is_bot
        self.difficulte = difficulte if is_bot else 0


class Plateau:
    '''Représente le plateau de jeu et contient tout ses paramètres
    Cette classe assure le fonctionnement du jeu.
    
    Attributs : n (int) - Nombres de joueurs, choisi par l'utilisateur.
                tab (list) - Plateau de jeu sous forme de liste, actualisé au fur et à mesure.
                ordre (list) - Ordre de passage des joueurs après le lancé de dé.
                players (list) - Liste des joueurs (liste d'objets de classe Joueurs)
                partieEnCours (bool) - True si la partie est en cours, False si la partie n'est pas en cours.
                manche (int) - Numéro de manche actuelle
                manchemax (int) - Nombres de manches au total, choisi par l'utilisateur.
                joueurActuel (objet de classe Joueurs) - Joueur dont c'est le tour.
                nextPlayer (objet de classe Joueurs) - Joueur qui jouera au prochain tour.
                taille (int) - Taille du plateau, choisi par l'utilisateur.
                index (int) - Index nous situant dans la liste d'ordre de passage.
                day (str) - Jour où la partie a été lancée.
                time (str) - Heure à laquelle la partie a été lancée.
                
    Méthodes : creationtab - Crée le plateau de jeu sous forme de liste, selon la taille choisie.
               initialisationcolor - Pose les premiers pions au centre du plateau de jeu.
               lance_de - Détermine le premier joueur.
               valid_pos - Vérifie que la position souhaitée par le joueur est possible.
               new_manche - Initialise une nouvelle manche.
               fin_de_manche - Détermine si une manche est finie.
               fin_de_partie - Détermine si la partie est finie.
               next_turn - Détermine le prochain joueur.
               game_on - Pose un pion et détermine où capturer. 
               capture_direction - Capture les pions.'''
    
    def __init__(self, nb=2, taille=8, manche=2, nb_bots=0):
        self.n = nb
        self.tab = []
        self.ordre = []
        self.players = None
        self.partieEnCours = True
        self.manche= 0
        self.nb_bots= nb_bots
        self.manchemax= manche
        self.joueurActuel = None
        self.nextPlayer = None
        self.score_totaux = 4
        self.taille = taille
        self.index = 0
        self.valid_positions= set()

        self.day=date.today()
        self.day=self.day.strftime("%B %d, %Y")
        self.time=str(datetime.now())
        self.time=self.time[11:]
        self.time=self.time[:5]

    def creationtab(self):
        """Crée un plateau de jeu vide avec la taille spécifiée."""
        self.tab = [[0] * self.taille for i in range(self.taille)]

    def initialisationcolor(self):
        """
        Initialise le plateau avec les couleurs de départ des pions ou de leur forme pour le mode daltonien.
        Le placement des pions dépend de la taille du plateau.
        
        - Return: (list) Le plateau avec les pions initialisés.
        """
        centre = self.taille // 2
        if self.taille % 2 == 0:
        
            self.tab[centre - 1][centre - 1] = 'R' if not mode_daltonien else 'cercle'  
            self.tab[centre - 1][centre] = 'J' if not mode_daltonien else 'carre'      
            self.tab[centre][centre - 1] = 'B' if not mode_daltonien else 'triangle'   
            self.tab[centre][centre] = 'V' if not mode_daltonien else 'etoile'       
        else: 
            self.tab[centre][centre] = 'R' if not mode_daltonien else 'cercle'           
            self.tab[centre - 1][centre] = 'J' if not mode_daltonien else 'carre'       
            self.tab[centre][centre - 1] = 'B' if not mode_daltonien else 'triangle'     
            self.tab[centre - 1][centre - 1] = 'V' if not mode_daltonien else 'etoile'   
        return self.tab

    def ordre_init(self, first):
        self.ordre = []  
        self.joueurActuel = first
        joueurs=self.players
        index = joueurs.index(first)

        ordre_classObject = [joueurs[i] for i in range(index, len(joueurs))] + \
                     [joueurs[i] for i in range(index)]
        
        self.ordre = [joueurs[i].nom for i in range(index, len(joueurs))] + \
                     [joueurs[i].nom for i in range(index)]
        
        self.index = 0
        self.nextPlayer = ordre_classObject[self.index+1]

    def valid_pos(self, x, y):
        """
        Vérifie si un pion peut être placé à la position souhaitée (x, y).
        
        - param x: (int) La coordonnée x de la case.
        - param y: (int) La coordonnée y de la case.
        - retourne: (bool) True si la position est valide, False sinon.
        """
        if self.tab[x][y] != 0:  
            return False

        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue  
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.taille and 0 <= ny < self.taille and self.tab[nx][ny] != 0:
                    return True 
        return False

    def new_manche(self):
        '''Va initialiser la prochaine manche.'''
        self.tab= [[0] * self.taille for i in range(self.taille)]
        self.initialisationcolor()


    def fin_de_manche(self):
        """
        Vérifie si la manche est terminée.
        
        - Return: (bool) True si la partie est terminée, False sinon.
        """
        for row in self.tab:
            if 0 in row:
                return False
        return True

    def fin_de_partie(self):
        '''Vérifie si la partie est terminée
        Return : booléen - True si la partie est terminée, False sinon.'''
        if self.manche >= self.manchemax and self.fin_de_manche:
            return True
        return False

    def next_turn(self):
        """
        Passe au joueur suivant et retourne le joueur actuel.
        
        - Return: (objet de classe Joueurs) Le joueur actuel après le changement de tour.
        """
        self.index = (self.index + 1) % len(self.ordre)  
        prochain_nom = self.ordre[self.index]
        nom_dapres = self.ordre[(self.index + 1) % len(self.ordre)]
     
        for joueur in range(len(self.players)):
            if self.players[joueur].nom == prochain_nom:
                self.joueurActuel = self.players[joueur]
            elif self.players[joueur].nom == nom_dapres:
                self.nextPlayer = self.players[joueur]
        return self.joueurActuel


    def game_on(self, x, y):
        """
        Met à jour le plateau après un coup et effectue les captures.
        
        - param x: (int) La coordonnée x du coup.
        - param y: (int) La coordonnée y du coup.
        """
        self.joueurActuel.score +=1
        identifiant = self.joueurActuel.id
        self.tab[x][y] = identifiant

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1), 
                      (-1, -1), (-1, 1), (1, -1), (1, 1)]  

        for dx, dy in directions:
            self.capture_direction(x, y, dx, dy, identifiant)

    def capture_direction(self, x, y, dx, dy, joueur_id):
        """
        Vérifie et effectue les captures dans une direction donnée. Actualise les scores.
        
        - param x: (int) La coordonnée x du coup.
        - param y: (int) La coordonnée y du coup.
        - param dx: (int) La direction sur l'axe x.
        - param dy: (int) La direction sur l'axe y.
        - param joueur_id: (int) L'identifiant du joueur effectuant la capture.
        """
        i, j = x + dx, y + dy
        captures = []  

     
        while 0 <= i < self.taille and 0 <= j < self.taille:
            if self.tab[i][j] == 0: 
                return
            if self.tab[i][j] == joueur_id:  
                for cx, cy in captures:
                    joueur_mange=self.tab[cx][cy]
                    for p in self.players:
                        if p.id==joueur_mange:
                            p.score-=1
                            break
                    self.tab[cx][cy] = joueur_id 
                    self.joueurActuel.score += 1
                return
            captures.append((i, j))  
            i, j = i + dx, j + dy
            
        
    def get_valid_muvs(self):
        valid_moves = []
        for x in range(self.taille):
            for y in range(self.taille):
                if self.valid_pos(x, y): 
                    valid_moves.append((x, y)) 
        return valid_moves
    
    def copy(self):
        return copy.deepcopy(self)

