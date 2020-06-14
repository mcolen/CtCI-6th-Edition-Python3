"""Tests for chapter16.intersection."""

import unittest

from chapter16 import intersection


class TestIntersection(unittest.TestCase):

    def test_axes(self) -> None:
        x_axis = intersection.Segment(start=intersection.Point(
            x=-1, y=0), end=intersection.Point(x=1, y=0))
        y_axis = intersection.Segment(start=intersection.Point(
            x=0, y=1), end=intersection.Point(x=0, y=-1))
        self.assertEqual(intersection.Point(x=0, y=0),
                         intersection.intersection(x_axis, y_axis))

    def test_parallel(self) -> None:
        x_axis = intersection.Segment(start=intersection.Point(
            x=-1, y=0), end=intersection.Point(x=1, y=0))
        y_axis = intersection.Segment(start=intersection.Point(
            x=0, y=1), end=intersection.Point(x=0, y=-1))
        self.assertEqual(intersection.Point(x=0, y=0),
                         intersection.intersection(x_axis, y_axis))


if __name__ == '__main__':
    unittest.main()
