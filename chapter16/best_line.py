"""Solution to 16.14 Best Line.

Given a two-dimensional graph with points on it, find a line which
passes through the most number of points.
"""

import collections
from typing import Dict, Sequence

from chapter16 import geometry


def best_line(points: Sequence[geometry.Point]) -> geometry.Line:
    """Finds a line which passes through the most number of points.

    Args:
        Points: A sequence of points in two dimensions.

    Returns:
        A line passing through the maximum possible number of points.
    """
    line_counts: Dict[geometry.Line, int] = collections.defaultdict(int)
    for i, point1 in enumerate(points):
        for j in range(i + 1, len(points)):
            point2 = points[j]
            if point1 is point2:
                continue
            line = geometry.Segment(point1, point2).to_line()
            line_counts[line] += 1
    return max(line_counts, key=lambda line: line_counts[line])
