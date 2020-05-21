"""Test for chapter4.route_between_nodes."""

import unittest

from chapter4.route_between_nodes import exists_route, Node


class TestRouteBetweenNodes(unittest.TestCase):

    def test_route_exists(self) -> None:
        node_a = Node('a')
        node_b = Node('b')
        node_c = Node('c')
        node_d = Node('d')
        node_e = Node('e')
        node_f = Node('f')

        node_a.neighbors.append(node_b)
        node_a.neighbors.append(node_c)
        node_a.neighbors.append(node_d)
        node_d.neighbors.append(node_e)
        node_e.neighbors.append(node_f)

        self.assertTrue(exists_route(node_d, node_f))


if __name__ == '__main__':
    unittest.main()
