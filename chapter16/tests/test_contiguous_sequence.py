"""Tests for chapter16.contiguous_sequence."""

import unittest

from chapter16 import contiguous_sequence


class TestMaxSum(unittest.TestCase):

    def test_2_n8_3_n2_4_n10(self) -> None:
        self.assertEqual(5,
                         contiguous_sequence.max_sum([2, -8, 3, -2, 4, -10]))


if __name__ == '__main__':
    unittest.main()
