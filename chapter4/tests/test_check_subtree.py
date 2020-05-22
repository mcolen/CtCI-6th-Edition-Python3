"""Tests for chapter4.check_subtree."""

import unittest

from chapter4.check_subtree import is_subtree
from chapter4.tree import TreeNode


class TestCheckSubtree(unittest.TestCase):

    def test_is_2_3_1_subtree_of_1_2_1_3_1_1_5(self) -> None:
        tree_2_3_1 = TreeNode(value=2, left=TreeNode(3), right=TreeNode(1))
        self.assertTrue(is_subtree(_tree_1_2_1_3_1_1_5(), tree_2_3_1))

    def test_is_1_2_3_subtree_of_1_2_1_3_1_1_5(self) -> None:
        tree_1_2_3 = TreeNode(value=1, left=TreeNode(2), right=TreeNode(3))
        self.assertFalse(is_subtree(_tree_1_2_1_3_1_1_5(), tree_1_2_3))


def _tree_1_2_1_3_1_1_5() -> TreeNode:
    # Construct and return tree.
    return TreeNode(value=1,
                    left=TreeNode(value=2, left=TreeNode(3),
                                  right=TreeNode(1)),
                    right=TreeNode(value=1,
                                   left=TreeNode(1),
                                   right=TreeNode(5)))


if __name__ == '__main__':
    unittest.main()
