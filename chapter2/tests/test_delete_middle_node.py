"""Tests for chapter2.delete_middle_node."""

import unittest

from chapter2 import delete_middle_node, llist


class TestDeleteMiddleNode(unittest.TestCase):

    def test_delete_c_from_abcdef(self) -> None:
        head = llist.Node('a')
        head.next = llist.Node('b')
        head.next.next = llist.Node('c')
        head.next.next.next = llist.Node('d')
        head.next.next.next.next = llist.Node('e')
        head.next.next.next.next.next = llist.Node('f')

        head_deleted_c = llist.Node('a')
        head_deleted_c.next = llist.Node('b')
        head_deleted_c.next.next = llist.Node('d')
        head_deleted_c.next.next.next = llist.Node('e')
        head_deleted_c.next.next.next.next = llist.Node('f')

        delete_middle_node.delete_middle_node(head.next.next)
        self.assertEqual(head_deleted_c, head)


if __name__ == '__main__':
    unittest.main()
