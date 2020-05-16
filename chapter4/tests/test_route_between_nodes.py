"""Test for chapter4.route_between_nodes."""

import unittest

from chapter4.route_between_nodes import exists_route, Node


class TestRouteBetweenNodes(unittest.TestCase):

    def test_route_exists(self):
        node_a = Node(name='a', neighbors=[])
        node_b = Node(name='b', neighbors=[])
        node_c = Node(name='c', neighbors=[])
        node_d = Node(name='d', neighbors=[])
        node_e = Node(name='e', neighbors=[])
        node_f = Node(name='f', neighbors=[])

        node_a.neighbors.append(node_b)
        node_a.neighbors.append(node_c)
        node_a.neighbors.append(node_d)
        node_d.neighbors.append(node_e)
        node_e.neighbors.append(node_f)

        self.assertTrue(exists_route(node_d, node_f))


if __name__ == '__main__':
    unittest.main()
