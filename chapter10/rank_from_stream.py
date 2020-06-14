"""Solution to 10.10 Rank from Stream.

Imagine you are reading in a stream of integers. Periodically, you wish
to be able to look up the rank of a number `x` (the number of values
less than or equal to `x`). Implement the data structures and algorithms
to support these operations. That is, implement the method `track(int
x)`, which is called when each number is generated, and the method
`getRankOfNumber(int x)`, which returns the number of values less than
or equal to `x` (not including this instance of `x` itself).

EXAMPLE
Stream (in order of appearance): 5, 1, 4, 4, 5, 9, 7, 13, 3
getRankOfNumber(1) = 0 // values:
getRankOfNumber(3) = 1 // values: s[1] = 1
getRankOfNumber(4) = 3 // values: s[1] = 1, s[2] = 4, s[8] = 3
"""

from __future__ import annotations

import dataclasses
from typing import Optional, Set


@dataclasses.dataclass
class _Node:
    """A node in a binary search tree that knows size of left branch."""
    val: int
    left: Optional[_Node] = None
    left_size: int = 0
    right: Optional[_Node] = None


class StreamRanker:
    """Supports looking up rank of an integer among integers tracked."""

    def __init__(self) -> None:
        self._root: Optional[_Node] = None
        self._seen: Set[int] = set()

    def track(self, x: int) -> None:
        """Factors given x into future computed ranks."""
        if x in self._seen:
            return
        self._seen.add(x)
        if not self._root:
            self._root = _Node(val=x)
            return
        parent = self._root
        node: Optional[_Node] = self._root
        while node:
            if x > node.val:
                parent, node = node, node.right
            elif x < node.val:
                node.left_size += 1
                parent, node = node, node.left
        if x > parent.val:
            parent.right = _Node(val=x)
        else:
            parent.left = _Node(val=x)

    def get_rank_of_number(self, x: int) -> int:
        """Returns the rank of a previously tracked integer."""
        res, node = 0, self._root
        while node and node.val != x:
            if x > node.val:
                res += node.left_size + 1
                node = node.right
            elif x < node.val:
                node = node.left
        if not node:
            raise ValueError('cannot get rank for untracked integer')
        return res + node.left_size + 1
