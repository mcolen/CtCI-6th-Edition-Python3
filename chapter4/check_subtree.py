"""Solution to 4.10 Check Subtree.

`T1` and `T2` are two very large binary trees, with `T1` much bigger
than `T2`. Create an algorithm to determine if `T2` is a subtree of
`T1`.

A tree `T2` is a subtree of `T1` if there exists a node `n` in `T1` such
that the subtree of `n` is identical to `T2`. That is, if you cut off
the tree at node `n`, the two trees would be identical.
"""

from chapter4.tree import Tree


def is_subtree(T1: Tree, T2: Tree) -> bool:
    """Return True if T2 is a subtree of T1."""
    if T1 is None or T2 is None:
        return T1 is None and T2 is None
    if T1 == T2:
        return True
    return is_subtree(T1.left, T2) or is_subtree(T1.right, T2)
