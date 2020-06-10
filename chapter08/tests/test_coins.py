"""Tests for chapter08.coins."""

import unittest

from chapter08 import coins


class TestCoins(unittest.TestCase):

    def test_29(self) -> None:
        self.assertEqual(13, coins.coin_combinations(n=29))


if __name__ == '__main__':
    unittest.main()
