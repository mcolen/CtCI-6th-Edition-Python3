""" Tests for chapter4.list_of_depths."""

import unittest

from chapter4.check_balanced import is_balanced
from chapter4.tree import TreeNode
from chapter4.validate_bst import is_bst


class TestCheckBalanced(unittest.TestCase):

    def test_bst_5_1_0_2_3_8_6_7_9_10(self) -> None:
        tree = TreeNode(value=5,
                        left=TreeNode(
                            value=1,
                            left=TreeNode(0),
                            right=TreeNode(value=2,
                                           left=None,
                                           right=TreeNode(3)),
                        ),
                        right=TreeNode(value=8,
                                       left=TreeNode(value=6,
                                                     left=None,
                                                     right=TreeNode(7)),
                                       right=TreeNode(value=9,
                                                      left=None,
                                                      right=TreeNode(10))))
        assert is_bst(tree)
        self.assertTrue(is_balanced(tree))

    def test_bst_5_1_0_2_3_4_8_6_7_9_10(self) -> None:
        tree = TreeNode(value=5,
                        left=TreeNode(
                            value=1,
                            left=TreeNode(0),
                            right=TreeNode(value=2,
                                           left=None,
                                           right=TreeNode(value=3,
                                                          left=None,
                                                          right=TreeNode(4))),
                        ),
                        right=TreeNode(value=8,
                                       left=TreeNode(value=6,
                                                     left=None,
                                                     right=TreeNode(7)),
                                       right=TreeNode(value=9,
                                                      left=None,
                                                      right=TreeNode(10))))
        assert is_bst(tree)
        self.assertFalse(is_balanced(tree))


if __name__ == '__main__':
    unittest.main()
