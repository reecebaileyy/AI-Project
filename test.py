import unittest
from game_of_nim import GameOfNim
from games import GameState

class TestGameOfNim(unittest.TestCase):
    def setUp(self):
        """Initialize a small Nim board for testing."""
        self.game = GameOfNim([5, 3, 1])
        self.initial_state = self.game.initial

    # Testing the constructor and moves
    def test_initial_moves(self):
        expected_moves = [
            (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (1, 1), (1, 2), (1, 3), (2, 1)
        ]
        self.assertEqual(self.initial_state.moves, expected_moves)

    # Checking that actions() returns same list as GameState.moves
    def test_actions_returns_valid_moves(self):
        self.assertEqual(self.game.actions(self.initial_state), self.initial_state.moves)

    # Checkking that result() produces correct new state
    def test_result_updates_board_correctly(self):
        move = (0, 2)  # remove 2 from row 0
        new_state = self.game.result(self.initial_state, move)
        self.assertEqual(new_state.board, [3, 3, 1])
        self.assertEqual(new_state.to_move, 'MIN')

    # Checking that terminal_test() detects empty board
    def test_terminal_state(self):
        terminal_state = GameState(to_move='MIN', utility=0, board=[0, 0, 0], moves=[])
        self.assertTrue(self.game.terminal_test(terminal_state))

    # Testing utility() values when game ends
    def test_utility_values(self):
        last_move_state = GameState(to_move='MIN', utility=-1, board=[0, 0, 0], moves=[])
        self.assertEqual(self.game.utility(last_move_state, 'MAX'), -1)
        self.assertEqual(self.game.utility(last_move_state, 'MIN'), 1)

    # Testing to_move() uses parent Game implementation
    def test_to_move_method(self):
        self.assertEqual(self.game.to_move(self.initial_state), 'MAX')

if __name__ == '__main__':
    unittest.main()
