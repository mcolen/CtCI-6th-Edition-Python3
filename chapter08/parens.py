"""Solution to 8.9 Parens.

Implement an algorithm to print all valid (e.g., properly opened and
closed) combinations of n pairs of parentheses.

EXAMPLE
Input:  3
Output: ((())), (()()), (())(), ()(()), ()()()
"""

from typing import NamedTuple


class _Node(NamedTuple):
    ending: str
    opened: int
    closed: int


def print_valid_combinations(n: int) -> None:
    """Prints all valid combinations of n pairs of parentheses."""
    nodes = [_Node(ending='', opened=0, closed=0)]
    for _ in range(2 * n):
        next_nodes = []
        for ending, opened, closed in nodes:
            if closed < n:
                next_nodes.append(_Node(ending=')' + ending,
                                        opened=opened, closed=closed + 1))
            if opened < closed:
                next_nodes.append(_Node(ending='(' + ending,
                                        opened=opened + 1, closed=closed))
        nodes = next_nodes
    print(', '.join(node.ending for node in nodes))
