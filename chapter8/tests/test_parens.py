"""Tests for chapter8.parens."""

import io
import unittest
import unittest.mock

from chapter8 import parens


class TestParens(unittest.TestCase):

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_3(self, mock_stdout: io.StringIO) -> None:
        parens.print_valid_combinations(n=3)
        self.assertCountEqual(
            ['((()))', '(()())', '(())()', '()(())', '()()()'],
            set(mock_stdout.getvalue()[:-1].split(', ')))


if __name__ == '__main__':
    unittest.main()
