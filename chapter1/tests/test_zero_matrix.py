"""Tests for chapter1.zero_matrix."""

import unittest

from chapter1.zero_matrix import zero_matrix


class TestZeroMatrix(unittest.TestCase):

    def test_some_zeros(self):
        matrix = [
            [1, 2, 3, 4, 0],
            [6, 0, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 0, 18, 19, 20],
            [21, 22, 23, 24, 25],
        ]
        zerod = [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [11, 0, 13, 14, 0],
            [0, 0, 0, 0, 0],
            [21, 0, 23, 24, 0],
        ]
        zero_matrix(matrix)
        self.assertEqual(zerod, matrix)


if __name__ == '__main__':
    unittest.main()
