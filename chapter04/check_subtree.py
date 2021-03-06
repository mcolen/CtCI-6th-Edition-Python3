"""Solution to 4.10 Check Subtree.

`T1` and `T2` are two very large binary trees, with `T1` much bigger
than `T2`. Create an algorithm to determine if `T2` is a subtree of
`T1`.

A tree `T2` is a subtree of `T1` if there exists a node `n` in `T1` such
that the subtree of `n` is identical to `T2`. That is, if you cut off
the tree at node `n`, the two trees would be identical.
"""

from typing import Any

from chapter04 import tree


def is_subtree(T1: tree.Tree[Any], T2: tree.Tree[Any]) -> bool:
    """Returns True if T2 is a subtree of T1."""
    if T1 is None or T2 is None:
        return T1 is None and T2 is None
    return any(subtree == T2 for subtree in T1)
