"""Tests for chapter16.sub_sort."""

import unittest

from chapter16 import sub_sort


class TestIndices(unittest.TestCase):

    def test_1_2_4_7_10_11_8_12_5_6_16_18_19(self) -> None:
        self.assertEqual(
            (3, 9),
            sub_sort.indices([1, 2, 4, 7, 10, 11, 8, 12, 5, 6, 16, 18, 19]))


if __name__ == '__main__':
    unittest.main()
