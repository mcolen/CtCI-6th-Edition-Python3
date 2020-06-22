"""Tests for chapter16.pattern_matching."""

import unittest

from chapter16 import pattern_matching


class TestMatches(unittest.TestCase):

    def test_ababb_backbatbackbatbat(self) -> None:
        self.assertTrue(pattern_matching.matches('ababb', 'backbatbackbatbat'))

    def test_ababaa_batgobatgobatbat(self) -> None:
        self.assertTrue(pattern_matching.matches('ababaa', 'batgobatgobatbat'))

    def test_bb_backback(self) -> None:
        self.assertTrue(pattern_matching.matches('bb', 'backback'))

    def test_ababb_backbatbackbatbackbat(self) -> None:
        self.assertTrue(
            pattern_matching.matches('ababb', 'backbatbackbatbackbat'))

    def test_abab_backsbatbackbats(self) -> None:
        self.assertFalse(pattern_matching.matches('abab', 'backsbatbackbats'))

    def test_aba_backsbatbacksbat(self) -> None:
        self.assertTrue(pattern_matching.matches('aba', 'backsbatbacksbat'))


if __name__ == '__main__':
    unittest.main()
