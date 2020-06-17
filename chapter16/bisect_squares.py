"""Solution to 16.13 Bisect Squares.

Given two squares on a two-dimensional plane, find a line that would cut
these two squares in half. Assume that the top and the bottom sides of
the square run parallel to the x-axis.
"""

import dataclasses
from typing import Optional

from chapter16 import geometry


@dataclasses.dataclass
class Square:
    """A square with top and bottom sides parallel to the x-axis."""
    center: geometry.Point
    side: float


def bisect(square1: Square, square2: Square) -> geometry.Segment:
    """Finds a minimal line segment that bisects two squares.

    Args:
        square1: A square with top and bottom sides running parallel to
            the x-axis.
        square2: A square with top and bottom sides running parallel to
            the x-axis.

    Returns:
        A line segment that starts and ends on edges of the squares and
        bisects both squares.
    """
    if square1.center == square2.center:
        x = square1.center.x
        max_side = max(square1.side, square2.side)
        top = geometry.Point(x, square1.center.y + max_side / 2)
        bottom = geometry.Point(x, square1.center.y + max_side / 2)
        return geometry.Segment(bottom, top)

    slope = geometry.Segment(square1.center, square2.center).slope
    edges1 = _draw_line_through_center_to_edges(square1, slope)
    edges2 = _draw_line_through_center_to_edges(square2, slope)
    points = [edges1.start, edges1.end, edges2.start, edges2.end]
    start = min(points, key=lambda point: (point.x, point.y))
    end = max(points, key=lambda point: (point.x, point.y))
    return geometry.Segment(start, end)


def _draw_line_through_center_to_edges(
        square: Square, slope: Optional[float]) -> geometry.Segment:
    """Extends a line with given slope through square center to edges.

    Args:
        square: The square through which line is extended.
        slope: The slope of the line to be extended.

    Returns:
        The minimal line segment through center of given square with
        given slope that intersects the square twice.
    """
    if slope is None:
        x1 = x2 = square.center.x
        y1 = square.center.y + square.side / 2
        y2 = square.center.y - square.side / 2
    elif abs(slope) <= 1:
        x1 = square.center.x + square.side / 2
        x2 = square.center.x - square.side / 2
        y1 = square.center.y + slope * (x1 - square.center.x)
        y2 = square.center.y + slope * (x2 - square.center.x)
    else:
        y1 = square.center.y + square.side / 2
        y2 = square.center.y - square.side / 2
        x1 = square.center.x + (y1 - square.center.y) / slope
        x2 = square.center.x + (y2 - square.center.y) / slope
    return geometry.Segment(geometry.Point(x1, y1), geometry.Point(x2, y2))
