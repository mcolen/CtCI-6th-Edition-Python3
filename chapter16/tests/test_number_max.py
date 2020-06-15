"""Tests for chapter16.number_max."""

import unittest

from chapter16 import number_max


class TestNumberMax(unittest.TestCase):

    def test_26_and_negative_15(self) -> None:
        self.assertEqual(26, number_max.number_max(26, -15))

    def test_negative_15_and_2147483647(self) -> None:
        self.assertEqual(2147483647, number_max.number_max(-15, 2147483647))


if __name__ == '__main__':
    unittest.main()
