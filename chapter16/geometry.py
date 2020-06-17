
"""Geometric entities for use in chapter 16 solutions."""

import dataclasses
import fractions
from typing import Any, Optional


@dataclasses.dataclass(frozen=True)
class Point:
    """A point in two dimensions."""
    x: float
    y: float


@dataclasses.dataclass(frozen=True)
class Line:
    """An infinite line defined by slope and y-intercept.

    Slope and y-intercept are stored as exact fractions to facilitate
    hashing.
    """
    slope: Optional[fractions.Fraction]
    y_intercept: Optional[fractions.Fraction]


@dataclasses.dataclass(frozen=True)
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

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, Segment):
            return False
        return {self.start, self.end} == {other.start, other.end}

    def to_line(self) -> Line:
        """Returns the line formed by extending this segment."""
        if self.slope is None:
            return Line(slope=None, y_intercept=None)
        assert self.y_intercept is not None
        return Line(fractions.Fraction(self.slope),
                    fractions.Fraction(self.y_intercept))
