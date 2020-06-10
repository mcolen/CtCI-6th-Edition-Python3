"""Solution to 8.10 Paint Fill.

Implement the "paint fill" function that one might see on many image
editing programs. That is, given a screen (represented by a
two-dimensional array of colors), a point, and a new color, fill in the
surrounding area until the color changes from the original color.
"""

from typing import Any, MutableSequence, Sequence


def paint_fill(screen: Sequence[MutableSequence[Any]], r: int, c: int,
               color: Any) -> None:
    """Fills in an area on screen with a new color.

    Recursively fills starting point and all adjacent
    (up/down/right/left) locations on screen that were the same color as
    the starting location.

    Args:
        screen: A two-dimensional array of colors.
        r: 0-indexed row to start fill.
        c: 0-indexed column to start fill.
        color: New color with which to fill.
    """
    original_color = screen[r][c]

    def helper(r: int, c: int) -> None:
        if not 0 <= r < len(screen) or not 0 <= c < len(screen[r]):
            return
        if screen[r][c] == original_color:
            screen[r][c] = color
            helper(r - 1, c)
            helper(r + 1, c)
            helper(r, c - 1)
            helper(r, c + 1)

    if color != original_color:
        helper(r, c)
