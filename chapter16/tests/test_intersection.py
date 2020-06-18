"""Tests for chapter16.intersection."""

import unittest

from chapter16 import geometry, intersection


class TestIntersection(unittest.TestCase):

    def test_axes(self) -> None:
        x_axis = geometry.Segment(
            start=geometry.Point(x=-1, y=0), end=geometry.Point(x=1, y=0))
        y_axis = geometry.Segment(
            start=geometry.Point(x=0, y=1), end=geometry.Point(x=0, y=-1))
        self.assertEqual(geometry.Point(x=0, y=0),
                         intersection.intersection(x_axis, y_axis))

    def test_parallel(self) -> None:
        x_axis = geometry.Segment(
            start=geometry.Point(x=-1, y=0), end=geometry.Point(x=1, y=0))
        y_axis = geometry.Segment(
            start=geometry.Point(x=0, y=1), end=geometry.Point(x=0, y=-1))
        self.assertEqual(geometry.Point(x=0, y=0),
                         intersection.intersection(x_axis, y_axis))


if __name__ == '__main__':
    unittest.main()
