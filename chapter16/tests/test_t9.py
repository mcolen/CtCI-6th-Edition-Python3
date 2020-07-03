"""Tests for chapter16.t9."""

import unittest

from chapter16 import t9


class TestMatchingWords(unittest.TestCase):

    def test_8733(self) -> None:
        self.assertEqual({'tree', 'used'}, t9.matching_words(
            digits=['8', '7', '3', '3'],
            dictionary={'the', 'of', 'and', 'a', 'that', 'used', 'tree'}))


if __name__ == '__main__':
    unittest.main()
