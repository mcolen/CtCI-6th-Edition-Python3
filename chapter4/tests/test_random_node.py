"""Tests for chapter4.random_node."""

import random
import unittest

from chapter4 import random_node


class TestRandomNode(unittest.TestCase):

    def test_1_0_6_2_3_9_4_5_8_7(self) -> None:
        tree = random_node.BinarySearchTree()
        tree.insert(1)
        tree.insert(0)
        tree.insert(6)
        tree.insert(2)
        tree.insert(3)
        tree.insert(9)
        tree.insert(4)
        tree.insert(5)
        tree.insert(8)
        tree.insert(7)

        counts = [0] * 10
        random.seed(0)
        for _ in range(100000):
            counts[tree.get_random_node().value] += 1
        self.assertEqual(
            [9994, 10104, 10128, 9953, 10128, 9929, 10086, 10027, 9857, 9794],
            counts)


if __name__ == '__main__':
    unittest.main()
