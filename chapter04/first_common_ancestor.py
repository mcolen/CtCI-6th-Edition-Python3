"""Solve 4.8 First Common Ancestor.

Design an algorithm and write code to find the first common ancestor of
two nodes in a binary tree. Avoid storing additional nodes in a data
structure. NOTE: This is not necessarily a binary search tree.
"""

import dataclasses
from typing import Generic, Optional, TypeVar

from chapter04 import tree

T = TypeVar('T')


def first_common_ancestor(root: tree.Node[T],
                          node1: tree.Node[T],
                          node2: tree.Node[T]) -> Optional[tree.Node[T]]:
    """Finds the first common ancestor of two nodes in a binary tree.

    Args:
        root: The root of the tree in which to look for ancestors.
        node1: The first node for which to find an ancestor.
        node2: The second node for which to find an ancestor.

    Returns:
        The first common ancestor in tree with given root of both
        argument node1 and argument node2, or None if at least one of
        node1 and node2 is not in the tree with given root.
    """
    return _search(root, node1, node2).first_common_ancestor


@dataclasses.dataclass
class _SearchResult(Generic[T]):
    has_node1: bool
    has_node2: bool
    first_common_ancestor: Optional[tree.Node[T]]


def _search(root: tree.Tree[T],
            node1: tree.Node[T],
            node2: tree.Node[T]) -> _SearchResult[T]:
    if not root:
        return _SearchResult(has_node1=False,
                             has_node2=False,
                             first_common_ancestor=None)
    if root is node1 and root is node2:
        return _SearchResult(has_node1=True,
                             has_node2=True,
                             first_common_ancestor=root)
    left_result = _search(root.left, node1, node2)
    if left_result.first_common_ancestor:
        return left_result
    has_node1 = left_result.has_node1 or root is node1
    has_node2 = left_result.has_node2 or root is node2
    if has_node1 and has_node2:
        return _SearchResult(has_node1=True,
                             has_node2=True,
                             first_common_ancestor=root)
    right_result = _search(root.right, node1, node2)
    if right_result.first_common_ancestor:
        return right_result
    has_node1 |= right_result.has_node1
    has_node2 |= right_result.has_node2
    return _SearchResult(
        has_node1,
        has_node2,
        first_common_ancestor=root if has_node1 and has_node2 else None)
