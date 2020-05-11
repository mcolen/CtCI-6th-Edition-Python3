"""Tests for chapter1.check_permutation."""

import unittest

from chapter1.check_permutation import are_permutations


class TestCheckPermutation(unittest.TestCase):

    def test_apple_papel(self):
        self.assertTrue(are_permutations('apple', 'papel'))

    def test_carrot_tarroc(self):
        self.assertTrue(are_permutations('carrot', 'tarroc'))

    def test_hello_llloh(self):
        self.assertFalse(are_permutations('hello', 'llloh'))


if __name__ == '__main__':
    unittest.main()
