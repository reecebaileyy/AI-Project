from games import Game, GameState

class GameOfNim(Game):
    """Implements the Game of Nim according to project specifications."""

    def __init__(self, board):
        """
        Initializes the Game of Nim with a given starting board.
        Example: [7, 5, 3, 1] means 4 piles with 7, 5, 3, and 1 objects.
        """
        moves = self._generate_moves(board)
        self.initial = GameState(to_move='MAX', utility=0,
                                 board=board, moves=moves)

    def _generate_moves(self, board):
        """Return all valid (row, num_removed) moves for a given board."""
        moves = []
        for r, count in enumerate(board):
            for n in range(1, count + 1):
                moves.append((r, n))
        return moves

    def actions(self, state):
        """Return a list of all valid moves for the given state."""
        return state.moves

    def result(self, state, move):
        """
        Apply a move (r, n) to a state and return the resulting GameState.
        """
        r, n = move
        board = state.board.copy()
        board[r] -= n 

        next_player = 'MIN' if state.to_move == 'MAX' else 'MAX'
        moves = self._generate_moves(board)

        utility = 0
        if self.terminal_test(GameState(next_player, 0, board, moves)):
            utility = -1 if state.to_move == 'MAX' else 1

        return GameState(to_move=next_player, utility=utility,
                         board=board, moves=moves)

    def terminal_test(self, state):
        """Return True if all piles are empty (game over)."""
        return all(x == 0 for x in state.board)

    def utility(self, state, player):
        """
        Return the utility of the state for the given player:
        +1 if player wins, -1 if player loses.
        """
        return state.utility if player == 'MAX' else -state.utility

    def display(self, state):
        """Print the current board configuration."""
        print(f"board: {state.board}")
