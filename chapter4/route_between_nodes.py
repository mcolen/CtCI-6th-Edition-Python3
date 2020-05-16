"""Solution to 4.1 Route Between Nodes.

Given a directed graph and two nodes (`S` and `E`), design an algorithm
to find out whether there is a route from `S` to `E`.
"""

import collections
from typing import MutableSet


Node = collections.namedtuple('Node', ['name', 'neighbors'])


def exists_route(start: Node, end: Node) -> bool:
    """Returns True if there is a route from start to end."""
    deque = collections.deque([start])
    visited: MutableSet[str] = set()
    while deque:
        node = deque.popleft()
        if node is end:
            return True
        visited.add(node.name)
        deque.extend(
            node for node in node.neighbors if node.name not in visited)
    return False
