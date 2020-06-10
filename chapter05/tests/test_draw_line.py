"""Tests for chapter05.draw_line."""

import unittest

from chapter05 import draw_line


class TestDrawLine(unittest.TestCase):

    def test_0b01111100(self) -> None:
        screen = bytearray(1)
        draw_line.draw_line(screen, width=24, x1=1, x2=5, y=0)
        self.assertEqual(bytearray([0b01111100]), screen)


if __name__ == '__main__':
    unittest.main()
