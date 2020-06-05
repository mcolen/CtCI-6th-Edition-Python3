"""Tests for chapter8.paint_fill."""

import unittest

from chapter8 import paint_fill


class TestPaintFill(unittest.TestCase):

    def test_ten_by_ten(self) -> None:
        screen = [
            ['G', 'G', 'G', 'G', 'B', 'G', 'B', 'G', 'G', 'G'],
            ['B', 'B', 'G', 'G', 'B', 'G', 'G', 'G', 'G', 'G'],
            ['B', 'B', 'G', 'G', 'G', 'G', 'G', 'B', 'G', 'G'],
            ['G', 'B', 'G', 'G', 'B', 'B', 'B', 'G', 'G', 'G'],
            ['G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'B'],
            ['G', 'B', 'B', 'B', 'B', 'G', 'G', 'G', 'G', 'G'],
            ['G', 'G', 'G', 'G', 'B', 'B', 'G', 'G', 'B', 'G'],
            ['G', 'B', 'B', 'B', 'B', 'G', 'B', 'B', 'G', 'B'],
            ['G', 'G', 'B', 'B', 'G', 'B', 'G', 'B', 'G', 'B'],
            ['G', 'B', 'B', 'G', 'G', 'G', 'G', 'B', 'B', 'G'],
        ]
        filled_w_at_2_2 = [
            ['W', 'W', 'W', 'W', 'B', 'W', 'B', 'W', 'W', 'W'],
            ['B', 'B', 'W', 'W', 'B', 'W', 'W', 'W', 'W', 'W'],
            ['B', 'B', 'W', 'W', 'W', 'W', 'W', 'B', 'W', 'W'],
            ['W', 'B', 'W', 'W', 'B', 'B', 'B', 'W', 'W', 'W'],
            ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'B'],
            ['W', 'B', 'B', 'B', 'B', 'W', 'W', 'W', 'W', 'W'],
            ['W', 'W', 'W', 'W', 'B', 'B', 'W', 'W', 'B', 'W'],
            ['W', 'B', 'B', 'B', 'B', 'G', 'B', 'B', 'G', 'B'],
            ['W', 'W', 'B', 'B', 'G', 'B', 'G', 'B', 'G', 'B'],
            ['W', 'B', 'B', 'G', 'G', 'G', 'G', 'B', 'B', 'G'],
        ]
        paint_fill.paint_fill(screen, r=2, c=2, color='W')
        self.assertEqual(filled_w_at_2_2, screen)


if __name__ == '__main__':
    unittest.main()
