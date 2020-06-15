"""Tests for chapter05.insertion."""

import unittest

from chapter05 import insertion


class TestInsertBits(unittest.TestCase):

    def test_bits_29_through_31(self) -> None:
        N = 0b11111111111111111010010010000000  # 32 bits
        M = 0b101
        self.assertEqual(0b10111111111111111010010010000000,
                         insertion.insert_bits(N, M, i=29, j=31))


if __name__ == '__main__':
    unittest.main()
