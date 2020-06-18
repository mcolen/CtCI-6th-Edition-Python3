"""Tests for chapter16.master_mind."""

import unittest

from chapter16 import master_mind


class TestFeedback(unittest.TestCase):

    def test_guess_GGRR_solution_RGBY(self) -> None:
        self.assertEqual(
            master_mind.GuessResult(hits=1, pseudo_hits=1),
            master_mind.feedback(
                guess=(
                    master_mind.Ball.GREEN,
                    master_mind.Ball.GREEN,
                    master_mind.Ball.RED,
                    master_mind.Ball.RED
                ),
                solution=(
                    master_mind.Ball.RED,
                    master_mind.Ball.GREEN,
                    master_mind.Ball.BLUE,
                    master_mind.Ball.YELLOW
                )))


if __name__ == '__main__':
    unittest.main()
