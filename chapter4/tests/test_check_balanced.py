""" Tests for chapter4.list_of_depths."""

import unittest

from chapter4.check_balanced import is_balanced
from chapter4.tree_node import TreeNode


class TestCheckBalanced(unittest.TestCase):

    def test_balanced_1_2_3_4_5_6_7_8_9_10(self) -> None:
        tree = TreeNode(
            value=1,
            left=TreeNode(
                value=2,
                left=TreeNode(
                    value=4,
                    left=TreeNode(8, None, None),
                    right=TreeNode(9, None, None)
                ),
                right=TreeNode(
                    value=5,
                    left=TreeNode(10, None, None),
                    right=None
                )
            ),
            right=TreeNode(
                value=3,
                left=TreeNode(6, None, None),
                right=TreeNode(7, None, None)
            )
        )
        self.assertTrue(is_balanced(tree))

    def test_not_balanced_1_2_3_4_5_6_7_8_9_10(self) -> None:
        tree = TreeNode(
            value=1,
            left=TreeNode(
                value=2,
                left=TreeNode(
                    value=4,
                    left=TreeNode(
                        value=8,
                        left=TreeNode(10, None, None),
                        right=None
                    ),
                    right=TreeNode(9, None, None)
                ),
                right=TreeNode(5, None, None)
            ),
            right=TreeNode(
                value=3,
                left=TreeNode(6, None, None),
                right=TreeNode(7, None, None)
            )
        )
        self.assertFalse(is_balanced(tree))


if __name__ == '__main__':
    unittest.main()
