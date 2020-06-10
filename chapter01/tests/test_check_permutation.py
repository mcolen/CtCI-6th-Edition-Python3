"""Tests for chapter 01.check_permutation."""

import unittest

from chapter01 import check_permutation


class TestCheckPermutation(unittest.TestCase):

    def test_apple_papel(self) -> None:
        self.assertTrue(check_permutation.are_permutations('apple', 'papel'))

    def test_carrot_tarroc(self) -> None:
        self.assertTrue(check_permutation.are_permutations('carrot', 'tarroc'))

    def test_hello_llloh(self) -> None:
        self.assertFalse(check_permutation.are_permutations('hello', 'llloh'))


if __name__ == '__main__':
    unittest.main()
