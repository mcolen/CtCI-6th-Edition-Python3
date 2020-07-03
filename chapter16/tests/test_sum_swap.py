"""Tests for chapter16.sum_swap."""

import unittest

from chapter16 import sum_swap


class TestPair(unittest.TestCase):

    def test_4_1_2_1_1_2_and_3_6_3_3(self) -> None:
        self.assertIn(sum_swap.pair([4, 1, 2, 1, 1, 2], [3, 6, 3, 3]),
                      {(1, 3), (4, 6)})


if __name__ == '__main__':
    unittest.main()
