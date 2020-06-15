"""Tests for chapter16.tic_tac_win."""

import unittest

from chapter16 import tic_tac_win

RED = tic_tac_win.Piece.RED
BLUE = tic_tac_win.Piece.BLUE


class TestHasWinner(unittest.TestCase):

    def test_empty_board(self) -> None:
        self.assertFalse(tic_tac_win.has_winner([
            [None, None, None],
            [None, None, None],
            [None, None, None],
        ]))

    def test_rbr_bbr_rbb(self) -> None:
        self.assertTrue(tic_tac_win.has_winner([
            [RED, BLUE, RED],
            [BLUE, BLUE, RED],
            [RED, BLUE, BLUE],
        ]))


if __name__ == '__main__':
    unittest.main()
