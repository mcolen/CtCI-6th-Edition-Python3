"""Tests for chapter08.parens."""

import io
import unittest
import unittest.mock

from chapter08 import parens


class TestPrintValidCombinations(unittest.TestCase):

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_3(self, mock_stdout: io.StringIO) -> None:
        parens.print_valid_combinations(n=3)
        self.assertCountEqual(
            ['((()))', '(()())', '(())()', '()(())', '()()()'],
            mock_stdout.getvalue()[:-1].split(', '))


if __name__ == '__main__':
    unittest.main()
