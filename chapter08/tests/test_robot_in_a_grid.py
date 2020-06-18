"""Tests for chapter08.robot_in_a_grid."""

import unittest

from chapter08 import robot_in_a_grid

DOWN = robot_in_a_grid.Direction.DOWN
RIGHT = robot_in_a_grid.Direction.RIGHT


class TestFindPath(unittest.TestCase):

    def test_exists_path(self) -> None:
        grid = [
            [True, True, True, True, False],
            [True, False, False, False, True],
            [True, True, True, True, True],
            [True, True, True, False, True],
        ]

        res = robot_in_a_grid.find_path(grid)

        self.assertEqual([DOWN, DOWN, RIGHT, RIGHT, RIGHT, RIGHT, DOWN], res)

    def test_no_path(self) -> None:
        grid = [
            [True, True, True, True, False],
            [True, False, False, False, True],
            [True, True, False, True, True],
            [True, True, True, False, True],
        ]

        res = robot_in_a_grid.find_path(grid)

        self.assertIsNone(res)


if __name__ == '__main__':
    unittest.main()
