"""Solution to 5.2 Binary to String.

Given a real number between 0 and 1 (e.g. 0.72) that is passed in as a
double, print the binary representation. If the number cannot be
represented accurately in binary with at most 32 characters, print
"ERROR."
"""

from typing import List


def print_fraction_in_binary(x: float) -> None:
    """Prints the binary representation of a fraction.

    If the fraction cannot be represented accurately in binary with at
    most 32 characters, prints "ERROR."

    Args:
        x: A real number in the range [0, 1) (e.g. 0.72).
    """
    res: List[str] = []
    while x > 0:
        if len(res) >= 32:
            print("ERROR.")
            return
        x *= 2
        if x >= 1:
            res.append('1')
            x -= 1
        else:
            res.append('0')
    print('.' + ''.join(res))
