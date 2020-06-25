"""Tests for chapter08.eight_queens."""

import contextlib
import io
import unittest

from chapter08 import eight_queens


class TestPrintSolutions(unittest.TestCase):

    def test_4_queens(self) -> None:
        mock_stdout = io.StringIO()
        with contextlib.redirect_stdout(mock_stdout):
            eight_queens.print_solutions(n=4)

        solutions = mock_stdout.getvalue()[:-2].split('\n\n')
        self.assertCountEqual([
            '- Q - -\n'
            '- - - Q\n'
            'Q - - -\n'
            '- - Q -',

            '- - Q -\n'
            'Q - - -\n'
            '- - - Q\n'
            '- Q - -',
        ], solutions)

    def test_8_queens(self) -> None:
        mock_stdout = io.StringIO()
        with contextlib.redirect_stdout(mock_stdout):
            eight_queens.print_solutions(n=8)

        solutions = mock_stdout.getvalue()[:-1].split('\n\n')
        # https://en.wikipedia.org/wiki/Eight_queens_puzzle#Solutions
        self.assertEqual(92, len(solutions))


if __name__ == '__main__':
    unittest.main()
