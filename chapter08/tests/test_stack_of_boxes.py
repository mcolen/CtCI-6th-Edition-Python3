"""Tests for chapter08.stack_of_boxes."""

import unittest

from chapter08 import stack_of_boxes


class TestMaxHeight(unittest.TestCase):

    def test_three_boxes_two_stackable(self) -> None:
        box1 = stack_of_boxes.Box(width=4, height=1, depth=1)
        box2 = stack_of_boxes.Box(width=7, height=4, depth=4)
        box3 = stack_of_boxes.Box(width=1, height=3, depth=1)

        res = stack_of_boxes.max_height({box1, box2, box3})

        self.assertEqual(7, res)


if __name__ == '__main__':
    unittest.main()
