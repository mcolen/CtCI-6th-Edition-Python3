"""Tests for chapter1.palindrome_permutation."""

import unittest

from chapter1 import palindrome_permutation


class TestPalindromePermutation(unittest.TestCase):

    def test_rats_live_on_no_evil_star(self) -> None:
        self.assertTrue(
            palindrome_permutation.is_palindrome_permutation(
                'Rats live on no evil star'))

    def test_a_man_a_plan_a_canal_panama(self) -> None:
        self.assertTrue(
            palindrome_permutation.is_palindrome_permutation(
                'A man, a plan, a canal, panama'))

    def test_lleve(self) -> None:
        self.assertTrue(
            palindrome_permutation.is_palindrome_permutation('Lleve'))

    def test_tacotac(self) -> None:
        self.assertTrue(
            palindrome_permutation.is_palindrome_permutation('Tacotac'))

    def test_asda(self) -> None:
        self.assertFalse(
            palindrome_permutation.is_palindrome_permutation('asda'))


if __name__ == '__main__':
    unittest.main()
