"""Tests for chapter01.zero_matrix."""

import unittest

from chapter01 import zero_matrix


class TestZeroMatrix(unittest.TestCase):

    def test_some_zeros(self) -> None:
        matrix = [
            [1, 2, 3, 4, 0],
            [6, 0, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 0, 18, 19, 20],
            [21, 22, 23, 24, 25],
        ]
        zeroed = [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [11, 0, 13, 14, 0],
            [0, 0, 0, 0, 0],
            [21, 0, 23, 24, 0],
        ]
        zero_matrix.zero_matrix(matrix)
        self.assertEqual(zeroed, matrix)


if __name__ == '__main__':
    unittest.main()
