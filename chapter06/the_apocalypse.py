"""Simulation of 6.7 The Apocalypse.

In the new post-apocalyptic world, the world queen is desperately
concerned about the birth rate. Therefore, she decrees that all families
should ensure that they have one girl or else they face massive fines.
If all families abide by this policy - that is, they have continue to
have children until they have one girl, at which point they immediately
stop - what will the gender ratio of the new generation be? (Assume that
the odds of someone having a boy or a girl on any given pregnancy is
equal). Solve this out logically and then write a computer simulation of
it.
"""

import enum
from typing import NamedTuple
import random


class Gender(enum.Enum):
    """Possible types of children a family can have."""
    BOY = 0
    GIRL = 1


def simulate_child() -> Gender:
    """Simulates a family having a child and returns the gender."""
    return random.choice([Gender.BOY, Gender.GIRL])


class Family(NamedTuple):
    """A simulated family with gendered children."""
    num_boys: int
    num_girls: int


def simulate_family() -> Family:
    """Simulates one family having children.

    Returns:
        The resulting Family.
    """
    num_boys = sum(1 for _ in iter(simulate_child, Gender.GIRL))
    return Family(num_boys=num_boys, num_girls=1)


def simulate_apocalypse(num_families: int) -> float:
    """Simulates apocalypse and returns gender ratio.

    Gender ratio is considered to be the ratio between the total number
    of boys and the total number of children.
    """
    total_boys = total_girls = 0
    for _ in range(num_families):
        family = simulate_family()
        total_boys += family.num_boys
        total_girls += family.num_girls
    return total_boys / (total_boys + total_girls)


if __name__ == '__main__':
    print(simulate_apocalypse(1_000_000))
