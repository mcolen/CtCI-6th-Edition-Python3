"""Solution to 8.13 Stack of Boxes.

You have a stack of `n` boxes, with widths `w_i`, heights `h_i`, and
depths `d_i`. The boxes cannot be rotated and can only be stacked on top
of one another if each box in the stack is strictly larger than the box
above it in width, height, and depth. Implement a method to compute the
height of the tallest possible stack. The height of a stack is the sum
of the heights of each box.
"""

import dataclasses
import operator
from typing import AbstractSet


@dataclasses.dataclass(frozen=True)
class Box:
    """A stackable box with dimensions."""
    width: int
    height: int
    depth: int


def max_height(boxes: AbstractSet[Box]) -> int:
    """Returns height of tallest possible stack from given boxes."""
    sorted_boxes = sorted(boxes, key=operator.attrgetter('height'))
    dp = [0] * (len(boxes) + 1)
    for i, base in enumerate(sorted_boxes):
        dp[i + 1] = max(base.height + dp[j] for j in range(i + 1)
                        if j == 0 or _can_stack(sorted_boxes[j - 1], base))
    return dp[-1]


def _can_stack(above: Box, below: Box) -> bool:
    return (above.width < below.width and
            above.height < below.height and
            above.depth < below.depth)
