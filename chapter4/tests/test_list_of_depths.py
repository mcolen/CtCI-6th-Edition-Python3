""" Tests for chapter4.list_of_depths."""

from typing import Set
import unittest

from chapter2 import llist
from chapter4 import list_of_depths, tree


class TestListOfDepths(unittest.TestCase):

    def test_1_2_3_4_5_6_7_8_9_10(self) -> None:
        root = tree.Node(value=1,
                         left=tree.Node(value=2,
                                        left=tree.Node(value=4,
                                                       left=tree.Node(8),
                                                       right=tree.Node(9)),
                                        right=tree.Node(value=5,
                                                        left=tree.Node(10),
                                                        right=None)),
                         right=tree.Node(value=3,
                                         left=tree.Node(6),
                                         right=tree.Node(7)))
        lists = list_of_depths.depth_lists(root)
        self.assertEqual(4, len(lists))
        self.assertEqual({1}, _set_of_data(lists[0]))
        self.assertEqual({2, 3}, _set_of_data(lists[1]))
        self.assertEqual({4, 5, 6, 7}, _set_of_data(lists[2]))
        self.assertEqual({8, 9, 10}, _set_of_data(lists[3]))


def _set_of_data(node: llist.Node) -> Set[int]:
    """Returns the Set of all data in given linked list."""
    ret = {node.data}
    if node.next:
        ret |= _set_of_data(node.next)
    return ret


if __name__ == '__main__':
    unittest.main()
