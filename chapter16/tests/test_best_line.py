"""Tests for chapter16.best_line."""

import fractions
import unittest

from chapter16 import best_line, geometry


class TestBestLine(unittest.TestCase):

    def test_three_of_four_collinear(self) -> None:
        self.assertEqual(
            geometry.Line(
                slope=fractions.Fraction(1),
                y_intercept=fractions.Fraction(3)
            ),
            best_line.best_line(points=[
                geometry.Point(-1, 2),
                geometry.Point(0, 3),
                geometry.Point(0, 0),
                geometry.Point(1, 4),
            ]))


if __name__ == '__main__':
    unittest.main()
