"""Solution to 4.11 Random Node.

You are implementing a binary search tree class from scratch, which, in
addition to `insert`, `find`, and `delete`, has a method
`getRandomNode()` which returns a random node from the tree. All nodes
should be equally likely to be chosen. Design and implement an algorithm
for `getRandomNode`, and explain how you would implement the rest of the
methods.
"""

from __future__ import annotations

import dataclasses
import random
from typing import Any, Optional


class EmptyTreeError(Exception):
    """Raised when a node is requested from an empty tree."""


@dataclasses.dataclass
class Node:
    """A node in BinarySearchTree."""
    value: Any
    left: Optional[Node] = None
    right: Optional[Node] = None
    size = 1


class BinarySearchTree:
    """A binary search tree which supports `get_random_node()`."""

    def __init__(self) -> None:
        self._root: Optional[Node] = None

    def insert(self, value: Any) -> None:
        """Inserts value into the tree."""
        node = Node(value)
        if not self._root:
            self._root = node
            return
        curr: Optional[Node] = self._root
        while curr:
            curr.size += 1
            if value <= curr.value:
                prev, curr = curr, curr.left
            else:
                prev, curr = curr, curr.right
        if value < prev.value:
            prev.left = node
        else:
            prev.right = node

    def get_random_node(self) -> Node:
        """Returns a random node from the tree.

        Raises:
            EmptyTreeError: The tree was empty.
        """
        if not self._root:
            raise EmptyTreeError
        k = random.randrange(self._root.size)
        curr = self._root
        while k > 0:
            left_size = curr.left.size if curr.left else 0
            if k <= left_size:
                assert curr.left
                curr, k = curr.left, k - 1
            else:
                assert curr.right
                curr, k = curr.right, k - 1 - left_size
        return curr
