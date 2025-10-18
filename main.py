from games import query_player
from game_of_nim import GameOfNim

def alphabeta_player(game, state):
    moves = game.actions(state)
    if not moves:
        return None
    return moves[0]

if __name__ == "__main__":
    nim = GameOfNim([7, 5, 3, 1])
    nim.play_game(alphabeta_player, query_player)
