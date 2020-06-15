"""Test for chapter04.minimal_tree."""

import unittest

from chapter04 import minimal_tree, tree, validate_bst


class TestMinimalBST(unittest.TestCase):

    def test_1_2_3_4_5_6_7_8_9_10(self) -> None:
        root = minimal_tree.minimal_bst([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        self.assertTrue(validate_bst.is_bst(root))
        self.assertEqual(4, _height(root))


def _height(root: tree.Tree) -> int:
    if not root:
        return 0
    return max(_height(root.left), _height(root.right)) + 1


if __name__ == '__main__':
    unittest.main()
