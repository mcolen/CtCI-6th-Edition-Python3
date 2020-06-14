"""Solution to 16.3 Intersection.

Given two straight line segments (represented as a start point and an
end point), compute the point of intersection, if any.
"""

import dataclasses
from typing import Optional, Tuple


@dataclasses.dataclass
class Point:
    """A point in two dimensions."""
    x: float
    y: float


@dataclasses.dataclass
class Segment:
    "A line segment represented by two distinct points."
    start: Point
    end: Point

    @property
    def slope(self) -> Optional[float]:
        """The slope of this line segment."""
        if self.start.x == self.end.x:
            return None
        return (self.end.y - self.start.y) / (self.end.x - self.start.x)

    @property
    def y_intercept(self) -> Optional[float]:
        """The y-intercept of this line segment."""
        if self.slope is None:
            return None
        return self.start.y - self.slope * self.start.x


def intersection(segment1: Segment, segment2: Segment) -> Optional[Point]:
    """Computes point of intersection between segment1 and segment2.

    Returns:
        A point of intersection of segment1 and segment2, or None if the
        line segments do not intersect.
    """
    m1, m2 = segment1.slope, segment2.slope
    b1, b2 = segment1.y_intercept, segment2.y_intercept
    if m1 == m2:
        return _parallel_helper(segment1, segment2)
    if m1 is None:
        assert m2 is not None and b2 is not None
        x = segment1.start.x
        y = m2 * x + b2
    elif m2 is None:
        assert m1 is not None and b1 is not None
        x = segment2.start.x
        y = m1 * x + b1
    else:
        assert m1 is not None and m2 is not None
        assert b1 is not None and b2 is not None
        x = (b2 - b1) / (m1 - m2)
        y = m1 * x + b1
    point = Point(x, y)
    if (_point_is_between(point, (segment1.start, segment1.end)) and
            _point_is_between(point, (segment2.start, segment2.end))):
        return point
    return None


def _parallel_helper(segment1: Segment, segment2: Segment) -> Optional[Point]:
    if segment1.y_intercept != segment2.y_intercept:
        return None
    bounds = (segment1.start, segment1.end)
    if _point_is_between(segment2.start, bounds):
        return segment2.start
    if _point_is_between(segment2.end, bounds):
        return segment2.end
    return None


def _point_is_between(point: Point, bounds: Tuple[Point, Point]) -> bool:
    return (_val_is_between(point.x, (bounds[0].x, bounds[1].x)) and
            _val_is_between(point.y, (bounds[0].y, bounds[1].y)))


def _val_is_between(val: float, bounds: Tuple[float, float]) -> bool:
    min_bound, max_bound = min(bounds), max(bounds)
    return min_bound <= val <= max_bound
