"""Tests for chapter10.sorted_search_no_size."""

import unittest

from chapter10 import sorted_search_no_size


class TestIndex(unittest.TestCase):

    def test_find_1_in_1_2_4_5_6_7_9_10_11_12_13_14_16_18(self) -> None:
        listy = sorted_search_no_size.Listy(
            [1, 2, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 16, 18])
        self.assertEqual(0, sorted_search_no_size.index(listy, target=1))

    def test_find_2_in_1_2_4_5_6_7_9_10_11_12_13_14_16_18(self) -> None:
        listy = sorted_search_no_size.Listy(
            [1, 2, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 16, 18])
        self.assertEqual(1, sorted_search_no_size.index(listy, target=2))

    def test_find_4_in_1_2_4_5_6_7_9_10_11_12_13_14_16_18(self) -> None:
        listy = sorted_search_no_size.Listy(
            [1, 2, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 16, 18])
        self.assertEqual(2, sorted_search_no_size.index(listy, target=4))

    def test_find_5_in_1_2_4_5_6_7_9_10_11_12_13_14_16_18(self) -> None:
        listy = sorted_search_no_size.Listy(
            [1, 2, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 16, 18])
        self.assertEqual(3, sorted_search_no_size.index(listy, target=5))

    def test_find_6_in_1_2_4_5_6_7_9_10_11_12_13_14_16_18(self) -> None:
        listy = sorted_search_no_size.Listy(
            [1, 2, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 16, 18])
        self.assertEqual(4, sorted_search_no_size.index(listy, target=6))

    def test_find_7_in_1_2_4_5_6_7_9_10_11_12_13_14_16_18(self) -> None:
        listy = sorted_search_no_size.Listy(
            [1, 2, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 16, 18])
        self.assertEqual(5, sorted_search_no_size.index(listy, target=7))

    def test_find_9_in_1_2_4_5_6_7_9_10_11_12_13_14_16_18(self) -> None:
        listy = sorted_search_no_size.Listy(
            [1, 2, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 16, 18])
        self.assertEqual(6, sorted_search_no_size.index(listy, target=9))

    def test_find_10_in_1_2_4_5_6_7_9_10_11_12_13_14_16_18(self) -> None:
        listy = sorted_search_no_size.Listy(
            [1, 2, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 16, 18])
        self.assertEqual(7, sorted_search_no_size.index(listy, target=10))

    def test_find_11_in_1_2_4_5_6_7_9_10_11_12_13_14_16_18(self) -> None:
        listy = sorted_search_no_size.Listy(
            [1, 2, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 16, 18])
        self.assertEqual(8, sorted_search_no_size.index(listy, target=11))

    def test_find_12_in_1_2_4_5_6_7_9_10_11_12_13_14_16_18(self) -> None:
        listy = sorted_search_no_size.Listy(
            [1, 2, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 16, 18])
        self.assertEqual(9, sorted_search_no_size.index(listy, target=12))

    def test_find_13_in_1_2_4_5_6_7_9_10_11_12_13_14_16_18(self) -> None:
        listy = sorted_search_no_size.Listy(
            [1, 2, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 16, 18])
        self.assertEqual(10, sorted_search_no_size.index(listy, target=13))

    def test_find_14_in_1_2_4_5_6_7_9_10_11_12_13_14_16_18(self) -> None:
        listy = sorted_search_no_size.Listy(
            [1, 2, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 16, 18])
        self.assertEqual(11, sorted_search_no_size.index(listy, target=14))

    def test_find_16_in_1_2_4_5_6_7_9_10_11_12_13_14_16_18(self) -> None:
        listy = sorted_search_no_size.Listy(
            [1, 2, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 16, 18])
        self.assertEqual(12, sorted_search_no_size.index(listy, target=16))

    def test_find_18_in_1_2_4_5_6_7_9_10_11_12_13_14_16_18(self) -> None:
        listy = sorted_search_no_size.Listy(
            [1, 2, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 16, 18])
        self.assertEqual(13, sorted_search_no_size.index(listy, target=18))

    def test_find_15_in_1_2_4_5_6_7_9_10_11_12_13_14_16_18(self) -> None:
        listy = sorted_search_no_size.Listy(
            [1, 2, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 16, 18])
        self.assertIsNone(sorted_search_no_size.index(listy, target=15))


if __name__ == '__main__':
    unittest.main()
