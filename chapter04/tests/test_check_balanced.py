""" Tests for chapter04.list_of_depths."""

import unittest

from chapter04 import check_balanced, tree, validate_bst


class TestIsBalanced(unittest.TestCase):

    def test_bst_5_1_0_2_3_8_6_7_9_10(self) -> None:
        root = tree.Node(value=5,
                         left=tree.Node(
                             value=1,
                             left=tree.Node(0),
                             right=tree.Node(value=2,
                                             left=None,
                                             right=tree.Node(3)),
                         ),
                         right=tree.Node(value=8,
                                         left=tree.Node(value=6,
                                                        left=None,
                                                        right=tree.Node(7)),
                                         right=tree.Node(value=9,
                                                         left=None,
                                                         right=tree.Node(10))))
        assert validate_bst.is_bst(root)
        self.assertTrue(check_balanced.is_balanced(root))

    def test_bst_5_1_0_2_3_4_8_6_7_9_10(self) -> None:
        root = tree.Node(value=5,
                         left=tree.Node(
                             value=1,
                             left=tree.Node(0),
                             right=tree.Node(value=2,
                                             left=None,
                                             right=tree.Node(
                                                 value=3,
                                                 left=None,
                                                 right=tree.Node(4))),
                         ),
                         right=tree.Node(value=8,
                                         left=tree.Node(value=6,
                                                        left=None,
                                                        right=tree.Node(7)),
                                         right=tree.Node(value=9,
                                                         left=None,
                                                         right=tree.Node(10))))
        assert validate_bst.is_bst(root)
        self.assertFalse(check_balanced.is_balanced(root))


if __name__ == '__main__':
    unittest.main()
