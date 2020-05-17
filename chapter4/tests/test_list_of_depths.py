""" Tests for chapter4.list_of_depths."""

from typing import Set
import unittest

from chapter2.node import Node as ListNode
from chapter4.list_of_depths import depth_lists
from chapter4.tree_node import TreeNode


def _set_of_data(node: ListNode) -> Set[int]:
    ret = {node.data}
    if node.next:
        ret |= _set_of_data(node.next)
    return ret


class TestListOfDepths(unittest.TestCase):

    def test_1_2_3_4_5_6_7_8_9_10(self) -> None:
        root = TreeNode(
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
        lists = depth_lists(root)
        self.assertEqual(4, len(lists))
        self.assertEqual({1}, _set_of_data(lists[0]))
        self.assertEqual({2, 3}, _set_of_data(lists[1]))
        self.assertEqual({4, 5, 6, 7}, _set_of_data(lists[2]))
        self.assertEqual({8, 9, 10}, _set_of_data(lists[3]))


if __name__ == '__main__':
    unittest.main()
