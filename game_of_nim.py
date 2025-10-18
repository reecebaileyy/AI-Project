from games import Game, GameState

class GameOfNim(Game):
    """Implements the Game of Nim according to project specifications."""

    def __init__(self, initial_board):
        moves = self._generate_moves(initial_board)
        initial_state = GameState(to_move='MAX', utility=0,
                                board=initial_board, moves=moves)
        self.initial = initial_state  # store manually since parent has no __init__


    # -----------------------------------------------------------------------
    # Helper: generate all possible moves given a board configuration
    # -----------------------------------------------------------------------
    def _generate_moves(self, board):
        """Return all valid moves from the given board."""
        moves = []
        for r, count in enumerate(board):
            for n in range(1, count + 1):  # can remove 1 up to count items
                moves.append((r, n))
        return moves

    # -----------------------------------------------------------------------
    # Core Methods Required by Abstract Class Game
    # -----------------------------------------------------------------------

    def actions(self, state):
        """Return a list of all valid moves (r, n) for the current state."""
        return state.moves

    def result(self, state, move):
        """
        Given a state and a valid move (r, n),
        return the new GameState after applying the move.
        """
        r, n = move
        board = state.board.copy()
        board[r] -= n  # remove n objects from pile r

        next_player = 'MIN' if state.to_move == 'MAX' else 'MAX'
        moves = self._generate_moves(board)

        # Check if the game is over (no objects left)
        utility = 0
        if self.terminal_test(GameState(next_player, 0, board, moves)):
            # Player who took the last move loses
            utility = -1 if state.to_move == 'MAX' else 1

        return GameState(to_move=next_player, utility=utility,
                         board=board, moves=moves)

    def terminal_test(self, state):
        """Return True if the game is over (all piles empty)."""
        return all(x == 0 for x in state.board)

    def utility(self, state, player):
        """
        Return the utility of the state for the given player:
        +1 if player wins, -1 if player loses.
        """
        return state.utility if player == 'MAX' else -state.utility

    # -----------------------------------------------------------------------
    # Optional Debug/Play Helper
    # -----------------------------------------------------------------------
    def display(self, state):
        """Print the current board state."""
        print(f"board: {state.board}")
