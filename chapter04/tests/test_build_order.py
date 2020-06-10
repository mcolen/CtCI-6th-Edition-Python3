"""Tests for chapter04.build_order."""

import unittest

from chapter04 import build_order


class TestBuildOrder(unittest.TestCase):

    def test_10_projects(self) -> None:
        projects = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
        dependencies = [
            ('a', 'b'),
            ('b', 'c'),
            ('a', 'c'),
            ('a', 'c'),
            ('d', 'e'),
            ('b', 'd'),
            ('e', 'f'),
            ('a', 'f'),
            ('h', 'i'),
            ('h', 'j'),
            ('i', 'j'),
            ('g', 'j'),
        ]
        order = build_order.build_order(projects, dependencies)
        self.assertEqual(len(projects), len(order))
        self.assertEqual(set(projects), set(order))
        for dependency, dependant in dependencies:
            self.assertLess(order.index(dependency), order.index(dependant))


if __name__ == '__main__':
    unittest.main()
