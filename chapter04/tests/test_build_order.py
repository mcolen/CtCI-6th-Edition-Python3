"""Tests for chapter04.build_order."""

from typing import Sequence, Tuple
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

        self.assertCountEqual(projects, order)
        self.assertBuildable(order, dependencies)

    def assertBuildable(self, order: Sequence[str],
                        dependencies: Sequence[Tuple[str, str]]) -> None:
        """Fails if order cannot be built subject to dependencies."""
        for dependency, dependant in dependencies:
            if order.index(dependency) > order.index(dependant):
                self.fail(dependency + ' must be built before ' + dependant)


if __name__ == '__main__':
    unittest.main()
