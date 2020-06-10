"""Solution to 8.2 Robot in a Grid.

Imagine a robot sitting on the upper left corner of grid with `r` rows
and `c` columns. The robot can only move in two directions, right and
down, but certain cells are "off limits" such that the robot cannot step
on them. Design an algorithm to find a path for the robot from the top
left to the bottom right.
"""

import dataclasses
import enum
from typing import List, Optional, Set, Sequence


class Direction(enum.Enum):
    """A cardinal direction that the robot can travel."""
    DOWN = 1
    RIGHT = 2


@dataclasses.dataclass(frozen=True)
class _Point:
    """A point in a grid."""
    row: int
    column: int


def find_path(grid: Sequence[Sequence[bool]]) -> Optional[List[Direction]]:
    """Finds a path for robot from top left to bottom right of grid.

    Args:
        grid: A non-empty 2-d array of bools. A value of False indicates
            cells in the grid that are "off limits" to the robot.

    Returns:
        Sequence of DOWN/RIGHT that will take the robot from top left to
            bottom right without traversing "off limits" cells, or None
            if no such sequence exists.
    """
    path: List[Direction] = []
    visited: Set[_Point] = set()

    def helper(r: int, c: int) -> bool:
        # Tries to get to (0, 0) from (r, c).
        if not grid[r][c] or _Point(r, c) in visited:
            return False
        if r == 0 and c == 0:
            return True
        if r > 0 and helper(r - 1, c):
            path.append(Direction.DOWN)
            return True
        if helper(r, c - 1):
            path.append(Direction.RIGHT)
            return True
        visited.add(_Point(r, c))
        return False

    return path if helper(len(grid) - 1, len(grid[-1]) - 1) else None
