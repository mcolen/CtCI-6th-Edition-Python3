"""Tests for chapter16.bisect_squares."""

import unittest

from chapter16 import bisect_squares
from chapter16 import geometry


class TestBisect(unittest.TestCase):

    def test_partially_overlapping_side_by_side(self) -> None:
        self.assertEqual(
            geometry.Segment(geometry.Point(8, 15), geometry.Point(20, 15)),
            bisect_squares.bisect(
                bisect_squares.Square(
                    center=geometry.Point(x=15, y=15), side=10),
                bisect_squares.Square(
                    center=geometry.Point(x=13, y=15), side=10)))


if __name__ == '__main__':
    unittest.main()
