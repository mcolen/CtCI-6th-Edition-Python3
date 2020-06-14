"""Tests for chapter16.number_swapper."""

import unittest

from chapter16 import number_swapper


class TestNumberSwapper(unittest.TestCase):

    def test_1672_9332(self) -> None:
        num1, num2 = number_swapper.Int(1672), number_swapper.Int(9332)
        number_swapper.swap(num1, num2)
        self.assertEqual(9332, num1.val)
        self.assertEqual(1672, num2.val)


if __name__ == '__main__':
    unittest.main()
