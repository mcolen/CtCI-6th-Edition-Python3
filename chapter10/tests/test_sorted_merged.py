"""Tests for chapter10.sorted_merge."""

import unittest

from chapter10 import sorted_merge


class TestMerge(unittest.TestCase):

    def test_2_3_4_5_6_8_10_100_and_1_4_5_6_7_7(self) -> None:
        A = [2, 3, 4, 5, 6, 7, 10, 100, 0, 0, 0, 0, 0, 0]
        B = [1, 4, 5, 6, 7, 7]

        sorted_merge.merge(A, B)

        self.assertEqual([1, 2, 3, 4, 4, 5, 5, 6, 6, 7, 7, 7, 10, 100], A)


if __name__ == '__main__':
    unittest.main()
