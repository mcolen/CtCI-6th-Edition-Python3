"""Tests for chapter8.stack_of_boxes."""

import unittest

from chapter8 import stack_of_boxes


class TestStackOfBoxes(unittest.TestCase):

    def test_three_boxes_two_stackable(self) -> None:
        box1 = stack_of_boxes.Box(width=4, height=1, depth=1)
        box2 = stack_of_boxes.Box(width=7, height=4, depth=4)
        box3 = stack_of_boxes.Box(width=1, height=3, depth=1)
        self.assertEqual(7, stack_of_boxes.max_height({box1, box2, box3}))


if __name__ == '__main__':
    unittest.main()
