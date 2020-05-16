"""Test for chapter4.minimal_tree."""

import unittest

from chapter4.minimal_tree import minimal_bst, Node


def _is_bst(root: Node) -> bool:
    if not root:
        return True
    if root.left and root.left.value > root.value:
        return False
    if root.right and root.right.value < root.value:
        return False
    return _is_bst(root.left) and _is_bst(root.right)


def _height(root: Node) -> int:
    if not root:
        return 0
    return max(_height(root.left), _height(root.right)) + 1


class TestMinimalTree(unittest.TestCase):

    def test_1_2_3_4_5_6_7_8_9_10(self):
        root = minimal_bst([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        self.assertTrue(_is_bst(root))
        self.assertEqual(4, _height(root))


if __name__ == '__main__':
    unittest.main()
