"""Solution to 8.9 Parens.

Implement an algorithm to print all valid (e.g., properly opened and
closed) combinations of n pairs of parentheses.

EXAMPLE
Input:  3
Output: ((())), (()()), (())(), ()(()), ()()()
"""

import dataclasses


@dataclasses.dataclass
class _Node:
    ending: str
    opened: int
    closed: int


def print_valid_combinations(n: int) -> None:
    """Prints all valid combinations of n pairs of parentheses."""
    nodes = [_Node(ending='', opened=0, closed=0)]
    for _ in range(2 * n):
        next_nodes = []
        for node in nodes:
            if node.closed < n:
                next_nodes.append(_Node(ending=')' + node.ending,
                                        opened=node.opened,
                                        closed=node.closed + 1))
            if node.opened < node.closed:
                next_nodes.append(_Node(ending='(' + node.ending,
                                        opened=node.opened + 1,
                                        closed=node.closed))
        nodes = next_nodes
    print(', '.join(node.ending for node in nodes))
