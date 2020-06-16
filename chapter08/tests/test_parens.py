"""Tests for chapter08.parens."""

import unittest

from chapter08 import parens


class TestPrintValidCombinations(unittest.TestCase):

    def test_3(self) -> None:
        self.assertEqual({'((()))', '(()())', '(())()', '()(())', '()()()'},
                         parens.valid_combinations(n=3))


if __name__ == '__main__':
    unittest.main()
