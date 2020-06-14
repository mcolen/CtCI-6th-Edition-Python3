"""Tests for chapter10.peaks_and_valleys."""

import unittest

from chapter10 import peaks_and_valleys


class TestModuleName(unittest.TestCase):

    def test_5_3_1_2_3(self) -> None:
        ints = [5, 3, 1, 2, 3]
        peaks_and_valleys.sort(ints)
        self.assertCountEqual([5, 3, 1, 2, 3], ints)
        self.assertGreaterEqual(ints[0], ints[1])
        self.assertLessEqual(ints[1], ints[2])
        self.assertGreaterEqual(ints[2], ints[3])
        self.assertLessEqual(ints[3], ints[4])


if __name__ == '__main__':
    unittest.main()
