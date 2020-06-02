"""Tests for chapter8.triple_step."""

import unittest

from chapter8 import triple_step


class TestTripleStep(unittest.TestCase):

    def test_4_steps(self) -> None:
        self.assertEqual(7, triple_step.possible_climbs(steps=4))


if __name__ == '__main__':
    unittest.main()
