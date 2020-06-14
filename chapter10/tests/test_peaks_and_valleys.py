"""Tests for chapter10.peaks_and_valleys."""

import unittest

from chapter10 import peaks_and_valleys


class TestModuleName(unittest.TestCase):

    def test_5_3_1_2_3(self) -> None:
        nums = [5, 3, 1, 2, 3]
        peaks_and_valleys.sort(nums)
        self.assertCountEqual([5, 3, 1, 2, 3], nums)
        self.assertGreaterEqual(nums[0], nums[1])
        self.assertLessEqual(nums[1], nums[2])
        self.assertGreaterEqual(nums[2], nums[3])
        self.assertLessEqual(nums[3], nums[4])


if __name__ == '__main__':
    unittest.main()
