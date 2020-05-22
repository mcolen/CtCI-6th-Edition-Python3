"""Solution to 4.1 Route Between Nodes.

Given a directed graph and two nodes (`S` and `E`), design an algorithm
to find out whether there is a route from `S` to `E`.
"""

from __future__ import annotations

import collections
import dataclasses
from typing import MutableSet, MutableSequence


@dataclasses.dataclass
class Node:
    """A node in a graph with a name and list of neighbors."""
    name: str
    neighbors: MutableSequence[Node] = dataclasses.field(default_factory=list)


def exists_route(start: Node, end: Node) -> bool:
    """Return True if there is a route from start to end."""
    nodes = collections.deque([start])
    visited: MutableSet[str] = set()
    while nodes:
        node = nodes.popleft()
        if node is end:
            return True
        visited.add(node.name)
        nodes.extend(node for node in node.neighbors
                     if node.name not in visited)
    return False
