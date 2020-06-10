"""Tests for chapter08.towers_of_hanoi."""

import unittest

from chapter08 import towers_of_hanoi


class TestTowersOfHanoi(unittest.TestCase):

    def test_5_disks(self) -> None:
        towers = towers_of_hanoi.TowersOfHanoi(N=5)
        towers_of_hanoi.solve(towers, N=5)
        self.assertTrue(towers.is_solved())


if __name__ == '__main__':
    unittest.main()
