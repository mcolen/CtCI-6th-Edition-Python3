"""Solution to 4.3 List of Depths.

Given a binary tree, design an algorithm which creates a linked list of
all the nodes at each depth (e.g., if you have a tree with depth `D`,
you'll have `D` linked lists).
"""

import collections
from typing import Dict, TypeVar

from chapter2 import llist
from chapter4 import tree

T = TypeVar('T')


def depth_lists(root: tree.Tree[T]) -> Dict[int, llist.Node[T]]:
    """Creates a linked list of all the nodes at each depth.

    Args:
        root: The root of a binary tree (or None).

    Returns:
        Mapping from each depth in the given tree to a linked list of
            all the node values found at that depth.
    """
    ret: Dict[int, llist.Node[T]] = {}
    if not root:
        return ret
    nodes_and_depths = collections.deque([(root, 0)])
    while nodes_and_depths:
        tree_node, depth = nodes_and_depths.popleft()
        list_node = llist.Node(data=tree_node.value,
                               next_=ret.get(depth, None))
        ret[depth] = list_node
        if tree_node.left:
            nodes_and_depths.append((tree_node.left, depth + 1))
        if tree_node.right:
            nodes_and_depths.append((tree_node.right, depth + 1))
    return ret
