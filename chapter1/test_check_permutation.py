"""Tests for solution to 1.2 Check Permutation."""

import unittest

from chapter1.check_permutation import are_permutations


class TestCheckPermutation(unittest.TestCase):
    """Simple tests of string permutability."""

    def test_apple_papel_are_permutations(self):
        self.assertTrue(are_permutations('apple', 'papel'))

    def test_carrot_tarroc_are_permutations(self):
        self.assertTrue(are_permutations('carrot', 'tarroc'))

    def test_hello_llloh_are_not_permutations(self):
        self.assertFalse(are_permutations('hello', 'llloh'))


if __name__ == '__main__':
    unittest.main()
