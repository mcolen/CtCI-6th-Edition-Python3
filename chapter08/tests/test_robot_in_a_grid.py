"""Tests for chapter08.robot_in_a_grid."""

import unittest

from chapter08 import robot_in_a_grid

DOWN = robot_in_a_grid.Direction.DOWN
RIGHT = robot_in_a_grid.Direction.RIGHT


class TestRobotInAGrid(unittest.TestCase):

    def test_exists_path(self) -> None:
        grid = [
            [True, True, True, True, False],
            [True, False, False, False, True],
            [True, True, True, True, True],
            [True, True, True, False, True],
        ]
        self.assertEqual([DOWN, DOWN, RIGHT, RIGHT, RIGHT, RIGHT, DOWN],
                         robot_in_a_grid.find_path(grid))

    def test_no_path(self) -> None:
        grid = [
            [True, True, True, True, False],
            [True, False, False, False, True],
            [True, True, False, True, True],
            [True, True, True, False, True],
        ]
        self.assertIsNone(robot_in_a_grid.find_path(grid))


if __name__ == '__main__':
    unittest.main()
