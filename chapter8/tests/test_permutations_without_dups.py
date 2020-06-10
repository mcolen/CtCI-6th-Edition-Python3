"""Tests for chapter8.permutations_without_dups."""

import unittest

from chapter8 import permutations_without_dups


class TestPermutationsWithoutDups(unittest.TestCase):

    def test_abc(self) -> None:
        self.assertEqual({'abc', 'acb', 'bac', 'bca', 'cab', 'cba'},
                         permutations_without_dups.permutations('abc'))


if __name__ == '__main__':
    unittest.main()