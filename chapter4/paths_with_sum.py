"""Solution to 4.12 Paths with Sum.

You are given a binary tree in which each node contains an integer value
(which might be positive or negative). Design an algorithm to count the
number of paths that sum to a given value. The path does not need to
start or end at the root or a leaf, but it must go downwards (traveling
only from parent nodes to child nodes.
"""

import collections
from typing import DefaultDict

from chapter4 import tree


def paths_with_sum(root: tree.Tree[int], sum_: int) -> int:
    """Returns number of paths in given Tree that sum to given sum_.

    Paths must include at least 2 distinct nodes. Paths do not need to
    start or end at the roof or a leaf, but they most go downwards
    (traveling only from parent nodes to child nodes.)
    """
    running_sum_counts: DefaultDict[int, int] = collections.defaultdict(int)
    # A sum of 0 can be achieved by not including any nodes.
    running_sum_counts[0] = 1

    def helper(node: tree.Tree[int], running_sum: int) -> int:
        # Returns number of paths ending at/below node that add to sum_.
        if not node:
            return 0
        running_sum += node.value
        count = running_sum_counts[running_sum - sum_]
        # Compensate for lone-node "path" being counted above. A path
        # must have at least two nodes.
        if node.value == sum_:
            count -= 1
        running_sum_counts[running_sum] += 1
        count += helper(node.left, running_sum)
        count += helper(node.right, running_sum)
        running_sum_counts[running_sum] -= 1
        return count

    return helper(root, running_sum=0)
