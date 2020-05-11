"""Tests for chapter1.rotate_matrix."""

import unittest

from chapter1.rotate_matrix import rotate_matrix


class TestRotateMatrix(unittest.TestCase):
    """Simple tests of matrix rotation."""

    def test_five_by_five_matrix(self):
        matrix = [
            [1, 2, 3, 4, 5],
            [6, 7, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 17, 18, 19, 20],
            [21, 22, 23, 24, 25],
        ]
        rotated = [
            [21, 16, 11, 6, 1],
            [22, 17, 12, 7, 2],
            [23, 18, 13, 8, 3],
            [24, 19, 14, 9, 4],
            [25, 20, 15, 10, 5],
        ]
        rotate_matrix(matrix)
        self.assertEqual(rotated, matrix)


if __name__ == '__main__':
    unittest.main()
