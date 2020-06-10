"""Tests for chapter05.flip_bit_to_win."""

import unittest

from chapter05 import flip_bit_to_win


class TestFlipBitToWin(unittest.TestCase):

    def test_0b11011101111(self) -> None:
        self.assertEqual(8, flip_bit_to_win.max_length(0b11011101111))


if __name__ == "__main__":
    unittest.main()
