"""Solution to 8.1 Triple Step.

A child is running up a staircase with `n` steps and can hop either 1
step, 2 steps, or 3 steps at a time. Implement a method to count how
many possible ways the child can run up the stairs.
"""


def possible_climbs(steps: int) -> int:
    """Returns how many ways to climb given number of steps."""
    if steps < 0:
        return 0
    if steps == 0:
        return 1
    if steps == 1:
        return 1
    if steps == 2:
        return 2
    down3, down2, down1 = 1, 1, 2
    for _ in range(3, steps):
        down3, down2, down1 = down2, down1, down3 + down2 + down1
    return down3 + down2 + down1
