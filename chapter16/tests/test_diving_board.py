"""Tests for chapter16.diving_board."""

import unittest

from chapter16 import diving_board


class TestPossibleLengths(unittest.TestCase):

    def test_shorter_2_longer_3_k_12(self) -> None:
        self.assertEqual(
            {24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36},
            diving_board.possible_lengths(shorter=2, longer=3, k=12))


if __name__ == '__main__':
    unittest.main()
