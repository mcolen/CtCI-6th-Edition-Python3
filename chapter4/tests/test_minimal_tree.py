"""Test for chapter4.minimal_tree."""

import unittest

from chapter4.minimal_tree import minimal_bst
from chapter4.tree_node import Tree
from chapter4.validate_bst import is_bst


class TestMinimalTree(unittest.TestCase):

    def test_1_2_3_4_5_6_7_8_9_10(self) -> None:
        tree = minimal_bst([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        self.assertTrue(is_bst(tree))
        self.assertEqual(4, _height(tree))


def _height(root: Tree) -> int:
    # Return height of given tree.
    if not root:
        return 0
    return max(_height(root.left), _height(root.right)) + 1


if __name__ == '__main__':
    unittest.main()
