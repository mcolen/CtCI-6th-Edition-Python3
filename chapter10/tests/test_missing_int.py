"""Tests for chapter10.missing_int."""

import io
import unittest

from chapter10 import missing_int


class TestMissing(unittest.TestCase):

    def test_0_0_1_2_3_4_5_8_9_6_6_from_0_to_9(self) -> None:
        self.assertEqual(7, missing_int.missing(
            io.StringIO('0\n0\n1\n2\n3\n4\n5\n8\n9\n6\n6\n'), lo=0, hi=9))


class TestMissingUniqueNonNegativeSigned32Bit(unittest.TestCase):

    def test_0_1_2_3_4_5_8_9_6(self) -> None:
        res = missing_int.missing_unique_nonnegative_signed_32_bit(
            io.StringIO('0\n1\n2\n3\n4\n5\n8\n9\n6\n'))
        self.assertNotIn(res, {0, 1, 2, 3, 4, 5, 8, 9, 6}, res)
        self.assertGreaterEqual(res, 0)
        self.assertLessEqual(res, missing_int.MAX_SIGNED_32_BIT_INT)


if __name__ == '__main__':
    unittest.main()
