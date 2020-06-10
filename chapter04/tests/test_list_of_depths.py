""" Tests for chapter04.list_of_depths."""

import unittest

from chapter04 import list_of_depths, tree


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
        self.assertCountEqual([1], [node.data for node in lists[0]])
        self.assertCountEqual([2, 3], [node.data for node in lists[1]])
        self.assertCountEqual([4, 5, 6, 7], [node.data for node in lists[2]])
        self.assertCountEqual([8, 9, 10], [node.data for node in lists[3]])


if __name__ == '__main__':
    unittest.main()
