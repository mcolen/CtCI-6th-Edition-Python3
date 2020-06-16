"""Solution to 16.11 Diving Board.

You are building a diving board by placing a bunch of planks of wood
end-to-end. There are two types of planks, one of length `shorter` and
one of length `longer`. You must use exactly `K` planks of wood. Write a
method to generate all possible lengths for the diving board.
"""

from typing import Set


def possible_lengths(shorter: int, longer: int, k: int) -> Set[int]:
    """Generates all possible lengths for a diving board.

    Args:
        shorter: The length of the shorter type of plank.
        longer: The length of the longer type of plank.
        k: The number of planks that must be used in the diving board.

    Returns:
        The set of all possible total lengths of k planks.
    """
    return set(range(k * shorter, k * longer + 1, longer - shorter))
