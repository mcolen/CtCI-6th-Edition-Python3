"""Solution to 10.7 Missing Int.

Given an input file with four billion non-negative integers, provide an
algorithm to generate an integer that is not contained in the file. Assume you
have 1 GB of memory available for this task.

FOLLOW UP
What if you have only 10 MB of memory? Assume that all the values are distinct
and we now have no more than one billion non-negative integers.
"""

from typing import Optional, TextIO

MAX_SIGNED_32_BIT_INT = 2 ** 31 - 1


def missing(file: TextIO,
            lo: int = 0,
            hi: int = MAX_SIGNED_32_BIT_INT) -> Optional[int]:
    """Generates an integer not contained in given file.

    Uses one bit of memory for every integer in range [lo, hi], which
    comes out to 268 MB for default arguments.

    Args:
        file: A file with one integer per line. May or may not contain
            duplicates.
        lo: Minimum value of any integer in the file or any integer that
            may be generated.
        hi: Maximum value of any integer in the file or any integer that
            may be generated.

    Returns:
        An integer in range[lo, hi] not contained in the file, or None
        if no such integer exists.
    """
    bit_vector = bytearray(0 for _ in range((hi - lo) // 8 + 1))
    for line in file:
        index = int(line) - lo
        bit_vector[index // 8] |= 1 << index % 8
    for i, byte in enumerate(bit_vector):
        if byte != 0xFF:
            return lo + 8 * i + next(bit for bit in range(8)
                                     if 1 << bit & byte == 0)
    return None


def missing_unique_nonnegative_signed_32_bit(file: TextIO) -> Optional[int]:
    """Generates an integer not contained in given file.

    Uses less than 10 MB of memory, not including the memory needed to
    read the file.

    By "non-negative, signed 32-bit", we mean integers in the range:
    [0, 2 ** 31 -1].

    Args:
        file: A file with one unique, non-negative, signed 32-bit
            integer per line.

    Returns:
        A non-negative, signed 32-bit integer not contained in the file,
        or None if no such integer exists.
    """
    range_size = 1 << 20
    blocks = [0] * ((MAX_SIGNED_32_BIT_INT + 1) // range_size + 1)
    for line in file:
        blocks[int(line) // range_size] += 1
    try:
        block = next(i for i in range(len(blocks))
                     if blocks[i] != range_size)
    except StopIteration:
        return None
    bit_vector = bytearray(0 for _ in range(range_size // 8 + 1))
    file.seek(0)
    for line in file:
        if range_size * block <= int(line) <= range_size * (block + 1):
            index = int(line) % range_size
            bit_vector[index // 8] |= 1 << index % 8
    i = next(i for i, byte in enumerate(bit_vector) if byte != 0xFF)
    return range_size * block + 8 * i + next(bit for bit in range(8)
                                             if 1 << bit & bit_vector[i] == 0)
