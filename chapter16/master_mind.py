"""Solution to 16.15 Master Mind.

The Game of Master Mind is played as follows:

The computer has four slots, and each slot will contain a ball that is
red (R), yellow (Y), green (G) or blue (B). For example, the computer
might have RGGB (Slot #1 is red, Slots #2 and #3 are green, Slot #4 is
blue).

You, the user, are trying to guess the solution. You might, for example,
guess YRGB.

When you guess the correct color for the correct slot, you get a "hit."
If you guess a color that exists but is in the wrong slot, you get a
"pseudo-hit." Note that a slot that is a hit can never count as a
pseudo-hit.

For example, if the actual solution is RGBY and you guess GGRR, you have
one hit and one pseudo-hit.

Write a method that, given a guess and a solution, returns the number of
hits and pseudo-hits.
"""

import collections
import dataclasses
import enum
from typing import Tuple


class Ball(enum.Enum):
    """A ball in the Game of Master Mind."""
    RED = 1
    YELLOW = 2
    GREEN = 3
    BLUE = 4


ComputerSlots = Tuple[Ball, Ball, Ball, Ball]


@dataclasses.dataclass
class GuessResult:
    """The feedback given to the user after a guess."""
    hits: int
    pseudo_hits: int


def feedback(guess: ComputerSlots, solution: ComputerSlots) -> GuessResult:
    """Computes the number of hits and pseudo-hits.

    Args:
        guess: The user's guess at the solution.
        solution: The actual solution.

    Returns:
        A GuessResult with the number of hits and pseudo-hits.
    """
    hits = sum(ball1 == ball2 for ball1, ball2 in zip(guess, solution))
    guess_counts = collections.Counter(guess)
    solution_counts = collections.Counter(solution)
    pseudo_hits = sum((guess_counts & solution_counts).values()) - hits
    return GuessResult(hits, pseudo_hits)
