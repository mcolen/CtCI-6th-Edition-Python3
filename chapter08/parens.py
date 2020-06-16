"""Solution to 8.9 Parens.

Implement an algorithm to print all valid (e.g., properly opened and
closed) combinations of n pairs of parentheses.

EXAMPLE
Input:  3
Output: ((())), (()()), (())(), ()(()), ()()()
"""

import dataclasses
from typing import Set


@dataclasses.dataclass(frozen=True)
class _Node:
    ending: str
    opened: int
    closed: int


def valid_combinations(n: int) -> Set[str]:
    """Returns all valid combinations of n pairs of parentheses."""
    nodes = {_Node(ending='', opened=0, closed=0)}
    for _ in range(2 * n):
        next_nodes = set()
        for node in nodes:
            if node.closed < n:
                next_nodes.add(_Node(ending=')' + node.ending,
                                     opened=node.opened,
                                     closed=node.closed + 1))
            if node.opened < node.closed:
                next_nodes.add(_Node(ending='(' + node.ending,
                                     opened=node.opened + 1,
                                     closed=node.closed))
        nodes = next_nodes
    return set(node.ending for node in nodes)
