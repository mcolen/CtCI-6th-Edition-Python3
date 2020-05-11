"""Tests for chapter1.check_permutation."""

import unittest

from chapter1.check_permutation import are_permutations


class TestCheckPermutation(unittest.TestCase):

    def test_apple_papel_are_permutations(self):
        self.assertTrue(are_permutations('apple', 'papel'))

    def test_carrot_tarroc_are_permutations(self):
        self.assertTrue(are_permutations('carrot', 'tarroc'))

    def test_hello_llloh_are_not_permutations(self):
        self.assertFalse(are_permutations('hello', 'llloh'))


if __name__ == '__main__':
    unittest.main()
