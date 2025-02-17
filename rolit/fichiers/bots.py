import random
from . import config

def bot_move(game, joueur_actuel):
    """
    Bot facile : fait un coup aléatoire.
    """
    valid_moves = game.get_valid_muvs()
    if valid_moves:
        muv = random.choice(valid_moves)
        game.game_on(muv[0], muv[1])

def bot_coup_moyen(game, joueur_actuel):
    """
    Bot moyen : choisit le coup qui capture le plus de pièces.
    """
    valid_muvs = game.get_valid_muvs()
    best_muv = None
    max_captures = -1

    for muv in valid_muvs:
        temp_game = game.copy()
        temp_game.game_on(muv[0], muv[1])

        captures = count_captures(temp_game, joueur_actuel)
        if captures > max_captures:
            max_captures = captures
            best_muv = muv

    if best_muv:
        game.game_on(best_muv[0], best_muv[1])

def bot_coup_difficile(game, joueur_actuel):
    """
    Bot difficile : fait un coup qui maximise ses chances à long terme.
    """
    valid_muvs = game.get_valid_muvs()
    best_muv = None
    best_score = -float('inf')

    for muv in valid_muvs:
        temp_game = game.copy()
        temp_game.game_on(muv[0], muv[1])

        score = evaluate_position(temp_game, joueur_actuel)
        if score > best_score:
            best_score = score
            best_muv = muv

    if best_muv:
        game.game_on(best_muv[0], best_muv[1])

def count_captures(game, player):
    """
    Compte le nombre de pièces capturées après un coup.
    """
    opponent = game.players[1] if player == game.players[0] else game.players[0]
    return sum(1 for x in range(config.taille) for y in range(config.taille) 
               if game.tab[x][y] == opponent.id)

def evaluate_position(game, player):
    """
    Évalue une position simple pour le bot difficile.
    """
    player_score = player.score  
    opponent = game.players[1] if player == game.players[0] else game.players[0]
    opponent_score = opponent.score

    return player_score - opponent_score


