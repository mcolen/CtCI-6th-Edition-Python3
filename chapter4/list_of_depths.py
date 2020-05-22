"""Solution to 4.3 List of Depths.

Given a binary tree, design an algorithm which creates a linked list of
all the nodes at each depth (e.g., if you have a tree with depth `D`,
you'll have `D` linked lists).
"""

import collections
from typing import Dict

from chapter2 import llist
from chapter4 import tree


def depth_lists(root: tree.Tree) -> Dict[int, llist.Node]:
    """Return map from depth to linked list of values at that depth."""
    ret: Dict[int, llist.Node] = {}
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
