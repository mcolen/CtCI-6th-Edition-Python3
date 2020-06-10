"""Tests for chapter10.search_in_rotated_array."""

import unittest

from chapter10 import search_in_rotated_array


class TestSearchInRotatedArray(unittest.TestCase):

    def test_find_5_in_15_16_19_20_25_1_3_4_5_7_10_14(self) -> None:
        self.assertEqual(8, search_in_rotated_array.index(
            [15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14], target=5))

    def test_find_2_in_2_3_1_2_2_2_2_2_2_2(self) -> None:
        self.assertIn(
            search_in_rotated_array.index(
                [2, 3, 1, 2, 2, 2, 2, 2, 2, 2], target=2),
            {0, 3, 4, 5, 6, 7, 8, 9})

    def test_find_3_in_2_3_1_2_2_2_2_2_2_2(self) -> None:
        self.assertEqual(1, search_in_rotated_array.index(
            [2, 3, 1, 2, 2, 2, 2, 2, 2, 2], target=3))

    def test_find_4_in_2_3_1_2_2_2_2_2_2_2(self) -> None:
        self.assertIsNone(search_in_rotated_array.index(
            [2, 3, 1, 2, 2, 2, 2, 2, 2, 2], target=4))

    def test_find_1_in_2_3_1_2_2_2_2_2_2_2(self) -> None:
        self.assertEqual(2, search_in_rotated_array.index(
            [2, 3, 1, 2, 2, 2, 2, 2, 2, 2], target=1))

    def test_find_8_in_2_3_1_2_2_2_2_2_2_2(self) -> None:
        self.assertIsNone(search_in_rotated_array.index(
            [2, 3, 1, 2, 2, 2, 2, 2, 2, 2], target=8))


if __name__ == '__main__':
    unittest.main()
