"""Tests for chapter8.power_set."""

from typing import FrozenSet, Set
import unittest

from chapter8 import power_set


class TestPowerSet(unittest.TestCase):

    def test_three_elements(self) -> None:
        set_ = {1, 2, 3}
        subsets: Set[FrozenSet[int]] = set()
        subsets.add(frozenset())
        subsets.add(frozenset({1}))
        subsets.add(frozenset({2}))
        subsets.add(frozenset({3}))
        subsets.add(frozenset({1, 2}))
        subsets.add(frozenset({1, 3}))
        subsets.add(frozenset({2, 3}))
        subsets.add(frozenset({1, 2, 3}))
        self.assertEqual(subsets, power_set.power_set(set_))


if __name__ == '__main__':
    unittest.main()
