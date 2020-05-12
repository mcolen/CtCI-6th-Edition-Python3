"""Tests for chapter2.remove_dups."""

from typing import Callable
import unittest

from ..node import Node
from ..remove_dups import remove_dups1, remove_dups2


def make_test_case(impl: Callable[[Node], None]):
    """Returns a test case for provided impl to be tested."""
    class TestRemoveDups(unittest.TestCase):

        def test_01010101(self):
            head = Node(0)
            head.next = Node(1)
            head.next.next = Node(0)
            head.next.next.next = Node(1)
            head.next.next.next.next = Node(0)
            head.next.next.next.next.next = Node(1)
            head.next.next.next.next.next.next = Node(0)
            head.next.next.next.next.next.next.next = Node(1)

            deduped_head = Node(0)
            deduped_head.next = Node(1)

            impl(head)
            self.assertEqual(deduped_head, head)

    return TestRemoveDups


class TestRemoveDups1(make_test_case(remove_dups1)):  # type: ignore
    pass


class TestRemoveDups2(make_test_case(remove_dups2)):  # type: ignore
    pass


if __name__ == '__main__':
    unittest.main()
