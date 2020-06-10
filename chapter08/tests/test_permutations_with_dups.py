"""Tests for chapter08.permutations_with_dups."""

import unittest

from chapter08 import permutations_with_dups


class TestPermutationsWithDups(unittest.TestCase):

    def test_abb(self) -> None:
        self.assertEqual({'abb', 'bab', 'bba'},
                         permutations_with_dups.permutations('abb'))


if __name__ == '__main__':
    unittest.main()
