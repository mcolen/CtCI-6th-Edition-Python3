"""Test for chapter04.route_between_nodes."""

import unittest

from chapter04 import route_between_nodes


class TestExistsRoute(unittest.TestCase):

    def test_route_exists(self) -> None:
        node_a = route_between_nodes.Node('a')
        node_b = route_between_nodes.Node('b')
        node_c = route_between_nodes.Node('c')
        node_d = route_between_nodes.Node('d')
        node_e = route_between_nodes.Node('e')
        node_f = route_between_nodes.Node('f')

        node_a.neighbors.append(node_b)
        node_a.neighbors.append(node_c)
        node_a.neighbors.append(node_d)
        node_d.neighbors.append(node_e)
        node_e.neighbors.append(node_f)

        self.assertTrue(route_between_nodes.exists_route(node_d, node_f))


if __name__ == '__main__':
    unittest.main()
