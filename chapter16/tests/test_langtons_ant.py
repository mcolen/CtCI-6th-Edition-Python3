"""Tests for chapter16.langtons_ant."""

import contextlib
import io
import unittest

from chapter16 import langtons_ant


class TestPrintKMoves(unittest.TestCase):

    def test_6_moves(self) -> None:
        mock_stdout = io.StringIO()
        with contextlib.redirect_stdout(mock_stdout):
            langtons_ant.print_k_moves(k=6)

        self.assertEqual(
            '0 1 0\n'
            '1 0 0\n'
            '1 1 0\n',
            mock_stdout.getvalue())


if __name__ == '__main__':
    unittest.main()
