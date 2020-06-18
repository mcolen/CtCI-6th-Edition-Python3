"""Tests for chapter05.conversion."""

import unittest

from chapter05 import conversion


class TestNumBitsDifferent(unittest.TestCase):

    def test_0b0001010010001111000_0b1111101000010000100(self) -> None:
        A = 0b0001010010001111000
        B = 0b1111101000010000100

        self.assertEqual(13, conversion.num_bits_different(A, B))


if __name__ == '__main__':
    unittest.main()
