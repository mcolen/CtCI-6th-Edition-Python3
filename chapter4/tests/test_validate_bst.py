"""Tests for chapter4.validate_bst."""

import unittest

from chapter4.tree import TreeNode
from chapter4.validate_bst import is_bst


class TestValidateBST(unittest.TestCase):

    def test_bst_min_3_5_6_10_13_15_max(self) -> None:
        tree = TreeNode(
            value=6,
            left=TreeNode(
                value=3,
                left=TreeNode(float('-inf'), None, None),
                right=TreeNode(5, None, None)
            ),
            right=TreeNode(
                value=13,
                left=TreeNode(10, None, None),
                right=TreeNode(
                    value=15,
                    left=None,
                    right=TreeNode(float('inf'), None, None)
                )
            )
        )
        self.assertTrue(is_bst(tree))

    def test_non_bst_min_6_5_6_10_13_15_max(self) -> None:
        tree = TreeNode(
            value=6,
            left=TreeNode(
                value=6,
                left=TreeNode(float('-inf'), None, None),
                right=TreeNode(5, None, None)
            ),
            right=TreeNode(
                value=13,
                left=TreeNode(10, None, None),
                right=TreeNode(
                    value=15,
                    left=None,
                    right=TreeNode(float('inf'), None, None)
                )
            )
        )
        self.assertFalse(is_bst(tree))


if __name__ == '__main__':
    unittest.main()
