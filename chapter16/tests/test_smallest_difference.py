"""Tests for chapter16.smallest_difference."""

import unittest

from chapter16 import smallest_difference


class TestSmallestDifference(unittest.TestCase):

    def test_1_3_15_11_2_and_23_127_235_19_8(self) -> None:
        self.assertEqual(3, smallest_difference.smallest_difference(
            [1, 3, 15, 11, 2], [23, 127, 235, 19, 8]))


if __name__ == '__main__':
    unittest.main()
