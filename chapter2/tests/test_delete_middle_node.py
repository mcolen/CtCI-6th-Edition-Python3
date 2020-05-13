"""Tests for 2.3 Delete Middle Node."""

import unittest

from chapter2.delete_middle_node import delete_middle_node
from chapter2.node import Node


class TestDeleteMiddleNode(unittest.TestCase):

    def test_delete_c_from_abcdef(self):
        head = Node('a')
        head.next = Node('b')
        head.next.next = Node('c')
        head.next.next.next = Node('d')
        head.next.next.next.next = Node('e')
        head.next.next.next.next.next = Node('f')

        head_deleted_c = Node('a')
        head_deleted_c.next = Node('b')
        head_deleted_c.next.next = Node('d')
        head_deleted_c.next.next.next = Node('e')
        head_deleted_c.next.next.next.next = Node('f')

        delete_middle_node(head.next.next)
        self.assertEqual(head_deleted_c, head)


if __name__ == '__main__':
    unittest.main()
