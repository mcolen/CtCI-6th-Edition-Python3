"""Test for chapter4.minimal_tree."""

from typing import Any
import unittest

from chapter4.minimal_tree import minimal_bst
from chapter4.tree_node import Tree


def _is_bst(root: Tree, mini: Any = None, maxi: Any = None) -> bool:
    if not root:
        return True
    if mini is not None and root.value < mini:
        return False
    if maxi is not None and root.value > maxi:
        return False
    if not _is_bst(root.left, mini, root.value):
        return False
    if not _is_bst(root.right, root.value, maxi):
        return False
    return True


def _height(root: Tree) -> int:
    if not root:
        return 0
    return max(_height(root.left), _height(root.right)) + 1


class TestMinimalTree(unittest.TestCase):

    def test_1_2_3_4_5_6_7_8_9_10(self) -> None:
        tree = minimal_bst([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        self.assertTrue(_is_bst(tree))
        self.assertEqual(4, _height(tree))


if __name__ == '__main__':
    unittest.main()
