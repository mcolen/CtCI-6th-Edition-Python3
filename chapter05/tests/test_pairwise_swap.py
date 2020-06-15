"""Tests for chapter05.pairwise_swap."""

import unittest

from chapter05 import pairwise_swap


class TestSwapBits(unittest.TestCase):

    def test_0b111001001101010001(self) -> None:
        n = 0b111001001101010001
        m = 0b110110001110100010
        self.assertEqual(m, pairwise_swap.swap_bits(n))


if __name__ == '__main__':
    unittest.main()
