"""Tests for chapter4.successor."""

from typing import Optional
import unittest

from chapter4.minimal_tree import minimal_bst
from chapter4.successor import successor
from chapter4.tree_node import TreeNode


def _find_or_die(root: TreeNode, value: int) -> TreeNode:
    # Return TreeNode with given value in tree given by root.  Assert
    # that such a node exists.
    def find(root: TreeNode, value: int) -> Optional[TreeNode]:
        # Return TreeNode with given value in tree given by root.  If
        # there is no such node, return None.
        if root.value == value:
            return root
        if root.left and root.value > value:
            return find(root.left, value)
        if root.right and root.value < value:
            return find(root.right, value)
        return None

    node = find(root, value)
    assert node
    return node


class TestSuccessor(unittest.TestCase):

    def setUp(self) -> None:
        # minimal_bst(range(7)) is fully specified and unique.
        self.bst_7 = minimal_bst(range(7))

    def test_0(self) -> None:
        node = _find_or_die(self.bst_7, 0)
        res = successor(node)
        self.assertIsNotNone(res)
        # https://github.com/python/mypy/issues/4063
        self.assertEqual(1, res.value)  # type: ignore[union-attr]

    def test_1(self) -> None:
        node = _find_or_die(self.bst_7, 1)
        res = successor(node)
        self.assertIsNotNone(res)
        # https://github.com/python/mypy/issues/4063
        self.assertEqual(2, res.value)  # type: ignore[union-attr]

    def test_2(self) -> None:
        node = _find_or_die(self.bst_7, 2)
        res = successor(node)
        self.assertIsNotNone(res)
        # https://github.com/python/mypy/issues/4063
        self.assertEqual(3, res.value)  # type: ignore[union-attr]

    def test_3(self) -> None:
        node = _find_or_die(self.bst_7, 3)
        res = successor(node)
        self.assertIsNotNone(res)
        # https://github.com/python/mypy/issues/4063
        self.assertEqual(4, res.value)  # type: ignore[union-attr]

    def test_4(self) -> None:
        node = _find_or_die(self.bst_7, 4)
        res = successor(node)
        self.assertIsNotNone(res)
        # https://github.com/python/mypy/issues/4063
        self.assertEqual(5, res.value)  # type: ignore[union-attr]

    def test_5(self) -> None:
        node = _find_or_die(self.bst_7, 5)
        res = successor(node)
        self.assertIsNotNone(res)
        # https://github.com/python/mypy/issues/4063
        self.assertEqual(6, res.value)  # type: ignore[union-attr]

    def test_6(self) -> None:
        node = _find_or_die(self.bst_7, 6)
        res = successor(node)
        self.assertIsNone(res)


if __name__ == '__main__':
    unittest.main()
