"""Tests for chapter10.sorted_matrix_search."""

import unittest

from chapter10 import sorted_matrix_search


class TestIndex(unittest.TestCase):

    def test_find_23_in_5_by_5(self) -> None:
        matrix = [
            [1, 2, 3, 4, 5],
            [6, 7, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 17, 18, 19, 20],
            [21, 22, 23, 24, 25],
        ]

        res = sorted_matrix_search.index(matrix, target=23)

        self.assertEqual((4, 2), res)


if __name__ == '__main__':
    unittest.main()
